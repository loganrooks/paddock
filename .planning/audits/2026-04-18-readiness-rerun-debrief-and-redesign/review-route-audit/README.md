Date: 2026-04-22
Status: active bounded audit family

# Review Route Audit

## Purpose

- [g:r:i] This subtree audits and sharpens the repo-local cross-vendor review route centered on `$gsd-review`.
- [d:r:i] Its focus is not generic multi-provider parity.
- [d:r:i] Its focus is the repo-local review route as an operator surface:
  - review-run home
  - prompt and output durability
  - launch-truth and timing calibration
  - provider-shaped runner differences
  - failure-path salvage
  - planner-consumer carry into `REVIEWS.md`

## Current Lane

- [d:r:i] Lane `01` is the opening Opus widening audit over the current `gsd-review` route and the first local hardening shape.

## Expected Artifact Pattern

- [d:r:i] packet
- [d:r:i] spec
- [d:r:i] prompt
- [d:r:i] launch-truth
- [d:r:i] output
- [d:r:i] inheritance

## Current Consequence

- [d:r:i] The next move inside this family is to complete lane `01`, then decide whether the first live slice should:
  - harden the existing `gsd-review` route directly
  - add a helper-backed run-home/logging layer beside it
  - or split those into a narrower first implementation plus later follow-through
