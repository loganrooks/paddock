---
id: sig-2026-04-08-recursive-gsd-orchestration
type: signal
project: prix-guesser
tags: [orchestration, codex, delegation, anti-pattern]
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
  - "detected at 2026-04-08T18:00:00Z: discovered through failed Phase 1 planning"
  - "triaged at 2026-04-08T22:00:00Z: formalized in AGENTS.md constraints"
confidence: high
confidence_basis: "Directly observed: generic agent spawned gsd-plan-phase which itself tried to spawn researcher/planner/checker, creating broken-telephone delegation."
evidence:
  supporting:
    - "Codex session history shows nested skill invocation causing opaque stalls"
    - "Recovery required full repo reset and re-planning from scratch"
    - "Documented in .continue-here.md as blocking constraint"
  counter: []
triage:
  decision: address
  rationale: "Recursive orchestration made stalls impossible to debug and wasted multiple sessions"
  priority: critical
  by: user
  at: 2026-04-08T22:00:00Z
remediation:
  status: complete
  approach: "AGENTS.md now requires top-level orchestrator to spawn only concrete role agents directly, never generic agents that invoke GSD skills"
  at: 2026-04-08T22:00:00Z
---

# Recursive GSD Orchestration Causes Opaque Stalls

## What happened

A generic spawned agent was told to run `gsd-plan-phase`, which itself was designed to spawn `gsd-phase-researcher`, `gsd-planner`, and `gsd-plan-checker`. This created a broken-telephone delegation chain where stalls were impossible to diagnose from the top level.

## Impact

- Multiple sessions wasted on recovery
- Required full repo reset to clean pre-plan state
- Led to premature manual plan authoring (itself another anti-pattern)

## Rule

Keep orchestration at the top level. The top-level orchestrator may run workflow logic, but it must spawn only the concrete role agents directly — never a generic agent that invokes a GSD skill.
