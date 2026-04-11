---
deliberation: 2026-04-11-long-arc-canon-and-harness-plan
created: 2026-04-11T04:43:28-04:00
status: proposed
type: implementation-plan
scope: Canonize the long-arc strategy posture in a dedicated planning artifact, integrate that artifact into the repo-local GSD planning chain, and prepare the project for a clean Phase 1 replanning pass against the clarified canon.
related_documents:
  - ../../PROJECT.md
  - ../../ROADMAP.md
  - ../../REQUIREMENTS.md
  - ../../STATE.md
  - ../2026-04-10-roadmap-refresh-reread-plan.md
  - ../2026-04-10-future-awareness-harness-patch.md
  - ../2026-04-11-canon-refresh-change-justification.md
  - JUSTIFICATION.md
---

# Long-Arc Canon And Harness Integration Plan

## Why This Exists

The repo now has enough future-facing thinking to guide execution, but that thinking is still distributed across:

- canon files
- audit synthesis
- multiple research lanes
- exploration logs and checkpoints
- workflow-patch deliberations

That is strong raw material, but weak canon transmission.

The goal of this plan is to:

1. ratify one durable long-arc strategy artifact
2. wire that artifact into the existing canon instead of letting it float as background reading
3. integrate it into the repo-local GSD workflow with the lightest patch that makes downstream propagation reliable
4. stop Phase 1 replanning from starting until that clarified canon exists

## Scope Boundary

This plan is intentionally about:

- long-arc canonization
- milestone-to-milestone transition doctrine
- harness propagation
- verification and diagnostics

This plan is not:

- a Phase 1 execution plan
- a rewrite of the current milestone roadmap
- a decision to build public features now
- a commitment to paid access, public community governance, or peer-to-peer room authority

## Outcome We Want

After this plan lands, the repo should have:

- one concise canonical long-arc strategy document
- a clear pointer from `PROJECT.md` to that document
- `ROADMAP.md` phase refs that deliberately pull the strategy doc into all phases where it matters
- `REQUIREMENTS.md` left unchanged in this pass, with any required doctrinal promotion deferred to a later explicit follow-up
- repo-local GSD discuss flow that reads the strategy doc automatically when it exists
- downstream research and planning continuing to consume the strategy doc through the existing `canonical_refs` mechanism
- a clean basis for rerunning `discuss-phase 1`

## Proposed Deliverables

### Canon Deliverables

- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md` update
- `.planning/ROADMAP.md` update
- `.planning/STATE.md` update

### Harness Deliverables

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-power.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md`
- `tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md`
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`

### Reasoning / Audit Deliverables

- this plan
- the paired justification sidecar

## Execution Profile

This plan should be executed as a deterministic canon-and-tooling pass, not as an exploratory writing session.

Default rule:

- if a choice is not explicitly authorized below, do not improvise it

## Allowed Write Set

The implementation pass is allowed to modify only these files:

- `.planning/config.json` verification target only; do not edit in this pass
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-power.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md`
- `tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md`
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`

The implementation pass may also update the live repo-local runtime only by rerunning:

- `./scripts/setup-portable-gsd.sh`

after the overlay files above are edited.

## Forbidden Write Set

Do not modify any of the following during this pass:

- `.planning/REQUIREMENTS.md`
- `.planning/phases/**`
- `.planning/research/**`
- `.planning/audits/**`
- `.planning/explore/**`
- `.codex/**` by hand
- any application source code

If implementation reveals that `REQUIREMENTS.md` truly must change, stop and create a follow-up note instead of expanding this pass.

## Non-Discretion Rules

1. Do not rewrite milestone shape in `ROADMAP.md`.
2. Do not rename phases.
3. Do not change requirement-to-phase mappings.
4. Do not add new requirements in this pass.
5. Do not run a fresh `gsd-discuss-phase 1` automatically as part of implementation, because that mutates live Phase 1 artifacts.
6. Do not hand-edit the live `.codex/` runtime copy. Patch the tracked overlay, then rerun `./scripts/setup-portable-gsd.sh`.
7. If a planned change would require touching files outside the allowed write set, stop and record the blocker in a short note appended to `JUSTIFICATION.md`.

## Bounded Decision Authority

The implementing model is allowed to make local decisions only inside the bounded spaces below.

When choosing among allowed options, apply this priority order:

1. preserve canon consistency
2. preserve current milestone scope
3. minimize file churn
4. prefer additive edits over rewrites
5. prefer reusable generic workflow wording over repo-specific hardcoding
6. prefer stopping and documenting a blocker over speculative expansion

### Allowed Decision Windows

#### Decision Window A: Exact wording inside `.planning/LONG-ARC.md`

Allowed discretion:

- choose phrasing
- choose paragraph versus bullet form
- choose how to compress evidence-backed doctrine into concise canon language

Not allowed:

- changing the required doctrine points
- introducing new roadmap work
- inventing new requirement IDs

Choose the wording that is clearest, shortest, and most reusable as a cited doctrine source.

#### Decision Window B: Exact insertion point in `PROJECT.md`

Preferred location:

- immediately after the `Milestone Arc` introduction

Fallback location if that paragraph has drifted:

- immediately before `## How The Long Arc Constrains v1`

Do not insert the pointer anywhere else unless both anchor locations are absent.

#### Decision Window C: Exact `ROADMAP.md` bullet wording

Allowed discretion:

- choose one shared explanatory phrase for the `.planning/LONG-ARC.md` canonical-ref bullet

Required outcome:

- all phases cite the same long-arc doctrine with only minor local adaptation

Preferred interpretation:

- the doc defines long-arc product, visibility, hosting, support, and future-wrapper doctrine that current work must preserve without widening scope

#### Decision Window D: Exact `STATE.md` insertion location

Preferred location:

- a current-status, recent-decisions, or active-guidance section

Fallback:

- the closest section that influences the next planning action

Do not create a large new section if an existing status section can carry the note.

#### Decision Window E: `discuss-phase` patch strategy

The implementing model may choose between these two implementation patterns:

1. add explicit conditional loading of `.planning/LONG-ARC.md` during prior-context gathering and future-awareness derivation
2. add explicit mention during future-awareness derivation and canonical-ref accumulation if the workflow structure makes a single prior-context load point awkward

Choose option 1 if feasible without broad surgery.
Choose option 2 only if option 1 would require disproportionate workflow restructuring.

#### Decision Window F: Contradiction cleanup in `ROADMAP.md`

If adding `.planning/LONG-ARC.md` exposes a direct contradiction in `Protects`, `Does not decide yet`, or `Assumed posture`, the implementing model may tighten only that local text.

A valid contradiction is one of:

- current text implies a publicness posture the new doctrine explicitly rejects
- current text implies a hosting path the new doctrine explicitly rejects
- current text implies future scope import that the new doctrine explicitly defers

If the contradiction is broader than one local phase note, stop and document it instead of rewriting the roadmap.

## Stop Conditions

Stop the implementation pass and append a blocker note to `JUSTIFICATION.md` if any of the following occur:

1. `.planning/LONG-ARC.md` would require adding new requirement IDs to be intelligible
2. `PROJECT.md` pointer placement requires structural rewrite rather than a local addition
3. `ROADMAP.md` needs changes outside `Canonical refs`, `Protects`, `Does not decide yet`, or `Assumed posture`
4. `STATE.md` cannot carry the note without materially redefining execution posture
5. the overlay patch would require touching additional workflows beyond standard discuss, power discuss, assumptions discuss, or quick `--discuss`
6. a verify-only consumer path proves it would still drop `.planning/LONG-ARC.md` after the upstream patches
7. `./scripts/setup-portable-gsd.sh` fails

## Execution Order

The implementation pass must follow this exact order:

1. Run config preflight
2. Run harness surface coverage audit
3. Create `.planning/LONG-ARC.md`
4. Patch `.planning/PROJECT.md`
5. Patch `.planning/ROADMAP.md`
6. Patch `.planning/STATE.md`
7. Patch the overlay files
8. Run `./scripts/setup-portable-gsd.sh`
9. Run verification commands
10. Stop

Do not reorder these steps.

## File-By-File Change Spec

## Execution Checklist

Maintain this checklist in-place while executing the plan.

Rules:

1. Mark each item complete immediately after it is actually finished, not before.
2. If execution pauses, leave the checklist in its true current state.
3. If a stop condition is hit, mark the relevant item as blocked and append a short blocker note under `Execution Notes`.
4. If compaction or session reset happens, this checklist is the first recovery surface to read.
5. Do not delete checklist items even if they become blocked; preserve the execution trail.

### Checklist

- [ ] Step 0 complete: config preflight read and current local mode recorded
- [ ] Step 0.5 complete: harness surface coverage audit performed and all required surfaces classified
- [ ] Step 1 complete: `.planning/LONG-ARC.md` created
- [ ] Step 2 complete: `.planning/PROJECT.md` patched
- [ ] Step 3 complete: `.planning/ROADMAP.md` patched
- [ ] Step 4 complete: `.planning/STATE.md` patched
- [ ] Step 5A complete: `discuss-phase.md` patched
- [ ] Step 5B complete: `discuss-phase-power.md` patched
- [ ] Step 5C complete: `discuss-phase-assumptions.md` overlay created and patched
- [ ] Step 5D complete: `quick.md` overlay created and patched
- [ ] Step 5E complete: `gsd-discuss-phase` skill guidance patched
- [ ] Step 5F complete: `context.md` template guidance patched
- [ ] Step 5G complete: verify-only consumer surfaces checked
- [ ] Step 6 complete: `./scripts/setup-portable-gsd.sh` run successfully
- [ ] Step 7 complete: all verification commands run and reviewed
- [ ] Final review complete: allowed write set respected and no stop condition was triggered

## Execution Notes

Use this section as the live execution ledger.

Required update behavior:

- append one short note after each completed major step
- include the date or timestamp if the work spans multiple sessions
- record blocker notes here if a stop condition is hit
- record any bounded-decision choice here when more than one allowed option existed

Suggested note format:

- `2026-04-11T00:00:00-04:00 — Step 0 complete. Local config confirms discuss_mode=exploratory.`
- `2026-04-11T00:05:00-04:00 — Step 5D complete. Created overlay quick.md from current .codex quick workflow and patched only --discuss path.`

## Step 0: Config Preflight

### Required Read

Read:

- `.planning/config.json`

### Required Extraction

Capture at minimum:

- `workflow.discuss_mode`
- `workflow.skip_discuss`
- `workflow.research_before_questions`
- `workflow.ui_phase`
- `workflow.ui_safety_gate`

### Required Interpretation

Treat the extracted config as authoritative for this repo.

The implementing model must explicitly determine:

- whether the repo is currently running `exploratory`, `discuss`, or `assumptions` mode
- whether discuss is enabled
- which context-producing surfaces are active today versus merely latent

### Step 0 Acceptance Criteria

- the current local discuss mode is explicitly recorded during implementation
- patch choices are tied to actual local config, not generic GSD assumptions

## Step 0.5: Harness Surface Coverage Audit

### Purpose

Before editing anything, enumerate every relevant local path by which long-arc doctrine could enter or fail to enter `CONTEXT.md`, quick-context, research, or planning flows.

### Required Surface List

The implementing model must classify each of these as `patch now`, `verify only`, or `out of scope`:

1. standard discuss workflow
2. power discuss workflow
3. assumptions discuss workflow
4. quick workflow with `--discuss`
5. plan-phase standard `CONTEXT.md` consumption
6. research-phase standard `CONTEXT.md` consumption
7. plan-phase PRD express path

### Required Classification Outcome

Use this target classification:

- standard discuss: `patch now`
- power discuss: `patch now`
- assumptions discuss: `patch now`
- quick `--discuss`: `patch now`
- plan-phase standard consumption: `verify only`
- research-phase standard consumption: `verify only`
- PRD express path: `verify only`

### Audit Rule

If a new local `CONTEXT.md` producer or consumer is discovered, add it to this classification before proceeding.

### Step 0.5 Acceptance Criteria

- all seven required surfaces were explicitly considered
- no active local context-producing surface was silently omitted

## Step 1: Create `.planning/LONG-ARC.md`

### Purpose

Create one canon-adjacent strategy artifact that ratifies the long-arc doctrine without turning every future possibility into a present-tense requirement.

### Required Frontmatter

The new file must contain frontmatter with at least:

- `document`
- `created`
- `status`
- `type`
- `scope`
- `related_documents`

### Required Headings

Use these exact top-level headings, in this exact order:

1. `Why This Exists`
2. `Current Product Center`
3. `Mature Product Hypothesis`
4. `Milestone Arc`
5. `Transition Doctrine`
6. `Visibility And Discovery Ladder`
7. `Hosting And Scaling Ladder`
8. `Support, Access, And Contribution Doctrine`
9. `Streamer And Spectator Doctrine`
10. `Protected Bets For This Milestone`
11. `Explicit Deferrals`
12. `What Changes Would Reopen This Doctrine`

Do not add extra top-level headings in this first pass.

### Required Content

The file must explicitly state all of the following:

- the current product center is a private, watchable, host-led, browser-first F1 game-night ritual
- the mature shape is best understood as an authored F1 substrate plus multiple possible wrappers
- Milestone 1 proves the private ritual and protects later wrappers without importing them
- visibility/publicness is staged and surface-specific
- self-hostable authoritative rooms are the primary branch to preserve
- support, access, and service obligation are distinct concepts
- streamer-friendliness first means watchability, role clarity, code safety, and spectator seams
- full peer-to-peer room authority is not the primary path
- public live participation, paid guaranteed access, open creator marketplace, and broad community-host governance remain deferred

The file must keep these future surfaces explicitly alive but uncommitted:

- async challenge
- solo support shell
- spectator or streamer-adjacent shell
- broader F1 party platform expansion

### Style Constraints

- strategic, not speculative sprawl
- stable enough to cite phase by phase
- short enough that discuss-phase can load it without turning planning into research replay
- target length: roughly 900-1800 words
- no implementation tasks
- no roadmap renumbering
- no requirement IDs invented inside this doc

### Source Priority Rule For `.planning/LONG-ARC.md`

When doctrine wording must choose between sources, use this precedence order:

1. current canon (`PROJECT.md`, `ROADMAP.md`, `REQUIREMENTS.md`, `STATE.md`)
2. audit synthesis (`SYNTHESIS.md`, `CONVERGENCE.md`)
3. latest research lanes
4. exploration logs, checkpoints, and reflections

Use lower-priority sources to sharpen or interpret, not to silently overrule higher-priority canon.

### Step 1 Acceptance Criteria

- `.planning/LONG-ARC.md` exists
- it uses the required headings in the required order
- it contains the required doctrine statements above
- it does not create new requirement IDs

## Step 2: Patch `PROJECT.md`

### Allowed Change Scope

- add one concise pointer to `.planning/LONG-ARC.md`
- optionally add one short sentence clarifying that `PROJECT.md` is the concise identity/milestone arc and `LONG-ARC.md` is the detailed transition doctrine

### Required Insertion Behavior

Insert the pointer in the area where a reader looking for the milestone arc will find it naturally.

Use the bounded-decision insertion rule above.

Do not rewrite these sections in this pass:

- `What This Is`
- `Core Value`
- `Requirements`
- `Out of Scope`
- `Constraints`
- `Key Decisions`
- `Open Questions`

### Step 2 Acceptance Criteria

- `PROJECT.md` references `.planning/LONG-ARC.md`
- the reference makes the document split explicit
- no unrelated section was rewritten

## Step 3: Patch `ROADMAP.md`

### Allowed Change Scope

- add `.planning/LONG-ARC.md` to each phase’s `Canonical refs`
- make only minimal text-tightening changes where needed to remove contradiction with the new doctrine

### Required Change

For phases `1`, `2`, `3`, `3.1`, `4`, `5`, `6`, and `7`:

- add a `Canonical refs` bullet for `.planning/LONG-ARC.md`

Use one consistent explanation for that bullet across phases, adapted only if needed for local fit, following Decision Window C above.

### Forbidden Change Scope

Do not change:

- phase numbers
- phase names
- phase ordering
- success criteria
- requirement lists
- progress table

unless the file would otherwise directly contradict `.planning/LONG-ARC.md`. If such a contradiction appears, stop and record it instead of improvising a roadmap rewrite.

### Step 3 Acceptance Criteria

- each current milestone phase cites `.planning/LONG-ARC.md` in `Canonical refs`
- no phase numbering or requirements mapping changed
- no success criteria were rewritten beyond contradiction cleanup

## Step 4: Patch `STATE.md`

### Required Change

Add one brief state note that:

- `.planning/LONG-ARC.md` is now canonical long-arc guidance
- future-aware discuss/planning should cite it
- Phase 1 replanning should consume it before fresh planning artifacts are treated as authoritative

Use the bounded-decision insertion rule above.

### Forbidden Change Scope

Do not otherwise reinterpret project status or phase readiness in this pass.

### Step 4 Acceptance Criteria

- `STATE.md` mentions `.planning/LONG-ARC.md`
- no new execution claims or replanning claims are introduced beyond the intended note

## Step 5: Patch Overlay Files

Patch only these tracked overlay files:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-power.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md`
- `tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md`
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`

## Step 5A: Patch `discuss-phase.md`

### Search Anchors

Look for these existing concepts before editing:

- prior context loading
- `Derive future awareness`
- `Canonical refs`

Prefer local edits near those existing anchors rather than adding a new detached section.

### Required Behavior Changes

1. When `.planning/LONG-ARC.md` exists, it should be treated as prior context during steering.
2. When deriving future awareness, the workflow should consider `.planning/LONG-ARC.md` a first-class input.
3. When generating `canonical_refs`, the workflow should preserve `.planning/LONG-ARC.md` when it materially constrains the phase.

### Forbidden Behavior Changes

Do not:

- make `.planning/LONG-ARC.md` mandatory for repos that do not have it
- change the overall discuss flow
- change phase boundary rules
- add new interactive questions just because the doc exists

### Step 5A Acceptance Criteria

- the workflow text explicitly mentions `.planning/LONG-ARC.md` conditionally
- the logic is conditional on file existence
- no broad workflow redesign is introduced

## Step 5B: Patch `discuss-phase-power.md`

### Why This Is In Scope

`discuss-phase-power.md` is another `CONTEXT.md` producer. Leaving it untouched would create a real propagation gap whenever `--power` is used.

### Search Anchors

Look for:

- `Load prior context (PROJECT.md, REQUIREMENTS.md, STATE.md, prior CONTEXT.md files)`
- references to generated `canonical_refs`
- references to `future_awareness`

### Required Behavior Changes

1. When `.planning/LONG-ARC.md` exists, power mode should treat it as prior context.
2. Power mode should preserve the same long-arc doctrine into generated `canonical_refs`.
3. Power mode should not lag behind standard discuss mode on future-awareness doctrine inputs.

### Forbidden Behavior Changes

Do not:

- redesign the JSON or HTML state format
- add new question categories solely because `.planning/LONG-ARC.md` exists
- make power mode stricter than standard discuss mode

### Step 5B Acceptance Criteria

- power mode now mentions `.planning/LONG-ARC.md` conditionally
- power mode preserves doctrine parity with standard discuss mode
- no HTML/JSON format churn was introduced

## Step 5C: Patch `discuss-phase-assumptions.md`

### Why This Is In Scope

Assumptions mode is a real local `CONTEXT.md` producer, even if it is not the current default mode.

### Implementation Method

There is no tracked overlay file for this workflow today.

The implementing model must:

1. create `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md`
2. seed it from the current live repo-local source:
   - `.codex/get-shit-done/workflows/discuss-phase-assumptions.md`
3. apply only the minimum edits needed to give assumptions mode long-arc parity with standard discuss mode

### Search Anchors

Look for:

- project-level file loading
- prior context loading
- `canonical_refs`
- `future_awareness`

### Required Behavior Changes

1. When `.planning/LONG-ARC.md` exists, assumptions mode should read it during prior-context loading.
2. Assumptions mode should preserve the doctrine into generated `canonical_refs` when relevant.
3. Assumptions mode should not lag standard discuss mode on long-arc future-awareness inputs.

### Forbidden Behavior Changes

Do not:

- redesign assumptions mode philosophy
- increase user questioning
- rewrite unrelated assumption-analysis logic

### Step 5C Acceptance Criteria

- a tracked overlay copy now exists
- the overlay copy is seeded from the current live workflow, not invented from scratch
- assumptions mode now conditionally includes `.planning/LONG-ARC.md`

## Step 5D: Patch `quick.md` For `--discuss`

### Why This Is In Scope

Quick mode with `--discuss` is a real local context-producing workflow, and leaving it untouched would preserve a known gap.

### Implementation Method

There is no tracked overlay file for quick workflow today.

The implementing model must:

1. create `tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md`
2. seed it from the current live repo-local source:
   - `.codex/get-shit-done/workflows/quick.md`
3. patch only the `--discuss`-relevant parts

### Search Anchors

Look for:

- `Write CONTEXT.md`
- `canonical_refs`
- quick research `<files_to_read>`
- quick planning `<files_to_read>`

### Required Behavior Changes

1. When quick mode is used with `--discuss` and `.planning/LONG-ARC.md` exists, the quick context path should be able to include it in `canonical_refs`.
2. Quick research and quick planning should preserve that context path when present.
3. Quick mode should not silently lag the main discuss path on long-arc doctrine when `--discuss` is active.

### Forbidden Behavior Changes

Do not:

- redesign quick mode
- add phase-style complexity to non-discuss quick tasks
- force doctrine refs into quick tasks that had no discuss context or no relevant external docs

### Step 5D Acceptance Criteria

- a tracked overlay copy now exists
- the overlay copy is seeded from the current live workflow
- quick `--discuss` can preserve `.planning/LONG-ARC.md` in its context path when relevant

## Step 5E: Patch `gsd-discuss-phase` Skill Guidance

### Search Anchor

Look for the current summary bullet that says:

- `Load prior context (PROJECT.md, REQUIREMENTS.md, STATE.md, prior CONTEXT.md files)`

Patch that guidance locally instead of rewriting the whole skill.

### Required Change

Update the skill guidance so “load prior context” no longer implies that only `PROJECT.md`, `REQUIREMENTS.md`, and `STATE.md` matter.

The guidance should mention the long-arc doctrine file conditionally when present.

### Step 5E Acceptance Criteria

- the skill text now reflects the actual intended prior-context set
- the wording remains generic enough to stay repo-local and maintainable

## Step 5F: Patch `context.md` Template Guidance

### Search Anchors

Look for:

- the `Canonical References` section
- explanatory notes near `canonical_refs`
- any guidance about source-of-truth files or doctrine docs

Patch those local notes instead of restructuring the template.

### Required Change

Add or strengthen guidance that durable doctrine docs like `.planning/LONG-ARC.md` belong in `canonical_refs` when they actively constrain the phase.

### Forbidden Change

Do not hardcode `.planning/LONG-ARC.md` as a universal requirement in the template.

### Step 5F Acceptance Criteria

- the template now teaches inclusion of doctrine docs when relevant
- the template still works for repos that do not have this file

## Step 5G: Verify Consumer Surfaces Without Patching Them

### Required Verification Targets

Verify only:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`
- the PRD express path section in `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`

### Required Conclusion

Confirm that these remain consumer paths fed by:

- `ROADMAP.md` canonical refs
- generated `CONTEXT.md` canonical refs

Do not patch them in this pass unless the audit proves they would still drop `.planning/LONG-ARC.md` after the upstream changes.

## Step 6: Refresh The Live Repo-Local Runtime

Run:

- `./scripts/setup-portable-gsd.sh`

This is the only approved way to propagate overlay edits into `.codex/`.

### Step 6 Acceptance Criteria

- the script completes successfully
- the corresponding `.codex/` files now reflect the overlay edits

## Step 7: Verification

Run these exact checks:

1. `git diff --check`
2. `rg -n "LONG-ARC.md" .planning/PROJECT.md .planning/ROADMAP.md .planning/STATE.md tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
3. `rg -n "LONG-ARC.md" tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-power.md`
4. `rg -n "LONG-ARC.md" tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md`
5. `rg -n "LONG-ARC.md" .codex/get-shit-done/workflows/discuss-phase.md .codex/get-shit-done/workflows/discuss-phase-power.md .codex/get-shit-done/workflows/discuss-phase-assumptions.md .codex/get-shit-done/workflows/quick.md .codex/skills/gsd-discuss-phase/SKILL.md .codex/get-shit-done/templates/context.md`
6. `git status --short --untracked-files=all`

### Expected Verification Outcome

Acceptable result:

- only the allowed write-set files are modified or newly created

Unacceptable result:

- any modified file outside the allowed write set
- any hand-edited `.codex/**` file before the setup script rerun

### Verification Stop Rule

Do not run `gsd-discuss-phase 1 --auto` in the same pass unless the user explicitly asks for that next step after reviewing the canon/tooling changes.

## Diagnostics If Something Fails

If a verification step fails, inspect in this order:

1. `.planning/LONG-ARC.md`
2. `.planning/ROADMAP.md`
3. `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
4. `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-power.md`
5. `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md`
6. `tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md`
7. `tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md`
8. `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
9. the refreshed `.codex/` copies created by `setup-portable-gsd.sh`

If the failure would require expanding scope beyond the allowed write set, stop and document the blocker in `JUSTIFICATION.md` rather than improvising a larger patch.

## Commit Strategy

Recommended commit split:

1. `planning: canonize long-arc strategy doctrine`
   - `.planning/LONG-ARC.md`
   - `PROJECT.md`
   - `ROADMAP.md`
   - `STATE.md`

2. `tooling: load long-arc doctrine in discuss-phase`
   - overlay skill/workflow/template files, including standard discuss, power, assumptions, and quick-discuss parity

3. optional `tooling: refresh repo-local GSD runtime` only if you want the setup-script rerun represented distinctly

Do not bundle unrelated planning changes into these commits.

## Explicit Non-Goals

This plan does not itself authorize:

- Phase 1 implementation
- a broader roadmap rewrite
- new public-facing product commitments
- monetization changes
- public repo publication
- streamer integration work
- requirements expansion
- fresh phase-artifact generation

## Completion Criteria

This plan should be considered successfully consumed only when all of the following are true:

- `.planning/LONG-ARC.md` exists and is linked from canon
- all eight current milestone phases can cite the long-arc doctrine where relevant
- the repo-local discuss flow loads the doctrine automatically when present
- standard discuss, power discuss, assumptions discuss, and quick `--discuss` all preserve the doctrine
- the doctrine propagates into `CONTEXT.md` via `canonical_refs` and `future_awareness`
- the project has a cleaner basis for rerunning Phase 1 planning than it has now
- no files outside the allowed write set were modified

## Next Action After This Plan

If this plan is accepted, the next artifact to consume is:

- `.planning/deliberations/2026-04-11-long-arc-canonization/JUSTIFICATION.md`

That sidecar should be treated as the evidence and diagnosis companion for the implementation pass.
