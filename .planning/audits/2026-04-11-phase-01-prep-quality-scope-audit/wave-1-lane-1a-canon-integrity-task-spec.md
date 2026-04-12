---
date: 2026-04-11
wave: 1
lane: 1A
audit_subject: claim_integrity
audit_orientation: investigatory
audit_delegation: self
auditor_model: claude-opus-4-6
agent_type: gsdr-auditor
scope: "Re-verify the 2026-04-08 predecessor audit's claims about the canon (PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md, STATE.md) against the actual current canon. Apply the 'three legitimate outcomes' framing to each predecessor recommendation. Investigate whether the canon's apparent coherence is earned convergence or repeated assumption — the central claim under audit."
triggered_by: "wave-1 parallel dispatch from phase-01-prep-quality-scope-audit-2 orchestrator (Claude Opus 4.6, claude-code session)"
parent_task_spec: phase-01-prep-quality-scope-audit-2-task-spec.md
predecessor_audits:
  - .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md
  - .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md
  - .planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md
ground_rules: "core+investigatory+claim_integrity+chain+framework-invisibility"
tags:
  - wave-1
  - lane-1a
  - canon-integrity
  - claim-integrity
  - investigatory
  - opus
output_files:
  - wave-1-lane-1a-canon-integrity.md
---

# Wave 1 / Lane 1A — Canon Claim Integrity (Opus)

**You are running as gsdr-auditor on Claude Opus 4.6.**

## Lane Position In The Audit

This lane is one of three parallel agents in Wave 1 of a planned wave-structured audit. The full audit (`phase-01-prep-quality-scope-audit-2-task-spec.md`) was originally drafted as a single-agent dispatch but the orchestrator restructured it into a wave plan after the user pointed out that auditing whether prix-guesser's narrow initiative inherits the f1-modeling iteration discipline using a single one-shot agent would be methodologically ironic. The audit itself now models the discipline it is evaluating.

The three Wave 1 lanes are:

- **Lane 1A (this lane, Opus)** — canon claim integrity. Your job.
- **Lane 1B (Opus, gsdr-auditor)** — methodological inheritance comparison between prix-guesser's and f1-modeling's vision-alignment PLAN.md and RESEARCH-PRINCIPLES.md files.
- **Lane 1C (Opus, general-purpose with WebSearch/WebFetch/Context7)** — external gap research; identifying alternatives the prix-guesser research did not consider.

You are running in parallel with 1B and 1C. **You do not need to do their work.** You should not duplicate their reading. Your output will be consumed by a Wave 3 synthesis pass (and possibly a Wave 2 follow-up if Review Gate 1 makes it necessary).

## Lane Fit Assessment

This lane is **claim_integrity × investigatory × self** because the central question — "is the canon really aligned, or only apparently aligned?" — is the kind of question that closes wrong if forced to a yes/no verdict prematurely. Each predecessor audit recommendation is a claim about what *should* be in the canon; each canon document is evidence about what *is* in it. The integrity check is whether the gap between recommendation and current state is principled, lazy, or unaddressed.

The three legitimate outcomes for each predecessor recommendation (per the parent task spec):

1. **The predecessor was right and the canon was revised accordingly.** Verify the revision actually happened and was responsive to the predecessor's substance, not just nominally adopted.
2. **The predecessor was right but the canon was NOT revised.** Surface this as a gap, qualified by whether the recommendation is load-bearing for current Phase 01 readiness or peripheral.
3. **The predecessor was wrong, OR right in spirit but wrong in shape, OR the project deliberately and correctly chose not to adopt the recommendation for principled reasons.** This is the outcome most likely to be missed by chain integrity applied naively. Some predecessor recommendations may be appropriate to a serious public product and inappropriate to a private friends-only fan game; some may be correct in substance but wrong in the specific implementation the predecessor proposed.

**For each recommendation you check, ask both "was it adopted?" AND "should it have been adopted in the form proposed?"** Treat the predecessor's recommendations as contestable claims, not as authoritative requirements.

---

## Epistemic Ground Rules

### Core Rules (every audit)

1. **Every factual claim cites file:line and quotes the relevant passage.** Do not assert what a file contains without opening it. Do not summarize without quoting. Bad: "PROJECT.md has been updated to address Lane 3." Good: "PROJECT.md line 5 states 'Prix Guesser is an unofficial, private-only F1 fan game project...' This 'private-only' framing was already present before the 2026-04-08 audit; verify by reading the file's modification history if needed. The current PROJECT.md does not contain the phrase 'hosted game that happens to be built by a developer' that the predecessor audit Lane 3 (Opus) recommended. Whether the absence is principled or evasive depends on whether the project has internalized the 'real stakeholder is the friend, not the developer' framing in some other form."

2. **For every finding, BEFORE writing it, ask "What would disconfirm this?" and CHECK.** Not rhetorical — actually look for counter-evidence. Example: if you are about to claim "the canon is internally consistent on the 'private-only' posture," first search PROJECT.md, ROADMAP.md, REQUIREMENTS.md, and LONG-ARC.md for any passage that softens, qualifies, or contradicts the private-only stance. If you find one, the consistency claim weakens. If you don't, name what you searched for and why a contradiction would have been visible there if it existed.

3. **Distinguish what you measured from what the measure captures.** Every measurement is a proxy. Name the gap. Example: "I checked whether 'watchability' appears in PROJECT.md, ROADMAP.md, and LONG-ARC.md. It appears 12 times. Frequency of mention is not depth of definition. The predecessor audit's Lane 2 finding was that 'watchability is load-bearing but undefined' — frequency of mention does not refute that finding; only operational definition would. I then searched for an operational definition (e.g., 'watchability means X measurable thing') and found / did not find it."

4. **Rule 4 (escape hatch): What did you encounter that these ground rules didn't prepare you for?** Address in the mandatory **What the Obligations Didn't Capture** section at the end of your output. If "nothing," consider whether the rules shaped your attention so thoroughly that you didn't notice what they excluded.

5. **Rule 5 (frame-reflexivity): Did the framing shape what you found?** For investigatory orientation, Rule 5 is a **full section**.

   *Specific grounding questions (copy verbatim into your output):*
   1. *"If this lane had been classified as a different subject (e.g., `requirements_review` instead of `claim_integrity`, or `artifact_analysis` instead of `claim_integrity`), what would it have looked for that I didn't?"*
   2. *"If this lane had been classified with a different orientation (e.g., `standard` instead of `investigatory`), what would it have held open that I closed?"*
   3. *"What about the current classification shapes what I am prepared to notice and what I am not? Name one concrete example."*

   **Anti-performativity warning.** An empty Rule 5 ("I considered my biases" without a concrete consequence visible in the findings) means Rule 5 has been performed, not engaged with. Refuse compliance theater.

### Orientation Obligations (investigatory)

Phrasing is load-bearing — do not paraphrase.

- **I1 — Start from the discrepancy, not a theory.** The discrepancy here: the 2026-04-08 audit said the canon needs revision; the narrow initiative says the canon is already aligned. These cannot both be fully true — but the resolution may be more nuanced than either claim. Name the discrepancy and what makes the comparison points the comparison points.

- **I2 — Let the investigation guide artifact selection.** Don't mandate which artifacts to read in advance. The "Suggested Starting Orientation" below is a starting list, not a closed read list. If the evidence asks you to read something not on the list, read it.

- **I3 — Present competing explanations.** For each finding, offer at least two interpretations. "The canon doesn't include DEPLOY-01..05" could mean (a) the project missed the predecessor's recommendation, (b) the project deliberately excluded these because they're inappropriate for the friends-on-couch use case, or (c) the project addressed the underlying concern through a different mechanism the predecessor didn't anticipate. Don't collapse to one without ruling out the alternatives.

- **I4 — Name the position of the investigation.** You are running as Claude Opus 4.6, dispatched by an orchestrator that is also Opus, in a session where the user has stated a stance ("not convinced by momentum/time-pressure arguments; consider deployment/distribution/adoption broadly"). Name how that affects what you are prepared to notice. A separate audit by Codex GPT-5.4 would notice differently. An adversarial human reviewer would notice differently.

- **Show what remains unknown.** Explicit unknowns are findings — they map the edge of the investigation. Do not close on a story that the evidence does not fully support.

- **Show how you navigated any tensions between obligations.** If clean resolutions emerge, that is a red flag — read the parent task spec's Composition Principle.

### Subject Obligations (claim_integrity)

> *"Verify claims against citations; surface untyped load-bearing assumptions; trace dependency chains."*

For this lane, the operative claims are:

1. **The narrow initiative's claim** that "the broader product posture is already relatively well-aligned across PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md" (`.planning/initiatives/vision-alignment-2026-04/README.md` lines 24–31). Verify each component of this claim by reading the canon docs themselves.

2. **The 2026-04-08 predecessor audit's claims** about specific gaps in the canon. The predecessor's SYNTHESIS.md identified at least:
   - Lane 1: Phase 1 plan structural gaps (G1 venue identity ambiguity, G2 PackSourceSchema reference shape, G3 Plan 01-03 verification weakness, G4 stable diagnostic codes)
   - Lane 2: design/UX critical gap (no visual identity, watchability undefined, host/controller distinction, recommended Phase 3.5 inserted phase)
   - Lane 3: distribution critical gap (no deployment mechanism, DEPLOY-01..05 proposed, Colyseus-vs-PartyKit as distribution decision, Supabase wrong-fit, "hosted game built by developer" framing)
   - Lane 4: architectural seam gaps (hierarchical answer targets, branded PlayerId, content hash, schema-driven judging, deployment-agnostic room core, three-milestone arc)
   - Strategic Q1-Q6: design phase formality, F1-GeoGuessr-vs-Jackbox identity, multi-milestone leverage marking, hosted-only operator model, v2 requirements completeness, Supabase verification

   **You do not need to verify all of these.** Pick the ones that are load-bearing for the question of whether the narrow initiative's "canon already aligned" claim is warranted. Specifically: the items that, if not addressed, would mean the canon is *not* aligned in the way the narrow initiative claims.

3. **Untyped load-bearing assumptions** in the canon itself. The canon claims certain things are "decided" or "open." Are the closure / open distinctions load-bearing? Are there assumptions the canon treats as settled that are actually working assumptions presented as decisions?

### Cross-Cutting Obligations

#### Chain integrity

> "When audit B uses audit A's finding as evidence, and audit A had a quality failure, audit B inherits the failure invisibly. **Obligation:** For each finding that depends on a predecessor audit's claim, re-verify that claim independently before incorporating it. State the re-verification or state why it was not done."

**This applies fully here.** The 2026-04-08 audit is the predecessor whose claims you are most likely to inherit. Re-verify each predecessor claim you actually rely on by reading the file the predecessor cited. State your re-verification method.

**The full form of chain integrity** (per the parent task spec): the predecessor's *recommendations* themselves are also contestable claims. The predecessor was produced from a particular methodology (4 lanes × 2 model passes) and may have over-recommended or made recommendations more appropriate to a serious public product than to a private fan game. For each recommendation you check, ask both "was it adopted?" AND "should it have been adopted in the form proposed?" This is the three-outcome framing.

#### Framework invisibility

> *"Name a concrete finding that would not appear no matter how rigorously this audit was conducted, because of how this audit's scope was framed. If you can't name one, that's suspicious — the framework is probably hiding something from you that it's also hiding from itself."*

**Specific to this lane:** the lane is framed in terms of "verify the predecessor's claims and the narrow initiative's claims." This framing makes invisible: claims neither the predecessor nor the narrow initiative made about the canon. There may be canon content that is doing load-bearing work that *both* the predecessor audit and the narrow initiative missed. If you find such content, name it as a finding and observe that the lane's framing would have hidden it from you if you hadn't actively looked for it.

---

## The Lane Situation

### Files to read (suggested starting list — NOT closed)

**The canon (the substrate the narrow initiative claims is aligned):**
- `.planning/PROJECT.md` (191 lines, last updated 2026-04-11)
- `.planning/LONG-ARC.md` (154 lines)
- `.planning/ROADMAP.md` (205 lines, last updated 2026-04-11)
- `.planning/REQUIREMENTS.md` (191 lines)
- `.planning/STATE.md` (81 lines)

**The narrow initiative under audit (specifically its claim about canon alignment):**
- `.planning/initiatives/vision-alignment-2026-04/README.md` (89 lines) — especially lines 24–31 ("Why This Is Not A Full Vision Initiative")
- `.planning/initiatives/vision-alignment-2026-04/PLAN.md` (123 lines) — especially "This Plan Is Scaffolding, Not A Commitment To Over-Research"

**The Phase 01 live artifacts (additional canon-adjacent material):**
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md` (179 lines)
- `.planning/phases/01-authored-round-contract/01-RESEARCH.md` (418 lines)
- `.planning/phases/01-authored-round-contract/01-VALIDATION.md` (80 lines)
- `.planning/phases/01-authored-round-contract/01-DISCUSSION-LOG.md` (76 lines)

**The predecessor audit (whose claims you are re-verifying):**
- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md` (the consolidated claims and recommendations)
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md` (only if the SYNTHESIS uses claims from it)
- `.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md` (read this — it surfaces methodological caveats about the predecessor itself, which directly bears on whether the predecessor's recommendations should be inherited)
- Lane reports (`lane-1-plan-quality.md`, `lane-2-frontend-design.md`, `lane-3-stakeholder-distribution.md`, `lane-4-multi-milestone-vision.md`) — read only if the SYNTHESIS uses claims from a specific lane that you need to verify

**The four `01-XX-PLAN.md` files in `.planning/phases/01-authored-round-contract/` are being deleted as stale residue.** Do not read them as authoritative. They are not load-bearing for canon integrity.

### What you may NOT inherit as ground truth

- The narrow initiative's claim that the canon is "already relatively well-aligned." This is the central claim under audit. Verify it directly.
- The 2026-04-08 audit's claim that the canon "needs revision." Also under audit. Verify it directly against the canon as it exists *now*.
- The orchestrator's framing that the predecessor and the narrow initiative are in tension. They may turn out to be reconcilable in ways neither directly states.

### What this lane is NOT investigating (assigned to other lanes)

- **Lane 1B** is comparing the methodological inheritance from f1-modeling's RESEARCH-PRINCIPLES and PLAN to prix-guesser's. You do **not** need to read the f1-modeling files. If you find that the canon's alignment claim depends on methodological assumptions that 1B is checking, note it as a cross-lane dependency for the synthesizer.
- **Lane 1C** is using web research to identify alternatives the prix-guesser research did not consider. You do **not** need to do web research. If you find that the canon's alignment claim depends on the project having considered an alternative not visible in the repo, note it as a question for 1C.

If you need to do work that overlaps with 1B or 1C, do the part you need but flag it as cross-lane so the synthesizer doesn't double-count.

---

## Lane Investigatory Questions

These are starting questions, not a closed list. Add, drop, or reframe as the investigation reveals what's load-bearing.

### LQ-1A.1 — Earned convergence vs repeated assumption

What in the canon supports the claim that "the broader product posture is already relatively well-aligned"? What cuts against it? Is the apparent coherence *earned convergence* (same questions asked in different ways, got the same answers, stress-tested against alternatives) or *repeated assumption* (same framing authored once and copied across documents without independent verification)?

Concrete tests:
- Pick a load-bearing claim that appears in multiple canon documents (e.g., "private-only fan project," "host-screen-friendly," "geography-and-circuit anchor"). For each appearance, is the claim *argued* or *asserted*? If asserted, is the assertion supported by reasoning elsewhere in the canon, or is it the kind of claim that simply propagates?
- Are there places where the canon documents diverge (one document treats a question as open while another treats it as closed)? Divergence is evidence of unfinished alignment work.
- Are there places where the canon documents *agree but for different reasons* — i.e., the same conclusion follows from different premises in different documents? If so, the agreement is fragile.

### LQ-1A.2 — Predecessor recommendation status, with three-outcome framing

For each of the following predecessor recommendations, ask both "was it adopted?" and "should it have been adopted in the form proposed?":

- **DEPLOY-01..05** (Lane 3 GPT). Has REQUIREMENTS.md been updated? In the proposed form, a different form, or not at all? Is the current state principled?
- **"F1 GeoGuessr vs F1 Jackbox" identity question** (Q2). Has the identity been resolved in the canon? If so, where and which way? If not, is the deferral principled or evasion?
- **"Watchability" operationalization** (Lane 2 convergent). Has the term been operationalized? If still abstract, is the abstraction principled?
- **Hierarchical-vs-flat answer target model** (Lane 4 GPT-unique, "THE most important architectural decision"). Has the decision been made anywhere readable? Is it inside or outside the narrow initiative's scope, and is that placement principled?
- **Phase 3.1 (UI-SPEC) inserted phase** (Q1). Look at ROADMAP.md line 26. The phase exists by name. Does the goal/criteria actually deliver what the predecessor was asking for, or is it a phantom integration?
- **"Hosted game that happens to be built by a developer" framing** (Lane 3 Opus, called "the single most valuable framing of the entire audit"). Has PROJECT.md adopted this framing? In what form?
- **"Cosmetics out of scope" warning** (Lane 2 GPT-unique). Has the project guarded against the misreading the predecessor flagged?

For each, state your re-verification method and what you found. If the predecessor's recommendation is itself contestable, state your reading of whether it should have been adopted.

### LQ-1A.3 — Untyped load-bearing assumptions

What does the canon treat as decided that is actually a working assumption? PROJECT.md has a "Key Decisions" table (lines 151–159) that marks several as "Adopted" and others as "Still open." Are those classifications honest? Specifically:
- Is "Initialize as a private-only fan project" really decided, or is it deferring distribution questions by definitional fiat?
- Is "Bias toward authored F1 rounds" really decided, or is it papering over an unanswered question about how authoring sustainability scales?
- Is "Bias toward host-screen-friendly private play" really decided, or is it inheriting an aesthetic preference without engaging the operational requirements?

The PROJECT.md "Open Questions" table (lines 161–171) marks several as "Critical" with "Pending" status. Are these the right open questions, or are there critical questions that have been smuggled into the "Adopted" table?

### LQ-1A.4 — The narrow initiative's exclusions as canon claims

The narrow initiative's `Out of scope` list at `.planning/initiatives/vision-alignment-2026-04/README.md` lines 59–66 explicitly excludes "frontend framework choice, room runtime and authority implementation, deploy topology decisions, public/share-by-link/public-spectator posture, adjacent F1 mode expansion, in-app authoring UI." For each exclusion:
- Where in the canon is the corresponding decision made or deferred?
- If the canon doesn't address it, is the narrow initiative's exclusion a way of *deferring* the question (legitimate) or *declaring it non-existent* (illegitimate)?
- The user's stance specifically named "deployment, distribution, adoption" as concerns. The exclusions overlap with these. Is the canon adequate to support the exclusions, or do the exclusions point to gaps the canon does not own?

---

## What Must Appear In The Lane Output

Write your output to `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1a-canon-integrity.md`.

The output is consumed by the Wave 3 synthesis pass and possibly by Review Gate 1. It does NOT need to be the final audit output — it is a focused lane report. Length: as long as the situation requires, no longer.

Required elements:

- **All obligations addressed in substance** — Core Rules 1–5 (with Rule 5 as a full section), investigatory I1–I4 plus the two additional obligations, claim_integrity subject obligations, chain integrity, framework invisibility. Woven into the narrative; not necessarily as labeled sections.

- **A re-verification ledger** for each predecessor claim you actually rely on. State the claim, the file:line you re-opened, what you found, and whether the predecessor's reading still holds.

- **A three-outcome assessment** for each predecessor recommendation you check. For each: addressed? / should it have been? / what's the principled reading?

- **A direct verdict on LQ-1A.1** (earned convergence vs repeated assumption). This is the lane's load-bearing question. Don't hedge.

- **A "Position of the Investigation" section** addressing I4. Where are you looking from? What is this Opus-on-Opus self-dispatch in this particular session prepared to notice and what is it not?

- **A Rule 5 frame-reflexivity section** answering the three specific questions verbatim. Anti-performativity warning applies.

- **A "What the Obligations Didn't Capture" section** — mandatory.

- **A "Cross-Lane Notes for the Synthesizer" section** — anything you found that overlaps with Lane 1B (methodological inheritance) or Lane 1C (external gap research). The synthesizer needs to know what to weigh and what to dedupe.

- **A list of candidates for Wave 2 follow-up** — questions this lane raises that it could not answer with the available evidence and that would benefit from a focused Wave 2 pass. The orchestrator and user use this list at Review Gate 1 to decide whether Wave 2 happens and what it investigates.

---

## Composition Principle (read if tensions emerge)

When obligations tension against each other, you must not pick a winner. You must:

1. **Name the tension.** Concretely, in this situation.
2. **Name what about the situation creates it.**
3. **Show how you navigated it** — responsive to both demands.
4. **The resolution emerges from engagement,** not from a precedence rule applied in advance.

If your output contains zero tensions, ask whether you smoothed them out or whether they really weren't there. The honest answer is more valuable than the polished one.

---

## Output File

Write the lane output to:

`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1a-canon-integrity.md`

Do not return a conversational summary instead of the file. Write the file, then exit. The orchestrator will read it from disk.
