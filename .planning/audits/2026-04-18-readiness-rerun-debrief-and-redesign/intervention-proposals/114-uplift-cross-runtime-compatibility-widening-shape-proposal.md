Date: 2026-04-22
Status: active bounded proposal

# Uplift Cross-Runtime Compatibility Widening Shape Proposal

## Purpose

- [g:r:i] Open the next bounded cross-runtime proposal after the completed concern-family split lane.
- [g:r:i] The target is not a live compatibility-matrix claim, not `.claude` translation, and not a composition judgment.
- [g:r:i] The target is to choose how the existing uplift-side compatibility anchor should widen, if at all.

## Why This Proposal Opens First

- [e:c+i] The concern-family split lane recommends `compatibility-family widening shape` as the first bounded proposal because it is already a decision surface rather than another field-discovery surface. Source:
  - [entry-uplift-audit/outputs/12-uplift-cross-runtime-concern-family-split-opus47-max-r1.md](../entry-uplift-audit/outputs/12-uplift-cross-runtime-concern-family-split-opus47-max-r1.md)
- [d:r:i] The current compatibility anchor already has one durable home:
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
  - the `Project Uplift` section in [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- [d:r:i] The current shape choice also gates where `consumer-chain asymmetry` can later live. Opening the shape proposal first keeps that downstream family from being forced into the wrong home too early.

## Current Anchor Posture

- [e:c+i] The current compatibility anchor posture is `observed_basis_only`, with `.codex` as the observed runtime basis and broader cross-runtime compatibility still held. Source:
  - [43-project-uplift-compatibility-anchor-slice.md](43-project-uplift-compatibility-anchor-slice.md)
- [d:r:i] The current anchor therefore carries real observed `.codex` basis, but still leaves `.claude` mostly in prose and audit surfaces rather than in the durable anchor itself.

## Candidate Shapes

### 1. Annotation Posture

- [d:r:i] Keep `observed_basis_only` as the anchor posture.
- [d:r:i] Add an explicit held `.claude` runtime row plus a bounded note that the repo currently has a second observed runtime with different version / carrier posture.
- [d:r:i] This shape keeps the anchor narrow while making the cross-runtime relation more legible.

### 2. Dual-Basis Posture

- [d:r:i] Widen the anchor so both `.codex` and `.claude` sit inside one observed-basis surface.
- [d:r:i] This shape gives more immediate symmetry but risks suggesting a stronger equivalence than the current routes and consumers have earned.

### 3. Typed Multi-Runtime Carrier

- [d:r:i] Leave the current uplift-side anchor narrow and open a separate typed carrier for multi-runtime compatibility.
- [d:r:i] This shape gives the most structural separation, but it also introduces a new carrier family earlier than the current field seems to require.

## Recommended Shape

- [d:r:i] Recommend **annotation posture** as the next bounded move.

## Why Annotation Posture First

- [d:r:i] It keeps the current `.codex` observed-basis anchor honest instead of widening it faster than the present carrier field warrants.
- [d:r:i] It makes the currently live `.claude` version and posture difference durable inside the existing anchor family rather than leaving them only in packet/reread prose.
- [d:r:i] It gives the next family, `consumer-chain asymmetry`, a clearer immediate home without forcing a separate typed carrier first.
- [d:r:i] It avoids the stronger equivalence signal that a dual-basis posture could imply before route-asymmetry field mapping and later translation triage have been carried further.
- [d:r:i] It avoids opening a new multi-runtime carrier family before the current one has been widened in its smallest high-yield form.

## What This Proposal Does Not Authorize

- [d:r:i] No live edit to `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, or `.planning/STATE.md` yet.
- [d:r:i] No compatibility-matrix claim.
- [d:r:i] No `.claude` route translation.
- [d:r:i] No cross-runtime composition judgment.
- [d:r:i] No change to `$gsd-propagation-review`.

## Verification Gates

- [d:r:i] The chosen shape must stay family-by-family rather than widening into parity appetite.
- [d:r:i] The chosen shape must preserve the current observed-basis discipline around `.codex` even if `.claude` becomes more visible.
- [d:r:i] The chosen shape must make the next family opening for `consumer-chain asymmetry` cleaner rather than blurrier.
- [d:r:i] The proposal should remain narrow enough that a later implementation slice can update the existing compatibility anchor without also forcing matrix work or translation work.

## Current Consequence

- [d:r:i] The cross-runtime uplift family now has a concrete next bounded proposal instead of only a wider audit result.
- [d:r:i] If this proposal is accepted, the next move after it should be one small implementation slice on the existing compatibility anchor surfaces, followed by the bounded `consumer-chain asymmetry` proposal it unblocks.
