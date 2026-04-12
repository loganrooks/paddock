---
date: 2026-04-11
wave: 3
lane: synthesis
audit_subject: no-subject
audit_orientation: investigatory
audit_delegation: self
auditor_model: claude-opus-4-6
agent_type: gsdr-auditor
scope: "Compose the findings of the 8 Wave 1 and Wave 2 lane outputs (1A, 1B, 1C, B2-Opus, B2-Sonnet, B3, B4, B7) into the parent audit's final output (`phase-01-prep-quality-scope-audit-2-output.md`). The synthesis is not a fresh investigation — it is a composition task that honors the parent audit's obligations, holds competing lane readings in tension, tests the orchestrator's emerging conclusion against the lane evidence, and produces a practical conclusion in one of the four shapes the parent task spec named (or a fifth shape the synthesis surfaces). Separately, the synthesis produces a meta-comparison of the B2 Opus-vs-Sonnet twinned lanes as a methodological deliverable for future audit dispatches in this project."
triggered_by: "wave-3 dispatch after Review Gate 2, after B7 supplement completed; user chose Path A (B7 then synthesis) at the pause state documented in CLAUDE-SESSION-HANDOFF.md"
parent_task_spec: phase-01-prep-quality-scope-audit-2-task-spec.md
predecessor_lanes:
  - wave-1-lane-1a-canon-integrity.md
  - wave-1-lane-1b-methodological-inheritance.md
  - wave-1-lane-1c-external-gap-research.md
  - wave-2-lane-b2-opus-authoring-sustainability.md
  - wave-2-lane-b2-sonnet-authoring-sustainability.md
  - wave-2-lane-b3-distributed-methodology.md
  - wave-2-lane-b4-f1-legal-carveout-citation.md
  - wave-2-lane-b7-f1-legal-ambiguity.md
ground_rules: "core+investigatory+chain+self-dispatch-hygiene+framework-invisibility+synthesis-chain-integrity"
tags:
  - wave-3
  - synthesis
  - investigatory
  - opus
  - gsdr-auditor
  - parent-output
output_files:
  - phase-01-prep-quality-scope-audit-2-output.md
---

# Wave 3 — Synthesis Task Spec

**You are running as gsdr-auditor on Claude Opus 4.6.**

**Classification:** no named subject × investigatory × self (inherited from the parent audit `phase-01-prep-quality-scope-audit-2-task-spec.md`). Your job is to compose the 8 Wave 1 and Wave 2 lane outputs into the parent audit's final output file, honoring the parent's obligations at the composition layer rather than the investigation layer.

**Model selection rationale**: Opus is non-negotiable for this synthesis. You are holding 8+ lane outputs (including one controlled twin-pair) in tension, characterizing a third pattern under uncertainty, framework-invisibility on deeply interpretive questions, and producing a practical conclusion in a situation where the orchestrator's current read is explicitly a hypothesis for the synthesis to test (not a pre-decided outcome). This is maximum-stakes hermeneutic composition.

**Agent-type rationale**: gsdr-auditor because the obligations are audit obligations, not research. You do not need WebFetch — B7 already did the external web work, and no further external research is in scope. You need discipline, not tools.

---

## What This Synthesis Is (and Is Not)

### What it IS

- **A composition task.** You compose what 8 lane outputs already produced. Lane outputs are the primary evidence base; you are not re-investigating the canon from scratch.
- **A judgment task.** You produce the practical conclusion of the parent audit, in one of the four shapes the parent task spec named (see "Practical Conclusion Shape" below) — or a fifth shape if the lane evidence surfaces one.
- **A meta-comparison task.** The Wave 2 B2 controlled twin-pair (B2-Opus vs. B2-Sonnet) is a methodological deliverable that must be analyzed separately from the substantive authoring-sustainability findings, because it is load-bearing for future audit dispatches in this project.
- **A chain-integrity task applied to lane outputs.** Every load-bearing claim from any lane that you incorporate into your synthesis must be independently re-verified against its source before incorporation. The 2-of-8 orchestrator task-spec error rate seen in Wave 1 is evidence that lane outputs are not infallible transmission channels; lane outputs have their own error rates, and some lanes already caught and corrected predecessor lanes (B7 modified Lane 1C's "strongest defense" claim and contradicted Lane B4's minimum viable text).
- **A framework-invisibility task at the composition layer.** What does the composition frame itself make invisible? The synthesis can inherit the lanes' blind spots silently unless you name them.

### What it is NOT

- **Not a re-investigation.** You do not re-verify the full canon against the predecessor 2026-04-08 audit. Lane 1A did that. You may spot-check specific claims from Lane 1A that you rely on, but you are not re-running Lane 1A.
- **Not a consensus-builder.** You do not resolve lane disagreements by averaging them. Where lanes disagree, the disagreement itself may be a finding (e.g., B2-Opus and B2-Sonnet converged on substance but differed on framing — this is the meta-finding, not a problem to solve).
- **Not a prisoner of the orchestrator's emerging read.** The `CLAUDE-SESSION-HANDOFF.md` file contains the orchestrator's "Emerging Audit Conclusion" section. That section is explicitly a hypothesis for you to test, not a pre-decided outcome. If the lane evidence supports a different conclusion, write the different conclusion. If the lane evidence converges with the orchestrator's read, name the convergence and say why.
- **Not constrained to the lane questions.** The lane questions shaped what each lane produced, but the synthesis composes across questions. If the right conclusion requires crossing question boundaries, cross them.

---

## Epistemic Ground Rules (copied verbatim from parent task spec, DC-2 discipline)

The parent audit's obligations apply to the synthesis at full strength. They are copied below in full so that this task spec stands alone without requiring you to re-read the parent task spec's obligations section. Where the synthesis has additional obligations (lane-chain-integrity, meta-comparison, orchestrator-error-rate), they are named in the **Synthesis-Specific Obligations** section after the inherited obligations.

### Core Rules (every audit)

1. **Every factual claim cites file:line and quotes the relevant passage.** Do not assert what a file contains without opening it. Do not summarize without quoting. For synthesis, this applies at two layers: (a) when you cite a lane output's finding, cite the lane file and line number and quote the finding; (b) when you incorporate a finding as a load-bearing synthesis claim, also cite the underlying source file the lane cited (re-verify the chain, don't accept lane citations blindly). Example: "Lane B7 at `wave-2-lane-b7-f1-legal-ambiguity.md:51` states 'F1's text contains no definition of "motorsport simulator."' B7's methodology at lines 59–67 describes two independent WebFetches confirming this; I am accepting this claim because the methodology is rigorous, and I have not re-fetched F1's guidelines myself."

2. **For every finding, BEFORE writing it, ask "What would disconfirm this?" and CHECK.** This is not a rhetorical question. For synthesis, disconfirmation often lives in other lane outputs — if you are about to claim "the narrow initiative should add three PLAN additions," first ask whether any lane output provides evidence that adding them would be inappropriate or that the additions B3 identified as absent are compensated for somewhere else the orchestrator's read did not see. Actually check the other lanes for the disconfirming evidence before closing on the claim.

3. **Distinguish what you measured from what the measure captures.** Every composition is a proxy. Name the gap between "what the 8 lanes collectively produced" and "the actual state of prix-guesser's preparatory work." Lane outputs measure what 8 parallel and sequential auditors surfaced under their specific framings; they do not measure everything about the project.

4. **Rule 4 (escape hatch): What did you encounter that these ground rules didn't prepare you for?** Address in the mandatory **What the Obligations Didn't Capture** section. For synthesis, this rule is particularly important because composition tasks can surface meta-findings about the audit framework itself that lane-level rules do not anticipate. E.g., if the synthesis surfaces something about how audit chains propagate errors or how twin-pair comparisons expose model-class dependencies, that finding probably does not fit any lane-level obligation category.

5. **Rule 5 (frame-reflexivity): Did the framing shape what you found?** For investigatory orientation at the synthesis layer, Rule 5 is a **full section**. Answer these three grounding questions verbatim (do not paraphrase):

   1. *"If this synthesis had been classified as a different subject (e.g., `process_review` instead of no-subject, or `claim_integrity` instead of no-subject, or `comparative_quality` instead of no-subject), what would it have looked for that you didn't? What findings would that synthesis have produced that yours doesn't?"*
   2. *"If this synthesis had been classified with a different orientation (e.g., `standard` instead of `investigatory`), what would it have held open that you closed? What would it have investigated that you accepted?"*
   3. *"What about the current classification shapes what you are prepared to notice and what you are not? Name one concrete example."*

   **Anti-performativity warning.** A Rule 5 section that reads "I considered my biases" without concrete consequence is compliance theater. Name something specific about the synthesis framing that pushed you toward or away from a specific finding visible in the composition itself.

### Orientation Obligations (investigatory)

The investigatory orientation is occasioned by *breakdown or apparent contradiction* — expectations were violated, something does not line up, and diagnosis is needed. The phrasing of I1–I4 below is **load-bearing and must not be paraphrased**. Each comes with a "why this matters" paragraph that grounds the obligation in the failure mode it is meant to catch.

- **I1 — Start from the discrepancy, not a theory.** Describe what was expected, what was delivered, and why those expectations are being treated as the standard — the choice of comparison point is already an interpretive act. *(Why this matters for synthesis: an investigation that starts from a theory selects lane findings to confirm the theory. The synthesis starts from a discrepancy — the user's concern that the narrow initiative might be under-scoped, vs. the narrow initiative's claim that the canon is aligned. The 8 lanes tested both framings. Your synthesis should start from the discrepancy the lanes addressed, not from the orchestrator's current read of where the findings compose. The orchestrator's "Emerging Audit Conclusion" is a theory; it selects evidence to confirm itself. Start from the user's concern vs. the narrow initiative's claim, hold both open, and let the lane evidence resolve or complicate the discrepancy.)*

- **I2 — Let the investigation guide artifact selection.** Don't mandate which artifacts to read in advance. Follow the evidence — if the synthesis points to a specific lane output that needs deeper engagement, read that lane more thoroughly. If it points to a canon file a lane cited but you want to verify, read the canon file. The artifact chain is a finding, not an input. *(Why this matters for synthesis: a pre-specified reading order (read 1A first, then 1B, etc.) encodes a hypothesis about how the findings compose. The synthesis should let the composition emerge from engagement with the evidence, not from the orchestrator's pre-specified order. If you find yourself reading lanes in the order they were produced and then writing the synthesis in that order, you may be honoring dispatch chronology rather than composition logic. If a later lane (B7) changes how an earlier lane (1C) should be read, you should read them in the order that surfaces the change, not the order of production.)*

- **I3 — Present competing explanations.** For each finding, offer at least two interpretations. Don't collapse to one. *(Why this matters for synthesis: an investigation that presents a single explanation has stopped investigating. The criterion for closing a synthesis is not "I found an explanation" but "the evidence rules out the alternatives." At the synthesis layer, competing explanations often appear at the composition level: "the lanes together support conclusion X" vs. "the lanes together expose a tension that X papers over." Both must be held open until the lane evidence rules one out — or until you discover that both are partially right and the situation calls for a third reading. The "Six Specific Additions" conclusion in the orchestrator's current read is one interpretation; hold it in tension with at least one alternative.)*

- **I4 — Name the position of the investigation.** Every investigation is conducted from somewhere — with particular attunements, particular things it's prepared to notice, particular things it isn't. *(Why this matters for synthesis: every synthesizer is embedded in a particular chain of dispatches and reads. You are Claude Opus 4.6, running as gsdr-auditor, composing the outputs of 7 other Claude subagents (and one Sonnet) dispatched by the same orchestrator that wrote this task spec. The orchestrator is Claude Opus 4.6 in a claude-code session with a user who has a specific stance. Name how this specific position shapes what you are prepared to notice. A human expert in the same corpus would notice differently. An adversarial reviewer would notice differently. A Codex synthesis of the same 8 lane outputs would notice differently.)*

- **Show what remains unknown.** Not everything needs resolution. Explicit unknowns are findings — they map the edge of the synthesis. *(Why this matters: the temptation at the end of a synthesis is to close on a unified story. Resisting that temptation — and naming what the story cannot yet explain — is what distinguishes a synthesis from a speculation. The user explicitly invited qualified, conditional judgments — including "the preparatory corpus is not yet strong enough to justify either conclusion." If that is what the lane evidence supports, write that.)*

- **Show how you navigated any tensions between obligations.** When investigatory obligations tension with cross-cutting obligations or with each other, the navigation itself is a finding. See the Composition Principle below. *(Why this matters for synthesis: the synthesis layer is where tensions between the parent audit's obligations and the lane outputs' findings compose most visibly. If you find yourself cleanly resolving a tension at the synthesis layer, check whether you have smoothed over a real disagreement between lanes or between obligations.)*

### Subject Obligations

**No named subject** at the synthesis layer, inherited from the parent audit. Lane-level subjects were:
- Lane 1A: claim_integrity
- Lane 1B: comparative_quality
- Lane 1C: no-subject (exploratory orientation with named subject unavailable)
- Lane B2-Opus / B2-Sonnet: requirements_review
- Lane B3: process_review
- Lane B4: claim_integrity
- Lane B7: claim_integrity (standard escalated to investigatory)

The synthesis composes across six distinct subjects. If a subject becomes operative mid-synthesis — e.g., if you find the synthesis is really doing an artifact_analysis of the 8 lane outputs as a corpus — name the subject explicitly and apply its obligations from that point forward. The shift is itself a finding worth recording.

### Cross-Cutting Obligations

#### Chain integrity (extended to lane outputs)

> "When audit B uses audit A's finding as evidence, and audit A had a quality failure, audit B inherits the failure invisibly. This is the single most consequential failure mode in the discuss-phase session chain. **Obligation:** For each finding that depends on a predecessor audit's claim, re-verify that claim independently before incorporating it. State the re-verification or state why it was not done."

**Applicability at the synthesis layer is extreme.** This synthesis has 8 lane outputs as predecessors plus the inherited predecessors of the parent audit (the 2026-04-08 pre-execution review, Codex's original task spec, Codex's briefing, Codex's best-case memo). That is potentially 12+ predecessor claims-sources. The extended form:

1. **Lane outputs are predecessors.** Every load-bearing claim from any lane is subject to re-verification. Do not accept a lane's conclusion as ground truth just because the lane was conducted carefully. Specifically:
   - Lane 1A's claim that the canon is "recent earned convergence stapled onto older repeated assumption" — if you rely on this, spot-check the canon dates and the convergence pattern yourself.
   - Lane 1B's claim that prix-guesser's methodology is distributed across files — if you rely on this, spot-check the file list Lane 1B identified.
   - Lane 1C's quotations of F1's guidelines — B7 already re-verified these (all verbatim accurate). Accept B7's re-verification.
   - Lane 1C's "strongest defense" characterization — B7 modified this to "a potentially relevant defense, not the strongest." Accept B7's modification.
   - Lane B2-Opus's draft OPS-04 and Lane B2-Sonnet's named risk acknowledgment — if you rely on either, verify the PITFALLS.md Pitfall 14 citation and the current REQUIREMENTS.md citation mechanism.
   - Lane B3's "Tiered decision-surface methodology" claim — if you rely on this, note B3's own "proposed, not battle-tested" qualifier and preserve it.
   - Lane B4's claim that the canon contains no legal rationale — B7 verified this independently. Accept it.
   - Lane B4's draft minimum viable citation text — B7 contradicted this. Accept B7's contradiction.
   - Lane B7's own findings about Games/Apps/Simulator subsections and the "educational" ambiguity — if you rely on these, spot-check B7's methodology (two independent WebFetches) and verbatim passage quotations.

2. **Three-outcome discipline for predecessor lane claims.** For each claim you rely on, ask:
   - (a) Was the claim factually correct?
   - (b) Was the claim load-bearing for the lane that made it, and is it load-bearing for your synthesis?
   - (c) Is your use of the claim principled regardless of the lane's framing?

3. **The 2026-04-08 predecessor audit's recommendations** are inherited from the parent task spec. Lane 1A's 12 REV-* entries already applied the three-outcome ledger to those recommendations. Do not re-run the ledger. Use Lane 1A's ledger as the primary source for how the predecessor audit's claims compose into the current audit, but spot-check any REV entry you rely on.

4. **Codex's original task spec / briefing / best-case memo.** These are pre-audit predecessor artifacts that shaped the orchestrator's initial framing. The orchestrator has since moved past them; they are not load-bearing for the synthesis. Do not re-engage with them unless the synthesis surfaces a specific reason to.

**The chain integrity obligation creates a gate at the synthesis layer**: you may not carry forward a claim from any lane that you have not independently re-verified (by spot-checking the source the lane cited, or by accepting a downstream lane's verification of the upstream lane), or you must explicitly note that you did not re-verify and why.

#### Self-dispatch hygiene (continues to apply)

This is a **self** delegation at the synthesis layer, same as the parent audit. Claude orchestrator dispatched to Claude subagents. The standard dispatch-hygiene obligation about cross-model framing contamination does not apply directly, but the extended form does:

> **For self-delegated syntheses where the orchestrator's emerging read is documented in a handoff file that the synthesizer has access to, verify that the orchestrator's read is treated as an *input* to the composition rather than as a *conclusion* the synthesis must reach. Audit your own engagement with the handoff for whether you are following the lane evidence or following the orchestrator's framing.**

The user's original stance (from the parent audit):

> "we are here to critically, honestly, responsibly, thoroughly audit the repo and their claims. I am not convinced personally by any worries regarding 'loss of momentum' and 'time-concerns', its better to get it done well and right than have to spend time fixing things later because its broken, written poorly, we haven't considered enough how we are to deploy at scale, or distribute, or advertise, or make it easy to adopt / share etc. our response doesn't have to be an outright rejection or approval, we can thoroughly qualify and put conditions on our judgements."

The orchestrator's emerging read (from `CLAUDE-SESSION-HANDOFF.md` "Emerging Audit Conclusion" section) proposes a "six specific additions" conclusion. This is **the orchestrator's current read, explicitly flagged as a hypothesis for the synthesis to test**, not a pre-decided outcome. Concretely:

- It is **not** the synthesis's job to confirm the orchestrator's current read.
- It **is** the synthesis's job to engage with the substance of the read honestly. If the lane evidence supports it, say so. If the lane evidence contradicts it, say so.
- It is **especially** the synthesis's job to notice if the orchestrator's current read has smoothed over lane disagreements or missed findings the lanes surfaced.
- If you write the orchestrator's current read back to the user as a conclusion, you have not performed a synthesis. You have performed agreement with the orchestrator, which is a form of self-dispatch contamination.

**Note this self-dispatch hygiene obligation in your output. State explicitly whether you found yourself drifting toward the orchestrator's current read, and what you did about it.**

#### Framework invisibility (at the synthesis layer)

> "The obligations have I4 ('name the position of the investigation') but nothing that specifically asks: 'What does this audit's framework make invisible? What kinds of findings would not appear in this audit no matter how rigorously it was conducted?' **Obligation:** Name what your audit framework cannot see — not what you chose not to look at, but what the structure of the audit makes invisible."

**Ground framework invisibility in the specific question (copy verbatim):**

> *"Name a concrete finding that would not appear no matter how rigorously this synthesis was conducted, because of how this audit's scope was framed. If you can't name one, that's suspicious — the framework is probably hiding something from you that it's also hiding from itself."*

**The synthesis layer has its own framework-invisibility hazards** that lane-level hazards do not cover. Starting prompts (not a closed list):

- The synthesis is framed as "compose 8 lane outputs" — but maybe the most important finding is something no lane produced because no lane was dispatched to produce it. The audit's wave structure pre-specified what would be looked at; findings that would only appear under a different wave decomposition are invisible to this synthesis.
- The synthesis inherits the lanes' blind spots. If all 8 lanes silently shared an assumption (e.g., that prix-guesser's friends-on-couch scenario corresponds to a real situation friends would actually want), that assumption is propagated to the synthesis unexamined.
- The synthesis is framed around "the narrow initiative under audit" — but the parent audit's framework invisibility prompt asked whether the initiative is the right unit of analysis at all. Lane 1B and Lane B3 both surfaced findings that push in this direction (methodology is distributed, not centralized in the initiative). If the synthesis stays inside the initiative frame, it propagates the initiative-as-unit assumption unexamined.
- The synthesis is the end of this audit chain. What it does not name will not be named by this audit. If something important would only appear under a different audit classification (cross_model instead of self, standard instead of investigatory, with a named subject instead of no-subject), the synthesis cannot produce it by being more rigorous within its current framing — the framing is what excludes it.

These are starting prompts. The actual framework-invisibility finding at the synthesis layer must be something *you* identify in the composition itself, with concrete grounding in how the synthesis frame shapes what you produced. Generic prompts about bias produce compliance theater.

---

## Synthesis-Specific Obligations

Three obligations beyond the inherited ones, specific to the synthesis task shape.

### SO1 — The B2 Opus-vs-Sonnet Meta-Comparison

Lane B2 was dispatched as a controlled twin-pair: B2-Opus and B2-Sonnet ran the same task spec with the same scope, same obligations, and same predecessor set. The orchestrator added the twin explicitly as a controlled comparison of model-class performance on investigatory × requirements_review audit work.

**The synthesis must analyze the meta-comparison as its own section, not bury it in the substantive authoring-sustainability findings.** The specific questions the meta-analysis must address:

1. **Substantive convergence/divergence**: where did the two lanes agree substantively? Where did they disagree? The orchestrator's current read in the handoff claims they converged on substance while differing on depth and framing. Test this claim directly. Quote specific passages from each lane where they agree or diverge.

2. **Which lane caught what**: did one lane catch something the other missed? The handoff claims B2-Opus caught more adjacent vocabulary and produced a weighted-probability classification; B2-Sonnet caught the task-spec inference error more sharply and produced a cleaner verdict. Test both claims.

3. **The model-class finding**: what does this specific comparison tell us about Sonnet-vs-Opus capability on this specific audit profile (investigatory × requirements_review × gsdr-auditor on a corpus of ~5 canon files plus predecessor lanes)? The handoff's claim is "Sonnet is adequate for lane-level hermeneutic work with rigorous ground rules." Is this claim supported by the specific comparison evidence, or is it over-generalized from one data point?

4. **The dispatch implication**: the handoff concludes "default future audit dispatches to Sonnet unless there's a specific reason to escalate." Test this conclusion. If the comparison evidence supports it, endorse it and write a "For Future Audit Dispatches" subsection naming the specific reasons that would justify Opus escalation. If the evidence does not support it, say so.

The meta-comparison should be its own section in the synthesis output, clearly marked, so the project owner can cite it as a methodological finding independent of the substantive audit conclusion.

### SO2 — The Orchestrator-Error-Rate Section

The audit has surfaced several orchestrator task-spec errors:
- Lane 1B caught 2 of 8 pre-list errors (25% rate) — Path of Inquiry and Dependencies and Relations sections were claimed dropped but were preserved.
- Lane B2-Opus and Lane B2-Sonnet both caught the orchestrator's inference that the long-arc-canonization PLAN owned authoring-sustainability risk. Direct grep showed zero content.
- Lane B7 caught the orchestrator's framing of the F1 legal ambiguity as "carveout vs. simulator," when the actual ambiguity was wider (Games and Apps subsections, "educational" definition).
- Lane B7 also caught that the orchestrator, Lane 1C, and Lane B4 silently conflated "private fan use" with "private educational purpose."

**The synthesis must include an orchestrator-error section** that:
1. Lists every task-spec error the lanes surfaced, with the lane that caught it and the specific error.
2. Notes the error rate (small single digits to ~25% depending on how you count).
3. Names this as **the system working correctly**, not as a failure. The discipline the audit required (task-spec claims are contestable; flag errors as findings not silent corrections) was honored by the lanes. This is what chain integrity looks like when it works.
4. Notes whether the synthesis itself produced any new orchestrator-error findings. If it did, list them.
5. Notes whether the synthesis has its own error rate (the synthesis is a task spec too, and any claims in this task spec are contestable — if you find errors in this task spec, flag them in this section, not silently).

This section is not self-flagellation. It is the audit's own chain-integrity ledger applied to the audit itself.

### SO3 — The Practical Conclusion Shape

The parent task spec named four possible conclusion shapes. Reproduced here for direct use:

1. **The narrow vision-alignment initiative is justified as currently scoped**, and Phase 01 planning may proceed after the initiative completes its currently-planned 2 research calls + 1 deliberation + 1 decision anchor.
2. **The narrow initiative should widen in specific named ways before Phase 01 planning proceeds** — list the specific widenings and why each is load-bearing.
3. **The preparatory corpus is not yet strong enough to justify either the narrow or a broadened initiative** — name the specific missing pieces and the smallest concrete next step that would make the question answerable.
4. **Some fourth shape the investigation surfaces** that the orchestrator did not anticipate. (E.g., "the right next step is not an initiative at all." Or "the right shape is a deferral of the canon question entirely until a play-test happens.")

**The synthesis must produce one of these conclusions** (or a fifth shape), with concrete specifics. The orchestrator's current read is in the family of conclusion #2 (the "six specific additions" conclusion — three canon, three PLAN). **This is a hypothesis for the synthesis to test, not a pre-decided outcome.** If the evidence supports a different shape, write the different shape.

Concrete specifics the synthesis must provide, whichever shape it lands on:

- **If shape 1**: what specific lane evidence supports "justified as currently scoped"? What counter-arguments did the synthesis consider and reject?
- **If shape 2**: what are the specific widenings? For each, cite the lane evidence that makes it load-bearing. Distinguish required widenings from optional ones. Consider whether the widenings compose (i.e., do they represent a coherent shape-change, or are they independent fixes?).
- **If shape 3**: what are the specific missing pieces? What is the smallest concrete next step? What would change the situation into shape 1 or shape 2?
- **If shape 4/5**: name the reframing explicitly and explain why it is the actual answer. Show what the orchestrator's current read misses and why that miss is load-bearing.

For any shape, **list the strongest counter-arguments to your conclusion** and your honest assessment of how decisive each is. This is part of I3 — competing explanations are not just a finding format, they are the criterion for closing on a conclusion.

---

## Lane Outputs: The Primary Evidence Base

Read each lane output in full before composing. They are the evidence base. Do not deep-read canon files — the lanes already did that. The synthesis composes what the lanes produced; it does not re-run lane-level investigation.

### Wave 1 lanes

1. **`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1a-canon-integrity.md`** — Lane 1A (Opus, gsdr-auditor, claim_integrity). Canon integrity audit, three-outcome ledger with 12 REV-* entries, claim re-verification against predecessor 2026-04-08 audit. Load-bearing claim: the canon is "recent earned convergence stapled onto older repeated assumption." Key gap finding: stable diagnostic codes for venueRef (REV-12). ~72KB file; read thoroughly.

2. **`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1b-methodological-inheritance.md`** — Lane 1B (Opus, gsdr-auditor, comparative_quality). Methodological inheritance comparison between prix-guesser's and f1-modeling's vision-alignment files. Three operational gaps found: structure-wrongness permission, prompt-file authorship strategy at gates, loopback permission. Framework-invisibility finding: methodology is distributed across files, not concentrated in the initiative. Caught 2-of-8 orchestrator task-spec errors. ~72KB; read thoroughly.

3. **`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md`** — Lane 1C (Opus, general-purpose, exploratory). External web research on room frameworks, content models, F1 fan games, "private-only" as a framing pattern. Load-bearing finding: F1's guidelines contain both a private-educational carveout and a motorsport-simulator prohibition (B7 has since re-verified and modified this). PBLive identified as near-exact prior art for the Phase 01 YAML quiz contract. ~62KB; read thoroughly, but note that LQ-1C.4 is partially superseded by B7.

### Wave 2 lanes

4. **`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b2-opus-authoring-sustainability.md`** — Lane B2-Opus (Opus, gsdr-auditor, requirements_review × investigatory). Authoring sustainability as a first-class canon risk. Draft OPS-04 requirement proposed (5-round time audit, 30-min pain threshold, PITFALLS.md#14 citation). Partially disconfirmed Lane 1A's "canon doesn't own it" claim (canon has related M2-destination vocabulary). Caught the long-arc-canonization-PLAN inference error. ~96KB; read thoroughly.

5. **`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b2-sonnet-authoring-sustainability.md`** — Lane B2-Sonnet (Sonnet, gsdr-auditor, requirements_review × investigatory). Same task spec as B2-Opus. Named the risk as "owner-friction-exceeds-motivation." Proposed named risk acknowledgment with deferral trigger. Also caught the long-arc-canonization-PLAN inference error. ~57KB; read thoroughly. **Compare to B2-Opus for SO1 meta-comparison.**

6. **`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b3-distributed-methodology.md`** — Lane B3 (Opus, gsdr-auditor, process_review × investigatory). Verified Lane 1B's "substantively stronger" claim with a category-difference qualifier. Named a third pattern: "Tiered decision-surface methodology" across six tiers. Critical qualifier: proposed-not-battle-tested. Three framework-invisibility findings. Cross-lane handoff to B2: the meta-methodology reflection document is a soft-canon candidate for a fifth authoring-sustainability outcome neither B2 lane fully reached. ~100KB; read thoroughly.

7. **`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b4-f1-legal-carveout-citation.md`** — Lane B4 (Sonnet, gsdr-auditor, claim_integrity × standard). Canon grep confirmed zero legal rationale in canon. Slot identified: PROJECT.md Constraints section. Draft minimum viable text proposed (subsequently contradicted by B7). Gap-or-choice reading: more likely gap. ~29KB; read thoroughly.

8. **`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b7-f1-legal-ambiguity.md`** — Lane B7 (Opus, general-purpose with WebFetch, claim_integrity × standard escalated to investigatory). Resolved the carveout-vs-simulator ambiguity with Reading C ("irreducible on F1's text, but with structure"). Surfaced Games subsection and Apps subsection that Lane 1C and Lane B4 both omitted. Surfaced that the "educational" condition is itself ambiguous and may not apply to a party game. Modified multiple Lane 1C claims and contradicted Lane B4's draft citation text. Bonus finding: F1 explicitly redirects circuit IP licensing to circuit owners, meaning prix-guesser's core circuit-recognition content is not F1-owned IP — but the exposure is redirected to circuit owners. ~512 lines, ~55KB; read thoroughly.

### Task specs (for context, not deep-read)

- **`phase-01-prep-quality-scope-audit-2-task-spec.md`** — the parent task spec. You have the essential obligations copied above; do not re-read in full unless a specific question requires it.
- **The 8 lane task specs** (each `...-task-spec.md` file) — skim frontmatter only if you need to verify a lane's classification or model. Do not re-read them as artifacts under audit; the lane outputs are the primary artifacts.

### Session handoff (the orchestrator's notes to you)

- **`CLAUDE-SESSION-HANDOFF.md`** — contains the orchestrator's emerging read, the wave-structure rationale, the lessons-learned section, and the pause state. Read it for context, but apply the self-dispatch hygiene obligation: the orchestrator's emerging read is a hypothesis, not a conclusion. The handoff also contains the "Lessons Learned From This Session" section with 8 lessons the synthesis should preserve and build on where they hold.

### Canon files (read only for spot-check re-verification, not re-investigation)

- `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`. If you need to verify a lane's citation, open the specific file at the specific line. Do not read them in full.

---

## What Must Appear in the Synthesis Output

Write your output to `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-2-output.md`. This is the path the parent task spec named as `output_files`. Do not write to a different path.

### Mandatory structural elements

Not as labeled containers — as substantive engagement with each.

1. **YAML frontmatter** identifying the audit, its classification, the synthesizer's model, the predecessor lanes, and the output file path
2. **Opening context** (2–4 paragraphs): what this audit is, what it produced, where the evidence converged and where it did not. No executive summary that front-loads the conclusion — let the evidence lead the reader to the conclusion
3. **Primary findings** organized by the substantive threads the lanes produced: canon integrity, methodological inheritance, F1 legal posture, authoring sustainability, distributed methodology, and any additional threads the synthesis surfaces. For each thread, cite the load-bearing lane findings, re-verify as needed, and name the composed finding.
4. **Practical conclusion** (per SO3): one of shapes 1–4 (or a fifth). Concrete specifics. Strongest counter-arguments with honest assessment of how decisive each is.
5. **Meta-comparison: B2 Opus vs. Sonnet** (per SO1): its own clearly-marked section. Four specific questions addressed (substantive convergence/divergence, which lane caught what, the model-class finding, the dispatch implication).
6. **Orchestrator-error section** (per SO2): the audit's own chain-integrity ledger applied to the audit itself, including any errors in this synthesis task spec the synthesis surfaces.
7. **Position of the Investigation** section addressing I4.
8. **How I Navigated Tensions** section. If no tensions emerged, write that and consider whether the absence is evidence the obligations were too easily satisfied (RESEARCH.md Pitfall 3 — clean collapse). If tensions emerged, name them concretely per the Composition Principle and show how you navigated each.
9. **Full Rule 5 frame-reflexivity section** answering the three grounding questions verbatim. Anti-performativity warning applies.
10. **Framework invisibility section** at the synthesis layer. What does the synthesis framing make invisible that the lane framings did not?
11. **What the Obligations Didn't Capture** section — mandatory in every audit output. The structural opening for excess: findings that do not fit any obligation, any template, any expected shape. For synthesis, this section is particularly important because composition tasks often surface meta-findings about the audit framework itself.
12. **For Future Audit Dispatches** section (within the meta-comparison section if natural, or as its own subsection) — actionable implications of the meta-comparison for future audits in this project.
13. **Cross-Lane chain-integrity ledger** — for each load-bearing lane claim you incorporated, state: VERIFIED (accepted from lane with stated reason), MODIFIED (accepted with changes), CONTRADICTED (rejected with stated reason), or RE-VERIFIED (independently checked by the synthesis).
14. **"What Wave 3 Didn't Answer" section** — candidates for post-synthesis follow-up. The orchestrator's current candidates (from the handoff): PBLive archive reason, authoring-time interview with the project owner, the distributed methodology's first real execution cycle test, the synthesis's own chain-integrity rate. Add or subtract as the evidence supports.

### Length expectation

As long as the situation requires, no longer. The obligations are satisfied by substance, not by length. A synthesis that addresses every obligation honestly in 800 lines is better than one that performs each one in 2000 lines. A synthesis that tries to compose all 8 lane outputs in 400 lines has probably lost important detail.

**Rough target**: 1000–1800 lines. The lane outputs total ~3500 lines. A synthesis that compresses them to ~1/3 or ~1/2 is plausible. A synthesis under 600 lines has probably lost too much detail; a synthesis over 2500 lines is probably padding.

### Format

Markdown. Clear section headings. Inline citations in file:line format for lane claims and canon claims. Tables where they help (the chain-integrity ledger, the orchestrator-error list, the three-outcome lane-claim status).

---

## Composition Principle (copied verbatim from parent task spec)

Obligations from different axes compose into a flat list. They do not form a hierarchy. When obligations tension against each other in this synthesis, you must not pick a winner. You must:

1. **Name the tension.** Say what the two (or more) obligations are and how they pull differently *in this situation*. Not abstractly — concretely.

2. **Name what about the situation creates the tension.** The tension is not abstract; it is occasioned by particulars. What about *this* synthesis makes the obligations tension? Another synthesis might have no tension at all.

3. **Show how you navigated it.** Responsive to both demands, not cleanly picking one side. The navigation is part of the finding — the reader needs to see both the reasoning and the fact that the reasoning was not a clean resolution.

4. **The resolution emerges from engagement** with the situation, not from a precedence rule applied in advance. If you can write down in advance what would resolve every tension between these obligations, you haven't understood the principle — or the obligations can be collapsed to one, which is evidence that the framework is over-specified.

This is a **hermeneutic principle, not an algorithmic one.** The sign of engaged composition is not a clean resolution — it is a navigated one, where both obligations leave traces in the finding.

**If your synthesis contains zero tensions encountered** — *especially* if it ends in a clean conclusion that satisfies all obligations without any of them visibly competing — read your output again and ask whether you smoothed the tensions out or whether they really weren't there. The honest answer is more valuable than the polished one. At the synthesis layer, clean collapse is especially suspicious because composition across 8 lanes with 6 different subjects produces almost-guaranteed tension. If you found none, you probably missed some.

---

## Important Reminders

1. **The orchestrator's emerging read in the handoff is a hypothesis, not a conclusion.** Self-dispatch hygiene requires you to test it, not to confirm it. If your synthesis ends up convergent with the orchestrator's read, name the convergence and the specific lane evidence that produced it. If your synthesis diverges, name the divergence explicitly and reason about why.

2. **Task-spec errors are contestable.** If anything in this task spec is factually wrong (file paths, predecessor-lane characterizations, the framing of what each lane found, the "emerging read" summary), surface it as a finding. The 25% error rate the audit has been tracking applies to this task spec too. The discipline is: flag errors as findings, not silent corrections.

3. **Read lane outputs in full, not summaries.** The handoff contains summaries of the lane outputs. The summaries are compression and are explicitly flagged as not load-bearing ("these are summaries; do not rely on them for any load-bearing claim without reading the source"). Every claim you incorporate should be grounded in the lane output itself, cited by file:line.

4. **Do not over-rely on B7's re-verification of earlier lanes.** B7 is one lane; it can also have errors. Where B7 modified or contradicted an earlier lane's claim, verify that the modification is load-bearing for the synthesis. If it is, cite B7 directly. If it isn't, the earlier lane's framing may still stand.

5. **Lane B2 is a controlled twin-pair. The meta-finding is a deliverable.** Do not bury it in the substantive authoring-sustainability section. It gets its own section because it is methodologically load-bearing for future audits.

6. **Framework invisibility is where the sharpest findings live.** The handoff's L7 lesson names this explicitly. Do not treat framework invisibility as a checkbox. Engage with it as seriously as the primary obligations.

7. **You are the final lane in this audit chain.** What you do not name will not be named by this audit. What you smooth over will propagate forward to Phase 01 planning as silent assumption. Trust this specific position — if you see something worth saying, say it, even if no upstream lane set you up for it.

---

## Output File

Write the synthesis output to:

`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-2-output.md`

This is the `output_files` path named in the parent task spec's frontmatter. Do not write to a different path.

**Do not return a conversational summary instead of the file.** Write the file, then exit. The orchestrator will read the file from disk and report the findings to the user.

When you exit, return a brief note (under 200 words) confirming the file was written and naming the practical conclusion shape (1, 2, 3, 4, or a described fifth). Nothing more — the output file is the deliverable.
