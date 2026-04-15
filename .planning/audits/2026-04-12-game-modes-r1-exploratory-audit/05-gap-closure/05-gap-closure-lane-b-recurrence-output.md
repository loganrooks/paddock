---
date: 2026-04-14
audit_subject: mature_product_closure
audit_orientation: exploratory
audit_delegation: delegated
scope: "Close the recurrence and return-loop part of the mature-product gap"
triggered_by: "05-gap-closure-synthesis.md"
tags:
  - exploratory-audit
  - gap-closure
  - recurrence
  - return-loop
  - retention
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-lane-b-recurrence-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-lane-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-context-and-plan.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-synthesis.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-handoff-gap-review.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-experience-archetypes-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-a-local-party-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-b-private-online-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-c-solo-async-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-d-community-event-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-b-history-cadence-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-sensitivity-map-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
---

# 05 Gap Closure Lane B: Recurrence And Return Loops

## Lane framing

`[governing:cited]` This lane exists to close the still-open `Retention mechanics / return loop` gap and the sharper audit-revealed gap that recurrence is layered rather than singular (`05-gap-closure-context-and-plan.md:55-56`, `05-gap-closure-context-and-plan.md:65-67`). `05-gap-closure-synthesis.md` then makes this lane specifically responsible for ordering room folklore, personal mastery, editorial return, replay/review surfaces, and event cadence rather than leaving the dominant return logic unresolved (`05-gap-closure-synthesis.md:49-50`, `05-gap-closure-synthesis.md:91-92`, `05-gap-closure-synthesis.md:124-126`).

`[governing:cited]` Steering sources for this lane were:

- `05-gap-closure-context-and-plan.md`
- `05-gap-closure-synthesis.md`
- `05-handoff-gap-review.md`
- `round-2a-experience-archetypes-output.md`
- `round-2a-lane-a-local-party-output.md`
- `round-2a-lane-b-private-online-output.md`
- `round-2a-lane-c-solo-async-output.md`
- `round-2b-lane-b-history-cadence-output.md`
- `round-2b-sensitivity-map-output.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/REQUIREMENTS.md`

`[governing:cited]` Background-only sources for this lane were:

- `HANDOFF.md`, as motivating pressure for mature-product return questions rather than as binding solution authority
- `round-2a-lane-d-community-event-output.md`, used only to keep `event cadence` legible without drifting into bounded-public shell ordering, which belongs to Lane C

`[governing:cited]` This lane does not answer:

- the authored-content pipeline, evergreen-library policy, or contribution posture beyond the recurrence consequences they create
- community, spectator, showcase, clip, or audience-right ordering beyond the narrow question of whether event cadence is a first-order return layer
- support, premium, access, or service-obligation transitions
- exact daily/weekly/seasonal cadence taxonomy, exact progression metrics, or final durable nouning for room/group/event memory

`[projected:reasoned]` Downstream consequence: the later mature-product synthesis should inherit a ranked recurrence stack rather than a flat `retention` bucket; the later sensitivity pass should test whether canon and Phase 01 carry-forward language preserve that stack without collapsing memory, cadence, or wrapper layers; canon patching is therefore most likely to affect `PROJECT.md`, `LONG-ARC.md`, and `REQUIREMENTS.md`, with lighter ripple into `ROADMAP.md`.

## Traceability and scope

`[evidenced:cited]` This lane directly answers one `handoff-relative gap` and one `emergent audit-revealed gap` from `05-gap-closure-context-and-plan.md`:

| Gap class | Gap | Why this lane owns it |
|---|---|---|
| `handoff-relative gap` | `Retention mechanics / return loop` | The audit surfaced solo ritual, house memory, replay/review, and layered cadence, but never closed a ranked thesis for which recurrence layers matter first (`05-gap-closure-context-and-plan.md:55-56`). |
| `emergent audit-revealed gap` | `Recurrence is layered, not one generic retention loop` | The audit explicitly learned that room folklore, trusted-group ritual, solo editorial return, and bounded event cadence are different goods that now need ordering (`05-gap-closure-context-and-plan.md:65-67`). |

`[evidenced:cited]` `05-handoff-gap-review.md` adds the key shape constraint: retention answers cannot be written as if one default social form exists, and they cannot be left as loose feature-bucket prompts. They must be indexed by archetype and shell, while still honoring Round 2B non-foreclosure doctrine (`05-handoff-gap-review.md:43-45`, `05-handoff-gap-review.md:61-63`, `05-handoff-gap-review.md:69-75`, `05-handoff-gap-review.md:81-84`).

`[assumed:reasoned]` The practical scope boundary is therefore: decide the recurrence stack and the first real repeat-return loop in a private-first, layered-memory product. Do not silently widen this into content operations, public-shell programming, or premium ladder design just because those topics touch recurrence.

## What is already settled

`[governing:cited]` Several doctrines are already settled and must constrain this lane rather than be reopened:

- the product center is still a private, watchable, browser-first game-night ritual built on a substrate-plus-wrappers posture rather than one frozen app shape (`PROJECT.md:102-112`, `PROJECT.md:136-146`, `LONG-ARC.md:69-77`)
- memory and cadence must stay layered: player history, room/group memory, event memory, and content calibration/history are not one ledger, and session pacing is not editorial rhythm or event cadence (`PROJECT.md:141-145`, `LONG-ARC.md:48-67`)
- recurrence begins privately before it becomes public; bounded public or spectator-facing shells are wrappers around private-first play, not the default recurrence model (`round-2a-experience-archetypes-output.md:221-238`, `PROJECT.md:138-146`, `LONG-ARC.md:79-102`, `LONG-ARC.md:131-137`)
- the mature-product question is not whether recurrence exists, but which layers matter first and how they should attach without forcing one universal cadence model or one universal history ledger (`round-2b-lane-b-history-cadence-output.md:117-123`, `round-2b-lane-b-history-cadence-output.md:145-150`, `round-2b-sensitivity-map-output.md:153-159`)

`[evidenced:cited]` The canon already contains light recurrence anchors that this lane can build on rather than inventing from scratch:

- `ROOM-05` and `UX-04` already treat rematch/replay and structured session summary as first-class room outcomes (`REQUIREMENTS.md:44-56`)
- `RET-01` through `RET-04` already keep recurring challenge, lightweight history, round-by-round review, and replay surfaces alive as v2 requirements (`REQUIREMENTS.md:97-103`)
- Milestone 2 and the future-aware posture already keep solo/async wrappers, lightweight identity, room/group memory, and layered cadence visible without importing them into Milestone 1 scope (`PROJECT.md:100-111`, `PROJECT.md:140-145`)

`[assumed:reasoned]` What is not yet settled is the ordering. The repo has preserved the recurrence layers; it has not yet decided which layers form the real product return engine versus which ones are amplifiers or later wrappers.

## Path of inquiry

`[assumed:reasoned]` The inquiry path for this lane was:

1. Start from the gap documents to pin the exact closure obligation: rank recurrence layers and define the first real repeat-return loop, not merely restate that recurrence is layered (`05-gap-closure-context-and-plan.md:55-56`, `05-gap-closure-synthesis.md:124-126`).
2. Re-read the Round 2A archetype outputs to recover what recurrence actually means in each experience class: house memory in local play, room ritual in private sync, mastery and editorial return in solo async, and appointment cadence in event shells (`round-2a-experience-archetypes-output.md:221-238`, `round-2a-lane-a-local-party-output.md:151-162`, `round-2a-lane-b-private-online-output.md:98-104`, `round-2a-lane-c-solo-async-output.md:64-73`, `round-2a-lane-c-solo-async-output.md:111-123`).
3. Pressure-test those meanings against the Round 2B memory/cadence lane and sensitivity map so the result would respect layered history, layered cadence, and non-collapse seams (`round-2b-lane-b-history-cadence-output.md:117-150`, `round-2b-lane-b-history-cadence-output.md:154-162`, `round-2b-sensitivity-map-output.md:144-159`).
4. Compare the resulting stack against the live canon and requirements to see which recurrence surfaces already exist as protected seams and which ones still need operating-model closure (`PROJECT.md:100-145`, `LONG-ARC.md:48-89`, `REQUIREMENTS.md:44-56`, `REQUIREMENTS.md:97-103`).

`[assumed:reasoned]` The ranking criterion used here was deliberately product-facing rather than growth-metric-facing:

- does the layer reinforce the private-first product center?
- does it create repeat return beyond a single-night rematch?
- does it avoid forcing public-platform or heavy live-service obligations too early?
- does it bridge across the strongest archetypes rather than belonging to only one shell?
- does it preserve rather than collapse the memory/cadence seams Round 2B already established?

## Core closure questions

`[governing:cited]` The lane needed to close five questions:

1. Which recurrence layer is foundational for the current product center?
2. Which layer creates the first meaningful between-session reason to come back?
3. What role should replay/review surfaces actually play: pillar, bridge, or afterthought?
4. Should editorial cadence or event cadence be treated as the primary return engine?
5. What recurrence ordering can guide synthesis and canon patching without falsely locking exact cadence taxonomy or wrapper order?

## Findings

### 1. Room folklore is the first emotional recurrence layer, but not the whole return engine

`[evidenced:cited]` Round 2A is unusually consistent that recurrence begins with trusted groups rather than with public feeds. Local recurring party wants house memory, recurring hosts, recurring packs, race-weekend themed nights, rematches, and lightweight bragging rights (`round-2a-lane-a-local-party-output.md:149-162`). Private online sync wants recurring private packs, room history, and friend-group ritual rather than universal public challenge logic (`round-2a-lane-b-private-online-output.md:98-104`). The central archetype synthesis then compresses that into a clean cross-lane conclusion: recurrence begins privately before it becomes public (`round-2a-experience-archetypes-output.md:221-238`).

`[assumed:reasoned]` This makes `room folklore` the first emotional recurrence layer because it is where replay value feels most native to the current product center. The product's first proof is still a trusted-group ritual, and that ritual naturally creates rematches, recurring jokes, recurring controversies, and memory of who is good at what.

`[assumed:reasoned]` But room folklore alone is not yet the full return engine, because it depends on a group already deciding to reconvene. It explains why repeat play matters; it does not by itself explain how the product reaches back between sessions.

### 2. Personal mastery is the first scalable between-session recurrence layer

`[evidenced:cited]` The solo async lane is clear that its strongest shape is not generic solo play but a layered return stack built from daily pulse, race-weekend ritual, evergreen deepening, and private shadow-presence (`round-2a-lane-c-solo-async-output.md:64-73`). It also says the core experiential goods are editorial return, personal completion, private rhythm, and a growing relationship with F1 places and patterns rather than public-performance pressure (`round-2a-lane-c-solo-async-output.md:73`, `round-2a-lane-c-solo-async-output.md:111-123`).

`[evidenced:cited]` The canon already protects this direction lightly through Milestone 2's expected additions of solo/async wrappers, lightweight player identity, session history, and room/group memory surfaces (`PROJECT.md:100-111`). `RET-01` through `RET-03` likewise keep recurring challenge, lightweight player identity, and reviewable round-by-round history alive without requiring a heavy public-account posture (`REQUIREMENTS.md:97-102`).

`[assumed:reasoned]` This makes `personal mastery` the first scalable between-session layer. It creates a reason to come back on an individual timescale without demanding stranger-facing publicness or a heavy moderation surface. It is also the layer most capable of turning the anchor geography/circuit fantasy into sustained return rather than one-off party novelty.

### 3. Replay/review surfaces are connective tissue, not a standalone recurrence pillar

`[evidenced:cited]` The current requirements already treat replay and structured review as meaningful surfaces rather than cosmetic summaries: the room should end with a session summary that supports replay or switching packs, and session results should remain browsable afterward as a replay or structured review surface (`REQUIREMENTS.md:55-56`, `REQUIREMENTS.md:101-102`).

`[evidenced:cited]` Round 2B strengthens why these surfaces matter: memory cannot collapse into one flat ledger, and cadence cannot collapse into one clock. The history/cadence lane explicitly separates player history, room/group history, event memory, and content history, while the sensitivity map warns against treating content calibration, replay, and retention history as one undifferentiated record (`round-2b-lane-b-history-cadence-output.md:145-149`, `round-2b-lane-b-history-cadence-output.md:156-162`, `round-2b-sensitivity-map-output.md:149-159`).

`[assumed:reasoned]` The recurrence consequence is that `replay/review` is not its own primary return layer. It is the bridge surface that converts one session into:

- room folklore the group can remember and revisit
- personal mastery the player can inspect and improve
- editorial resurfacing later, when a challenge or pack is re-featured

`[assumed:reasoned]` If review stays a dead-end summary screen, the product loses the cleanest bridge between social ritual and individual return.

### 4. Editorial cadence should prompt return, not carry the whole product alone

`[evidenced:cited]` The solo async lane says editorial scheduling is part of the experience, especially for race-weekend and post-race reactive loops, and that daily, race-weekend, and evergreen cadences need to coexist (`round-2a-lane-c-solo-async-output.md:101-107`, `round-2a-lane-c-solo-async-output.md:148-152`). Round 2B then generalizes that finding: session pacing, editorial cadence, event cadence, and progression cadence are distinct concerns and should not be flattened into one governing clock (`round-2b-lane-b-history-cadence-output.md:117-123`, `round-2b-lane-b-history-cadence-output.md:149-150`).

`[assumed:reasoned]` Editorial cadence therefore matters materially, but it should not be treated as the base return engine. If the product needs constant drops to create any reason to return, it becomes operationally brittle and starts leaning on a content-flywheel answer that this lane does not yet own. Editorial cadence is best understood as a prompting and mood-shaping layer that reactivates room folklore and personal mastery rather than replacing them.

### 5. Event cadence is an amplifier layer, not the first recurrence base

`[evidenced:cited]` The archetype synthesis is explicit that event cadence matters, but not every archetype wants the same cadence (`round-2a-experience-archetypes-output.md:221-232`). It also classifies bounded event shells as important but still secondary in product center-of-gravity terms compared with local recurring party, private online sync, and solo async ritual (`round-2a-experience-archetypes-output.md:242-250`).

`[evidenced:cited]` The Long Arc likewise places spectator/showcase wrappers later and keeps visibility state staged and surface-specific rather than treating public-facing shells as the core recurrence layer (`LONG-ARC.md:79-102`, `LONG-ARC.md:131-137`).

`[assumed:reasoned]` This means `event cadence` should be ranked as an amplifier. It can make the product feel alive, seasonal, and socially legible, but it should not be the first return engine the mature-product story depends on. Making it primary would quietly move the product toward public-shell programming or operational/event burden before the private-first loop has fully earned it.

### 6. The first real repeat-return loop should be a blended private loop, not a single isolated layer

`[assumed:reasoned]` The strongest closure answer is not `room folklore alone`, `daily challenge alone`, or `race-weekend events alone`. The first real repeat-return loop should be:

1. a trusted private session creates memorable reveals, rematches, and group-specific folklore
2. the session leaves behind a structured review surface rather than disappearing into a one-night result
3. that review surface feeds private mastery, light progression, or shadow-community return between sessions
4. editorial prompts and race-weekend framing periodically reactivate both the room ritual and the mastery loop

`[assumed:reasoned]` In short: `room ritual -> review -> mastery return -> next trusted session`.

`[evidenced/governing:mixed]` This blended loop is the only one that fits all of the strongest constraints at once:

- it honors the private-first emotional center (`PROJECT.md:136-146`, `LONG-ARC.md:69-77`)
- it uses review/replay as already-protected connective tissue (`REQUIREMENTS.md:55-56`, `REQUIREMENTS.md:101-102`)
- it gives between-session return a real shape without forcing public-platform obligation or one universal daily cadence (`round-2a-lane-c-solo-async-output.md:111-123`, `LONG-ARC.md:79-89`)
- it preserves layered memory and cadence rather than collapsing them (`LONG-ARC.md:60-67`, `round-2b-sensitivity-map-output.md:155-159`)

## Live options or operating shapes

`[assumed:reasoned]` Four recurrence shapes remain visible, but they do not all deserve equal carry-forward weight:

| Operating shape | What leads | Strengths | Vulnerabilities | Current status |
|---|---|---|---|---|
| `room-folklore-led` | rematches, private-room ritual, recurring hosts, house memory | strongest fit to current product center; lowest public obligation | weak between-session pull if the group does not reconvene soon | `necessary but insufficient` |
| `mastery-led` | private progression, history, collection, self-comparison | strongest between-session pull; fits private-first and async wrappers | can drift into generic challenge grind if detached from social ritual or F1 calendar texture | `core bridge layer` |
| `editorial-led` | featured drops, race-weekend prompts, freshness | gives return timeliness and mood; helps keep the product feeling alive | operationally heavy if asked to carry the whole loop; bleeds into Lane A if over-expanded | `supporting prompt layer` |
| `event-led` | appointment nights, featured events, semi-public rituals | strong atmosphere and shared memory when shells exist | risks public-first drift and premature shell/ops burden | `amplifier, not base` |

`[assumed:reasoned]` The winning shape is therefore not one row by itself. It is a weighted stack in which `room-folklore-led` and `mastery-led` form the base, `editorial-led` acts as the prompting layer, and `event-led` remains a later amplifier rather than the first return foundation.

## Recommended carry-forward

`[projected:reasoned]` The recurrence ordering to carry into mature-product synthesis should be:

1. `session replay / rematch and room-group folklore`
2. `review surfaces and private mastery return`
3. `editorial prompting and race-weekend framing`
4. `event cadence and later showcase ritual`

`[projected:reasoned]` The first real repeat-return loop should therefore be named as:

- `private ritual loop`
- meaning: `play together -> review what happened -> come back privately to improve or revisit -> reconvene or re-enter through the next trusted session`

`[projected:reasoned]` This should change how later work talks about recurrence:

- do not treat `retention` as a single KPI-shaped bucket
- do treat `replay/review` as bridge infrastructure between social memory and personal return
- do treat `solo/async challenge or practice` as the first non-room wrapper most justified by recurrence pressure, while leaving exact wrapper ordering for final synthesis and sensitivity testing
- do keep `room/group memory`, `player progression`, `event memory`, and `content history` conceptually distinct so the recurrence stack has somewhere coherent to attach

`[projected:reasoned]` Downstream consequences:

- `mature-product synthesis`: should integrate content cadence as a support layer for this recurrence stack, not as the stack's substitute; should also treat any public/event recurrence as secondary to the private loop rather than as the default center
- `later sensitivity pass`: should explicitly test whether canon wording accidentally universalizes `daily challenge`, `room history`, or `event programming` as the single recurrence model
- `canon patching`: should likely strengthen `PROJECT.md` and `LONG-ARC.md` language around recurrence ordering and use `REQUIREMENTS.md` to clarify that review/history surfaces bridge room ritual and later mastery rather than merely record scores

## Explicit deferrals

`[governing:cited]` This lane closes recurrence ordering, not every cadence detail. The following remain explicitly deferred:

- exact cadence names or frequencies such as `daily`, `weekly`, `race-weekend`, `seasonal`, or `off-week` as formal product taxonomy
- the exact first personal mastery metric: circuit completion, accuracy trend, era mastery, prediction accuracy, or a mixed profile
- exact room/group nouning and whether later durable identity looks more like `room`, `house`, `club`, or another term
- public-shell event programming, audience participation, or showcase mechanics beyond the narrow judgment that event cadence is not the first return base
- content-flywheel burden, editorial staffing implications, and evergreen-library policy beyond the recurrence consequences already noted
- monetization, premium gating, or obligation changes that might later interact with recurrence

`[assumed:reasoned]` These deferrals are healthy because the lane now answers the operating-model order without pretending it can also settle cadence taxonomy, community shell design, or content operations in one pass.

## What the later sensitivity pass must test from this lane

`[projected:reasoned]` The dedicated post-closure sensitivity pass should test whether this lane's carry-forward:

- preserves the private-first center instead of quietly recasting recurrence as a public challenge or event-programming problem
- preserves layered memory by keeping room/group memory, player progression, event memory, and content history distinct
- preserves layered cadence by keeping session replay/rematch, personal mastery return, editorial prompting, and event cadence separate instead of collapsing them into one `challenge` concept
- keeps replay/review as an actual bridge surface in canon and requirements rather than leaving it as a terminal summary screen
- protects a lightweight non-room recurrence wrapper without importing heavy account, moderation, or public-obligation assumptions
- avoids forcing every mode family into the same mastery depth or the same editorial cadence, especially where Round 2A already showed context-specialist modes should resist universal parity
- creates any need to clarify `PROJECT.md`, `LONG-ARC.md`, `REQUIREMENTS.md`, or future roadmap notes about recurrence ordering and replay/history language

## Coverage note

`[evidenced:cited]` This lane materially closes the `Retention mechanics / return loop` gap by replacing the repo's prior flat retention language with a ranked recurrence stack and by naming the first real repeat-return loop in private-first product terms (`05-gap-closure-context-and-plan.md:55-56`, `05-gap-closure-synthesis.md:124-126`).

`[evidenced:cited]` It also materially closes the emergent gap that `recurrence is layered, not one generic retention loop` by deciding that:

- `room folklore` is the foundational emotional recurrence layer
- `personal mastery plus review` is the first scalable between-session layer
- `editorial cadence` is a prompt layer
- `event cadence` is an amplifier layer rather than the first base (`05-gap-closure-context-and-plan.md:65-67`, `round-2a-experience-archetypes-output.md:221-238`, `round-2b-lane-b-history-cadence-output.md:117-123`)

`[assumed:reasoned]` What remains open after this lane is narrower and appropriate for synthesis rather than for another recurrence pass:

- exact wrapper sequencing beyond the recurrence evidence contributed here
- exact cadence taxonomy and progression metric design
- how content-flywheel decisions and community-shell ordering should modulate the recurrence stack

`[projected:reasoned]` The practical handoff is therefore strong: mature-product synthesis can now treat recurrence as a structured operating-model answer rather than as a placeholder topic, and the later sensitivity pass can test whether canon and planning surfaces preserve that answer honestly.
