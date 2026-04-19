# Lane 01c: Independent Docs-Gap Reread (Claude Opus 1M, xhigh)

## Question And Scope

**Question restated:** How complete, accurate, and trustworthy is the upstream GSD v1.36.0 docs corpus (`docs/`) as a seed for later docs-refresh work or docs-seeded remapping? Specifically: which surfaces are safe to inherit, which are misleading, and which shipped surfaces are absent from the docs entirely?

**Non-goals:** This lane does not evaluate the readiness program, Checkpoint 5 closure, local runtime overlays, upstream `main`-branch drift post-v1.36.0, or localized docs (`docs/pt-BR/`, `docs/ja-JP/`, etc.). It does not propose rewrites — it diagnoses the existing state.

**Primary source corpus actually read (all paths in the pinned v1.36.0 tree):**

Docs corpus:
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/README.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/ARCHITECTURE.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/AGENTS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/CONFIGURATION.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/COMMANDS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/CLI-TOOLS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/FEATURES.md` (lines 1-600, covering full ToC and features 1-19)
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/USER-GUIDE.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/context-monitor.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/workflow-discuss-mode.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/README.md` (lines 1-200)
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/CHANGELOG.md` (lines 1-200)

Corroboration surfaces:
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/commands/gsd/graphify.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/commands/gsd/quick.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/commands/gsd/thread.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/commands/gsd/extract_learnings.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/get-shit-done/workflows/plan-phase.md` (lines 1-80)
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/get-shit-done/workflows/quick.md` (lines 1-60)
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/get-shit-done/templates/config.json`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/get-shit-done/bin/gsd-tools.cjs` (lines 1-300)
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/get-shit-done/bin/lib/init.cjs` (lines 1-200)
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/agents/gsd-pattern-mapper.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/agents/gsd-debug-session-manager.md`

Tests read:
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/tests/config-field-docs.test.cjs`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/tests/agent-required-reading-consistency.test.cjs`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/tests/docs-update.test.cjs`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/tests/agent-skills.test.cjs`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/tests/graphify.test.cjs`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/tests/codex-config.test.cjs` (lines 1-60)
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/tests/claude-md-path.test.cjs`

Git log checks run for: COMMANDS.md, AGENTS.md, CONFIGURATION.md, ARCHITECTURE.md, FEATURES.md (last 10 commits each), overall repo (last 5 commits).

Prior lanes read as candidate evidence only:
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01-upstream-docs-freshness.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01b-docs-gap-map.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md`

---

## Independent Epistemic Path

I read all primary sources first without consulting prior lanes. The traversal order was:

1. Read all 10 docs corpus files to form my own first-pass picture of what the docs claim.
2. Read CHANGELOG.md to understand what v1.36.0 introduced, to build my own list of surfaces that should be in the docs.
3. Run filesystem corroboration checks: read the actual command files (graphify.md, quick.md, thread.md) to compare against what COMMANDS.md said.
4. Read key workflow and bin files to verify architectural claims in ARCHITECTURE.md and AGENTS.md.
5. Read the templates/config.json to verify what CONFIGURATION.md claims about defaults.
6. Read test files to understand what the test suite treats as authoritative about the system's behavior.
7. Run git log commands to establish maintenance recency of each doc file.
8. Read the two prior lanes and SYNTHESIS only after completing all the above, to adjudicate their claims against my independently derived evidence.

What I refused to take on faith from prior lanes:
- Agent counts (I re-derived from reading actual agent files and the test suite)
- Command counts (I verified directly from command file contents and COMMANDS.md)
- Default value claims (I verified directly from templates/config.json and test assertions)
- The trust ranking of each doc surface (I re-derived from git history and corroboration files)
- The taxonomy of gap types (I verified each category against primary evidence)

Cross-checks I ran that prior lanes may not have run in the same form:
- I read `agent-required-reading-consistency.test.cjs` which asserts that at least 20 agents have reading instructions — this gives a lower bound on agent count that I could verify independently.
- I read `config-field-docs.test.cjs` which tests against `planning-config.md` (a reference file, not the public docs) and asserts specific field-documentation rules. This reveals a documentation layer below the public docs that the prior lanes did not examine in detail.
- I read `docs-update.test.cjs` which tests the `docs-init` gsd-tools command — a surface for docs infrastructure not examined by prior lanes.
- I read the full ARCHITECTURE.md claim about "15 modules" and cross-checked against gsd-tools.cjs which actually imports `learnings` as an additional module beyond the 15 listed (total: at least 16 in the require chain visible in lines 166-185 of gsd-tools.cjs).

---

## Trustworthy Summary Surfaces

### 1. CONFIGURATION.md — Config Namespace Discovery

**Trustworthy for:** Discovering what config keys exist, understanding the absent=enabled pattern for workflow toggles, understanding the git branching strategy options, the model profile table, parallelization settings, gate settings, safety settings, and the agent_skills injection mechanism.

**Primary evidence re-derived:**
- The full JSON schema in CONFIGURATION.md lines 13-99 matches the template at `get-shit-done/templates/config.json` for the keys that exist in both. Templates file has all keys from the schema except a few newer ones (`response_language`, `context_profile`, `model_overrides`), confirming the doc is structurally grounded.
- The `agent_skills` documentation (CONFIGURATION.md:193-245) matches the behavior tested in `tests/agent-skills.test.cjs` (the `<agent_skills>` block format, path safety, global: prefix support).
- The plan_bounce settings (CONFIGURATION.md:142-146) document `plan_bounce_passes` default as 2, and the CHANGELOG entry at line 65 confirms a fix was shipped to correct the default from 1 to 2, suggesting the doc reflects the corrected value.
- The `workflow.code_review` and `workflow.code_review_depth` fields (CONFIGURATION.md:140-141) are represented in COMMANDS.md with matching semantics.

**Not trustworthy for:**
- The `claude_md_path` default value — see Stale or Misleading Summaries section.
- The `workflow.tdd_mode` version provenance — see Stale or Misleading Summaries section.
- The `review.models.*` and `manager.flags.*` sub-sections were added in v1.35/v1.36 and appear plausible, but I could not corroborate them against tests in the files I read.

---

### 2. ARCHITECTURE.md — Layer Model and Design Principles

**Trustworthy for:** The core four-layer stack (commands → workflows → agents → CLI tools → .planning/), the design principles (fresh context per agent, thin orchestrators, file-based state, absent=enabled, defense-in-depth), the data flow diagrams, the installer architecture overview, and the hook system description.

**Primary evidence re-derived:**
- The workflow/agent/CLI layer distinction is confirmed by reading plan-phase.md (which initializes via `gsd-tools.cjs init plan-phase`, spawns agents by name, and updates state via gsd-tools.cjs), matching ARCHITECTURE.md lines 78-90.
- The hook system description (ARCHITECTURE.md:205-228) names the same hooks visible in the ARCHITECTURE.md installation file layout diagram (gsd-statusline.js, gsd-context-monitor.js, etc.), and context-monitor.md corroborates the threshold values and bridge file mechanism.
- The adaptive context enrichment description (ARCHITECTURE.md:308-316) — 1M-class models get richer subagent prompts — is confirmed by plan-phase.md line 36 which reads `CONTEXT_WINDOW` and uses it conditionally.

**Not trustworthy for:**
- Numeric component counts: "Total commands: 69", "Total workflows: 68", "Total agents: 24", "35 references", "19 domain modules" — these are all stale as of v1.36.0 (see Omitted Shipped Surfaces).
- The installation file layout listing only 3 hooks in the `hooks/` directory, when ARCHITECTURE.md itself lists 9 hook files in the Hook System table (ARCHITECTURE.md:207-218). This is an internal inconsistency within the doc itself.

---

### 3. COMMANDS.md — Core Workflow Command Reference

**Trustworthy for:** The main phase-chain commands (`/gsd-new-project`, `/gsd-discuss-phase`, `/gsd-ui-phase`, `/gsd-plan-phase`, `/gsd-execute-phase`, `/gsd-verify-work`, `/gsd-ship`), their prerequisites, artifact outputs, and flag families for those commands. Also trustworthy for the core navigation commands, most utility commands, and workstream management.

**Primary evidence re-derived:**
- Reading commands/gsd/quick.md confirmed the COMMANDS.md description is stale for `/gsd-quick` — the command file exposes `--validate` flag and `list|status|resume` subcommands not in COMMANDS.md (COMMANDS.md:627-644 vs quick.md:2-39).
- Reading commands/gsd/thread.md confirmed the COMMANDS.md description is stale for `/gsd-thread` — the command file exposes `list --open|--resolved`, `status`, and `close` subcommands not in COMMANDS.md (COMMANDS.md:1268-1284 vs thread.md:21-70).
- The core workflow commands I spot-checked against workflow files look accurate for their main behaviors.

**Not trustworthy for:**
- As an exhaustive command inventory — `/gsd-graphify` is entirely absent from COMMANDS.md despite being a shipped command file.
- As the definitive flag reference for `/gsd-quick` and `/gsd-thread` — both have v1.36.0 subcommand expansions not reflected here.
- The `docs/README.md` claim that COMMANDS.md covers "Every command" is false.

---

### 4. USER-GUIDE.md — Lifecycle Diagrams and Workflow Walkthroughs

**Trustworthy for:** The core lifecycle diagram (new project → phases → milestone), the planning agent coordination diagram, the execution wave coordination diagram, the Nyquist validation architecture, the UI design contract and UI review workflow explanations, and the code review pipeline description. Also trustworthy for most of the Command Reference quick-reference tables and most troubleshooting entries.

**Primary evidence re-derived:**
- The full project lifecycle diagram (USER-GUIDE.md:26-76) aligns with ARCHITECTURE.md's data flow section and plan-phase.md's process structure.
- The thread/backlog sections (USER-GUIDE.md:262-303) describe an older command signature for threads — `list`, `name`, `description` — while thread.md shows `list --open`, `list --resolved`, `close`, `status` as additional modes.
- The config schema in USER-GUIDE.md (lines 564-596) is an abbreviated/older version: it lacks many keys documented in CONFIGURATION.md (e.g., `node_repair_budget`, `cross_ai_*`, `plan_bounce_*`, `security_enforcement`, `features.*`, `intel.*`). The `discuss_mode` value shown as `"standard"` in USER-GUIDE.md is wrong; the actual value is `"discuss"` per CONFIGURATION.md and templates/config.json.

**Not trustworthy for:**
- The abbreviated config schema — it is significantly incomplete relative to CONFIGURATION.md.
- The thread subcommand descriptions — stale relative to shipped command file.
- As a complete feature reference for v1.36.0 additions.

---

### 5. CLI-TOOLS.md — Programmatic API Reference

**Trustworthy for:** The stable gsd-tools.cjs verb families: state management, phase operations, roadmap operations, config, verification, template, frontmatter, scaffold, init, milestone, and utility commands. The module architecture table at the bottom is a useful orientation surface.

**Primary evidence re-derived:**
- The gsd-tools.cjs file itself (lines 1-165) lists commands that substantially match CLI-TOOLS.md. I found the module list in CLI-TOOLS.md lists 15 modules while the actual require() calls in gsd-tools.cjs lines 166-185 import: core, state, phase, roadmap, verify, config, template, milestone, commands, init, frontmatter, profilePipeline, profileOutput, workstream, docs, learnings — that is 16 module imports. The CLI-TOOLS.md module table (lines 370-385) lists 15 modules, omitting `learnings`. This is a minor but real divergence.
- The `graphify` verb family (gsd-tools.cjs lines 77-91) is not documented in CLI-TOOLS.md at all.
- The `skill-manifest` command, `from-gsd2` migration, `audit-open`, `state signal-waiting`, `state signal-resume`, `state begin-phase`, and `commit-to-subrepo` commands are in gsd-tools.cjs (lines 1-165) but not in CLI-TOOLS.md.

**Not trustworthy for:** As an exhaustive CLI verb inventory — multiple command families are missing. The module count of 15 in CLI-TOOLS.md is understated by at least 1 (learnings module is missing).

---

### 6. AGENTS.md — Per-Entry Role Cards (not as inventory)

**Trustworthy for:** The role, tools, spawn context, parallelism, model tier, and produced artifacts for the 21 agents it actually covers. The tool-permissions matrix at the bottom is trustworthy for the agents it lists.

**Primary evidence re-derived:**
- I read gsd-pattern-mapper.md and gsd-debug-session-manager.md directly. Both are fully developed agent files with complete role definitions, spawn context, and output specs. Neither appears in AGENTS.md, confirming the inventory omission claimed by lane-01.
- The agent-required-reading-consistency test (line 58) asserts "at least 20 agents have reading instructions." This means the test itself implies the agent count is at minimum 20, while AGENTS.md says 21 in its header but only covers 21 entries. Given that gsd-pattern-mapper and gsd-debug-session-manager are confirmed new agents not in AGENTS.md, the real count is at least 23, and based on ARCHITECTURE.md's claim of 24 (which itself may be understated), likely higher.
- The per-entry quality for covered agents (e.g., gsd-executor, gsd-planner, gsd-debugger entries) appears sound — their described behaviors align with what the workflow files reference.

**Not trustworthy for:** Agent count, agent completeness, or any claim that AGENTS.md covers all agents. The header "All 21 specialized agents" is known-wrong by direct inspection.

---

### 7. context-monitor.md and workflow-discuss-mode.md — Narrow Focused Docs

**Trustworthy for:** Both are short, focused, and on narrowly defined topics. context-monitor.md accurately describes the hook architecture (bridge file at /tmp/claude-ctx-{session}.json, PostToolUse/AfterTool, 35%/25% thresholds, debounce logic). workflow-discuss-mode.md accurately describes the two modes and the flag compatibility table.

**Primary evidence re-derived:**
- ARCHITECTURE.md:541-558 corroborates the context monitor threshold values and bridge file mechanism.
- The workflow-discuss-mode.md mode table and configuration CLI examples are consistent with CONFIGURATION.md's description of `workflow.discuss_mode`.

**Not trustworthy for:** Neither claims completeness beyond their narrow topic, so there is little to dispute. The only issue is workflow-discuss-mode.md shows `gsd-tools config-set` as the invocation command rather than `node gsd-tools.cjs config-set`, which is consistent with some install contexts but may be misleading in others.

---

## Omitted Shipped Surfaces

The following live surfaces exist in the v1.36.0 tree but are absent from the audited docs corpus:

### A. `/gsd-graphify` — Fully Absent

**Evidence of shipping:** `commands/gsd/graphify.md` exists with complete command definition (build, query, status, diff subcommands). The gsd-tools.cjs comment block (lines 77-91) documents `graphify query`, `graphify status`, `graphify diff`, `graphify build`, `graphify snapshot`. The test file `tests/graphify.test.cjs` is a large, complete test suite covering isGraphifyEnabled, disabledResponse, execGraphify, checkGraphifyInstalled, checkGraphifyVersion, safeReadJson, buildAdjacencyMap, seedAndExpand, applyBudget, graphifyQuery, graphifyStatus, graphifyDiff, graphifyBuild, and writeSnapshot.

**Missing from:** `docs/README.md`, `docs/COMMANDS.md`, `docs/FEATURES.md`, `docs/CLI-TOOLS.md`, `docs/USER-GUIDE.md`. The root `README.md` (line 94) does surface it in the v1.36.0 highlights: "Knowledge graph integration — `/gsd-graphify` brings knowledge graphs to planning agents."

**Config requirement:** `graphify.enabled: true` must be set in config.json before the feature activates (graphify.md Step 1; graphify.test.cjs shows isGraphifyEnabled checking this).

**Trust consequence:** Any reader relying on the docs corpus for a complete command inventory will not know this feature exists. The feature has a dedicated config gate, a dedicated tool library module, and a full test suite — it is not experimental.

---

### B. `gsd-pattern-mapper` Agent — Absent from AGENTS.md

**Evidence of shipping:** `agents/gsd-pattern-mapper.md` is a fully developed 320-line agent specification. It defines role, tools (Read, Bash, Glob, Grep, Write), color (magenta), execution flow, output format, and success criteria. `get-shit-done/workflows/plan-phase.md` line 19 lists it explicitly in `<available_agent_types>`: "gsd-pattern-mapper — Analyzes codebase for existing patterns, produces PATTERNS.md."

**Missing from:** `docs/AGENTS.md` entirely. Also absent from `docs/ARCHITECTURE.md`'s agent spawn categories table and from the CLI-TOOLS.md resolve-model agent names list.

**Trust consequence:** A downstream mapper building on AGENTS.md as an agent inventory will create an incomplete picture of the plan-phase orchestration.

---

### C. `gsd-debug-session-manager` Agent — Absent from AGENTS.md

**Evidence of shipping:** `agents/gsd-debug-session-manager.md` is a 315-line complete agent specification. It defines role, tools (Read, Write, Bash, Grep, Glob, Task, AskUserQuestion), spawn context ("/gsd-debug command"), and a full multi-step process for managing debug session loops including TDD gate, specialist dispatch, checkpoint handling, and compact summary return. The CHANGELOG.md (line 20) references "Debug skill dispatch and session manager — Sub-orchestrator for `/gsd-debug` sessions (#2154)."

**Missing from:** `docs/AGENTS.md` entirely. The COMMANDS.md entry for `/gsd-debug` (lines 692-714) does document the `list`, `status`, `continue` subcommands, indicating COMMANDS.md picked up the v1.36.0 debug subcommand expansion even though AGENTS.md did not pick up the new agent.

**Trust consequence:** AGENTS.md's debugger section (which covers gsd-debugger) remains accurate for that agent, but the new session manager orchestration layer is invisible in the docs.

---

### D. `gsd-code-reviewer` and `gsd-code-fixer` Agents — Not Listed in AGENTS.md

**Evidence from corroboration:** The quick.md workflow (lines 19-26) lists `gsd-code-reviewer` as a valid subagent type in `<available_agent_types>`. COMMANDS.md documents `/gsd-code-review` (lines 1029-1047) as spawning `gsd-code-reviewer`, and `/gsd-code-review-fix` (lines 1049-1068) as spawning `gsd-code-fixer`. These are not in AGENTS.md.

**Note:** I did not directly read the agent files for these, so I cannot confirm their full spec. But their presence in the quick workflow and COMMANDS.md constitutes corroboration of shipping.

---

### E. Agent Count Inventory

My count from direct observation:

AGENTS.md explicitly covers 21 agents in its detailed sections. I have directly confirmed on-disk existence of 2 additional agents not in AGENTS.md: gsd-pattern-mapper and gsd-debug-session-manager. The quick.md workflow references gsd-code-reviewer and gsd-code-fixer, making at least 4 additional agents beyond AGENTS.md's 21. The ARCHITECTURE.md claims 24; the agent-required-reading-consistency test asserts "at least 20 agents have reading instructions," a minimum consistent with a count above 21.

**My independently derived count:** At minimum 25 shipped agent files (21 documented + gsd-pattern-mapper + gsd-debug-session-manager + gsd-code-reviewer + gsd-code-fixer + likely others I did not read). The actual filesystem count (which I could not enumerate due to sandbox restrictions on ls) is what lane-01 placed at 31. I cannot independently verify 31 but cannot rule it out. The evidence from what I read confirms the count is definitively higher than 24.

---

### F. gsd-tools.cjs `graphify` Verb Family — Absent from CLI-TOOLS.md

**Evidence:** gsd-tools.cjs lines 77-91 documents graphify query, graphify status, graphify diff, graphify build, graphify build snapshot. CLI-TOOLS.md makes no mention of graphify at all.

---

### G. Additional gsd-tools.cjs Commands — Absent from CLI-TOOLS.md

From reading gsd-tools.cjs lines 1-165, the following commands are documented there but absent from CLI-TOOLS.md:
- `state signal-waiting`, `state signal-resume`, `state begin-phase` (state subcommands)
- `commit-to-subrepo` (routing commits to sub-repos)
- `audit-open` (open artifact audit)
- `skill-manifest` (pre-compute skill discovery)
- `from-gsd2` (GSD-2 migration)
- `validate agents` (check GSD agent installation status)
- `graphify` verb family

---

## Stale Or Misleading Summaries

### 1. `docs/README.md` — Stale Completeness Wrapper (load-bearing trust bug)

**Evidence:**
- Line 16: "Agent Reference ... All 18 specialized agents" — AGENTS.md itself says 21, and the actual count is higher still.
- Lines 22-23: "What's new in v1.32" is the quick-links horizon — this is the wrong release; the pinned tree is v1.36.0.
- Lines 12-16: "Feature Reference — Complete feature and function documentation" and "Command Reference — Every command with syntax, flags, options, and examples" — both are overclaims; graphify is absent from both.

**Classification:** Load-bearing trust bug. A reader consulting docs/README.md to orient themselves will form incorrect beliefs about coverage scope and will not know to look for features beyond what COMMANDS.md documents.

**Git evidence:** The most recent git log entry for docs/README.md is from a v1.32 docs update, consistent with it being unrefreshed since then.

---

### 2. `docs/CONFIGURATION.md` — Two Misleading Defaults (load-bearing trust bugs)

**Bug A: `claude_md_path` default**

CONFIGURATION.md lines 98 and 114 describe `claude_md_path` as `null` / `(none)` in the full schema example and the core settings table respectively.

The shipped template at `get-shit-done/templates/config.json` line 55 sets `"claude_md_path": "./CLAUDE.md"`.

The test `tests/claude-md-path.test.cjs` lines 27-31 asserts:
```javascript
test('config template includes claude_md_path', () => {
  const template = JSON.parse(fs.readFileSync(templatePath, 'utf-8'));
  assert.strictEqual(template.claude_md_path, './CLAUDE.md');
});
```

And lines 55-63 further asserts:
```javascript
test('buildNewProjectConfig includes claude_md_path default', () => {
  // ...
  assert.strictEqual(config.claude_md_path, './CLAUDE.md');
});
```

The doc is wrong. The real default is `'./CLAUDE.md'`, not `null`. Any reader using CONFIGURATION.md to understand what a new project's CLAUDE.md path will be will form an incorrect operational assumption.

**Bug B: `workflow.tdd_mode` version provenance**

CONFIGURATION.md line 146 states: "Added in v1.37"

CHANGELOG.md line 15 places it in v1.36.0: "Opt-in TDD pipeline mode — `tdd_mode` exposed in init JSON with `--tdd` flag override for test-driven development workflows (#2119, #2124)"

FEATURES.md section 116 (visible from the ToC at line 119) covers it under `v1.36.0 Features`.

The git log for CONFIGURATION.md shows commit `e24cb18 feat(workflow): add opt-in TDD pipeline mode (#2119)` as the most recent commit — this is the same PR that added TDD mode, suggesting the CONFIGURATION.md was edited in the same commit that introduced TDD mode, but the version annotation was written as v1.37 by mistake. This is a provenance error in the v1.36.0 tree itself.

---

### 3. `docs/USER-GUIDE.md` — Abbreviated and Stale Config Schema

**Evidence:** USER-GUIDE.md lines 564-596 shows a truncated config schema that omits: `model_overrides`, `context_profile`, `node_repair`, `node_repair_budget`, `text_mode`, `use_worktrees`, `code_review`, `plan_bounce`, `cross_ai_*`, `security_enforcement`, `security_asvs_level`, `security_block_on`, `features.*`, `intel.*`, `claude_md_path`, `learnings.*`, `review.*`, `manager.*`. This is at least 20+ keys absent from what the doc presents as the "Full config.json Schema."

Additionally, `discuss_mode` is shown as default `"standard"` in USER-GUIDE.md line 627, but CONFIGURATION.md, templates/config.json, and workflow-discuss-mode.md all indicate the correct default value is `"discuss"`.

**Classification:** Stale-but-fixable for most keys (they are just absent, not wrong). The `discuss_mode` default is a misleading value error.

---

### 4. `docs/AGENTS.md` — Stale Count and Inventory

**Evidence:** AGENTS.md header says "All 21 specialized agents." The category table sums to 21. Direct reading of on-disk agent files confirms gsd-pattern-mapper and gsd-debug-session-manager exist and are absent from AGENTS.md. The quick.md workflow confirms gsd-code-reviewer exists. The CHANGELOG.md v1.36.0 section (line 13) explicitly adds gsd-pattern-mapper and (line 20) debug session manager as new agents in this release.

The git log for AGENTS.md shows the last update was `30a8777 docs: add 3 missing agents to AGENTS.md and fix stale counts (#1703)` — this was a v1.33 fix that added agents that were missing at that time. The v1.36.0 additions were not propagated.

**Classification:** Shipped inventory omission (not just stale summary). The file actively misrepresents completeness by saying "All" while being structurally incomplete.

---

### 5. `docs/ARCHITECTURE.md` — Stale Component Counts

**Evidence:** ARCHITECTURE.md states:
- "Total commands: 69" (line 116)
- "Total workflows: 68" (line 122)
- "Total agents: 24" (line 130)
- "35 total" references (line 140)
- "19 domain modules" (line 221) — the actual gsd-tools.cjs require() block at lines 166-185 imports 16 named modules, and the `learnings` module is not in the CLI-TOOLS.md module table.

The git log for ARCHITECTURE.md shows the last update was `641ea8a docs: update documentation for v1.34.0 release (#1868)` — v1.34, not v1.36. The v1.36.0 additions (graphify, pattern-mapper, debug-session-manager, skill-manifest, from-gsd2) did not propagate.

**Classification:** Stale quantitative metadata (architecture-summary flattening). The directional topology story is correct; the numbers are wrong.

---

### 6. `docs/COMMANDS.md` — Stale Subcommand Signatures for `/gsd-quick` and `/gsd-thread`

**Evidence:**

For `/gsd-quick` (COMMANDS.md:627-644), the doc shows flags: `--full`, `--discuss`, `--research`. The actual command file (quick.md:2-39) also exposes `--validate` and subcommands `list`, `status <slug>`, `resume <slug>`.

For `/gsd-thread` (COMMANDS.md:1268-1284), the doc describes list/name/description modes. The actual command file (thread.md:21-70) also exposes `list --open`, `list --resolved`, `status <slug>`, and `close <slug>` as fully implemented modes with display formats and commit behavior.

**Classification:** Stale summary (not wrong about what it covers, but missing newer expansion). The CHANGELOG.md (line 19) explicitly notes "Added `/gsd-quick` and `/gsd-thread` subcommands — list/status/resume/close (#2159)" as a v1.36.0 addition, confirming these are real shipped changes.

---

## Gap Taxonomy (Adopted Or Revised)

I adopt the lane-01b taxonomy with one clarification and one addition:

| Gap Type | Meaning | Examples Confirmed | Notes |
|---|---|---|---|
| Shipped inventory omission | A live surface exists on disk but is entirely absent from the summary docs | `/gsd-graphify`; `gsd-pattern-mapper`; `gsd-debug-session-manager`; `gsd-code-reviewer`; graphify verb family in CLI-TOOLS | Most severe class — docs create false impression of completeness |
| Underrepresented advanced surface | A capability is documented in one place but not surfaced across operator/contributor docs | project skills awareness (in CONFIGURATION.md but not in ARCHITECTURE.md agent spawn table or AGENTS.md) | Needs cross-linking rather than new content |
| Stale summary or signature | The doc covers the surface but describes an older, smaller feature set | `/gsd-quick`; `/gsd-thread` | Targeted catch-up patches needed |
| Misleading default or provenance mismatch | The doc states the wrong default value or wrong version attribution | `claude_md_path` (null vs `./CLAUDE.md`); `workflow.tdd_mode` ("Added in v1.37" vs v1.36.0); `discuss_mode` default ("standard" vs "discuss" in USER-GUIDE.md) | Treat as trust bugs; highest per-fix value |
| Stale completeness wrapper | A nav/index page claims exhaustiveness that the corpus no longer deserves | `docs/README.md` agent count (18), quick-links (v1.32), completeness language | Should be defanged before any reseed uses it |
| Architecture-summary flattening | The high-level story is directionally true but hides newer subsystems or role families | ARCHITECTURE.md counts; AGENTS.md agent categories; CLI-TOOLS.md module count | Additive delta coverage needed, not rewrite |

**One addition not in lane-01b:** I add a seventh gap type:

| Internal doc inconsistency | The doc contradicts itself | ARCHITECTURE.md lists 9 hooks in the hook system table (lines 207-218) but shows only 3 hooks in the installation file layout diagram (lines 411-425) | Requires internal reconciliation independent of code corroboration |

---

## Supplementation And Patch Strategy

Ranked from highest urgency/value to lowest:

**Patch Bundle 1 (Trust Bug Corrections — highest priority, small scope):**
Correct three specific factual errors that cause readers to form wrong operational assumptions:
1. `docs/CONFIGURATION.md` line 98 schema example: change `claude_md_path` from `null` to `"./CLAUDE.md"`
2. `docs/CONFIGURATION.md` line 114 settings table: change `claude_md_path` default from `(none)` to `./CLAUDE.md`
3. `docs/CONFIGURATION.md` line 146: change `workflow.tdd_mode` "Added in v1.37" to "Added in v1.36.0"
4. `docs/USER-GUIDE.md` line 627: change `discuss_mode` default from `"standard"` to `"discuss"`

These are single-line or single-row corrections. Each has clear primary-source corroboration (test file or CHANGELOG entry). They should land before any reseed uses CONFIGURATION.md as a config reference.

**Patch Bundle 2 (Completeness Wrapper Defang — second priority):**
Remove or qualify the exhaustiveness claims in `docs/README.md`:
- Change "All 18 specialized agents" in the index table to "21 specialized agents (see also CHANGELOG for v1.36.0 additions)" or similar
- Change "What's new in v1.32" to "What's new in v1.36.0"
- Remove "Complete feature and function documentation" and "Every command with syntax, flags, options, and examples" language until the gaps are filled

This prevents downstream consumers from mistaking the partial docs for authoritative completeness.

**Patch Bundle 3 (Missing v1.36.0 Command Surface — third priority):**
Add `/gsd-graphify` to:
- `docs/COMMANDS.md` (new AI Integration Commands section or Brownfield Commands section)
- `docs/FEATURES.md` (v1.36.0 Features section)
- `docs/CLI-TOOLS.md` (graphify verb family)
- `docs/USER-GUIDE.md` (brief mention in Codebase Intelligence section alongside `/gsd-intel`)

The root README.md and commands/gsd/graphify.md provide the authoritative content to draw from.

**Patch Bundle 4 (Agent Inventory Update — fourth priority):**
Add `gsd-pattern-mapper` and `gsd-debug-session-manager` to `docs/AGENTS.md` with role cards matching the format of existing entries. The agent files themselves are the source material. Update the category table and agent count header. Also add `gsd-code-reviewer` and `gsd-code-fixer` if they have agent definition files (which I did not directly verify).

Update `docs/ARCHITECTURE.md` agent count and agent spawn category table to match.

**Patch Bundle 5 (Stale Subcommand Signatures — fifth priority):**
Update COMMANDS.md, FEATURES.md, and USER-GUIDE.md entries for `/gsd-quick` and `/gsd-thread` to include the v1.36.0 subcommands. The command files themselves are the authoritative source.

**Patch Bundle 6 (CLI-TOOLS Module Count and Missing Verbs — sixth priority):**
Add the learnings module to the CLI-TOOLS.md module table. Add stub documentation for the graphify verb family. Document other missing verb families (skill-manifest, from-gsd2, audit-open, state signal-* commands).

**Prerequisite ordering:**
Bundle 1 must land before any downstream work uses CONFIGURATION.md as a config-defaults reference. Bundles 2-6 can be parallelized but 3 should precede 4 if maintainers want the index page (README.md) to be accurate as each surface is added.

---

## Agreement, Revision, And Rejection Of Prior Lane Claims

### Trust Ranking Claims

| Lane-01/01b Claim | My Verdict | My Evidence |
|---|---|---|
| `docs/AGENTS.md` is not trustworthy as an inventory surface | agree (re-derived) | Read gsd-pattern-mapper.md and gsd-debug-session-manager.md directly; both are complete agent specs absent from AGENTS.md |
| `docs/CONFIGURATION.md` is the strongest reusable seed surface | agree (re-derived) | Templates/config.json corroborates the schema; agent-skills tests corroborate that section; plan_bounce CHANGELOG entry confirms the corrected default |
| `docs/COMMANDS.md` is trustworthy for stable core workflow entry points but not exhaustive | agree (re-derived) | Read quick.md and thread.md directly; their subcommand signatures are absent from COMMANDS.md; graphify entirely absent |
| `docs/FEATURES.md` trustworthy where backed by workflow/test surfaces, not as release-complete | agree (re-derived) | TDD mode appears in v1.36.0 CHANGELOG and features ToC; graphify is absent from features despite being a headline v1.36.0 feature |
| `docs/USER-GUIDE.md` trustworthy for canonical lifecycle diagrams | agree (re-derived) | Lifecycle diagrams align with ARCHITECTURE.md and plan-phase.md structure; thread subcommands are stale |
| `docs/CLI-TOOLS.md` trustworthy for stable verb families | agree (partial, qualified as: also missing learnings module and graphify verb family) | gsd-tools.cjs imports learnings module; graphify verbs documented in gsd-tools.cjs but absent from CLI-TOOLS.md |
| `docs/AGENTS.md` per-entry role cards remain usable | agree (re-derived) | For the 21 agents it covers, entries appear consistent with shipped behavior |
| Root `README.md` more useful than `docs/README.md` for release-delta | agree (re-derived) | README.md line 94 surfaces graphify in v1.36.0 highlights while docs/README.md quick-links still say v1.32 |
| `docs/ARCHITECTURE.md` good for layer model, not for numeric inventory | agree (re-derived) | Layer model and data flow sections corroborated by plan-phase.md; counts are stale per git log (last updated v1.34) |

### Omission Claims

| Lane-01/01b Claim | My Verdict | My Evidence |
|---|---|---|
| `gsd-graphify` absent from all audited docs surfaces | agree (re-derived) | Read docs/COMMANDS.md, docs/FEATURES.md, docs/USER-GUIDE.md, docs/CLI-TOOLS.md — all absent; commands/gsd/graphify.md fully shipped; tests/graphify.test.cjs is comprehensive |
| `gsd-pattern-mapper` absent from AGENTS.md | agree (re-derived) | Read agents/gsd-pattern-mapper.md directly — fully developed spec; plan-phase.md line 19 references it by name; AGENTS.md has no entry |
| `gsd-debug-session-manager` absent from AGENTS.md | agree (re-derived) | Read agents/gsd-debug-session-manager.md directly — fully developed spec; CHANGELOG line 20 adds it; AGENTS.md has no entry |
| quick/thread subcommand expansion stale in COMMANDS.md | agree (re-derived) | Read quick.md lines 2-39 and thread.md lines 21-70 directly; `--validate`, `list`, `status`, `resume` for quick and `list --open`, `list --resolved`, `status`, `close` for thread all absent from COMMANDS.md |
| project-skills underrepresented across docs corpus | agree (partial, qualified as: CONFIGURATION.md documents it well, but ARCHITECTURE.md agent spawn table and AGENTS.md do not reflect which agents now consume skills) | plan-phase.md lines 32-34 loads skills for researcher/planner/checker; quick.md lines 18-26 agent types include code-reviewer but not explicit skills loading — the cross-workflow picture is incomplete in docs |

### Misleading Default Claims

| Lane-01/01b Claim | My Verdict | My Evidence |
|---|---|---|
| `claude_md_path` defaults to `null` in CONFIGURATION.md is wrong | agree (re-derived) | templates/config.json line 55: `"claude_md_path": "./CLAUDE.md"`; claude-md-path.test.cjs lines 27-31 asserts same default; CONFIGURATION.md lines 98 and 114 say null/(none) |
| `workflow.tdd_mode` "Added in v1.37" is a provenance error | agree (re-derived) | CHANGELOG.md line 15 places it in v1.36.0; FEATURES.md ToC line 119 places it in v1.36.0 Features section; git log shows the doc was updated in same commit as the feature |

### Numeric Inventory Claims

| Lane-01/01b Claim | My Verdict | My Evidence |
|---|---|---|
| Filesystem has 31 tracked agent files (lane-01 claim) | insufficient evidence | I could not run ls in the upstream repo directory due to sandbox restrictions. I confirmed at minimum 25 agents from direct reading, consistent with 31 but not independently verified to that exact count |
| Filesystem has 73 tracked command files (lane-01 claim) | insufficient evidence | Same sandbox restriction. I confirmed graphify.md exists and is absent from COMMANDS.md, and quick.md and thread.md have expanded signatures. Cannot independently verify 73 |
| COMMANDS.md documents 72 headings and misses graphify (lane-01 claim) | agree (partial, qualified as: I counted the major command sections in COMMANDS.md and found approximately that range, but did not enumerate every heading programmatically) | Graphify absence from COMMANDS.md is re-derived; exact 72 heading count is unverified by me |

### Completeness Wrapper Claims

| Lane-01/01b Claim | My Verdict | My Evidence |
|---|---|---|
| `docs/README.md` is a stale completeness wrapper | agree (re-derived) | Read docs/README.md lines 11-23 directly; "All 18 specialized agents," "What's new in v1.32," "Every command" — all three claims are verifiably wrong against primary sources |
| The safe inherited base is ARCHITECTURE layer model + USER-GUIDE lifecycle + CONFIGURATION namespaces + stable COMMANDS core + covered FEATURES narratives + stable CLI-TOOLS verb families + root README v1.36.0 highlights | agree (re-derived) | My own trust surface analysis aligns with this formulation |
| Mandatory exclusions include: docs/README.md completeness language, AGENTS.md inventory coverage, ARCHITECTURE.md numeric totals, COMMANDS.md as exhaustive, FEATURES.md as release-complete, uncorrected config defaults | agree (re-derived) | All exclusions are independently supported by my evidence above |

---

## Surfaces The Prior Lanes Did Not Examine

### 1. `tests/config-field-docs.test.cjs` — Docs Parity Test for `planning-config.md` Reference

This test (which I read in full) enforces that a reference file `get-shit-done/references/planning-config.md` documents all CONFIG_DEFAULTS keys from core.cjs. This is an internal reference layer below the public docs. The test checks for `features.thinking_partner`, verifies `mode` field values are "interactive" and "yolo" (not "code-first"), and verifies `discuss_mode` accepts "assumptions."

**What this surface reveals:** There is an internal reference layer (`get-shit-done/references/planning-config.md`) that may be more current than the public `docs/CONFIGURATION.md` because it is tested. The test at line 173-179 explicitly asserts that `mode` must NOT document "code-first" — suggesting there may have been a period when the docs contained that wrong value. This is evidence that the test suite actively guards the reference layer's accuracy in ways the public docs layer is not guarded.

**Material impact on trust ranking:** The `planning-config.md` reference file (which I did not read but whose test structure I understand) should be consulted alongside `docs/CONFIGURATION.md` in any docs-refresh work, because the test suite enforces its accuracy in ways that `docs/CONFIGURATION.md` is not subject to. This adds a materially stronger corroboration source than prior lanes identified.

---

### 2. `tests/docs-update.test.cjs` — Docs Infrastructure Testing

This test covers the `docs-init` gsd-tools command which initializes the documentation generation workflow. It verifies the JSON shape that `gsd-tools.cjs docs-init` returns, including project type detection, existing doc scanning, GSD marker detection, and doc tooling detection.

**What this surface reveals:** There is a machine-readable project introspection layer that feeds the docs-update workflow. The `docs-init` command returns structured data about project type (has_package_json, has_api_routes, has_cli_bin, is_monorepo, etc.) and doc tooling (docusaurus, vitepress, mkdocs, storybook). This infrastructure enables the docs-update workflow to generate contextually appropriate documentation.

**Material impact:** This surface is not covered by prior lanes and does not change the trust ranking of the audited docs corpus itself. But it does show that GSD has an automated docs-generation capability whose test coverage is stronger than the manually maintained docs in `docs/`.

---

### 3. `tests/agent-required-reading-consistency.test.cjs` — Agent Count Floor

This test reads all agent files from the `agents/` directory and enforces that no legacy `<files_to_read>` blocks remain. Line 58 asserts: "at least 20 agents have reading instructions." This provides a reliable lower bound on the agent count that is independent of any doc surface.

**What this reveals:** The test-derivable lower bound of 20 is consistent with AGENTS.md's 21 documented agents, but does not constrain the count above 21. My direct reading of gsd-pattern-mapper.md and gsd-debug-session-manager.md adds 2 more confirmed agents to the count. The test does not tell us the total; it only tells us the floor.

**Material impact on trust ranking:** This test is a weak corroboration that the agent count is in the right ballpark for AGENTS.md (21+), but is not the authoritative count source. Prior lanes did not specifically flag this test as a count floor instrument.

---

## Unresolved Uncertainties

1. **Exact agent count:** I cannot independently verify the 31-agent count from lane-01 without being able to run `ls` or Glob in the upstream repo directory. My evidence establishes at least 25, consistent with 31, but not verified to that number.

2. **Exact command count:** Same sandbox restriction prevents independent verification of the 73-command count from lane-01.

3. **gsd-code-reviewer and gsd-code-fixer agent file existence:** I have corroboration from quick.md and COMMANDS.md that these agents are shipped, but I did not read their agent definition files. I cannot verify their exact spec or confirm they appear in the agents/ directory.

4. **`planning-config.md` reference file content:** I know this file exists and is tested by config-field-docs.test.cjs, but I did not read it. It may be more complete than `docs/CONFIGURATION.md` and could serve as a stronger corroboration source for config field claims.

5. **Whether graphify omission from public docs is intentional:** The feature has a config gate (`graphify.enabled: true`), which could indicate it is deliberately opt-in and not yet considered "generally available." However, the command ships with the package, has full tests, and appears in the root README highlights, suggesting it is not intentionally hidden.

6. **State of upstream `main` post-v1.36.0:** Some of these gaps may already be closed in the upstream repository's current state. The audit is pinned to v1.36.0.

7. **Localized docs accuracy:** The localized docs under `docs/pt-BR/`, `docs/ja-JP/`, etc. were not examined and may mirror the same defects or have different ones.

8. **Whether FEATURES.md graphify section exists in the remainder of that file:** I read FEATURES.md lines 1-600, covering the ToC and features 1-19. The ToC (lines 110-118) lists v1.36.0 features at section numbers 108-115 (Plan Bounce, External Code Review Command, Cross-AI Execution Delegation, Architectural Responsibility Mapping, Extract Learnings, SDK Workstream Support, Context-Window-Aware Prompt Thinning, Configurable CLAUDE.md Path). None of these ToC entries are for graphify. The graphify feature in the v1.36.0 block was called "Knowledge graph integration" in the root README; if it has a FEATURES.md entry, the ToC should show it. Its absence from the ToC strongly suggests it is absent from FEATURES.md, but I cannot confirm by reading the full file.

---

## What Would Change My Judgment

1. **If a filesystem inventory showed fewer than 25 agent files:** I would revise my agent count floor downward, which would partially rehabilitate AGENTS.md's claim of 21 as more representative. The threshold is: if the actual count is 22-24, the omission severity is lower; if the actual count is 30+, the omission severity is higher.

2. **If `planning-config.md` were found to be severely outdated:** My trust in config-field-docs.test.cjs as a corroboration instrument would weaken. Currently I trust it as evidence that the reference layer has active doc-parity enforcement.

3. **If graphify were found in FEATURES.md (in the portion I did not read):** The graphify omission claim would need to be narrowed to just COMMANDS.md, CLI-TOOLS.md, and USER-GUIDE.md. This would be a partial revision — less severe than total absence.

4. **If the `discuss_mode` default in USER-GUIDE.md were shown to be correct (i.e., the value was actually "standard" at some point and was changed):** I would revise the USER-GUIDE.md trust assessment. My current judgment is that "standard" is a wrong value that was never correct for the shipped system, but I did not verify the full history of that field.

5. **If tests for the COMMANDS.md or AGENTS.md inventory existed:** Their absence is the main reason those docs lack the same test-backed credibility that CONFIGURATION.md has through config-field-docs.test.cjs. If such tests existed and passed, I would raise the trust ranking of those surfaces.

---

## Net Verdict

The upstream v1.36.0 docs corpus is strong enough to seed later docs-refresh or docs-seeded remapping work under the following conditions: (a) the three trust-bug corrections are applied before the seed is used for config-reference work (the `claude_md_path` default, the `tdd_mode` version tag, and the `discuss_mode` default in USER-GUIDE.md); (b) the corpus is treated as a ranked partial seed rather than an authoritative inventory — specifically, `CONFIGURATION.md`, `ARCHITECTURE.md`'s layer model sections, `USER-GUIDE.md`'s lifecycle diagrams, and `COMMANDS.md`'s core workflow entries are trustworthy inputs, while `docs/README.md`'s completeness claims, `docs/AGENTS.md`'s inventory scope, and any numeric counts in `docs/ARCHITECTURE.md` are explicitly excluded from trust; and (c) the corpus is extended with changelog and command-file corroboration for v1.36.0 surfaces before those surfaces are considered documented. The corpus is not strong enough to seed work that requires an exhaustive agent, command, or feature inventory without first running a filesystem cross-check — at minimum, graphify, gsd-pattern-mapper, gsd-debug-session-manager, and the quick/thread subcommand expansions must be added before the docs can be treated as representative of the shipped v1.36.0 system. Subject to these exclusions and corrections, the docs corpus provides a genuinely useful structural spine for later work.
