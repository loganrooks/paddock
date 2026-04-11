# Future-Awareness Harness Patch

Date: 2026-04-10
Status: approved for implementation
Owner: Codex orchestration session

## Purpose

Record why this harness patch exists, why these changes were selected instead of broader or narrower alternatives, what outcomes are predicted, and how later review should judge whether the patch actually improved planning behavior.

This is the canonical reasoning record for the patch itself.

Evidence gathering remains in the inquiry package:

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/SUMMARY.md`
- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/01-canonical-artifacts-and-lightweight-doc-levers.md`
- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/02-downstream-consumers-and-prompt-operationalization.md`
- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/03-overlay-and-harness-modification-points.md`

## Problem Statement

The repo already carries meaningful future-awareness, but the current harness still loses that signal too easily.

The inquiry converged on three operational weaknesses:

1. Exploratory planning can proceed without `CONTEXT.md`, which means the steering brief can be absent precisely when ambiguity is highest.
2. `canonical_refs` are captured but not turned into hard downstream reads, so important source-of-truth docs can degrade into soft suggestions.
3. Future-aware seams are visible during discussion but are not preserved as a first-class planning artifact, so review and later reflection depend too much on prose memory.

The patch therefore aims to harden transmission, not invent a new abstract workflow.

## Scope Decision

This patch is intentionally layered and repo-local.

Included:

- workflow behavior changes in the portable overlay
- matching updates to the live `.codex` runtime copy so current behavior changes immediately
- canonical planning doc tightening in `.planning/`
- a durable reasoning record for later reflection

Explicitly excluded in this pass:

- a new persistent config toggle for context bypass
- a general-purpose exploration formalization workflow
- stricter `verify.cjs` enforcement that would break legacy plan artifacts
- a broad redesign of GSD planning architecture

## Chosen Changes And Justifications

### 1. Hard gate exploratory planning when `CONTEXT.md` is missing, with `--allow-no-context` as the only bypass

Why this change:

- The inquiry showed the current weakest path is not absence of ideas but absence of the steering brief at the exact moment planning commits structure.
- Exploratory mode is where assumptions, open questions, and future seams matter most. Allowing silent continuation in that mode weakens the whole chain.
- A CLI flag is better than a persistent config knob for the first pass because bypass should stay explicit, local to a run, and easy to audit later.

Why not a total ban:

- There are legitimate emergency or low-context planning cases.
- The bypass preserves operator autonomy while forcing an intentional acknowledgement of reduced guarantees.

### 2. Normalize `future_awareness` into explicit buckets

Chosen buckets:

- `Protected Seams`
- `Explicit Non-Decisions`
- `Current Posture`
- `Future Shape Notes`

Why this change:

- The current `future_awareness` section is directionally useful but too free-form to propagate consistently.
- The inquiry found the canonical-doc gap was normalization, not absence.
- These buckets separate different kinds of future-facing information that otherwise get collapsed:
  - seams that must not be broken now
  - things intentionally not decided yet
  - the current trust and visibility posture the project is actually operating under
  - shape notes about plausible wrapper or sibling-surface evolution

Why these buckets specifically:

- They map to this repo's actual product posture: private-room core, open wrapper questions, and deliberately deferred public obligations.
- They are narrow enough to be operational but broad enough to survive multiple phases.

### 3. Force `canonical_refs` toward concrete downstream reads

Why this change:

- The discuss flow already accumulates useful references.
- The current weakness is not capture but downstream enforcement.
- If refs are not operationalized, planners and researchers can satisfy the letter of the workflow while missing the actual sources of truth.

Why use file expansion instead of only stronger wording:

- Prompt wording alone leaves too much room for omission.
- Concrete reads are auditable and later reviewable.

### 4. Require planner/checker preservation of every material future-aware item

Mapping rule:

- preserved seam
- sequencing choice
- validation task
- explicit non-action rationale

Why this change:

- The current harness says future-awareness matters, but does not force a plan-time accounting loop.
- The patch converts "remember this" into "account for this."
- This is the minimum needed to make dropped future constraints visible during verification.

Why checker enforcement matters:

- Planner-only guidance is too weak; omissions become apparent only if a verifier is instructed to treat silent drops as failures.

### 5. Add `future_preservation` to the plan artifact

Why this change:

- The inquiry showed the chain is strongest during discuss/planning and weakest once the final `PLAN.md` becomes the durable artifact.
- Frontmatter is the right first location because it is structured, reviewable, and compatible with current parsing.

Why not enforce it in global verification yet:

- This repo already contains pre-patch plans.
- Immediate hard enforcement in `verify.cjs` would create backward-compatibility churn before the new workflow has proven itself.

### 6. Tighten canonical docs in parallel

Target docs:

- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`

Why this change:

- Workflow hardening without sharper canonical inputs would produce more structured but still low-signal outputs.
- The inquiry explicitly found that docs are already directionally right and mainly need normalization.

Why these docs:

- `PROJECT.md` is where long-arc posture belongs.
- `ROADMAP.md` is where phase-by-phase preservation and deferral logic should stay visible.
- `REQUIREMENTS.md` needs a middle category between v1 commitments and v2 aspirations so protected seams and explicit deferrals are not inferred indirectly.

### 7. Patch the workflow files, not just templates

Primary levers:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`

Supporting surfaces:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-power.md`
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
- `tooling/portable-gsd/overlay/get-shit-done/templates/phase-prompt.md`

Why this change:

- The inquiry established that template-only edits are easy to bypass because the active workflow bodies write or interpret these artifacts inline.
- `discuss-phase-power.md` is included because it is another `CONTEXT.md` producer and should not lag standard discuss mode.

## Rejected Alternatives

### Rejected: template-only patch

Reason:

- High risk of false confidence.
- Does not reliably change active orchestration behavior.

### Rejected: doc-only patch

Reason:

- Helpful for clarity, insufficient for behavior.
- Leaves known weak propagation points untouched.

### Rejected: new persistent config toggle for no-context planning

Reason:

- Makes the bypass too easy to normalize.
- First pass should bias toward explicit operator intent, not ambient configuration.

### Rejected: immediate global strict validation on legacy plans

Reason:

- Good long-term candidate, poor first-pass rollout.
- Would conflate backward-compatibility cleanup with the harness-behavior experiment itself.

### Rejected: formalize a generic exploration workflow now

Reason:

- The current task is to harden future-awareness propagation in this repo.
- Exploration formalization may be worthwhile later, but it is not on the critical path for this patch.

## Quality Gates For This Change

Implementation is not considered complete unless all of the following are true:

- The deliberation record exists before workflow edits.
- Exploratory `plan-phase` blocks on missing `CONTEXT.md` unless `--allow-no-context` is present.
- The bypass path emits an explicit reduced-guarantee warning.
- `future_awareness` uses the same normalized bucket vocabulary across discuss, PRD-generated context, and standalone research guidance.
- `canonical_refs` are treated as concrete downstream reads when the files exist.
- Planner guidance requires every material future-aware item to be preserved, sequenced, validated, or explicitly justified as not actionable now.
- Checker guidance treats silent drops as failures.
- Newly generated plan artifacts have a structured `future_preservation` field.
- Re-running `./scripts/setup-portable-gsd.sh` would preserve the tracked behavior because the overlay contains the durable changes.

## Predictions

### Base predictions

- Contextless exploratory planning will become materially rarer because the default path now blocks unless the operator explicitly bypasses it.
- New `CONTEXT.md` files will better distinguish what must remain open from what must remain protected.
- Plans created after the patch will be easier to audit because future-aware preservation intent will be visible in the artifact, not only implied by task prose.

### Qualified predictions

- If operators rarely use `--allow-no-context`, planning quality should improve because the steering brief becomes the normal prerequisite.
- If operators frequently use `--allow-no-context`, the patch will mostly improve explicitness rather than actual planning quality.
- If canonical docs stay sharp, the new bucket structure should reduce ambiguity in later replans and reviews.
- If canonical docs remain vague, the new structure may become formulaic boilerplate without adding much real signal.
- If the planner actually emits `future_preservation` consistently, later reflection and review should become easier because preserved seams and deferred decisions will be queryable in frontmatter rather than buried in free prose.

## Falsifiers And Review Hooks

The patch should be considered weak or failed if later review finds any of the following:

- Operators still routinely plan exploratory phases without `CONTEXT.md`.
- `--allow-no-context` is used so often that the hard gate has little practical effect.
- New `future_awareness` sections are structurally present but content-thin, repetitive, or disconnected from actual project posture.
- The planner or checker still allows future-aware items to disappear silently.
- `future_preservation` is technically present but too generic to help later review.

Review should look specifically at:

- actual bypass frequency and reasons
- whether plan reviews mention protected seams or explicit non-decisions more often
- whether replanning becomes easier because posture and deferrals remain visible
- whether any new friction is disproportionately caused by the hard gate rather than by real missing context

The review artifact for that later assessment is:

- `.planning/deliberations/2026-04-10-future-awareness-harness-patch-review.md`

## Implementation Order

1. Write this deliberation record and the paired review stub.
2. Patch workflow producers and consumers in the overlay.
3. Patch matching live `.codex` copies so current runtime behavior matches the tracked overlay.
4. Tighten canonical planning docs.
5. Verify the resulting surfaces against the quality gates above.

## Notes For Later Reflection

Do not judge this patch only by whether more structure appears in files.

Judge it by whether:

- future-sensitive choices are dropped less often
- planning inputs are harder to bypass accidentally
- later reviewers can tell what was protected, what was deferred, and why
- the extra structure remains specific to Prix Guesser instead of becoming generic harness theater
