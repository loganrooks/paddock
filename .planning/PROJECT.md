# Prix Guesser

## What This Is

Prix Guesser is an unofficial, private-only F1 fan game project built around the fantasy of "GeoGuessr for Formula 1 places." It starts with grand prix venues, circuits, and race-weekend location literacy, while intentionally leaving room to grow into a broader F1-flavored party game where geography is the anchor rather than the whole product.

The initial audience is knowledgeable long-time F1 fans who can recognize circuits, venue texture, eras, and sport-specific signals. The project is being initialized for personal and friend play rather than public release.

## Core Value

Knowledgeable F1 fans can have a genuinely compelling, social, expert-feeling game night built around authored F1 rounds that reward real sport-specific recognition and interpretation.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Deliver one strong F1 geography-and-circuit anchor mode that feels meaningfully different from a generic geography quiz.
- [ ] Support private social play rather than only solo play, with a room structure that can fit couch, remote, or hybrid sessions.
- [ ] Keep the guest experience browser-first and low-friction across local, LAN, and privately hosted remote sessions.
- [ ] Use an authored round model that can represent circuit, venue, section, clue ladder, reveal explanation, and multiple answer surfaces.
- [ ] Build a curated content corpus strong enough to prove the core loop with real venues and recognizable fan texture.
- [ ] Preserve room for adjacent F1 party-game expansion without letting broader mode sprawl dominate the first implementation.

### Out of Scope

- Public-release hardening, rights-clean commercialization, and distribution-safe compromises — this is private-only for now.
- Large-scale competitive infrastructure such as ranked ladders, public matchmaking, or serious anti-cheat — not needed for initial private play.
- Fully procedural or AI-generated content as the basis of the product — the project needs authored quality first.
- Trying to ship a complete "all F1 party modes" platform in v1 — the first release needs one clear anchor.

## Context

This project started with a pre-GSD discovery pass captured in `discovery/`. That discovery work deliberately explored product framing, option space, open-source references, mode families, feasibility, stack decisions, room/backend decisions, and circuit-coverage uncertainty without prematurely locking the design.

Three tensions need to stay visible:

- the seed fantasy is "GeoGuessr for grand prix locations"
- the bigger ambition is "an F1-flavored party game platform"
- the current reality is "private-only project for personal and friend play"

The current most useful vocabulary distinction is:

- **anchor mode**: the authored geography-and-circuit round contract itself
- **event container**: a higher-level social or programmed shell that may outlive one active game
- **room**: the participant and trust shell in which a group gathers
- **game instance**: the active playable loop or frozen session currently being run inside a room or wrapper
- **session wrapper**: live room, solo practice, aftermath recap/report surface, share-by-link challenge, or later bounded-audience/spectator-facing shell
- **watchability layer**: the host-screen clarity, suspense, and reveal payoff that make a session socially legible
- **platform shell**: the broader long-arc product, if later wrappers and sibling modes genuinely reuse the same substrate

Research and synthesis so far suggest:

- the strongest early shape is likely location-led rather than location-only
- the geography core should feel circuit-aware and reveal-rich, not merely distance-scored
- the product is likely strongest in a host-screen-friendly social format
- one shared content substrate may later support solo, aftermath/recap, share-by-link challenge, couch, and private-room wrappers
- host-screen-friendly should be read as a watchability and shared-legibility bias, not as a claim that every participant always shares one truth surface

The most important modeling distinction discovered so far is:

- thin geography rounds store only coordinates and pano-style data
- authored F1 rounds carry sport-specific meaning such as circuit, section, clue ladders, answer target types, and reveal explanations

The current bias is strongly toward the authored model.

Open-source references already studied include:

- `benlikescode/geohub` for serious GeoGuessr-like product shape and reveal grammar
- `RasterCrow/Geo-Locator` for lightweight room/lobby flow
- `xchau/react-geofindr` for compact clue-ladder round loops
- `PartyKit`, `Colyseus`, and `boardgame.io` for room/state architecture patterns

The consolidated initialization brief is in `discovery/14-gsd-seed.md`.

## Milestone Arc

The project now has a sensible three-milestone directional arc. This is not a second active roadmap; it is the longer-range frame that current-phase planning should preserve without prematurely importing later scope.

For the concise identity and milestone frame, use this document. For the detailed transition doctrine that current planning should preserve, see `.planning/LONG-ARC.md`.

### Milestone 1: Game Night Works

Goal:

- prove one authored geography-and-circuit anchor mode and one watchable private-room wrapper that real friends actually want to replay

What this milestone must establish:

- authored round and pack contracts with stable identity and fallback posture
- pure judging and reveal logic independent of room transport
- private-room authority, browser-first join, host-screen legibility, and replayable social flow
- curated starter packs and enough calibration signal to improve the corpus

### Milestone 2: Play Anytime, Anywhere

Goal:

- prove that the same substrate can support more durable remote/private access, low-burden wrapper experiments, layered memory, and more sustainable content operations without turning the project into a public-platform obligation or choosing later winners too early

What this milestone is expected to add:

- remote/private convenience and more persistent access patterns
- low-burden wrapper experiments such as solo practice, aftermath recap/report, or share-by-link challenge surfaces, with the first post-private wrapper still open
- lightweight player identity, session history, and room/group memory or recurrence surfaces, if earned
- authoring and preview tooling that make content production sustainable
- richer content operations, official-library growth, pack sharing, calibration insight, and reusable content/history surfaces across wrappers
- preserved host-identity and discovery-choice seams so later convenience hosting or outside-pack status questions stay explicit rather than silently settled

### Milestone 3: F1 Party Platform

Goal:

- expand from one strong anchor mode into a broader F1 party platform only if the shared substrate has actually earned that expansion

What this milestone is expected to add:

- adjacent non-anchor mode families
- team variants and richer room roles
- bounded-audience, spectator-facing, or showcase-friendly wrappers
- deeper content programming, replay, and social surfaces

## How The Long Arc Constrains v1

The long-arc vision should influence current work in one specific way:

- Milestone 1 work should preserve seams for later wrappers, identity, content scaling, and adjacent modes where cheap to do so.
- Milestone 1 work should not pull Milestone 2 or 3 feature scope forward just because the later path is visible.
- The shared substrate matters more than forecasting exact later features. Preserve the substrate; defer the wrappers until they are earned.

## Future-Aware Posture

The current product posture should stay explicit while planning evolves:

- The emotional center of v1 is a watchable private game-night ritual for trusted groups, not ambient public discovery.
- The guest-facing product surface should stay browser-first whether the operator is running locally, on a LAN, or on a privately hosted remote box.
- The shared substrate should stay reusable across likely later wrappers such as solo practice, aftermath recap/report surfaces, share-by-link challenge links, private remote rooms, or bounded-audience shells.
- `presence identity` should remain separable from later persistent identity so low-friction room join does not harden into the wrong long-term model.
- Memory should stay layered: player history, room/group memory, event memory, and content calibration/history should not be treated as one flat ledger by default.
- Cadence should stay layered: session pacing, editorial/content rhythm, and later event cadence should remain distinguishable even if Milestone 1 implements only a narrow subset.
- Visibility state should stay explicit: trusted private rooms now, unlisted/share-by-link surfaces later, and broader public discovery only when the project deliberately accepts stronger moderation and status obligations.
- Watchability should stay tied to shared legibility and reveal payoff, not to one permanent truth surface or one fixed audience-right bundle.
- The official curated library should remain the trust anchor even if later editorial activation, visible outside credit, or other discovery states are explored.
- Bounded public or spectator-facing shells should be understood as wrappers around private-first play, not as evidence that the product center has become public-first.
- Current trust and service assumptions remain modest: private use, low moderation burden, no strong public uptime promise, no paid guaranteed access promise, and no obligation yet to support stranger participation well.

## Constraints

- **Product scope**: Private-only, unofficial fan project — early choices should optimize for real play value instead of public-safe caution.
- **Audience**: Initial audience is expert-biased long-time fans — the design does not need to flatten itself for casual users first.
- **Project state**: Greenfield project — major architecture choices remain open.
- **Design posture**: Keep decision context explicit without prematurely locking open product questions.
- **Content quality**: Authored content quality matters more than scale at initialization.
- **Geography fidelity**: Circuit-internal recognition is the primary fantasy — venue-approach clues are secondary and should not silently replace it.
- **Architecture leverage**: The highest-leverage technical choices are likely the round/content model and room authority model, not only the frontend framework.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Initialize as a private-only fan project | Public-safe constraints would distort the early product and reduce fidelity | Adopted |
| Treat geography as the anchor rather than the entire product identity | Preserves the clean hook while keeping broader F1 party-game expansion possible | Adopted |
| Bias toward authored F1 rounds instead of thin location-only rounds | The game should reward F1-specific recognition and explanation, not only generic geography guessing | Adopted |
| Keep the frontend/framework decision open | Ecosystem, room model, and content architecture matter more than locking a UI framework too early | Still open |
| Keep the room/backend decision open | The correct authority model depends on how durable, self-hostable, and synchronized the first live-room experience needs to be | Still open |
| Bias toward host-screen-friendly private play | The strongest current social fantasy is couch or private-room play with strong watchability | Adopted for v1 |
| Treat browser-first host/controller join as the real product surface | Guests should experience one coherent product whether the operator runs locally or on a private host | Adopted for v1 |

## Open Questions

| Question | Why It Matters | Criticality | Status |
|----------|----------------|-------------|--------|
| Is the best first product a tight geography game or a broader party shell with one anchor mode? | This shapes the roadmap width and how much the architecture must anticipate multi-mode expansion | Critical | Leaning: anchor-first with future wrappers protected |
| Which later wrapper should prove substrate reuse first after live private rooms: solo practice, aftermath recap/report surfaces, share-by-link challenge links, or bounded-audience shells? | This shapes what Phase 1 and Phase 3 must protect without widening v1 prematurely | Critical | Pending |
| Which answer surfaces should become first-class in the authored round model? | This determines schema design, scoring logic, and content authoring workload | Critical | Pending |
| How much unrestricted Street View exploration should exist, if any? | This affects clue design, difficulty, dependency on external APIs, and gameplay feel | Medium | Pending |
| How much should the first version optimize for watchability versus pure solver challenge? | This changes reveal pacing, host tooling, and UI priorities | Medium | Leaning: watchability is load-bearing, exact balance still open |
| When do internal authoring tools become necessary? | This determines whether v0 can stay file- or spreadsheet-driven or needs productized tooling immediately | Medium | Pending |
| Which visibility state, if any, should arrive first after trusted private rooms? | Public read surfaces, async challenge sharing, and public participation carry different trust and service obligations | Medium | Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-13 after Round 2B canon patch*
