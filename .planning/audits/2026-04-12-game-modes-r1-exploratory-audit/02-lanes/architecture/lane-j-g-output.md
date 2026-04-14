---
date: 2026-04-13
lane: j-g
lane_name: "Racing / large-event topology follow-up"
orientation: exploratory
delegation_class: replanning-revision-gap-filling
---

# Lane J-G: Racing / Large-Event Topology Follow-Up

## Lane framing

This follow-up was run as a mechanism-level pass on how racing systems keep large participation tractable without turning the whole event into one giant fair-contact field.

The strongest direct evidence in this pass came from official product and competition materials, not deep engine writeups:

- Trackmania docs that explicitly describe qualification, divisions, knockout eliminations, room splitting, and ghost surfaces
- iRacing sporting-code and support docs that explicitly describe field-size policy, race splits, heat structures, ghost racing, and connection fault containment
- Gran Turismo World Series official competition pages that explicitly describe league-based online qualifiers feeding much smaller live-event fields

The main high-confidence conclusion is not that racing products solve scale with one universal networking trick.

It is that they repeatedly reduce active coupling through event structure:

- qualifier seeding
- league/division partitioning
- parallel splits
- heats and consolations
- ghost or time-attack participation
- smaller decisive finals

That is mostly an event-shell pattern, not proof of one specific netcode stack.

## Reference cases and source audit

| Reference case | Source type | Reliability | What the source actually exposes | What it does not expose | Direct vs inferred |
| --- | --- | --- | --- | --- | --- |
| Trackmania | Official gameplay and competition docs | High for event topology, low-medium for engine internals | `Cup of the Day` uses a `15` minute qualification phase, then places players into divisions of similar skill with `max. 64 players per division`; knockout removes `4 / 2 / 1` players per round depending on remaining field; room settings allow `1-100` max players per server and a `scalable room` option that splits servers as player count approaches the cap; qualifier tooling auto-creates servers from registrations vs configured max players; official docs also expose leaderboard and VIP ghosts | Transport model, collision/netcode details, replication/interest-management internals | Qualification, divisions, knockout, room splitting, and ghost surfaces are direct. Any claim that these are chosen for a specific network budget is inference. |
| iRacing | Official sporting code plus official support docs | High for operational rules, medium for engine internals | Ranked race field size is chosen to keep racing `safe, fun, and competitive`; if too many drivers register, identical events run in parallel as separate fields; race splits are driven primarily by `iRating` with latency/farm selection also discussed in support docs; ghost racing is invisible and non-colliding while preserving draft and track-condition effects; heat-race presets explicitly funnel `50` or `60` entries into much smaller feature fields; `Connection Black Flag` makes unstable drivers intangible and teleports them to pit lane | Low-level replication, exact collision architecture, precise farm-selection implementation | Splits, ghosting, heats, and connection fault containment are direct. Treating them as general coupling-reduction precedents is inference, but strong inference. |
| Gran Turismo World Series | Official championship and event pages | Medium-high for competition shell, low for engine internals | Online Qualifiers use a league format (`GT1`, `GT2`, `GT3`) based on driver rating; entrants pick participation time slots; top GT1 competitors advance to live events; live-event pages expose qualifying time trials and multi-race weekends where one stage sets the next starting grid; final live fields are far smaller than the open qualifier population | Public-field caps, networking internals, matchmaking/server-topology details | League funnel and stage-to-stage seeding are direct. Any claim about server pressure is inference. |
| Forza Motorsport 7 Rivals / Leaderboards | Official support doc | Medium | Official support exposes `Training Ghost` rivals that stay on track while driving; leaderboard laps are invalidated by contact, drafting, rewinds, and track-limit violations | Large live-event topology, modern competition structure, networking internals | The ghost and invalidation rules are direct. Using this as a broad large-event precedent is weak and should stay secondary. |

### Official sources used

- Trackmania, `How to play Cup Of The Day?`: https://doc.trackmania.com/play/how-to-play-cotd/
- Trackmania, `Room`: https://doc.trackmania.com/club/activities/room/
- Trackmania, `Adding a qualifier`: https://doc.trackmania.com/club/competition-tool/create-competition/qualifier/
- Trackmania, `Using the structure importer`: https://doc.trackmania.com/club/competition-tool/create-competition/structure-importer/
- Trackmania, `Watching replays`: https://doc.trackmania.com/play/watch-replays/
- Trackmania, `VIP Keys`: https://doc.trackmania.com/play/vip-keys/
- iRacing Official Sporting Code, version dated March 10, 2026: https://ir-core-sites.iracing.com/members/pdfs/20260310-official_sporting_code_dated_Mar_10_2026.pdf
- iRacing support, `Why are there Race Splits?` (modified January 2, 2024): https://support.iracing.com/support/solutions/articles/31000133457-why-are-there-race-splits-
- iRacing support, `Ghost Racing` (modified December 19, 2025): https://support.iracing.com/support/solutions/articles/31000133497-ghost-racing
- iRacing support, `Setting up Heat races` (modified August 15, 2024): https://support.iracing.com/support/solutions/articles/31000152676-setting-up-heat-races
- Gran Turismo World Series 2025 Race Details, official event page: https://www.gran-turismo.com/us/gt7/events/gtws2025/worldfinals/race_info/
- Gran Turismo World Series 2025 Overview, official championship page: https://us.gran-turismo.com/us/gt7/championships/2025/overview/
- `The "Gran Turismo World Series" 2025 - Manufacturers Cup Online Qualifiers Details`, official news page: https://www.gran-turismo.com/us/gt7/news/00_1076836.html
- `The "Gran Turismo World Series" 2025 - Nations Cup Online Qualifiers Details`, official news page: https://www.gran-turismo.com/us/gt7/news/00_3853706.html
- Forza Support, `FM7 Rivals and Leaderboards`: https://support.forzamotorsport.net/hc/en-us/articles/360005424113-FM7-Rivals-and-Leaderboards

## Concrete event-structure and coupling-reduction mechanisms

### 1. Qualifier seeding turns "many entrants" into ordered downstream groups

Direct evidence:

- Trackmania `Cup of the Day` runs `10` minutes to finish plus `5` minutes to improve, then uses the best time to place players into similarly skilled divisions capped at `64` players.
- Trackmania's competition tool describes the qualifier phase as seeding players and says it can determine whether a player even reaches the bracket phase.
- Gran Turismo World Series official pages describe open online qualifiers feeding smaller elite live-event fields, with league assignment by driver rating.

Why this matters:

- Qualification is not just pre-show.
- It is a load-shaping mechanism that converts one large entrant pool into smaller, ordered downstream groups.

Direct evidence vs inference:

- The existence of qualifier seeding is direct.
- Reading it as coupling reduction is a justified inference, because it reduces who has to matter to whom in later stages.

### 2. Parallel splits are event-shell sharding, not one giant room

Direct evidence:

- iRacing's sporting code says that when more drivers register than a track or series allows, the event is instantiated into separate fields racing at the same time.
- The same code defines `Splits` as parallel sessions created when more than the maximum number of participants want one event.
- iRacing support adds that split assignment is automatic and primarily driven by `iRating`, while also considering latency/farm selection.
- Trackmania room settings expose a `scalable room` option that lets the server split as player numbers approach the configured maximum.
- Trackmania qualifier docs say qualifier servers are automatically created around `30` minutes before start based on registrations compared to the configured per-server max.

Why this matters:

- This is one of the clearest direct answers to "how do you handle large participation without one giant field?"
- You keep one event shell, but you do not keep one active interaction shell.

What kind of solution this is:

- Mostly event-shell and orchestration design.
- Not proof of one specific replication design.

### 3. Heats and consolations deliberately reduce contact density before the decisive race

Direct evidence:

- iRacing's sporting code defines `Heat Racing` as a structure where performance in early sessions determines eligibility for later sessions, including `Practice`, `Qualify`, `Heat`, `Consolation`, and `Feature`.
- iRacing's hosted heat-race presets explicitly show structures like `50 entries -> 5 heats -> D/C/B mains -> 23-driver A Main` and `60 entries -> 6 heats -> D/C/B mains -> 24-driver A Main`.
- Trackmania's knockout structure is a related funnel even though it is time-attack / survival flavored rather than traditional heat racing.

Why this matters:

- This is not just tournament decoration.
- It is an explicit mechanism for keeping the final contact-sensitive field materially smaller than the registration pool.

Product-shape inference:

- For Prix Guesser, the closest lesson is not "copy dirt heat formats."
- It is "large event participation and small decisive live field can be intentionally decoupled."

### 4. Ghosting keeps shared context while removing collision coupling

Direct evidence:

- iRacing ghost racing places a user into a populated live race or practice session as an invisible, non-colliding participant.
- The same doc says the ghost still gets draft effects and track-condition changes.
- Trackmania docs expose leaderboard ghosts and VIP ghosts as first-class replay/learning surfaces inside the normal play ecosystem.
- Forza's official Rivals support doc exposes a `Training Ghost` rival that stays on track while the player drives.

Why this matters:

- Ghosting preserves same-track comparison and event texture while removing the main source of mutual disruption.
- It is a concrete coupling-reduction mechanism, not just a replay viewer convenience.

Limits:

- Trackmania and Forza ghost surfaces here are stronger evidence for comparison shells and learning loops than for large live shared events.
- iRacing is the strongest direct case for live-session ghosting.

### 5. Stage-to-stage result propagation replaces all-to-all interaction

Direct evidence:

- Gran Turismo live-event race details pages explicitly describe a `Qualifying Time Trial` that determines the Race 1 grid, then Race 1 determines the Race 2 grid, then later races determine the final grid.
- Trackmania's knockout divisions similarly use earlier performance to decide who remains relevant in later rounds.

Why this matters:

- One way to scale participation is to let results travel forward instead of making all participants directly interact at the same time.
- That is a competition-shell mechanism, not a networking mechanism.

Why it still matters architecturally:

- If a future Prix Guesser action mode wants larger race-weekend events, it may need first-class support for:
- qualification outputs
- bracket/division membership
- advancement rules
- later-stage seeding from earlier-stage results

### 6. Fault containment can reduce coupling even inside one live field

Direct evidence:

- iRacing's sporting code defines `Connection Black Flag` for unstable connections: the affected driver becomes intangible, is teleported to pit lane, and can rejoin if the connection stabilizes.

Why this matters:

- This is a different kind of coupling reduction.
- It is not about scaling entrant count; it is about preventing one unstable participant from continuing to perturb a contact-sensitive field.

Relevance:

- This is one of the few direct official examples in this source set where the platform explicitly reduces interaction rights in response to runtime instability.

## Concrete tradeoffs and limits

### Highest-confidence tradeoffs

- Qualifiers, splits, and heats preserve broad participation, but they reduce the fantasy that everyone is contesting one equal-contact race together.
- Splits improve fairness and tractability, but they fragment social cohesion unless the product also supplies a unifying event shell, standings, or broadcast layer.
- Heats and consolations produce cleaner finals, but they add scheduling and rules complexity.
- Ghosting keeps shared timing and comparison, but it removes blocking, overtaking consequence, and some of the drama of direct racecraft.
- League funnels and live-event shells are strong evidence for competition structure, not strong evidence for large public-field simulation internals.

### What the source set does and does not really prove

What is directly supported:

- Racing products often avoid one giant decisive contact field once participation gets large.
- They do so with qualifiers, divisions, splits, heats, ghosting, and staged finals.
- Some products also expose fault-containment rules that temporarily remove unstable participants from active coupling.

What is not directly supported:

- The exact netcode or replication strategy inside Trackmania, Gran Turismo, or iRacing for these structures.
- Whether these structures were chosen mainly for fairness, spectacle, server cost, moderation, latency, or all of the above.
- Any general claim that a given product can scale a fair high-contact race to very large equal-participant counts.

### Event-shell solution vs netcode solution

Strong event-shell solutions in this lane:

- qualifier seeding
- parallel splits
- leagues/divisions
- heats/consolations/features
- stage-to-stage advancement

Mechanisms that also touch runtime interaction policy:

- ghosting
- connection fault isolation

The evidence here is much stronger for event-shell orchestration than for deep networking architecture.

## What seems relevant to Prix Guesser

### 1. Separate the event shell from the active interaction shell

The clearest takeaway is that a future Prix Guesser racing or action event does not need one giant mutually consequential field to feel large.

A more evidence-backed shape is:

- one event shell with shared registration, standings, host presentation, and finals logic
- smaller active shells for qualifiers, divisions, heats, or finals

### 2. Make coupling policy a first-class mode decision

The source set suggests a useful future mode axis:

- full contact
- reduced contact
- ghost / no-contact
- eliminated but spectating
- qualified but waiting for the next shell

That should not be an accidental implementation detail if the project ever grows into action-heavy modes.

### 3. Preserve qualification and advancement as reusable primitives

If the project ever experiments with:

- circuit sprints
- venue runs
- obstacle/elimination race variants
- race-weekend party events

then the reusable primitive is not "large room."

It is:

- qualification result
- division assignment
- heat membership
- advancement / elimination rule
- downstream seeding

### 4. Ghost comparison looks more plausible than large shared collision chaos

For circuit-recognition or racing-adjacent futures, the evidence is stronger for:

- same track
- same clock or same conditions
- ghosted opponents
- split finals

than for:

- `50+` players in one fair-contact live field

### 5. Fault isolation may matter even for modest future live modes

The iRacing `Connection Black Flag` example suggests that if a future live mode becomes contact-sensitive, the system may need a degraded interaction mode for unstable clients rather than letting them remain fully consequential.

For Prix Guesser that could mean:

- automatic spectator fallback
- ghost fallback
- reduced authority or reduced interaction rights for degraded clients

That is still speculative for this project, but the precedent is concrete.

## What remains uncertain

- We still do not have primary-source exposure to the low-level networking internals behind Trackmania, Gran Turismo, or iRacing field handling.
- The public docs are much stronger on competition topology than on transport/replication mechanics.
- Gran Turismo is a useful official case for qualifier funnels and staged finals, but it is weaker than iRacing or Trackmania on explicit room-shape and scaling operations.
- Forza's ghost evidence is real but secondary in this lane because it is older and not a large live-event document.
- We do not yet have a strong official Rocket Racing source set that exposes comparable mechanisms in enough detail to use confidently here.
- If the user later wants a dedicated `50+ synchronous action` architecture pass, that should be a separate research lane focused on primary technical materials rather than competition-rule docs.
