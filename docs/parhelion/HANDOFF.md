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
