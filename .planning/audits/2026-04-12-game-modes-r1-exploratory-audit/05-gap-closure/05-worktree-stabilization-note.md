# 05 Worktree Stabilization Note

## Purpose

This is an operational control artifact for the current mixed worktree.

It exists to stop the `05-gap-closure` audit, canon-uplift response, AGENTS overhaul, knowledge-base updates, and new orchestration-framework audit from remaining one implicit pile of changes.

This note is not product canon. It is a task-boundary and concern-bucket control note.

## Trigger

The user explicitly flagged that the worktree had become disorganized and that substantive work was continuing across mixed concern buckets without a clean transition boundary.

## Current Snapshot

Observed live buckets in the worktree:

1. `canon uplift`
2. `AGENTS overhaul`
3. `05-gap-closure audit corpus`
4. `knowledge-base signals / index`
5. `2026-04-15 orchestration-framework audit`

The main problem is not merely that the tree is dirty. It is dirty across multiple unrelated substantive buckets whose review/acceptance states are different.

## Concern Buckets

### Bucket A: Canon Uplift

**Files**
- `.planning/REQUIREMENTS.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-task-spec.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-report.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-patch-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md`
- related steering proposal/spec artifacts in the same directory

**Status**
- `review-needed`

**Why**
- the execution worker completed and the patch is bounded
- but the bucket has not yet been explicitly accepted, revised, or parked as a reviewed unit

**What must happen next**
- main-thread review of the four canon diffs as one bounded patch task
- explicit disposition:
  - `accept`
  - `request revision`
  - or `park as provisional`

### Bucket B: AGENTS Overhaul

**Files**
- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/research/2026-04-14-agents-md-audit/01-agents-md-audit-and-improvement-proposal.md`

**Status**
- `review-needed`

**Why**
- the split and rewrite were already performed
- but this bucket has not yet been bounded as its own accepted governance change

**What must happen next**
- review the root vs `.planning/` split as one governance bucket
- decide whether it is acceptable as-is or needs follow-up refinement

### Bucket C: 05-Gap-Closure Audit Corpus

**Files**
- the untracked `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/` directory
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/INDEX.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md`

**Status**
- `intentional corpus / review-needed`

**Why**
- this is not random debris; it is the actual audit trail
- but it is still unbounded operationally because it has not been explicitly treated as one checkpointable corpus

**What must happen next**
- decide whether this directory is:
  - a single intentional audit corpus to checkpoint together
  - or a mixture that needs internal pruning / promotion / parking

### Bucket D: Knowledge-Base Signal Layer

**Files**
- `.planning/knowledge/index.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-orchestrator-underdelegation-dirty-transitions.md`

**Status**
- `needs refinement`

**Why**
- the signal was too coarse and should be split
- at minimum into:
  - dirty worktree / bad task-transition hygiene
  - poor orchestration / underdelegated exploratory work
- launch-spec auditability may deserve a third signal if kept distinct

**What must happen next**
- split or supersede the coarse signal with cleaner scoped signals
- update the knowledge index accordingly

### Bucket E: 2026-04-15 Orchestration-Framework Audit

**Files**
- `.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`

**Status**
- `active but bounded`

**Why**
- the lane outputs exist
- the bundle still needs a converged synthesis/response layer
- but this bucket is now at least isolated to one research directory with a persisted launch bundle spec

**What must happen next**
- synthesize the three lane outputs into one remedy/decision artifact
- do not let this bucket bleed into canon or governance edits before that synthesis exists

## Working Rule From This Point

No new substantive bucket should be started until one of the current buckets is explicitly marked:

- `accepted`
- `revised`
- `parked`
- or `intentionally active but isolated`

`dirty tree` is not the only trigger. `mixed unbounded buckets` is the real trigger.

## Recommended Stabilization Sequence

### Step 1

Refine Bucket D first.

Reason:
- the signal layer should describe the failure correctly before we formalize the response to it

### Step 2

Bound Bucket E with a converged synthesis/response artifact.

Reason:
- the orchestration-framework audit is already running and now has its lane outputs
- it should become one reviewed research bucket instead of staying half-open

### Step 3

Review Bucket A as one canon-uplift patch unit.

Reason:
- this is the most important substantive doc-change bucket already present in the tree
- its execution worker already returned a bounded report

### Step 4

Review Bucket B as one governance bucket.

Reason:
- AGENTS changes are meaningful, but they are lower priority than the canon-uplift and process-failure response buckets

### Step 5

Checkpoint Bucket C intentionally.

Options:
- accept it as the historical audit corpus
- or identify a smaller set of promoted artifacts vs parked historical trail

## What This Note Is Not Doing

- It is not cleaning the tree by itself.
- It is not deciding which bucket to commit first.
- It is not collapsing all modified files into one fake “current task.”
- It is not promoting the current mixed tree as acceptable.

## Immediate Use

Until this note is superseded, any further substantial work should cite which concern bucket it belongs to and whether it is:

- closing an existing bucket
- refining an existing bucket
- or improperly starting a new one
