# Claude Review Commands

These are concrete Claude CLI command patterns for readiness-package cross-vendor rereads.

They assume:

- you are in repo root
- the target artifact set is already coherent enough to review
- a baseline commit or explicit clean snapshot already exists
- the review prompt has been written to a file

Use these as execution patterns, not as blind ritual.

## Current Model Choices

Based on the repo's model-assignment research:

- routine external audit:
  - `claude-sonnet-4-6`
  - `--effort high`
- high-stakes doctrine / harness / readiness / stubborn-debug audit:
  - `claude-opus-4-6`
  - `--effort high`
- hardest or most adversarial Opus reread:
  - `claude-opus-4-6`
  - `--effort max`

Why:

- Sonnet is the routine strong external audit lane.
- Opus is the stronger high-stakes cross-vendor lane.
- The local CLI exposes `--effort`, not Anthropic's `adaptive` label, so use `high` by default and `max` only when the task is genuinely hard enough to justify it.

## Basic Pattern

Write the review prompt to a file first, for example:

```bash
PROMPT=.planning/readiness/phase-01-rerun/review-prompts/checkpoint-4-review-prompt.md
OUT=.planning/readiness/phase-01-rerun/reviews/checkpoint-4-claude-sonnet-review.md
```

Then run:

```bash
claude -p \
  --model claude-sonnet-4-6 \
  --effort high \
  "$(cat "$PROMPT")" \
  > "$OUT"
```

## Routine External Audit

Use for:

- governance-doc normalization audit reread
- doctrine-sensitive phase-plan reread where strong external pressure is useful but Opus is not justified
- rerun-readiness verification when the judgment matters but is not maximally fraught

```bash
PROMPT=.planning/readiness/phase-01-rerun/review-prompts/routine-external-review.md
OUT=.planning/readiness/phase-01-rerun/reviews/routine-claude-sonnet-review.md

claude -p \
  --model claude-sonnet-4-6 \
  --effort high \
  "$(cat "$PROMPT")" \
  > "$OUT"
```

## High-Stakes Doctrine / Harness Audit

Use for:

- harness ownership review
- canon-sensitive synthesis reread
- rerun-readiness judgment with real interpretive load

```bash
PROMPT=.planning/readiness/phase-01-rerun/review-prompts/high-stakes-review.md
OUT=.planning/readiness/phase-01-rerun/reviews/high-stakes-claude-opus-review.md

claude -p \
  --model claude-opus-4-6 \
  --effort high \
  "$(cat "$PROMPT")" \
  > "$OUT"
```

## Hardest Adversarial Opus Pass

Use sparingly for:

- architecture-setting disputes
- highest-stakes canon/harness rereads
- stubborn-debug escalations where weaker review already failed

```bash
PROMPT=.planning/readiness/phase-01-rerun/review-prompts/adversarial-review.md
OUT=.planning/readiness/phase-01-rerun/reviews/adversarial-claude-opus-max-review.md

claude -p \
  --model claude-opus-4-6 \
  --effort max \
  "$(cat "$PROMPT")" \
  > "$OUT"
```

## Fresh Phase 01 Plan Reread

Default stronger external reread for a doctrine-sensitive fresh plan:

```bash
PROMPT=.planning/readiness/phase-01-rerun/review-prompts/phase-01-plan-review.md
OUT=.planning/readiness/phase-01-rerun/reviews/phase-01-plan-claude-sonnet-review.md

claude -p \
  --model claude-sonnet-4-6 \
  --effort high \
  "$(cat "$PROMPT")" \
  > "$OUT"
```

Escalate to Opus if the plan remains contested or heavily interpretive:

```bash
PROMPT=.planning/readiness/phase-01-rerun/review-prompts/phase-01-plan-review.md
OUT=.planning/readiness/phase-01-rerun/reviews/phase-01-plan-claude-opus-review.md

claude -p \
  --model claude-opus-4-6 \
  --effort high \
  "$(cat "$PROMPT")" \
  > "$OUT"
```

## Prompt Discipline

Before running the command:

- persist the prompt file in the repo
- name the exact artifact(s) under review
- include the baseline commit or explicit clean snapshot
- keep the prompt comparable across vendors when doing cross-vendor rereads

After running the command:

- write a review artifact using [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md)
- record whether the Claude lane used was:
  - routine Sonnet
  - high-stakes Opus
  - adversarial Opus max
- record what independence added or why the Claude lane was unavailable

## What Not To Do

- do not use `claude -c` or `--resume` for these checkpoint reviews
- do not rely on chat-local prompts that are not persisted
- do not treat Sonnet and Opus as interchangeable
- do not use `max` by default just because it sounds stronger
