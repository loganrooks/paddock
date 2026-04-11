# Second Research Wave: Scaling, Funding, Public Transition, And Risk

Date: 2026-04-10
Orchestrator: Codex
Status: launched

## Why This Wave Exists

The first research wave clarified the broad terrain:

- Prix Guesser likely makes more sense as a shared authored F1 substrate plus multiple wrappers
- the first strong proof still likely looks like a watchable private game-night shell
- web-first remains plausible across local, self-hosted, and later modest public operation
- future-aware planning should likely be made explicit with light schema rather than heavy governance

What the first wave did not answer well enough are the harder transition questions:

- can the project scale with minimal personal financial risk?
- is any form of peer-assisted or cooperative compute remotely feasible?
- what funding and access models are aligned with the project's ethos?
- how does a private-first niche product become selectively public?
- what security, trust, and operational burdens appear as those transitions happen?

This second wave is narrower in subject but deeper and more dialectical in method.

## Governing Standard

All lanes must follow:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md`

That means every lane must:

- map its inquiry trajectory
- show branching paths and dependencies
- explicitly mark scope expansions
- dwell in gray areas and live tensions
- preserve rival models that remain viable
- distinguish technical, operational, adoption, economic, and ethical feasibility

## Shared Starting Context

All lanes should read these first:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/.continue-here.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/01-product-futures.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/03-precedents-and-trajectories.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md`

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
10. `What Would Change This View`
11. `Open Questions Worth A Third Pass`
12. `Source Ledger`

All substantive claims should still be marked with:

- `[CONFIRMED]`
- `[INFERRED]`
- `[HYPOTHESIS]`

## Lane Map

1. `01-cooperative-scaling-and-p2p-feasibility`
   Focus: whether peer-assisted or cooperative compute could ever be part of the transition story, and what technical, adoption, and trust barriers appear.

2. `02-funding-access-and-transparency-models`
   Focus: donations, paid/free tiers, contribution models, capacity guarantees, and honest capacity communication.

3. `03-public-transition-and-discovery`
   Focus: how a private-first niche hobby project might become selectively public, how discovery might work, and what kinds of growth loops align with the product.

4. `04-security-trust-and-operational-risk`
   Focus: attack surface, abuse, moderation, privacy, operational burden, and failure modes introduced by broader hosting or cooperative contribution.

5. `05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility`
   Focus: a comparison-depth pass on the hardest lane, using `xhigh` reasoning to test whether the higher-reasoning run surfaces materially different tensions, hidden assumptions, or dependency structures than the `high` run.

## Output Contract

Each lane owns exactly one findings file under `findings/`.

No lane should modify any other file.

## Launch Record

Requested launch settings for all lanes:

- `agent_type`: `gsd-phase-researcher`
- `model`: `gpt-5.4`
- `reasoning_effort`: `high`

Launched lanes:

- lane `01-cooperative-scaling-and-p2p-feasibility`
  - agent id: `019d793e-6e97-7630-9ca2-c4ba750c2c13`
  - nickname: `Bernoulli`
  - output: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/01-cooperative-scaling-and-p2p-feasibility.md`
- lane `02-funding-access-and-transparency-models`
  - agent id: `019d793e-6ee2-7793-b054-6f1436307a6c`
  - nickname: `Ampere`
  - output: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/02-funding-access-and-transparency-models.md`
- lane `03-public-transition-and-discovery`
  - agent id: `019d793e-6f35-7110-b6ab-43136805ce1b`
  - nickname: `Hooke`
  - output: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/03-public-transition-and-discovery.md`
- lane `04-security-trust-and-operational-risk`
  - agent id: `019d793e-6f9f-7571-b588-d9a913162bed`
  - nickname: `Feynman`
  - output: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/04-security-trust-and-operational-risk.md`

Comparison lane planned after launch:

- lane `05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility`
  - requested agent type: `gsd-phase-researcher`
  - requested model: `gpt-5.4`
  - requested reasoning: `xhigh`
  - rationale: this is the lane most likely to reward extra depth because technical possibility, social tolerability, room authority, cheating/trust, browser/network limits, and adoption friction all interact
  - output: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md`

Comparison lane launch result:

- agent id: `019d7945-7650-76a0-903a-7f2f01cefa82`
- nickname: `Bohr`
- requested settings: `gpt-5.4` with `xhigh`
- effective launch concern: the user-visible spawn banner reported `gpt-5.4 high`, not `xhigh`
- action taken: the lane was shut down immediately rather than treated as a valid `xhigh` run
- output status: no accepted comparison findings from this lane

Valid comparison rerun using a default agent:

- agent id: `019d794e-cc74-7472-a19c-3e4ace3d2424`
- nickname: `Einstein`
- agent type: `default`
- requested settings: `gpt-5.4` with `xhigh`
- user-visible spawn evidence: confirmed by user as `xhigh`
- output: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md`
- status: completed and accepted as the valid `xhigh` comparison pass

Verification note:

- per repo policy, requested launch settings and effective runtime-persisted settings are separate facts
- `codex-tui.log` confirms launched child threads for these agent ids under `model=gpt-5.4`
- in-session readback from `/home/rookslog/.codex/logs_1.sqlite` and `/home/rookslog/.codex/state_5.sqlite` was blocked by the same readonly SQLite issue encountered earlier, so effective persisted reasoning could not be positively verified here
- therefore this artifact records the requested settings and the partial model confirmation only; it does not claim positive verification of effective persisted `reasoning_effort`
- for the comparison lane, the user-visible launch banner was treated as stronger evidence that the effective launch did not honor the requested `xhigh`, so the lane was stopped
- for the replacement default-agent comparison lane, the user-visible launch banner was treated as positive evidence that `xhigh` did honor the request

## Intended Use

This wave is not a decision wave.

Its purpose is to improve the quality of the open exploration by:

- clarifying hard tradeoffs
- showing where gray areas remain
- and identifying what can only be learned by experiment rather than armchair reasoning
