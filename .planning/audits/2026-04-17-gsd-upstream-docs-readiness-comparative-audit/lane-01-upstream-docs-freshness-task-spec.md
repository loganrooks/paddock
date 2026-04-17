# Lane 01: Upstream Docs Freshness Audit

## Purpose And Honest Scope Claim

Audit the upstream `get-shit-done` documentation corpus for freshness, internal coherence, and corroboration quality relative to the exact-version baseline and nearby change pressure.

This lane is not:

- a full architecture map
- a local-runtime comparison
- a verdict on whether the earlier readiness mapping was worthwhile

## Audit Stance

- gap exposure / completeness challenge
- anti-doc-triumphalism
- anti-changelog-only reasoning
- anti-false-ground-truth promotion

## Governing Inputs

1. [PROGRAM.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/PROGRAM.md)
2. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/STATUS.md)
3. `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
4. `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md`
5. `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-reference-points.md`
6. `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-baseline-schema.md`

## Candidate Surfaces

- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/README.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/ARCHITECTURE.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/AGENTS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/CONFIGURATION.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/COMMANDS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/CLI-TOOLS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/FEATURES.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/USER-GUIDE.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/context-monitor.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/workflow-discuss-mode.md`

## Corroboration / Drift Surfaces

- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/CHANGELOG.md`
- git history for `docs/` and `CHANGELOG.md`
- doc-relevant tests such as:
  - `tests/config-field-docs.test.cjs`
  - `tests/agent-required-reading-consistency.test.cjs`
  - `tests/docs-update.test.cjs`
  - `tests/command-count-sync.test.cjs` if present
  - any other tests you find that explicitly guard doc/runtime parity claims
- implementation files only where needed to verify contested doc claims

## Questions

1. Which upstream docs are genuinely load-bearing for understanding the harness rather than merely user-facing summaries?
2. Which important claims in the docs are corroborated by code/tests/changelog, and which are weak, stale, contradictory, or under-supported?
3. Which changelog items that matter to architecture, config, runtime materialization, or workflow semantics are missing from the docs corpus or only partially reflected there?
4. Are there internal doc contradictions or stale counts/categories that a later reader could mistake for settled truth?
5. Is the upstream docs corpus strong enough to serve as a mapping seed, and if so with what cautions?

## Output

Write:

- `lane-01-upstream-docs-freshness.md`

Required sections:

- `Question`
- `Corpus Read`
- `Freshness Findings`
- `Internal Doc Contradictions`
- `Changelog / Test Corroboration`
- `Docs Strong Enough For What?`
- `Unknowns`
- `What The Obligations Didn't Capture`
- `Follow-on Pressure For Later Lanes`
