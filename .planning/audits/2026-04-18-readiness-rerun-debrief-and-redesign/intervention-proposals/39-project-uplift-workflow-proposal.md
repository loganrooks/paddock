Date: 2026-04-21
Status: active workflow proposal

# Project Uplift Workflow Proposal

## Purpose

- [g:r:i] This proposal turns the revised entry/uplift terrain in `37` and the stronger carrier-placement map in `38` into one bounded composition-layer workflow.
- [g:r:i] The target is not generic onboarding. The target is one explicit owned path for taking an existing project whose posture has thinned or aged and bringing runtime/install truth, governing posture, planning doctrine, and durable uplift memory into stronger alignment.

## Why This Workflow Now

- [e:c+i] `37` now maps the widened family directly: creation, milestone opening, docs bootstrap/merge, re-entry, repair, update, migration, workspace/worktree entry, phase-injection entry, installer rerun, governing-posture install, split uplift families, forensics entry, archived-milestone re-entry, and audit-subtree aging all now sit in one terrain map. Source: [37-entry-surface-and-project-uplift-map.md](./37-entry-surface-and-project-uplift-map.md:1).
- [e:c+i] `38` now records strongest placement for that family: runtime/install, governing-doc, required-reading, claim-type, long-horizon, state-boundary, discovery, cross-runtime, tooling, audit-aging, and uplift-output concerns are all mapped to primary carriers, supporting carriers, and non-owners. Source: [38-entry-surface-concern-and-carrier-placement-map.md](./38-entry-surface-concern-and-carrier-placement-map.md:1).
- [d:r:i] Those two artifacts are enough to define a workflow owner cleanly. What is still missing is the workflow shape itself.

## Working Handle

- [d:r:i] Preferred working handle: `gsd-uplift-project`
- [d:r:i] Alternate handle kept seeded: `gsd-upgrade-project`
- [d:r:i] This proposal uses `gsd-uplift-project` because the family is broader than version upgrade alone.

## Workflow Objective

- [d:r:i] The workflow should do four things well:
  1. detect when a project deserves uplift as its own action rather than silent continuation
  2. gather the right evidence from specialist owners without absorbing them
  3. refresh the strongest subset of repo-local carriers in one coherent pass
  4. write durable uplift memory and route the operator to the correct next action

## Ownership Boundary

### What This Workflow Should Own

- [d:r:i] posture detection for existing projects
- [d:r:i] composition of evidence from runtime/install, structural health, governing-doc posture, long-horizon posture, and repo-local tooling posture
- [d:r:i] compact refresh of the strongest first-slice carrier set
- [d:r:i] durable uplift outputs and routing

### What This Workflow Should Not Absorb

- [d:r:i] `new-project` creation flow
- [d:r:i] `new-milestone` milestone-opening flow
- [d:r:i] `ingest-docs` docs bootstrap/merge flow
- [d:r:i] `health` structural repair logic
- [d:r:i] `update` runtime install/version flow
- [d:r:i] `from-gsd2` migration flow
- [d:r:i] `mandatory-initial-read` enforcement
- [d:r:i] repo-local tooling behavior itself

## Entry Conditions

### Explicit Entry

- [d:r:i] The workflow should be invokable directly when the operator wants a repo-local posture refresh:
  - `Run $gsd-uplift-project`

### Routed Entry

- [d:r:i] The workflow should later become a routed recommendation from:
  - `progress`
  - `resume-project`
  - `health`
  - `update`
  - `ingest-docs`
  - `new-milestone`
- [d:r:i] In the first slice, routed recommendation is enough. Those specialist surfaces do not need to absorb uplift logic.

## Detection Signals

- [d:r:i] A first-slice uplift pass should open when one or more of these signals appear:
  - existing project carries thin or older governing-doc posture
  - root/planning `AGENTS.md` or `CLAUDE.md` wrappers are absent or materially older than current repo doctrine
  - `.planning/CLAIM-TYPES.md` is absent
  - `.planning/LONG-ARC.md` is absent or clearly outside current repo posture
  - required-reading installation practice is absent from local packet/spec/prompt surfaces
  - strengthening-route carry is absent from the local discuss/context/plan/research chain where the repo now expects it
  - repo-local tooling expected by doctrine is absent
  - the project resumed or opened a new milestone after a major doctrine move without a posture refresh
  - the project was initialized under a thinner or different runtime posture than current local doctrine expects

## First-Slice Scope

- [d:r:i] The first slice should cover:
  - one repo at a time
  - vanilla and lightly aged projects first
  - single-runtime posture refresh first
  - governing/posture refresh and durable output
- [d:r:i] The first slice should hold out:
  - full runtime reinstall
  - structural repair beyond `health`
  - cross-project batching
  - workstream reconciliation
  - aged-bespoke deep merge
  - full audit-tree restructuring
  - full upstream-template expression pass

## Proposed Workflow Shape

### 1. Open The Pass And Classify It

- [d:r:i] Read the minimal current posture surfaces:
  - root `AGENTS.md`
  - `.planning/AGENTS.md`
  - root/planning `CLAUDE.md`
  - `STATE.md`
  - `.planning/LONG-ARC.md` if present
  - `.planning/CLAIM-TYPES.md` if present
- [d:r:i] Classify the uplift family:
  - vanilla uplift
  - aged-bespoke uplift
  - cross-runtime uplift
  - upstream-template-drift uplift
- [d:r:i] For first slice, only vanilla and lightly aged cases should proceed automatically; the others should be explicitly flagged and narrowed or deferred.

### 2. Gather Evidence From Specialist Owners

- [d:r:i] Pull runtime/install truth from:
  - `update` posture
  - `runtime_visibility.py`
  - `manifest_install_coherence.py` where helpful
- [d:r:i] Pull structural health from:
  - `health`
- [d:r:i] Pull project/milestone state from:
  - `STATE.md`
  - `progress`
  - `resume-project` context where relevant
- [d:r:i] Pull docs/bootstrap context from:
  - `ingest-docs` outputs where relevant
- [d:r:i] The workflow consumes these outputs. It does not reimplement them.

### 3. Refresh The First-Slice Carrier Set

- [d:r:i] Refresh or install the strongest compact set:
  - root `AGENTS.md` only where the repo expects repo-local doctrine to exist
  - `.planning/AGENTS.md`
  - root/planning `CLAUDE.md` wrappers
  - `.planning/CLAIM-TYPES.md` where absent
  - `.planning/LONG-ARC.md` where absent or clearly stale at the posture level
  - required-reading installation practice on relevant request/spec/prompt surfaces
  - presence of repo-local tooling that current doctrine assumes
- [d:r:i] For first slice, prefer refreshing carrier presence and posture over rewriting lots of project-specific content.

### 4. Write Durable Uplift Outputs

- [d:r:i] First-slice outputs should be:
  - `UPLIFT-REPORT.md`
  - `UPLIFT-STATE.md` or a dedicated uplift section inside `STATE.md`
- [d:r:i] `UPLIFT-REPORT.md` should record:
  - detected uplift class
  - before-state posture
  - what was refreshed
  - what was intentionally not refreshed
  - what should be routed later
- [d:r:i] `UPLIFT-STATE.md` or equivalent should record:
  - last uplift date
  - last uplift class
  - whether doctrine has materially moved since the last uplift
- [d:r:i] A project doctrine manifest remains promising, but it can be a second-slice object if `UPLIFT-REPORT.md` and state carry already make the first slice legible.

### 5. Route The Next Action

- [d:r:i] After refresh, the workflow should route explicitly:
  - to `new-milestone` when the real next move is milestone opening
  - to `progress` when posture is refreshed and ordinary routing can resume
  - to `health` when structural issues block uplift follow-through
  - to `update` when install/runtime issues block posture refresh
  - to `discuss-phase` when a phase boundary should be reopened under current doctrine
  - to `plant-seed` when a stronger future move is out of scope for the current uplift slice

## Carrier Decisions

### Best Place For The Workflow To Live

- [d:r:i] Preferred form:
  - repo-local skill plus workflow surface
- [d:r:i] Why:
  - this family is composition-layer behavior, not a one-off audit note
  - it should be callable directly and routable later from specialist surfaces

### Best Place For Its Outputs

- [d:r:i] `UPLIFT-REPORT.md`
  - strongest for per-pass memory and operator-facing before/after truth
- [d:r:i] `UPLIFT-STATE.md` or state section
  - strongest for later routing by `progress` / `resume-project`
- [d:r:i] seeds
  - strongest for out-of-slice deferred strengthening

## Review And Verification Gates

- [g:r:i] Before any implementation slice is accepted:
  - run `scan_threshold_language.py` on new request/spec/prompt/proposal surfaces
  - run `audit_refmap.py verify` on the active audit root
  - if runtime surfaces change, re-materialize through `./scripts/setup-portable-gsd.sh`
  - reread touched workflow/skill surfaces against `37` and `38`, not against memory
- [g:r:i] Before the first live slice is accepted:
  - test one vanilla project case
  - test one lightly aged project case
  - confirm the workflow routes rather than absorbs specialist-owner work
  - confirm the output artifacts make the before/after legible

## Current Consequence

- [d:r:i] The family now has:
  - `36` plan
  - revised `37` terrain map
  - `38` concern/carrier placement map
  - this bounded workflow proposal
- [d:r:i] The next move after local reread should be a bounded cross-vendor challenge on `37 + 38 + 39` together, or a direct first-slice implementation only if the workspace decides the proposal is already sharp enough to carry without that challenge.
