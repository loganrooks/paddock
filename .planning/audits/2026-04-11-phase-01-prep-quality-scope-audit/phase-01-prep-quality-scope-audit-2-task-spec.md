---
date: 2026-04-11
audit_orientation: investigatory
audit_delegation: self
scope: "Critically assess whether the Prix Guesser preparatory corpus and the proposed narrow pre-Phase-01 vision-alignment initiative justify proceeding to Phase 01 planning. Engage explicitly with the f1-modeling vision-alignment initiative as a comparative reference point. Engage explicitly with deployment, distribution, scale, adoption, and downstream concerns the narrow framing may have excluded or pre-decided. Permit qualified, conditional judgments — neither outright approval nor outright rejection is required."
auditor_model: claude-opus-4-6
triggered_by: "user: /gsdr:audit invoked from Claude Code with explicit framing that (a) rejects time-pressure / loss-of-momentum arguments as load-bearing, (b) asks the audit to consider deployment/scale/distribution/adoption broadly, and (c) requests evaluation against f1-modeling vision-alignment as a comparative reference point. This is the canonical Claude self-dispatch in this session — Codex previously authored phase-01-prep-quality-scope-audit-task-spec.md as a proposed cross_model dispatch; that file is now a predecessor preparation artifact, not the live dispatch."
task_spec: phase-01-prep-quality-scope-audit-2-task-spec.md
ground_rules: "core+investigatory+chain+self-dispatch-hygiene+framework-invisibility"
predecessor_audits:
  - .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md
  - .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md
  - .planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md
  - .planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-task-spec.md
  - .planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-briefing.md
  - .planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-best-case-minimal-alignment.md
tags:
  - phase-01
  - preparatory-work
  - investigatory
  - vision-alignment
  - claude-self-dispatch
  - f1-modeling-comparison
  - deployment-distribution-adoption
output_files:
  - phase-01-prep-quality-scope-audit-2-output.md
---

# Audit Task Spec: phase-01-prep-quality-scope-audit (Claude self-dispatch, v2)

**Date:** 2026-04-11
**Classification:** no named subject × investigatory × self (gsdr-auditor)
**Auditor model:** claude-opus-4-6 (you are running as the gsdr-auditor agent on Claude Opus 4.6)

## Fit Assessment

This audit is dispatched **investigatory × no-subject × self** because the question under inquiry is genuinely open in shape and resists premature subject lock-in. The user is not asking "verify Phase 01 plans" (`phase_verification`), nor "is the canon document complete" (`requirements_review`), nor "did the methodology work as designed" (`process_review`) — though the investigation may *discover* that one or more of those subjects becomes operative as it proceeds. The question is: **does the prepared corpus actually warrant the narrow initiative that was just authored, or has the narrow framing pre-decided what the investigation was supposed to find?**

Forcing a subject at dispatch time would smuggle in the conclusion the audit is meant to interrogate. If you find mid-investigation that the audit is really a `process_review` of how the narrow initiative was scoped, or a `comparative_quality` audit of prix-guesser's preparation against f1-modeling's preparation, or a `claim_integrity` audit of whether the narrow initiative's claims about canon alignment are warranted by the canon as it actually stands — name that explicitly and apply the corresponding subject obligations from that point forward. The shift is itself a finding. The investigation begins from a discrepancy and an opening question, not from a hypothesis-laden subject.

The orientation is **investigatory** rather than `standard` because: (a) the user explicitly wants competing explanations and qualified, conditional judgments; (b) the question concerns whether the apparent coherence of the canon is *earned convergence or repeated assumption*, which is exactly the kind of question that closes on the wrong answer if forced to a verdict prematurely; (c) the predecessor audit (2026-04-08) and the recently-authored narrow initiative are in apparent tension over the state of the canon, and the investigation must hold both claims open until evidence rules out alternatives.

The delegation is **self** because Claude Code dispatched this audit and the auditor is the gsdr-auditor agent running on Claude Opus 4.6 — the same model class as the orchestrator, in the same conversational context. There is no cross-model dispatch involved. **However**, see the modified dispatch-hygiene obligation below: self-dispatch does not eliminate framing risk; it relocates it. The orchestrator's framing of this task spec is itself a potential source of contamination, and the user's stated stance (which the orchestrator has copied into this spec) is a starting orientation, **not a conclusion the audit must reach**.

You are free to reframe this fit assessment as a finding if the investigation reveals that any of these classification choices were wrong for what the situation actually asked of you. Per Rule 5 below, that reframing is not a meta-commentary detachment from the audit — it is the audit doing its job.

---

## Epistemic Ground Rules

### Core Rules (every audit)

1. **Every factual claim cites file:line and quotes the relevant passage.** Do not assert what a file contains without opening it. Do not summarize without quoting. Bad: "The narrow initiative claims the canon is aligned." Good: "The narrow initiative README at `.planning/initiatives/vision-alignment-2026-04/README.md` line 25 states 'This project does **not** currently have the same kind of wide, cross-domain architectural uncertainty that justified the larger `f1-modeling` initiative shape. The broader product posture is already relatively well-aligned across...'." Quote the actual claim, then engage with it.

2. **For every finding, BEFORE writing it, ask "What would disconfirm this?" and CHECK.** This is not a rhetorical question. Actually look for counter-evidence before committing the finding to the output. If you cannot find disconfirming evidence, note what you searched and why you didn't find it — not finding counter-evidence is different from there being none. Example: if you are about to claim "the canon is internally consistent," first search for a passage where it contradicts itself; if you don't find one, name what you searched and why a contradiction would have been visible there if it existed.

3. **Distinguish what you measured from what the measure captures.** Every measurement is a proxy. Name the gap between your metric and the thing you care about. Example: "I counted 869 lines across the canon docs (PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md, STATE.md). Line count measures volume of writing, NOT depth of alignment. A canon that is convergent because it repeats the same framing in many words is not the same as a canon that is convergent because the framing has been stress-tested."

4. **Rule 4 (escape hatch): What did you encounter that these ground rules didn't prepare you for?** This rule is an invitation, not enforcement. It ensures the ground rules do not become a ceiling on rigor. If your answer to Rule 4 is "nothing," that may be accurate — or it may indicate the ground rules shaped your attention so thoroughly that you didn't notice what they excluded. Consider the possibility before answering. Address Rule 4 in the mandatory **What the Obligations Didn't Capture** section at the end of your output.

5. **Rule 5 (frame-reflexivity): Did the framing shape what you found?** For investigatory orientation, Rule 5 is a **full section** — the frame-reflexivity is not decoration but part of the investigation, because an investigation that cannot see its own orientation is one that has quietly closed on a theory without knowing it.

   *Specific grounding questions to answer (copy verbatim — do not paraphrase, generic prompts about "bias" produce compliance theater):*

   1. *"If this audit had been classified as a different subject (e.g., `process_review` instead of no-subject, or `claim_integrity` instead of no-subject, or `comparative_quality` instead of no-subject), what would it have looked for that you didn't? What findings would that audit have produced that yours doesn't?"*
   2. *"If this audit had been classified with a different orientation (e.g., `standard` instead of `investigatory`), what would it have held open that you closed? What would it have investigated that you accepted?"*
   3. *"What about the current classification shapes what you are prepared to notice and what you are not? Name one concrete example."*

   **Anti-performativity warning.** If your answer to Rule 5 is "nothing" or "I considered my biases" without a concrete consequence visible in the findings, **Rule 5 has not been engaged with — it has been performed**. An empty Rule 5 is not neutral. It is a signal that the frame is invisible to the auditor, which is exactly the failure mode the rule exists to catch. The auditor who cannot name what their frame hid from them is the auditor most hidden from their frame. If the specific questions above produce only empty answers after genuine engagement, write that result and name why no alternative reading surfaces — that too is a finding.

### Orientation Obligations (investigatory)

The investigatory orientation is occasioned by *breakdown or apparent contradiction* — expectations were violated, something does not line up, and diagnosis is needed. The phrasing of I1–I4 below is **load-bearing and must not be paraphrased**. Each comes with a "why this matters" paragraph that grounds the obligation in the failure mode it is meant to catch.

- **I1 — Start from the discrepancy, not a theory.** Describe what was expected, what was delivered, and why those expectations are being treated as the standard — the choice of comparison point is already an interpretive act. *(Why this matters: investigations that start from a theory select evidence to confirm the theory. Investigations that start from the discrepancy remain open to evidence the theory is wrong. The gap between expectation and delivery is a starting orientation, not a neutral fact — name why the expectation is the expectation. In this audit, the explicit comparison points are (a) the 2026-04-08 predecessor audit's findings, (b) the f1-modeling vision-alignment initiative's shape, and (c) the user's stated concerns about deployment/distribution/adoption. None of these is a neutral measuring stick — name what each one assumes and what each one excludes.)*

- **I2 — Let the investigation guide artifact selection.** Don't mandate which artifacts to read in advance. Follow the evidence — if the discrepancy points to the planning stage, read planning artifacts. If it points to requirements, read requirements. The artifact chain is a finding, not an input. *(Why this matters: a pre-specified reading list encodes a hypothesis about where the failure lies. The investigation should discover where to read from what it finds, not from what the orchestrator specified. If the orchestrator pre-selected artifacts — see the "Suggested Starting Orientation" below — I2 is in tension with that pre-selection. **Surface the tension; do not silently honor the pre-selection.** The starting list is a starting list, not a closed read list. You are free to deviate if the evidence asks you to.)*

- **I3 — Present competing explanations.** For each finding, offer at least two interpretations. "The narrow initiative excludes deployment topology" could mean "the initiative is correctly scoped because deployment is downstream of substrate," OR it could mean "the initiative inherits an under-scoping the predecessor audit already flagged." Don't collapse to one. *(Why this matters: an investigation that presents a single explanation has stopped investigating. The criterion for closing an investigation is not "I found an explanation" but "the evidence rules out the alternatives." An explanation without ruled-out alternatives is a hypothesis, not a finding. Both the user's stance (narrow is too small) and Codex's best-case memo (narrow is justified) are hypotheses you must hold in tension until the evidence rules one out — or until you discover that both are partially right and the situation calls for a third reading.)*

- **I4 — Name the position of the investigation.** Every investigation is conducted from somewhere — with particular attunements, particular things it's prepared to notice, particular things it isn't. This isn't about cataloguing determinate "blind spots" as if they're hidden objects waiting to be found, but about acknowledging what this particular way of looking is oriented toward and what a differently-situated investigation would attend to. *(Why this matters: every investigator is embedded. Pretending otherwise produces the illusion of neutrality, and that illusion hides the frame from both the auditor and the reader. Naming the position is the minimum epistemic hygiene of situated inquiry — and it also gives the reader the information they need to decide how far to trust the investigation's framing. **You are running as Claude Opus 4.6, dispatched by an orchestrator that is also Claude Opus 4.6, in a session where the user has stated a stance. Name how that affects what you are prepared to notice.** A separate Codex audit of the same corpus would notice differently. A human philosopher of game design would notice differently. An adversarial reviewer would notice differently. Where are *you* looking from?)*

- **Show what remains unknown.** Not everything needs resolution. Explicit unknowns are findings — they map the edge of the investigation. *(Why this matters: the temptation at the end of an investigation is to close on a story. Resisting that temptation — and naming what the story cannot yet explain — is what distinguishes an investigation from a speculation. The user explicitly invited qualified, conditional judgments — including "the preparatory corpus is not yet strong enough to justify either conclusion." If that is what the evidence supports, write that.)*

- **Show how you navigated any tensions between obligations.** When investigatory obligations tension with cross-cutting obligations or with each other, the navigation itself is a finding. See the Composition Principle below. *(Why this matters: how an investigator resolves tensions reveals their working frame. Making that resolution explicit — rather than performing a clean synthesis — gives the reader the information they need to evaluate whether the navigation was sound. **If the tensions in this audit collapse cleanly, that is a red flag.** The framework was rewritten in Phase 57.4 specifically because clean collapse was the failure mode of the v1 type-family approach.)*

### Subject Obligations

**No subject is named for this audit at dispatch time.** Core Rules 1–5 plus the investigatory orientation obligations plus the cross-cutting obligations below are the full obligation set. If a subject becomes operative as the investigation proceeds — for example, if you find that the audit is really a `claim_integrity` audit of the narrow initiative's claims about canon alignment, or a `comparative_quality` audit of prix-guesser's preparation versus f1-modeling's, or a `process_review` of the methodology that produced the narrow initiative — then **name the subject explicitly in the output** and apply its obligations from that point forward. The shift is itself a finding worth recording.

For reference, the candidate subjects most likely to become operative mid-investigation, with their obligations from the audit-ground-rules.md table:

| Subject | Obligations |
|---|---|
| `claim_integrity` | Verify claims against citations; surface untyped load-bearing assumptions; trace dependency chains |
| `comparative_quality` | Define comparison axis explicitly; compare like with like; note what axis makes invisible |
| `process_review` | Compare execution against process spec/intent; examine methodology assumptions; check if process worked-as-designed vs. design is wrong |
| `artifact_analysis` | State corpus and why it's representative; look for patterns AND anti-patterns; note what the corpus excludes |

You may name more than one if the investigation calls for composition across subjects. The composition principle below tells you how to navigate the tensions that arise.

### Cross-Cutting Obligations

#### Chain integrity

> "When audit B uses audit A's finding as evidence, and audit A had a quality failure, audit B inherits the failure invisibly. This is the single most consequential failure mode in the discuss-phase session chain. **Obligation:** For each finding that depends on a predecessor audit's claim, re-verify that claim independently before incorporating it. State the re-verification or state why it was not done."

**Applicability is high here.** This audit has multiple predecessors:

1. **The 2026-04-08 pre-execution review** (`.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`, `CONVERGENCE.md`, `METHODOLOGY-REVIEW.md`, lane reports). It made strong claims — "Project artifacts (PROJECT.md, REQUIREMENTS.md, ROADMAP.md): NEED REVISION — three critical gaps identified before execution burns effort in the wrong direction." Those claims are load-bearing for this audit, because the narrow initiative's central claim ("the canon is already relatively well-aligned") is in tension with them. **You may not inherit the predecessor's claims as ground truth — and you may also question the predecessor's *recommendations* themselves.** For any predecessor finding you rely on, re-open the cited files yourself and re-verify the claim against the current state of the canon. **Three distinct outcomes are all legitimate findings** and the audit should treat them with equal seriousness:

   - The predecessor was right and the canon was revised accordingly. Verify the revision happened.
   - The predecessor was right but the canon was NOT revised. Surface this as a gap — possibly a serious one, possibly a minor one, depending on whether the recommendation was load-bearing for current Phase 01 readiness.
   - **The predecessor was wrong, OR its recommendation was right in spirit but should be addressed differently than the predecessor proposed, OR the project deliberately and correctly chose not to adopt the recommendation for principled reasons.** This third outcome is the one most likely to be missed by chain integrity applied naively. The 2026-04-08 audit was itself produced by a particular methodology (4 parallel lanes, 2 model passes) and surfaced 27+ recommendations plus Q1–Q6 strategic questions. Some of those recommendations may be principled to defer; some may be inappropriate to a private friends-only fan game even though they would be appropriate to a public-product project; some may be correct in substance but wrong in the specific shape the predecessor proposed (e.g., "the predecessor said add DEPLOY-01..05 as formal requirements, but the project chose to address the underlying concern through a different mechanism").

   For each predecessor recommendation you check, ask **both** "was it adopted?" *and* "should it have been adopted in the form the predecessor proposed?" The naive form of chain integrity treats the predecessor as authoritative and the present project as the thing being evaluated against it. The full form treats both as contestable claims, with the predecessor having the additional burden of being older (the canon may have moved) and being produced from a particular framing (the predecessor's framing may have been wrong for what the project actually is).

2. **Codex's task spec** (`phase-01-prep-quality-scope-audit-task-spec.md` in this same session directory). Codex authored a thoughtful investigatory task spec but did so from a particular framing — the framing of an external orchestrator dispatching to Claude. **Treat that task spec as an artifact under audit, not as a closed framing for this audit.** If you find that Codex's framing pre-decided something the investigation should hold open, name it.

3. **Codex's briefing** (`phase-01-prep-quality-scope-audit-briefing.md`). Codex labels this "a starting map, not a closed read list" and explicitly invites you to follow evidence wherever it leads. Honor that invitation — the briefing is one input among many.

4. **Codex's "best-case memo"** (`phase-01-prep-quality-scope-audit-best-case-minimal-alignment.md`). This is *deliberately one-sided advocacy* for the narrow-initiative position. Codex explicitly states it should be used as "an argument to test, not an answer to trust." Treat it that way: read it for the strongest possible version of the minimal-alignment case, then test each of its claims against the canon. Several of its claims are testable (e.g., "the highest-risk architectural seam has already been correctly identified"; "the open questions are bounded, not existential"; "the long-arc doctrine is already separated from current-scope work"). Test them.

**The chain integrity obligation creates a gate**: you may not carry forward a claim from any of these predecessors that you have not independently re-verified, or you must explicitly note that you did not and why.

#### Self-dispatch hygiene (modified from cross_model dispatch hygiene)

The standard dispatch-hygiene obligation (`audit-ground-rules.md` Section 3.3) addresses `cross_model` delegation, where prompts authored in one model's context can systematically bias another model's output. This audit is **self** delegation — same model class, same conversational context, same orchestrator. Cross-model framing contamination does not directly apply.

**However, framing contamination does not require crossing models.** It requires only that the dispatch prompt encode a stance the auditor will absorb without examining. The standard obligation is therefore extended here in modified form:

> **For self-delegated audits where the orchestrator has incorporated the user's stance into the task spec, verify that the user's stance is treated as an *input* to the investigation rather than as a *conclusion* the audit must reach. Audit your own engagement with the task spec for whether you are following evidence or following the orchestrator's framing.**

The user has stated, in their original invocation: *"I am not convinced personally by any worries regarding 'loss of momentum' and 'time-concerns', its better to get it done well and right than have to spend time fixing things later because its broken, written poorly, we haven't considered enough how we are to deploy at scale, or distribute, or advertise, or make it easy to adopt / share etc."*

This stance is **a starting orientation, not a conclusion**. Concretely:

- It is **not** the audit's job to confirm the user's stance.
- It **is** the audit's job to engage with the substance of the stance honestly. If the evidence supports the user's stance, say so. If the evidence supports the opposite stance, **say so**, even though saying so is in tension with the framing the user gave the orchestrator.
- It is **especially** the audit's job to consider whether time-pressure / momentum arguments could be valid in some specific dimension the user has not considered. The user explicitly said "we can thoroughly qualify and put conditions on our judgements" — the qualified, partial defense of the narrow initiative is a legitimate possible finding.
- If you write the user's stance back to them as a finding, you have not performed an audit. You have performed agreement.

**Note this self-dispatch hygiene obligation in your output. State explicitly whether you found yourself drifting toward the user's stance, and what you did about it.**

#### Framework invisibility

> "The obligations have I4 ('name the position of the investigation') but nothing that specifically asks: 'What does this audit's framework make invisible? What kinds of findings would not appear in this audit no matter how rigorously it was conducted?' **Obligation:** Name what your audit framework cannot see — not what you chose not to look at, but what the structure of the audit makes invisible."

**Relationship to I4 and Rule 5.** Framework invisibility is distinct from both. I4 names the investigator's position — *where they're looking from*. Rule 5 asks whether the audit's *classification* (subject × orientation × delegation) was the right frame. Framework invisibility asks the deepest version of the question: **what kinds of findings cannot appear in this audit at all, because of how the audit's scope was structured?** The distinction: I4 is about the auditor, Rule 5 is about the classification, framework invisibility is about the structural edges of what the audit can see no matter how well it's conducted.

**Ground framework invisibility in the specific question (copy verbatim):**

> *"Name a concrete finding that would not appear no matter how rigorously this audit was conducted, because of how this audit's scope was framed. If you can't name one, that's suspicious — the framework is probably hiding something from you that it's also hiding from itself."*

Concrete examples of what *might* be invisible to this audit's framing — not as a closed list, but as starting prompts:

- The audit is framed in terms of "narrow initiative vs. broader initiative" — but maybe the right answer is *"no initiative, just commit to a different overall approach"*, or *"the initiative is the wrong unit of work for this kind of question."*
- The audit is framed around the existing artifact corpus — but maybe the more important question is what's *not in any corpus at all* (e.g., user research, real friends as test stakeholders, content authoring practice, the actual experience of running a private F1 game night with friends to verify the core fantasy works).
- The audit is framed around Phase 01 readiness — but maybe Phase 01 itself is the wrong unit, and the question is whether the project should have phases at all in its current form, or whether it should commit to a real-world play test of an MVP before any further substrate work.
- The audit is framed in terms of "is the canon aligned?" — but maybe "aligned" itself is a measure that doesn't capture what matters (e.g., whether the canon's fictional friends-on-couch scenario corresponds to a real situation that real friends would actually want to participate in repeatedly).

These are starting prompts. The actual framework-invisibility finding must be something *you* identify in *this particular* audit's structure, with concrete grounding in how the audit was framed. Generic prompts about bias produce compliance theater.

---

## The Situation

### What the user asked

The user invoked `/gsdr:audit` from Claude Code with the following arguments (verbatim):

> "we are running an audit on this repo which has been initialized by codex, codex has also written a few briefing docs, and try to put forward its best argument for its position. We are here to critically, honestly, responsibly, thoroughly audit the repo and their claims. I am not convinced personally by any worries regarding 'loss of momentum' and 'time-concerns', its better to get it done well and right than have to spend time fixing things later because its broken, written poorly, we haven't considered enough how we are to deploy at scale, or distribute, or advertise, or make it easy to adopt / share etc. our response doesn't have to be an outright rejection or approval, we can thoroughly qualify and put conditions on our judgements, for example, rethinking what precisely ought to be considered in the vision alignment initiative which is based off of what the f1-modeling project here in '/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04' is doing."

The user subsequently clarified, mid-orchestration, that the four `01-XX-PLAN.md` files in `.planning/phases/01-authored-round-contract/` are being deleted as stale residue and should not be treated as load-bearing artifacts. **Do not interpret the worktree-vs-state mismatch involving those plan files as evidence.** Codex's briefing (line 70) framed it as interpretively load-bearing; with the deletion, that frame no longer applies.

### What the orchestrator inferred

Three things in the user's stance shape the situation:

1. **Time-pressure / momentum concerns are explicitly de-prioritized as a justification for narrowness.** This means that any defense of the narrow initiative that rests on "but doing more would slow us down" is flagged in advance as not load-bearing for this audit. Defenses that rest on "the narrow scope is correct because the broader questions are genuinely closed" remain valid and must be tested on their substance.

2. **Deployment, scale, distribution, advertising, and adoption are explicitly named as concerns the user does not want pre-decided as out-of-scope.** Several of these were flagged in the 2026-04-08 predecessor audit as critical gaps (Lane 3: distribution; Lane 2: design contract for watchability/host-screen; Lane 4: identity question of "F1 GeoGuessr vs F1 Jackbox"). The narrow vision-alignment initiative's `Out of scope` list at `.planning/initiatives/vision-alignment-2026-04/README.md` lines 59–66 explicitly excludes "frontend framework choice, room runtime and authority implementation, deploy topology decisions, public/share-by-link/public-spectator posture, adjacent F1 mode expansion, in-app authoring UI." There is at least surface tension between the user's stated concerns and the narrow initiative's stated scope. Test whether that tension is real and whether it is decisive.

3. **The f1-modeling vision-alignment initiative is named as a comparison standard for "what precisely ought to be considered in the vision alignment initiative."** This is a comparative-quality dimension the audit is asked to engage with — but only with explicit care, because comparing-like-with-like is hard when the projects differ in domain, scale, ambition, and stage. See the Investigatory Questions section below.

### The state of play

- **Project state.** `.planning/STATE.md` line 30 says "Status: Replanning required before execution"; line 24 names "Phase 1 — Authored Round Contract" as current focus; pending todos include "Rerun discuss-phase for Phase 1 against refreshed canon before execution" and "Replan Phase 1 from the refreshed steering brief rather than using the archived superseded bundle."

- **Canon docs (the substrate the narrow initiative declares aligned).** `.planning/PROJECT.md` (191 lines), `.planning/LONG-ARC.md` (154 lines), `.planning/ROADMAP.md` (205 lines), `.planning/REQUIREMENTS.md` (191 lines), `.planning/STATE.md` (81 lines). Total: ~822 lines of canonical text. PROJECT.md was last updated 2026-04-11. Read these to test whether they actually converge on the same product center, or whether they preserve enough open surface that the narrow initiative's premise of "already aligned" is shakier than it claims.

- **The narrow initiative under audit.**
  - `.planning/initiatives/vision-alignment-2026-04/README.md` (89 lines)
  - `.planning/initiatives/vision-alignment-2026-04/PLAN.md` (123 lines)
  - `.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md` (125 lines)
  - Total: 337 lines. The README directly invokes f1-modeling as a contrast: "This project does **not** currently have the same kind of wide, cross-domain architectural uncertainty that justified the larger `f1-modeling` initiative shape." (lines 24–25). The PLAN proposes a minimum shape of 2 research calls + 1 deliberation + 1 decision anchor.

- **The f1-modeling comparison initiative.** Located at `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/`. **Important framing correction up front: do not measure this against prix-guesser's narrow initiative by raw artifact size.** F1-modeling's initiative is large because it has been *executing for several waves* — wave 1 research, wave 1.5 envelopes, wave 2A deliberation, wave 2B-i and 2B-ii deliberations, gate reviews, cross-model audits, decision anchors. Of course it has produced more artifacts than a freshly authored, not-yet-executed scaffold for a different project. **Size is not the comparison axis.** The meaningful comparison is *plan structure and expansion provisions*: what does each initiative's PLAN allow as legitimate findings, what review gates does it specify, what permission does it give to grow, and what threshold triggers that growth.

  Read the f1-modeling artifacts the user explicitly named as the comparison material:

  - `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/README.md` — initiative framing, trigger, scope, completion criteria
  - `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/PLAN.md` — wave structure, review gate questions, iteration norms, prompt-file authorship strategy
  - `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md` — the methodology document that the prix-guesser RESEARCH-PRINCIPLES.md is a derivative of (see the methodological-inheritance observation below)
  - At least one deliberation as an example — the orchestrator suggests `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/deliberations/01-backend-boundary-architecture.md` (the full deliberation, ~600 lines, shows what a wave 2 output looks like in practice including its "Gray Areas Still Unresolved" tagged DEFER/FOLLOW-AND-MARK/REVISIT-LATER section, "Closure Analysis", and 1/3/5-year trajectory tradeoffs) and its companion `deliberations/01-decision-anchor.md` (the compact one-paragraph-per-contract handoff that subsequent deliberations consume — this is structurally the same shape as the "decision anchor" prix-guesser's PLAN proposes to produce). Sample one or both as the situation requires.

  **A specific methodological observation worth testing.** The two RESEARCH-PRINCIPLES files are not equivalent. Prix-guesser's vision-alignment RESEARCH-PRINCIPLES.md is 125 lines; f1-modeling's is 426 lines. F1-modeling's file says "These principles critically inherit from methodological work done on the Prix Guesser project (2026-04), which learned through iteration that premature solution-space foreclosure is a methodological error." So the inheritance is *prix-guesser → f1-modeling*, with f1-modeling having "adapted and extended" the principles. Yet the *current* prix-guesser vision-alignment RESEARCH-PRINCIPLES.md drops several things f1-modeling kept and elaborated:

  - **Trajectory analysis (1-year / 3-year / 5-year horizons + doors opened / doors closed).** Notably absent from prix-guesser's, even though prix-guesser has an explicit 3-milestone long arc in PROJECT.md and LONG-ARC.md and the questions Phase 01 is freezing are exactly the kind that should be tested across that arc.
  - **Precedent analysis with specific named cases** (not generalities). Notably absent, even though prix-guesser has explicit named precedents (`benlikescode/geohub`, `RasterCrow/Geo-Locator`, `xchau/react-geofindr`, `PartyKit`, `Colyseus`, `boardgame.io`).
  - **Calibrated confidence markers** (Known / Likely / Plausible / Speculative / Unknown). Notably absent.
  - **Path of Inquiry section requirement** (branching paths considered, pursued, abandoned, reframed) and **Dependencies and Relations section requirement** as required output sections.
  - **Hypothesis testing as a distinct mode** alongside terrain mapping, deliberation, and synthesis.
  - **Reframing permission section** (the explicit permission to answer a different question than the one asked, when the evidence justifies it).
  - **The detailed gray-area handling framework with worked examples** (prix-guesser's mentions defer/follow-and-mark/revisit-later but is much briefer about when each applies).
  - **The 16-section research and 13-section deliberation required structures.**

  Test whether each of these omissions is principled (the smaller scope of prix-guesser's narrow initiative legitimately doesn't need them, or they were dropped in deliberate simplification with reasoning) or whether they were lost as collateral damage of the narrow scoping. **A truncation of methodology that looks innocent at the principle level may be exactly the mechanism by which the narrow initiative would fail to surface what it should surface.** A prix-guesser deliberation that doesn't do trajectory analysis is one that cannot answer "will this authored-substrate decision hold across Milestone 1, 2, and 3," which is exactly the kind of question Phase 01 is supposed to be answering.

  **What this comparison can and cannot show.** It can show what prix-guesser's narrow initiative explicitly invites, permits, and forbids. It can show whether the initiative inherits the methodological vocabulary that proved necessary in f1-modeling's actual execution. It cannot show — without prix-guesser actually running its initiative — whether the smaller scope will turn out to be enough or not. The right finding from this comparison may be a statement of risk and a proposed expansion provision, not a verdict on whether the narrow initiative will succeed or fail.

- **The 2026-04-08 predecessor audit.** Located at `.planning/audits/2026-04-08-pre-execution-review/`. Includes SYNTHESIS.md, CONVERGENCE.md, METHODOLOGY-REVIEW.md, lane reports for plan-quality, frontend-design, stakeholder-distribution, and multi-milestone-vision (Opus and GPT passes for each). Its overall verdict: "**Phase 1 plans: READY WITH CAVEATS** — commit the uncommitted diffs, proceed to execution. **Project artifacts (PROJECT.md, REQUIREMENTS.md, ROADMAP.md): NEED REVISION** — three critical gaps identified before execution burns effort in the wrong direction." It made 27+ recommendations and surfaced 6 strategic questions for human deliberation. Test whether the canon has been revised in the ways the predecessor audit asked, or whether the narrow initiative is asserting alignment that has not actually been earned through the predecessor's recommended revisions.

- **Phase 01 live artifact set (NOT including the deleted plan files).**
  - `.planning/phases/01-authored-round-contract/01-CONTEXT.md` (179 lines)
  - `.planning/phases/01-authored-round-contract/01-DISCUSSION-LOG.md` (76 lines)
  - `.planning/phases/01-authored-round-contract/01-RESEARCH.md` (418 lines)
  - `.planning/phases/01-authored-round-contract/01-VALIDATION.md` (80 lines)
  - **Ignore** `01-01-PLAN.md` through `01-04-PLAN.md` — these are being deleted as stale residue per the user's mid-orchestration clarification.
  - There is also a superseded archive at `superseded/2026-04-11-pre-rerun-overreach/` which contains the prior planning bundle that was cleared. The narrow initiative's best-case memo treats the existence of this archive as evidence of *successful course correction*. Test whether that interpretation is warranted by the contents of the archive.

- **Recent commit history (worth reading for context, not as authoritative truth).** `1a66b78` loaded long-arc doctrine into discuss workflows; `c553955` cleared the live Phase 01 bundle and retained a superseded archive; `c97d24a` introduced the current Phase 01 CONTEXT and DISCUSSION-LOG; `5189d4b` updated STATE.md; `2ab8491` added the current Phase 01 RESEARCH; `b34cba7` added the current Phase 01 VALIDATION. There is also a revert sequence: `33131c9` (record planned status), `e9350da` (add starter pack fixture plan), then `d67551b` and `7203964` reverting both. The reverts are evidence that something was tried, found to be premature, and rolled back. **Do not assume the reverts represent successful course correction without verifying** — a revert can represent "we corrected the mistake" or "we backed off but the underlying confusion remains."

- **Working tree diffs.** `.planning/config.json` shows `_auto_chain_active: false` (was `true`), and `scripts/setup-portable-gsd.sh` reapplies repo-local reasoning defaults into `.codex/config.toml`. These are tooling/runtime changes. The best-case memo argues these reduce procedural noise and therefore strengthen the case for narrow alignment. Test whether tooling improvements actually translate to product-alignment improvements, or whether they are orthogonal.

### What you may NOT inherit as ground truth

- The narrow initiative's claim that the canon is "relatively well-aligned." This is the central claim under audit. Verify it directly against the canon.
- The 2026-04-08 audit's claim that the canon "needs revision." This is also a claim about the canon. Verify it directly against the canon as it exists *now* — the audit was 3 days ago, and the canon may have been revised since.
- Codex's briefing's framing of which artifacts are high-signal. Read the briefing for orientation, then read what the evidence actually points to.
- Codex's best-case memo's individual sub-claims about what is "already known" or "already aligned." Each of these is testable. Test them.
- The user's stance that the narrow initiative is too small. The user's stance is the orchestrator's framing input, not a conclusion the audit must reach.
- The orchestrator's (this task spec's) implicit suggestion that comparison with f1-modeling will be unfavorable for the narrow initiative. The comparison may turn out to favor the narrow initiative — for example, if the projects differ in ways that make the f1-modeling shape inappropriate for prix-guesser. Test the comparison; do not pre-decide it.

---

## Investigatory Questions

These are the questions the orchestrator believes the investigation should engage. They are **not** a closed list. You are free to add, drop, or reframe them as the investigation reveals which questions are actually load-bearing.

### Q1 — The substance of canon alignment

What in the actual canon (PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md) supports the narrow initiative's claim that "the broader product posture is already relatively well-aligned"? What in the actual canon cuts against that claim? Is the apparent coherence *earned convergence* (the same questions were asked in different ways and got the same answers, stress-tested against alternatives) or *repeated assumption* (the same framing was authored once and copied across documents without independent verification)? The best-case memo names this as "the most important vulnerability" in the minimal-alignment argument — engage with it directly.

### Q2 — Chain integrity vs. the predecessor audit

The 2026-04-08 audit said the canon needs revision. The narrow initiative says the canon is aligned. **Both cannot be fully true.** Which is correct as of now (2026-04-11)? Specifically:

- Has DEPLOY-01..05 been added to REQUIREMENTS.md? (Lane 3 of the predecessor audit explicitly proposed these as new requirements.)
- Has the "F1 GeoGuessr vs F1 Jackbox" identity question (predecessor audit Q2) been resolved? If yes, where is the resolution recorded? If no, why is the narrow initiative excluding this from scope?
- Has the "watchability is load-bearing but undefined" gap (predecessor audit Lane 2 convergent finding) been operationalized? If yes, where? If no, is operationalization deferred to Phase 3.1, and is that deferral justified or evasion?
- Has the hierarchical-vs-flat answer target question (predecessor audit Lane 4 GPT-unique, named "THE most important architectural decision" in the audit) been resolved in the canon, in the Phase 01 research, or anywhere? Is it inside the narrow initiative's scope or outside?
- Has the Colyseus-vs-PartyKit decision been made? (The predecessor audit said this is a distribution decision, not a neutral runtime choice.) The narrow initiative explicitly excludes "room runtime and authority implementation" from scope. Is that exclusion correct or evasive?
- Has the Phase 3.1 (UI-SPEC) inserted-phase recommendation actually been integrated into ROADMAP.md, or is it a phantom integration?

For each predecessor finding you check, **state your re-verification method and what you found**. Do not say "the predecessor found X" without checking whether X is still true.

### Q3 — The f1-modeling comparison

The user explicitly requested comparison with f1-modeling. Engage with this question carefully:

- **Define the comparison axis explicitly.** What dimension are you comparing? Volume of alignment work? Methodological rigor? Number of distinct decisions made? Coverage of question types? The comparative_quality subject obligation says "Define comparison axis explicitly; compare like with like; note what axis makes invisible." Honor it.
- **Note what about the projects themselves makes the comparison hard or easy.** Prix Guesser is a private F1 fan game; f1-modeling is (apparently from the docs) a serious engineering-and-education platform with computational backends, visualization at scale, and educational content architecture. These are different domains with different stakes. Some of f1-modeling's alignment work is appropriate to its domain and would be inappropriate for a private fan game; some of it might be appropriate to *any* serious project in its starting phase. Distinguish the two.
- **The user's framing is "what precisely ought to be considered in the vision alignment initiative which is based off of what the f1-modeling project ... is doing."** This phrasing assumes that f1-modeling's approach is the standard prix-guesser's narrow initiative is *based off of*. The narrow initiative's README confirms this: "This project does **not** currently have the same kind of wide, cross-domain architectural uncertainty that justified the larger `f1-modeling` initiative shape." So prix-guesser's narrow initiative is explicitly a *narrowing* of the f1-modeling pattern. The question is whether the narrowing is principled (the projects differ in ways that justify it) or reflexive (the same starting framework was applied with less ambition).
- **What is at stake in this comparison.** If prix-guesser's narrow initiative inherits f1-modeling's methodology but applies less of it, the question is whether the methodology's value scales linearly or step-wise. F1-modeling's RESEARCH-PRINCIPLES.md (which prix-guesser inherits) lists non-foreclosure, hidden-assumption surfacing, trajectory analysis, gray-area handling, path-of-inquiry traceability, and deferral as legitimate outcomes as core principles. Did prix-guesser's narrow initiative actually preserve these principles, or did it preserve them in name while truncating them in practice?

### Q4 — The deployment / distribution / adoption frame the user named

The user asked to consider "how we are to deploy at scale, or distribute, or advertise, or make it easy to adopt / share." The narrow initiative's `Out of scope` list explicitly excludes "deploy topology decisions, public/share-by-link/public-spectator posture." The 2026-04-08 audit's Lane 3 made distribution a critical gap.

- Where in the canon (or in any planning artifact) are deployment, distribution, and adoption questions being treated? Are they being deferred with explicit closure criteria, or being deferred in the loose sense of "we'll think about that later"?
- The product is described in PROJECT.md as "private-only, unofficial fan project" (line 5) and "private-only fan project" with public-release "out of scope" (line 30). Is this a substantive product decision or a way of declaring distribution out-of-scope by definition? Test whether the "private-only" framing is doing analytic work or evasive work.
- The user asked specifically about "advertising" and "make it easy to adopt / share." These are barely visible in the current canon. Is that absence principled (private-only doesn't need adoption) or is it evasive (the friends who are supposed to play this game are real adoption targets, and the canon's silence about how they actually find out about it and join is a real gap)?

### Q5 — The shape of the right next step

If the narrow initiative is justified, what is the strongest version of "this is enough"? If broader alignment is needed, what is the minimum broadening that would be principled? If neither — if the preparatory corpus is not yet strong enough to justify either the narrow or a broader initiative — what is the actual next step?

**One legitimate finding is "the right next step is not an initiative at all."** For example: "the right next step is to play one round of the proposed game with three real friends in a real living room and see whether the core fantasy works at all, before any further substrate work." Or: "the right next step is to write down the exact question that distinguishes the F1-GeoGuessr identity from the F1-Jackbox identity and answer it before any further canon work." Or: "the right next step is to commit the canon as it stands, run Phase 01 with its current uncertainties, and treat the first execution as the alignment work." The user has explicitly invited qualified, conditional, and reframing answers. Use the permission.

### Q6 — What this audit cannot see

Per the framework-invisibility obligation above. Name something concrete this audit's framing cannot bring into view, no matter how rigorously you conduct it.

---

## What Must Appear in the Output

The obligations are addressed through engagement, not by filling labeled containers. However, the following structural elements are mandatory:

- **All obligations addressed in substance.** Core Rules 1–5, investigatory I1–I4 plus the two additional obligations, chain integrity, self-dispatch hygiene, framework invisibility — all woven into the narrative wherever they emerge naturally.

- **A clear engagement with the user's stance** that explicitly distinguishes "I am following evidence" from "I am following the framing the user gave the orchestrator." The self-dispatch hygiene obligation is satisfied by this explicit reflection, not by performing distance from the user.

- **A structured re-verification of predecessor audit claims** for each predecessor claim you rely on. State your re-verification method (file:line citations) and what you found.

- **A structured comparison with f1-modeling** that names its axis, compares like with like, and acknowledges what the axis makes invisible. The comparison may be brief if the projects turn out to be too different to compare meaningfully — but if so, **explain what you tried and why it failed**, do not silently drop the comparison.

- **A "Position of the Investigation" section** addressing I4. Where are you looking from? What is this Claude-on-Claude self-dispatch prepared to notice and what is it not?

- **A "How I Navigated Tensions" section.** If no tensions emerged, write that, and consider whether the absence of tensions is evidence the obligations were too easily satisfied (RESEARCH.md Pitfall 3 — clean collapse is the failure mode the framework was rewritten to catch). If tensions emerged, name them concretely per the Composition Principle below and show how you navigated each.

- **A full Rule 5 frame-reflexivity section** answering the three specific grounding questions verbatim. Anti-performativity warning above applies in full.

- **A "What the Obligations Didn't Capture" section** — mandatory in every audit output per the audit conventions. This is the structural opening for excess: findings that do not fit any obligation, any template, any expected shape. If this section is consistently substantial across multiple audits, it is evidence that the framework needs a new obligation, a new subject, or a new axis.

- **A practical conclusion** that says one of:
  - The narrow vision-alignment initiative is justified as currently scoped, and Phase 01 planning may proceed after the initiative completes its currently-planned 2 research calls + 1 deliberation + 1 decision anchor.
  - The narrow initiative should widen in specific named ways before Phase 01 planning proceeds — list the specific widenings and why each is load-bearing.
  - The preparatory corpus is not yet strong enough to justify either the narrow or a broadened initiative — name the specific missing pieces and the smallest concrete next step that would make the question answerable.
  - **Or some fourth shape the investigation surfaces** that the orchestrator did not anticipate. (E.g., "the right next step is not an initiative at all." Or "the right shape is a deferral of the canon question entirely until a play-test happens.") If you reach a fourth shape, name it explicitly as a reframing and explain why it's the actual answer.

- **A list of the strongest counter-arguments to your conclusion** and your honest assessment of how decisive each is. This is part of I3 — competing explanations are not just a finding format, they are the criterion for closing on a conclusion. If you cannot name the strongest counter-arguments to your own conclusion, you have stopped investigating.

---

## Composition Principle (read if tensions emerge)

Obligations from different axes compose into a flat list. They do not form a hierarchy. When obligations tension against each other in this audit, you must not pick a winner. You must:

1. **Name the tension.** Say what the two (or more) obligations are and how they pull differently *in this situation*. Not abstractly — concretely. Example specific to this audit: "I2 says let the investigation guide artifact selection, but the orchestrator pre-listed predecessor audits in chain integrity, and following I2 would mean possibly skipping some of those if the evidence didn't ask for them. The chain integrity obligation says re-verify each predecessor claim before relying on it — but only the claims you actually rely on. So I2 and chain integrity don't tension as long as I2 is the *primary* artifact selector and chain integrity activates only on the predecessors I2 leads me to. Resolved by reading I2's selection first and applying chain integrity only on the subset I2 surfaces."

2. **Name what about the situation creates the tension.** The tension is not abstract; it is occasioned by particulars. What about *this* audit makes the obligations tension? Another investigation might have no tension at all. (Example: in the audit above, the tension exists because the orchestrator pre-listed multiple predecessors in chain integrity. An audit with one or zero predecessors would have no such tension.)

3. **Show how you navigated it.** Responsive to both demands, not cleanly picking one side. The navigation is part of the finding — the reader needs to see both the reasoning and the fact that the reasoning was not a clean resolution.

4. **The resolution emerges from engagement** with the situation, not from a precedence rule applied in advance. If you can write down in advance what would resolve every tension between these obligations, you haven't understood the principle — or the obligations can be collapsed to one, which is evidence that the framework is over-specified.

This is a **hermeneutic principle, not an algorithmic one.** Per `audit-taxonomy-three-axis-obligations.md` line 164: "If you find yourself cleanly ignoring one obligation in favor of another, you've likely stopped engaging with the tension." The sign of engaged composition is not a clean resolution — it is a navigated one, where both obligations leave traces in the finding.

If your output contains zero tensions encountered — *especially* if it ends in a clean conclusion that satisfies all obligations without any of them visibly competing — read your output again and ask whether you smoothed the tensions out or whether they really weren't there. The honest answer is more valuable than the polished one.

---

## Suggested Starting Orientation (NOT a closed read list)

This is a suggestion for where to start. You are explicitly free to deviate per I2.

1. Read `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md` — the canon the narrow initiative declares aligned. Read them with Q1 in mind: is this earned convergence or repeated assumption?
2. Read `.planning/initiatives/vision-alignment-2026-04/README.md`, `PLAN.md`, `RESEARCH-PRINCIPLES.md` — the narrow initiative under audit. Note specifically what its Out of scope list excludes and what its In scope list includes.
3. Read `.planning/phases/01-authored-round-contract/01-CONTEXT.md`, `01-RESEARCH.md`, `01-VALIDATION.md`, `01-DISCUSSION-LOG.md` — the live Phase 01 substrate work. Test whether 01-RESEARCH.md explores the option space or collapses prematurely toward one shape. Test whether 01-CONTEXT.md is a strong steering brief or an early closure of substrate questions.
4. Read `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`. Identify which of its claims you actually need to rely on for your investigation. For each one, re-verify against the current state of the canon. Also read `CONVERGENCE.md` and `METHODOLOGY-REVIEW.md` if your investigation needs them.
5. Read `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-task-spec.md` (Codex's earlier task spec — predecessor in this audit's chain) and `phase-01-prep-quality-scope-audit-best-case-minimal-alignment.md` (Codex's one-sided advocacy memo). Treat both as artifacts under audit.
6. Sample `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/README.md`, `PLAN.md`, and at least one of the codex-call files (e.g., `codex-call-1A.md` or `codex-call-2B-i.md`) plus `BOUNDARY-CONTRACT-MEMO.md` to understand the f1-modeling shape *as it actually executed*, not as it was planned. The PLAN may not be a fair comparison; the executed wave artifacts are.
7. Read `.planning/phases/01-authored-round-contract/superseded/2026-04-11-pre-rerun-overreach/README.md` to understand what was archived and why. Test whether the archive represents successful course correction or unstable planning.
8. The four files at `.planning/phases/01-authored-round-contract/01-01-PLAN.md` through `01-04-PLAN.md` are being deleted. **Do not read them as authoritative.** If they still exist when you read this, treat them as stale residue.
9. The runtime/tooling diffs in `.planning/config.json` and `scripts/setup-portable-gsd.sh` are low-priority for this audit's question. Sample them only if the investigation surfaces a reason to.

You may also need to look at things this list does not anticipate. That is the I2 obligation in action. Follow the evidence.

---

## Output File

Write the audit output as markdown to:

`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-2-output.md`

Do not return a conversational summary instead of the file. Write the file to the path above, then exit. The orchestrator will read the file from disk and report the result to the user.

Length: as long as the situation requires, no longer. The obligations are satisfied by substance, not by length. A short audit that addresses every obligation honestly is better than a long audit that performs each one without engaging it.
