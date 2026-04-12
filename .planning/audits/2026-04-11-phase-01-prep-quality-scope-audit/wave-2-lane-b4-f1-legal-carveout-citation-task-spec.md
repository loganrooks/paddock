---
date: 2026-04-11
wave: 2
lane: B4
audit_subject: claim_integrity
audit_orientation: standard
audit_delegation: self
auditor_model: claude-sonnet-4-6
agent_type: gsdr-auditor
scope: "Empirical verification: does the prix-guesser canon cite F1's fan-use trademark carveout, or any other legal rationale for the private-only posture? Lane 1C Finding 1 identified F1's official guidelines as explicitly carving out 'limited use... for a private, educational purpose only' while also stating motorsport simulators/software 'should not make any use of the FORMULA 1 Rights without an express written license' — a legal reason the private-only framing is exactly the right posture. Lane 1C said naming the legal rationale in the canon 'would strengthen the posture substantially.' This lane does the primary empirical check (is it cited?) plus the secondary generative question (if not, what's the right file and form for the citation?)."
triggered_by: "wave-2 dispatch from phase-01-prep-quality-scope-audit-2 orchestrator after Review Gate 1; prompted by Lane 1C Finding 1"
parent_task_spec: phase-01-prep-quality-scope-audit-2-task-spec.md
predecessor_lanes:
  - wave-1-lane-1c-external-gap-research.md
  - wave-1-lane-1a-canon-integrity.md
ground_rules: "core+standard+claim_integrity+chain"
tags:
  - wave-2
  - lane-b4
  - f1-legal-carveout
  - claim-integrity
  - standard
  - sonnet
output_files:
  - wave-2-lane-b4-f1-legal-carveout-citation.md
---

# Wave 2 / Lane B4 — F1 Legal Carveout Citation Check (Sonnet)

**You are running as gsdr-auditor on Claude Sonnet 4.6.**

You are the only Sonnet lane in Wave 2 — Lane B2 (authoring sustainability) and Lane B3 (distributed methodology) are both Opus. You were assigned Sonnet because this lane is primarily structured empirical work (verify whether a specific citation exists in the canon), which is the task profile Sonnet handles well and for which Opus would be budget-wasteful.

**Mark your model identity explicitly in your output frontmatter and findings, so the Wave 3 synthesizer has model-class attribution when it weights findings across lanes.** Wave 1 was entirely Opus (no cross-class signal). Wave 2 has one Sonnet lane (you). The synthesizer should be able to see which lane ran on which model class.

## Lane Position In The Audit

This is a Wave 2 lane running in parallel with Lane B2 (authoring sustainability, Opus) and Lane B3 (distributed methodology, Opus). Wave 2 composes with Wave 1 at the Wave 3 synthesis. Your job is narrow and focused: an empirical citation check plus a small generative follow-up. Do not try to do B2 or B3 work.

## Lane Fit Assessment

This lane is **claim_integrity × standard × self** because the primary question — "does the canon cite F1's fan-use carveout or any legal rationale for private-only?" — has a direct empirical answer. The canon either contains the citation, or it doesn't. Standard orientation is correct because the question closes on evidence: a citation either exists or it doesn't.

The lane has a small **generative secondary question**: if the citation is missing, what's the right file and form for it? This is a design call rather than a verification call. Standard orientation still fits because the design question has a relatively bounded answer space (the citation goes in PROJECT.md or LONG-ARC.md or a new file, and the form is a constraint / key decision / footnote / open question). The generative part is light — you are not drafting pages of text, just identifying the right slot.

If the empirical check turns out to be more complicated than expected (e.g., the canon cites F1 rights in some oblique form that doesn't match the Lane 1C language but does engage the legal concern), the orientation may shift toward investigatory. If that happens, say so explicitly and apply investigatory obligations from that point forward.

## Epistemic Ground Rules

### Core Rules (every audit)

1. **Every factual claim cites file:line and quotes the relevant passage.** Bad: "The canon doesn't cite F1 trademark policy." Good: "I searched `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, and `.planning/STATE.md` for these terms (case-insensitive): 'F1', 'Formula 1', 'trademark', 'copyright', 'fan use', 'fair use', 'unofficial', 'licensed', 'rights', 'intellectual property', 'IP', 'legal', 'guidelines.4EOKE9RRqevL4niTK9kWyt'. I found [N] matches. [Quote each match and assess whether it constitutes a legal rationale for the private-only posture.]"

2. **For every finding, BEFORE writing it, ask "What would disconfirm this?" and CHECK.** Example: if you are about to claim "the canon treats private-only as YAGNI not legal," first search for passages where the canon names F1 as a rights-holder or notes the unofficial/fan-use character of the project as a constraint on distribution. If you find one, the "YAGNI not legal" claim weakens.

3. **Distinguish what you measured from what the measure captures.** Example: "I checked whether the canon cites F1's fan-use carveout URL. URL-citation check measures whether the specific link is named, NOT whether the legal rationale is present in some other form (e.g., a paraphrased reference, an acknowledgment of F1's guidelines without a URL, a 'this is a fan project' constraint that implicitly recognizes the legal context). I separately checked for implicit treatments."

4. **Rule 4 (escape hatch).** Address in the mandatory **What the Obligations Didn't Capture** section.

5. **Rule 5 (frame-reflexivity).** For standard orientation, Rule 5 is a **lightweight closing step** (1–3 sentences, not a full section). Answer the three specific questions concisely:
   - *"If this lane had been classified as `requirements_review` (checking whether a legal-compliance requirement exists) instead of `claim_integrity` (checking whether a specific citation exists), what would it have looked for that I didn't?"*
   - *"If this lane had been classified with `investigatory` orientation, what would it have held open that I closed? Specifically: the question 'is the canon wrong to not cite this?' is a judgment call, not a fact-check."*
   - *"What about the `claim_integrity × standard` classification shapes what I am prepared to notice and what I am not? Name one concrete example."*

   **Anti-performativity warning.** Even a standard-orientation Rule 5 must have concrete consequence, not an empty "I considered my biases."

### Orientation Obligations (standard)

Standard orientation is the routine case. You know what you're checking; the goal is to close on findings with evidence.

- **Close on findings with evidence.** Every finding lands — pass, fail, or explicit defer-with-reason. If the citation exists, state it with file:line and assess adequacy. If it doesn't, state it with reasoning about where you searched and why absence is confidently claimed.

- **Produce a clear verdict or assessment.** At the scope level: does the canon cite F1's legal carveout or any legal rationale for private-only? Yes / no / partially. Don't hedge beyond what the evidence requires.

- **Address all items in scope.** Don't partially address the question. If scope is too large, narrow and state what was excluded — don't silently skip.

### Subject Obligations (claim_integrity)

> *"Verify claims against citations; surface untyped load-bearing assumptions; trace dependency chains."*

For this lane, the operative claim is Lane 1C's assertion that F1's official guidelines legitimize the private-only framing. Your job is to verify whether that rationale is reflected in the canon as a cited or paraphrased legal justification. The claim is narrow; the subject obligation is a good fit.

**A load-bearing untyped assumption you should surface**: the canon currently treats private-only as a product decision ("private-only fan project" is listed as a scope choice). Whether this is a *product* scope choice or a *legal* constraint is not made explicit. That ambiguity is itself a finding worth recording — the canon may be making a legal decision without acknowledging that it's legal.

### Cross-Cutting Obligations

#### Chain integrity

Primary predecessors:

1. **Lane 1C Finding 1** — F1's trademark guidelines at `https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt` explicitly carve out "limited use... for a private, educational purpose only" and state that motorsport simulators/software "should not make any use of the FORMULA 1 Rights without an express written license." **You cannot re-verify the external URL because you are gsdr-auditor (no WebSearch/WebFetch).** Rely on Lane 1C's quotation in good faith and note this explicitly. If your lane's conclusion depends on the external quotation being accurate, the conclusion is conditional on Lane 1C's claim, and the synthesizer should be told so.

2. **Lane 1A's canon-integrity ledger** — Lane 1A produced a three-outcome ledger for predecessor recommendations. Check whether Lane 1A's ledger addressed the F1 legal rationale question directly. If Lane 1A checked and found nothing, your lane should confirm with a more targeted search (Lane 1A had a broader scope and may not have searched specifically for legal language). If Lane 1A didn't check, your lane is doing a new verification.

**The orchestrator's task-spec claims are contestable.** Lane 1B caught 2 of 8 factual errors in this orchestrator's Wave 1 pre-list (25% error rate). If any claim I make about where the canon is located, what files to search, or what the prior lanes said turns out to be wrong, surface it as a finding.

#### Framework invisibility (encouraged for standard orientation, not required)

Standard orientation encourages but does not require framework invisibility engagement. For this lane, the framework-invisibility prompt is light:

> *"Is there a concrete finding that would not appear no matter how rigorously this lane was conducted, because of how the lane's scope was framed as 'does the canon cite the carveout or any legal rationale?'"*

One candidate: the lane cannot see whether the project's owner personally knows about F1's fan-use guidelines (knowledge outside the canon). The canon's silence on the legal rationale may be a choice rather than an omission — the owner may know the rationale and consider it not worth putting in the canon. That distinction is invisible to a document-reading lane.

## The Lane Situation

### What this lane must produce, at minimum

1. **Primary verdict**: Does the canon cite F1's fan-use carveout URL or any legal rationale for private-only? Yes / no / partially, with file:line citations and quoted passages as evidence.

2. **Secondary verdict**: If the canon treats private-only as a product decision rather than as a legal constraint, is that acknowledged anywhere, or is the legal dimension invisible?

3. **Generative follow-up (if the citation is missing)**: What's the right file and form for the citation? Identify the slot (file + section + form) without drafting extensive text.

### Read list (focused — this lane does not need the full corpus Wave 1 lanes read)

**The canon (primary search targets):**
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/STATE.md`

**Discovery material (referenced in PROJECT.md line 37 as the pre-GSD discovery pass):**
- `discovery/` directory — specifically `discovery/14-gsd-seed.md` if it exists, and any discovery files that discuss rights, licensing, or legal considerations. This is outside the canon per se but is referenced by the canon.

**Phase 01 live artifacts (briefly — check whether the phase context mentions F1 rights):**
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
- `.planning/phases/01-authored-round-contract/01-RESEARCH.md` — only if you have context budget left and the canon check doesn't resolve the question

**Predecessor audit treatment of F1 rights (for completeness):**
- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md` — search for F1 rights / trademark / licensing language. The predecessor may have treated the question in a way that influenced or didn't influence the canon.

**Wave 1 outputs (re-verify, don't inherit):**
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md` — specifically Finding 1 and its quoted F1 passage
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1a-canon-integrity.md` — check whether Lane 1A's ledger touched this

### Search terms to use (not exhaustive — add as the investigation prompts)

Case-insensitive grep across the canon files for:
- `F1`, `Formula 1`, `FORMULA 1`
- `trademark`, `copyright`, `IP`, `intellectual property`
- `fan use`, `fair use`, `fan project`, `fan-made`
- `unofficial`, `unauthorized`
- `rights`, `licensed`, `license`, `licensing`
- `legal`, `liability`
- `guidelines.4EOKE9RRqevL4niTK9kWyt` (the specific Lane 1C URL)
- `private`, `private-only`, `private use`, `educational purpose` (these may appear in contexts relevant to the legal framing)

The canon may use language like "unofficial fan project" (which partially engages the concern) without explicitly naming the legal rationale. Both absence of direct citation AND presence of oblique acknowledgment are findings worth recording.

### What this lane is NOT investigating

- **Lane B2** (authoring sustainability) — unrelated scope
- **Lane B3** (distributed methodology) — unrelated scope
- **Whether the legal rationale is factually correct** — you cannot verify F1's guidelines without web access, so you must take Lane 1C's quotation in good faith
- **Whether the project should be private-only** — out of scope; the project has decided this already

### What you may NOT inherit as ground truth

- Lane 1C's quotation of F1's guidelines (you cannot re-verify externally, but you can note the good-faith dependency explicitly)
- Lane 1A's implicit coverage of the legal question (verify by searching directly rather than trusting Lane 1A's scope)
- The orchestrator's implicit assumption that the citation is missing (Lane 1C's read was "appears to justify private-only as YAGNI/scope-management, not as legal-risk reduction" — this is a Lane 1C characterization, not a verified absence)

## Lane Questions

### LQ-B4.1 — Does the canon cite F1's fan-use carveout URL?

Primary empirical check. Search the canon for the specific URL (`guidelines.4EOKE9RRqevL4niTK9kWyt`) and variants (`formula1.com/en/information/guidelines`). Report findings with file:line.

### LQ-B4.2 — Does the canon cite any legal rationale for private-only?

Broader check. Search for trademark, copyright, fair use, unofficial, rights, licensing, and related terms. For each match, quote and assess whether it constitutes a legal rationale for the private-only posture or just an acknowledgment of the unofficial character.

### LQ-B4.3 — How does the canon frame the private-only decision?

Look specifically at PROJECT.md's "Constraints" section (around lines 139–147 per the parent task spec's citation) and PROJECT.md's "Key Decisions" table. How is "Initialize as a private-only fan project" justified? By what reasoning? Is that reasoning legal-rooted or product-rooted?

### LQ-B4.4 — If the citation is missing, where should it live?

Generative follow-up. Identify:
- **File**: PROJECT.md (Constraints)? LONG-ARC.md (long-arc-level framing)? A new section in PROJECT.md? A new file entirely?
- **Form**: Constraint? Key Decision row? Open Question? Footnote?
- **Minimum viable text**: a short phrase or sentence that would engage the legal rationale without being a legal document

Identify the slot, don't draft pages.

### LQ-B4.5 — Is the absence of the citation a gap or a choice?

The project owner may know about F1's fan-use guidelines and have deliberately chosen not to cite them in the canon (e.g., to avoid appearing to manufacture legal cover for a hobby project, or because legal advice is outside the canon's purpose). Alternatively, the absence may reflect that the decision was made on YAGNI/scope grounds without the legal rationale being considered. Your lane cannot definitively distinguish the two, but you can observe indicators:

- If the canon anywhere *mentions* F1's rights without citing the carveout, that's evidence the owner knows about the legal context and chose to be terse (more likely a choice).
- If the canon uses "unofficial fan project" language without ever mentioning F1 as a rights-holder, that's evidence the legal context is implicit and unexamined (more likely a gap).

Record the indicators you find and explicitly flag the limit of what a document-reading lane can conclude.

## What Must Appear In The Lane Output

Write your output to `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b4-f1-legal-carveout-citation.md`.

Required elements (shorter lane, shorter output):

- **Primary verdict on LQ-B4.1 and LQ-B4.2** — yes/no/partially with file:line evidence
- **A quoted search ledger** — which terms you searched, which files you searched, what you found for each
- **An assessment on LQ-B4.3** — how the canon frames private-only
- **If the citation is missing, a concrete slot identification on LQ-B4.4** — file, form, minimum viable text (not drafted pages)
- **An assessment on LQ-B4.5** — gap-or-choice indicators
- **Core Rules addressed in substance**, with Rule 5 as a lightweight closing step (1–3 sentences for standard orientation)
- **A "What the Obligations Didn't Capture" section** — mandatory
- **A "Cross-Lane Notes for the Synthesizer" section** — specifically flag anything that bears on B2 (authoring sustainability) if a legal constraint changes the framing, and note any findings that contradict Lane 1A's canon-integrity ledger
- **A sentence or two on Rule 4** (escape hatch) — is there anything you encountered that the claim_integrity × standard classification didn't prepare you for?

**Length expectation**: this is a focused lane with a narrow question. Your output should be substantive but compact — probably ~300–500 lines max. Don't pad.

## Composition Principle

Standard-orientation lanes typically have fewer tensions than investigatory lanes because the orientation closes on findings rather than holding them open. If tensions do emerge (e.g., the empirical search surfaces something that can't be closed without investigatory reframing), name the tension, show how you navigated it, and consider whether the orientation was the right classification.

If your output contains zero tensions and no Rule 4 finding, that's plausible for a standard-orientation empirical check — but double-check that the orientation didn't quietly hide something that an investigatory reading would have caught.

## Output File

Write the lane output to:

`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b4-f1-legal-carveout-citation.md`

Do not return a conversational summary instead of the file. Write the file, then exit.
