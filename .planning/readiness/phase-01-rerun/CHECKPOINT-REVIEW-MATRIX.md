# Checkpoint Review Matrix

This file defines what kind of review each readiness checkpoint should receive before closure.

The goal is not to force identical heavyweight review at every checkpoint.
The goal is to make review expectations explicit and proportionate.

## Review Modes

- `local-reread`
  Main-thread or orchestrator reread against the gate's quality questions and exit criteria.
- `internal-verification-agent`
  A repo-local bounded reviewer lane, normally `gpt-5.4` with `high` reasoning.
- `cross-vendor-reread`
  Independent reread by an Anthropic Claude lane when available.
  Current policy preference from the model-assignment research is:
  - routine strong external audit: `claude-sonnet-4.6`
  - high-stakes doctrine / architecture / canon-sensitive planning / harness ownership / stubborn-debug escalation: `claude-opus-4.6`
- `implementation-follow-through`
  A fix or patch pass triggered by review findings.

## Independence Rule

- Major checkpoint closure requires an independent reviewer.
- The lane that authored the artifact under review may participate in revision, but it must not be the only lane certifying closure.
- For authored-by-subagent work, orchestrator reread can count as the independent reviewer if it is explicit and recorded.
- For authored-by-orchestrator work, use at least one separate verification lane before major-checkpoint closure.
- Cross-vendor review does not replace the independence rule; it is an additional stronger mode when required or preferred.

## By Checkpoint

### Checkpoint 0: Governance Citation Bundle

- default review mode:
  - `local-reread`
  - `internal-verification-agent`
- cross-vendor default:
  - not required
- external model choice if escalated:
  - start with `claude-sonnet-4.6`
  - use `claude-opus-4.6` only if the problem has clearly stopped being mostly mechanical
- why:
  - this is mostly citation/marker repair and epistemic presentation cleanup
  - the right test is whether the bundle is concretely auditable, not whether a second vendor agrees with the prose
- escalate to cross-vendor only if:
  - the repaired bundle still carries doctrine-sensitive ambiguity
  - or the reread shows the issue is no longer mainly mechanical

### Checkpoint 1: Governance-Doc Normalization Audit

- default review mode:
  - `internal-verification-agent`
- cross-vendor default:
  - strongly preferred if the audit materially changes standing governance or harness doctrine
- external model choice:
  - default `claude-sonnet-4.6`
  - escalate to `claude-opus-4.6` if the audit is reshaping repo doctrine in a way likely to survive for a long time
- why:
  - this checkpoint can reshape the repo's operating doctrine
  - that is exactly where shallow internal agreement is dangerous

### Checkpoint 2: Governance-Doc Normalization Patch

- default review mode:
  - `internal-verification-agent`
- cross-vendor default:
  - conditional
- external model choice:
  - `claude-sonnet-4.6` by default
  - `claude-opus-4.6` if the patch materially changes doctrine or feels deceptively tidy after removing a lot of specificity
- use cross-vendor if:
  - the patch materially changes doctrine
  - the patch feels deceptively "clean" after removing a lot of specificity
  - the patch touches load-bearing distinctions from `05-gap-closure`

### Checkpoint 3: Conditional Harness / GSD Follow-Through

- default review mode:
  - `internal-verification-agent`
- cross-vendor default:
  - strongly preferred
- external model choice:
  - prefer `claude-opus-4.6`
- why:
  - machinery ownership mistakes can produce recurring silent failures
  - this is one of the highest-leverage places for independent scrutiny

### Checkpoint 4: Rerun-Readiness Verification

- default review mode:
  - `internal-verification-agent`
- cross-vendor default:
  - required when the verdict depends on doctrine-sensitive judgment rather than only mechanical closure
- external model choice:
  - default `claude-sonnet-4.6`
  - escalate to `claude-opus-4.6` if rerun-readiness judgment is carrying major doctrine or long-arc interpretive weight
- why:
  - this checkpoint decides whether the repo is ready to rerun Phase 01
  - false confidence here is expensive

### Checkpoint 5: Fresh Phase 01 Rerun

- discuss/context/planning bundle:
  - default review mode: `internal-verification-agent`
- fresh Phase 01 plan:
  - default review mode: `internal-verification-agent`
  - cross-vendor default: conditional
- external model choice:
  - `claude-sonnet-4.6` for routine doctrine-sensitive plan reread
  - `claude-opus-4.6` if the plan is highly contested, architecture-setting, or about to become execution-approved despite major interpretive load
- use cross-vendor if:
  - the fresh plan remains doctrine-sensitive or contested after internal review
  - the rerun appears to be recreating old asymmetries
  - the plan is about to become execution-approved despite real interpretive load

## Escalation Logic

Use the lightest sufficient review.

Escalate upward when:

- doctrine, harness ownership, or long-arc carry-forward is being shaped
- the artifact is likely to become a standing reference surface
- internal reread keeps finding the same kind of blind spot
- the cost of false confidence is high relative to the review cost

Do not escalate just because a checkpoint feels important in the abstract.

## Availability Rule

If a cross-vendor lane is not available:

- record that explicitly in the review artifact
- use an internal reread or verification agent instead
- do not speak as if same-vendor reread provides the same independence

If Anthropic availability is present but model tier choice is unclear:

- use `claude-sonnet-4.6` as the routine default
- use `claude-opus-4.6` when the checkpoint is shaping doctrine, harness ownership, or high-cost go/no-go judgment
