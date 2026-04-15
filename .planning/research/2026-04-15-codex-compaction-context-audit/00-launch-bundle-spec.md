# Codex Compaction And Context Behavior Audit

Date: 2026-04-15
Status: launch-ready

## Why This Exists

This bundle exists to answer a concrete operational question before more rerun-readiness work continues:

- what exactly happens during Codex compaction
- whether there are compaction-triggered hooks or other mechanism surfaces we can use
- why compaction appears to happen before the visible context meter reaches zero
- why post-compaction free-context can still remain far below `100%`
- whether other users have recently reported similar behavior and what workarounds they have found
- whether repo-local instruction loading or other context surfaces are wasting meaningful window budget

The immediate motivating conversation pressure was:

- need to preserve important readiness/rerun context across compaction
- frustration that compaction appears expensive and partially opaque
- desire to understand whether we can inject or force-read key readiness files after compaction
- desire to understand whether recent public reports suggest similar limits or practical mitigations

## Questions To Answer

1. What does official OpenAI Codex documentation say about:
   - compaction or context summarization behavior
   - AGENTS instruction loading
   - any relevant hook, session, or startup surfaces that affect post-compaction recovery
2. Are there official or credible recent public reports from approximately the last month that describe:
   - early compaction
   - partial context recovery after compaction
   - unexpectedly high persistent context usage
   - practical mitigations or workflow adjustments
3. Given this repo's structure, what is the most plausible explanation for:
   - non-zero baseline context usage
   - partial rather than full post-compaction headroom
   - instruction/file-loading overhead
4. What concrete actions should this repo take now, if any?

## Source Priorities

Priority order:

1. official OpenAI Codex docs and related official OpenAI sources
2. recent GitHub issues, discussions, or forum/community threads from roughly 2026-03-15 onward
3. other recent credible public reports only if needed

## Output Requirements

Write:

- [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md)

The output should include:

- direct answer on whether compaction hooks exist
- direct answer on what is known vs unknown about Codex compaction behavior
- explicit distinction between official evidence and recent public reports
- repo-specific interpretation for this project
- concrete recommended mitigations

## Claim / Citation Requirements

This is a load-bearing planning/process artifact.

Use the current repo claim notation for load-bearing claims where it materially helps:

- `[type:support:basis]`

Examples:

- `[e:c:i]`
- `[e:c:d]`
- `[p:r:i+d]`

For citations:

- internal cited claims must cite concrete repo file paths and line numbers near the claim
- external-direct claims should use markdown footnotes plus `External Works Cited`
- external-traceable claims should identify the local artifact and the traced external source when relevant

## Relevant Local Inputs

- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [PHASE-01-RERUN-READINESS-PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PHASE-01-RERUN-READINESS-PLAN.md)
- [INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md)
- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)

## Non-Goals

- do not drift into broader repo-ops or deployment governance unless directly relevant to compaction/context behavior
- do not rewrite the readiness package in this lane
- do not attempt speculative claims about hidden Codex internals without clearly marking them as inference
