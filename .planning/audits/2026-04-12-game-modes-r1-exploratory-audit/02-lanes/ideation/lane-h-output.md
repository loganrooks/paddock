# Lane H Output - Architecture-Pressure Lane

## Lane framing

This lane is not asking for a final stack decision or a generic scalability memo. It is asking which game shapes create real early architectural pressure, which pressures are still speculative noise, and which early shortcuts would quietly close doors.

The important correction from the source set is that "scale" is not one number:

- network scale
- room/session scale
- reveal scale
- spectator scale
- social-legibility scale

Those scales diverge sharply across the current and plausible portfolio.

- `prix-guesser` geography, `Words of Wisdom`, `Paddock Fashion`, `Meme Prompts`, and verdict/strategy rounds are mostly parallel submit-and-aggregate systems
- predator-hunter racing is a real-time collision/survival system
- `Pit Wall` / `Driver Override` / broader control-room ideas are asymmetric authority-and-visibility systems
- race-weekend events, ranked/team layers, and community packs create event scale and identity scale more than one giant synchronous room

This lane also carries forward the methodological warning from Round 1 and Round 2 prompts: do not flatten everything into one room shape, one ontology, or one "proper" display model.

The most load-bearing architectural pressure is not "can we one day run 50 sockets." It is whether session authority, role visibility, and display topology are modeled as separate concerns rather than fused into one host-screen party-room assumption.

## Why architecture needs to come forward here

Architecture needs to come forward because several promising families already want materially different session shapes:

- geography and `Words of Wisdom` can live comfortably in a host-screen + phones local form, but also have credible online-sync, async, and race-weekend event derivatives
- `Paddock Fashion` and `Meme Prompts` can absorb many parallel submissions, but their reveal grammar collapses if the architecture assumes every submission gets equal stage time in one linear room reveal
- predator-hunter racing wants a small active simulation, strong spectator readability, and maybe large audience or playlist value, but not necessarily large active-player rooms
- control-room / driver-vs-wall territory pressures hidden information, contested authority, same-house-different-rooms local play, and private online sync much harder than the current local-party anchor
- future ranked, team, or calendar layers mostly pressure identity, score routing, event containers, and many-instance coordination rather than one huge live room

If M1 hardcodes:

- one host role
- one active mode per room forever
- one shared truth rendered everywhere
- one display topology
- one networking profile

then M2/M3 stops being extension and becomes re-architecture.

The early job is therefore not to build everything now. It is to preserve the right seams.

## Player-count classes and what fits them

| Class | Natural game structures | Current or plausible modes | What breaks first | Architecture read |
| --- | --- | --- | --- | --- |
| `2-8` | couch play, private online sync, hybrid friend groups, hot-seat asymmetric play | geography, `Words of Wisdom`, `Paddock Fashion`, `The Stewards' Room`, `Team Principal's Desk`, `Pit Stop Co-op`, `Grid Walk`, predator-hunter racing | usually not raw network throughput; it is visibility assumptions, host flow, and role legibility | This is the M1 comfort zone, but it still already needs room/role/view separation if hidden info and hybrid remain live |
| `8-20` | larger party rooms, streamer lobbies, online friend groups, wider submit-and-aggregate rounds | geography events, `Words of Wisdom`, fashion showdown rounds, `Meme Prompts`, verdict theater, some hidden-hunter racing variants | reveal UX, social readability, join flow, moderation of chaos, authority over pacing | Many modes can technically accept this count, but the reveal layer usually breaks before the transport layer |
| `20-50` | eventized parallel participation, heats, audience-assisted play, multi-crew/team structures | race-weekend geography challenges, `Words of Wisdom`/fashion heats, large verdict polls, streamer control-room nights, team competitions with shared event windows | aggregation, spotlight selection, room authority, identity integrity, collision complexity if real-time action is shared | This band is real for some modes, but it usually wants phased structure, not one flat room |
| `50+` | async/public event participation, many small rooms tied to one event, audience scale, season/team contribution scale | calendar events, leaderboards, community packs, audience-mediated control-room or streamer formats, large team/career structures | for real-time collision: networking/simulation; for submit-and-aggregate: reveal and moderation; for team/event scale: identity, routing, trust, standings | `50+` is serious pressure, but mostly as event scale, audience scale, or distributed session scale rather than one shared live party room |

Specific read by class:

- `2-8` is where asymmetric authority games are strongest. Control-room families, same-house-different-rooms play, and hidden-role racing all feel designed for this band.
- `8-20` is where host-screen spectacle starts competing with fairness and pacing. A room can still feel like one room, but only if reveals are compressed and role complexity stays readable.
- `20-50` is where "everyone submits, then we curate or bracket" becomes a design necessity, not a nice-to-have.
- `50+` is only natural for a subset of futures. It is credible for events, audiences, prediction layers, team accumulation, or multi-heat competition. It is not a default target for every mode, and especially not for F1-like collision racing.

## Current and plausible future game shapes that pressure scale

### Parallel submit-and-aggregate games

Examples:

- geography
- `Words of Wisdom`
- `Paddock Fashion`
- `Meme Prompts`
- `The Stewards' Room`
- `Team Principal's Desk` when played as simultaneous judgment rather than live comms

These are the strongest candidates for `8-20`, `20-50`, and some `50+` event derivatives because the action is mostly parallel. But their scaling ceiling is determined by reveal and curation, not by submission throughput.

What they pressure:

- flexible submission windows
- aggregation logic
- staged reveal formats
- score routing
- spectator-facing summary views

What they do not justify on their own:

- heavy real-time simulation infrastructure

### Real-time collision / racing / survival games

Examples:

- `The Verstappen Game`
- `Talibantonelli / Osama bin Russell`
- any future car-combat or chase branch

These are the strongest pressure on simulation authority, latency tolerance, collision/event logging, and spectator readability. They are not strong evidence that the platform should optimize for `50+` active shared simulation. Their plausible path is:

- small active rooms
- richer spectator modes
- challenge playlists
- circuit packs
- tournament brackets or many parallel heats

not one giant F1-like melee by default.

### Asymmetric hot-seat + support / control-room games

Examples:

- `Pit Wall`
- `Driver Override`
- `Bad Wall`
- broader control-room terrain from Lane G and G2
- some `Grid Walk` realizations

This family pressures the session model hardest because it wants:

- one room with multiple authority centers
- genuinely private information
- sometimes physically separated local players
- private online sync as a first-class form, not a degraded fallback
- spectator readability without leaking every private desk

This is where room authority and visibility abstractions become clearly load-bearing.

### Spectator-heavy or audience-mediated games

Examples:

- streamer control-room formats
- eliminated-player powers in predator-hunter games
- fashion commentary overlays
- public voting on a narrowed finalist set
- pundit/race-control style participation

These modes may have only `2-8` active players and still pressure architecture more than a nominally bigger room because spectators are not just passive viewers. They may:

- vote
- inject chaos
- act as pundits
- supply rumor/noise
- trigger interventions

That is spectator scale, not active-player scale.

### Tournament / heat / bracket / phased-reveal games

Examples:

- fashion tournaments
- `Words of Wisdom` event nights
- race-weekend geography competitions
- team qualifiers feeding finals

This family matters because it is the cleanest way to make `20-50` and `50+` feel good without pretending one room can meaningfully present everything. It pressures:

- sub-room support
- round-to-round score routing
- bracket/heat structure
- finalist spotlighting
- event containers larger than one room

## Room / session / authority implications

The sources point toward four distinct things that should not be conflated:

- `room`: the social container or gathering
- `game instance`: one running mode or round sequence
- `authority`: who can advance or decide authoritative state
- `participant role`: player, host, spectator, hidden specialist, team desk, audience member

If those collapse into one "host starts a room and everyone else joins phones," several futures become awkward immediately.

### What gets pressured

#### Host assumptions

The host may be:

- a non-player emcee on the couch
- a player who also controls flow
- a rotating hot seat
- a shared set of capabilities across multiple people
- the platform itself for async/event/ranked flows

An architecture that treats `host` as a singular person-shaped role rather than a capability bundle will fight the portfolio.

#### Authority assumptions

Authority is not the same as presentation.

- in local M1, the host browser may run the authoritative state
- in online sync, a dedicated service may need to do that
- in control-room games, the driver may hold one kind of final authority while the wall holds another
- in hidden-hunter racing, role assignment and reveal rights become separate from movement authority

The early requirement is a logical authority boundary, not necessarily cloud deployment on day one.

#### Session shape assumptions

Some futures want:

- one active mode in one room
- background prediction or side-bet layers
- heats/finals under one event
- recurring group history outside one session
- many rooms contributing to one calendar event

M1 can still run one active instance at a time. The important point is to avoid modeling "game night" as the only meaningful container.

#### Identity assumptions

Large-player and later competitive futures mostly pressure identity and trust:

- ephemeral couch identities are fine for M1 moment-to-moment play
- event, team, and ranked layers need identities that can persist, upgrade, and carry score/event history
- spectators and audience participants may need lighter-weight identity than active players

This suggests identity grades, not one all-or-nothing account model.

### What should remain flexible early

- singular versus rotating host
- local-hosted versus dedicated authority runner
- player versus spectator versus hidden-specialist entry paths
- one-room play versus event-with-many-subinstances
- ephemeral identity versus claimable persistent identity

## Display / hidden-info / input implications

The display model cannot be treated as one universal host-screen truth.

### Shared spectacle + private inputs

Best fit for:

- geography
- `Words of Wisdom`
- `Paddock Fashion`
- `Meme Prompts`
- verdict/strategy rounds
- some local racing forms

This is still the M1 anchor. But even here, the host screen and phone screens are not just mirrors. They are different views of the same state.

### Full private-screen play

Best fit for:

- online-sync geography
- online-sync `Words of Wisdom`
- `Grid Walk`
- control-room families
- racing and predator-hunter branches

These forms need each player to have a complete, playable screen, not just a controller surface.

### Sanitized host screen + richer private views

This is the hidden-info pressure case.

Examples:

- hidden hunters in racing
- `Words of Wisdom` ownership/voting secrecy
- `Grid Walk` information splits
- control-room/private desk systems
- hybrid local+remote forms where the shared display must not leak role-specific truths

This means the host screen may sometimes show less than some players know. In other cases it may show more than any one player knows because it is a broadcast layer. Both must be possible.

### Unconventional local separation

Lane G and G2 matter here because they show local forms that are not just "everyone in front of the TV":

- same house, different rooms
- phone-call cockpit
- one hidden specialist
- rotating hot seat with local spectators

If the platform treats local play as physically co-present and mutually visible by default, these forms get accidentally designed out.

### Input implications

The portfolio already wants incompatible input surfaces:

- map pan/zoom/pin
- text entry
- drawing canvas
- verdict sliders and selectors
- restricted radio tokens
- virtual joystick or tilt steering
- keyboard/gamepad/touch equivalents online

The architecture should translate devices into game actions and role-specific UI surfaces. It should not assume one reusable phone controller is enough.

## Networking / simulation / transport implications

The portfolio needs transport classes, not one universal networking assumption.

### Event-driven / turn-based transport

Best fit for:

- geography
- `Words of Wisdom`
- `Paddock Fashion`
- `Meme Prompts`
- `The Stewards' Room`
- many `Team Principal's Desk` variants

Needs:

- durable submissions
- timers
- ordering
- reconnection handling
- aggregation

This is the least risky M1 networking profile.

### Low-latency asymmetric coordination

Best fit for:

- `Grid Walk`
- control-room families
- some `Pit Stop Co-op` variants

Needs:

- targeted role messages
- synchronized clocks and countdowns
- fast enough feedback to preserve trust under pressure
- voice-or-token adjacency if those forms survive

This is not racing-grade netcode, but it is more demanding than ordinary submit-and-reveal play.

### Real-time simulation transport

Best fit for:

- predator-hunter racing
- any future driving or collision-heavy mode

Needs:

- separate simulation authority
- higher update cadence
- collision/event logging
- client prediction or equivalent responsiveness strategy if online
- possible interest management if counts rise

The key architectural seam is logical separation between simulation and presentation so the same game logic is not trapped inside a host-only render loop.

### Large-player event transport

For many `20-50` and `50+` futures, the right answer is not one giant real-time room. It is:

- many smaller instances
- shared score/event ingestion
- event windows
- leaderboards
- audience channels

That is a different scaling problem than racing netcode.

### Important distinction

`50+` active racers and `5` active players plus `500` spectators are not the same transport problem. The latter is much more plausible earlier if spectator channels are read-only or low-interaction.

## Reveal UX / aggregation / spectator implications

Reveal is where many plausible futures really break.

### Geography

Scales better than most because the shared map can aggregate many guesses at once. Even so, large counts want:

- clustered guess maps
- percentile or nearest-callouts
- spotlighted outliers
- maybe heat/final structure for event play

### Words of Wisdom and Meme Prompts

These can collect many answers, but they cannot reveal `30` or `50` answers linearly without killing energy. Large-player versions need:

- curation
- seeded finalists
- vote-based advancement
- top-N surfacing

### Paddock Fashion

This is the clearest reveal-scaling failure case. Submission can scale. Catwalk attention cannot. Any `20+` or `50+` future for fashion needs:

- heats
- categories
- finalists
- commentary layers
- maybe team judging rather than full-room equal-stage reveals

### Stewards' Room and strategy/judgment games

These scale best through distribution views:

- split vote histograms
- confident outlier callouts
- who matched the real call
- team-versus-team summary

They do not need every individual judgment narrated in equal depth.

### Racing / predator-hunter

These reveal through live spectacle:

- position and threat readability
- crash replays
- elimination state
- hunter reveals
- spectator powers

Their spectator problem is different: the room must understand what is happening fast enough, and eliminated players should not become dead weight.

### Control-room families

These are watchable only if the host/broadcast layer exposes the shared crisis while preserving enough private desk logic to make disagreement meaningful. Too much privacy makes it opaque. Too much leakage makes the whole mechanic collapse.

This is why spectator scale and hidden-info scale must be treated together.

## Foreclosure risks and cheap early protections

| Pressure | Early shortcut that forecloses later | Cheap early protection | Likely overengineering right now |
| --- | --- | --- | --- |
| Room authority | make the host UI the only place authoritative state can live | define a logical authority runner separate from UI even if it executes in the host browser in M1 | building dedicated fleet/server orchestration before any mode needs it |
| Room/session model | equate room with one active game on one display | separate `room`, `game instance`, and future `event` as concepts | full multi-instance festival scheduler in M1 |
| Visibility | assume one shared truth is renderable on every screen | make per-view visibility a first-class concern in mode/view config | a giant generic permissions DSL for every byte of state |
| Display topology | hardcode "TV plus phone controller" as the only local shape | let modes declare supported topologies: host-screen + phones, private screens, hybrid, unconventional local | perfect support for every topology in M1 |
| Player counts | pick one global min/max player rule | let each mode declare `min`, `max`, `recommended`, and maybe `tested` ranges | a universal scaling promise across the platform |
| Transport | assume one WebSocket/event profile fits all modes | tag modes with transport classes: submit-and-aggregate, low-latency coordination, real-time simulation | racing-grade netcode for non-racing modes |
| Reveal | assume one round equals one linear reveal of every player output | support reveal stages, aggregation summaries, and future heat/final structures in the content/session model | full tournament engine before any eventized mode is chosen |
| Spectators | model all non-players as passive viewers or ignore them entirely | keep spectator as a first-class participant type and reserve a read-only or light-action channel | full Twitch-scale audience product |
| Scores and history | treat results as ephemeral session UI only | emit structured event and score outputs from modes even if M1 uses them lightly | final ranked/MMR system and full league math now |
| Identity | force full accounts or fully ephemeral nametags with no upgrade path | keep anonymous/ephemeral identities claimable later and tie scores/events to stable internal ids | shipping full social graph/friends/matchmaking early |

The common pattern is cheap separation now, not maximal infrastructure now.

## Most important implications for early planning

### 1. Define the core platform abstractions before Phase 01 hardens around one room shape

At minimum, early planning should explicitly define:

- room
- game instance
- event container
- participant
- role
- authority runner
- screen/view
- score/event output

Without this, the authored-round contract risks inheriting accidental party-room assumptions.

### 2. Treat mode declarations as architecture inputs, not just product metadata

Each mode should eventually declare at least:

- player-count band
- supported display topologies
- visibility/asymmetry profile
- transport class
- reveal class
- spectator role, if any

This is more useful early than arguing about a final tech stack.

### 3. Keep the authored-round substrate important, but do not pretend it is the whole platform

The round/content contract is still critical for geography, `Words of Wisdom`, fashion, and other authored modes. But some promising families are not primarily authored-round systems:

- predator-hunter racing
- control-room crisis play
- some co-op asymmetry branches

Those families may share identity, events, content packs, score outputs, and spectator systems without sharing the same round grammar.

### 4. Treat `50+` as selective, not universal

The platform should preserve the possibility of `50+`, but mostly in these forms:

- async/public event participation
- many-room competition
- audience or spectator scale
- team/season contribution scale

It should not distort the whole early architecture around the assumption that every mode wants a `50+` synchronous room.

### 5. The room/authority model matters more early than the frontend stack

The source set is consistent here. The most load-bearing early decision is whether game/session authority, role visibility, and presentation topology are separable. If yes, local host-screen play, private online sync, hybrid, hidden specialists, and future dedicated authority runners can all stay open. If not, several strong branches become rewrites later.

### 6. Document architectural watchpoints now

Watchpoints worth carrying into near-term planning:

- one-active-mode assumption
- hidden-info leakage through the host screen
- spectator role absence
- identity upgrade path
- event-scale versus room-scale confusion
- reveal grammar for `20+`
- simulation/presentation coupling in real-time modes

## What should feed into Round 2 and later architecture deliberation

Round 2 and later architecture work should pressure-test these questions directly:

### Which game families truly deserve `20-50` or `50+` active participation?

Likely yes:

- geography event play
- some `Words of Wisdom` / fashion / meme-prompt derivatives if they become heat-based or finalist-based
- calendar events, prediction, team accumulation

Likely no, or only through heats/spectators:

- F1-like collision racing
- dense hidden-role driving rooms
- control-room hot-seat formats

### Which control-room branch is the real architecture pressure case?

Lane G, G2, and F2 suggest this family is not one pitch. Architecture needs to know whether the strongest branch is:

- serious driver-versus-wall authority conflict
- chaos-comedy dysfunction with private desks
- same-house-different-rooms asymmetric local play
- streamer/audience-assisted control booth

Those branches all pressure room, visibility, and spectator abstractions differently.

### What is the acceptable hidden-info model for host-screen-first play?

This needs explicit deliberation:

- when should the host screen know less than players?
- when can it know more as a broadcast layer?
- how much asymmetry can local couch play tolerate before physical leakage defeats the mode?

### What should event scale look like if race-weekend and team futures survive?

Questions:

- one room per event, or many rooms feeding one event leaderboard?
- what is the minimum identity model needed for that?
- which score outputs must be structured from the start?

### Which unconventional local forms are important enough to preserve?

If "same house, different rooms," hidden specialists, or phone-call cockpit are meaningful futures, they should be named now as architecture preservation targets rather than rediscovered after local-only assumptions harden.

### Which architecture spikes are worth doing later?

Not now, but worth later targeted spikes:

- authority runner deployable locally and remotely
- per-view visibility in one asymmetric prototype
- `20+` reveal format prototype for a submit-and-aggregate game
- one small real-time action prototype to measure what "small active rooms" really means

The main conclusion for later deliberation is simple: the platform should stay biased toward small private rooms in product posture, but its architecture should not confuse that product posture with a permanent limit on room shape, authority shape, or scale shape.
