---
date: 2026-04-13
lane: i-b
lane_name: "Real-time action / collision room research"
delegation_class: initial-architecture-research-planning
output_file: 02-lanes/architecture/lane-i-b-output.md
audit_subject: lane-i-b-real-time-action-collision-racing
audit_orientation: exploratory
audit_delegation: self
scope: "Official/primary-source scan of medium-to-large real-time action, collision, and racing room patterns, connected to possible F1 modes and early substrate implications"
auditor_model: gpt-5.4
task_spec: 02-lanes/architecture/lane-i-b-task-spec.md
source_bias: "official game docs, official engine docs, official support pages, official sporting-code materials"
tags:
  - exploratory-audit
  - lane-i
  - lane-i-b
  - real-time-action
  - collision
  - racing
  - room-architecture
---

# Lane I-B: Real-time action / collision room research

## Lane framing

This lane is not asking whether this project should build a 50+ active-player F1 mode soon. It is asking what medium-to-large real-time action rooms actually look like in shipped products, what they do to avoid a fully shared collision problem, and what early substrate decisions become harder to reverse if even one future F1 mode wants that class.

The official-source pattern is uneven. Game teams often publish mode sizes, playlist shapes, and high-level networking architecture, but not a full postmortem on rollback, prediction, anti-cheat, or server topology. So this note combines:

- official game/mode pages for room shape and player-count intent
- official engine docs or tech blogs for replication/authority patterns
- official support/sporting-code docs for splits, field limits, and region/latency handling

Where I move from source facts to architectural interpretation, I say so explicitly.

The main synthesis point is that "`50+`" is not one thing. In the reference set below it means at least four different patterns:

- a large but sparse action world where only a local subset matters at any moment
- a chaotic obstacle room where everyone starts together but the design quickly reduces active coupling
- a racing event that is socially one event but operationally many heats or splits
- a same-track competition that scales by ghosting, time attack, or segmented elimination instead of continuous body-contact fairness

## Reference cases

### 1. Fall Guys: dense obstacle chaos works, but the product keeps shrinking the fully shared problem

Official Fall Guys material gives three useful signals. First, the game openly marketed 60-player gauntlets and races such as `Skyline Stumble` and `Roll On` in Season 4 ([Season 4 is OUT NOW](https://www.fallguys.com/en-US/news/season-4-is-out-now?lang=en-US)). Second, the team later cut the main Solos playlist from 60 players to 40 players specifically to improve matchmaking and "optimised performance in each Round" ([Creative, faster matchmaking, and an update about Seasons are all incoming!](https://www.fallguys.com/en-US/news/fall-guys-creative-faster-matchmaking-and-an-update-about-seasons-are-all-incoming?lang=en-US)). Third, the 2024 `Fall Forever` update pushed the core `Knockout` show to 32 players / 3 rounds and introduced a separate `Explore` mode at 10 players with queue-forward progression instead of forcing all players to wait for the whole room every time ([The Fall Forever Update](https://www.fallguys.com/en-US/news/fall-forever-update)).

The most important primary-source detail is not the marketing count. It is the technical shape of shared interaction. In Mediatonic's own write-up on movable blocks, the designer says the mechanic was "technically challenging for a networked game" and that having roughly 30 players all able to grab and climb the same blocks at once was "an awful lot for the game to manage" ([Moving parts! The brains behind the blocks](https://www.fallguys.com/en-US/news/moving-parts-the-brains-behind-the-blocks)).

Local conclusion: Fall Guys shows that high-concurrency embodied chaos is viable and fun, but dense shared physics is one of the first things that becomes expensive. The live product response was not "solve infinite scale." It was "reduce caps, shorten shows, separate calmer queue-forward modes, and keep the most intense shared interactions bounded."

### 2. Fortnite Battle Royale plus Unreal Replication Graph: 100-player rooms work by relevance filtering, not universal mutual interaction

Epic's official support page for private Fortnite Battle Royale matches states a hard maximum of 100 players in a match ([How to start a private match in Fortnite](https://www.epicgames.com/help/en-US/c-Category_OurCreatorPrograms/c-13889284176923/a202300000014175?lang=en-US)). Epic's Unreal tech blog then explains what that scale means under the hood: Fortnite was dealing with "up to 100 clients" in a world with "50,000 synced actors," and the old per-actor/per-client replication approach did not scale. Epic's response was the Replication Graph system, which caches and reuses relevance results, including a `Grid Spatialization 2D` node so clients only consider actors relevant to their occupied cells ([Replication Graph overview and proper replication methods](https://www.unrealengine.com/tech-blog/replication-graph-overview-and-proper-replication-methods?lang=en-US)).

This is the clearest primary-source example of what a large real-time action room usually really is. It is not 100 players all colliding with all other players and all objects at equal fidelity. It is a server-authoritative world where only a local slice is fully relevant at a given moment, and the engine spends real complexity budget on relevance management.

Local conclusion: large action rooms scale when the world is big, the interaction graph is sparse, and the runtime is built around interest management from the start.

### 3. Battlefield 2042: even games that can do 128 often decide many modes should not

EA's official Battlefield 2042 development update is unusually candid about mode-specific limits. The team says players enjoyed maps at 128-player Conquest, but also says they had "unshackled" themselves from always designing around 128 and moved Breakthrough to 64 players because it created more focused frontlines and less chaotic flank resistance ([Battlefield Briefing -- Development Update, May 2022](https://www.ea.com/en-au/games/battlefield/battlefield-2042/news/battlefield-briefing-development-update-may-2022)). The official Battlefield Portal briefing reinforces that this is not one-size-fits-all: the product exposes small map variants for intimate FFA/TDM, medium maps recommended for 64 players, and large maps suited for up to 128 ([Battlefield Briefing – Welcome to Battlefield Portal](https://www.ea.com/en-gb/games/battlefield/battlefield-2042/news/battlefield-briefing-welcome-to-battlefield-portal)).

The important lesson is not just that 128 exists. It is that the same franchise keeps different player counts, layouts, and rulesets because action density is mode-dependent. "Bigger room" is not automatically "better room."

Local conclusion: large active counts in shooter/vehicle sandboxes are usually achieved by sectors, fronts, and map-size variants that prevent the room from becoming one giant simultaneous contact knot.

### 4. Trackmania: racing scale is often social/event scale, not one fair contact field

Trackmania's official docs and news posts show multiple ways to scale racing without pretending the field is one flat shared problem. Royal is officially a 60-player mode in 20 teams of up to 3 players, built around five difficulty segments and progressive advancement ([DISCOVER THE NEW ROYAL UPDATE!](https://www.trackmania.com/news/7882); [What is Royal?](https://doc.trackmania.com/play/what-is-royal/)). Cup of the Day qualifies players, then places them into divisions capped at 64, with knockout rounds eliminating four players at a time until a winner remains ([How to play Cup of the Day?](https://doc.trackmania.com/play/how-to-play-cup-of-the-day/)). Trackmania's room settings also expose `max players per server` from 1 to 100 and offer `scalable room splits` when approaching the max player threshold ([Server room settings](https://doc.trackmania.com/play/server-room-settings/)).

This is not proof of a specific collision topology, because the official docs here focus on event structure more than netcode. The architectural inference is still strong: Trackmania scales competitive participation through segmented progression, divisions, and room splitting, not by requiring one giant field to maintain equally meaningful car-to-car fairness for everybody at once.

Local conclusion: one of the cleanest ways to make racing feel large is to make the event large while the decisive interaction set stays smaller, segmented, or split.

### 5. Rocket Racing: even arcade racing on Epic's stack keeps direct-contact races small and offloads scale to ghost/time-trial play

Epic's official UEFN documentation for Rocket Racing islands defines two templates: a `Competitive Race Track` for a maximum of 12 players over multiple laps, and a `Speed Run Track` where players compete for best lap time on the same track with up to 11 others ([Creating Rocket Racing Islands in Unreal Editor for Fortnite](https://dev.epicgames.com/documentation/en-us/fortnite/creating-rocket-racing-islands-in-unreal-editor-for-fortnite)). Epic's official `Speed Run` announcement makes the scaling trick explicit: collisions with other players are turned off, drafting is disabled, and the mode is built around ghosts and leaderboards instead ([Set a Speed Run Record in Rocket Racing v28.30!](https://www.fortnite.com/news/set-a-speed-run-record-in-rocket-racing-v28-30?lang=en-US)). Epic also publicly acknowledged collision problems in ranked racing and said they were making collisions "far less extreme" in v28.20 ([Rocket Racing v28.20 Swerves In with Advanced Tracks!](https://www.fortnite.com/news/rocket-racing-v28-20-swerves-in-with-advanced-tracks?lang=en-US)).

This is a very relevant boundary case. Epic already has large-scale action networking expertise, and yet its arcade racing product still keeps direct competitive races small and pushes larger comparison play into ghosted time-trial structure.

Local conclusion: if even an intentionally arcade racing product does not stretch contact racing into large active fields, that is a warning against assuming an F1 party game should do so casually.

### 6. iRacing: the sim-racing solution is explicit field caps, official splits, and relevance filtering

The current iRacing Sporting Code says the maximum number of drivers for each ranked race is chosen to ensure "safe, fun, and competitive racing" and that if more drivers register than the track or series allows, they are split into separate fields racing at the same time, primarily by iRating ([2026 Official Sporting Code](https://ir-core-sites.iracing.com/members/pdfs/20260310-official_sporting_code_dated_Mar_10_2026.pdf)). iRacing's support articles add current operational detail: race assignment also considers internet latency and friends in some cases, and the field is split automatically when large numbers register at the same time ([Why are there Race Splits?](https://support.iracing.com/support/solutions/articles/31000133457-why-are-there-race-splits-); [The official session I registered for showed 150 drivers registered; why did the session I was in only have 12 drivers?](https://support.iracing.com/support/solutions/articles/31000133589-the-official-session-i-registered-for-showed-150-drivers-registered-why-did-the-session-i-was-in-onl)).

Another official iRacing support article is especially useful for substrate thinking: in large fields the sim does not necessarily transmit every car to every client equally. The `Max Cars` setting exists because "not all cars in the race may be sent to every driver" and the system biases nearby cars in front and behind while dropping others when necessary ([connection type and max cars](https://support.iracing.com/support/solutions/articles/31000133494-connection-type-max-cars)).

Local conclusion: high-fidelity racing systems protect fairness by capping fields, splitting oversubscribed events, and filtering relevance. They do not treat "one giant full-contact grid" as the default answer.

## What scales and what breaks first

Patterns that scale relatively cleanly across the reference set:

- Large worlds with low local density. Fortnite and Battlefield can support high headline counts because only a local slice of the room matters intensely at any given moment.
- Event structures that reduce concurrent coupling over time. Fall Guys, Trackmania Royal, and Cup of the Day all narrow the meaningful interaction set through elimination, segmentation, or progression.
- Same-track competition that does not require continuous contact fairness. Rocket Racing Speed Run and iRacing Time Trial style structures scale by comparing times, ghosts, or rankings rather than by adjudicating dozens of simultaneous collisions.
- Multi-instance events. Trackmania divisions, iRacing splits, and Battlefield's small/medium/large map variants all treat "one event" as compatible with multiple actual interaction containers.
- Explicit relevance filtering. Unreal Replication Graph and iRacing `Max Cars` are strong primary-source evidence that large rooms are partly won by not sending or evaluating everything for everyone.

What appears to break first:

- Shared rigid-body or shared-object interaction where many players can all touch the same thing at once. Fall Guys' own designers call out the cost of roughly 30 players all grabbing and climbing the same blocks.
- Fair contact racing at large N. The racing examples consistently either cap direct races, split the field, or disable collisions when the experience becomes more about comparison than direct battling.
- Product assumptions that every mode should use the same room cap. Battlefield's official mode revisions are a direct counterexample.
- Any topology that assumes all entities remain equally relevant to all players every frame. Epic's own networking write-up frames that as the non-scaling strategy.

The practical interpretation is that the phrase "`50+ players`" usually means "`50+ participants in one branded event or shared world shell`," not "`50+ mutually important collision peers at equal fidelity all the time.`"

## How these designs avoid one giant fully-shared problem

Across the sources, the recurring avoidance strategies are remarkably consistent:

- Spatial separation. Big maps, sectors, fronts, and grid-based relevance ensure only nearby actors are hot.
- Event segmentation. Qualification, divisions, heats, and splits let many players enter the same event without forcing one overloaded simulation.
- Elimination. Fall Guys and Trackmania let many players start together, but the system steadily reduces how many active competitors matter.
- Contact downgrades. Rocket Racing literally turns collisions off in Speed Run; other products reduce collision severity or keep contact-heavy modes smaller.
- Mode-specific caps. Products do not pretend all action modes deserve the same room size.
- Relevance filtering. Unreal's Replication Graph and iRacing's `Max Cars` make "not everything for everyone" a first-class runtime rule.

This matters because the avoidance is not merely technical. It is product design. These teams change the fantasy slightly so the networking problem becomes tractable.

## Relevance to possible F1 modes

The most plausible F1-adjacent uses of these patterns are not "50+ fully shared Formula 1 car battles." They are narrower and more mode-shaped.

Plausible fits:

- A non-contact circuit sprint or time-trial family. This is the cleanest route to "many participants" while preserving recognizable circuit geography. Ghosts, split leaderboards, heats, or same-room asynchronous comparison fit Trackmania, Rocket Racing Speed Run, and iRacing Time Trial patterns.
- A 12 to 24 player arcade race or chase family. If the product ever wants a more direct action mode, Rocket Racing is the more relevant pressure example than Fortnite BR. That implies small, contact-light rooms and carefully bounded collision behavior.
- A 24 to 40 player elimination obstacle race themed around circuits, pit lane, paddock, marshal posts, or trackside hazards. Fall Guys is the important reference here. The likely winning structure is rounds plus eliminations, not one long fully shared race where everyone keeps colliding the whole time.
- A large community event that is socially one room but mechanically many shards. Trackmania and iRacing both suggest that a race-weekend F1 event could feel big through divisions, heats, or bracketed finals without ever simulating one giant fair-contact pack.

Weak fits that should probably not be pushed into this architecture lane:

- 50+ fully shared contact racing on one track where overtakes, bumps, and recovery all need to feel fair in real time.
- 50+ players all manipulating the same physical barriers, cars, or track objects as core gameplay.
- Any future mode whose fantasy depends on every player materially colliding with many other players at once rather than mostly interacting with the course.

My inference is that if this project ever reaches beyond private-room party sizes, the most promising "large" F1 action modes are likely to be:

- non-contact or light-contact
- eventized or elimination-based
- socially large but mechanically sharded

That is very different from "build a mini-MMO racetrack."

## Early architectural implications

If even one future F1 mode wants this class of real-time action room, several early substrate choices become worth preserving now:

1. Separate the social room from the simulation instance. A room, lobby, or watch-party should be able to own multiple heats, splits, or action shards. This is the single most important hedge.

2. Make collision/authority model a per-mode contract, not a global assumption. Some modes may be `ghosted`, some `light-contact`, some `full-contact`, some `shared-physics-object`. That contract should drive caps, reconciliation rules, and network topology.

3. Avoid baking all authority into a pure host-client party model if future action modes remain live possibilities. Host-screen and phone-controller orchestration may still be perfect for many party modes, but collision-sensitive action modes usually want a more authoritative runtime boundary than "whoever created the room."

4. Plan for interest management early. Even medium room sizes benefit from explicit relevance rules for players, hazards, projectiles, checkpoints, moving track elements, and spectators.

5. Treat heats, eliminations, and divisions as product primitives, not emergency fallback. The reference set shows they are not second-best hacks; they are normal ways large events stay legible and fair.

6. Add ghost/replay/time-trial capabilities early if racing-like modes remain on the table. These are the cheapest architectural bridge between small private rooms and "large participation" fantasies.

7. Keep per-mode caps configurable. Battlefield is the warning that one cap for the whole game is usually the wrong abstraction.

8. Be cautious with shared movable physics objects. Fall Guys' own account of the block mechanic is a direct warning that this cost spikes quickly even well below "massive" player counts.

9. Keep region/latency policy out of the mode core where possible. iRacing's split logic shows that once action fairness matters, server placement and latency become part of match assembly, not just transport plumbing.

The lowest-regret interpretation is not "build 100-player infrastructure now." It is "do not hard-code the product so that a future action mode can only exist as one browser-hosted fully shared room."

## Uncertainties and limits

- Official sources rarely expose the full prediction/rollback/anti-cheat stack, so this lane can say more about room patterns and architectural shape than about exact implementation recipes.
- Trackmania is especially informative on event segmentation and room splitting, but the collision/authority interpretation there is partly inferential because the official docs emphasize mode structure more than low-level netcode.
- Battlefield and Fortnite official materials clearly describe player counts and relevance-management direction, but they do not publish a complete simulation topology for every mode.
- These cases are pressure examples, not portfolio recommendations. The project may never need anything beyond small private rooms. The value here is in preserving optionality and in understanding what "large action room" really cashes out to when products actually ship.
- Confidence is highest on the structural conclusions: large real-time rooms are usually made tractable by segmentation, relevance filtering, collision downgrades, or smaller decisive cohorts. Confidence is lower on any claim that a specific future F1 mode should definitely target one of these patterns now.
