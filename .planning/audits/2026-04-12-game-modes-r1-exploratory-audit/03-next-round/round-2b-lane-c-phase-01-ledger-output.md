---
date: 2026-04-13
audit_subject: artifact_analysis
audit_orientation: exploratory
audit_delegation: self
scope: "Round 2B Wave 2 Lane C: planning-facing decision ledger and foreclosure warning synthesis"
triggered_by: "manual: Round 2B Lane C request"
tags:
  - exploratory-audit
  - round-2b
  - lane-c
  - decision-ledger
  - non-foreclosure
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/next-round-gap-review.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-foreclosure-synthesis-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-a-room-topology-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-b-history-cadence-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-sensitivity-map-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-experience-archetypes-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
planning_surfaces_inspected:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/01-CONTEXT.md
---

# Round 2B Lane C Output

## Lane framing

`[governing:cited]` This is the `Wave 2` planning-facing ledger for Round 2B. Its job is to classify candidate early decisions into `explicit now`, `keep open`, and `defer`, while naming the shortcuts most likely to cause foreclosure and the uncertainties too large to fake as solved (`round-2b-lane-c-phase-01-ledger-task-spec.md:44-60`).

`[governing:cited]` It is not the authoritative closure artifact for `RESP-04`. It prepares the draft decision surface that the main-thread synthesis must later consume (`round-2b-lane-c-phase-01-ledger-task-spec.md:59-66`, `round-2b-foreclosure-synthesis-task-spec.md:156-173`).

`[assumed:reasoned]` The filename is Phase-01-leaning, but the real scope is broader. The task spec explicitly extends this lane across the rest of Milestone 01 and doctrine-level carry-forward, and the Wave 1.5 sensitivity map shows that most high-risk shortcuts harden in Phases 3 through 7 rather than inside the authored-round contract itself (`round-2b-lane-c-phase-01-ledger-task-spec.md:30-31`, `round-2b-lane-c-phase-01-ledger-task-spec.md:62-66`, `round-2b-sensitivity-map-output.md:115-126`, `round-2b-sensitivity-map-output.md:140-195`).

## Traceability and scope

`[evidenced:cited]` This lane directly supports `RESP-04` and must map back explicitly to `GAP-05` and `GAP-08` (`round-2b-lane-c-phase-01-ledger-task-spec.md:68-79`). The governing gap review defines those gaps as:

- the missing experience-to-architecture foreclosure matrix (`next-round-gap-review.md:300-333`)
- the missing Phase-01-facing decision surface that translates engineering exposure into planning input (`next-round-gap-review.md:409-441`)

`[governing:cited]` Steering precedence for this artifact is: governance framework, gap review, Round 2B task spec, Wave 1.5 sensitivity map, Wave 1 outputs, Round 2A archetype convergence, then `lane-i` and `lane-j` (`round-2b-lane-c-phase-01-ledger-task-spec.md:123-135`).

`[assumed:reasoned]` This artifact does not:

- choose implementation libraries or vendor stacks
- close the final Round 2B synthesis on behalf of the main thread
- lock exact capability bundles, wrapper taxonomy, or higher-tempo transport design where the evidence remains suggestive rather than decisive

## Calibration carry-forward

`[governing:cited]` The governing method is non-foreclosure, traceability, and epistemic candor: do not collapse option space prematurely, tie load-bearing judgments to evidence or reasoned inference, and distinguish what is closed from what remains open (`review-trail-framework.md:146-183`).

`[governing:cited]` Round 2B is not a new ideation round. It must work from the already-mapped experience archetypes plus the already-run engineering exposure, and it must not let architectural language quietly replace lived product language (`round-2b-lane-common-scaffold.md:18-25`, `round-2b-lane-common-scaffold.md:38-49`, `round-2b-foreclosure-synthesis-task-spec.md:67-84`).

`[governing:cited]` The most important carry-forward corrections remain active here:

- do not force one universal ontology or one universal room shape
- do not treat creator examples as mandatory taxonomies
- separate broad architecture exposure from large-room feasibility
- do not assume the relevant planning surface is only `Phase 01`

Those constraints come from the Round 2B task stack and the handoff's foreclosure thread rather than from older mixed architecture artifacts (`round-2b-foreclosure-synthesis-task-spec.md:67-84`, `round-2b-lane-common-scaffold.md:40-49`, `HANDOFF.md:124-135`).

## Path of inquiry

`[assumed:reasoned]` The reading path for this ledger was:

1. Re-read the governance framework and gap review to anchor the response in `RESP-04`, `GAP-05`, and `GAP-08` rather than in Wave 1 language alone (`review-trail-framework.md:146-183`, `next-round-gap-review.md:300-333`, `next-round-gap-review.md:409-503`).
2. Re-read the Round 2B synthesis spec and Lane C task spec to hold the output contract constant: classify, do not re-ideate; keep scope broader than Phase 01 where ripple warrants it (`round-2b-foreclosure-synthesis-task-spec.md:43-154`, `round-2b-lane-c-phase-01-ledger-task-spec.md:44-113`).
3. Re-read Lane A, Lane B, and the Wave 1.5 sensitivity map with emphasis on shortcuts, preserved seams, confidence level, and ripple scope (`round-2b-lane-a-room-topology-output.md:243-303`, `round-2b-lane-b-history-cadence-output.md:141-191`, `round-2b-sensitivity-map-output.md:53-205`).
4. Cross-check those seam claims against the Round 2A convergence so the ledger stays anchored in concrete experience classes instead of architecture taste (`round-2a-experience-archetypes-output.md:221-277`).
5. Re-test the same judgments against `lane-i` and `lane-j`, then inspect the active canon and Phase 01 context to identify the true ripple surface (`lane-i-output.md:352-685`, `lane-j-output.md:123-381`, `PROJECT.md:45-58`, `PROJECT.md:121-171`, `LONG-ARC.md:35-129`, `ROADMAP.md:34-186`, `REQUIREMENTS.md:89-138`, `01-CONTEXT.md:145-162`).

`[assumed:reasoned]` The result is deliberately asymmetric. The strongest evidence is about which seams must stay visible in planning. The weakest evidence is about the final nouns, the final wrapper taxonomy, and the exact higher-tempo substrate.

## Experience-to-architecture pressure map

### 1. Container layering and recurrence attachment

`[evidenced/governing:mixed]` The strongest cross-lane convergence is that collapsing `event_container`, `room`, and `game_instance` into one object creates both topology distortion and memory/cadence distortion. Lane A makes the topology case, Lane B makes the recurrence and content-model case, the sensitivity map elevates it as a strong cross-lane seam, and `lane-i`/`lane-j` independently treat shell separation as normal rather than exotic (`round-2b-lane-a-room-topology-output.md:121-137`, `round-2b-lane-b-history-cadence-output.md:109-123`, `round-2b-sensitivity-map-output.md:55-63`, `lane-i-output.md:352-385`, `lane-j-output.md:123-141`, `lane-j-output.md:313-320`).

`[assumed:reasoned]` Planning consequence: this separation needs to be explicit now as a protective seam even though Milestone 1 will often present it as `1:1` in the visible UI.

### 2. Topology plurality and visibility-scoped reveal

`[evidenced/governing:mixed]` Host-screen-friendly play cannot be allowed to harden into a universal one-surface truth model. Lane A, the sensitivity map, `lane-i`, and `lane-j` all converge that staged reveal, private submissions, same-house-separated play, role-private views, and audience-readable shells depend on visibility-scoped publication rather than one shared state blob hidden in the client (`round-2b-lane-a-room-topology-output.md:159-212`, `round-2b-sensitivity-map-output.md:75-83`, `lane-i-output.md:419-442`, `lane-j-output.md:143-157`, `lane-j-output.md:222-237`, `lane-j-output.md:313-320`).

`[assumed:reasoned]` Planning consequence: this is another `explicit now` seam. The exact implementation can stay open, but the canon cannot keep implying that host-screen watchability means one permanent viewer surface.

### 3. Authority portability and participation rights

`[evidenced/governing:mixed]` Lane A surfaces the product pressure directly: social host, presenter, room owner, moderator, judge-like roles, and audience rights are not reducible to one `host/player` split. The architecture lanes support the same point technically via capability-shaped participants, moderation rights, and audience shells (`round-2b-lane-a-room-topology-output.md:179-198`, `round-2b-lane-a-room-topology-output.md:247-265`, `round-2b-sensitivity-map-output.md:85-93`, `lane-i-output.md:387-417`, `lane-j-output.md:188-201`, `lane-j-output.md:281-305`, `lane-j-output.md:313-320`).

`[assumed:reasoned]` Planning consequence: the portability seam is `explicit now`; the minimum useful capability bundle is still `keep open`.

### 4. Presence identity, join semantics, and room lifecycle

`[evidenced/governing:mixed]` There is strong support for separating lightweight presence identity from durable history identity, and for treating join, rejoin, invite posture, seat claim, and ownership continuity as real room-lifecycle concerns rather than one monolithic join action (`round-2b-lane-a-room-topology-output.md:139-157`, `round-2b-lane-b-history-cadence-output.md:99-107`, `round-2b-sensitivity-map-output.md:65-73`, `lane-i-output.md:556-580`, `lane-j-output.md:205-221`, `lane-j-output.md:300-305`).

`[assumed:reasoned]` Planning consequence: the identity seam belongs in `explicit now`, while the exact lifecycle primitive set and whether ownership migration needs first-order planning prominence remain `keep open`.

### 5. Authored artifacts, session snapshots, memory ledgers, and cadence layers

`[evidenced/governing:mixed]` Lane B and the sensitivity map are strongest here: `authored content artifact`, `session snapshot`, `event/editorial wrapper`, `player history`, `room/group history`, `event memory`, and `content calibration history` should not collapse into one noun or one ledger. The current canon already protects part of this seam, but its vocabulary is thinner than the current evidence now justifies (`round-2b-lane-b-history-cadence-output.md:91-149`, `round-2b-sensitivity-map-output.md:95-113`, `ROADMAP.md:34-55`, `ROADMAP.md:76-94`, `ROADMAP.md:154-168`, `REQUIREMENTS.md:99-130`, `01-CONTEXT.md:145-162`).

`[assumed:reasoned]` Planning consequence: the non-collapse rule belongs in `explicit now`; the final nouns and final cadence taxonomy remain `keep open`.

### 6. Audience/public-shell separation and private-first recurrence

`[evidenced/governing:mixed]` The Round 2A convergence is explicit that privacy is not the opposite of community and that bounded public shells should wrap private-first play rather than replace it. Lane A and Lane B each translate that into architecture pressure for audience boundaries, public-shell memory, and layered cadence (`round-2a-experience-archetypes-output.md:221-238`, `round-2a-experience-archetypes-output.md:248-257`, `round-2b-lane-a-room-topology-output.md:214-228`, `round-2b-lane-b-history-cadence-output.md:117-131`, `round-2b-sensitivity-map-output.md:105-113`, `PROJECT.md:131-137`, `LONG-ARC.md:70-81`, `LONG-ARC.md:110-117`).

`[assumed:reasoned]` Planning consequence: private-first plus bounded-shell doctrine should be reaffirmed now; public-shell implementation specifics and exact cadence vocabulary should stay open or deferred.

### 7. Tempo-class sensitivity

`[evidenced/governing:mixed]` `lane-i` and `lane-j` make a real technical distinction between sparse prompt/reveal modes and later higher-tempo action modes, but Round 2A also classifies futures where real-time action defines the whole platform as more speculative than the central private, social, authored experience classes (`round-2a-experience-archetypes-output.md:253-257`, `lane-i-output.md:474-500`, `lane-i-output.md:628-669`, `lane-j-output.md:159-187`, `lane-j-output.md:321-380`).

`[assumed:reasoned]` Planning consequence: Phase 01 and Milestone 01 should not universalize the current event-turn shape as eternal law, but exact higher-tempo transport and authority profiles do not yet warrant `explicit now` treatment. This is mostly a `defer` area with one carry-forward warning.

## Sensitivity and ripple map

`[evidenced/governing:mixed]` The Wave 1.5 map is treated here as a real dependency rather than a hint. Its main conclusion is that the biggest foreclosure risk comes from small-looking simplifications that later harden in Phases 3 through 7 or in canon doctrine, not inside the narrow implementation scope of Phase 01 (`round-2b-sensitivity-map-output.md:36-51`, `round-2b-sensitivity-map-output.md:115-126`, `round-2b-sensitivity-map-output.md:140-195`).

| Pressure cluster | Phase 01-local | Rest of Milestone 01 | Doctrine / canon | Evidence strength | Ledger note |
|---|---|---|---|---|---|
| Container layering and recurrence attachment | Light protective note | High | High | Strong | `explicit now` |
| Visibility, reveal, and topology plurality | Light but real | High | High | Strong | `explicit now` |
| Presence identity and join/lifecycle separation | Light | High | Medium | Strong | `explicit now` on seam, `keep open` on exact primitive set |
| Authority portability and participation rights | Minimal direct effect | High | Medium-high | Medium-strong | `explicit now` on seam, `keep open` on exact capability bundles |
| Authored artifacts, memory ledgers, and cadence layering | Medium | Medium-high | High | Strong | `explicit now` on non-collapse rule |
| Audience/public-shell separation | Very light | Medium | High | Medium-strong | `explicit now` on wrapper boundary |
| Tempo-class sensitivity | None | Low-medium | Medium / later-arc | Suggestive-medium | `defer` exact profile, preserve caution note only |

`[assumed:reasoned]` The key pattern is that `explicit now` rarely means "implement now." It means "name the seam now so later phases do not accidentally erase it."

## Early decision ledger

`[governing:cited]` The classifications below are planning-surface judgments, not immediate implementation commands (`round-2b-lane-c-phase-01-ledger-task-spec.md:46-66`, `round-2b-sensitivity-map-output.md:189-195`).

| Decision surface | Classification | Why this classification lands | Ripple scope | Basis |
|---|---|---|---|---|
| Keep `event_container`, `room`, and `game_instance` logically distinct | `explicit now` | Strongest cross-lane convergence; the shortcut breaks topology, recurrence, and result routing at once | `Milestone 01-wide` and `canonical-doc doctrine`, with light `Phase 01` wording impact | `round-2b-sensitivity-map-output.md:55-63`, `lane-i-output.md:352-385`, `lane-j-output.md:123-141` |
| Treat visibility as scoped publication and reveal as topology-sensitive | `explicit now` | Strong evidence that host-screen-friendly does not mean one truth surface, and that reveal logic is part of product value | `Phase 01-local` light ripple, `Milestone 01-wide` high ripple, doctrine reaffirmation | `round-2b-sensitivity-map-output.md:75-83`, `lane-i-output.md:419-442`, `01-CONTEXT.md:145-162` |
| Preserve `presence identity` apart from `persistent identity` | `explicit now` | Needed so low-friction private join and later progression/event memory do not force a rewrite against one binary identity model | `Milestone 01-wide`, with requirements and roadmap carry-forward | `round-2b-sensitivity-map-output.md:65-73`, `lane-i-output.md:556-580`, `REQUIREMENTS.md:99-130` |
| Preserve authority portability across room admin, progression, moderation, and audience rights | `explicit now` | `host/player` is too flat; this is a real non-foreclosure seam even if the exact role set is unresolved | `Milestone 01-wide` plus doctrine carry-forward | `round-2b-sensitivity-map-output.md:85-93`, `lane-i-output.md:387-417`, `lane-j-output.md:188-201` |
| Keep `authored content artifact`, `session snapshot`, and later wrapper/context nouns distinct | `explicit now` | Phase 01 already needs a wording guard here, and later content/history layers become misleading if `pack` or `session` harden as the only durable nouns | `Phase 01-local`, `Milestone 01-wide`, and doctrine-level | `round-2b-sensitivity-map-output.md:95-103`, `round-2b-lane-b-history-cadence-output.md:109-149`, `01-CONTEXT.md:145-162` |
| Treat memory and cadence as layered rather than singular | `explicit now` | Strong evidence for the non-collapse rule, but not for one final taxonomy | `Milestone 01-wide` and doctrine-level, light `Phase 01` wording effect | `round-2b-lane-b-history-cadence-output.md:117-149`, `round-2b-sensitivity-map-output.md:105-113`, `PROJECT.md:121-137` |
| Keep the exact room-lifecycle primitive set (`invite`, `seat claim`, `lock`, `ownership migration`, `audience-only entry`) unresolved | `keep open` | The seam is real, but the first useful bundle and prominence of ownership migration are still explicitly uncertain | Mostly `Milestone 01-wide` | `round-2b-lane-a-room-topology-output.md:292-301`, `round-2b-sensitivity-map-output.md:163-169` |
| Keep the exact capability bundles and first Milestone 1 role vocabulary unresolved | `keep open` | Evidence supports layered rights, not one canonical first bundle | `Milestone 01-wide` and doctrine carry-forward | `round-2b-lane-a-room-topology-output.md:288-300`, `round-2b-sensitivity-map-output.md:163-169` |
| Keep the final durable group-identity noun and event/editorial wrapper taxonomy unresolved | `keep open` | Need for layered memory is strong; final vocabulary remains under-justified | Mostly doctrine-level | `round-2b-lane-b-history-cadence-output.md:181-189`, `round-2b-sensitivity-map-output.md:163-169`, `HANDOFF.md:126-135` |
| Keep the exact cadence vocabulary and first reuse wrapper ordering unresolved | `keep open` | Separation is justified; the winning taxonomy and sequencing still are not | Doctrine-level and later-arc | `round-2b-lane-b-history-cadence-output.md:181-189`, `PROJECT.md:165-171` |
| Formalize higher-tempo transport/authority profile specifics now | `defer` | Tempo-class sensitivity is real, but exact evented-turn vs realtime profile design would overdetermine current planning from still-secondary futures | Mostly `later-arc only`, with a light Milestone 01 caution note | `round-2a-experience-archetypes-output.md:253-257`, `lane-i-output.md:474-500`, `lane-j-output.md:375-381` |
| Build public-shell participation, moderation, and discovery mechanics into current phase scope | `defer` | Doctrine already defers stronger publicness obligations; the seam should be preserved, not imported | Doctrine reaffirmation and later-arc only | `LONG-ARC.md:70-81`, `LONG-ARC.md:131-142`, `REQUIREMENTS.md:132-138` |

## Shortcuts most likely to cause foreclosure

`[assumed:reasoned]` Ranked by how much cross-phase rewrite they would trigger if accepted early:

1. Collapsing `room = event = active session = recurrence unit`.
2. Treating host-screen presentation as the universal gameplay truth and publishing one shared state blob to every client.
3. Encoding participant authority as only `host` versus `player`, with runtime authority fused to the presenting browser.
4. Treating `pack` or `session snapshot` as the only durable content nouns the system will ever need.
5. Flattening player progression, room/group memory, event memory, and content calibration into one results ledger.
6. Treating join as one monolithic action instead of distinct lifecycle semantics.
7. Letting ambient public identity or public-shell assumptions become the default recurrence model.
8. Letting speculative higher-tempo futures overdetermine the current browser-first private-room architecture.

`[assumed:reasoned]` The single most dangerous tempting shortcut is `room = event = active session = recurrence unit`. It looks efficient because Milestone 1 can visibly behave that way, but it silently damages topology, replay/rematch flow, audience-shell separation, memory layers, and future event structure at the same time (`round-2b-sensitivity-map-output.md:55-63`, `round-2b-lane-a-room-topology-output.md:257-265`, `round-2b-lane-b-history-cadence-output.md:156-163`).

## What should be explicit now

`[assumed:reasoned]` The evidence justifies making the following explicit now in planning surfaces:

- Prix Guesser should distinguish `event_container`, `room`, and `game_instance` logically even if Milestone 1 usually renders them `1:1`.
- Host-screen-friendly should be reaffirmed as a watchability posture, not a one-surface ontology.
- Visibility and reveal should be described as scoped publication problems, not only UI hiding problems.
- `presence identity` and `persistent identity` should be preserved as different conceptual layers.
- Authority should remain portable across room admin, game progression, moderation/operator controls, and audience rights.
- Phase 01 carry-forward language should stop short of implying that `pack` and `session` are the only durable future nouns.
- Doctrine should reaffirm that bounded public or spectator shells wrap private-first play rather than replacing it.
- Memory and cadence should be described as layered concerns even though Milestone 1 only directly implements a narrow subset.

## What should stay open

`[open:reasoned]` The evidence is not strong enough to lock these yet:

- the minimum useful capability bundle for the first serious room-role model
- the full room-lifecycle primitive set and the planning prominence of ownership migration
- the final durable noun for recurring group identity: `room`, `house`, `club`, `cohort`, or something else
- the final vocabulary for `event/editorial wrapper`, `editorial drop`, and `evergreen collection`
- the exact cadence taxonomy and which later wrapper should prove substrate reuse first
- the first topology stress-test that deserves explicit downstream planning priority
- how much persistent structure later event memory really needs versus lighter recap/folklore surfaces

## What can be deferred

`[assumed:reasoned]` These areas can safely remain deferred if the seams above are preserved:

- exact higher-tempo transport profiles, prediction models, rollback, or reconciliation machinery
- formal mode-manifest schema for action-sensitive branches
- public-shell implementation details beyond bounded-wrapper doctrine
- stranger participation, public discovery, and heavier moderation/runtime obligations
- durable event standings or richer public memory structures
- commercialization-shaped access and service obligations

`[governing:cited]` Deferring these is consistent with the existing doctrine: preserve future seams early when cheap, but earn each wrapper and obligation threshold before importing it into active scope (`LONG-ARC.md:56-68`, `LONG-ARC.md:70-81`, `LONG-ARC.md:131-142`, `REQUIREMENTS.md:134-138`).

## Affected artifacts and planning surfaces

| Surface | Judgment | Carry-forward consequence |
|---|---|---|
| `.planning/phases/01-authored-round-contract/01-CONTEXT.md` | Change via light carry-forward note | Preserve reveal semantics without implying one universal viewer surface, and stop short of implying that `pack` and `session` are the only durable future nouns (`01-CONTEXT.md:145-162`). |
| `.planning/ROADMAP.md` | Change via Milestone 01 carry-forward notes | Phase 3 should inherit container separation, authority portability, and presence-vs-persistence identity; Phase 3.1 should inherit multi-surface visibility; Phase 4 should inherit join/rejoin/seat-claim distinction; Phase 5 should inherit audience-readable but not universal reveal logic; Phase 6 should inherit separated content/history ledgers; Phase 7 should inherit lifecycle continuity rather than pure refresh recovery (`ROADMAP.md:76-186`). |
| `.planning/REQUIREMENTS.md` | Change via stronger seam anchors, not new ship-gates | Current seams already protect room-authority separation and wrapper visibility, but they are thinner than the current evidence around active instance separation, presence-vs-persistence identity, visibility-scoped publication, and layered memory/history (`REQUIREMENTS.md:99-138`). |
| `.planning/PROJECT.md` | Change via doctrine clarification | Expand the current `anchor mode / session wrapper / watchability layer / platform shell` vocabulary so host-screen-friendly is not misread as one topology, and private-first does not imply no bounded audience/public shells (`PROJECT.md:45-58`, `PROJECT.md:121-137`). |
| `.planning/LONG-ARC.md` | Change via doctrine reaffirmation and extension | Extend wrapper and visibility doctrine into clearer language about room shell vs active instance, bounded audience shells, and layered memory/cadence while keeping public obligations deferred (`LONG-ARC.md:35-81`, `LONG-ARC.md:110-142`). |
| Future Phase 3 planning artifacts | Explicit carry-forward required | Must not hardcode `room = game_instance = recurrence unit`, or `host = authority = presenter` by default. |
| Future Phase 3.1 planning artifacts | Explicit carry-forward required | Must not freeze the interaction contract around one shared truth surface. |
| Future Phase 4 planning artifacts | Explicit carry-forward required | Must distinguish join path, rejoin, seat claim, and possible audience-only entry. |
| Future Phase 5 planning artifacts | Explicit carry-forward required | Must preserve staged reveal and audience readability without turning private-state modes into shared-state modes. |
| Future Phase 6 planning artifacts | Explicit carry-forward required | Must keep content calibration/history separate from player, room/group, and event memory. |
| Future Phase 7 planning artifacts | Explicit carry-forward required | Must treat reconnect as room-lifecycle and authority continuity work, not only state reload. |

## Open uncertainties and further research needs

`[open:reasoned]` The strongest unresolved questions after this ledger are:

- what the first useful capability bundle actually is for a private-room-first milestone
- whether ownership migration deserves first-order planning treatment or only a carry-forward note
- what doctrine term should hold recurring group identity without prematurely locking the social ontology
- what the right wrapper taxonomy is for later editorial/event surfaces
- how much explicit event-memory persistence later shells would truly need
- whether any credible future action mode actually earns deeper transport complexity, or whether staged reduction and event-shell structure will remain the more appropriate answer

`[assumed:reasoned]` None of those uncertainties weaken the stronger non-collapse judgments above. They only narrow where the ledger should refuse fake certainty.

## Phase 01 and Milestone 01 feed-in

`[assumed:reasoned]` Phase 01 should stay narrow. The ledger does not justify widening the authored-round contract into room runtime, identity, moderation, or public-shell implementation. It does justify three protective notes:

- Phase 01 future-awareness should preserve authored artifact versus later session/wrapper separation.
- Phase 01 reveal language should not imply one universal viewer surface.
- Phase 01 stable-identity language should remain reusable across later snapshots, calibration, wrapper reuse, and layered history without importing persistence features now.

`[evidenced:reasoned]` No current finding justifies reordering Milestone 01. The roadmap sequence still makes sense as written (`round-2b-sensitivity-map-output.md:140-151`, `ROADMAP.md:23-30`, `ROADMAP.md:190-202`).

`[assumed:reasoned]` The actual Milestone 01 effect is on protected seams, not sequence:

- Phase 3 should plan around room-shell vs active-instance separation and authority portability.
- Phase 3.1 should plan around multi-surface visibility rather than only `host screen + controller`.
- Phase 4 should plan around graded join/lifecycle semantics.
- Phase 5 should plan around reveal/watchability without universalizing one truth surface.
- Phase 6 should plan around separate content and social/history ledgers.
- Phase 7 should plan around reconnect as lifecycle continuity.

## Dependencies and relations

`[evidenced:cited]` This ledger depends directly on the governance stack, the Round 2A archetype convergence, the Round 2B Wave 1 lane outputs, the Wave 1.5 sensitivity map, the earlier architecture exposure lanes, and the currently active canon/Phase 01 context (`round-2b-lane-c-phase-01-ledger-task-spec.md:14-25`, `round-2b-foreclosure-synthesis-task-spec.md:88-154`, `round-2b-sensitivity-map-output.md:206-212`).

`[governing:cited]` It is an upstream input to the authoritative final Round 2B closure artifact, not a replacement for it (`round-2b-lane-c-phase-01-ledger-task-spec.md:115-121`, `round-2b-foreclosure-synthesis-task-spec.md:156-173`).

`[assumed:reasoned]` Coverage judgment:

- `GAP-05`: answered strongly. This artifact converts the experience map plus engineering exposure into an explicit early-decision ledger instead of leaving them as parallel research streams.
- `GAP-08`: answered strongly. The Phase-01-facing and Milestone-01-facing decision surface is now explicit, with `explicit now / keep open / defer` judgments and named ripple surfaces.
- `RESP-04`: materially advanced but still not closed here, because the main-thread synthesis still owns the final integrated foreclosure statement.
