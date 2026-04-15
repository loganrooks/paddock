# Checkpoint Ledger

This ledger records meaningful readiness checkpoint boundaries and the commits that captured them.

## Pending Checkpoints

| Checkpoint | Intended boundary | Commit status |
|---|---|---|
| 1 | governance-doc normalization audit artifact, if independently reviewable | Pending |
| 2 | governance-doc normalization patch | Pending |
| 3 | conditional harness/GSD follow-through | Conditional |
| 4 | rerun-readiness verification artifact, if produced | Pending |
| 5 | fresh Phase 01 discuss/context/plan bundle before execution approval | Pending |

## Recorded Commits

| Checkpoint | SHA | Commit message | Notes |
|---|---|---|---|
| 0 baseline | `9d1e22b` | `docs(governance): tighten claim typing and checkpoint rules` | Governance/process baseline committed before the corrective bundle pass |
| 0 baseline | `2ad87fc` | `docs(readiness): scaffold phase 01 rerun package` | Readiness control surface established |
| 0 baseline | `c38ad2a` | `docs(research): checkpoint multi-layer governance audit bundle` | Stable review baseline, but not the final corrected Checkpoint 0 closeout |
| 0 support | `33fa17b` | `docs(readiness): integrate model policy and cross-audit gates` | Readiness package updated to reflect model-policy and cross-vendor gate consequences |
| 0 support | `bfd09f1` | `docs(readiness): add research intake layer` | Added explicit research-to-package absorption surface |
| 0 support | `63bb5ce` | `docs(readiness): absorb cross-model audit findings` | Accepted cross-model integration findings as conditional follow-through, not a blocker |
| 0 support | `cffee7d` | `docs(readiness): add checkpoint review policy` | Added review matrix and checkpoint review template |
| 0 support | `bdcf4b3` | `docs(readiness): tighten autonomy and review controls` | Added machine-readable review policy, opportunity tracking, deviation taxonomy, and stronger independence rules |
| 0 support | `433bb00` | `docs(readiness): specify Claude review lanes and commands` | Made cross-vendor review concrete for this repo's current Claude lanes |
| 0 support | `f7c49c2` | `docs(workflow): add compaction continuity mitigations` | Added session continuity mitigation at the workflow layer |
| 0 support | `c919bd8` | `docs(codex): refresh readiness compact prompt` | Refreshed the temporary readiness compact prompt after later readiness-control changes |
| 0 closure input | `dd3966c` | `docs(research): repair governance audit bundle citations and markers` | Separate research-bundle repair commit. Closure evidence lives in [GATES/checkpoint-0.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-0.md) and [REVIEWS/checkpoint-0-internal-review-r2.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-0-internal-review-r2.md) |
