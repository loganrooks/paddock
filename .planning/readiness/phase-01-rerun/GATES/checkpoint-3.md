# Checkpoint 3: Workflow / Harness Scope Audit

Status: in progress  
Last updated: 2026-04-15

## Objective

- map the relevant workflow and harness landscape before the deeper excellence audit fixes its scope
- determine what the real unit of analysis should be for the later tandem audit
- produce a reusable harness-map / onboarding surface for later audits and later harness work

## Primary Inputs

- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
- [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
- repo-local GSD runtime under [.codex/get-shit-done](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done)

## Scope Questions

- what are the real load-bearing layers of the current harness?
- where are the critical path surfaces for planning quality, research quality, execution quality, verification quality, and auditability?
- should the later deeper audit primarily reason about:
  - individual skills
  - workflow stages
  - runtime/harness layers
  - cross-layer seams
- what is broad but not load-bearing, and what looks narrow but actually carries a lot of downstream consequence?

## Exit Criteria

- the later deeper audit has an explicit, justified audit envelope
- if the initial GSD mapping fired the split trigger, the deeper GSD mapping sublanes and GSD-only synthesis are complete before the overall scope synthesis closes
- the result can explain why some surfaces deserve deep audit and others do not
- the package no longer relies on ambient assumptions about what the harness "really is"
- the mapping output is reusable as a later harness-orientation and audit-onboarding asset

## Quality Questions

- have we mapped the landscape honestly enough to avoid blind spots?
- have we avoided confusing "what is easiest to inspect" with "what most needs scrutiny"?
- would a later expert reader see a defensible reason for the chosen audit envelope?

## Commit Rule

- if the scoping artifact is independently reviewable, checkpoint it before launching the deeper tandem audit

## Reopen Triggers

- later deeper audit reveals that the scope audit missed a load-bearing harness surface
- later findings show the chosen audit unit was wrong or too narrow
