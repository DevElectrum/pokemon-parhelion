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
