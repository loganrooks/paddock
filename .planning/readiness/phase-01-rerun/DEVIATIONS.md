# Readiness Plan Deviations

This file records meaningful sequence changes instead of letting them disappear into silent plan edits.

## Deviation Types

Use one or more of:

- `operational-restructure`
  Control surfaces changed, but the sequence did not.
- `sequence-reorder`
  Checkpoint order or dependency order changed.
- `upstream-reactivation`
  A later finding reopened an earlier checkpoint or prior doctrine/harness layer.
- `new-blocker`
  A newly recognized blocker changed what must happen next.
- `strategic-opportunity`
  A non-blocking but high-upside finding changed what should be tracked for best later outcomes.
- `evidence-overturn`
  New evidence materially changed what the package believed.
- `user-directed-change`
  The user explicitly changed the route or priority.

## Logging Format

For each deviation, record:

- type:
- date:
- trigger:
- effect on sequence:
- package surfaces changed:
- whether user consultation was required:

## 2026-04-15

- type: `operational-restructure`
- date: 2026-04-15
- trigger: top-level readiness plan was too fragile to survive context compaction as a single file
- effect on sequence: none
- package surfaces changed:
  - `PLAN.md`
  - `STATUS.md`
  - `STATE.yaml`
  - gate files
  - task tracking
  - deferrals
  - checkpoint logging
- whether user consultation was required: no
