# 05 Git Cleanup Execution Task Spec

## Purpose

Execute the current Git cleanup/checkpoint plan by converting the mixed working tree into explicit, reviewable Git change sets with bounded commits.

This is an execution/verification task, not a new research lane.

## Task Classification And Runtime

- classification: `execution/verification`
- recommended model: `gpt-5.4`
- recommended reasoning: `high`

## Ownership

You are responsible for:

- staging and committing the current doc/process change sets cleanly
- refining the coarse 2026-04-15 orchestration signal into the two cleaner signals the user requested
- writing one execution report

You are **not** responsible for:

- starting any new substantive research lane
- changing product doctrine beyond what is already in the current diffs
- creating new implementation/code changes
- widening the scope into CI/deployment governance

## Write Scope

You may edit and commit only the files required to close the current cleanup plan, including:

- current dirty tracked/untracked files already identified in the cleanup plan
- new split signal files under `.planning/knowledge/signals/prix-guesser/`
- `.planning/knowledge/index.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md`

Do not touch unrelated files.

## Onboarding Sequence

Read these in order before committing anything.

### 1. Root repo instruction

- `AGENTS.md`

Why:
- repo quality bar
- spawn and orchestration policy
- current project posture and rerun boundary

### 2. Planning-local instruction

- `.planning/AGENTS.md`

Why:
- artifact discipline
- canon vs audit vs exploration distinctions
- future-flexibility statusing expectations

### 3. Operational cleanup control notes

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`

Why:
- these define the intended Git change sets and cleanup sequence

### 4. Current active process/remedy bundle

- `.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`

Why:
- this is the active change set `D`
- it gives the wider context needed to commit the process/remedy bundle coherently

### 5. Canon uplift context

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-patch-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-task-spec.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-report.md`

Why:
- these explain why the canon diffs exist and what boundaries they were supposed to preserve

### 6. AGENTS overhaul context

- `.planning/research/2026-04-14-agents-md-audit/01-agents-md-audit-and-improvement-proposal.md`

Why:
- this is the rationale for the AGENTS split and root-file narrowing

### 7. Live repo state

Run and review:

```bash
git status --short
git diff --stat
git diff --name-only
```

Why:
- confirm the cleanup plan still matches actual working tree state

## Required Change Sets

### Change Set D: Orchestration / Framework Audit And Process Response

This set should include:

- `.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- split signal files replacing the coarse one
- `.planning/knowledge/index.md`

#### Signal refinement required

The current coarse signal:

- `.planning/knowledge/signals/prix-guesser/2026-04-15-orchestrator-underdelegation-dirty-transitions.md`

should not survive unchanged.

Replace it with at least these two clearer signals:

1. dirty task transitions / mixed worktree hygiene
2. underdelegated exploratory work / orchestrator role drift

If you think a third separate signal for launch-bundle auditability is genuinely warranted, you may add it, but do not force one if the evidence is too thin.

Prefer replacement over keeping the coarse uncommitted predecessor around.

#### Default commit message

If the resulting diff still fits one coherent process/remedy unit, use:

- `docs(process): close orchestration audit and record cleanup protocol`

If you need two commits, prefer:

1. `docs(process): record orchestration audit and remedy synthesis`
2. `docs(signal): split orchestration failure into cleaner signals`

### Change Set A1: Canon Uplift Support Trail

This set should include:

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-task-spec.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-patch-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-task-spec.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-report.md`

#### Default commit message

- `docs(audit): add canon uplift steering and execution trail`

### Change Set A2: Canon Uplifted Planning Docs

This set should include only:

- `.planning/REQUIREMENTS.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`

#### Default commit message

- `docs(planning): uplift canon for wrapper, host, and memory doctrine`

### Change Set B: AGENTS Overhaul

This set should include:

- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/research/2026-04-14-agents-md-audit/01-agents-md-audit-and-improvement-proposal.md`

#### Default commit message

- `docs(agents): split root and planning instruction layers`

### Change Set C: 05-Gap-Closure Audit Corpus

This set should include:

- the remaining intended `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/` corpus not already consumed by sets A or D
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/INDEX.md`

#### Default commit strategy

Prefer one commit if it remains legible:

- `docs(audit): checkpoint 05 gap-closure corpus`

If the diff is too large or semantically mixed, split into:

1. `docs(audit): update 05 gap-closure governance and index`
2. `docs(audit): checkpoint 05 gap-closure corpus`

## Wider-Context Rule For Commits

Do not path-stage mechanically without understanding why a file belongs to a change set.

For each commit, confirm:

1. what question or response it answers
2. why the grouped files belong together
3. what would make the commit misleadingly broad
4. whether any file should be moved to a later commit instead

If the default grouping from this spec is wrong after inspection, adjust it and explain why in the execution report.

## Execution Rules

- Use path-specific staging only.
- Do not stage everything with `git add .`.
- Do not rewrite or revert unrelated content.
- Do not start any new substantive artifact beyond the execution report and the split signals.
- If a change set turns out to be not ready for a clean commit boundary, stop and report rather than forcing it.

## End State Requirement

Preferred end state:

- the current dirty tree is converted into bounded commit series for D, A1, A2, B, and C
- `git status --short` is clean at the end

If not fully possible, report exactly which change set remains uncommitted and why.

## Required Output

Write:

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md`

Include:

1. actual commit sequence performed
2. final path membership by commit
3. any deviation from the default grouping and why
4. final `git status --short`
5. anything intentionally left uncommitted
