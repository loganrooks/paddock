Date: 2026-04-22
Status: active opening audit family

# Extraction Audit

## Purpose

- [g:r:i] This subtree exists to audit whether the repo-local harness modifier should become its own standalone project and, if so, what that project would need to own cleanly.
- [d:r:i] Its focus is:
  - host-project versus harness carrier separation
  - installer/materialization ownership
  - `.codex` / `.claude` compatibility declaration shape
  - distribution and migration shape for later standalone install

## Opening Lane

- [d:r:i] Lane `01` will challenge the first local extraction field map rather than jumping straight to repo split or npm packaging.
- [d:r:i] Lane `01` current tuple:
  - [packets/01-harness-extraction-field-map-audit-packet.md](packets/01-harness-extraction-field-map-audit-packet.md)
  - [specs/01-harness-extraction-field-map-audit-spec.md](specs/01-harness-extraction-field-map-audit-spec.md)
  - [prompts/01-harness-extraction-field-map-audit-opus47-max-r1-launch-prompt.md](prompts/01-harness-extraction-field-map-audit-opus47-max-r1-launch-prompt.md)
  - [launch-truth/01-harness-extraction-field-map-audit-launch-truth.md](launch-truth/01-harness-extraction-field-map-audit-launch-truth.md)
  - [outputs/01-harness-extraction-field-map-audit-opus47-max-r1.md](outputs/01-harness-extraction-field-map-audit-opus47-max-r1.md)
  - [dispositions/01-harness-extraction-field-map-audit-inheritance.md](dispositions/01-harness-extraction-field-map-audit-inheritance.md)

## Current Next Step

- [d:r:i] The first two bounded extraction follow-through slices are now landed:
  - [intervention-proposals/139-harness-modifier-in-place-rehome-step-1-implementation.md](../intervention-proposals/139-harness-modifier-in-place-rehome-step-1-implementation.md)
  - [../propagation-audit/51-harness-modifier-in-place-rehome-step-1-change-triggered-refresh.md](../propagation-audit/51-harness-modifier-in-place-rehome-step-1-change-triggered-refresh.md)
  - [intervention-proposals/141-harness-modifier-compatibility-declaration-carrier-implementation.md](../intervention-proposals/141-harness-modifier-compatibility-declaration-carrier-implementation.md)
  - [../propagation-audit/52-harness-modifier-compatibility-declaration-carrier-change-triggered-refresh.md](../propagation-audit/52-harness-modifier-compatibility-declaration-carrier-change-triggered-refresh.md)
- [d:r:i] The next adjacent extraction question is no longer whether the compatibility carrier should exist. It is which later step should inherit after the helper rehome plus portable declaration:
  - [intervention-proposals/142-harness-modifier-overlay-carrier-rehome-next-proposal.md](../intervention-proposals/142-harness-modifier-overlay-carrier-rehome-next-proposal.md)
  - standalone repo boundary design
  - second-host exercise

## Expected Artifact Pattern

- [d:r:i] packet
- [d:r:i] spec
- [d:r:i] prompt
- [d:r:i] launch-truth
- [d:r:i] output
- [d:r:i] inheritance
