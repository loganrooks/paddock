---
date: 2026-04-13
audit_subject: process_review
audit_orientation: exploratory
audit_delegation: self
scope: "Artifact sequence and dependency map for the next review -> prompt -> output chain"
triggered_by: "manual: follow-on after review-trail framework creation"
tags:
  - exploratory-audit
  - next-round
  - sequencing
  - dependencies
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/AUDIT-EXECUTION-PLAN-game-modes-r1.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/round-1-self-eval.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2-prompts.md
---

# Next-Round Artifact Sequence

## Purpose

This file records the intended dependency order for the next audit artifacts so the trace chain stays inspectable.

Governing framework:

- `00-governance/review-trail-framework.md`

## Sequence

### Step 1: Detailed review and gap register

Artifact:

- `00-governance/next-round-gap-review.md`

Purpose:

- record the substantive gaps, stale artifacts, creator corrections, and unresolved architectural-foreclosure needs
- turn those into a traceable gap register with requested responses

This is the source-of-truth review artifact.

### Step 2: Next-round prompt or task spec

Artifact:

- `round-2a-task-spec.md` or a more precise successor name

Purpose:

- inherit from the gap review rather than from stale carry-forward docs alone
- identify which gap IDs it is answering
- state what is intentionally left for later

This is the response-request artifact.

### Step 3: Next-round output or synthesis

Artifact:

- to be named after the actual next-round structure

Purpose:

- report what it answered
- mark full, partial, or unresolved coverage against the requested response
- preserve open questions and scope expansions

This is the response artifact.

### Step 4: Follow-up review

Artifact:

- future review file, only after the next-round output exists

Purpose:

- assess whether the response actually closed, partially addressed, or missed the prior gaps

This is the reassessment artifact.

## Dependency map

- `00-governance/review-trail-framework.md`
  governs all later artifacts in this chain
- `00-governance/next-round-gap-review.md`
  depends on the framework and current audit corpus
- the next-round prompt
  depends on the gap review
- the next-round output
  depends on the prompt and should report against it
- the follow-up review
  depends on the output and the prior gap review

## Immediate work order

1. write `00-governance/next-round-gap-review.md`
2. use it to replace or supersede stale prompting artifacts
3. only then dispatch the next round

## Anti-patterns this sequence is meant to prevent

- writing a new prompt straight from memory or current conversation mood
- treating stale carry-forward docs as current source-of-truth
- producing an output that cannot be mapped back to specific gaps
- reassessing a round without a clear record of what it was asked to do
