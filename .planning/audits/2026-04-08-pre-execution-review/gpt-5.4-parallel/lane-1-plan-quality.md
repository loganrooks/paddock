# Lane 1: Phase 1 Plan Quality Audit

## Overall Verdict

**ready-with-caveats**

The four plans cover the Phase 1 roadmap goal and requirement surface well enough to execute in order, and I found no invalid `read_first` targets of the specific bad kind called out in the task spec. The remaining problems are mostly contract-clarity and verification-quality issues rather than outright execution blockers.

## Per-Plan Assessment

### 01-01-PLAN.md

Status: strong, but slightly under-specified.

- Good: establishes the workspace, command surface, and package split needed by every later plan.
- Good: freezes most of the high-risk vocabulary early, which is the right move for a phase whose main risk is schema drift.
- Caveat: it does not freeze the `PackSource` / `roundOrder` reference shape, even though later plans depend on that being canonical (`01-01-PLAN.md:113`).
- Caveat: it standardizes on global `content/venues/*.yaml` immediately, which is defensible, but stronger than the research recommendation required for a single-pack Phase 1 (`01-01-PLAN.md:113`, `01-RESEARCH.md:354-357`).

### 01-02-PLAN.md

Status: strong and aligned with Phase 1 success criteria.

- Good: directly covers PACK-02, PACK-03, and OPS-01 through tests plus strict schemas.
- Good: keeps Phase 1 scoring explicit without drifting into Phase 2 rule-engine work.
- Caveat: `PackSourceSchema` is required, but its exact top-level shape and `roundOrder` reference structure are still left to executor judgment (`01-02-PLAN.md:107`).
- Caveat: the tests pin media kinds and fallback behavior, but they do not pin the exact nested pack-reference contract that Plan 03 must later author against.

### 01-03-PLAN.md

Status: good example-authoring plan, but its verification is weaker than the earlier schema plan.

- Good: it demonstrates both supported v1 answer surfaces and all three coverage classes.
- Good: it keeps authored content transport-agnostic and fallback-explicit, which matches the roadmap and context.
- Caveat: Task 1 requires both `id` and `venueId` in each venue profile, while later round files only refer to `venueRef`; the canonical join key is not stated (`01-03-PLAN.md:80`, `01-03-PLAN.md:98`, `01-04-PLAN.md:88`).
- Caveat: Task 2's strongest acceptance criteria are still manual, not automated: “mirrors the `roundOrder` reference shape” and “mirror the implemented nested shapes” are correct goals, but the listed verify command does not actually prove them (`01-03-PLAN.md:98-110`).

### 01-04-PLAN.md

Status: good compiler/validator plan with one remaining diagnostic-contract gap.

- Good: it completes PACK-04 with cross-file validation and a real compile path.
- Good: it keeps validation and compile on the stable root command surface frozen in Plan 01.
- Good: the uncommitted diff adding `tests/contract/content-graph-loading.test.ts` materially improves execution-readiness (`01-04-PLAN.md:86-97`).
- Caveat: Task 2 standardizes diagnostics for duplicate keys, broken round refs, alias conflicts, and missing fallback declarations, but not for broken `venueRef` resolution or path-policy failures even though Task 1 explicitly implements both (`01-04-PLAN.md:88`, `01-04-PLAN.md:107-118`).

## Cross-Plan Consistency Check

- Phase 1 success criteria are covered in sequence: 01-01 freezes vocabulary, 01-02 makes the contract executable, 01-03 proves authors can actually use it, and 01-04 enforces pack-level validity against authored YAML (`ROADMAP.md:31-45`).
- No invalid `read_first` targets found. Every `read_first` path is either already present now or is created by an upstream dependency before the consuming plan runs. The known bad anti-pattern of pointing `read_first` at same-plan create targets does not appear in these plans.
- Main contract inconsistency: venue identity is ambiguous. Venue files are required to contain both `id` and `venueId`, but rounds only store `venueRef`, and the compiler only says it resolves `venueRef` against `content/venues/*.yaml`; it never states whether `venueRef` matches filename, `id`, or `venueId` (`01-03-PLAN.md:80`, `01-03-PLAN.md:98`, `01-04-PLAN.md:88`).
- Main specification gap: `PackSourceSchema` and the exact `roundOrder` reference shape are not frozen in Plan 01, even though Plan 03 depends on them as canonical (`01-01-PLAN.md:113`, `01-02-PLAN.md:107`, `01-03-PLAN.md:98-109`).
- Secondary specification gap: Plan 03 depends on exact nested shapes for `acceptedAnswers`, `reveal`, and `clueSteps[*].media`, but its automated verification only greps for field names, so that contract is not independently proven until Plan 04 (`01-03-PLAN.md:99-110`).

## Assessment Of Uncommitted Diffs

- `01-02-PLAN.md`: improvement. The `must_haves.truths` wording now matches roadmap outcomes better and is easier to audit against Phase 1 success criteria. No regression found.
- `01-03-PLAN.md`: clear improvement. The diff fixes the stale `mediaKind` wording and correctly points the plan at `clueSteps[*].media.kind`. Removing the vague “authored asset-path fields” language is also a net positive because those fields were not frozen elsewhere.
- `01-04-PLAN.md`: mostly improvement. Adding `tests/contract/content-graph-loading.test.ts` makes Task 1 much more concrete. Removing `UNSAFE_ASSET_PATH` from Task 2 is reasonable if path-policy failures are treated as loader-level failures, but then the plan should explicitly say what stable diagnostic shape those failures use.
- `.continue-here` deletion: irrelevant to plan quality. It should not affect execution of the four plans.

## Specific Issues Found

- `warning`: Venue reference identity is ambiguous. `01-03-PLAN.md:80` requires both `id` and `venueId`, but rounds use only `venueRef` and `01-04-PLAN.md:88` does not define which field `venueRef` targets.
- `warning`: `PackSourceSchema` / `roundOrder` is not frozen early enough. `01-01-PLAN.md:113` freezes many inner shapes but not the pack reference contract that `01-03-PLAN.md:98-109` later treats as canonical.
- `warning`: Plan 03 acceptance criteria are partly non-concrete. The automated check at `01-03-PLAN.md:99-100` cannot prove the stronger criteria at `01-03-PLAN.md:109-110`.
- `warning`: Plan 04 does not define stable validator output for broken venue refs or path-policy failures, even though PACK-04 and the research both emphasize rejecting broken references before play (`01-04-PLAN.md:88`, `01-04-PLAN.md:107-118`, `01-RESEARCH.md:228-230`, `01-RESEARCH.md:430-431`).
- `note`: Global venue profiles are a valid choice, but the plan hardens that choice earlier than the research strictly requires for a single-pack phase (`01-01-PLAN.md:113`, `01-RESEARCH.md:354-357`).

## Recommendations

1. Add one explicit sentence to the Phase 1 contract saying `venueRef` resolves against `VenueProfileSource.id`, or else rename/remove `venueId` so there is only one canonical venue key.
2. Freeze `PackSource` and the `roundOrder` reference shape explicitly in 01-01 or 01-02, instead of leaving that decision implicit until implementation.
3. Tighten 01-03 verification by adding one schema-backed authored-content smoke test or a minimal loader invocation once the domain schemas exist, so nested YAML shape mismatches are caught before Plan 04.
4. Extend 01-04 to specify stable diagnostics for broken venue references and path-policy failures, or explicitly document that they reuse a single generalized reference/path error code.
5. Keep the current uncommitted diffs for 01-02, 01-03, and 01-04; they improve the plans overall.
