# Lane 14: PR4 Continuation Report

> Continuation of the previous execution lane (which ended only because its conversation context grew too long).
> Scope strictly limited to completing PR4 on top of the existing local branch stack (`docs/pr4-consistency-drift-guards`).
> No push, no PR, no remote activity, no localized doc changes, no CHANGELOG edits, no revisit of PR1/PR2/PR3.

---

## Final State

- **Branch:** `docs/pr4-consistency-drift-guards`
- **Head SHA:** `4f3de809d684773fd2e8ecd40bbe768fae083adb`
- **Parent:** `88eeb7e` (PR3 head: `docs: make inventory authoritative and reconcile architecture`)
- **Commit message:** `test(docs): add consistency guards and remove duplicate refs`

## Files Changed

| File | Change |
|------|--------|
| `docs/USER-GUIDE.md` | Replaced the ~220-line Command Reference + Configuration Reference subsections (lines ~471–640 pre-edit) with a three-bullet link block pointing at `docs/COMMANDS.md`, `docs/CONFIGURATION.md`, and `docs/workflow-discuss-mode.md`, plus a paragraph naming the drift incidents that motivated the delete (`workflow.discuss_mode`, `claude_md_path`, the abbreviated model-profile table) and two `<!-- -->` comments marking what was removed (including the `resolve_model_ids` ghost key). TOC updated: the two separate anchors `#command-reference` and `#configuration-reference` collapsed into one `#command-and-configuration-reference` entry. |
| `docs/FEATURES.md` | TOC reordered chronologically: v1.32 now precedes v1.34.0 / v1.35.0 / v1.36.0 (v1.33 has no dedicated feature section). Body section order unchanged — it was already chronological. |
| `docs/ARCHITECTURE.md` | Hook table (L207–218 pre-edit) expanded from 9 rows to 11 — `gsd-read-injection-scanner.js` (`PostToolUse`) and `gsd-check-update-worker.js` (helper worker) added, with a trailing "See [INVENTORY.md](...hooks-11-shipped) for the authoritative 11-hook roster" pointer. Installation File Layout (L414–432 pre-edit) hook enumeration collapsed from three named files (`gsd-statusline.js`, `gsd-context-monitor.js`, `gsd-check-update.js`) to two pattern lines: `hooks/*.js` and `hooks/*.sh`. The `# N …` count annotations on the other tree lines (slash commands, domain modules, workflow definitions, etc.) were preserved/refreshed (75/24/72/41/31) because `tests/command-count-sync.test.cjs` locks `# N slash commands` against the filesystem; removing those annotations would have broken a pre-existing CI guard. |
| `docs/CLI-TOOLS.md` | Module Architecture table: added three rows — `audit.cjs`, `gsd2-import.cjs`, `intel.cjs`. State Commands block: added `state begin-phase`, `state signal-waiting`, `state signal-resume` entries. Utility Commands block: added `audit-open` and `from-gsd2` entries. Skill Manifest section was already present at lines 316–328 (left alone). |
| `docs/workflow-discuss-mode.md` | Two invocation lines normalized: `gsd-tools config-set` → `node gsd-tools.cjs config-set` to match the form used across `docs/CLI-TOOLS.md` and CHANGELOG. |
| `tests/inventory-counts.test.cjs` | New. Locks the six "## Family (N shipped)" headline counts in `docs/INVENTORY.md` against `readdirSync` counts of `agents/gsd-*.md`, `commands/gsd/*.md`, `get-shit-done/workflows/*.md`, `get-shit-done/references/*.md`, `get-shit-done/bin/lib/*.cjs`, and `hooks/*.{js,sh}`. 6 subtests; all passing. |
| `tests/commands-doc-parity.test.cjs` | New. For every `commands/gsd/*.md`, asserts the corresponding `/gsd-<slug>` appears either as a `###` heading in `docs/COMMANDS.md` or as a row in the INVENTORY.md Commands table. Normalizes `_`→`-` to handle the single legacy-underscore filename (`extract_learnings.md` → `/gsd-extract-learnings`). 75 subtests; all passing. |
| `tests/agents-doc-parity.test.cjs` | New. For every `agents/gsd-*.md`, asserts the agent name appears as a row in INVENTORY.md's Agents table (deliberately does not enforce AGENTS.md card presence — AGENTS.md is allowed to carry a curated subset under Phase 1). 31 subtests; all passing. |
| `tests/cli-modules-doc-parity.test.cjs` | New. For every `get-shit-done/bin/lib/*.cjs`, asserts the module appears as a row in INVENTORY.md's CLI Modules table. 24 subtests; all passing. |
| `tests/hooks-doc-parity.test.cjs` | New. For every `hooks/*.{js,sh}`, asserts the hook appears as a row in INVENTORY.md's Hooks table. 11 subtests; all passing. |

Pre-existing tests re-checked: `tests/command-count-sync.test.cjs` (4 subtests) and `tests/architecture-counts.test.cjs` (3 subtests) still pass.

## Pre-existing Dirty `docs/USER-GUIDE.md` Edit

**Preserved and extended.** The previous lane had already performed the substantive delete-and-link inside the Command And Configuration Reference block (lines ~468–482). I left that substantive content (the three link bullets, the drift-rationale paragraph, and the two `<!-- -->` removal markers) intact and only completed the loose ends it had not yet finished:

1. Updated the TOC entries at the top of the file (lines 14–15 pre-edit) — the prior lane had merged the section but the TOC still listed two separate entries pointing at `#command-reference` and `#configuration-reference` that no longer existed. Collapsed to one entry pointing at `#command-and-configuration-reference`.
2. Verified no other in-file cross-links referenced the removed anchors (`grep -n "Command Reference\|Configuration Reference\|#command-reference\|#configuration-reference"` — the remaining hit at line 674 is a cross-file link to `CONFIGURATION.md#non-claude-runtimes-...` and is correct).
3. Verified the `INVENTORY.md#commands-75-shipped` fragment the prior lane had written actually resolves (it does — `## Commands (75 shipped)` renders as `#commands-75-shipped`).

Nothing in the prior-lane partial edit was reverted or replaced.

## Lane-12 Recommendations I Revised Against Live Repo State

1. **Lane-12 recommended collapsing the *entire* installation-layout tree to pattern form, including dropping the `# 75 slash commands` / `# 19 domain modules` / etc. counts.** I kept the non-hook count annotations and only collapsed the hook enumeration. Reason: `tests/command-count-sync.test.cjs` has a pre-existing assertion that matches the regex `commands/gsd/\*\.md[^\n]*#\s*(\d+)\s+slash commands` against the filesystem — silently removing that annotation would have caused a CI regression outside PR4's stated scope. I also refreshed the inline `19` → `24` (domain modules) and `35` → `41` (references) counts in the tree so the unlocked counts at least match the filesystem; PR3 had updated the prose counts but left the tree annotations stale.
2. **Lane-12 mentioned `skill-manifest` as a "missing verb" in CLI-TOOLS.md.** `docs/CLI-TOOLS.md` lines 316–328 already contain a full Skill Manifest section (two invocation examples plus a paragraph describing the returned JSON schema). No edit needed; left alone. The other three verbs it named (`from-gsd2`, `audit-open`, `state signal-*`) were genuinely missing and were added.

## Intentionally Deferred

- **PR5 content beyond PR4's scope** — e.g. the Phase-2 AGENTS.md structural redesign (delete 31 role cards, reposition AGENTS.md as a narrative about how agents work) and the localization backport. Both are explicitly out of scope per lane-12 and per the continuation brief.
- **`docs/ARCHITECTURE.md` Agent Spawn Categories relabel** — lane-12 assigned this edit to revised-PR3, not PR4. The live file already carries the relabel ("Conceptual spawn-pattern taxonomy for the 21 primary agents. For the authoritative 31-agent roster… see [INVENTORY.md](...)") at line 277, confirming PR3 landed that edit. No PR4 action.
- **`workflow-discuss-mode.md` deeper rewrite** — only the two invocation lines were normalized. The rest of the file was stable under prior lanes.

## Test Results Summary

```
$ node --test tests/inventory-counts.test.cjs tests/commands-doc-parity.test.cjs \
               tests/agents-doc-parity.test.cjs tests/cli-modules-doc-parity.test.cjs \
               tests/hooks-doc-parity.test.cjs
# tests 147, # pass 147, # fail 0

$ node --test tests/command-count-sync.test.cjs tests/architecture-counts.test.cjs
# tests 8, # pass 8, # fail 0
```

## Commit Policy Compliance

- Local commit only; no push. ✓
- Committed on `docs/pr4-consistency-drift-guards`. ✓
- Uses the suggested commit message (`test(docs): add consistency guards and remove duplicate refs`). ✓
- No remotes touched, no PR opened. ✓
- No CHANGELOG or localized-docs edits. ✓
