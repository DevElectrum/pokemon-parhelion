# Parhelion prologue maps | source layouts v0.1

**Status:** original terrain layouts and map source added; compile and emulator walkthrough **not verified**. All visual tiles are temporary Emerald art.

The protagonist lives in a **secluded homestead**. North is **Rescue Woods** where the wounded starter is found; south is a **winding woodland approach** to the first town. The town is unavailable during the prologue because storm-fallen trees block the south exit of the homestead. The homestead has a **separate door-warped home interior**.

### New map IDs

- `ParhelionRescueWoods` (28×24), south ↔ homestead north.
- `ParhelionHomestead` (28×24), north ↔ woods, south ↔ town path, home door ↔ interior. **First battle area:** around tile (11,14).
- `ParhelionTownPath` (28×24), north ↔ homestead, south ↔ first town.
- `ParhelionFirstTown` (28×24), north ↔ path. **Three temporary houses** are exterior-only facade placeholders, not usable interiors yet.
- `ParhelionHomeInterior` (10×9), a copied **House1** interior layout, return warp ↔ homestead. Later: original furnishings and character art.

### Gate and script handoff

Two fallen-tree object events at homestead tiles **(13,21)** and **(14,21)** block the two-wide town path. They are conditionally hidden by `FLAG_PARHELION_TOWN_PATH_OPEN` (alias to an unused Emerald flag `0x035`). The **future first-battle aftermath script** must set this flag. The gate works as map-source geometry; the battle is **not** scripted yet.

### Legend

`#` impassable tree; `H` temporary house facade; `:` path; `~` tall grass; `.` grass/clearing; `R` rescue scene marker, future script; `B` first-battle courtyard marker, future script; `G` fallen-tree blockade NPC; `p` town plaza.

These are *source-grid previews*, not emulator screenshots. Final map section names, tilesets, starter spawn, weather scenes, NPCs and the region map are deferred. Using `REGION_HOENN` and Hoenn map-section IDs is a **temporary engine compatibility choice**, not Parhelion canon.

## ParhelionRescueWoods

```text
############################
############################
####..................##..##
####.............##~~~##..##
##...##.........~##~~~~.####
##..~##~~.......~~.~~~~~####
##.~.~~~##......~~.....~..##
####~.~~##......~~.....~..##
####~~.~~~......~~..R..~..##
##.~~~~.~~##.....~.....~..##
##.~~~~~.~##....~.........##
##..~~~~~.......~~.~::~~..##
##..............~:::::##..##
##.##...........~::~.~##..##
##.##...##.......::.......##
##......##.......::.......##
##..~~~~~.~~.....::.....####
##.~.~~~~~.~.::::::.....####
##.~~.~~~~~..::...........##
##.~~##~~~~~.::......####.##
##.~~##.~~~~.::......####.##
##.~~~~~.~~~.::...........##
#############::#############
#############::#############
```

## ParhelionHomestead

```text
#############::#############
#############::#############
##...........::...........##
####.........::.....##....##
####.........::.....##....##
##...........::::.........##
##.....HHHHH...::.........##
##.....HHHHH...::.....##..##
##..~~~HHHHH...::.~~~~##~.##
##.~.~~HHHHH...::~.~~~~~..##
##.~~.~HHHHH...::~~.~~~~~.##
##.~##.~.........~~~.~~~~.##
##.~##~..........~~~~.~~~.##
##.~~~~~.........~~~~~.~####
##..~~~~...B......~~~~~.####
##.~.~~~.........~.~~~~~..##
##.................##.....##
##....##.....::....##.....##
##.##.##.....::...........##
##.##........::.......##..##
############.::.############
############.GG.############
#############::#############
#############::#############
```

## ParhelionTownPath

```text
#############::#############
#############::#############
##......##...::...........##
##.##...##...::....##.....##
##.##........:::::.##.....##
##...##.........::....##..##
##...##.........::....##..##
##..............::~~~~~.~.##
##..~~~~~.~~....::.~~~~~..##
##.~.~~~~~.~::::::~.~~~~####
##.~~.~~~~~.::...~~~.~~~####
####~~.~~##~::...~##~.~~~.##
####~~~.~##~::...~##~~.~~.##
##.~~~~~.~~~::....~~~~~.~.##
##..~~~~~.~~:::::::~~~~~..##
##.~##~~~~.~.....::.~~~~~.##
##..##...........::~.~~##.##
##...............::~~.~##.##
##....##.....::::::~##.~~.##
##....##.....::.....##....##
##...........::...........##
##...........::.......##..##
#############::#############
#############::#############
```

## ParhelionFirstTown

```text
#############::#############
#############::#############
####.........::.........####
####.........::.........####
##...........::...........##
##..HHHHH....::.....HHHHH.##
##..HHHHH....::.....HHHHH.##
##..HHHHH....::.....HHHHH.##
##..HHHHH....::.....HHHHH.##
##..HHHHH....::.....HHHHH.##
##.##..:::::::::::::::....##
##.##~~~..ppp::pppp.~~~~~.##
##~.~~~~..ppp::pppp~.##~~~##
##~~.~~~..ppppppppp~~##~~~##
##~~~.~~..ppppppppp~~~.~~~##
##~~~~.~..ppppppppp~~~~.~~##
##~~HHHHH.ppppppppp~~~~~.~##
##.~HHHHH.ppp:ppppp.~~~~~.##
##..HHHHH....:............##
##..HHHHH....:............##
####HHHHH.::::.........##.##
####.::::::............##.##
############################
############################
```


## Real-tileset source visualization pipeline

`scripts/render_parhelion_maps.py` now reads the actual binary layout and tileset art (indexed PNGs, JASC palettes and 8-tile metatile definitions) and creates one PNG per map plus `all_parhelion_maps.png`. It draws **annotation markers** for the rescue tile, confrontation tile and fallen-tree object-event positions, not runtime NPC sprites.

You can run it locally using `python3 -m pip install Pillow` followed by `python3 scripts/render_parhelion_maps.py --out preview`. GitHub Actions `map-previews.yml` can render and upload the PNGs as an artifact, with a manual **Run workflow** action.

**This is still not an in-game screenshot.** Runtime animation, collision effects, object sprite art, cutscenes and the GBA renderer may differ. Full emulator screenshots require a compiled ROM, a reliable warp/spawn into these maps and an emulator capture. Before claiming success, inspect the actual generated PNG artifact and, later, emulator footage. No successful new Actions run for current Parhelion commits has been observed as of authoring.
