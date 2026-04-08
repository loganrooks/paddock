# Prix Guesser GSD Seed

This document is the consolidated idea brief for initializing GSD from the discovery package.

It captures the current project shape without pretending every major design decision is already settled.

## Project Summary

Prix Guesser is an unofficial, private-only F1 fan game project.

The seed fantasy is "GeoGuessr for Formula 1 places," starting with grand prix venues and circuits. The broader ambition is to grow that into an F1-flavored party game platform where the geography mode is the anchor rather than the whole identity.

The initial audience is knowledgeable long-time F1 fans, roughly people who have followed the sport for years and can recognize circuits, eras, race-weekend texture, and deeper sport-specific signals.

This is not being initialized as a public-safe commercial product. It is being initialized as a private project for personal use and friend play.

## Core Product Thesis

The most promising current thesis is:
- one strong geography-and-circuit anchor mode
- layered clue ladders that reward genuine F1 literacy
- a host-screen-friendly party shell for couch or private-room play
- room to expand later into adjacent F1 social modes

The product should feel:
- authentic to knowledgeable fans
- socially alive rather than solitary
- legible to watch, not only fun to play
- flexible enough to grow beyond one mode

## Anchor Mode Shape

The anchor mode should not be treated as a generic geography clone with only coordinates and distance scoring.

The more interesting direction is an authored F1 round model where a round can encode:
- circuit identity
- venue identity
- specific sections or corners
- venue-approach context
- era-sensitive meaning
- reveal explanations that teach why the clue was identifiable

Important distinction:
- the main fantasy is mostly circuit-internal recognition
- approach-to-circuit or surrounding-area clues can exist, but should be treated as a distinct clue flavor or mode family, not the default replacement

Promising answer surfaces worth keeping visible:
- circuit
- venue complex
- exact corner or section
- approach context
- combined answers such as `circuit + corner`

These are examples of the design space, not locked final mode definitions.

## Adjacent Mode Expansion Space

The broader project may eventually include adjacent F1 party modes such as:
- circuit recognition from shape fragments or sector logic
- race-weekend texture and venue atmosphere identification
- history and memory modes tied to place and era
- strategy and prediction modes
- regulation and stewarding judgment modes
- bluffing, debate, ranking, and social-mischief modes

Discovery so far suggests the product could become a strong party-night game if it preserves one clear anchor instead of becoming a pile of unrelated trivia.

## Audience And Difficulty

The first serious audience is expert-biased, not general casual sports traffic.

That means:
- harder clue design is acceptable
- reveals should respect deep fan knowledge
- difficulty can range upward aggressively
- the project does not need to flatten itself for mainstream readability at initialization time

It may still later support layered difficulty, but expert-fan authenticity is the current priority.

## Product Shape Options Still Open

The discovery package intentionally does not lock the final product shape.

Open product-shape possibilities still in play:
- a tight geography-first game
- a location-led F1 party game with adjacent modes around one anchor
- a broader F1 party platform where geography is one pillar

The current bias is toward the middle option, but this should still be treated as a hypothesis rather than a decision.

## Social Structure Options Still Open

The discovery work points toward a shared content substrate that could support:
- solo play
- challenge links
- live private rooms
- couch co-op
- hybrid shared-screen plus phone-controller play

The current strongest social fantasy is host-screen-first or hybrid private-room play, but solo and async challenge formats may still matter.

## Content And Media Posture

The content system will likely be curated and hand-authored first.

The strongest initial content posture appears to be:
- curated rounds rather than procedural generation
- packs built around circuits, calendars, themes, or eras
- strong reveal explanations
- multiple clue media types

Possible media families:
- Google Street View static clues
- map or satellite snippets
- authored clue text
- venue-adjacent photographs or authored reference crops

The project should not assume universal Street View quality across all circuits. Coverage should be curated venue by venue and segment by segment.

## Technical Posture

The discovery phase produced several important technical conclusions:

### Frontend / Stack

The framework decision should remain open.

What matters more than framework popularity:
- product-model clarity
- maps/media integration
- agent editability
- host-screen plus phone-controller fit
- internal content-authoring fit
- operational simplicity
- debuggability

Serious current frontend candidates:
- React + Vite
- Next.js
- SvelteKit
- Vue/Nuxt
- smaller minimal TypeScript setup

Current non-binding read:
- React is defensible because of ecosystem and OSS inheritance
- Next is not automatically justified
- React + Vite may be a better baseline than a heavier full-app framework
- SvelteKit remains a credible lean alternative

### Room / Backend

The realtime room decision should also remain open.

What matters most:
- authority model
- timer and reveal synchronization
- reconnect and recovery story
- host-control ergonomics
- ease of local and multi-client testing
- compatibility with the richer authored round model

Serious current room/backend candidates:
- PartyKit as the speed-first room candidate
- Colyseus as the stronger authority-first room candidate
- boardgame.io mainly for later phase-heavy party modes
- a BaaS-led approach for app plumbing, but not as a substitute for a real room-authority model

Current non-binding read:
- PartyKit is the strongest fast private-prototype option
- Colyseus is the strongest sturdier-foundation option

### Content Model

One of the most important architectural choices is not the frontend framework.
It is whether the system is built around:
- thin `lat/lng + pano` rounds
or
- richer F1-authored rounds with multiple answer surfaces and reveal logic

The current clear bias is toward the authored model.

## Open-Source Reference Inheritance

Important open-source references already studied:
- `benlikescode/geohub`
- `RasterCrow/Geo-Locator`
- `xchau/react-geofindr`
- `boardgame.io`
- `Colyseus`
- `PartyKit`

Current inheritance stance:
- inherit session/reveal/challenge ideas from `geohub`
- inherit simple lobby-oriented room flow from `Geo-Locator`
- inherit minimal clue-ladder loop ideas from `react-geofindr`
- do not inherit a thin generic geography model
- do not assume unrestricted Street View free-roam should be the default

## Feasibility Snapshot

Current discovery suggests:
- the concept is feasible
- a private browser-based prototype is realistic
- host screen plus phone controllers looks viable
- the main engineering difficulty is choosing where complexity belongs:
  - content authoring
  - room synchronization
  - map/media handling
  - reveal and watchability flow

Street View and circuit coverage are not uniform, but a curated venue-by-venue approach looks workable. Some venues are strong for circuit-internal clues, some are usable with fallbacks, and some should be treated as fallback-first.

## Working Constraints

- Private-only project for now
- Greenfield project
- Initial product should optimize for real play value, not public-release caution
- Keep decision context explicit without prematurely locking design
- Preserve expansion room for broader F1 party-game possibilities

## Suggested v1 Bias For Initialization

The initialization should probably bias toward this interpretation:
- web-based experience
- private rooms
- host-screen-first or hybrid social play
- one strong geography/circuit anchor mode
- curated hand-authored content
- architecture that does not block future adjacent party modes

This is a bias for roadmap shaping, not a hard lock on final product scope.

## Important Open Questions To Preserve

- Is the best first product a tight geography game or a broader party shell with one standout geography mode?
- How much should the first version optimize for watchability versus pure solver challenge?
- Should live rooms or challenge links be the first-class shared format?
- How much unrestricted Street View exploration should exist, if any?
- When do we need internal authoring tools rather than simple content files or spreadsheets?
- How much of the eventual party-game expansion needs to influence v1 architecture up front?
- Which answer surfaces should become first-class in the initial authored round model?

## Discovery Inputs

This seed brief is derived from the discovery package in `discovery/`, especially:
- `01-vision.md`
- `02-option-space.md`
- `04-modes.md`
- `08-open-source-comparables.md`
- `09-feasibility.md`
- `10-critical-inheritance-geoguessr-core.md`
- `11-circuit-coverage-audit.md`
- `12-framework-decision-context.md`
- `13-room-backend-decision-context.md`
