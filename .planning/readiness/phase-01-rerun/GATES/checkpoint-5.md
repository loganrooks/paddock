# Checkpoint 5: Conditional Harness / GSD Follow-Through

Status: in progress  
Last updated: 2026-04-15

## Objective

- execute the reactivated harness follow-through that Checkpoint 4 proved is warranted before rerun-readiness verification
- preserve the already-completed Track A/B/C work, but do not let that partial bundle stand in for the full checkpoint
- keep the checkpoint centered on rerun-blocking harness quality, not on omnibus hardening

## Governing inputs

- [AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md)
- [AUDITS/checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md)
- [AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md)

## Activation Criteria

- Checkpoint 4 concluded that:
  - the phase-critical runtime-authoritative worker surface still carries stale doctrine
  - review / closure pressure is still too soft for the rerun standard
  - launch/model-truth capture remains too implicit for later audit
  - workflow-chain follow-through is still needed on steering translation, research adequacy, permissive closure, and clean-versus-debt-carrying completion

## Likely Targets

- phase-critical registered `.toml` worker prompts under [.codex/agents](/home/rookslog/workspace/projects/prix-guesser/.codex/agents)
- repo-local GSD workflow / review / completion surfaces under [.codex/get-shit-done](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done), especially:
  - [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md)
  - [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md)
  - [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md)
  - [.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md)
- repo-local overlay under `tooling/portable-gsd/overlay/` only where the bounded follow-through truly requires it
- rerun-critical wrappers under [.codex/skills](/home/rookslog/workspace/projects/prix-guesser/.codex/skills) only as a secondary alignment surface after workflow changes land
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md) only where a doc-level policy needs explicit machinery-backed protocol

## Bounded Scope

- required:
  - align the phase-critical runtime-authoritative `.toml` worker prompts with the repo’s actual instruction and skill surfaces
  - tighten review / closure-pressure harness surfaces so lone strong criticism and debt-carrying completion are handled more explicitly
  - define the durable rule for launch/model-truth capture on doctrine-sensitive worker launches
  - add workflow-chain follow-through on steering-to-plan traceability, research adequacy/disposition, doctrine-sensitive closure pressure, and clean-versus-debt-carrying completion
  - align rerun-critical wrappers where the invocation surface would otherwise lag the corrected workflow doctrine
- explicitly deferred unless the active work reaches those surfaces directly:
  - broad install pinning
  - archival provenance replacement
  - full path-portability hardening
  - broader branch/worktree redesign

## Exit Criteria

- the phase-critical worker authority surface is aligned for the roles the rerun will actually exercise
- review/closure changes preserve lone strong criticism and distinguish clean completion from debt-carrying completion where rerun quality depends on that distinction
- launch/model-truth capture now has a clear, reviewable rule for doctrine-sensitive worker launches
- workflow-chain follow-through has addressed the Checkpoint 4 seams on `discuss-phase`, `research-phase`, `plan-phase`, and `execute-phase`
- rerun-critical wrappers no longer lag the corrected workflow doctrine where they are the first invoked surface
- any broader portability/provenance hardening is either completed because the checkpoint touched those surfaces directly, or explicitly deferred rather than silently expanding scope

## Quality Questions

- are these real harness defects with clean ownership stories?
- are we moving only the controls that genuinely improve reliability?
- are we keeping broader hardening explicit instead of smuggling it into the pre-rerun checkpoint?
- are we carrying forward the accepted Checkpoint 4 workflow findings rather than silently dropping them because the initial Checkpoint 5 launch spec was narrower?

## Review Note

- the existing Checkpoint 5 internal and cross-vendor reviews apply only to the pre-reactivation partial bundle
- closure of the reactivated checkpoint requires fresh internal and cross-vendor review against the widened scope

## Commit Rule

- keep harness changes separate from governance wording unless inseparable
