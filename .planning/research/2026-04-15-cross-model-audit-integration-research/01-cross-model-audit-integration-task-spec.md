# Cross-Model Audit Integration Task Spec

Date: 2026-04-15  
Status: launch-ready

## Objective

Determine how cross-vendor / cross-model audit should be integrated into this repo's workflows, readiness gates, and harness surfaces without overbuilding or duplicating existing mechanisms.

This is a design-and-ownership question, not a request to implement a new skill immediately.

## Output

Write:

- [01-cross-model-audit-integration-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-cross-model-audit-integration-research/01-cross-model-audit-integration-research.md)

## Required Onboarding

Read these first and use them as the authority stack for the task:

1. [02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md)  
   Significance:
   current repo policy baseline for model selection and cross-vendor audit preference.

2. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)  
   Significance:
   active rerun-readiness sequence and the checkpoints where stronger independent review may matter.

3. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md) and [DEFERRED.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEFERRED.md)  
   Significance:
   current live placement of conditional follow-through and the explicit deferral of dedicated skill creation.

4. [gsd-review](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md)  
   Significance:
   existing repo-local external review surface, currently scoped to phase-plan peer review from external AI CLIs.

5. [gsdr-audit](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md)  
   Significance:
   broader audit orchestration surface that may already cover some of the needed ownership territory.

6. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md), and [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)  
   Significance:
   standing repo doctrine on delegation, checkpointing, review quality, and where general operating rules should live.

Read additional files only if they materially improve the answer.

## Questions To Answer

1. Across this repo's important work types, where is cross-vendor audit:
   - necessary
   - strongly preferred
   - optional
   - counterproductive

At minimum, consider:

- governance-doc normalization
- high-stakes harness/governance audits
- canon-sensitive synthesis
- rerun-readiness verification
- doctrine-sensitive Phase 01 planning
- routine execution verification
- stubborn debugging

2. What can current surfaces already do well enough?

Evaluate at least:

- direct top-level orchestration
- `gsd-review`
- `gsdr-audit`
- standing doc-level policy

3. Where are the real gaps?

Distinguish:

- missing guidance
- missing workflow integration
- missing mechanism
- missing vendor/tool availability

4. What should own the behavior if we do more?

Answer whether the next step should be:

- no new mechanism; keep it as doctrine + orchestration
- patch an existing workflow or skill
- create a reusable task-spec / protocol pattern
- create a new dedicated skill

If you recommend a new skill, justify why existing surfaces are insufficient.

5. How should this interact with Git/checkpoint discipline?

Address:

- commit-before-delegation baselines
- review boundaries
- attribution for later expert audit
- whether external audit should occur before or after verification / fix passes in different situations

## Constraints

- Do not recommend a new skill merely because the concept is important.
- Prefer the smallest mechanism that preserves clarity, auditability, and reuse.
- Do not treat high-stakes independent review as if it must occur on every artifact.
- Do not collapse current readiness-specific needs into permanent repo-wide doctrine without justification.
- Keep the answer grounded in this repo's actual workflow surfaces, not abstract process preference.

## Output Shape

Use this structure:

1. `Problem framing`
2. `Work-type matrix`
3. `Current surfaces and what they already cover`
4. `Real gaps`
5. `Near-term readiness recommendation`
6. `Longer-term project / harness recommendation`
7. `Decision on dedicated cross-model-audit skill`
8. `Recommended next actions`

For load-bearing claims, follow current repo claim-type and source-basis conventions.
