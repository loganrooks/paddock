# .planning/AGENTS.md

## Scope

This file applies to work inside `.planning/`.

Read it together with root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md), not instead of it.

Its job is to keep planning, audit, research, canon, and phase-steering work rigorous without bloating the root file.

## Live Planning Sources Of Truth

Treat these as the primary planning canon:

- [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
- [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
- [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
- [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)
- [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- active phase docs under `.planning/phases/`

Additional rules:

- Prefer the latest non-superseded artifact.
- Prefer canon docs over exploratory notes when they conflict.
- Treat `discovery/` as upstream context, not live operational state.
- If canon conflicts, report the conflict explicitly instead of silently choosing one side.

## Artifact Discipline

The detailed artifact taxonomy and retention rules live in [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md).

Inside `.planning/`:

- keep `canon`, `phase work`, `audit trail`, `exploration`, and `generated corpus` distinct
- do not silently promote one class into another
- do not turn exploratory conclusions into canon without an explicit proposal or patch step
- if a newer artifact supersedes an older steering artifact, mark that relationship explicitly
- if an artifact is stale but still historically relevant, prefer status notes and replacement pointers over deletion
- do not let large generated corpora dominate the active planning surface without an explicit retention decision

### Reference-Graph Hygiene

For structural `.planning/` changes that can affect markdown links, prefer the repo-local reference tool over ad hoc manual rewrites:

- `python3 tooling/codex/audit_refmap.py map <root>`
  - use before a move or cleanup pass to see inbound/outbound pressure and missing local links
- `python3 tooling/codex/audit_refmap.py snapshot <root>`
  - use when a lane, checkpoint, or cleanup pass needs a machine-readable view of the current markdown reference graph
  - prefer this over hand-maintained link inventories
- `python3 tooling/codex/audit_refmap.py move <root> --moves <manifest.tsv>`
  - use for bounded artifact-family moves or renames
  - this is the preferred path when you are reorganizing an audit workspace, corpus subtree, or other markdown-heavy planning surface
- `python3 tooling/codex/audit_refmap.py retire <root> --target <path> [--replacement <path>]`
  - use when a markdown artifact should stop being active without silently breaking refs
  - this writes a tombstone in place and can redirect local markdown references to a replacement
- `python3 tooling/codex/audit_refmap.py verify <root>`
  - use after reference-heavy edits, restructures, or deletion/supersession work
  - prefer running this before checkpoint commits when `.planning/` topology changed materially
- `python3 tooling/codex/verify_touched_audit_refs.py`
  - use as the lightweight default check before a checkpoint when only some audit roots changed
  - `--staged` limits the check to staged audit roots
  - `--all` is a broader hygiene sweep and can legitimately fail on pre-existing debt outside the current work
- `python3 tooling/codex/runtime_visibility.py`
  - use for harness-intervention or portable-GSD runtime work when the real question is how final `.codex/` runtime surfaces differ from tracked overlay canon after materialization
  - prefer it over vague `overlay/live drift` language when you need a bounded, classified view of high-leverage runtime families
- `python3 tooling/codex/capture_runtime_visibility_snapshot.py --label ... --output ...`
  - use for selected audit/intervention lane boundaries when ephemeral terminal output is too weak and the lane needs a frozen runtime-truth record with commit metadata
  - prefer this over hand-written runtime summaries when classified final-runtime carry is part of the later inheritance surface
- `python3 tooling/codex/manifest_install_coherence.py . --snapshot <snapshot.json> --output <report.json> --strict`
  - use for manifest/install coherence work after a selected-lane runtime snapshot exists
  - prefer this over prose-only coherence judgments when the lane needs auditable comparison across updater-boundary truth, tracked carried-subset truth, and frozen final-runtime truth
  - `--strict` is the default quality gate when you want the report to refuse dirty current state or unresolved runtime ambiguity

Move manifest format:

- one TSV row per move
- `OLD_PATH<TAB>NEW_PATH`
- both paths repo-relative

Operational rules:

- do not do large `.planning/` move/rename passes by hand when the refmap tool can carry them more safely
- treat the reference graph as derived state; do not hand-maintain a separate truth file unless a specific workflow has earned that burden
- prefer bounded subtree reorganization plus verification over wholesale reshuffles
- if a move is large enough that readers could lose continuity, add a local README or topology note in the destination subtree

Deletion / retirement rules:

- do not silently delete referenced planning artifacts
- use `retire` for markdown artifacts that need a tombstone and optional replacement routing
- for non-markdown artifacts, or when `retire` is not the right fit:
  - decide whether the artifact should be replaced, tombstoned, or merely marked superseded
  - patch or redirect references deliberately
  - then run `verify`
- when an older artifact remains historically relevant, prefer replacement pointers, supersession notes, or tombstones over hard removal

## Launch-Truth Discipline

For spawned planning, audit, review, or doctrine-sensitive work inside `.planning/`:

- do not rely on private sqlite inspection plus chat memory as the only launch-truth surface
- prefer durable requested-vs-effective capture with `python3 tooling/codex/capture_launch_truth.py`
- use a strong pre-spawn `--since` boundary when available
- preserve the capture in the relevant launch-truth, review, audit, or disposition artifact before inheriting the return
- treat missing runtime fields as unresolved rather than silently inferred matches

## Research And Audit Quality

For non-trivial research, audit, gap-closure, sensitivity, or synthesis work:

- make the path of inquiry visible
- separate evidence from inference and unknowns
- surface assumptions rather than smuggling them in
- define loaded terms and anti-misread rules when they matter
- do not silently broaden scope
- do not let threshold framing (`adequate`, `sufficient`, `good enough`, `well enough`, `pass/fail`, `ready/not ready`) become the governing question when the real task is to increase leverage, carry, visibility, or intervention power
- keep the stronger distinction visible:
  - whether a document, map, lane, or doctrine surface can carry work
  - how strongly, clearly, and future-resiliently it carries that work compared with stronger available forms
- when naming gains, prefer `load-bearing gain`, `higher-yield distinction`, `stronger carry surface`, `better intervention visibility`, or `transformation pressure` over threshold praise like `works well`
- use gate language only for actual gates; do not let gate language flatten optimization, redesign, or long-horizon planning questions into a mere threshold check
- do not accept a weaker frame, shortcut, or premature closure just because it was requested; push back when the request would degrade the quality of canon, planning, verification, or process doctrine
- that pushback should be explicit and well-argued:
  - identify the specific loss or risk
  - explain the stronger alternative
  - ground the case in artifacts, consequences, or reasoning that can withstand scrutiny
- partial pushback is often preferable to flat rejection:
  - keep the goal if it is sound
  - reject or revise the method, sequencing, scope, or closure pressure if that is the real problem

Prefer the repo-local `gsd-rigorous-research` skill for standalone research lanes.

When source grounding matters, distinguish clearly between:

- direct external grounding
- traceable external grounding through repo-local synthesis
- internal canon or audit support only

Do not treat repo-local restatement as if it were fresh external grounding.

For load-bearing planning/process artifacts, expose claim type and source-basis explicitly when a reader could otherwise mistake internal support for external support.

- Prefer `[t:s:b]`; use `[t:b]` only when the support mode is obvious.
- Minimal reminder:
  - claim type: `e` evidenced, `d` decided, `a` assumed, `o` open, `p` projected, `s` stipulated, `g` governing
  - support mode: `c` cited, `r` reasoned, `b` bare
  - source-basis: `i` internal, `d` external-direct, `t` external-traceable
- Join material support or basis codes with `+`.
- Internal cited grounding must cite the direct repo file and line numbers near the claim.
- External grounding should use markdown footnotes and an `External Works Cited` section.
- Detailed semantics live in:
  - [.planning/CLAIM-TYPES.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAIM-TYPES.md)
  - `.codex/skills/gsd-rigorous-research/references/method.md`

## Future-Flexibility Statusing

When a planning or audit pass is preserving future flexibility, require outputs to distinguish at least:

- `direct doctrine`
- `bounded-open branches`
- `preserve-only seams`
- `reversal-sensitive boundaries`
- `inquiry debt`

Do not flatten those categories into generic `open` or `deferred` language.

If terms like `challenge`, `showcase`, `hosted`, `premium`, `event`, `reviewed`, or `unsupported` are doing too much work, spell out the distinction instead of relying on local context.

## Canon And Roadmap Response Rules

- Do not treat `no blockers found` or `safe enough to proceed` as the satisfying endpoint of exploratory work when the better next step is canon uplift, roadmap clarification, or future-aware steering.
- Do not treat `adequate`, `sufficient`, `good enough`, or `works well` as satisfying conclusions for canon, roadmap, or intervention-planning work unless the artifact is genuinely a narrow gate check and nothing more.
- In canon-facing or audit-facing synthesis, ask not only `can this carry?` but `what does it newly expose, what does it still flatten, and what stronger next form would carry more of the work?`
- If a pass earns substantive doctrine, explicitly ask whether:
  - canon should be uplifted
  - roadmap language should be clarified
  - future seams should become more explicit
  - `LONG-ARC.md` should absorb or sharpen any doctrine that reaches beyond the next milestone
- Broad canon changes should usually have a proposal artifact first.
- Keep current execution scope narrow, but do not let Milestone 01 convenience create avoidable Milestone 02 ambiguity or later long-arc distortion.
- Treat horizon handling explicitly:
  - `ROADMAP.md` and phase docs carry near-term sequencing
  - `PROJECT.md` carries the compact product identity and milestone frame
  - `LONG-ARC.md` carries the farther doctrine that current planning must preserve without prematurely importing later scope
- Do not let repeated naming density or omission silently choose winners between still-live branches.

## Phase And Rerun Hygiene

- Treat active `CONTEXT.md` files as steering briefs, not lightweight notes.
- Do not import later wrapper, hosting, monetization, or event-memory decisions into a current phase unless they are explicitly in scope.
- Current repo boundary:
  - Phase 01 is at a pre-rerun boundary
  - use a fresh discuss + planning pass before execution
- Do not treat older `01-*` artifacts as execution-approved just because they exist.

## Planning-Local Self-Audit

Before adding or expanding instruction in either root `AGENTS.md` or `.planning/AGENTS.md`, ask:

- Is this truly agent-facing runtime guidance?
- Is it stable enough for a durable instruction file?
- Is it already governed elsewhere?
- Is it specific enough to deserve prompt budget?
- Would a nested file be a better fit than root?
- What stale-state risk does this add?

## Maintenance

- This file should stay durable and subtree-local.
- Do not create deeper nested `AGENTS.md` files under `.planning/` unless the subtree is both durable and meaningfully different in workflow.
- If `.planning/` operating norms change, update this file in the same change rather than letting local instruction drift.
