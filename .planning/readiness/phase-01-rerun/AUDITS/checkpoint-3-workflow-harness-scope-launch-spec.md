# Checkpoint 3 Workflow / Harness Scope Audit Bundle

This bundle defines how Checkpoint 3 should be executed.

## Purpose

Map the real workflow / harness landscape before Checkpoint 4 fixes the deeper excellence-audit envelope.

The output of this checkpoint must be reusable later as:

- a harness-orientation / audit-onboarding surface
- the justified audit envelope for Checkpoint 4
- a filter that distinguishes doc-local governance issues already handled in Checkpoint 2 from deeper machinery-owned follow-through

## Bundle Shape

Run these lanes:

1. `checkpoint-3-codex-surface-map`
2. `checkpoint-3-gsd-surface-map`
3. `checkpoint-3-scope-synthesis`

## Launch Order

- Launch the Codex and GSD mapping lanes in parallel.
- Do not launch the synthesis lane until both mapping outputs exist or the GSD lane explicitly requests a deeper split.

## Global Non-Goals

- do not redesign the harness in Checkpoint 3
- do not patch GSD or Codex machinery in Checkpoint 3
- do not confuse skill count with harness importance
- do not optimize for the smallest possible audit envelope if that would hide a load-bearing surface

## Split Trigger

The GSD lane must not bluff completeness.

If the GSD mapper concludes that the repo-local GSD surface is too broad to map honestly in one pass, it must:

- say so explicitly
- identify the sublanes it thinks are required
- explain why the split is load-bearing rather than merely convenient
- stop short of pretending to have completed the full GSD map

If that happens:

- checkpoint the partial mapping honestly
- launch the required GSD sublanes
- add a GSD-only synthesis step before returning to the overall Checkpoint 3 synthesis

## Expected Primary Outputs

- [checkpoint-3-codex-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-codex-surface-map.md)
- [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md)
- [checkpoint-3-workflow-harness-scope-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md)

## Model / Reasoning

- mapping lanes: `gpt-5.4 xhigh`
- synthesis lane: `gpt-5.4 xhigh`

## Closure Standard

Checkpoint 3 is not complete when we merely have "some notes about the harness."

It is complete only when:

- the later Checkpoint 4 audit has a defensible unit of analysis
- later auditors can onboard into the harness landscape without relying on session memory
- broad-but-shallow surfaces have been separated from narrow-but-load-bearing ones
- any required GSD split was handled honestly rather than waved away
