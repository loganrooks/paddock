# AGENTS.md

## Project Context

This repository is using regular GSD for Codex, not GSD Reflect.

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
- Keep product decisions explicit, but do not prematurely lock open design questions that were intentionally preserved in discovery.
- This project now uses `workflow.discuss_mode: exploratory` in `.planning/config.json`.
- Treat `CONTEXT.md` as a steering brief: decisions, assumptions, open questions, canonical refs, code context, and future awareness all matter downstream.

## Current Product Posture

- unofficial private-only F1 fan project
- geography/circuit guessing is the anchor mode
- likely social shape is private rooms, couch play, or host-screen plus phone controllers
- long-term expansion into adjacent F1 party modes remains open

## Notes For Future Agents

- The most important early architectural decisions are likely the authored round/content model and the room authority model.
- Do not collapse those into a premature frontend-framework choice.
- Circuit-internal recognition is the primary fantasy; venue-approach clues are secondary and should not silently replace it.
- Process lesson: if planner/checker agents fail or stall, do not treat manually written PLAN artifacts as equivalent to a properly verified GSD planning pass. Either restore the planning/checking path or perform stricter local validation before any execution attempt.
- Orchestration lesson: do not treat short agent silence as proof of failure. Use a proper gauntlet first: allow a longer uninterrupted run, check for artifact output or commits, send one status probe, and only then classify the agent path as blocked.
- Plan-authoring rule: never put create-target files in a task's `read_first` list. `read_first` is only for files that already exist and must be inspected before edits. For create-from-scratch tasks, point `read_first` at existing source-of-truth or reference files instead.
- Environment rule: do not assume bare `pnpm` exists on PATH in this repo. Prefer `corepack pnpm` unless the environment has already proven otherwise.
