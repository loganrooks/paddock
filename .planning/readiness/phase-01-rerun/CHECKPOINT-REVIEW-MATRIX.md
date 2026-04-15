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
  Independent reread by a non-OpenAI external lane when available.
  Current policy preference is:
  - routine strong external audit: Sonnet
  - high-stakes doctrine / architecture / stubborn-debug escalation: Opus
- `implementation-follow-through`
  A fix or patch pass triggered by review findings.

## By Checkpoint

### Checkpoint 0: Governance Citation Bundle

- default review mode:
  - `local-reread`
  - `internal-verification-agent`
- cross-vendor default:
  - not required
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
- why:
  - this checkpoint can reshape the repo's operating doctrine
  - that is exactly where shallow internal agreement is dangerous

### Checkpoint 2: Governance-Doc Normalization Patch

- default review mode:
  - `internal-verification-agent`
- cross-vendor default:
  - conditional
- use cross-vendor if:
  - the patch materially changes doctrine
  - the patch feels deceptively "clean" after removing a lot of specificity
  - the patch touches load-bearing distinctions from `05-gap-closure`

### Checkpoint 3: Conditional Harness / GSD Follow-Through

- default review mode:
  - `internal-verification-agent`
- cross-vendor default:
  - strongly preferred
- why:
  - machinery ownership mistakes can produce recurring silent failures
  - this is one of the highest-leverage places for independent scrutiny

### Checkpoint 4: Rerun-Readiness Verification

- default review mode:
  - `internal-verification-agent`
- cross-vendor default:
  - required when the verdict depends on doctrine-sensitive judgment rather than only mechanical closure
- why:
  - this checkpoint decides whether the repo is ready to rerun Phase 01
  - false confidence here is expensive

### Checkpoint 5: Fresh Phase 01 Rerun

- discuss/context/planning bundle:
  - default review mode: `internal-verification-agent`
- fresh Phase 01 plan:
  - default review mode: `internal-verification-agent`
  - cross-vendor default: conditional
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
