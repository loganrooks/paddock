# Model Assignment Policy Response

Date: 2026-04-15  
Status: active policy response

This artifact translates:

- [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md)

into current repo policy, bounded follow-through, and what should remain open.

## What Is Decided Now

- `[d:c:i+d]` Keep `gpt-5.4` as the repo's primary default model family. The current evidence does not justify replacing it with `gpt-5.3-codex` as the broad default for this repo's mixed work ([01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:151), [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:103)).
- `[d:c:i+d]` Keep `xhigh` for top-level orchestration, ambiguity-heavy exploratory research, mature-product/canon synthesis, and planning-oriented work ([01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:115), [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:151)).
- `[d:c:i+d]` Keep `high` for execution, debugging, validation, and verification by default ([01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:118), [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:152)).
- `[d:c+r:i+d]` For high-stakes audit and review, prefer cross-vendor audit over same-model effort-only reruns when an external lane is available. Same-model effort changes are useful depth adjustments, but not a strong substitute for an independent reviewer ([01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:135), [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:153)).

## Strong Current Preference For External Audit

- `[d:c+r:i+d]` Use `claude-opus-4.6` as the strongest current external audit / hard-problem escalation lane for:
  - architecture-setting review
  - canon-sensitive planning review
  - stubborn debugging
  - adversarial rereading of major synthesis or audit outputs
- `[d:c+r:i+d]` Use `claude-sonnet-4.6` as the cheaper routine external audit lane where:
  - the work is review-worthy
  - vendor diversity still matters
  - but full Opus cost/latency is not justified

These are current policy preferences, not permanent doctrine. They should be revisited if local evals or vendor changes materially shift the tradeoff.

## What Stays Conditional

- `[a:c+r:i+d]` `gpt-5.3-codex` remains a plausible bounded execution specialist, but only conditionally. The current evidence supports piloting it later on narrow code-heavy execution loops, not replacing `gpt-5.4 high` repo-wide ([01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:129), [01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:154)).
- `[o:c+r:i+d]` The exact local crossover point where `gpt-5.3-codex high` beats `gpt-5.4 high` for this repo's bounded execution tasks remains open ([01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:156)).
- `[o:c+r:i+d]` The exact best external audit default between routine Sonnet and escalated Opus also remains open, though the current preference is clear enough for policy use now ([01-model-assignment-and-cross-audit-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/01-model-assignment-and-cross-audit-research.md:157)).

## What We Should Not Do

- `[d:c+r:i+d]` Do not replace repo model policy based on anecdotal issue-thread chatter alone.
- `[d:c+r:i+d]` Do not let narrow execution-only claims silently choose the default model for mixed planning/canon/coding work.
- `[d:c+r:i+d]` Do not treat same-model reasoning-effort changes as if they automatically provide meaningful audit independence.

## Suggested Follow-Through

- `[p:r:i]` Keep current AGENTS-level model defaults as they are for now.
- `[p:r:i]` If later we want to refine execution-lane policy, run a bounded local eval comparing:
  - `gpt-5.4 high`
  - `gpt-5.3-codex high`
  on representative narrow execution tasks from this repo.
- `[p:r:i]` If Anthropic access becomes part of routine workflow, define a simple escalation ladder:
  - routine external audit -> Sonnet
  - high-stakes architecture/canon/stubborn-debug escalation -> Opus
