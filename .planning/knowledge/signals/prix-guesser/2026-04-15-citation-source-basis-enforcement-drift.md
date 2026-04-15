---
id: sig-2026-04-15-citation-source-basis-enforcement-drift
type: signal
project: prix-guesser
tags: [audit-quality, citation-discipline, source-basis, governance-audit]
created: 2026-04-15T07:15:11Z
updated: 2026-04-15T07:15:11Z
durability: principle
status: active
severity: notable
signal_type: deviation
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

# Citation Source-Basis Enforcement Drift

## What Happened

During the newer `2026-04-15-multilayer-harness-governance-audit` bundle, the stricter citation/source-basis standard established during the `05-gap-closure` audit was no longer being surfaced in the outputs. The newer audit artifacts and lane outputs were using motivating-ground references and ordinary internal citations, but they were not exposing whether a cited support was:

- internal only
- external-direct
- or external-traceable

That means the upgraded epistemic-quality standard was not actually being enforced across the newer audit bundle.

## Context

During the `05-gap-closure` audit, the repo explicitly upgraded its claim/citation framing to distinguish epistemically relevant grounding modes, including the difference between repo-local support and outside-source support that is direct or only traceable through another artifact. That distinction mattered because earlier audit rounds had been too permissive about treating internal docs as if they provided the same grounding as fresh external research.

In the broader multi-layer harness/governance audit bundle, that stronger standard was no longer visibly present in the specs or the returned lane outputs. The user caught this regression and explicitly pointed out that the bundle was no longer exposing source basis in the way the `05` audit had taught the repo to do.

## Potential Cause

The repo improved the doctrine around source-basis and epistemic quality during the `05` audit, but that improvement was not propagated into enough durable enforcement surfaces:

- newer audit specs did not require source-basis markers explicitly
- validation focused on motivating grounds and lane structure, not source-basis discipline
- the newer bundle leaned on repo-grounded governance analysis, which made it easy to slide back into ordinary internal citation habits

So the standard existed as learned doctrine, but not yet as a sufficiently enforced cross-bundle requirement.
