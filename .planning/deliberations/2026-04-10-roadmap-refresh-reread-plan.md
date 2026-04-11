# Roadmap Refresh Reread Plan

Date: 2026-04-10
Status: completed on 2026-04-11
Purpose: bounded reread and targeted re-roadmap review before starting Phase 1 execution properly

## Why This Exists

The harness patch is done, but that patch mostly improved how planning preserves and propagates future-aware context.

It did **not** perform a full structural re-roadmap from the latest research and audit wave.

What has already changed:

- `PROJECT.md`, `ROADMAP.md`, and `REQUIREMENTS.md` were tightened so they are more future-aware and more referenceable.
- `ROADMAP.md` now includes per-phase canonical refs back to requirement IDs and posture docs.
- `REQUIREMENTS.md` now has stable `SEAM-*` and `DEF-*` anchors.
- discuss/plan/research workflows now preserve future-awareness more rigorously.

What has **not** yet happened:

- no fresh derivation of phase ordering from the recent audit and 2026-04-10 research wave
- no decision yet on whether the roadmap needs only targeted edits or a deeper resequencing
- no insert/remove/reframe pass on roadmap phases driven by the newest findings
- no staleness review of the baseline research canon in `.planning/research/`

Current working judgment:

- no roadmap-shape conclusion should be treated as settled before the bounded reread
- the later pass must allow all of these outcomes:
  - no meaningful roadmap change
  - targeted roadmap refresh
  - material resequencing
  - broader product-approach reframing
  - defer roadmap edits and run another bounded research round first

The point of this plan is to make that decision explicit instead of smuggling in a prior assumption.

## Important Scope Note

This repo uses the local regular GSD harness, not Reflect.

Relevant patch status:

- patched: `discuss-phase`, `plan-phase`, `research-phase`, `discuss-phase-power`, `context.md`, `phase-prompt.md`
- not patched: a `ROADMAP.md` template generator or dedicated roadmapper workflow

Implication:

- this roadmap refresh is a project-doc operation first
- after the refresh, the patched planning harness will consume the improved `PROJECT.md`, `ROADMAP.md`, and `REQUIREMENTS.md`
- if roadmap generation itself later needs system-level changes, that is a separate patch task

## Deliverables For The Later Pass

The later agent should produce:

1. A short decision summary answering:
   - keep current roadmap spine
   - keep spine but modify some phases
   - resequence phases materially
   - insert one or more decimal phases
   - pause and run more research before changing canon
2. A concrete modification plan for:
   - `/.planning/ROADMAP.md`
   - `/.planning/PROJECT.md`
   - `/.planning/REQUIREMENTS.md`
   - `/.planning/research/SUMMARY.md`
   - `/.planning/research/ARCHITECTURE.md`
   - `/.planning/research/FEATURES.md`
   - `/.planning/research/PITFALLS.md`
   - optionally `/.planning/research/STACK.md`
   - optionally `/.planning/STATE.md` if the canonical posture changes materially
3. A short “why” memo listing which research or audit artifacts drove each roadmap change
4. Updates to the live task list in this document
5. If more research is required before editing canon, a short research brief covering:
   - the unresolved question
   - why current evidence is insufficient
   - what exact files or domains should be researched next
   - what decision that research is intended to unlock

## Refresh Outcome (2026-04-11)

### Decision Summary

- Keep the current roadmap spine.
- Apply targeted canonical refreshes rather than a deeper resequencing.
- Insert one decimal phase: `3.1 UI Direction, Design System, And Interaction Contract`.
- Do not run another research round before editing canon.

### Modification Plan Executed

- `/.planning/PROJECT.md`
  - clarified browser-first guest surface, wrapper vocabulary, visibility-state posture, and adopted-vs-open decisions
- `/.planning/ROADMAP.md`
  - kept the private-room spine, inserted Phase `3.1`, and made deployment, join, and TV-legibility obligations explicit
- `/.planning/REQUIREMENTS.md`
  - added `DEPLOY-01` through `DEPLOY-05`, sharpened `SEAM-01`, added `SEAM-05`, widened `OPS-02`, and softened `RET-02`
- `/.planning/research/SUMMARY.md`
  - patched stale hosted-stack wording and marked the older numbered phase sketch as superseded by the refreshed roadmap
- `/.planning/research/ARCHITECTURE.md`
  - appended refresh guidance about deployment parity, wrapper vocabulary, and typed room commands/events
- `/.planning/research/FEATURES.md`
  - appended refresh guidance about browser-first operator flow, QR/link/code join, and later wrapper posture
- `/.planning/research/PITFALLS.md`
  - appended refresh guidance about watchability, staged visibility, and scope restraint as a trust strategy
- `/.planning/research/STACK.md`
  - patched the old managed-platform bias so `Supabase` is optional convenience rather than the canonical hosting posture
- `/.planning/STATE.md`
  - updated current focus and blockers so Phase 1 does not resume against stale guidance

### Why Memo

- `SYNTHESIS.md` and `CONVERGENCE.md` drove the Phase `3.1` UI-contract insertion, the deployment requirement additions, and the need to keep private-room-first while protecting richer seams.
- `2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md` drove the browser-first operator flow, private-host parity, and join-surface updates.
- `2026-04-10-vision-hosting-wave/findings/03-precedents-and-trajectories.md` reinforced QR/link/code join, bounded creator posture, and TV-legibility expectations.
- `2026-04-10-second-wave-scaling-governance/findings/03-public-transition-and-discovery.md` drove the clearer visibility-state and selective-publicness framing.
- `2026-04-10-second-wave-scaling-governance/findings/04-security-trust-and-operational-risk.md` drove the stronger trust-boundary and service-obligation language, especially around keeping public participation deferred.
- `2026-04-10-vision-hosting-wave/findings/01-product-futures.md` and the reflection note drove the wrapper vocabulary refresh and the choice to keep future wrappers explicit without widening v1.

### Phase 1 Validity Check

The current Phase 1 artifacts are still directionally aligned with the refreshed canon, but they are not execution-ready unchanged.

They need a targeted revision pass before execution to absorb:

- the explicit `venue -> circuit -> section -> corner` seam
- venue identity and pack-reference-shape clarification
- remaining validation and diagnostic gaps from the pre-execution audit
- the refreshed deployment and future-wrapper posture now expressed in canon

### Phase 1 Follow-Through (2026-04-11)

The targeted Phase 1 revision pass has now been completed.

- `01-CONTEXT.md` and `01-RESEARCH.md` were refreshed so the phase brief explicitly preserves answer-target lineage and canonical pack-reference expectations.
- `01-01-PLAN.md` and `01-02-PLAN.md` now freeze v1 lineage rules, `VenueProfileSource.id` as the `venueRef` target, and `roundOrder[]` as exact `{ roundId, path }` objects before implementation begins.
- `01-03-PLAN.md` and `01-04-PLAN.md` now call for schema-backed fixture verification and stable diagnostics including `BROKEN_VENUE_REFERENCE`, `UNSAFE_CONTENT_PATH`, and `DUPLICATE_YAML_KEY`.
- Phase 1 is now ready to start at `01-01` without another plan-revision pass unless canon changes again.

## Read Order

The point is to load the minimum high-signal context first and only read deeper if the decision remains unresolved.

### Pass 0: Current Canon

Read these first, in order:

1. `.planning/PROJECT.md`
2. `.planning/ROADMAP.md`
3. `.planning/REQUIREMENTS.md`
4. `.planning/STATE.md`

Why:

- establish the current official posture before letting research pull the repo sideways
- see what was already changed during the harness patch

### Pass 0.5: Active Execution State

Read these next if they exist:

1. `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
2. `.planning/phases/01-authored-round-contract/01-RESEARCH.md`
3. `/.planning/phases/01-authored-round-contract/*-PLAN.md`
4. `.planning/phases/01-authored-round-contract/.continue-here.md`

Why:

- if the roadmap or research canon changes materially, existing Phase 1 artifacts may become stale
- the refresh pass should not assume Phase 1 execution can continue unchanged afterward

### Pass 1: Audit Synthesis

Read these next:

1. `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
2. `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`

Read only if needed afterward:

3. `.planning/audits/2026-04-08-pre-execution-review/lane-4-multi-milestone-vision.md`
4. `.planning/audits/2026-04-08-pre-execution-review/lane-1-plan-quality.md`

Why:

- `SYNTHESIS.md` is the high-signal audit condensation
- `CONVERGENCE.md` is the cross-lane agreement surface
- lane 4 is the most likely follow-up if the issue is roadmap shape rather than plan quality

### Pass 2: Baseline Research Canon

Read these next:

1. `.planning/research/SUMMARY.md`
2. `.planning/research/ARCHITECTURE.md`
3. `.planning/research/FEATURES.md`
4. `.planning/research/PITFALLS.md`

Why:

- `SUMMARY.md` re-establishes the original synthesis used to build the initial roadmap
- `ARCHITECTURE.md` matters if the phase sequence should change around room authority, reconnect, or wrapper seams
- `FEATURES.md` matters if daily/challenge/public surfaces are being over- or under-weighted
- `PITFALLS.md` matters if the roadmap currently bakes in known mistakes

Additional question for this pass:

- which of these files should remain canonical as written, which need edits, and which should instead gain a clear update/superseded note pointing to newer findings

### Pass 3: 2026-04-10 Research Wave

Read these next:

1. `.planning/research/2026-04-10-vision-hosting-wave/findings/01-product-futures.md`
2. `.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`
3. `.planning/research/2026-04-10-vision-hosting-wave/findings/03-precedents-and-trajectories.md`
4. `.planning/research/2026-04-10-second-wave-scaling-governance/findings/03-public-transition-and-discovery.md`
5. `.planning/research/2026-04-10-second-wave-scaling-governance/findings/04-security-trust-and-operational-risk.md`
6. `.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md`

Why:

- these are the most likely files to change roadmap ordering, public/private posture, wrapper sequencing, and hosting assumptions
- the reflections file may already contain a partial synthesis of what the later wave should imply for roadmap posture

### Pass 4: Tie-Breaker Reads Only If Still Unresolved

Read only if the roadmap decision is still ambiguous:

1. `.planning/research/2026-04-10-clean-room-public-transition-xhigh/findings/01-public-transition-and-discovery-clean-room-xhigh.md`
2. `.planning/research/2026-04-10-first-wave-xhigh-comparisons/findings/01-product-futures-xhigh-comparison.md`
3. `.planning/research/2026-04-10-first-wave-xhigh-comparisons/findings/02-hosting-transition-xhigh-comparison.md`
4. `.planning/research/2026-04-10-second-wave-scaling-governance/findings/01-cooperative-scaling-and-p2p-feasibility.md`
5. `.planning/research/2026-04-10-second-wave-scaling-governance/findings/02-funding-access-and-transparency-models.md`

Why:

- these are useful tie-breakers, not the first-line source of truth for the roadmap refresh

## Questions The Later Agent Must Answer

1. Does the current roadmap still reflect the strongest v1 path, or did the recent research materially strengthen a different path?

2. Is the repo still right to keep:
   - live private rooms as the first social wrapper
   - async challenges outside v1
   - public/discovery moves outside the main early roadmap

3. Does Phase 3 still hold too much unresolved runtime risk and deserve:
   - stronger success criteria only
   - more explicit decision criteria
   - or an inserted spike/decision phase before full room authority work

4. Should any of the following move earlier than currently planned:
   - preview / accessibility / participant-device question display ideas
   - frozen challenge or solo practice surfaces
   - bounded custom-pack sharing or trusted creator input

5. Do the current phases already reflect the “watchable private game night” path strongly enough, or are they still too neutral between conflicting futures?

6. Did the audit surface any roadmap smells that the recent doc tightening did not already address?

7. Are there unresolved framing or sequencing questions where current evidence is too thin to justify roadmap edits yet?

8. If uncertainty remains, is it acceptable planning uncertainty or unacceptable roadmap-shaping uncertainty?

## Uncertainty Triage

The later agent should classify major unresolved points into one of two buckets.

### Acceptable Uncertainty

These do not block roadmap refresh on their own:

- implementation-detail uncertainty inside a phase whose boundary remains sound
- tool/runtime uncertainty where the roadmap already keeps the decision open intentionally
- uncertainty about distant public or retention surfaces that are explicitly outside the current roadmap spine
- uncertainty that can be safely preserved as an open decision, protected seam, or explicit deferral

### Unacceptable Uncertainty

These should block roadmap edits and trigger another bounded research round:

- uncertainty about the actual v1 product spine, not just phase wording
- uncertainty about whether live private rooms, frozen challenges, or another wrapper should be the first real proving surface
- uncertainty about whether current Phase 1 assumptions would force a later rewrite if the stronger product path is different
- uncertainty where the audit and newer research materially conflict and the repo has no justified basis for choosing
- uncertainty that would make roadmap edits look precise while still resting on guesswork

If uncertainty lands in this second bucket, the correct output is not “best guess roadmap edits.” The correct output is “pause, research this next.”

## Candidate Modification Types To Consider

These are hypotheses to evaluate, not pre-approved changes:

### Type A: Keep the spine, sharpen the wording

Examples:

- refine overview/open-decisions language
- tighten phase goals or success criteria
- sharpen `Canonical refs`, `Protects`, `Does not decide yet`, `Assumed posture`

### Type B: Keep the spine, add one or more decimal phases

Examples to test:

- `2.1` or `3.1` runtime-decision / room-authority spike if Phase 3 still hides too much risk
- `5.1` or `6.1` frozen challenge / solo practice insertion if research says wrapper reuse should be proven earlier
- later bounded creator/share phase if custom-pack sharing should appear before broader public moves

### Type C: Resequence existing phases

Only if the reread strongly supports it.

Examples to test:

- whether reconnect/durability belongs earlier relative to calibration
- whether some host-screen/watchability work should land earlier than current Phase 5

### Type D: Broaden or narrow the roadmap horizon

Examples:

- keep public transition entirely off-roadmap and only in posture docs
- or explicitly add later-phase placeholders if the newer research makes that necessary

### Type E: Pause For More Research Before Editing Canon

Examples to test:

- wrapper ordering still unclear after the bounded reread
- public/private framing implications are still too ambiguous
- baseline research canon and later research wave materially disagree on a roadmap-shaping point
- current evidence cannot justify whether to preserve, insert, resequence, or reframe

## Approach Rules For The Later Agent

1. Do not read every file in every research directory.
2. Start with the pass order above and stop descending when the decision is already clear enough.
3. Separate:
   - v1 roadmap changes
   - long-term posture clarifications
   - speculative future opportunities
4. Do not let public-transition research silently override the repo’s present private-first stance unless the evidence clearly justifies it.
5. If the strongest conclusion is “the current roadmap is basically right,” say that directly and keep edits narrow.
6. If an insertion is proposed, justify:
   - why the current phase sequence is insufficient
   - what exact decision or risk the insertion resolves
   - why that work cannot simply be folded into an existing phase
7. If the latest research materially changes product posture, decide whether current Phase 1 plans should be revised or invalidated before execution.
8. If baseline research docs are stale, do not keep using them silently as canonical input.
9. If another research round is required, keep it bounded and decision-oriented rather than reopening the whole domain.

## Files Most Likely To Be Modified

- `.planning/ROADMAP.md`
- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/research/SUMMARY.md`
- `.planning/research/ARCHITECTURE.md`
- `.planning/research/FEATURES.md`
- `.planning/research/PITFALLS.md`
- optionally `.planning/STATE.md`

Potentially useful for reference only, not likely edit targets:

- `.planning/deliberations/2026-04-10-future-awareness-harness-patch.md`
- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/SUMMARY.md`
- `AGENTS.md` unless the repo’s orchestration or model-policy guidance itself needs to change
- `discovery/14-gsd-seed.md` unless the roadmap refresh turns into a true project re-initialization posture change

## Research Canon Staleness Check

The baseline research files in `.planning/research/` are not disposable notes. They are still used as canonical inputs and are referenced directly by current project docs.

Observed reasons to treat them as potentially stale:

- `REQUIREMENTS.md` motivations still point into `.planning/research/SUMMARY.md`, `FEATURES.md`, and `PITFALLS.md`
- the audit synthesis introduced structural findings that were not obviously folded back into all baseline research files
- the 2026-04-10 wave added future-wrapper, hosting-transition, public-transition, and governance material that may materially refine the old canon

For each of these files:

- `.planning/research/SUMMARY.md`
- `.planning/research/ARCHITECTURE.md`
- `.planning/research/FEATURES.md`
- `.planning/research/PITFALLS.md`
- `.planning/research/STACK.md`

the later agent should choose one status:

- keep as-is
- patch in place
- append an update note that points to newer findings
- or regenerate/supersede if the older framing is no longer trustworthy

Do not leave them silently stale if roadmap or requirements are refreshed against newer evidence.

## Downstream Consumer Check

If the roadmap refresh or research-canon refresh changes project posture materially, review these downstream consumers before Phase 1 execution resumes:

- `.planning/STATE.md` — current focus or recent decisions may be stale
- `.planning/phases/01-authored-round-contract/*` — plans and context may no longer match canon
- `.codex/get-shit-done/templates/claude-md.md` — references stack/architecture sources for generated guidance
- requirement motivation anchors in `REQUIREMENTS.md` that would break if research sections are rewritten

This does not mean all of them must be edited. It means they must be checked explicitly.

## If Another Research Round Is Needed

The follow-up should be small and targeted.

Rules:

- research only the unresolved decision, not the whole project again
- define the exact decision to unlock before starting
- state why the current audit/research corpus is insufficient
- write findings so they can directly support either roadmap edits or a justified “still defer” decision

Good examples:

- wrapper-ordering question: live private rooms first vs frozen async challenge first
- phase-sequencing question: whether room-runtime risk needs a dedicated spike before current Phase 3
- framing question: whether the repo’s v1 posture is still best framed as watchable private game night or whether another emotional center is now better supported

## Live Task List

The later agent should update this section as decisions firm up.

- [x] Re-read Pass 0 files
- [x] Re-read Pass 0.5 active execution-state files
- [x] Re-read audit synthesis/convergence
- [x] Re-read baseline research canon
- [x] Re-read targeted 2026-04-10 findings
- [x] Classify remaining uncertainty as acceptable or unacceptable
- [x] Decide whether roadmap needs: wording-only changes, insertions, resequencing, reframing, no structural changes, or another research round first
- [x] Decide baseline research-canon status for `SUMMARY.md`, `ARCHITECTURE.md`, `FEATURES.md`, `PITFALLS.md`, and `STACK.md`
- [x] Write a short “roadmap decision summary” before editing docs
- [x] Confirm another research round is not required before canon edits
- [x] Update `ROADMAP.md`
- [x] Update `PROJECT.md` if product posture needs correction
- [x] Update `REQUIREMENTS.md` if new anchors or deferrals are needed
- [x] Update baseline research docs or mark them as superseded/updated if needed
- [x] Check whether current Phase 1 artifacts are still valid after the refresh
- [x] Update `STATE.md` if current focus, posture, or decision history changed materially
- [x] Update this task list with any emergent tasks discovered during reread
- [x] Verify the edited docs still agree with each other

### Emergent Tasks

Add new items here during the later pass instead of relying on memory.

- [x] Revise the Phase 1 plans before execution so they match the refreshed canon on answer-target hierarchy, venue identity/reference shape, pack reference shape, and validation diagnostics.

## Stop Conditions

Stop and hand back to the user if:

- the reread implies a major product-direction change rather than a roadmap refinement
- the strongest conclusion would invalidate the current Phase 1 scope entirely
- multiple conflicting future paths remain plausible and cannot be narrowed without fresh user preference input

## Completion Criteria

This plan is complete when a later agent can:

- clear context safely
- follow the read list without hunting for files
- make a concrete roadmap-refresh decision
- edit the right project docs
- and then return to proper Phase 1 planning/execution with the patched harness consuming sharper canon
