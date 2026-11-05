#!/usr/bin/env python3
"""Render Parhelion's actual metatile map source to PNG. Not an emulator screenshot."""
import argparse
import json
import struct
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw

MAPS = (
    "ParhelionRescueWoods",
    "ParhelionHomestead",
    "ParhelionTownPath",
    "ParhelionFirstTown",
    "ParhelionHomeInterior",
)
PRIMARY_TILES = 512
PRIMARY_METATILES = 512
PRIMARY_PALETTES = 6


def jasc(path):
    lines = path.read_text(encoding="ascii").splitlines()
    if lines[0:2] != ["JASC-PAL", "0100"]:
        raise ValueError("Expected a JASC-PAL file: " + str(path))
    count = int(lines[2])
    colors = [tuple(map(int, line.split())) for line in lines[3:3+count]]
    if len(colors) != 16 or any(len(c) != 3 for c in colors):
        raise ValueError("Invalid 16-color palette: " + str(path))
    return colors


class Renderer:
    def __init__(self, root, primary, secondary):
        bases = [
            root / "data/tilesets/primary" / primary,
            root / "data/tilesets/secondary" / secondary,
        ]
        self.images = [Image.open(p / "tiles.png").convert("P") for p in bases]
        self.metatiles = [(p / "metatiles.bin").read_bytes() for p in bases]
        palettes = [[jasc(p / "palettes" / f"{i:02d}.pal") for i in range(16)] for p in bases]
        self.palettes = palettes[0][:PRIMARY_PALETTES] + palettes[1][PRIMARY_PALETTES:]

    @lru_cache(maxsize=8192)
    def tile(self, encoded):
        n = encoded & 0x3FF
        flip_h, flip_v = bool(encoded & 0x400), bool(encoded & 0x800)
        palette = self.palettes[(encoded >> 12) & 15]
        bank = 0 if n < PRIMARY_TILES else 1
        if bank:
            n -= PRIMARY_TILES
        sheet = self.images[bank]
        cols = sheet.width // 8
        if n >= cols * (sheet.height // 8):
            raise ValueError(f"Invalid tile {n} in bank {bank}")
        x, y = (n % cols) * 8, (n // cols) * 8
        raw = sheet.crop((x, y, x+8, y+8))
        if flip_h:
            raw = raw.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        if flip_v:
            raw = raw.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        out = Image.new("RGBA", (8, 8))
        for py in range(8):
            for px in range(8):
                value = raw.getpixel((px, py))
                out.putpixel((px, py), (*palette[value], 0 if value == 0 else 255))
        return out

    @lru_cache(maxsize=1000)
    def metatile(self, index):
        bank = 0 if index < PRIMARY_METATILES else 1
        local = index if bank == 0 else index - PRIMARY_METATILES
        data = self.metatiles[bank]
        offset = local * 16
        if offset + 16 > len(data):
            raise ValueError(f"Unknown metatile {index}")
        parts = struct.unpack_from("<8H", data, offset)
        result = Image.new("RGBA", (16, 16), (0, 0, 0, 255))
        for layer in range(2):
            for quadrant in range(4):
                result.alpha_composite(self.tile(parts[4*layer+quadrant]),
                    ((quadrant % 2)*8, (quadrant // 2)*8))
        return result


def tileset_folder(name):
    # gTileset_GenericBuilding => generic_building; gTileset_General => general
    tail = name.removeprefix("gTileset_")
    return "".join(("_" + c.lower()) if c.isupper() else c for c in tail).lstrip("_")


def draw_markers(img, map_name, cfg):
    draw = ImageDraw.Draw(img)
    for obj in cfg.get("object_events", []):
        if obj.get("graphics_id") == "OBJ_EVENT_GFX_CUTTABLE_TREE":
            x, y = obj["x"], obj["y"]
            draw.rectangle((16*x+1, 16*y+1, 16*x+14, 16*y+14),
                           outline="#FFD479", width=2)
    anchors = {"ParhelionRescueWoods": (20, 8), "ParhelionHomestead": (11, 14)}
    if map_name in anchors:
        x, y = anchors[map_name]
        draw.ellipse((x*16+4, y*16+4, x*16+12, y*16+12),
                     fill="#FFD479" if map_name == "ParhelionRescueWoods" else "#FF9B98")


def render(root, name, output, markers):
    doc = json.loads((root/"data/layouts/layouts.json").read_text())
    lay = next(x for x in doc["layouts"] if x["name"] == name + "_Layout")
    cfg = json.loads((root/f"data/maps/{name}/map.json").read_text())
    primary = tileset_folder(lay["primary_tileset"])
    secondary = tileset_folder(lay["secondary_tileset"])
    tiles = Renderer(root, primary, secondary)
    width, height = lay["width"], lay["height"]
    raw = (root / lay["blockdata_filepath"]).read_bytes()
    if len(raw) != width*height*2:
        raise ValueError(f"{name} map binary size mismatch")
    image = Image.new("RGBA", (width*16, height*16), "#203C31")
    for i, (packed,) in enumerate(struct.iter_unpack("<H", raw)):
        image.alpha_composite(tiles.metatile(packed & 0x3FF),
                              ((i % width)*16, (i // width)*16))
    if markers:
        draw_markers(image, name, cfg)
    output.parent.mkdir(parents=True, exist_ok=True)
    rgb = image.convert("RGB")
    rgb.save(output)
    print(f"{name}: {width}x{height} metatiles, {rgb.width}x{rgb.height} pixels")
    return rgb


def make_contact(images, path):
    cell_w, cell_h, gap = 486, 449, 20
    canvas = Image.new("RGB", (cell_w*2 + gap*3, cell_h*3 + gap*4), "#F5F2EC")
    draw = ImageDraw.Draw(canvas)
    for idx, (name, img) in enumerate(images):
        x = gap + (idx%2)*(cell_w+gap)
        y = gap + (idx//2)*(cell_h+gap)
        draw.rounded_rectangle((x, y, x+cell_w, y+cell_h),
                               radius=10, fill="#FFFFFF", outline="#D2D6CE", width=2)
        draw.text((x+12,y+12), name, fill="#234337")
        img.thumbnail((cell_w-20,cell_h-48),Image.Resampling.NEAREST)
        canvas.paste(img,(x+(cell_w-img.width)//2,y+40))
    canvas.save(path)


def make_metatile_atlas(root, output):
    tiles = Renderer(root, "general", "petalburg")
    for tag, start, end in (("primary", 0x000, 0x100), ("petalburg", 0x200, 0x290)):
        cols, cw, ch = 12, 70, 63
        count = end - start
        rows = (count + cols - 1) // cols
        board = Image.new("RGB", (cols*cw, rows*ch), "#F1F0E9")
        draw = ImageDraw.Draw(board)
        for i in range(count):
            idx = start + i
            x, y = (i % cols)*cw, (i // cols)*ch
            tile = tiles.metatile(idx).resize((40, 40), Image.Resampling.NEAREST)
            board.paste(tile.convert("RGB"), (x+15, y+2))
            draw.text((x+19,y+44), f"{idx:03X}", fill="#25312B")
        board.save(output / f"metatile_atlas_{tag}.png")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out", type=Path, default=Path("parhelion-map-previews"))
    parser.add_argument("--no-markers", action="store_true")
    parser.add_argument("--atlas", action="store_true", help="Produce metatile index atlases")
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    images = [(name,render(args.root,name,out/f"{name}.png",not args.no_markers)) for name in MAPS]
    make_contact(images,out/"all_parhelion_maps.png")
    if args.atlas:
        make_metatile_atlas(args.root, out)
    print("Contact sheet:",out/"all_parhelion_maps.png")


if __name__ == "__main__":
    main()
