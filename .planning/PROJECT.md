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

Research and synthesis so far suggest:

- the strongest early shape is likely location-led rather than location-only
- the geography core should feel circuit-aware and reveal-rich, not merely distance-scored
- the product is likely strongest in a host-screen-friendly social format
- one shared content substrate may later support solo, challenge, couch, and private-room wrappers

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
| Initialize as a private-only fan project | Public-safe constraints would distort the early product and reduce fidelity | — Pending |
| Treat geography as the anchor rather than the entire product identity | Preserves the clean hook while keeping broader F1 party-game expansion possible | — Pending |
| Bias toward authored F1 rounds instead of thin location-only rounds | The game should reward F1-specific recognition and explanation, not only generic geography guessing | — Pending |
| Keep the frontend/framework decision open | Ecosystem, room model, and content architecture matter more than locking a UI framework too early | — Pending |
| Keep the room/backend decision open | The correct authority model depends on how durable and synchronized the first live-room experience needs to be | — Pending |
| Bias toward host-screen-friendly private play | The strongest current social fantasy is couch or private-room play with strong watchability | — Pending |

## Open Questions

| Question | Why It Matters | Criticality | Status |
|----------|----------------|-------------|--------|
| Is the best first product a tight geography game or a broader party shell with one anchor mode? | This shapes the roadmap width and how much the architecture must anticipate multi-mode expansion | Critical | Pending |
| Should the first shared format be live rooms or challenge links? | This changes room architecture, content flow, and where synchronization complexity lands | Critical | Pending |
| Which answer surfaces should become first-class in the authored round model? | This determines schema design, scoring logic, and content authoring workload | Critical | Pending |
| How much unrestricted Street View exploration should exist, if any? | This affects clue design, difficulty, dependency on external APIs, and gameplay feel | Medium | Pending |
| How much should the first version optimize for watchability versus pure solver challenge? | This changes reveal pacing, host tooling, and UI priorities | Medium | Pending |
| When do internal authoring tools become necessary? | This determines whether v0 can stay file- or spreadsheet-driven or needs productized tooling immediately | Medium | Pending |
| How much should future non-geography party modes influence v1 architecture? | Over-weighting future expansion could over-engineer v1, but under-weighting it could force a rewrite | Medium | Pending |

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
*Last updated: 2026-04-08 after initialization*
