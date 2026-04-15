# .planning/AGENTS.md

## Scope

This file applies to work inside `.planning/`.

Read it together with root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md), not instead of it.

Its job is to keep planning, audit, research, canon, and phase-steering work rigorous without bloating the root file.

## Live Planning Sources Of Truth

Treat these as the primary planning canon:

- [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
- [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
- [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
- [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)
- [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- active phase docs under `.planning/phases/`

Additional rules:

- Prefer the latest non-superseded artifact.
- Prefer canon docs over exploratory notes when they conflict.
- Treat `discovery/` as upstream context, not live operational state.
- If canon conflicts, report the conflict explicitly instead of silently choosing one side.

## Artifact Discipline

The detailed artifact taxonomy and retention rules live in [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md).

Inside `.planning/`:

- keep `canon`, `phase work`, `audit trail`, `exploration`, and `generated corpus` distinct
- do not silently promote one class into another
- do not turn exploratory conclusions into canon without an explicit proposal or patch step
- if a newer artifact supersedes an older steering artifact, mark that relationship explicitly
- if an artifact is stale but still historically relevant, prefer status notes and replacement pointers over deletion
- do not let large generated corpora dominate the active planning surface without an explicit retention decision

## Research And Audit Quality

For non-trivial research, audit, gap-closure, sensitivity, or synthesis work:

- make the path of inquiry visible
- separate evidence from inference and unknowns
- surface assumptions rather than smuggling them in
- define loaded terms and anti-misread rules when they matter
- do not silently broaden scope
- do not accept a weaker frame, shortcut, or premature closure just because it was requested; push back when the request would degrade the quality of canon, planning, verification, or process doctrine
- that pushback should be explicit and well-argued:
  - identify the specific loss or risk
  - explain the stronger alternative
  - ground the case in artifacts, consequences, or reasoning that can withstand scrutiny
- partial pushback is often preferable to flat rejection:
  - keep the goal if it is sound
  - reject or revise the method, sequencing, scope, or closure pressure if that is the real problem

Prefer the repo-local `gsd-rigorous-research` skill for standalone research lanes.

When source grounding matters, distinguish clearly between:

- direct external grounding
- traceable external grounding through repo-local synthesis
- internal canon or audit support only

Do not treat repo-local restatement as if it were fresh external grounding.

For load-bearing planning/process artifacts, expose claim type and source-basis explicitly when a reader could otherwise mistake internal support for external support.

- Prefer `[t:s:b]`; use `[t:b]` only when the support mode is obvious.
- Minimal reminder:
  - claim type: `e` evidenced, `d` decided, `a` assumed, `o` open, `p` projected, `s` stipulated, `g` governing
  - support mode: `c` cited, `r` reasoned, `b` bare
  - source-basis: `i` internal, `d` external-direct, `t` external-traceable
- Join material support or basis codes with `+`.
- Internal cited grounding must cite the direct repo file and line numbers near the claim.
- External grounding should use markdown footnotes and an `External Works Cited` section.
- Detailed semantics live in:
  - [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md)
  - `.codex/skills/gsd-rigorous-research/references/method.md`

## Future-Flexibility Statusing

When a planning or audit pass is preserving future flexibility, require outputs to distinguish at least:

- `direct doctrine`
- `bounded-open branches`
- `preserve-only seams`
- `reversal-sensitive boundaries`
- `inquiry debt`

Do not flatten those categories into generic `open` or `deferred` language.

If terms like `challenge`, `showcase`, `hosted`, `premium`, `event`, `reviewed`, or `unsupported` are doing too much work, spell out the distinction instead of relying on local context.

## Canon And Roadmap Response Rules

- Do not treat `no blockers found` or `safe enough to proceed` as the satisfying endpoint of exploratory work when the better next step is canon uplift, roadmap clarification, or future-aware steering.
- If a pass earns substantive doctrine, explicitly ask whether:
  - canon should be uplifted
  - roadmap language should be clarified
  - future seams should become more explicit
  - `LONG-ARC.md` should absorb or sharpen any doctrine that reaches beyond the next milestone
- Broad canon changes should usually have a proposal artifact first.
- Keep current execution scope narrow, but do not let Milestone 01 convenience create avoidable Milestone 02 ambiguity or later long-arc distortion.
- Treat horizon handling explicitly:
  - `ROADMAP.md` and phase docs carry near-term sequencing
  - `PROJECT.md` carries the compact product identity and milestone frame
  - `LONG-ARC.md` carries the farther doctrine that current planning must preserve without prematurely importing later scope
- Do not let repeated naming density or omission silently choose winners between still-live branches.

## Phase And Rerun Hygiene

- Treat active `CONTEXT.md` files as steering briefs, not lightweight notes.
- Do not import later wrapper, hosting, monetization, or event-memory decisions into a current phase unless they are explicitly in scope.
- Current repo boundary:
  - Phase 01 is at a pre-rerun boundary
  - use a fresh discuss + planning pass before execution
- Do not treat older `01-*` artifacts as execution-approved just because they exist.

## Planning-Local Self-Audit

Before adding or expanding instruction in either root `AGENTS.md` or `.planning/AGENTS.md`, ask:

- Is this truly agent-facing runtime guidance?
- Is it stable enough for a durable instruction file?
- Is it already governed elsewhere?
- Is it specific enough to deserve prompt budget?
- Would a nested file be a better fit than root?
- What stale-state risk does this add?

## Maintenance

- This file should stay durable and subtree-local.
- Do not create deeper nested `AGENTS.md` files under `.planning/` unless the subtree is both durable and meaningfully different in workflow.
- If `.planning/` operating norms change, update this file in the same change rather than letting local instruction drift.
