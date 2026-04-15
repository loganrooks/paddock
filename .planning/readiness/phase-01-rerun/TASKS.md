# Readiness Tasks

This board tracks only work that materially affects Phase 01 rerun readiness.

## Active

| ID | Checkpoint | Task | Status | Output / Evidence |
|---|---|---|---|---|
| R1.1 | 1 | Run governance-doc normalization audit | Not started | audit artifact |

## Upcoming

| ID | Checkpoint | Task | Status | Output / Evidence |
|---|---|---|---|---|
| R2.1 | 2 | Patch governance docs based on normalization audit | Not started | normalized governance docs |
| R4.1 | 4 | Run rerun-readiness verification gate | Not started | verification artifact or gate verdict |
| R5.1 | 5 | Run fresh Phase 01 discuss pass | Not started | fresh discuss output |
| R5.2 | 5 | Produce new live `01-CONTEXT.md` | Not started | refreshed context file |
| R5.3 | 5 | Produce fresh Phase 01 plan | Not started | refreshed plan artifacts |

## Conditional

| ID | Checkpoint | Task | Trigger | Status |
|---|---|---|---|---|
| R3.1 | 3 | Patch repo-local GSD / overlay / workflow machinery | governance normalization audit proves important rule ownership belongs in machinery | Conditional |
| R3.2 | 3 | Design project-wide compact prompt and Codex/GSD integration | stable project-wide control surfaces are clear enough that the readiness-specific compact prompt should be generalized | Conditional |
| R3.4 | 3 | Draft repo-local non-phase external-reread protocol/template | Checkpoints 1-2 settle and later harness follow-through still needs a repeatable non-phase external-reread surface | Conditional |
| R4.2 | 4 | Targeted canon patch before rerun | readiness verification finds real canon gap rather than governance/process gap | Conditional |
| R4.3 | 4 | Run cross-vendor reread on rerun-readiness verification artifact | rerun-readiness verdict depends on doctrine-sensitive judgment rather than only mechanical closure | Conditional |
| R5.4 | 5 | Run cross-vendor reread on fresh Phase 01 plan before execution approval | fresh plan remains doctrine-sensitive or contested after internal review | Conditional |

## Done

| ID | Task | Evidence |
|---|---|---|
| R-.1 | Create readiness package backbone | [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md), [INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md), [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md), [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml) |
| R-.2 | Capture pre-rerun sequence and `05` carry-forward history | [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md) |
| R-.3 | Checkpoint readiness/governance baselines before corrective pass | `9d1e22b`, `2ad87fc`, `c38ad2a` |
| R-.4 | Capture model-assignment and cross-vendor audit policy baseline | [02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md) |
| R-.5 | Review focused cross-model audit integration research | [01-cross-model-audit-integration-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-cross-model-audit-integration-research/01-cross-model-audit-integration-research.md), [RESEARCH-INTAKE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/RESEARCH-INTAKE.md) |
| R0.1 | Repair stale or mispointed internal file-line citations in governance audit `01`-`06` | `dd3966c`, [01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md) |
| R0.2 | Align claim markers in governance audit `01`-`06` with actual support mode and basis | `dd3966c`, [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md) |
| R0.3 | Re-review repaired governance audit bundle before checkpointing | [REVIEWS/checkpoint-0-internal-review-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-0-internal-review-r1.md), [REVIEWS/checkpoint-0-internal-review-r2.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-0-internal-review-r2.md) |
| R0.4 | Checkpoint current governance/process wave with clean commit split | `dd3966c`, [CHECKPOINT-LEDGER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-LEDGER.md), [GATES/checkpoint-0.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-0.md) |
| R0.5 | Add temporary readiness-specific compact prompt and session continuity mitigation | `f7c49c2`, `baaf732`, `c919bd8`, [SESSION-REENTRY-CHECKLIST.md](/home/rookslog/workspace/projects/prix-guesser/.planning/SESSION-REENTRY-CHECKLIST.md), [.codex/tooling/compact-prompts/readiness.md](/home/rookslog/workspace/projects/prix-guesser/.codex/tooling/compact-prompts/readiness.md) |
| R0.6 | Store Checkpoint 0 reviews and reusable review spec under `REVIEWS/` | [REVIEWS/checkpoint-0-internal-review-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-0-internal-review-spec.md), [REVIEWS/checkpoint-0-internal-review-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-0-internal-review-r1.md), [REVIEWS/checkpoint-0-internal-review-r2.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-0-internal-review-r2.md) |
