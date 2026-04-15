---
id: sig-2026-04-15-dirty-task-transitions-mixed-worktree
type: signal
project: prix-guesser
tags: [orchestration, codex, task-transition, worktree-hygiene, git]
created: 2026-04-15T04:39:01Z
updated: 2026-04-15T04:39:01Z
durability: principle
status: active
severity: critical
signal_type: struggle
signal_category: negative
polarity: negative
response_disposition: formalize
phase: 1
detection_method: manual
origin: user-correction
runtime: codex-cli
model: gpt-5.4
lifecycle_state: triaged
lifecycle_log:
  - "detected at 2026-04-15T04:39:01Z: user flagged repeated task transitions across an unresolved mixed worktree"
  - "triaged at 2026-04-15T04:39:01Z: formalized as a distinct dirty-transition and concern-bucket hygiene failure"
confidence: high
confidence_basis: "Directly observed in-session: canon, AGENTS, audit, knowledge-base, and orchestration-framework changes coexisted in one unresolved working tree while forward motion continued."
evidence:
  supporting:
    - "git status showed unresolved changes spanning canon docs, AGENTS policy, audit corpus, knowledge-base files, and new orchestration research at the same time"
    - "The user had to stop forward motion and require an explicit cleanup/checkpoint plan before more substantial work continued"
    - "05-worktree-stabilization-note and 05-git-cleanup-checkpoint-plan were needed to recover explicit concern buckets and bounded change sets"
  counter: []
triage:
  decision: address
  rationale: "Mixed-bucket worktrees hide review boundaries, increase cross-task contamination risk, and make later acceptance or rollback much less reliable"
  priority: critical
  by: user
  at: 2026-04-15T04:39:01Z
remediation:
  status: in_progress
  approach: "Treat git status as a task-transition gate, classify live edits into concern buckets, and require accept/revise/park decisions before a new substantive task begins"
related_signals:
  - sig-2026-04-08-recursive-gsd-orchestration
  - sig-2026-04-15-underdelegated-exploration-orchestrator-role-drift
---

# Dirty Task Transitions And Mixed Worktree Hygiene

## What Happened

The session crossed from one substantive task into another while the working tree still held unresolved edits from multiple logical buckets. Canon uplift, AGENTS changes, audit-corpus additions, knowledge-base updates, and orchestration-framework research all accumulated together before the earlier work had been explicitly accepted, revised, or parked.

## Context

The immediate trigger was not just "the tree is dirty." The real failure was that the dirtiness spanned different review states and different kinds of work. A canon patch, governance changes, historical audit corpus, and new process research all ended up sharing one unresolved working tree. That forced a later recovery pass to reconstruct concern buckets after the fact instead of using the working tree itself as a clean checkpoint boundary.

## Potential Cause

The orchestrator was not treating `git status` as a task-transition control surface. Without a rule that a mixed concern-bucket tree blocks new substantive work, it became easy to keep moving while the repo no longer reflected one reviewable change set.
