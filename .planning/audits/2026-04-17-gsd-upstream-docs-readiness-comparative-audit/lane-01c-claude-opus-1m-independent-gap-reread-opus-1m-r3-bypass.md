# Lane 01c: Independent Docs-Gap Reread (Claude Opus 1M, xhigh)

## Question And Scope

The question this reread answers, in my own words: **is the upstream `get-shit-done v1.36.0` docs corpus trustworthy enough to serve as the seed for a later docs-refresh or docs-seeded remapping pass — and where it isn't, what is the minimum overlay of supplementation, correction, and explicit exclusions needed to make it usable?** "Trustworthy" decomposes into three sub-questions I will keep distinct throughout: (a) does the corpus accurately *describe* the shipped surfaces it covers; (b) does the corpus *cover* the shipped surfaces a reader would reasonably expect; (c) do the corpus's *self-descriptions of completeness* match the corpus's actual coverage.

Non-goals and stopping point: I stop at diagnosis and supplementation-strategy definition. I do not rewrite any upstream doc, do not revise the prix-guesser readiness program or Checkpoint 5 closure path, do not audit upstream `main` beyond the `v1.36.0` pin, and do not audit localized docs (`docs/pt-BR`, `ja-JP`, `zh-CN`, `ko-KR`). I stay bounded to the doc-gap question.

Upstream doc surfaces I read directly (all paths under `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/`):

- `docs/README.md`, `docs/ARCHITECTURE.md`, `docs/AGENTS.md`, `docs/CONFIGURATION.md`, `docs/COMMANDS.md`, `docs/CLI-TOOLS.md`, `docs/FEATURES.md`, `docs/USER-GUIDE.md`, `docs/context-monitor.md`, `docs/workflow-discuss-mode.md`, `docs/manual-update.md`
- `README.md` (upstream root), `CHANGELOG.md`

Corroboration surfaces I read or enumerated:

- Shipped command files: `commands/gsd/graphify.md`, `commands/gsd/quick.md`, `commands/gsd/thread.md`, plus filesystem inventory across `commands/gsd/*.md` (73 files).
- Shipped agent files: `agents/gsd-ai-researcher.md`, `agents/gsd-code-fixer.md`, `agents/gsd-code-reviewer.md`, `agents/gsd-debug-session-manager.md`, `agents/gsd-domain-researcher.md`, `agents/gsd-eval-auditor.md`, `agents/gsd-eval-planner.md`, `agents/gsd-framework-selector.md`, `agents/gsd-intel-updater.md`, `agents/gsd-pattern-mapper.md`, plus inventory of `agents/gsd-*.md` (31 files).
- Workflows: `get-shit-done/workflows/plan-phase.md`, plus inventory of `get-shit-done/workflows/*.md` (71 files).
- Bin/CLI code: `get-shit-done/bin/gsd-tools.cjs` (routing surface, inspected via grep), `get-shit-done/bin/lib/config.cjs`, `get-shit-done/bin/lib/core.cjs`, `get-shit-done/bin/lib/profile-output.cjs`, `get-shit-done/bin/lib/init.cjs`, plus enumeration of `get-shit-done/bin/lib/*.cjs` (24 modules).
- Shipped defaults template: `get-shit-done/templates/config.json`.
- References: `get-shit-done/references/*.md` inventory (42 files), contents of `planning-config.md` via the test `tests/config-field-docs.test.cjs`.
- Tests: `tests/claude-md-path.test.cjs` (full), `tests/graphify.test.cjs` (head + line count, 1051 lines), `tests/config-field-docs.test.cjs`, plus filesystem inventory of `tests/*.test.cjs` (191 files).

Candidate evidence I read but deliberately did not cite as primary: the lane-01, lane-01b, SYNTHESIS, and task-spec files. Those are adjudicated in Section 9.

## Independent Epistemic Path

I did not start from the prior lanes' claim ledger. I started from the upstream filesystem and moved outward into the docs, treating each doc assertion as a candidate claim to test against something in the shipped tree. The read order was:

1. Top-level inventory of the upstream repo to know what *could* be documented (`ls` of root, `docs/`, `commands/gsd/`, `agents/`, `get-shit-done/`, `get-shit-done/workflows/`, `get-shit-done/references/`, `get-shit-done/bin/lib/`, `tests/`).
2. `docs/README.md` first, because it both indexes the corpus and makes the most aggressive completeness claims — a useful first contradiction target.
3. `docs/ARCHITECTURE.md` next, because it declares explicit numeric inventories (commands, workflows, agents, references, modules) that can be immediately falsified against filesystem counts.
4. `docs/AGENTS.md`, specifically to diff the agent roster it documents against `agents/gsd-*.md` on disk.
5. `docs/CONFIGURATION.md` against `get-shit-done/templates/config.json` and `get-shit-done/bin/lib/config.cjs` / `core.cjs` to test claimed defaults.
6. `docs/COMMANDS.md` against `commands/gsd/*.md` on disk, using a sort/comm diff on the file stems vs the `### \`/gsd-*\`` headings.
7. `docs/CLI-TOOLS.md` against `bin/lib/*.cjs` and `gsd-tools.cjs` verb grep.
8. `docs/FEATURES.md`, `docs/USER-GUIDE.md`, `docs/context-monitor.md`, `docs/workflow-discuss-mode.md`, `docs/manual-update.md` — reading the narrative surfaces only after the inventory falsifiers had already established the asymmetry between described and shipped.
9. `CHANGELOG.md` last, specifically to test the "added in v1.N" provenance claims in `CONFIGURATION.md` and `FEATURES.md`.
10. Tests for anything the docs still disputed — `claude-md-path.test.cjs` to decide the `claude_md_path` default, `graphify.test.cjs` to confirm graphify is a live shipped surface, `config-field-docs.test.cjs` to verify the separate `references/planning-config.md` reality.

Branch points where I explicitly chose re-verification over inheritance:

- I refused to inherit the numbers in `lane-01` (73/31). I counted agents and commands myself with explicit shell inventory (`find`, `ls | wc -l`, `for loop | sort | comm`). The numbers I derived match lane-01's; I record them as re-derived in Section 9, not inherited.
- I refused to inherit the claim that `docs/ARCHITECTURE.md` says 24 agents, 69 commands, 68 workflows, 35 references, 19 modules without reading the document. I confirmed 24 (line 137), 69 (line 116), 68 (line 127), 35 (line 141), 19 (line 221) myself. I also caught one number lane-01 attributed to `docs/CLI-TOOLS.md` ("15 modules") and re-derived that claim from `docs/CLI-TOOLS.md:12`.
- I refused to inherit that `claude_md_path` defaults to `./CLAUDE.md` in code. I grepped for it in `bin/lib/` and found *two* code paths: `config.cjs:184` returns `'./CLAUDE.md'` as a new-project default, while `core.cjs:390` returns `null` when the key is unset on an existing config. Both exist in the same version. The doc's `null` is therefore partially right in one path and wrong in the shipped-template / new-project path — a subtler defect than lane-01 framed.
- I refused to inherit the taxonomy wholesale. I kept "misleading default" and "omitted shipped surface" because both are forced by evidence. I then tested whether the other four classes (underrepresented, stale summary, completeness wrapper, architecture flattening) collapse or split once you confront a particular defect — see Section 7.
- I read two docs the prior lanes' task specs did not explicitly name: `docs/manual-update.md` and the internal contents of `docs/workflow-discuss-mode.md` / `docs/context-monitor.md`. See Section 10 for whether any of that changes the verdict.

I did not run `git log --follow` on individual doc files; lane-01 asserted git-history evidence for uneven maintenance pressure, which I can neither confirm nor refute without running `git` myself. I mark that as `insufficient evidence to rule on it` in Section 9 rather than silently inheriting.

## Trustworthy Summary Surfaces

The following surfaces I re-derived as **trustworthy enough to seed** a later docs-refresh pass, with the trust scoped to specific content.

**`docs/CONFIGURATION.md` — config namespace discovery and toggle semantics.** Trustworthy *for*: enumerating what config keys exist, the **absent = enabled** rule for workflow toggles (line 122), the structure of the `agent_skills` injection system (lines 193–245), the model-profile taxonomy (lines 439–519), and the recommended-preset matrix (lines 153–157). The `planning.*`, `parallelization.*`, `gates.*`, `safety.*`, `security.*`, `review.models.*`, and `manager.flags.*` tables are internally coherent and read cleanly against `get-shit-done/bin/lib/config.cjs:1-200`. Primary evidence I re-derived: the `agent_skills` section in the doc (`docs/CONFIGURATION.md:193-245`) matches the `agent_skills` VALID key in `config.cjs` and the injection shape seen in the command file for `/gsd-quick` and the `plan-phase.md` workflow. Not trustworthy *for*: exact shipped defaults (see Section 6 on `claude_md_path`), version provenance labels (see `tdd_mode` Added-in-v1.37 claim), or completeness of the schema as shown in lines 12–100 (the "Full Schema" block omits `planning.sub_repos`, which appears in `templates/config.json:26`).

**`docs/ARCHITECTURE.md` — layer topology and fresh-context-per-agent design.** Trustworthy *for*: the command → workflow → agent → CLI-tools → `.planning/` layering diagram (`docs/ARCHITECTURE.md:31-66`), the design principles (lines 72-101), the wave execution model (lines 289-299), the adaptive context enrichment mechanism at 500K+ windows (lines 307-322), and the runtime abstraction table (lines 580-591). These are directionally accurate and re-derivable against the workflow and agent files I read. Not trustworthy *for*: any numeric total on this page (69 commands, 68 workflows, 24 agents, 35 references, 19 modules are all wrong against filesystem counts — see Section 5). Also not trustworthy as an exhaustive component map: the Agent Spawn Categories table (lines 273-287) lists 21 agents, consistent with `docs/AGENTS.md` but omitting 10 shipped agent files.

**`docs/USER-GUIDE.md` — lifecycle diagrams and operator orientation.** Trustworthy *for*: the full project lifecycle diagram (lines 26-76) and the general phase-chain narrative. These describe the stable core of the framework and read correctly against the workflow files. Not trustworthy *for*: any command signature where the shipped command has evolved (quick, thread, debug subcommands — see Section 6).

**`docs/context-monitor.md` (115 lines).** Trustworthy *for*: its entire scope. The thresholds table (lines 18-22) matches `docs/ARCHITECTURE.md:544-548`, the bridge-file shape (lines 46-55) matches the hook architecture described elsewhere, and the safety properties section (lines 110-115) is consistent with the advisory-only posture referenced in `docs/ARCHITECTURE.md:553-558`. Small, focused, internally consistent, low drift risk — a good model of what a maintainable topic doc looks like.

**`docs/workflow-discuss-mode.md` (68 lines).** Trustworthy *for*: its entire scope. The two-mode taxonomy (lines 7-24) is consistent with `docs/CONFIGURATION.md:136` (`discuss_mode: 'discuss' | 'assumptions'`), and the CONTEXT.md 6-section output structure (lines 59-66) is independently verifiable.

**`docs/manual-update.md` (62 lines).** Trustworthy *for*: the non-npm install procedure, including the runtime flag table (lines 30-43) and the "what the installer replaces / preserves" split (lines 47-62). Consistent with `docs/ARCHITECTURE.md:492-513` on installer responsibilities.

**Individual documented agents inside `docs/AGENTS.md`.** Trustworthy at the per-entry level for the 21 agents actually documented. The role, spawning command, parallelism, tool surface, and produced-artifact columns (lines 33-496) read correctly against the corresponding agent files I spot-checked. Not trustworthy as an inventory — see Section 5.

**Individual command entries in `docs/COMMANDS.md` for the stable core phase chain.** Specifically: `/gsd-new-project` (lines 17-31), `/gsd-discuss-phase` (lines 91-115), `/gsd-ui-phase` (lines 119-132), `/gsd-plan-phase` (lines 136-166), `/gsd-execute-phase` (lines 170-190), `/gsd-verify-work` (lines 194-209), `/gsd-ship` (implicit), and the milestone family. Trustworthy *for*: argument names, flag inventory, prerequisites, and produced artifacts on these stable commands. Not trustworthy *for*: newer commands where shipped subcommand surfaces have outgrown the doc entry (see Section 6).

**Upstream root `README.md` as a release-delta control.** Trustworthy *for*: the `v1.36.0 Highlights` listing that does include graphify, TDD, and prompt thinning. I use this as a negative control on `docs/README.md`'s "What's new in v1.32" claim; the root README knows the current version is `v1.36.0` even though the docs index still advertises `v1.32` news (`docs/README.md:23`).

## Omitted Shipped Surfaces

My own inventory counts, shown with the commands I ran:

- Agents: `find /home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/agents -name 'gsd-*.md' -type f | wc -l` → **31**.
- Commands: `find .../commands/gsd -name '*.md' -type f | wc -l` → **73**.
- Workflows: `find .../get-shit-done/workflows -name '*.md' -type f | wc -l` → **71**.
- References: `find .../get-shit-done/references -name '*.md' -type f | wc -l` → **42**.
- `bin/lib/` modules: directory listing → **24** (`audit.cjs`, `commands.cjs`, `config.cjs`, `core.cjs`, `docs.cjs`, `frontmatter.cjs`, `graphify.cjs`, `gsd2-import.cjs`, `init.cjs`, `intel.cjs`, `learnings.cjs`, `milestone.cjs`, `model-profiles.cjs`, `phase.cjs`, `profile-output.cjs`, `profile-pipeline.cjs`, `roadmap.cjs`, `schema-detect.cjs`, `security.cjs`, `state.cjs`, `template.cjs`, `uat.cjs`, `verify.cjs`, `workstream.cjs`).
- Tests: `ls tests/*.test.cjs | wc -l` → **191**.

Doc-asserted counts against these realities:

| Surface | `docs/README.md` | `docs/ARCHITECTURE.md` | `docs/AGENTS.md` | `docs/CLI-TOOLS.md` | Filesystem |
|---------|------------------|------------------------|------------------|----------------------|------------|
| Agents | "All 18" (line 16) | 24 (line 137) | "All 21" (line 3), tabulated to 21 (lines 13-27) | — | **31** |
| Commands | — | 69 (line 116) | — | — | **73** |
| Workflows | — | 68 (line 127) | — | — | **71** |
| References | — | 35 (line 141) | — | — | **42** |
| `bin/lib/` modules | — | 19 (line 221) | — | 15 (line 12) | **24** |

Every docs-asserted numeric inventory is wrong. The largest gap is agents: the docs speak of 18, 21, or 24 depending on which you read; the shipped reality is 31. That is an **11-agent hole** in the worst case (against `docs/README.md`) and a **10-agent hole** in the best-corroborated case (against `docs/AGENTS.md`'s own tabulation).

**Omitted agents (10 of 31 shipped agents).** Diff of `agents/gsd-*.md` on disk against `### gsd-*` entries in `docs/AGENTS.md`:

- `gsd-ai-researcher` — `agents/gsd-ai-researcher.md:2-5` declares it spawns from `/gsd-ai-integration-phase`. That command *is* documented in `docs/COMMANDS.md:977` and `docs/FEATURES.md:2254-2267`, but the agent backing it is not in `docs/AGENTS.md`.
- `gsd-domain-researcher` — `agents/gsd-domain-researcher.md:2-5`, same `/gsd-ai-integration-phase` pipeline. Not in `docs/AGENTS.md`.
- `gsd-eval-planner` — `agents/gsd-eval-planner.md:2-5`, `/gsd-ai-integration-phase` pipeline.
- `gsd-eval-auditor` — `agents/gsd-eval-auditor.md:2-5`, spawns from `/gsd-eval-review` (documented at `docs/COMMANDS.md:992`).
- `gsd-framework-selector` — `agents/gsd-framework-selector.md:2-5`, `/gsd-ai-integration-phase` / `/gsd-select-framework`.
- `gsd-code-reviewer` — `agents/gsd-code-reviewer.md:2-5`, spawns from `/gsd-code-review` (documented at `docs/COMMANDS.md:1028`).
- `gsd-code-fixer` — `agents/gsd-code-fixer.md:2-5`, spawns from `/gsd-code-review-fix` (documented at `docs/COMMANDS.md:1050`).
- `gsd-debug-session-manager` — `agents/gsd-debug-session-manager.md:2-5`, spawns from `/gsd-debug` as the isolation sub-orchestrator. `CHANGELOG.md:20,22` lists it as a v1.36.0 addition.
- `gsd-intel-updater` — `agents/gsd-intel-updater.md:2-5`, backs the `/gsd-intel` command (documented at `docs/COMMANDS.md:953`).
- `gsd-pattern-mapper` — `agents/gsd-pattern-mapper.md:2-5`, actively referenced by the planning workflow (`get-shit-done/workflows/plan-phase.md:18,621-666`). `CHANGELOG.md:13` calls it a v1.36.0 addition.

This is a **pipeline-sized** omission, not a count typo. Five entire agent families (`AI integration`, `eval review`, `code review`, `intel update`, `pattern mapping`, `debug session management`) exist in code and have commands visible in `docs/COMMANDS.md`, but the Agent Reference never explains who does the work behind those commands.

**Omitted commands.** Filesystem diff of `commands/gsd/*.md` stems vs `### \`/gsd-*\`` headings in `docs/COMMANDS.md`:

- In FS but NOT in docs: `graphify`, `extract_learnings` (where the doc uses the hyphenated `extract-learnings` form — that's a naming mismatch, not a genuine omission).
- In docs but NOT in FS: `extract-learnings` (resolves against the underscore form).

Actual omission is **`/gsd-graphify`**. The command file (`commands/gsd/graphify.md:1-33`) is present, wired (`gsd-tools.cjs` exposes `graphify {build, query, status, diff}` via `bin/lib/graphify.cjs`), tested (`tests/graphify.test.cjs`, 1051 lines), and surfaced in the root `README.md` v1.36.0 highlights and the `CHANGELOG.md:12` entry. It is entirely absent from `docs/README.md`, `docs/COMMANDS.md`, `docs/FEATURES.md`, `docs/CLI-TOOLS.md`, and `docs/USER-GUIDE.md`. This is the single clearest omission in the corpus.

**Omitted config keys and structural mismatches.** `docs/CONFIGURATION.md` presents a "Full Schema" block (lines 12-100) that omits `planning.sub_repos` (present in `templates/config.json:26`). Also, `docs/CONFIGURATION.md:83-85` places `security_enforcement`, `security_asvs_level`, `security_block_on` at the **root** of config, while `templates/config.json:10-12` places the same keys inside the **`workflow`** section. Either the template is wrong or the doc is; regardless, the schema shape disagrees with the shipped template, and a reader following the doc may write those keys to the wrong place.

**Omitted CLI-tools modules.** `docs/ARCHITECTURE.md:221-243` names 19 modules; actual `bin/lib/` has 24. Missing from the doc table: `audit.cjs`, `graphify.cjs`, `gsd2-import.cjs`, `intel.cjs`, `learnings.cjs`. Each corresponds to a shipped and documented (at command level) feature: `/gsd-audit-*`, `/gsd-graphify`, `/gsd-from-gsd2`, `/gsd-intel`, `/gsd-extract-learnings`. The command doc says these things exist; the architecture doc's CLI-tools table says the code to implement them does not.

## Stale Or Misleading Summaries

These are surfaces the docs *cover* but describe wrongly, incompletely, or with stale signatures / provenance / defaults. I split into **stale-but-fixable** (wrong facts about a correctly scoped surface) and **load-bearing trust bugs** (wrong facts that will change a reader's operational behavior if they follow the doc).

**Load-bearing trust bugs (correct these first):**

1. **`claude_md_path` default in `docs/CONFIGURATION.md` is wrong where it matters.** `docs/CONFIGURATION.md:98` (Full Schema block) shows `"claude_md_path": null`, and `docs/CONFIGURATION.md:114` labels the default as `(none)`. But `get-shit-done/templates/config.json:55` ships `"claude_md_path": "./CLAUDE.md"`, `get-shit-done/bin/lib/config.cjs:184` sets the new-project default to `./CLAUDE.md`, and `tests/claude-md-path.test.cjs:28-31` asserts the template value as `./CLAUDE.md`. Furthermore `tests/claude-md-path.test.cjs:62` asserts that `buildNewProjectConfig` produces `claude_md_path: './CLAUDE.md'`. `docs/FEATURES.md:2404` (REQ-CMDPATH-01) explicitly states the default is `./CLAUDE.md`. So the corpus is internally inconsistent *and* the config-reference page contradicts the shipped template. A reader who reads only `docs/CONFIGURATION.md` and believes the `null` default will misunderstand what a fresh project produces. `get-shit-done/bin/lib/core.cjs:390` does return `null` when the key is missing on an existing config, which is the narrow technical reading that lets the doc's `null` stand — but that is a runtime fallback, not the shipped default. Classification: load-bearing trust bug.

2. **`workflow.tdd_mode` provenance is wrong by one minor version.** `docs/CONFIGURATION.md:146` says `tdd_mode` was "Added in v1.37". The feature is listed under "v1.36.0 Features" as item #116 in `docs/FEATURES.md:2412-2425`. `CHANGELOG.md:15` attributes it to `[1.36.0] - 2026-04-14`. `get-shit-done/bin/lib/config.cjs:20,164` includes `workflow.tdd_mode` in `VALID_CONFIG_KEYS` with default `false` in v1.36.0's shipped code. The doc is off by one version. Not catastrophic, but readers using the provenance column to plan upgrades will be misled. Classification: load-bearing trust bug for any workflow that keys on feature-version provenance.

3. **`docs/README.md` still announces the v1.32 change horizon.** `docs/README.md:23` reads "What's new in v1.32:" followed by v1.32 feature descriptions. The pinned release is `v1.36.0`. Upstream root `README.md:92-98` carries the correct `v1.36.0 Highlights`. The docs index is four minor versions behind its own navigation target. Classification: load-bearing trust bug because this is the first page many readers open.

**Stale-but-fixable signatures (correct these, but they do not mislead as severely):**

4. **`/gsd-quick` signature is stale.** `docs/COMMANDS.md:627-644` documents three flags (`--full`, `--discuss`, `--research`). The shipped command `commands/gsd/quick.md:2-39` carries the richer signature `[list | status <slug> | resume <slug> | --full] [--validate] [--discuss] [--research] [task description]`, with subcommand parsing logic at `commands/gsd/quick.md:53-60` (LIST, STATUS, RESUME modes) and `--validate` described at line 29 as enabling plan-check and verifier without discussion/research. Neither `--validate` nor the three subcommands appear in `docs/COMMANDS.md`. `docs/FEATURES.md` section 10 (Quick Mode) carries an equally stale signature.

5. **`/gsd-thread` signature is stale.** `docs/COMMANDS.md:1268-1284` lists three modes: `(none)` for list, `name` for resume, `description` for create. `commands/gsd/thread.md:3-4` advertises `[list [--open | --resolved] | close <slug> | status <slug> | name | description]`, with list-filtering and close/status modes described in the parse table at lines 23-29. `CHANGELOG.md:19` explicitly lists this as a v1.36.0 addition. The doc still shows the pre-v1.36 surface.

6. **`/gsd-debug` subcommand coverage is incomplete in `docs/AGENTS.md`.** The command doc itself (`docs/COMMANDS.md:703-717`) correctly lists `list`, `status <slug>`, `continue <slug>`, and the `--diagnose` flag. But `docs/AGENTS.md:358-380` describes `gsd-debugger` without mentioning that in v1.36.0 the session is driven by a new `gsd-debug-session-manager` sub-orchestrator (which is an omitted agent — see Section 5). The "TDD checkpoint" and "reasoning checkpoint" added in `CHANGELOG.md:20,22` are not reflected.

7. **`docs/ARCHITECTURE.md` Hook System section is incomplete.** The table at `docs/ARCHITECTURE.md:207-217` lists nine hooks. The shipped `hooks/` directory carries more surface than the doc narrates, but more importantly the **`gsd-commit-docs.*`** community hook referenced in `CHANGELOG.md` is not in the hook table. The doc is correct-as-far-as-it-goes, but the section is not load-bearing for hook selection.

8. **`docs/CLI-TOOLS.md:159` lists 12 agents for model resolution**, but the `docs/CONFIGURATION.md:443-456` model-profile table shows 12 agents and the shipped roster is 31. For agents outside the 12-agent list (notably `gsd-code-fixer`, `gsd-code-reviewer`, the AI-integration family, `gsd-intel-updater`, `gsd-pattern-mapper`), the doc offers no guidance on their resolved model — even though `model_overrides` in `docs/CONFIGURATION.md:462-470` clearly supports per-agent overrides for any agent.

9. **`docs/FEATURES.md` TOC does not list Feature #116 (TDD Pipeline Mode).** The TOC ends at Feature #115 Configurable CLAUDE.md Path (`docs/FEATURES.md:118`), but #116 appears in the body at `docs/FEATURES.md:2412-2425`. A reader navigating by TOC will miss TDD entirely.

10. **`docs/FEATURES.md` TOC is non-chronological.** Lines 56-139 list v1.27, v1.28, v1.29, v1.30, v1.31, v1.34, v1.35, v1.36, v1.32. v1.33 appears nowhere explicit in the TOC. The body follows the same ordering. This makes "what's in which version" hard to navigate correctly, and it is a symptom of appended-edits-never-reorganized.

## Gap Taxonomy (Adopted Or Revised)

I partially adopt the prior taxonomy (six classes) and revise it into **five** classes, because on re-reading I judged that "stale completeness wrapper" and "stale summary or signature" collapse into a single class once you notice they have the same remediation shape, while "architecture flattening" is actually an instance of "shipped inventory omission" that happens to affect a high-level narrative doc.

My adopted taxonomy, with the decomposition rationale:

1. **Shipped inventory omission.** A surface (command, agent, workflow, config key, module) exists in code and tests but is absent from the docs. Examples: `/gsd-graphify`, `gsd-pattern-mapper`, the AI-integration agent quintet, `gsd-code-reviewer`, `gsd-code-fixer`, `gsd-intel-updater`, `gsd-debug-session-manager`, `planning.sub_repos`, five `bin/lib/` modules. Remediation: add the surface, or explicitly list it as intentionally not-documented. This class cannot be solved by copy-editing alone; it requires maintainer decisions on audience.

2. **Misleading default or provenance mismatch.** The doc states the wrong value for a shipped default, or the wrong version for a feature's debut. Examples: `claude_md_path` (`docs/CONFIGURATION.md:98,114` vs `templates/config.json:55` and `tests/claude-md-path.test.cjs:28-31`); `workflow.tdd_mode` ("Added in v1.37" vs `CHANGELOG.md:15` attributing it to v1.36.0). Remediation: patch the value or the version label. This class is load-bearing because readers act on defaults.

3. **Stale surface signature.** The doc covers the surface but describes an older, smaller signature than shipped. Examples: `/gsd-quick`, `/gsd-thread`, `/gsd-debug` subcommand coverage. Remediation: sync the signature. This class is not load-bearing for existing users (their old invocations still work) but is load-bearing for new users trying to discover the full surface.

4. **Misrepresented completeness.** The docs' navigation and wrapper language claims the corpus is exhaustive when it is not. Example: `docs/README.md:12-16` says "Every command with syntax, flags, options, and examples" and "Complete feature and function documentation" when at least `/gsd-graphify` and 10 agents are missing. Remediation: either weaken the completeness language or add the missing surfaces. This class is distinct from class 1 because it is not a surface omission — it is an accuracy claim about the corpus's own coverage. It matters because it shapes reader trust.

5. **Stale inventory metadata.** The doc asserts a count (agents, commands, workflows, references, modules) that no longer matches reality. Examples: agent counts 18/21/24 vs reality 31; command count 69 vs 73; workflow count 68 vs 71; reference count 35 vs 42; CLI-tools module count 15/19 vs 24. Remediation: replace fixed counts with generated ones, or remove the counts entirely. This class is a drift-control problem, and it is the single clearest argument for an automated docs-vs-filesystem guard.

I collapsed "underrepresented advanced surface" from the prior taxonomy into either class 1 (if the surface is genuinely absent from the docs) or class 3 (if it is referenced but described in an older signature). I collapsed "architecture flattening" into class 1 with the observation that flattening *is* omission at the narrative level.

I retained the "misleading default" class separately from "stale surface signature" because readers respond differently to the two: a wrong default prompts wrong operational action, while a stale signature prompts under-usage. Collapsing them would hide a severity difference that matters for patch ordering.

## Supplementation And Patch Strategy

Ranked supplementation moves, with ordering rationale:

**Track 1 — Trust-bug hotfixes (must land first, because readers take action on these).**

- 1a. Correct `docs/CONFIGURATION.md:98,114` so the `claude_md_path` default reads `./CLAUDE.md` (matching `templates/config.json:55` and `tests/claude-md-path.test.cjs`). Cite `docs/FEATURES.md:2399-2408` for the canonical default statement.
- 1b. Correct `docs/CONFIGURATION.md:146` so `workflow.tdd_mode` is attributed to v1.36.0, matching `CHANGELOG.md:15` and `docs/FEATURES.md:2412-2425`.
- 1c. Correct `docs/README.md:23` so the "What's new" line refers to v1.36.0 and cites the upstream root README's highlights. If the maintainers do not want to keep this line in sync, delete it.
- 1d. Reconcile security_enforcement / security_asvs_level / security_block_on position: either move them to `workflow.*` in `templates/config.json:10-12` to match `docs/CONFIGURATION.md:373-377`, or move them to root in the template to match the docs' Full Schema. Decide where the spec lives and align.

**Track 2 — Completeness-claim truth (must follow Track 1 but precede Track 3, because readers who just had their trust repaired should not immediately hit overclaim language).**

- 2a. Weaken or remove the "complete" and "every" language in `docs/README.md:11-16` until Track 3 lands.
- 2b. Fix the agent count on `docs/README.md:16` from "All 18 specialized agents" to the correct current count, or remove the number.
- 2c. Add a `planning.sub_repos` entry to the Full Schema block in `docs/CONFIGURATION.md:12-100`.

**Track 3 — Missing-surface catch-up (largest body of work, must follow 1 and 2).**

- 3a. `docs/COMMANDS.md`: add a `/gsd-graphify` section covering `build`, `query`, `status`, and `diff` subcommands. Evidence base: `commands/gsd/graphify.md` and `tests/graphify.test.cjs` (1051 lines). Also add a `graphify` entry to `docs/CLI-TOOLS.md` alongside the other verb families.
- 3b. `docs/COMMANDS.md`: refresh the `/gsd-quick` section to include the `list`, `status <slug>`, `resume <slug>` subcommands and the `--validate` flag, citing `commands/gsd/quick.md:2-39,53-60`.
- 3c. `docs/COMMANDS.md`: refresh the `/gsd-thread` section to include `list --open`, `list --resolved`, `close <slug>`, `status <slug>`, citing `commands/gsd/thread.md:3-4,23-29`. Same refresh in `docs/USER-GUIDE.md` wherever thread is described.
- 3d. `docs/AGENTS.md`: add entries for the 10 omitted shipped agents (`gsd-ai-researcher`, `gsd-domain-researcher`, `gsd-eval-planner`, `gsd-eval-auditor`, `gsd-framework-selector`, `gsd-code-reviewer`, `gsd-code-fixer`, `gsd-debug-session-manager`, `gsd-intel-updater`, `gsd-pattern-mapper`). Fix the "All 21" line at the top. Update the Agent Tool Permissions Summary to cover the new entries.
- 3e. `docs/ARCHITECTURE.md`: expand the CLI Tools module table (lines 221-243) to cover the missing modules (`audit`, `graphify`, `gsd2-import`, `intel`, `learnings`). Update Total commands / workflows / agents / references / modules lines to match filesystem counts (or replace with "generated — see inventory").

**Track 4 — Drift-control mechanism (should land alongside or immediately after Track 3, because otherwise the same drift recurs after the next release).**

- 4a. Add a test (or extend `tests/config-field-docs.test.cjs`) that asserts every `commands/gsd/*.md` has a matching `### \`/gsd-*\`` entry in `docs/COMMANDS.md`, and every `agents/gsd-*.md` has a matching `### gsd-*` entry in `docs/AGENTS.md`. Failure messages should point at the specific missing file. This is cheap to write because `tests/config-field-docs.test.cjs` already models the shape.
- 4b. Consider replacing numeric totals in `docs/ARCHITECTURE.md` with generated values via a template step in the build, so the count can never drift.
- 4c. Add a pre-release checklist item: every `CHANGELOG.md` `Added` bullet that introduces a command/agent/config key has a corresponding doc entry or an explicit "not documented: {reason}" line.

**Ordering rationale:**
- Track 1 before everything because `claude_md_path` and `tdd_mode` defects change operational behavior.
- Track 2 before Track 3 because leaving completeness claims in place while 3 lands means the corpus is still overclaiming during the catch-up window, compounding trust loss.
- Track 3 is the largest body of work; splitting it across PRs by surface family (commands, agents, architecture) lets reviewers keep each PR small.
- Track 4 pays forward: shipping it with Track 3 means the next release cannot recreate the same gap silently.

## Agreement, Revision, And Rejection Of Prior Lane Claims

I re-read `lane-01-upstream-docs-freshness.md` and `lane-01b-docs-gap-map.md` against what I derived independently. Each significant claim is adjudicated below. Citations in this section are to the primary sources I re-derived, not to the prior lane files.

| # | Prior claim (paraphrased) | Verdict | My primary evidence |
|---|--------------------------|---------|---------------------|
| T1 | Upstream docs freshness is uneven — split between older nav/inventory pages and newer config/feature pages. | **agree (re-derived)** | `docs/README.md:16,23` still references "18 agents" and "v1.32" news; `docs/CONFIGURATION.md:142-149,267` still carries v1.36.0 entries (plan_bounce, intel, claude_md_path). |
| T2 | Inventory surfaces are not authoritative: 31 tracked agents vs 18/21/24 in docs. | **agree (re-derived)** | `find agents -name 'gsd-*.md' \| wc -l` → 31; `docs/README.md:16`, `docs/AGENTS.md:3`, `docs/ARCHITECTURE.md:137`. |
| T3 | 73 tracked command files; `docs/COMMANDS.md` covers 72 headings after underscore/hyphen normalization; `/gsd-graphify` is missing entirely. | **agree (re-derived)** | `find commands/gsd -name '*.md' \| wc -l` → 73; comm-diff of stems vs `### \`/gsd-\`` headings shows only `graphify` and `extract_learnings`→`extract-learnings` differences; `commands/gsd/graphify.md:1-33` exists. |
| T4 | `/gsd-quick` and `/gsd-thread` ship richer subcommand surfaces than the docs describe. | **agree (re-derived)** | `commands/gsd/quick.md:3-4,29,35-38,53-60`; `commands/gsd/thread.md:3-4,23-29`; `docs/COMMANDS.md:627-644,1268-1284` show the older signatures. |
| T5 | `workflow.plan_phase.md` actively spawns `gsd-pattern-mapper`. | **agree (re-derived)** | `get-shit-done/workflows/plan-phase.md:18,621-666` calls the agent by name in the subagent_type field. |
| T6 | `claude_md_path` default: docs say null/none, template says `./CLAUDE.md`, tests confirm template. | **agree (re-derived, with a qualification)** | `docs/CONFIGURATION.md:98,114`; `templates/config.json:55`; `tests/claude-md-path.test.cjs:28-31,62`. My qualification: `bin/lib/core.cjs:390` does return `null` for unset keys, so the `null` reading is technically defensible for the runtime-fallback path. The doc is still wrong for the "shipped default" reading, which is the reader-expected meaning. |
| T7 | `workflow.tdd_mode` marked v1.37 in `docs/CONFIGURATION.md`; `FEATURES.md`, `CHANGELOG.md`, and workflow code place it in v1.36.0. | **agree (re-derived)** | `docs/CONFIGURATION.md:146`; `docs/FEATURES.md:2412`; `CHANGELOG.md:15`; `get-shit-done/bin/lib/config.cjs:20,164`. |
| T8 | `agent_skills` is documented in `docs/CONFIGURATION.md` and corroborated by tests. | **agree (re-derived)** | `docs/CONFIGURATION.md:193-245`; I confirmed `tests/agent-skills.test.cjs` exists via `ls tests/`. I did not re-read the test body line-for-line; my confidence is moderate. |
| T9 | Completeness language in `docs/README.md` ("Every command", "Complete feature…") no longer holds. | **agree (re-derived)** | `docs/README.md:12-16`; my own diff shows `/gsd-graphify` missing from COMMANDS.md and 10 agents missing from AGENTS.md. |
| T10 | `docs/AGENTS.md` omits `gsd-pattern-mapper` and `gsd-debug-session-manager`. | **agree (re-derived) and extend** | `docs/AGENTS.md` does not contain `### gsd-pattern-mapper` or `### gsd-debug-session-manager`. My re-derivation finds 10 omitted agents, not 2. The prior lane's framing is correct in kind but understated in quantity. |
| T11 | `docs/ARCHITECTURE.md` stale counts: 69 commands, 68 workflows, 24 agents, 35 references. | **agree (re-derived)** | `docs/ARCHITECTURE.md:116,127,137,141`; filesystem counts 73/71/31/42. |
| T12 | `docs/CLI-TOOLS.md` claims 15 modules; real count is higher. | **agree (re-derived), revise the count** | `docs/CLI-TOOLS.md:12` says "15 domain modules". My ls of `bin/lib/` shows 24. The prior lane noted the drift; I re-derived the exact count. |
| T13 | `docs/README.md` quick-links still frames v1.32 as the change horizon. | **agree (re-derived)** | `docs/README.md:23`. |
| T14 | `docs/FEATURES.md` correctly places prompt thinning (#114), claude_md_path (#115), TDD (#116) under v1.36.0. | **agree (re-derived) and extend** | `docs/FEATURES.md:2385-2425`. Extension: the TOC only lists up to #115; #116 is in the body but not the TOC. |
| T15 | Taxonomy: six classes (shipped inventory omission, underrepresented advanced surface, stale summary/signature, misleading default/provenance, stale completeness wrapper, architecture flattening). | **revise (the prior framing is accurate but over-decomposed)** | My re-read collapsed this to five classes (see Section 7). "Underrepresented advanced surface" reduces to either omission or stale signature; "architecture flattening" is narrative-level omission. The collapse changes nothing about remediation, but a simpler taxonomy makes the patch-bundle mapping one-to-one. |
| T16 | Track A/B/C/D/E patch-bundle structure. | **agree in shape, revise in ordering and scope** | My Track 1–4 structure preserves the prior lane's bundling logic but reorders (trust-bugs before completeness-language before missing-surface catch-up), merges the prior A and D into my 1 and 3, and adds explicit drift-control as Track 4 rather than a lower-priority E. The substantive content is consistent; the sequencing is revised. |
| T17 | Uneven git-history maintenance pressure across doc files (`docs/README.md` last in v1.32, `CONFIGURATION.md`/`COMMANDS.md` receiving v1.36.0 work). | **insufficient evidence to rule on it** | I did not run `git log --follow` against these files. The conclusion is plausible and consistent with content-level staleness I did observe, but I cannot re-derive it from primary git history in this run. |
| T18 | Lane-01b claim that "upstream root README is a better freshness-control surface than docs/README.md." | **agree (re-derived)** | Upstream root `README.md` carries a `v1.36.0 Highlights` block (I observed it via the lane-01 citation; I did not re-read the block line-by-line, but `docs/README.md:23` advertising v1.32 is sufficient one-sided evidence that the docs index is staler). |
| T19 | Lane-01 assertion that Codex hook install fix is corroborated by `tests/codex-config.test.cjs`. | **insufficient evidence to rule on it** | I did not read the test body in this run. `CHANGELOG.md:55` confirms the fix; the test's existence in my `ls tests/` output confirms a test file exists. I did not verify the line-range claim. |
| T20 | Lane-01 assertion that `agent-required-reading-consistency.test.cjs` corroborates the required_reading standardization (changelog entry #2176). | **agree (partial, qualified as file-exists-not-content-verified)** | `ls tests/` confirms the file exists; `CHANGELOG.md:46` confirms the changelog entry. I did not read the test body to verify it checks repo-wide consistency as asserted. |
| T21 | Lane-01b: "The seed is requalified from 'the upstream docs corpus' to 'a ranked hybrid doc seed with explicit exclusions.'" | **agree (re-derived in my own framing)** | My Net Verdict (Section 13) lands in the same place via a different path. |
| T22 | Lane-01b: project-skills awareness is "underrepresented rather than fully absent". | **agree (partial, qualified)** | `docs/CONFIGURATION.md:193-245` covers the config shape; the cross-doc "who consumes these skills" bridge is indeed thin. But I would qualify: the root README v1.36.0 highlights and `docs/CONFIGURATION.md:217-232` list consumer agent types explicitly, so calling this "underrepresented" is softer than it sounds — it is closer to "complete at one surface, under-cross-linked." I adopt the claim; I soften the framing. |

Claims deliberately not revisited (flagged, not silently omitted):

- Git-history-based maintenance-pressure inferences (T17 above).
- Line-range verifications inside `tests/agent-skills.test.cjs`, `tests/plan-bounce.test.cjs`, `tests/codex-config.test.cjs`, `tests/agent-required-reading-consistency.test.cjs` (I read headers or relied on file existence; I did not re-read bodies).
- The prior lanes' contention about "mainline drift already fixing some of this"; out of scope per my pinning to v1.36.0.

## Surfaces The Prior Lanes Did Not Examine

- **`docs/manual-update.md`** (62 lines). Reading it, I found it is focused and internally consistent with the installer behavior described in `docs/ARCHITECTURE.md:492-513`. It is not a source of gap pressure. Does not change the trust ranking; it belongs in the Trustworthy Summary Surfaces section.
- **`docs/FEATURES.md` TOC ordering and the #116 gap.** The prior lanes noted the staleness of `docs/FEATURES.md` in specific sections (quick mode, thread mode). They did not flag that the TOC is non-chronological and that Feature #116 (TDD Pipeline Mode) appears in the body but not the TOC. This is a navigation defect distinct from the signature-staleness defects the prior lanes caught.
- **Structural schema mismatch on `security_*` keys.** Prior lanes caught `claude_md_path` and `tdd_mode` as misleading defaults. I found that `docs/CONFIGURATION.md:83-85` places `security_enforcement`, `security_asvs_level`, `security_block_on` at the **root** of the config schema, while `templates/config.json:10-12` places them inside the **`workflow`** section. This is a structural-shape defect, not a value defect, and readers acting on the doc's Full Schema block may write those keys to the wrong location. The prior lanes did not call this out.
- **`planning.sub_repos` missing from Full Schema.** Present in `templates/config.json:26`, absent from `docs/CONFIGURATION.md:19-22`. A small additional completeness gap.
- **Five `bin/lib/` modules missing from `docs/ARCHITECTURE.md`** (`audit`, `graphify`, `gsd2-import`, `intel`, `learnings`). Prior lanes framed the module-count gap as "15 (CLI-TOOLS.md) / 19 (ARCHITECTURE.md) vs reality ~24" and flagged it as an inventory drift. I re-derived it and named the five specific missing modules, each of which corresponds to a documented command feature. This sharpens the gap: the architecture doc's CLI-tools table is not just numerically stale, it is silent about code that implements commands the same corpus documents.
- **Agent Spawn Categories table coverage gap.** `docs/ARCHITECTURE.md:273-287` lists 21 agents in its spawn-categories table. The 10 omitted agents are missing from this table too. Prior lanes flagged the `docs/AGENTS.md` omission; I am flagging that the architecture doc inherits the same blind spot.
- **`docs/AGENTS.md:471-495` Agent Tool Permissions Summary** — 21 rows, missing 10 agents, so the "least privilege" analysis it offers is also incomplete.

None of these materially change the trust ranking I give the corpus — they shift it in the same direction the prior lanes already pushed. They do add to Track 3's scope and add a small new item to Track 1 (the security-keys structural mismatch).

## Unresolved Uncertainties

- **Maintainer intent on withheld surfaces.** I cannot tell from the upstream tree whether `/gsd-graphify`, `gsd-pattern-mapper`, `gsd-debug-session-manager`, `gsd-intel-updater`, the AI-integration quintet, and the code-review pair are deliberately not surfaced in user-facing docs, or whether this is simple drift. The command-level docs say most of those pipelines exist; the agent- and architecture-level docs stay silent about them. Both interpretations (intent vs drift) are consistent with the evidence I have. A maintainer would have to weigh in.
- **Upstream `main` drift.** I am pinned to `v1.36.0` per the task spec. Some of these defects may already be fixed on `main`. I did not look.
- **Localization parity.** I did not read `docs/pt-BR`, `docs/ja-JP`, `docs/ko-KR`, `docs/zh-CN`. The same class of defects may or may not be present there, and any real docs-refresh track needs an explicit localization decision.
- **Git history evidence for uneven maintenance cadence.** I did not run `git log --follow` in this session. The doc-content-level staleness is sufficient to support the remediation plan, but I cannot independently attest the specific commit/date attribution the prior lanes used.
- **Test-body verifications.** For `tests/agent-skills.test.cjs`, `tests/plan-bounce.test.cjs`, `tests/codex-config.test.cjs`, `tests/agent-required-reading-consistency.test.cjs`, I relied on file existence plus the narrower tests I did read (`tests/claude-md-path.test.cjs`, `tests/graphify.test.cjs` head, `tests/config-field-docs.test.cjs`). My confidence in claims that refer to those tests is moderate rather than high.
- **Whether `docs/CONFIGURATION.md:443-456` model-profile coverage of 12 agents is intentional.** The docs never explicitly say the profile applies only to those 12 agents; the shipped `model_overrides` mechanism is agent-agnostic. A reader could reasonably wonder what the default resolution is for `gsd-code-reviewer` or `gsd-pattern-mapper`. I could not settle that without reading `bin/lib/model-profiles.cjs` in detail.
- **The "1M context" enrichment behavior described in `docs/ARCHITECTURE.md:307-322`.** I accepted it as directionally correct against the mention of `config_get context_window` in the doc, but I did not trace it through `init.cjs` end-to-end.

I did not let any of these uncertainties collapse into false certainty. Where I adopt a claim at moderate confidence, I say so.

## What Would Change My Judgment

Concrete observations that would cause me to revise either the trust ranking or the supplementation strategy:

- **If maintainers published a "docs policy" stating that graphify / pattern-mapper / debug-session-manager / AI-integration agents are intentionally undocumented in user-facing surfaces**, I would reclassify those from "shipped inventory omission" to "intentional exclusion" and remove them from Track 3. The supplementation strategy would then be about labeling the absence rather than filling it.
- **If `git log --follow` on the individual doc files showed that `docs/CONFIGURATION.md:146` was corrected post-v1.36.0 on `main`** (tdd_mode provenance), I would lower the severity of that trust bug from "load-bearing" to "already addressed upstream, carry a local note."
- **If I read the bodies of `tests/agent-skills.test.cjs` and `tests/plan-bounce.test.cjs` and found they do not actually exercise the behaviors I attributed to them**, the "trustworthy seed" rating for `docs/CONFIGURATION.md` would drop a notch, since my trust rests partly on test corroboration.
- **If `templates/config.json:10-12` turns out to be a bug** (security keys in the wrong section) **that the shipped code corrects at runtime**, the structural-schema-mismatch trust bug I flagged for Track 1 drops in severity; it becomes a template patch, not a doc patch.
- **If `docs/FEATURES.md:2412-2425` proves to be narrative-only while the actual code implementing TDD mode is absent or stub**, that changes the Corroboration Surfaces trust picture — the docs would be overclaiming feature completeness, which is a sharper defect than a provenance label.
- **If a separate internal consistency test** (e.g., a command-file ↔ doc-entry assertion) **already exists in `tests/`** and I missed it, Track 4a is unnecessary and the overall taxonomy's "stale inventory metadata" class becomes less urgent because drift control is already partly wired.
- **If localized docs (`docs/pt-BR`, etc.) contain corrections to the English versions**, the trust ranking of English-language surfaces drops relative to localized ones, and Track 3 acquires a "port corrections back" sub-task I have not modeled.
- **If the maintainer wire-up for `gsd-tools.cjs config-get --default` returns `./CLAUDE.md` even when the doc says null** (which `tests/claude-md-path.test.cjs:38-41` may already be doing), then the `claude_md_path` issue is a documentation-only defect, not a behavior defect. Either way it still deserves Track 1a, but the blast radius is smaller.

## Net Verdict

The upstream `v1.36.0` docs corpus is **strong enough to seed a later docs-refresh or docs-seeded remapping pass, but only as a ranked hybrid seed with explicit exclusions and a corrective overlay.** The trustworthy spine is the layered-architecture story, the config namespace surface, the core-phase-chain command entries, the well-scoped topic docs (`context-monitor.md`, `workflow-discuss-mode.md`, `manual-update.md`), and individual agent entries for the 21 agents actually documented. The corpus is **not** trustworthy as an exhaustive inventory (10 of 31 shipped agents and `/gsd-graphify` entirely are absent from agent/command references; five of 24 `bin/lib/` modules are absent from the architecture doc; `planning.sub_repos` is absent from the config schema), **not** trustworthy on shipped defaults (`claude_md_path` and `security_*` placement are both wrong or structurally misplaced), **not** trustworthy on version provenance (`workflow.tdd_mode` is off by one minor version, `docs/README.md` still advertises v1.32 as current), and **not** trustworthy as a release-complete feature list for v1.36.0. A guarded later pass should inherit the corpus's trustworthy sections directly, apply the Track 1 trust-bug hotfixes before acting on any default, weaken or remove the corpus's completeness claims until Track 3 lands, and add a Track 4 drift-control mechanism (file ↔ doc parity test) so the same class of errors does not recur at the next release. Under those conditions — and only under those conditions — the v1.36.0 docs qualify as seed substrate, not as sovereign ground truth and not as discardable noise.
