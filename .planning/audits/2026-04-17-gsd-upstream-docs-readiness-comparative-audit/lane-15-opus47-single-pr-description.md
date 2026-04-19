# Title
docs: authoritative shipped-surface inventory with filesystem-backed parity tests

# Body
## Why

The broad docs drifted from what actually ships. Readers were acting on wrong defaults (`workflow.discuss_mode: standard`, `claude_md_path: null`, ghost `resolve_model_ids` key), stale exhaustiveness claims ("All 18/21 agents", "35 references", "19 modules"), and surfaces that shipped in v1.36 but had no entry anywhere (`/gsd-graphify`, `--validate`, `gsd-read-injection-scanner`, the 10 advanced agents). Piecemeal fixes would keep losing this race. This PR picks a different shape: one authoritative roster file, narrative docs reconciled against it, and tests that fail when either side drifts.

## What changed

**`docs/INVENTORY.md` (new, authoritative).** A single file enumerating every shipped surface in all six families — 31 agents, 75 commands, 72 workflows, 41 references, 24 CLI modules, 11 hooks — each row carrying a one-line role, spawner/invoker, and source link. Other docs are permitted to be narrative or curated; INVENTORY is the source of truth when they disagree.

**Five parity tests in `tests/`.** Each test walks the filesystem and asserts every shipped artifact is accounted for in INVENTORY:

- `inventory-counts` — `## Agents (N shipped)` style headers must match `ls` for all six families. No hardcoded numbers on either side.
- `commands-doc-parity` — every `commands/gsd/*.md` must appear as a `### /gsd-<name>` heading in `COMMANDS.md` or a row in INVENTORY.
- `agents-doc-parity` / `cli-modules-doc-parity` / `hooks-doc-parity` — every shipped agent/module/hook must have a row in INVENTORY (AGENTS.md, CLI-TOOLS.md, and ARCHITECTURE.md's hook table are allowed to be curated subsets).

**Broad docs reconciled against INVENTORY.**

- `AGENTS.md`: header corrected from "21 specialized agents" to "21 primary + 10 advanced (31 shipped)"; new *Advanced and Specialized Agents* section with role cards for the 10 previously-omitted agents (pattern-mapper, debug-session-manager, code-reviewer, code-fixer, ai-researcher, domain-researcher, eval-planner, eval-auditor, framework-selector, intel-updater); Tool Permissions Summary footnoted as primary-agents-only.
- `ARCHITECTURE.md`: stale "35 references" / "19 modules" counts replaced with pointers to INVENTORY; hook table expanded to the 11 shipped hooks (`gsd-read-injection-scanner`, `gsd-check-update-worker` added); installation-layout hook enumeration collapsed to `*.js` / `*.sh` pattern; "Agent Spawn Categories" relabelled *Primary* with a footer naming the 10 advanced agents.
- `USER-GUIDE.md`: duplicate Command Reference and Configuration Reference sections collapsed into short pointers to `COMMANDS.md` / `CONFIGURATION.md` / `workflow-discuss-mode.md`. Eliminates the ghost `resolve_model_ids` key and the stale `discuss_mode: standard` default that lived only in this file.
- `CONFIGURATION.md`: `workflow.security_*` moved under `workflow.*` to match `templates/config.json` and the SDK runtime reads; `planning.sub_repos` added; new Graphify Settings section; `claude_md_path` default corrected to `./CLAUDE.md`; `workflow.tdd_mode` provenance corrected to v1.36.
- `COMMANDS.md` / `CLI-TOOLS.md`: `/gsd-graphify` section (build/query/status/diff + config gate); `--validate` and list/status/resume for `/gsd-quick`; list/close/status subcommands for `/gsd-thread`; graphify verb-family + Graphify/Learnings rows in the Module Architecture table; `audit`, `gsd2-import`, `intel` rows and `signal-*`, `audit-open`, `from-gsd2` verbs added.
- `FEATURES.md`: TOC reordered chronologically (v1.32 → v1.34 → v1.35 → v1.36); v1.36 TOC entries and body added for #116 TDD Pipeline Mode and #117 Knowledge Graph Integration.
- `README.md`: exhaustiveness claims dropped ("Complete feature", "Every command", "All 18 agents"); version-pinned v1.32 bullet replaced with a CHANGELOG pointer.
- `workflow-discuss-mode.md`: invocations normalized to `node gsd-tools.cjs config-set`.

## Validation

`node --test tests/inventory-counts.test.cjs tests/commands-doc-parity.test.cjs tests/agents-doc-parity.test.cjs tests/cli-modules-doc-parity.test.cjs tests/hooks-doc-parity.test.cjs` passes against the current tree. All five tests compute expected values from the filesystem at runtime — merging a new command/agent/hook/module without an INVENTORY row will fail CI at the parity boundary.

Reviewer guidance: read `docs/INVENTORY.md` first (it defines the contract), then the five `tests/*-doc-parity.test.cjs` files (they enforce it), then skim the narrative-doc diffs for tone. The AGENTS.md advanced-agent cards and the USER-GUIDE.md delete-and-link are the two largest prose changes.

## Follow-up

`VALID_CONFIG_KEYS` in `bin/lib/config.cjs` does not yet include `workflow.security_*` or `planning.sub_repos`, so `config-set` rejects keys that the shipped template and SDK runtime both read. Pre-existing validator gap; this PR documents the keys where they actually live but does not widen the validator.
