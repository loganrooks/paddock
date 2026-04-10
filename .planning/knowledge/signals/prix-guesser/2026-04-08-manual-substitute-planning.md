---
id: sig-2026-04-08-manual-substitute-planning
type: signal
project: prix-guesser
tags: [planning, codex, anti-pattern, plan-quality]
created: 2026-04-08T18:00:00Z
updated: 2026-04-08T18:00:00Z
durability: principle
status: active
severity: critical
signal_type: struggle
signal_category: negative
polarity: negative
response_disposition: formalize
phase: 1
detection_method: manual
origin: codex-session-forensic
runtime: codex-cli
model: gpt-5.4
lifecycle_state: triaged
lifecycle_log:
  - "detected at 2026-04-08T18:00:00Z: hand-authored plan led to invalid read_first targets"
  - "triaged at 2026-04-08T22:00:00Z: formalized as blocking constraint"
confidence: high
confidence_basis: "Directly observed: manually written plan contained read_first paths to files that didn't exist, stalling execution."
evidence:
  supporting:
    - "Bad 01-02-PLAN.md listed create-target files in read_first"
    - "Executor stalled because read_first contract requires existing files"
    - "Root cause was writing plans manually when planner/checker path felt uncertain"
  counter: []
triage:
  decision: address
  rationale: "Manual plans bypass the validation that planner/checker provide, introducing subtle contract violations"
  priority: critical
  by: user
  at: 2026-04-08T22:00:00Z
remediation:
  status: complete
  approach: "AGENTS.md now explicitly prohibits hand-authoring PLAN artifacts when planner/checker execution is degraded. Either restore the real planning path or halt."
  at: 2026-04-08T22:00:00Z
related_signals:
  - sig-2026-04-08-recursive-gsd-orchestration
---

# Manual Substitute Plans Bypass Validation And Break Execution

## What happened

When the planner/checker agent path felt uncertain (due to recursive orchestration stalls), a Phase 1 plan was hand-authored and trusted as if it had been properly validated. That plan contained `read_first` entries pointing to files that didn't exist yet — create-targets that belong in tasks, not in `read_first`.

## Impact

- Executor stalled on missing `read_first` files
- Wasted execution time on a structurally invalid plan
- Created false confidence that planning was complete

## Rule

Do not hand-write replacement plan artifacts in place of a real planner/checker pass. If the agent path is degraded, debug it or stop. Create-targets belong in task definitions, never in `read_first`.
