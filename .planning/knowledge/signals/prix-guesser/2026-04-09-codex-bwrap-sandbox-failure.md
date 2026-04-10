---
id: sig-2026-04-09-codex-bwrap-sandbox-failure
type: signal
project: prix-guesser
tags: [codex, sandbox, bwrap, apparmor, ubuntu-24.04, infrastructure]
created: 2026-04-09T04:00:00Z
updated: 2026-04-09T04:10:00Z
durability: workaround
status: active
severity: critical
signal_type: config-mismatch
signal_category: negative
polarity: negative
response_disposition: fix
phase: 1
detection_method: manual
origin: codex-exec-failure-during-audit
runtime: claude-code
model: claude-opus-4-6
lifecycle_state: remediated
lifecycle_log:
  - "detected at 2026-04-09T04:00:00Z: codex exec --full-auto fails with bwrap loopback RTM_NEWADDR permission denied"
  - "remediated at 2026-04-09T04:10:00Z: switched to Landlock sandbox via config.toml, verified working"
confidence: high
confidence_basis: "Full causal chain confirmed from journalctl AppArmor audit logs, bwrap --unshare-net in Codex binary strings, and kernel.apparmor_restrict_unprivileged_userns=1 sysctl."
evidence:
  supporting:
    - "journalctl shows apparmor=AUDIT operation=userns_create profile=unconfined comm=bwrap target=unprivileged_userns"
    - "journalctl shows apparmor=DENIED operation=capable profile=unprivileged_userns comm=bwrap capability=12 capname=net_admin"
    - "strings on Codex binary confirms --unshare-net in workspace-write sandbox template"
    - "sysctl kernel.apparmor_restrict_unprivileged_userns = 1 confirmed"
    - "Landlock ABI v6 confirmed available as alternative"
  counter: []
triage:
  decision: address
  rationale: "Codex exec completely non-functional without fix — all shell commands denied"
  priority: critical
  by: user
  at: 2026-04-09T04:00:00Z
remediation:
  status: complete
  approach: "Added use_legacy_landlock=true and use_linux_sandbox_bwrap=false to ~/.codex/config.toml [features] section. Switches from bwrap (requires user namespaces) to Landlock (kernel-native, no namespace needed). Verified working."
  at: 2026-04-09T04:10:00Z
verification:
  status: passed
  method: active-retest
  evidence_required: "codex exec runs shell commands successfully"
  at: 2026-04-09T04:10:00Z
depends_on:
  - "Ubuntu 24.04 with kernel.apparmor_restrict_unprivileged_userns=1"
  - "Codex CLI using bwrap sandbox by default"
---

# Codex bwrap Sandbox Fails on Ubuntu 24.04 Due to AppArmor Namespace Restrictions

## What happened

`codex exec --full-auto` (which uses `--sandbox workspace-write`) failed on every shell command with `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`. No Codex agent could read files or run any command.

## Root cause

Ubuntu 24.04 sets `kernel.apparmor_restrict_unprivileged_userns=1` by default. When bwrap calls `unshare(CLONE_NEWUSER | CLONE_NEWNET)`, AppArmor auto-transitions the process into the `unprivileged_userns` profile which denies all capabilities, including `CAP_NET_ADMIN` needed to configure the loopback interface.

**Not caused by:** tmux, the kernel version, Docker, or the broken HWE kernel package.

## Fix applied

Added to `~/.codex/config.toml` under `[features]`:
```toml
use_legacy_landlock = true
use_linux_sandbox_bwrap = false
```

Switches to Landlock sandbox backend (kernel ABI v6 confirmed). Loses network namespace isolation but retains filesystem access control. Verified working.

## Alternative fix (requires root)

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```
