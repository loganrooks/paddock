Date: 2026-04-21
Status: active map artifact

# Entry Surface And Project Uplift Map

## Purpose

- [g:r:i] This artifact maps the full entry-surface family opened in `36` so later uplift design can build from the real harness terrain rather than from a generic “improve onboarding” slogan.
- [g:r:i] The target is broader than first-run setup. The target is the whole family of moments where a project enters, re-enters, changes milestone, is bootstrapped from docs, is repaired, is updated, or is migrated into the repo-local harness posture.

## Framing

- [d:r:i] The current family contains at least five distinct jobs:
  - initial creation
  - milestone opening
  - docs bootstrap / docs merge
  - session re-entry and planning recovery
  - runtime / planning / doctrine uplift for projects that already exist
- [d:r:i] The first four jobs already have real owners. The fifth is distributed across several surfaces and still lacks one explicit owner.
- [d:r:i] This map therefore asks not only what each surface already carries, but also where ownership thins, where carry becomes scattered across multiple commands, and where a dedicated uplift workflow should later gather the work into one auditable path.

## Scenario Map

- [d:r:i] `Fresh greenfield repo`
  - current primary owner: `new-project`
- [d:r:i] `Brownfield repo with code but no .planning/`
  - current primary owner: `new-project`, with optional `map-codebase` detour first
- [d:r:i] `Existing project opening a new milestone`
  - current primary owner: `new-milestone`
- [d:r:i] `Docs-heavy repo bootstrapping or merging planning state`
  - current primary owner: `ingest-docs`
- [d:r:i] `Existing project returning after time away`
  - current primary owners: `resume-project` and `progress`
- [d:r:i] `Existing project with damaged or thin planning state`
  - current primary owner: `health`
- [d:r:i] `Existing project updating runtime install/version`
  - current primary owner: `update`
- [d:r:i] `Project migrating from GSD2 back to .planning/`
  - current primary owner: `from-gsd2`
- [d:r:i] `Existing vanilla or older GSD project that should inherit stronger repo-local doctrine, governing docs, long-horizon carry, and runtime posture`
  - current owner: no single explicit owner yet
  - current practical reality: the user/operator must compose pieces from `update`, `health`, `resume-project`, `progress`, governing-doc rereads, and local audit/onboarding artifacts by hand

## Current Surface Map

### 1. `new-project`

- [e:c+i] `new-project` already owns a thick creation path: init checks, git/bootstrap decisions, brownfield codebase-map offer, config creation, prior spike/sketch discovery, project synthesis, requirements, roadmap, state initialization, and instruction-file generation. Sources: .codex/get-shit-done/workflows/new-project.md:57-67, .codex/get-shit-done/workflows/new-project.md:104-124, .codex/get-shit-done/workflows/new-project.md:212-231, .codex/get-shit-done/workflows/new-project.md:242-261, .codex/get-shit-done/workflows/new-project.md:332-436, .codex/get-shit-done/workflows/new-project.md:1046-1247, .codex/get-shit-done/workflows/new-project.md:1335-1368.
- [d:r:i] Its strongest carry is creation-time coherence: it can move from idea or brownfield discovery into `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, config, research, and runtime instruction file in one owned flow.
- [d:r:i] Its thinner edge for the current family is that it assumes the project is crossing into planning for the first time. It does not own “take an already-initialized vanilla project and bring it into stronger repo-local posture” as a separate governed action.

### 2. `new-milestone`

- [e:c+i] `new-milestone` already owns a thick existing-project entry: it loads `PROJECT.md`, `MILESTONES.md`, and `STATE.md`, scans planted seeds, refreshes milestone summary, keeps the evolution section alive, can archive old phase directories before numbering reset, optionally runs fresh milestone research, defines requirements, and roadmaps the next milestone. Sources: .codex/get-shit-done/workflows/new-milestone.md:30-33, .codex/get-shit-done/workflows/new-milestone.md:49-96, .codex/get-shit-done/workflows/new-milestone.md:153-172, .codex/get-shit-done/workflows/new-milestone.md:174-198, .codex/get-shit-done/workflows/new-milestone.md:218-231, .codex/get-shit-done/workflows/new-milestone.md:235-249, .codex/get-shit-done/workflows/new-milestone.md:350-377, .codex/get-shit-done/workflows/new-milestone.md:431-496.
- [d:r:i] Its strongest carry is milestone-shaped continuation plus seed resurfacing.
- [d:r:i] Its thinner edge is posture inheritance. It assumes the project already has a meaningful `PROJECT.md` / `STATE.md` / roadmap baseline. It can widen scope intelligently, but it does not own a deeper refresh of runtime posture, governing-doc stack, or repo-local doctrine when the existing project is older or thinner than the current harness.

### 3. `ingest-docs`

- [e:c+i] `ingest-docs` already owns docs bootstrap and docs merge: it auto-detects `new` vs `merge`, classifies mixed doc sets, writes intel and conflict reports, blocks on blockers, routes clean new-mode synthesis through `gsd-roadmapper`, and in merge mode plans requirement / decision / roadmap additions against existing `.planning/` state. Sources: .codex/get-shit-done/workflows/ingest-docs.md:48-77, .codex/get-shit-done/workflows/ingest-docs.md:128-149, .codex/get-shit-done/workflows/ingest-docs.md:173-199, .codex/get-shit-done/workflows/ingest-docs.md:205-230, .codex/get-shit-done/workflows/ingest-docs.md:238-258, .codex/get-shit-done/workflows/ingest-docs.md:268-277, .codex/get-shit-done/workflows/ingest-docs.md:287-310.
- [d:r:i] Its strongest carry is document-origin reconciliation with conflict gating.
- [d:r:i] Its thinner edge is repo-local uplift beyond document synthesis. It can build or merge planning state from docs, but it does not install a stronger governing-doc stack, does not refresh runtime/local doctrine, and does not own the “older project to stronger repo-local posture” move once the docs merge itself is complete.

### 4. `resume-project` / `gsd-resume-work`

- [e:c+i] `resume-project` already owns session re-entry and recovery: it can restore from `STATE.md`, reconstruct `STATE.md` when absent, detect `HANDOFF.json`, `.continue-here`, incomplete plans, interrupted agents, and route toward the next appropriate discuss / plan / execute step. Sources: .codex/get-shit-done/workflows/resume-project.md:19-31, .codex/get-shit-done/workflows/resume-project.md:36-58, .codex/get-shit-done/workflows/resume-project.md:62-111, .codex/get-shit-done/workflows/resume-project.md:156-192, .codex/get-shit-done/workflows/resume-project.md:227-316; .codex/skills/gsd-resume-work/SKILL.md:48-75.
- [d:r:i] Its strongest carry is context restoration and resumption routing.
- [d:r:i] Its thinner edge is posture uplift. It restores where the project is, but it does not ask whether the project’s runtime, governing docs, required-reading posture, or long-horizon carry should be refreshed before continuing.

### 5. `progress`

- [e:c+i] `progress` already owns situational awareness and next-step routing: it detects missing planning state, analyzes the roadmap/state snapshot, surfaces verification debt, distinguishes phase states, and routes to execution, discuss, plan, verify, audit, milestone close, or new milestone start. Sources: .codex/get-shit-done/workflows/progress.md:25-41, .codex/get-shit-done/workflows/progress.md:45-69, .codex/get-shit-done/workflows/progress.md:83-137, .codex/get-shit-done/workflows/progress.md:141-207, .codex/get-shit-done/workflows/progress.md:403-516.
- [d:r:i] Its strongest carry is routing the operator through current project state.
- [d:r:i] Its thinner edge is structural uplift detection. It knows whether a project is missing planning state or carries verification debt, but it does not currently own a richer “this project exists, but it still deserves repo-local harness uplift” branch.

### 6. `health`

- [e:c+i] `health` already owns structural planning validation and narrow repair: it can detect missing core files, invalid config, naming mismatch, invalid phase references, absent nyquist key, and stale task directories, and it can repair specific low-risk structural issues such as missing config or missing `STATE.md`. Sources: .codex/get-shit-done/workflows/health.md:25-38, .codex/get-shit-done/workflows/health.md:60-94, .codex/get-shit-done/workflows/health.md:123-159, .codex/get-shit-done/workflows/health.md:161-180.
- [d:r:i] Its strongest carry is integrity checking plus low-risk repair.
- [d:r:i] Its thinner edge is that it draws a hard boundary around deeper content/doctrine change. That is good for safety, but it means `health` cannot by itself carry a richer uplift path involving governing docs, required-reading posture, long-horizon installation, or doctrine refresh.

### 7. `update`

- [e:c+i] `update` already owns runtime/version posture: it detects local vs global install, resolves preferred runtime/config-dir, checks npm release state, warns about clean install boundaries, preserves custom files, runs the install, clears update cache, and points to local patch reapplication. Sources: .codex/get-shit-done/workflows/update.md:12-23, .codex/get-shit-done/workflows/update.md:76-116, .codex/get-shit-done/workflows/update.md:288-320, .codex/get-shit-done/workflows/update.md:353-368, .codex/get-shit-done/workflows/update.md:464-487, .codex/get-shit-done/workflows/update.md:558-567.
- [d:r:i] Its strongest carry is runtime-install truth and safe update execution.
- [d:r:i] Its thinner edge is project-level onboarding. It updates the harness install and protects user files, but it does not bring a repo’s governing docs, `.planning/` posture, seeds, long-horizon carry, or instruction surfaces into current local doctrine by itself.

### 8. `from-gsd2`

- [e:c+i] `from-gsd2` already owns hierarchy migration from `.gsd/` into `.planning/`, preserving slices/tasks as phases/plans and carrying completion state where possible. Sources: .codex/skills/gsd-from-gsd2/SKILL.md:48-82.
- [d:r:i] Its strongest carry is structural migration across generations.
- [d:r:i] Its thinner edge is that it stops at format migration. It does not then run a richer repo-local uplift pass over the migrated project.

### 9. Governing / Onboarding Carriers

- [e:c+i] `mandatory-initial-read` enforces `<required_reading>` when a workflow has already named files to load. Source: .codex/get-shit-done/references/mandatory-initial-read.md:1.
- [d:r:i] That makes it an important discipline carrier, but not an uplift owner. It does not decide what a vanilla or older project should newly inherit; it only ensures required files are read once they have already been named.

## Interaction Map

- [d:r:i] `new-project` and `new-milestone` are the thickest creation/continuation surfaces.
- [d:r:i] `ingest-docs` is the thickest document-origin bridge.
- [d:r:i] `resume-project` and `progress` are the thickest situational/re-entry surfaces.
- [d:r:i] `health` is the thickest structural repair surface.
- [d:r:i] `update` is the thickest runtime-version surface.
- [d:r:i] `from-gsd2` is the thickest format migration surface.
- [d:r:i] None of these currently owns the full cross-surface move:
  - detect older/vanilla posture
  - check runtime/install state
  - check `.planning/` structural health
  - install or refresh repo-local governing docs/instruction carriers
  - ensure required-reading and long-horizon carry are active
  - output an explicit uplift disposition showing what was refreshed, what stayed local, and what still needs later work

## Where Carry Is Currently Scattered

### Governing-Doc Refresh

- [d:r:i] The current harness can generate an instruction file during `new-project`, and local audit work has its own onboarding companions, but there is no single follow-through path for refreshing root/planning `AGENTS.md`, thin `CLAUDE.md` wrappers, or related governance documents on an already-existing project. Sources: .codex/get-shit-done/workflows/new-project.md:1247, .codex/get-shit-done/workflows/new-project.md:1346.

### Long-Horizon And Strengthening Carry Install

- [d:r:i] The strengthening family is now live in discuss/context/plan/research/seed surfaces, but there is no owned entry/uplift surface that checks whether an existing project has actually inherited those newer carriers before ordinary planning continues. Sources: intervention-proposals/32-strengthening-opportunity-first-slice-implementation.md:1, intervention-proposals/33-research-and-planner-strengthening-carry-follow-through.md:1.

### Vanilla-Project Uplift

- [d:r:i] An existing vanilla project can currently be updated, repaired, resumed, or progressed, but it still lacks one explicit route that says: detect thinner posture, refresh runtime/governing/planning carriers, and write a durable report of the uplift. This is the family’s clearest ownerless seam.

### Output Record

- [d:r:i] The current entry surfaces each produce their own local outputs (`PROJECT.md`, `STATE.md`, roadmap, conflicts, repair results, resume status), but there is no single uplift report surface that records the before/after of a project-wide repo-local refresh.

## Candidate Ownership Split For A Later Uplift Workflow

- [d:r:i] `new-project`, `new-milestone`, and `ingest-docs` should stay the primary owners of creation / milestone / docs merge.
- [d:r:i] `health` should stay the owner of low-risk structural repair.
- [d:r:i] `update` should stay the owner of runtime install/version change.
- [d:r:i] `progress` and `resume-project` should stay the owners of situational routing and session restoration.
- [d:r:i] A later uplift workflow should own the composition layer:
  - detect whether uplift is worth opening
  - gather runtime/install, planning-health, and governing-posture evidence
  - refresh repo-local carriers that belong together
  - write a durable uplift report / disposition
  - route any remainder into later work instead of mutating silently

## Current Consequence

- [d:r:i] The family terrain is now sharp enough for a next design object.
- [d:r:i] The next exact object should be `38-project-uplift-workflow-proposal.md`.
- [d:r:i] Before or alongside `38`, this map is now strong enough to serve as the local scaffold for the later `opus[1m]` widening pass the workspace already agreed to run.
