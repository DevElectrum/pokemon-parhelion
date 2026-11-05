# Prologue — first playable story slice

**Scope:** one fixed Gen 8 starting region, three small connected gameplay maps, four mutually exclusive starter variants and one scripted **ordinary** battle. This file is a requirement for a **future** implementation, not evidence the maps or events exist.

## Scene sequence

| Beat | Event | Expected state |
| --- | --- | --- |
| 0 | Pre-game selection of Type: Null, Jangmo-o, Dreepy or Frigibax | One persistent species choice |
| 1 | Thunderstorm disrupts Gen 8 traffickers' rare-Pokémon shipment | Only selected companion escapes, wounded |
| 2 | Protagonist finds the companion near the outskirts | Rescue event fires once |
| 3 | Several weeks of care at home create the bond | Selected Pokémon becomes battle-capable |
| 4 | Low-level criminals finally track it to the protagonist's home | One-time confrontation |
| 5 | Criminals demand its return; protagonist refuses | **First ordinary trainer battle** |
| 6 | Immediate aftermath and save/continue | End of initial milestone |

Exact dialogue, event pacing, first opponent's species/levels, scene transitions and the opening-battle defeat branch remain **open**. Placeholders may be used for engineering only and must be labeled.

## Planned three-map skeleton

- `PARHELION_HOME`: interior, recovery sequence, safe exit.
- `PARHELION_TOWN`: protagonist's home exterior, public movement, confrontation/battle tile.
- `PARHELION_OUTSKIRTS`: wounded companion discovery, a short path back to town, optional brief storm cutscene.

These are **working map identifiers**, not final internal map constants or region names. A transport cutscene can reuse a temporary mapped area; no requirement to build a fourth fully designed location.

## Mandatory checks before accepting the slice

1. New game with each of **4** starter selections produces exactly the correct Pokémon, exactly once.
2. Three maps connect without invalid warps, blocked exits or out-of-bounds walking.
3. Storm, rescue, recovery, confrontation and battle flags persist after saving.
4. The selected companion is battle-capable before the first battle.
5. First opponent is an ordinary trainer, with no accidental official duel/legal rank logic.
6. Victory proceeds correctly; battle defeat/retry behavior is **explicitly specified and tested** before acceptance.
7. Player can save, close emulator, reopen, continue and retain the correct story/party state.
8. All displayed art passes actual emulator-resolution/palette inspection.

**Deferred:** full regional map, nobility implementation, the Gen 9 lab, later NPC cast, UB/Terastal mechanical demonstrations and multi-region travel.
