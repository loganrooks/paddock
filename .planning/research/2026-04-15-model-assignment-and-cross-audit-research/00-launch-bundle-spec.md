# Model Assignment And Cross-Audit Research

Date: 2026-04-15
Status: launch-ready

## Why This Exists

This bundle exists to improve model-assignment policy for this repo's agentic work.

The motivating questions are:

- which recent Codex/GPT models are best for which task types important to this project
- whether claims like "`gpt-5.3-codex` can outperform `gpt-5.4` for execution" are real, conditional, or merely anecdotal
- how recent GPT models compare with Claude Sonnet and Opus across reasoning levels
- when cross-model auditing is genuinely useful versus mostly redundant
- what the different "reasoning levels" likely mean operationally

The target is not abstract model fandom. The target is better assignment policy for:

- orchestration
- exploratory research
- product/canon synthesis
- planning
- execution/editing
- debugging
- validation/checking
- cross-model audit or review

## Questions To Answer

1. As of 2026-04-15, what official guidance exists from OpenAI and Anthropic about:
   - current model families relevant to coding/reasoning work
   - reasoning-effort levels or analogous modes
   - intended use cases and tradeoffs
2. What credible recent comparative evidence exists about:
   - GPT-5.4 vs GPT-5.3-codex vs other relevant recent GPT coding models
   - Claude Sonnet vs Claude Opus on similar coding/reasoning tasks
   - how reasoning levels change quality, latency, and reliability
3. For repo-relevant task families, what assignment guidance is justified, and what remains mostly anecdotal?
4. How useful is cross-model auditing:
   - across companies
   - across model tiers
   - across reasoning levels of the same family
5. What is the best current assignment matrix for this repo, with caveats?

## Task Families To Cover

- top-level orchestration
- ambiguity-heavy exploratory research
- mature-product/canon synthesis
- phase planning
- execution / implementation edits
- debugging
- validation / checking / review
- adversarial or cross-model audit

## Source Priorities

Priority order:

1. official OpenAI documentation and official OpenAI sources
2. official Anthropic documentation and official Anthropic sources
3. recent credible benchmarks, technical writeups, issue threads, or practitioner reports
4. anecdotal reports only when clearly marked as anecdotal

## Output

Write:

- [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md)

The output should include:

- official baseline by vendor
- explanation of what reasoning levels appear to do, with clear separation of evidence vs inference
- comparison table by task family
- explicit note where evidence is thin or mostly anecdotal
- repo-specific assignment recommendations
- commentary on cross-model audit value and likely failure modes

## Claim / Citation Requirements

This is a load-bearing planning/process artifact.

Use the repo claim/citation scheme for load-bearing claims where it materially helps:

- `[type:support:basis]`

External-direct claims should use markdown footnotes plus `External Works Cited`.

If a recommendation is mainly reasoned synthesis from mixed evidence, say so rather than presenting it as a settled benchmark result.

## Relevant Local Inputs

- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md)
- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)

## Non-Goals

- do not drift into broad AI philosophy
- do not pretend there is precise universal benchmarking for every reasoning level combination if there is not
- do not recommend repo policy changes without tying them back to actual task families in this repo
