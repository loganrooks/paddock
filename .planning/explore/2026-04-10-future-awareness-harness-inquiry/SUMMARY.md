# Future-Awareness Harness Inquiry Summary

Updated: 2026-04-10
Status: synthesized

## Purpose

This inquiry tested how repo-local GSD currently carries future-awareness and where the most robust patch points likely are.

The goal was not to edit the harness immediately.

The goal was to produce reusable, planning-ready evidence about:

- what already works
- what is only documented
- what is operationalized downstream
- where a future patch would actually matter

## Method

This inquiry was run as a delegated-first exploration with persisted prompts and disjoint markdown outputs.

Artifacts:

- orchestration:
  - `.planning/explore/2026-04-10-future-awareness-harness-inquiry/00-ORCHESTRATION.md`
- prompts:
  - `.planning/explore/2026-04-10-future-awareness-harness-inquiry/prompts/01-canonical-artifacts-and-lightweight-doc-levers.prompt.md`
  - `.planning/explore/2026-04-10-future-awareness-harness-inquiry/prompts/02-downstream-consumers-and-prompt-operationalization.prompt.md`
  - `.planning/explore/2026-04-10-future-awareness-harness-inquiry/prompts/03-overlay-and-harness-modification-points.prompt.md`
- delegated findings:
  - `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/01-canonical-artifacts-and-lightweight-doc-levers.md`
  - `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/02-downstream-consumers-and-prompt-operationalization.md`
  - `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/03-overlay-and-harness-modification-points.md`

## Runtime Note

Requested delegation settings were:

- agent class: `explorer`
- model: `gpt-5.4`
- reasoning target: `xhigh`

What was verified:

- live `codex-tui.log` activity confirmed spawned child threads under `model=gpt-5.4`

What was not positively verified:

- immutable reads against `~/.codex/state_5.sqlite` did not surface child-thread rows for these explorer ids during this session
- because of that, effective persisted reasoning effort should be treated as unresolved rather than confirmed

This summary therefore distinguishes requested launch settings from effective runtime-state confirmation.

## Converged Findings

### 1. The repo already has meaningful future-aware leverage

The explorer outputs converged that the current repo is not missing future-awareness entirely.

What already exists:

- `PROJECT.md` already carries the long-arc product posture
- `ROADMAP.md` already stages proofs instead of reading like a flat backlog
- `REQUIREMENTS.md` already separates present obligations from later possibilities
- the repo-local `CONTEXT.md` shape already distinguishes `future_awareness` from `deferred`

Best evidence:

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/01-canonical-artifacts-and-lightweight-doc-levers.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:475`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:1071`

### 2. The main canonical-doc gap is normalization, not absence

The doc layer is directionally right but does not yet normalize the concepts the latest exploration says matter most.

Missing or under-specified in canonical artifacts:

- protected futures / protected seams
- explicit non-decisions
- visibility-state posture
- trust / service-obligation posture
- wrapper vs sibling-surface distinction

This points to a low-drag doc refinement path in:

- `PROJECT.md`
- `ROADMAP.md`
- `REQUIREMENTS.md`

Best evidence:

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/01-canonical-artifacts-and-lightweight-doc-levers.md`

### 3. The overlay already operationalizes future-awareness downstream

The strongest surprise from the harness-facing lanes is that the current overlay is more operational than the handoff initially feared.

Confirmed operationalization:

- `discuss-phase.md` explicitly derives future-awareness from downstream phases and future ambitions before writing `CONTEXT.md`
- `plan-phase.md` explicitly tells researcher, planner, and checker to preserve `<future_awareness>` and `<derived_constraints>`
- `research-phase.md` separately tells standalone research to treat `<future_awareness>` as a guardrail

Key local confirmation:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:475-482`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:220-239`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:329-333`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:635-640`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:775-778`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md:68-72`

Best evidence:

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/02-downstream-consumers-and-prompt-operationalization.md`

### 4. The chain is still fragile at three specific points

All harness-facing conclusions converge on the same weak spots:

- planning can still continue without `CONTEXT.md`
- `canonical_refs` are declared as mandatory but are not expanded into hard `files_to_read` for downstream agents
- the final plan artifact does not preserve future-aware seams as a first-class field, so the signal can disappear into prose

Key local confirmation:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:211-251`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:1027-1045`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:614-629`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:647-694`

Best evidence:

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/02-downstream-consumers-and-prompt-operationalization.md`
- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/03-overlay-and-harness-modification-points.md`

### 5. The robust patch path is workflow-first, not template-first

The most important converged judgment is about patch order.

Most robust first-line levers:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`

Optional support surface:

- `tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs`

Follow-up sync surfaces, not primary levers:

- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
- `tooling/portable-gsd/overlay/get-shit-done/templates/config.json`
- `tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md`

Why:

- `discuss-phase.md` writes the active `CONTEXT.md` body inline
- `plan-phase.md` is the real propagation and checking point
- `research-phase.md` keeps standalone research aligned
- template-only edits are easy to make and easy to bypass

Best evidence:

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/03-overlay-and-harness-modification-points.md`

## Most Promising Follow-Up Leads

These are the strongest next investigation or patch targets if the repo decides to formalize this later:

1. Tighten `plan-phase.md`’s context gate for exploratory mode.
   Why: the harness currently admits a known weak path where future-aware planning can proceed without a steering brief.

2. Add a structured preservation loop in planner/checker prompts.
   Why: future-awareness is currently mentioned as a guardrail, but not forced through a repeatable mapping like:
   - future-aware item
   - present design consequence
   - protected seam
   - explicit rationale for non-action

3. Make `canonical_refs` more operational.
   Why: the discuss flow accumulates strong references, but downstream agents are not forced to read them directly.

4. Decide whether the final plan artifact should preserve future-aware seams explicitly.
   Why: the strongest current chain ends at planning time; it is weaker at plan-review and execution time.

5. Refine canonical docs in parallel, but do not mistake that for sufficient harness change.
   Why: the doc layer should be sharper, but the workflow prompt layer is the stronger leverage point.

## Current Recommendation

If work resumes later, the recommended order is:

1. Preserve this inquiry as the reusable evidence base.
2. If the repo wants immediate low-drag improvement, refine canonical docs:
   - `PROJECT.md`
   - `ROADMAP.md`
   - `REQUIREMENTS.md`
3. If the repo wants reliable harness behavior, patch the workflow prompt layer next:
   - `discuss-phase.md`
   - `plan-phase.md`
   - `research-phase.md`
4. Only after behavior is settled, sync templates/docs/config references.

This inquiry does not support the conclusion that a template-only `Future Awareness` section is enough.

It also does not support the conclusion that the repo needs a ground-up harness redesign.

The evidence points to a narrower judgment:

- canonical-doc sharpening plus workflow-prompt reinforcement is the likely right layered path

## Changed files

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/SUMMARY.md`
