---
date: 2026-04-13
lane: j-b
lane_name: "Real-time action / racing systems engineering exposure"
orientation: exploratory
delegation_class: initial-architecture-research-planning
---

# Lane J-B: Real-Time Action / Racing Systems Engineering Exposure

## Lane framing

This lane was run as an engineering-exposure pass, not a headline-player-count pass.

The strongest material in this source set came from:

- official Unreal Engine networking documentation that explicitly references `Fortnite Battle Royale`
- official Trackmania documentation describing room splitting, qualifiers, divisions, and knockout structure
- official iRacing sporting-code and support documentation describing field-size policy, splits, ghost participation, and heat structures

The weaker material came from:

- official Battlefield 2042 briefings, which expose topology and pacing decisions but not low-level netcode
- official Fall Guys updates, which expose room-size and cadence tradeoffs but not transport/replication internals

The main high-confidence pattern across this lane is not "big rooms solved by one magic stack."

It is:

- large shared spaces use relevance filtering, prioritization, dormancy, or mode-specific layouts
- large racing/event participation is often stabilized by qualifiers, splits, heats, or ghost/no-contact participation
- official public sources are much better at exposing topology and competition-shape decisions than they are at exposing the underlying netcode details

## Reference cases and source audit

| Reference case | Source class | Reliability | What the source actually exposes | What it does not expose | Direct vs inferred |
| --- | --- | --- | --- | --- | --- |
| Unreal / Fortnite Battle Royale | Official engine docs | High | `Replication Graph` exists to reduce per-actor/per-client work; Epic says Fortnite BR starts with `100 connected players` and about `50,000 replicated Actors`; official docs also expose filtering, prioritization, relevancy, dormancy, delta serialization, and per-connection replication flow | Fortnite's exact game-specific heuristics, exact bandwidth budgets, exact battle-royale collision/physics architecture | The `100 players / ~50k actors` RepGraph claim is direct. Using the surrounding UE docs as likely mechanism families for Fortnite is partly inference, though very well-supported inference. |
| Trackmania | Official product/docs | High for product topology, Medium for engine internals | `Cup of the Day` uses a `15-minute` qualification phase, then places players into `similarly skilled` divisions with `max. 64 players per division`; knockout eliminates `4 / 2 / 1` players per round depending on remaining field; club rooms can set `1-100` max players per server and optionally enable `scalable room` splitting; competitions auto-create qualifier servers based on registrations vs per-server max | Low-level transport model, rollback/prediction details, collision/netcode internals | Divisioning, auto-server creation, and knockout structure are direct. Any claim about why the underlying networking works at scale is inference because Ubisoft does not expose those internals here. |
| iRacing | Official sporting code and support docs | High for operational rules, Medium for engine internals | Field size is set per ranked race to ensure `safe, fun, and competitive racing`; overflow registrations are split into separate fields racing simultaneously; splits are based primarily on `iRating`; ghost racing lets a player join a populated live session while being invisible and non-colliding but still experiencing draft and track conditions; hosted heat-race presets show how larger entry pools are reduced into smaller feature fields | Low-level replication, latency compensation, physics/netcode architecture | Splits, ghost racing, and heat structures are direct. Using them as engineering precedents for reducing contact density is inference, but strongly grounded. |
| Battlefield 2042 | Official product/dev briefings | Medium | Large matches are shaped with `Clustering`, `Sectors`, different map layouts, AI server fill, and mode-specific player counts; EA later says it moved Breakthrough to `64 players` because it played more tactically and gave more focused frontlines, with less chaotic resistance on the flanks; future maps were planned smaller with fewer sectors/capture points | Frostbite replication details, interest-management internals, exact CPU/bandwidth constraints | Sectors, layouts, AI fill, and the 128-to-64 mode retreat are direct. Any claim about exact engine pressure is inference. |
| Fall Guys | Official update posts | Medium-low | The team reduced Solos/Main Show lobby size from `60` to `40` for faster matchmaking and `more optimised performance`; later `Knockout` was reframed as `32 players, 3 rounds`; `Explore` is a `10 player` mode where players can move on without waiting for everyone else | Netcode, state sync, collision budgeting, server architecture | The room-size and cadence choices are direct. Any deeper technical reading is weak inference only. |

### Official sources used

- Epic Games, `Replication Graph` docs: https://dev.epicgames.com/documentation/en-us/unreal-engine/replication-graph?application_version=4.27
- Epic Games, `Introduction to Iris`: https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-iris-in-unreal-engine?application_version=5.6
- Epic Games, `Actor Priority`: https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-priority-in-unreal-engine
- Epic Games, `Actor Relevancy`: https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine
- Epic Games, `Detailed Actor Replication Flow`: https://dev.epicgames.com/documentation/en-us/unreal-engine/detailed-actor-replication-flow-in-unreal-engine
- Epic Games, `FFastArraySerializer::FastArrayDeltaSerialize`: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/NetCore/Net/Serialization/FFastArraySerializer/FastArrayDeltaSe-
- Epic Games, `AActor::FlushNetDormancy`: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/FlushNetDormancy
- Trackmania docs, `Cup of the Day`: https://doc.trackmania.com/play/how-to-play-cotd/
- Trackmania docs, `Room`: https://doc.trackmania.com/club/activities/room/
- Trackmania docs, `Adding a qualifier`: https://doc.trackmania.com/club/competition-tool/create-competition/qualifier/
- Trackmania docs, `Ranked 2v2`: https://doc.trackmania.com/play/what-is-ranked-2v2/
- Trackmania docs, `Watching replays`: https://doc.trackmania.com/play/watch-replays/
- Trackmania docs, `VIP keys`: https://doc.trackmania.com/play/vip-keys/
- iRacing Official Sporting Code, version dated March 10, 2026: https://ir-core-sites.iracing.com/members/pdfs/20260310-official_sporting_code_dated_Mar_10_2026.pdf
- iRacing support, `Why are there Race Splits?`: https://support.iracing.com/support/solutions/articles/31000133457-why-are-there-race-splits-
- iRacing support, `Ghost Racing`: https://support.iracing.com/support/solutions/articles/31000133497-ghost-racing
- iRacing support, `Setting up Heat races`: https://support.iracing.com/support/solutions/articles/31000152676-setting-up-heat-races
- EA, `Battlefield Briefing: Welcome to 2042`: https://www.ea.com/en-gb/games/battlefield/battlefield-2042/news/battlefield-briefing-welcome-to-2042
- EA, `Battlefield Briefing: Answering Your Reveal Questions`: https://www.ea.com/en-gb/games/battlefield/battlefield-2042/news/battlefield-briefing-answering-your-reveal-questions
- EA, `Battlefield Core Feedback Maps Kick-Off`: https://www.ea.com/en-gb/games/battlefield/battlefield-2042/community/battlefield-core-feedback-maps-kick-off
- EA, `Battlefield Briefing -- Development Update, May 2022`: https://www.ea.com/en-gb/games/battlefield/battlefield-2042/news/battlefield-briefing-development-update-may-2022
- Fall Guys, `Creative, faster matchmaking, and an update about Seasons`: https://www.fallguys.com/en-US/news/fall-guys-creative-faster-matchmaking-and-an-update-about-seasons-are-all-incoming
- Fall Guys, `The Fall Forever Update`: https://www.fallguys.com/en-US/news/fall-forever-update
- Epic Games support, `Why are Rocket Racing, Ballistic, and Festival Battle Stage being removed from Fortnite?`: https://www.epicgames.com/help/c-202300000001637/c-202300000001726/rocket-racing-fortnite-a202300000083621

## Concrete engineering mechanisms exposed

### 1. Per-connection relevance, prioritization, and dormancy in Unreal/Fortnite-adjacent material

Direct evidence from Epic's docs:

- `Replication Graph` was introduced to avoid evaluating every actor for every client every frame; Epic describes it as a persistent graph of nodes that shares work across frames and clients.
- Epic explicitly cites `Fortnite Battle Royale` as a case starting with `100 connected players` and about `50,000 replicated Actors`.
- `Iris` keeps a quantized copy of replicated state, performs filtering and prioritization, serializes for transport, and is designed to share work between connections and parallelize more cleanly.
- Unreal's actor-priority docs describe saturation handling as load-balancing: actors get numerical priority and replication order depends on priority, distance, time since last replication, and viewer context.
- Unreal's actor-relevancy/dormancy docs expose standard tools for culling objects from replication and waking them only when needed.
- `FastArrayDeltaSerialize` exposes an explicit CPU/bandwidth tradeoff: one official path is described as less CPU-intensive but more bandwidth-hungry.

Why this matters:

- This is the cleanest public engineering exposure in the lane for "big active session, but not all state is equally important to every client."
- The relevant mechanism is not "support N players."
- The relevant mechanism is "treat replication as filtered, prioritized, and connection-specific work."

High-confidence inference:

- Any future Prix Guesser real-time action mode that puts many moving entities on a shared map will need some version of this thinking even if the implementation stack is much simpler than Unreal.
- The substrate seam to preserve is likely not `UE-style replication` specifically, but `per-connection visibility + priority + wake/sleep semantics`.

### 2. Qualification, divisional splitting, and elimination rather than one giant contact field

Direct evidence from Trackmania:

- `Cup of the Day` runs a qualification phase, then places players into divisions of similar skill with `max. 64 players per division`.
- The knockout phase removes multiple players per round: `4` at high remaining counts, then `2`, then `1`.
- Trackmania rooms allow a configurable `max players per server` from `1-100` and a `scalable room` option that splits servers as the room approaches the cap.
- Trackmania competition tooling auto-creates qualifier servers according to registrations relative to the configured per-server max.

Direct evidence from iRacing:

- Ranked-race field size is not universal; it is chosen per race to keep racing `safe, fun, and competitive`.
- When too many drivers register, the race is instantiated and entrants are split into separate fields racing at the same time.
- iRacing heat-race presets show explicit staged funnels such as `50 entries -> 5 heats -> consolations -> 23-car A Main`, or `60 entries -> 6 heats -> D/C/B mains -> 24-car A Main`.

Why this matters:

- This is a strong precedent that "big event" and "big single decisive contact session" are different things.
- The exposed mechanism is staged reduction:
  qualification -> split -> heat/knockout -> smaller decisive field

High-confidence inference:

- For any F1-adjacent action mode with more than a small private-room field, staged reduction is a much more evidence-backed route than trying to preserve one giant all-contact race.

### 3. Ghosting / no-contact participation as a first-class stability tool

Direct evidence from iRacing:

- `Ghost Racing` lets a user enter a populated live race or practice session as a spectator-driver who is invisible to other drivers and cannot make contact.
- The ghost still experiences draft and track-condition effects.

Direct evidence from Trackmania's ecosystem:

- Official docs expose broad ghost/replay/leaderboard-ghost usage, including VIP ghosts and leaderboard ghosts.
- This is not the same as live shared-contact racing, but it is a direct product pattern where meaningful comparison and learning happen without collision coupling.

Why this matters:

- This is the clearest racing precedent in the lane for keeping many people "in the same event" without forcing a shared collision budget.
- It also cleanly separates:
  shared timing context
  shared environmental state
  no player-to-player contact consequences

High-confidence inference:

- If Prix Guesser ever explores circuit sprint, kart-chaos, or venue-run modes, a ghosted or semi-ghosted format is much more supported by the evidence than "large shared collision chaos."

### 4. Geometry and mode layout as scaling tools, not just aesthetic choices

Direct evidence from Battlefield 2042:

- `Clustering` and `Sectors` were introduced to create deliberate activity zones and to preserve focused combat within larger maps.
- Different game modes use different areas of the same large maps.
- Battlefield Portal explicitly supports small, medium, and large layouts from the same map set, with `recommended maximum of 64 players` for medium maps and `up to 128 players` for large maps.

Why this matters:

- The exposed mechanism is not only network-facing.
- It is also spatial and rules-facing: choose the amount of playspace, number of objective zones, and number of simultaneous fronts to control what "large player count" even means.

High-confidence inference:

- A future F1 action mode probably should not define "mode" independently from:
  active area
  number of simultaneous fronts
  contact policy
  spectator routes

### 5. Reducing room size and mode duration to preserve clarity, performance, and cadence

Direct evidence from Fall Guys:

- The team reduced the main solo lobby from `60` to `40` players for faster matchmaking and `more optimised performance`.
- Later, `Knockout` became `32 players, 3 rounds`, explicitly to make wins feel more achievable and games `snappier`.
- `Explore` became a `10 player` mode where players can move on immediately instead of waiting for everyone.

Direct evidence from Battlefield 2042:

- EA later said `128 players won't be going anywhere` for some experiences, but Breakthrough was kept at `64 players` because that made it a better tactical experience with more focused frontlines.

Why this matters:

- Published counts are reversible. Products do cut room sizes when spectacle, readability, or technical stability degrade.
- This lane repeatedly shows that teams do not treat the highest possible concurrency as the sacred target.

## Concrete tradeoffs and limits

### Highest-confidence tradeoffs

- `Fortnite / Unreal`: the strongest exposed precedent for large active sessions is filtered and prioritized replication, not naive full-state broadcasting.
- `Trackmania`: large participation is handled by qualification, divisioning, and knockout reduction. The product does not imply that huge equal-contact finals are the goal.
- `iRacing`: overflow is handled by splits; larger entry pools are normalized into safer/fairer fields; ghost mode is an explicit no-contact participation channel.
- `Battlefield 2042`: more players and more map area can reduce combat focus; EA publicly moved a flagship mode from 128 to 64 for better frontlines and tactical clarity.
- `Fall Guys`: large bean counts were not preserved at all costs; official updates tie lower counts to matchmaking, performance, and game pacing.

### What player-count claims are actually backed by engineering exposure?

Strongest backed claim in this lane:

- Epic's own documentation directly says `Replication Graph` is used in a setting exemplified by `Fortnite Battle Royale` starting with `100 connected players` and about `50,000 replicated Actors`.

Reasonably backed operational claims:

- Trackmania officially supports room/server settings up to `100` players per server and scalable split rooms, while major competitive flows still divide players into smaller divisions and knockout brackets.
- iRacing officially documents overflow splitting, configurable heat/consolation structures, and feature-field reduction.

Weakly backed "count" claims:

- Battlefield's `128` and Fall Guys' `60/40/32` are directly documented product numbers, but public sources here do not expose the low-level systems that made or unmade those counts.
- Those sources are useful for tradeoff reading, not for copying the transport model.

### Limits the sources make visible

- Official public materials disproportionately expose orchestration and room-shape mechanisms, not deep netcode internals.
- Racing products repeatedly avoid "everyone can fully collide with everyone forever" once participation rises.
- Count ceilings are mode-specific, map-specific, and interaction-specific.
- Contact density appears more important than raw headcount.

## What seems relevant to Prix Guesser

### 1. Preserve a separation between event shell and active interaction shell

This lane makes a strong case for separating:

- many entrants or spectators in one event shell
- smaller decisive interaction groups inside that shell

For Prix Guesser, that suggests future action modes may want:

- qualifiers feeding smaller live finals
- parallel divisions or heats
- spectators and ghosts staying present even when not collision-active

This is more evidence-backed than treating "50+ players in one race" as the default ambition.

### 2. Make interaction policy a first-class mode parameter

The most important future-facing distinction may be:

- full contact
- reduced contact
- ghost / no-contact
- spectator-only

The iRacing and Trackmania material especially suggests that "who is physically consequential to whom" should be a declared property of the mode, not an implementation accident.

### 3. Preserve per-client visibility and update-priority seams early

If a future mode has:

- moving entities
- role-specific overlays
- spectators
- private data
- different relevance by distance or phase

then the architecture benefits from a seam where each client/view can receive only what matters at the moment.

For Prix Guesser this matters even outside racing:

- a host/spectator view might need broader state than a player view
- ghost/spectator entrants might not need the same update rate as active racers
- players far from a local interaction hotspot may not need every high-frequency detail

### 4. Use topology and pacing as the first scaling knobs before deeper netcode investment

The source set repeatedly shows teams scaling by:

- shrinking the active field
- shrinking or reshaping the playspace
- splitting sessions
- reducing wait coupling
- changing round cadence

That is good news for Prix Guesser because those are product/topology levers, not only engine levers.

If the project ever wants a broader participation racing-adjacent mode, the evidence suggests starting with:

- time attack
- ghost sprint
- knockout elimination
- staged heats

before exploring shared-contact chaos.

### 5. AI fill looks lower-priority than splits, ghosting, and spectators

Battlefield uses AI soldiers to keep matches full. That is a real precedent, but for this project's current private-room posture it looks less important than:

- split orchestration
- spectator handling
- ghost participation
- role/visibility control

It is relevant mainly if the product later wants public matchmaking or drop-in public lobbies.

## Uncertain but promising leads

- `Rocket Racing` remains a thin public engineering reference. Epic's public creator docs expose race devices and course-management concepts, but not the scaling or authority model. As of the Epic support notice crawled in April 2026, Rocket Racing is also scheduled for removal from Fortnite in `October 2026`, which makes it a less stable precedent than it first appears.
- `Battlefield` is useful for map/topology and player-count tradeoffs, but weak for low-level networking lessons because public Frostbite netcode exposure here is sparse.
- `Fall Guys` is useful as a warning that headline counts get cut when clarity/performance suffer, but not as a strong source for concrete transport or replication mechanisms.
- `Trackmania` likely has more to mine in dedicated-server and plugin ecosystems if later research needs organizer tooling, live-event admin workflows, or automated split orchestration.
- `iRacing` likely has more to mine in series-specific supplemental regulations and track-specific field-size practices if later research needs stronger evidence on how track geometry, pit infrastructure, and class mix affect field caps.
- If Prix Guesser gets serious about synchronous contact-heavy driving rather than ghosted/segmented racing, this lane should be followed by a separate netcode-focused pass on rollback/prediction/reconciliation literature and postmortems. This source set suggests segmentation more strongly than it supports full-contact browser racing.
