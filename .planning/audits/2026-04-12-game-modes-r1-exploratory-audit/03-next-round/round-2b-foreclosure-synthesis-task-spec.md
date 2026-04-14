---
date: 2026-04-13
audit_subject: artifact_analysis
audit_orientation: exploratory
audit_delegation: self
scope: "Round 2B task spec: experience-to-architecture foreclosure synthesis"
triggered_by: "manual: follow-on from Round 2A experience mapping"
tags:
  - exploratory-audit
  - round-2b
  - foreclosure
  - architecture
  - task-spec
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/next-round-gap-review.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-experience-archetypes-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
---

# Round 2B Task Spec

## Position in the sequence

This artifact follows:

- `03-next-round/round-2a-experience-archetypes-output.md`
- `02-lanes/architecture/lane-i-output.md`
- `02-lanes/architecture/lane-j-output.md`

It is meant to answer:

- `RESP-04`

It should also tighten the planning-facing consequences of:

- `RESP-03`

It is not a new ideation round.

Although the immediate next consumer is still the next planning wave, this round is not only about `Phase 01`. It should identify ripple effects across:

- the rest of Milestone 01
- the canonical planning doctrine in `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, and `.planning/REQUIREMENTS.md`
- current and future phase steering artifacts where those assumptions are carried forward

## What this round is

This is a foreclosure synthesis round.

It is meant to answer:

- which concrete user experiences pressure which early architectural decisions
- which early shortcuts would silently foreclose which promising futures
- what should be explicit now, what should stay open, and what can safely wait

It is not meant to:

- rank game families again
- pick a final frontend stack
- rerun large-room research as if it were the whole architecture question
- treat one reference mechanism as the obvious solution
- collapse the whole product into one canonical room shape

## Governing carry-forward

This round must inherit the creator-corrected carry-forward already stabilized in Round 2A:

- treat ideas and mode territories as design terrain, not prematurely fixed implementations
- do not force one ontology across the whole portfolio
- let each game's own ontology matter
- preserve cultural charge together with mechanical spine where that tension is load-bearing
- treat examples as probes rather than mandatory branches
- allow absurd but still F1-rooted realizations
- separate broad architecture exposure from large-room feasibility
- make traceability, justification, and epistemic reliability concrete

This round adds one more methodological rule:

- do not let architectural language quietly replace lived product language

If a claimed early decision cannot be traced back to a concrete experience pressure, it should be treated with suspicion.

`HANDOFF.md` should be treated here as a source of motivating questions and original problem pressure, not as binding solution authority.

## Steering-source rule

Primary steering sources for Round 2B are:

- `00-governance/review-trail-framework.md`
- `00-governance/next-round-gap-review.md`
- this task spec and the Round 2B lane bundle
- `03-next-round/round-2a-experience-archetypes-output.md`
- `02-lanes/architecture/lane-i-output.md`
- `02-lanes/architecture/lane-j-output.md`
- `HANDOFF.md`

Background-only historical sources:

- `01-round-1/round-1-self-eval.md`
- `03-next-round/round-2-prompts.md`
- older mixed architecture artifacts that predate the lane separation

These may still be cited, but they should not override the newer governance, experience-map, and engineering-exposure artifacts.

## Core question

Given the now-mapped experience archetypes, what early architectural decisions need to remain open or become explicit so that Prix Guesser does not silently foreclose its strongest mature-product futures, and which planning surfaces would those judgments need to change or constrain?

## Required synthesis axes

This round must explicitly map experience pressures against at least:

1. `event container`, `room`, and `active game/session instance`
2. topology and input/display surfaces
3. authority boundaries and operator roles
4. visibility scopes and staged reveal surfaces
5. identity, history, recurrence, and memory layers
6. editorial cadence, content/runtime model, and event scheduling
7. audience/public-shell boundaries and moderation/operator needs
8. tempo classes and transport sensitivity
9. planning posture: `explicit now`, `keep open`, `defer`
10. artifact and doctrine ripple surface:
    `phase-local`, `Milestone 01-wide`, `canonical-doc doctrine`, or `later-arc only`

## Required questions

For each major pressure cluster, ask:

- which concrete experience or experiences create this pressure?
- what exact early shortcut would damage or distort that experience later?
- what seam, separation, or abstraction would keep the future open?
- is this something that must be explicit in Phase 01, or merely not foreclosed?
- is the consequence phase-local, Milestone 01-wide, or doctrine-level?
- which planning artifacts would need to change or carry the result if this judgment lands?
- what is still too uncertain to lock now?

## Required output sections

1. `Calibration carry-forward`
2. `Path of inquiry`
3. `Experience-to-architecture pressure map`
4. `Sensitivity and ripple map`
5. `Early decision ledger`
6. `Shortcuts most likely to cause foreclosure`
7. `What should be explicit now`
8. `What should stay open`
9. `What can be deferred`
10. `Affected artifacts and planning surfaces`
11. `Open uncertainties and further research needs`
12. `Phase 01 and Milestone 01 feed-in`
13. `Dependencies and relations`

## Authoritative closure contract

The authoritative `RESP-04` closure artifact for Round 2B is:

- `round-2b-foreclosure-synthesis-output.md`

Ownership:

- the main thread owns that final artifact

Lane C is not itself the final closure artifact.
Lane C is a required upstream input that prepares a Phase-01-facing draft ledger for the main-thread final synthesis.

If Lane C and the final synthesis diverge:

- the final synthesis must explicitly note the divergence and why

That rule exists so `RESP-04` closes in one clearly named place rather than being split across multiple documents.

## Anti-goals

Do not:

- pretend the product must optimize every experience class equally
- force all modes into one room model
- turn the engineering-exposure research into architecture cargo culting
- confuse "large participation" with "one giant fully coupled room"
- smuggle broad new ideation into the center of this round
- overstate confidence where the evidence is only suggestive

## Output target

Primary intended artifact:

- `round-2b-foreclosure-synthesis-output.md`

Supporting artifacts may include wave outputs if the round is split.

## Planned decomposition

Round 2B is expected to run in waves:

- `03-next-round/round-2b-lane-common-scaffold.md`
- `03-next-round/round-2b-lane-a-room-topology-task-spec.md`
- `03-next-round/round-2b-lane-b-history-cadence-task-spec.md`
- `03-next-round/round-2b-sensitivity-map-task-spec.md`
- `03-next-round/round-2b-lane-c-phase-01-ledger-task-spec.md`

Wave 1 should surface the architecture pressures.
Wave 1.5 should consolidate the ripple and sensitivity map.
Wave 2 should consolidate that map into a planning-facing ledger.

## What should follow this round

If Round 2B succeeds, the next planning-facing artifacts should be:

- a compact Phase 01 decision memo or ledger
- updates or explicit carry-forward notes for any affected Milestone 01 canonical docs
- explicit non-foreclosure notes that can feed phase planning
- a cleaner answer to the handoff's architecture-facing open threads
