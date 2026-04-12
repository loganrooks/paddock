---
date: 2026-04-11
handoff_for: continuation of wave-structured audit `phase-01-prep-quality-scope-audit-2`
status: Wave 1 complete, Wave 2 complete, Review Gate 2 pending, Wave 3 synthesis not yet dispatched
audit_session_dir: .planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/
authoring_session: Claude Opus 4.6 (claude-code, 1M context, /effort max/high across the session)
---

# Claude Session Handoff — Phase 01 Prep Quality & Scope Audit

> **This file is the primary session-continuity document for the in-progress audit of prix-guesser's Phase 01 preparatory work.** Read this first on reentry. It should contain everything needed to continue the work without re-reading the full conversation history or the predecessor Codex prep documents.

---

## ⏸ Pause State — Where The Session Stopped

**The orchestrator (Claude Opus 4.6) paused at Review Gate 2, immediately before either (a) dispatching Lane B7 as a pre-synthesis bolt-on or (b) dispatching Wave 3 synthesis directly.** The user asked for this handoff specifically because context was getting high. No further dispatches have been made after Wave 2's four lanes (B2-Opus, B2-Sonnet, B3, B4) completed.

**The decision held at the pause**: whether to dispatch B7 (F1 legal ambiguity deep-read via WebFetch on Opus general-purpose, ~15-20 min) before Wave 3 synthesis, or to skip directly to synthesis. The orchestrator recommended "B7 then synthesis" but did not commit. **This is the first question a reentry session must resolve.**

---

## 📋 START HERE — Onboarding for a Reentry Session

If you are a Claude session picking up this work fresh:

1. **Read this handoff in full first** — it is the navigational entry point.
2. **Read the parent audit task spec**: `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/phase-01-prep-quality-scope-audit-2-task-spec.md`. This contains the full audit obligations, the classification (investigatory × no-subject × self), and the original investigatory questions. The task spec is ~600 lines.
3. **Briefly skim the Wave 1 and Wave 2 lane outputs** (pointers in the File Inventory section below). Don't deep-read all of them unless the next action requires it — the summaries in this handoff are intentionally substantive to minimize required re-reading.
4. **Check the STATE.md and config.json** for any changes since this handoff (`cat .planning/STATE.md .planning/config.json` or Read them).
5. **Resume at the pause state above**. Decide B7 vs direct-to-synthesis.

If you are the original orchestrating session returning after context compression or a break:

- You probably remember most of this. The handoff is a safety net. Skim the Status and Pause State sections to re-anchor, then continue.

---

## The Project (one paragraph)

**Prix Guesser** is an unofficial, private-only F1 fan game project being built around the fantasy of "GeoGuessr for Formula 1 places." V1 targets friends-on-couch / private-remote / hybrid game nights with browser-first guests and host-screen watchability. The anchor mode is authored geography-and-circuit rounds with clue ladders and reveal grammar. The project has a three-milestone long arc (M1 "Game Night Works" → M2 "Play Anytime Anywhere" → M3 "F1 Party Platform") where only M1 is on the active execution spine. Canon docs are at `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/STATE.md`. Phase 01 is "Authored Round Contract" — the substrate-freezing phase that will lock the authored-pack-and-round contract. STATE says "Replanning required before execution."

---

## The Audit (one paragraph)

The audit investigates whether prix-guesser's preparatory work (canon + Phase 01 context/research/validation + a newly-authored "narrow vision-alignment initiative") justifies proceeding to Phase 01 planning, or whether broader alignment work is needed. The audit is **investigatory × no-subject × self** — the subject is deliberately left open because forcing it would smuggle in the conclusion. The user explicitly invoked this audit from Claude Code with the framing that (a) time-pressure/momentum arguments are not load-bearing, (b) deployment/distribution/adoption concerns should be considered broadly, and (c) qualified conditional judgments are permitted (not just approve/reject). The comparison reference is the f1-modeling vision-alignment initiative at `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/`. The full scope is in the parent task spec (`phase-01-prep-quality-scope-audit-2-task-spec.md`).

---

## The Wave Structure Decision

**Why we are doing waves instead of single-shot single-agent dispatch:**

The orchestrator initially drafted a single-agent investigatory task spec. The user questioned whether the audit should itself model the iteration discipline it is evaluating (since the audit is partly about whether prix-guesser's narrow initiative has equivalent expansion provisions to f1-modeling's vision-alignment initiative, which explicitly uses wave structure with review gates). Auditing iteration discipline via a one-shot agent would be methodologically ironic. The user chose a light wave structure:

- **Wave 1 — terrain mapping** (3 parallel lanes, all Opus initially)
- **Review Gate 1** — orchestrator+user review, decide Wave 2 shape
- **Wave 2 — focused deepening** (4 parallel lanes: 2 Opus substantive, 1 Sonnet controlled twin on B2, 1 Sonnet empirical)
- **Review Gate 2** — current pause state
- **Wave 3 — synthesis** (1 Opus agent, single output file, not yet dispatched)
- **Optional bolt-on: B7** (F1 legal ambiguity, Opus general-purpose with web tools, ~15-20 min) before Wave 3

Total cost: 4-6 subagents originally proposed; Wave 1 used 3 + 1 search job; Wave 2 used 4. Running total: 8 subagent dispatches (not counting the initial Sonnet search job for comparison data). Wave 3 would be 1 more (plus B7 if dispatched).

**The user explicitly chose Option C (wave structure) over Option A (single-agent) and Option B (4-lane parallel dispatch without gates) at the pre-Wave-1 decision point.** The wave structure is load-bearing for the audit's methodological coherence.

---

## Status Table — Wave 1

| Lane | Subject × Orientation × Model | Status | Output file |
|---|---|---|---|
| **1A — Canon Claim Integrity** | `claim_integrity × investigatory × Opus gsdr-auditor` | ✅ Complete | `wave-1-lane-1a-canon-integrity.md` |
| **1B — Methodological Inheritance** | `comparative_quality × investigatory × Opus gsdr-auditor` | ✅ Complete | `wave-1-lane-1b-methodological-inheritance.md` |
| **1C — External Gap Research** | `no-subject × exploratory × Opus general-purpose (web)` | ✅ Complete | `wave-1-lane-1c-external-gap-research.md` |

All three Wave 1 task specs are also on disk in the session directory with `-task-spec.md` suffixes.

## Status Table — Wave 2

| Lane | Subject × Orientation × Model | Status | Output file |
|---|---|---|---|
| **B2-Opus — Authoring Sustainability** | `requirements_review × investigatory × Opus gsdr-auditor` | ✅ Complete | `wave-2-lane-b2-opus-authoring-sustainability.md` |
| **B2-Sonnet — Authoring Sustainability (twin)** | `requirements_review × investigatory × Sonnet gsdr-auditor` | ✅ Complete | `wave-2-lane-b2-sonnet-authoring-sustainability.md` |
| **B3 — Distributed Methodology** | `process_review × investigatory × Opus gsdr-auditor` | ✅ Complete | `wave-2-lane-b3-distributed-methodology.md` |
| **B4 — F1 Legal Carveout Citation** | `claim_integrity × standard × Sonnet gsdr-auditor` | ✅ Complete | `wave-2-lane-b4-f1-legal-carveout-citation.md` |

All four Wave 2 task specs are on disk with `-task-spec.md` suffixes.

## Status Table — Wave 2 Supplement + Wave 3

| Item | Status |
|---|---|
| **B7 — F1 Legal Ambiguity Resolution** | **NOT YET DISPATCHED**. Would be Opus general-purpose with WebFetch, ~15-20 min. Specifically asked to resolve the tension Lane 1C surfaced between F1's "private educational use" carveout and F1's "motorsport simulators/software should not make any use without an express written license" clause. Whether prix-guesser (a browser game with authored F1 content) falls under the carveout or the simulator prohibition is unresolved. |
| **Wave 3 Synthesis** | **NOT YET DISPATCHED**. Would be Opus gsdr-auditor. Would read all 7 (or 8 with B7) lane outputs plus the parent task spec and produce `phase-01-prep-quality-scope-audit-2-output.md` (the canonical final audit output path named in the parent task spec frontmatter). |

---

## ⚡ Immediate Next Actions (in priority order)

1. **Decide B7 vs direct-to-synthesis.** (This is the pause-state question.) Orchestrator's recommendation at the pause was "B7 first, then synthesis" because the F1 legal ambiguity is directly load-bearing for the final audit conclusion — the "cite the carveout" recommendation is weaker if the carveout doesn't actually apply. But "synthesis now, name the ambiguity as a two-part recommendation" is a legitimate alternative. User did not commit.
2. **If B7**: write `wave-2-lane-b7-f1-legal-ambiguity-task-spec.md`, dispatch one Opus general-purpose agent with WebFetch access. Read F1's actual guidelines at `https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt` and resolve whether the private-educational carveout or the simulator prohibition applies to prix-guesser's specific shape. Output to `wave-2-lane-b7-f1-legal-ambiguity.md`. Then proceed to step 3.
3. **Write the Wave 3 synthesis task spec**: `wave-3-synthesis-task-spec.md`. Should reuse most of the parent task spec's obligations verbatim (Core Rules 1-5, investigatory I1-I4, chain integrity, framework invisibility, composition principle) but reframe the lane from "audit this directly" to "synthesize N lane outputs into the final audit output, explicitly comparing B2-Opus and B2-Sonnet as a controlled meta-finding." Must name all lane outputs as predecessors and require the synthesizer to re-verify any load-bearing claims before incorporating them (chain integrity applies to lane outputs, not just 2026-04-08 predecessor audit claims).
4. **Dispatch Wave 3 synthesis** as a single Opus gsdr-auditor agent. Foreground. Model selection: Opus, not negotiable — synthesizer needs maximum hermeneutic depth to hold 7+ lane outputs in tension and produce the practical conclusion.
5. **Read the synthesis output** (`phase-01-prep-quality-scope-audit-2-output.md`), verify it addresses all obligations, and report the findings back to the user.
6. **Commit the audit session directory** using the standard GSD commit pattern if `commit_docs` is true in `.planning/config.json` (currently true per earlier read).

---

## Audit Classification Summary (canonical reference)

**Parent audit (phase-01-prep-quality-scope-audit-2)**: `no-subject × investigatory × self` — Claude Opus 4.6 dispatching to gsdr-auditor subagents in a claude-code session.

**Not**: `cross_model` delegation (Codex had originally written a `cross_model:claude-opus-4.6` task spec, but that was Codex dispatching to Claude; when Claude Code picked up the audit, it became `self` delegation because Claude is dispatching to Claude subagents).

**Subject deliberately left open** because forcing a subject would smuggle in the conclusion the audit is interrogating. Each Wave 1/2 lane applied a specific subject for its own focused scope (claim_integrity, comparative_quality, requirements_review, process_review) — these were lane-level subject assignments, not a parent-audit subject. Wave 3 synthesis inherits the parent's no-subject classification because it composes across multiple lane subjects.

**Ground rules composition**: `core + investigatory + chain + self-dispatch-hygiene + framework-invisibility`. Full text is in the parent task spec.

---

## Headline Findings Across Both Waves (condensed)

**These are SUMMARIES. The full findings are in the lane output files.** Do not rely on these summaries for any load-bearing claim without reading the source — this is explicitly the chain-integrity discipline the audit requires.

### Wave 1 convergences

1. **Lane 1A**: The canon is "recent earned convergence stapled onto older repeated assumption." `LONG-ARC.md` is one day old (canonized 2026-04-11) and older canon docs were retrofitted to cite it in commit `5dfaa59`. The narrow initiative's "already aligned" claim reads a state that has not yet survived its first planning cycle (the pending discuss-phase rerun is the first test). Three-outcome ledger with 12 REV-* entries applied to predecessor recommendations: mix of clean adoptions, principled softenings, and one real gap (stable diagnostic codes for venueRef, REV-12).

2. **Lane 1B**: Prix-guesser's narrow initiative is NOT structurally equivalent to f1-modeling's on three specific operational provisions — (a) explicit permission to declare structure wrong at review gates, (b) prompt-file authorship strategy at gates (most consequential), (c) explicit loopback permission. Also: most methodological drops are principled but three cross into collateral damage — reframing permission, trajectory analysis as output production, calibrated confidence markers. **Framework-invisibility finding**: prix-guesser's methodological discipline is distributed across files, not concentrated in the vision-alignment initiative files. `.planning/deliberations/2026-04-11-long-arc-canonization/PLAN.md` (~892 lines) was flagged as containing execution discipline "substantively stronger than anything in f1-modeling's vision-alignment PLAN."

3. **Lane 1C**: **F1's own trademark guidelines actively legitimize the "private-only" framing.** F1 carves out "limited use... for a private, educational purpose only" while also stating motorsport simulators/software "should not make any use of the FORMULA 1 Rights without an express written license." **This inverts the user's initial concern**: the "private-only under-considers distribution" worry is wrong in the legal direction — private-only is the exact legal carveout F1 permits. But the canon doesn't cite this rationale (verified by Wave 2 B4). Also: all existing F1 fan games are single-player daily-puzzles; zero are private-room multiplayer party games. **The adoption challenge is shape education, not distribution.** PBLive (https://github.com/RunasSudo/PBLive) is near-exact prior art for the Phase 01 authored YAML quiz contract and was archived August 2022 without a documented reason (not yet investigated — candidate for Wave 2 follow-up).

4. **Orchestrator fallibility caught by Lane 1B**: the orchestrator's Wave 1 pre-list of methodological drops had 2 of 8 factually wrong claims (25% error rate). Path of Inquiry and Dependencies and Relations sections in prix-guesser's RESEARCH-PRINCIPLES.md were explicitly preserved at lines 108 and 111 — the orchestrator claimed they were dropped. This lesson propagated to all Wave 2 task specs as an explicit "task-spec claims are contestable, flag errors as findings not silent corrections" warning.

### Wave 2 findings

5. **B2-Opus + B2-Sonnet convergences (the controlled comparison)**:
   - Both partially disconfirmed Lane 1A's "canon doesn't own it" claim. The canon has related vocabulary ("sustainable content operations," "content scaling," "authoring and preview tooling that make content production sustainable") — at **Milestone 2 destination level**, not M1 risk level. Lane 1A's substantive claim holds in a softened form.
   - **Both disconfirmed the task spec's inference that long-arc-canonization PLAN owns the risk.** Direct grep on the 892-line PLAN found zero authoring-sustainability content. It is a procedural implementation document, not a risk-ownership document. Both lanes surfaced this as a task-spec factual error — same category as Lane 1B's 25% rate.
   - Both softened the predecessor's "#1 risk" ranking. Lane 4 of the 2026-04-08 audit used alphabetical labels (Risk A), not numeric ranks. Rhetorical convergence, not scored ranking.
   - Both reframed "authoring sustainability" away from public-product vocabulary. Opus decomposed into (a) first-5-rounds reality-check, (b) owner-hobby-budget working-assumption, (c) shape-validation pre-build checkpoint. Sonnet named it "owner-friction-exceeds-motivation." Same shape, different wording.
   - Both proposed concrete canon claims. Opus drafted OPS-04 (5-round time audit, 30-min pain threshold, PITFALLS.md#14 citation). Sonnet proposed a named risk acknowledgment with specific deferral trigger.
   - **Opus caught a cheap standalone finding**: PITFALLS.md Pitfall 14 ("Delaying content validation and authoring support until the corpus is already painful," Severity: High) is owned at the research layer. REQUIREMENTS.md has a working citation mechanism that cites Pitfalls 6, 8, 9 — **but NOT Pitfall 14**. Cheap ownership gap that is true regardless of outcome.

6. **B2 meta-comparison — the methodologically most important finding**: **Sonnet 4.6 and Opus 4.6 produced substantively equivalent findings on investigatory × requirements_review hermeneutic work with rigorous ground rules.** Disagreements were about depth and framing, not substance. Opus caught more adjacent vocabulary and produced a weighted-probability classification; Sonnet caught the task-spec inference error more sharply and produced a cleaner verdict. Neither missed the load-bearing conclusions the other reached. **This validates the framework's documented escalation posture**: Sonnet is the baseline for audit work, Opus is for escalation when warranted — not Opus by default. **Future audit dispatches can default to Sonnet unless specific hermeneutic stress justifies escalation.**

7. **B3 (distributed methodology, Opus)**:
   - Verified Lane 1B's "substantively stronger" claim with a category-difference qualifier. The two plans are rigorous at different *decision surfaces* (execution-bounds vs deliberation-shape), not on one scale.
   - **Third pattern named: "Tiered decision-surface methodology."** Each tier specializes in a class of decision: execution-bounds, deliberation-procedure, meta-methodology, non-foreclosure, workflow-operational, canon-output. Six tiers across ~14 methodology-adjacent files.
   - **Critical qualifier**: proposed-not-battle-tested. Less than 24 hours old in its current shape. One execution cycle at one tier-combination only (discuss-phase → canon-output). Functional for that path; **NOT functional** for the initiative-planning case.
   - **Lane 1B's three operational gaps are NOT compensated by the distribution**. Structure-wrongness permission: present in 1 of 3 forms. Prompt-at-gate authorship: absent. Loopback permission: absent.
   - **Framework-invisibility findings (three)**: (1) methodology may not be the right unit of analysis — the author's *relation* to it is; (2) the pattern may be "Opus-reflection" not "project-reality"; (3) the long-arc-canonization PLAN's rigor may be a local response to over-patching fears, not a general methodology primitive.
   - **Cross-lane handoff to B2 for the synthesizer**: the meta-methodology reflection document is a candidate "soft canon" source for authoring sustainability's outcome C. The sidecar pattern (PLAN + JUSTIFICATION) is an existing primitive that could be instantiated for authoring sustainability as a sibling deliberation — a *fifth* outcome that neither B2 lane fully reached.

8. **B4 (F1 legal carveout citation, Sonnet)**:
   - **NO legal rationale in the canon.** Search terms "trademark," "copyright," "intellectual property," "fan use," "fair use," "licensing," "legal," "educational purpose" all returned zero matches across the five canon files. "Unofficial" appears but purely as an identity label, never grounded in legal policy.
   - **"The canon is making a legal decision without acknowledging it is legal."** The Key Decisions rationale at `PROJECT.md:153` gives "Public-safe constraints would distort the early product and reduce fidelity" — entirely product/scope framing, no legal dimension.
   - **Citation slot identified**: Constraints section of PROJECT.md (around line 141) and/or Key Decisions rationale cell. One-to-two sentences, not a new file. Minimum viable text drafted in the lane output.
   - **Gap-or-choice assessment**: more likely gap than choice. Discovery directory's `05-content-and-rights.md` does IP-risk reasoning **without referencing F1's policy document**, suggesting the policy was not consulted.
   - **Unresolved legal ambiguity (critical for synthesis)**: F1's guidelines contain BOTH a "private educational use" carveout and a "motorsport simulators/software should not make any use without an express written license" clause. **Whether prix-guesser (a browser game with authored F1 content) falls under the first or the second is NOT closed.** The "cite the carveout" recommendation is weaker than Lane 1C's summary implied. This is the specific question B7 would resolve if dispatched.

---

## 🧭 The Emerging Audit Conclusion (the orchestrator's current read)

**Not the synthesizer's output — the orchestrator's current read of where the findings compose.** A Wave 3 synthesis may differ.

1. **The narrow vision-alignment initiative's "canon is aligned" premise is directionally right but reads a fresh state.** The canon was consolidated in the 24 hours before audit dispatch. This is the most important qualifier the synthesis must carry.

2. **The canon has specific fixable gaps, not a widening-required scope problem.** The audit's practical conclusion is emerging as: *"The narrow initiative can proceed with six specific additions — three canon additions and three PLAN additions — without widening the initiative's scope. Skipping any of the six requires a documented decision about why."*

   **The three canon additions**:
   - **Authoring sustainability ownership** at risk level (not M2 destination level), reframed as owner-friction / first-5-rounds reality-check / shape-validation. Concrete draft candidates: OPS-04 (Opus's version) or a named risk acknowledgment with deferral trigger (Sonnet's version). Plus the cheap fix: add `research: .planning/research/PITFALLS.md#14` citation to REQUIREMENTS.md.
   - **F1 legal context acknowledgment** in the Constraints section of PROJECT.md. NOT a confident "cite the carveout" but rather "name the legal ambiguity and how the project navigates it." The simulator-clause-vs-carveout tension must be named, not papered over.
   - **Third pattern name and qualifier**: explicit acknowledgment that prix-guesser's methodology is a "Tiered decision-surface methodology" that is proposed-not-battle-tested. This is optional — the synthesizer may decide this is meta-documentation that doesn't belong in the product canon.

   **The three PLAN additions** (to the narrow vision-alignment initiative's PLAN.md):
   - Explicit permission to declare the planned structure wrong at a review gate
   - Prompt-file authorship strategy at review gates (author Wave 2A prompt at Gate 1, not now)
   - Explicit loopback permission (allow later stages to trigger earlier stages)

3. **The user's stated concern about "deployment, distribution, adoption" is partially wrong in the direction assumed.** Private-only is the correct legal posture (per Lane 1C) — the question is not "should we broaden scope" but "does the canon own *why* we're private-only." Lane B4 confirmed the canon doesn't. The adoption challenge is shape-education (teaching friends a new party-game shape into an F1 fan ecosystem that is all daily-puzzles), not distribution infrastructure.

4. **None of the findings support outright rejection of the narrow initiative**. The conclusion is qualified and conditional, exactly what the user invited.

5. **The meta-comparison between B2-Opus and B2-Sonnet** is a separate deliverable at the synthesis level — it is methodologically load-bearing for future audit dispatches in this project.

---

## 🎓 Lessons Learned From This Session

Lessons the next session should carry forward — both about the audit and about dispatch discipline.

### L1 — Task spec errors happen; flag them as findings

**The orchestrator made factual errors in Wave 1 pre-listing.** Lane 1B caught that 2 of 8 "methodological drops" in prix-guesser's RESEARCH-PRINCIPLES.md were not actually dropped (Path of Inquiry and Dependencies and Relations sections are explicitly preserved). Lane B2-Sonnet and Lane B2-Opus additionally caught that the task spec's inference about the long-arc-canonization PLAN owning authoring sustainability was factually wrong (direct grep showed zero content).

**The discipline**: every task spec the orchestrator writes is contestable. Subagents should be told to flag task-spec errors as findings, not silent corrections. This was baked into every Wave 2 task spec as a chain-integrity reminder. **Continue this discipline in the Wave 3 synthesis task spec.**

### L2 — Sonnet is adequate for hermeneutic audit work with rigorous ground rules

**The B2 controlled comparison is empirical data on the Sonnet-vs-Opus question.** The same task spec on both models produced substantively equivalent findings. This matches the framework's documented escalation posture (gsdr-auditor defaults to Sonnet; orchestrator escalates for specific investigatory/epistemic cases) and the 2026-04-09 gold-standard Sonnet audit result (`get-shit-done-reflect/.planning/audits/2026-04-09-discuss-phase-exploration-quality/rigorous-comparative-audit.md`).

**The discipline**: default future audit dispatches to Sonnet unless there's a specific reason to escalate. Opus is for "maximum hermeneutic stress" cases (e.g., Wave 3 synthesis of many lane outputs, characterizing a third pattern under uncertainty, framework invisibility on deeply interpretive questions). Most lane-level audit work is Sonnet territory.

### L3 — Size is a lazy comparison axis

**The orchestrator initially compared prix-guesser's vision-alignment initiative to f1-modeling's by raw artifact size.** The user correctly pushed back: f1-modeling is large because it has been *executing* for several waves, while prix-guesser's initiative is a freshly-authored scaffold that hasn't started running. The meaningful comparison is **PLAN structure and expansion provisions** (what each permits, what review gates say, what thresholds trigger growth, what prompt-authorship strategy applies at gates), not size.

**The discipline**: when comparing methodology artifacts, compare PLAN structure and expansion provisions, not artifact count or line count. This discipline is load-bearing for Lane 1B's work and must propagate to Wave 3 synthesis.

### L4 — Predecessor audit recommendations are contestable, not authoritative

**The three-outcome framing for chain integrity.** For every predecessor recommendation, ask (a) was it adopted? (b) **should it have been adopted in the form proposed?** (c) is the current state principled despite not matching the predecessor's exact recommendation? The 2026-04-08 audit's recommendations include many shaped for a serious public product (DEPLOY-01..05 formalization, hosted-game framing, Phase 3.5 inserted phase with full component inventory); some of these are inappropriate for a private-only fan game even though they would be right elsewhere.

**The discipline**: chain integrity is not just "verify the predecessor's claims" — it is "verify the predecessor's claims AND question whether the predecessor's recommendations were correct for this project." This was baked into all Wave 2 task specs and must carry into Wave 3 synthesis.

### L5 — The orchestrator error rate is small but real

Lane 1B: 2 of 8 pre-list errors (25%). Lane B2-Opus: the same long-arc-canonization PLAN error (counted as ~1 of 9, or ~11%). **The overall orchestrator-claim error rate is small single digits to ~25% depending on how you count.** The synthesizer should apply the same discipline to this handoff — if anything the orchestrator wrote turns out to be wrong, that is a finding, not a silent correction.

### L6 — Wave structure as methodological self-honesty

The user pushed back on a single-agent single-shot audit specifically because auditing iteration discipline via a one-shot agent would be methodologically ironic. **The audit itself models the discipline it evaluates.** Wave structure with review gates is how the audit honors the principle it's checking prix-guesser's narrow initiative against. This is the meta-level answer to "why aren't we just doing single-shot": *because an audit that asks "does this project iterate when warranted?" cannot honor that question by not iterating itself.*

### L7 — Framework invisibility is not compliance theater — it is the hardest real work

Every lane was required to name what its framing made invisible. The strongest findings across all 7 Wave 1/2 lanes came from the framework-invisibility sections:
- Lane 1A: canon doesn't own authoring-sustainability risk (visible only when canon is audited as itself claim-bearing rather than reference point)
- Lane 1B: prix-guesser's methodology is distributed across files, not in the initiative
- Lane 1C: the most important missed alternative is pre-build playtesting practice
- B2-Opus: canon form vocabulary has no native home for "measurement-triggered priority flip"
- B3: three distinct findings about methodology-as-unit, Opus-reflection-vs-project-reality, and local-response-vs-general-primitive

**The discipline**: the framework-invisibility section is not a checkbox. It is where the highest-leverage findings live. Wave 3 synthesis must address it as seriously as the primary obligations.

### L8 — Controlled comparison is cheap and high-value

Running B2 on both Sonnet and Opus in parallel cost approximately one additional Sonnet dispatch ($0.24 worth of tokens, ~15 min wall-clock at most since it ran in parallel). The meta-finding it produced is load-bearing for every future audit dispatch in this project. **Twin-pair controlled comparisons are under-utilized and should be used more often when the orchestrator has a specific model-class question.**

---

## 🔑 Critical Moments In Session History

In rough chronological order. These are the decision points where the audit's shape was set.

1. **User invoked `/gsdr:audit` from Claude Code** with a multi-sentence framing that rejected time-pressure arguments and asked for f1-modeling comparison. Codex had previously authored a task spec for `cross_model:claude-opus-4.6` dispatch; Claude Code's dispatch became `self` delegation.

2. **User clarified mid-orchestration** that the four `01-XX-PLAN.md` files in `.planning/phases/01-authored-round-contract/` were being deleted as stale residue. Codex's briefing had framed the worktree-vs-state mismatch as interpretively load-bearing; with the deletion, that frame no longer applied. **Wave 1 task specs were explicitly instructed to ignore those files.**

3. **Orchestrator drafted a single-agent task spec** (the v2 task spec at `phase-01-prep-quality-scope-audit-2-task-spec.md`) and then the user pushed back asking whether the audit should be multi-agent, multi-wave. Orchestrator laid out Options A (single-agent), B (4-lane parallel without gates), C (full wave structure). **User chose Option C light** — not full f1-modeling shape, just 2-lane Wave 1 → gate → optional Wave 2 → synthesis. Eventually this became 3-lane Wave 1 with the addition of research-lane B1C (general-purpose Opus with web tools).

4. **User challenged the Opus-vs-Sonnet assignment for Lane 1B.** The orchestrator had originally assigned Sonnet to Lane 1B on the grounds that structured comparison was Sonnet territory. The user asked for empirical data ("an audit somewhere in the past 3 days that compared these models"). Orchestrator dispatched a Sonnet search agent which surfaced the 2026-04-09 gold-standard Sonnet audit and the GSDR framework's escalation decision (sonnet baseline, opus escalation). The user then said "let's go with Opus" for Lane 1B. Sonnet-to-Opus reversal was done, and Lane 1B dispatched as Opus.

5. **User asked about metacomparison for Wave 2.** Orchestrator had dropped the B8 (Sonnet-Opus head-to-head) option in its initial Wave 2 recommendation. User surfaced it: "Wait so we aren't doing the metacomparison?" Orchestrator honestly reconsidered and agreed the rejection was rationalization. **Twinned B2 (Opus + Sonnet on same task spec) was added to Wave 2** as a controlled comparison, making Wave 2 a 4-lane shape instead of 3.

6. **Wave 2 completed** with all four lane outputs written to disk. B2-Opus and B2-Sonnet produced substantively equivalent findings, resolving the Sonnet-vs-Opus question empirically.

7. **User paused before Wave 3 dispatch** and asked for this handoff. Context was getting high and the user wanted to ensure session continuity before another round of dispatch.

---

## 📁 File Inventory

All paths relative to the repo root unless otherwise noted.

### This audit's session directory

`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/`

**Task spec files (all hand-authored by the orchestrator, consumed by subagents)**:
- `phase-01-prep-quality-scope-audit-task-spec.md` — Codex's original v1 task spec (predecessor preparation artifact, not the live dispatch)
- `phase-01-prep-quality-scope-audit-briefing.md` — Codex's briefing memo (starting map, not closed read list)
- `phase-01-prep-quality-scope-audit-best-case-minimal-alignment.md` — Codex's one-sided advocacy memo (stress target, not trusted premise)
- `phase-01-prep-quality-scope-audit-2-task-spec.md` — **the parent task spec for this session's audit**. Opus self-dispatch. ~600 lines. Full obligations and classification.
- `wave-1-lane-1a-canon-integrity-task-spec.md`
- `wave-1-lane-1b-methodological-inheritance-task-spec.md`
- `wave-1-lane-1c-external-gap-research-task-spec.md`
- `wave-2-lane-b2-opus-authoring-sustainability-task-spec.md`
- `wave-2-lane-b2-sonnet-authoring-sustainability-task-spec.md` (twinned with -opus- version)
- `wave-2-lane-b3-distributed-methodology-task-spec.md`
- `wave-2-lane-b4-f1-legal-carveout-citation-task-spec.md`

**Lane output files (produced by subagents, full findings)**:
- `wave-1-lane-1a-canon-integrity.md`
- `wave-1-lane-1b-methodological-inheritance.md`
- `wave-1-lane-1c-external-gap-research.md`
- `wave-2-lane-b2-opus-authoring-sustainability.md`
- `wave-2-lane-b2-sonnet-authoring-sustainability.md`
- `wave-2-lane-b3-distributed-methodology.md`
- `wave-2-lane-b4-f1-legal-carveout-citation.md`

**Not yet written (Wave 3 / B7 work)**:
- `wave-2-lane-b7-f1-legal-ambiguity-task-spec.md` (if B7 is dispatched)
- `wave-2-lane-b7-f1-legal-ambiguity.md` (B7 output if dispatched)
- `wave-3-synthesis-task-spec.md` (Wave 3 synthesis task spec)
- `phase-01-prep-quality-scope-audit-2-output.md` — **the final audit output path, named in the parent task spec's frontmatter**. Wave 3 synthesis will write here.

**This handoff**:
- `CLAUDE-SESSION-HANDOFF.md` (this file)

### Canon files (Phase 01 substrate the audit investigates)

- `.planning/PROJECT.md` (191 lines)
- `.planning/LONG-ARC.md` (154 lines) — **1 day old as of the audit, per Lane 1A**
- `.planning/ROADMAP.md` (205 lines)
- `.planning/REQUIREMENTS.md` (191 lines)
- `.planning/STATE.md` (81 lines)
- `.planning/config.json` (47 lines)

### Narrow vision-alignment initiative under audit

- `.planning/initiatives/vision-alignment-2026-04/README.md` (89 lines)
- `.planning/initiatives/vision-alignment-2026-04/PLAN.md` (123 lines)
- `.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md` (125 lines)

### Phase 01 live artifacts (DO NOT include the four deleted `01-XX-PLAN.md` files)

- `.planning/phases/01-authored-round-contract/01-CONTEXT.md` (179 lines)
- `.planning/phases/01-authored-round-contract/01-DISCUSSION-LOG.md` (76 lines)
- `.planning/phases/01-authored-round-contract/01-RESEARCH.md` (418 lines)
- `.planning/phases/01-authored-round-contract/01-VALIDATION.md` (80 lines)
- `.planning/phases/01-authored-round-contract/superseded/2026-04-11-pre-rerun-overreach/` (archive of prior overreach)

### Predecessor audit (2026-04-08 pre-execution review — contestable, not authoritative)

- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
- `.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md`
- Lane reports (`lane-1-plan-quality.md`, `lane-2-frontend-design.md`, `lane-3-stakeholder-distribution.md`, `lane-3-stakeholder-distribution-gpt.md`, `lane-4-multi-milestone-vision.md`, `lane-4-multi-milestone-vision-gpt.md`)

### F1-modeling comparison material (external project, read as needed)

- `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/README.md`
- `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/PLAN.md` (335 lines)
- `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md` (426 lines)
- `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/deliberations/01-decision-anchor.md` (the compact one — structurally the shape prix-guesser proposes to produce)
- `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/deliberations/01-backend-boundary-architecture.md` (the full deliberation, ~600 lines, showing what Wave 2 output looks like in practice)

### Distributed-methodology files (per Lane B3's corpus map)

- `.planning/deliberations/2026-04-11-long-arc-canonization/PLAN.md` (~892 lines — Lane 1B flagged as strong; both B2 lanes grep-confirmed it has NO authoring-sustainability content; it is a procedural PLAN, not a risk-owning PLAN)
- `.planning/deliberations/2026-04-10-roadmap-refresh-reread-plan.md` (474 lines — Lane B3 found this additional)
- `.planning/deliberations/2026-04-10-future-awareness-harness-patch.md` (276 lines — Lane B3 found this additional)
- `.planning/explore/2026-04-10-vision-future-hosting/` directory — contains the obsolete 2026-04-10 checkpoint-handoff file (decision: leave alone, historically complete, not interfering)

### Audit ground rules references (read for obligations vocabulary)

- `~/.claude/get-shit-done-reflect/references/audit-ground-rules.md`
- `~/.claude/get-shit-done-reflect/references/audit-conventions.md`
- `.planning/deliberations/audit-taxonomy-three-axis-obligations.md` (authority for the 3-axis model)
- `.planning/deliberations/audit-taxonomy-retrospective-analysis.md`

---

## 🎯 Open Questions The Wave 3 Synthesis Must Address

In rough priority order. The synthesizer should answer these explicitly.

1. **The F1 legal ambiguity** (B4's finding). Should the canon "cite the carveout" with confidence, or should it "name the legal ambiguity between private-educational carveout and simulator prohibition"? If B7 is dispatched, this resolves empirically. If not, the synthesis must hold both readings open.

2. **The three-outcome classification for authoring sustainability.** Both B2 lanes softened the three-outcome framing to a composition (~30% A + ~30% B + ~25% C + ~15% reframe for Opus; "Outcome A partial + reframe" for Sonnet). The synthesizer needs to name its own composition verdict and explain why.

3. **The third-pattern characterization** from B3. Is "Tiered decision-surface methodology" real, or is it an Opus charitable interpretation of uncentralized writing? The qualifier "proposed, not battle-tested" should carry through to any synthesis-level recommendation.

4. **Lane 1B's three operational gaps** (prompt-at-gate, loopback, structure-wrongness permission). B3 confirmed the distributed methodology does NOT compensate. The synthesis needs to either (a) recommend adding the three to the narrow initiative's PLAN, or (b) justify why the project can proceed without them. The synthesis should also consider whether the existing `deliberations/2026-04-11-long-arc-canonization/PLAN.md`'s execution-bounds discipline partially substitutes for one or more of them (B3 checked this but the synthesizer should verify).

5. **The meta-comparison finding** (B2 Sonnet vs Opus). This needs to be surfaced as its own meta-deliverable, not buried in the synthesis. It is methodologically load-bearing for future audit dispatches. Include a brief "For Future Audit Dispatches" section.

6. **The orchestrator error rate.** Both Lane 1B and both B2 lanes caught factual errors in task specs. The synthesis should note this explicitly — not as self-criticism but as chain-integrity discipline. The discipline worked: the auditors caught the errors. That is the system operating correctly.

7. **The practical conclusion shape.** The orchestrator's current read (this handoff's "Emerging Audit Conclusion" section) is a starting position, not the synthesis's conclusion. The synthesizer should produce its own reading, and if it converges with the orchestrator's read, note the convergence; if it diverges, name the divergence and reason about it.

---

## 🏗 Wave 3 Synthesis Task Spec Design Notes

When writing `wave-3-synthesis-task-spec.md`, the synthesis task spec should:

1. **Reuse most of the parent task spec's obligations verbatim** — Core Rules 1-5, investigatory I1-I4 plus two additional, chain integrity, self-dispatch hygiene (the synthesis is also self-dispatch so this still applies), framework invisibility, composition principle. DC-2 discipline: copy, don't reference.

2. **Add a synthesis-specific obligation**: the synthesizer must apply chain integrity to **lane outputs**, not just predecessor audit claims. Every lane output is a predecessor. Any load-bearing claim from any lane must be independently re-verified before incorporation.

3. **Frame the task differently from a lane**: the synthesis is not "investigate X" but "compose N lane investigations into the practical conclusion that honors the parent audit's obligations and produces the file the parent task spec named."

4. **Require the meta-comparison as its own section**. The B2 Opus-vs-Sonnet controlled comparison has to be analyzed separately from the substantive authoring sustainability findings. This is not "which one is right?" but "what did each lane produce, where did they converge/diverge, what does the comparison tell us about model-class dependence on hermeneutic audit work?"

5. **Require an explicit orchestrator-error section**. Not as shame, as discipline — the task specs had errors, the lanes caught some, the synthesizer should catch others if they exist. This is the system working correctly.

6. **Require the full Rule 5 section** (investigatory orientation, so it is a full section not a closing step) with the three specific grounding questions, and the anti-performativity warning.

7. **Require the mandatory "What the Obligations Didn't Capture" section.**

8. **Require the practical conclusion to be a concrete, actionable recommendation**. The user invited qualified/conditional judgments. "Six specific additions" is one possible shape. The synthesizer should produce a similarly concrete conclusion even if it differs from the orchestrator's current read.

9. **Include a "What Wave 3 Didn't Answer" section** — candidates for post-synthesis follow-up. The current candidates from the orchestrator's view: PBLive history deep-read (why was it archived?), authoring-time interview with the project owner (the fastest way to settle LQ-B2.3), the distributed methodology's first real execution cycle test (when does it run and what does it reveal?), the synthesis's own chain-integrity rate (how many of this synthesis's claims would a follow-up audit catch?).

10. **Output path**: `phase-01-prep-quality-scope-audit-2-output.md` — this is the file path named in the parent task spec's `output_files` field. Do not write to a different path.

**Model**: Opus. Non-negotiable. Synthesizing 7+ lane outputs while holding competing interpretations in tension is maximally hermeneutic work. Even though the B2 meta-finding shows Sonnet is adequate for lane-level hermeneutic work, the synthesis layer is one step further in stakes and composition complexity.

**Agent type**: gsdr-auditor. Has the ground rules discipline. No web tools needed since B7 would handle any web research separately.

**Dispatch**: single foreground agent. Not parallel. Duration estimate: 40-70 min depending on how thoroughly the synthesizer reads the lane outputs.

---

## 🧩 B7 Task Spec Design Notes (if dispatched)

If Wave 2 supplement B7 is dispatched before synthesis, it should:

1. Be **Opus general-purpose** (not gsdr-auditor — needs WebSearch/WebFetch). The general-purpose agent has full tool access.

2. **Scope**: narrow and empirical. Use WebFetch to retrieve F1's actual guidelines at `https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt`. Read the full guidelines. Resolve the tension between:
   - "limited use... for a private, educational purpose only" (the carveout)
   - "motorsport simulators and/or software that simulates auto racing... should not make any use of the FORMULA 1 Rights without an express written license" (the prohibition)

3. **Specific question**: does a browser game with authored F1 content (circuits, venues, races), used for private friends-only play, fall under the carveout or the prohibition? If ambiguous, what conditions would push it into each category?

4. **Output**: a short report (~200-400 lines) that either resolves the ambiguity or names the specific conditions of ambiguity that the canon's citation should address. Not a legal opinion — a factual reading of F1's own published guidelines.

5. **Chain integrity**: the lane must read Lane 1C's and Lane B4's treatment of the F1 guidelines and treat both as predecessors with contestable claims.

6. **Orientation**: standard (the question has an empirical answer from F1's actual text). If the question turns out to require interpretive judgment rather than just reading, the orientation may shift to investigatory mid-lane — the task spec should permit this.

7. **Dispatch duration**: ~15-20 min. Cheap. Foreground.

---

## 🔄 How To Resume Each Possible Next State

### Resume Path A: B7 then Wave 3

1. Write `wave-2-lane-b7-f1-legal-ambiguity-task-spec.md` per the design notes above.
2. Dispatch Opus general-purpose B7 foreground. Wait for output at `wave-2-lane-b7-f1-legal-ambiguity.md`.
3. Write `wave-3-synthesis-task-spec.md` per the design notes above, naming B7 as a predecessor alongside all Wave 1 and Wave 2 lanes.
4. Dispatch Opus gsdr-auditor Wave 3 synthesis foreground. Wait for output at `phase-01-prep-quality-scope-audit-2-output.md`.
5. Read the synthesis output, verify obligations addressed, report to user.

### Resume Path B: Direct to Wave 3 synthesis (no B7)

1. Write `wave-3-synthesis-task-spec.md` per the design notes above, naming all 7 Wave 1/2 lanes as predecessors but NOT B7. Add a specific instruction: "the F1 legal ambiguity from Lane 1C and Lane B4 must be preserved as a named unresolved tension; the synthesizer must NOT resolve it without evidence the lane outputs do not contain."
2. Dispatch Opus gsdr-auditor Wave 3 synthesis foreground.
3. Read synthesis output, verify, report.

### Resume Path C: User wants to read lane outputs before Wave 3

1. The user reads the Wave 1 and Wave 2 outputs themselves from disk.
2. User may give additional instructions (add a lane, change synthesis task spec shape, reframe the audit, etc.).
3. Continue based on user's instruction.

### Resume Path D: Reframe mid-audit

If the user decides (or a new finding surfaces) that the audit should be reframed, the reframe should be captured as a finding, not a reset. The lane outputs already on disk are valid artifacts — a reframe is a change in how they compose, not a reason to re-dispatch them.

---

## 🙈 Things This Handoff Might Be Wrong About

In the spirit of L1 and L5. This handoff was written by the same orchestrator whose task specs had 2-of-8 factual errors caught by Wave 1 Lane 1B. The reentry session should treat this handoff's claims as contestable:

- Any factual claim about file contents can be verified by opening the file
- Any claim about what a lane output said can be verified by reading the lane output
- Any claim about what the user decided can be verified by checking the conversation history (if accessible) or asking the user
- The "Emerging Audit Conclusion" section is explicitly the orchestrator's read, not the synthesizer's — it is a hypothesis for the synthesis to test, not a pre-decided outcome
- The handoff may have omitted important details from earlier in the session that the reentry session will only discover by asking the user or re-reading the conversation

**The reentry session should assume this handoff is ~90% reliable, verify the ~10% it's uncertain about, and treat any discrepancies between this handoff and the actual artifacts as findings about the handoff itself.**

---

## 📞 User Communication Norms Observed In This Session

- **User prefers quality over speed.** Rejected "loss of momentum" arguments explicitly at audit start. Wants the work done right.
- **User is technically engaged and corrects specific errors.** Caught the size-is-lazy framing mid-conversation. Noticed when the orchestrator dropped the metacomparison from Wave 2. Asked about model assignments specifically.
- **User wants model-class attribution of findings.** Explicitly asked earlier: "we should mark who is opus and who is sonnet so we can relate to and qualify their results / findings accordingly."
- **User pauses to check in at decision points.** Doesn't let the orchestrator run away on autopilot. Review gates are real.
- **User wants minimum token waste.** Explicitly asked to use `cp` + targeted edits rather than full file rewrites when creating the B2-Sonnet twin.
- **User wants qualified, conditional judgments** — not just approve/reject. The practical conclusion the audit produces should be actionable but honestly uncertain where uncertainty is warranted.
- **User's effort setting has bounced high/max** across the session, indicating they want deeper reasoning (not faster/shallower).

---

## 🔚 End Of Handoff

When you reach this line, you should have enough context to resume. Your immediate next action is **step 1 of "Immediate Next Actions"**: decide B7 vs direct-to-synthesis. If the user is available, ask them. If you're continuing autonomously, the orchestrator's recommended path was "B7 first, then synthesis."

**Good luck. The findings are substantive; the synthesis has enough to work with; the audit's practical conclusion is within reach.**

---

*Handoff authored: 2026-04-11, same session that ran Wave 1 and Wave 2. Claude Opus 4.6 (claude-code, 1M context). If this file becomes stale — if the findings change, if the user reframes, if new lane outputs appear — update it in place rather than creating a successor. Successor handoffs fragment continuity; the file can evolve.*
