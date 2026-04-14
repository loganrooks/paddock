---
date: 2026-04-13
audit_subject: artifact_analysis
audit_orientation: exploratory
audit_delegation: self
scope: "Round 2B Lane A: room, topology, authority, visibility, and audience-shell pressures"
triggered_by: "manual: Round 2B preparation"
tags:
  - exploratory-audit
  - round-2b
  - lane-a
  - room-model
  - topology
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/next-round-gap-review.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-foreclosure-synthesis-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-experience-archetypes-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-a-local-party-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-b-private-online-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-d-community-event-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
---

# Round 2B Lane A Task Spec

## Lane purpose

This lane maps the early architectural pressures created by:

- local recurring party topology
- private online sync topology
- hybrid and same-house-separated forms
- bounded public/event shells that introduce audience and host surfaces

It should answer:

- what kinds of `room`, `event`, `session`, `authority`, and `visibility` separations need to stay open

It should not answer:

- long-horizon identity/history/cadence questions except where they directly affect room shape
- the final Phase 01 decision ledger

## Traceability and scope

This lane directly supports:

- `RESP-04`

It most strongly informs:

- `GAP-05`
- `GAP-08`

It also uses the outputs of `RESP-03` as its main product-experience inputs.

## Required focus

This lane must explicitly reason about:

- `event container` vs `room` vs `active game instance`
- room lifecycle mechanics such as join, seat claim, invites, rejoin, locking, and ownership migration
- host screen vs handset vs private screen vs audience surface
- local shared-stage vs topology-sensitive separated-local forms
- private-room vs public-shell boundaries
- authority roles beyond simple `host/player`
- visibility-scoped state and staged reveal
- topology differences that matter enough to shape early abstractions
- where those judgments would ripple into `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, and relevant phase context/plan artifacts

## Required questions

Ask:

- which experience classes break if room and game instance are collapsed?
- which experience classes break if everyone is assumed to share one information surface?
- where do host, operator, judge, audience, narrator, or moderator roles become structurally important?
- which topologies need to be modeled as first-class possibilities even if they are not all Phase 01 features?
- what early UI/runtime shortcuts would later make private-sync, same-house-separated, or public-shell futures awkward or expensive?
- which of those consequences are only Phase 01-local, which affect the rest of Milestone 01, and which rise to doctrine-level planning surfaces?
- if a room/topology judgment lands, which planning artifacts would need explicit updates or carry-forward notes?

## Steering precedence

Primary steering order for this lane is:

1. `00-governance/review-trail-framework.md`
2. `00-governance/next-round-gap-review.md`
3. `03-next-round/round-2b-foreclosure-synthesis-task-spec.md`
4. `03-next-round/round-2a-experience-archetypes-output.md`
5. `02-lanes/architecture/lane-i-output.md` and `02-lanes/architecture/lane-j-output.md`

The Round 2A lane-specific outputs are corroborative, not controlling.
`HANDOFF.md` supplies motivating questions and original pressure, not binding solution shape.

## Anti-goals

Do not:

- pick a networking library
- overfit to large-room patterns
- treat audience shell as identical to active participation
- decide product priority by room model alone

## Output target

- `round-2b-lane-a-room-topology-output.md`
