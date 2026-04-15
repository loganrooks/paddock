# Workflow

This document defines the repo's human and agent operating workflow.

`AGENTS.md` is intentionally narrower. It should contain only agent-facing runtime rules, model/delegation policy, and source-of-truth pointers. Broader git, devops, and artifact process lives here and in:

- [AI-GUARDRAILS.md](./AI-GUARDRAILS.md)
- [ARTIFACT-GOVERNANCE.md](./ARTIFACT-GOVERNANCE.md)

## Current posture

- Solo-developer project using agentic AI for planning, research, review, and execution assistance.
- Repo uses regular repo-local GSD for Codex, not Reflect.
- Current product center is still the Milestone 01 anchor mode, not the full adjacent-mode portfolio.
- Planning is intentionally future-aware, but current execution should stay narrow.
- Phase 01 is currently at a pre-rerun boundary: use a fresh discuss+plan pass before treating the existing `01-*` bundle as execution-approved.

## Legal and branding posture

- Treat the project as an unofficial F1-adjacent fan project.
- Do not brand the product using `F1`, `Formula 1`, or related marks as the primary product brand without an explicit decision.
- Driver names, team names, circuits, and factual references may be used as referential content, but public-facing surfaces should carry a clear disclaimer that the project is not affiliated with Formula One.
- Current benchmark posture comes from the repo's legal research and BoxBoxd comparison work, especially [.planning/research/2026-04-11-f1-fan-project-legal-landscape/06-synthesis.md](./.planning/research/2026-04-11-f1-fan-project-legal-landscape/06-synthesis.md).
- This workflow is not legal advice. If the project moves toward public launch, paid access, or stronger commercial posture, revisit the legal research before shipping.

## Git workflow

### Branching

- Do not work directly on `main` for substantive code or canon changes.
- Prefer short-lived branches with explicit scope.
- Suggested branch prefixes:
  - `feat/`
  - `fix/`
  - `chore/`
  - `docs/`
  - `planning/`
  - `spike/`
  - `archive/`
  - `research-archive/`
- One branch should usually correspond to one coherent objective or one tightly related change set.

### Commits

- Keep commits reviewable and scoped.
- Separate planning/canon changes from implementation changes when practical.
- Do not mix bulky generated artifacts into unrelated code commits.
- If a change updates canon docs because of a planning conclusion, include the reasoning artifact in the same branch.
- For load-bearing planning/process work, make checkpoint commits at meaningful reasoning or scope boundaries once the current artifact set can stand on its own.
- Good checkpoint boundaries include:
  - initial internally coherent synthesis
  - later external/comparative pressure
  - revision or integration in response to that pressure
- Avoid checkpoint commits that are only time-based or that split one still-dependent reasoning unit awkwardly.

### Delegated work checkpoints

- Before delegating substantial bounded edits, establish an auditable baseline and clean task boundary.
- Preferred order:
  1. if the current state is coherent, checkpoint it
  2. if it is not coherent, split or park it first
  3. only then delegate the next substantial edit pass
- After a worker returns:
  - review and disposition the result before committing it
  - do not auto-commit merely because the worker finished
  - if a verification lane is warranted, treat that as a new stage with its own review boundary
  - if a fix lane follows verification, prefer a checkpoint between findings and fixes when the findings artifact is worth preserving

### Merge posture

- Prefer PR-style review boundaries even when working solo.
- Prefer squash merge for most branches unless preserving a multi-commit audit trail is especially useful.
- Before merge, verify that the branch can be explained in one short paragraph. If not, the branch is probably too mixed.

### Branch protection recommendations

These should be implemented in the remote host when available:

- protect `main`
- disallow force-push to `main`
- disallow deletion of `main`
- require PRs to merge to `main`
- require status checks before merge
- require branch to be up to date before merge

## Verification ladder

### Planning or canon changes

- Verify internal consistency against the live source-of-truth docs.
- For non-trivial planning/canon changes, produce or preserve a verification artifact.
- If a planning change supersedes older steering, mark that relationship explicitly rather than silently leaving both live.

### Code changes

- Run the narrowest meaningful test or validation command first.
- If no automated validation exists, state that plainly and do a manual reasoning pass.
- For non-trivial changes, prefer a separate verification or code-review pass before merge.

### Exploratory or research work

- Distinguish evidence from inference.
- Record source quality where it matters.
- If a lane is exploratory, do not present speculative structure as settled canon.
- For load-bearing planning/process artifacts, expose source-basis on load-bearing claims when a reader could confuse:
  - repo-internal support
  - externally grounded support
  - or reasoned but not externally validated recommendation
- Treat repo-state diagnosis and repo-internal mechanism review as legitimately internal when that is the real evidence base, but do not let that silently masquerade as broader externally grounded best practice.

## Session continuity

- For resumed or compaction-affected sessions doing load-bearing work, run a short continuity check rather than trusting the thread blindly.
- Repo checklist:
  - `.planning/SESSION-REENTRY-CHECKLIST.md`
- Prefer fresh-thread boundaries at meaningful checkpoints over letting one thread absorb repeated compactions.
- Treat `/status` and similar UI surfaces as advisory when they conflict with direct repo state or observed behavior.

## DevOps minimum

Before the project grows much further, keep these basics in place:

- one reproducible local bootstrap path
- one reproducible test or validation entry point
- explicit secret handling outside the repo
- a simple rollback posture for deployed environments
- basic logging/observability once any public or semi-public runtime exists
- backup or export posture for authored content and canonical planning docs

## Solo + AI operating norms

- Optimize for controlled velocity, not maximum autonomous throughput.
- Use agents for bounded work with clear outputs.
- Keep human judgment at the boundaries where mistakes would be expensive:
  legal posture, roadmap/canon shifts, monetization, destructive cleanup, public branding, and infra changes.
- When a task would create a lot of repo surface, decide first whether that surface is meant to be canonical, historical, generated, or disposable.

## GSD-specific note

- Treat repo-local GSD config as harness-state that may change faster than this workflow doctrine.
- Verify the current automation posture in `.planning/config.json` when it matters.
- Until branch automation changes intentionally, branch discipline must be enforced by repo convention rather than assumed from GSD.
- If branch automation is introduced later, update this document and `AGENTS.md` together.

## Codex hooks posture

- Codex hooks are available as an experimental runtime feature, but they are not the primary enforcement layer for this repo.
- Current hook inventory and exact pilot behavior live in `.codex/hooks.json`; treat those details as harness-state, not durable workflow doctrine.
- Use `.codex/hooks.json`, not legacy `[[hooks]]` config stanzas.
- Keep hooks short, deterministic, and easy to remove.
- Do not use hooks as a substitute for branch protection, CI, source-of-truth docs, or explicit review boundaries.
- If a hook pilot becomes noisy, flaky, or hard to explain, remove it quickly rather than letting it become ambient workflow sludge.

## Maintenance rule

Review this document when any of the following changes:

- branching or merge policy
- remote branch protection settings
- validation/CI expectations
- legal/public-launch posture
- solo+AI signoff rules
- artifact retention policy

If one of those changes, update this file first and then adjust `AGENTS.md` only where agent-facing behavior actually changes.
