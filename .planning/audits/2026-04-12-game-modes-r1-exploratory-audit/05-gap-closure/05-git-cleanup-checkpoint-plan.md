# 05 Git Cleanup / Checkpoint Plan

## Purpose

Translate the current mixed working tree into explicit Git change sets.

This is the version-control companion to [05-worktree-stabilization-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md).

The goal is not just to "make the tree clean." The goal is to recover:

- reviewable diffs
- coherent commits
- safe rollback boundaries
- clear ownership of ongoing work

## Scope

This plan covers the current dirty working tree on `phase-01-guardrails-rerun-boundary`.

It does not decide final merge order into `main`, and it does not replace later release/deployment governance.

## Core Rule

The current working tree should be understood as multiple logical Git change sets, not one active task.

Each change set must become one of:

- committed as its own bounded series
- explicitly parked
- or explicitly abandoned

Signals are not their own standalone bucket by default. They should usually travel with the change set or process bucket that caused them, unless a signal truly spans multiple buckets and needs separate treatment.

## Current Change Sets

### Change Set A: Canon Uplift

**Core files**
- `.planning/REQUIREMENTS.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`

**Support artifacts**
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-patch-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-task-spec.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-report.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-task-spec.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md`

**Recommended Git handling**
- one bounded commit series, preferably:
  1. audit/steering support artifacts
  2. canon doc patch

**Why**
- the four canon files are one substantive doctrine change set
- the support artifacts provide traceability without needing to live in the same diff hunk-by-hunk

**Precondition**
- explicit review of the canon diff as one bounded patch task

### Change Set B: AGENTS Overhaul

**Files**
- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/research/2026-04-14-agents-md-audit/01-agents-md-audit-and-improvement-proposal.md`

**Recommended Git handling**
- one bounded governance/docs commit

**Why**
- these files are tightly related and represent one repo-instruction change set

**Precondition**
- confirm the root vs `.planning/` split still reflects current intent and does not duplicate later governance changes

### Change Set C: 05-Gap-Closure Audit Corpus

**Files**
- the untracked `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/` corpus
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/INDEX.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md`

**Recommended Git handling**
- one intentional audit-corpus checkpoint commit, or a short series:
  1. governance/index changes
  2. 05 corpus import

**Why**
- this is historical audit trail, not product canon
- it should be checkpointed as an intentional corpus, not left as ambient untracked state

**Precondition**
- confirm that this corpus is meant to be retained as a whole and not pruned first

### Change Set D: 2026-04-15 Orchestration / Framework Audit

**Files**
- `.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- related synthesis artifact once written
- related signals and `.planning/knowledge/index.md` updates

**Recommended Git handling**
- do not commit yet
- keep as the current active change set until the converged synthesis/response artifact exists

**Why**
- the research lanes are written, but the remedy layer is not yet closed
- committing before synthesis would freeze an unfinished process bucket

**Precondition**
- write the converged synthesis/response artifact first
- split/refine the current coarse signal structure

## Recommended Immediate Sequence

### Step 1: Finish Change Set D before touching other sets again

Reason:
- it is the currently active process/remedy bucket
- its outputs already exist and only need synthesis/response closure
- finishing it reduces the chance of adding yet another cross-cutting operational artifact later

### Step 2: Review and checkpoint Change Set A

Reason:
- it is the most important substantive doc patch already present
- it is already bounded by an execution report and patch plan

### Step 3: Review and checkpoint Change Set B

Reason:
- important governance change, but lower risk than the canon patch

### Step 4: Checkpoint Change Set C intentionally

Reason:
- it is audit history and should stop living as a giant untracked directory

## Execution Approach For The Current Tree

### Preferred approach now

Use path-specific staging and commits in the current checkout.

Why:
- the change sets already coexist in this working tree
- retroactively moving them into separate worktrees would add complexity without reducing present confusion much
- path-based checkpointing is enough to recover clean commit boundaries here

### Preferred approach later

Use separate branches or `git worktree` checkouts when:

- two substantial streams need to continue in parallel
- one stream is research/audit and another is canon or code implementation
- subagents need to operate for a while on independent write scopes

That should be used prospectively, not only after the tree is already mixed.

## Commands / Tactics To Prefer

For current recovery:
- `git status --short`
- `git diff --name-only`
- `git diff -- <paths>`
- `git add <paths>`
- `git commit -m "..."`

If a set is not ready:
- park it explicitly rather than letting it remain ambient
- use path-scoped stash only if truly necessary and only with clear labels

Avoid:
- generic "clean everything later"
- mixing unrelated paths into one commit because they are all docs
- starting a new substantive change set before one of the existing sets is checkpointed

## Mapping To Future Workflow Discipline

Going forward, every substantial task should answer:

1. What Git change set am I working in?
2. What files belong to it?
3. Is this same-checkout work, or should it have a separate branch/worktree?
4. What is the commit/park/reject condition before another change set starts?

## What This Plan Does Not Yet Solve

- branch protection and release policy
- deployment environments
- CI enforcement
- secrets and rollout discipline

Those should be handled in a later repo-operations / devops governance pass once the current working tree is stabilized.
