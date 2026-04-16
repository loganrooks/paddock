---
id: sig-2026-04-16-cross-vendor-duplicate-dispatch-and-overconfident-causal-attribution
type: signal
project: prix-guesser
tags: [cross-vendor-review, claude, duplicate-dispatch, idempotency, causal-attribution, checkpoint-5]
created: 2026-04-16T04:23:43Z
updated: 2026-04-16T04:23:43Z
durability: principle
status: active
severity: critical
signal_type: struggle
phase: 1
plan: checkpoint-5
polarity: negative
source: manual
occurrence_count: 5
related_signals:
  - sig-2026-04-15-cross-vendor-review-artifact-authority-failure
  - sig-2026-04-15-overgeneralized-scope-rule-without-provenance
  - sig-2026-04-08-premature-stall-diagnosis
runtime: codex-cli
model: gpt-5.4
gsd_version: 1.36.0
---

# Cross-Vendor Duplicate Dispatch And Overconfident Causal Attribution

## What Happened

During Readiness Package cross-vendor review work, multiple Claude review prompts were dispatched twice.

The failure had two layers:

1. real duplicate or repeated Claude dispatch happened on expensive cross-vendor lanes
2. after being challenged, I gave an overconfident causal explanation that went beyond what the local evidence actually justified

The strongest proven case is the later `R5.16a` / `R5.16b` Track B / Track C propagation review pair:

- I launched Claude once using full prompt text as a CLI argument
- the runs did not fail cleanly at dispatch; they progressed and later ended with `Prompt is too long`
- I then relaunched through a different transport path
- that created a second dispatch of effectively the same prompt

That behavior doubled Claude-side usage on already expensive lanes.

But when I was challenged on the broader pattern, I overgeneralized from the latest pair and claimed that all five observed duplicate pairs were the same class of failure. The available evidence did not warrant that claim.

## Epistemic Status

### What Is Proven

- The latest `R5.16a` / `R5.16b` Claude lanes were duplicated by my own workflow.
- The duplicate-dispatch pattern is real and economically meaningful.
- Local Codex sqlite evidence does not currently show a hidden Codex-side mirrored "cross-vendor review" dispatch path that would explain the Claude duplicates automatically.

### What Is Not Proven

- The earlier Checkpoint 3 / Checkpoint 4 duplicate-looking pairs are not fully explained by the latest transport/retry story.
- Some earlier pairs appear to be genuine rereads or model-distinct outputs rather than the same accidental mechanism.
- I therefore did not have enough evidence to collapse all five cases into one causal story.

## Context

The user brought in external Claude-side evidence showing five paired cross-vendor prompt dispatches, with:

- three earlier pairs that were byte-identical or effectively identical
- two later pairs with a one-character difference consistent with trailing newline handling

The user also brought a stronger Claude-side interpretation:

- some earlier pairs may reflect real reread or distinct-slot behavior
- the later Track B / Track C pair is a real bug pattern around context-overflow/re-dispatch

That evidence undercut my earlier attempt to explain the entire history with one simplified mechanism.

## Why This Matters

This is not only a token-cost problem.

It is also a trust and auditability problem:

- cross-vendor review is supposed to provide scarce independent pressure
- duplicate dispatch without strict idempotency controls wastes that scarce budget
- overconfident explanation after the fact makes later process diagnosis less reliable

In other words, the failure is both operational and epistemic.

## Potential Cause

The likely combined causes were:

- no hard single-dispatch guard for Claude review prompts
- no explicit launch ledger keyed by prompt hash, output path, and session identity
- too-loose rerun threshold for scarce cross-vendor lanes
- weak separation between:
  - intentional reread
  - transport failure
  - context-overflow failure
  - dissatisfied interpretation of a completed run
- overconfident causal reasoning under pressure instead of proven-vs-unproven separation

## Corrective Principle

Future cross-vendor review workflow should enforce:

1. one persisted prompt file per intended run
2. one explicit output slot per intended run
3. one launch ledger entry before dispatch
4. no redispatch of the same prompt/output slot without an explicit failed-state record
5. strict separation between:
   - intentional reread
   - retry after confirmed failure
   - new model/vendor slot
6. proven-vs-unproven causal accounting when explaining failures

## Durable Lesson

When a cross-vendor dispatch problem occurs, I should not jump from:

- "some evidence suggests a mechanism"

to:

- "the whole pattern is explained"

The correct discipline is:

1. state what is proven
2. state what remains ambiguous
3. avoid unifying distinct cases under one story unless the evidence actually supports it

For expensive external lanes, idempotency and epistemic restraint are both load-bearing.
