# Briefing: Phase 01 Preparatory Work And Initiative Scope

This memo is a **starting map** for the audit in `phase-01-prep-quality-scope-audit-task-spec.md`.

It is intentionally not a closed read list. Use it to get oriented quickly, then follow evidence wherever it leads.

## What This Audit Is Trying To Judge

The immediate question is whether the repo's current preparatory work supports a **small, targeted pre-Phase-01 vision-alignment initiative**, or whether that judgment is too narrow and the project actually needs broader alignment work before Phase 01 planning is rerun.

The deeper question is the quality of the preparatory corpus itself:

- does it genuinely narrow risk?
- does it only appear coherent because the same assumptions echo across documents?
- did recent GSD/framework/runtime adjustments materially improve the planning surface?
- are there unresolved contradictions between current state, committed docs, and live working-tree artifacts?

## High-Signal Canon Docs

These define the current project posture and should be read before judging whether broader alignment is needed:

- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/STATE.md`

Key issue to test:

- do these docs actually converge on one stable product center?
- or do they preserve enough open surface that broader initiative work is still warranted?

## Phase 01 Live Artifact Set

These are the main live Phase 01 inputs:

- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
- `.planning/phases/01-authored-round-contract/01-DISCUSSION-LOG.md`
- `.planning/phases/01-authored-round-contract/01-RESEARCH.md`
- `.planning/phases/01-authored-round-contract/01-VALIDATION.md`

The narrow-initiative judgment was based heavily on the claim that these, together with the core canon, make the remaining uncertainty look **phase-local** rather than project-wide.

Test that claim.

Questions worth asking:

- Is `01-CONTEXT.md` a genuinely strong steering brief, or did it close substrate questions too early?
- Does `01-RESEARCH.md` explore the option space honestly, or does it prematurely collapse toward one implementation shape?
- Does `01-VALIDATION.md` meaningfully increase confidence, or is it mostly downstream execution hygiene?

## Phase 01 State Mismatch

Current state and current worktree do not line up cleanly.

State says:

- `.planning/STATE.md` records Phase 01 as current focus
- status: planning
- stopped_at: `Phase 01 context gathered`
- plan count effectively back to zero

But the working tree currently contains untracked Phase 01 plan files:

- `.planning/phases/01-authored-round-contract/01-01-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-02-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-03-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-04-PLAN.md`

Interpretive question:

- are these legitimate current candidates, stale local residue, or evidence that the actual planning surface is muddier than the state file suggests?

## Superseded Archive

There is an explicit archive of prior overreach:

- `.planning/phases/01-authored-round-contract/superseded/2026-04-11-pre-rerun-overreach/README.md`
- `.planning/phases/01-authored-round-contract/superseded/2026-04-11-pre-rerun-overreach/phase/`
- `.planning/phases/01-authored-round-contract/superseded/2026-04-11-pre-rerun-overreach/project/STATE.md`

This matters because one reason a narrow initiative looked attractive was the belief that the earlier planning overreach had already been surfaced, corrected, and bounded.

Test whether that belief is warranted.

## Earlier Audit Corpus

Existing pre-execution audit set:

- `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md`
- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
- `.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md`
- lane reports in the same directory

Use these as predecessors, not as authoritative truth.

Chain-integrity question:

- Which claims from that audit set still hold after the later roadmap refresh, long-arc doctrine work, Phase 01 re-discuss, and planning/runtime changes?

## New Initiative Proposal Under Audit

This was just authored and should be treated as the thing being evaluated, not the answer:

- `.planning/initiatives/vision-alignment-2026-04/README.md`
- `.planning/initiatives/vision-alignment-2026-04/PLAN.md`
- `.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md`

This proposal is explicitly narrower than the `f1-modeling` initiative that inspired it. Its core claim is:

- Prix Guesser benefits from the methodology
- but only needs a smaller initiative focused on the authored substrate seam

Test whether that scope judgment was earned or merely asserted.

There is also an explicit one-sided advocacy memo making the strongest charitable case for that narrowness:

- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-best-case-minimal-alignment.md`

Use it as a stress target, not as a trusted premise.

## Recent Commit Chain To Inspect

The following commits are high-signal for how the preparatory surface evolved:

- `1a66b78` `tooling: load long-arc doctrine in discuss workflows`
  - changed repo-local GSD overlay files and discuss workflow behavior
  - relevant because it changed how canon is fed into discuss/planning

- `c553955` `planning: clear live phase 1 artifacts and retain superseded archive`
  - deleted a large prior live Phase 01 bundle and preserved it under superseded
  - relevant because it reset what counted as authoritative

- `c97d24a` `docs(01): capture phase context`
  - introduced the current `01-CONTEXT.md` and `01-DISCUSSION-LOG.md`

- `5189d4b` `docs(state): record phase 01 context session`
  - updated `.planning/STATE.md`

- `2ab8491` `docs(01-authored-round-contract): research phase domain`
  - added current `01-RESEARCH.md`

- `b34cba7` `docs(01): add validation strategy`
  - added current `01-VALIDATION.md`

Also inspect the overreach / revert sequence:

- `33131c9` `docs(state): record phase 01 planned status`
- `e9350da` `docs(01): add starter pack fixture plan`
- `d67551b` `Revert "docs(01): add starter pack fixture plan"`
- `7203964` `Revert "docs(state): record phase 01 planned status"`

Interpretive question:

- does this history show a repo that has already meaningfully corrected its planning excesses?
- or a repo whose planning surface is still unstable enough to justify broader alignment?

## Current Uncommitted Changes

Tracked diffs:

- `scripts/setup-portable-gsd.sh`
- `.planning/config.json`

Key content of those diffs:

- `.planning/config.json`
  - `_auto_chain_active` changed from `true` to `false`
  - relevant to the earlier question of whether discuss should auto-continue into planning/execution

- `scripts/setup-portable-gsd.sh`
  - now reapplies repo-local reasoning defaults into `.codex/config.toml`
  - injects per-agent `model_reasoning_effort` into named GSD role TOMLs
  - relevant because the preparatory work included debugging and reshaping the GSD runtime itself

Interpretive question:

- do these framework/runtime changes materially improve trust in the next planning pass?
- or are they orthogonal to the product-alignment question and therefore weak evidence for initiative sizing?

## Current Live Runtime Files Worth Sampling

These are not tracked in git, but they are part of the present local environment:

- `.codex/config.toml`
- `.codex/agents/gsd-planner.toml`
- `.codex/agents/gsd-phase-researcher.toml`
- `.codex/agents/gsd-project-researcher.toml`
- `.codex/agents/gsd-roadmapper.toml`
- `.codex/agents/gsd-ui-researcher.toml`
- `.codex/agents/gsd-executor.toml`
- `.codex/agents/gsd-debugger.toml`
- `.codex/agents/gsd-doc-writer.toml`
- `.codex/agents/gsd-plan-checker.toml`

These matter because recent work adjusted reasoning defaults so high-level planning/research roles can run `xhigh` while execution/verification roles stay `high`.

Possible relevance to this audit:

- positive case: the preparatory environment is more trustworthy now because role reasoning policy is explicit
- negative case: this is tooling hygiene, not evidence that the product doctrine is aligned enough for a narrow initiative

## Suggested Starting Order

This is a suggestion, not a constraint:

1. Read the core canon: `PROJECT.md`, `LONG-ARC.md`, `ROADMAP.md`, `REQUIREMENTS.md`
2. Read the live Phase 01 set: `01-CONTEXT.md`, `01-RESEARCH.md`, `01-VALIDATION.md`
3. Read the superseded archive README and compare it with current state
4. Read the 2026-04-08 audit synthesis and methodology review, but re-verify any claim you use
5. Read the new initiative proposal and test whether its narrowness follows from the evidence
6. Inspect the commit chain above to understand what changed the planning surface
7. Sample the current runtime/framework diffs only after the product-side corpus is understood

## Tensions Worth Explicitly Testing

### Tension 1: Coherence vs. premature closure

The current canon may be genuinely aligned.

But it may also merely share the same hidden assumptions.

### Tension 2: Phase-local uncertainty vs. broader under-alignment

The open questions in Phase 01 may truly be just authored-substrate questions.

Or they may be symptoms of broader unresolved doctrine about wrappers, content strategy, or room assumptions.

### Tension 3: Better workflow vs. better product understanding

Recent GSD/runtime tuning may make planning execution cleaner.

But cleaner planning machinery is not the same thing as stronger product alignment.

### Tension 4: Reverted overreach vs. persistent instability

The repo may have already learned from the earlier overreach and corrected course.

Or the reverts and leftover artifacts may show that the planning surface is still unstable enough that stronger alignment is prudent.

## Deliverable The Audit Should Produce

The final audit should make a judgment on at least these points:

- how strong the preparatory corpus actually is
- whether the narrow initiative is justified by evidence
- what broader questions, if any, still remain load-bearing
- whether current state/artifacts are clean enough to rerun Phase 01 planning responsibly
- what exact next step should happen before planning resumes
