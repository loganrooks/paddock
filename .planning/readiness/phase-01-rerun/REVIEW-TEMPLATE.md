# Checkpoint Review Template

Use this for explicit readiness checkpoint reviews.

## Review Stance

- Review against a high bar, not a minimal pass bar.
- Be firm, clear, and specific when the work is weak, thin, or settling for adequacy.
- Do not be rude, performatively harsh, or arbitrarily negative.
- Criticism must be justified in terms of a higher standard of work:
  - rigor
  - auditability
  - architectural soundness
  - future viability
  - quality of judgment
- Do not treat `technically passes` or `mostly fine` as sufficient if a stronger artifact was reasonably achievable.
- Try seriously to falsify closure-readiness before declaring an artifact strong.

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
  - for `internal-verification-agent`, default is `gpt-5.4 high`
  - for `cross-vendor-reread`, name the exact Claude model used, normally `claude-sonnet-4.6` or `claude-opus-4.6`
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
- What is the strongest justified criticism of this artifact?
- What is merely adequate here but should be stronger?
- What would fail later stringent audit by strong engineers, designers, or researchers?
- What meaningful quality opportunity is being left unused?

## Findings

List findings in severity order with concrete file references where possible.

- Do not soften a finding just to sound polite.
- Do not inflate a finding just to sound demanding.
- Tie every material criticism to a clear standard the artifact is not yet meeting.

## What Is Already Strong

State what is genuinely strong so the later fix pass preserves it rather than regressing it.

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
  Explain whether the artifact is merely acceptable, genuinely strong, or still too thin to carry forward safely.

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
- If cross-vendor was available, which Claude lane was appropriate here and why?
- If not used, why not?
- If used, what did independence add?
