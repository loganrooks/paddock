---
date: 2026-04-13
artifact_type: repo_scan
scope: "Repo-local scan for existing sensitivity-analysis / impact-analysis / dependency-tracing conventions relevant to Round 2B foreclosure synthesis"
status: complete
---

# Round 2B Sensitivity Analysis Repo Scan

## Short answer

The repo does **not** appear to have a named, formal `sensitivity analysis` or `impact analysis` artifact pattern.

It **does** already have a meaningful adjacent pattern under other names:

- `future_awareness`
- `Protected Seams`
- `Explicit Non-Decisions`
- assumptions with explicit `If wrong` consequences
- `Dependencies and Relations`
- `pressure map`
- `early decision ledger`
- `non-foreclosure`

That is real signal, not just vague wording. But it is still missing one thing Round 2B now wants: an explicit **experience -> shortcut -> seam -> downstream ripple** map.

## 1. Existing pattern, under different names?

Yes, partially.

The strongest repo-local equivalents are:

- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
  Carries explicit `Protected Seams`, `Explicit Non-Decisions`, `Future Shape Notes`, and downstream integration points. This is the closest planning-native non-foreclosure surface.
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
  Normalizes the same `future_awareness` buckets as a reusable planning shape.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
  Treats future-awareness as a first-class output and explicitly derives it from downstream phases and future ambitions.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md`
  Requires assumptions to include `If wrong` consequences. That is effectively a lightweight local sensitivity-analysis convention.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
  Carries forward `future_preservation`, checks whether plans silently drop future-aware items, and forces planner/checker attention to preserved seams and non-decisions.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/next-round-gap-review.md`
  Already names the missing artifact directly: the audit lacks an explicit `experience-to-architecture foreclosure matrix`.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-foreclosure-synthesis-task-spec.md`
  Converts that gap into a Round 2B requirement via `pressure map`, `early decision ledger`, and `shortcuts most likely to cause foreclosure`.

So the repo already has a mature **non-foreclosure / dependency / consequence** grammar, but not yet a dedicated ripple-analysis artifact class.

## 2. Most relevant files and conventions

Most relevant now:

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md`
  Best local doctrine for `non-foreclosure`, `traceability`, and `dependency tracing`.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/next-round-gap-review.md`
  Best explicit statement of what is still missing and why Round 2B exists.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-foreclosure-synthesis-task-spec.md`
  Best current shape for the needed synthesis axes.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-a-room-topology-task-spec.md`
  Closest lane to topology/authority/visibility ripple tracing.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-b-history-cadence-task-spec.md`
  Closest lane to persistence/cadence/content-model ripple tracing.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-c-phase-01-ledger-task-spec.md`
  Current place where planning judgments become `explicit now / keep open / defer`.
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
  Concrete proof that the repo already uses protected seams and explicit non-decisions in a planning-facing way.
- `.planning/LONG-ARC.md`
  Canonical long-arc doctrine for preserving seams without importing future scope.
- `.planning/ROADMAP.md`
  Already carries some staged dependency logic and explicit “does not decide yet” posture.
- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/SUMMARY.md`
  Best repo-local retrospective on where future-aware planning is strong and where it still loses signal.
- `discovery/12-framework-decision-context.md` and `discovery/13-room-backend-decision-context.md`
  Good examples of separating coupled decisions into clearer surfaces instead of flattening them into one stack/backend choice.

Useful convention summary:

- planning doctrine uses seam preservation, not just feature lists
- dependency tracing is usually expressed narratively via `Dependencies and Relations`
- sensitivity is usually expressed as `If wrong` or “what this shortcut would foreclose”
- final planning classification happens later via ledgering, not in first-pass exploration

## 3. Are these patterns good enough for Round 2B?

Partly, but not fully.

What is good:

- The repo already knows how to talk about protected seams, open decisions, downstream dependencies, and anti-foreclosure posture.
- The audit stack already has traceability rules and a strong `pressure map -> ledger` decomposition.
- Phase planning machinery already recognizes “preserve this now without overcommitting.”

What is missing:

- no standard compact matrix for `experience pressure -> tempting shortcut -> preserved seam -> affected later surfaces`
- no standard severity/strength marker for ripple size
- no explicit cross-lane synthesis convention for “if we collapse X now, which later archetypes become awkward, expensive, or distorted?”
- `future_preservation` is strong for phase planning, but Round 2B is still one level earlier and broader than a normal phase plan

So the repo has the right ingredients, but not a single established artifact that fully covers the current need.

## 4. Recommendation for Round 2B Lane A/B

Round 2B should include **explicit sensitivity/ripple mapping inside Lane A and Lane B**, not only after them.

Recommended posture:

- Wave 1 (`Lane A` / `Lane B`): each lane should explicitly map
  `experience pressure -> early shortcut -> preserved seam/separation -> likely foreclosure/ripple`
- Wave 2 (`Lane C`): should classify those mapped pressures into
  `explicit now / keep open / defer`
- final synthesis: should consolidate and resolve overlaps, not invent the ripple logic from scratch

Why this order fits the repo:

- it matches the existing `pressure map` then `ledger` structure already defined in the Round 2B specs
- it avoids pushing all sensitivity work too late into Lane C, where it would become compressed and second-hand
- it preserves the repo's usual distinction between exploratory pressure-mapping and later planning judgment

## Bottom line

The repo already has a meaningful **non-foreclosure / dependency / consequence** pattern, but mostly under planning and audit language rather than under the label `sensitivity analysis`.

For the current need, that pattern is useful but incomplete. Round 2B should treat **explicit ripple mapping in Lane A/B** as a missing-but-compatible extension of the repo's existing conventions, with Lane C and the final synthesis responsible for classification and closure rather than first discovery.
