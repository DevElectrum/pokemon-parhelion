# Engine baseline, reproducibility and provenance

**Pinned original upstream source (2026-11-05):**
- Repository: https://github.com/rh-hideout/pokeemerald-expansion
- Branch when captured: `master`
- Exact source commit: `3ecef35381e321157c97c3aa0d064438026c7d68`
- Git tree: `c8a6de1d2186b5b1a5bba233bd7cb11aea3a048a`
- Same commit and tree initially observed in `DevElectrum/pokemon-parhelion` before original Parhelion commits.
- This project will retain upstream history/credits. Upstream improvements should be merged **selectively and deliberately**, not automatically.

**Target:** `GAME_VERSION=EMERALD`, English. Normal `make` output: `pokeemerald.gba`. The ROM is a **base engine image**, not an implemented Parhelion game.

## Ubuntu/Pop!_OS or compatible Linux

Use [upstream Linux instructions](../../docs/install/linux/UBUNTU.md) or:
```sh
sudo apt install build-essential binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi git libpng-dev python3
git clone https://github.com/DevElectrum/pokemon-parhelion.git
cd pokemon-parhelion
git remote add upstream https://github.com/rh-hideout/pokeemerald-expansion.git
make -j"$(nproc)"
```

Optional verification on a local machine: use **mGBA** to launch the built `pokeemerald.gba` and record a screenshot or reproducible log. The initial CI only compiles and checks ROM header/size; it **does not launch mGBA**.

## GitHub Actions

`.github/workflows/build.yml` narrows the inherited multi-game CI to one **Emerald-target build**. It validates the output exists, falls within standard 32 MiB GBA ROM bounds, has a non-empty header title, and prints a SHA-256 digest. It deliberately does **not** upload the ROM.

**Evidence log:**
- 2026-11-05: original source commit/tree confirmed through GitHub repository APIs. Local source cloning and compilation in the assistant runtime were not possible (no GitHub DNS access and no ARM toolchain installed).
- CI result and emulator boot are still **pending** and must be filled in with actual run evidence once known.

## Guardrails

Do not alter other DevElectrum repos; do not require XGBA. Confirm any graphics/map format behavior against **this pinned code**, not a generic tutorial or a different expansion release.
