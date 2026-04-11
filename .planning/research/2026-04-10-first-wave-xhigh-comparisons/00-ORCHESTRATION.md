# First-Wave XHigh Comparison Reruns

Date: 2026-04-10
Orchestrator: Codex
Status: completed

## Why This Wave Exists

The first exploratory research wave was useful, but it was run before the stricter second-wave research standard existed.

This comparison wave reruns the two most important first-wave lanes:

- `01-product-futures`
- `02-hosting-transition`

The purpose is not to invalidate the first wave reflexively.

The purpose is to test what changes when:

- the charter is rewritten to the stronger exploratory standard
- the agent is a plain `default` subagent rather than `gsd-phase-researcher`
- the requested reasoning level is `xhigh`

## Why These Two Lanes

These two lanes exert the strongest pressure on the exploration:

1. `product futures`
   - identity, stage-shapes, wrappers, watchability, and what kind of product this is becoming

2. `hosting transition`
   - local-first, self-hosting, public transition, trust-preserving capacity limits, and material constraints

Together they shape both the product horizon and the operational trajectory.

## Why Default Agents

This wave intentionally uses `default` agents rather than `gsd-phase-researcher`.

Reason:

- `gsd-phase-researcher` is optimized for planner-facing, prescriptive phase research
- this comparison wave is exploratory, gray-area-preserving, and not downstream-planner-driven
- a plain `default` agent is the better instrument for open inquiry here

## Governing Standard

These reruns must follow:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md`

## Shared Starting Context

All lanes should read these first:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/.continue-here.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md`

## Comparison Discipline

Each lane must:

1. read the original first-wave spec for that lane
2. perform an independent rerun against the stronger standard
3. read the original first-wave findings only after its own map has been formed
4. explicitly compare:
   - what the original pass got right
   - what the rerun sees more clearly
   - where the rerun disagrees
   - whether the difference comes from reasoning depth, better standards, or just changed framing

## Required Output Structure

Each findings file must include:

1. `Question Space`
2. `Method And Sources`
3. `Inquiry Trajectory`
4. `Branching Paths And Dependencies`
5. `Findings`
6. `Gray Areas And Live Tensions`
7. `Scope Expansions`
8. `Rival Models Still Alive`
9. `Practical Implications`
10. `Comparison With Original First-Wave Pass`
11. `What Would Change This View`
12. `Open Questions Worth A Further Pass`
13. `Source Ledger`

All substantive claims should still be marked with:

- `[CONFIRMED]`
- `[INFERRED]`
- `[HYPOTHESIS]`

## Lane Map

1. `01-product-futures-xhigh-comparison`
   Focus: rerun the product-futures / stage-shapes / watchability inquiry under the stricter exploratory standard.

2. `02-hosting-transition-xhigh-comparison`
   Focus: rerun the hosting / staged transition / trust-preserving public growth inquiry under the stricter exploratory standard.

## Output Contract

Each lane owns exactly one findings file under `findings/`.

No lane should modify any other file.

## Launch Record

Requested launch settings for this wave:

- `agent_type`: `default`
- `model`: `gpt-5.4`
- `reasoning_effort`: `xhigh`

Launched lanes:

- lane `01-product-futures-xhigh-comparison`
  - agent id: `019d7955-d394-7403-acc3-249e86d2d912`
  - nickname: `Maxwell`
  - spec: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/specs/01-product-futures-xhigh-comparison.md`
  - output: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/findings/01-product-futures-xhigh-comparison.md`
- lane `02-hosting-transition-xhigh-comparison`
  - agent id: `019d7956-8632-7880-b90f-ac166e1b461c`
  - nickname: `Faraday`
  - spec: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/specs/02-hosting-transition-xhigh-comparison.md`
  - output: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/findings/02-hosting-transition-xhigh-comparison.md`

Filesystem note:

- `findings/` now exists explicitly under this comparison workspace
- both rerun findings files later landed successfully

Verification note:

- the engine log records the requested `spawn_agent` calls with `agent_type:"default"` and `reasoning_effort:"xhigh"`
- earlier in this session, a `default` comparison agent (`Einstein`) was confirmed by the user-visible spawn banner to have launched as `xhigh`
- that makes these reruns materially better-founded than the earlier `gsd-phase-researcher` comparison attempt
- requested settings and effective runtime state are still separate facts, so this file records the request side explicitly and relies on user-visible spawn evidence when available

Completion note:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/findings/01-product-futures-xhigh-comparison.md` landed
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/findings/02-hosting-transition-xhigh-comparison.md` landed
- both rerun agents were closed after completion

## Intended Use

This wave is a comparison and refinement wave.

It should help answer:

- whether the first-wave results remain robust under a stronger standard
- what the original research missed or flattened
- whether `default` + `xhigh` produces materially better exploratory outputs for this project than the planner-oriented research role
