# Parhelion development changelog

## 2026-11-05 — F0 foundation

- Adopt **Pokémon Parhelion** as the official project name.
- Verify independent source repository initially matches upstream `pokeemerald-expansion` commit `3ecef35381e321157c97c3aa0d064438026c7d68`.
- Replace the inherited README with a project-specific entrypoint while preserving upstream documentation and credits.
- Add `AGENTS.md`, canonical design summary, prologue requirements, procedural art policy, roadmap, pinned engine baseline and handoff.
- Narrow the inherited three-game + release CI to one focused Emerald source build; retain ROMs as ignored local output.
- **No custom maps, character graphics, dialogue or game code** in this commit. **Do not** count workflow creation as a passing compile or emulator boot.
