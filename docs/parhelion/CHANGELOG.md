# Parhelion development changelog

## 2026-11-05 — pause handoff and original tileset direction

- Documented user's explicit pause; no further game implementation authorized until resumed.
- Recorded decision to develop **original Parhelion environment/map tilesets** rather than rely on stock Pokémon graphics.
- Outlined a small reusable starter environment pack and distinguished source art from GBA-integrated metatiles.
- Archived a code-based investigation of `porymap-mcp`, including compatibility opportunities and the current ChatGPT/Nyx connection limitation.
- Updated `AGENTS.md`, art policy, roadmap and handoff. **Documentation only**; no installs, new map art, game-code edits or CI work.


## 2026-11-05 — visual pass: natural footpaths

- Source tileset PNG renderer succeeded in GitHub Actions; first actual-art previews revealed every marked footpath was a chain of flowers (general metatile `0x004`).
- Replaced the continuous flower trails/plaza with walkable grass (`0x001`) plus sparse flower clusters and a compact town flowerbed.
- Kept woodland clearings, gate locations, warps and map connectivity unchanged; these are still *temporary Emerald tiles* rather than original Parhelion artwork.
- Removed automatic metatile-atlas rendering from routine map previews. The optional `--atlas` flag remains available for future artist selection. No emulator exploration claimed.


## 2026-11-05 — first terrain source batch

- Added four original 28×24 outdoor terrain layouts, five map definitions, house-interior copy, map connections and warps.
- Added homestead gate: two storm-fallen trees blocked until the future first-battle completion flag is set.
- Added in-repo ASCII layout previews and handoff notes.
- Source authored, but **not yet compiled or played**; no custom art or story scripts completed.


## 2026-11-05 — F0 foundation

- Adopt **Pokémon Parhelion** as the official project name.
- Verify independent source repository initially matches upstream `pokeemerald-expansion` commit `3ecef35381e321157c97c3aa0d064438026c7d68`.
- Replace the inherited README with a project-specific entrypoint while preserving upstream documentation and credits.
- Add `AGENTS.md`, canonical design summary, prologue requirements, procedural art policy, roadmap, pinned engine baseline and handoff.
- Narrow the inherited three-game + release CI to one focused Emerald source build; retain ROMs as ignored local output.
- **No custom maps, character graphics, dialogue or game code** in this commit. **Do not** count workflow creation as a passing compile or emulator boot.
