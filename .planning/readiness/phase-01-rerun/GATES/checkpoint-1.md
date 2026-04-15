# Checkpoint 1: Governance-Doc Normalization Audit

Status: not started  
Last updated: 2026-04-15

## Objective

- audit the standing governance docs for abstraction quality, ownership, duplication, and case-specific residue

## Primary Inputs

- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
- [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)

## Known Triggers

- broad conduct rules may be trapped in overly narrow sections
- root `AGENTS.md` may still contain audit-era residue where general rules should dominate
- policy may be duplicated at inconsistent levels of abstraction across governance docs

## Exit Criteria

- each rule lives in the document whose scope actually justifies it
- rules are stated at the right level of generality
- examples remain examples rather than replacing the governing rule
- the audit clearly distinguishes doc-local cleanup from deeper harness ownership problems

## Quality Questions

- if recent audit history vanished from memory, would these docs still read as coherent doctrine?
- are the docs slim and stable enough to guide future agents without carrying lane sediment?

## Commit Rule

- if the audit artifact is independently reviewable, checkpoint it before the patch pass

## Reopen Triggers

- discovery that important standing rules really belong in machinery rather than docs
- later patch pass showing the audit missed major duplication or ownership drift
