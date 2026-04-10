---
id: sig-2026-04-08-premature-stall-diagnosis
type: signal
project: prix-guesser
tags: [orchestration, codex, patience, anti-pattern]
created: 2026-04-08T18:00:00Z
updated: 2026-04-08T18:00:00Z
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
lifecycle_state: triaged
lifecycle_log:
  - "detected at 2026-04-08T18:00:00Z: quiet planner runs treated as failed too quickly"
  - "triaged at 2026-04-08T22:00:00Z: formalized as blocking constraint with gauntlet protocol"
confidence: high
confidence_basis: "Directly observed: premature stall diagnosis fed the bad manual recovery path that produced invalid plans."
evidence:
  supporting:
    - "Short subagent quiet periods led to premature diagnosis and bad recovery decisions"
    - "Premature diagnosis was the trigger for manual substitute planning"
  counter: []
triage:
  decision: address
  rationale: "Silence is not failure — long-running agents need real runway before being declared stalled"
  priority: high
  by: user
  at: 2026-04-08T22:00:00Z
remediation:
  status: complete
  approach: "Gauntlet protocol: longer wait, artifact/commit check, one status probe, then classify as blocked. Documented in .continue-here.md."
  at: 2026-04-08T22:00:00Z
related_signals:
  - sig-2026-04-08-manual-substitute-planning
---

# Premature Stall Diagnosis Triggers Bad Recovery Paths

## What happened

Quiet planner/checker runs were treated as failed too quickly. The short silence was interpreted as a stall, which triggered manual substitute planning — itself another anti-pattern.

## Impact

- Fed directly into the manual substitute planning failure
- Created unnecessary recovery work that was worse than waiting

## Rule

Use a real diagnostic gauntlet before declaring an agent stalled: longer wait, check for new artifacts or commits, send one status probe, then classify as blocked. Silence is not failure.
