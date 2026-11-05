# Art policy and NPC generation

## Direction

Original, expressive characters inspired by the **visual proportions and readability** of Pokémon Black/White, while respecting the pinned GBA engine's palette, tile, frame and memory constraints. Inspiration does not mean copying existing sprites.

## Production tiers

| Tier | Who | Method |
| --- | --- | --- |
| 1 — cast | Player, recurring major characters, officials, named rivals/antagonists | Individually drawn and animated original art, unique battle sprites/portraits |
| 2 — support | Recurring local officials, researchers, supporting characters | Generated base plus deliberate manual edits |
| 3 — population | Ordinary trainers, common civilians, guards and low-level trafficker grunts | Procedurally seeded sprites from shared original templates |

## Technical proposal

A persistent appearance record should include stable character ID and random seed, hair color/style, skin palette, age/shape range, face geometry, outfit/occupation, optional accessories and region/faction tags.

The same appearance record should feed **all four facing directions**, movement frames, and (once implemented) a **matching trainer battle portrait**, rather than randomizing each graphic independently. Character names, teams and dialogue are authored separately.

The local **NPC Sprite Lab v0.1** has demonstrated seeded 4-direction/3-frame procedural overworld images, but its shapes/animation are still too rigid for finished BW-inspired art. It does **not** currently produce matching trainer battle artwork or demonstrate in-ROM compatibility. The original archive is in the separate project-library snapshot; this repository is not claiming that tool has been integrated.

## First slice art budget

- One **custom** player design and backsprite (temporary placeholders permissible during engineering).
- One ordinary criminal trainer battle sprite and up to two overworld grunt variants from the procedural pipeline.
- Town/house/outskirts environment tiles and minimal battle background(s); use temporary compatible visuals first, then replace with original art.
- Inspect at native GBA size, validate palettes, transparency and frame order **in a real game build**.
- Track permission, attribution and hashes for every imported asset. Avoid unlicensed artwork and published compiled ROMs.

Do not allow a beautiful standalone render to substitute for verified, animated in-engine assets.
