# Initiative: Vision Alignment 2026-04

**Status:** Planned
**Started:** 2026-04-11
**Owner:** Logan Rooks
**Scope class:** Pre-Phase-01 alignment

---

## Why This Exists

Phase 01 is the first substrate-setting phase in Prix Guesser. It is where the project freezes the authored content contract that later rules, room, calibration, and wrapper work will consume.

That makes it unusually dangerous to treat ordinary phase planning as enough. The current canon is already directionally strong, but a few load-bearing questions remain open in the Phase 01 context:

1. Where coverage and fallback truth should live
2. How explicit the first answer-target lineage must be
3. How much scoring intent should be encoded now
4. How pack/round identity and references should freeze before compiler work starts

This initiative exists to reduce the chance of closing those questions in the wrong shape just because the planner wants a neat schema quickly.

## Why This Is Not A Full Vision Initiative

This project does **not** currently have the same kind of wide, cross-domain architectural uncertainty that justified the larger `f1-modeling` initiative shape. The broader product posture is already relatively well-aligned across:

- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`

So this initiative is deliberately narrower.

It does **not** reopen:

- private-first product posture
- host-screen/watchability bias
- browser-first join posture
- the long-arc milestone frame
- whether geography-and-circuit play is the v1 anchor

It exists only to align the authored substrate decisions that Phase 01 is about to freeze.

## Core Question

What content-contract decisions must be closed now to keep Phase 01 moving, and which decisions must remain explicitly deferred so the project does not accidentally bake future wrappers, room assumptions, or fallback drift into the authored model?

## Scope

**In scope**

- Authored round ontology and answer-surface hierarchy
- Coverage/fallback doctrine and clue-family semantics
- Pack/round identity and reference freezing
- The minimum scoring-intent contract Phase 01 should carry into Phase 2
- Decision anchors and planning guidance that Phase 01 must consume

**Out of scope**

- frontend framework choice
- room runtime and authority implementation
- deploy topology decisions
- public/share-by-link/public-spectator posture
- adjacent F1 mode expansion
- in-app authoring UI

## Intended Outputs

- `RESEARCH-PRINCIPLES.md`
- `PLAN.md`
- research notes under `research/`
- deliberation outputs under `deliberations/`
- a compact decision anchor that can be consumed before rerunning Phase 01 planning

## Completion Criteria

This initiative is complete when:

1. The authored-substrate option space has been mapped without premature closure
2. The few decisions that truly must close before Phase 01 planning are closed explicitly
3. Remaining uncertainty is recorded as deferral criteria, not hand-waved away
4. A decision anchor exists that the next Phase 01 planning pass can consume directly
5. The initiative produces concrete guidance for whether existing `01-CONTEXT.md`, `01-RESEARCH.md`, and pending Phase 01 plans should be amended, replaced, or left as-is

## Structural Posture

This initiative is intentionally small.

It starts with two research lanes, then one synthesis deliberation, then a decision anchor. If those steps surface critical underdetermination, the initiative may expand with targeted follow-up research or a second deliberation. Expansion is a legitimate outcome, but only if the findings warrant it.
