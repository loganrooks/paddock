# Master Plan: Vision Alignment 2026-04

**Target runtime:** Codex GPT-5.4
**Required reading:** `RESEARCH-PRINCIPLES.md`
**Purpose:** reduce Phase 01 substrate risk before rerunning planning

---

## This Plan Is Scaffolding, Not A Commitment To Over-Research

The initiative is deliberately small because the repo already has a relatively coherent product doctrine. The job here is not to relitigate the whole roadmap. The job is to determine whether the authored content substrate is sufficiently aligned to justify a clean Phase 01 planning pass.

One valid outcome at any review gate is:

> "The remaining uncertainty is bounded enough that Phase 01 can proceed."

Another valid outcome is:

> "One or two questions are still too underdetermined; commission targeted follow-up."

The structure should expand only if the findings warrant it.

## Required Inputs

Every call in this initiative should read:

- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
- `.planning/phases/01-authored-round-contract/01-RESEARCH.md`
- `.planning/phases/01-authored-round-contract/01-VALIDATION.md`
- `RESEARCH-PRINCIPLES.md`

## Wave Structure

### Wave 1 — Terrain Mapping (2 calls)

| Call | Focus | Mode | Reasoning |
|------|-------|------|-----------|
| 1A | Authored ontology, answer-surface hierarchy, scoring-intent minimums | terrain mapping | high |
| 1B | Coverage/fallback doctrine, clue-family semantics, identity/reference freezing | terrain mapping | high |

### Review Gate 1

Questions to answer:

1. Are the Phase 01 open questions actually separable, or are they coupled enough to require one joint closure?
2. Which decisions must close before Phase 01 planning can proceed?
3. Which decisions should be deferred explicitly?
4. Do the current `01-CONTEXT.md` and `01-RESEARCH.md` already capture the right substrate shape, or are they materially incomplete?

Possible outcomes:

- proceed to one synthesis deliberation
- commission one targeted follow-up research call
- conclude the current canon is already sufficient and skip further initiative work

### Wave 1.5 — Targeted Follow-Up Research (optional, 0-1 calls)

Run only if Review Gate 1 identifies a truly load-bearing unresolved question, for example:

- exactly where coverage/fallback truth should live
- whether answer-surface lineage needs another intermediate object
- whether scoring intent should be presets-only or hybrid

### Wave 2 — Synthesis Deliberation (1 call)

| Call | Focus | Mode | Reasoning |
|------|-------|------|-----------|
| 2A | Close only the authored-substrate decisions that must be settled before Phase 01 planning; defer the rest explicitly | deliberation | xhigh |

This call should produce a clear distinction between:

- closed now
- deferred with closure criteria
- explicitly out of scope for Phase 01

### Review Gate 2

Questions to answer:

1. Is there now a decision anchor strong enough to govern a new Phase 01 planning pass?
2. Did the deliberation stay within authored-substrate scope?
3. Did it preserve the existing long-arc doctrine without dragging in later-wrapper assumptions?

Possible outcomes:

- accept and draft a decision anchor
- request one revision
- commission one narrow follow-up if a truly blocking gap remains

### Wave 3 — Decision Anchor (1 call or local synthesis)

| Output | Focus | Reasoning |
|--------|-------|-----------|
| `deliberations/01-decision-anchor.md` | compact handoff for the next Phase 01 planning pass | high |

The decision anchor should answer:

- what Phase 01 must treat as closed
- what Phase 01 must preserve but not activate
- what Phase 01 must explicitly defer
- what should change in the existing planning inputs, if anything

## Minimum Shape

Minimum initiative size:

- 2 research calls
- 1 deliberation
- 1 decision anchor

Expanded shape:

- add 1 targeted research follow-up only if findings justify it

## Success Test

The initiative succeeded if the next planner can answer Phase 01 contract questions without inventing policy on the fly.

It failed if it produces polished prose without narrowing the actual substrate risk.
