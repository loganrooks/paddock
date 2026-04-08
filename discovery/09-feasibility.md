# Feasibility

This document tracks what looks easy, medium, and hard for a private F1 fan party game prototype.

## Bottom Line

The concept looks feasible.

The main difficulty is not "can this be built?" It is choosing where to spend complexity:
- map and clue media
- room/multiplayer architecture
- content authoring
- watchability and reveal flow

## Feasibility By Area

### 1. Core Geography / Track Guessing Loop

Looks feasible with multiple viable prototype paths:

#### Path A: Google-First Prototype

- Street View Static API for clue images
- Google Maps Embed for answer reveal
- optional Static Maps for map-snippet clue rounds

Pros:
- quickest path to GeoGuessr-like feel
- low engineering effort
- high "this already feels real" factor

Cons:
- requires venue-by-venue and even segment-by-segment curation
- Google UI and policy constraints
- easier to overbuild around external APIs

Source-backed note:
- Google documents that Street View Static requests can be made by `location` or by specific `pano` ID, and that when imagery is unavailable the API returns a generic image unless `return_error_code=true` is used or metadata is checked first.
- Google also notes that imagery refreshes over time and panorama IDs can change, so curation must be maintained rather than assumed stable.

Implication for Prix Guesser:
- do not assume "track coverage is weak" or "track coverage is strong" globally
- test and curate exact target points at each circuit
- store target locations and refreshed pano references as authored content

#### Path B: Open Map + Curated Media

- MapLibre or another open map renderer
- hosted map tiles, not raw public OSM tile servers
- curated images, Wikimedia assets, self-authored clue media

Pros:
- more control
- less platform lock-in
- clearer long-term portability

Cons:
- loses some immediate Street View magic
- more content work

#### Path C: No Live Map APIs During Play

- authored clue cards
- static reveals
- schematic maps
- circuit fragments and city cues

Pros:
- cheapest
- fastest to prototype
- most stable

Cons:
- less immediate GeoGuessr fantasy
- relies more on writing and curation quality

### 2. Multiplayer And Room Flow

Research suggests this is feasible without heroic engineering if the scope stays disciplined.

#### Easy

- private room codes
- join links and QR joins
- host screen plus phone controllers
- timer-based rounds
- basic scoring
- kick/remove and reconnect banners

#### Medium

- one content substrate working across solo, couch, and remote
- team scoring
- challenge links
- difficulty tiers
- spreadsheet-backed authoring pipeline

#### Hard

- truly polished hybrid couch + remote sync
- spectator-grade watchability
- strong anti-cheat beyond private play
- sophisticated multi-view remote presentation without screen sharing

## Recommended Prototype Shapes

### Prototype Shape 1: Host-Screen Party Prototype

Best if the goal is to prove:
- room energy
- couch friendliness
- quick fan delight

Build:
- one host screen
- one phone controller page
- private rooms only
- 2-8 players
- curated rounds

### Prototype Shape 2: Solo + Challenge Link Prototype

Best if the goal is to prove:
- core geography loop
- scoring
- clue quality
- repeatability

Build:
- solo play
- friend challenge links
- no heavy multiplayer infra initially

### Prototype Shape 3: Hybrid Foundation Prototype

Best if the goal is to keep growth paths open:
- solo
- couch
- remote

Build:
- authoritative room model from day one
- more engineering cost upfront
- cleaner path to multiple future modes

## Architecture Options

### Lightweight

- PartyKit for rooms and realtime
- custom frontend
- spreadsheet or JSON-backed rounds

Best when:
- speed matters most
- early scope stays private and small

### Authoritative

- Colyseus for room state and timers
- custom frontend
- stronger server control

Best when:
- multiple clients need synchronized state
- fairness and reconnection matter

### Turn-Based / Phase-Heavy

- boardgame.io
- especially for bluffing, drafting, stewarding, bracket, or argument modes

Best when:
- the product leans toward party modes more than freeform map exploration

## Content Pipeline Feasibility

This looks very feasible if the first corpus is hand-authored.

Strongest initial approach:
- start from the 2026 calendar and a curated subset of iconic venues
- author `5-10` rounds per venue
- store each round with:
  - venue id
  - year or era
  - round type
  - clue text
  - lat/lng or answer target
  - difficulty
  - source URL
  - media type

The research suggests the initial corpus does not need scale first. It needs:
- strong clue ladders
- variation in answer type
- credible fan texture

## If Street View Coverage Is Missing For A Target Segment

Supplementation should preserve the same identity surface whenever possible.

Preferred fallback ladder:

### 1. Same circuit, different curated pano

If one corner or segment lacks useful imagery, try another verified pano on the same circuit or venue complex.

### 2. Same circuit, static map or satellite snippet

Use a static map image or authored map fragment of that same section or venue area rather than jumping immediately to generic city approaches.

### 3. Same circuit, authored clue ladder

Use:
- corner-sequence clue
- sector personality clue
- runoff / elevation / overtaking-profile clue
- reveal text explaining why the venue is identifiable

### 4. Approaches and surrounding area

Use this when the mode explicitly allows it, or when the goal is venue-adjacent recognition rather than circuit-internal recognition.

This should be treated as a different clue flavor, not the default replacement for missing on-track imagery.

## What Looks Less Feasible Early

- fully procedural content generation
- perfect cross-mode balance across many mode families
- a public-safe, rights-clean, large-scale content corpus
- complex anti-cheat or ranked ladders
- custom synchronized remote broadcasting experience

## Current Take

The cleanest early move appears to be:
- browser-based
- private rooms
- host screen + phone controllers
- curated content
- one geography anchor mode
- a few adjacent expert-fan modes

The highest-leverage technical decision is probably not the frontend framework. It is deciding whether the first prototype proves:
- the map clue fantasy
- the room/social fantasy
- or both at once

For the frontend and stack conversation specifically, see `12-framework-decision-context.md`. The point is to make the decision context explicit without pretending the framework choice is settled yet.

For the multiplayer and synchronization layer specifically, see `13-room-backend-decision-context.md`. That note separates room authority, timers, transport, reconnection, and persistence so "backend choice" does not stay vague.
