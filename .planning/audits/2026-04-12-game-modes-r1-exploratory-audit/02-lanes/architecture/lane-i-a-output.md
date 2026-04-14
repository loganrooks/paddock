---
date: 2026-04-13
lane: i-a
lane_name: "High-fanout browser / audience pattern research"
delegation_class: initial-architecture-research-planning
output_file: 02-lanes/architecture/lane-i-a-output.md
task_spec: 02-lanes/architecture/lane-i-a-task-spec.md
root_lane_spec: 02-lanes/architecture/lane-i-task-spec.md
ground_rules: "official-or-primary-sources-where-possible"
tags:
  - exploratory-audit
  - lane-i
  - browser
  - audience
  - host-screen
  - scaling
  - research
---

# Lane I-A: High-Fanout Browser / Audience Pattern Research

## Lane framing

This lane is about browser-first, low-latency-light participation patterns: host screen plus phones, audience voting, submit-and-aggregate, and event-style participation. That is a different scaling class from movement-heavy action rooms or hidden-info social rooms. The project already wants browser-first guests and host-screen watchability, and the current architecture notes already distinguish shared-display-plus-phone play from all-screens online sync (`.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md:33`; `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:13-24,57-64`).

The strongest recurring pattern in official sources is simple: large published counts appear when each participant sends small, discrete payloads on a shared prompt cadence. Votes, multiple-choice answers, short text, word clouds, and map guesses scale far more cleanly than continuous control or dense private state. That matters because several current F1 mode families already live in this territory: geography, `Words of Wisdom`, `Stewards' Room`, `Team Principal's Desk`, and prompt-response play all fit prompt / submit / reveal loops better than real-time action does (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:13-18,39-45,61-71,427-438`; `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:28-30`).

## Reference cases

### Jackbox

Official sources used:
- [How many players can join each game?](https://support.jackboxgames.com/hc/en-us/articles/15794756085015-How-many-players-can-join-each-game)
- [Can I play Jackbox Games remotely?](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely)
- [How does Moderation work?](https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work)
- [Jackbox Party Game Night at Your College or University](https://www.jackboxgames.com/blog/jackbox-party-game-night-at-your-college-or-university)

Jackbox is the clearest official example of the `host screen + phones + optional audience` topology. Its current support matrix still shows most titles in roughly the `3-10` active-player range, with some special cases like `Bracketeering` at `3-16` and `Lie Swatter` at `1-100`, while the same support article notes that the vast majority of games also support an audience. Jackbox's own large-group blog goes further: audience mode can extend participation to as many as `10,000`, but the audience is not doing the same thing as the core contestants. They are voting, influencing results, or trying to beat the players in specific audience-aware games, while the authored or performative core remains small.

The topology is explicit in Jackbox's docs: one person runs the game, the group watches the shared screen or stream, and participants join on `jackbox.tv` from a browser on their phones. Remote play is still basically `screen share + personal phones`, and Jackbox recommends low-latency streaming settings plus extended timers for remote games. It also treats moderation as first-class: passworded rooms, room-code hiding, Twitch-verified joining, moderator review of UGC before broadcast, and kick controls all exist because public or semi-public rooms are otherwise troll magnets.

The most useful scaling signal is not the `10,000` headline by itself. It is Jackbox's own recommendation for a `400`-person college event: split that crowd into `50` groups of `8` with separate hosts and titles rather than trying to turn one authored-text room into a `400`-player equal-participation game. In other words: Jackbox scales far by adding an audience layer and by sharding into many tables when the number of active creators gets too high.

Inference from the official setup docs: Jackbox's latency demands are low-to-moderate, not frame-critical. It still wants reasonably low stream delay and stable timers, but the interaction model is tolerant because the important transport is discrete submissions and votes rather than continuous control.

### Kahoot

Official sources used:
- [How to host a live kahoot](https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot)
- [How many participants can play a kahoot?](https://support.kahoot.com/hc/en-us/articles/115003072287-How-many-participants-can-play-a-kahoot)
- [How to enable “See questions on participant’s screen” in Kahoot! live games](https://support.kahoot.com/hc/en-us/articles/115003197928-How-to-enable-See-questions-on-participant-s-screen-in-Kahoot-live-games)
- [How to avoid connectivity issues](https://support.kahoot.com/hc/en-us/articles/115003198708-How-to-avoid-connectivity-issues)

Kahoot is a stronger example of `many equal responders to one timed prompt` than Jackbox. The host flow is PIN / link / QR based, participants can join from `kahoot.it` or the app, later joiners can still enter while the session is running, and the host can lock entry when needed. Its published participant ceilings are plan-dependent rather than universal, but the official help center currently lists live `Present` limits from the low tens on free tiers up to `2,000` on several paid tiers, with business one-time event plans going to `5,000`. Some assignment modes go higher still, which is useful precisely because async assignment is an even lighter scaling problem than live play.

Kahoot also exposes an important topology detail: it can run as classic `shared screen + phone answers`, but it also supports showing questions and answers directly on participant devices for remote play, large rooms, and accessibility. Kahoot explicitly notes that this improves large-room usability while also increasing bandwidth because participant devices now preload more content. Its connectivity article is unusually helpful: live games rely on open WebSocket connections for fast, low-bandwidth transfers between presenter and players.

The scaling lesson is that Kahoot's high counts are built on a tightly phase-driven loop. Everybody gets the same question window, the same answer window, and the same reveal cadence. There is very little pairwise state. There is also little ambiguity about authority: the host session controls the prompt timeline, and participants mostly send small state changes upstream.

Inference from the official docs: Kahoot can tolerate hundreds or thousands because the product is still fundamentally submit-and-aggregate. Even where WebSockets are used, this is not a simulation problem. It is a prompt scheduler plus fast answer collection problem.

### Mentimeter

Official sources used:
- [How many people can participate in a Mentimeter presentation?](https://help.mentimeter.com/en/articles/465589-how-many-people-can-participate-in-a-mentimeter-presentation)
- [How to participate in a Mentimeter presentation](https://help.mentimeter.com/en/articles/410537-how-to-participate-in-a-mentimeter-presentation)
- [Requirements for running Mentimeter](https://help.mentimeter.com/en/articles/410951-requirements-for-running-mentimeter)

Mentimeter is less game-shaped than Jackbox or Kahoot, but it is a clean primary-source example of large browser-first audience participation. Mentimeter says paid plans can be used with any audience size, but quiz slides cap at `2,000` participants while non-quiz question types have no limit. For events above `10,000`, Mentimeter asks presenters to notify them in advance. Joining is pure browser-first ceremony: join code at `menti.com`, QR, or direct link.

The important distinction is interaction type. Mentimeter's own participant-limit page explicitly separates quizzes from other question types, and recommends multiple-choice or open-ended slides instead of quiz slides when the crowd is larger than `2,000`. Its requirements pages also expose a practical venue-level constraint: the platform may be fine, but room Wi-Fi can become the real bottleneck, with Mentimeter giving explicit bandwidth guidance up to `1,000` participants and recommending wired presentation devices plus care around venue Wi-Fi saturation.

This is a very useful reference because it shows what truly high-fanout participation often looks like in practice: not many equal contestants performing rich authored turns, but many people submitting lightweight responses into a visible aggregate such as a poll, ranking, or open-ended text cloud.

Inference from the official docs: Mentimeter's scaling envelope is strongest when the system is aggregating many small submissions into one public artifact, not when it is trying to preserve individualized dramatic state for every participant.

### Slido

Official sources used:
- [All about one-time plans](https://community.slido.com/pricing-plan-options-235/all-about-one-time-plans-611)

Slido is another primary-source event-participation system worth studying because it makes several structural assumptions explicit. Its one-time plans support polls, quizzes, surveys, and Q&A; allow a slido to stay live for up to `7` continuous days; provide multiple rooms for parallel sessions; expose moderation, privacy, and security options; and support `200`, `1,000`, or `5,000` participants depending on plan, with higher counts handled separately. Participants can join by code, link, or QR. Slido can also be embedded into a website or event app, and can coexist with presentation and conferencing tools.

Two details matter here. First, Slido's count is event-participation count, not "5,000 fully equal active players inside a dense shared game world." Second, Slido explicitly models multiple rooms for parallel sessions. That is a reminder that large events often scale not by making one richer room huge, but by keeping an event container above several lighter-weight participation spaces.

Inference from the official docs: Slido is strongest as an audience layer, conference companion, or prompt-and-response shell. It is a good analogy for watch-party companion features, race-weekend question walls, or parallel-room club events, not for one giant hidden-info or high-authorship room.

### GeoGuessr Party / Live Challenge

Official sources used:
- [How many can I invite to my Party?](https://geoguessr.zendesk.com/hc/en-us/articles/4409656812049-How-many-can-I-invite-to-my-Party)
- [What are Live Challenges?](https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges)
- [How do I set up a Private Lobby?](https://geoguessr.zendesk.com/hc/en-us/articles/4413903235729-How-do-I-set-up-a-Private-Lobby)

GeoGuessr is the most directly relevant reference for the anchor geography fantasy. Its official help center says a `Party` can contain `100` people, but most games inside that party still cap at `10` players, with `Team Duels` at `20`. `Live Challenge` is the important exception: everyone in the party can play a five-location score challenge together, and the help article explicitly says all `100` party members can be invited into that mode. The private-lobby article also notes that bigger parties can be split into specific game lobbies by sharing direct lobby URLs, and that running multiple lobbies at the same time requires more than one Pro account.

This is the clearest official case here for `one event container, several possible room scales inside it`. GeoGuessr does not make every geography mode equally large. Instead, it keeps the `party` abstraction broad while allowing specific game types to scale differently. `Live Challenge` works at the top end because it is round-based and score-based. The richer modes stay smaller.

Inference from the official docs: geography can scale surprisingly far when everyone is solving the same clue set independently and the system mainly needs to collect guesses, compute score, and reveal standings. It scales much less cleanly if the mode depends on high-density interaction among all participants.

## What scales well in this pattern

- Shared prompt windows with centrally controlled timers scale well. Kahoot, Mentimeter, Slido, Jackbox audience play, and GeoGuessr Live Challenge all keep everyone aligned to the same round cadence instead of letting each participant advance the room independently.
- Small submissions scale well. Votes, multiple-choice, confidence picks, short text, map coordinates, and simple ratings are much easier to fan out than continuous movement or long-form authored turns.
- Audience-as-layer scales well. Jackbox's published pattern is not "make the authoring room huge"; it is "keep the core contestants small, then add a broad audience influence layer."
- Aggregation and sampling scale well. Mentimeter and Slido are strongest when the crowd becomes a poll, Q&A queue, or text cloud. That same logic applies to creative F1 modes: large rooms need highlight selection or finalist pipelines, not exhaustive broadcast of every submission.
- Room-container plus subroom scaling works well. Jackbox's college-event guide and GeoGuessr's party/lobby split both point the same way: once authorship density or host burden gets too high, shard into smaller active rooms while keeping a larger event shell around them.
- Browser-first join flows scale well when the ceremony is lightweight. PINs, codes, QR, and direct links appear across every strong case in this lane.

This lines up with the project's current text-first mode families and with the internal observation that modes like geography, `Words of Wisdom`, `Stewards' Room`, and voting-heavy formats want different phone inputs but still fit the same broad `prompt -> submit -> reveal` skeleton (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:42-55,88-103`).

## What the counts actually mean

- `10,000 audience` does not mean `10,000 equal contestants`. In Jackbox, the authored or social-performance core usually remains in the single digits even when the audience becomes huge.
- `100-party` does not necessarily mean `100-player match`. GeoGuessr's own docs split party size from specific game caps, with only certain modes such as `Live Challenge` stretching to the full party.
- `2,000` or `5,000` usually means `everyone is responding to the same staged prompt`, not `everyone has rich private state`. Kahoot, Mentimeter, and Slido all fit this pattern.
- Some counts are question-type-specific or plan-specific. Mentimeter's quiz cap differs from its non-quiz slide behavior. Kahoot's live caps differ by plan and account type. Slido's participant count depends on plan and treats every joined participant as part of the total.
- Large-room participation is often as much a venue and moderation problem as an application-server problem. Mentimeter explicitly calls out venue Wi-Fi load. Jackbox explicitly calls out moderation, room-code security, and gatekeeping for public streams.

The practical translation is: published high counts usually mean `broad lightweight participation`, not `broad rich interaction`.

## Relevance to possible F1 modes

- `Circuit / venue guesser at scale` is plausible, but likely in a GeoGuessr/Kahoot shape rather than a dense shared-room shape. A large-room version would look like everyone guessing from the same clue set within a timed round, then receiving a leaderboard and reveal. That fits the project's anchor geography fantasy, but the high-count form should stay round-based and independent per player rather than trying to make `50+` people co-occupy one elaborate shared reveal flow (`.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md:33`; `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:52-55`).

- `Words of Wisdom` is plausible for large rooms only if it changes shape. The current core mechanic is great for small private groups because friends generate the content (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:13-18`; `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:170-172`). At larger sizes, the obvious fit is `small core writers + broad audience voters`, or `everybody answers a lighter version while only sampled responses hit the host screen`. A `100`-person equal-text-authoring WoW room would create moderation and pacing problems very quickly.

- `Stewards' Room` and `Team Principal's Desk` may be the cleanest large-room fits in the current F1 portfolio. They are already prompt-based judgment modes rather than movement or hidden-info modes, and the fun often lives in seeing the room split, not in preserving deeply individualized state (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:39-45,61-71`). They map naturally to Kahoot/Mentimeter/Slido patterns: verdict polls, confidence picks, live prediction rounds, and race-weekend companion sessions.

- `Paddock Fashion` and `Meme Prompts` can use the pattern, but only selectively. Their private-room strength is that player-generated content is the game (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:376-401,427-438`; `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:170-172`). A larger event version should therefore look like `submit privately -> pick finalists -> runway / reveal / audience vote`, not `force the host screen to meaningfully display every entry`.

- `Commentary clip ID` and `crowd reaction ID` are plausible high-fanout event modes because they can be reduced to short audio prompt plus guess / confidence / multiple-choice answer (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:361-366`). They fit the Kahoot / Mentimeter class much better than the Jackbox authored-text class.

- `Pit Stop Co-op`, the predator-hunter driving family, and likely `The Grid Walk` should not be forced into this lane's scaling pattern. Those are either movement-heavy or hidden-info-heavy and belong in the other large-room research lanes (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:75-92,459-472`; `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:38-39`).

## Early architectural implications

- Model participation roles explicitly. `host`, `core_player`, `audience`, `spectator`, and `moderator` should be capability sets, not ad hoc flags. This follows directly from the internal concern about singular fixed host roles and equal-information assumptions, and it is reinforced by Jackbox and Slido's public moderation and audience layers (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:198-206`; Jackbox moderation docs; Slido one-time plan docs).

- Separate the event container from the active game instance. GeoGuessr's `party` versus specific lobbies and Jackbox's campus-event sharding both point toward the same protection: one code or event should be able to contain multiple active rooms, heats, or tables without pretending they are one fully shared match (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:198-204`).

- Treat discrete-response transport as its own substrate. This lane mostly needs `submit answer`, `submit text`, `vote`, `send confidence`, `place pin`, and `acknowledge reveal`, not continuous control. The internal architecture notes already separate abstract game actions from raw device input; this lane argues that low-frequency response transport should stay distinct from any future action-netcode path (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:57-64,88-103,185-188`).

- Build a reusable prompt / reveal scheduler. The common large-room browser pattern is `join window -> prompt -> submission -> lock -> reveal -> score -> next round`. Geography, WoW variants, steward verdicts, strategy polls, and audio-identification rounds can all sit on that spine even if their inputs differ (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:42-55,90-97`).

- Separate private pending submissions from public aggregates and public reveals. Large-room systems usually keep raw participant responses private until a reveal or aggregate step. That matches the internal warning about role-based visibility control and future spectator asymmetry (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:206`).

- Plan for moderation and sampling before broadcast. If a future F1 event mode includes free text or image creation at anything beyond a small private room, the platform needs either moderator review, automated filtering, finalist selection, or all three. Jackbox's tooling is the clearest proof that this becomes necessary quickly once UGC meets public audience.

- Keep join / rejoin / lock behavior abstract. PIN, code, QR, direct link, late join, lock room, password, and maybe verified identity all recur in the official products studied here. The project's own join-flow notes already point toward this seam; this lane strengthens the case that it is cheap insurance, not overengineering (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:72-84,198-204,216`).

- Preserve a low-capability participant path. The highest-fanout browser cases assume that almost everyone can join from a normal phone browser with little more than text, taps, and maybe media playback. If future large-room F1 audience modes require gyroscope, WebGL, or dense canvas interaction on every device, they will narrow the scaling path sharply (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:210`).

These implications do not argue for building `5,000`-person infrastructure in M1. They argue for avoiding early substrate choices that make audience roles, prompt-driven event modes, room sharding, or moderator-reviewed UGC awkward later.

## Uncertainties and limits

- Several published counts are commercial plan limits, not engineering postmortems. They are still useful signals, but they are not hard technical ceilings.
- The official sources here are mostly support, help-center, and vendor blog materials. They are primary sources for product behavior, but not deep architecture disclosures.
- Latency assessments in this document are partly inference from official interaction design and networking guidance, not direct source claims.
- Venue networking can be the first real bottleneck well before application limits are hit. Mentimeter is unusually explicit about this, but the lesson likely generalizes.
- Some GeoGuessr party documentation is older than the Jackbox/Kahoot/Mentimeter materials. I used currently published help-center articles, but those limits could change.
- Large-room browser participation says little about whether those modes are the best product direction. It only shows which future F1 mode families could plausibly inhabit this scaling shape if the project wants them to.

Official sources above were accessed on 2026-04-13.
