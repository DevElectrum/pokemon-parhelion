# AGENTS.md — Pokémon Parhelion

## Read first

1. `README.md` and `docs/parhelion/HANDOFF.md`.
2. `docs/parhelion/CANON.md` for confirmed creative choices.
3. `docs/parhelion/PROLOGUE.md` for the **only** currently detailed story slice.
4. `docs/parhelion/ROADMAP.md` for actual acceptance criteria.
5. `docs/parhelion/BASELINE.md` before changing build infrastructure or upstream engine code.

## Scope

Parhelion is a **standalone conventional GBA ROM hack** using `pokeemerald-expansion`. Do not edit or borrow unreviewed game code from `grand-anthology`, `pokemon-mosaic`, or `xgba`; no custom emulator dependency is intended.

**Current authorized foundation pass:** establish docs, baseline, reproducible compilation checks and handoff. Do not implement speculative later acts, official-duel mechanics, region-wide maps or complete faction leadership in this pass.

## Canon governance

- User/creative director decisions supersede assistant proposals.
- Keep **CONFIRMED**, **PROPOSED / WORKING**, **OPEN**, and **IMPLEMENTED** clearly separate. A passing source check is not proof of a visually tested gameplay scene.
- Do not silently choose the protagonist's family history, villain organization name, secret laboratory purpose, ancient-war cause, Terapagos explanation or regional names.
- Develop **incrementally**, one playable slice at a time. Detailed endgame outlines are not a prerequisite.
- Do not reframe the first criminal fight as a formal noble duel. The annual cooldown and noncanonical-defeat rules belong to **formal duels only**.
- If a plot decision is necessary to compile, use an explicitly labeled temporary placeholder, not invented canon.

## Engineering

- Preserve upstream history and credits. Pin an exact engine base; update upstream **deliberately**, not automatically.
- For each material source change, describe affected paths, tests actually run and test limits.
- Build before claiming "compiles"; execute in a real emulator before claiming "boots"; play through events before claiming "playable".
- Use existing `pokeemerald-expansion` systems and Porymap-compatible maps. Do not build an alternate battle or map engine.
- First slice targets three connected maps, four possible starter substitutions, one ordinary battle, save/continue. Enforce no duplicate starter, valid warps/collisions and consistent event flags.
- Main characters receive custom artwork; recurring support is hybrid; generic NPCs are seeded/procedural. A seed-only overworld generator is **not** automatically a finished matching battle-sprite pipeline.
- Keep `.gba`, `.elf`, save files, proprietary assets, credentials and local workspace paths out of commits. Maintain attribution/provenance for all external assets.

## Working rhythm

1. Check branch/CI/current handoff before editing.
2. Make a substantial coherent change; avoid tiny speculative patch loops.
3. Test proportionately, record real outcomes and limitations.
4. Update handoff/changelog on milestone boundaries.
5. Never label a milestone accepted solely because code was pushed.
