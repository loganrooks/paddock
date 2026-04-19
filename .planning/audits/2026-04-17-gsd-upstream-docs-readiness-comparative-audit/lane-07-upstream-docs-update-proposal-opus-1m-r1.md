# Lane 07: Upstream Docs Update Proposal

## Question And Decision Posture

This lane converts the gap diagnoses of lanes 01, 01b, 01c, and the bypass-rerun 01c-r3 into a concrete, seed-able upstream docs update proposal. The question is not "is the v1.36.0 docs corpus trustworthy" — prior lanes already answered that with a ranked "partly, under corrections." The question is:

> given the audited defects plus the live state of upstream `main` and the composition of existing docs files, what exactly should be changed, added, split, created, deferred, or explicitly left undocumented in the upstream docs corpus, and in what minimum-PR order?

Posture: opinionated. Where two documentation architectures are plausible, I name one as recommended and one as fallback. Where defects interact (the `claude_md_path` default, the `security_*` placement, the model-profile table), I take an independent normative view on which side is the spec and which side is the bug. Where maintainer intent is genuinely uncertain (whether graphify is deliberately out of user-facing docs), I still choose a default posture — "drift, not intent, pending a maintainer signal" — and call out the alternative.

Scope: the `v1.36.0` pinned docs tree with explicit comparison to `origin/main`. Localized docs (`docs/pt-BR`, `ja-JP`, `zh-CN`, `ko-KR`) are surveyed but not in the first PR. Non-doc runtime refactors (e.g. moving `security_*` keys in the template) are noted as prerequisite decisions for the proposal but are not themselves PR 1 content.

## What This Proposal Is Trying To Achieve

1. Eliminate the three load-bearing trust bugs — `claude_md_path` default, `workflow.tdd_mode` provenance, and `docs/README.md`'s stale "v1.32" / "18 agents" / "Every command / Complete feature" claims — before the next downstream consumer reads the corpus as config or release reference.
2. Close or explicitly name the shipped-surface omissions — `/gsd-graphify` and at least 10 omitted agents — so the inventory pages stop misrepresenting corpus coverage.
3. Resolve the one schema-shape disagreement that a simple doc patch cannot settle alone: the `security_*` keys live under `workflow.*` in `templates/config.json:10-12` but appear at the root in `docs/CONFIGURATION.md:83-85`. The proposal picks a side and flags it as a pre-PR decision owned by maintainers.
4. Import the drift-control mechanism that upstream `main` already accepted (`tests/architecture-counts.test.cjs` in `#2260`, `tests/command-count-sync.test.cjs` in `#2259`) into this proposal so the next release does not re-introduce the same counts gap.
5. Sequence the changes so the smallest PR possible lands the trust-bug fix first, with each follow-on PR limited to one surface family so reviewers can evaluate independently.
6. Leave explicit unresolved items — localization parity, model-profile coverage for the 13 uncovered shipped agents, the `security_*` placement decision — labeled as post-PR-1 work so the first PR is not held hostage by the hardest questions.

Anti-goal: this is not a docs rewrite and is not an invitation to widen the corpus with new narrative. Every recommendation below either corrects an existing surface, adds a missing surface the corpus already implied exists, or removes a claim the corpus no longer deserves to make.

## Prior Audit Convergence And What I Treat As Settled

Five claims agreed across lanes 01, 01b, 01c, and 01c-r3 are treated as settled for this proposal:

1. **Shipped-surface omission of `/gsd-graphify`.** The command file (`commands/gsd/graphify.md`), the CLI routing (`get-shit-done/bin/gsd-tools.cjs:77-91`), the library (`get-shit-done/bin/lib/graphify.cjs`), the config gate (`graphify.enabled`, `graphify.build_timeout` in `get-shit-done/bin/lib/config.cjs:49-50`), the root-README v1.36.0 highlight (`README.md:94`), and the test suite (`tests/graphify.test.cjs`, ~1051 lines) all exist. The feature is missing from `docs/README.md`, `docs/COMMANDS.md`, `docs/FEATURES.md`, `docs/CLI-TOOLS.md`, and `docs/USER-GUIDE.md`. I confirmed on upstream `main` (`git show origin/main:docs/CONFIGURATION.md`, etc.) that these omissions persist.

2. **Shipped-agent omissions in `docs/AGENTS.md`.** At minimum `gsd-pattern-mapper`, `gsd-debug-session-manager`, `gsd-code-reviewer`, `gsd-code-fixer`, `gsd-ai-researcher`, `gsd-domain-researcher`, `gsd-eval-planner`, `gsd-eval-auditor`, `gsd-framework-selector`, `gsd-intel-updater` are on disk (`agents/gsd-*.md`) and not in `docs/AGENTS.md`. The file's "All 21 specialized agents" header (line 3) is false. This persists on `main`.

3. **`claude_md_path` default is wrong in `docs/CONFIGURATION.md`.** The file shows `null` / `(none)` at lines 98 and 114. The template sets `./CLAUDE.md` (`get-shit-done/templates/config.json:55`), `tests/claude-md-path.test.cjs:28-31` asserts it, and `docs/FEATURES.md:2399-2408` (REQ-CMDPATH-01) explicitly states the default is `./CLAUDE.md`. This is an internal-corpus inconsistency plus a code/doc inconsistency. Persists on `main`.

4. **`workflow.tdd_mode` is mis-versioned.** `docs/CONFIGURATION.md:146` says "Added in v1.37" while `CHANGELOG.md:15` places it in `[1.36.0] - 2026-04-14`, `docs/FEATURES.md:2412` places #116 under "v1.36.0 Features", and the shipped config validator includes it in v1.36.0's `VALID_CONFIG_KEYS` (`get-shit-done/bin/lib/config.cjs:20`). Persists on `main`.

5. **Stale subcommand signatures.** `docs/COMMANDS.md` describes `/gsd-quick` with only `--full|--discuss|--research` (lines 627-644) and `/gsd-thread` with only `(none)|name|description` (lines 1268-1284). `commands/gsd/quick.md:2-39,53-60` and `commands/gsd/thread.md:3-4,23-29` expose richer surfaces that `CHANGELOG.md:19` explicitly attributes to v1.36.0. Persists on `main`.

Additionally settled on upstream-`main`-already-fixed status (I re-verified via `git show origin/main:docs/ARCHITECTURE.md` and commit inspection):

6. **ARCHITECTURE.md counts are already corrected on `main`** by `c051e71` (#2257/#2259) and `8b94f03` (#2260). Commit messages: "commands: 69→74", "workflows: 68→71", "agents: 24→31". Those two commits also shipped `tests/architecture-counts.test.cjs` and `tests/command-count-sync.test.cjs`. **This is a proposal-relevant fact**: the drift-control mechanism lane-01b Track E suggested already exists upstream. The proposal imports it rather than invents it.

## Gaps From Prior Runs That I Addressed Here

Prior lanes (mainly the bypass-rerun 01c-r3) left these items open. For each, I took a concrete proposal stance so the rest of this document can be acted on.

**Omitted surfaces: drift or intent?** I default to drift. The pattern of each omitted feature having a shipped command file, a non-trivial test suite, a root-README highlight, and a live CHANGELOG entry is inconsistent with a maintainer decision to keep it out of public docs. In particular `/gsd-graphify` is listed in the upstream root README's `v1.36.0 Highlights` (`README.md:94`) as a user-facing feature, which is evidence *against* the "deliberately undocumented" reading. Fallback: if a maintainer ACKs that graphify is experimental or meant for a separate advanced doc, the correct move is not "remove it from Track 3" but "add a one-paragraph callout linking to an advanced-inventory file" — which the Recommended Documentation Architecture below makes trivial to do.

**Upstream main vs v1.36.0 — what's already fixed?** I inspected `origin/main` directly for the five load-bearing defects. Only the ARCHITECTURE.md component counts (6 above) are fixed on `main`. The `claude_md_path` default, `tdd_mode` provenance, `docs/README.md` "v1.32" horizon, `docs/README.md` "18 agents" claim, `docs/AGENTS.md` "All 21" header, `/gsd-graphify` omissions across `COMMANDS.md/FEATURES.md/CLI-TOOLS.md/USER-GUIDE.md`, and the stale quick/thread subcommand signatures **all persist on `main`**. This means the proposal PR sequence targets live bugs, not historical artifacts.

**Localization in the first PR?** No. Defer. Rationale below:
- pt-BR `CONFIGURATION.md` is explicitly abbreviated ("esta versão resume os parâmetros principais" … "para schema completo, veja inglês") — it already points back to English, so English fixes benefit pt-BR readers without a port.
- zh-CN `docs/zh-CN/` has no `CONFIGURATION.md` at all — a structural gap that requires a localization-initiative PR, not a doc-correction PR.
- ja-JP and ko-KR look like full translations and will need the same corrections, but that is a second-wave PR after the English source stabilizes. Doing them in PR 1 would double reviewer load on a proposal whose minimum goal is trust-bug repair.
- I recommend a post-PR-1 "localize-delta" PR that is explicitly scoped to porting the three trust-bug corrections back into ja-JP and ko-KR, with pt-BR touched only if its abbreviated table drifts.

**`security_*` placement.** This is the one defect that is NOT purely a doc bug. `VALID_CONFIG_KEYS` in `get-shit-done/bin/lib/config.cjs:14-52` does not contain `security_enforcement`, `security_asvs_level`, or `security_block_on` at *any* path. The template puts them under `workflow.*` (lines 10-12). The docs' "Full Schema" block (lines 83-85) puts them at root. The docs' descriptive table (lines 373-377) uses the bare names, which is ambiguous. **Proposal stance:** treat this as a schema bug plus a doc bug. The proposal recommends normalizing them under `workflow.*` to match the shipped template and the operational intent (security is a per-workflow toggle family), then correcting the doc's Full Schema to match. This is bigger than pure doc work — it should be a two-PR arc: PR 1a patches the doc's Full Schema so it matches the shipped template (drops the root-level keys, adds them under `workflow.*`), PR 1b (follow-on, requires maintainer signoff) updates `VALID_CONFIG_KEYS` so the keys actually validate. If maintainers disagree, the fallback is to correct the template to match the doc (move the keys to root), which is a bigger blast radius because existing user configs may already have them nested — so I recommend against the fallback unless maintainers explicitly pick it.

**Model-profile coverage.** `docs/CONFIGURATION.md:443-456` tables 12 agents. `get-shit-done/bin/lib/model-profiles.cjs:9-27` actually defines 18 agents in `MODEL_PROFILES`. The shipped agent roster is 31. So three concentric sets: **12 in the doc ⊂ 18 in the code ⊂ 31 shipped**. This is simultaneously a doc bug (the table is stale against the code) and a spec gap (the code has no explicit profile for 13 shipped agents). Proposal stance: fix the doc first to match code (add the 6 missing agents to the table), and separately flag the 13 uncovered agents as a distinct open question — not a doc bug — with a proposed disposition ("document the fallback-to-runtime-default behavior explicitly; do not add fake profile entries"). The doc patch belongs in PR 3; the code/spec question is explicitly left as a post-proposal follow-up.

**The `docs/CONFIGURATION.md` `null` vs `./CLAUDE.md` ambiguity.** The bypass-rerun 01c-r3 flagged that `get-shit-done/bin/lib/core.cjs:390` returns `null` for unset keys, making the doc's `null` defensible as a runtime-fallback reading. I treat this as a doc-framing bug, not a real ambiguity: the doc is the "shipped defaults reference," not the "runtime-fallback-when-key-absent reference," and readers expect the former. Fix the doc to say `./CLAUDE.md`. Optionally add one sentence distinguishing "shipped template value" from "runtime fallback when key is absent" to prevent future re-litigation. This minor framing improvement is a nice-to-have, not PR 1 material.

## Recommended Documentation Architecture

Recommended: **keep the existing broad docs structure, patch in place, and add one new curated-inventory surface.** Fallback: **keep the existing broad docs structure, patch in place, accept that the inventory pages will always drift, and delete self-completeness language permanently.**

Why the recommended:
- The corpus already has the right shape for broad docs (one page per concern: README/ARCHITECTURE/AGENTS/CONFIGURATION/COMMANDS/CLI-TOOLS/FEATURES/USER-GUIDE). Restructuring would be a multi-month project and would interact badly with localization and existing cross-links.
- The real failure mode is that `docs/AGENTS.md`, `docs/COMMANDS.md`, and `docs/README.md` promise exhaustiveness they cannot maintain. The minimum fix is to stop promising it.
- Upstream `main` already chose this architecture direction by adding `tests/architecture-counts.test.cjs` and `tests/command-count-sync.test.cjs` — it is treating broad docs as authoritative *and* adding mechanical guards against count drift. The proposal should continue that trajectory, not reverse it.
- The 13 uncovered-by-model-profile agents, the graphify subsystem, and specialty agents like `gsd-ai-researcher` / `gsd-eval-*` / `gsd-framework-selector` are legitimately advanced. A single new file — `docs/INVENTORY.md` or `docs/ADVANCED-SURFACES.md` — can hold them with low-prose role cards plus a footer note "not all shipped agents appear in AGENTS.md; this file is the authoritative roster." This preserves the broad docs' readability without hiding the shipped roster.

Why the fallback (and when to choose it):
- If maintainers object to adding a new doc file at all — e.g. because they want the corpus to stay stable at 9 files — the fallback is to patch only existing docs and accept that `docs/AGENTS.md` will either need to grow to cover all 31 agents (which is fine, the file is already 496 lines and adding 10 role cards is ~200 more) or stay explicitly curated (in which case the header must say "curated subset" and link to the filesystem). Either of these is acceptable; both are strictly worse than the new-inventory-file option because they force `docs/AGENTS.md` to either become a long but brittle total-roster document or an admitted partial listing.

The recommended architecture's concrete new doc file is proposed in Section 7 below. If the fallback is chosen, delete that subsection and adjust Track 3 to expand `docs/AGENTS.md` to full roster instead.

## File-By-File Modification Plan

Each subsection names the file, what is wrong with it, the exact corrections, and the PR bucket.

### `docs/README.md` — navigation index

**Why it needs change.** Three load-bearing overclaims and one stale version pointer. Readers land here first; wrong claims here compound trust loss across the corpus.

**Exact claims to correct.**
- Line 12: "Feature Reference — Complete feature and function documentation with requirements." Remove "Complete." Replace with: "Feature Reference — feature narratives and requirements for released features (see CHANGELOG for latest additions)."
- Line 13: "Command Reference — Every command with syntax, flags, options, and examples." Replace "Every command" with "All stable commands."
- Line 16: "Agent Reference ... All 18 specialized agents." Remove "All 18." Replace with: "Agent Reference — role cards for the primary agents (the filesystem is authoritative; see `agents/` and the inventory addendum for the full roster)."
- Line 23: "**What's new in v1.32:**" line — delete this entire bullet. Replace with: "**What's new:** see [CHANGELOG](../CHANGELOG.md) for the current release notes, and upstream [README.md](../README.md) for release highlights." Rationale: keeping "What's new" in sync across 4 minor versions has failed; outsource it to CHANGELOG/root README which ARE in sync.

**Restructures.** None. This is a line-edit patch, ~6 line-changes.

**PR bucket.** **PR 1** (trust-bug hotfix bundle).

### `docs/CONFIGURATION.md` — config reference

**Why it needs change.** Two load-bearing defaults/provenance errors, one schema-shape disagreement with the shipped template, one missing key, an incomplete model-profile table.

**Exact claims to correct.**
- Line 98 (Full Schema JSON block): `"claude_md_path": null` → `"claude_md_path": "./CLAUDE.md"`.
- Line 114 (core settings table): `| (none) |` → `| ./CLAUDE.md |`. Also tighten the description sentence since `(none)` carries connotations the corrected default does not.
- Line 146 (workflow toggles): "Added in v1.37" → "Added in v1.36".
- Lines 83-85 (Full Schema): remove the root-level `"security_enforcement"`, `"security_asvs_level"`, `"security_block_on"` entries. Add them inside the `"workflow": { ... }` block to match `get-shit-done/templates/config.json:10-12`. Update lines 373-377 to refer to them as `workflow.security_enforcement` / `workflow.security_asvs_level` / `workflow.security_block_on`. Caveat: this presumes the code-side decision is "workflow is the canonical location." See Section 3's `security_*` stance and Section 12's residual uncertainties.
- Line 19-22 (`"planning": { ... }` inside Full Schema): add `"sub_repos": []` to match `get-shit-done/templates/config.json:26`. Corresponding description row in the Planning Settings table.
- Lines 440-456 (model profile table): currently 12 agents. Add the 6 agents already defined in `get-shit-done/bin/lib/model-profiles.cjs:22-27` that are missing from the doc: `gsd-pattern-mapper`, `gsd-ui-researcher`, `gsd-ui-checker`, `gsd-ui-auditor`, `gsd-doc-writer`, `gsd-doc-verifier`. Add one explanatory sentence below the table: "Agents not listed here inherit the runtime default; `model_overrides` can set any shipped agent explicitly."

**Restructures.** None structural. All changes are edits to existing rows or a single row-add.

**PR bucket.** 
- `claude_md_path`, `tdd_mode` corrections → **PR 1** (trust bugs).
- `security_*` relocation and `planning.sub_repos` row → **PR 2** (schema truth; needs maintainer signoff on the security_* decision before PR lands).
- Model-profile table expansion → **PR 3** (agent inventory catchup).

### `docs/AGENTS.md` — agent reference

**Why it needs change.** The "All 21 specialized agents" claim is false; 10 shipped agents (lane-01c-r3 evidence) are absent; the category table (lines 13-27) is stale.

**Exact claims to correct.**
- Line 3: "All 21 specialized agents" → either "primary agents" (if we add a separate inventory file and leave AGENTS.md as a curated role-cards doc) or "All 31 specialized agents" (if we expand AGENTS.md to full roster).
- Lines 13-27 (Agent Categories table): either (recommended architecture) update the totals to match the new "primary" vs "advanced" split with a footer referencing the inventory addendum; or (fallback architecture) update the category counts to the real filesystem counts and add the missing rows.
- Agent Details sections (after line 33): under the recommended architecture, AGENTS.md stays at its current 21-agent depth, with a new trailing section "Advanced and Specialized Agents" giving one-paragraph stubs for `gsd-pattern-mapper`, `gsd-debug-session-manager`, `gsd-code-reviewer`, `gsd-code-fixer`, `gsd-ai-researcher`, `gsd-domain-researcher`, `gsd-eval-planner`, `gsd-eval-auditor`, `gsd-framework-selector`, `gsd-intel-updater`, each linking to the new `docs/INVENTORY.md`. Under the fallback architecture, expand each to a full role-card block matching the existing 21-entry format.
- Lines 471-495 (Agent Tool Permissions Summary): either footnote "primary agents only" (recommended) or expand to all 31 (fallback).

**Restructures.** One new "Advanced and Specialized Agents" subsection under recommended architecture. No restructure under fallback.

**PR bucket.** **PR 3** (inventory catchup). Not PR 1 or 2 because changing agent role cards is a larger edit and its correctness needs independent review.

### `docs/COMMANDS.md` — command reference

**Why it needs change.** `/gsd-graphify` is entirely absent; `/gsd-quick` and `/gsd-thread` signatures are stale; the completeness promise is broken.

**Exact claims to correct.**
- Add a new section `/gsd-graphify` somewhere adjacent to Codebase Intelligence commands (currently `/gsd-intel`, `/gsd-map-codebase`, `/gsd-scan`). Source content: `commands/gsd/graphify.md:1-33` for the command header and the four subcommands (`build`, `query`, `status`, `diff`). Include the config gate (`graphify.enabled: true` must be set; graphify is opt-in).
- Lines 627-644 (`/gsd-quick`): expand the flag table to add `--validate`. Add a subcommand table below the flag table with rows for `list`, `status <slug>`, `resume <slug>`. Source: `commands/gsd/quick.md:2-39,53-60`. Update the example block to include at least one subcommand example.
- Lines 1268-1284 (`/gsd-thread`): expand the argument table to add `list --open`, `list --resolved`, `close <slug>`, `status <slug>`. Source: `commands/gsd/thread.md:3-4,23-29`. Update examples accordingly.
- Optionally, add a prefatory sentence in the TOC area noting "the `commands/gsd/*.md` files are the authoritative command surface; this reference documents stable commands."

**Restructures.** One new command subsection. No section renames.

**PR bucket.**
- `/gsd-graphify` addition → **PR 2** (v1.36.0 surface catchup, specifically the graphify missing-surface item).
- `/gsd-quick` and `/gsd-thread` subcommand refresh → **PR 2** (same bucket, all v1.36.0 surface catchup).

### `docs/FEATURES.md` — feature reference

**Why it needs change.** Graphify has no feature entry at all despite being a headline v1.36.0 feature; Feature #116 (TDD Pipeline Mode) appears in the body (line 2412) but not in the TOC (which ends at #115 on line 118); TOC version ordering is non-chronological.

**Exact claims to correct.**
- Add a new numbered feature — likely #117 (Knowledge Graph Integration) — under the "v1.36.0 Features" section (after #116 TDD). Source content: `commands/gsd/graphify.md` and the CHANGELOG entry. Include REQ-GRAPH-0X bullets analogous to adjacent features (REQ-GRAPH-01: config gate required; REQ-GRAPH-02: subcommand surface; REQ-GRAPH-03: test backing; etc.).
- Line 118 (TOC): add a TOC entry for #116 TDD Pipeline Mode so the TOC matches the body. Add the new #117 TOC entry.
- Lines 110 and 131 (TOC ordering): reorder v1.32 to its chronological position or delete the "v1.32 Features" TOC block entirely if the per-version subheadings are meant to be in-flow. Non-chronological ordering is a readability defect that was not load-bearing before but becomes load-bearing once a reader tries to navigate by version.

**Restructures.** One new feature body entry. One TOC reorder.

**PR bucket.**
- Adding #117 graphify feature → **PR 2** (v1.36.0 catchup).
- Adding #116 TDD to the TOC → **PR 2** (same bucket).
- TOC reorder → **PR 2** or defer to **PR 5** (cleanup); I lean toward defer since it is aesthetic and the TOC already links correctly to anchors in the body.

### `docs/CLI-TOOLS.md` — programmatic API reference

**Why it needs change.** Claims "15 domain modules" (line 12) when `get-shit-done/bin/lib/` has 24 `.cjs` files; the graphify verb family is absent; the `learnings`, `audit`, `gsd2-import`, `intel` modules are absent from the module architecture table even though their backing commands are documented elsewhere in the corpus.

**Exact claims to correct.**
- Line 12: "15 domain modules" → update to the correct count. Recommended: delete the fixed number and replace with "See the Module Architecture table below; the `get-shit-done/bin/lib/` directory is authoritative." Prevents recurrence.
- Module Architecture table (near end of file): add rows for `audit`, `graphify`, `gsd2-import`, `intel`, `learnings` modules. Each corresponds to a shipped command family already documented in COMMANDS.md (`/gsd-audit-*`, `/gsd-graphify`, `/gsd-from-gsd2`, `/gsd-intel`, `/gsd-extract-learnings`).
- Verb families section: add a graphify subsection covering `graphify build`, `graphify query`, `graphify status`, `graphify diff`, `graphify snapshot`. Source: `get-shit-done/bin/gsd-tools.cjs:77-91`.
- Also add rows or brief mentions for `skill-manifest`, `from-gsd2`, `audit-open`, and the `state signal-waiting / signal-resume / begin-phase` verbs. These are in `gsd-tools.cjs` (lines 1-165) but absent from CLI-TOOLS.md. These are programmatic contributor-facing surfaces; omitting them leaves the "programmatic API reference" title materially wrong.

**Restructures.** One new verb-family section (graphify). Otherwise table-row additions.

**PR bucket.** **PR 2** (v1.36.0 catchup) for graphify and learnings. The other missing verb families can land in **PR 3** to keep PR 2 focused on the headline v1.36.0 items.

### `docs/ARCHITECTURE.md` — layer topology

**Why it needs change.** Already partially fixed on `origin/main` (counts); remaining defects are the agent spawn categories table (lines 273-287 — lists 21, should list 31 or be tagged "primary"), the 19-modules claim at line 221 (should be 24 or "generated"), and the installation file layout diagram / Hook System table internal inconsistency (lane-01c noted 3 hooks in one place vs 9 in another).

**Exact claims to correct.**
- Line 116-141 (component counts block): if not already backported from `main`, bring in the `#2257/#2259/#2260` commits. Those commits changed 69→74, 68→71, 24→31. Since the counts on `main` are authoritative, pull them over to the backport if the proposal targets a v1.36.1 hotfix; otherwise just track the `main` fix as a reference precedent.
- Line 221: "19 domain modules" → 24, or remove the fixed number. Prefer remove; the new `tests/command-count-sync.test.cjs` pattern can be extended to module counts cheaply.
- Agent Spawn Categories table (lines 273-287): under the recommended architecture, relabel as "Primary Agent Spawn Categories" and add a footer "the filesystem roster at `agents/gsd-*.md` is authoritative; see `docs/INVENTORY.md` for the full roster." Under the fallback architecture, expand to include the 10 omitted families.
- Hook System internal inconsistency (lane-01c lines 114-115 finding): reconcile the Hook System table (lines 207-218, 9 hooks) with the Installation File Layout diagram (lines 411-425, 3 hooks). The recommended fix is to refer both to a single source of truth — the Hook System table — and remove the 3-hook list from the installation diagram or explicitly annotate it as "primary hooks only."

**Restructures.** None structural; cells get updated or notes added.

**PR bucket.**
- Counts sync (if not yet on the pinned tree) → **PR 1 or backport-only** if the proposal is for v1.36.1; **already-landed on main** for anyone targeting main.
- Agent Spawn Categories relabel → **PR 3** (inventory catchup, same bucket as AGENTS.md changes).
- Hook System internal inconsistency → **PR 5** (cleanup).
- Module count fix / generification → **PR 3**.

### `docs/USER-GUIDE.md` — lifecycle walkthroughs

**Why it needs change.** Thread subcommand section (lines 289-303 area) describes the older thread signature; config schema at lines 564-596 is an abbreviated and now-stale snapshot; `discuss_mode` default is shown as `"standard"` (line 627) but the real default is `"discuss"`.

**Exact claims to correct.**
- Lines 289-303 (threads): refresh to match the shipped command surface (`list --open`, `list --resolved`, `close <slug>`, `status <slug>`). Or shorten this section to a one-paragraph summary with a link to `docs/COMMANDS.md#/gsd-thread` as the authoritative reference. Preferred: shorten; a lifecycle doc does not need the full command signature reproduced, and that duplication is what created the drift.
- Line 627: `discuss_mode` default `"standard"` → `"discuss"`.
- Lines 564-596 (config schema): either delete the abbreviated schema and replace with a link to `docs/CONFIGURATION.md#full-schema`, or update the abbreviated schema to match the corrected `docs/CONFIGURATION.md` Full Schema. Preferred: delete-and-link; maintaining two copies has produced demonstrable drift.

**Restructures.** Two shorten-and-link replacements. This is a small restructure but a high-value one — it eliminates a drift class.

**PR bucket.**
- `discuss_mode` default and thread signature refresh → **PR 1** (trust-bug bundle) — same bundle as the CONFIGURATION.md defaults because they are cognitively related to "what does the shipped system actually do?"
- Config schema delete-and-link → **PR 4** (drift-prevention refactor) — structural change, belongs in a separate reviewable PR.

### `docs/context-monitor.md`, `docs/workflow-discuss-mode.md`, `docs/manual-update.md` — focused topic docs

**Why it needs change.** Largely does not. These three files are the closest the corpus has to durable, drift-resistant documentation. The only defect is `docs/workflow-discuss-mode.md`'s invocation examples using `gsd-tools config-set` rather than `node gsd-tools.cjs config-set` (lane-01c finding), which is context-dependent.

**Exact claims to correct.**
- `docs/workflow-discuss-mode.md`: reconcile the `gsd-tools config-set` examples with the invocation syntax used elsewhere in the corpus. Not load-bearing; cleanup-only.

**PR bucket.** **PR 5** (cleanup).

### `CHANGELOG.md` — release notes

**Why it needs change.** Probably does not, for the purposes of this proposal. CHANGELOG.md is already the most trustworthy release-delta source (corroboration-grade for every other doc correction above). Touching CHANGELOG in these PRs invites unrelated review.

**Exact claims to correct.** None.

**PR bucket.** Not touched.

## Recommended New Doc Files

Under the recommended architecture, **one** new file:

### `docs/INVENTORY.md` — Authoritative Shipped Surfaces

**Purpose.** A contributor-facing inventory of everything in the filesystem that ships in v1.36.0 (and later), grouped by family: commands, agents, workflows, references, bin/lib modules, hooks. Each item gets a one-line role description and a link to its source file. Counts are either removed or auto-generated.

**Why existing files are the wrong home.**
- `docs/AGENTS.md` is role-card format; expanding it to all 31 agents turns it into a 900+ line wall that undermines its current "read this to learn the architecture" function.
- `docs/COMMANDS.md` is usage format; exhaustive surface listing competes with example-driven usage.
- `docs/ARCHITECTURE.md` is conceptual; an inventory addendum would dilute the layer-model story.
- None of the existing files currently cross-families (commands + agents + workflows + modules + hooks). An inventory naturally does.

**Proposed sections.**
1. Commands — one row per `commands/gsd/*.md` with a one-line purpose and the doc entry (if any) that covers it.
2. Agents — one row per `agents/gsd-*.md` with role, spawn context, and whether `docs/AGENTS.md` has a full role card.
3. Workflows — one row per `get-shit-done/workflows/*.md`.
4. References — one row per `get-shit-done/references/*.md`.
5. Bin/lib modules — one row per `get-shit-done/bin/lib/*.cjs`.
6. Hooks — one row per installed hook.

**PR bucket.** **PR 3** (inventory catchup). This file's first version can be mostly auto-generated (see Track 4).

**Fallback.** If maintainers reject a new doc file, expand `docs/AGENTS.md` to cover all 31 agents and add tables to `docs/CLI-TOOLS.md` for all modules; keep the corpus at 9 files but accept the individual file sizes grow.

## Concrete Edit Inventory

A punch-list, suitable for task breakdown. Each item is phrased so it can become a single commit.

**PR 1 — Trust-bug hotfix bundle (single PR; ~10 line-changes total):**

1. `docs/README.md:12` — weaken "Complete feature and function documentation" language.
2. `docs/README.md:13` — weaken "Every command with syntax, flags, options, and examples" language.
3. `docs/README.md:16` — remove "All 18 specialized agents."
4. `docs/README.md:23` — replace "What's new in v1.32" bullet with a CHANGELOG pointer.
5. `docs/CONFIGURATION.md:98` — change `"claude_md_path": null` to `"claude_md_path": "./CLAUDE.md"` in Full Schema.
6. `docs/CONFIGURATION.md:114` — change default from `(none)` to `./CLAUDE.md` in core settings table.
7. `docs/CONFIGURATION.md:146` — change `tdd_mode` provenance from "Added in v1.37" to "Added in v1.36".
8. `docs/USER-GUIDE.md:627` — change `discuss_mode` default from `"standard"` to `"discuss"`.
9. `docs/AGENTS.md:3` — remove or update "All 21 specialized agents" header (minimal change: drop "All" → "21 specialized agents"; full change in PR 3).

**PR 2 — Shipped-surface catchup (v1.36.0 inventory):**

10. `docs/COMMANDS.md` — add `/gsd-graphify` section with `build|query|status|diff` subcommands, config gate, and one usage example.
11. `docs/COMMANDS.md:627-644` — expand `/gsd-quick` flag table: add `--validate`; add subcommand rows for `list`, `status <slug>`, `resume <slug>`; update example block.
12. `docs/COMMANDS.md:1268-1284` — expand `/gsd-thread` argument table: add `list --open`, `list --resolved`, `close <slug>`, `status <slug>`; update examples.
13. `docs/FEATURES.md` — add feature #117 "Knowledge Graph Integration" body entry under v1.36.0 Features, with REQ-GRAPH-0X bullets.
14. `docs/FEATURES.md:118` — add TOC entries for #116 TDD Pipeline Mode and #117 Knowledge Graph Integration.
15. `docs/CLI-TOOLS.md` — add graphify verb family section covering `build|query|status|diff|snapshot`.
16. `docs/CLI-TOOLS.md` — add `learnings` row to module architecture table.
17. `docs/CLI-TOOLS.md:12` — delete the hardcoded "15 domain modules" count; replace with "see table below."
18. `docs/CONFIGURATION.md:83-85` — move `security_*` keys from root to `workflow.*` in Full Schema; update description rows 373-377 to use `workflow.` prefix. (This bundles with the schema-shape decision; if maintainers do not sign off on `workflow.*` as canonical, this item slips to later PR and the template is corrected instead.)
19. `docs/CONFIGURATION.md:19-22` — add `"sub_repos": []` to `planning` in Full Schema; add description row.

**PR 3 — Inventory catchup and model-profile truth:**

20. `docs/AGENTS.md` — add "Advanced and Specialized Agents" trailing section with one-paragraph stubs for each of the 10 omitted agents (recommended architecture) OR full role cards (fallback).
21. `docs/AGENTS.md:13-27` — update Agent Categories table to current filesystem count with category footers.
22. `docs/AGENTS.md:471-495` — extend Agent Tool Permissions Summary with the newly-listed agents or footnote that table as "primary agents only."
23. `docs/CONFIGURATION.md:440-456` — add `gsd-pattern-mapper`, `gsd-ui-researcher`, `gsd-ui-checker`, `gsd-ui-auditor`, `gsd-doc-writer`, `gsd-doc-verifier` rows to the model-profile table.
24. `docs/CONFIGURATION.md:440-456` — add explanatory sentence: agents not in the table inherit the runtime default; `model_overrides` can set any shipped agent explicitly.
25. `docs/ARCHITECTURE.md:273-287` — relabel Agent Spawn Categories table and add filesystem footnote (recommended) or expand to 31 entries (fallback).
26. `docs/ARCHITECTURE.md:221` — remove "19 domain modules" fixed count.
27. `docs/CLI-TOOLS.md` — add `audit`, `gsd2-import`, `intel` rows to module architecture table.
28. `docs/CLI-TOOLS.md` — add short mentions of `skill-manifest`, `from-gsd2`, `audit-open`, `state signal-*` verbs.
29. (New file) `docs/INVENTORY.md` — create the authoritative shipped-surfaces inventory with the six sections from Section 7 above. First version can be generated by a script and committed as seed content.

**PR 4 — Drift-prevention structural moves:**

30. `docs/USER-GUIDE.md:564-596` — delete the abbreviated config schema; replace with link to `docs/CONFIGURATION.md#full-schema`.
31. `docs/USER-GUIDE.md:289-303` — shorten threads lifecycle description to a paragraph with a link to `docs/COMMANDS.md#/gsd-thread`.
32. Port upstream `main`'s `tests/architecture-counts.test.cjs` and `tests/command-count-sync.test.cjs` into the proposal's target branch if the target is not `main` itself. Extend the pattern to `tests/agents-count-sync.test.cjs` (enforces `docs/AGENTS.md` primary-agent count matches a declared expected list + a filesystem comparison sanity check), and `tests/cli-tools-module-sync.test.cjs` (enforces `docs/CLI-TOOLS.md` module table rows == `get-shit-done/bin/lib/*.cjs` count, or at least the named subset).
33. Add a `tests/commands-doc-parity.test.cjs` that asserts every `commands/gsd/*.md` file has either a `### /gsd-*` entry in `docs/COMMANDS.md` or an entry in `docs/INVENTORY.md`. Failure message points at the specific missing file. This is the drift-control Track 4 artifact; the test file goes in `tests/` so CI runs it.

**PR 5 — Cleanup:**

34. `docs/FEATURES.md:100-135` — reorder TOC to chronological, moving v1.32 block to its correct position before v1.34.
35. `docs/ARCHITECTURE.md:207-218` vs `docs/ARCHITECTURE.md:411-425` — reconcile hook listings; delete the 3-hook list from the installation diagram or annotate as "primary hooks only."
36. `docs/workflow-discuss-mode.md` — normalize `gsd-tools config-set` example syntax.

**Post-proposal follow-ups (explicit; not in PR sequence):**

37. Maintainer decision on `security_*` placement in `VALID_CONFIG_KEYS`. Either update the template and doc to root, or update `VALID_CONFIG_KEYS` to accept `workflow.security_*`. I recommend the latter.
38. Model-profile coverage: decide whether the 13 uncovered shipped agents should get explicit entries in `get-shit-done/bin/lib/model-profiles.cjs`, or whether the doc should explicitly document runtime-default fallback semantics. I recommend documenting the fallback; do not fabricate profile entries.
39. Localization delta: backport PRs 1 through 3 into `docs/ja-JP/`, `docs/ko-KR/`. For `docs/pt-BR/`, verify the abbreviated content still accurately points to updated English. For `docs/zh-CN/`, a separate maintainer-owned localization-initiative PR is required since `CONFIGURATION.md` is absent from that tree.

## Proposed PR Sequence

**PR 1 — Trust-bug hotfixes (small, fast-merge-eligible).** Items 1–9. One PR. Goal: eliminate factual errors that change reader operational behavior. Smallest possible delta. If this PR sits in review for more than a week, downstream consumers continue acting on wrong defaults. Everything here has primary-source corroboration already cited; review load is low.

**PR 2 — Shipped-surface catchup for v1.36.0 (graphify, quick, thread).** Items 10–19. One PR. Goal: make the docs' v1.36.0 coverage match shipped reality. This PR is bigger than PR 1 but has clear boundaries (every change ties to a single v1.36.0 changelog entry). The `security_*` item (18) can slip to a later PR if maintainer signoff is delayed.

**PR 3 — Inventory and model-profile truth.** Items 20–29. One PR. Goal: agent inventory matches filesystem; model-profile table matches code. Adds `docs/INVENTORY.md` under the recommended architecture (or expands `docs/AGENTS.md` under the fallback). This PR requires more careful review because the `AGENTS.md` changes are stylistic as well as factual; it is the largest of the four.

**PR 4 — Drift-prevention refactor.** Items 30–33. One PR. Goal: structural moves that make recurrence harder. The delete-and-link moves in USER-GUIDE.md and the doc-parity tests together prevent the same class of defects from recurring at the next release.

**PR 5 — Cleanup.** Items 34–36. One PR. Goal: navigation and internal consistency polish. Deferrable indefinitely without functional impact.

**Ordering rationale.**
- PR 1 first because trust bugs compound: every day it's not merged, a new reader forms wrong operational beliefs about `claude_md_path`.
- PR 2 before PR 3 because PR 2 is v1.36.0-specific and time-sensitive (closes the gap before the v1.37 cycle adds new pressure), while PR 3 is timeless (it catches up historical drift that accumulated across v1.32–v1.36).
- PR 3 before PR 4 because PR 4's drift tests will fail against the current `docs/AGENTS.md` (21) vs filesystem (31) mismatch. PR 3 fixes the content; PR 4 installs the guard.
- PR 4 before PR 5 because cleanup without drift tests leaves the corpus in a "fixed again but will re-drift" state.
- PR 5 last and optional.

**Parallel work.** PRs 2 and 3 can be developed in parallel by different contributors since they touch different files (with one overlap: `docs/AGENTS.md` is touched only by PR 3; `docs/CONFIGURATION.md` is touched by PRs 1, 2, and 3 in distinct sections). Expect minor merge conflicts; resolvable.

**First PR critical path.** The minimum credible upstream PR is just items 5, 6, 7, 8 (3 files, 4 lines changed). Item 4 (docs/README.md line 23) is almost free and dramatically improves trust posture. Everything else can wait. If the maintainer signal on a broader PR is uncertain, submit the 5–8 minimum first and hold the rest.

## What Should Not Be Done

- **Do not rewrite `docs/AGENTS.md` as a complete roster document in the same PR as a trust-bug patch.** Mixing factual corrections with stylistic agent-card writing will slow review on the urgent content. Keep PR 1 lean.
- **Do not add a new top-level doc file in PR 1.** If `docs/INVENTORY.md` is proposed, it should land in PR 3 after the broad file revisions so reviewers see why it's needed.
- **Do not delete any existing doc file, even if it overlaps with others.** Cross-references across the corpus depend on stable filenames. Shorten files and point to canonical sources; do not delete.
- **Do not attempt to fix the model-profile coverage gap by fabricating profile entries for the 13 uncovered shipped agents.** That would be a spec change disguised as a doc fix. Document the fallback-to-default behavior and let maintainers decide whether code-side expansion is wanted.
- **Do not port PRs 1 or 2 to `docs/ja-JP`, `docs/ko-KR`, `docs/pt-BR`, `docs/zh-CN` in the same PR as the English changes.** Localization parity is a separate concern and a separate reviewer pool. A mixed-language PR is high-risk for review.
- **Do not touch `CHANGELOG.md` in any of these PRs.** It is the last authoritative source the docs depend on; a CHANGELOG edit alongside doc edits undermines that authority chain.
- **Do not promise completeness anywhere in the replacement language.** Every place "Every command," "All agents," "Complete feature" comes out should be replaced with language that names the authoritative surface (the filesystem, the CHANGELOG) rather than claiming the doc itself is authoritative.
- **Do not unify `docs/README.md` quick-links with `README.md` v1.36.0 highlights by copying.** Link to the root README instead; copying recreates the same drift problem at a smaller scale.
- **Do not defer the `workflow.tdd_mode` provenance fix on the grounds that it is "just a label."** Readers use provenance to plan upgrades; a wrong version label will cause real upgrade-planning errors in projects that gate v1.37 adoption on the feature list.

## Residual Uncertainties And How The Proposal Handles Them

- **`security_*` key location (workflow vs root).** Unresolved at the spec level. The proposal handles it by making the maintainer decision a PR 2 prerequisite and splitting the proposal's stance: the default recommended move is to normalize under `workflow.*` (matches template, matches operational intent), with a clear fallback (normalize at root, update template). If the maintainer signal is silent after a reasonable window, PR 2 can ship without item 18 and the security_* placement defect persists for one more release cycle without blocking the rest of the PR.
- **Model-profile coverage (13 uncovered shipped agents).** Unresolved at the spec level. The proposal adds six missing doc rows where the code is authoritative and explicitly flags the 13-agent gap as a post-proposal spec question. It does not try to paper over the gap with doc prose.
- **Maintainer intent on graphify and specialty agents.** Unresolved but defaulted. The proposal treats omissions as drift and adds the features/agents. If a maintainer signals "intentional exclusion" during review, the recommended architecture makes the retraction cheap: move the graphify content to `docs/INVENTORY.md`, add a one-sentence "experimental" note in `docs/FEATURES.md`, and leave `docs/COMMANDS.md` without the section. That retraction is a smaller change than the inclusion.
- **Localized docs parity.** Deferred by design. The proposal explicitly names the post-proposal localize-delta PR as item 39 and does not attempt it in PR 1–5.
- **Upstream `main` trajectory.** The proposal verified the five load-bearing trust bugs persist on `main` and imported the count-drift-guard test pattern that `main` already accepted. If `main` changes before these PRs merge, rebase will be mechanical for most items; the `security_*` and `claude_md_path` items in particular should stay stable.
- **Corroboration depth.** I did not re-read bodies of `tests/agent-skills.test.cjs`, `tests/plan-bounce.test.cjs`, `tests/codex-config.test.cjs`, `tests/agent-required-reading-consistency.test.cjs`; I relied on file existence plus the narrower tests I did read. If any of these turn out to not test what the prior lanes attributed to them, the `docs/CONFIGURATION.md` "Trustworthy for `agent_skills` injection" framing weakens — but none of the PR 1–5 items rest on that framing for their primary corroboration.

## PR-Readiness Judgment

Yes, this proposal is ready to drive an upstream PR now, with the following checks:

1. **Maintainer signal on the `security_*` placement question.** A public ACK is required before item 18 lands. In its absence, PR 2 ships without item 18 and the defect is documented as an explicit follow-up.
2. **Maintainer signal on whether `docs/INVENTORY.md` is welcome.** If yes, PR 3 includes item 29. If no, PR 3 expands `docs/AGENTS.md` instead. Either way the PR structure holds.
3. **Maintainer signal on backport policy.** PR 1 targets `main` (where the bugs persist) or a hypothetical v1.36.1 hotfix branch. If there is a hotfix branch preference, PR 1 should be submitted against it to match release convention.
4. **Reviewer availability.** PR 1 is small enough that a single contributor-reviewer round-trip should suffice. PRs 2–4 are bigger and will want at least two reviewers each.

The proposal is not ready to drive PR submission without those signals: specifically the `security_*` placement question has real runtime consequences and should not be decided unilaterally by the doc PR author. Every other item is self-contained and can proceed under standard review.

Proposal-quality checks that already hold:
- Every recommended change cites a specific primary source (file + line range).
- Every stale claim I recommend correcting has been verified against both the v1.36.0 pin and upstream `origin/main` to distinguish persistent bugs from already-fixed drift.
- Every new doc file proposal names an exact path and explains why existing files are the wrong home.
- Every defer decision names the follow-up PR or post-proposal item so deferred work is not lost.
- The PR sequence is ordered so the smallest credible PR ships first and each subsequent PR has independent review value.

## Net Recommendation

Adopt the Recommended Documentation Architecture (patch broad docs in place, add `docs/INVENTORY.md` for the authoritative shipped roster). Execute the five-PR sequence with PR 1 as the fast-merge trust-bug bundle (items 1–9), PR 2 as the v1.36.0 surface catchup (items 10–19 with item 18 contingent on maintainer signal), PR 3 as the inventory and model-profile truth pass (items 20–29), PR 4 as the drift-prevention refactor importing the `architecture-counts`/`command-count-sync` test pattern already on `main` (items 30–33), and PR 5 as optional cleanup (items 34–36). Keep localization, the `security_*` runtime decision, and the model-profile coverage spec question as explicit post-proposal follow-ups (items 37–39). Do not expand scope; do not delete existing files; do not touch CHANGELOG.md; do not mix languages in a single PR. The minimum credible first upstream submission is items 5–8 (the four config/guide default corrections) plus item 4 (the README quick-links delinkage), five lines of changes across three files, and that alone measurably repairs the trust posture of the entire docs corpus.
