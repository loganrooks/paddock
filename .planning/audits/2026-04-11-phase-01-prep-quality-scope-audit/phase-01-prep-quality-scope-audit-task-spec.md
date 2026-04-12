---
date: 2026-04-11
audit_orientation: investigatory
audit_delegation: cross_model:claude-opus-4.6
scope: "Assess whether the current Prix Guesser preparatory work justifies a narrowly scoped pre-Phase-01 vision-alignment initiative, or whether the evidence points to broader unresolved uncertainty and stronger preparatory work being required before Phase 01 is planned again."
auditor_model: claude-opus-4.6
triggered_by: "manual: user requested a Claude audit of the preparatory corpus, the basis for the 'small initiative' judgment, and the overall quality of pre-Phase-01 work"
task_spec: phase-01-prep-quality-scope-audit-task-spec.md
ground_rules: "core+investigatory+chain+dispatch+framework-invisibility"
predecessor_audits:
  - .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md
  - .planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md
tags:
  - phase-01
  - preparatory-work
  - investigatory
  - vision-alignment
  - claude
output_files:
  - phase-01-prep-quality-scope-audit-output.md
---

# Audit Task Spec: phase-01-prep-quality-scope-audit

**Date:** 2026-04-11
**Classification:** no named subject × investigatory × cross_model:claude-opus-4.6
**Fit assessment:** This audit starts without a named subject because forcing the subject now would smuggle in the very conclusion under dispute. The question is not merely whether the existing documents are "good" or whether the new initiative is "too small"; it is whether the evidence base built so far actually warrants a narrow pre-Phase-01 alignment effort, or whether the apparent coherence of the current canon is masking larger unresolved uncertainty. The investigation is free to discover that the real issue is process quality, artifact quality, initiative framing quality, or some combination.

## Epistemic Ground Rules

### Core Rules (every audit)

1. **Every factual claim cites file:line and quotes the relevant passage.** Do not assert what a file contains without opening it. Do not summarize without quoting.

2. **For every finding, BEFORE writing it, ask "What would disconfirm this?" and CHECK.** This is not a rhetorical question. Actually look for counter-evidence before committing a finding to the output. If you cannot find disconfirming evidence, note what you searched and why you didn't find it -- not finding counter-evidence is different from there being none.

3. **Distinguish what you measured from what the measure captures.** Every measurement is a proxy. Name the gap between your metric and the thing you care about.

4. **Rule 4: What did you encounter that these ground rules didn't prepare you for?** This rule is an invitation, not enforcement. It ensures the ground rules do not become a ceiling on rigor. If your answer to Rule 4 is "nothing," that may be accurate -- or it may indicate the ground rules shaped your attention so thoroughly that you didn't notice what they excluded. Consider the possibility before answering.

5. **Rule 5: Did the framing shape what you found?** For investigatory orientation, Rule 5 is a full section -- the frame-reflexivity is not decoration but part of the investigation, because an investigation that cannot see its own orientation is one that has quietly closed on a theory without knowing it.

   *Specific grounding questions to answer:*

   1. "If this audit had been classified as a different subject (e.g., `process_review` instead of `no named subject`), what would it have looked for that you didn't? What findings would that audit have produced that yours doesn't?"
   2. "If this audit had been classified with a different orientation (e.g., `standard` instead of `investigatory`), what would it have held open that you closed? What would it have investigated that you accepted?"
   3. "What about the current classification shapes what you are prepared to notice and what you are not? Name one concrete example."

   **Anti-performativity warning:** if your answer to Rule 5 is "nothing" or "I considered my biases" without a concrete consequence visible in the findings, Rule 5 has not been engaged with -- it has been performed. An empty Rule 5 is not neutral. It is a signal that the frame is invisible to the auditor. If the specific questions above produce only empty answers after genuine engagement, write that result and name why no alternative reading surfaces -- that too is a finding.

### Orientation Obligations (investigatory)

- **I1 — Start from the discrepancy, not a theory.** Describe what was expected, what was delivered, and why those expectations are being treated as the standard — the choice of comparison point is already an interpretive act. *(Why this matters: investigations that start from a theory select evidence to confirm the theory. Investigations that start from the discrepancy remain open to evidence the theory is wrong. The gap between expectation and delivery is a starting orientation, not a neutral fact — name why the expectation is the expectation.)*

- **I2 — Let the investigation guide artifact selection.** Don't mandate which artifacts to read in advance. Follow the evidence — if the discrepancy points to the planning stage, read planning artifacts. If it points to requirements, read requirements. The artifact chain is a finding, not an input. *(Why this matters: a pre-specified reading list encodes a hypothesis about where the failure lies. The investigation should discover where to read from what it finds, not from what the orchestrator specified. If the orchestrator pre-selected artifacts, I2 is in tension with that pre-selection — surface the tension, don't silently honor the pre-selection.)*

- **I3 — Present competing explanations.** For each finding, offer at least two interpretations. "The research narrowed scope" could mean the researcher made an error, OR the researcher correctly applied constraints the investigator hasn't understood yet. Don't collapse to one. *(Why this matters: an investigation that presents a single explanation has stopped investigating. The criterion for closing an investigation is not "I found an explanation" but "the evidence rules out the alternatives." An explanation without ruled-out alternatives is a hypothesis, not a finding.)*

- **I4 — Name the position of the investigation.** Every investigation is conducted from somewhere — with particular attunements, particular things it's prepared to notice, particular things it isn't. This isn't about cataloguing determinate "blind spots" as if they're hidden objects waiting to be found, but about acknowledging what this particular way of looking is oriented toward and what a differently-situated investigation would attend to. *(Why this matters: every investigator is embedded. Pretending otherwise produces the illusion of neutrality, and that illusion hides the frame from both the auditor and the reader. Naming the position is the minimum epistemic hygiene of situated inquiry — and it also gives the reader the information they need to decide how far to trust the investigation's framing.)*

- **Show what remains unknown.** Not everything needs resolution. Explicit unknowns are findings — they map the edge of the investigation. *(Why this matters: the temptation at the end of an investigation is to close on a story. Resisting that temptation — and naming what the story cannot yet explain — is what distinguishes an investigation from a speculation.)*

- **Show how you navigated any tensions between obligations.** When investigatory obligations tension with other obligations or with each other, the navigation itself is a finding. See the Composition Principle below. *(Why this matters: how an investigator resolves tensions reveals their working frame. Making that resolution explicit — rather than performing a clean synthesis — gives the reader the information they need to evaluate whether the navigation was sound.)*

### Subject Obligations (none named at dispatch)

No subject is named for this audit. Core + orientation obligations are the full obligation set at dispatch time. If a subject becomes clear mid-audit, say so explicitly and note which subject obligations then came online: `process_review`, `artifact_analysis`, `comparative_quality`, or something else.

### Cross-Cutting Obligations

**Chain integrity**

> "When audit B uses audit A's finding as evidence, and audit A had a quality failure, audit B inherits the failure invisibly. This is the single most consequential failure mode in the discuss-phase session chain. **Obligation:** For each finding that depends on a predecessor audit's claim, re-verify that claim independently before incorporating it. State the re-verification or state why it was not done."

This applies here because the starting corpus includes prior audit outputs. Do not inherit their claims without re-verification.

**Dispatch hygiene**

> "When running model comparison experiments or multi-agent parallel dispatch, the prompts themselves can contaminate the results (the contamination experiment in the session-log audit found 50% GPT inflation from framing effects). **Obligation:** For `cross_model` delegation, verify that the delegation prompt does not include framing that could systematically bias findings (comparative framing, target counts, desired conclusions). If the comparison is intentional, note it explicitly in the audit frontmatter as a confound."

This task spec is intentionally not asking for a target verdict. Audit whether the prompt itself nevertheless nudges you toward "the initiative is too small" or "the initiative is fine."

**Framework invisibility**

> "The obligations have I4 ('name the position of the investigation') but nothing that specifically asks: 'What does this audit's framework make invisible? What kinds of findings would not appear in this audit no matter how rigorously it was conducted?' **Obligation:** Name what your audit framework cannot see — not what you chose not to look at, but what the structure of the audit makes invisible."

**Relationship to I4 and Rule 5.** Framework invisibility is distinct from both. I4 names the investigator's position. Rule 5 asks whether the audit's classification was the right frame. Framework invisibility asks the deepest version of the question: what kinds of findings cannot appear in this audit at all, because of how the audit's scope was structured?

**Ground framework invisibility in a specific question:**

> "Name a concrete finding that would not appear no matter how rigorously this audit was conducted, because of how this audit's scope was framed. If you can't name one, that's suspicious — the framework is probably hiding something from you that it's also hiding from itself."

## The Situation

The user wants an external Claude audit of the preparatory work that has accumulated around Prix Guesser before Phase 01 is rerun. The immediate dispute is not a narrow implementation bug. It is a judgment call: whether the project's current canon and preparatory artifacts justify a **small, targeted pre-Phase-01 vision-alignment initiative**, or whether that judgment itself was premature and the repo actually needs broader alignment before foundational contract decisions are frozen.

Recent local work produced a narrow initiative scaffold at:

- `.planning/initiatives/vision-alignment-2026-04/README.md`
- `.planning/initiatives/vision-alignment-2026-04/PLAN.md`
- `.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md`

That scaffold should be treated as a proposal under audit, not as an accepted answer.

Current project state says:

- `.planning/STATE.md` identifies Phase 01 as current focus
- `.planning/STATE.md` says "Replanning required before execution"
- `.planning/STATE.md` records `plan_count: 0` and `stopped_at: Phase 01 context gathered`

At the same time, the working tree contains untracked Phase 01 plan files:

- `.planning/phases/01-authored-round-contract/01-01-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-02-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-03-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-04-PLAN.md`

That mismatch is part of the situation and should be interpreted, not ignored.

Use this briefing memo as a starting map, not a closed read list:

- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-briefing.md`

## Investigatory Questions

1. What in the actual preparatory corpus supports the judgment that only a small, targeted vision-alignment initiative is warranted?
2. What in the corpus cuts against that judgment?
3. Is the current preparatory work genuinely high quality, or merely internally consistent because the same assumptions were repeated across documents?
4. Are the remaining uncertainties phase-local authored-substrate questions, or signs of broader under-alignment that should widen the initiative?
5. How much confidence should be placed in the existing Phase 01 context, research, validation, prior audits, and recent framework/runtime changes?
6. What would the most defensible next step be before rerunning Phase 01 planning?

## What Must Appear in the Output

- All obligations above addressed in substance
- A clear explanation of what evidence most strongly supports a narrow initiative
- A clear explanation of what evidence most strongly supports a broader initiative or further preparatory work
- Independent re-verification of any predecessor-audit claims you rely on
- A section titled `What the Obligations Didn't Capture`
- A full Rule 5 frame-reflexivity section
- A section titled `Position Of The Investigation`
- A section titled `How I Navigated Tensions`
- A practical conclusion that says one of:
  - the current narrow initiative is justified
  - the initiative should widen in specific ways
  - the preparatory corpus is not yet strong enough to justify either conclusion

## Composition Principle

Obligations from different axes compose into a flat list. They do not form a hierarchy. When obligations tension against each other, you must not pick a winner. You must:

1. **Name the tension.** Say what the two or more obligations are and how they pull differently in this situation.
2. **Name what about the situation creates it.** The tension is occasioned by particulars; identify those particulars.
3. **Show how you navigated it.** Be responsive to both demands, not cleanly loyal to one side.
4. **Let the resolution emerge from engagement** with the situation, not from a precedence rule applied in advance.

This is a hermeneutic principle, not an algorithmic one. If the tensions disappear into tidy prose, that is itself suspicious.

## Output File

Write the audit output as markdown to:

`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-output.md`

Do not return a conversational summary instead of the file.
