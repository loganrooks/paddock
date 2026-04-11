# Checkpoint 05: Second Wave Landed, XHigh Comparison Failed

Updated: 2026-04-10

## Why This Checkpoint Exists

This checkpoint captures two things that materially changed the state of the exploration:

- the four main second-wave research lanes completed and wrote findings
- an attempted `xhigh` comparison pass was launched, appeared to land as `high`, and was shut down rather than accepted

Both matter for session continuity.

## What Landed

The following second-wave findings are now on disk:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/01-cooperative-scaling-and-p2p-feasibility.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/02-funding-access-and-transparency-models.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/03-public-transition-and-discovery.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/04-security-trust-and-operational-risk.md`

So the exploration is no longer in "research launched" state. It is in "second-wave evidence available for reading" state.

## Why The XHigh Attempt Matters

The user suggested a good methodological refinement:

- pick one of the hardest questions
- create a stricter comparison charter for it
- run an `xhigh` comparison pass so that the `high` and `xhigh` outputs can be contrasted

The chosen question was cooperative scaling / P2P feasibility because it is unusually tangled:

- technical possibility
- room authority
- cheating and trust
- browser constraints
- operator burden
- casual-user adoption friction

That made it a strong candidate for a deeper comparison run.

## What Went Wrong

A separate comparison charter was written and a comparison agent was launched.

But the user saw the spawn banner report:

- `Spawned Bohr [gsd-phase-researcher] (gpt-5.4 high)`

That conflicted with the requested `xhigh`.

This is important because the issue here is not whether the request looked right in the orchestration file. The issue is whether the effective launch matched it.

Per the repo's explicit policy, the mismatch was treated seriously. The lane was shut down immediately rather than treated as "probably fine."

So there is currently:

- a written comparison charter
- no accepted `xhigh` comparison findings

## Why This Should Be Preserved

This is not just an orchestration footnote.

It changes how future research comparisons should be handled. The session has now learned that:

- requested settings are not enough
- user-visible launch state may reveal mismatches earlier than the orchestrator can prove from local runtime files
- any future attempt to compare reasoning levels should begin by solving or understanding the spawn-setting reliability problem

## Best Next Resumption Move

When resuming:

1. read the four landed second-wave findings
2. treat them as pressure tests on the design space, not as automatic decisions
3. decide whether to investigate the `xhigh`/`high` mismatch before attempting another comparison run
4. continue the product-vision discussion with transition, hosting risk, and publicness still treated as first-class concerns
