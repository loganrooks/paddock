Date: 2026-04-22
Status: active bounded proposal

# Milestone-Boundary Uplift Shared-Reference First Slice Proposal

## Purpose

- [g:r:i] Open the next bounded `119` route after the landed transition/state continuity slice in `121`.
- [g:r:i] The target is not another direct per-workflow patch by itself.
- [g:r:i] The target is to carry held-runtime awareness through milestone open and milestone close by attaching both routes to one shared read-only reference instead of widening either route into write-side posture.

## Why This Proposal Opens Now

- [e:r:i] `119` already classifies the milestone-boundary pair as:
  - `attach through a shared reference`
  - surfacing direction: `read-only`
- [e:r:i] `121` now gives the family a top-level `Project Uplift` digest in `STATE.md`, helper-side fill-in-place behavior, and explicit preserve-versus-refresh handling at phase close.
- [e:r:i] `60` already gives milestone open and milestone close a stronger future-carry bridge through `LONG-ARC.md` and `Future Carry Forward`.
- [d:r:i] That means the next missing lift is narrower:
  - do not rediscover uplift posture at milestone boundaries from ambient memory
  - do not widen milestone boundaries into write-side compatibility dispatch
  - instead, attach the pair to one shared reference that tells them what to read, what to surface, and what to keep held

## Current Boundary

- [d:r:i] The relevant milestone-boundary carriers already exist:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md)
- [d:r:i] The relevant uplift continuity carriers now already exist too:
  - [tooling/portable-gsd/overlay/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/state.md)
  - [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
- [d:r:i] What is still missing is the explicit boundary-reader that tells milestone open and milestone close:
  - the `Project Uplift` digest is the first compact read
  - `UPLIFT-REPORT.md` is the next narrative read when the boundary needs more context
  - `UPLIFT-MANIFEST.json` is the typed detail surface when the route hits real basis or annotation ambiguity
  - none of that widens the milestone boundary into matrix claims, parity claims, or inline write-side dispatch

## Proposed First Slice

- [d:r:i] Add one shared reference under the repo-local GSD references layer for milestone-boundary uplift continuity.
- [d:r:i] Teach both `new-milestone.md` and `complete-milestone.md` to read that shared reference as part of their boundary packet rather than inventing separate uplift prose in each workflow.
- [d:r:i] Keep the shared reference read-only in character:
  - milestone open should surface uplift posture only when it materially affects milestone framing, carry-forward pressure, or route selection
  - milestone close should keep uplift posture visible when it materially affects what stays explicit after close
  - neither route should become the place that runs `$gsd-uplift-project --write` by default

## Shared-Reference Shape

- [d:r:i] The shared reference should define:
  - primary compact read:
    - `STATE.md` top-level `Project Uplift`
  - supporting narrative read:
    - `.planning/UPLIFT-REPORT.md`
  - deeper typed read:
    - `.planning/UPLIFT-MANIFEST.json`
- [d:r:i] The shared reference should also keep the interpretation frame explicit:
  - `compatibility_posture: observed_basis_only` remains the top-level posture
  - held runtime annotation is visible but still distinct from dual-basis relabel
  - milestone boundaries may surface the posture
  - milestone boundaries do not convert that posture into parity, translation, or version-window claims

## Workflow Follow-Through Intended By This Proposal

- [d:r:i] `new-milestone.md`
  - read the shared reference in the milestone-opening packet
  - keep uplift posture visible when milestone framing or route choice actually depends on it
  - keep the boundary read-only rather than turning milestone open into an uplift-write checkpoint
- [d:r:i] `complete-milestone.md`
  - read the shared reference beside the existing future-carry and long-arc review
  - keep uplift posture visible when deciding what remains explicit after close
  - keep the boundary read-only rather than turning milestone close into a compatibility-dispatch route

## Why This Route Before `health.md`

- [d:r:i] This route intensifies two lifecycle boundaries at once instead of one repair-facing carrier.
- [d:r:i] This route composes directly with already-landed milestone-boundary lifecycle carry from `60` and transition/state continuity from `121`.
- [d:r:i] `health.md` remains a real next route, but it is narrower:
  - structural-health and later posture separation already travel there
  - the milestone-boundary pair broadens carry across entry and closure together

## What This Proposal Does Not Authorize

- [d:r:i] No write-recommending milestone-boundary dispatcher.
- [d:r:i] No compatibility matrix or version-window claims.
- [d:r:i] No `.claude` parity or route-translation claim.
- [d:r:i] No structural-row promotion inside milestone workflow output.
- [d:r:i] No widening of `health.md` through this slice.
- [d:r:i] No cross-repo extraction or npm/`npx` work through this family.

## Verification Gates

- [d:r:i] The shared reference must stay narrower than a second uplift manifest.
- [d:r:i] Both milestone workflows must point to the same reference rather than drifting into two separate local doctrines.
- [d:r:i] The landed slice must survive repo-local rematerialization through tracked overlay carry.
- [d:r:i] The landed slice should leave one explicit propagation refresh and one governance-trace note rather than only mutating workflow prose.

## Held Later

- [d:r:i] `health.md` deepen-in-place route remains explicit as the next adjacent single-carrier alternative after this proposal.
- [d:r:i] Wider family-6 route asymmetry remains parallelizable rather than absorbed here.
- [d:r:i] Compatibility-anchor structural-row, typed standalone carrier, translation posture, and extraction/distribution all remain later-family questions.

## Current Consequence

- [d:r:i] The next `119` choice is now no longer ambient.
- [d:r:i] The active next object is:
  - milestone-boundary uplift shared-reference first
- [d:r:i] The held adjacent route remains:
  - `health.md` deepen-in-place follow-through
