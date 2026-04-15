# Readiness Plan Deviations

This file records meaningful sequence changes instead of letting them disappear into silent plan edits.

## 2026-04-15

- Extracted the original top-level readiness plan into a package under [.planning/readiness/phase-01-rerun](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun) so readiness state can survive context compaction.
- The sequence itself did not change.
- The main change was operational:
  - stable sequence moved into `PLAN.md`
  - live state moved into `STATUS.md` and `STATE.yaml`
  - gate evidence, task tracking, deferrals, and checkpoint logging now have dedicated files
