# Claim Types

This file is the deeper reference for terse claim markers used in load-bearing planning/process artifacts.

Here, `load-bearing planning/process artifacts` means artifacts that can materially steer:

- canon
- phase execution
- verification or validation
- workflow or process policy

Use it together with:

- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [review-trail-framework.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md)

## Compact Syntax

Preferred inline forms:

- `[t:b]`
- `[t:s:b]`

For load-bearing claims, prefer `[t:s:b]`.

Use `[t:b]` only as shorthand when the omitted support mode is obvious from nearby structure or not important to the reading.

Where:

- `t` = claim type
- `s` = support mode
- `b` = source-basis

Examples:

- `[e:c:i]`
- `[e:c:d]`
- `[e:c+r:i]`
- `[a:r:i]`
- `[p:r:i+d]`

## Claim Type Codes

- `e` evidenced
  Claim is supported strongly enough to rely on, given the cited or described basis.
- `d` decided
  Claim records an explicit repo decision that should be treated as chosen unless reopened.
- `a` assumed
  Claim is a working premise or load-bearing assumption that is not yet fully earned.
- `o` open
  Claim marks a live unresolved question, comparison, or uncertainty.
- `p` projected
  Claim forecasts a likely future state, implication, or pressure.
- `s` stipulated
  Claim sets a temporary or local rule for the current artifact, pass, or workflow.
- `g` governing
  Claim expresses higher-order doctrine or instruction that should constrain later interpretation.

## Support Mode Codes

- `c` cited
  Directly grounded in named artifacts or external sources used in the current work.
- `r` reasoned
  Inference, synthesis, or judgment is doing real work beyond direct citation.
- `b` bare
  Weakly supported or merely asserted. Use sparingly and usually as a sign the claim needs strengthening.

If more than one support mode materially matters, join the real support codes with `+`:

- `c+r`

Interpretation rule:

- `c+r` means the claim is not just quoted from a source; the current artifact is also doing non-trivial synthesis or inference
- use `c+r` when both are materially true, not just because every cited claim involves a little interpretation

## Source-Basis Codes

- `i` internal
  Grounded in repo-local canon, planning artifacts, audit artifacts, or other repo state.
- `d` external-direct
  Grounded in outside sources directly engaged in the current artifact.
- `t` external-traceable
  Grounded through repo-local artifacts whose relevant support can be traced outward, but the current artifact did not directly re-engage those outside sources.

If more than one basis materially matters, join the real basis codes with `+`:

- `i+d`
- `i+t`
- `d+t`
- `i+d+t`

Interpretation rule:

- the `+` means more than one grounding origin is materially doing work
- read the combined basis as cumulative, not averaged or blurred
- if one basis is clearly dominant, explain that in prose rather than relying on the marker alone

## Citation Expectations

Use citations to make the marker auditable, not decorative.

### Internal grounding

For `[*:c:i]` claims, cite the direct repo-local source next to the claim.

- prefer the exact file and line numbers carrying the support
- use clickable file links where the renderer supports them
- if several internal sources materially support the claim, cite the main one inline and add the others only if they change interpretation

Example:

- `[e:c:i]` The current repo diagnosis still ranks lifecycle carry-forward as weaker than doctrine definition ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:1)).

### External-direct grounding

For `[*:c:d]` claims:

- use markdown footnotes inline where the claim is made
- maintain an `External Works Cited` section near the end of the artifact
- each footnote should identify the external source precisely enough that a later reader can re-open it

Example:

- `[e:c:d]` GitHub rulesets support branch-level enforcement of reviews and status checks.[^gh-rulesets]

Then later:

- `## External Works Cited`
- `[^gh-rulesets]: GitHub Docs, "About rulesets", URL`

### External-traceable grounding

For `[*:c:t]` claims:

- cite the repo-local artifact being relied on
- identify the traced external source in prose or footnote if that trace matters to interpretation
- do not write the claim as if the current artifact directly re-checked the outside source when it did not

### Mixed basis grounding

For `[*:...:i+d]`, `[*:...:i+t]`, and similar combinations:

- make the internal anchor visible
- make the external anchor visible
- if one side is only supportive and the other is load-bearing, say so in prose

The goal is not maximum citation density. The goal is that a later reader can tell:

- what kind of claim is being made
- where the support actually comes from
- whether the current artifact directly engaged the outside source or only inherited it

## How To Read The Marker

- Type tells you what kind of claim you are looking at.
- Support tells you how much inference versus direct citation is doing the work.
- Basis tells you where the grounding lives.

The marker does not guarantee truth. It exposes epistemic posture.

## Practical Reading Rules

- Lean most confidently on `e`, `d`, and `g`, but still check support and basis.
- Treat `a`, `p`, and `o` as materially less settled, even when they are useful.
- Be careful when a claim sounds strong but is only `[*:r:i]`; it may be a good repo judgment, but not externally validated.
- Be careful when a claim uses basis `t`; it is still one step removed from direct engagement.
- Be careful with `[*:...:i+d]` or similar combinations; they often mean the repo judgment is partly externally strengthened, not fully externally settled.
- When a claim moves from repo-state diagnosis toward broader prescription, basis matters more, not less.

## When To Mark Claims

Do not mark every sentence.

Do mark:

- load-bearing conclusions
- branch rankings
- prescriptive governance or workflow recommendations
- claims likely to be mistaken as externally settled
- claims whose status affects whether later work should treat them as doctrine, open terrain, or hypothesis

## Progressive Disclosure

Use terse markers inline.

Put fuller explanation in the surrounding prose only when the reader could otherwise misread:

- what kind of claim is being made
- where the support actually comes from
- how much confidence the current artifact is asking for
