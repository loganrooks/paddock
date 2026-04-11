# Phase 1: Authored Round Contract - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-11
**Phase:** 1-authored-round-contract
**Areas discussed:** Answer target structure and content identity, clue media and fallback modeling, coverage source of truth, validation and compile posture, future-aware seam protection

---

## Answer Target Structure And Content Identity

| Option | Description | Selected |
|--------|-------------|----------|
| Flat `circuit` / `venue` contract only | Optimize purely for the immediate v1 answer surfaces and defer deeper relationships. | |
| Hierarchy-preserving authored substrate | Keep v1 active answer surfaces at `circuit` and `venue`, but preserve the explicit `venue -> circuit -> section -> corner` relationship chain and stable content identity now. | ✓ |
| Broad multi-mode party schema now | Pull large amounts of future adjacent-mode structure into Phase 1 immediately. | |

**User's choice:** `exploratory --auto` selected the hierarchy-preserving authored substrate as the grounded direction.
**Notes:** Grounded by `SEAM-01`, the refreshed roadmap/canon, and the rerun audit findings that Phase 1 should protect cheap future seams without widening shipped scope.

---

## Clue Media And Fallback Modeling

| Option | Description | Selected |
|--------|-------------|----------|
| Street View as the default substrate | Assume pano-style clues are the real contract and other media are exceptions. | |
| Provider-agnostic mixed-media clue contract | Use one clue-step contract that preserves explicit clue-family semantics while supporting Street View, image, map fragment, text, and fallback media. | ✓ |
| Ad hoc fallback handling | Keep fallback logic outside the core content contract and resolve it manually per round. | |

**User's choice:** `exploratory --auto` selected the provider-agnostic mixed-media contract.
**Notes:** Grounded by `PACK-03`, `OPS-01`, the coverage audit, and prior Phase 1 context. Circuit-aware clue families remain explicit so fallback-heavy venues do not silently redefine the game.

---

## Coverage Source Of Truth

| Option | Description | Selected |
|--------|-------------|----------|
| Round-level only | Every round owns all coverage and fallback posture directly. | |
| Venue-profile only | Shared venue profiles own coverage posture and rounds only reference the venue. | |
| Hybrid venue profile plus round-level resolved posture | Shared venue profiles provide canonical posture while rounds can carry explicit resolved fallback or overrides. | ✓ |

**User's choice:** `exploratory --auto` treated the hybrid model as the best current working assumption.
**Notes:** This was not forced as a fully locked decision. It stays an open design question for replanning because requirements demand explicit fallback posture but do not yet prove the lowest-friction authoring split.

---

## Validation And Compile Posture

| Option | Description | Selected |
|--------|-------------|----------|
| Runtime-only validation | Let bad authored content fail later in gameplay/runtime flows. | |
| Strict pre-play compile validation | Reject incomplete, ambiguous, or broken authored content before it becomes playable, with stable diagnostics and explicit reference resolution. | ✓ |
| Manual editorial review only | Depend mainly on human review and loose conventions instead of strong validation tooling. | |

**User's choice:** `exploratory --auto` selected strict pre-play compile validation.
**Notes:** Grounded by `PACK-04`, prior Phase 1 context, and the rerun audit’s emphasis on venue identity ambiguity, concrete verification, and stable diagnostic expectations.

---

## Future-Aware Seam Protection

| Option | Description | Selected |
|--------|-------------|----------|
| Optimize only for the immediate anchor loop | Keep Phase 1 narrowly local even if cheap seam protection is lost. | |
| Protect cheap future seams while keeping shipped scope anchor-first | Add low-cost substrate protections now without importing future wrapper or adjacent-mode scope. | ✓ |
| Design an explicit platform schema now | Treat Phase 1 as the start of a broad F1 party-platform schema rather than an authored anchor-mode contract. | |

**User's choice:** `exploratory --auto` selected cheap future seam protection with anchor-first shipped scope.
**Notes:** Grounded by `.planning/LONG-ARC.md`, the refreshed roadmap, and the project posture that Milestone 1 should preserve substrate reuse without widening into Milestone 2 or 3 scope.

---

## the agent's Discretion

- Exact authored source format.
- Exact package layout for domain schemas, compiler, and tests.
- Exact canonical identifier field names once a single reference system is chosen.
- Exact representation of tags, content hashes, and related seam-protection metadata.

## Deferred Ideas

- Internal authoring UI beyond file/compiler workflows.
- Active rollout of `section`, `corner`, and composite answer surfaces in v1 gameplay.
- Adjacent non-anchor F1 party modes.
- Public challenge surfaces, public leaderboards, and spectator-facing shells.
- Unrestricted Street View free-roam or generic geography-first play.
