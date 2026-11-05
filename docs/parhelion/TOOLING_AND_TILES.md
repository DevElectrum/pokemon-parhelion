# Tooling investigation and original environment tile workflow

**Investigated:** 2026-11-05. **Decision:** no adoption or installation; development paused by user. This note is for future resumption, not authorization to proceed.

## Porymap MCP: `hugomrts/porymap-mcp`

Source: https://github.com/hugomrts/porymap-mcp

- Python FastMCP project; `pyproject.toml` showed **version 1.0.1**. Claims focus on `pokeemerald-expansion`, the same decomp family used by Parhelion.
- Exposes **24 tools** across discovery, map creation/painting, map registration, events and rendering. Examples include `create_map`, `paint_metatile`, `paint_rectangle`, `flood_fill`, `paint_prefab`, `add_warp`, `add_object_event`, `add_sign`, `add_trigger`, `render_map` and `render_map_region`.
- Its source uses atomic individual file writes; a multi-file `create_map` sequence is **not** one all-or-nothing transaction.
- Render pipeline consumes real tileset assets. Project author reports pixel-identical output against several Porymap exports; this has **not** been independently verified on Parhelion.
- **Does not provide** dedicated adjacent-map connection editing, original image/tile asset creation, or full story script authoring.
- **Not live-connected to an open Porymap UI.** Its design explicitly abandons simultaneous Porymap editing. Close/reopen or reload as appropriate; don't let two processes overwrite files.
- Its project parser expects a local `porymap.project.cfg`; the Parhelion GitHub repository did not contain that file when checked. Opening the checkout with Porymap can establish local project configuration.
- Its tileset discovery derives C labels by directory naming convention and does not fully verify them against the engine headers; custom tilesets need care.
- This chat has a GitHub connector but **no direct remote invocation of a local MCP process or Nyx's filesystem**. Merely installing Porymap MCP on Nyx or connecting it to a different agent does not make tools available to Astra here.

**Verdict:** potentially useful for map-file manipulation and accurate previews in a properly connected local agent, but **not** a replacement for Porymap and not central to original-art creation. A single small sandbox-branch trial is enough before any adoption. Avoid investing in an elaborate testing framework.

## Original map tiles: intended approach

**User priority:** Parhelion needs **original environmental graphics**, not stock Emerald art with rearranged layouts.

**Suggested production path (not yet approved as a complete implementation plan):**

1. Establish a coherent mood/palette and functional modular requirements for **Starter Environment Pack 01**: rescue woods, secluded homestead, winding town path, first town and a small interior.
2. Create original modular source sprites/tiles for ground, soil/paths, tall grass, tree edges, foliage, fences, exterior architecture and interior basics. AI-generated concepts can inform the look but may require manual pixel cleanup; do not assume image generation automatically yields engine-ready tiles.
3. Prepare palette-conscious, grid-aligned tile sheets and assemble metatiles with proper seams, layers, animations (if any), collisions and behaviors. **Porytiles** is a tool candidate for source art conversion; verify its actual accepted formats against the pinned expansion engine.
4. Open and refine the map layouts using graphical **Porymap**. Porymap MCP is optional acceleration only if callable from the chosen environment.
5. Inspect the actual imported tiles in a ROM at **one meaningful milestone**, rather than testing every decorative edit.

**Open:** precise regional palette, architecture, art dimensions and set composition. No original pack has been generated or imported yet.

## Separation of responsibilities

- **Art generator / drawing:** creates original source images and visual concepts; not an engine file importer by itself.
- **Porytiles or equivalent conversion tooling:** converts validated art into tileset/metatile assets.
- **Porymap:** edits map layouts, objects, warps and connections with visual feedback.
- **MCP:** optional programmatic manipulator of existing map data, provided a compatible local connector is actually available.
- **mGBA/build:** verifies the resulting ROM when a significant content batch is ready.

Until explicitly unpaused: **no tool setup, no repository implementation changes, no new asset generation and no CI runs.**
