---
date: 2026-04-14
audit_subject: mature_product_closure
audit_orientation: exploratory
audit_delegation: delegated
scope: "Close the content-flywheel part of the mature-product gap"
triggered_by: "05-gap-closure-lane-a-content-flywheel-task-spec.md"
tags:
  - exploratory-audit
  - gap-closure
  - content-flywheel
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-lane-a-content-flywheel-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-lane-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-synthesis.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-context-and-plan.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-handoff-gap-review.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/04-closeout/whole-job-verification-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-experience-archetypes-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md
---

# 05 Gap Closure Lane A: Content Flywheel

## Lane framing

`[governing:cited]` This lane exists to close the still-open `content flywheel design` gap identified in the original handoff, the closeout verification, the context-and-plan artifact, and the gap-closure synthesis (`HANDOFF.md:106-114`; `whole-job-verification-output.md:35-37`, `120-121`; `05-gap-closure-context-and-plan.md:55`; `05-gap-closure-synthesis.md:121-125`).

`[assumed:reasoned]` The core question is not "how do we maximize content volume?" It is "what content operating model lets a private-first, curated F1 product keep getting better over time without assuming public-platform scale, open publishing, or a constant live-service treadmill?"

`[assumed:reasoned]` For this repo, `content flywheel` should be treated as a layered operating model with four parts:

- an evergreen authored library
- a bounded editorial freshness layer
- a calibration and revision loop
- a staged contribution posture that does not smuggle in open publishing

## Traceability and scope

`[governing:cited]` This lane directly helps answer these `handoff-relative gaps` from `05-gap-closure-context-and-plan.md:53-59`:

- `Content flywheel design`
- the content-side part of `Community features beyond gameplay / community-authoring posture`

`[governing:cited]` This lane partially helps answer these `emergent audit-revealed gaps` from `05-gap-closure-context-and-plan.md:65-70`:

- `Recurrence is layered, not one generic retention loop`, but only insofar as content cadence must be separated from session cadence and from later return-loop ranking
- `Mature-product closure depends on durable room/group/event-memory vocabulary`, because content calibration/history must stay distinct from player, room/group, and event memory

`[governing:cited]` Steering sources for this lane are:

- `05-gap-closure-lane-a-content-flywheel-task-spec.md`
- `05-gap-closure-lane-common-scaffold.md`
- `05-gap-closure-synthesis.md`
- `05-gap-closure-context-and-plan.md`
- `05-handoff-gap-review.md`
- `whole-job-verification-output.md`
- `HANDOFF.md`
- `PROJECT.md`
- `LONG-ARC.md`
- `ROADMAP.md`
- `REQUIREMENTS.md`
- `round-2a-experience-archetypes-output.md`

`[background:cited]` The following were re-engaged directly but remain background-only rather than governing doctrine:

- `IDEAS-platform.md`
- `RESEARCH-TODOS.md`

`[assumed:reasoned]` This lane is not answering:

- the overall return-loop ranking across room folklore, personal mastery, editorial return, and event cadence
- support, premium, pricing, or obligation laddering
- spectator or bounded-public shell ordering
- public UGC moderation, open creator publishing, or marketplace design

## What is already settled

`[governing:cited]` The following doctrine is already settled and should constrain this lane rather than be reopened:

- the product center is a private, watchable, browser-first ritual built on authored rounds and curated packs (`PROJECT.md:88-96`; `LONG-ARC.md:71-77`)
- Milestone 1 already commits to curated starter packs plus calibration signal, not public content scale (`PROJECT.md:91-97`; `ROADMAP.md:170-188`)
- Milestone 2 already keeps alive authoring, preview, pack sharing, and richer content operations, but only if earned and without prematurely accepting public-platform obligations (`PROJECT.md:98-111`; `LONG-ARC.md:73-77`)
- memory and cadence must stay layered, including explicit separation between event memory and content calibration/history, and between session pacing, editorial rhythm, and later event cadence (`PROJECT.md:142-145`; `LONG-ARC.md:60-67`; `ROADMAP.md:185-187`; `REQUIREMENTS.md:135`)
- contribution and sharing must be staged carefully and must not silently imply open publishing, community governance, or a marketplace (`LONG-ARC.md:122-129`, `157-164`; `REQUIREMENTS.md:139-151`)

`[assumed:reasoned]` The practical effect is that the lane does not need to prove that curation-first is allowed. It needs to specify what curation-first sustainability actually looks like.

## Path of inquiry

`[assumed:reasoned]` The lane was evaluated as a comparison among four operating shapes:

- `evergreen library first`
- `editorial calendar first`
- `layered library plus editorial spotlight plus calibration`
- `open community marketplace`

`[assumed:reasoned]` The comparison criteria were:

- fit with the private-first, curated product center
- compatibility with staged visibility and contribution doctrine
- operator burden and editorial sustainability
- reuse across later wrappers without requiring a second content core
- ability to improve quality over time rather than only inflate volume

`[assumed:reasoned]` This is intentionally narrower than a full mature-product pass. It asks what the content machine is, not what the entire recurrence or monetization strategy should be.

## Core closure questions

`[assumed:reasoned]` The closure work for this lane comes down to five questions:

1. What is the durable foundation of content supply: evergreen library, live calendar, or community publishing?
2. What role should F1-season freshness play: core engine, bounded overlay, or optional garnish?
3. What contribution posture fits current doctrine: official curation only, trusted-private sharing, or public creator ecosystem?
4. What loops actually make the content better over time: preview, playtest, calibration, promotion, retirement?
5. What should hosts and later players see at the pack surface so "more content over time" feels legible without implying public discovery?

## Findings

### 1. The evergreen circuit-and-venue library should be the foundation of the flywheel

`[evidenced/governing:mixed]` The canon already centers curated starter packs, authored round contracts, and later reusable content/history surfaces rather than a public feed or procedural treadmill (`PROJECT.md:93-111`; `ROADMAP.md:170-188`; `REQUIREMENTS.md:73-76`, `117-118`).

`[background:cited]` The exploratory platform notes also point to `circuit pack` logic as the natural evergreen organizing principle: the circuit is the content bundle, and the same place can hold multiple rounds, eras, and clue types (`IDEAS-platform.md:7-22`).

`[assumed:reasoned]` The durable answer is therefore: `more content over time` should first mean a deeper, better-tagged, better-calibrated authored library of circuit, venue, era, and clue-shape material. The foundation is not daily churn. It is a reusable library that gets richer and sharper.

### 2. Editorial freshness should sit on top of the library, not replace it

`[evidenced/governing:mixed]` Round 2A already gives solo async and race-weekend return the shape of `editorial return plus evergreen deepening`, not pure live-service novelty (`round-2a-experience-archetypes-output.md:95-108`, `159-170`). The canon also explicitly separates session pacing, editorial rhythm, and later event cadence (`PROJECT.md:142-145`; `LONG-ARC.md:60-67`).

`[background:cited]` The exploratory platform notes likewise argue that the calendar layer sits on top of circuit packs, with race-weekend or post-race content acting as featured freshness rather than replacing the evergreen base (`IDEAS-platform.md:25-38`).

`[assumed:reasoned]` The right carry-forward is a `bounded editorial spotlight` layer:

- current-circuit or race-weekend features
- selective reactive drops when the sport produces genuinely gameable moments
- off-season retrospectives, historical deep dives, or themed programming when useful

`[assumed:reasoned]` This makes freshness a lever, not a treadmill. The product can feel timely without promising that it must publish on a relentless cadence to stay alive.

### 3. Curation-first is the operating doctrine; contribution should be staged behind trusted boundaries

`[governing:cited]` The repo already defers open creator publishing, broad public publishing, and marketplace logic, while keeping contribution and sharing alive only in carefully staged form (`LONG-ARC.md:122-129`, `157-164`; `REQUIREMENTS.md:139-151`).

`[assumed:reasoned]` That means a sustainable flywheel does not require an open creator ecosystem to count as solved. The nearer and doctrine-compatible ladder is:

- official curated authoring now
- later preview/import/export tooling for trusted-instance or friend-group sharing
- possible later editorial intake of outside submissions if the project deliberately chooses that responsibility

`[background:cited]` The exploratory notes explicitly separate private creation from public creation and treat private, schema-aligned authoring as far cheaper and safer than public publishing (`IDEAS-platform.md:163-199`).

`[assumed:reasoned]` The recommended doctrine-level closure is therefore: `private or trusted-circle contribution stays alive as a future seam; public creator ecosystem stays deferred`.

### 4. Calibration is a core flywheel engine, not a supporting metric

`[governing:cited]` The canon already requires round-level evidence capture, calibration-aware curation, and author decisions to keep, revise, retire, or rebalance content (`ROADMAP.md:170-188`; `REQUIREMENTS.md:75-76`, `117-118`).

`[assumed:reasoned]` This lane should make that more explicit: the flywheel works when every play session can improve the library. Broken rounds get retired, trivial rounds get hardened, misleading rounds get repaired, fallback-heavy venues are made explicit, and high-value rounds get promoted.

`[assumed:reasoned]` This is the strongest private-first sustainability answer available in the repo. It improves quality without needing public scale, algorithmic feeds, or a constant flood of net-new content.

### 5. Preview and pack surfaces should express content state, not just content existence

`[evidenced/governing:mixed]` Milestone 2 already expects authoring, preview, pack sharing, and reusable content/history surfaces (`PROJECT.md:102-111`; `REQUIREMENTS.md:106-108`). The lane task spec also explicitly asks for preview, showcase, and pack-surface implications.

`[assumed:reasoned]` The content model therefore needs visible pack states, not only raw pack files. The useful states are:

- `draft / preview`
- `playtested / revision-in-progress`
- `featured / timely`
- `evergreen / stable library`
- `retired or archived`

`[assumed:reasoned]` The pack surface should make a pack's role legible before play. At minimum, later surfaces should be able to convey:

- the pack's anchor circuit, venue, era, or theme
- whether it is evergreen or time-bound
- rough session shape or expected round mix
- notable fallback or media posture where relevant
- whether the pack is still experimental versus stable

`[assumed:reasoned]` That is a better interpretation of `showcase` than a generic public gallery. In this repo's current doctrine, showcase first means curated surfacing for hosts and trusted audiences, not default public discovery.

### 6. The strongest content-flywheel answer is a layered editorial loop, not a volume-maximizing treadmill

`[assumed:reasoned]` The strongest overall operating shape is:

1. build and expand the evergreen authored library
2. preview and privately playtest new or revised packs
3. publish some packs as stable evergreen library entries and some as bounded featured spotlights
4. collect structured round and clue-step evidence from play
5. revise, promote, reframe, or retire packs based on that evidence
6. use seasonal or event-tied editorial programming to point attention back into the library when it genuinely adds value

`[assumed:reasoned]` This answers the original flywheel question without needing to decide that the product must become a public content platform.

## Live options or operating shapes

### Option A: Pure evergreen library

`[assumed:reasoned]` Strengths:

- strongest fit with private-first curation
- low service and moderation burden
- clean compatibility with Milestone 1 and Phase 6

`[assumed:reasoned]` Weaknesses:

- underuses the F1 calendar
- gives a thinner answer to freshness and topical return

`[assumed:reasoned]` Status: viable but too thin on its own.

### Option B: Editorial calendar as the primary engine

`[assumed:reasoned]` Strengths:

- strongest topical freshness
- strongest tie to race-weekend mood and current conversation

`[assumed:reasoned]` Weaknesses:

- highest operator burden
- easiest path into accidental live-service obligation
- weakest fit with the repo's current private-first and low-obligation posture

`[assumed:reasoned]` Status: not recommended as the main operating model.

### Option C: Layered curated flywheel

`[assumed:reasoned]` Shape:

- evergreen library as foundation
- selective editorial spotlight on top
- calibration as the refinement loop
- trusted-private contribution as a preserved seam

`[assumed:reasoned]` Strengths:

- best doctrinal fit
- strongest reuse across wrappers
- improves quality over time without requiring public scale
- leaves later private-sharing and showcase surfaces alive without forcing them now

`[assumed:reasoned]` Weaknesses:

- still needs disciplined metadata, preview, and revision states
- can drift into vagueness if the pack lifecycle is not named clearly in canon later

`[assumed:reasoned]` Status: recommended carry-forward.

### Option D: Open community marketplace

`[governing:cited]` This conflicts directly with the current deferrals around public publishing, moderation, and marketplace logic (`LONG-ARC.md:157-164`; `REQUIREMENTS.md:139-151`).

`[assumed:reasoned]` Status: explicitly deferred, not a live recommendation.

## Recommended carry-forward

`[projected:reasoned]` The recommended carry-forward is:

- `curated evergreen library` as the durable base
- `selective editorial spotlight` as the freshness layer
- `calibration-driven revision` as the main quality loop
- `trusted-private contribution and pack exchange` as the future seam worth preserving

`[projected:reasoned]` In operational terms, this means:

- `more content` should mean more depth, better calibration, broader circuit and era coverage, and stronger pack curation before it means more sheer volume
- race-weekend or post-race content should be treated as featured programming that points back into the library, not as a mandatory publishing treadmill
- preview, import/export, and pack-state surfaces should be justified primarily as curation and trusted-sharing tools, not as steps toward an open marketplace
- content history should be modeled as its own layer so pack quality can improve without collapsing into player, room, or event memory

`[projected:reasoned]` Downstream consequence for mature-product synthesis:

- the later synthesis should be able to treat `content sustainability` as `library + spotlight + calibration + staged trusted contribution`
- Lane B can then decide how much of the return loop comes from editorial return versus room folklore or personal mastery without having to invent the content machine from scratch

`[projected:reasoned]` Downstream consequence for later sensitivity pass:

- test whether any canon wording about pack sharing, showcase, or editorial cadence accidentally implies public discovery, stronger service promises, or a public creator ecosystem

`[projected:reasoned]` Downstream consequence for canon patching:

- `PROJECT.md` and `LONG-ARC.md` can name `evergreen library plus selective editorial spotlight` more explicitly
- `ROADMAP.md` and `REQUIREMENTS.md` may need later wording that makes pack preview, pack states, and trusted-instance sharing more legible as content-ops surfaces rather than marketplace precursors

## Explicit deferrals

`[governing:cited]` The following stay deferred from this lane:

- exact pricing, subscription, supporter, or premium-content packaging
- final return-loop ranking across editorial return, room folklore, personal mastery, replay, and event cadence
- public showcase/discovery strategy beyond bounded curated surfacing
- public UGC moderation systems, ratings, reporting, or creator governance
- open creator marketplace or broad public publishing

`[assumed:reasoned]` The following are also not closed here:

- whether AI-assisted drafting should play any role in future authoring operations
- exact pack taxonomy beyond what the current circuit/venue substrate already supports
- exact seasonal publishing commitment or weekly editorial staffing expectation

## What the later sensitivity pass must test from this lane

`[projected:reasoned]` The sensitivity pass should test whether this lane's carry-forward:

- preserves the private-first center instead of drifting toward public-feed assumptions
- keeps `content calibration/history` distinct from player, room/group, and event memory
- keeps `editorial rhythm` distinct from session pacing and from later event cadence
- preserves `trusted-private sharing` as distinct from `open publishing`
- keeps pack preview and showcase language compatible with staged visibility doctrine
- introduces any new requirement or carry-forward note for `PROJECT.md`, `LONG-ARC.md`, `ROADMAP.md`, `REQUIREMENTS.md`, or the future rerun inputs

## Coverage note

`[assumed:reasoned]` This lane directly closes the missing positive answer for `content flywheel design` and gives a narrower, doctrine-compatible answer to the content side of `community-authoring posture`.

`[assumed:reasoned]` It intentionally does not close the full recurrence question, the support/premium question, or the community/spectator shell-ordering question. Those remain the job of later lanes and the converged mature-product synthesis.

`[assumed:reasoned]` Epistemic note: this lane uses only repo-local doctrine plus directly re-engaged exploratory notes. No external reference memo was used here, so any claim about comparative market plausibility or exact editorial workload should still be treated as provisional until the broader bundle's reference-grounded work is complete.
