---
id: sig-2026-04-08-codex-reasoning-effort-mismatch
type: signal
project: prix-guesser
tags: [codex, runtime, reasoning-effort, delegation, harness-bug]
created: 2026-04-09T00:10:00Z
updated: 2026-04-09T00:10:00Z
durability: workaround
status: active
severity: critical
signal_type: config-mismatch
signal_category: negative
polarity: negative
response_disposition: investigate
phase: 1
detection_method: manual
origin: codex-runtime-investigation
runtime: codex-cli
model: gpt-5.4
lifecycle_state: triaged
lifecycle_log:
  - "detected at 2026-04-09T00:10:00Z: spawn_agent requests for 'high' consistently landing as 'xhigh' for planner/checker roles"
  - "triaged at 2026-04-09T00:10:00Z: root cause unproven, workaround documented"
confidence: high
confidence_basis: "Proven from logs_1.sqlite (requested) vs state_5.sqlite (effective). Three planner/checker spawns confirmed mismatched. Control case (default agent) matched correctly."
evidence:
  supporting:
    - "Planner 019d6f70: requested high, effective xhigh"
    - "Checker 019d6f76: requested high, effective xhigh"
    - "Planner 019d6f81: requested high, effective xhigh"
    - "Control agent 019d6f7c (default role): requested high, effective high — matched correctly"
    - "Changing plan_mode_reasoning_effort from xhigh to high did not fix it"
  counter:
    - "Exact mechanism not found in accessible config or hook files"
depends_on:
  - "codex-cli runtime behavior — may change with updates"
triage:
  decision: investigate
  rationale: "Root cause unproven. Something in Codex harness auto-promotes planner/checker roles to xhigh regardless of requested effort."
  priority: high
  by: user
  at: 2026-04-09T00:10:00Z
---

# Codex Silently Promotes Planner/Checker Reasoning Effort

## What happened

When spawning `gsd-planner` and `gsd-plan-checker` agents with `gpt-5.4` at `high` reasoning effort, the effective child-thread reasoning consistently landed as `xhigh`. A control spawn of a default (non-role) agent with the same settings correctly landed as `high`.

## Investigation performed

- `~/.codex/config.toml` had `plan_mode_reasoning_effort = "xhigh"` — changed to `high`, re-tested, still promoted
- No hooks directory found under `~/.codex/`
- No explicit `xhigh` override in agent TOML files or `.planning/config.json`
- Promotion appears to be an internal Codex harness behavior tied to agent role names

## Impact

- Planner/checker loops may run with different reasoning characteristics than intended
- Requested spawn args cannot be trusted as proof of effective launch settings
- Cost and latency implications of xhigh vs high

## Workaround

AGENTS.md now requires verifying effective launch settings from runtime state after every spawn. If requested and effective differ: stop, kill the agent, report the mismatch.
