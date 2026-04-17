---
id: sig-2026-04-16-explicit-opus-1m-needed-for-large-claude-reread
type: signal
project: prix-guesser
tags: [cross-vendor-review, claude, opus-1m, context, reread, checkpoint-5]
created: 2026-04-16T14:52:22Z
updated: 2026-04-16T14:52:22Z
durability: principle
status: active
severity: notable
signal_type: lesson
phase: 1
plan: checkpoint-5
polarity: mixed
source: manual
occurrence_count: 1
related_signals:
  - sig-2026-04-16-cross-vendor-duplicate-dispatch-and-overconfident-causal-attribution
  - sig-2026-04-15-cross-vendor-review-artifact-authority-failure
runtime: codex-cli
model: gpt-5.4
gsd_version: 1.36.0
---

# Explicit Opus 1M Needed For Large Claude Reread

## What Happened

During the `R5.17e` cross-vendor reread lane, the standard Opus launch wrote a usable artifact but still ended the session with `Prompt is too long`.

The same lane was then rerun as an explicit `claude-opus-4-6[1m]` launch, using a separate prompt file and separate output slot. That explicit `1m` run completed cleanly and wrote:

- [checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md)

while the earlier non-`[1m]` run ended with:

- [checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-r1.stdout.log](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-r1.stdout.log)

## What Is Proven

- The non-`[1m]` `R5.17e` Opus run wrote an artifact and still ended with `Prompt is too long`.
- The explicit `claude-opus-4-6[1m]` rerun of the same lane shape completed and wrote its artifact cleanly.
- For this readiness package, explicit `1m` selection is therefore an effective mitigation for large Claude adjudication/reread lanes.

## What Is Not Proven

- This does not prove that every Max-plan Opus lane silently runs below `1m` unless `[1m]` is named.
- This does not prove that every future `Prompt is too long` failure is solved only by explicit `1m`.
- It is an observed lane-level operational lesson from this package, not yet a universal harness law.

## Why This Matters

The package already had enough evidence that large Claude reread/adjudication lanes were sensitive to accumulated context, but the `R5.17e` pair established a stronger operational distinction:

- relying on implicit Opus selection was not good enough for this lane
- explicitly requesting `claude-opus-4-6[1m]` changed the outcome

That means future large cross-vendor doctrine / adjudication / reread lanes should not rely on ambient assumptions about context size when Max access is available.

## Corrective Principle

For large Claude cross-vendor adjudication or reread lanes on Max:

1. prefer explicit `claude-opus-4-6[1m]`
2. record that `1m` was used
3. preserve separate artifacts for non-`[1m]` and `[1m]` runs when comparing outcomes
4. state this as an observed mitigation, not as a universal law unless later evidence warrants it
