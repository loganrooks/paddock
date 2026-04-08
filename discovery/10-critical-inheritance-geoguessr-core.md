# Critical Inheritance: GeoGuessr Core

This document is about the GeoGuessr-style core only.

Scope:
- clue media
- guess map
- reveal flow
- scoring
- content model
- room/challenge structure directly supporting the core

It is not about the broader party-game expansion space except where that affects the core room shape.

Important note:
- this document should not be read as locking the design
- it defines candidate structures and design vocabulary so later docs have something concrete to react to
- if a prototype suggests a better answer surface or round shape, that should win

## Why This Exists

The goal is not to copy an existing clone.

The goal is to inherit the strongest proven ideas from open-source references while being explicit about where Prix Guesser should do something different because:
- it is F1-specific
- it is expert-first
- it is private-only for now
- it wants room to grow beyond generic geography

## Strongest Reference Roles

### `geohub`

Best reference for:
- a serious open-source GeoGuessr-like product shape
- custom maps and challenge links
- round snapshotting and reveal grammar

### `Geo-Locator`

Best reference for:
- lightweight live-room shell
- host-controlled rounds and timers
- simple curated pack selection

### `react-geofindr`

Best reference for:
- minimal single-round guess loop
- clue reveal ladder attached to one target
- simple submit-and-reveal flow

### `PartyKit`

Best reference for:
- the fastest private prototype room layer

### `Colyseus`

Best reference for:
- a stronger expandable room foundation

### `boardgame.io`

Useful but secondary reference for:
- phase-heavy or turn-based future variants
- not the most natural fit for the GeoGuessr core itself

## What To Inherit

### 1. Snapshot The Rounds Up Front

From `geohub`:
- build a content pack
- sample the rounds once
- freeze the sequence for that game or challenge

Why this matters:
- fairness across players
- reproducible challenge links
- easier reveal and score comparison

### 2. Keep The Reveal Grammar

From `geohub` and `react-geofindr`:
- play the clue
- make the guess
- reveal the answer
- show the error visually
- show score

This is still the right loop.

The key improvement is not changing the loop. It is changing what the reveal explains.

### 3. Support Packs, Not Only Freeform Randomness

From `Geo-Locator`:
- let the host choose a pack
- let the room play a short set of rounds

For Prix Guesser, packs likely matter more than “world/random.”

Examples:
- 2026 calendar
- classic street circuits
- technical circuits
- night races
- hybrid-era iconic weekends

### 4. Allow Clue Ladders Per Round

From `react-geofindr`:
- each target can have attached hints
- the round can reveal more over time or at a cost

This is highly relevant for Prix Guesser because expert-first play benefits from layered clue ladders.

### 5. Keep The Host-Controlled Room Shape Simple

From `Geo-Locator`:
- room code
- host controls settings
- players join
- rounds progress
- total scores at the end

That shell is enough for a private prototype.

## What To Deliberately Reject

### 1. Reject The Thin `lat/lng only` Content Model

This is the biggest divergence.

Generic geography clones often treat a round as:
- coordinates
- maybe pano id
- maybe heading/pitch/zoom

Prix Guesser needs a richer authored round object.

At minimum it likely wants:
- `venue_id`
- `circuit_id`
- `grand_prix_name`
- `city`
- `country`
- `era` or `season_validity`
- `answer_target_type`
- `reveal_bounds`
- `clue_steps`
- `media_assets`
- `difficulty`
- `aliases`
- `source_refs`
- `reveal_explanation`

This is a direction of travel, not a frozen schema.

### 2. Reject “Distance Is The Whole Truth”

Generic GeoGuessr clones mostly explain:
- how far off you were

Prix Guesser should also explain:
- why the correct answer was this venue
- what clue signals mattered
- whether the player was right venue but wrong point
- whether they identified the right circuit but wrong era

The reveal has to carry domain meaning, not only geography.

### 3. Reject Free-Roam Street View As The Default Assumption

This is the most important design caution from the delegated analysis.

Why:
- free roam often rewards generic geolocation skill
- Prix Guesser wants to reward F1-specific recognition and interpretation
- curated clue media gives you much stronger control over difficulty and meaning

This does not mean “do not use Street View.”

It means:
- use it deliberately
- often as curated static or constrained clues
- not automatically as unrestricted pano wandering

### 4. Reject Community-Map Complexity In Early Versions

`geohub` benefits from:
- public maps
- publishing
- likes
- discovery

Prix Guesser does not need that early.

A strong internal curated corpus is more valuable than public-content complexity.

### 5. Reject Hard-Coded Generic Session Assumptions

Things Prix Guesser should not inherit:
- fixed 5-round assumptions
- world-scale score ceilings
- generic country/city answer assumptions

F1-specific scoring and answer surfaces need their own logic.

## What To Redesign For Prix Guesser

### 1. The Round Should Be F1-Authored, Not Merely Located

A round is not just “where is this?”

It may be:
- which circuit
- which part of the circuit
- which venue complex
- which grand prix host city
- which era of the venue

And the clue should help the player reason at that level.

### 2. The Reveal Should Explain Identity

Best delegated insight:
- the reveal should explain why it was clearly Suzuka, Baku, Spa, Monaco, or Singapore

Possible reveal elements:
- venue name
- corner or section name
- key circuit traits
- why the clue was distinctive
- what an expert fan could have noticed

### 3. The Scoring Should Be Multi-Layered

Possible score layers:
- exact point accuracy
- correct circuit
- correct venue complex
- correct city
- correct country
- clue usage
- time pressure

This is better than a single generic kilometers formula.

### 4. The Mode Should Separate `Circuit-Internal` From `Venue-Approach`

This matters because you clarified that the main fantasy is mostly parts of the circuits themselves.

That implies two different clue families:

#### Circuit-Internal

- actual track sections
- circuit-side infrastructure
- runoff, kerbs, barriers, elevation
- corner personality

#### Venue-Approach

- roads approaching the venue
- nearby landmarks
- city/transport texture
- fan arrival context

The second is still useful, but it should not silently replace the first.

## Provisional Answer Surfaces

These are not final mode definitions. They are candidate answer surfaces that seem useful enough to keep visible.

### Circuit

The player identifies the overall circuit.

### Venue Complex

The player identifies the broader venue area without needing the exact on-track segment.

### Exact Corner Or Section

The player identifies a more specific slice of the circuit.

### Approach Context

The player identifies the venue from roads, landmarks, or surrounding context rather than the circuit itself.

### Composite Answer

The player identifies more than one layer, such as:
- `circuit + corner`
- `venue + era`
- `circuit + confidence`

The point of listing these now is not to commit to all of them. It is to make sure the core data model is not accidentally too narrow for them.

### 5. The Pack Model Should Be Explicit

A pack should probably mean something more intentional than “a bucket of random points.”

Better pack types:
- one circuit, many segments
- one season calendar
- one thematic family
- one era across several venues

## Infrastructure Inheritance

### Fast Private Prototype

Best fit from delegated analysis:
- `PartyKit`

Why:
- fast room setup
- natural private-room URLs
- low ops overhead
- enough for host screen, phone controllers, timers, reveal flow, and scoreboard sync

See `13-room-backend-decision-context.md` for the wider decision framing around authority, reconnection, persistence, and growth path.

### More Expandable Foundation

Best fit from delegated analysis:
- `Colyseus`

Why:
- authoritative room state
- stronger join/auth patterns
- better reconnection and room control story
- cleaner long-term base if the product grows

See `13-room-backend-decision-context.md` for the wider decision framing around authority, reconnection, persistence, and growth path.

### Why Not `boardgame.io` First

It is useful, but less natural for the GeoGuessr core because:
- it is game-engine-first rather than room-first
- it fits turn/phases abstractions better than map/reveal room orchestration

It may become more relevant later for bluffing, drafting, stewarding, or debate variants.

## Current Recommended Inheritance Pattern

If the goal is a disciplined v0 for the GeoGuessr-style core:

- inherit the product-grade reveal and challenge grammar from `geohub`
- inherit the lightweight room shell from `Geo-Locator`
- inherit the clue-ladder idea from `react-geofindr`
- use `PartyKit` if speed matters most
- use `Colyseus` if you want stronger long-term room foundations from the start

But do not inherit:
- thin location-only rounds
- generic geography scoring
- unrestricted Street View as the default play substrate
- public-map/discovery complexity

## Working Design Thesis

Prix Guesser’s GeoGuessr core should probably be:
- room-friendly
- reveal-rich
- authored rather than random-first
- circuit-aware rather than city-aware only
- expert-readable rather than generic-geography-readable

That is the main difference between “an F1 clone of GeoGuessr” and “a GeoGuessr-like game that actually feels native to F1.”

## Remaining Questions

- What is the main answer target in the anchor mode:
  - exact point
  - track section
  - circuit
  - venue complex
  - host city
- How much unrestricted Street View exploration should exist, if any?
- Should challenge links be the first shared format, or live rooms?
- Does the first pack model center on current calendar venues or iconic historical circuits?
- How much explanation should the reveal give before it starts feeling over-authored?
