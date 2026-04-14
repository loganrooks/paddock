---
date: 2026-04-13
lane: j
lane_name: "Engineering-exposure research lane"
delegation_class: initial-architecture-research-planning
output_file: 02-lanes/architecture/lane-j-output.md
task_spec: 02-lanes/architecture/lane-j-task-spec.md
source_artifacts:
  - 02-lanes/architecture/lane-j-a-output.md
  - 02-lanes/architecture/lane-j-b-output.md
  - 02-lanes/architecture/lane-j-c-output.md
  - 02-lanes/architecture/lane-j-d-output.md
  - 02-lanes/architecture/lane-j-e-output.md
  - 02-lanes/architecture/lane-j-f-output.md
  - 02-lanes/architecture/lane-j-g-output.md
tags:
  - exploratory-audit
  - lane-j
  - engineering-exposure
  - synthesis
---

# Lane J: Engineering-Exposure Research

## Lane framing

This lane was run to answer a narrower question than the earlier architecture summaries:

- what do relevant reference systems actually expose about their engineering?

Not:

- what architecture should Prix Guesser definitely choose
- which stack is "best"
- whether one mechanism solves everything

The lane used a two-wave structure:

- first wave for broad ecosystem coverage
- second wave for the weak spots that still needed deeper engineering exposure

The result is uneven by ecosystem, but much better grounded than the earlier architecture-only synthesis.

## Evidence quality and source audit summary

### Strongest evidence classes in this run

Highest-confidence engineering exposure came from:

- official engine/networking docs
  Unreal networking, Replication Graph, Iris
- official engineering blogs
  Riot VALORANT netcode and Fog of War
- official technical talks / slide decks
  Overwatch scripted weapons/abilities, Jackbox GDC deck
- official framework/service docs
  Colyseus, boardgame.io, PlayFab Lobby/Party

These sources directly exposed mechanisms like:

- authoritative state ownership
- per-client visibility or filtering
- seat reservation and reconnect
- replication prioritization and dormancy
- prediction and rollback/repair loops
- room shell / lobby shell lifecycle

### Medium-confidence evidence

Useful but less deeply technical sources came from:

- official product/support docs
  Kahoot, Mentimeter, Slido, GeoGuessr, Among Us, iRacing support, Trackmania docs, Gran Turismo World Series pages

These are strong for:

- topology
- room/event shapes
- moderation and role boundaries
- qualifiers, splits, heats, ghosting
- public limits and operator controls

They are weaker for:

- low-level transport
- exact authority internals
- replication details

### Secondary but still useful framing

- Gaffer on Games
- Age of Empires networking paper mirror
- publisher/book references

These were useful mainly as conceptual framing and source-hunt leads, not as primary evidence for a shipped browser-first product.

### Source-audit conclusion

The strongest direct engineering evidence in this run came from:

- `Colyseus`
- `boardgame.io`
- `PlayFab Lobby / Party`
- `Unreal`
- `Riot VALORANT`
- `Overwatch` slide material
- `GGPO`
- `Jackbox` engineering/GDC material

The strongest topology/event evidence came from:

- `Trackmania`
- `iRacing`
- `Gran Turismo World Series`
- `Among Us`
- `Spaceteam`
- `Artemis`

That means the synthesis should be trusted most where it references those direct mechanisms, and treated more cautiously where it generalizes from product docs alone.

## Concrete engineering patterns exposed by reference designs

### 1. Separate shells and states are normal, not exotic

Multiple references directly or strongly imply a separation between:

- event shell
- room/lobby shell
- active game/session instance

Concrete evidence:

- `Slido` multiple rooms
- `GeoGuessr` party vs specific lobbies
- `Trackmania` scalable rooms, qualifiers, divisions
- `iRacing` event registration vs actual split fields
- `PlayFab Lobby` as shell separate from Party network or gameplay state

High-confidence read:

- large participation and small decisive interaction are routinely separated by design

### 2. Visibility filtering is a real engineering mechanism, not just UI hiding

Concrete evidence:

- `Colyseus StateView`
- `boardgame.io playerView` and log redaction
- `Riot` Fog of War visibility withholding
- `Unreal` relevancy, prioritization, dormancy

High-confidence read:

- the right technical question is often not "what data exists?"
- it is "which client/view is allowed to receive which slice, when?"

This is one of the most relevant exposed mechanisms for Prix Guesser.

### 3. Authoritative state is usually preserved even when local responsiveness is needed

Concrete evidence:

- `Unreal` server-authoritative replication
- `Riot` server-authoritative model with client prediction and bounded rewind
- `Overwatch` authoritative scripted gameplay plus rollback/replicate/simulate repair
- `Colyseus` server-room lifecycle and state mutation model
- `boardgame.io` server-only moves and filtered sync

High-confidence read:

- local responsiveness and authoritative truth are not opposites
- mature systems usually preserve both by giving clients narrowly scoped predictive work, not full trust

### 4. Large rooms scale through coupling reduction more than raw transport heroics

Concrete evidence:

- `Trackmania` qualifiers/divisions/room splits
- `iRacing` splits/heats/ghost racing/connection black flags
- `Gran Turismo` leagues and qualifier funnels
- `Jackbox` large audience shell over tiny active rooms
- `Mentimeter`/`Kahoot`/`Slido` shared prompt cadence with small payloads

High-confidence read:

- many "large participation" successes are achieved by reducing who matters to whom, or when

### 5. Moderation and operator controls are part of the runtime

Concrete evidence:

- `Jackbox` moderation controls, passwording, Twitch gating
- `Mentimeter` moderation queues and profanity filter
- `Slido` moderation review flow and co-host privileges
- `Among Us` reports, chat restrictions, public-lobby safety changes
- `Blood on the Clocktower` storyteller / moderation / blocking / flagging model

High-confidence read:

- once public or semi-public participation enters the picture, moderation is not an afterthought
- it changes room shape, rights, and reveal pipelines

## Concrete problems and concrete mechanisms

### Problem: how do players enter and claim a place in a session?

Concrete exposed mechanisms:

- `Colyseus`
  reserve seat -> claim seat, with timeout
- `boardgame.io`
  claim seat by `playerID` plus credential token
- `PlayFab Lobby`
  join via connection string, invites, search, or arranged-lobby handoff
- browser-party systems
  short code + QR + direct link patterns

What this suggests:

- join flow, seat claiming, and room ownership should be thought of as explicit mechanics, not one monolithic "join room" action

### Problem: how do different clients see different truths safely?

Concrete exposed mechanisms:

- `Colyseus StateView`
  object-level per-client filtering
- `boardgame.io playerView`
  game-state redaction before payload emission
- `Riot` Fog of War
  server-side withholding of enemy information
- `Unreal`
  relevancy/prioritization/dormancy

What this suggests:

- visibility policy belongs in state publication, not just UI

### Problem: how do you keep local feel under authority?

Concrete exposed mechanisms:

- `Riot`
  local self-prediction, rewind hit registration, bounded lag compensation
- `Overwatch`
  local rollback/replicate/simulate loop for local entities, remote replication for others
- `GGPO`
  input prediction plus save/load rollback contract
- `Gaffer`
  snapshot interpolation, state sync, jitter buffering

What this suggests:

- if Prix ever builds higher-tempo action play, the likely path is not "trust clients"
- it is a narrowly scoped local-feel layer on top of authoritative state

### Problem: how do you let many people participate without one giant mutually coupled field?

Concrete exposed mechanisms:

- qualifiers
- divisions
- splits
- heats/consolations
- ghost racing
- finalist funnels
- audience shells

Concrete examples:

- `Trackmania`
- `iRacing`
- `Gran Turismo`
- `Jackbox`
- `GeoGuessr Live Challenge`

What this suggests:

- event-shell design is at least as important as netcode design for scaling

### Problem: how do you keep live participation safe and legible?

Concrete exposed mechanisms:

- moderator roles
- co-host rights
- pre-display approval queues
- profanity filters
- kick/ban/report flows
- public/private discoverability controls

What this suggests:

- rights and moderation cannot be bolted on later if public participation matters

## What seems most relevant to Prix Guesser

### Most relevant direct mechanisms

The most directly relevant exposed mechanisms for Prix Guesser are:

- `Colyseus`-style authoritative room lifecycle, seat reservation, reconnect, and filtered state views
- `boardgame.io`-style player-specific state redaction, phase/stage control, and server-only moves
- `PlayFab Lobby`-style room shell lifecycle, ownership migration, access policies, invites, and TTL behavior
- `Jackbox`-style active-room vs audience-shell separation and moderator/operator controls
- `Trackmania` / `iRacing`-style qualifiers, splits, heats, ghosting, and staged reduction
- `Unreal` / `Riot` / `Overwatch` patterns for authority + filtering + limited local responsiveness, but only if a future action mode genuinely needs them

### Highest-signal architectural implications

Without turning this into premature stack selection, the research now gives stronger support for these early concerns:

- `room shell` and `active game instance` should stay conceptually separate
- participant rights should be richer than `host` and `player`
- visibility/publication policy should be explicit
- browser-first modes and action-heavy modes should not be forced through one identical transport/update assumption
- larger participation likely means:
  audience shells, finalists, qualifiers, heats, or splits
  not giant equal-contact rooms

### Strong fit by future mode family

- geography / verdict / strategy / audio ID / some WoW variants:
  strongest fit with browser-first authoritative room/state and audience-shell patterns
- Pit Wall / Bad Wall / Driver Override / sabotage / rumor:
  strongest fit with explicit visibility contracts, role rights, and topology-sensitive small rooms
- racing / predator-hunter / future action branches:
  strongest fit with staged reduction, ghosting, qualifiers, and maybe modest local prediction on top of authority

## What remains uncertain but promising

### Still-promising sources to deepen later

From the source-hunt and second wave, the best follow-up targets remain:

- `Halo 2 LAN Party Online`
  likely highly relevant for local-social -> online-social infrastructure
- deeper `Overwatch Gameplay Architecture and Netcode`
  likely richer than the scripted-abilities slice alone
- the IEEE paper on browser multiplayer with imperfect information
  unusually close to browser hidden-info play
- a focused `Jackbox` second wave
  if we want more concrete host/controller/ops architecture clues

### Important uncertainties still unresolved

- exact browser-appropriate implementations for higher-tempo authoritative action
- the practical ceiling for phone-controller action before local prediction/correction becomes too annoying
- which browser-first room/state frameworks are best fits in practice, as opposed to merely exposing useful mechanisms
- whether any planned action mode actually justifies deeper sync complexity versus a ghosted/no-contact or staged structure
- how much built-in comms/moderation Prix would ever want versus relying on external voice/private-room trust

## Candidate follow-up research questions

1. Which concrete browser-first room/state mechanisms are worth preserving conceptually even if no framework is chosen yet?
2. For hidden-info modes, what is the cleanest way to represent `public`, `role-private`, `moderator-only`, and `revealable-later` data?
3. If a future action mode exists, should the first prototype be:
   ghosted
   lightly authoritative with local self-prediction
   or purely event-shell/qualifier based?
4. What moderation and operator controls are truly necessary for private-room-first play, and which only become necessary with public discovery?
5. Which event-shell mechanisms should Phase 01 planning keep open:
   finalists, heats, parallel rooms, audience shell, or none yet?

## What should and should not influence early architecture decisions

### Should influence early decisions

- the need to separate shell/container concepts from active instances
- the need for explicit role/capability modeling
- the need for explicit visibility-scoped state publication
- the need to avoid assuming one universal room/update model
- the strong evidence that coupling reduction and event structure matter more than headline player-count ambition

### Should not yet overdetermine early decisions

- exact framework or middleware choice
- exact server deployment pattern
- whether built-in voice is needed
- whether any action mode deserves shooter-grade sync sophistication
- whether a public/community shell is strategically worth building soon

The lane supports preserving the right seams. It does not yet justify prematurely hardening one implementation stack.
