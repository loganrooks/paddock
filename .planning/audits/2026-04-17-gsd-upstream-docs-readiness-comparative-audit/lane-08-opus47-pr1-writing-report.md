# Lane 08: PR 1 Writing Pass Report

## Scope

Targeted docs-only edits implementing PR 1 ("trust-bug hotfix bundle") from lane-07's proposal, against branch `docs/pr1-trust-bug-hotfixes` of `get-shit-done-upstream`. No PR 2+ content, no CHANGELOG edits, no new files, no commits.

## Requested PR 1 Fixes — Status

All 8 requested fixes were verified as still needed against the current branch tip and applied.

| # | File | Change | Status |
|---|------|--------|--------|
| 1 | `docs/README.md:12,13` | Weaken "Complete feature..." and "Every command..." language | Applied |
| 2 | `docs/README.md:16` | Remove stale "All 18 specialized agents" claim | Applied |
| 3 | `docs/README.md:23` | Replace "What's new in v1.32" bullet with CHANGELOG pointer | Applied |
| 4 | `docs/CONFIGURATION.md:98` | `claude_md_path` Full Schema default: `null` → `"./CLAUDE.md"` | Applied |
| 5 | `docs/CONFIGURATION.md:114` | `claude_md_path` core settings table default: `(none)` → `./CLAUDE.md` | Applied |
| 6 | `docs/CONFIGURATION.md:146` | `workflow.tdd_mode` provenance: "Added in v1.37" → "Added in v1.36" | Applied |
| 7 | `docs/USER-GUIDE.md:626` | `workflow.discuss_mode` default: `standard` → `discuss` | Applied |
| 8 | `docs/AGENTS.md:3` | Weaken "All 21 specialized agents" header (minimal PR 1 fix) | Applied |

## Skipped (already fixed on current main)

None. Every requested fix was still outstanding on the branch tip.

## Edit Details

- **README.md line 12**: Replaced "Complete feature and function documentation with requirements" with "Feature narratives and requirements for released features (see CHANGELOG for latest additions)". Inlined a CHANGELOG link.
- **README.md line 13**: Replaced "Every command with syntax..." with "Stable commands with syntax...".
- **README.md line 16**: Replaced "All 18 specialized agents — roles, tools, spawn patterns" with "Role cards for primary agents — roles, tools, spawn patterns (the `agents/` filesystem is authoritative)".
- **README.md line 23**: Replaced the version-pinned "What's new in v1.32: ..." bullet with "What's new: see CHANGELOG for current release notes, and upstream README for release highlights".
- **CONFIGURATION.md line 98**: `"claude_md_path": null` → `"claude_md_path": "./CLAUDE.md"`.
- **CONFIGURATION.md line 114**: Default cell `(none)` → `` `./CLAUDE.md` ``. Also tightened description sentence to state the default explicitly (`"Defaults to ./CLAUDE.md at the project root"`) rather than use the stale `(none)` wording.
- **CONFIGURATION.md line 146**: `workflow.tdd_mode` "Added in v1.37" → "Added in v1.36".
- **USER-GUIDE.md line 626**: `workflow.discuss_mode` row — Options corrected `standard, assumptions` → `discuss, assumptions` (the stale mode name was accompanying the stale default); Default `standard` → `discuss`.
- **AGENTS.md line 3**: Minimum PR 1 truth fix only — reworded header from "All 21 specialized agents —" to "Role cards for 21 specialized agents —" and appended a pointer to the authoritative `agents/` directory. Did not touch category table, tool-permission summary, or add the 10 missing agents (those are PR 3 scope per lane-07).

## Ambiguities / Concerns

1. **USER-GUIDE.md Options cell for `discuss_mode` (line 626)**: The cell listed `standard, assumptions` as the option set. The CONFIGURATION.md authoritative row (line 136) uses `discuss` and `assumptions`. I changed the Options cell to `discuss, assumptions` alongside the default fix, since leaving the stale enum string would have contradicted the corrected default. This is within the spirit of PR 1's "trust-bug" scope (matching documented behavior to shipped behavior) but is technically one token beyond the literal "change default" instruction. Flagging for reviewer visibility.

2. **AGENTS.md line 3 wording**: The instruction says "make only the minimal PR 1 truth fix". I interpreted "minimal" as eliminating the false exhaustiveness claim ("All 21 specialized agents" is false because shipped roster is 31 per lane-01c/lane-07). I chose the minimal-delta phrasing "Role cards for 21 specialized agents" plus a filesystem-authoritative footnote. This preserves the 21 count as descriptive of the doc's current coverage without claiming the doc is the complete roster. Alternative minimal phrasing ("21 specialized agents — roles...") would drop only the word "All"; my choice adds a filesystem pointer. If the reviewer prefers the narrower one-word delete, this can be reduced further.

3. **CONFIGURATION.md line 114 description edit**: Lane-07 item 6 says "tighten the description sentence since `(none)` carries connotations the corrected default does not." I made a light one-sentence tightening (`"Defaults to ./CLAUDE.md at the project root."`) rather than a full rewrite. Still within PR 1 scope.

4. **Hook read-before-edit warnings**: The PostToolUse/PreToolUse hook fired repeatedly warning me I hadn't read files before editing them. I had in fact read all target files during this session before editing. All Edit operations succeeded — the warnings did not block. Worth noting in case the hook is over-reporting.

## Out-of-Scope (confirmed not done)

- No new file `docs/INVENTORY.md`
- No CHANGELOG.md touches
- No `/gsd-graphify` additions to COMMANDS / FEATURES / CLI-TOOLS (PR 2)
- No `/gsd-quick` or `/gsd-thread` signature refresh (PR 2)
- No `security_*` schema relocation (PR 2)
- No `planning.sub_repos` row addition (PR 2)
- No agent inventory catchup, no new "Advanced and Specialized Agents" section, no category-table expansion in AGENTS.md (PR 3)
- No model-profile table expansion in CONFIGURATION.md (PR 3)
- No ARCHITECTURE.md / USER-GUIDE.md structural moves (PR 4)
- No FEATURES.md TOC reorder, no hook-list reconciliation, no workflow-discuss-mode.md invocation-syntax fix (PR 5)
- No commit created

## Files Modified

- `docs/README.md`
- `docs/CONFIGURATION.md`
- `docs/USER-GUIDE.md`
- `docs/AGENTS.md`

Diff size estimate: ~11 line-changes across 4 files, consistent with lane-07's "~10 line-changes total" PR 1 size target.
