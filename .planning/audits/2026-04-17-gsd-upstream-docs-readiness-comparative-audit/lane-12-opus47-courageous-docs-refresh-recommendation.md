# Lane 12: Courageous Docs Refresh Recommendation

> A recommendation lane. No edits to the upstream repo; no PR actions. Output is this artifact only.
> Grounded in the live docs tree, the three local commits (`88e0169`, `164cdb7`, `8521364`), and the prior audit artifacts (Lane 07 proposal, Lane 10 underreach audit, Lane 11 PR3 substantive report).
> Written to optimize for *a better, truer, more maintainable docs system*, not for the lowest-friction PR shape.

---

## Current State Judgment

**Short version.** PR1 is surgical and directionally right but materially incomplete — it missed a load-bearing duplicate in the same trust-bug class it was meant to fix. PR2 is the strongest of the three: it takes a position on `security_*` placement, closes the v1.36.0 surface gap, and explicitly records the `VALID_CONFIG_KEYS` follow-up without pretending to close it. PR3 is the biggest leap — creating `docs/INVENTORY.md` was the right architectural call — but it stops at "complete for agents, selective for others," which is half the commitment the file's name makes. Taken together, the stack is *materially good but structurally unfinished*: it is substantive progress, not a shipped redesign.

**Per-commit judgment.**

- **PR1 (`88e0169`, 4 files / 9 edits).** Materially good on the trust bugs it names: `claude_md_path` default, `tdd_mode` provenance, `discuss_mode` default in the USER-GUIDE table, the `docs/README.md` overclaim delinkage. **But it missed a strictly-adjacent duplicate:** `docs/USER-GUIDE.md:581` still contains `"discuss_mode": "standard"` inside the abbreviated Full Schema block at lines 564–596. PR1 fixed the table at line 627 and left the JSON above it carrying the bug. A reader who copy-pastes the schema block, not the table, acts on the wrong default. This is the exact class of defect PR1 existed to close. Call it 80 % complete on its own charter.
- **PR2 (`164cdb7`, 4 files / 110 insertions).** Materially good, courageously scoped. It is the only commit in the stack that takes a runtime-adjacent position (`workflow.security_*` as canonical) and it records the `VALID_CONFIG_KEYS` gap honestly instead of papering over it. The graphify additions are anchored to `commands/gsd/graphify.md` and the CHANGELOG entry — nothing invented. No gap I would fix in this PR itself.
- **PR3 (`8521364`, 3 files / 359 insertions).** Materially good on the agent-inventory truth axis that Lane 10 demanded. The 31-row agent table in `docs/INVENTORY.md` plus the 10 new Advanced Agent stubs in `docs/AGENTS.md` plus the explicit "Scope: 21 primary agents only" callout on the permissions table together resolve the original underreach. **The new architectural weakness is INVENTORY.md's self-scoping.** It is "complete for agents, selectively detailed for others." That is exactly the posture that landed the corpus in its current drift state: promise the index, deliver the curated subset, re-drift at the next release. If `docs/INVENTORY.md` is worth creating at all — and it is — it is worth filling out across all six families.

**What the stack has genuinely achieved** (worth building on, not rewriting):

- A factually accurate set of *defaults* in `docs/CONFIGURATION.md` and `docs/USER-GUIDE.md` (the table, at least).
- A factually accurate *v1.36.0 surface inventory* in `docs/COMMANDS.md`, `docs/CLI-TOOLS.md`, `docs/FEATURES.md`.
- A single canonical placement decision for `security_*` (`workflow.*`) that matches the shipped template.
- A real inventory file with an authoritative agent roster, plus concise stubs for the ten previously-invisible agents.
- A per-section fallback posture on model profiles (18 covered ⊂ 31 shipped) that enumerates the 13 uncovered agents by name instead of waving at them.

**What the stack has not done** (and where the earlier proposal was too cautious):

- `docs/USER-GUIDE.md:564–640` still duplicates the config reference that `docs/CONFIGURATION.md` already owns — and that duplication has demonstrably drifted (line 581). The earlier proposal asked to "delete and link" in PR 4; there is no reason this is PR 4 rather than PR 1.
- `docs/ARCHITECTURE.md` is now the least-true file in the set — its references-count (`35` @ L141), domain-modules count (`19` @ L221), Agent Spawn Categories table (L273-287, 21-era), Hook table (9 rows @ L207-218), and Installation File Layout (3-hook enumeration @ L419-423) all contradict the numbers `docs/INVENTORY.md` introduced one commit ago. The proposal deferred this to PR 5 cleanup. That is too soft: ARCHITECTURE.md is exactly the file a new contributor reads first.
- `docs/INVENTORY.md`'s commands/workflows/references sections are narrative + count. The file's value as a drift anchor is proportional to how many row-level facts it carries. At ~150 lines it has capacity for 75 + 72 + 41 more rows without becoming unusable; at that size it genuinely becomes the single source a drift test can lock against.
- `docs/AGENTS.md` is now a hybrid: 21 primary cards + 10 advanced stubs + a scoped permissions table that inherently can't grow. That is *one release cycle* worth of architecture. The next agent added forces a category decision (primary or advanced?) that is a purely stylistic call with no principled answer. The earlier proposal never said this; it should have.
- `docs/workflow-discuss-mode.md:29–33` still uses `gsd-tools config-set` rather than the shipped invocation form. Minor but unresolved.
- `docs/COMMANDS.md:3` still subtitles "Complete command syntax, flags, options, and examples" — the same "Complete" / "Every" overclaim language PR1 deleted from `docs/README.md`.
- `docs/FEATURES.md:110-142` still orders v1.36.0 before v1.32 in the TOC.

Net: the stack moved the needle from "not trustworthy" to "mostly trustworthy on defaults and v1.36.0 surfaces; inconsistent on inventory truth across ARCHITECTURE vs INVENTORY vs AGENTS." That is progress, not completion.

---

## Target Docs Architecture

The target is **not** a restructure of file topology — the nine-file shape is fine. The target is a redefinition of *what each file is allowed to claim authority over*, enforced by one consolidated roster file and mechanical drift guards.

**Principle 1 — one family, one authority.**
Every shipped surface family (commands, agents, workflows, references, CLI modules, hooks) has exactly one file that is the authoritative roster. That file carries a row per shipped item, derived from the filesystem. Other docs reference the roster; they do not re-enumerate it.

**Principle 2 — narrative vs inventory, never both in one file.**
Broad docs (`ARCHITECTURE.md`, `AGENTS.md`, `COMMANDS.md`, `USER-GUIDE.md`, `FEATURES.md`) describe *how* and *why*. The inventory file describes *what ships*. When a broad doc needs to show a roster, it links; it does not copy.

**Principle 3 — counts are mechanical or absent.**
No broad doc carries a hardcoded surface count ("19 modules", "35 references", "21 agents") unless a CI test locks the number to the filesystem. If a number is not CI-locked, it is deleted and replaced with a link to the authoritative roster or the directory.

**Principle 4 — `CHANGELOG.md` is the only version-labeled narrative.**
Broad docs never carry "What's new in v1.XX" blocks. They reference `CHANGELOG.md` and the root `README.md`. This is already PR1's posture on `docs/README.md`; it should be enforced across the corpus.

**Concrete role for each file under the target.**

- **`docs/README.md`** — navigation index. Eight one-line pointers to the other docs. No "what's new," no counts, no version claims. (PR1 took this almost all the way; fine as-is.)
- **`docs/INVENTORY.md`** — authoritative roster for all six families, fully enumerated. This is the file a drift test locks to. **First-class**, yes — and larger than its current 150 lines.
- **`docs/ARCHITECTURE.md`** — conceptual topology. The *agent model*, *orchestrator pattern*, *wave execution*, *data flow*, *installation layout narrative*. No component counts, no per-item roster, no duplicated hook enumeration. Points at INVENTORY.md for rosters.
- **`docs/AGENTS.md`** — *how agents work in GSD*. Orchestrator → agent pattern, tool permissions principle, spawn parallelism conventions, model-profile resolution, agent output formats. Under the **target** architecture (see "Phase 2" in the implementation-shape section) this file contains no per-agent role cards; it directs readers to INVENTORY.md for the roster and to `agents/gsd-*.md` for each agent's own frontmatter+body. Under the **Phase 1** architecture (what the current stack is partway to) it keeps the 21 primary cards + delegates advanced agents to INVENTORY.md, but that is a transitional shape.
- **`docs/COMMANDS.md`** — user-facing command usage reference. Every *stable* command described with flags/examples. Commands that are documented only by example — or specialty commands like `/gsd-ai-integration-phase`, `/gsd-eval-review`, `/gsd-select-framework`, `/gsd-from-gsd2`, `/gsd-extract-learnings` — are listed with a one-line description + link to the command file rather than omitted. The file's header subtitle drops "Complete" / "Every."
- **`docs/CONFIGURATION.md`** — single authoritative config reference. Every shipped key, shipped default, shipped provenance. The `USER-GUIDE.md` schema duplicate (L564–596) is deleted.
- **`docs/FEATURES.md`** — per-feature narratives with REQ-IDs. Chronological TOC. No count claims; features are ordered by release, releases by date.
- **`docs/CLI-TOOLS.md`** — programmatic API reference for `gsd-tools.cjs` and `gsd-sdk query`. Points at INVENTORY.md's CLI Modules table as authoritative; describes each verb family and its handler signature. No inline module count.
- **`docs/USER-GUIDE.md`** — lifecycle walkthroughs. Workflow diagrams, UI contract, backlog/threads, workstreams, security narrative, usage examples, troubleshooting, recovery. The file *does not* re-document commands or config — those sections get deleted and replaced with one-paragraph "see X" pointers. This is the single largest duplication-kill in the corpus.
- **`docs/context-monitor.md`, `docs/workflow-discuss-mode.md`, `docs/manual-update.md`** — focused topic docs. Stable. Fix the `gsd-tools config-set` invocation syntax and leave them alone.

**Drift guards (mechanical, not aspirational).**
Extending the pattern already landed on `main` (`tests/architecture-counts.test.cjs`, `tests/command-count-sync.test.cjs`):

1. `tests/inventory-counts.test.cjs` — parses each of the six family tables in `docs/INVENTORY.md` and asserts row count matches `ls commands/gsd/*.md | wc -l`, etc. One test, six assertions.
2. `tests/commands-doc-parity.test.cjs` — for every `commands/gsd/*.md`, assert the file name appears either (a) as a `### /gsd-*` heading in `docs/COMMANDS.md` or (b) as a row in `docs/INVENTORY.md`. Failure names the missing file.
3. `tests/agents-doc-parity.test.cjs` — for every `agents/gsd-*.md`, assert the agent name appears as a row in `docs/INVENTORY.md`'s agent table. (AGENTS.md card presence is *not* enforced — that file is allowed to be a curated subset under Phase 1.)
4. `tests/cli-modules-doc-parity.test.cjs` — for every `get-shit-done/bin/lib/*.cjs`, assert the module name appears in `docs/INVENTORY.md`'s CLI Modules table.
5. `tests/hooks-doc-parity.test.cjs` — similar, for `hooks/*` vs INVENTORY.md's hook table.

These five tests — written once, locked forever — are the mechanism that makes the target architecture durable.

---

## Keep / Revise / Replace Decisions For Existing Local Work

| Branch | Commit | Decision | Detail |
|---|---|---|---|
| `docs/pr1-trust-bug-hotfixes` | `88e0169` | **Revise** (amend or extend on same branch) | Add one more edit: `docs/USER-GUIDE.md:581` `"discuss_mode": "standard"` → `"discuss_mode": "discuss"`. Same trust-bug class, same PR. Also fix `docs/COMMANDS.md:3` subtitle — strip "Complete"/"Every" to match the posture the README now carries. Nine edits becomes eleven; still a small PR. |
| `docs/pr2-shipped-surface-catchup` | `164cdb7` | **Keep** (accept as-is) | No changes. The PR is courageously scoped and honest about its one deferred item (`VALID_CONFIG_KEYS`). |
| `docs/pr3-inventory-model-profile-truth` | `8521364` | **Revise substantially** (amend or replace with a larger commit on the same branch) | Keep everything it already does. **Add full enumeration to `docs/INVENTORY.md`'s commands, workflows, and references sections** — one row per shipped item, one-line role, link to source. This is the courage-upgrade Lane 10 asked for the first time and got partial. Also add, in this same PR, the INVENTORY-referencing edits to `docs/ARCHITECTURE.md` (references count, modules count, Agent Spawn Categories footer) so the ARCHITECTURE/INVENTORY mismatch that the current stack introduces does not survive the PR that introduces it. |
| *(new, proposed)* PR4 | — | **Replace the prior PR 4+PR 5 pair with a single "consistency + drift guards" PR** | Collapses the prior proposal's PR4 (structural delete-and-link) and PR5 (cleanup). Drops the stale `USER-GUIDE.md` config sections, normalizes `workflow-discuss-mode.md` invocation syntax, reorders the `FEATURES.md` TOC chronologically, reconciles `ARCHITECTURE.md` Hook table with Installation Layout diagram, and lands all five doc-parity tests from the Target Architecture section. |
| *(new, proposed, deferred)* PR5 | — | **Defer to a later release cycle** | AGENTS.md structural redesign — delete per-agent role cards, let INVENTORY.md own the roster, rewrite AGENTS.md as a narrative about *how agents work in GSD*. Not part of the current refresh; propose when PR4 has proven the INVENTORY-as-authority pattern holds for a release cycle. |

**On discarding anything from the stack.** Nothing in the current three commits should be discarded. The stack accumulated real truth. The criticism is that it stopped short, not that it misfired.

**On squashing the stack.** Tempting — the three commits are each small — but not recommended. The separation *by concern* (trust bugs vs surface catchup vs inventory truth) is the single most useful signal a reviewer has. Squashing trades review legibility for branch count.

---

## File-By-File Recommendations From Current State

For each file, current-state assessment + next recommended change + which PR bucket owns it under the revised structure.

### `docs/README.md` — navigation index
**Current:** Correct as of PR1. "What's new" bullet replaced with CHANGELOG pointer. "All 18 agents" / "Every command" / "Complete feature" language gone.
**Recommend:** Leave alone.
**PR bucket:** — (done).

### `docs/CONFIGURATION.md` — config reference
**Current:** Accurate on `claude_md_path`, `tdd_mode`, `security_*` placement, `planning.sub_repos`, model-profile fallback. The strongest file in the corpus after PR1+PR2+PR3.
**Recommend:** Leave alone. Any further change should be feature-driven, not drift-driven.
**PR bucket:** — (done).

### `docs/AGENTS.md` — agent reference
**Current:** Hybrid. 21 primary role cards + 10 advanced stubs + a scoped permissions table. Internally coherent after PR3. Header claims 31 total with 21 primary + 10 advanced. Permissions table is explicitly primary-only.
**Recommend, Phase 1 (current stack):** Leave alone. PR3's shape is defensible for one release cycle.
**Recommend, Phase 2 (deferred PR5):** Delete all 31 per-agent cards. Replace with three narrative sections — *how agents spawn*, *how model profiles resolve*, *how tool permissions are principled* — and point every "what agents ship" question at `docs/INVENTORY.md`. Rationale: the primary-vs-advanced categorization has no principled rule; every new agent forces a stylistic call; sooner or later the rule breaks. Killing the cards now kills a whole class of future drift.
**PR bucket:** — (Phase 1 done; Phase 2 deferred to post-refresh).

### `docs/INVENTORY.md` — authoritative shipped-surfaces inventory
**Current:** Full for agents (31), full for CLI modules (24), full for hooks (11). *Narrative+count* for commands (75), workflows (72), references (41). This is the courage gap.
**Recommend:** Fill out all three under-enumerated sections to the same standard as the agent table. Each row: name, one-line role, source link. A 75-row command table and a 41-row references table are not unwieldy — `docs/COMMANDS.md` is 1300+ lines and `docs/AGENTS.md` is 700+; an inventory page with 250 rows across six families is in the same magnitude. The 72 workflows are thinner orchestrators and can carry an even shorter one-liner; the value is exhaustiveness, not prose. This is the *one* change that most increases the corpus's truth value per line edited.
**PR bucket:** PR3 (revised).

### `docs/COMMANDS.md` — command reference
**Current:** Substantively correct after PR2. `/gsd-graphify` added. `/gsd-quick` and `/gsd-thread` subcommand surfaces filled in. Only residual defect: subtitle at line 3 still claims "Complete command syntax, flags, options, and examples."
**Recommend:** Drop "Complete" in the subtitle (one-line edit, parallels the PR1 posture on `docs/README.md`). Otherwise leave. Deferred item: specialty commands `/gsd-ai-integration-phase`, `/gsd-eval-review`, `/gsd-select-framework`, `/gsd-from-gsd2`, `/gsd-extract-learnings`, `/gsd-code-review`, `/gsd-code-review-fix` should each have at least a short section entry (not omitted); grep for whether they already exist rather than assume.
**PR bucket:** PR1 (subtitle edit); PR4 (specialty-command parity if any are missing).

### `docs/FEATURES.md` — feature reference
**Current:** #117 Knowledge Graph added by PR2. TOC includes #116 and #117. But the TOC still orders *v1.36.0 Features* before *v1.32 Features* (L110–142), which is confusing to any reader scanning by version.
**Recommend:** Reorder the TOC chronologically: v1.32 → v1.33 → v1.34 → v1.35 → v1.36. Small edit, meaningful readability win. Keep body order consistent with TOC.
**PR bucket:** PR4.

### `docs/CLI-TOOLS.md` — programmatic API reference
**Current:** Hardcoded module count replaced with a table pointer (good, from PR2). Graphify verb-family section added. Learnings module row added.
**Recommend:** Add rows to the Module Architecture table for `audit.cjs`, `gsd2-import.cjs`, `intel.cjs` (not added by PR2). Add short mentions for `skill-manifest`, `from-gsd2`, `audit-open`, and `state signal-waiting/signal-resume/begin-phase` verbs in the Verb Families section. With INVENTORY.md being the authoritative roster of 24 modules, CLI-TOOLS.md does not have to be exhaustive — but it should stop being conspicuously short on contributor-facing verbs.
**PR bucket:** PR4.

### `docs/ARCHITECTURE.md` — layer topology
**Current:** The least-true file after the stack. L141 says 35 references (real: 41). L221 says 19 domain modules (real: 24). L273-287 Agent Spawn Categories table omits all ten advanced agents that PR3 documented. L207-218 Hook table lists 9 entries (real: 11, missing `gsd-read-injection-scanner.js` and `gsd-check-update-worker.js`). L419-423 Installation File Layout diagram enumerates only 3 hooks — a partial list that silently contradicts both the Hook table above it and the 11 hooks in INVENTORY.md.
**Recommend, line-by-line:**
- L141 refs count 35 → 41 (or delete the count; INVENTORY owns it).
- L221 modules count 19 → 24 (or delete the count).
- L273-287 Agent Spawn Categories: either extend with rows for pattern-mapper / code-reviewer+fixer / debug-session-manager / ai-researcher / domain-researcher / eval-planner+auditor / framework-selector / intel-updater, *or* relabel the table "Primary Agent Spawn Categories" and add a footer line directing readers to INVENTORY.md. Prefer the relabel — the narrative value of the table is the *conceptual spawn-pattern taxonomy*, not exhaustive coverage.
- L207-218 Hook table: add rows for `gsd-read-injection-scanner.js` and `gsd-check-update-worker.js`. Mark the worker as "(helper)".
- L419-425 Installation File Layout: collapse the 3-hook enumeration to `hooks/*.js` + `hooks/*.sh` (or a single line). The diagram is not the place for a partial hook list.
**PR bucket:** Split. The references/modules count updates + Agent Spawn relabel move into **PR3 (revised)** so the INVENTORY/ARCHITECTURE mismatch does not survive the commit that introduces it. The Hook table expansion + Installation Layout cleanup move into **PR4**.

### `docs/USER-GUIDE.md` — lifecycle walkthroughs
**Current:** Correct on `discuss_mode` default in the *table* (L627). Wrong on `discuss_mode` in the abbreviated *schema block* (L581 still says `"standard"`). The entire abbreviated schema (L564–596) is badly stale — missing `tdd_mode`, `plan_bounce`, `plan_bounce_script`, `plan_bounce_passes`, `code_review`, `code_review_depth`, `code_review_command`, `cross_ai_execution`, `cross_ai_command`, `cross_ai_timeout`, `security_enforcement`, `security_asvs_level`, `security_block_on`, `use_worktrees`, `node_repair`, `node_repair_budget`, `text_mode`, `claude_md_path`. It also contains a *ghost key* (`"resolve_model_ids": "anthropic"`, L584) that does not appear in the shipped template at all — it is either obsolete or aspirational, not shipped. The table below it (L598–640) is also an abbreviated duplicate of `docs/CONFIGURATION.md`'s workflow/planning/hook tables.
**Recommend:**
- **PR1 (minimal):** Fix the L581 `"standard"` → `"discuss"` bug. That alone matches the PR1 charter.
- **PR4 (structural):** Delete lines ~540–640 in their entirety (the "Configuration Reference" and preceding "Command Reference" subsections of USER-GUIDE). Replace with a single paragraph: *"Configuration Reference: see [`docs/CONFIGURATION.md`](CONFIGURATION.md) for the full schema, workflow toggles, model profiles, git branching, and security settings. Command Reference: see [`docs/COMMANDS.md`](COMMANDS.md) for every stable command's flags and examples."* This is the biggest single duplication-kill in the corpus. It also retires the `resolve_model_ids` ghost key without having to investigate it, because it was only ever in the abbreviated doc's copy.
**PR bucket:** PR1 (one-line fix) + PR4 (delete-and-link).

### `docs/context-monitor.md`
**Current:** Stable. No defects flagged by any prior lane.
**Recommend:** Leave alone.
**PR bucket:** —.

### `docs/workflow-discuss-mode.md`
**Current:** Correct on the `discuss_mode` semantics. Minor: invocation examples at L29–33 use `gsd-tools config-set` rather than `node gsd-tools.cjs config-set` (the form used consistently in `docs/CLI-TOOLS.md` and CHANGELOG).
**Recommend:** Normalize to `node gsd-tools.cjs config-set` (or, if the SDK query handler exists, `gsd-sdk query config set`). Two-line edit.
**PR bucket:** PR4.

### `docs/manual-update.md`
**Current:** Stable.
**Recommend:** Leave alone.
**PR bucket:** —.

### Localized docs (`docs/ja-JP/`, `docs/ko-KR/`, `docs/pt-BR/`, `docs/zh-CN/`)
**Current:** Untouched; carry the same trust bugs as pre-PR1 English.
**Recommend:** **Defer until the refresh stabilizes on `main`.** A locale port landed concurrently with the English refresh will either (a) rebase against moving targets or (b) freeze a localization at a transitional state. Neither is worth the reviewer load. A single post-refresh "localize-delta" PR backporting all three revised PRs into ja-JP + ko-KR (and pt-BR if its abbreviation drifted) is the right shape. zh-CN needs a structural localization-initiative PR of its own (no `CONFIGURATION.md` in that tree); that is a maintainer-owned scope and not part of this refresh.
**PR bucket:** deferred.

### `CHANGELOG.md`
**Current:** Most trustworthy file in the corpus; every other doc correction cites it.
**Recommend:** Do not touch.
**PR bucket:** —.

---

## Recommended Implementation Shape

**Four PRs, stacked, in the sequence below.** Not five. The earlier proposal fragmented consistency work across PR4 and PR5 for reviewer-diplomacy reasons; that fragmentation buys nothing now that PR2 has already shown maintainers the doc author is willing to take positions. Collapse them.

### Why stacked rather than one big refresh

One mega-PR would fix more in one sweep but would force the reviewer to validate inventory truth, surface catchup, trust bugs, and structural deletes simultaneously. Each PR in the stack below has a **single review axis**:

- PR1 reviews facts (nine defaults are wrong; change them).
- PR2 reviews surfaces (v1.36.0 shipped these; docs now list them).
- PR3 reviews architecture (add an inventory file; update ARCHITECTURE counts to match; upgrade INVENTORY sections to full enumeration).
- PR4 reviews consistency (delete duplicates; add drift guards).

Each PR is independently shippable — if reviewer appetite collapses after PR2, the corpus is still materially better than it was before the refresh.

### PR1 — Trust bugs, revised (small, fast-merge-eligible)

Amend or extend on top of `88e0169`. Additions:

1. `docs/USER-GUIDE.md:581` — `"discuss_mode": "standard"` → `"discuss_mode": "discuss"`.
2. `docs/COMMANDS.md:3` — drop "Complete command syntax" language to match the README posture.

Total PR size ~11 edits, 4–5 files.

### PR2 — Shipped-surface catchup (unchanged)

Keep `164cdb7` as-is. Nothing to revise.

### PR3 — Inventory truth + ARCHITECTURE reconciliation (revised, larger than current `8521364`)

Amend or extend the current PR3 commit. Adds:

1. **Fill out `docs/INVENTORY.md` commands section** — one row per `commands/gsd/*.md` (75 rows), columns: name, one-line role, link. Grouping matches `docs/COMMANDS.md` section order.
2. **Fill out `docs/INVENTORY.md` workflows section** — one row per `get-shit-done/workflows/*.md` (72 rows), columns: name, one-line role.
3. **Fill out `docs/INVENTORY.md` references section** — one row per `get-shit-done/references/*.md` (41 rows), grouped by the existing ARCHITECTURE.md groupings (Core, Workflow, Thinking-Model, Modular Planner).
4. `docs/ARCHITECTURE.md:141` — references count 35 → 41 (or delete the parenthetical count).
5. `docs/ARCHITECTURE.md:221` — modules count 19 → 24 (or delete).
6. `docs/ARCHITECTURE.md:273-287` — relabel table to "Primary Agent Spawn Categories" and add a footer pointing to `docs/INVENTORY.md` for the 31-agent roster.

The rationale for landing the ARCHITECTURE edits in PR3 rather than PR4: PR3 is the commit that introduces the INVENTORY/ARCHITECTURE mismatch (by bringing INVENTORY in with fresh counts). Leaving the mismatch un-resolved across the PR boundary is exactly the defect-introduction pattern this refresh exists to stop.

### PR4 — Consistency + drift guards (combines the prior proposal's PR4 + PR5)

New commits. Edits:

1. `docs/USER-GUIDE.md:540-640` — delete the Command Reference and Configuration Reference subsections. Replace with a one-paragraph link block pointing at `docs/COMMANDS.md` and `docs/CONFIGURATION.md`.
2. `docs/FEATURES.md:100-142` — reorder TOC chronologically.
3. `docs/ARCHITECTURE.md:207-218` — expand Hook table to 11 rows (add read-injection-scanner + check-update-worker).
4. `docs/ARCHITECTURE.md:419-425` — collapse hook enumeration in Installation Layout diagram to `hooks/*.js` + `hooks/*.sh`.
5. `docs/CLI-TOOLS.md` — add `audit`, `gsd2-import`, `intel` rows to Module Architecture; add `skill-manifest`, `from-gsd2`, `audit-open`, `state signal-*` verb mentions.
6. `docs/workflow-discuss-mode.md:29-33` — normalize invocation syntax.
7. New: `tests/inventory-counts.test.cjs` — row-count parity for all six INVENTORY.md family tables.
8. New: `tests/commands-doc-parity.test.cjs` — every shipped command documented somewhere.
9. New: `tests/agents-doc-parity.test.cjs` — every shipped agent in INVENTORY's agent table.
10. New: `tests/cli-modules-doc-parity.test.cjs` — every `bin/lib/*.cjs` in INVENTORY's module table.
11. New: `tests/hooks-doc-parity.test.cjs` — every hook in INVENTORY's hook table.

PR4 is the largest PR in the stack — ~300+ line-changes, 5 new tests, one substantial delete. Its blast radius is high but its ongoing value is the highest of any PR in the refresh: it *structurally prevents* the re-drift that otherwise wipes out PRs 1-3 within two release cycles.

### Deferred (not part of this refresh)

- **Phase-2 AGENTS.md redesign** — delete 31 role cards, rewrite as narrative. Propose after PR4 has shown the INVENTORY-as-authority pattern holds for one release.
- **Localization delta** — backport PRs 1-3 (and where applicable 4) into `docs/ja-JP/` and `docs/ko-KR/`.
- **`VALID_CONFIG_KEYS` maintainer call** — accept or reject `workflow.security_*` and `planning.sub_repos`. Code-side, not docs-side.
- **Model-profile coverage** — decide whether `model-profiles.cjs` grows rows for the 13 uncovered agents, or whether the current runtime-default fallback is canonical. Spec call, not docs.

---

## Anti-Patterns To Avoid

- **Do not add a "What's new in v1.XX" block to any broad doc.** CHANGELOG owns release deltas. PR1 removed this from `docs/README.md`; do not re-introduce it in `docs/USER-GUIDE.md` or `docs/ARCHITECTURE.md` during the refresh.
- **Do not hardcode surface counts without a CI test that locks the number.** If a count is not enforced, delete it; link to the authoritative roster or the directory. Every past drift episode began with an unlocked count.
- **Do not invent "Advanced" vs "Primary" categorizations for new surfaces.** The advanced-agent split in `docs/AGENTS.md` is a transitional compromise, not a principle. No new doc should introduce a fresh curated-subset / authoritative-roster split.
- **Do not duplicate config, command, or agent rosters across files.** If a surface appears in INVENTORY.md and a broad doc needs to show a row, link. The current `USER-GUIDE.md` config duplication is the exact pattern to stop reproducing.
- **Do not fabricate model-profile entries for the 13 agents the code does not cover.** The doc's job is to accurately describe runtime behavior — fallback to the default is the behavior. Filling in fictitious rows would make the doc less true, not more.
- **Do not port English refresh PRs into localized trees concurrently.** Localization has a different reviewer pool and a moving English target. Wait until `main` stabilizes.
- **Do not expand `docs/AGENTS.md` permissions table to all 31 agents** under Phase 1. That table is already complex; doubling its size re-raises accuracy questions the advanced-stub inline-tools approach explicitly finessed. Either keep it scoped to 21 primary (current) or delete it entirely under Phase 2.
- **Do not touch `CHANGELOG.md` during the refresh.** It is the authority every correction depends on; editing it alongside doc corrections undermines that authority chain.
- **Do not squash the stack.** Review legibility is the single most useful signal in a multi-concern doc refresh.
- **Do not ship PR3 without ARCHITECTURE.md's references/modules counts.** The current PR3 commit explicitly punts these to PR5; doing so introduces an INVENTORY/ARCHITECTURE contradiction in the very commit that adds INVENTORY. Fix it in the same PR that introduces it.
- **Do not describe `docs/INVENTORY.md` as "selectively detailed."** Either it is the authoritative shipped-surfaces roster (the current title) or it is not. A file named "Shipped Surface Inventory" that carries full enumeration for half its families and narrative for the other half is a half-kept promise. Promote it to full enumeration or rename the file.

---

## Net Recommendation

**Do not treat the current local stack as complete and do not treat it as wrong.** Preserve PR1 (with two small additions), preserve PR2 verbatim, substantially revise PR3 so `docs/INVENTORY.md` is actually exhaustive across all six families and `docs/ARCHITECTURE.md`'s counts match the commit that introduces INVENTORY, and collapse the prior proposal's PR4-and-PR5 into a single consistency-and-drift-guards PR4 that deletes the `USER-GUIDE.md` config duplication, reconciles the Hook table, reorders the FEATURES TOC, normalizes the workflow-discuss-mode invocation syntax, and lands five mechanical doc-parity tests anchored on `docs/INVENTORY.md`.

The most courageous single move is **upgrading `docs/INVENTORY.md` from "complete for agents" to "complete for everything shipped"** in the revised PR3, and then **locking it with CI tests** in PR4. That one combination converts the refresh from a trust-bug patch into a structural change to how the corpus maintains itself. Everything else — the `USER-GUIDE.md` delete-and-link, the `ARCHITECTURE.md` counts, the TOC reorder, the subtitle language — is incidental follow-through from that single architectural commitment.

The Phase-2 AGENTS.md redesign (delete per-agent cards, reposition the file as *how agents work*, let INVENTORY.md own the roster) is the right long-term shape but does not need to block this refresh. Propose it explicitly as the next architectural move after one release cycle has shown the INVENTORY-as-authority pattern holds.

Localization, `VALID_CONFIG_KEYS`, and model-profile spec coverage remain deferred — each is a different scope, a different reviewer pool, and a different stakeholder set. Handling them in this refresh would conflate three concerns and buy nothing for docs truth that the proposed four PRs do not already deliver.
