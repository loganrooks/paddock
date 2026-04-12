---
date: 2026-04-11
wave: 1
lane: 1B
audit_subject: comparative_quality
audit_orientation: investigatory
audit_delegation: self
auditor_model: claude-opus-4-6
agent_type: gsdr-auditor
scope: "Compare prix-guesser's vision-alignment-2026-04 PLAN.md and RESEARCH-PRINCIPLES.md against f1-modeling's vision-alignment-2026-04 PLAN.md and RESEARCH-PRINCIPLES.md. Identify expansion provisions, review gate questions, and what is preserved vs dropped from the methodological inheritance. For each drop, assess whether it is principled or collateral damage. Sample at least one f1-modeling deliberation to ground the comparison in what wave 2 outputs actually look like."
triggered_by: "wave-1 parallel dispatch from phase-01-prep-quality-scope-audit-2 orchestrator (Claude Opus 4.6, claude-code session)"
parent_task_spec: phase-01-prep-quality-scope-audit-2-task-spec.md
task_spec: wave-1-lane-1b-methodological-inheritance-task-spec.md
ground_rules: "core+investigatory+comparative_quality+framework-invisibility"
tags:
  - wave-1
  - lane-1b
  - methodological-inheritance
  - comparative-quality
  - investigatory
  - opus
---

# Wave 1 / Lane 1B — Methodological Inheritance Comparison

**Classification:** `comparative_quality × investigatory × self`
**Auditor:** Claude Opus 4.6, running as `gsdr-auditor` subagent, file-reads only, no web access.
**Output consumed by:** Wave 3 synthesis pass.

---

## I1 — The Discrepancy

The load-bearing discrepancy this lane started from:

1. F1-modeling's `RESEARCH-PRINCIPLES.md` explicitly names prix-guesser (2026-04) as the source of its methodological inheritance, with the phrase "adapts and extends those lessons" — lineage runs **prix-guesser → f1-modeling**, not the other way (`/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md:5`: *"These principles critically inherit from methodological work done on the Prix Guesser project (2026-04), which learned through iteration that premature solution-space foreclosure is a methodological error. This document adapts and extends those lessons for the F1 Modeling Lab vision alignment work."*).

2. Yet prix-guesser's *current* vision-alignment-2026-04 `RESEARCH-PRINCIPLES.md` (`/home/rookslog/workspace/projects/prix-guesser/.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md`) is **125 lines** vs f1-modeling's **426 lines**, and drops named methodological sections that f1-modeling's version keeps as non-negotiable.

3. Prix-guesser's `README.md:23-42` identifies itself explicitly as a narrowing of f1-modeling's shape: *"This project does not currently have the same kind of wide, cross-domain architectural uncertainty that justified the larger `f1-modeling` initiative shape."*

4. The investigation asks: is the narrowing principled — i.e., is the smaller file the result of deliberate scope fit — or is it inheritance-then-truncation where things that were load-bearing in f1-modeling's executing practice were dropped because they didn't survive the round-trip through a scope reduction?

The comparison point — f1-modeling's version — is being used as the methodological standard because the lineage runs through it. This is already an interpretive choice. A different comparison point (e.g., a baseline "generic research methodology" or the prior prix-guesser 2026-04 methodology work that both derived from) would tell a different story. I name this choice so the reader can see the frame being used before reading the findings from within it.

**What this lane is NOT comparing.** Not size. Not artifact count. Not executing volume. F1-modeling has executed through Wave 2C as of 2026-04-11 (`f1-modeling/.../PLAN.md:301-314`); prix-guesser's initiative has not started (`prix-guesser/.../README.md:3` *"Status: Planned"*, initiative `research/` and `deliberations/` directories are empty). Comparing deliverable volume at this moment would be comparing an executing body of work against a freshly authored scaffold — the size trap.

---

## I2 — How The Investigation Unfolded

I began with the orchestrator's pre-selected file list (both READMEs, both PLANs, both RESEARCH-PRINCIPLES, two deliberation samples). I worked through the prix-guesser side first in full, then f1-modeling's PLAN and RESEARCH-PRINCIPLES in full, then the decision-anchor sample in full and the ~280 lines of `01-backend-boundary-architecture.md` the task spec recommended.

Two mid-investigation branches then surfaced that the pre-selection did not cover:

- **Branch pursued:** Prix-guesser has a `.planning/deliberations/2026-04-11-long-arc-canonization/` directory outside the vision-alignment initiative. The task spec flagged that "methodological discipline that lives somewhere other than the PLAN/PRINCIPLES files" is the framework-invisibility gap, and I recognized that I could not honestly assess the claim "prix-guesser dropped X" without at least sampling where else in prix-guesser's `.planning/` that X might live. I read `long-arc-canonization/PLAN.md` in full (892 lines). This is the branch with the most consequential finding — see the framework invisibility section below.

- **Branch pursued:** I grep-checked the `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md` file (1346 lines) for trajectory/precedent/reframing/terrain-mapping vocabulary, to test whether prix-guesser's discuss-phase workflow absorbs any of the discipline the initiative's RESEARCH-PRINCIPLES.md does not carry. It does not meaningfully — trajectory appears 4 times as shallow mentions, not as the disciplined 1/3/5-year practice (see "Cross-Cutting: Framework Invisibility" below).

- **Branch pursued:** I read the first ~100 lines of the 2026-04-08 prior audit's `METHODOLOGY-REVIEW.md`. This sample establishes that prix-guesser has sophisticated meta-methodology capacity elsewhere in the repo (detailed confound analysis, A/B replication framing, epistemic humility about the orchestrator not being blind to either pass). This matters because it changes how the "drops" in the current initiative read: they are not evidence that prix-guesser lacks the methodological vocabulary, only evidence that the vocabulary was not re-imported into this initiative.

The investigation's shape changed mid-flight. I came in expecting to verify the orchestrator's list of drops with "was it dropped? was the drop principled?" for each item. I ended up finding that **one of the orchestrator's listed drops was factually wrong** (Path of Inquiry and Dependencies and Relations are *not* dropped — they are explicitly in prix-guesser's required output sections at lines 108 and 111 of its RESEARCH-PRINCIPLES.md), and that **the framework-invisibility question became the most load-bearing question in the lane**, because the discipline apparently lost in the initiative files turns out to exist elsewhere in the project's planning surface, under different names, with different structure.

---

## I3 — The Comparisons

### Comparison A: PLAN structure (LQ-1B.1)

Prix-guesser's PLAN.md is **123 lines**. F1-modeling's PLAN.md is **335 lines**. Both files explicitly frame themselves as "scaffolding, not commitment" — literally the same phrase in both:

- `prix-guesser/.../PLAN.md:9` *"This Plan Is Scaffolding, Not A Commitment To Over-Research"*
- `f1-modeling/.../PLAN.md:9` *"This Plan Is Scaffolding, Not an Execution Contract"*

This is preserved inheritance, and it's the most important load-bearing claim of the plan-authoring posture. It survives into prix-guesser's version.

Now the structural dimensions:

| Dimension | Prix-guesser | F1-modeling | Functional delta |
|---|---|---|---|
| **Wave count (nominal)** | W1 (2 parallel research calls), optional W1.5, W2 (1 deliberation), W3 (1 decision anchor) | W1 (3 parallel), optional W1.5 (executed), W2a (D1), W2b (D2/D3 iterative 2-3 calls), W2c (D5), W2d (D4), W3 (3A, 3B) | F1-modeling has more waves because it has more deliberation domains, not because its plan is structurally larger. See LQ-1B.4. |
| **Review gates** | Gate 1 (L45-58), Gate 2 (L80-92) | Gate 1 (L78-94), Gate 2a (L112-117), Gate 2b (L138-144), Gate 2c (L158-163), Gate 2d (L177-179), Final Review (L192-194) | 2 vs 6. More to say here — see Gate Questions comparison. |
| **Gate 1 question count** | 4 questions (L47-52) | 6 questions (L80-88) | Prix-guesser's 4 match f1-modeling's 1, 2, 4, and 5 conceptually; f1-modeling's 3 ("are gray areas collapsing?") and 6 ("is Round 1.5 warranted?") have no analogue in prix-guesser. The Round-1.5 question may be implicit in prix-guesser's "possible outcomes" list at L54-58. |
| **Gate outcome space** | "proceed to synthesis / commission targeted follow-up / skip further initiative work" (L54-58) | "proceed as planned / commission Round 1.5 / restructure deliberation plan / add/remove research tasks / reframe initiative scope" (L90-95) | F1-modeling's outcome space explicitly includes **restructuring subsequent waves** and **reframing initiative scope**; prix-guesser's outcome space does not. This is a real gap — see verdict below. |
| **Expansion provisions** | "expansion is a legitimate outcome, but only if the findings warrant it" (README:89) / "if those steps surface critical underdetermination, the initiative may expand with targeted follow-up research or a second deliberation" (README:89) / Wave 1.5 optional 0-1 calls (L60-66) | "subject to revision at every review gate" (L11) / "one valid outcome is: the planned structure is wrong; here is the right structure" (L13) / "Round 1.5 may add 1-N calls" (L222) / "Wave 2b-iii may be skipped if unnecessary" (L222) | Prix-guesser's expansion is quantitatively bounded ("0-1 calls") and its structural revision language is softer ("may expand with targeted follow-up"). F1-modeling's is open-ended ("1-N calls") and includes explicit permission to declare the planned structure wrong. |
| **Prompt-authorship strategy** | Not mentioned | Explicit section L251-262: *"Prompt files for Waves 2 and 3 are authored at the appropriate review gate, informed by what earlier waves actually found"* | **This is one of the strongest preserved-then-dropped items.** See analysis below. |
| **Iteration norms** | Not stated as a named principle | "This initiative supports iteration when warranted, not as busywork" (L45) | Prix-guesser's initiative does not have an "iteration is legitimate when warranted" stance stated. Whether this matters is argued below. |
| **Loopback permission** | Not stated | Explicit: *"Any stage can trigger a loopback to an earlier stage if its findings reveal that earlier work needs extension"* (L53-54) | Prix-guesser has no explicit loopback language. The Gate 2 outcome *"commission one narrow follow-up if a truly blocking gap remains"* (L92) implicitly allows a loopback from synthesis to research, but does not name it as such. |
| **"Deliberation plan can restructure" language** | Absent | L15-21: deliberations are "provisional handles"; the right number may be 3 or 5 not 4; deliberations may merge, split, or be completely restructured | This is the strongest structural-revision language f1-modeling has, and prix-guesser has nothing like it. |

**Verdict on LQ-1B.1 (are prix-guesser's expansion provisions equivalent in operational power to f1-modeling's?).**

**No, not equivalent.** Prix-guesser's PLAN preserves the **scaffolding-not-execution** framing and the **one-valid-outcome-is-proceed** escape hatch. But it drops three specific expansion provisions that do functional work in f1-modeling:

1. **Explicit permission to declare the planned structure wrong at a review gate** (`f1-modeling/PLAN.md:13`). Prix-guesser's plan has no equivalent sentence. Its outcome space at Review Gate 1 includes proceeding, commissioning follow-up, or skipping further work — but does not include "the wave structure itself is wrong, here is the right one." An initiative whose PLAN omits this permission is more likely to treat the planned wave shape as a contract under pressure, even though it explicitly says it is not one. The absence is not compensated by the "may expand" language because "expand" assumes the existing shape is right and adds to it.

2. **Prompt-file authorship at the review gate informed by what earlier waves found** (`f1-modeling/PLAN.md:251-262`). Prix-guesser's PLAN does not say whether Wave 2A's prompt is authored now or at Review Gate 1. This is not a cosmetic distinction. Pre-authoring the Wave 2A prompt before Wave 1 runs pre-decides what the deliberation will investigate — it bakes the current best guess about what's uncertain into a prompt that is then consumed by the deliberation model as "the question." Authoring at the gate lets the prompt absorb what Wave 1 actually found, including reframings. The fact that prix-guesser has only one deliberation in nominal shape makes this more, not less, load-bearing: the single deliberation is the entire closure step, and if its prompt is pre-authored, it is doing closure under a pre-Wave-1 framing.

3. **Explicit loopback permission.** The RESEARCH-PRINCIPLES inheritance (see Comparison B) makes the loopback drop a compound issue: it is dropped in the PLAN and dropped in the PRINCIPLES.

On the other side: prix-guesser's PLAN has one provision f1-modeling's does not have — **the "skip further initiative work" outcome at Review Gate 1** (L57: *"conclude the current canon is already sufficient and skip further initiative work"*). This is a meaningful addition. Prix-guesser's narrower scope legitimately allows an outcome where Wave 1 reveals the current canon is already adequate and no deliberation is needed at all. F1-modeling's plan does not allow this outcome because its audit findings forced deliberation. So prix-guesser is not strictly less permissive than f1-modeling — it is differently permissive. The differences are real but not all in one direction.

**The operational gap that matters most is #2 (prompt-file authorship strategy).** I would have listed this as the single most consequential drop from the PLAN inheritance if I had to pick one.

### Comparison B: RESEARCH-PRINCIPLES content (LQ-1B.2)

Prix-guesser's file: 125 lines, 11 sections. F1-modeling's file: 426 lines, 13 sections (plus TOC).

**Verifying the orchestrator's list of drops.** I searched both files line-by-line. For each item the orchestrator claimed was dropped:

| Item orchestrator claimed dropped | Confirmed? | Evidence |
|---|---|---|
| Trajectory analysis (1/3/5-year + doors opened/closed) | **Yes, fully dropped.** | Zero hits for "trajectory", "1-year", "3-year", "5-year", "doors opened", "doors closed" in prix-guesser's PRINCIPLES. F1-modeling's section at L104-114 is a named methodological principle #2 with required analysis dimensions. |
| Precedent analysis with named cases | **Yes, fully dropped.** | Zero hits for "precedent", "named case", "Successes", "Failures", "analog" in prix-guesser's PRINCIPLES. F1-modeling's L116-125 gives the disciplined form with the "'React apps use a visualization library' is not a precedent. 'Grafana uses a hybrid SVG + Canvas approach...' is a precedent" distinction. |
| Calibrated confidence markers (Known / Likely / Plausible / Speculative / Unknown) | **Yes, fully dropped.** | Zero hits. F1-modeling L60-68 defines the five-level scale. |
| **Path of Inquiry as required output section** | **NO — the orchestrator was wrong.** | Prix-guesser's `RESEARCH-PRINCIPLES.md:111` explicitly lists `Path Of Inquiry` as a required output section. What is dropped is the *internal structure* of that section (f1-modeling's seven named subsections at L231-240: entry point, branches considered, branches pursued, branches abandoned, unexpected branches, dead ends, reframings). The section heading is preserved; the structure it enforces is not. |
| **Dependencies and Relations as required output section** | **NO — the orchestrator was wrong.** | Prix-guesser's `RESEARCH-PRINCIPLES.md:108` explicitly lists `Dependencies And Relations` as a required output section. What is dropped is f1-modeling's internal structure (the four named subsections at L246-251: questions this depends on, questions this affects, adjacent questions, coupling strength). The heading is preserved; the enforced structure is not. |
| Hypothesis testing as a distinct mode | **Yes, fully dropped.** | Zero hits for "hypothesis" in prix-guesser's PRINCIPLES. F1-modeling L45-48 defines it as a named mode alongside terrain mapping, solution evaluation, and synthesis. Prix-guesser has only three modes at L26-40: terrain mapping, deliberation, synthesis. |
| Reframing permission section (explicit permission to answer a different question) | **Yes, fully dropped.** | Zero hits for "reframe", "reframing", "better question" in prix-guesser's PRINCIPLES. F1-modeling's L270-290 gives a full section with the four named reframing signals. |
| Detailed gray-area handling framework with worked examples | **Partially dropped.** | Prix-guesser has the three responses (Defer / Follow-and-mark / Revisit later at L62-77) — the framework is preserved in name and shape. What is dropped is the worked examples, the decision logic diagram, and the required-output-when-deferring templates. F1-modeling's L151-220 is six times longer and includes two concrete examples. |
| 16-section research / 13-section deliberation required structures vs prix-guesser's 7 required output sections | **Confirmed as count, misleading as framing.** | Prix-guesser requires 7 output sections (L102-111). F1-modeling requires 16 for research and 13 for deliberation. But f1-modeling's count is inflated by things like `Metadata`, `Executive Summary`, `Question as Received`, `References` — structural/hygiene sections, not substantive research moves. The substantive methodological sections prix-guesser is missing compared to f1-modeling's research template are: `Trajectory Analysis`, `Precedent Analysis`, `Reframing (if any)`, `Scope Expansion Notes`, `Provisional Position`, `Confidence Ledger`, `Unresolved Questions`. That is the real delta, not 7-vs-16. |

**One orchestrator claim I need to call out explicitly as a finding about the audit itself.** The task spec's framing of drops was 80% accurate but asserted Path of Inquiry and Dependencies and Relations were dropped when they are explicitly preserved as section headings. This matters for two reasons: (a) if I had taken the orchestrator's framing on faith without running Rule 2's disconfirmation check, the lane would have propagated the factual error into the Wave 3 synthesis, and (b) the orchestrator's own error — claiming sections are dropped when they are preserved but thinner — is itself evidence of how the comparative_quality frame invites you to see what's missing more readily than what's hollow. I discuss this in the Rule 5 section below.

**Per-drop assessment.** For each confirmed drop, I worked through: principled (the smaller scope legitimately doesn't need it), compensated (carried elsewhere in the initiative or project), or lost (collateral damage).

| Drop | Principled? | Compensated where? | Lost? | Consequence for a prix-guesser deliberation |
|---|---|---|---|---|
| **Trajectory analysis (1/3/5-year)** | **Partially — and partially not.** The initiative's stated scope is "close what Phase 01 needs, defer the rest" and Phase 01 is a substrate-freezing phase. Trajectory analysis is *exactly* the discipline you need to answer "will this substrate hold through M2/M3?" — which is literally the job the initiative says it is doing (README:14 *"reduce the chance of closing those questions in the wrong shape"*). The argument that trajectory analysis is principled would have to say "we don't need 1/3/5-year horizons because all the trajectory work lives in LONG-ARC.md" — and that argument has merit, because LONG-ARC.md does carry the long-arc work, and it is a required reading (PLAN:28). | **Partially compensated** via LONG-ARC.md (PLAN L28) as required reading for every call. The deliberation will have trajectory context available even if it is not required to produce trajectory analysis as output. But **consumption is not equivalent to production.** Reading LONG-ARC.md means the deliberator has the long-arc frame in mind. Producing a trajectory-labeled "doors opened / doors closed" analysis means the deliberator has to *reason* in that frame and output the reasoning in a form later readers can inspect. The difference is structural: consumption puts the trajectory in the deliberator's working memory; production puts it in the record. | **Partly lost.** The production-vs-consumption distinction is where the loss lives. | A deliberation that doesn't produce trajectory analysis as a named section may still reason about the long arc, but it will not leave behind a trajectory-labeled record. The next Phase 01 planning pass will not be able to see *which specific contract decisions were checked against which M2/M3 scenario*, only that the deliberator was told to keep the long arc in mind. |
| **Precedent analysis with named cases** | **Partially principled.** The narrow initiative's domain is content-contract decisions (answer-surface ontology, clue families, scoring intent). Those are narrower than f1-modeling's "which visualization library / which compute runtime?" questions where precedent matters enormously. BUT prix-guesser has real named precedents: the task spec itself named geohub, Geo-Locator, react-geofindr, PartyKit, Colyseus, boardgame.io. These live in prix-guesser's prior research at `.planning/research/2026-04-10-first-wave-xhigh-comparisons/` which the initiative's PLAN does not list as required reading. | **Partially compensated** via the prior research lane being available in the repo for any deliberator to grep. But the initiative does not *require* reading it (`PLAN.md:25-34` lists only the canon docs and the 01-phase files). | **Partly lost.** The rigor is not mandated even though the material exists. | A deliberation that doesn't require precedent analysis may cite no precedents, or may cite them in passing without the "specific named case with specific outcome" discipline. The risk is that the deliberation closes a contract decision based on internal reasoning alone when the precedents would have ruled out or reshaped options. |
| **Calibrated confidence markers** | **Not principled; weakly compensated.** No scope-based argument justifies dropping this — confidence calibration is a general-purpose discipline, not a domain-specific one. | Not compensated in the initiative files. Prix-guesser's prior METHODOLOGY-REVIEW.md engages confidence calibration sophisticated-ly (see framework invisibility section), so the project has the vocabulary — it just isn't imported into this initiative. | **Lost, but the loss is smaller than it looks.** | A deliberation without calibrated confidence markers may present its recommendations with uniform confidence, losing the Known/Likely/Plausible/Speculative distinction. For a narrow-scope deliberation with a single closure call, this matters less than for a broad-scope deliberation with many findings — but it still matters for the "defer explicitly with closure criteria" doctrine, which depends on the deliberator knowing how confident they are in the reasons-for-deferral. |
| **Path of Inquiry internal structure** (section heading preserved, subsections dropped) | **Principled.** Prix-guesser's deliberation shape is smaller and more focused. Requiring seven named subsections (entry point, branches considered, pursued, abandoned, unexpected, dead ends, reframings) for a single-domain deliberation would be disproportionate scaffold. The section heading is preserved, which is the important thing. | N/A (not compensated — the section itself is kept). | **Not lost.** | The deliberator is still expected to produce a Path of Inquiry section; they just aren't forced into seven sub-headings. This is the principled way to do a drop: preserve the methodological commitment, relax the scaffolding. |
| **Dependencies and Relations internal structure** (section heading preserved, subsections dropped) | **Principled, same as above.** | N/A. | **Not lost.** | Same reasoning. |
| **Hypothesis testing as a distinct mode** | **Probably principled.** Prix-guesser's initiative is genuinely terrain-mapping and deliberation work; nothing in the scope says "test whether the current canon's claim X holds up." F1-modeling's hypothesis-testing mode is there because its initiative does stress-test findings against specific code. | N/A. | **Not lost in the current scope.** But worth noting: if the initiative discovers at Gate 1 that a specific canon claim needs stress-testing, the absence of the mode means the deliberator has no named frame for doing so. This is a low-probability gap, not a high-probability loss. | A deliberator who needs to hypothesis-test a canon claim will improvise it rather than execute it. The improvisation may be adequate. |
| **Reframing permission section** | **Not principled. This is the most consequential real drop.** The strongest moments in f1-modeling's Wave 1 and Wave 2A are reframings (*"the durable decision is not Python vs Rust vs TypeScript. The durable decision is the contract that separates..."* — backend-boundary deliberation L32). F1-modeling's Gate 1 explicitly triggered a structural reframing based on a "convergent boundary insight" (`f1-modeling/.../PLAN.md:305`). An initiative that does not give its deliberator explicit permission to reframe the question that was asked is an initiative that treats the question-as-asked as a contract. For a narrow initiative closing a small set of content-contract decisions, the likelihood that reframing is load-bearing is smaller than for f1-modeling — but **the specific load-bearing question prix-guesser is asking is itself susceptible to reframing**. The question at `PLAN.md:47-50` is "which decisions must close before Phase 01 planning can proceed?" A reframing might be "the wrong question is which decisions must close; the right question is how Phase 01's discuss workflow can close decisions in-flight without requiring this initiative at all." That reframing is available from the scope boundary ("skip further initiative work") but the deliberator has no explicit permission to produce it as a named output. | Not compensated. | **Lost.** | A deliberation that cannot name a reframing is a deliberation that answers the question it was given even when the right move is to answer a different question. |
| **Gray-area handling worked examples** | **Principled.** Prix-guesser preserves the three responses by name (Defer / Follow-and-mark / Revisit-later at L62-77). Worked examples are scaffolding for internalizing the framework; once the framework is internalized, the examples become redundant. A small-scope initiative whose deliberator has the canon already in context can reasonably skip the examples. | N/A — the framework itself is preserved. | **Not lost.** | Same as above. |
| **Iteration norms as a named principle** | **Not principled, but the absence is smaller than it looks.** Prix-guesser's PLAN says expansion is a legitimate outcome (`README:89`, `PLAN:21`). What's missing is the f1-modeling phrasing "iteration is legitimate when warranted, not as busywork" — the balance between "iterate when needed" and "don't iterate as busywork." | Partially compensated by the "success/failure test" at `PLAN:120-123`: the initiative fails if it produces "polished prose without narrowing the actual substrate risk." This is the anti-busywork clause under a different name. | Partly lost. | A deliberator pressured to produce substance may over-expand; a deliberator pressured to conclude quickly may under-expand. The f1-modeling discipline gives a named frame for both. Prix-guesser's frame is unilateral (anti-busywork) rather than bilateral. |
| **Explicit loopback permission** | **Not principled.** There is no scope argument that justifies dropping explicit loopback permission — it is a general-purpose discipline and it is load-bearing for *any* iterative initiative. | Partially compensated at Gate 2 by the outcome *"commission one narrow follow-up if a truly blocking gap remains"* (PLAN:92), which is a gate-2-to-gate-1.5 loopback under a different name. | **Partly lost.** | Prix-guesser allows one specific loopback (Gate 2 commissioning Wave 1.5-style follow-up). It does not allow loopbacks from the decision anchor back to research, or from synthesis back to deliberation. For a four-step initiative, this is a smaller gap than for f1-modeling's ten-step initiative. |

**Verdict on LQ-1B.2 (are the methodological drops principled?).**

**Mostly principled, but three drops cross the line from scope fit to collateral damage:**

1. **Reframing permission** — the highest-conviction call. Not principled. Real loss. A one-deliberation initiative has one chance to reframe, and removing the explicit permission closes the most valuable failure mode an initiative's deliberator can produce.

2. **Trajectory analysis as production** (not consumption) — partly principled via LONG-ARC.md compensation, partly not. The deliberator will have trajectory context in mind, but will not leave behind a trajectory-labeled record for the next planner. For an initiative whose explicit job is preserving future lineage without widening Phase 01 scope, the inability to produce a trajectory-labeled audit trail is a concrete gap.

3. **Calibrated confidence markers** — the loss is smaller than #1 or #2, but the drop is not justified by scope. The project already has sophisticated confidence-calibration vocabulary in its audit methodology (see framework invisibility below), and nothing about a smaller initiative makes Known/Likely/Plausible/Speculative harder to use. The drop is collateral.

**Drops that are defensibly principled and should not be restored on my recommendation:**
- Internal structure of Path of Inquiry and Dependencies and Relations sections (heading preserved, subsections dropped). This is the correct way to do a scope reduction.
- Worked examples of the gray-area framework.
- Hypothesis testing as a named mode.
- Iteration norms — the anti-busywork stance is compensated by the success/failure test.

**Loopback permission** sits on the border. The one-loopback-at-Gate-2 compensation is adequate for a four-step initiative, but barely; if Wave 1.5 runs and a second loopback is needed, the initiative has no named frame for it.

### Comparison C: Sample deliberation character (LQ-1B.3)

I read f1-modeling's `deliberations/01-decision-anchor.md` in full (18 lines; extremely compact) and the first 280 lines of `01-backend-boundary-architecture.md`.

**What the f1-modeling deliberation actually produces:**

1. **Four contracts closed simultaneously in one call** (C1 compute execution boundary, C2 job/event protocol, C3 artifact/provenance, C4 regulation execution-flow slice). The deliberation doesn't close one question — it closes four coupled questions in one pass, with each contract having its own option space, tradeoffs, closure analysis, and outcome (`f1-modeling/.../deliberations/01-backend-boundary-architecture.md:25-44`).

2. **Tradeoffs explicitly structured by 1-year / 3-year / 5-year horizons** (L101-124). This is the trajectory-analysis discipline in action. For each of the four contracts, there are three sub-analyses. Example from C1: *"1-year: a worker-backed TypeScript implementation preserves delivery speed and Phase 4 continuity, while still forcing request compilation and compute execution apart. Staying synchronous is lower effort but deepens the wrong seam. 3-year: a message-based local worker process keeps Python/Rust/C++ sidecars viable without rewriting the browser/API contract..."*

3. **"Gray Areas Still Unresolved" section with explicit [FOLLOW-AND-MARK], [REVISIT-LATER], [DEFER] tags** (L126-152). The framework prix-guesser's PRINCIPLES names-but-doesn't-example is directly in use here, with reasoning per tag. `[DEFER] Cross-era comparability ontology` at L150-152 is an instructive example of a deferral with explicit handoff criteria.

4. **Closure Analysis section asking "Can it be closed now? Evidence?" per contract** (L154-203). Not just "here is my recommendation" — explicit warrant about whether there is enough evidence to close at all. C2 closes "mostly yes, with a provisional transport binding" (L170). This is the calibrated-commitment principle producing a specific shape of outcome.

5. **Concrete TypeScript interface definitions** in the Outcome section (L227-272). The deliberation isn't just framing — it's specifying the contract shapes at the level of method signatures and type unions. This is the level of substance the narrow prix-guesser initiative would need to produce equivalent-character work.

**Could prix-guesser's PLAN produce a deliberation of this character with one Wave 2A call?**

**Partly yes, partly no. Two things about prix-guesser's one-deliberation shape give me concerns about whether it can produce work of this character without addressing them.**

Things that make me think **yes**:
- The shape of prix-guesser's closure targets (answer-surface hierarchy, clue families, pack/round identity, scoring intent minimums) is substantively similar to f1-modeling's — each is a contract decision with multiple coupled sub-decisions. A single deliberation call closing "four contracts" in f1-modeling terms maps cleanly onto prix-guesser's "decide the authored-substrate contract" call.
- Prix-guesser's stated Wave 2A outcome shape (`PLAN.md:74-78` — "closed now / deferred with closure criteria / explicitly out of scope for Phase 01") is conceptually identical to f1-modeling's Outcome section taxonomy (Recommendation / Provisional recommendation / Deferral / Reframing). Minus reframing, which is the drop.
- The guardrails at `RESEARCH-PRINCIPLES.md:79-99` are specific and load-bearing: Guardrail 2 about preserving venue/circuit/section/corner across milestones is effectively a compressed trajectory-analysis clause for the specific substrate being frozen.

Things that make me think **no, not without addressing specific gaps**:
- **The prompt for Wave 2A is authored up-front** (there is no "at the gate" language in prix-guesser's PLAN). If the prompt is authored at initiative-launch time, it bakes in the pre-Wave-1 framing. F1-modeling's D1 prompt was authored at Gate 1 after Wave 1 surfaced a convergent boundary insight that restructured what D1 was closing (`f1-modeling/.../PLAN.md:305`: *"Convergent boundary insight, boundary memo written, Codex cross-model review triggered restructure to δ"*). Prix-guesser's PLAN does not guarantee equivalent responsiveness.
- **The deliberator is not required to produce trajectory-labeled analysis in the record**, only to reason with the long-arc context in mind. A deliberation that is not required to produce its trajectory reasoning as a named output is more likely to produce reasoning that cannot be later audited.
- **The deliberator has no explicit permission to reframe** the closure question. If Wave 1 surfaces that the real question is different from the one in the Wave 2A prompt, the deliberator has no named vocabulary for saying so. (Possible compensation: the deliberator is reading RESEARCH-PRINCIPLES.md at the start of every call, and the "gray-area" framework's "Revisit later" response is structurally similar to reframing, but it is not the same thing — Revisit-later leaves the question intact, Reframing changes it.)
- **The deliberation is one call, not a sequence of iterative drafts** like f1-modeling's 2B-i → 2B-ii → optional 2B-iii pattern. For a narrow initiative this is probably correct — the content-contract decisions do not have obvious bidirectional coupling the way D2 (viz) and D3 (edu) have. But the initiative has no affordance for discovering bidirectional coupling mid-deliberation and iterating to honor it.

**Read on LQ-1B.3: could produce equivalent-character work *if* three specific things are addressed.**

The three things:

1. Author the Wave 2A prompt at Review Gate 1, not now. This is free to do at no cost.
2. Add a requirement that the Wave 2A output include a "Trajectory Check" section per closed contract, naming which M1/M2/M3 constraint the contract is being checked against. This is a targeted import from f1-modeling's methodology — not a full trajectory-analysis section, just a trajectory-labeled checkpoint per contract.
3. Add an explicit reframing-permission line to the PLAN's Wave 2A description. One sentence.

With those three changes, I would read the one-deliberation shape as adequate-to-equivalent for the initiative's scope. Without them, there is a real risk that the deliberation produces substantively sound content-contract decisions that are not inspectable as decisions-against-the-long-arc and cannot absorb a Wave 1 reframing.

### Comparison D: Domain difference as justification (LQ-1B.4)

The task spec framed the question as "distinguish methodological apparatus appropriate to the domain from apparatus appropriate to any substrate-freezing work." I take that seriously.

**Where domain difference justifies the narrowing:**
- F1-modeling is closing boundary contracts involving compute runtimes (TypeScript, Python, Rust, C++), IPC protocols (SSE, WebSocket, gRPC), performance envelopes in the 0.25-1 Hz cadence range, and artifact manifests with explicit schema versioning. These are adversarial engineering domains where precedent analysis of specific named libraries (Grafana, visx) and calibrated confidence markers about performance claims directly shape the decisions. Prix-guesser's domain — authored content contract for a private F1 fan game — does not have adversarial technical dependencies at that level. A full 1/3/5-year trajectory analysis of whether to use `venue`/`circuit`/`section`/`corner` as the answer-surface hierarchy is disproportionate scaffolding when the LONG-ARC.md doctrine already answers the trajectory question for these specific entities.
- F1-modeling synthesizes across five deliberation domains (D1 compute, D2 viz, D3 edu, D5 regulation, D4 long-horizon) with explicit inter-domain coupling. Prix-guesser's one deliberation has one primary domain (authored substrate). The iterative-drafting pattern (2B-i → 2B-ii → optional 2B-iii) is an appropriate response to bidirectional coupling and is correctly absent from prix-guesser's plan, because the coupling is not there.

**Where domain difference does NOT justify the narrowing:**
- **Calibrated confidence markers** are not domain-specific. Known/Likely/Plausible/Speculative/Unknown works equally well for "should answer-surface hierarchy collapse venue into circuit?" as it does for "should the compute runtime be Python or TypeScript?"
- **Reframing permission** is not domain-specific. The moment where "the real question is different" can happen in any deliberation that isn't rote execution of a pre-decided closure call. A narrow initiative *is at least as likely to need reframing as a broad one*, because the narrowness of the original framing is itself a risk factor for getting the question wrong.
- **Explicit loopback permission** is not domain-specific. A narrow initiative with one deliberation needs loopback even more than a broad initiative with many, because there is no lateral safety from another deliberation catching the mistake.
- **Precedent analysis** is domain-specific in the sense that *which precedents to cite* changes — prix-guesser would cite geohub, PartyKit, boardgame.io, not Grafana. But the *discipline* of citing specific named cases with specific outcomes is not domain-specific. The drop of the discipline cannot be justified by saying "the cases are different."

**Verdict on LQ-1B.4:** Three specific drops (calibrated confidence, reframing permission, precedent-analysis discipline) cannot be justified by domain difference. They are not scope-appropriate; they are inheritance-then-truncation. The other drops are defensible.

---

## I4 — Position of the Investigation

I am Claude Opus 4.6, running as `gsdr-auditor` subagent via the Claude Code `Task` tool, with file-reads only and no web access. I was dispatched by a Claude Opus 4.6 orchestrator in a claude-code session running `/gsdr:audit`. My task spec was copied inline with all obligations. I am one of three lanes in Wave 1.

**What this position is prepared to notice:**
- Structural comparison between two methodology files (I can read them line by line and diff them substantively).
- Verification of claims against primary sources (Rule 1 is my strong suit — file:line citations cost me nothing).
- Disconfirmation checks against the orchestrator's pre-listed findings (I found one factual error in the orchestrator's list; see I3 Comparison B).
- Narrative-level interpretation of whether a deliberation of f1-modeling's character could emerge from prix-guesser's plan (I am unusually well-suited to this because I run deliberations like f1-modeling's sample as a matter of daily work).

**What this position is NOT prepared to notice:**
- **Code-level reality check.** I did not read prix-guesser's source code (`apps/`, `packages/`). If the content-contract decisions interact with code structure in ways that change the urgency of the methodological apparatus, I would not see it. A general-purpose agent with broader read scope would catch code-methodology interaction issues I miss.
- **External precedents and alternatives.** I have no web access. Lane 1C has this mandate explicitly, so I do not need to duplicate it — but my findings about "precedent analysis is dropped" cannot be paired with "here is what the precedents actually say." Lane 1C will pair them at synthesis.
- **Canon-substance claims.** I read LONG-ARC.md's existence and its role as required reading, but I did not read LONG-ARC.md itself for substance. Lane 1A owns the canon integrity work. If LONG-ARC.md fails to carry the trajectory discipline I am relying on it to carry (see the trajectory compensation argument), my "partially compensated" verdict changes to "not compensated."
- **What a GPT-5.4 xhigh would see.** The prior prix-guesser audit ran A/B Opus/GPT comparison and documented model-specific biases (`prior audit METHODOLOGY-REVIEW.md:28-45`). I cannot replicate that comparison. A GPT-5.4 xhigh reader with the same task spec would likely emphasize different drops, catch different inheritance lines, and may or may not make the same disconfirmation catch I made on Path of Inquiry.
- **What a Sonnet reader with the same rigor would see.** The task spec notes that the orchestrator initially considered Sonnet for this lane and reversed to Opus specifically because of hermeneutic work. I have no way to know whether a Sonnet running the same spec with the same rigor would miss something I caught or catch something I missed. This is a real gap in Wave 1's coverage — all three lanes are Opus, so convergence across lanes cannot be used as a model-class convergence signal.

**What a differently-situated investigator would do differently:**
- **A cross-model auditor (Codex GPT-5.4 xhigh) running this same spec** would likely catch different things. I have seen enough in the f1-modeling PLAN's "Codex cross-model review triggered restructure to δ" note (L305) to know that f1-modeling's methodology treats cross-model audit as load-bearing, and I am not providing one.
- **A general-purpose Opus with web access** running this spec would likely be tempted to fold in Lane 1C's web work ("did the orchestrator's list of drops correspond to what methodology literature considers essential?"). I am deliberately not doing that — my lane is internal comparison — but the absence of that check is real.
- **A reader with full code-reading time budget** would read prix-guesser's app code and check whether the content-contract decisions the initiative is closing actually map to code structures that already have their own implicit contract. The explicit contract decisions in the initiative may be under-specified versions of contracts that already exist in code, or over-specified versions of contracts that code has not yet committed to. I did not do this check.

---

## What Remains Unknown

These questions cannot be answered from the PLAN/PRINCIPLES files alone. They would need observation of how the initiatives execute in practice, or access to artifacts outside my file-read scope.

- **Does prix-guesser's Wave 2A actually produce a deliberation of equivalent character when it runs?** F1-modeling has executed through Wave 2C; prix-guesser has executed nothing. I can compare PLAN shapes, but I cannot observe output character until it exists. My LQ-1B.3 reading (*"adequate-to-equivalent if three specific things are addressed"*) is a hypothesis about execution shape, not an observation of it.

- **Does the Wave 2A deliberation actually absorb the long-arc context at output time, or does it only absorb it at input time?** LONG-ARC.md is listed as required reading. Whether the deliberator produces trajectory-labeled reasoning in its output depends on model behavior I cannot predict from the plan files.

- **Would a Gate 1 review actually trigger expansion or restructuring** under prix-guesser's narrower outcome space? The plan says expansion is a legitimate outcome. Whether the reviewer-orchestrator at Gate 1 actually exercises that permission depends on human (or model) discretion I cannot observe.

- **Whether prix-guesser's discuss-phase workflow absorbs the methodological discipline the initiative does not carry**. I grep-checked the workflow file for trajectory/precedent vocabulary and found shallow mentions only (see framework invisibility). But I did not read the workflow file in full — a full read might reveal that the discipline is encoded under different names. A future audit focused on the discuss-phase workflow as the methodology-carrier would close this question.

- **Whether LONG-ARC.md itself is rigorous enough to compensate for the trajectory-analysis drop**. Lane 1A owns this. If Lane 1A finds LONG-ARC.md is either too shallow or too canon-bound to substitute for produced trajectory analysis, my "partially compensated" verdict softens.

- **Whether prix-guesser's prior research lanes (`2026-04-10-first-wave-xhigh-comparisons/`, etc.) actually contain the precedent analyses the initiative's RESEARCH-PRINCIPLES does not require.** If they do, the "precedent-analysis drop is collateral damage" verdict weakens — the work exists, it's just not imported. If they don't, the drop is real.

---

## How I Navigated Tensions Between Obligations

Three tensions emerged during this lane that I had to navigate rather than resolve by picking a winner.

**Tension 1: Subject obligation (comparative_quality, "compare like with like") vs. investigatory I2 ("let the investigation guide artifact selection").**

The subject obligation says "compare PLAN to PLAN, RESEARCH-PRINCIPLES to RESEARCH-PRINCIPLES, deliberation example to deliberation example." The investigatory obligation says let the investigation pull in artifacts the pre-selection didn't cover. These tensioned when I hit the framework-invisibility question: to answer whether prix-guesser's discipline lives elsewhere, I had to read files outside the strict like-for-like comparison (long-arc-canonization/PLAN.md, discuss-phase workflow, prior audit's METHODOLOGY-REVIEW.md). Reading those is not a like-with-like comparison — it is a cross-shape comparison between prix-guesser's *elsewhere* and f1-modeling's *here*.

**How I navigated it.** I treated the like-for-like comparison as the primary output and the cross-shape reads as *supporting evidence for the framework-invisibility section specifically*. I did not use the long-arc-canonization PLAN to claim "prix-guesser's PLAN is actually as rigorous as f1-modeling's because it has that file" — that would be collapsing the comparison by pretending different shapes are the same shape. I used the cross-shape reads only to argue that the audit's frame (comparing two initiative-internal files) is too narrow to see where the discipline lives, which is the framework-invisibility claim the lane is explicitly required to make. The tension was real; the resolution was "use one reading for the comparison claim and a different reading for the meta-claim about the frame."

**Tension 2: Rule 2 (disconfirmation check) vs. the task spec's pre-listed drops.**

The task spec listed specific drops the orchestrator had already identified and asked me to verify or refute. Rule 2 says I should check what would disconfirm any finding before writing it. These tensioned when the task spec's pre-listing created a temptation to read forward into the claims rather than read the primary sources fresh. If I had trusted the orchestrator's list, I would have written "Path of Inquiry is dropped" — and that would have been wrong. Trust-and-verify is not the same as verify.

**How I navigated it.** I ran the grep checks explicitly for each pre-listed drop, against prix-guesser's RESEARCH-PRINCIPLES.md specifically, before writing the comparison table. This caught the Path-of-Inquiry error. I then made a separate methodological finding: that the orchestrator's error is itself a finding about the audit's frame (the comparative_quality frame invites you to see missing items more readily than hollow items), and I surfaced the error explicitly rather than silently correcting it. Silent correction would have hidden the frame bias from the next reader. The tension was real; the resolution was "correct the error, name the correction, make the error itself a data point."

**Tension 3: Investigatory I3 (present competing explanations) vs. the directness requirements in the output spec.**

The task spec says I must not hedge on LQ-1B.1 ("are the expansion provisions actually equivalent?") and LQ-1B.2 ("are the methodological drops principled?"). I3 says I must present at least two interpretations for each finding and not collapse to one. These tensioned when I had to write the verdicts: "give a direct read without hedging" and "present competing explanations" pulled against each other on the same sentences.

**How I navigated it.** I treated "direct verdict" and "multiple interpretations" as operating at different levels of the finding. For each load-bearing drop, I wrote out the principled reading, the collateral-damage reading, and the compensated reading at the level of *evidence and reasoning*. Then I committed to a direct verdict at the level of *recommendation*. This is not a clean resolution — a reader who disagrees with my collapsed verdict can go back to the evidence-level multiple interpretations and see which one I weighted more and why. The traceability is there, but the directness is also there. If this split is actually not navigating the tension but just smuggling hedging under different labels, I want to flag that possibility honestly. The reader can judge.

---

## Cross-Cutting: Framework Invisibility

*Task spec's grounding question: "Name a concrete finding that would not appear no matter how rigorously this audit was conducted, because of how this audit's scope was framed."*

**The finding the frame hides.** This lane's frame is "compare prix-guesser's initiative PLAN/PRINCIPLES against f1-modeling's initiative PLAN/PRINCIPLES." That frame makes invisible the fact that prix-guesser's methodological discipline is mostly not concentrated in the initiative files at all. It is distributed across:

1. **The `.planning/deliberations/2026-04-11-long-arc-canonization/PLAN.md`** (892 lines). This file contains methodological discipline that is substantively stronger than anything in f1-modeling's vision-alignment PLAN — allowed write sets, forbidden write sets, bounded decision windows with preference/fallback rules, explicit stop conditions, step-by-step acceptance criteria per step, a commit strategy with named commits, and explicit non-goals. The bounded-decision-windows pattern (`long-arc-canonization/PLAN.md:157-234`) is a methodological primitive I have not seen in f1-modeling's initiative and would consider load-bearing for high-risk canon work. This file is not the vision-alignment initiative's file, but it is in the same repo, in the same `.planning/` directory, and it was authored the same week.

2. **The `.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md`** (>100 lines on confounds alone). This is a sophisticated engagement with A/B replication, prompt-drift confounds, runtime-environment confounds, and orchestrator-non-independence confounds. The vocabulary of "the orchestrator is not blind to either pass" (L90-92) is the kind of frame-reflexivity that the vision-alignment initiative's RESEARCH-PRINCIPLES.md does not carry.

3. **The `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`** (1346 lines). I grep-checked this file for trajectory/precedent/reframing vocabulary and found only shallow mentions (4 matches for the whole cluster, and they are thin — *"plausible wrappers...without pulling future scope in"*). The discipline does NOT live in the workflow file in any deep form — terrain mapping vocabulary does (32 matches for the relevant cluster), but the specific elements dropped from the initiative's RESEARCH-PRINCIPLES.md are not carried here in full form.

**The implication.** When I assess "prix-guesser dropped X from f1-modeling's methodology," the honest read is that prix-guesser's *initiative files* dropped X but prix-guesser's *planning surface as a whole* has methodological vocabulary that is at least as sophisticated as f1-modeling's — just distributed differently. The long-arc-canonization PLAN is evidence that the author can write detailed execution discipline when they choose to. The fact that they chose not to for the vision-alignment initiative is either (a) a deliberate choice that the narrower scope does not justify the overhead, or (b) an incomplete inheritance where the methodology vocabulary available in the repo was not imported into this specific initiative.

**A finding that would not appear no matter how rigorously this lane was conducted** within its scope: the absence of a cross-initiative methodology-propagation mechanism. Prix-guesser has three different methodological vocabularies in three different places (long-arc-canonization's execution-discipline style, prior audit's confound-analysis style, vision-alignment initiative's simplified non-foreclosure style). F1-modeling has one vocabulary concentrated in one file that every Codex call reads. Whether the *distributed* pattern or the *concentrated* pattern is better methodology is a question this audit cannot answer within its scope. It is the kind of question that would need a different audit (a process_review or exploratory orientation) to address.

**Where else might the discipline live that I did not check:**
- Other workflow files in `tooling/portable-gsd/overlay/` (research-phase.md, plan-phase.md — I did not read them).
- Other files in the `.planning/deliberations/` hierarchy that are not the long-arc-canonization file.
- The `.planning/knowledge/signals/` subdirectory referenced in f1-modeling's README (I did not check whether prix-guesser has an equivalent).
- The `.planning/explore/` directory (I did not check its contents).
- The per-phase PLAN files at `.planning/phases/01-authored-round-contract/01-*-PLAN.md` — which are committed and visible in git status but I did not read for methodology vocabulary.

A cross-cutting follow-up audit could survey the full methodological vocabulary distribution across prix-guesser's `.planning/` and produce a propagation map. That is out of this lane's scope.

---

## Rule 5 — Frame-Reflexivity (Full Section)

### Grounding Question 1: *"If this lane had been classified as a different subject (e.g., `process_review` instead of `comparative_quality`), what would it have looked for that I didn't?"*

A `process_review × investigatory` lane looking at prix-guesser's vision-alignment initiative would have looked at **the process by which the initiative files themselves were authored**. That process includes:

- Who wrote which file. (The initiative was authored 2026-04-11, same day as this audit. Who was the author — Codex? Claude? The user? I do not know and did not check.)
- Whether the RESEARCH-PRINCIPLES.md was authored fresh, or copied-and-edited from an existing file (the long-arc-canonization PLAN has a different style — which of the two patterns is the author's "default"?).
- Whether the PLAN's reference to `.planning/phases/01-authored-round-contract/01-CONTEXT.md`, `01-RESEARCH.md`, and `01-VALIDATION.md` at L31-33 actually matches what those files contain, or whether the PLAN was authored against an imagined version of them.
- Whether the initiative's "narrowing" was deliberated or assumed. The README at L25-31 says *"This project does not currently have the same kind of wide, cross-domain architectural uncertainty"* — but whether that claim was tested against the four stated open questions (coverage/fallback, answer-target lineage, scoring intent, pack identity) is a process question, not a comparative one.

**A concrete finding I did not produce because my frame was wrong:** I did not check whether the initiative's claim of narrowness was itself audited. The claim "the broader product posture is already relatively well-aligned" is the load-bearing premise of the entire scope reduction, and I took it on faith. A process_review lane would have asked "how was this claim evaluated?" and would have either found an evaluation record or named the absence.

### Grounding Question 2: *"If this lane had been classified with a different orientation (e.g., `standard` instead of `investigatory`), what would it have held open that I closed?"*

A `comparative_quality × standard × self` lane with the same scope would have closed on a verdict cleanly: "Here are the drops. Here is the severity. Recommend restoring reframing permission and calibrated confidence markers." It would not have held open the question of whether the three drops I categorized as "not principled" are actually not principled versus just *differently principled*.

**What I held open that standard would have closed:** The reading that "reframing permission" is load-bearing for this narrow initiative is an inference from f1-modeling's executing behavior. I do not have direct evidence that prix-guesser's single deliberation will actually need to reframe. I argued for the drop being real, but I argued it with a hedge — *"the specific load-bearing question prix-guesser is asking is itself susceptible to reframing"*. A standard orientation would have pushed me to either back that claim with harder evidence (which I do not have without observing the deliberation) or drop it. Investigatory let me keep it as an investigation-shaped finding: "this is the drop I am most concerned about; I cannot prove the concern is correct without observation."

**What I closed that investigatory should have held more open:** I closed on the claim that "the long-arc-canonization PLAN is evidence the author can write detailed execution discipline when they choose to." That framing imputes agency to "the author" — a single entity choosing among methodological vocabularies. A more investigatory read would hold open the possibility that different files in prix-guesser's `.planning/` hierarchy were authored by different models at different times under different framings, and that the *absence of a unified methodological voice* is itself evidence of something (maybe: the project is methodologically experimental; maybe: the project has lost coherence; maybe: the project is genre-mixing deliberately). I am not sure which reading is right. I closed on the "deliberate choice" reading because it is the more charitable one.

### Grounding Question 3: *"What about the current classification shapes what I am prepared to notice and what I am not? Name one concrete example. (E.g., `comparative_quality` orients you toward differences; what similarities might be load-bearing that you did not notice because you were looking for differences?)"*

The `comparative_quality` frame orients me toward differences. I looked for what prix-guesser drops from f1-modeling. I looked less hard for what both projects keep that might itself be the load-bearing thing.

**One concrete similarity I almost failed to notice:** Both initiatives are "scaffolding-not-execution" plans authored 2026-04-10/11 as explicit responses to audit findings. Both have the same four-beat shape underneath (research → review gate → deliberation → decision anchor). Both use the same phrase "scaffolding, not" (`prix-guesser/PLAN.md:9`, `f1-modeling/PLAN.md:9`). Both treat deferral as a legitimate outcome. Both have a "possible outcomes at review gate" section at Gate 1.

**Why this similarity is load-bearing:** It says the two projects *converged on the same structural answer to the same class of problem* (how do you run a vision-alignment initiative before a substrate-freezing planning phase?) and they did so because the same author was working through the same set of lessons learned across both projects. The comparative_quality frame treats the two files as independent data points to compare. The similarity says they are not independent — they are two instances of the same template, and the template is worth naming.

**What I did not produce because the frame is "comparison":** A characterization of the shared template. The methodological inheritance is not just "f1-modeling inherits from prix-guesser's prior work" — it is "both prix-guesser and f1-modeling's current vision-alignment initiatives are instances of the same substrate-freezing-preparation template." That template is more interesting as a methodological artifact than either of its instances. A `standard × self` comparative lane would have collapsed the similarity into "they're similar; here are the differences." A `exploratory × self` lane focused on the template itself would have produced something genuinely new.

### Model-class identity (investigatory I4 reminder)

I am Claude Opus 4.6. The task spec reminds me that "running as Opus does not immunize you against" performative Rule 5. The Rule 5 failure mode I am most susceptible to as Opus is **sophisticated hedging dressed as epistemic humility** — phrases like "I closed on the more charitable reading because..." that preserve my reading while ostentatiously acknowledging I could have read otherwise. The corrective is to note that I produced a direct verdict on LQ-1B.2 ("mostly principled, but three drops cross the line") and I am not walking it back in Rule 5. The Rule 5 section is for *what the frame hides*, not for softening the findings the frame allowed me to see. The three drops I flagged are real. The charitable reading ("the author deliberately chose") does not weaken the finding about the drops; it only changes the story about why they happened.

---

## What The Obligations Didn't Capture

Obligations covered in the lane: core Rules 1-5, investigatory I1-I4 plus "what remains unknown" plus "how I navigated tensions," comparative_quality subject obligations (comparison axis, like-with-like, what the axis makes invisible), framework invisibility cross-cutting.

**What the obligations didn't capture:**

1. **The audit's own methodological lineage.** This lane is itself a substrate-freezing-preparation step — it is prep-quality-scope-audit-2, Wave 1, Lane 1B, authored in response to the user's observation that the first version of the audit was methodologically ironic. The audit inherits from prix-guesser's own methodology work. **The audit is an instance of the same substrate-freezing-preparation template it is auditing.** No obligation in my task spec asks me to notice this. The task spec treats the audit as the auditor and prix-guesser-plus-f1-modeling as the audited. But if the template being used for the audit is the same template being used for the initiative under audit, then finding failures in the template would implicate the audit as well. I do not have enough cross-session context to say whether that is happening. I flag it because the obligations did not make me look at it.

2. **The cross-initiative propagation question.** I surfaced this in framework invisibility. It does not fit any obligation cleanly — it is not strictly comparative (it is about the shape of *distribution* not the shape of difference), not strictly investigatory of the drops (the drops are real regardless of where the discipline lives elsewhere), not framework-invisibility only (it is a concrete finding, not a meta-level claim about what the frame cannot see). It sits across multiple obligations and leaves a residual that needs its own naming.

3. **The status of the audit task spec's pre-listed errors.** The Path-of-Inquiry/Dependencies-and-Relations factual error in the task spec is a finding about the orchestrator's framing. The obligations tell me to correct it and proceed. They do not tell me what to do about the fact that an orchestrator with Opus-level capacity produced a list where two of the eight listed drops were factually wrong. That is a 25% error rate on a pre-listed set of findings that the task spec asked me to "verify or refute." A 25% error rate is high enough that I would not trust a pre-listed set of findings from this orchestrator in future audits without running full primary-source verification. That is not a comparative_quality finding or an investigatory finding — it is a finding about the *upstream* audit process that produced my task spec. The obligations give me no place to put it.

4. **The dispatch decision itself.** The task spec opened with a long explanation of why Opus-not-Sonnet for this lane. I do not think that decision has been validated or refuted by my output. My reading is that the hermeneutic work was real and that I engaged it, but I cannot distinguish "Opus was necessary for this work" from "Opus happened to be the model that did this work acceptably." A Sonnet dispatch on the same task spec with the same rigor might have produced the same output, or a different output, or a worse output. I have no way to know. Claims about model-class necessity from single-model runs should be treated as hypotheses about the dispatch, not confirmations. The obligations did not ask me to engage this question — I am engaging it here because it is what did not fit anywhere else.

5. **The residual methodological question of whether the f1-modeling "concentrated vocabulary" pattern or the prix-guesser "distributed vocabulary" pattern is better.** I surfaced this in framework invisibility but did not take a position. It may be the single most interesting question this lane surfaced, and I have no obligation that tells me what to do with it. Flagging for synthesis.

---

## Cross-Lane Notes For The Synthesizer

- **Lane 1A (canon claim integrity).** My verdict on trajectory-analysis-as-production being "partially compensated by LONG-ARC.md as required reading" depends on Lane 1A's read of LONG-ARC.md's actual substance. If Lane 1A finds LONG-ARC.md is either too shallow or too canon-bound to substitute for produced trajectory analysis, my compensation claim weakens and the trajectory drop becomes closer to "fully lost."
- **Lane 1A.** I noted that prix-guesser's initiative PLAN lists `01-CONTEXT.md`, `01-RESEARCH.md`, and `01-VALIDATION.md` as required reading (`prix-guesser/.../PLAN.md:31-33`). If Lane 1A finds these files are substantively incomplete or unreliable, the whole initiative's foundation weakens.
- **Lane 1C (external gap research).** I explicitly did not do precedent research. My finding that "precedent-analysis discipline drops are not justified by domain difference" is a methodological claim. Lane 1C's finding about what alternatives the research did not consider should pair with my finding about what precedent-analysis discipline the research does not require. If Lane 1C finds many alternatives the initiative did not consider, that is evidence the precedent-analysis drop has operational consequences.
- **Shared finding across lanes (candidate).** I suspect all three lanes will surface something about "the distributed methodology vocabulary" in different forms. Lane 1A may see it as "the canon docs carry what the initiative doesn't." Lane 1C may see it as "external precedents are easy to find and the initiative doesn't require them." I see it as "the initiative files are thinner than the repo's methodological capacity." A Wave 3 synthesis that ties these three readings together would be more valuable than three separate observations.
- **Model-class diversity.** All three Wave 1 lanes are Opus. The synthesizer cannot use cross-lane agreement as a convergence signal because the model class is held constant. If Wave 2 dispatches a cross-model check (e.g., a Codex run on the same task specs), the cross-lane Opus agreements should be treated as a single data point, not three.

---

## Candidates For Wave 2 Follow-Up

1. **Audit the full methodological vocabulary distribution across prix-guesser's `.planning/` surface.** Survey all PLAN files, all deliberations, all audit files, and the tooling workflow files for methodological vocabulary (trajectory, precedent, reframing, calibrated confidence, gray-area handling, etc.) and produce a propagation map. Subject: `process_review × exploratory × self`. Purpose: settle whether prix-guesser's distributed-vocabulary pattern actually covers the methodological ground or only appears to.

2. **Cross-model replication of this lane.** Run a Codex GPT-5.4 xhigh against the same task spec. Compare findings. Specifically check whether a non-Opus reader would catch the Path-of-Inquiry factual error in the orchestrator's pre-list, and whether a non-Opus reader would come to the same three-drops-are-not-principled verdict. Subject: `comparative_quality × investigatory × cross-model`. Purpose: test the dispatch decision's claim that Opus is the right model class for this work.

3. **Execute Wave 2A of the vision-alignment initiative with the three specific changes I recommended** (author prompt at Gate 1, require Trajectory Check per closed contract, add reframing permission). Compare the output to what the current PLAN would produce. Subject: the initiative itself, not an audit. Purpose: observational test of whether the three changes I flagged actually change the deliberation character.

4. **Characterize the shared "substrate-freezing-preparation template"** that both prix-guesser and f1-modeling's vision-alignment initiatives instance. This is the Rule 5 finding I did not produce because the frame is comparison. Subject: `process_review × exploratory`. Purpose: extract the template so future substrate-freezing initiatives can instance it explicitly instead of by ad-hoc adaptation.

5. **Audit the audit's own methodological lineage.** Check whether `/gsdr:audit`'s command-as-orchestrator pattern, the task spec authoring process, and the wave-dispatch pattern themselves inherit from the same methodology the audit is auditing, and whether the audit would catch failures in the pattern if the pattern is what is being used. Subject: `process_review × investigatory × self`. Purpose: the recursive check the current audit's obligations do not ask for but the current audit's existence implies is needed.

---

*End of Lane 1B output. Awaiting Wave 3 synthesis.*
