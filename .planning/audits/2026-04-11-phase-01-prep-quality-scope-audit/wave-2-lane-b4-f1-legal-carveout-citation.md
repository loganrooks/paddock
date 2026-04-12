---
date: 2026-04-11
wave: 2
lane: B4
audit_subject: claim_integrity
audit_orientation: standard
audit_delegation: self
auditor_model: claude-sonnet-4-6
agent_type: gsdr-auditor
scope: "Empirical verification: does the prix-guesser canon cite F1's fan-use trademark carveout, or any other legal rationale for the private-only posture? Primary check (LQ-B4.1, LQ-B4.2) plus framing assessment (LQ-B4.3), slot identification (LQ-B4.4), and gap-or-choice indicators (LQ-B4.5)."
triggered_by: "wave-2 dispatch after Review Gate 1; prompted by Lane 1C Finding 1"
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

# Wave 2 / Lane B4 — F1 Legal Carveout Citation Check

**Model:** Claude Sonnet 4.6 (the only Sonnet lane in Wave 2; B2 and B3 are Opus).
**Classification:** claim_integrity × standard × self

---

## Question and Scope

Does the prix-guesser canon cite F1's fan-use trademark carveout — specifically the language from `https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt` that Lane 1C quoted — or any other legal rationale for the private-only posture? If not, where in the canon should that rationale live?

The canon files searched: `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`. The discovery directory (`discovery/05-content-and-rights.md`, `discovery/14-gsd-seed.md`, `discovery/07-sources.md`) was also searched as pre-canon material referenced by PROJECT.md line 37. Phase 01 artifacts (`.planning/phases/01-authored-round-contract/01-CONTEXT.md`) and the predecessor audit synthesis (`.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`) were checked for coverage of the legal question.

The task spec's fit assessment is correct: this question has a direct empirical answer. The canon either contains the legal rationale or it does not. Standard orientation closed appropriately. No orientation shift to investigatory was required — the evidence is unambiguous.

---

## Artifacts Examined

- `.planning/PROJECT.md` (full, 192 lines)
- `.planning/LONG-ARC.md` (full, 155 lines)
- `.planning/ROADMAP.md` (lines 1–80 read; legal-term grep across full file)
- `.planning/REQUIREMENTS.md` (full, 192 lines)
- `.planning/STATE.md` (full, 82 lines)
- `discovery/05-content-and-rights.md` (full, 126 lines)
- `discovery/14-gsd-seed.md` (legal-term grep)
- `discovery/07-sources.md` (legal-term grep)
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md` (legal-term grep)
- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md` (lines 1–60; legal-term grep across full file)
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md` (lines 1–410, full)
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1a-canon-integrity.md` (full, read in two passes)

---

## Search Ledger

I ran case-insensitive searches across canon files (PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md, STATE.md) and discovery files for every term the task spec specified plus several variants. Results below.

### Term: `guidelines.4EOKE9RRqevL4niTK9kWyt` (the specific Lane 1C URL)

**Result:** Zero matches across all canon and discovery files.

### Terms: `trademark`, `copyright`, `intellectual property`, `\bIP\b`, `fan use`, `fair use`, `fan-made`, `educational purpose`, `private use`

**Result:** Zero matches in canon files (PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md, STATE.md). Zero matches in discovery files (05-content-and-rights.md, 14-gsd-seed.md, 07-sources.md). Zero matches in 01-CONTEXT.md.

In SYNTHESIS.md, the only match is a non-legal usage: "unofficial F1 broadcast production" as a design aesthetic phrase (`SYNTHESIS.md`, CONVERGENCE.md line 112), not a legal characterization.

### Terms: `unofficial`, `unauthorized`

**Canon results:**

- `PROJECT.md:5` — "Prix Guesser is an **unofficial**, private-only F1 fan game project"
- `PROJECT.md:141` — "Private-only, **unofficial** fan project"
- `01-CONTEXT.md:157` — "This is a private-only, **unofficial** fan project for trusted-circle play"

**Discovery results:**

- `discovery/01-vision.md:5` — "An **unofficial**, private-only fan-made party game"
- `discovery/03-reference-designs.md:8` — "private-only fan project"
- `discovery/07-sources.md:11` — "private-only fan project"
- `discovery/README.md:12` — "unofficial fan product"

In all cases the word "unofficial" appears as a project-identity label — it describes what the project *is*, not why the project chose to stay private-only. None of these passages reference F1's rights, F1's trademark guidelines, or any legal instrument as the basis for the "unofficial" characterization.

### Terms: `rights`, `license`, `licensed`, `licensing`

**Canon results:**

- `LONG-ARC.md:78` — "narrower interaction rights than full public participation" (visibility-ladder context; this is about user access rights in a product sense, not F1's intellectual property rights)
- `REQUIREMENTS.md:150` — "Public-release legal or commercial hardening | This project is private-only for now" (Out of Scope table)
- `ROADMAP.md` — no matches for rights or licensing terms

**Discovery results:**

- `discovery/03-reference-designs.md:13` — "what creates the strongest play, watchability, fan delight, and mode expansion headroom if **legal publishing constraints are temporarily set aside**?" (the word "legal" appears here but as a reason to *bracket* the concern, not as a named constraint grounded in F1's actual policy)
- `discovery/09-feasibility.md:230` — "a public-safe, rights-clean, large-scale content corpus" (under a "not the goal" framing)
- `discovery/05-content-and-rights.md` — the entire document discusses content source types and fragility but never names F1 as a trademark holder, never cites F1's guidelines, and frames the rights question as "lower-fragility vs higher-fragility material types" rather than as a legal constraint

### Terms: `legal`, `liability`

**Canon results:** Zero matches.

**Discovery results:**

- `discovery/03-reference-designs.md:13` — "legal publishing constraints" (as above — bracketing the concern rather than naming it)

**Phase 01 artifacts:**

- `.planning/phases/01-authored-round-contract/superseded/2026-04-11-pre-rerun-overreach/phase/.continue-here.md:556` — "Private-only project — NO commercialization, no public release, no legal/commercial hardening needed" (superseded file; not in the active canon)

### Predecessor audit (SYNTHESIS.md)

- `SYNTHESIS.md` legal-term search: zero matches for trademark, copyright, IP, fan use, fair use, educational purpose, licensing. One match for "unofficial F1 broadcast production" as an aesthetic phrase, not a legal one. The predecessor audit did not address F1 rights or legal rationale at all.

---

## Findings

### LQ-B4.1 — Does the canon cite F1's fan-use carveout URL?

**Verdict: No.**

The specific URL `guidelines.4EOKE9RRqevL4niTK9kWyt` and any variant of `formula1.com/en/information/guidelines` appear nowhere in the canon (PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md, STATE.md), the discovery directory, phase context files, or the predecessor audit SYNTHESIS.md.

The search was exhaustive. The absence is confidently claimed: the URL was not cited, not paraphrased with attribution, not referenced by name.

*What would disconfirm this (Rule 2 check):* I searched for partial URL variants, domain names, and guideline keywords before claiming absence. No evidence emerged.

### LQ-B4.2 — Does the canon cite any legal rationale for private-only?

**Verdict: No.** The canon uses the word "unofficial" as a project-identity descriptor but does not ground that descriptor in any legal rationale. The absence is across all canonical dimensions:

- No mention of F1 trademark, F1 copyright, or F1 intellectual property
- No mention of fan use, fair use, or any legal doctrine
- No mention of F1 as a rights-holder whose permissions constrain the project
- No mention of what "private" provides legally that "public" would not

The single closest passage is `REQUIREMENTS.md:150`:

> "Public-release legal or commercial hardening | This project is private-only for now"

This names "legal hardening" as an out-of-scope item, but frames the absence of that hardening as a *scope choice* rather than naming the specific legal exposure that would require it. The canon does not say "F1's trademark policy requires private-only use to avoid express-license obligations." It says "we don't need to do hardening for legal reasons because we're private-only." This is circular: the legal rationale for the posture is absent; only the posture's label is present.

*What would disconfirm this (Rule 2 check):* Before claiming absence, I checked whether the discovery file `05-content-and-rights.md` engaged the legal rationale — it came closest, with its "higher-fragility material types" section distinguishing official logos and stylized branding from safer content. But this is a content-risk inventory, not a legal-rationale statement. It does not name F1 as a rights-holder, does not cite any F1 policy, and does not explain what legal status the "private-only" label actually provides.

*What the measure captures vs. does not capture (Rule 3):* I measured whether the canon contains explicit or paraphrased legal rationale grounded in F1's own guidelines. What this does not measure: whether the project owner has read F1's guidelines independently and made a tacit decision that citing them is not necessary. That is invisible to a document-reading lane.

### LQ-B4.3 — How does the canon frame the private-only decision?

The primary framing is as a **product and scope decision**, not a legal constraint. The Key Decisions table in `PROJECT.md:153` reads:

> "Initialize as a private-only fan project | Public-safe constraints would distort the early product and reduce fidelity | Adopted"

The rationale given — "public-safe constraints would distort the early product" — is a product-quality argument. It says going public would require compromises that harm the design. This is the YAGNI/scope-management framing Lane 1C identified: "private-only" is being justified as better for the product, not as required to avoid legal exposure.

Additional framing instances:

- `PROJECT.md:30` — "Public-release hardening, rights-clean commercialization, and distribution-safe compromises — this is private-only for now." The phrase "rights-clean commercialization" is interesting: it acknowledges that a public release *would need* rights-cleanliness, but doesn't name what rights are involved or why private-only avoids the issue.

- `PROJECT.md:141` — "Private-only, unofficial fan project — early choices should optimize for real play value instead of public-safe caution." Again, product optimization as the frame.

- `LONG-ARC.md:58-68` — The Transition Doctrine section argues that moving toward public hosting means accepting increased "trust and accountability" obligations. This is framed in terms of service obligations (moderation, uptime, support), not legal obligations (IP rights, trademark compliance).

**Concrete characterization:** The canon frames private-only as a *product scope decision* — "we're private so we can make better design choices without worrying about public-safe caution." The legal dimension — "we're private because F1's own trademark guidelines carve out private educational use while prohibiting public use without an express written license" — is entirely absent. The canon is making a legal decision without acknowledging that it's legal.

This is the untyped load-bearing assumption the task spec specifically asked to surface. The absence is load-bearing because the justification for private-only in the Key Decisions table would be *strengthened substantially* by a legal grounding, and the posture could be *undermined* if the "private is better for product quality" argument later loses force (e.g., if the project seriously considers share-by-link or unlisted hosting) without the legal grounding to hold the posture in place independently.

### LQ-B4.4 — If the citation is missing, where should it live?

The citation is missing. The right slot:

**File:** `.planning/PROJECT.md`, Constraints section (lines 139–146) or Key Decisions table (lines 149–159).

The Constraints section currently reads:

> "**Product scope**: Private-only, unofficial fan project — early choices should optimize for real play value instead of public-safe caution."

This is the primary location where new readers first encounter the private-only posture as a constraint. Adding the legal rationale here converts the constraint from a scope label into a grounded architectural decision.

The Key Decisions table row for "Initialize as a private-only fan project" is the second natural location. The Rationale column currently reads "Public-safe constraints would distort the early product and reduce fidelity." A legal grounding can be added there without replacing the product-quality rationale.

**Form:** Constraint annotation or Key Decision rationale augmentation — not a new file, not a new section. This is a one-line or two-line addition, not a new document.

**Minimum viable text (for the Constraints section):**

> "Private-only, unofficial fan project — F1's own trademark guidelines carve out 'limited use for a private, educational purpose only' as permissible fan use, while requiring an express written license for any public use of FORMULA 1 Rights. Early choices should optimize for real play value within this licensed zone rather than incurring public-safe caution or distribution overhead that private use does not require."

**Minimum viable text (for the Key Decisions table):**

> Augment the Rationale cell to read: "Public-safe constraints would distort the early product and reduce fidelity; additionally, F1's trademark guidelines explicitly permit private fan use while requiring an express license for public use of FORMULA 1 Rights."

The source attribution should cite Lane 1C's finding and, if the owner can verify it directly, the URL: `https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt`.

**Why not a new file?** A new "LEGAL-NOTES.md" or "RIGHTS.md" would over-architecturalize a one-sentence rationale. The appropriate register is a canon annotation — a grounding clause in an existing constraint or decision row. Escalating to a new file implies legal-document intent that this is not. The discovery directory already has `05-content-and-rights.md` for deeper content-risk reasoning; if the legal rationale citation is to live anywhere beyond PROJECT.md, it should go there rather than in a new canon-level file.

### LQ-B4.5 — Is the absence a gap or a choice?

**Reading: more likely a gap than a choice, with meaningful uncertainty.**

Indicators toward gap (legal context unexamined):

1. The canon uses "unofficial" as a project identity label but never once references F1 as a rights-holder. A project owner who had consciously engaged with F1's trademark guidelines and decided not to cite them in the canon would almost certainly have left some trace — a comment in discovery notes, a note in the CONTEXT file, or at minimum a "this is intentionally not cited here" remark. No such trace appears anywhere in the searched corpus.

2. `discovery/05-content-and-rights.md` engages in a relatively careful content-risk inventory (distinguishing logos and broadcast assets from geography and rules content) but does this *without referencing F1's own policy*. If the owner had read F1's guidelines, the discovery file's content-fragility distinctions would likely have been organized around the policy's carveout language rather than being independently constructed. The absence of the policy as an anchor for the fragility reasoning suggests the policy was not consulted.

3. The predecessor audit (SYNTHESIS.md) also never references F1's trademark guidelines despite auditing the project's distribution posture across four lanes. This supports the hypothesis that the legal dimension was not in circulation in the pre-execution review discussions.

4. Lane 1A confirmed the private-only posture is "asserted in PROJECT.md:5, 30, 141, 153 and argued in LONG-ARC.md:58–68 and REQUIREMENTS.md:134–138" — but the arguments in LONG-ARC.md are about service obligations and the arguments in REQUIREMENTS.md are about deferred features, not about legal rights. The reasoning chain is entirely product-facing.

Indicators toward choice (legal context known, not cited):

1. The canon does use the phrase "rights-clean commercialization" at `PROJECT.md:30`, which implies awareness that public commercialization involves rights questions. This is not the same as awareness of F1's specific trademark guidelines, but it does show the owner is not entirely unaware that IP rights exist in the space.

2. `discovery/05-content-and-rights.md` names "official logos and stylized branding" and "exact circuit outlines if later public sharing matters" as higher-fragility material — this shows some IP awareness, just not an F1-policy-specific one.

3. The project might deliberately avoid citing legal sources in a product canon to avoid the appearance of manufacturing legal cover or treating the canon as a legal document. This is a legitimate framing choice even if the owner knows about the guidelines.

**Document-reading limit, explicitly flagged:** This lane cannot determine whether the project owner has personally read F1's trademark guidelines. The indicators above are document-level signals about what left traces in the canon. The owner may know about the guidelines and have made a considered choice not to cite them; the canon-level evidence cannot distinguish that scenario from one where the guidelines were not consulted. The synthesizer should treat the gap-probability as high but not certain.

**Operative implication regardless of gap-or-choice:** Even if the absence is a deliberate choice, naming the legal rationale in the canon would strengthen the posture. If "private-only" rests only on a product-quality argument ("public-safe constraints would distort the product"), the posture is vulnerable to any argument that public hosting could be done *without* distorting product quality. A legal grounding is not vulnerable to that argument — F1's guidelines say "no public use without an express written license" regardless of whether the public use would distort the product.

---

## Chain Integrity

### Lane 1C — F1 carveout quotation

The task spec is correct: I cannot re-verify the external URL. I rely on Lane 1C's WebFetch in good faith.

Lane 1C's quoted passage from `wave-1-lane-1c-external-gap-research.md:236-243`:

> "Limited use of our Other Intellectual Property Rights for educational purposes may be acceptable where the use is justified, limited, and non-commercial. However, please note, this does not include public postings such as YouTube, websites and social media. It must be for a private, educational purpose only."

And:

> "Motorsport simulators and/or software that simulates auto racing (including those that are digital only or those that incorporate physical elements such as racing car chassis) should not make any use of the FORMULA 1 Rights without an express written license."

**Dependency flagged for synthesizer:** My LQ-B4.4 recommendation (the minimum viable text for the Constraints annotation) depends on this quotation being accurate. If Lane 1C's WebFetch was incorrect or the guidelines have changed, the specific language I've suggested would need revision. The *existence of a citation gap* (LQ-B4.1 and LQ-B4.2 verdicts) does not depend on Lane 1C's quotation — that finding is grounded in canon searches alone.

The two-part tension in Lane 1C's quotation is also worth noting for the synthesizer: the first passage carves out private educational use; the second passage says motorsport simulators/software "should not make any use of the FORMULA 1 Rights" without an express license. Prix-guesser is arguably a software product (not strictly a "motorsport simulator," but the second passage's "digital only" language creates ambiguity). Lane 1C addressed this tension in LQ-1C.4 but didn't fully close it. My lane's scope does not include resolving that ambiguity — I flag it so the synthesizer can route it to appropriate follow-up.

### Lane 1A — prior legal-question coverage

Lane 1A conducted a broad canon integrity audit with claim re-verification across 12 predecessor recommendations (REV-1 through REV-12). I checked Lane 1A's output for any coverage of F1 rights or trademark issues.

**Finding:** Lane 1A did not address the legal dimension at all. The audit's LQ-1A.1 "private-only fan project" test case lists all the canon appearances of the private-only posture (`wave-1-lane-1a-canon-integrity.md:252-265`) and assesses whether the posture is "argued or asserted," but does not ask whether the argument engages F1's legal position. Lane 1A's LEV-* series does not include a REV entry for any predecessor recommendation about legal rationale, because the predecessor audit (SYNTHESIS.md) itself did not surface the legal dimension.

This confirms: my lane is doing new verification work, not duplicating Lane 1A's scope. Lane 1A had a broader scope and a different focus (claim chains between predecessor audit and current canon); the legal-rationale check was not part of that scope. The citation gap is real and independently confirmed by this lane's direct search.

---

## Cross-Lane Notes for the Synthesizer

**For Lane B2 (authoring sustainability):** The legal framing has an indirect bearing. One risk in Lane B2's scope is whether the project's posture is stable enough to support sustained authoring investment. The legal grounding matters here: if "private-only" rests only on a product-quality argument, it is more susceptible to scope-creep pressure ("we could make it semi-public without hurting quality"). A legal grounding stabilizes the posture as a hard constraint rather than a preference. Lane B2 should be aware that the absence of a legal citation makes the private-only posture slightly more fragile to internal pressure.

**For the synthesizer — the two-passage tension in Lane 1C's F1 quotation:** The first passage carves out "private, educational purpose only" as permissible. The second passage says motorsport simulators and software "should not make any use of the FORMULA 1 Rights without an express written license." Whether prix-guesser (a browser-based game with authored F1 content, not strictly a "motorsport simulator") falls under the second passage rather than the first is an unresolved ambiguity. Lane 1C noted this without closing it. My lane cannot close it without web access. The synthesizer should flag this for the project owner as an open question that the citation, if added to the canon, should honestly acknowledge rather than paper over.

**Factual claim check on the task spec:** The task spec at line 123 refers to "PROJECT.md's 'Constraints' section (around lines 139–147 per the parent task spec's citation)." The actual Constraints section in the current PROJECT.md runs from line 139 to line 146. This is accurate. No factual error found in the task spec's file-location claims for the canon files I verified directly.

---

## What the Obligations Didn't Capture

Two things emerged that don't fit neatly into the claim_integrity × standard obligations:

**1. The discovery directory is doing the work the canon should be doing, more honestly than the canon.** `discovery/05-content-and-rights.md` is not a canon file — it's pre-GSD discovery material — but it engages with the rights question more substantively than any canon file does. It distinguishes higher-fragility from lower-fragility content, names "official logos and stylized branding" and "exact circuit outlines if later public sharing matters" as risk categories, and explicitly tracks "source opportunities and practical boundaries for a private-only unofficial fan product." This is essentially the kind of thinking that should have been canonized and cited. Instead it sits in a discovery file that the canon references only once (PROJECT.md:37, "This project started with a pre-GSD discovery pass captured in `discovery/`") without extracting its legal-risk reasoning into the canon's constraint layer. The obligation framework asked me to check whether the legal rationale was in the canon; I found it more-or-less absent from the canon but present in attenuated form in a discovery file the canon does not promote. That's not exactly a citation gap — it's a knowledge-promotion failure: the project has some rights-related thinking, but it has not been elevated to the layer where it would actually constrain planning decisions.

**2. The "rights-clean commercialization" phrase in PROJECT.md:30 is doing more than it appears.** The Out of Scope entry "Public-release hardening, rights-clean commercialization, and distribution-safe compromises — this is private-only for now" contains the compound phrase "rights-clean commercialization." This implies awareness that commercialization involves rights questions. But the phrase is buried in a scope-exclusion list; it reads like a label rather than a grounded claim. A reader of the canon encounters this phrase and learns "public commercial release would need rights-cleaning" but does not learn "F1's own guidelines require an express written license for any public use." The canon is gesturing at the legal dimension without pointing to it. This is an intermediate state between full awareness and full absence — and the standard claim_integrity obligations (verify presence/absence of a citation) don't have a clean category for "the concept is gestured at but the grounding is absent."

---

## Rule 4 (Escape Hatch)

The main escape-hatch finding: the classification as claim_integrity × standard was correct for LQ-B4.1 and LQ-B4.2 (pure presence/absence check), but the generative secondary question (LQ-B4.4, LQ-B4.5) pushed briefly into territory closer to a design-review or requirements-analysis orientation. I did not shift the orientation — the task spec explicitly anticipated this and said to stay standard unless the empirical check became complicated. The empirical check was not complicated; the evidence was unambiguous. The generative questions were bounded and I handled them within standard orientation. No escape hatch was needed, but the boundary was visible.

---

## Rule 5: Frame-Reflexivity (Lightweight — Standard Orientation)

**If classified as requirements_review instead of claim_integrity:** A requirements_review would have asked whether a *legal-compliance requirement* exists in the canon — whether there is a named, testable obligation like "the project must maintain private-only hosting to comply with F1's trademark guidelines." That framing would have found, in addition to the citation gap, that no such requirement exists as a formally stated rule. REQUIREMENTS.md has no legal-compliance requirement. A requirements_review would have surfaced the regulatory gap at a higher level of severity than my claim_integrity check, which found "no citation" without explicitly asking "should there be a requirement?"

**If classified with investigatory orientation:** An investigatory lane would have held open the gap-or-choice question (LQ-B4.5) rather than settling on "more likely a gap." My standard-orientation reading committed to an assessment of the evidence; an investigatory reading would have demanded more to rule out the "deliberate choice" interpretation before settling. The assessment I gave is conditional — I flagged the document-reading limit explicitly — but standard orientation led me to close on an assessment rather than leaving it fully open.

**What the claim_integrity × standard classification shapes attention toward and away from:** It shaped attention toward "is the citation present or absent?" (present/absent is a verifiable state) and away from "is the absence of the citation itself a problem?" (a value question about what the canon *should* contain). I answered LQ-B4.4 (where should it live?) as a generative follow-up, which helped — but the primary engine of the audit was citation verification, not normative analysis of what the canon's silence means for the project's legal exposure. The normative question is real and I named it in LQ-B4.5, but it is not what claim_integrity's orientation was designed to produce.
