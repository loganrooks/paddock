# Best-Case Memo: Why Minimal Vision Alignment Might Be Sufficient

This memo is intentionally one-sided.

It is not the final judgment. It is the strongest charitable case for the claim that Prix Guesser may need only a **minimal, targeted pre-Phase-01 vision-alignment initiative** rather than a broader one.

Use it as an argument to test, not an answer to trust.

## Core Claim

The repo may already be aligned enough at the product and roadmap level that the remaining uncertainty is **narrow, local, and Phase-01-specific** rather than broad and project-defining.

If that is true, then a small initiative focused on the authored substrate is the right move.

## Why This Claim Is Plausible

### 1. The product center is already unusually explicit for a repo at this stage

The core canon is not vague about what the project is:

- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`

Across those files, the project repeatedly converges on the same center:

- private-only, trusted-group posture
- one strong authored geography-and-circuit anchor mode
- watchable host-screen social play as the v1 wrapper
- browser-first guest/controller flow
- preserve future seams without importing future scope

That matters because a full vision-alignment initiative is most justified when the base canon is still fighting itself. The current canon may not be complete, but it is not obviously incoherent.

### 2. The highest-risk architectural seam has already been correctly identified

The repo does not currently seem confused about where the real early risk is.

Both the canon and the recent Phase 01 work point to the same seam:

- the authored round and pack contract
- answer-surface ontology
- clue-family and fallback doctrine
- identity/reference freezing

That is visible in:

- `.planning/ROADMAP.md` Phase 1
- `.planning/REQUIREMENTS.md` requirements `PACK-02`, `PACK-03`, `PACK-04`, `OPS-01`
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
- `.planning/phases/01-authored-round-contract/01-RESEARCH.md`

This is a strong sign. A broader initiative is most necessary when the project is still asking the wrong-sized question. Prix Guesser may already be asking the right one.

### 3. The open questions look bounded, not existential

The main open questions now seem to be:

- where coverage/fallback truth should live
- how much answer-target lineage must be explicit now
- how rich the first scoring-intent contract should be

Those are serious questions, but they are not obviously "what is this product?" questions. They look more like:

- how to freeze the authored substrate without overfitting it

That distinction is the best argument for minimal alignment. If the remaining questions are seam-shaping but not product-redefining, then the initiative should stay narrow.

### 4. The repo already corrected one round of planning overreach

There is concrete evidence that the repo has already identified and bounded a previous overreach cycle:

- `c553955` cleared the live Phase 01 bundle and retained the prior work under a superseded archive
- `c97d24a` and `5189d4b` rebuilt the Phase 01 context/state surface
- `2ab8491` and `b34cba7` rebuilt research and validation
- `d67551b` and `7203964` reverted earlier premature planned-state artifacts

The best charitable interpretation is:

- the repo already learned that "plans existing" is not the same as "alignment achieved"
- the current surface is a second pass, not naïve first-pass optimism

If true, that makes a small corrective initiative more plausible than a large reset.

### 5. The long-arc doctrine is already separated from current-scope work

One of the biggest reasons to do a large initiative is when later-platform ambition keeps leaking into v1 decisions.

But `.planning/LONG-ARC.md` seems designed precisely to prevent that. It tries to:

- preserve Milestone 2 and 3 seams
- keep publicness and wrapper transitions explicit
- avoid importing later obligations into current planning

And `1a66b78` explicitly wired long-arc doctrine into discuss workflows. That is evidence that the repo has already operationalized some of the alignment work a broader initiative would otherwise need to perform.

### 6. The new narrow initiative is not arbitrary

The proposed initiative under:

- `.planning/initiatives/vision-alignment-2026-04/README.md`
- `.planning/initiatives/vision-alignment-2026-04/PLAN.md`
- `.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md`

is not merely "do less."

It is doing something more specific:

- refusing to reopen already-stabilized product doctrine
- focusing only on the authored-substrate seam Phase 01 is about to freeze
- allowing expansion only if the research surfaces broader underdetermination

That is arguably the correct posture when the repo looks directionally aligned but still needs one final contract-level clarification pass.

### 7. Recent GSD/runtime work may reduce procedural noise

Part of the earlier confusion came from the planning machinery itself:

- discuss/plan auto-chaining confusion
- named-role reasoning mismatches
- unclear role defaults for planning agents

Current changes suggest the repo is cleaning that up:

- `.planning/config.json` now has `_auto_chain_active: false` in the working tree
- `scripts/setup-portable-gsd.sh` now reapplies explicit reasoning defaults
- live `.codex/` agent TOMLs pin high-value planning/research roles to `xhigh` while leaving execution/verification at `high`

The strongest version of the minimal-alignment case says:

- some of what felt like "vision uncertainty" may actually have been workflow noise, orchestration error, and unreliable planning conditions
- now that the planning environment is cleaner, a narrow initiative may be enough

## The Strongest Positive Reading Of The Current Corpus

If one reads the current repo as charitably as possible, the picture is:

1. The project already knows what kind of thing it is.
2. The roadmap already protects the right long-arc seams.
3. The early highest-risk seam has already been correctly identified as authored content substrate, not frontend or room tech.
4. The remaining uncertainty is real but bounded.
5. Prior overreach has already been surfaced and partially corrected.
6. The new initiative proposal is narrow for substantive reasons, not just to save time.

Under that reading, a minimal initiative is not reckless. It is proportionate.

## What Would Have To Be True For This Memo To Hold

This best-case argument only works if several things are true:

- the canon docs are convergent for real, not merely rhetorically similar
- the Phase 01 context/research set does not smuggle in premature closure
- the open questions are truly authored-substrate questions, not disguised product-shape questions
- the superseded archive and revert history reflect genuine course correction, not ongoing instability
- the recent runtime/workflow changes remove procedural distortion rather than simply shifting it

If any of those fail under audit, the case for minimal alignment weakens quickly.

## Most Important Vulnerability In This Argument

The biggest weakness in the minimal-alignment case is this:

documents can look aligned because they repeat the same framing, not because the framing has actually been stress-tested.

So the audit should especially test whether the current coherence is:

- earned convergence
- or repeated assumption

That is the pressure point.

## Bottom Line

The strongest argument for minimal vision alignment is not "we should hurry" or "the docs look fine."

It is:

- the repo may already have done most of the broad alignment work,
- the remaining uncertainty may genuinely sit at the authored-substrate seam,
- and a narrow initiative may therefore be the most disciplined way to reduce risk without reopening settled doctrine.
