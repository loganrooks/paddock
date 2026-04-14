---
date: 2026-04-13
audit_subject: artifact_analysis
audit_orientation: exploratory
audit_delegation: self
scope: "Round 2A task spec: calibration repair and experience-archetype mapping for the game-modes audit"
triggered_by: "manual: follow-on from 00-governance/next-round-gap-review.md"
tags:
  - exploratory-audit
  - round-2a
  - task-spec
  - experience-archetypes
  - calibration
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/next-round-artifact-sequence.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/next-round-gap-review.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/AUDIT-EXECUTION-PLAN-game-modes-r1.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/round-1-output.md
---

# Round 2A Task Spec

## Position in the sequence

This task spec is the first response artifact after:

- `00-governance/review-trail-framework.md`
- `00-governance/next-round-gap-review.md`

It is meant to answer:

- `RESP-01`
- `RESP-02`
- `RESP-03`

It is not yet meant to close:

- `RESP-04`

That later foreclosure synthesis should come after the experience map is clearer.

## What this round is

This is a calibration-and-experience round.

It is not:

- another general family-deepening round
- another broad net-new ideation spray
- the final architecture-foreclosure synthesis
- a mixed large-room plus broad architecture lane

It is:

- a repair of the carry-forward calibration
- an explicit mapping of concrete user-experience archetypes the platform may want to support
- a bridge between the original handoff's broader experience questions and the later architecture research

## Governing carry-forward

This round must inherit the following creator-corrected methodological commitments:

- treat promising ideas as design terrain, not prematurely fixed pitches
- do not impose one ontology across the whole portfolio
- let each game's ontology emerge from the game itself where relevant
- preserve the tension between cultural charge and mechanical spine where that tension is load-bearing
- do not overconstrain exploration by turning examples into mandatory branches
- allow absurd but still F1-rooted realizations
- do not mix broad architecture exposure with large-room feasibility unless explicitly asked
- keep space for judgment where abstraction is appropriate, but make traceability, justification, and epistemic reliability concrete

## Steering-source rule

Primary steering sources for Round 2A are:

- `00-governance/review-trail-framework.md`
- `00-governance/next-round-gap-review.md`
- this task spec and the Round 2A lane bundle

Background-only historical sources:

- `01-round-1/round-1-self-eval.md`
- `03-next-round/round-2-prompts.md`

These may still be consulted, but they should not override the newer governance and gap-review artifacts.

## Core question

What are the most important concrete user experiences Prix Guesser may want to support as it matures, and what do those experiences imply about the shape of the product before we even get to a narrower foreclosure synthesis?

## Required experience classes

This round should explicitly consider at least:

1. `local recurring party night`
2. `private online synchronous group`
3. `solo async ritual / race-weekend return loop`
4. `community / public / streamer-adjacent event shell`
5. `hybrid or unconventional local forms`
   examples may include host-screen plus phones, separate rooms, partial separation, or other topology-sensitive local play

These are not assumed to be equally important.
They are required comparison classes.

## Required questions

For each experience class, ask:

- what actually happens from the player's point of view?
- what social texture does it create?
- what kinds of games or mode shapes fit it especially well?
- what does it want from room shape, input/display topology, and authority?
- what kind of community, privacy, or persistence does it want?
- what kinds of experiences would distort or fail in this class?
- how might it change the strongest realization of an already-known idea?

## Handoff alignment

This round should explicitly answer the still-open parts of:

- `HANDOFF.md` Thread 2: multiplayer shapes and social experiences
- `HANDOFF.md` Thread 3: platform maturity vision
- the experience-facing side of Thread 5: architectural foreclosure

It should not yet pretend to fully answer the architecture side of Thread 5.

## Required output sections

1. `Calibration carry-forward`
2. `Path of inquiry`
3. `Experience archetype map`
4. `Per-archetype pressures and opportunities`
5. `How existing game territories read differently under each archetype`
6. `Community, privacy, recurrence, and event cadence`
7. `Which experiences feel central, peripheral, or speculative`
8. `What this round parks for later foreclosure synthesis`
9. `Dependencies and relations`

## Anti-goals

Do not:

- collapse back into ranking game families as the main task
- treat every mode as if it must support every context
- turn one creator example into the center of the taxonomy
- smuggle the full foreclosure synthesis into this round
- smuggle the large-room research question back into this round as if it were the same thing

## Output target

Primary intended artifact:

- `round-2a-experience-archetypes-output.md`

If the work is split later across lanes, the synthesis should still land there or in a clearly named successor artifact.

## Planned decomposition

The current planned split for launch is:

- `03-next-round/round-2a-lane-common-scaffold.md`
- `03-next-round/round-2a-lane-a-local-party-task-spec.md`
- `03-next-round/round-2a-lane-b-private-online-task-spec.md`
- `03-next-round/round-2a-lane-c-solo-async-task-spec.md`
- `03-next-round/round-2a-lane-d-community-event-task-spec.md`

The lane split is meant to prevent local party, remote sync, solo async, and community/event-shell experiences from being flattened back together too early.

## What should follow this round

If this round succeeds, the next artifact should be a narrower foreclosure synthesis that maps the experience archetypes plus engineering exposure research into:

- what early architecture must keep open
- what should already be explicit
- what can safely wait
