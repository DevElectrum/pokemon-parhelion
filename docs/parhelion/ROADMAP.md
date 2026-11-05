# Milestones and acceptance evidence

**Principle:** keep steps substantial and playable, without weeks of redundant CI loops. The engine does the heavy lifting; no new game engine or XGBA-only features are planned.

| Phase | Scope | Acceptance evidence |
| --- | --- | --- |
| F0 — foundation | Exact upstream baseline; project docs, handoff, focused Emerald build CI | Repository changes committed; CI compilation checked; **boot test separately identified** |
| P1 — movement | Small connected house, town and outskirts; temporary art | Navigable map/warp/collision smoke test in emulator |
| P2 — companion | One chosen species first, then Type: Null / Jangmo-o / Dreepy / Frigibax support | 4/4 choices; no dupes; clean save/continue |
| P3 — first battle | Storm escape; discovery; recovery montage; trafficker confrontation; one ordinary battle | Four starter paths; win/loss states; event flags; cold save |
| P4 — visuals | Custom player plus first grunt and targeted original backgrounds | In-game screenshots at native scale; sprite consistency and palette checks |
| P5 — prologue acceptance | Focused end-to-end run | Cold boot → choice → first battle → save/continue; no softlocks |

Do **not** start all acts, full world maps, the rank-duel engine, exotic renderer changes, a custom emulator, extensive battle balance, or finished soundtrack before the first slice.

## Current scorecard — 2026-11-05

- [x] New standalone public repository exists.
- [x] Source matches upstream Emerald expansion at base `3ecef353`.
- [x] Narrative scope and asset ownership categories decided.
- [ ] Parhelion foundation CI has passed on the project commit.
- [ ] A Parhelion project build has been booted in mGBA.
- [ ] Original three maps implemented.
- [ ] First playable opening battle implemented.
- [ ] Original art accepted in game.

Only check boxes after evidence exists. A newly committed CI workflow is **not** itself a passed CI result.


**P1 source work completed 2026-11-05:** Four distinct exterior blockmaps + a separate copied house interior, registered map groups/layouts, connections, home warp and storm-fallen gate. Compilation and interactive navigation have not been verified, so P1 is not yet accepted.


**Map visibility (2026-11-05):** source-grid schematic produced locally; real tileset preview renderer and GitHub Actions artifact workflow committed, **not yet run/inspected**. Emulator screenshots remain pending.


## Source visual gate verified on 2026-11-05

- **Refined four-exterior-map source-art render succeeded:** GitHub Actions run [42112246709](https://github.com/DevElectrum/pokemon-parhelion/actions/runs/42112246709), commit `7ac7788`.
- Its `parhelion-map-previews` artifact contains five individual PNGs and a contact sheet, reconstructed from actual `map.bin`, tilesets, metatiles and JASC palettes.
- Human visual inspection confirmed the initial flower-railroad defect was corrected: paths now use normal grass and sparse flowers. The homestead, rescue clearing, connecting trail, small town and house interior all appear in the preview.
- **Not an emulator capture:** object sprites, movement, new-game spawn, door entry, collision behavior, save/continue and the first battle have not been explored in-game. The current base-game intro still launches first.
- Existing Emerald build run [42111570036](https://github.com/DevElectrum/pokemon-parhelion/actions/runs/42111570036) passed on a map-preview renderer commit; newer source compilation runs may still be in progress. Do not infer acceptance for the latest head until its specific build is green.

**Next substantial gameplay batch:** wire the Parhelion starting position, then implement the opening rescue/recovery and one criminal confrontation with the four selected starters. Do not spend more work polishing temporary Emerald foliage or performing redundant CI reruns.
