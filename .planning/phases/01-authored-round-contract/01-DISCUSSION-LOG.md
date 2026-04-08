# Phase 1: Authored Round Contract - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md. This log preserves the alternatives considered during `exploratory --auto`.

**Date:** 2026-04-08
**Phase:** 1-authored-round-contract
**Areas discussed:** Round and pack contract, Clue media and fallback modeling, Validation posture

---

## Round And Pack Contract

| Option | Description | Selected |
|--------|-------------|----------|
| Thin location schema | Treat a round as mostly coordinates, panorama settings, and minimal metadata. | |
| Authored semantic round contract | Treat a round as authored game data with answer target, clue steps, aliases, reveal explanation, scoring profile, and venue/circuit semantics. | ✓ |
| Broad multi-mode schema now | Encode large portions of future party-mode breadth into the first contract immediately. | |

**User's choice:** `exploratory --auto` selected the authored semantic round contract as the grounded direction.
**Notes:** Grounded by Phase 1 roadmap scope, `PACK-02`, research pitfalls around thin schemas, and discovery guidance rejecting `lat/lng`-only rounds. Active v1 answer surfaces stay anchored at `circuit` and `venue`; future `section` or composite targets remain an extensibility concern rather than an immediate content commitment.

---

## Clue Media And Fallback Modeling

| Option | Description | Selected |
|--------|-------------|----------|
| Street View as the default substrate | Assume pano-style clues are the primary contract and other media are exceptions. | |
| Provider-agnostic mixed-media clue contract | Use one clue-step contract that can carry Street View, map, image, text, and fallback media with explicit coverage metadata. | ✓ |
| Ad hoc fallback handling | Keep fallback media outside the core contract and resolve gaps manually per round. | |

**User's choice:** `exploratory --auto` selected the provider-agnostic mixed-media contract with explicit coverage and fallback metadata.
**Notes:** Grounded by `PACK-03`, `OPS-01`, the coverage audit, and repeated research guidance that Street View must stay optional. The unresolved structural question is whether coverage metadata should be attached per round, per venue profile, or both.

---

## Validation Posture

| Option | Description | Selected |
|--------|-------------|----------|
| Runtime-only validation | Allow packs to load and rely on gameplay/runtime code to detect bad content. | |
| Strict pre-play validation | Reject incomplete, ambiguous, or broken rounds before they become playable. | ✓ |
| Manual editorial process only | Rely mainly on human review and loose conventions instead of a strong validator/importer path. | |

**User's choice:** `exploratory --auto` selected strict pre-play validation.
**Notes:** Grounded by `PACK-04`, research pitfalls around delayed validation, and the recommendation to begin with checked-in files plus validation/import tooling rather than a heavy authoring UI. Exact file format and validator package boundaries remain open for planning.

---

## the agent's Discretion

- Exact authored file format
- Exact validator/compiler package layout
- Exact naming and stable ID conventions

## Deferred Ideas

- Internal authoring UI beyond file/import tooling
- Active v1 rollout of `section`, `corner`, and composite answer surfaces
- Broader adjacent F1 party modes
- Unrestricted Street View free-roam or generic free-roam play
