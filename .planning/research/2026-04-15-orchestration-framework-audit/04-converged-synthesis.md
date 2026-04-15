# 04 Converged Synthesis

## Research Frame
- Mode: `synthesis`
- Question:
  Given the three lane outputs, what can now be concluded about:
  - the recent orchestration/task-transition failure
  - the current local GSD framework's ability to support long-horizon doctrine
  - the highest-value guardrails and workflow changes for this repo
- Scope:
  - [01-orchestration-and-task-transition-failure-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md)
  - [02-long-arc-lifecycle-integration-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md)
  - [03-guardrails-mechanisms-and-command-proposals.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md)
- Non-goals:
  - patching the framework in this artifact
  - deciding final production CI/CD or release engineering policy
  - replacing repo-local GSD with a different system
- Stop condition:
  - close this audit as one bounded research change set
  - identify what can be acted on now
  - identify what should be deferred to a later repo-operations / production-governance pass

## Artifacts Read
- [00-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md)
- [01-orchestration-and-task-transition-failure-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md)
- [02-long-arc-lifecycle-integration-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md)
- [03-guardrails-mechanisms-and-command-proposals.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md)

## Integrated Decision Structure

### 1. What failed

The recent failure was not simply “bad delegation” or “dirty tree” in isolation.

The strongest integrated model is:

1. a meaningful execution task was delegated successfully
2. the returned task was not converted into an explicit `accept / revise / park` checkpoint
3. the main thread resumed exploratory work locally instead of delegating that exploration
4. the working tree accumulated multiple unresolved logical change sets
5. user interruption became the only effective transition gate

So the real defect is:

- `underdelegated exploratory work`
- plus `missing task-transition control`
- plus `weak Git change-set discipline`

### 2. What the framework already does well

The current repo-local GSD stack is stronger than generic workflow tooling in one important area:

- it already has a real phase-steering model for long-horizon work

That strength comes from:

- `exploratory` discuss mode
- required `canonical_refs`
- required `future_awareness`
- normalized buckets:
  - `Protected Seams`
  - `Explicit Non-Decisions`
  - `Current Posture`
  - `Future Shape Notes`
- planner/research/checker flows that treat those as real guardrails
- repo overlay coverage for discuss/plan/research/context

So the repo is not starting from nothing. It already has a serious substrate for future-aware phase work.

### 3. Where the framework is still weak

The weakness is lifecycle continuity, not phase-local intelligence.

`LONG-ARC.md` is strong in:

- `discuss-phase`
- `CONTEXT.md`
- `research-phase`
- `plan-phase`

But it is weak or absent in:

- `new-project`
- `new-milestone`
- `progress`
- `transition`
- `complete-milestone`
- generic `PROJECT.md` / `ROADMAP.md` templates

That means the framework is currently:

- `capable` of long-horizon design
- but not yet `robustly lifecycle-aware`

The repo is compensating through strong local canon and AGENTS rules, which works, but is brittle.

### 4. What kind of guardrail strategy is actually justified

The right strategy is not “more hooks everywhere.”

The strongest cross-lane conclusion is:

- nuanced failures here should be handled mostly by explicit workflow gates, commands, and artifact contracts
- not by broad opaque blocking hooks

So the preferred order of mechanisms is:

1. repo policy
2. workflow / command support
3. narrow reminder hooks
4. hard blocking hooks only for obvious destructive cases

## What Can Close Now

### Close 1: Progressive guardrails are a valid principle, with the right qualifier

The right principle is not:

- “more complex project -> always more guardrails”

It is:

- `higher-risk, higher-blast-radius, higher-parallelism, and higher-environment-complexity work -> stronger workflow and release discipline`

That means progressive guardrails are justified when:

- more contributors or subagents can interfere
- more parallel streams are active
- deployment environments matter more
- rollback cost rises
- doctrine drift becomes more expensive
- the cost of a bad release becomes materially higher

So yes, guardrail complexity should grow over time, but in proportion to operational risk and coordination complexity, not just repo size.

### Close 2: The immediate remedy should focus on workflow and Git discipline, not production automation yet

The current strongest near-term actions are:

- make exploration subagent-first by default
- add a real task-transition gate
- treat the working tree as explicit Git change sets
- tighten autonomy defaults that currently bypass too many checkpoints
- lift `LONG-ARC.md` into lifecycle workflows

These are more urgent than jumping straight to CI/CD design.

### Close 3: This repo needs a later repo-operations / production-governance pass

That future pass should cover:

- branch strategy
- worktree strategy
- PR/review expectations
- CI / GitHub Actions
- environment promotion
- secrets handling
- release / rollback practice
- deploy/runbook expectations

But that is a distinct change set from the current orchestration/framework audit.

## What Must Stay Open

- Exactly which changes should live as:
  - repo-local policy
  - overlay workflow changes
  - new repo-local skills/commands
  - config defaults
- Whether the active coarse signal should be split into:
  - dirty task transitions / mixed worktree
  - underdelegated exploratory work
  - launch-bundle auditability gap
- Whether some autonomy defaults should be tightened immediately or only after the current dirty tree is stabilized
- Whether future Git discipline should be enforced mainly by:
  - workflow commands
  - branch/worktree norms
  - CI checks
  - or a combination

## Recommended Near-Term Response Sequence

1. Refine the signal layer so the failure is recorded cleanly.
2. Treat this audit as closed and bounded with this synthesis artifact.
3. Stabilize the current working tree using the Git cleanup/checkpoint plan.
4. After the tree is stabilized, run a distinct repo-operations / production-governance research pass.

That later pass should explicitly study:

- good Git discipline for large agent-assisted repos
- branch/worktree policy for Codex-heavy work
- CI and GitHub Actions enforcement
- deployment / release discipline
- how to stage stronger controls progressively as risk rises

## Recommended Mechanisms To Carry Forward

### Immediate, high-leverage

- exploratory and scope-shaping work defaults to subagent bundles
- every non-trivial bundle gets a persisted `00-launch-bundle-spec.md` at launch time
- every returned subagent task must be dispositioned:
  - `accept`
  - `revise`
  - `park`
  - `reject`
- no new substantive task begins while the current Git change set is unresolved

### Next framework/workflow layer

- add a task-transition gate command or workflow step
- add mixed-change-set awareness to progress/next-step routing
- add long-arc carry-forward checks to milestone start, transition, and milestone completion
- tighten repo-local autonomy defaults to fit this repo's rigor bar

### Later production-governance layer

- branch and worktree policy
- PR and review discipline
- CI / GitHub Actions
- deploy/release controls
- environment and rollback policy

## Planning Handoff

### What can now be treated as decided

- the recent failure was structurally real and not just user impatience
- subagent-first exploration should become a repo operating rule
- task-transition gating is missing and should become first-class
- `LONG-ARC.md` is phase-strong but lifecycle-weak in the framework
- broad hook overreach is not the preferred fix

### What remains assumed or open

- exact command/skill design for transition gating
- exact split between repo-local overlay changes and repo-only governance
- exact future CI/release/deployment enforcement strategy

### Derived constraints

- future process fixes should be Git- and workflow-aware, not just prompt-aware
- future long-horizon support must reach lifecycle workflows, not only phase steering
- future enforcement should prefer visible gates and commands over opaque denials

### Future-awareness seams to preserve

- long-arc doctrine must remain distinct from the roadmap
- repo-local speed paths must not silently bypass doctrine-sensitive checkpoints
- Git cleanliness must be understood as logical change-set discipline, not just absence of modified files

### Deferred follow-up lane

- `repo operations / production governance audit`
  - Git discipline
  - branch/worktree strategy
  - CI / GitHub Actions
  - deployment/release posture
  - progressive guardrail escalation by risk and complexity
