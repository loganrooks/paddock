# Lane 01c: Claude Opus 1M Independent Docs-Gap Reread

## Purpose And Honest Scope Claim

Run a cross-vendor, large-context reread of the docs-gap problem using Claude Code CLI with `opus[1m]` and `xhigh`.

This lane exists because the user explicitly objected to treating the internal `lane-01` and `lane-01b` path as epistemically sufficient for a later docs-refresh or docs-seeded remapping decision. The Claude lane should therefore re-traverse the task independently, while treating prior internal artifacts as:

- candidate claims
- suggested read surfaces
- possible blindspot seeds

and not as settled truth.

This lane is not:

- permission to rewrite the upstream docs directly
- a readiness-program revision lane
- a requirement to agree with `lane-01` or `lane-01b`
- a generic harness map from scratch beyond what the docs-gap question requires

## Execution Shape

1. Persist a prompt-writer prompt artifact.
2. Run Claude Code CLI `opus[1m]` `xhigh` to write the execution prompt artifact.
3. Run a second Claude Code CLI `opus[1m]` `xhigh` using that execution prompt.
4. Persist the resulting reread artifact in this audit directory.

## Governing Inputs

1. [PROGRAM.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/PROGRAM.md)
2. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/STATUS.md)
3. [lane-01-upstream-docs-freshness-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01-upstream-docs-freshness-task-spec.md)
4. [lane-01-upstream-docs-freshness.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01-upstream-docs-freshness.md)
5. [lane-01b-docs-gap-map-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01b-docs-gap-map-task-spec.md)
6. [lane-01b-docs-gap-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01b-docs-gap-map.md)
7. [SYNTHESIS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md)
8. [CLAUDE-REVIEW-COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CLAUDE-REVIEW-COMMANDS.md)
9. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)

## Output Artifacts

- `lane-01c-claude-opus-1m-prompt-writer-prompt.md`
- `lane-01c-claude-opus-1m-execution-prompt.md`
- `lane-01c-claude-opus-1m-independent-gap-reread.md`

## Required Final Reread Focus

The final Claude reread should independently answer:

1. Which upstream docs or doc sections are accurate enough to seed later docs-refresh work?
2. Which shipped or load-bearing surfaces are omitted, stale, flattened, or misleadingly summarized?
3. Which parts of the internal `lane-01` / `lane-01b` picture seem undercalled, overcalled, or inadequately supported?
4. What supplementation or patch-track strategy would let the repo build on the upstream docs instead of starting from scratch?
5. What remains genuinely uncertain even after the large-context reread?

## Required Constraint

The final Claude reread must not say, in effect, "lane-01 already proved X, therefore X." It must do its own reading and treat internal artifacts as inputs to challenge or refine, not as authoritative premises.
