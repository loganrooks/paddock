# Portable GSD Overlay

This directory makes the repo-local Codex GSD runtime reproducible across machines without committing the live `.codex/` install.

## Why This Exists

The repo uses a local GSD install under `.codex/`, but that install is intentionally ignored by git and contains absolute paths tied to the current checkout location. Raw `.codex/` contents are therefore not portable by themselves.

This overlay solves that by tracking only the project-specific patched files and templating repo-root paths as `__PROJECT_ROOT__`.

## How It Works

1. [`scripts/setup-portable-gsd.sh`](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh) installs regular local GSD with:
   - `npx get-shit-done-cc --codex --local`
2. The script validates [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json), which explicitly types every tracked overlay file as either:
   - `overwrite` — deliberate replacement of an upstream-shipped surface already backed by `backup-meta.json`
   - `add` — deliberate additive repo-local owner outside the updater/carried-subset backup surface
3. The script then copies the tracked overlay files into `.codex/`
4. While copying, it replaces `__PROJECT_ROOT__` with the current checkout path
5. It also materializes the compact prompt selector:
   - repo default: `tooling/compact-prompts/project.md`
   - one-off override: `PRIX_COMPACT_PROMPT_FILE=tooling/compact-prompts/readiness.md ./scripts/setup-portable-gsd.sh`
   - persistent worktree-local override: first line of `.codex.local/compact-prompt.txt`
6. After overlay copy and reasoning-default application, the script runs a post-materialization coherence gate so the live `.codex/` frontier must still match the tracked overlay/install contract.

Compact prompt paths are config values relative to `.codex/`.

## What The Overlay Changes

The overlay currently patches regular local GSD so this project gets:

- `workflow.discuss_mode: exploratory` as the local default
- exploratory discuss behavior as a real mode, not just a convention
- richer `CONTEXT.md` steering briefs
- `future_awareness` support in context generation
- research/planning prompts that consume assumptions, open questions, and future-aware constraints
- a general project compact prompt as the repo default instead of a readiness-specific global pin

## Overlay Contract

The tracked overlay now carries an explicit install contract instead of relying on ambient knowledge:

- [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/portable_gsd_contract.py)

That shared contract is now used by:

- the installer
- post-materialization coherence verification
- runtime visibility classification of install-mutation targets

This keeps overlay ownership, backup-carried overwrite truth, and additive repo-local owners from drifting silently apart.

## Codex Model Policy

This repo treats Codex model selection as a repo-level policy, not an implicit runtime default.

- `.planning/config.json` uses `model_overrides` to pin core GSD role agents to `gpt-5.4`
- top-level orchestration is expected to use `gpt-5.4` with `xhigh` reasoning
- spawned core GSD role agents are expected to use `gpt-5.4` with `high` reasoning

This is intentionally separate from the legacy `opus` / `sonnet` / `haiku` profile tables, which are too ambiguous for Codex-native orchestration.

## Updating The Overlay

If you intentionally patch the local `.codex/` GSD runtime again, regenerate the overlay from the live patched files before committing:

```bash
repo_root="$(pwd)"
overlay_root="tooling/portable-gsd/overlay"
files=(
  ".codex/skills/gsd-discuss-phase/SKILL.md"
  ".codex/get-shit-done/bin/lib/config.cjs"
  ".codex/get-shit-done/templates/config.json"
  ".codex/get-shit-done/workflows/settings.md"
  ".codex/get-shit-done/references/planning-config.md"
  ".codex/get-shit-done/templates/context.md"
  ".codex/get-shit-done/workflows/discuss-phase.md"
  ".codex/get-shit-done/workflows/discuss-phase-power.md"
  ".codex/get-shit-done/workflows/research-phase.md"
  ".codex/get-shit-done/workflows/plan-phase.md"
)
```

Then rewrite each copied file so the current repo root becomes `__PROJECT_ROOT__`.
