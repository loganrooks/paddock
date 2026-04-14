# AGENTS.md

## Project Context

This repository is using regular GSD for Codex, not GSD Reflect.

This file is intentionally agent-facing.

For broader repo workflow, human signoff rules, and artifact-retention policy, also read:

- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`

GSD for this project is repo-local. Do not assume a global `$HOME/.codex/get-shit-done` install is the active runtime.

The active local runtime for this project lives at:
- `.codex/get-shit-done`

The local installation command is:
- `./scripts/setup-portable-gsd.sh`

That script:
- installs regular repo-local GSD for Codex
- reapplies this repo's tracked overlay in `tooling/portable-gsd/overlay/`
- preserves the exploratory discuss-phase and future-aware `CONTEXT.md` behavior expected by this project

Do not use:
- `~/.codex/get-shit-done-reflect`
- any Reflect-specific workflow, config, or skill path

If GSD needs to be reinstalled for this repo, reinstall the regular Codex-local version with the command above.

## Initialization

This project began with a pre-GSD discovery pass.

The discovery package lives in:
- `discovery/`

The consolidated seed document for project initialization is:
- `discovery/14-gsd-seed.md`

If `.planning/` does not exist yet, initialize the project from that seed using regular GSD:

```bash
$gsd-new-project --auto @discovery/14-gsd-seed.md
```

## Workflow Expectations

- Prefer the local project GSD install over any global or reflect-flavored install.
- Treat `discovery/` as upstream exploratory context, not as the active implementation workflow state.
- Once initialized, treat `.planning/` as the canonical project workflow state.
- Treat `.planning/STATE.md`, `.planning/ROADMAP.md`, and the active phase docs as the live operational state. Do not let `AGENTS.md` become the place where current project status is manually tracked.
- For non-phase-bound research or deliberation, prefer the repo-local `gsd-rigorous-research` skill over ad hoc research structure.
- Keep product decisions explicit, but do not prematurely lock open design questions that were intentionally preserved in discovery.
- This project now uses `workflow.discuss_mode: exploratory` in `.planning/config.json`.
- Treat `CONTEXT.md` as a steering brief: decisions, assumptions, open questions, canonical refs, code context, and future awareness all matter downstream.

## Current Product Posture

- unofficial private-only F1 fan project
- geography/circuit guessing is the anchor mode
- likely social shape is private rooms, couch play, or host-screen plus phone controllers
- long-term expansion into adjacent F1 party modes remains open
- do not brand the product primarily with F1 marks without an explicit decision; public-facing surfaces should carry a non-affiliation disclaimer

## Notes For Future Agents

- The most important early architectural decisions are likely the authored round/content model and the room authority model.
- Do not collapse those into a premature frontend-framework choice.
- Distinguish `general architectural exposure` from `large-scale player-count / massive-room research`.
- A general architectural exposure pass should ask which promising game shapes pressure early substrate decisions and which future directions might be silently foreclosed.
- A large-scale player-count pass should be treated as a separate research track unless the user explicitly wants them combined. Do not mix “broad promising-ideas architecture audit” with “how far could we scale to 50+ or massive rooms?” into one muddy lane.
- Questions about `50+` or larger player support often require external comparative research on relevant reference designs, case studies, and latency/topology tradeoffs, not just internal ideation.
- Before launching a mixed-scope architecture lane, stop and discuss the split with the user first.
- Circuit-internal recognition is the primary fantasy; venue-approach clues are secondary and should not silently replace it.
- Codex GSD orchestration must happen at the top level. The main orchestrator should run the workflow logic itself and spawn role agents directly (`gsd-phase-researcher`, `gsd-planner`, `gsd-plan-checker`, `gsd-executor`) rather than spawning a generic agent whose job is to invoke a GSD skill.
- Do not create recursive GSD call graphs like `orchestrator -> generic agent -> gsd-plan-phase skill -> gsd-planner`. That introduces broken-telephone risk and makes debugging much harder.
- When agent orchestration is needed, prefer high-reasoning top-level orchestration and keep the call graph explicit before launching anything.
- Codex-native model policy for this repo: top-level orchestration should prefer `gpt-5.4` with `xhigh` reasoning.
- Execution and verification agents should prefer `gpt-5.4` with `high` reasoning unless a narrower task justifies less.
- For the first couple of phases, planning-related agents may use `gpt-5.4` with `xhigh` reasoning when extra rigor is worth the latency. In practice this applies to `gsd-phase-researcher` and `gsd-planner` during early architecture-setting work.
- Replanning, revision, and gap-closure planning should use `gpt-5.4` with `high` reasoning. Do not use `xhigh` for checker-driven plan fixes or gap-filling passes.
- `gsd-plan-checker` is treated as a verification agent for reasoning policy and should stay at `gpt-5.4` with `high` reasoning.
- Before every agent spawn, re-read this `AGENTS.md` section instead of relying on memory.
- Before every agent spawn, classify the task explicitly as one of: initial architecture research/planning, replanning/revision/gap-filling, or execution/verification.
- Before every delegation, state the exact mapping in one line in commentary using the format `agent -> model -> reasoning` so the chosen model and reasoning level are visible and auditable.
- If a user intervention changes delegation policy mid-turn, that intervention overrides any prior delegation plan immediately.
- If a spawn-policy mistake is detected, stop the delegation loop and correct policy adherence before spawning anything else.
- Never report requested spawn settings as if they prove the effective launch settings. Requested `spawn_agent` arguments and the runtime-persisted child-thread settings are separate facts.
- For this Codex environment, verify effective launched settings against the local runtime state after every spawn before claiming the launch matched policy. In practice: requested settings come from `~/.codex/logs_1.sqlite` or `~/.codex/log/codex-tui.log`; effective launched settings come from `~/.codex/state_5.sqlite` child-thread rows.
- If requested and effective launch settings differ, stop immediately, kill the agent, and report the mismatch plainly. Do not defend the request as if it were the launch.
- Repo config pins the core GSD role models via `.planning/config.json` `model_overrides`. Do not rely on legacy `opus`/`sonnet` labels to mean anything precise in Codex.
- Codex hooks are experimentally available in this repo, and a narrow repo-local pilot now lives in `.codex/hooks.json`.
- Current live hook scope is intentionally small: `SessionStart` dirty-tree / branch / rerun-boundary reminder plus a `PreToolUse` destructive-Bash tripwire.
- Do not expand hooks into a broad enforcement layer without an explicit decision, and do not rely on legacy `[[hooks]]` stanzas in `.codex/config.toml`.
- Process lesson: if planner/checker agents fail or stall, do not treat manually written PLAN artifacts as equivalent to a properly verified GSD planning pass. Either restore the planning/checking path or perform stricter local validation before any execution attempt.
- Orchestration lesson: do not treat short agent silence as proof of failure. Use a proper gauntlet first: allow a longer uninterrupted run, check for artifact output or commits, send one status probe, and only then classify the agent path as blocked.
- Plan-authoring rule: never put create-target files in a task's `read_first` list. `read_first` is only for files that already exist and must be inspected before edits. For create-from-scratch tasks, point `read_first` at existing source-of-truth or reference files instead.
- Environment rule: do not assume bare `pnpm` exists on PATH in this repo. Prefer `corepack pnpm` unless the environment has already proven otherwise.
- Maintenance rule: if this file starts carrying broad workflow, devops, retention, or signoff detail that belongs in the reference docs above, move that detail out instead of letting `AGENTS.md` become the only operating manual.
- Maintenance rule: if project posture, workflow policy, or source-of-truth references change, update `AGENTS.md` in the same change rather than letting it drift behind the repo's actual operating model.
