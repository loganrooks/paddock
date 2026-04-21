Date: 2026-04-21
Status: active opening batch

# Propagation Audit

## Purpose

- [g:r:i] This subtree exists to make contract propagation explicit across the GSD network rather than leaving it as an ambient expectation.
- [g:r:i] The target is broader than markdown-reference rewrites, broader than runtime/install coherence alone, and broader than one uplift family. The target is how contract changes move across workflows, skills, scripts, registries, wrappers, manifests, durable outputs, and governing-doc carriers.

## Family Role

- [d:r:i] Use this family when the question is not only `what changed here?` but `what else should now be in tune with it?`
- [d:r:i] The opening basis for this family is:
  - [intervention-proposals/41-contract-propagation-and-dependency-carry-audit-seed.md](../intervention-proposals/41-contract-propagation-and-dependency-carry-audit-seed.md)
  - [intervention-proposals/42-project-uplift-signal-layer-harden-slice.md](../intervention-proposals/42-project-uplift-signal-layer-harden-slice.md)
  - the older Checkpoint-3 workflow/artifact-contract lineage
  - the companion harness docs layer

## Opening Sequence

1. [01-contract-propagation-and-dependency-carry-opening-note.md](01-contract-propagation-and-dependency-carry-opening-note.md)
2. local producer / consumer and impact map
3. local carrier-placement or docs-surface follow-through if the map shows a weak route
4. bounded external challenge lane only after the local map and impact surface are explicit

## Quality Gates

- [d:r:i] Before any external lane opens in this subtree:
  - local producer / consumer and impact routing must be written down first
  - the read set must be explicit and bounded
  - packet/spec/prompt wording must clear the threshold-language scanner
  - the launch basis commit must be frozen and recorded
- [d:r:i] Before a local disposition is treated as carrying force:
  - touched vs intentionally-held neighbor surfaces must be named
  - governing spine surfaces must be updated
  - the batch must pass `audit_refmap.py verify` and `git diff --check`

## Review Gates

- [d:r:i] Do not accept a propagation judgment that only says local edits look coherent.
- [d:r:i] A stronger review in this family should ask:
  - which surfaces are direct producers
  - which are direct consumers
  - which are narrative mirrors only
  - which neighboring carriers should have moved but did not
  - which held neighbors are deliberate and well-routed rather than accidental omissions

## Current Consequence

- [d:r:i] This family is now open as a governed subtree rather than only as a seed note.
- [d:r:i] The next concrete object should be the local producer / consumer and impact map for the current uplift example plus the adjacent harness surfaces it touches.
