# Lane 11: Opus 4.7 PR3 Substantive Agent Inventory Truth Report

## Branch And Commit

- Working branch: `docs/pr3-inventory-model-profile-truth` (not pushed, no PR)
- Parent commit: `164cdb7` (`docs: refresh shipped surface coverage for v1.36`)
- New local commit: **`8521364`** — `docs: complete substantive agent inventory truth for PR3`
- Commit stats: 3 files changed, 359 insertions(+), 1 deletion(-)

## Files Changed

1. `docs/AGENTS.md` — modified (top-level header, category-table intro note, new section, permissions footnote)
2. `docs/CONFIGURATION.md` — modified (fallback note for unlisted-in-profile agents, on top of the six profile rows already added in the paused partial work)
3. `docs/INVENTORY.md` — **created** (new file, 153 lines)

No other files were touched. `docs/ARCHITECTURE.md`, `docs/CLI-TOOLS.md`, `docs/COMMANDS.md`, `docs/README.md`, and the localized docs were deliberately left untouched — each was considered for consistency scope but did not require a change to make PR3 internally coherent.

## Was `docs/INVENTORY.md` Created?

**Yes.** It is a new file on this branch. It carries:

- A header explaining its role as the authoritative shipped-surface inventory and how it relates to the broad docs.
- An **Agents section** that lists **all 31 shipped agents** in a single table: one-line role, spawner, and a `Primary doc` column flagging each agent as `primary` (full card in `docs/AGENTS.md`), `advanced stub` (concise stub in the new `docs/AGENTS.md` section), or `inventory only` (none shipped in this pass — **zero agents fall in this bucket after PR3**, by design).
- **Commands, Workflows, References, CLI Modules, Hooks** sections giving real counts derived from the filesystem (75, 72, 41, 24, 11 respectively) and deferring per-item detail to the broad docs or directory listings where appropriate. The CLI-module table is fully enumerated (all 24 modules). The hooks table is fully enumerated (all 11 hooks, including the v1.36+ `gsd-read-injection-scanner` and the check-update worker that `docs/ARCHITECTURE.md` omits). Commands, workflows, and references use count + narrative-and-link rather than a full re-listing, with explicit text acknowledging that.
- A Maintenance section naming the drift-control posture (which tests already anchor counts on `main`, which ones would need to be extended).

The file is explicit that it is **complete for agents** and **selectively detailed for other surfaces**, rather than pretending exhaustive coverage across families.

## Missing Agents Added Or Summarized

Ten previously-omitted shipped agents are now represented both in `docs/AGENTS.md` (via a new `## Advanced and Specialized Agents` section with per-agent role cards) and in `docs/INVENTORY.md` (via the 31-row agent table). They are:

1. `gsd-pattern-mapper` — planner pipeline; produces `PATTERNS.md`.
2. `gsd-debug-session-manager` — isolated `/gsd-debug` loop driver; introduced for v1.36.0.
3. `gsd-code-reviewer` — `/gsd-code-review`; produces `REVIEW.md`.
4. `gsd-code-fixer` — `/gsd-code-review-fix`; produces `REVIEW-FIX.md` and atomic commits.
5. `gsd-ai-researcher` — `/gsd-ai-integration-phase`; writes AI-SPEC sections 3–4b.
6. `gsd-domain-researcher` — `/gsd-ai-integration-phase`; writes AI-SPEC §1b.
7. `gsd-eval-planner` — `/gsd-ai-integration-phase`; writes AI-SPEC §5–7.
8. `gsd-eval-auditor` — `/gsd-eval-review`; produces `EVAL-REVIEW.md`.
9. `gsd-framework-selector` — `/gsd-ai-integration-phase`, `/gsd-select-framework`; ranked framework recommendation.
10. `gsd-intel-updater` — `/gsd-intel`; writes `.planning/intel/*.json`.

Each advanced-agent stub in `docs/AGENTS.md` includes: role, spawned by, parallelism, tools, model (balanced), color, produces, and a short "key behaviors" list — not as long as the 21 primary cards but substantive enough that a reader does not have to leave the doc to learn what the agent does or how it is invoked. Details were derived from the agent's own frontmatter and role body in `agents/gsd-*.md` and cross-checked against workflow / command references where relevant.

## Count And Categorization Decisions

- **Header framing.** `docs/AGENTS.md` now opens with: "Full role cards for 21 primary agents plus concise stubs for 10 advanced/specialized agents (31 shipped agents total)." This replaces the pre-existing "21 specialized agents" claim. The top-level framing is consistent with both the new in-file content and with `docs/INVENTORY.md`.
- **Category table.** The existing category table (lines 15–29) was not expanded. Instead the intro note above it was tightened to name the table as covering the 21 primary role cards and to direct readers to the new Advanced section and to `docs/INVENTORY.md` for the authoritative roster. This keeps the table usable as a quick visual for the stable core while not lying about coverage.
- **Permissions summary.** The Agent Tool Permissions Summary still contains 21 rows. Rather than expanding it (which would have doubled the table size and re-raised accuracy questions for the specialty agents where tool access is noted inline in their stubs), the table is now prefixed with an explicit "Scope: 21 primary agents only" callout. The advanced-agent stubs each list their tool surfaces inline; `docs/INVENTORY.md` repeats no tool data.
- **Model-profile coverage.** `docs/CONFIGURATION.md`'s profile table now has 18 rows (unchanged from the paused partial work). The fallback note was tightened to: (a) state "18 of 31 shipped agents", (b) enumerate the 13 uncovered agents by name, (c) document that `model_overrides` accepts any shipped agent name regardless of whether it has a profile row, (d) point at `get-shit-done/bin/lib/model-profiles.cjs` and `docs/INVENTORY.md` as the two authoritative sources. No fake profile entries were fabricated for uncovered agents; the spec decision on whether the code-side table should grow is left to maintainers.
- **Inventory filesystem counts.** `docs/INVENTORY.md` claims: 75 commands, 72 workflows, 41 references, 24 CLI modules, 31 agents, 11 hooks — each re-derived from `ls` / `wc -l` on the checkout at `164cdb7`. The values for commands (75), workflows (72), and agents (31) match what `docs/ARCHITECTURE.md:116,127,137` already carries after the `#2257/#2259/#2260` corrections. The reference count `docs/ARCHITECTURE.md` shows (35) is now stale against a live count of 41; `docs/INVENTORY.md` reports 41 and flags the drift without attempting to patch the ARCHITECTURE.md count in this PR. Likewise the CLI-tools 19 vs 24 drift: `docs/INVENTORY.md` reports 24; `docs/ARCHITECTURE.md` was left at 19 pending PR5 cleanup scope.
- **Hooks.** 11 hooks reported (9 in `docs/ARCHITECTURE.md`'s hooks table plus the `gsd-check-update-worker.js` helper and the v1.36+ `gsd-read-injection-scanner.js` from PR #2328/#2201). INVENTORY flags that the row count exceeds the ARCHITECTURE table but does not attempt to re-edit ARCHITECTURE in PR3.

## Local Commit

A single local commit was created:

- SHA: **`8521364c336bd65ec98203f9c2e67dd92b0603dd`**
- Short message: `docs: complete substantive agent inventory truth for PR3`
- Body: enumerates the three files touched and what each one accomplishes, in line with the project's existing `docs:` commit style.
- Branch: `docs/pr3-inventory-model-profile-truth` — **not pushed, no PR opened or reopened.**

## What Still Remains For Later PRs

Deliberately out of scope for PR3, consistent with the Lane 07 proposal sequencing:

- **PR4 drift-prevention:** a future `tests/agents-count-sync.test.cjs` (mirror of `architecture-counts.test.cjs`) that asserts `docs/AGENTS.md`'s primary-agent count + `docs/INVENTORY.md`'s agent-table row count match the filesystem. Similar test for CLI modules and hooks. `docs/INVENTORY.md`'s Maintenance section flags this as the follow-up.
- **PR4/PR5 consistency touch-ups in `docs/ARCHITECTURE.md`:** the references count (35 → 41), the CLI-tools module count (19 → 24 or "see table below"), the Agent Spawn Categories table (21 entries → 31-entry version or a footnoted "primary" label), and the hook-count reconciliation with the installation-diagram snippet. All of these were left untouched here because the Lane 10 spec explicitly bounded PR3 to agent-inventory truth and cautioned against expanding into PR4/PR5 drift-prevention or cleanup scope.
- **PR5 feature-doc parity for advanced agents:** `docs/FEATURES.md` does not yet narrate the AI-integration / eval / code-review pipelines as numbered features. Not a PR3 concern.
- **Code-side spec decision on the 13 uncovered model profiles:** whether `get-shit-done/bin/lib/model-profiles.cjs` should grow rows for `gsd-ai-researcher`, `gsd-code-reviewer`, etc., or whether the runtime-default fallback should remain canonical. PR3 documents the fallback; the spec call is deferred to maintainers (Lane 07 item 38).
- **Localized docs:** `docs/ja-JP`, `docs/ko-KR`, `docs/pt-BR`, `docs/zh-CN` were deliberately not touched, per the task spec.
- **`CHANGELOG.md` / `docs/ARCHITECTURE.md` / `docs/CLI-TOOLS.md`:** not touched, per the task spec and the Lane 07 PR-boundary discipline.

## Coherence Check

After PR3, the following internal consistency holds:

- 21 primary role cards + 10 advanced stubs + 11-hook inventory + 24-module inventory + 31-agent inventory all line up against the filesystem.
- Every pointer introduced by the paused partial work now lands on real content: the category-table note's link to `#advanced-and-specialized-agents` resolves to the new section; the link to `docs/INVENTORY.md` resolves to the new file.
- The Agent Tool Permissions Summary is now explicitly scoped and no longer misleads by silently excluding the advanced agents.
- The model-profile fallback note in `docs/CONFIGURATION.md` is specific enough (13 named uncovered agents) that a reader acting on it will not be surprised by runtime behavior.

PR3 is now reviewable as a substantive inventory-truth PR rather than a claim-weakening patch.
