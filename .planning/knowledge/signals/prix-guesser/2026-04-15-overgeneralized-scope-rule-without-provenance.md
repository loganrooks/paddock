---
id: sig-2026-04-15-overgeneralized-scope-rule-without-provenance
type: signal
project: prix-guesser
tags: [orchestration, codex, scope-control, provenance, checkpoint-5]
created: 2026-04-15T23:46:29Z
updated: 2026-04-15T23:46:29Z
durability: principle
status: active
severity: notable
signal_type: struggle
phase: 1
plan: checkpoint-5
polarity: negative
source: manual
occurrence_count: 2
related_signals:
  - sig-2026-04-15-underdelegated-exploration-orchestrator-role-drift
  - sig-2026-04-15-dirty-task-transitions-mixed-worktree
  - sig-2026-04-08-recursive-gsd-orchestration
  - sig-2026-04-08-premature-stall-diagnosis
runtime: codex-cli
model: gpt-5.4
gsd_version: 1.34.2
---

# Overgeneralized Scope Rule Without Provenance

## What Happened

During the readiness-package follow-through after the multi-layer harness audit, I treated a narrow Checkpoint 3 scoping heuristic as if it were a broader standing command against widening the active checkpoint.

Concretely, I leaned on the idea that the harness should not be audited by merely enumerating visible surfaces or reducing GSD to a flat skill inventory. That principle was real in its original context, but I overextended it into a de facto anti-widening rule for Checkpoint 5.

That caused me to defend an overly narrow Checkpoint 5 scope focused on:

- runtime-authoritative `.toml` worker prompts
- a limited review-surface patch
- launch-truth capture

while underweighting workflow-level defects that Checkpoint 4 had already surfaced strongly enough to justify modifying `discuss-phase.md`, `research-phase.md`, `plan-phase.md`, and `execute-phase.md`.

When challenged, I initially could not justify the narrowing doctrine from explicit cited repo sources. The user had to push for the provenance chain and point out that a command like "do not widen audits by enumerating every visible surface" can collapse into laziness if it is detached from its original scope and purpose.

## Context

The legitimate source of the narrower rule was the Checkpoint 3 mapping/scoping phase:

- `checkpoint-3-gsd-surface-map-spec.md` required a broad preliminary scan across workflows, skills, agents, references, templates, and local patches, then asked what the real load-bearing units were instead of assuming the harness was just a skill list.
- `checkpoint-3-gsd-surface-map.md` concluded that skills were usually wrappers/adapters into workflows and that a flat skill-count audit would be a misleading primary unit.
- `checkpoint-3-workflow-harness-scope-audit.md` carried that forward as a scoped heuristic for audit-envelope design: do not confuse easy enumeration with true load-bearing surfaces, and if a deeper skill/adapter audit becomes necessary, split and justify it explicitly.

That was a valid Checkpoint 3 scoping rule. It was not a general doctrine that workflow widening should be resisted after later evidence surfaced stronger workflow-level defects.

By the time Checkpoint 5 was active, Checkpoint 4 had already produced workflow-file findings showing that:

- research quality was under-gated
- `plan-phase.md` still allowed cheap `Proceed anyway` exits
- auto mode thinned excellence pressure
- `execute-phase.md` still let debt-carrying completion read too much like clean completion

So the later evidence base had already changed the warranted scope. The failure was not that the repo lacked a source chain; it was that I used the older scoped rule beyond the bounds that source chain justified, and I did so without citing it when challenged.

## Potential Cause

The likely cause was a compound reasoning failure:

- I over-learned a correct anti-false-completeness lesson from Checkpoint 3.
- I converted "use the true load-bearing unit, not the easiest-to-enumerate unit" into "resist widening unless forced."
- I then gave too much weight to runtime-authoritative surfaces and too little weight to workflow-level follow-through already established by Checkpoint 4.
- I failed to keep the provenance of the scoping rule explicit, so it hardened into an unsupported command instead of remaining a checkpoint-specific heuristic with clear escape conditions.

This is a harness/governance reasoning failure, not just a tone or communication failure. It leaves quality gains on the table by making later follow-through too timid even when the audit record already supports a wider, better-targeted patch set.
