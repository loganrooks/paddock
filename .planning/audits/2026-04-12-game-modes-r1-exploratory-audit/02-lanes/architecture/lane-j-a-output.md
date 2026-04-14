---
date: 2026-04-13
lane: j-a
lane_name: "Browser / audience systems engineering exposure"
delegation_class: initial-architecture-research-planning
tags:
  - exploratory-audit
  - lane-j-a
  - browser
  - audience
  - host-screen
  - engineering-exposure
---

# Lane J-A: Browser / audience / host-screen systems engineering exposure

## Lane framing

This sub-lane is about browser-first systems that coordinate a host surface, participant devices, and sometimes an overflow audience.

The strongest direct engineering exposure in this pass came from `Jackbox`, plus one Mentimeter technical requirements page. `Kahoot`, `Slido`, and `GeoGuessr` were much more support-doc-driven: useful for topology, joins, moderation, and room/session shape, but weaker on internals. I am therefore treating them as evidence of exposed mechanisms and operator constraints, not as deep proof of backend design.

Bias for this pass:

- prioritize topology, role separation, join/rejoin, moderation, and reveal cadence
- treat raw participant limits as secondary unless they reveal a distinct interaction shape
- mark direct facts separately from researcher inference

## Reference cases and source audit

| Reference case | Source class | Reliability | What it actually exposes | What it does not expose | Direct vs inferred |
| --- | --- | --- | --- | --- | --- |
| `Jackbox` | Class 2 official talk, Class 3 official product/blog docs | High | browser-controller architecture, audience mode shape, streamer moderation features, controller/server traffic spikes, ops impact from traffic surges | transport choice, authoritative-state internals, exact sharding model | audience layering and moderation surfaces are direct; backend topology beyond that is inferred |
| `Kahoot` | Class 3 official support docs | Medium-high | host PIN flow, QR/link joins, shared-device vs personal-device team modes, optional question-on-device mode, late join/rejoin behavior, identifier/reporting flow | internal networking architecture, exact authority model, scaling internals | mode topology is direct; architectural consequences are inferred |
| `Mentimeter` | Class 1-ish official technical requirements + Class 3 support docs | High for exposed surfaces | browser-only runtime, realtime and quiz endpoints, WebSocket requirement, different caps for quiz vs non-quiz slides, waiting-room behavior, Q&A moderation link, stable link/QR vs rotating code | detailed service topology, internal queueing/sharding, exact reveal scheduler internals | endpoint/realtime split and moderation flows are direct; service decomposition beyond named endpoints is inferred |
| `Slido` | Class 3 official community/help docs | Medium-high | event with multiple rooms, present mode, cumulative participant counting, QR/code/link joins, co-host capability split, Q&A moderation review flow | internal backend architecture, exact room routing, scaling internals | room/event distinction is direct; system reasons behind limits are partly inferred |
| `GeoGuessr` | Class 3 official support docs | Medium | party container, multiple game-lobbies, per-lobby/pro-hosting constraints, private-lobby links, live challenge cap, kick/ban tooling, limited in-game moderation | deep engineering detail, internal authority model, sync implementation | party/lobby/operator shape is direct; broader architecture implications are inferred |

### Primary sources used

- Jackbox GDC talk: [The Players You Didn’t Plan For: How Jackbox Games Has Adjusted to Life During Quarantine](https://media.gdcvault.com/gdcsummer2020/presentations/Bilder-Mike-The%20Players%20You%20Didnt%20Plan%20For%20How%20Jackbox.pdf)
- Jackbox blog: [Streaming, Moderation, and Accessibility Features in The Jackbox Party Pack 8](https://www.jackboxgames.com/blog/streaming-moderation-accessibility-features-jackbox-party-pack-eight)
- Jackbox blog: [How Audience Play-Along Differs In Each Jackbox Game](https://www.jackboxgames.com/blog/how-audience-play-along-differs-in-each-jackbox-game)
- Jackbox blog: [Behind the Scenes of Party Pack 10: Game Engineering Edition!](https://www.jackboxgames.com/blog/behind-the-scenes-of-pp10-engineering)
- Kahoot support: [Kahoot! game: play in team mode](https://support.kahoot.com/hc/en-us/articles/4408679135891-Kahoot-game-play-in-team-mode)
- Kahoot support: [How to find Kahoot! PIN](https://support.kahoot.com/hc/en-us/articles/360000109048-How-to-find-Kahoot-PIN)
- Kahoot support: [Kahoot! join: How to join a Kahoot! game](https://support.kahoot.com/hc/en-us/articles/360039890713-Kahoot-join-How-to-join-a-Kahoot-game)
- Kahoot support: [Player identifier](https://support.kahoot.com/hc/en-us/articles/360036178314-Player-identifier)
- Kahoot support: [How to host a live kahoot](https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot)
- Kahoot support: [How to enable “See questions on participant’s screen” in Kahoot! live games](https://support.kahoot.com/hc/en-us/articles/115003197928-Kahoot-live-game-see-questions-on-participant-s-screen)
- Mentimeter help: [Requirements for running Mentimeter](https://help.mentimeter.com/en/articles/410951-requirements-for-running-mentimeter)
- Mentimeter help: [What if I can't log in or access Mentimeter?](https://help.mentimeter.com/en/articles/1148527-what-if-i-can-t-log-in-or-access-mentimeter)
- Mentimeter help: [How many people can participate in a Mentimeter presentation?](https://help.mentimeter.com/faq/presenting-and-voting/how-many-can-vote-on-a-mentimeter-question)
- Mentimeter help: [How to host the Quiz Competition](https://help.mentimeter.com/en/articles/4305015-how-to-play-the-quiz-competition)
- Mentimeter help: [Moderate your Q&A session to ensure a great experience](https://help.mentimeter.com/en/articles/1840522-moderate-your-q-a-session-to-ensure-a-great-experience)
- Mentimeter help: [Mentimeter's profanity filter](https://help.mentimeter.com/en/articles/1649840-mentimeter-s-profanity-filter)
- Mentimeter help: [How to participate in a Mentimeter presentation](https://help.mentimeter.com/how-to-vote/different-ways-to-enter-the-voting-session/)
- Mentimeter help: [How long is my join code valid?](https://help.mentimeter.com/en/articles/2780681-for-how-long-is-my-votin)
- Slido community/help: [Set up Multiple Rooms in your slido](https://community.slido.com/general-settings-220/set-up-multiple-rooms-in-your-slido-412)
- Slido community/help: [How many participants can ask questions or vote in polls?](https://community.slido.com/slido-fundamentals-205/how-many-participants-can-ask-questions-or-vote-in-polls-553)
- Slido community/help: [Use co-hosts to collaborate and help manage slidos](https://community.slido.com/co-hosting-and-shared-access-228/use-co-hosts-to-collaborate-and-help-manage-slidos-501)
- Slido community/help: [Use Slido with a QR code](https://community.slido.com/presenter-best-practices-214/use-slido-with-a-qr-code-529)
- Slido community/help: [Use Moderation and manage audience questions](https://community.slido.com/q-a-settings-222/use-moderation-and-manage-audience-questions-477)
- GeoGuessr support: [What are Live Challenges?](https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges)
- GeoGuessr support: [How do I set up a Private Lobby?](https://geoguessr.zendesk.com/hc/en-us/articles/4413903235729-How-do-I-set-up-a-Private-Lobby)
- GeoGuessr support: [How do I kick a player in an ongoing game?](https://geoguessr.zendesk.com/hc/en-us/articles/27521109954705-How-do-I-kick-a-player-in-an-ongoing-game)
- GeoGuessr support: [How do I ban someone from my private party?](https://geoguessr.zendesk.com/hc/en-us/articles/4418018073233-How-do-I-ban-someone-from-my-private-party-)

## Concrete engineering mechanisms exposed

### 1. Browser-first join flows are usually dual-path: short live code plus stable deep link / QR

- `Jackbox` exposes the lowest-friction variant: phone browser controller, no app download, and room code shown on the host surface. Source: Jackbox Pack 8 blog, Jackbox GDC talk.
- `Kahoot` explicitly separates a temporary live `PIN` from stable join alternatives: participants can join by `PIN`, direct link, or QR; the live PIN expires when the game ends, while assigned-game joins can persist to a deadline. Source: Kahoot PIN + join docs.
- `Mentimeter` says the numeric join code is temporary and renews after idle time, while QR code and direct link remain stable. Source: Mentimeter join-code-validity + QR/link docs.
- `Slido` keeps code/QR always visible in Present mode and also supports direct links. Source: Slido QR + participant docs.

Direct conclusion:

- these systems do not rely on one join primitive
- they pair a human-readable ephemeral code with a shareable stable join artifact

Prix-relevant inference:

- `temporary room code + permanent invite/deep link` is the resilient pattern for host-screen-plus-phones systems
- rotating the human code without invalidating the room/container identity looks like the safer default

### 2. Host surface and player surface are not one topology; mature products support multiple view contracts

- `Kahoot` directly exposes `Classic`, `Team vs Team: Shared devices`, and `Team vs Team: Personal devices`. It also separately exposes `Show questions & answers on participants' devices`, explicitly for remote play, large classrooms, and accessibility. Source: Kahoot team mode + question-on-device docs.
- `Mentimeter` is browser-only but describes a presenter screen driving a shared presentation while participants usually use phones, tablets, or laptops. Source: Mentimeter requirements + participation docs.
- `Slido` distinguishes `Host mode`, `Present mode`, and participant mode, with Present mode as the public wall. Source: Slido multiple rooms, QR, and present-mode docs.
- `Jackbox` still centers the host/TV surface, but audience features and streamer-mode settings show that the public display is a separate, configurable projection of state rather than just a mirror of controller state. Source: Jackbox blogs.

Direct conclusion:

- browser-first audience systems frequently split:
  - operator/host view
  - public display view
  - participant interaction view

Prix-relevant inference:

- a future-safe Prix substrate should expect at least three screen contracts from the start, even if M1 only exercises a subset

### 3. Active players, audience, and moderators are separate roles with different rights

- `Jackbox` has the clearest published role layering: small core player counts, overflow `audience`, optional `hive mind` audience in streamer mode, `VIP` or host controls, password rooms, Twitch-gated joining, and a separate moderation site at `mod.jackboxgames.com`. Source: Jackbox GDC talk + Pack 8 blog.
- `Mentimeter` Q&A moderation uses a separate moderation link where a helper can approve or dismiss incoming questions before the audience sees them. The moderator does not need their own license. Source: Mentimeter Q&A moderation doc.
- `Slido` separates host/co-host capabilities; co-hosts can moderate, archive, answer, label, highlight, delete, start or stop polls, and access analytics, but cannot change core settings like codes, privacy, dates, or multiple-room configuration unless they are full members on the same license. Source: Slido co-host doc.

Direct conclusion:

- these systems do not treat "everyone in the room" as the same role
- moderation is implemented as a rights-bearing role, not just a UI toggle

Prix-relevant inference:

- host authority and moderation authority should be modeled separately
- audience should be treated as a first-class role, not as failed players or anonymous extras

### 4. The strongest published scaling pattern is shared prompt cadence plus discrete submissions

- `Jackbox` added audience mode up to `10,000` people, but official audience docs show the audience mostly votes, predicts, submits constrained text in selected games, or behaves as a single group. Source: Jackbox GDC talk + audience play-along breakdown.
- `Mentimeter` explicitly distinguishes `Quiz` slides, capped at `2,000`, from non-quiz slide types with no published hard cap, and asks organizers of `10,000+` presentations to coordinate ahead of time. Source: Mentimeter participant-limit doc.
- `GeoGuessr` Live Challenge allows inviting a party of up to `100` players to the same five-location score-comparison game. Source: GeoGuessr Live Challenge doc.

Direct conclusion:

- published large counts in browser-first systems are usually attached to:
  - one shared prompt timeline
  - lightweight or bounded submissions
  - aggregated comparison or voting

Prix-relevant inference:

- if Prix wants larger live participation later, the likely scalable branch is not "everyone is a rich, fully symmetric actor"
- it is "everyone answers or votes on the shared beat, then the system aggregates or stages reveals"

### 5. Moderation surfaces are integrated into the runtime, not bolted on as post-processing

- `Jackbox` added room-code hiding, passworded games, Require Twitch, VIP censoring/moderation, family-friendly and profanity filters, and extended timers for stream delay. Source: Jackbox GDC talk + Pack 8 blog.
- `Mentimeter` exposes both a profanity filter and a pre-display Q&A approval queue. It notes profanity filtering is imperfect and recommends using other slide types when risk is high. Source: Mentimeter profanity + Q&A moderation docs.
- `Slido` moderation keeps questions in `In review` until approved; participants see `Waiting for review`, and edits can return a question to review. Source: Slido moderation doc.
- `GeoGuessr` exposes both lobby-level banning and in-game kicking for Live Challenge, with chat-driven kick tooling. Source: GeoGuessr kick/ban docs.

Direct conclusion:

- moderation in these systems is part of the live control loop
- publish-to-audience is often a gated transition, not an automatic consequence of submission

Prix-relevant inference:

- any UGC-heavy Prix mode should treat "submitted", "approved for local host", and "revealed publicly" as separate states

### 6. Event container, room, and active interaction instance are often different objects

- `Slido` directly exposes one slido with up to `200` rooms, separate polling/Q&A per room, room activation/deactivation, permanent links to specific rooms, and participant room switching. Source: Slido multiple rooms doc.
- `GeoGuessr` directly exposes a `Party` container with multiple game-lobbies, and notes that one player can create only one game-lobby within a party; running multiple game-lobbies at the same time requires more than one Pro account starting them. Source: GeoGuessr private lobby doc.
- `Kahoot` distinguishes live sessions from assignments, which already implies a container/experience split even though the support docs do not frame it architecturally. Source: Kahoot PIN/join docs.

Direct conclusion:

- mature browser participation products often separate:
  - the broader event/container
  - one or more joinable rooms or lobbies
  - the currently running poll/quiz/game phase

Prix-relevant inference:

- `room` should probably not be the only session object in Prix
- a future race-weekend or party-night shell likely wants a container that can hold multiple rounds, lobbies, finalists, or side activities

### 7. Rejoin and continuity policy are mode-specific and sometimes intentionally lossy

- `Kahoot` says live players can join late while the PIN is visible and entry is unlocked; one host doc says reconnecting players may resume with the same nickname and score, while the team-mode doc says team-mode rejoins reset nickname and score. Source: Kahoot host doc + team mode doc.
- `Mentimeter` quiz docs say devices are remembered so returning quiz participants are automatically assigned the same avatar and nickname. Source: Mentimeter quiz competition doc.
- `GeoGuessr` exposes host kick and lobby ban controls rather than deep continuity behavior. Source: GeoGuessr kick/ban docs.

Direct conclusion:

- rejoin behavior is not globally uniform even inside one product
- identity continuity, score continuity, and room continuity are separable policies

Prix-relevant inference:

- Prix should not hardcode a single rejoin model
- different mode families likely need different policies for:
  - same identity?
  - same score?
  - rejoin in audience only?
  - late join allowed only between phases?

### 8. There is direct evidence that "show everything on every device" changes bandwidth and timing behavior

- `Mentimeter` recommends bandwidth based on participant count and names separate realtime and quiz endpoints, plus WebSockets over HTTPS on specific domains. Source: Mentimeter requirements + access-troubleshooting docs.
- `Kahoot` explicitly warns that enabling questions on every participant device raises bandwidth because devices preload media simultaneously; it can also cause some devices to see questions later than others. Source: Kahoot question-on-device doc.
- `Jackbox` engineering commentary for Party Pack 10 calls out new engineering problems created by simultaneous typing visibility and multi-device instrument sync. Source: Jackbox engineering edition blog.

Direct conclusion:

- richer per-device presentation is not free
- synchronized shared moments become harder when more state and media move to participant devices

Prix-relevant inference:

- if Prix wants both host-screen spectacle and rich player-side UI, asset-loading and reveal-timing control need to be part of the architecture, not afterthoughts

## Concrete tradeoffs and limits

### High-confidence tradeoffs

- `audience scale` usually comes from reducing interaction density, not from letting thousands of equally privileged players act richly at once
- `shared-display clarity` and `private-device richness` pull in opposite directions; putting more on player devices improves remote accessibility but increases bandwidth, timing skew, and per-device state burden
- `UGC expressiveness` and `moderation cost` rise together; every product studied adds filters, pre-approval, gated reveal, or operator tools once public or semi-public participation enters the picture
- `stable access` and `easy memorability` are solved differently; short codes are easy to say aloud, but durable links/QRs are better for pre-sharing and remote sessions
- `participant continuity` is not one thing; products split identity persistence, scoring continuity, and room presence differently by mode

### Published limits that seem architecturally meaningful

- `Jackbox` audience up to `10,000` is meaningful mainly as evidence of a layered audience role, not as evidence that 10,000 full contestants share one symmetric game
- `Mentimeter` `2,000`-participant quiz cap versus no stated cap for other question slides is meaningful because it reveals that competitive quiz mechanics are operationally different from looser polling
- `GeoGuessr` `100`-player Live Challenge cap is meaningful because the interaction is score aggregation around shared rounds, not full mutual interaction
- `Slido` participant counting is cumulative per slido and can trigger blocking if significantly exceeded; that is operationally important because it makes reusing one event object across repeated sessions a real systems concern

### Important uncertainties

- `Jackbox` exposes controller/server traffic and outages, but not enough to say how its sessions are partitioned or what state authority model it uses
- `Kahoot` help docs reveal behavior but not whether its host surface is authoritative, merely orchestrating, or backed by more centralized control
- `Mentimeter` endpoint names suggest service separation between realtime and quiz flows, but that remains an inference unless deeper technical material is found
- `Slido` multiple rooms clearly exist, but the docs do not reveal whether rooms are isolated data partitions, routing labels on one event stream, or something in between
- `GeoGuessr` party and game-lobby docs reveal shell structure, but not the degree of server authority versus client coordination

## What seems relevant to Prix Guesser

### 1. Treat host screen, player controller, and audience wall as separate contracts

This is the clearest repeated pattern across Jackbox, Kahoot, Mentimeter, and Slido. Even when a product markets itself as "simple browser join," the public display, operator controls, and participant UI are not the same surface.

Strong implication for Prix:

- define view rights and view responsibilities per role early
- do not let the M1 host-screen implementation become the implicit truth model for all future play contexts

### 2. Model roles more richly than `host` and `player`

Published systems repeatedly expose at least:

- host/operator
- active player / responder
- audience / overflow participant
- moderator / co-host

Prix likely also wants:

- spectator-only
- maybe adjudicator / judge for certain modes later

### 3. Separate container, room, and active round instance

This appears in different forms in Slido and GeoGuessr and fits the project's own concern about not locking future party-night or race-weekend shells into one small-room assumption.

Promising Prix split:

- `event container`
  party night, circuit pack session, race-weekend shell
- `room`
  joinable cohort with roles and permissions
- `active round/game instance`
  the currently running authored experience

### 4. Plan for phase-aware join and rejoin policies

The products reviewed do not promise universal seamless continuity. They define operator-visible rules.

That suggests Prix should make join policy configurable per mode or per phase:

- pre-start join open/locked
- between-round join open/locked
- in-round late join to audience only
- kicked players banned from room vs only current round
- score-preserving rejoin vs fresh rejoin

### 5. Put moderation inside the live pipeline for any reveal-facing UGC mode

This matters less for pure geography pin drops and more for radio-text, captions, prompt-writing, or future audience chat/poll features.

The repeated published pattern is:

- submit
- hold or filter
- optionally approve
- reveal publicly

not:

- submit and instantly show to everyone

### 6. Large live F1 participation, if wanted later, should likely be built around staged aggregate beats

The evidence here does not support aiming for "one giant rich room where everyone is equally active." It supports:

- synchronized prompt beats
- individual bounded submissions
- finalist, vote, or aggregate reveal logic

That is much closer to:

- big live circuit-guess or steward-verdict events

than to:

- giant fully symmetric party rooms

## Uncertain but promising leads

- `Jackbox ecast / blobcast` history likely hides better technical precedent than current marketing docs expose. Worth a second source-hunt wave for engineering talks or older architecture notes.
- `Mentimeter` naming separate `realtime-api`, `quiz-api`, and Ably-based realtime endpoints strongly hints at distinct service paths for quiz cadence versus generic interactive slides. This is still inference, but it is one of the most promising direct technical breadcrumbs in this lane.
- `Slido` multiple-room behavior plus permanent links to specific rooms looks very relevant to any future Prix event shell with parallel tables, heats, or side rooms. More technical material is needed to know whether that should influence early data-model seams.
- `Kahoot` exposes a surprisingly strong topology menu: shared-device teams, personal-device teams, host-screen mode, and question-on-device mode. A deeper source hunt might reveal how much of that is separate products versus one underlying session model.
- `GeoGuessr` party container plus game-lobbies is highly relevant to Prix's possible circuit-pack / party-night shell, but current evidence is almost entirely support-facing. A second wave should look for official engineering or product talks around party, live challenge, or social systems.
