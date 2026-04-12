---
date: 2026-04-11
wave: 2
lane: B2
audit_subject: requirements_review
audit_orientation: investigatory
audit_delegation: self
auditor_model: claude-opus-4-6
agent_type: gsdr-auditor
scope: "Investigate whether authoring sustainability should be owned as a canon claim in prix-guesser, and if so, in what form. Apply the three-outcome framing (canon-wrong-to-not-own / canon-right-to-defer / canon-already-owns-in-form-Wave-1-missed) to each sub-question. Re-verify the Wave 1 lane findings that triggered this lane rather than inheriting them."
triggered_by: "wave-2 dispatch from phase-01-prep-quality-scope-audit-2 orchestrator after Review Gate 1; cross-lane convergence on authoring sustainability as the strongest load-bearing finding from Wave 1"
parent_task_spec: phase-01-prep-quality-scope-audit-2-task-spec.md
task_spec: wave-2-lane-b2-opus-authoring-sustainability-task-spec.md
predecessor_lanes:
  - wave-1-lane-1a-canon-integrity.md
  - wave-1-lane-1b-methodological-inheritance.md
  - wave-1-lane-1c-external-gap-research.md
predecessor_audits:
  - .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md
  - .planning/audits/2026-04-08-pre-execution-review/lane-4-multi-milestone-vision.md
ground_rules: "core+investigatory+requirements_review+chain+framework-invisibility"
tags:
  - wave-2
  - lane-b2
  - authoring-sustainability
  - requirements-review
  - investigatory
  - opus
---

# Wave 2 / Lane B2 — Authoring Sustainability As Canon Claim (Opus)

**Classification:** `requirements_review × investigatory × self` (Claude Opus 4.6, gsdr-auditor subagent, file-reads only, no web)

---

## I1 — The Discrepancy, Named Concretely

The discrepancy this lane started from is not the one the orchestrator stated. The orchestrator stated:

> "the canon does not appear to claim [authoring sustainability] (per Lane 1A); the narrow initiative excludes in-app authoring UI (per Lane 1B). Is the discrepancy real, or is it a misreading that three Wave 1 lanes converged on because they were oriented to find it?"

After re-verifying Lane 1A's search directly against the canon files, the actual discrepancy is sharper and more interesting than the orchestrator's framing:

**Layer 1 — the predecessor's risk claim.** `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md:186`: *"Content authoring is too painful → corpus never reaches critical mass (both ranked this #1)"*. The risk is real, specific, and cross-model convergent in the predecessor audit. Its concrete form is elaborated in `.planning/audits/2026-04-08-pre-execution-review/lane-4-multi-milestone-vision.md:191-200` ("Risk A: Content Authoring Is Too Painful (Effort Risk)") with a named mitigation — a **time-per-round measurement** with a pain threshold — not merely a hand-wave.

**Layer 2 — the research layer.** `.planning/research/PITFALLS.md:253-267` is a whole numbered section titled **"Pitfall 14: Delaying content validation and authoring support until the corpus is already painful"** rated Severity: High, with the specific warning *"Every new round requires code edits, manual image rescue, and fragile spreadsheet habits. Content velocity collapses right when the project needs more packs to learn."* And `PITFALLS.md:305`: `| Authoring Tools + Expansion | Tooling arrives only after content velocity collapses | Build validation/import first, UI tooling second |`.

**Layer 3 — the canon's most-adjacent language.** Lane 1A searched the canon for *"authoring sustainability," "author workload," "corpus critical mass," "authoring pain"* and reported "Nothing at the canon level" (`wave-1-lane-1a-canon-integrity.md:382`). That search was too narrow. A broader grep against `PROJECT.md` for `corpus|sustain|content operations|content scaling|content ops|workload` returns seven hits, the load-bearing ones being:
  - `PROJECT.md:25`: *"Build a curated content corpus strong enough to prove the core loop..."* (requirement, assumes viability, doesn't own the risk)
  - `PROJECT.md:98`: *"the same substrate can support asynchronous, remote, recurring, and more sustainable content operations"* (Milestone 2 goal — the word "sustainable" is in the canon but scoped to M2)
  - `PROJECT.md:105`: *"authoring and preview tooling that make content production sustainable"* (Milestone 2 *deliverable*, not M1 risk posture)
  - `PROJECT.md:167`: *"Which answer surfaces should become first-class in the authored round model? | This determines schema design, scoring logic, and **content authoring workload** | Critical | Pending"* — the phrase "content authoring workload" is in the canon, embedded as a *consequence* of a schema decision inside the Open Questions table, not as a standalone risk claim.
  - `LONG-ARC.md:52`: *"Milestone 2... content operations maturity"* (M2 phrase, not M1 risk posture)
  - `REQUIREMENTS.md:71`: v1 section header `### Content Operations And Calibration` (OPS-01/02/03 — coverage class, session outcome telemetry, testability; none of these engage authoring effort)
  - `REQUIREMENTS.md:104, 115`: v2 section headers `### Content Operations` (OPS-V2-01/02/03) and `### Content Scaling` (CONTENT-01/02) — and these are **uncited as motivation** (contrast with v1 OPS items at `REQUIREMENTS.md:74, 76` which cite `PITFALLS.md#Pitfall 6` and `#Pitfall 9`; none of OPS-V2-* or CONTENT-* cite `PITFALLS.md#Pitfall 14`)

**The discrepancy restated.** The canon contains *the vocabulary* of content operations and content sustainability, but it uses that vocabulary exclusively as an M2 goal / deliverable / seam-preservation — never as the M1 frame "the biggest single risk to whether this project has enough fun rounds to run a game night" that both predecessor passes independently landed on. And `PITFALLS.md:253` directly owns Pitfall 14, but `PITFALLS.md` is *research*, not canon, and no canon requirement cites Pitfall 14 specifically (verified via `Grep` of `REQUIREMENTS.md` for `PITFALLS` — it cites Pitfalls 6, 8, and 9 only).

So Lane 1A was **factually slightly wrong** (the canon contains adjacent vocabulary Lane 1A's narrower search missed) but **substantively mostly right** (no canon file owns the risk as a load-bearing M1 concern; the adjacent vocabulary is scoped to M2 or embedded as a Q-consequence). The discrepancy this lane must resolve is not "absent or present" — it is "present as M2 vocabulary, absent as M1 risk posture, and the predecessor's risk framing was M1."

Why the discrepancy-as-reframed matters. If the risk is genuinely M1-shaped, then the canon's M2-scoping is a category error and the canon should name the risk at M1. If the risk is genuinely M2-shaped, then the canon's M2-scoping is correct and the predecessor audit was ranking an M2 risk as #1 when the real #1 M1 risk is something else ("the game is not actually fun", `SYNTHESIS.md:187`, was ranked #2). This is exactly the kind of question the three-outcome frame needs to hold open.

---

## I2 — How The Investigation Unfolded

The investigation departed from the orchestrator's suggested read list in three places.

**Departure 1: Running my own grep of the canon rather than trusting Lane 1A's search.** Chain integrity required re-verification. I searched `PROJECT.md`, `LONG-ARC.md`, `ROADMAP.md`, `REQUIREMENTS.md`, and `STATE.md` with a broader term set than Lane 1A: `authoring|author\b|corpus|sustain|content operations|content scaling|content ops|workload|burn|pack production|round production|authoring workload|author burnout|content authoring|painful|critical mass`. This caught the "content authoring workload" appearance at `PROJECT.md:167` that Lane 1A's narrower term set missed. **This is a finding about the audit chain:** Lane 1A's "nothing at the canon level" (`wave-1-lane-1a-canon-integrity.md:382`) is a search-terms-specific claim, not a canon-substance-specific claim. The claim holds for the specific phrases Lane 1A tried; it weakens for the broader vocabulary set.

**Departure 2: Reading `.planning/research/PITFALLS.md` in full.** The orchestrator's read list named the canon files and the distributed-methodology candidates but not the project's own risk research. PITFALLS.md is not canon, but it is *cited* by REQUIREMENTS.md as motivation for requirements (`REQUIREMENTS.md:54, 74, 76`) — meaning the canon has a formal intake mechanism from PITFALLS.md. Checking whether Pitfall 14 is cited anywhere in canon-via-this-mechanism is directly relevant to the "is the risk owned in a form Wave 1 missed" question. It is not cited. The intake mechanism exists and was *used* for Pitfalls 6, 8, and 9 but was not used for Pitfall 14. That is a concrete canon integrity finding the suggested read list did not aim at.

**Departure 3: Reading `.planning/audits/2026-04-08-pre-execution-review/lane-4-multi-milestone-vision.md` directly rather than trusting the SYNTHESIS.md summary of it.** The orchestrator said to verify the "#1 ranking is actually supported by the predecessor's methodology rather than being a rhetorical prioritization." The only way to check the ranking mechanism is to read the primary lane that produced the ranking, not the synthesis that compiled it. Reading Lane 4 directly revealed:

  - Lane 4 named the risk as **"Risk A: Content Authoring Is Too Painful (Effort Risk)"** (`lane-4-multi-milestone-vision.md:191`) — a **category** ("Effort Risk"), not a numerical rank.
  - Lane 4 gave the risk a **concrete operationalization**: *"If creating one round takes more than 15-20 minutes of focused work, the content corpus will never reach critical mass"* (`lane-4-multi-milestone-vision.md:194`).
  - Lane 4 gave the risk a **specific mitigation**: *"After the first 5 rounds are authored, do a time audit. If a round takes more than 30 minutes, prioritize authoring tooling over additional game features"* (`lane-4-multi-milestone-vision.md:200`), and `MR-3` at line 264: *"Track authoring time per round and set a pain threshold"*.
  - Lane 4 placed it as the *first* listed risk in a list where risks are named A, B, C — alphabetical rather than ranked. The "both ranked this #1" claim at `SYNTHESIS.md:186` is a synthesis-level *interpretation* of the fact that both passes named it as a biggest-risk, **not** a primary-source ranking. The ranking mechanism is rhetorical convergence between two independent passes (which is still meaningful but is not a scored prioritization).

This matters for I3 because it opens an interpretation the orchestrator's framing did not: the predecessor's "#1" is not a methodologically-produced rank; it is both-passes-naming-it-first. And that naming-first might be because it is first *alphabetically* in Lane 4's list. Lane 1A treated the ranking as if it were methodologically produced; Wave 1 as a whole inherited that treatment. I am not claiming the risk is unreal — the risk is clearly substantive in both passes. I am claiming the specific claim "ranked #1" is softer than Wave 1 treated it.

**Departure 4 (attempted, negative result): Searching the long-arc canonization PLAN for authoring-sustainability vocabulary.** Lane 1B's framework-invisibility claim named this file as the strongest distributed-methodology file and implicitly raised the possibility that the risk might be owned there. I grepped it for `authoring|author\b|content workload|corpus|content operations|content scaling|pack production|round production|sustainability|sustain|burn` (case-insensitive). **Zero matches.** The long-arc canonization PLAN is about the *meta-work of canonizing LONG-ARC.md into the canon*, not about any substantive content risk. Lane 1B was right about the file's execution-discipline sophistication but that sophistication is applied to document-management, not to any specific product risk. Authoring sustainability is *not* owned in the long-arc canonization PLAN. The outcome-C interpretation that was "maybe it lives in the distributed methodology" fails for this specific file.

The investigation's shape shifted twice. I came in expecting to answer "is it in the canon or not" as a binary. I ended up finding that the canon *contains the vocabulary* in multiple places but *uses it as M2 framing, not M1 risk framing*, and that the risk lives most concretely in the research-layer PITFALLS.md Pitfall 14 — which the canon cites as motivation for *other* pitfalls but not for this one. The honest shape of the finding is not about presence/absence but about **framing mismatch** between canon and predecessor.

---

## Re-Verification Ledger (Chain Integrity)

Each row re-verifies a Wave 1 claim or an orchestrator task-spec claim that this lane relies on. Format: claim → what I did → what I found → whether the prior reading still holds.

### REV-1 — Lane 1A's framework-invisibility finding: "the canon does not own the authoring-sustainability risk anywhere"

**What Lane 1A said** (`wave-1-lane-1a-canon-integrity.md:412-418`, repeated at `:315, :382`): *"The canon does not own the authoring-sustainability risk anywhere, despite the predecessor audit ranking it #1 in both passes."*

**What I did.** Ran `Grep` with term set `authoring|author\b|corpus|sustain|content operations|content scaling|content ops|workload|burn|pack production|round production|authoring workload|author burnout|content authoring|painful|critical mass` (case-insensitive) against `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`.

**What I found.**
- `PROJECT.md:25`: *"curated content corpus"* (M1 requirement; assumes authoring viability)
- `PROJECT.md:92`: *"curated starter packs and enough calibration signal to improve the corpus"* (M1, Phase 6)
- `PROJECT.md:98`: *"the same substrate can support... more sustainable content operations"* (M2 goal)
- `PROJECT.md:104-106`: M2 deliverables include *"authoring and preview tooling that make content production sustainable"* and *"richer content operations, pack sharing, and calibration insight"*
- `PROJECT.md:125`: *"content scaling"* named as a seam to preserve in M1 work
- `PROJECT.md:167`: *"content authoring workload"* as the consequence framing of the Critical open question about first-class answer surfaces
- `LONG-ARC.md:37`: *"content operations that can survive wrapper changes"* (substrate doctrine)
- `LONG-ARC.md:52`: *"content operations maturity"* (M2)
- `ROADMAP.md:155`: Phase 6 goal mentions *"improve the corpus"*
- `REQUIREMENTS.md:71`: v1 header `### Content Operations And Calibration` (OPS-01/02/03: coverage class, session telemetry, testability)
- `REQUIREMENTS.md:104`: v2 header `### Content Operations` (OPS-V2-01/02/03: preview, ergonomic editor, pack sharing)
- `REQUIREMENTS.md:115`: v2 header `### Content Scaling` (CONTENT-01/02: tagged round pools, calibration data)

**Does Lane 1A's reading still hold?** Partially. Lane 1A's exact claim — *"The canon does not address this risk anywhere"* (`wave-1-lane-1a-canon-integrity.md:315`) — is factually too strong. The canon *contains* vocabulary (corpus, sustainable content operations, content scaling, content authoring workload) that touches the risk area. Lane 1A's narrower search (`"authoring sustainability," "author workload," "corpus critical mass," "authoring pain"` — `wave-1-lane-1a-canon-integrity.md:382`) did not catch these phrases because none of them match verbatim.

But Lane 1A's *substantive* claim is still basically correct: **the canon does not frame authoring sustainability as an M1 load-bearing risk**. The adjacent vocabulary in the canon is uniformly framed as (a) M2 goals, (b) M2 deliverables, (c) M1 seam-preservation, or (d) a consequence-framing embedded in the Open Questions table — **not** as a top-level risk with mitigation criteria. The predecessor's Lane 4 had the risk framed as effort-risk with a 15-20 minute-per-round operationalization and a 5-round-audit trigger; none of that operationalization is anywhere in the canon.

**Re-verification verdict:** Lane 1A's claim softens from *"not addressed anywhere"* to *"addressed distributedly via M2 vocabulary and Q-consequence framing, but not owned as an M1 risk with operational criteria."* The latter is a more defensible claim and happens to be the claim this lane's investigation actually supports.

**Consequence for this lane's outcome classification.** The softer claim does not collapse the three-outcome space; it reshapes it. Outcome A ("canon is wrong to not own this") still holds if the M1 risk framing is the right one; the canon's M2 framing is then a category error. Outcome B ("canon is right to defer") holds if the M2 framing is correct; the predecessor's M1 ranking is then the category error. Outcome C ("already owned in a form Wave 1 missed") holds in a *partial and weaker* form — the canon does own the vocabulary, but not as a risk, so it is partially owned.

### REV-2 — Lane 1B's claim: "the long-arc canonization PLAN contains execution discipline substantively stronger than anything in the vision-alignment PLAN, and may own the risk"

**What Lane 1B said** (`wave-1-lane-1b-methodological-inheritance.md:289`): *"`.planning/deliberations/2026-04-11-long-arc-canonization/PLAN.md` (892 lines). This file contains methodological discipline that is substantively stronger than anything in f1-modeling's vision-alignment PLAN..."*. The orchestrator's task spec (`wave-2-lane-b2-opus-authoring-sustainability-task-spec.md:100`) extends this: *"If authoring sustainability is owned anywhere in prix-guesser, the long-arc-canonization PLAN is the most likely place outside the canon."*

**What I did.** Read the first 250 lines of `.planning/deliberations/2026-04-11-long-arc-canonization/PLAN.md` to verify its character. Ran `wc -l` to verify line count: **892 lines confirmed**. Ran `Grep` for `authoring|author\b|content workload|corpus|content operations|content scaling|pack production|round production|sustainability|sustain|burn|workload` (case-insensitive) against the full file.

**What I found.**
- **Line count verified**: exactly 892 lines.
- **Execution discipline verified**: lines 98-146 do contain the execution primitives Lane 1B named — allowed write set, forbidden write set, non-discretion rules, bounded decision windows with priority orders, stop conditions. This is substantive discipline.
- **Authoring-sustainability content: ZERO MATCHES.** Not a single mention of `authoring`, `author`, `content workload`, `corpus`, `content operations`, `content scaling`, `pack production`, `round production`, `sustainability`, `sustain`, `burn`, or `workload` in the entire 892-line file.

**Does Lane 1B's reading still hold?** Lane 1B's structural claim about the file's discipline is correct. But the orchestrator's *extension* of that claim — "if authoring sustainability is owned anywhere outside canon, it's most likely here" — is **disconfirmed by direct read**. The file is about the meta-work of canonizing LONG-ARC.md into the canon. Its execution discipline is document-management discipline, not product-risk discipline. The file does not own any substantive product risk, including authoring sustainability. The risk of the outcome-C interpretation ("the distributed methodology owns the risk") living in this file specifically is ruled out.

**Consequence.** The orchestrator's hypothesis that Lane 1B's framework-invisibility finding points to an outcome-C reading of the authoring-sustainability question is **weakened** by direct check. The distributed methodology is distributed — but not in a way that owns this specific risk in this specific file. This does not rule out outcome C entirely (the risk might still be owned via PITFALLS.md + the citation mechanism, or via some other file I did not check), but it removes the strongest single candidate location.

### REV-3 — Lane 1C's Finding 1: "F1's own trademark guidelines actively legitimize the 'private-only' framing"

**What Lane 1C said** (`wave-1-lane-1c-external-gap-research.md:234-246`): Cited https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt with quoted passages: *"Limited use of our Other Intellectual Property Rights for educational purposes may be acceptable where the use is justified, limited, and non-commercial. However, please note, this does not include public postings..."* and *"Motorsport simulators... should not make any use of the FORMULA 1 Rights without an express written license."*

**What I did.** I have no web access. I read Lane 1C's quotations as they appear in the lane output. I cannot re-verify the URL.

**Relied-on reading.** I am trusting Lane 1C's quotation in good faith as required by chain integrity under file-read-only constraints. This is an **explicitly unverified predecessor claim**. Lane B4 (Sonnet gsdr-auditor) is running in parallel on citation-checking the canon against this exact claim; B4's output at Wave 3 synthesis is the right place to cross-check. For this lane's purposes, I note: **if the Lane 1C quotation is accurate**, then the private-only framing is legally load-bearing, which means the authoring-sustainability failure mode is "the single private owner burns out" rather than "the content ecosystem fails to scale." **If the quotation is inaccurate**, my reframing in LQ-B2.4 softens. I note the dependency explicitly.

### REV-4 — Lane 1C's Finding 3: "all existing F1 fan games are single-player daily-puzzles; zero are private-room multiplayer party games"

**What Lane 1C said** (`wave-1-lane-1c-external-gap-research.md:192-196, 303-307`): Named Formudle, Stewardle, F1DLE, emcrald/F1-Driver-Wordle, SmCTwelve/f1-bot, andrerfcsantos/f1-discord-bot, CorrosiveKid/fantasy-f1-discord-bot. Found zero F1 private-room multiplayer party games.

**What I did.** Checked that Lane 1C named specific instances with distinguishing detail (puzzle types, game shape, URLs) rather than making an ungrounded absence claim. Lane 1C did name specifics — Formudle is described as daily F1 games, F1DLE is described as "Driver Puzzle, Circuit Challenge, Car Recognition, Track Puzzle, Season Standings" with *"no visible unofficial disclaimer on the landing page"* — and Lane 1C explicitly marked the absence-of-private-room-multiplayer as a search result, not an assertion. I cannot re-verify the specific games without web access.

**Relied-on reading.** Trusting Lane 1C in good faith, with a note that the claim is verifiable-in-principle by someone with web access. Lane 1C's framing that the adoption challenge "is shape education rather than distribution" (task spec reference; Lane 1C's own phrasing at `wave-1-lane-1c-external-gap-research.md:307`) is a reframing I engage with in LQ-B2.4.

### REV-5 — The 2026-04-08 predecessor audit's "#1 risk" ranking

**What the predecessor said.** `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md:186`: *"1. **Content authoring is too painful** → corpus never reaches critical mass (both ranked this #1)"*. Also `SYNTHESIS.md:144`: *"Content authoring pain is the #1 fun risk — if authoring is too expensive, the corpus never reaches critical mass"*.

**What I did.** Read the primary lane (`lane-4-multi-milestone-vision.md`) that produced the ranking, not just the synthesis. Searched for the ranking mechanism.

**What I found.**
- Lane 4 frames the risk as **"Risk A: Content Authoring Is Too Painful (Effort Risk)"** at line 191, using alphabetical labels (A through G implied, though I didn't enumerate all of them) — **not** a scored prioritization.
- Lane 4's operationalization: *"If creating one round takes more than 15-20 minutes of focused work, the content corpus will never reach critical mass"* (`lane-4-multi-milestone-vision.md:194`) — a concrete testable threshold.
- Lane 4's mitigation: *"After the first 5 rounds are authored, do a time audit. If a round takes more than 30 minutes, prioritize authoring tooling over additional game features"* (`lane-4-multi-milestone-vision.md:200`) — a concrete process with a specific trigger.
- Lane 4 MR-3 at line 264: *"Track authoring time per round and set a pain threshold"* — a named mitigation requirement.
- The "ranked #1" claim at `SYNTHESIS.md:186` appears to be a synthesis-level *interpretation* of the fact that both passes named this as a biggest-risk concern, **not** a primary-source ranking mechanism. I do not have access to the GPT-5.4 lane-4 output (`gpt-5.4-parallel/lane-4-multi-milestone-vision.md` exists in the directory per my earlier file listing) — I would need to read it to verify whether GPT also placed it first. I did not read that file because the file is outside my task spec's read list and because my Lane 1A re-verification load is already heavy. This is an acknowledged gap.

**Does the predecessor reading hold?** The substance holds — authoring sustainability is a real risk flagged by both passes with specific operationalization. The specific framing "ranked #1" is softer than Wave 1 treated it because (a) Lane 4 used alphabetical labels, not rank, and (b) I haven't confirmed the GPT pass's treatment. But the Opus Lane 4 treatment is substantive enough that even with the softening, the risk is meaningfully flagged.

**The more load-bearing finding about the predecessor**: Lane 4 gave the risk a **concrete operational criterion** (15-20 min per round target, 5-round audit, 30-min threshold). **None of that operational criterion is in the current canon.** Even if the canon cannot "own" a hobby-time risk in the same way it owns a product requirement, it could own the *measurement discipline* — a line like "track authoring time per round for the first 5 rounds" is exactly the kind of concrete thing a canon can state. The canon's silence on this specific concrete mitigation is a concrete gap regardless of which outcome (A/B/C) is correct.

### REV-6 — The orchestrator's task-spec claim about Lane 1B catching "2 of 8 factual errors" in the Wave 1 pre-list

**What the task spec said** (`wave-2-lane-b2-opus-authoring-sustainability-task-spec.md:108`): *"Lane 1B caught 2 of 8 factual errors in this orchestrator's Wave 1 pre-listing... That's a 25% error rate in my pre-listing."*

**What I did.** Read Lane 1B's primary finding on this at `wave-1-lane-1b-methodological-inheritance.md:110-123`.

**What I found.** Lane 1B's comparison table at lines 111-121 enumerates 9 drop-claims from the orchestrator (not 8): trajectory analysis, precedent analysis, calibrated confidence markers, Path of Inquiry, Dependencies and Relations, hypothesis testing, reframing permission, gray-area handling worked examples, and the 16-section framing. Lane 1B marked 2 as factually wrong (Path of Inquiry, Dependencies and Relations). So the orchestrator's self-description of "2 of 8" may itself be slightly off — I count "2 of 9". This is minor (it may depend on whether the 16-section framing counts as a drop-claim or a framing-claim), but it is a finding consistent with the orchestrator's own acknowledgment that the pre-list is error-prone.

**Consequence for this lane.** The orchestrator's own self-described error rate in pre-listings makes me especially cautious about inheriting this task spec's framing without checking. Concretely: the task spec's framing that the three-outcome space is cleanly A / B / C is itself a framing that may be wrong. I engage with that in LQ-B2.5-6 by surfacing a reframing as a fourth outcome.

---

## LQ-B2.1 Verdict — Does The Canon Own Authoring Sustainability Anywhere?

**Direct verdict: the canon owns the *vocabulary* of authoring sustainability in multiple places but does not own the *risk posture* in any place.**

Evidence the vocabulary is present:
- `PROJECT.md:98` names "sustainable content operations" as an M2 goal
- `PROJECT.md:105` names "authoring and preview tooling that make content production sustainable" as an M2 deliverable
- `PROJECT.md:125` names "content scaling" as a seam to preserve in M1
- `PROJECT.md:167` names "content authoring workload" as the consequence of an M1 Critical open question
- `LONG-ARC.md:52` names "content operations maturity" as part of the M2 theme
- `REQUIREMENTS.md:104` has a v2 section `### Content Operations` with OPS-V2-01/02/03
- `REQUIREMENTS.md:115` has a v2 section `### Content Scaling` with CONTENT-01/02

Evidence the risk posture is absent:
- No file I searched frames authoring sustainability as an M1 load-bearing risk
- No file names an M1 measurement or threshold (contrast with the predecessor's 15-20-min-per-round criterion)
- `REQUIREMENTS.md` cites `PITFALLS.md#Pitfall 6, 8, 9` as motivation but does not cite `Pitfall 14` despite that pitfall being directly about the risk
- The v2 `### Content Operations` and `### Content Scaling` section items (OPS-V2-01, OPS-V2-02, OPS-V2-03, CONTENT-01, CONTENT-02) carry **no `Motivation` citations at all** — unlike v1 items which uniformly cite `research:` sources. These are uncited floating assumptions, and uncited assumptions-about-M2 cannot be doing the work of an M1 risk claim.
- The Open Questions table at `PROJECT.md:163-171` does not include an entry for "will authoring remain sustainable enough to reach critical mass" or similar
- The Key Decisions table at `PROJECT.md:151-159` does not include a decision about how authoring workload is managed

**The answer to the literal question "does the canon own authoring sustainability anywhere?" is: partially, in M2-framed form, not in M1-framed form.** Under the M2 framing, the canon owns the concept. Under the M1 framing the predecessor used, the canon is silent.

**Interpretations competing:**

- *Interpretation 1 (the canon is wrong): the risk is genuinely M1-shaped (authoring needs to reach critical mass for M1 to succeed, since M1 is "Game Night Works" and game night requires enough packs), and the canon's scoping it to M2 is a category error.*
- *Interpretation 2 (the canon is right): the risk is genuinely M2-shaped (the first 10-20 rounds can be authored by a single motivated owner before the risk materializes; the risk materializes only when the corpus needs to scale, which is an M2 concern), and the predecessor audit was projecting M2 concerns onto M1.*
- *Interpretation 3 (neither frame fits): the risk is a hobby-commitment question that no canon-style document can own, regardless of milestone — it is managed by the owner's time and interest, not by any requirement.*

I cannot rule out any of the three from canon-reads alone. What I can say: **Interpretation 2 is partially supported** by the specific shape of Milestone 1 ("Game Night Works" — one pack to prove the loop, not many), and by `PROJECT.md:145`: *"Authored content quality matters more than scale at initialization."* That quote is a canon-level framing that scale is deferred beyond M1. If "scale is deferred" is correct, then "authoring sustainability at scale" is legitimately an M2 concern. **But** "authoring sustainability" and "authoring scale" are not the same concern: an M1 that requires 10-20 high-quality rounds still needs the author to sustain authoring through 10-20 rounds, and that is where Lane 4 Risk A's 15-20-min-per-round threshold applies.

**The verdict at LQ-B2.1**: The canon partially owns the vocabulary; does not own the risk as an M1 concern with operational criteria. Outcome-C is *partially live*, outcome-A is *partially live*, and the weight between them depends on whether M1 needs 10-20 rounds (Lane 4's concern) or M1 can survive with fewer rounds (which the canon treats as true — `PROJECT.md:145`). **That is itself a canon ambiguity the canon has not closed.**

---

## LQ-B2.2 Verdict — Is It Owned In The Distributed Methodology?

**Direct verdict: No, not in the file Lane 1B pointed to. Partially yes, in the research layer via PITFALLS.md Pitfall 14, but the canon's citation mechanism has not pulled Pitfall 14 into the canon.**

The long-arc-canonization PLAN — the strongest candidate for outcome-C from Lane 1B's framework-invisibility finding — contains zero mentions of any authoring-sustainability vocabulary (verified by grep). The file is about the meta-work of canonizing LONG-ARC.md. Its execution discipline is document-management discipline, not product-risk discipline.

The research layer, however, does own the concern:
- `PITFALLS.md:253-267`: Pitfall 14 "Delaying content validation and authoring support until the corpus is already painful", rated Severity: High, with concrete warning signs ("Engineers are hand-editing runtime code to add or fix rounds", "One bad source URL or bad pano breaks a pack late in QA") and prevention strategy ("Start with files or spreadsheets, but put a validator/import step in front of the app")
- `PITFALLS.md:305`: Phase-Specific Warning: *"Authoring Tools + Expansion | Tooling arrives only after content velocity collapses | Build validation/import first, UI tooling second"*
- `PITFALLS.md:290`: *"Spreadsheet-driven authoring vs internal tooling is not itself the pitfall. The pitfall is having no validation/import discipline while waiting for a future tool."*

**The research layer owns the risk better than the canon does.** But the research layer is not canon in the same way PROJECT.md/LONG-ARC.md/ROADMAP.md/REQUIREMENTS.md are — it's an input to the canon, not a durable product claim. The relevant question is whether PITFALLS.md#14 is *cited* as motivation for any canon requirement. I verified by grep: **it is not cited.** The canon cites `PITFALLS.md#Pitfall 6, 8, 9` only. The research-to-canon intake mechanism exists and has been used selectively; Pitfall 14 was not selected.

**This is the sharpest finding in the lane.** The canon has an existing citation-based mechanism for pulling risks from research into requirements. That mechanism was used for three of the pitfalls in PITFALLS.md and not used for Pitfall 14 specifically, despite Pitfall 14 being the pitfall that corresponds most directly to the predecessor audit's top convergent risk. Whether the non-selection was deliberate (scope judgment) or accidental (omission), the effect is the same: the risk is named in research, the canon has a way to own it, and the canon chose not to.

**Interpretations competing:**

- *Interpretation 1 (deliberate non-citation): the canon author judged that Pitfall 14 did not need a v1 requirement because its mitigation is "start with files or spreadsheets, put a validator in front of the app" — which is exactly what `REQUIREMENTS.md#PACK-04` (pack validation) and `REQUIREMENTS.md#OPS-01` (content workflow) already do in v1. Under this interpretation, Pitfall 14's prevention strategy is already canonized, just not under the Pitfall-14 label. The non-citation is a harmless labeling difference.*
- *Interpretation 2 (accidental omission): the author selected the pitfalls to cite based on what maps to concrete schema work (fallback strategy, ambiguous prompts, calibration) and passed over the meta-pitfall about authoring velocity because it does not map to a single schema decision. Under this interpretation, the canon's citation mechanism is structurally biased against meta-risks that do not have a single-requirement landing place.*
- *Interpretation 3 (the concern is already covered by the OPS-* section header organization): the existence of v1 `### Content Operations And Calibration` section, v2 `### Content Operations` section, and v2 `### Content Scaling` section means the canon has organized its vocabulary around the concern even without citing Pitfall 14 directly. Under this interpretation, the section-header-level organization is the canon's answer to the concern.*

I find Interpretation 1 partially correct: PACK-04 and OPS-01 do in fact implement part of Pitfall 14's prevention strategy (validation/import before the app). But Interpretation 1 is also incomplete: Pitfall 14's warning signs include "engineers are hand-editing runtime code to add or fix rounds" and "one bad source URL or bad pano breaks a pack late in QA" — these are about author-time diagnostics, not about schema validation. None of v1's OPS-* or PACK-* requirements directly address author-time diagnostics or author-time time-per-round measurement.

**Verdict on LQ-B2.2**: The risk is owned in the research layer (PITFALLS.md#14) at a level of rigor that matches or exceeds the canon's treatment of other risks, but the canon has not pulled it through its citation mechanism. The risk is *not* owned in the long-arc canonization PLAN or any other distributed-methodology file I checked. So the outcome-C interpretation of the risk being "already owned in a form Wave 1 missed" is partially true (PITFALLS.md owns it) but the Wave 1 framing was oriented at the wrong layer — the distribution is at the research layer, not at a deliberation or initiative layer.

---

## LQ-B2.3 Verdict — Is The Predecessor's "#1 Ranking" Itself Warranted?

**Direct verdict: The substance of the risk is warranted; the specific "#1" framing is softer than Wave 1 treated it.**

The substance, re-verified from Lane 4 directly (`lane-4-multi-milestone-vision.md:191-200`): the risk has a named effort-cost operationalization (15-20 min per round), a specific failure mechanism (corpus never reaches critical mass → core loop never gets enough content to feel fun), and a concrete mitigation (5-round time audit, 30-min threshold). This is substantive risk analysis, not a hand-wave.

The "#1" framing, re-verified from the same file: Lane 4 used **alphabetical labels** (Risk A, Risk B, ...), not a numerical rank. `SYNTHESIS.md:186`'s *"both ranked this #1"* is a synthesis-level interpretation that imposes a ranking order on both passes' risk sections. The claim that *both* passes ranked it #1 requires verifying the GPT-5.4 pass's lane-4 output — which I have not read directly, but which the task spec did not explicitly require me to read.

**The weaker claim that still holds**: both passes named the authoring-effort risk among their biggest risks, with convergent operationalization (both framed it as effort-cost, both had concrete mitigation). Cross-model convergence of this shape is meaningful evidence. It is **not** evidence of a methodologically scored prioritization.

**Interpretations competing:**

- *Interpretation 1 (the "#1" framing was convergence-as-ranking): two independent passes with different models independently arrived at "authoring effort is among the biggest risks" — that is exactly what cross-model validation is for, and treating it as a soft #1 is legitimate synthesis.*
- *Interpretation 2 (the "#1" framing was rhetorical amplification): the synthesizer imposed a ranking that the primary lanes did not produce, in order to make the finding more load-bearing in the synthesis. Under this interpretation, the risk is real but the "#1" is softer.*
- *Interpretation 3 (the ranking is warranted for M1 but miscalibrated): the predecessor audit was treating the project as if it were approaching M1 production with a long-tail corpus expectation. The actual M1 — "Game Night Works" with one pack of high-recognition circuits per `ROADMAP.md:159` — may only need 10-20 rounds, which is within single-owner reach for a motivated F1 fan. The risk calibration is right for the larger corpus the project will eventually need; it is miscalibrated for the specific M1 milestone.*

I find Interpretation 3 the most load-bearing. The predecessor's mitigation ("After the first 5 rounds are authored, do a time audit") is actually consistent with Interpretation 3 — it names the first 5 rounds as the operational check, which suggests the predecessor knew the measurement applies at a small-n scale. The canon's silence on the 5-round check is the actual gap — not the absence of the risk per se, but the absence of the operational criterion.

**Verdict on LQ-B2.3**: The predecessor's risk is substantively warranted. The "#1" label is softer than Wave 1 treated it but the substance survives the softening. **What the canon is most conspicuously missing is the operational criterion (a 5-round audit with a 30-minute threshold) rather than the risk framing itself.** If I had to recommend a minimum-viable canon addition, it would be the operational criterion, not a risk label. See LQ-B2.5.

---

## LQ-B2.4 Verdict — Is "Authoring Sustainability" Even The Right Frame?

**Direct verdict: "Authoring sustainability" is the closest available frame but is an imported public-product vocabulary applied to a private-only fan project. A reframe that composes three sub-concerns is more accurate than any single frame.**

I tested the three alternative frames named in the task spec against the canon evidence.

### Alternative 1: Playing-friend vs authoring-friend gap

The test: is the real concern that the friends who enjoy playing won't or can't author content?

Evidence in favor:
- `PROJECT.md:7`: *"The initial audience is knowledgeable long-time F1 fans"* — establishes the playing audience as F1-expert plural.
- `PROJECT.md:3-8` does not name anyone as the authoring audience; by inference and by Lane 4's framing, it is the project owner (Logan).
- `lane-4-multi-milestone-vision.md:226`: *"authors (which is just Logan and maybe one friend) will burn out"* — the predecessor explicitly named the one-or-two-author bottleneck.

Evidence against:
- The gap is structurally real but it is a *design choice*, not a risk to be mitigated. A private game where 1-2 people author content for 5-10 friends to play is not "the gap" — it is the configuration.
- The canon owns the configuration implicitly via the private-only framing. The gap is the M2-to-M3 transition concern (community authoring) not an M1 concern.

**Reading**: This alternative framing is partially accurate but it is really an M2 concern under a different name. For M1 it is a trivially true observation (one author, many players), not a risk.

### Alternative 2: Owner commitment

The test: is the real concern a personal question about whether the project owner can sustain authoring over time, i.e. a hobby-sustainability question?

Evidence in favor:
- A private-only fan project has hobby-sustainability as its native failure mode. No product failure mode applies because there is no product.
- `PROJECT.md:130`: *"current trust and service assumptions remain modest: private use, low moderation burden, no strong public uptime promise"* — the canon explicitly deflates product-style commitments. In a context of deflated product commitments, hobby-sustainability is structurally the load-bearing commitment instead.
- `LONG-ARC.md:146-153` names "What Changes Would Reopen This Doctrine" — conditions under which the long-arc doctrine should be revisited. The list includes *"real playtesting shows the private watchable ritual is not the strongest center after all"* (l.148) but **does not name** *"the owner loses interest in authoring"* as a reopen condition. A doctrine that names several reopen conditions but silently omits the hobby-sustainability one is either (a) treating hobby-sustainability as obvious enough to not need naming, or (b) missing the most structurally important reopen condition.

Evidence against:
- "Owner commitment" as a frame is not something a canon can own in the same way it owns a product claim. The canon cannot state "the owner will stay committed" as a requirement — it can only state working assumptions.
- The frame implies a lever (owner's personal decision) that is outside the requirements vocabulary. Requirements-review as a subject cannot generate requirements about a single person's future hobby interest.

**Reading**: This alternative framing is the most *descriptively accurate* of the three for a private-only project, but it is also the least *addressable* through the canon's vocabulary. The honest statement is that the canon's deepest load-bearing assumption is one the canon cannot write down as a requirement — and this is not a failure of the canon, it is a reality of private-only hobby projects.

### Alternative 3: Shape education burden (Lane 1C's reframe)

The test: if F1 fan games are all single-player daily-puzzles and prix-guesser occupies an unoccupied party-game slot, is teaching friends the new shape itself a form of authoring work?

Evidence in favor (trusted from Lane 1C, unverified by me):
- Lane 1C's claim that F1 fan games are all daily-puzzle-shaped (`wave-1-lane-1c-external-gap-research.md:194-196`, `:303-307`) means prix-guesser's target audience has been trained by existing ecosystem to expect solo daily puzzles, not party-game evenings.
- The authoring work then is not just writing rounds; it is running the first game nights where the shape is introduced and validated by play.
- Lane 1C's framework-invisibility finding (`wave-1-lane-1c-external-gap-research.md:422-430`): *"the alternative to freezing the authored content contract in Phase 01 is to freeze the authored content contract in Phase 02 and run three manual game-night sessions with paper clue ladders and a whiteboard reveal in Phase 01 first, to discover what the contract actually needs to encode before committing to a shape."*

Evidence against:
- Shape education is a real concern but it is adoption-shaped, not authoring-shaped. Calling it "authoring" conflates two distinct practices.
- The canon's `PROJECT.md:141-148` "Constraints" section names several concrete constraints but does not name shape-education or first-playtest-validation as a constraint. The gap is real.

**Reading**: This alternative framing identifies a real gap — pre-build playtesting as a practice — but the gap is closer to *process* than to *requirements*. It should be a discuss-phase or phase-planning concern, not a canon requirement.

### Composing the three

Each of the three alternative frames captures a genuine but partial piece. The M1-specific concern is best described as:

> **"The first 10-20 rounds are a single-person time commitment by the owner, who is also the one most motivated to do it; the project's M1 success depends on that commitment staying within the owner's sustainable hobby time budget, AND on the first game-night sessions validating that the party-game shape actually works for friends trained by daily-puzzle F1 games, AND on the schema not making authoring materially heavier than it needs to be."**

That is three linked concerns, not one. It is not the predecessor's *"authoring is too painful → corpus never reaches critical mass"* — which is a public-product risk framing — but it is also not cleanly "hobby-sustainability" or "shape-education" alone.

**The reframe I would propose**: the canon does not need an "authoring sustainability" requirement. It needs a **first-five-rounds reality-check** — a canon-level claim that says "we will author 5 rounds and run one game night before treating the schema as settled; if the 5 rounds cost more than X minutes each, or if the game night does not validate the shape, we will pause Phase 2 and revisit." That is the predecessor's Lane 4 MR-3 adapted for M1-reality and adapted for the hobby-project context.

**Verdict on LQ-B2.4**: "Authoring sustainability" is not the right frame. The right frame is closer to **first-five-rounds reality-check + owner-hobby-budget working-assumption + shape-validation pre-build checkpoint**. These are the three things the canon could meaningfully own that would replace the predecessor's public-product risk framing with a private-only-project-appropriate shape.

---

## LQ-B2.5 — If Outcome A Holds: What Should The Canon Claim Look Like?

The claim I would propose if outcome A holds — and I would propose a *version* of it regardless of which outcome ultimately holds, because the first-five-rounds reality-check is useful under A, B, *and* C:

**Draft requirement (where):** `.planning/REQUIREMENTS.md`, new subsection under existing `### Content Operations And Calibration` (v1), probably as OPS-04 to preserve the PACK-*/OPS-* section structure.

**Draft requirement (form):** A testable v1 requirement with `research:` citation to `PITFALLS.md#Pitfall 14` (which the existing citation mechanism supports).

**Draft requirement (text):**

> **OPS-04**: After the first 5 authored rounds exist, the authoring workflow is measured against a time-per-round pain threshold (target: ≤ 20 minutes per round; threshold: ≤ 30 minutes per round). If the threshold is exceeded, Phase 6 authoring-tool work takes priority over further Phase 2/3/4/5 feature work until the threshold is met.
>
>   - *Motivation:* `research: .planning/research/PITFALLS.md#Pitfall 14: Delaying content validation and authoring support until the corpus is already painful` and `audit: .planning/audits/2026-04-08-pre-execution-review/lane-4-multi-milestone-vision.md` (Risk A and MR-3).

**Why this form specifically**:

1. **It is measurable.** Unlike "authoring sustainability" as a vague claim, a time-per-round measurement is something the project owner can actually run against the first 5 rounds with a timer.
2. **It is importable.** The citation mechanism already exists in REQUIREMENTS.md (three v1 requirements cite PITFALLS.md); this just uses the same mechanism for the risk currently missing a citation.
3. **It does not commit the project to Phase 6 scope creep.** It names a threshold *below which* Phase 6 work jumps priority; above the threshold, the current phase-ordering stands.
4. **It is scope-appropriate for private-only.** It does not require building an authoring tool, adding a preview UI, or formalizing anything. It requires running a timer and making a decision.
5. **It survives the reframe.** Whether the "authoring sustainability" concern is really an owner-hobby-budget concern, a playing-authoring-friend gap concern, or a shape-education concern, the first-5-rounds time check still produces information relevant to all three.

**What this draft deliberately does NOT do**:

- It does not add a "risk register" to the canon. The canon's current vocabulary (Key Decisions, Open Questions, Requirements, Constraints) does not have a risk-register section, and adding one for a single concern is premature.
- It does not elevate the concern to a top-level Constraint or Key Decision. A measurement requirement is more actionable than an aspirational constraint.
- It does not commit the project to specific tooling. The threshold triggers a priority decision; what tool to build is left to the phase where the decision triggers.

**If outcome B or C holds instead, this draft is still useful** because the measurement is cheap, the insight is concrete, and no harm is done by measuring something the canon's existing framing already assumes is okay. OPS-04 would function as a validation check for the canon's M2-scoping assumption.

---

## LQ-B2.6 — If Outcome B Or C Holds: Where Is The Deferral / Ownership?

### If Outcome B (canon is right to defer)

The deferral would live across:
- `PROJECT.md:98, 104-106`: Milestone 2 goal and deliverables about sustainable content operations
- `LONG-ARC.md:52`: "content operations maturity" as M2 theme
- `REQUIREMENTS.md:104-108`: v2 `### Content Operations` section with OPS-V2-01/02/03
- `REQUIREMENTS.md:115-118`: v2 `### Content Scaling` section with CONTENT-01/02
- `ROADMAP.md:154-169`: Phase 6 "Starter Packs And Calibration" (closest M1 touchpoint)

**Is the deferral explicit?** Partially. The canon *says* the deferral exists via the M2 vocabulary, but it does not say "we are deferring this risk to M2 *because*..." with closure criteria. A principled deferral under investigatory doctrine would need:
  - named criterion for when the deferral reopens (e.g., "if M1's first 5 rounds exceed X time per round, reopen")
  - named risk-holder (who tracks this between M1 and M2?)
  - named trigger event (what event reopens the deferral?)

None of those are in the canon. The deferral is *implicit*: the M2 vocabulary exists, but there is no explicit bridge from "this is a concern" to "we are deferring it to M2 because of X, and will reopen if Y."

**Is the implicit deferral adequate?** For a private-only fan project managed by one person, arguably yes — the owner knows their own risk profile and doesn't need to write it down. For a canon that is supposed to be durable and survive the owner's forgetting, arguably no — the risk could be invisibly dropped at any phase transition.

**If outcome B is correct, the canon should add one line to `PROJECT.md` or `LONG-ARC.md` making the deferral explicit.** Something like: *"Authoring sustainability beyond the first 5-10 rounds is deferred to M2; M1 succeeds as long as the owner can author a starter pack within their hobby time budget without burning out on the first 5 rounds."* Then the implicit deferral becomes explicit and can be tested for principled-ness.

### If Outcome C (already owned in a form Wave 1 missed)

The ownership lives in:
- `PITFALLS.md:253-267` (Pitfall 14, Severity: High) — the risk is owned at the research layer with concrete warning signs and prevention strategy
- `PITFALLS.md:305` (Phase-Specific Warnings) — "Tooling arrives only after content velocity collapses"
- `PROJECT.md:167` (Open Questions table) — "content authoring workload" as Q-consequence
- `PROJECT.md:98, 104-106` and `REQUIREMENTS.md` v2 sections — M2 vocabulary

**Why Lane 1A's framework did not see it as "owning" the risk**: Lane 1A was searching the canon for "authoring sustainability"-shaped language. The canon uses "content operations", "content scaling", "sustainable content operations" — adjacent vocabulary that Lane 1A's term list did not catch — and treats these as M2 concerns. Lane 1A also did not read PITFALLS.md directly (PITFALLS.md is research, not canon, and Lane 1A's scope was canon re-verification). The ownership is distributed across (research layer: PITFALLS.md#14 | canon layer: M2 vocabulary | intake mechanism: REQUIREMENTS.md citation system used selectively) and no single file owns it as a named M1 risk. Lane 1A's framework saw "nothing at the canon level" — which is true for the specific search Lane 1A ran — and missed that the canon layer does contain the vocabulary but uses it differently than the predecessor.

**Why outcome C is partial rather than full**: the research-layer ownership exists and is substantial, but the canon's citation mechanism did not pull it through for this specific pitfall. That is a gap in the existing ownership mechanism, not a gap in the existence of ownership. An honest outcome-C reading says "the project owns the concern, but owns it in the wrong layer for canon-based planning to see it." Fixing outcome-C is cheaper than fixing outcome-A — one added citation line in REQUIREMENTS.md (linking OPS-V2-02 or a new OPS-04 to PITFALLS.md#14) would make the ownership visible at the canon layer.

---

## LQ-B2.7 / Framework Invisibility

**What this lane's scope makes invisible:**

The lane was framed as a requirements-review question ("should the canon claim authoring sustainability?"). That framing makes invisible a finding that I think is more load-bearing than the framing can see: **whether the canon's citation mechanism from `PITFALLS.md` into `REQUIREMENTS.md` is systematically biased against meta-risks, or whether it just happened to miss this one pitfall.**

The concrete invisibility: my requirements-review frame asks "what should the canon claim?" and treats each potential claim atomistically. It cannot ask "how does the canon form claims, and does that mechanism have a systematic bias?" That is a `process_review` question, not a `requirements_review` question.

Evidence for the suspicion that the bias is systematic, not one-off: the v1 REQUIREMENTS section cites PITFALLS.md for pitfalls that map to a *single-requirement landing place* (Pitfall 6 → OPS-01 via coverage class; Pitfall 8 → UX-03 via answer surface; Pitfall 9 → OPS-02 via session data). Pitfall 14 does not map to a single requirement — it maps to a *measurement practice* (time-per-round with a 5-round audit trigger). The canon's citation mechanism is optimized for one-requirement-per-pitfall mapping and is structurally blind to pitfalls that require operational practices rather than requirement statements. If this is a systematic bias, there are probably other pitfalls with similar shape that I haven't enumerated.

**A concrete finding the requirements-review frame cannot produce**: the canon's form-shape (Key Decisions, Open Questions, Requirements, Constraints, Evolution protocol) is structurally unable to own "do this measurement, and if it fails, change priorities." The closest shape the canon has is a Requirement, which is framed as "the system does X." A measurement-trigger-priority-flip pattern is a *process*, not a system behavior. A canon built to own product requirements cannot own a measurement-triggered process without either distorting the requirement shape (making OPS-04 a requirement that the system measures itself, which it's not, since the system has no author-time telemetry yet) or extending the canon's form vocabulary (adding a "Practices" section, which is a structural canon change).

**This is the framework-invisibility finding the requirements-review frame cannot surface within itself.** The requirements-review frame asks "what should the requirements claim?" when the actual answer may be "nothing, because the concern is not shaped like a requirement — it is shaped like a measurement practice, and the canon does not have a form for practices."

A `process_review × investigatory × self` version of this lane would have asked this question directly. I did not — I engaged with the requirements-review framing as given and noticed the invisibility only in writing this section.

**A second invisibility** (less load-bearing but worth naming): my frame assumes "the canon" is the M1 canon. I inherited PROJECT.md / LONG-ARC.md / ROADMAP.md / REQUIREMENTS.md / STATE.md as the canon files per the task spec's read list. But the Phase 01 `01-CONTEXT.md:69` has an Open Question — *"How much answer-target lineage should be explicit now for later `section`, `corner`, and composite answers **without making v1 authoring materially heavier?**"* — that is awareness of authoring weight as a Phase-01-level concern. That awareness lives outside "the canon" as defined but inside the phase planning surface that will drive M1 work. A frame that treats canon and phase-planning as separable would have placed this finding in the phase-planning layer and declared outcome-C; a frame that treats the canon as the only place risks can be "owned" missed this until now.

---

## Three-Outcome Classification Verdict

The three-outcome framing was "canon wrong to not own (A) / canon right to defer (B) / canon already owns in form Wave 1 missed (C)". My finding does not fit cleanly into any one of these.

**My verdict: the right answer is a composition — 30% A + 30% B + 25% C + 15% reframe (D)**. That is not a hedge; it is what the evidence actually supports. Let me disaggregate.

**~30% outcome A (canon is wrong to not own)**: The canon lacks an operational criterion for an M1 time-per-round check. This gap is real and cheap to fix. If I had to commit to a single line change, I would add `OPS-04` per LQ-B2.5 — the canon would be better with it than without it.

**~30% outcome B (canon is right to defer to M2)**: The canon's M2 vocabulary for "sustainable content operations" is principled for a project whose M1 is "Game Night Works" and whose M1 starter-pack can plausibly be authored by one motivated F1 fan over a few evenings. The predecessor audit's risk framing was projecting a larger-corpus concern onto an M1 that does not require a larger corpus. The canon's deferral is not explicit — there is no line saying "we defer authoring sustainability to M2 because X with trigger Y" — but the implicit deferral is defensible.

**~25% outcome C (canon already owns in a form Wave 1 missed)**: The canon contains the vocabulary (sustainable content operations, content scaling, content authoring workload) and the research layer (PITFALLS.md#14) owns the specific risk with concrete prevention strategy. Lane 1A's framing did not catch it because Lane 1A's search terms were too narrow and because Lane 1A scoped to canon-not-research. The ownership exists but is partial and distributed in a way that is invisible to a canon-only read.

**~15% reframe (outcome D)**: "Authoring sustainability" is an imported public-product frame applied to a private-only fan project where the real concern decomposes into (a) first-5-rounds reality-check, (b) owner-hobby-budget working-assumption, (c) shape-validation pre-build checkpoint. None of the three are what "authoring sustainability" means in a public-product context. The canon's silence on the imported frame is partially principled because the frame is partially wrong for this project.

**How these compose into a Wave 3 synthesis recommendation**: The Wave 3 synthesizer should treat the verdict as "add OPS-04 (outcome A), make the M2 deferral explicit (outcome B), cite PITFALLS.md#14 in REQUIREMENTS.md (outcome C), and note the imported-frame problem in LONG-ARC.md or in the vision-alignment initiative's justification layer (outcome D)" — all four of which are compatible with each other and none of which exceeds a small canon change.

---

## I4 — Position of the Investigation

I am Claude Opus 4.6 running as `gsdr-auditor` subagent via the Claude Code `Task` tool, file-reads only, no web. I was dispatched by a Claude Opus 4.6 orchestrator in a claude-code session. I am one of three Wave 2 lanes; Lane B3 (Opus gsdr-auditor, distributed methodology) and Lane B4 (Sonnet gsdr-auditor, F1 legal carveout citation) are running in parallel. All three Wave 1 lanes were also Opus. That means **Wave 2 has a single cross-class data point** (Lane B4's Sonnet pass on a narrow empirical check) and the rest is Opus-on-Opus convergence which cannot be used as a model-class validation signal.

**What this Opus-on-Opus position is prepared to notice for the authoring-sustainability question:**
- Vocabulary-level reading of the canon and surrounding files (I caught Lane 1A's too-narrow search term set by running a broader grep; my Rule 1 discipline costs me nothing)
- Layered finding shapes — the "risk lives in research-layer not canon-layer" finding is a layering observation that Opus's surface-specific reading is suited to
- Composition across multiple files (I can hold PROJECT.md, REQUIREMENTS.md, PITFALLS.md, and predecessor Lane 4 in working context and compose a claim across them)
- Frame-mismatch findings (I noticed the canon-predecessor framing mismatch between M2-goal and M1-risk because I compared the two directly)

**What this Opus-on-Opus position is NOT prepared to notice:**
- **What an actual content author would notice about whether the risk is real at the small-n scale.** I have never authored an F1 round. I do not know whether 15-20 minutes is a plausible first-pass time. A person who has actually tried to author a round (the project owner) has direct data I do not have. My claim that "a motivated F1 fan can author a starter pack over a few evenings" (in the outcome-B section above) is a hypothesis about human behavior I cannot validate from file-reads.
- **What a product manager who has seen authoring-sustainability failures in practice would notice.** A PM with direct experience of content-ops failures knows the specific ways authoring pipelines actually collapse (cognitive burden of schema completion, media-asset management pain, the "one bad asset breaks the pack" mode the predecessor named). I can recognize these when named but I cannot identify the specific mode that is most likely to hit prix-guesser from a file-read alone.
- **What a Sonnet or GPT run with the same task spec would catch.** Lane 1B explicitly flagged that all-Opus Wave 1 cannot use cross-lane agreement as convergence signal. The same applies to Wave 2 as far as this lane is concerned. Lane B4 is Sonnet but is checking a narrow citation-empirical question, not the risk-framing question I am engaged with. I have no cross-model data point on my specific findings.
- **The hobby-time-budget question at all.** I am a language model. I do not have a time budget, I do not experience fatigue, and I have no idea what "sustainable hobby commitment for a specific F1 fan over M1 timeframe" feels like from the inside. My claim that owner-commitment is the most load-bearing frame for a private-only project is a structural claim, not an empirical one.

**What a differently-situated investigator would do differently:**
- **The project owner, interviewed directly**, would have answers to the time-per-round question I can only hypothesize about. A half-hour conversation — "have you drafted a round yet? how long did it take? which parts were painful?" — would produce more direct evidence for LQ-B2.3 than anything I can read from files.
- **A product manager with content-ops failure experience** would probably reframe my "first-5-rounds reality-check" into something more specific — they would know which sub-tasks in a round-authoring workflow most commonly become the bottleneck (image rescue? schema field completion? answer-alias curation? reveal writing?) and would produce a more targeted measurement than a flat time-per-round threshold.
- **A Codex GPT-5.4 xhigh** reader running the same task spec would probably catch structural-contract gaps in the citation mechanism between PITFALLS.md and REQUIREMENTS.md that I only gestured at (the one-pitfall-per-requirement mapping bias). GPT's structural-reading strength would make that specific finding sharper than mine.
- **An ethnographer who had observed one game night** would have direct data on whether the shape-education concern (Lane 1C's reframe) is load-bearing in practice. I can only note that the concern *exists* on the basis of Lane 1C's external research.

---

## What Remains Unknown

- **Whether the project owner has in fact authored a round yet and how long it took.** This is the single piece of evidence that would most sharpen LQ-B2.3 and LQ-B2.5. It is outside my scope but it is the data point the audit is most starved for.
- **Whether GPT-5.4's 2026-04-08 Lane 4 output converges with Opus-Lane-4 on Risk A specifically, or diverges.** I did not read `gpt-5.4-parallel/lane-4-multi-milestone-vision.md`. The claim that "both ranked this #1" (`SYNTHESIS.md:186`) is therefore unverified at the primary-source level from my side. Lane 1A's REV ledger does not include this file either; this is a gap in the combined Wave 1 + Wave 2 re-verification.
- **Whether the first 10-20 rounds of a starter pack is a realistic M1 target or whether the project needs 50+ rounds to prove the loop.** The canon says "curated starter packs" (`PROJECT.md:25`, `ROADMAP.md:159`) but does not name a round count. If M1 needs 10 rounds, the risk is manageable; if M1 needs 50, the risk is real. This is Phase 6 planning territory, not canon territory, but the canon's silence on the target count is itself a gap.
- **Whether Lane 1C's external research on the F1 fan-game ecosystem shape holds up to an independent check.** I cannot re-verify Lane 1C's URLs. The shape-education reframe depends on Lane 1C's Finding 3 being accurate.
- **Whether Lane B3's distributed methodology work will surface an ownership location I did not find.** I checked the long-arc canonization PLAN and found zero matches. Lane B3's broader survey may find ownership in files I did not check (the initiative's `RESEARCH-PRINCIPLES.md`, Phase 01 `01-VALIDATION.md`, other deliberation files). If Lane B3 finds the risk is owned elsewhere, my outcome weighting shifts toward outcome C.
- **Whether the canon citation mechanism's bias against meta-risks is systematic or one-off.** I named the hypothesis in framework invisibility but did not enumerate other pitfalls to test whether the pattern holds.

---

## How I Navigated Tensions Between Obligations

**Tension 1: Chain integrity's "re-verify predecessor claims independently" vs. the sheer volume of predecessor claims from three Wave 1 lanes plus the 2026-04-08 predecessor plus the orchestrator's task spec.**

If I re-verified every claim at full depth, I would have nothing left for the investigation itself. If I re-verified nothing, the Wave 1 findings would propagate invisibly into Wave 3 synthesis as if they were ground truth. I resolved by re-verifying the specific claims that were *load-bearing for my outcome classification* and explicitly marking the others as "relied on in good faith" or "outside my file-read scope." REV-1 (Lane 1A's framework-invisibility claim) got deep re-verification because the outcome classification depends on whether the canon actually owns the risk. REV-2 (Lane 1B's distributed methodology claim) got deep re-verification because the outcome-C interpretation depends on it. REV-3 and REV-4 (Lane 1C's external claims) got explicit "I cannot verify the URL, trusting the quotation in good faith" markers. REV-5 (the #1 ranking) got partial re-verification (I read the Opus Lane 4 directly but not the GPT Lane 4). The result is a ledger with different depths of rigor for different claims, which is not a clean solution but reflects what the actual evidence permits.

**Tension 2: The requirements_review subject obligation ("assess missing requirements") vs. my growing conviction that the right answer is not a requirement at all.**

The requirements-review obligation pulled me toward drafting a canon claim (LQ-B2.5), and I did draft one (OPS-04). But my investigation was also leading me to the finding that the concern is shaped like a measurement practice, not a requirement — and the canon has no "Practices" section. If I had picked "requirements-review wins", I would have produced OPS-04 as the verdict and not engaged with the frame-shape problem. If I had picked "the real answer is that the canon has a form gap", I would have dropped the OPS-04 draft and argued for a structural canon change. I resolved by doing both: producing OPS-04 as a testable draft (so the requirements-review obligation is engaged with in substance) and separately flagging the form-gap in framework invisibility (so the finding I would have produced under a different subject is still on the record). The tension is not resolved cleanly — a synthesizer reading this output will see the OPS-04 draft *and* the framework-invisibility flag and has to decide whether to propose OPS-04 as-is or treat it as a workaround for a deeper structural issue.

**Tension 3: I2's "let the investigation guide artifact selection" vs. the task spec's instruction to not read the four `01-XX-PLAN.md` files in `.planning/phases/01-authored-round-contract/`.**

I2 permits following the evidence wherever it leads. The task spec explicitly forbade reading the stale Phase 01 plan files. These tensioned when I was considering whether `01-CONTEXT.md:69`'s "without making v1 authoring materially heavier" Open Question might have an analogue in the Phase 01 plans that the canon inherited from. I did not read the plan files. This was a choice, not an oversight — the task spec's framing is that those files are being deleted and should not be treated as load-bearing. But the choice means any authoring-weight awareness in the Phase 01 plan files is invisible to this lane. I flag the choice and note that a Phase-01-planning-focused audit would surface what this lane cannot.

**Tension 4: Investigatory orientation's "present competing explanations" vs. the task spec's instruction to deliver "direct verdicts on LQ-B2.1 and LQ-B2.2".**

The task spec said don't hedge. Investigatory says don't collapse. I resolved each LQ verdict by producing a direct claim at the top ("Direct verdict: ...") and then unpacking the competing interpretations below. Whether this is a clean resolution or a smuggled hedge is a reader call; I flag the tension honestly. The LQ-B2.4 reframe verdict is the closest to unhedged — I say plainly that "authoring sustainability" is not the right frame and that the right frame is three linked concerns. The three-outcome classification verdict is the most hedge-shaped — I give percentages to all four possibilities rather than collapse to one. I did that because the evidence genuinely supports the composition, not because I was avoiding the direct call.

**Tension 5: The first-five-rounds reality-check being useful in all four outcomes (A/B/C/reframe) vs. the task spec's three-outcome classification requirement.**

I noticed while drafting LQ-B2.5 that OPS-04 is useful regardless of which outcome is correct. A classification scheme that forces me to choose one outcome would reject OPS-04 as a deliverable for any outcome except A. But OPS-04 is also useful for B (making the deferral testable), for C (providing the M1 bridge into the M2 vocabulary the canon already has), and for the reframe (providing the concrete first-5-rounds check the reframed concern needs). I chose to present OPS-04 as a cross-outcome deliverable rather than tie it to outcome A alone. This is not a navigation of the tension so much as a refusal to treat the three-outcome frame as exhaustive. The reader can disagree.

---

## Cross-Lane Notes For The Synthesizer

**For Lane B3 (distributed methodology, running in parallel):** My REV-2 finding that the long-arc canonization PLAN contains zero authoring-sustainability vocabulary is directly relevant. Lane B3 is characterizing the distributed methodology pattern; if Lane B3 finds the methodology does own authoring sustainability somewhere *other* than the long-arc canonization PLAN, that shifts my outcome-C weighting upward. If Lane B3 confirms the methodology is genuinely silent on this specific risk across all files, my outcome-C weighting shifts downward and outcome-A becomes the dominant reading. The cross-lane coupling runs in both directions — my LQ-B2.2 verdict depends on what Lane B3 finds.

**For Lane B4 (F1 legal carveout citation check):** My LQ-B2.4 analysis of the owner-commitment frame depends partially on Lane 1C's F1-legal-carveout claim being accurate. If Lane B4 finds that the canon does cite F1's legal rationale, the private-only framing is confirmed as a legal posture (not just a scope posture), which strengthens the owner-commitment frame I argued for. If Lane B4 finds the canon does not cite F1's legal rationale, the private-only framing is less load-bearing and the "why is this private-only" question becomes genuinely open — which weakens the owner-commitment frame specifically because it opens the possibility that "private-only" is a temporary scope choice rather than a durable configuration. The two lanes are not duplicating work — B4 checks citation presence, I check the consequences under the assumption that Lane 1C's quotation is accurate — but the outcome-weights compose at synthesis.

**For Wave 3 synthesis specifically:**
1. **The framework-invisibility finding about the PITFALLS-to-REQUIREMENTS citation mechanism's one-requirement-per-pitfall bias** is the single finding I most want engaged with. If the bias is systematic, there are probably other pitfalls with the same shape that need attention. A follow-up audit enumerating all 15 pitfalls against the citation mechanism would close this.
2. **The OPS-04 draft should be treated as a synthesizer-decision, not a Wave 2 commit.** I am surfacing what the claim should look like if outcome A is taken, not inserting it.
3. **The three-outcome framing itself is too narrow.** My verdict is a composition (30+30+25+15), not a selection. If Wave 3 forces a single-outcome collapse, information is lost. The composition itself is the finding.
4. **The "#1 risk ranking" has softer support than Wave 1 treated it.** Wave 3 should treat the predecessor's ranking as "two independent passes named it as a biggest concern with convergent operationalization" rather than as "methodologically scored #1." The substance holds; the framing is softer.
5. **The predecessor's MR-3 (5-round time audit with 30-min threshold) is the single most concrete canon addition the evidence supports.** If Wave 3 has time for one concrete recommendation, this is it.

**For deduplication with Lane B3:** I did not read `RESEARCH-PRINCIPLES.md` of the vision-alignment initiative for authoring-weight vocabulary beyond a quick grep (one hit only — "pack/round identity and reference shape" at line 20, which is scope, not authoring-sustainability). I did not read the Phase 01 `01-VALIDATION.md` file at all. Lane B3's broader distributed-methodology survey is the right place for those reads. If Lane B3 covers them, there is no duplication. If Lane B3 does not, there is a gap in our combined coverage that Wave 3 should note.

---

## What Remains Unknown (Addendum Beyond The Specific Bullets Above)

A meta-unknown worth naming: **I do not know whether the risk framing I pushed back against ("authoring sustainability" as imported public-product vocabulary) is actually wrong, or whether my pushback is Opus-posture bias toward "the canon is more principled than Wave 1 treated it."** Lane 1A named this self-criticism possibility at `wave-1-lane-1a-canon-integrity.md:401`: *"I am also susceptible to under-weighting findings that would implicitly recommend more refresh work, because the refresh already happened."* I am susceptible to the same bias in the opposite direction: I may be too willing to accept that the canon's framing is principled because the canon author is the same person who will read this audit. An adversarial human reviewer would push harder on whether the canon is genuinely right to use M2 framing or whether M2 framing is convenient-avoidance of an M1 concern.

---

## Rule 5 — Frame-Reflexivity (Full Section)

### Grounding Question 1: *"If this lane had been classified as `process_review` instead of `requirements_review` (asking 'how is the methodology handling authoring sustainability?' instead of 'should the requirements set claim it?'), what would it have looked for that I didn't?"*

A `process_review × investigatory × self` lane would have looked at the **process** by which risks move from research into canon. Specifically:

- It would have enumerated all 15 pitfalls in PITFALLS.md and checked which ones made it into REQUIREMENTS.md via the `Motivation: research: .planning/research/PITFALLS.md#...` citation pattern. I noted the pattern for Pitfalls 6, 8, 9 (cited) and Pitfall 14 (not cited) but did not enumerate the others. A process_review lane would have produced a complete map, which would have turned my "possibly systematic bias" hypothesis into a testable claim.
- It would have looked at the `discuss-phase` workflow to check whether that workflow has a step that pulls risks from research into canon — i.e., is the research-to-canon intake *automated* by the workflow or is it *manual and ad hoc*? Lane 1B grep-checked the workflow file shallowly (`wave-1-lane-1b-methodological-inheritance.md:293`). A process_review lane would go deeper.
- It would have looked at the predecessor audit's `METHODOLOGY-REVIEW.md` (which Lane 1A/1B both referenced but neither engaged with substantively) to see whether the methodology literature in that file addresses research-to-canon intake as a named methodology concern.
- It would have produced a **finding about the canon's form** rather than a finding about any specific requirement. The finding would be something like "the canon's Requirements section is shaped to own claims-about-the-system, not claims-about-the-authoring-process; that form shape is structurally blind to meta-risks that require measurement-triggered priority flips." I named this in framework invisibility but did not pursue it.

**Concrete example of something I did not notice because of the requirements_review frame**: the Phase-Specific Warnings table at `PITFALLS.md:294-305` has its own column for phase, pitfall, and mitigation. The Phase 1 row has no "Authoring" entry — the first phase-level mention of authoring is `| Authoring Tools + Expansion | Tooling arrives only after content velocity collapses | ...`. A process_review lane would have noticed that the phase at which the authoring risk materializes (per PITFALLS.md's own framing) is a phase *called* "Authoring Tools + Expansion" — which is not in the current ROADMAP.md phase list. That phase name is a holdover from an older phase taxonomy. The fact that the current ROADMAP does not have a phase called "Authoring Tools + Expansion" and does not map PITFALLS.md's "Authoring Tools + Expansion" row onto any existing phase is **a phase-taxonomy drift finding** that my requirements_review frame cannot produce because it is not asking about phase-taxonomy-alignment. A process_review frame asking "does the risk registry match the phase taxonomy?" would find this immediately.

This is a concrete finding the requirements-review frame produced only peripherally (I noticed the phase name mismatch while reading PITFALLS.md but did not follow up because the frame did not prioritize it).

### Grounding Question 2: *"If this lane had been classified with `standard` orientation instead of `investigatory`, what would it have closed on that I held open?"*

A `requirements_review × standard × self` lane would have closed on a clean verdict. Options it would have closed on:

- **"Authoring sustainability is a gap; add OPS-04."** — The simplest standard-orientation close, and the one the evidence most supports at surface level. I argued for OPS-04 but did not close on it as the single verdict.
- **"Authoring sustainability is already deferred to M2; no action needed."** — A lighter close, legitimate if the evidence is read from the canon-is-principled direction. I did not close on this either.
- **"The concern exists but is outside the canon's form; no requirement is the right answer."** — The hardest close, and the one that most respects the framework-invisibility finding. I did not close on this.

**What I held open that standard would have closed on**: I held the 30/30/25/15 composition open rather than picking one outcome. A standard orientation would have forced me to pick. My investigatory orientation let me say "the answer is a composition, not a choice" — and I think the composition is the correct finding, but a standard-orientation reader might reasonably say I avoided the decision. The anti-performativity concern here is real: am I using investigatory orientation as an excuse to avoid committing to a single verdict, or is the composition genuinely the answer? I think it is the answer (my OPS-04 draft is useful under all four outcomes; my framework-invisibility finding is about the form of the canon, not any single outcome; my reframe is about how the imported frame fits the project). But a reviewer should judge that themselves.

**Concrete example of closure I avoided**: I did not commit to the claim *"the canon author should add OPS-04 as a v1 requirement"* as a verdict. I drafted OPS-04 and named it as the claim I would propose under outcome A. The investigatory orientation let me present the draft as a finding-about-what-outcome-A-would-require rather than a recommendation-to-commit. A standard orientation would have pushed me harder to convert the draft into a recommendation. I think the distinction matters because a recommendation that skips the reframe (outcome D) is incomplete, and the reframe is not a recommendation shape.

### Grounding Question 3: *"What about the `requirements_review × investigatory` classification shapes what I am prepared to notice and what I am not? Name one concrete example."*

The `requirements_review × investigatory` classification **orients me toward treating claims as the unit of analysis and toward holding multiple interpretations open**. Concretely:

- It orients me toward looking for *absent* requirements and evaluating whether the absence is gap or principled. I did this throughout the LQ ledger.
- It orients me toward *vocabulary-level* engagement with the canon — reading each requirement text, checking for citations, checking for consequence-framing in Open Questions, etc. Lane 1A's search-term-specific framing was catchable by my investigatory orientation because I re-ran the search with a broader term set.
- It orients me **away from** engaging with "the form of the canon as a whole" as a unit of analysis. The canon's structure — Key Decisions, Open Questions, Requirements, Constraints, Evolution — is not something requirements_review asks me to examine. It is something I would examine under `artifact_analysis` or `process_review`. When I noticed the framework-invisibility finding about the canon's form lacking a "Practices" section, I was stepping outside my subject to name it. A requirements-review frame would have either (a) missed the finding entirely or (b) treated it as "not my job".

**Concrete example of one noticing the classification produced and one noticing it suppressed:**

- *Noticed*: the absence of a `Motivation:` citation for the v2 `### Content Operations` and `### Content Scaling` section items. I noticed this because citations are requirement-specific metadata and requirements_review is oriented toward requirement-level hygiene. This is a real finding — the v2 section is uncited where the v1 section is uniformly cited — and requirements_review made it visible.

- *Suppressed*: the question of whether the canon *can* own a measurement-triggered process, because that's a form question not a requirements question. I noticed the suppression only when writing framework invisibility. A reader of my output should understand that OPS-04 as drafted is a workaround for a form gap I named but did not fix.

### Anti-performativity note

This Rule 5 section names (1) a specific process-review finding I would have produced (phase-taxonomy drift between PITFALLS.md's "Authoring Tools + Expansion" and the current ROADMAP.md phase list); (2) a specific closure I avoided (OPS-04 as commitment-to-act); (3) a specific form-gap (measurement-triggered practices cannot live in current canon form). Each of these has concrete textual consequence in the findings above. If this section is empty or rhetorical on re-read, the ground rules were under-engaged. My self-check: the framework-invisibility section and this Rule 5 section converge on the same form-gap finding from different directions, which is weak evidence the finding is real and not a performative gesture.

---

## What The Obligations Didn't Capture

The obligations covered a lot. Five findings exceeded them.

1. **The form gap between "measurement-triggered practice" and "requirement"**. The canon has no form for "if X is measured and found to be Y, change priorities." Requirements are system-state claims; Constraints are product-shape claims; Key Decisions are closed choices with rationale; Open Questions are unresolved decisions; Evolution is a protocol for document updates. There is no place in the canon form for "run this measurement, decide based on result." OPS-04 as drafted is a workaround — it shapes a measurement-triggered practice as a requirement that the author (not the system) performs. The canon's form does not have a native home for the claim and the workaround is a finding about the canon's form, not about authoring sustainability per se. No obligation in my task spec asks me to notice form gaps.

2. **The question of whether "private-only fan project" is a product-shape or a hobby-shape**. The task spec names the qualifier *"private-only fan F1 game project whose v1 milestone is Game Night Works"* as load-bearing for the requirements_review judgment. But the qualifier itself contains an ambiguity I could not resolve: a private-only fan project can be (a) a small-team fan product that happens to be private, (b) a friends-only hobby that happens to have software, or (c) a personal creative practice that happens to be shareable with friends. The three shapes have different failure modes, different success criteria, and different canon vocabularies. The canon does not name which shape it is, and my investigation did not settle it. This is not a requirements-review finding; it is a product-identity finding that requirements-review cannot produce because the subject is about claims, not about identity.

3. **The risk that the audit chain is itself the "distributed methodology" pattern that Lane 1B flagged.** This audit is Wave 2 Lane B2. Wave 1 had 3 lanes, Wave 2 has 3 lanes, and there will be a Wave 3 synthesis. The convergence across waves is the audit's analogue to the distributed methodology prix-guesser uses — methodological discipline distributed across many files rather than concentrated in one. Lane 1B flagged this pattern for prix-guesser as a framework-invisibility finding. **The same pattern applies to the audit itself**: no single lane can produce the load-bearing finding; the finding emerges from composition. My output is just one piece of that composition. If the audit chain has the same systematic blindness prix-guesser's distributed methodology has, my output inherits the blindness invisibly. I cannot name it specifically, but I can name that the risk exists.

4. **The question of what "the canon" even is.** My task spec listed PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md, and STATE.md as canon. PITFALLS.md was listed as research. The initiative's README and PLAN were listed as distributed-methodology candidates. 01-CONTEXT.md was listed as a phase artifact. The boundary between "canon" and "not-canon" was prescribed, not investigated. But my finding that the risk lives in research (PITFALLS.md) and the canon-to-research citation mechanism chose not to pull it through — that finding only makes sense if canon and research are treated as separable. If the canon-research boundary is actually porous (which the citation mechanism implies it is), then "does the canon own X?" is partially a boundary-drawing question that my task spec pre-answered. A lane classified as `artifact_analysis × exploratory` would have investigated the boundary rather than inheriting it.

5. **The fact that I drafted OPS-04 without having ever authored an F1 round.** The draft is grounded in the predecessor's Lane 4 threshold (15-20 min target, 30 min threshold). Those numbers came from a different model reasoning about a project it had not executed. I am a second model reasoning about the numbers a first model produced, and neither of us has authored a round. The entire chain of reasoning about the right threshold is inference from file-reads, and none of the inference has been validated against direct experience. My OPS-04 draft is therefore a hypothesis about what a useful threshold would be, not a ground-truth measurement recommendation. The obligations do not ask me to name this specifically because the audit vocabulary treats "citing the predecessor" as sufficient grounding, but the chain from the predecessor's number to my draft is longer than a single citation and the grounding weakens at each hop.

---

## Candidates For Further Follow-Up

In descending priority order:

1. **Interview the project owner on authoring time for a sample round.** Not an audit — a conversation. Half an hour. "Can you draft one F1 round end-to-end while we track time per sub-task?" The direct data would close LQ-B2.3 and sharpen LQ-B2.5 faster than any further file-read audit could.

2. **Process-review audit of the PITFALLS-to-REQUIREMENTS citation mechanism.** Enumerate all 15 pitfalls in PITFALLS.md. For each, check whether any v1 or v2 requirement cites it. Check whether the citations follow a pattern (single-requirement landing place vs meta-process). Produce a propagation map. Suggested subject: `process_review × investigatory × self`. Purpose: settle whether the citation mechanism's bias against Pitfall 14 is systematic or one-off.

3. **Re-read GPT-5.4's 2026-04-08 Lane 4 output directly.** The "both ranked this #1" claim at `SYNTHESIS.md:186` is the load-bearing support for treating authoring sustainability as a cross-model convergent concern. I verified Opus-Lane-4 but not GPT-Lane-4. A short targeted read would close the gap. Can be done by the Wave 3 synthesizer in 15 minutes.

4. **Artifact-analysis audit of the canon's form vocabulary.** Does the canon need a "Practices" section? Does REQUIREMENTS.md need a subsection for measurement-triggered practices alongside Requirements? Does PROJECT.md's Key Decisions table need a "Measurement-Triggered Priority Flip" row type? These are form questions that would change what the canon *can* own. Subject: `artifact_analysis × exploratory × self`. Probably premature before a real M1 execution cycle tests the current form.

5. **Cross-model replication of this lane.** Run a Codex GPT-5.4 xhigh against the same task spec. Compare findings. Specifically check whether a non-Opus reader would catch the form-gap framework-invisibility finding, and whether a non-Opus reader would come to the same composition verdict (30/30/25/15). Subject: `requirements_review × investigatory × cross-model`. Purpose: test whether Opus-on-Opus convergence is real convergence or is an artifact of the model class holding constant.

6. **Phase-01-planning-layer audit of the 01-CONTEXT.md line 69 Open Question** ("How much answer-target lineage... without making v1 authoring materially heavier?"). This lane did not follow the authoring-heaviness thread into the phase-planning layer. A targeted audit would check whether phase planning has an implicit ownership of the concern that the canon does not.

7. **Whether the canon's "reopen doctrine" at `LONG-ARC.md:146-153` should name owner-interest-loss as a reopen condition.** This is a doctrinal question about what LONG-ARC.md should own, and would make the owner-commitment frame explicit in the canon without having to transform it into a requirement. Subject: `requirements_review × standard × self`, targeted narrowly.

---

## Meta-Reflection

The lane produced one concrete draft (OPS-04), one load-bearing framework-invisibility finding (the citation mechanism's bias against meta-risks), one reframe finding (authoring sustainability is not the right frame; three linked concerns are), one disconfirmation of the orchestrator's strongest outcome-C hypothesis (the long-arc canonization PLAN does not own the risk), one partial disconfirmation of Lane 1A's strongest claim (the canon does contain the vocabulary in narrower form than Lane 1A's search terms caught), and one softening of the predecessor's "#1 ranking" into "cross-model convergent biggest-risk-concern with shared operationalization."

The composition verdict (30/30/25/15) is not a hedge — it is what the evidence composes into. A single-outcome collapse would lose information. The right next action for Wave 3 is probably to take the OPS-04 draft as a candidate for outcome A, treat it as a validation check that would surface whether outcome B holds, and read my framework-invisibility finding as a standalone flag for a follow-up process-review pass.

The single most important thing I want Wave 3 to notice: **the canon has an existing citation mechanism for pulling research-layer risks into requirements, and the mechanism was used for three pitfalls but not for Pitfall 14, which corresponds exactly to the predecessor audit's top convergent concern.** That is a fixable mechanism-level finding that does not require deciding which outcome (A/B/C/reframe) is correct. Whichever outcome Wave 3 converges on, adding the citation is a low-cost high-value move.
