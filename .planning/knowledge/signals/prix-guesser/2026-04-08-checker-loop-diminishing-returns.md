---
id: sig-2026-04-08-checker-loop-diminishing-returns
type: signal
project: prix-guesser
tags: [planning, checker, codex, iteration-control]
created: 2026-04-09T00:10:00Z
updated: 2026-04-09T00:10:00Z
durability: convention
status: active
severity: notable
signal_type: struggle
signal_category: negative
polarity: negative
response_disposition: formalize
phase: 1
detection_method: manual
origin: codex-session-forensic
runtime: codex-cli
model: gpt-5.4
lifecycle_state: detected
lifecycle_log:
  - "detected at 2026-04-09T00:10:00Z: planner/checker revision loops continued past value-add point"
confidence: medium
confidence_basis: "Session history shows multiple checker re-runs on narrow contract inconsistencies that did not materially improve plans."
evidence:
  supporting:
    - "Commits c18a958 and 3684c2e are both checker-feedback revisions to the same plans"
    - "Checker got stuck on narrow contract inconsistencies (e.g., flat mediaKind vs nested clueSteps[*].media)"
    - "Session timeline shows ~2 hours of revision loops for Phase 1 planning alone"
  counter:
    - "Some checker feedback was genuinely valuable (the mediaKind shape fix)"
triage:
  decision: monitor
  rationale: "Need to distinguish valuable checker iterations from diminishing-returns loops"
  priority: medium
  by: user
  at: 2026-04-09T00:10:00Z
related_signals:
  - sig-2026-04-08-codex-reasoning-effort-mismatch
---

# Planner/Checker Revision Loops Continued Past Value-Add Point

## What happened

The planner/checker cycle for Phase 1 ran through multiple iterations, with commits showing repeated revisions. The checker flagged narrow contract inconsistencies (e.g., flat `mediaKind` vs nested `clueSteps[*].media.kind`) that produced real fixes, but the loop continued beyond the point where iterations were adding material value.

## Impact

- ~2 hours spent on Phase 1 planning revision alone
- Some later revisions were gap-fix edits that were never independently re-verified
- Unclear whether the current uncommitted plan diffs should be trusted

## Open question

How to set a circuit-breaker on checker loops — after N iterations or when issue severity drops below a threshold, stop and proceed to execution.
