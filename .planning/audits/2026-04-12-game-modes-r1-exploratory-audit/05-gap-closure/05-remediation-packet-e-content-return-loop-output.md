---
date: 2026-04-14
audit_subject: remediation_packet
audit_orientation: exploratory
audit_delegation: self
scope: "Content supply model, recurrence layers, and first repeat-return loop with direct outside-repo grounding"
triggered_by: "05-remediation-packet-e-content-return-loop-task-spec.md"
tags:
  - exploratory-audit
  - gap-closure
  - remediation
  - content
  - recurrence
  - retention
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-remediation-packet-e-content-return-loop-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-remediation-packet-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-next-round-gap-opportunity-register.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-lane-a-content-flywheel-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-lane-b-recurrence-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-reference-patterns-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-context-and-plan.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
external_sources:
  - https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely
  - https://support.jackboxgames.com/hc/en-us/articles/15794771245975-How-do-I-get-started-playing-Jackbox-Games
  - https://www.jackboxgames.com/games/the-jackbox-survey-scramble
  - https://www.jackboxgames.com/blog/how-to-stream-the-jackbox-survey-scramble
  - https://geoguessr.zendesk.com/hc/en-us/articles/360017579277-What-is-Explorer-Mode
  - https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge
  - https://geoguessr.zendesk.com/hc/en-us/articles/4407923951249-How-does-Event-work
  - https://geoguessr.zendesk.com/hc/en-us/articles/360019558397-Why-did-I-not-get-a-Medal-in-Explorer-Mode
  - https://geoguessr.zendesk.com/hc/en-us/articles/360017613357-Where-can-I-find-maps-to-play
  - https://geoguessr.zendesk.com/hc/en-us/articles/360017720578-How-do-I-create-a-Map
  - https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz
  - https://geoguessr.zendesk.com/hc/en-us/articles/9487018842129-What-are-Badges
  - https://support.chess.com/en/articles/8705902-what-does-my-stats-page-show
  - https://support.chess.com/en/articles/8584089-how-does-game-review-work
  - https://support.chess.com/en/articles/8598090-how-do-i-view-my-own-games
  - https://support.chess.com/en/articles/8618477-how-can-i-see-my-previous-puzzles-and-puzzle-rush-games
  - https://support.chess.com/en/articles/8708990-how-do-i-find-the-daily-puzzle
  - https://support.chess.com/en/articles/9714718-what-are-streaks
  - https://m.chessapp.com/article/view/daily-puzzle-curator
---

# 05 Remediation Packet E: Content Supply And First Repeat-Return Loop

## Packet framing

- Mode: `solution evaluation`
- Classification: `initial architecture research/planning`
- Question: what content operation should Prix Guesser actually preserve, and which repeat-return loop should matter first once direct outside grounding is added
- Scope:
  - evergreen library growth vs authored/editorial drop models
  - replay/review as a recurrence surface
  - room folklore, personal mastery, editorial return, and event carry-over
  - how those branches translate across local recurring party, private online sync, solo ritual, and bounded event shells
- Non-goals:
  - not the full community-shell ordering question
  - not support / premium / hosting posture
  - not exact daily / weekly / race-weekend taxonomy
  - not a final public contribution or discovery policy
- Stop condition: enough direct external grounding to decide the first content/return stack and to state the remaining open seams honestly
- Artifacts read:
  - `05-remediation-packet-e-content-return-loop-task-spec.md`
  - `05-remediation-packet-common-scaffold.md`
  - `05-next-round-gap-opportunity-register.md`
  - `05-gap-closure-lane-a-content-flywheel-output.md`
  - `05-gap-closure-lane-b-recurrence-output.md`
  - `05-gap-closure-reference-patterns-output.md`
  - `05-gap-closure-context-and-plan.md`
  - `.planning/PROJECT.md`
  - `.planning/LONG-ARC.md`
  - `.planning/ROADMAP.md`
  - `.planning/REQUIREMENTS.md`

`[governing:cited:internal]` Repo-local lane outputs remain prior synthesis and doctrine inputs, not direct external grounding. External comparisons below are grounded only in the direct outside sources listed in `Direct external source register`.

## Gap justification

This packet exists to address:

- `GCO-00`
- `GCO-00A`
- `GCO-08B`
- `GCO-08C`
- `GCO-08D`
- `GCO-08E`
- `GCO-09`
- `GCO-09A`
- `GCO-09B`

Why these belong together:

- `GCO-00A` and `GCO-08D` are the core substantive gap: the project still lacks a closure-grade answer about its content supply model and its first repeat-return loop.
- `GCO-08B`, `GCO-08C`, and `GCO-08E` are required translation work: the answer is not good enough unless it varies by archetype, separates first-value from later-value, and turns memory seams into actual surfaces.
- `GCO-09`, `GCO-09A`, and `GCO-09B` are methodological load-bearers for this packet: the question was previously over-closed partly because internal synthesis looked more externally grounded than it really was.
- `GCO-00` applies because this packet cannot speak as if one universal user posture exists; local recurring party, private online sync, solo ritual, and bounded event shells do not carry the same burden or extract the same value.

This packet is not trying to close:

- the full wrapper/community-shell ordering question
- support, premium, or hosting ladders
- the full contribution/discovery lane
- final cadence naming

## What is already settled

`[governing:cited:internal]` The following doctrine is already settled and constrains this packet rather than being reopened:

- the product center is still a private, watchable, browser-first ritual for trusted groups rather than ambient public discovery (`PROJECT.md:96,107-108,142-144`; `LONG-ARC.md:17-18,81`; `ROADMAP.md:13-15`)
- the initial release is curated-pack-first with calibration, not exhaustive coverage or open publishing (`PROJECT.md:96`; `ROADMAP.md:171-186`; `REQUIREMENTS.md:18`)
- memory and cadence must stay layered: player history, room/group memory, event memory, and content calibration/history are not one ledger; session pacing, editorial rhythm, and event cadence are not one clock (`PROJECT.md:142-144`; `LONG-ARC.md:62-63`; `REQUIREMENTS.md:135`)
- Lane A already argued that the best internal carry-forward is `curated evergreen library` plus `selective editorial spotlight`, with `trusted-private contribution` preserved as a future seam and a public creator ecosystem deferred (`05-gap-closure-lane-a-content-flywheel-output.md:241-244,270-273`)
- Lane B already argued that `room folklore` is the first emotional recurrence layer, `personal mastery plus review` is the first scalable between-session layer, `editorial cadence` is a prompt layer, and `event cadence` is an amplifier rather than the base (`05-gap-closure-lane-b-recurrence-output.md:131-143,159-171,260-263`)

`[assumed:reasoned:internal]` This packet therefore is not inventing a new worldview. It is testing whether direct external grounding strengthens, weakens, or reframes those earlier internal conclusions.

## Path of inquiry

- Entry point:
  - the remediation packet spec and its requirement to reopen content supply and first-repeat-return comparisons with direct outside grounding
- Branches considered:
  - evergreen library growth as the base content operation
  - authored/editorial daily or monthly drops as the base content operation
  - community-refreshed or contribution-led supply as the base content operation
  - room folklore, review/replay, personal mastery, editorial return, and event carry-over as candidate first repeat-return loops
- Branches pursued:
  - `Jackbox` for private session-first party loops, audience extension, and public moderation cost
  - `GeoGuessr` for evergreen mastery, community maps, friend challenges, daily challenge, and time-boxed events inside one geography product
  - `Chess.com` for review/history/mastery surfaces, daily puzzle recurrence, streaks, and explicit editorial curation burden
- Branches deferred or abandoned:
  - open-publishing platform examples such as Roblox/Steam Workshop because this packet is not closing the broader discovery/governance lane
  - generalized live-service games because they over-index on large-scale event ops that are outside this packet's scope
  - full public community or streamer-shell comparison because that belongs to the wrapper-shell packet
- Unexpected reframing:
  - outside grounding strengthened the previous distinction between `first emotional loop` and `first product-controlled repeat-return loop`
  - replay/review survived the comparison, but as bridge infrastructure rather than as a viable standalone retention pillar
  - editorial return remained real, but the external evidence made its operator burden more concrete than the local bundle had

## Direct external source register

| Source | Type | What it directly grounds here | Why it matters |
| --- | --- | --- | --- |
| Jackbox remote-play + getting-started docs | official support | no matchmaking, one host copy, remote play via screen-sharing, browser controllers, lightweight cookie-based past-game history | good model of `room folklore first`, but weak proof of a product-controlled between-session loop |
| Jackbox Survey Scramble product + streaming docs | official product + official blog | community-refreshed answer pool, 2-10 players plus large audience, public moderation controls, answer-recording fragility | useful caution for community-refreshed content and eventized audience shells |
| GeoGuessr Explorer / Badges / Maps / Create Map / Create Challenge docs | official help | evergreen mastery, achievements, official + community maps, user map creation, challenge sharing, public leaderboard / anonymous options | strong grounding for library growth plus optional contribution seams |
| GeoGuessr Daily Challenge / Events / Explorer medal restriction docs | official help | daily shared challenge, time-boxed event layer, and separation between mastery progression vs challenge/event shells | directly useful for first-value vs later-value and for memory-layer separation |
| Chess.com Stats / Game Review / Archive / previous puzzles docs | official help | review history, searchable archive, performance stats, replayable past puzzles | strongest direct grounding for `review -> mastery` as a bridge loop |
| Chess.com Daily Puzzle / Streaks / Daily Puzzle curator article | official help + official editorial article | daily pulse, previous-puzzle archive, streaks, daily curation burden, community submission-to-curator pattern | strongest direct grounding for editorial return as a real but non-trivial content operation |

## Reference translation

- `Jackbox`:
  - analogous:
    - host-led private group ritual
    - audience as a wrapper around a private core
    - recurrence driven first by people wanting to gather again
  - not analogous:
    - Jackbox is not a place-recognition/mastery product
    - its content is not organized around a deep evergreen world/library to the same extent Prix Guesser likely will be
  - borrowed as concern:
    - if group ritual is the only return engine, the product itself may not reach back between sessions
    - public-input or public-audience layers immediately create moderation settings and code-safety concerns

- `GeoGuessr`:
  - analogous:
    - geography-centered recognition product with multiple recurrence layers living side by side
    - evergreen map library, friend challenges, daily shared pulse, and time-boxed events all coexist in one surface
  - not analogous:
    - GeoGuessr is much more public, competitive, and globally scaled than Prix Guesser's current posture
    - its content base is wider and less tightly authored than Prix Guesser's intended pack model
  - borrowed as concern:
    - social challenge, mastery progression, and event cadence should not be collapsed into one results/memory system by default

- `Chess.com`:
  - analogous:
    - review/history/stat surfaces that convert a completed session into future mastery
    - editorial daily content layered on top of a larger evergreen practice system
  - not analogous:
    - chess is a pure skill game with deeper competitive-account posture than Prix Guesser needs
    - some of its progression depth would be too heavy for the current private-first product
  - borrowed as concern:
    - review is valuable when it feeds mastery, not when it dead-ends in a static summary screen
    - daily editorial cadence is an actual content operation with curation, explainers, and audience expectation

## Negative-case / failure evidence note

`[evidenced:cited:external]` The outside sources surfaced three relevant failure-mode families:

- `room-folklore-only products under-own between-session return`
  - Jackbox explicitly says its games do not offer online matchmaking and remote play depends on screen-sharing or third-party voice/video tools.
  - inference: group ritual can be strong, but the product itself may do little to create between-session pull once the room disperses.

- `community-refreshed content creates immediate moderation and data-hygiene burden`
  - Survey Scramble's own streaming guide recommends profanity filtering, moderation, and hiding full answer displays in public play; it also warns that quitting incorrectly can prevent submitted survey answers from being recorded.
  - inference: content refreshed by player submission is not a free freshness engine; it creates moderation, operational, and pipeline integrity burden immediately.

- `event and challenge shells do not automatically belong inside the mastery ledger`
  - GeoGuessr says Events use custom maps/settings for a specific time frame and do not affect rank, and that Explorer medals require a single-player run rather than a Challenge.
  - inference: if Prix Guesser wants event memory, social challenges, and mastery progression, it should expect to separate those ledgers intentionally rather than assuming they collapse cleanly.

`[evidenced:cited:external]` A fourth burden signal is narrower but still useful:

- `editorial daily content is a real staffed operation`
  - Chess.com's Daily Puzzle curator describes serving more than one million daily solvers, weekly difficulty shaping, video explainers, and community idea intake.
  - inference: an editorial-return-first strategy is not lightweight garnish; it commits the product to a meaningful and ongoing content pipeline.

## Live alternatives

### Content-supply model alternatives

| Branch | What it optimizes | Strongest direct grounding | Burden read | Current judgment |
| --- | --- | --- | --- | --- |
| `evergreen library growth` | reusable place knowledge, deeper pack corpus, calibration and long-horizon mastery | GeoGuessr Explorer / maps / badges; Chess archive + replayable previous puzzles | moderate and compounding rather than constant deadline-driven | strongest base |
| `editorial drops / daily pulse` | timeliness, ritual, reason to check back now | GeoGuessr Daily Challenge + Events; Chess Daily Puzzle + curator article | high recurring authoring and explanation burden | good overlay, weak base |
| `community-refreshed / contribution-led` | freshness and scale beyond core staff | GeoGuessr map maker + challenge creation; Survey Scramble answer submission | moderation, review, endorsement, and ingestion burden | preserve seam, not first |

### First repeat-return alternatives

| Candidate | What it gives first | Strongest direct grounding | Main weakness | Current judgment |
| --- | --- | --- | --- | --- |
| `room folklore` | the emotional reason a trusted group wants to reconvene | Jackbox private-host ritual and audience wrapper | depends on a group deciding to regroup; weak product-controlled between-session reach | essential emotional layer, not sufficient as the first system loop |
| `review / replay` | a bridge from finished session to reflection and future intent | Chess archive / Game Review / previous puzzles | weak as a standalone loop if it does not feed skill, memory, or reconvening | required connective surface, not the primary engine |
| `personal mastery` | a private reason to return between sessions | GeoGuessr Explorer + Badges; Chess Stats + Game Review | can drift into grind if it loses editorial texture or social context | best first product-controlled loop |
| `editorial return` | a timed prompt to check back today / this weekend | Chess Daily Puzzle; GeoGuessr Daily Challenge | creates recurring content obligation and brittle dependence on cadence | important prompt layer after the base exists |
| `event carry-over` | appointment energy, event memory, showcase-ready recurrence | GeoGuessr Events; Survey Scramble public-stream posture | later-shell burden, not universal across archetypes | amplifier later, not first |

## Findings

### 1. The strongest directly grounded base content operation is still `curated evergreen library growth`, not `editorial-first publishing`

#### Direct evidence

- GeoGuessr keeps an evergreen geography core through Explorer Mode, Badges, official maps, community maps, and map creation.
- GeoGuessr's help center exposes separate surfaces for `Explorer`, `Daily Challenge`, `Events`, `Maps`, and `Create Map`, which implies the library exists independently of the daily/event layer.
- Chess.com exposes archives, replayable past puzzles, and stats in addition to its Daily Puzzle, which means its daily editorial surface sits on top of a broader reusable practice/history system.

#### Inference and interpretation

- The most defensible content base for Prix Guesser is still a curated circuit/venue/era library that grows, sharpens, and gets better tagged over time.
- Outside grounding made this stronger, not weaker: the products with the healthiest recurrence stacks separate evergreen learning/library depth from timed prompt layers rather than making timed prompt layers do all the work.
- For Prix Guesser, that means `starter packs plus calibration plus library growth` remains the right base answer (`PROJECT.md:96`; `ROADMAP.md:171-186`; `REQUIREMENTS.md:18`).

#### Unknowns

- how quickly the evergreen library must widen beyond starter packs before it feels meaningfully replayable
- the exact pack-state taxonomy that should ship first

### 2. `Room folklore` survives as the first emotional recurrence layer, but not as the first product-controlled repeat-return loop

#### Direct evidence

- Jackbox's support posture is explicit: one host owns the game, friends join on browsers/phones, remote play uses screen-sharing, and there is no online matchmaking.
- Jackbox preserves lightweight memory through cookie-based access to past games on the device used to play, but it does not provide a deeper built-in between-session mastery system from those same docs.

#### Inference and interpretation

- This strongly supports the earlier local conclusion from Lane B: room folklore is a real good, especially for local recurring party and private online sync.
- It also confirms the limit: if Prix Guesser stops at `people had a good night and might schedule another one`, then the product has not really built a repeat-return loop it controls.
- `room folklore` should therefore be treated as the emotional start of recurrence, not the whole answer.

#### Unknowns

- how much explicit room/group-memory UI is needed early versus how much can remain implicit in recap/rematch flow

### 3. `Review / replay` should be treated as bridge infrastructure that converts a social session into personal mastery

#### Direct evidence

- Chess.com exposes `Game Review`, a full searchable `Archive`, replayable recent puzzles, and detailed `Stats`.
- Chess.com's streak system counts solving a puzzle, completing a game, or running a `Game Review` as valid continuity actions.
- Jackbox keeps lightweight past-game access on-device, which shows even a room-first product benefits from some replayable residue.

#### Inference and interpretation

- The best external pattern is not `review as standalone retention`.
- The useful pattern is `review as bridge`: finished session -> inspect what happened -> understand why -> build intent to return.
- This directly reinforces `RET-04` and the local Lane B judgment that replay/review is connective tissue rather than its own pillar (`REQUIREMENTS.md:101-102`; `05-gap-closure-lane-b-recurrence-output.md:143-152`).

#### Unknowns

- whether the first review surface should skew more toward `room recap` or `player mastery recap`
- how much explanation depth is needed beyond round outcomes and reveal reasoning

### 4. The strongest first product-controlled repeat-return loop is `review-backed personal mastery`, not `editorial return` or `event carry-over`

#### Direct evidence

- GeoGuessr's Explorer medals require single-player play rather than Challenges, which keeps mastery progression separate from friend-challenge shells.
- GeoGuessr Badges reward time spent in and around gameplay, giving a second mastery/achievement layer distinct from event ranking.
- Chess.com Stats, Archive, Game Review, previous puzzles, and Streaks all reinforce a loop where past activity feeds the next practice decision.

#### Inference and interpretation

- The best first loop Prix Guesser can own is:
  - `play a private session`
  - `leave a reviewable recap`
  - `turn recap into player-facing mastery or recognition depth`
  - `use that mastery to motivate the next private or solo return`
- In short:
  - `session -> review -> mastery return -> next session`
- This is more precise than the previous local phrasing because the outside grounding made the `mastery ledger` vs `challenge/event ledger` split much clearer.

#### Unknowns

- the first mastery metric
  - circuit completion
  - venue familiarity
  - clue-type accuracy
  - era mastery
  - some mixed profile

### 5. `Editorial return` is real and valuable, but it is too burden-heavy to be the base content engine

#### Direct evidence

- GeoGuessr Daily Challenge offers one shared daily world challenge.
- GeoGuessr Events are time-boxed, custom-map/custom-setting surfaces and do not affect rank.
- Chess.com's Daily Puzzle has past-puzzle access, streaks, daily timing, and an explicit curator-plus-explainer operation serving more than one million daily solvers.

#### Inference and interpretation

- Editorial cadence is not fake value. It clearly produces ritual, shared timing, and a reason to check back now.
- But the direct evidence also makes its burden undeniable: timed content requires curation, difficulty shaping, explanation, and expectation management.
- For Prix Guesser this pushes editorial return into `bounded spotlight / race-weekend prompt / featured pack resurfacing`, not `the thing that must exist for the product to be alive`.

#### Unknowns

- whether the first editorial layer should be `race-weekend spotlight`, `occasional featured pack`, or a lighter mixed prompt model

### 6. `Event carry-over` should attach to its own memory layer, not replace the base return model

#### Direct evidence

- GeoGuessr Events are explicitly time-bound, custom, and rank-separate.
- Survey Scramble's public-stream posture shows that once audience/event participation is widened, moderation and controls become first-class product work.

#### Inference and interpretation

- Prix Guesser should treat event carry-over as a later wrapper memory layer:
  - weekend board
  - featured challenge recap
  - hosted event results
  - maybe later showcase folklore
- It should not treat event carry-over as the first return engine for the mature product.

#### Unknowns

- which later event shell, if any, deserves explicit persistence before the wrapper-shell packet closes

### 7. `Community-assisted contribution` remains worth preserving, but the direct evidence argues against using it as the first supply answer

#### Direct evidence

- GeoGuessr exposes community maps, map creation, and Create Challenge with public leaderboard / anonymize-nickname controls.
- Survey Scramble shows player-submitted content can keep a pool changing, but only with moderation controls and operational care.
- Chess.com's Daily Puzzle curator describes a curated intake model where community members contribute ideas but a central editor shapes the final artifact.

#### Inference and interpretation

- The outside grounding does not support `open creator ecosystem first`.
- It does support `later trusted-private or curated contribution seam`:
  - submissions
  - imported packs
  - curated challenges
  - maybe later editorial intake
- This strengthens the earlier Lane A conclusion rather than weakening it.

#### Unknowns

- whether the first contribution seam should be `trusted instance-to-instance pack exchange` or `editorial intake of outside ideas`

## Dependencies and relations

| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| `curated evergreen library` | pack authoring, validation, calibration capture | every later recurrence surface | medium if metadata and pack-state language stay vague |
| `review-backed mastery loop` | recap/history surfaces, stable identifiers, explainable reveals | first repeat-return story, solo wrapper viability | medium-high if recap is too shallow |
| `room/group memory` | recurring private groups and rematch flow | local recurring party and private online sync recurrence | medium because it is real but group-scheduling-dependent |
| `editorial spotlight` | library base plus operator cadence capacity | race-weekend prompts, featured resurfacing | high because it creates recurring content obligation |
| `event carry-over` | bounded event shell plus moderation/ops posture | later showcase/community memory | high because it imports wrapper burden quickly |
| `trusted-private contribution seam` | import/export tooling, preview, review policy | later content scale and private sharing | high because endorsement and moderation lines appear fast |

## What can close now

- The base content operation can close as:
  - `curated evergreen library growth with calibration`
- The first product-controlled repeat-return loop can close as:
  - `session recap/review -> private mastery return -> next trusted session`
- `room folklore` can close as:
  - first emotional recurrence layer
  - not sufficient by itself as the first system loop
- `editorial return` can close as:
  - bounded prompt / spotlight layer
  - not the base content engine
- `event carry-over` can close as:
  - later amplifier layer with its own memory surface
- `community-assisted contribution` can close as:
  - preserve-a-seam-later
  - not the first operating model

## First-value vs later-value

| Branch | First-value | Later-value | Preserve without prioritizing |
| --- | --- | --- | --- |
| `curated evergreen library growth` | very high | very high | no |
| `review-backed mastery return` | very high | very high | no |
| `room folklore` | high emotionally, medium systemically | high | no |
| `editorial spotlight / race-weekend prompting` | medium | high | no |
| `event carry-over` | low | medium-high in bounded shells | yes |
| `trusted-private contribution` | low | medium-high if authoring matures | yes |
| `open/public contribution ecosystem` | very low | unresolved | yes, but explicitly deferred |

`[assumed:reasoned]` The key split is this:

- `first-value`:
  - evergreen library
  - review-backed mastery
  - lightweight room folklore support
- `later-value`:
  - editorial cadence
  - event carry-over
  - broader contribution/discovery

## Archetype-to-burden translation

| Branch | Local recurring party | Private online sync | Solo ritual | Bounded event shell | Burden translation |
| --- | --- | --- | --- | --- | --- |
| `room folklore` | strongest | strong | weak | medium | needs recap/rematch and group memory, but mostly lives on recurring-group behavior |
| `review-backed mastery` | medium-high | high | strongest | medium | needs player-facing history and explanation, but works without publicness |
| `editorial spotlight` | medium | medium | high | high | requires schedule, pack-state curation, and expectation management |
| `event carry-over` | low | low-medium | medium | strongest | requires event object, moderation rules, and a reason not to merge with mastery/history |
| `trusted-private contribution` | low | medium | low-medium | medium | requires review/import rules, not just file upload |

`[assumed:reasoned]` This packet's recommendation is archetype-aware in a narrow but important sense:

- the first emotional proof still belongs to trusted-group play
- the first scalable between-session loop belongs to solo/private mastery
- the first editorial/event surfaces belong later because they are archetype-selective and more burden-heavy

## Trigger conditions

| Later branch | Trigger condition before it should be prioritized |
| --- | --- |
| `editorial spotlight` | the evergreen library is large enough that resurfacing feels like value rather than camouflage for scarcity |
| `race-weekend / event carry-over` | there is a clear event object and recap surface that can hold event memory without overwriting mastery history |
| `trusted-private pack exchange` | preview/import/export and validation exist, and the project can review or bound what it is willing to surface |
| `curated external submissions` | there is an explicit endorsement rule and enough editorial capacity to reject, revise, or retire outside material |
| `heavier room/group memory` | recurring groups are common enough that recap/rematch no longer carries the whole social-memory burden |

## Recommended carry-forward

- Treat the content machine as:
  - `curated evergreen circuit/venue library`
  - `calibration and revision loop`
  - `bounded editorial spotlight layer`
  - `trusted-private contribution seam held open`
- Treat the first repeat-return loop as:
  - `play together -> review what happened -> return privately to improve / revisit -> reconvene`
- Build replay/review surfaces as:
  - bridge infrastructure
  - not terminal summary screens
- Keep memory layers separate in user-facing form:
  - `room recap / rematch`
  - `player mastery history`
  - `event board / featured-weekend recap`
  - `library / pack state`
- Do not let `daily challenge`, `race-weekend event`, or `community contribution` become the hidden first answer merely because they are vivid or easy to talk about.

## Explicit deferrals

- exact cadence labels and frequencies
- the first mastery metric
- the exact depth of room/group memory beyond recap/rematch
- which later event shell should arrive first
- public creator publishing, marketplace logic, or broad discovery
- support/premium/hosting implications of the later editorial or contribution layers

## What should remain open

- whether the first visible mastery surface is `completion`, `accuracy trend`, `collection depth`, or a mixed profile
- whether `editorial spotlight` first means a race-weekend feature, a featured evergreen pack, or both
- how much room/group memory needs explicit naming beyond recap/rematch before the wrapper-shell packet resolves
- the exact trusted-private contribution posture
- the final shape of any event-memory surface

## What later converged synthesis must reconcile

- this packet's `review-backed mastery first` verdict with the wrapper-shell packet's later community/event-shell ordering
- the content packet's `trusted-private contribution seam` with the contribution/discovery packet's governance and endorsement posture
- the `editorial spotlight later` judgment with the promise/support ladder so the project does not accidentally promise more cadence than it can sustain
- the memory-surface split here with host ecology and authority planning so `room`, `event`, `history`, and `content` do not collapse back into one ledger in canon language

## Sources

### Local

- `05-remediation-packet-e-content-return-loop-task-spec.md`
- `05-remediation-packet-common-scaffold.md`
- `05-next-round-gap-opportunity-register.md`
- `05-gap-closure-lane-a-content-flywheel-output.md`
- `05-gap-closure-lane-b-recurrence-output.md`
- `05-gap-closure-reference-patterns-output.md`
- `05-gap-closure-context-and-plan.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`

### External

- Jackbox Games support:
  - `Can I play Jackbox Games remotely?`
  - `How do I get started playing Jackbox Games?`
- Jackbox Games:
  - `The Jackbox Survey Scramble`
  - `How To Stream The Jackbox Survey Scramble`
- GeoGuessr help:
  - `What is Explorer Mode?`
  - `What is the Daily Challenge?`
  - `How does Event work?`
  - `Why did I not get a Medal in Explorer Mode?`
  - `Where can I find maps to play?`
  - `How do I create a Map?`
  - `How do i Create a Custom Quiz?`
  - `What are Badges?`
- Chess.com help/editorial:
  - `What does my Stats page show?`
  - `How does Game Review work?`
  - `How do I view my own games?`
  - `How can I see my previous puzzles and puzzle rush games?`
  - `How do I find the Daily Puzzle?`
  - `What are Streaks?`
  - `A Day In The Life Of Chess.com's Daily Puzzle Curator`
