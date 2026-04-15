---
id: sig-2026-04-15-cross-vendor-review-artifact-authority-failure
type: signal
project: prix-guesser
tags: [cross-vendor-review, claude, artifact-authority, rerun-discipline, patience]
created: 2026-04-15T21:59:11Z
updated: 2026-04-15T21:59:11Z
durability: principle
status: active
severity: notable
signal_type: struggle
phase: 1
plan: null
polarity: negative
source: manual
occurrence_count: 1
related_signals: []
runtime: codex-cli
model: gpt-5.4
gsd_version: 1.19.4
---

# Cross-Vendor Review Artifact-Authority Failure

## What Happened

During the Checkpoint 3 cross-vendor Claude review flow, I treated the run as unsettled even though a usable review artifact already existed on disk.

Instead of following an artifact-first review workflow, I let process ambiguity and prior zero-byte-output experience dominate my judgment. That pushed me toward rerunning an expensive Claude review lane before exhausting the cheap checks that should have come first.

The user had to stop me and point out that:

- the output artifact was already there
- I should have waited properly
- I should have read the artifact before considering any rerun
- unnecessary Claude reruns are especially costly because Claude usage is scarcer here than Codex usage

## Context

This failure happened inside the Readiness Package during Checkpoint 3 review closure work, after the workflow / harness scope audit had already been authored and both an internal review and a cross-vendor review lane had been set up.

The important procedural failure was not merely impatience. It was a bad priority rule:

- I privileged process-state ambiguity over artifact existence

For a scarce cross-vendor lane, that is the wrong order of operations.

The correct order should have been:

1. check whether the expected review artifact exists
2. read the artifact if it exists
3. only if there is no usable artifact, inspect process state and stderr
4. only after confirmed absence or confirmed failure, consider rerunning

Because I inverted that order, I wasted user attention, created confusion around whether the run had really failed, and risked unnecessary Claude token spend.

## Potential Cause

The current workflow discipline is still too weak on one specific point:

- external-review completion should be artifact-authoritative, not process-authoritative

I let three bad heuristics combine:

- earlier empty-output experience with Claude made me overreact to ambiguity
- process inspection felt more immediately legible than simply reading the artifact path
- I used a rerun threshold that was too loose for a scarce cross-vendor lane

The durable lesson is:

- for cross-vendor review workflows, artifact presence must outrank process ambiguity before any rerun is considered
- expensive reruns should require stronger evidence than local subagent recovery does
- patience windows and cheap probes must be exhausted before rerunning Claude
