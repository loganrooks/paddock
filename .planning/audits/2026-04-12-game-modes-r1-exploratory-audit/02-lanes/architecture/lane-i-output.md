---
date: 2026-04-13
lane: i
lane_name: "Large-room / high-player-count research lane"
delegation_class: initial-architecture-research-planning
output_file: 02-lanes/architecture/lane-i-output.md
task_spec: 02-lanes/architecture/lane-i-task-spec.md
source_artifacts:
  - 02-lanes/architecture/lane-i-a-output.md
  - 02-lanes/architecture/lane-i-b-output.md
  - 02-lanes/architecture/lane-i-c-output.md
tags:
  - exploratory-audit
  - lane-i
  - architecture
  - scaling
  - player-count
  - synthesis
---

# Lane I: Large-Room / High-Player-Count Research

## Lane framing

This lane is intentionally separate from the broader architecture-exposure audit.

It is not trying to answer:

- which game ideas are best overall
- whether every future mode should support `50+` players
- what the final networking stack should be

It is trying to answer:

- what different published high-player-count patterns actually are
- which of those patterns are plausibly relevant to this project
- what early substrate separations would keep those options open later

The three sub-lanes split the problem cleanly:

- `lane-i-a`
  browser-first / audience / submit-and-aggregate scaling
- `lane-i-b`
  real-time action / collision / racing scaling
- `lane-i-c`
  hidden-info / private-room / topology-limited scaling

The most important synthesis result is simple:

- there is no single meaningful `50+ players` target

Different room shapes hit different ceilings for different reasons.

## Why large-room research is a separate question

The mixed architecture lane was trying to do too much at once.

This lane makes the separation explicit:

- `general architectural exposure`
  asks which promising game shapes pressure early substrate decisions
- `large-room / high-player-count research`
  asks what scaling patterns actually exist and what they imply if even some future modes want them

That separation matters because large-room thinking can distort the broader audit if it is not kept in its own lane. A prompt-driven geography event, a hidden-info pit-wall control room, and a collision-heavy racing mode are not all chasing the same scaling problem.

The right question is not:

- how do we make every game support `50+`?

It is:

- which future modes might plausibly want larger participation envelopes
- what kind of scaling envelope would that actually be
- what cheap early seams keep those futures from turning into rewrites

## Reference patterns by scaling shape

### 1. High-fanout browser / audience / submit-and-aggregate

Primary signals from `lane-i-a`:

- large published counts usually mean shared prompt cadence plus lightweight submissions
- audience scale is often much larger than active contestant scale
- event container and active room are often different things

Representative official cases:

- `Jackbox`
  small core players, potentially huge audience
- `Kahoot`
  many equal responders to one timed prompt
- `Mentimeter` / `Slido`
  large-scale poll / Q&A / quiz aggregation
- `GeoGuessr Party / Live Challenge`
  large event shell, only some modes stretching to the full party

What this pattern really is:

- one shared timeline
- small or discrete payloads
- strong host/event authority
- aggregation, sampling, or finalist selection

What large counts mean here:

- not `5,000 equal rich participants`
- but `many people responding to the same staged prompt`

### 2. Real-time action / collision / racing

Primary signals from `lane-i-b`:

- large active rooms scale through sparsity, segmentation, elimination, ghosting, or relevance filtering
- products rarely preserve one giant equally meaningful fully shared contact field
- even when headline counts are high, decisive interaction sets are usually smaller than the room headline implies

Representative official cases:

- `Fortnite`
  large world plus interest management
- `Battlefield 2042`
  mode-specific room sizes rather than one universal cap
- `Fall Guys`
  high-concurrency starts, then shrinking active problem via round design
- `Trackmania`
  divisions, splits, room splits, event-level largeness
- `Rocket Racing`
  small contact races, ghost/time-trial structures for broader comparison
- `iRacing`
  field caps, official splits, relevance filtering

What this pattern really is:

- "large event" often means many shards, heats, divisions, or partially shared relevance zones
- "large room" rarely means fair full-contact everyone-matters-to-everyone simulation

### 3. Hidden-info / private-room / topology-limited

Primary signals from `lane-i-c`:

- hidden-info rooms usually cap because of legibility, moderation, trust, and comms bandwidth before raw transport
- same-room vs private-screen vs moderator-led topology matters more than raw socket count
- audience can scale much farther than active deception or asymmetric-role play

Representative official cases:

- `Among Us`
  moderate room size, private screens, accusation phases, moderation burden
- `Fakin' It` / `Push The Button`
  shared stage plus private phones, small active room, larger audience shell
- `Keep Talking and Nobody Explodes`
  split information with one live actor and expert/support roles
- `Artemis`
  station-based crew play
- `Blood on the Clocktower`
  larger social-deduction groups stabilized by human moderation/storytelling
- `Spaceteam`
  trusted-group voice-heavy coordination

What this pattern really is:

- topology-sensitive multiplayer
- visibility and role rights are central
- active room size is often socially bounded

## What kinds of future F1 modes might plausibly live in each pattern

### Strongest large-room candidates

These fit the high-fanout browser / prompt / aggregate class:

- large-room `circuit / venue guesser`
- race-weekend `Stewards' Room` verdict polls
- `Team Principal's Desk` prediction / confidence / strategy polling variants
- audio ID / commentary ID / crowd-reaction ID
- audience-layer `Words of Wisdom`
- finalist-based `Paddock Fashion` or `Meme Prompts`

The likely shape is:

- one host/event timeline
- browser-first join
- discrete submissions
- leaderboard, aggregate, or finalist reveal

### Medium-room but topology-sensitive candidates

These fit the hidden-info / private-room / comms-sensitive class:

- `Pit Wall`
- `Bad Wall`
- `Driver Override`
- `Split Pit Wall`
- sabotage / rumor / insider-information branches
- hidden-hunter or crash-politics variants

The likely shape is:

- smaller active rooms
- private views and role-specific visibility
- voice or structured comms
- strong private-room posture

### Large-participation action candidates, but only in specific forms

These fit the real-time action class only if the design shape changes:

- non-contact or ghosted circuit sprint / time trial
- elimination-style circuit obstacle / paddock chaos
- large race-weekend event shells with heats or splits
- socially large but mechanically sharded racing events

The likely shape is not:

- `50+` fair-contact F1 car chaos on one track

It is more likely:

- ghosts
- heats
- eliminations
- divisions
- same-track comparison without universal collision relevance

## What does not plausibly scale and should not be forced

- `Words of Wisdom` as `50+` equal authored contestants all hitting the host screen
- free-text or image-heavy UGC modes at large scale without moderation, finalist selection, or sampling
- hidden-info accusation games pushed toward very large active rooms just because transport might allow it
- `50+` fair-contact racing where everyone meaningfully collides with everyone else
- same-house/private-room asymmetric modes forced into generic public-lobby assumptions
- treating a big audience shell as equivalent to a big active game room

The recurring lesson from the references is that many large published counts are achieved by changing the interaction density, not by preserving one small-room fantasy unchanged and scaling it linearly.

## Most important early architectural implications

### 1. Separate `event container`, `room`, and `active game instance`

This is the most important seam.

Why:

- GeoGuessr separates party from specific game lobbies
- Jackbox scales large events by splitting into many smaller tables
- Trackmania and iRacing scale racing events through divisions and splits

What it protects:

- one race-weekend event containing many active rooms
- one watch party containing finalists or heats
- one community shell containing several mode instances

### 2. Model participant roles and capabilities explicitly

At minimum the substrate should not collapse everything into just `host` and `player`.

Likely useful capability sets:

- host
- core player
- audience participant
- spectator
- moderator
- role-specific specialist

Why:

- large audience shells differ from active rooms
- hidden-info modes need role-specific rights
- public-facing or event-facing modes may need moderation and sampling

### 3. Make visibility scopes first-class

Different modes will want:

- fully public prompt state
- private submissions until reveal
- per-role secret information
- audience-visible but player-hidden aggregates
- moderator-only controls

This should be modeled in session/state design, not improvised in UI conditionals.

### 4. Keep `prompt/reveal transport` distinct from `action/simulation transport`

The high-fanout browser cases and the action-heavy cases are fundamentally different.

One lane wants:

- votes
- text
- guesses
- confidence picks
- simple browser payloads

Another lane may eventually want:

- continuous control
- collision authority
- movement relevance
- ghost/replay/state interpolation

If these are fused too early, one side will distort the other.

### 5. Let modes declare their own topology contract

Examples:

- `shared_stage + private handsets`
- `all_private_screens + meeting phases`
- `one actor + experts`
- `ghosted time-trial`
- `elimination heat`
- `small contact race`

This is better than assuming the whole platform has one natural room shape.

### 6. Keep per-mode participation envelopes configurable

The reference set strongly argues against one global player cap.

A better abstraction is:

- each mode declares the kinds of participation it supports
- active-player cap
- audience cap or audience support
- whether sharding/heats/splits are allowed
- whether ghosting/contact rules change the scaling envelope

### 7. Preserve a low-capability browser join path

The large browser/audience cases all benefit from:

- code / QR / link joining
- phone browser participation
- lightweight payloads

This does not mean every future mode must run in a tiny browser capability envelope. It means some of the most plausible large-participation modes probably will.

## Technical pressure points and candidate solutions

This is the layer the first synthesis underplayed.

The architectural question is not just "keep options open." It is:

- what exact technical seams preserve those options?
- what exact shortcuts would prematurely fuse things together?
- what specific early decisions deserve conscious treatment now?

### 1. Session model: stop treating `room` as the only container

Technical problem:

- small private play can get away with `room = everything`
- larger events, heats, audience shells, and hidden-info side roles cannot

If we encode:

- one room
- one active game
- one host
- one participant list

then later support for audience, heats, finalists, or event-wide standings becomes awkward and cross-cutting.

Candidate solution:

Model at least three distinct entities:

- `event_container`
  optional higher-level shell for watch parties, large sessions, race-weekend events, or many-table gatherings
- `room`
  social gathering / join code / invite surface
- `game_instance`
  one running mode or heat with its own state, authority, and lifecycle

Recommended early decision:

- keep these as distinct concepts in the domain model, even if M1 usually maps `one room -> one game instance`

What this prevents:

- needing a rewrite when one event wants multiple heats, finalist rounds, or audience-over-player separation

### 2. Participant model: roles must be capabilities, not one enum

Technical problem:

- active players, spectators, hosts, moderators, audience members, and role-specialists do not all need the same rights
- future hidden-info/control-room modes need more than `host` versus `player`

If we encode:

- `participant.role in {host, player}`

we create a brittle model quickly.

Candidate solution:

Represent participants with composable capabilities such as:

- can_join_private_view
- can_submit_core_actions
- can_vote_as_audience
- can_start_or_advance_round
- can_moderate_or_filter_ugc
- can_view_spectator_overlay

Recommended early decision:

- build participant authorization around capability flags or capability bundles, not one fixed role enum

What this prevents:

- repainting the whole permission model when audience, moderator, or desk-specialist roles arrive

### 3. Visibility model: public state and private state must not be one blob

Technical problem:

- large-room browser modes want public prompts and private pending submissions
- hidden-info modes want per-role secrets
- spectator or streamer views may need more or less than active players

If we encode one shared state tree and hide fields in the client, we create leakage risk and future topology pain.

Candidate solution:

Treat visibility as part of state publication:

- `authoritative_state`
  full canonical state
- `view_projections`
  derived public or role-scoped views
- `private_payloads`
  per-participant or per-role secrets

Recommended early decision:

- modes should publish state through explicit visibility scopes rather than ad hoc UI hiding

What this prevents:

- hybrid/local leaks
- retrofitting hidden-info rules later
- making streamer/spectator views unsafe or awkward

### 4. Authority runner: logical server boundary now, deployment flexibility later

Technical problem:

- browser-first party modes can run with host-browser authority
- online sync, larger rooms, and action modes may later want a dedicated authority runner

If simulation and rendering are fused in one frontend runtime, moving to dedicated authority later becomes a rewrite rather than a deployment change.

Candidate solution:

Create a logical authority module that can run in two environments:

- local-hosted in the host browser for M1-style party play
- dedicated service later for online sync, larger rooms, or more latency-sensitive modes

Recommended early decision:

- keep game rules/state progression in a runtime-neutral module with clear command/state boundaries

What this prevents:

- having to extract "the server" out of UI code after the fact

### 5. Transport split: do not force prompt/reveal and action/simulation through one identical path

Technical problem:

- prompt-driven modes send sparse commands and reveals
- action modes may later need high-frequency control and state sync

If both are forced through one naive channel and one update model, one class will distort the other.

Candidate solution:

Define at least two technical profiles:

- `evented_turn_profile`
  sparse commands, timers, reveals, low-frequency updates
- `realtime_action_profile`
  higher-frequency commands/state, prediction/reconciliation concerns, relevance filtering

Recommended early decision:

- mode manifests should declare transport/authority profile
- the core platform should not assume one tick/update pattern for every mode

What this prevents:

- turning simple browser modes into fake action games
- or trying to bolt real-time action onto an architecture built only for form submissions

### 6. Mode manifest: each mode needs declared topology and scaling envelope

Technical problem:

- right now it is easy to talk about modes abstractly, but the substrate will need machine-readable declarations

Candidate solution:

Each mode should eventually declare something like:

- supported topologies
  `host_screen_plus_phones`, `all_private_screens`, `hybrid`, `same_house_split_rooms`
- active-player envelope
  `min`, `max`, `recommended`
- audience support
  yes/no and maybe limits
- authority profile
  `local_hosted`, `dedicated_ok`, `moderator_led`, etc.
- visibility profile
  `fully_public`, `private_submissions`, `per_role_secrets`
- scaling strategy
  `single_room`, `heats`, `splits`, `finalists`, `ghosted`, `audience_layer`

Recommended early decision:

- do not hardcode these assumptions in room logic; keep space for mode-declared constraints

What this prevents:

- one implicit room model silently becoming the platform law

### 7. Event log and score routing: large participation often becomes many smaller results feeding one shell

Technical problem:

- heats, finalists, race-weekend events, and cross-room standings all require score/result routing across more than one live instance

Candidate solution:

Introduce a normalized event/result log:

- commands in
- state transitions
- scored outcomes
- advancement records

Recommended early decision:

- keep scoring and progression outputs explicit rather than burying them inside view components or one-off mode code

What this prevents:

- difficulty stitching together heats, brackets, finalist selection, or event-wide leaderboards later

### 8. Join and identity model: separate presence from persistence

Technical problem:

- M1 can work with lightweight guest participation
- larger events or future competitive/team shells may need stronger identity and rejoin semantics

Candidate solution:

Treat identity in grades:

- ephemeral guest
- claimable lightweight profile
- persistent competitive identity

And keep join semantics explicit:

- invited participant
- room-code joiner
- audience-only joiner
- reconnecting participant

Recommended early decision:

- do not assume every participant is either anonymous forever or fully registered from day one

What this prevents:

- awkward migrations when standings, teams, or event histories need more stable identity

## Concrete early decisions to make soon

These are the highest-signal technical decisions this lane is actually exposing.

### Decision 1: Domain model separation

Make a conscious decision on whether the platform core distinguishes:

- `event_container`
- `room`
- `game_instance`
- `participant`
- `seat/role/capability`

My read:

- yes, at least logically
- even if M1 UI often collapses them for simplicity

### Decision 2: Runtime-neutral authority module

Make a conscious decision on whether game progression logic lives in:

- UI/client code tightly coupled to presentation
- or a runtime-neutral authority module that can run locally first and remotely later

My read:

- preserve the authority module boundary now
- do not overbuild deployment/infrastructure yet

### Decision 3: Visibility-scoped publication

Make a conscious decision on whether hidden/private information is handled by:

- client-side hiding on a shared state blob
- or explicit server/authority-side view projection

My read:

- explicit view projection is the safer long-term seam

### Decision 4: Multiple transport profiles

Make a conscious decision on whether the core platform assumes:

- one messaging/update pattern for every mode
- or mode-declared transport/authority profiles

My read:

- allow at least `evented_turn` versus `realtime_action`

### Decision 5: Audience as first-class or afterthought

Make a conscious decision on whether:

- audience/spectator is a hacked-on view-only state
- or a first-class participant type with separate rights/capabilities

My read:

- audience should be first-class because it matters both for large-room browser futures and for streamer/watch-party modes

### Decision 6: Heat/split/finalist support

Make a conscious decision on whether:

- every "large" mode must still be one active room
- or the platform core should conceptually allow many subinstances feeding one event shell

My read:

- preserve the concept now, even if no M1 mode uses it fully

## Technical shortcuts most likely to cause foreclosure

- fusing simulation/state progression into the host screen's rendering code
- making `room` the only real multiplayer container
- assuming one flat participant role model
- publishing one shared state object to every client and hiding secrets in UI only
- assuming every mode has one active instance and one host
- making scoring/results purely presentation-layer concerns instead of explicit outputs
- assuming all multiplayer is either tiny private play or giant public play, with no middle topologies

## Cheap early protections vs premature overengineering

### Cheap early protections

- separate event/container identity from active game-instance identity
- separate roles/capabilities from one flat participant model
- model visibility scopes explicitly
- keep prompt/reveal transport separate from action/simulation transport
- allow per-mode topology and cap declarations
- support audience as a distinct participation class
- keep join/rejoin/lock/invite abstractions clean
- preserve a path for heats, splits, finalists, and sharded subrooms
- avoid coupling session authority to one specific presentation topology

### Premature overengineering

- building `100`-player action netcode now
- designing for `5,000`-person live events in M1
- implementing public matchmaking and moderation infrastructure now
- assuming native voice must exist early
- solving server-region and action fairness at MMO scale before any chosen mode needs it
- designing every current idea as if it must one day become a huge-room mode

The right stance is not "optimize for massive rooms now." It is "avoid cheap early choices that would make the plausible larger-room branches painful later."

## What should feed later architecture deliberation

### Immediate carry-forward into architecture discussion

- authored prompt/reveal modes and action/simulation modes should not be assumed to share the same substrate seam
- room authority, visibility, and presentation topology should remain separable
- large audience participation and large active-room participation are different futures
- racing-like scale likely wants ghosts, heats, splits, elimination, or sharding rather than giant fair-contact rooms

### Good follow-on questions later

- which one or two promising F1 modes are the best concrete testbeds for the browser/audience pattern?
- which hidden-info / control-room mode should define the first serious visibility/topology contract?
- does the product want to preserve only `20-50` event-shell possibilities, or does it really care about `100+` browser-event participation?
- does any action-family mode actually deserve early prototyping in a ghosted / time-trial / elimination form?

### What this lane does not settle

- whether large-room modes are strategically important enough to build soon
- which exact backend/services stack to use
- whether the product should remain private-room first indefinitely
- whether any specific future F1 action mode is worth building

It only sharpens the architectural question:

- if later we want broader participation, what kind of broader participation is it actually?

The answer is not one number. It is a small set of very different scaling patterns.
