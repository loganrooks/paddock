# Cross-Model Audit Integration Research

Date: 2026-04-15  
Status: launch-ready spec

## Purpose

Determine whether and how cross-vendor / cross-model audit should be integrated into this repo's standing workflows and harness surfaces.

This is not an instruction to create a new skill by default.

The point is to decide:

- where cross-vendor audit is actually necessary
- where it is merely helpful
- what should own that behavior
- whether existing surfaces already cover the needed cases

## Motivating Grounds

- [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md)
- [02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md)
- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
- [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
- [DEFERRED.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEFERRED.md)
- [gsd-review](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md)
- [gsdr-audit](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md)

## Core Questions

1. For this repo's important work types, where is cross-vendor audit:
   - necessary
   - strongly preferred
   - optional
   - wasteful
2. Can the needed behavior be carried cleanly by current surfaces:
   - standing governance docs
   - direct top-level orchestration
   - `gsd-review`
   - `gsdr-audit`
3. If current surfaces are insufficient, what is the smallest correct intervention:
   - workflow guidance
   - task-spec pattern
   - command/skill extension
   - new skill
4. How should external audit integrate with checkpointing, commit boundaries, and later expert review?
5. What should be readiness-specific now, and what should become project-wide later?

## Expected Output

Write:

- [01-cross-model-audit-integration-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-cross-model-audit-integration-research/01-cross-model-audit-integration-research.md)

The output should give:

- a work-type matrix
- current-surface assessment
- gap assessment
- near-term readiness recommendation
- later project/harness recommendation
- explicit answer on whether to create a dedicated cross-model-audit skill now
