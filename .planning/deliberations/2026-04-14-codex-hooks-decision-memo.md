# Codex Hooks Decision Memo

## Purpose

Decide whether this repo should immediately adopt Codex hooks as an enforcement mechanism, and if not, what posture should govern later experimentation.

## What Is Known

- `codex_hooks` is enabled in the local runtime and repo config, but the feature is marked `under development`.
- Current official docs center hook configuration on `.codex/hooks.json`, not legacy `[[hooks]]` TOML stanzas.
- Current documented events are `SessionStart`, `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, and `Stop`.
- Current official docs and open-source code both indicate partial coverage: the reliable current surface is command-style handling, especially around simple Bash calls.
- This repo did not have an active `.codex/hooks.json` pilot. It did have a stale legacy hook stanza in `.codex/config.toml` pointing to a missing script.

## Decision

- Remove the stale legacy hook stanza from `.codex/config.toml`.
- Treat `.codex/hooks.json` as the only supported repo-local hook surface for this repo.
- Adopt a **minimal live pilot**, not a broad hook system.
- Do not use hooks as the primary enforcement layer for git hygiene, CI, source-of-truth policy, or research rigor.

## Rationale

- The feature is still experimental and partially covered.
- Hooks cannot currently substitute for branch protection, CI, or source-of-truth docs.
- The current repo problem is not “no automation exists”; it is that policy, planning state, and artifact retention need clearer operating boundaries first.
- A bad hook pilot will create ambient workflow friction faster than it creates safety.

## Approved Posture

- Hooks act as belt-and-suspenders guardrails, not the main policy layer.
- The active pilot is repo-local, short, deterministic, and easy to remove.
- Current live pilots are limited to:
  - `SessionStart` reminder covering dirty-tree state, `main` branch, and current rerun-boundary context
  - narrow `PreToolUse` destructive-Bash tripwire

## Explicit Non-Decisions

- No `Stop` hook pilot yet.
- No `PostToolUse` enforcement layer yet.
- No prompt-rewriting or prompt-redaction hook policy yet.
- No assumption that hooks can police MCP, web, or all write surfaces reliably.

## Live Pilot Files

- `.codex/hooks.json`
- `.codex/hooks/session_start_guardrail.py`
- `.codex/hooks/pre_tool_use_guardrail.py`

## Revisit Trigger

Revisit once:

- the working tree is materially cleaner
- the branch/archive posture is actually being followed
- there is one narrowly defined pain point worth automating

## Sources

- https://developers.openai.com/codex/hooks
- https://developers.openai.com/codex/config-advanced
- https://developers.openai.com/codex/config-reference
- https://developers.openai.com/codex/agent-approvals-security
- https://raw.githubusercontent.com/openai/codex/main/codex-rs/hooks/src/engine/discovery.rs
- `.codex/config.toml`
- `~/.codex/config.toml`
