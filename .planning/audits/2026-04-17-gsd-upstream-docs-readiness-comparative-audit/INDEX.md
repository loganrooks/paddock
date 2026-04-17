# GSD Upstream Docs / Readiness Comparative Audit

This audit session exists to compare newly surfaced upstream GSD documentation against the repo's existing readiness-era harness mapping and to decide whether the current intervention program should be reseeded, revised, or split.

- [g:c:i] This repo uses regular repo-local GSD for Codex, with the live runtime anchored in `.codex/get-shit-done`, and it explicitly forbids Reflect-specific runtime/config paths. Sources: `AGENTS.md:5-9`.
- [e:c:i] The live readiness boundary is still `Checkpoint 5`, and the current active question is still bounded harness follow-through before rerun-readiness verification. Sources: `.planning/readiness/phase-01-rerun/STATUS.md:7-10,28-33`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:8-11,59-63`.
- [g:c+i] This audit is not a minimal freshness check. It is a gap-exposure / completeness-challenge lane that must stay open to revising the program, adding subphases, or branching into narrower follow-on inquiry if the evidence warrants it. Sources: `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:9-10,87-100,132-140`; `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md:16-26,91-99`.

## Read Order

1. [PROGRAM.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/PROGRAM.md)
2. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/STATUS.md)
3. [gsd-upstream-docs-readiness-comparative-audit-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/gsd-upstream-docs-readiness-comparative-audit-task-spec.md)
4. lane specs:
   - [lane-01-upstream-docs-freshness-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01-upstream-docs-freshness-task-spec.md)
   - [lane-01b-docs-gap-map-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01b-docs-gap-map-task-spec.md)
   - [lane-01c-claude-opus-1m-independent-reread-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01c-claude-opus-1m-independent-reread-task-spec.md)
   - [lane-02-docs-vs-readiness-crosswalk-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-02-docs-vs-readiness-crosswalk-task-spec.md)
   - [lane-03-reseed-judgment-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-03-reseed-judgment-task-spec.md)
   - [lane-06-program-revision-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-06-program-revision-task-spec.md)
5. [LAUNCH-LEDGER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/LAUNCH-LEDGER.md)
6. support artifacts:
   - [launch-support-01-external-claude-cli-persistence-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/launch-support-01-external-claude-cli-persistence-research.md)
   - [support-01-claude-cli-session-persistence-forensics.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/support-01-claude-cli-session-persistence-forensics.md)
7. [SYNTHESIS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md)

## Source-Of-Truth Hierarchy

- stable sequence, expansion policy, and stop conditions: `PROGRAM.md`
- live mutable state: `STATUS.md`
- governing orchestration obligations and output contract: `gsd-upstream-docs-readiness-comparative-audit-task-spec.md`
- lane-local read sets and questions: `lane-0*-*.md`
- requested-versus-effective launch truth and audit dispatch history: `LAUNCH-LEDGER.md`
- external Claude CLI persistence / recovery note: `support-01-claude-cli-session-persistence-forensics.md`
- lane outputs and later synthesis: this session directory as they are added
- accepted cross-lane synthesis: `SYNTHESIS.md`
- current docs-gap qualification branch: `lane-01b-docs-gap-map-task-spec.md`
- current cross-vendor large-context reread branch: `lane-01c-claude-opus-1m-independent-reread-task-spec.md`
- next-branch planning surface: `lane-06-program-revision-task-spec.md`

## Planned Outputs

- `lane-01-upstream-docs-freshness.md`
- `lane-01b-docs-gap-map.md`
- `lane-01c-claude-opus-1m-execution-prompt.md`
- `lane-01c-claude-opus-1m-independent-gap-reread.md`
- `support-01-claude-cli-session-persistence-forensics.md`
- `lane-02-docs-vs-readiness-crosswalk.md`
- `lane-03-reseed-judgment.md`
- `SYNTHESIS.md`
- `lane-06-program-revision-proposal.md`
- optional expansion-lane specs and outputs if the current program proves under-scoped
- comparative synthesis and readiness-program consequence artifact

## Session Rule

- [g:c:i] Treat this directory as an audit trail, not canon. If its conclusions should alter readiness sequencing or checkpoint scope, the later change must be made explicitly in the readiness package after synthesis and review rather than by silently treating this session as live doctrine. Sources: `.planning/AGENTS.md:17-31`; `.planning/readiness/phase-01-rerun/AGENTS.md:10-16,33-40`.
