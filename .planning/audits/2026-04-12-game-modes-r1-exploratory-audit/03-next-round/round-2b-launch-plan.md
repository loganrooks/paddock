---
date: 2026-04-13
audit_subject: process_review
audit_orientation: exploratory
audit_delegation: self
scope: "Launch plan for Round 2B foreclosure synthesis"
triggered_by: "manual: post-Round-2A preparation"
tags:
  - exploratory-audit
  - round-2b
  - launch-plan
  - wave-based
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-foreclosure-synthesis-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-experience-archetypes-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-output.md
---

# Round 2B Launch Plan

## Position in the sequence

This plan sits between:

- the Round 2A experience map
- the Round 2B lane launches

It assumes a prelaunch meta-review may still tune the bundle before any substantive dispatch.

## Why Round 2B is wave-based

Round 2B should not run as one agent and should not run as three fully parallel lanes.

Main reason:

- the Phase 01 decision ledger depends on the pressure mapping work

So the correct shape is:

- `Wave 1`
  pressure-mapping lanes in parallel
- `Wave 1.5`
  dedicated sensitivity/ripple synthesis from the Wave 1 outputs
- `Wave 2`
  decision-ledger synthesis built from the sensitivity map plus the existing experience and engineering research

## Central ownership

The main thread should retain ownership of:

- policy adherence and launch verification
- final cross-wave comparison
- whether the Wave 2 decision ledger is good enough to stand
- final signoff on what feeds later Phase 01 planning
- final signoff on what affects the rest of Milestone 01 and the canonical planning docs
- the authoritative `RESP-04` closure artifact: `round-2b-foreclosure-synthesis-output.md`

## Proposed Wave 1 lane set

### Lane A: Room / topology / authority / visibility

Main scope:

- event container vs room vs active session
- host/player/audience surfaces
- topology-sensitive local and remote forms
- authority boundaries
- visibility scopes and staged reveals

Why separate:

- these questions are tightly coupled and heavily influenced by the Round 2A local/private-sync/event-shell outputs

### Lane B: Identity / history / cadence / content model

Main scope:

- player, group, and house memory
- recurrence and shadow-community layers
- editorial cadence and event scheduling
- content/runtime model
- private-first vs public-shell persistence layers

Why separate:

- these pressures come mostly from solo async, recurring group ritual, and event-shell maturity rather than from room transport alone

## Proposed Wave 1.5 artifact

### Sensitivity and ripple map

Main scope:

- consolidate Lane A and Lane B into one explicit ripple matrix
- identify whether each effect is Phase 01-local, Milestone 01-wide, doctrine-level, or later-arc only
- identify which planning artifacts would need updating or explicit carry-forward notes

Why separate:

- this is the missing translation layer between pressure discovery and planning judgment
- it prevents Lane C from inventing ripple analysis second-hand

## Proposed Wave 2 lane

### Lane C: Phase 01 decision ledger

Main scope:

- synthesize the sensitivity map plus the already existing engineering research
- produce a draft `explicit now`, `keep open`, and `defer` ledger
- identify which planning surfaces are phase-local, Milestone 01-wide, or doctrine-level
- name the shortcuts most likely to cause foreclosure

Why second wave:

- it depends on the pressure map rather than merely running beside it
- it prepares the planning-facing draft, but the final `RESP-04` closure still belongs to the main-thread synthesis artifact

## Recommended output set

- `round-2b-lane-a-room-topology-output.md`
- `round-2b-lane-b-history-cadence-output.md`
- `round-2b-sensitivity-map-output.md`
- `round-2b-lane-c-phase-01-ledger-output.md`
- `round-2b-foreclosure-synthesis-output.md`

## Dependency logic

Wave 1 outputs should feed:

- the Wave 1.5 sensitivity map
- the main thread's final synthesis

The Wave 1.5 sensitivity map should feed:

- the Wave 2 ledger lane
- the main thread's final synthesis

The final synthesis should then feed:

- Phase 01 planning inputs
- Milestone 01 roadmap and requirement posture where affected
- doctrine-layer carry-forward for `.planning/PROJECT.md` and `.planning/LONG-ARC.md` where affected
- later architecture and room-model decisions

Authoritative closure rule:

- `round-2b-foreclosure-synthesis-output.md` is the only final `RESP-04` closure artifact
- `round-2b-lane-c-phase-01-ledger-output.md` is a required upstream input, not a competing final answer

## What not to do at launch

Do not:

- collapse Wave 1 and Wave 2 into one mushy architecture pass
- let one lane quietly decide the whole product center of gravity
- smuggle in new large-room research
- ask any lane to pick a technical stack
- let older stale carry-forward artifacts become hidden steering sources again

## Ready-to-launch condition

Round 2B is ready to launch when:

- the prelaunch meta-review finds no blocking split or dependency problem
- Wave 1 and Wave 2 responsibilities are clearly separated
- the bundle is traceable back to `RESP-04`
- the lanes are concrete enough to produce planning-facing output rather than another abstract discussion
