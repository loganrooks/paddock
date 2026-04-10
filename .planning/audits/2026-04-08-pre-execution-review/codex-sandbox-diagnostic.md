# Codex Sandbox Diagnostic Report

**Date**: 2026-04-08  
**System**: dionysus (Intel Xeon W-2125, Ubuntu 24.04.4 LTS, kernel 6.14.0-36-generic)  
**Investigator**: Claude Code agent (claude-sonnet-4-6)  
**Symptom**: `codex exec --full-auto` fails with `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted` on every shell command

---

## 1. Environment Facts (Confirmed)

| Fact | Value | Source |
|------|-------|--------|
| bwrap version | 0.9.0-1ubuntu0.1 (amd64) | `dpkg -l bubblewrap` |
| bwrap binary path | `/usr/bin/bwrap` | `which bwrap` |
| Ubuntu version | 24.04.4 LTS (Noble) | `lsb_release -a` |
| Kernel version | 6.14.0-36-generic | `uname -r` |
| `kernel.unprivileged_userns_clone` | 1 (enabled) | `sysctl kernel.unprivileged_userns_clone` |
| `user.max_user_namespaces` | 126623 | `sysctl user.max_user_namespaces` |
| `kernel.apparmor_restrict_unprivileged_userns` | **1 (enabled)** | `sysctl kernel.apparmor_restrict_unprivileged_userns` |
| AppArmor module loaded | yes | `aa-status` output header |
| Landlock ABI version | **6** (fully operational) | `syscall(LANDLOCK_CREATE_RULESET, NULL, 0, LANDLOCK_CREATE_RULESET_VERSION)` returns 6 |
| Current AppArmor domain (this shell) | `unconfined` | `cat /proc/self/attr/current` |
| Codex binary type | Rust binary (musl static) | path: `.../x86_64-unknown-linux-musl/codex/codex` |
| `--full-auto` maps to | `--sandbox workspace-write` | `codex exec --help` |

---

## 2. Root Cause Analysis

### 2.1 The Causal Chain (Evidence-Backed)

**Step 1 — Codex invokes bwrap with `--unshare-net`**

[CONFIRMED] The Codex binary contains the literal string `--unshare-net` in its embedded bwrap command template for the `workspace-write` (and other) sandbox modes. Evidence from `strings` on the binary:

```
--unshare-net
workspace-write sandbox template must parse:
danger-full-access sandbox template must parse:
```

The `workspace-write` sandbox also creates a user namespace (`--unshare-user`) to allow unprivileged filesystem isolation. Creating a new network namespace alongside a new user namespace requires setting up a loopback interface (`lo`) inside the network namespace, which bwrap does immediately after `unshare()`. Setting up the loopback requires the `CAP_NET_ADMIN` capability (netlink operation `RTM_NEWADDR`).

**Step 2 — Ubuntu 24.04 AppArmor restricts unprivileged user namespaces**

[CONFIRMED] Ubuntu 24.04 introduced `kernel.apparmor_restrict_unprivileged_userns = 1` as a default security hardening measure. When this sysctl is `1`, any process that creates an unprivileged user namespace is automatically **transitioned** into the restricted AppArmor profile named `unprivileged_userns`, regardless of the parent process's domain.

This is confirmed by the journalctl audit log, which shows the exact transition happening:

```
apparmor="AUDIT" operation="userns_create" class="namespace"
  info="Userns create - transitioning profile"
  profile="unconfined" pid=1479808 comm="bwrap"
  requested="userns_create" target="unprivileged_userns"
```

**Step 3 — The `unprivileged_userns` profile denies all capabilities**

[CONFIRMED] The profile at `/etc/apparmor.d/unprivileged_userns` contains:

```
profile unprivileged_userns {
    audit deny capability,   # <-- ALL capabilities denied, audited
    ...
    allow network,
    ...
}
```

The `audit deny capability` rule denies every capability. Even though the process has `CAP_NET_ADMIN` within its new user namespace (user namespaces grant a full capability set for the namespace), AppArmor's MAC layer overrides this and denies the capability exercise.

**Step 4 — bwrap fails with the observed error**

[CONFIRMED] The audit log shows the exact denials that cause the failure:

```
apparmor="DENIED" operation="capable" class="cap"
  profile="unprivileged_userns" pid=1479811 comm="bwrap"
  capability=12  capname="net_admin"
```

`net_admin` (capability 12) is required for `RTM_NEWADDR` — the netlink message that adds an IP address to the loopback interface. Without it, the `RTM_NEWADDR` netlink operation returns `EPERM`, which bwrap reports as:

```
bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted
```

The `setpcap` (capability 8) denial is also logged and would prevent bwrap from adjusting its capability set inside the sandbox.

Additionally, the log shows AppArmor denying bwrap's attempt to write its UID map (`proc/PID/uid_map`), which is a secondary failure:

```
apparmor="DENIED" operation="open" class="file"
  profile="unprivileged_userns" name="proc/1488347/uid_map"
  requested_mask="wr" denied_mask="wr"
```

This would cause a `Permission denied` error even if the loopback issue were resolved.

### 2.2 Why This Happens in Ubuntu 24.04 Specifically

The `kernel.apparmor_restrict_unprivileged_userns` sysctl was added in Ubuntu's AppArmor kernel patches and enabled by default in Ubuntu 24.04 LTS. It is not an upstream kernel feature — it is Ubuntu-specific and not present in vanilla kernels. The feature forces user namespace creation through AppArmor mediation using a restricted profile (`unprivileged_userns`) that strips all capabilities from processes entering user namespaces.

This interacts fatally with bwrap because bwrap's entire sandbox model for network isolation relies on having `CAP_NET_ADMIN` inside its new user+network namespace.

### 2.3 Why the Kernel Version Is Not the Root Cause

[CONFIRMED NOT ROOT CAUSE] The note about "broken HWE kernel package set" refers to a failed package install, not a missing kernel feature. The kernel 6.14.0-36-generic fully supports:
- Unprivileged user namespaces (`unprivileged_userns_clone = 1`, `max_user_namespaces = 126623`)
- Landlock ABI v6 (verified by syscall returning version 6)
- Network namespaces

The failure is exclusively AppArmor policy enforcement, not kernel capability absence.

---

## 3. Is tmux a Factor?

**[CONFIRMED NOT A FACTOR]**

The AppArmor domain of the shell running this investigation (inside Claude Code → tmux → SSH) is `unconfined`, verified by `cat /proc/self/attr/current` returning `unconfined`. The `unconfined` domain places no restrictions on the parent process.

The AppArmor restriction fires only at the moment bwrap calls `unshare()` to create a user namespace. At that instant, the kernel transitions the new child process into the `unprivileged_userns` profile. This transition happens regardless of what domain the parent was in — it is triggered by the namespace creation event itself, not by the parent's domain.

The same failure would occur running `codex exec --full-auto` directly in an SSH session without tmux, or from any `unconfined` process. tmux is not the cause.

---

## 4. Recommended Fixes

### Fix A — Disable AppArmor unprivileged userns restriction system-wide (requires root)

**Command**:
```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```

**To persist across reboots**, add to `/etc/sysctl.d/99-userns.conf`:
```
kernel.apparmor_restrict_unprivileged_userns=0
```
Then run `sudo sysctl --system`.

**Tradeoffs**:
- SIMPLE. One command, immediately effective.
- Removes a security protection that Ubuntu added deliberately. This machine is a development server (not internet-facing services), so the risk is lower than for a production host.
- Affects all unprivileged namespace creation system-wide, not just bwrap/Codex.

### Fix B — Create an AppArmor local override to allow bwrap's capabilities (requires root)

Create `/etc/apparmor.d/local/unprivileged_userns` with content that allows the specific capabilities bwrap needs:

```
# Allow bwrap to set up network namespace loopback
allow capability net_admin,
allow capability setpcap,
# Allow bwrap to write UID/GID maps
allow /proc/*/uid_map rw,
allow /proc/*/gid_map rw,
allow /proc/*/setgroups rw,
```

Then reload: `sudo apparmor_parser -r /etc/apparmor.d/unprivileged_userns`

**Tradeoffs**:
- More surgical than Fix A — only relaxes specific capabilities for user namespace processes, not all restrictions.
- Requires root and a correct AppArmor policy edit. The `local/unprivileged_userns` file is included by the base profile via `include if exists <local/unprivileged_userns>` (confirmed in the profile).
- Still requires root and AppArmor profile reload.

### Fix C — Use Codex's Landlock sandbox instead of bwrap (no root required)

[CONFIRMED AVAILABLE] Landlock ABI v6 is operational on this kernel (verified). The Codex binary contains a feature flag `use_legacy_landlock` with description "Opt-in: use the legacy Landlock Linux sandbox fallback."

To enable, add to `~/.codex/config.toml`:
```toml
[features]
use_legacy_landlock = true
use_linux_sandbox_bwrap = false
```

Or pass at invocation:
```bash
codex exec --full-auto -c 'features.use_legacy_landlock=true' -c 'features.use_linux_sandbox_bwrap=false'
```

**Tradeoffs**:
- Requires NO root. Entirely within user space.
- Landlock provides filesystem access control without requiring user namespaces or `CAP_NET_ADMIN`. It does not sandbox the network namespace.
- The sandboxing is less comprehensive than bwrap (no network namespace isolation), but provides real filesystem protection (Landlock restricts which paths processes can access).
- The label "legacy" is concerning in naming but the underlying Landlock ABI v6 is the current implementation. The naming may reflect that this was Codex's original sandbox before bwrap was added.

### Fix D — Bypass sandboxing entirely (no root required)

Use `codex exec --dangerously-bypass-approvals-and-sandbox` or set `sandbox = "danger-full-access"` in config.

**Tradeoffs**:
- No root needed. Immediate workaround.
- Completely removes sandboxing. The Codex help text explicitly warns: "EXTREMELY DANGEROUS. Intended solely for running in environments that are externally sandboxed."
- Acceptable only if Codex is running in an already-isolated environment (container, VM, etc.). Dionysus is a shared development machine, so this should be a last resort.

---

## 5. Recommended Approach for This Environment

Given that dionysus is a personal development server (not shared multi-tenant, not internet-facing services), the recommended resolution order is:

1. **First try Fix C** (Landlock, no root needed): Add the feature flags to `~/.codex/config.toml`. This requires no privileges and preserves filesystem sandboxing. Verify with a test `codex exec --full-auto "echo hello"`.

2. **If Fix C is insufficient** (e.g., Landlock doesn't provide enough coverage for workspace-write use cases): Apply Fix A (disable userns restriction system-wide) with `sudo sysctl`. The machine is a single-user development server, and the practical security risk is low.

3. **Avoid Fix D** unless running inside a Docker container or VM.

---

## 6. What We Still Don't Know

1. **Whether `use_linux_sandbox_bwrap = false` + `use_legacy_landlock = true` is a fully supported configuration** or an internal/experimental path. The "legacy" label suggests it may be less actively maintained. This needs a live test to confirm the sandbox actually activates and behaves correctly.

2. **Whether Fix B (AppArmor local override) would fully restore bwrap functionality** or whether other capability denials would surface. The two confirmed denials (`net_admin`, `setpcap`) and the uid_map write denial are the ones observed, but there may be others that only appear after the initial failures are resolved.

3. **The exact scope of `use_linux_sandbox_bwrap`**: The binary contains both `use_linux_sandbox_bwrap` and `use_legacy_landlock` as separate feature flags. It is unclear whether setting `use_linux_sandbox_bwrap = false` automatically activates Landlock, or whether both flags must be explicitly set.

4. **Whether the broken HWE kernel package set causes any instability** at the kernel level. The kernel itself works (evidenced by Landlock v6 being functional), but the package inconsistency could cause issues on the next kernel update.

---

## 7. Evidence Chain Summary

```
codex exec --full-auto
  -> --sandbox workspace-write
  -> codex-linux-sandbox invokes bwrap with --unshare-user --unshare-net [CONFIRMED via binary strings]
  -> bwrap calls unshare(CLONE_NEWUSER | CLONE_NEWNET)
  -> AppArmor intercepts userns_create [CONFIRMED via journalctl audit log]
  -> kernel transitions bwrap child into "unprivileged_userns" profile
     [CONFIRMED: kernel.apparmor_restrict_unprivileged_userns=1]
  -> "unprivileged_userns" profile has "audit deny capability" [CONFIRMED via /etc/apparmor.d/unprivileged_userns]
  -> CAP_NET_ADMIN (12) denied [CONFIRMED: journalctl shows DENIED capability=12]
  -> bwrap's RTM_NEWADDR netlink call returns EPERM
  -> bwrap prints "loopback: Failed RTM_NEWADDR: Operation not permitted"
  -> sandbox exits with error before any shell command runs
```
