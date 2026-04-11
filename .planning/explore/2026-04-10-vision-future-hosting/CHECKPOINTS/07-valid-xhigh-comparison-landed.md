# Checkpoint 07: Valid XHigh Comparison Landed

Updated: 2026-04-10

## Why This Checkpoint Exists

This checkpoint captures a methodological turning point that matters for all subsequent exploration research:

- the `default`-agent `xhigh` comparison pass completed successfully
- so the session now has one valid high-vs-xhigh-style comparison artifact produced under the refined method

## What Landed

The completed valid comparison artifact is:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md`

This matters because the earlier `gsd-phase-researcher` attempt had to be discarded when the user-visible spawn banner showed `high`.

So until this file landed, the session only had:

- one failed role-based comparison attempt
- one methodological hunch that `default` was the right agent type

Now it has:

- a confirmed `default`-agent `xhigh` launch
- a completed comparison artifact produced through that path

## Why This Changes The Method

The session now has stronger practical grounds for a working rule:

- use `default` agents for exploratory comparison research
- reserve planner-shaped role agents for genuinely planner-shaped tasks

This does not prove the internal root cause of the earlier mismatch.

But it does provide a reliable-enough operational path for continuing the exploration without being blocked by that unresolved runtime question.

## Relation To The First-Wave Reruns

The new first-wave reruns were launched on precisely this basis.

Those reruns are:

- `01-product-futures-xhigh-comparison`
- `02-hosting-transition-xhigh-comparison`

And they are being run with:

- `agent_type: default`
- `model: gpt-5.4`
- `reasoning_effort: xhigh`

So this checkpoint should be read as the bridge between:

- the earlier spawn-mismatch confusion
- and the now-stabilized rerun method

## Best Next Resumption Move

When resuming:

1. treat `05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md` as the first valid demonstration of the refined method
2. wait for the first-wave reruns to complete
3. compare those reruns against the original first-wave findings
4. bring those comparisons back into the product-vision discussion
