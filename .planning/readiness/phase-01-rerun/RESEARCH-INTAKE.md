# Research Intake

This file records how completed or in-flight research bundles are absorbed into the readiness package.

The point is not just to list related research.
The point is to state:

- whether the research is readiness-critical or only conditional follow-through
- what parts are accepted now
- what remains open
- which readiness artifacts must change because of it
- whether it creates tasks, deferrals, or gate conditions

## Intake Rules

For each relevant research bundle, record:

- `relation to readiness`
  - `blocking`
  - `supporting`
  - `conditional follow-through`
  - `deferred`
- `intake status`
  - `pending review`
  - `accepted`
  - `partially accepted`
  - `parked`
  - `superseded`
- `current consequences`
  What changes the package should honor now.
- `later consequences`
  What should be revisited later, if anything.
- `package surfaces affected`
  Which of:
  - `PLAN.md`
  - `STATUS.md`
  - `STATE.yaml`
  - `TASKS.md`
  - `DEFERRED.md`
  - gate files
  - `CHECKPOINT-LEDGER.md`

If a research bundle has no current package consequences, say that explicitly.

## Current Intake

### Multi-layer Harness Governance Audit

- bundle:
  - [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md)
  - [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md)
- relation to readiness: `blocking`
- intake status: `partially accepted`
- current consequences:
  - Checkpoint 0 remains active until the `01`-`06` bundle is repaired and re-reviewed.
  - The governance-doc normalization audit is still the next major readiness layer after Checkpoint 0 closes.
  - Stronger governance/harness doctrine may require cross-vendor reread at later high-stakes gates.
- later consequences:
  - if normalization proves important rule ownership belongs in machinery, escalate to conditional harness follow-through
- package surfaces affected:
  - `PLAN.md`
  - `STATUS.md`
  - `STATE.yaml`
  - `TASKS.md`
  - `GATES/checkpoint-0.md`
  - `GATES/checkpoint-4.md`

### Codex Compaction Context Audit

- bundle:
  - [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md)
  - [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md)
  - [03-compaction-context-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/03-compaction-context-response.md)
- relation to readiness: `supporting`
- intake status: `accepted`
- current consequences:
  - use the readiness package as a durable control surface rather than relying on transcript continuity
  - use the session re-entry checklist for resumed or suspect-compaction sessions
  - use the current readiness-specific compact prompt as an immediate mitigation
- later consequences:
  - design a project-wide compact prompt after stable control surfaces are clearer
- package surfaces affected:
  - `PLAN.md`
  - `TASKS.md`
  - `DEFERRED.md`
  - `STATUS.md`

### Model Assignment And Cross-Audit Research

- bundle:
  - [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md)
  - [02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md)
- relation to readiness: `supporting`
- intake status: `accepted`
- current consequences:
  - use current model policy as settled readiness input
  - treat cross-vendor audit as a selective requirement at later high-stakes review boundaries, not as an every-artifact ritual
- later consequences:
  - if external audit becomes routine, define cleaner workflow/harness ownership for it
- package surfaces affected:
  - `PLAN.md`
  - `TASKS.md`
  - `STATUS.md`
  - `STATE.yaml`
  - `GATES/checkpoint-4.md`

### Cross-Model Audit Integration Research

- bundle:
  - [00-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-cross-model-audit-integration-research/00-launch-bundle-spec.md)
  - [01-cross-model-audit-integration-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-cross-model-audit-integration-research/01-cross-model-audit-integration-task-spec.md)
- relation to readiness: `conditional follow-through`
- intake status: `pending review`
- current consequences:
  - none beyond the existing readiness note that dedicated cross-model-audit mechanism design is conditional, not a current blocker
- later consequences:
  - depending on the result, update readiness tasks/deferrals and possibly the later harness-follow-through sequence
- package surfaces affected:
  - likely `PLAN.md`
  - `TASKS.md`
  - `DEFERRED.md`
  - possibly later gate files
