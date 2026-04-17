# Lane 01c Prompt-Writer Request

You are writing an execution prompt for a second Claude Code CLI `opus[1m]` `xhigh` run.

Your job is not to do the docs-gap audit itself. Your job is to write the best possible execution prompt for a later large-context Claude reread.

## Why This Prompt Exists

The user wants a cross-vendor, large-context reread of the upstream GSD docs gap problem, because they do not want to treat the existing internal `lane-01` or `lane-01b` path as fully epistemically reliable for a future docs-refresh or docs-seeded remapping decision.

The user instruction to preserve in spirit is:

> do not really take anything in the original lane 01 report for granted out of suspicion that the size of the task + the smaller context window, made certain interpretations of observations epistemically unreliable

The user also wants the reread aimed at:

- what in the docs is accurate enough to build from
- what is out of date
- what gaps or exclusions exist
- where the docs could use freshening
- how a supplementation pass could build off the docs instead of starting from scratch

## Inputs You Should Read Before Writing The Execution Prompt

1. `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01-upstream-docs-freshness-task-spec.md`
2. `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01-upstream-docs-freshness.md`
3. `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01b-docs-gap-map-task-spec.md`
4. `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01b-docs-gap-map.md`
5. `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md`
6. `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01c-claude-opus-1m-independent-reread-task-spec.md`

You may also reference the upstream repo directly:

- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/README.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/CHANGELOG.md`
- selected command, workflow, agent, template, and test surfaces as needed

## What The Execution Prompt Must Force The Later Reread To Do

- Treat `lane-01` and `lane-01b` as candidate evidence, suggested read surfaces, and possible blindspot seeds.
- Not assume those internal artifacts are correct.
- Read the upstream docs and corroboration surfaces directly.
- Re-traverse the docs-gap question with its own epistemic path.
- Focus on docs trust surfaces, omissions, stale summaries, misleading claims, supplementation strategy, and plausible patch bundles or PR tracks.
- Stay bounded to the docs-gap / docs-refresh / docs-seed question rather than wandering into general program revision.

## Output Contract For You

Write only the execution prompt text.

The execution prompt you produce should:

- be ready to pass directly to `claude -p --model 'opus[1m]' --effort xhigh`
- name the output file the later run should write:
  `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01c-claude-opus-1m-independent-gap-reread.md`
- require a structured final artifact with clearly named sections
- require the later run to explicitly note where it agrees with, revises, or rejects prior internal lane claims
- require the later run to distinguish:
  - trustworthy summary surfaces
  - omitted shipped surfaces
  - stale or misleading summaries
  - supplementation / patch strategy
  - unresolved uncertainties

Do not include any preamble or explanation. Output only the execution prompt.
