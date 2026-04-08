# Open-Source Comparables

This document tracks GitHub repos that are worth studying as implementation references.

The goal is not to copy them wholesale. It is to learn:
- what kinds of architecture are already proven
- which repos are substantial versus toy clones
- where the useful abstractions are

## Product-Like Open-Source Comparables

### GeoHub

- Repo: [benlikescode/geohub](https://github.com/benlikescode/geohub)
- Type: substantial open-source geography guessing game
- Stack surfaced in README:
  - Next.js + TypeScript
  - NextAuth
  - MongoDB
  - Styled Components
  - Zod
  - Google Maps API + DeckGL
- Why it matters:
  - closest credible open-source analogue to a real GeoGuessr-like web product
  - supports official maps, custom maps, challenge links, daily challenge, and streak variants
  - explicitly documents the operational reality of Google Maps API cost pressure
- What to learn from it:
  - map and round data modeling
  - custom map authoring flow
  - challenge-link flows
  - how one clue substrate can support multiple wrappers

### Geo Locator

- Repo: [RasterCrow/Geo-Locator](https://github.com/RasterCrow/Geo-Locator)
- Type: multiplayer-oriented GeoGuessr clone
- Stack surfaced in README:
  - React
  - Firebase Realtime Database
  - Firebase Hosting
  - Google Maps API
- Why it matters:
  - exposes a straightforward lobby-driven multiplayer shape
  - uses a simple location JSON authoring model
  - explicitly frames itself as "play with friends without paying monthly"
- What to learn from it:
  - lightweight room and lobby patterns
  - minimal-authoring content pipeline
  - results and reveal screens for shared play

### Geofindr

- Repo: [xchau/react-geofindr](https://github.com/xchau/react-geofindr)
- Type: smaller city-guessing clone
- Stack surfaced in README:
  - React
  - Express
  - PostgreSQL + Knex
- Why it matters:
  - useful as a compact single-loop reference
  - includes hint unlocks, which is relevant to clue-ladder design
- What to learn from it:
  - lean game-loop modeling
  - simple score-calculation approach
  - a smaller codebase that may be easier to inspect than larger clones

### GeoguessrClone-React-Typescript

- Repo: [jakubfalkiewicz/GeoguessrClone-React-Typescript](https://github.com/jakubfalkiewicz/GeoguessrClone-React-Typescript)
- Type: partial / in-progress clone conversion
- Why it still matters:
  - likely less useful as a full product reference
  - still useful as an indicator of common frontend architecture patterns used by clone builders
- What to learn from it:
  - little as a product model
  - maybe some frontend interaction wiring if the code is cleaner than the README implies

## Infrastructure-Focused Open-Source Comparables

These are not geography games. They matter because the party-game shape may depend more on room and state infrastructure than on map-specific code.

### boardgame.io

- Repo: [boardgameio/boardgame.io](https://github.com/boardgameio/boardgame.io)
- Type: turn-based multiplayer engine
- Why it matters:
  - built-in multiplayer, lobby, state management, phases, logs, and plugins
  - especially useful if the game leans toward rounds, phases, secret information, drafting, bluffing, or argument
- Best fit:
  - turn-based or timer-based party modes
  - modes with explicit phase transitions and server-managed state

### Colyseus

- Repo: [colyseus/colyseus](https://github.com/colyseus/colyseus)
- Type: authoritative multiplayer framework
- Why it matters:
  - room-based architecture
  - realtime state sync
  - matchmaking and reconnection
  - better fit when host authority, timers, and multi-client sync matter
- Best fit:
  - hybrid couch + remote rooms
  - competitive rounds where server authority and timing matter

### PartyKit

- Repo: [partykit/partykit](https://github.com/partykit/partykit)
- Type: lightweight real-time multiplayer platform
- Why it matters:
  - fast path to room-based browser multiplayer
  - lower ceremony than a heavier authoritative game server
- Best fit:
  - lightweight private rooms
  - host-screen orchestration
  - early prototypes where shipping quickly matters more than perfect game-authoritative architecture

## What These Repos Suggest

### 1. A Credible Open-Source GeoGuessr-Like Exists

`geohub` is the most important signal here. This is not just a toy clone. It demonstrates that a serious open-source geography guessing product can support:
- custom maps
- daily play
- challenge links
- multiple mode wrappers
- real operational concerns around map APIs

### 2. Multiplayer Can Stay Fairly Simple At First

`Geo Locator` suggests that a private-room prototype does not need enterprise netcode to be fun. Lobby + rounds + results may be enough for early proof.

### 3. The Party Layer And The Map Layer Do Not Need The Same Abstraction

The geography-product repos are useful for:
- map and clue modeling
- scoring
- location authoring

The multiplayer-framework repos are useful for:
- room state
- reconnection
- authoritative timing
- multi-client orchestration

This strongly suggests a split architecture:
- game-content model inspired by open-source geography games
- room/state infrastructure inspired by multiplayer frameworks

### 4. The Best Open-Source References Are Uneven

A lot of GitHub search results are shallow clones, abandoned experiments, or thin wrappers around Google Maps.

That means:
- the repo list should be curated, not exhaustive
- code quality matters more than keyword match
- strong infrastructure repos may be more valuable than weak direct clones

## Current Take

If the goal is to seed an implementation intelligently, the best open-source references right now are:
- `benlikescode/geohub` for product shape
- `RasterCrow/Geo-Locator` for lobby-oriented friend play
- `xchau/react-geofindr` for compact loop simplicity
- `boardgame.io`, `Colyseus`, and `PartyKit` for room/state architecture options

These should be treated as study targets, not as a mandate to copy their stacks.
