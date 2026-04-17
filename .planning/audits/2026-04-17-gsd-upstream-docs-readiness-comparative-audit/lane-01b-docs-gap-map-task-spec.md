# Lane 01b: Upstream Docs Gap Map

## Purpose And Honest Scope Claim

Take the accepted `lane-01` freshness judgment one step further by explicitly separating:

- doc surfaces that are accurate enough to reuse as seed summaries
- shipped surfaces that the audited docs omit, underrepresent, or misleadingly summarize
- supplementation moves that would let a later pass build on the upstream docs instead of rebuilding from scratch

This lane is not:

- a docs rewrite pass
- a pull request implementation pass
- a wider readiness-program revision
- a complete runtime archaeology of every file in the upstream repo

## Audit Stance

- gap exposure with positive-trust discrimination
- anti-all-or-nothing doc judgment
- anti-false-completeness
- proposal-before-doc-mutation

## Governing Inputs

1. [PROGRAM.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/PROGRAM.md)
2. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/STATUS.md)
3. [lane-01-upstream-docs-freshness.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01-upstream-docs-freshness.md)
4. [SYNTHESIS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md)
5. `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
6. `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md`

## Candidate Surfaces

- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/README.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/ARCHITECTURE.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/AGENTS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/CONFIGURATION.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/COMMANDS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/CLI-TOOLS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/FEATURES.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/USER-GUIDE.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/README.md`

## Corroboration / Supplementation Surfaces

- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/CHANGELOG.md`
- selected command pages under `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/commands/gsd/`
- selected agent specs under `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/agents/`
- selected workflow files under `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/get-shit-done/workflows/`
- selected runtime/template/test files only where needed to prove a gap or validate a trustworthy summary surface

## Questions

1. Which doc pages or sections currently provide accurate, reusable summaries of the harness, and what are they accurate enough for?
2. Which important surfaces are excluded, omitted, stale, flattened, or misleadingly summarized in the audited docs corpus?
3. Can those gaps be named more explicitly by type, for example inventory omission, stale count, stale subcommand signature, hidden advanced surface, runtime default mismatch, or architecture-summary flattening?
4. What ranked supplementation strategy would let later work extend the docs into a fresher and more complete map rather than starting from zero?
5. If a later documentation refresh or upstream PR were attempted, what patch bundles or workstreams would make sense?

## Output

Write:

- `lane-01b-docs-gap-map.md`

Required sections:

- `Question`
- `Positive Trust Surfaces`
- `Explicit Gap / Exclusion Inventory`
- `Gap Taxonomy`
- `What The Docs Currently Support Well`
- `What A Supplementation Pass Would Need To Add`
- `Candidate Patch Bundles Or PR Tracks`
- `Unknowns / Review Requirements`
- `How This Requalifies The Upstream Docs Seed`
