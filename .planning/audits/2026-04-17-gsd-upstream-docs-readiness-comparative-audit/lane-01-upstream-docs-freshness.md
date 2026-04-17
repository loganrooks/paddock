# Lane 01: Upstream Docs Freshness Audit

## Question

- Mode: `synthesis / comparative freshness audit`
- Question: How fresh and corroborated is the upstream `v1.36.0` docs corpus as a seed for later harness mapping?
- Scope: pinned `docs/` corpus compared against `CHANGELOG.md`, local git history for doc files, selected commands/workflows, selected implementation files, and targeted tests where doc claims were contested.
- Non-goals: local-runtime overlay analysis, upstream `main` trajectory, localized docs, or a full command-by-command rewrite audit.
- Stopping point: enough evidence to classify which doc surfaces are load-bearing, which are stale or partial, and what cautions later lanes must carry.

## Corpus Read

- Governing local artifacts: `PROGRAM.md`, `STATUS.md`, Checkpoint 5 upstream reference points, Checkpoint 5 upstream baseline schema, readiness doctrine, and audit-comparison policy.
- Upstream docs corpus read: `docs/README.md`, `ARCHITECTURE.md`, `AGENTS.md`, `CONFIGURATION.md`, `COMMANDS.md`, `CLI-TOOLS.md`, `FEATURES.md`, `USER-GUIDE.md`, `context-monitor.md`, and `workflow-discuss-mode.md`.
- Corroboration surfaces read from pinned `v1.36.0`: `CHANGELOG.md`; git history for the candidate docs; `commands/gsd/{graphify,quick,thread,extract_learnings}.md`; `get-shit-done/workflows/{plan-phase,quick}.md`; `get-shit-done/bin/{gsd-tools.cjs,lib/init.cjs}`; `get-shit-done/templates/config.json`; tests `{agent-skills,agent-required-reading-consistency,claude-md-path,plan-bounce,codex-config,graphify}.test.cjs`.
- Path of inquiry: start from docs inventory, test changelog propagation, inspect code/tests where the docs claimed completeness or conflicted on counts/defaults, then record only the bounded surfaces needed to judge freshness.
- Deferred: localized docs, root-level repo docs other than one comparison spot-check in upstream `README.md`, and all `main`-branch post-`v1.36.0` changes.

## Freshness Findings

### 1. Freshness is uneven across the corpus, not uniform

Direct evidence:

- `docs/README.md` still advertises the agent reference as “All 18 specialized agents” and its quick-links section still says “What’s new in v1.32” (`docs/README.md:11-23`).
- `docs/AGENTS.md` says “All 21 specialized agents” and its category table sums to 21 (`docs/AGENTS.md:3,13-27`).
- `docs/ARCHITECTURE.md` says “Total agents: 24” (`docs/ARCHITECTURE.md:129-137`).
- Local git history observation shows split maintenance pressure: `docs/README.md` was last touched in a v1.32 docs update (`05c08fd`), `docs/AGENTS.md` in a v1.33 stale-count fix (`30a8777`), `docs/ARCHITECTURE.md` in a v1.34 docs update (`641ea8a`), while `docs/CONFIGURATION.md` and `docs/COMMANDS.md` were still receiving v1.36 work (`e24cb18`, `c17209f`).

Inference:

- “Upstream docs freshness” is not one scalar. The corpus is split between older inventory/navigation pages and newer feature/config/reference pages.

### 2. Inventory surfaces are not authoritative enough to use as complete mapping seeds

Direct evidence:

- Tracked filesystem inventory observation: the pinned repo contains 31 tracked `agents/gsd-*.md` files, not 18, 21, or 24.
- Two examples present on disk but absent from `docs/AGENTS.md` are `gsd-pattern-mapper` (`agents/gsd-pattern-mapper.md:1-20`) and `gsd-debug-session-manager` (`agents/gsd-debug-session-manager.md:1-20`).
- The pinned repo contains 73 tracked command files under `commands/gsd/`. After underscore/hyphen normalization, `docs/COMMANDS.md` documents 72 command headings and still misses `gsd-graphify` entirely; the shipped command exists in `commands/gsd/graphify.md` (`commands/gsd/graphify.md:1-20`).
- `docs/README.md` describes `FEATURES.md` as “Complete feature and function documentation” and `COMMANDS.md` as “Every command with syntax, flags, options, and examples” (`docs/README.md:12-16`).

Inference:

- The docs corpus can orient a reader, but it cannot be treated as an exhaustive inventory of shipped agents or commands without a direct filesystem/code cross-check.

### 3. Several `v1.36.0` operational changes reached code/tests but did not fully propagate into `docs/`

Direct evidence:

- `CHANGELOG.md` for `1.36.0` adds `/gsd-graphify`, `gsd-pattern-mapper`, quick/thread subcommands, debug session management, project skills awareness, and TDD mode (`CHANGELOG.md:11-38`).
- `commands/gsd/quick.md` exposes `--validate` plus `list`, `status <slug>`, and `resume <slug>` subcommands (`commands/gsd/quick.md:2-39,53-80`), but `docs/COMMANDS.md` only lists `--full`, `--discuss`, and `--research` (`docs/COMMANDS.md:627-644`), and `docs/FEATURES.md` still defines quick mode as `/gsd-quick [--full] [--discuss] [--research]` (`docs/FEATURES.md:445-460`).
- `commands/gsd/thread.md` exposes `list --open`, `list --resolved`, `status <slug>`, and `close <slug>` (`commands/gsd/thread.md:1-80`), but `docs/COMMANDS.md` and `docs/USER-GUIDE.md` still only describe list/resume/create (`docs/COMMANDS.md:1268-1284`; `docs/USER-GUIDE.md:289-303`), and `docs/FEATURES.md` still says threads support only create/list/resume (`docs/FEATURES.md:1124-1137`).
- `commands/gsd/graphify.md` exists and requires `config.graphify.enabled` (`commands/gsd/graphify.md:1-33`), `gsd-tools.cjs` exposes `graphify {build,query,status,diff}` (`get-shit-done/bin/gsd-tools.cjs:1083-1105`), and graphify has its own code/test surface (repo search observation). Yet `graphify` is absent from `docs/README.md`, `docs/COMMANDS.md`, `docs/FEATURES.md`, `docs/CLI-TOOLS.md`, and `docs/USER-GUIDE.md` (repo search observation).
- `get-shit-done/workflows/plan-phase.md` lists `gsd-pattern-mapper` as a valid subagent type (`get-shit-done/workflows/plan-phase.md:15-21`), but `docs/AGENTS.md` does not include it.

Inference:

- The biggest freshness failures are not random typos. They cluster around newer discovery/inventory surfaces, which means a later mapper could form a systematically incomplete upstream picture if they trust the docs tree alone.

### 4. Some reference pages are still load-bearing when cross-checked

Direct evidence:

- `docs/CONFIGURATION.md` documents `agent_skills` in detail (`docs/CONFIGURATION.md:193-245`), the implementation reads `config.agent_skills[agentType]` directly (`get-shit-done/bin/lib/init.cjs:1489-1578`), and `tests/agent-skills.test.cjs` exercises the injected `<agent_skills>` block (`tests/agent-skills.test.cjs:1-120`).
- `docs/FEATURES.md` correctly describes prompt thinning and TDD mode as explicit features (`docs/FEATURES.md:2385-2425`), and the relevant behavior appears in workflow/agent code (`get-shit-done/workflows/plan-phase.md:30-39`; repo search observation in `agents/gsd-planner.md`).
- `docs/CONFIGURATION.md` documents `workflow.plan_bounce_passes = 2` (`docs/CONFIGURATION.md:142-146`), and both tests and workflow code corroborate that default (`tests/plan-bounce.test.cjs:50-76`; `get-shit-done/workflows/plan-phase.md:1023-1026`).
- The Codex hook-install fix in the changelog (`CHANGELOG.md:51-56`) is backed by a dedicated e2e test that verifies the referenced hook file is physically installed (`tests/codex-config.test.cjs:820-845`).
- The agent `required_reading` standardization in the changelog (`CHANGELOG.md:45-47`) is backed by a repo-wide consistency test (`tests/agent-required-reading-consistency.test.cjs:1-78`).

Inference:

- The upstream docs corpus is most trustworthy where it is paired with tests or templates. `CONFIGURATION.md` and covered parts of `FEATURES.md` / `COMMANDS.md` are materially stronger than `README.md`, `AGENTS.md`, and `ARCHITECTURE.md`.

## Internal Doc Contradictions

Direct evidence:

- Agent-count conflict:
  - `docs/README.md` says agent reference covers 18 agents (`docs/README.md:16`).
  - `docs/AGENTS.md` says 21 (`docs/AGENTS.md:3,13-27`).
  - `docs/ARCHITECTURE.md` says 24 (`docs/ARCHITECTURE.md:137`).
  - Filesystem inventory observation shows 31 tracked agent specs.
- `workflow.tdd_mode` version conflict:
  - `CHANGELOG.md` introduces opt-in TDD pipeline mode in `1.36.0` (`CHANGELOG.md:11-16`).
  - `docs/FEATURES.md` places it in section 116 of the `v1.36.0` feature block (`docs/FEATURES.md:2412-2425`).
  - `docs/CONFIGURATION.md` still marks `workflow.tdd_mode` as “Added in v1.37” (`docs/CONFIGURATION.md:146`).
- `claude_md_path` default conflict:
  - `docs/CONFIGURATION.md` full-schema example and core settings table show `claude_md_path` as `null` / “(none)” (`docs/CONFIGURATION.md:98,114`).
  - `docs/FEATURES.md` says `claude_md_path` defaults to `./CLAUDE.md` (`docs/FEATURES.md:2399-2408`).
  - The shipped template sets `"claude_md_path": "./CLAUDE.md"` (`get-shit-done/templates/config.json:53-56`), and the dedicated test asserts the same default (`tests/claude-md-path.test.cjs:22-31`).
- Completeness claim conflict:
  - `docs/README.md` promises `COMMANDS.md` covers every command and `FEATURES.md` is complete (`docs/README.md:12-16`).
  - Repo comparison shows `gsd-graphify` is shipped but absent from both `docs/COMMANDS.md` and `docs/FEATURES.md`.

Inference:

- The contradictions are load-bearing enough that doc self-description is not currently a reliable confidence signal. The corpus can sound more complete than it is.

## Changelog / Test Corroboration

| Surface | Changelog pressure | Code/test corroboration | Docs status | Judgment |
| --- | --- | --- | --- | --- |
| `/gsd-graphify` | Added in `1.36.0` (`CHANGELOG.md:12`) | Command file exists (`commands/gsd/graphify.md:1-33`), CLI route exists (`get-shit-done/bin/gsd-tools.cjs:1083-1105`), graphify code/tests exist (repo search observation) | Missing from `docs/README`, `COMMANDS`, `FEATURES`, `CLI-TOOLS`, `USER-GUIDE` | Missing from audited docs corpus despite live implementation |
| `gsd-pattern-mapper` | Added in `1.36.0` (`CHANGELOG.md:13`) | Agent file exists (`agents/gsd-pattern-mapper.md:1-20`), plan-phase exposes it (`get-shit-done/workflows/plan-phase.md:15-21`) | Missing from `docs/AGENTS.md` and not surfaced in other audited docs | Missing from agent inventory and architecture story |
| `/gsd-quick` and `/gsd-thread` subcommands | Added in `1.36.0` (`CHANGELOG.md:19`) | Command files define new subcommands (`commands/gsd/quick.md:2-80`; `commands/gsd/thread.md:1-80`) | COMMANDS / FEATURES / USER-GUIDE remain on older signatures (`docs/COMMANDS.md:627-644,1268-1284`; `docs/FEATURES.md:445-460,1124-1137`; `docs/USER-GUIDE.md:289-303`) | Partially propagated; user-facing docs are stale |
| `agent_skills` / project skills awareness | Added in `1.36.0` (`CHANGELOG.md:21`) | Implementation and tests are present (`get-shit-done/bin/lib/init.cjs:1489-1578`; `tests/agent-skills.test.cjs:1-120`); quick workflow also loads project skills (`get-shit-done/workflows/quick.md:589-596`) | `CONFIGURATION.md` documents the feature well (`docs/CONFIGURATION.md:193-245`) | One of the stronger, corroborated doc surfaces |
| `workflow.tdd_mode` | Added in `1.36.0` (`CHANGELOG.md:15`) | Workflow/test surfaces exist (`get-shit-done/workflows/plan-phase.md:30-39`; repo search observation) | Present, but `CONFIGURATION.md` mis-tags version as v1.37 (`docs/CONFIGURATION.md:146`) | Semantically documented, but provenance/version freshness is off |
| `claude_md_path` | Added in `1.36.0` (`CHANGELOG.md:31`) | Template and tests set default `./CLAUDE.md` (`get-shit-done/templates/config.json:53-56`; `tests/claude-md-path.test.cjs:22-31`) | Present, but default is misstated in `CONFIGURATION.md` (`docs/CONFIGURATION.md:98,114`) | Documented with a real default-value bug |
| Codex hook install fix | Fixed in `1.36.0` (`CHANGELOG.md:55`) | Dedicated e2e regression test exists (`tests/codex-config.test.cjs:820-845`) | Mostly inferable from architecture/hook docs, not highlighted in reference docs | Corroborated runtime claim; docs do not make it especially visible |

## Docs Strong Enough For What?

Direct evidence:

- The strongest corroborated docs are `CONFIGURATION.md` for covered config areas, `FEATURES.md` for covered feature narratives, and individual command pages when they have kept pace with runtime behavior.
- The weakest docs are inventory/navigation surfaces (`docs/README.md`, `docs/AGENTS.md`, `docs/ARCHITECTURE.md`) and command/guide summaries that promise completeness but omit newer surfaces.

Inference:

- The upstream docs corpus is strong enough to seed a later mapping pass for:
  - core workflow vocabulary
  - artifact names and phase-chain concepts
  - config namespace discovery
  - older, well-established command families
- It is not strong enough to be treated as authoritative for:
  - exhaustive command or agent inventory
  - release-complete feature discovery in `1.36.0`
  - exact defaults or “Added in vX.Y” provenance
  - deciding that earlier readiness mapping can be discarded as superseded
- Lane-level judgment: upstream docs are usable as a mapping seed only if later lanes ratify load-bearing claims against code, tests, and changelog before promotion. This lane does not justify promoting the docs corpus to sovereign ground truth.

## Unknowns

- I did not audit localized docs under `docs/pt-BR`, `ja-JP`, or `zh-CN`; they may be fresher, equally stale, or differently stale.
- I did not inspect upstream `main` after `v1.36.0`; some drift may already be fixed there.
- I did not enumerate every `1.36.0` changelog item against every doc page. The audit focused on architecture/config/runtime/workflow-semantics pressure rather than exhaustive release-note bookkeeping.
- I did not verify whether omitted surfaces such as graphify are intentionally withheld from public docs or simply missing. The current repo state only shows that they are shipped but under-documented in the audited corpus.

## What The Obligations Didn't Capture

Direct evidence:

- The candidate surface list did not include upstream root `README.md`, but that file already carries `v1.36.0` highlights including graphify and project skills awareness (`README.md:92-98`). That made it a useful negative-control surface for `docs/README.md`.
- The named test list in the spec was not sufficient for the strongest contradictory claims. I had to read `tests/claude-md-path.test.cjs` and `tests/graphify.test.cjs` to judge real doc/code drift on defaults and missing feature coverage.
- The spec did not explicitly call for filesystem inventory comparison. That comparison turned out to be necessary because the docs disagree with each other on counts and because completeness claims could not be evaluated honestly without counting shipped agents/commands.

Inference:

- The lane spec was slightly under-scoped for freshness work. I did not widen ownership beyond this file, but I did widen the read set enough to keep the audit from falsely promoting the docs corpus as more complete than it is.

## Follow-on Pressure For Later Lanes

- Lane 02 should weight upstream doc families differently instead of treating “upstream docs” as one coherent truth source. `CONFIGURATION.md` and selected workflow/command/test surfaces have much higher standing than `docs/README.md`, `docs/AGENTS.md`, and `docs/ARCHITECTURE.md`.
- Lane 03 should not frame the decision as “old readiness mapping vs fresh upstream docs.” The stronger framing is “readiness mapping vs a hybrid upstream seed assembled from docs plus code/tests.” This lane does not support a clean docs-only reseed.
- If later judgment needs a stronger yes/no on upstream-doc trust, an optional follow-on lane should do a direct docs-vs-runtime inventory drift pass for missing `1.36.0` surfaces, especially graphify, pattern-mapper, quick/thread subcommands, and graphify config keys.
- Any later synthesis that uses upstream docs as a seed should explicitly exclude self-completeness claims (“all agents”, “every command”, “complete feature reference”) unless a code/test crosswalk has revalidated them.
