# Checkpoint Review Template

Use this for explicit readiness checkpoint reviews.

## Header

- checkpoint:
- artifact(s) under review:
- review mode:
  - `local-reread`
  - `internal-verification-agent`
  - `cross-vendor-reread`
- authoring lane:
- reviewer:
- model / reasoning or vendor:
- baseline commit / artifact snapshot:
- independence relationship:
  - `independent`
  - `same-lane`
  - `cross-vendor`

## Review Questions

- What is this review trying to falsify?
- Which gate exit criteria are being tested?
- Which quality questions are being tested?
- Which regressions are most relevant here?

## Findings

List findings in severity order with concrete file references where possible.

## Gap Classification

For each material problem, classify the required response as one of:

- `accept`
  No material gap found.
- `revise-current`
  Fix inside the current checkpoint, then rereview.
- `reopen-current`
  The checkpoint is not ready to close; more than a narrow fix is required.
- `reactivate-earlier`
  The problem actually belongs to an earlier checkpoint or upstream doctrine/harness layer.
- `escalate-cross-vendor`
  Internal review is insufficient; independent external reread should occur if available.
- `strategic-opportunity`
  Not a blocker, but a meaningful short- or long-term quality opportunity should be tracked explicitly.
- `user-consult`
  The result changes the sequence or exposes a real strategic choice.
- `defer-nonblocking`
  Real issue, but not a readiness blocker now.

## Verdict

- status:
  - `blocked`
  - `provisional`
  - `strong`
  - `ready-to-carry-forward`
- explanation:

## Required Next Action

- exact next step:
- owner / lane:
- commit implication:
  - no commit yet
  - fix then commit
  - checkpoint now

## Independence Note

- Does this review satisfy the checkpoint's independent-review requirement?
- Was a cross-vendor lane available?
- If not used, why not?
- If used, what did independence add?
