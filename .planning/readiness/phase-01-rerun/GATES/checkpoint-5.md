# Checkpoint 5: Conditional Harness / GSD Follow-Through

Status: in progress  
Last updated: 2026-04-15

## Objective

- execute only the bounded harness follow-through that Checkpoint 4 proved is warranted before rerun-readiness verification
- keep the checkpoint centered on rerun-blocking harness quality, not on omnibus hardening

## Activation Criteria

- Checkpoint 4 concluded that:
  - the phase-critical runtime-authoritative worker surface still carries stale doctrine
  - review / closure pressure is still too soft for the rerun standard
  - launch/model-truth capture remains too implicit for later audit

## Likely Targets

- phase-critical registered `.toml` worker prompts under [.codex/agents](/home/rookslog/workspace/projects/prix-guesser/.codex/agents)
- repo-local GSD workflow / review / completion surfaces under [.codex/get-shit-done](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done)
- repo-local overlay under `tooling/portable-gsd/overlay/` only where the bounded follow-through truly requires it
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md) only where a doc-level policy needs explicit machinery-backed protocol

## Bounded Scope

- required:
  - align the phase-critical runtime-authoritative `.toml` worker prompts with the repo’s actual instruction and skill surfaces
  - tighten review / closure-pressure harness surfaces so lone strong criticism and debt-carrying completion are handled more explicitly
  - define the durable rule for launch/model-truth capture on doctrine-sensitive worker launches
- explicitly deferred unless the active work reaches those surfaces directly:
  - broad install pinning
  - archival provenance replacement
  - full path-portability hardening
  - broader branch/worktree redesign

## Exit Criteria

- the phase-critical worker authority surface is aligned for the roles the rerun will actually exercise
- review/closure changes preserve lone strong criticism and distinguish clean completion from debt-carrying completion where rerun quality depends on that distinction
- launch/model-truth capture now has a clear, reviewable rule for doctrine-sensitive worker launches
- any broader portability/provenance hardening is either completed because the checkpoint touched those surfaces directly, or explicitly deferred rather than silently expanding scope

## Quality Questions

- are these real harness defects with clean ownership stories?
- are we moving only the controls that genuinely improve reliability?
- are we keeping broader hardening explicit instead of smuggling it into the pre-rerun checkpoint?

## Commit Rule

- keep harness changes separate from governance wording unless inseparable
