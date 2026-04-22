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
- [d:r:i] Lane `02` is now the active challenge on that boundary:
  - [packets/02-harness-modifier-overlay-carrier-rehome-reread-packet.md](packets/02-harness-modifier-overlay-carrier-rehome-reread-packet.md)
  - [specs/02-harness-modifier-overlay-carrier-rehome-reread-spec.md](specs/02-harness-modifier-overlay-carrier-rehome-reread-spec.md)
  - [prompts/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1-launch-prompt.md](prompts/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1-launch-prompt.md)
  - [launch-truth/02-harness-modifier-overlay-carrier-rehome-reread-launch-truth.md](launch-truth/02-harness-modifier-overlay-carrier-rehome-reread-launch-truth.md)
  - [outputs/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1.md](outputs/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1.md)
  - [dispositions/02-harness-modifier-overlay-carrier-rehome-reread-inheritance.md](dispositions/02-harness-modifier-overlay-carrier-rehome-reread-inheritance.md)
- [d:r:i] Lane `02` is now completed and the narrowing it called for is now landed:
  - [../intervention-proposals/144-harness-modifier-overlay-roster-and-embedded-host-path-scan-proposal.md](../intervention-proposals/144-harness-modifier-overlay-roster-and-embedded-host-path-scan-proposal.md)
  - [harness_modifier/overlay/ROSTER.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/ROSTER.md)
  - [artifacts/03-overlay-embedded-host-path-scan.md](artifacts/03-overlay-embedded-host-path-scan.md)
  - [../intervention-proposals/146-harness-modifier-overlay-roster-and-embedded-host-path-scan-implementation.md](../intervention-proposals/146-harness-modifier-overlay-roster-and-embedded-host-path-scan-implementation.md)
- [d:r:i] That proposal is now landed too through:
  - [../intervention-proposals/147-harness-modifier-first-overlay-filesystem-rehome-proposal.md](../intervention-proposals/147-harness-modifier-first-overlay-filesystem-rehome-proposal.md)
  - [../intervention-proposals/148-harness-modifier-first-overlay-filesystem-rehome-implementation.md](../intervention-proposals/148-harness-modifier-first-overlay-filesystem-rehome-implementation.md)
  - [../propagation-audit/55-harness-modifier-first-overlay-filesystem-rehome-change-triggered-refresh.md](../propagation-audit/55-harness-modifier-first-overlay-filesystem-rehome-change-triggered-refresh.md)
- [d:r:i] The first specialist overlay tranche now uses:
  - modifier-owned source files under `harness_modifier/overlay/`
  - stable install targets still declared at `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
  - explicit source-path indirection instead of duplicated overlay ownership
- [d:r:i] The next extraction move is now active as lane `03`:
  - [packets/03-harness-modifier-first-overlay-filesystem-rehome-reread-packet.md](packets/03-harness-modifier-first-overlay-filesystem-rehome-reread-packet.md)
  - [specs/03-harness-modifier-first-overlay-filesystem-rehome-reread-spec.md](specs/03-harness-modifier-first-overlay-filesystem-rehome-reread-spec.md)
  - [prompts/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1-launch-prompt.md](prompts/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1-launch-prompt.md)
  - [launch-truth/03-harness-modifier-first-overlay-filesystem-rehome-reread-launch-truth.md](launch-truth/03-harness-modifier-first-overlay-filesystem-rehome-reread-launch-truth.md)
  - [outputs/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1.md](outputs/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1.md)
- [d:r:i] Lane `03` keeps the question bounded to the landed specialist source split before any second overlay tranche is chosen.
- [d:r:i] Lane `03` is now completed and inherited:
  - [outputs/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1.md](outputs/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1.md)
  - [dispositions/03-harness-modifier-first-overlay-filesystem-rehome-reread-inheritance.md](dispositions/03-harness-modifier-first-overlay-filesystem-rehome-reread-inheritance.md)
- [d:r:i] The next extraction move was then narrowed again:
  - [../intervention-proposals/149-harness-modifier-first-overlay-residue-classification-pass-proposal.md](../intervention-proposals/149-harness-modifier-first-overlay-residue-classification-pass-proposal.md)
- [d:r:i] `149` kept the next move on the first slice's residues instead of widening directly into a second filesystem tranche.
- [d:r:i] That residue-classification pass is now landed too:
  - [../intervention-proposals/150-harness-modifier-first-overlay-residue-classification-pass-implementation.md](../intervention-proposals/150-harness-modifier-first-overlay-residue-classification-pass-implementation.md)
  - [../propagation-audit/56-harness-modifier-first-overlay-residue-classification-change-triggered-refresh.md](../propagation-audit/56-harness-modifier-first-overlay-residue-classification-change-triggered-refresh.md)
- [d:r:i] The carried result is now explicit:
  - source-side token abstraction is now settled for the moved skill adapters
  - helper-payload promotion, default-source-root migration, and overwrite-family source indirection remain later bounded questions
- [d:r:i] Compact-prompt split, overwrite-family migration, and standalone repo design remain later.

## Expected Artifact Pattern

- [d:r:i] packet
- [d:r:i] spec
- [d:r:i] prompt
- [d:r:i] launch-truth
- [d:r:i] output
- [d:r:i] inheritance
