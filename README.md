# Pokémon Parhelion

**Pokémon Parhelion** is an in-development, fan-made GBA Pokémon adventure set across two hostile regions separated by a dangerous central No Man's Land. It is a **new, independent project**, not a continuation of Grand Anthology, Pokémon Mosaic, or XGBA.

> **Status (2026-11-05): Foundation only.** This repository currently contains the unmodified gameplay engine plus Parhelion planning/build infrastructure. No original Parhelion maps, encounters, dialogue, character sprites, or playable prologue have been implemented. A compiled base ROM is not equivalent to a playable Parhelion demo.

## The first milestone

A short playable prologue: choose one of four wounded companion Pokémon; see its escape during a thunderstorm; rescue and care for it; encounter the criminals searching for it; win the **first ordinary trainer battle** near the protagonist's home; save and continue. We are **not** plotting or implementing the entire game before this first slice.

Start here:
- [Handoff and state](docs/parhelion/HANDOFF.md)
- [Design canon](docs/parhelion/CANON.md)
- [Prologue requirements](docs/parhelion/PROLOGUE.md)
- [Art and NPC pipeline](docs/parhelion/ART_PIPELINE.md)
- [Roadmap and acceptance gates](docs/parhelion/ROADMAP.md)
- [Pinned upstream baseline](docs/parhelion/BASELINE.md)
- [Agent/developer instructions](AGENTS.md)

## Building the base

This project currently uses [RHH's `pokeemerald-expansion`](https://github.com/rh-hideout/pokeemerald-expansion) on the Emerald target. The initial upstream base is pinned by commit in [BASELINE.md](docs/parhelion/BASELINE.md).

On Ubuntu / Pop!_OS, follow the upstream [Linux setup guide](docs/install/linux/UBUNTU.md), then run:

```sh
make -j"$(nproc)"
```

The normal output is `pokeemerald.gba`. The GitHub Actions workflow checks that an Emerald-target base ROM compiles, **not** that the opening story is playable or that a human-verified emulator boot occurred. Do not commit built ROMs, save files, or non-permitted proprietary assets.

The project retains upstream [INSTALL.md](INSTALL.md), [FEATURES.md](FEATURES.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [CREDITS.md](CREDITS.md).

## Attribution

Built on **Rom Hacking Hideout's `pokeemerald-expansion`** and the `pret/pokeemerald` decompilation. Please preserve all original credits and notices. Pokémon and related trademarks/art belong to their respective rights holders; this is an unofficial fan project, not affiliated with or endorsed by Nintendo, Game Freak, or The Pokémon Company.
