# 00 Orchestration Framework Audit - Launch Bundle Spec

## Purpose

Persist the exact subagent research bundle used to investigate the current orchestration/process failure and the local GSD framework's ability to support long-horizon, high-rigor work.

This file exists so the research pass is auditable as a launched bundle rather than only recoverable from thread history.

## Trigger

The user explicitly corrected the orchestrator for:

- keeping exploratory, scope-shaping work in the main thread instead of delegating to subagents
- proceeding across tasks with an unresolved mixed worktree
- failing to enforce clean task-transition guardrails
- risking shallow exploration and poor decision-making as a result

## Bundle Shape

The remedy research was split into three subagent lanes so the work could be explored more deeply and in parallel instead of collapsed into one shallow main-thread pass.

### Lane 1: Orchestration And Task-Transition Failure Audit

- output: `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- agent id: `019d8f70-c3d0-72f3-9a33-76315fff2500`
- nickname: `Ohm`
- role: `worker`
- model: `gpt-5.4`
- reasoning: `xhigh`
- verified runtime branch: `phase-01-guardrails-rerun-boundary`

#### Scope

- audit the current orchestration/process failure as an inspectable failure model
- distinguish root causes, enabling conditions, and downstream harms
- propose an orchestration protocol that would have prevented this exact failure

#### Required reading

- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-recursive-gsd-orchestration.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-premature-stall-diagnosis.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-orchestrator-underdelegation-dirty-transitions.md`
- `.planning/STATE.md`
- canon-uplift execution/report artifacts under `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/`

### Lane 2: LONG-ARC Lifecycle Integration Audit

- output: `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md`
- agent id: `019d8f71-1acf-7b60-a47f-fcb108c72aed`
- nickname: `Carson`
- role: `worker`
- model: `gpt-5.4`
- reasoning: `xhigh`
- verified runtime branch: `phase-01-guardrails-rerun-boundary`

#### Scope

- audit how `.codex/get-shit-done` and the repo overlay integrate `.planning/LONG-ARC.md`, future-awareness, preserved seams, and non-decisions
- determine whether long-arc awareness is first-class across the project and milestone lifecycle or still too phase-local

#### Required reading

- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/plan-phase.md`
- `.codex/get-shit-done/workflows/research-phase.md`
- `.codex/get-shit-done/workflows/new-project.md`
- `.codex/get-shit-done/workflows/new-milestone.md`
- `.codex/get-shit-done/workflows/progress.md`
- `.codex/get-shit-done/workflows/transition.md`
- `.codex/get-shit-done/workflows/complete-milestone.md`
- `.codex/get-shit-done/templates/context.md`
- `.codex/get-shit-done/templates/project.md`
- `.codex/get-shit-done/templates/roadmap.md`
- overlay versions of relevant discuss/plan/context/workflow files where they exist

### Lane 3: Guardrails, Mechanisms, And Command Proposals

- output: `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- agent id: `019d8f71-6af5-7f82-aa05-20e39224f83e`
- nickname: `Avicenna`
- role: `worker`
- model: `gpt-5.4`
- reasoning: `xhigh`
- verified runtime branch: `phase-01-guardrails-rerun-boundary`

#### Scope

- propose concrete workflow/skill/hook/command/policy mechanisms for:
  - deeper subagent-led exploration
  - better task-transition hygiene
  - stronger long-term carry-forward
  - lower hallucination / shortcut / premature-closure risk
  - higher-quality autonomous work with less expert supervision

#### Required reading

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.codex/hooks.json`
- `.planning/config.json`
- `.planning/LONG-ARC.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-orchestrator-underdelegation-dirty-transitions.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-recursive-gsd-orchestration.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-manual-substitute-planning.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-premature-stall-diagnosis.md`
- relevant `.codex/get-shit-done` workflows/templates bearing on the recommendations

## Shared Bundle Constraints

- classify the work as `initial architecture research/planning`
- keep exploration repo-grounded rather than generic
- write directly to the owned output file only
- do not revert unrelated work
- do not silently flatten uncertainty or overclaim closure

## Why This Split

- Lane 1 captures the immediate failure pattern in this session and converts it into operating rules.
- Lane 2 checks whether the framework structurally supports the repo's long-horizon doctrine rather than relying on local heroics.
- Lane 3 turns the first two lanes into concrete mechanisms and candidate commands/skills rather than a vague process memo.

## Audit Note

This launch bundle spec was written after the subagents were launched because the original launch had not yet been persisted as a repo artifact. That omission is itself a process/auditability failure and should be treated as part of the broader orchestration-guardrail problem.
