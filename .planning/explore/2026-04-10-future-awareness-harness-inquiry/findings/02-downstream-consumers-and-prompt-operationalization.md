# Downstream Consumers And Prompt Operationalization

## 1. Scope and sources

This memo is limited to whether repo-local GSD downstream consumers actually notice and preserve future-aware material once it exists in canonical docs or `CONTEXT.md`.

Sources read:

- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md`
- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINTS/10-handoff-for-future-awareness-harness-inquiry.md`
- `.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md`
- `AGENTS.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
- `.codex/get-shit-done/templates/phase-prompt.md`
- `.codex/get-shit-done/templates/planner-subagent-prompt.md`

The framing docs are aligned on the concern: future-awareness should survive as active steering, not just as remembered conversation. `AGENTS.md` also makes that explicit by saying `CONTEXT.md` is a steering brief and that future awareness matters downstream.

## 2. Where future-awareness enters the flow today

Explicitly today, future-awareness enters through the phase steering brief path, not primarily through the final plan format.

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md` defines `CONTEXT.md` as a steering artifact that should capture future awareness alongside decisions, open questions, guardrails, and deferred ideas.
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md` makes `future_awareness` a required section and distinguishes it from `deferred`. That is a real structural entry point, not just a note in prose.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md` also injects future-awareness during the PRD express path by generating a `CONTEXT.md` with a `future_awareness` section.
- `AGENTS.md` reinforces the intended contract: downstream consumers are supposed to treat `CONTEXT.md` as steering, including future awareness.

Weak implication: canonical docs can carry future-aware material, but in the provided flow they are mostly upstream inputs unless someone translates that material into `CONTEXT.md` or embeds it directly into the spawned prompt guidance.

## 3. Where downstream prompts/workflows clearly operationalize it

There is stronger operationalization here than the handoff note feared, but it is concentrated in the overlay workflows.

- Explicit prompt instruction: `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md` tells the researcher to treat `CONTEXT.md` as a steering brief, not just locked choices, and to treat `derived_constraints` and `future_awareness` as implementation guardrails.
- Explicit prompt instruction: `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md` gives the planner the same framing and goes further: it says future-awareness should shape interfaces, data models, and abstractions now.
- Explicit prompt instruction: the checker section in `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md` tells `gsd-plan-checker` to flag plans that violate `future_awareness` or `derived_constraints`.
- Explicit workflow intent: `tooling/portable-gsd/overlay/get-shit-done/templates/context.md` says the researcher uses future-awareness to focus investigation and the planner uses it to create tasks without closing doors for later phases.
- Explicit propagation expectation: `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md` requires `CONTEXT.md` to be loaded early and passed to all agents.

This means future-awareness is not merely documented at the discuss layer. In the repo-local overlay, research, planning, and plan-checking are all explicitly instructed to consume it.

## 4. Where the chain still looks documentary or fragile

The weak points are not at the `CONTEXT.md` definition layer. They are at enforcement, portability, and artifact carry-through.

- Missing link: `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md` still allows planning to continue without `CONTEXT.md`. The warning is clear, but future-awareness remains optional at runtime if the operator proceeds anyway.
- Missing link: `.codex/get-shit-done/templates/planner-subagent-prompt.md` only passes the phase context path. It does not itself encode how future-aware material must be interpreted. In practice, the stronger behavior lives in the overlay `plan-phase.md`, so this is prompt logic split across files rather than one robust contract.
- Missing link: `.codex/get-shit-done/templates/phase-prompt.md` has no dedicated field for protected seams, future constraints, non-foreclosure notes, or explicit deferrals. Once planning finishes, future-awareness can disappear into task prose instead of surviving as a first-class part of the plan artifact.
- Weak implication: `tooling/portable-gsd/overlay/get-shit-done/templates/context.md` says downstream agents must read `canonical_refs`, but the spawn prompts do not expand those refs into concrete `files_to_read`. If future-aware material lives mainly in canonical docs rather than in `CONTEXT.md`, consumption depends on the subagent voluntarily following a reference inside `CONTEXT.md`.
- Missing link: the requirements/context coverage check in `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md` audits dropped items from `decisions`, but there is no equivalent structured audit that extracts every future-awareness item and proves each one was preserved, sequenced, or intentionally ignored with rationale.
- Weak implication: the checker is told to flag violations of future-awareness, but that remains natural-language guidance. There is no explicit mini-schema like "map each future-aware guardrail to a task, interface seam, checkpoint, or rationale."

So the current chain is best described as: explicit at prompt level, but still fragile at enforcement level.

## 5. Highest-leverage prompt or workflow modifications

- Tighten the context gate in `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`. In exploratory mode, future-aware planning should default to "stop and gather context" rather than allowing silent continuation without a steering brief.
- Add a required preservation pass in the planner prompt inside `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`: extract each future-awareness item and map it to a present-day design consequence, protected seam, validation task, or explicit "not acted on now" rationale.
- Add a matching checker pass in `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`: fail verification if a future-awareness item is neither reflected in plan structure nor explicitly justified as non-actionable for this phase.
- Expand `canonical_refs` into actual `files_to_read` for researcher, planner, and checker when `CONTEXT.md` names them. That would make future-aware material in canonical docs operational instead of merely discoverable.
- Extend `.codex/get-shit-done/templates/phase-prompt.md` so plans can carry forward a compact field such as `protected_seams`, `future_constraints`, or `non_foreclosure_notes`. That would preserve the signal beyond the planning conversation and into execution/review.

## 6. Recommendation

The repo-local overlay has already crossed the line from pure documentation into real prompt operationalization, especially in `research-phase.md` and `plan-phase.md`. The problem is that this operationalization is still soft: it depends on `CONTEXT.md` existing, on overlay-specific prompt text staying in place, and on plan authors carrying the intent forward manually.

The highest-leverage move is not another template-only change. It is a layered patch:

- keep the current `CONTEXT.md` future-awareness section
- strengthen `plan-phase.md` so future-aware context is harder to skip
- add a structured planner/checker preservation loop
- optionally extend the PLAN artifact so protected future seams remain visible after planning

That would turn future-awareness from "well-described and usually noticed" into something the harness can actually audit.

## Changed files

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/02-downstream-consumers-and-prompt-operationalization.md`
