# Parhelion — current handoff

**Updated:** 2026-11-05

## State

The user established an independent GitHub repository, `DevElectrum/pokemon-parhelion`, by importing RHH's `pokeemerald-expansion` with Git history intact. Its initial `master` matched upstream commit `3ecef35381e321157c97c3aa0d064438026c7d68`. The present foundation pass adds this project's docs and a focused Emerald-target build workflow. **No Parhelion game maps or scripts exist yet.**

## Decisions to honor

- Name: **Pokémon Parhelion**.
- Start: Gen 8-aligned martial region. Other Gen 9 academic region becomes significant at official Rank III.
- Two hostile regions, central Ultra Wormhole No Man's Land, temporary truce, resource rivalry under the Terastal Revolution.
- Four pre-game wounded starter options: Type: Null, Jangmo-o, Dreepy, Frigibax. Terapagos appears only later.
- Gen 8 criminal transport to secret Gen 9 lab; thunderstorm escape; weeks of nursing; couriers appear at player's house; protagonist's first fight is an **ordinary battle**.
- Main cast drawn individually; recurring support hybrid; generic NPCs generated. BW-inspired art target.
- Full story **not** written before implementation. No scope creep into advanced noble-duel systems yet.

## After the foundation pass

1. Check GitHub Actions status for the foundation commit and document whether the Emerald base compiled. Do not infer a boot from a build.
2. If CI fails, fix only the actual failure and re-run.
3. Verify local mGBA boot when an ARM toolchain/emulator is available. No claims of completed emulator testing until then.
4. Start P1: three connected placeholder maps (home, town, outskirts), safe warps/collisions and a simple NPC.
5. Start P2/P3: starter selection and opening events; test with all four choices and saves.

## Open decisions, not blockers for coding setup

Town/region names and actual map shapes; player art details; ordinary first-battle loss rule; first grunt roster; faction leadership; lab's goals; the protagonist's family situation; precise relationship between Terastal power, Ultra Beasts and Terapagos.

## Working rules

Read `AGENTS.md`, `CANON.md`, `PROLOGUE.md` and `ROADMAP.md`. Respect existing Grand Anthology/Mosaic/XGBA boundaries. Avoid megabatch planning, premature claims and test-loop perfectionism. Keep substantive milestones and concise verifiable reports.

## Opening terrain authored

Map-source batch added five Porymap-style maps and layouts: `ParhelionRescueWoods`, `ParhelionHomestead`, `ParhelionTownPath`, `ParhelionFirstTown`, `ParhelionHomeInterior`. Four exterior grids are original authored arrangements of temporary Emerald tiles, with map connections; house interior duplicates House1 tiles as a separate editable layout. See `docs/parhelion/maps/OVERVIEW.md` for dimensions and text previews. Homestead's storm-fallen-tree gate is hidden when `FLAG_PARHELION_TOWN_PATH_OPEN` gets set **by future story scripts**.

**Not yet proven:** compiled ROM, emulator movement, NPC art, new game start location, rescue scene and first battle. Base game still starts at original intro. Next: compile once and verify essential connections; then implement prologue scripts. No loop of speculative tests.

### Map preview workflow

Parhelion now has `scripts/render_parhelion_maps.py` plus `.github/workflows/map-previews.yml` to render PNGs directly from committed source metatiles. The user has a separate source-grid schematic image too. Actual tile PNG outputs and emulator captures remain **unverified until the workflow runs**. See maps/OVERVIEW.md for usage. Do not confuse the original upstream CI (successful on base commit) with a build of these new maps.

### 2026-11-05 first visual refinement

The map preview workflow **successfully rendered** source tiles and palettes. Visual review caught an inappropriate metatile: all route footprints appeared as dense flower trails. Corrected the four exterior blockmaps to clear turf plus small flower accents, without changing exits/gates. Review the next preview artifact before any 'final art' claim. Source art renders are not emulator screenshots.


## Source visual gate verified on 2026-11-05

- **Refined four-exterior-map source-art render succeeded:** GitHub Actions run [42112246709](https://github.com/DevElectrum/pokemon-parhelion/actions/runs/42112246709), commit `7ac7788`.
- Its `parhelion-map-previews` artifact contains five individual PNGs and a contact sheet, reconstructed from actual `map.bin`, tilesets, metatiles and JASC palettes.
- Human visual inspection confirmed the initial flower-railroad defect was corrected: paths now use normal grass and sparse flowers. The homestead, rescue clearing, connecting trail, small town and house interior all appear in the preview.
- **Not an emulator capture:** object sprites, movement, new-game spawn, door entry, collision behavior, save/continue and the first battle have not been explored in-game. The current base-game intro still launches first.
- Existing Emerald build run [42111570036](https://github.com/DevElectrum/pokemon-parhelion/actions/runs/42111570036) passed on a map-preview renderer commit; newer source compilation runs may still be in progress. Do not infer acceptance for the latest head until its specific build is green.

**Next substantial gameplay batch:** wire the Parhelion starting position, then implement the opening rescue/recovery and one criminal confrontation with the four selected starters. Do not spend more work polishing temporary Emerald foliage or performing redundant CI reruns.

## STOP HERE — explicit user pause (2026-11-05)

**User requested: "Just write to tree and stop. We'll continue when my brain doesn't feel like mush."** This pause supersedes earlier "next batch" suggestions in this file. No gameplay scripting, map editing, graphics generation, Porymap/Porytiles/MCP installation, CI triggering, or unsolicited follow-up work. Resume only on an explicit user request.

### New creative direction

The user wants **custom original maps and tiles**, rather than a game visually dependent on Emerald assets. Five opening maps already exist as layout files; these use Emerald tiles and are **temporary scaffold**. Plan for a compact **Starter Environment Pack 01** (homestead / rescue woods / woodland trail / first town / home interior) with original environment art. Source images alone are not equivalent to ready-to-use GBA tilesets: palette, alignment, seamless metatiles, collision/behavior and actual in-engine import still need to be handled. Stylistic choices have not been locked. See `docs/parhelion/ART_PIPELINE.md`.

### Tool decision not yet made

Investigated `hugomrts/porymap-mcp` (project describes v1.0.1 with 24 map/render/event tools). It edits Porymap-format project files directly and can render tile-based map PNGs; it **cannot** do live Porymap editing, does **not** offer dedicated connection editing or original tileset production, and this ChatGPT session **has no direct tool connection** to a local MCP process on Nyx. It is a possible future convenience, **not installed or adopted**. Porymap itself and Porytiles remain potential tooling. See `docs/parhelion/TOOLING_AND_TILES.md`.

### Engineering reality at pause

- Opening map structure: `ParhelionRescueWoods`, `ParhelionHomestead`, `ParhelionTownPath`, `ParhelionFirstTown`, `ParhelionHomeInterior`.
- The source-art renderer previously produced valid visual previews, **not** emulator screenshots. Some map CI had passed on earlier commits; do not assume the latest head/gameplay was played.
- **No original Parhelion environment tileset**, new-game spawn integration, playable rescue, recovery, or first criminal battle has been completed.
- Key approach once user returns: choose a practical original-art workflow, use it to replace the opening area's placeholder visuals in a focused batch, then progress the playable prologue. **No marathon test loops.**
