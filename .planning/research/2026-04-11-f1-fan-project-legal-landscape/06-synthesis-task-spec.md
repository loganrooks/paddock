---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-synthesis
question_focus: compose-all-5-research-lanes
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
tools_required: [Read, Grep, Glob]
scope: "Compose the 5 B8 research lane outputs (B8-1 BoxBoxd, B8-2 F1 fan survey, B8-3 analogous fan projects, B8-4 commercial threshold, B8-5 nominative fair use) into a practical answer to the user's questions: (a) legal conclusions and consequences for prix-guesser, (b) whether donation-based cost recovery counts as 'commercial' under F1's policy and general doctrine, (c) whether implicit F1 branding changes the analysis, (d) what BoxBoxd is doing (legal posture + game modes + differentiation surface), (e) what the broader F1 fan project landscape looks like, (f) what analogous domains tell us. Produces a synthesis that the user can use for both legal posture decisions and competitive differentiation decisions. Consolidates every OPUS-FOLLOWUP flag from the 5 lanes into a single list the user can route to future Opus dispatches."
triggered_by: "B8 research program synthesis dispatch after all 5 research lanes complete"
predecessor_lanes:
  - 01-boxboxd-deep-read.md
  - 02-f1-fan-project-survey.md
  - 03-analogous-fan-projects.md
  - 04-commercial-threshold.md
  - 05-nominative-fair-use.md
output_file: 06-synthesis.md
---

# B8 — Research Program Synthesis

**You are running as a general-purpose agent on Claude Sonnet 4.6. You do not need WebFetch or WebSearch — all web research was done by the 5 predecessor lanes. Your tools are Read, Grep, Glob.**

You are composing the outputs of 5 parallel research lanes into a single practical answer for the project owner. The research program was triggered by the user's questions during the pause of a separate audit about prix-guesser's Phase 01 preparatory work. The user explicitly asked for (a) legal conclusions and consequences, (b) whether donation-based cost recovery crosses the commercial line, (c) whether implicit branding changes the analysis, (d) what BoxBoxd is and how prix-guesser differs from it, and (e) broader landscape patterns.

**Mark your model identity explicitly in your output frontmatter.**

**Important note on your tool set**: you do NOT fetch any new web content. Your job is to compose and cross-reference what the 5 lanes already produced. If a predecessor lane left a gap, name it; do not fill it with new fetches.

## The Questions to Answer

Reproduced verbatim from the user's original question (for grounding):

> "What are the legal conclusions and consequences for our application? If we aren't commercializing but merely 'monetizing' in a donation capacity to keep servers running, would this be violating anything? And if we weren't to explicitly brand it as F1 GeoGuesser but just the quiz's concern F1 facts, we still have the 'f1 geoguesser' aspect without naming it as such. also like, what about BoxBoxd.com? that is entirely F1 Themed yet doesn't explicitly brand themselves as such I don't think. Or do they? Like do they have some legal arrangement with F1? and are there other 'f1-themed' things that are not officially partnered?"

And the follow-up expansion about BoxBoxd:

> "boxboxd is such a good reference design that we also need to differentiate ourselves from. https://boxboxd.fun/home also I screwed up and its .fun. im curious about its history and what not too. how and when did it come to be? the different game modes etc. because they have the Connections game from NYT but for F1 too! They are doing a similar idea X but for F1, and so we really need to differentiate ourselves from them."

The synthesis must answer each of these questions with grounding in the lane outputs. Questions the synthesis must address explicitly:

1. **Legal conclusions and consequences** for prix-guesser as currently scoped (private, friends-only, no donations yet) — what does the research landscape actually say about the operational risk posture?
2. **Donation / cost-recovery threshold** — does accepting donations to cover servers count as "commercial" under F1's policy and general IP doctrine? Jurisdiction-aware (US / UK / Canadian) if the doctrine differs.
3. **Implicit vs explicit branding** — does dropping the F1 wordmark and logo but keeping circuit/driver/race content meaningfully change the trademark analysis?
4. **BoxBoxd specifically**:
   - Legal posture (does it disclose licensing? disclaimers? monetization?)
   - Product shape (complete game mode inventory, history, community features)
   - Differentiation surface: where does prix-guesser's anchor (authored GeoGuessr-style F1 geography rounds for friends-on-couch/private-room play) differ from BoxBoxd's current offerings?
5. **Broader F1 fan project landscape** — what's the pattern across all active community F1 fan projects? What is the modal posture (branding, disclaimers, monetization, operational survival)?
6. **Analogous domains** — what do Nintendo, Marvel, NFL, Star Wars, other motorsports fan-project histories tell us about how IP holders actually behave toward fan projects and what triggers enforcement?

## Epistemic Ground Rules — HIGH CITATION STANDARDS

**This is a Sonnet synthesis lane producing "vague understanding" for further refinement, not a legal opinion. Preserve all predecessor-lane OPUS-FOLLOWUP flags and add your own for any new interpretive synthesis.**

### Core rules

1. **Every factual claim cites a predecessor lane output file + section + specific passage.** Bad: "Multiple F1 fan projects operate without disclaimers." Good: "Per `02-f1-fan-project-survey.md` section 'Pattern analysis', lines [N–M]: '[verbatim passage]'. This pattern is supported by [N] of the [M] cataloged projects listed in the Catalog section of that file."

2. **Quote full passages when composing across lanes.** When stating "B8-4 found X and B8-5 found Y, which compose into Z," quote the relevant passage from each lane and show the composition reasoning.

3. **Preserve all OPUS-FOLLOWUP flags from predecessor lanes.** Every OPUS-FOLLOWUP marker in a lane output must be carried into your synthesis — either by copying it verbatim with its source lane attribution, or by resolving it (e.g., "B8-4 flagged this for Opus follow-up because [X]; the composition with B8-5 resolves the flag because [Y]" — and show the reasoning).

4. **Add your own OPUS-FOLLOWUP flags for synthesis-level interpretations.** When you compose across lanes, the composition itself is often interpretation. Flag those interpretations. Example: "B8-1 shows BoxBoxd has mode X; B8-3 shows that monetization-free fan projects with high polish generally survive. Composition: BoxBoxd's operational survival is consistent with the tolerated-high-polish pattern. [OPUS-FOLLOWUP: cross-lane composition, not a single-lane finding]"

5. **For every synthesis claim, ask "What would disconfirm this?" and check across lanes.** If B8-2 says X and B8-3 says something that could contradict X, surface the contradiction before papering over it.

6. **"The evidence does not resolve this" is a valid finding.** The 5 lanes may not give you enough to answer every question confidently. When they don't, say so.

7. **Reasoning visible.** When you compose across lanes, show the composition steps — which lane contributed what, what reasoning bridges the contributions.

### Mandatory traceability deliverables

- **Lane-output sources table at top**: `[L1]` through `[L5]` + path + one-sentence description of each lane's scope. Plus any cross-referenced files (e.g., predecessor audit lanes) with their own IDs.
- **Inline citations by bracketed ID**: every synthesis claim cites `[L1]`, `[L2]`, etc., with the specific section or line range inside the lane output.
- **"What the Research Program Did NOT Cover" section**: the union of each lane's "What I Did NOT Check" section, plus anything the synthesis itself noticed was not covered by any lane.
- **"Consolidated OPUS-FOLLOWUP list"**: every flag from all 5 lanes, plus your synthesis-level flags, organized into:
  - Legal follow-ups (for future Opus dispatches on legal doctrine)
  - Competitive/Product follow-ups (for future dispatches on differentiation)
  - Empirical follow-ups (for future dispatches on landscape/enforcement history)
- **"Qualifications" section**: inherited qualifications from each lane + synthesis-level qualifications (jurisdiction scope, time-pinned currency, research-program partiality)

### Chain integrity

**The 5 research lanes are predecessors. Every load-bearing claim from a lane that you incorporate into your synthesis must be attributed to that lane and, if possible, spot-checked by opening the lane file at the cited section.** The lanes are not infallible — each is Sonnet research under a Sonnet time budget. If your synthesis surfaces a contradiction between two lanes, surface it as a finding.

Cross-reference to the original audit chain:
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md` — original source of the F1 legal framing
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b4-f1-legal-carveout-citation.md` — canon check
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b7-f1-legal-ambiguity.md` — the most thorough predecessor for F1's actual text; B7 surfaced the Games/Apps/Simulator prohibitions and the "educational" ambiguity

These are the audit-chain predecessors. The B8 research program was triggered to extend beyond them. Your synthesis should not re-litigate what the audit chain already established but should layer the B8 lanes' new findings on top.

### Negative discipline

- **No legal opinions.** The synthesis composes research into a practical reading for the project owner's decision-making; it is not legal advice.
- **No manufactured certainty.** If the evidence is mixed, report the mix.
- **No smoothed-over contradictions.** If two lanes disagree, name the disagreement and route to Opus.
- **No strategic recommendations.** Observations about differentiation surface, yes. "Prix-guesser should do X" — no. The user makes strategic decisions from the raw material you produce.

## What Must Appear in the Synthesis Output

Write your output to `.planning/research/2026-04-11-f1-fan-project-legal-landscape/06-synthesis.md`.

Required elements:

1. **YAML frontmatter** identifying the synthesis, model, date, predecessor lanes
2. **Lane sources table** at top
3. **TL;DR for the project owner** (6–12 bullets): the headline findings across all 5 lanes and the synthesis, organized by user-question
4. **Question 1 — Legal conclusions and consequences for prix-guesser (as currently scoped)**:
   - Composing findings from B8-4 (commercial threshold), B8-5 (nominative fair use), and the audit predecessors (B7 specifically)
   - What is the realistic operational risk posture for prix-guesser as a private-only, no-donations, friends-on-couch fan game?
   - What are the specific risks if the scope expands (public hosting, donations, broader distribution)?
   - OPUS-FOLLOWUP every doctrinal-to-fact translation
5. **Question 2 — Donation-based cost recovery and the "commercial" threshold**:
   - Composing B8-4 findings
   - F1's text (does it define "commercial"? does "non-commercial" contemplate cost recovery?)
   - US, UK, Canadian doctrine on commercial use
   - Trademark vs copyright "commercial" distinction
   - Published commentary on Patreon/Ko-fi-funded fan projects
   - Tentative reading on whether cost-recovery donations cross the line, with heavy OPUS-FOLLOWUP
6. **Question 3 — Implicit vs explicit F1 branding**:
   - Composing B8-5 findings
   - Nominative fair use doctrine
   - The identify-vs-brand distinction
   - Circuit/venue IP ownership (B7's finding that F1 disclaims circuit IP)
   - What dropping F1 wordmark/logo would change while content stays constant
7. **Question 4 — BoxBoxd: legal posture, product shape, and differentiation surface**:
   - Composing B8-1's dual-dimension findings
   - Legal: does BoxBoxd disclose/disclaim? how does it monetize?
   - Product: complete game mode inventory, history, product shape
   - Differentiation: where does prix-guesser's anchor (authored GeoGuessr-for-F1-places, private-room party shape) overlap with or diverge from BoxBoxd's offerings?
   - Specifically: does BoxBoxd already have a GeoGuessr-style mode? If yes, on what axes can prix-guesser still differentiate? If no, that's prix-guesser's clearest differentiation surface.
8. **Question 5 — Broader F1 fan project landscape**:
   - Composing B8-2's catalog and pattern findings
   - Modal posture of F1 fan projects (branding, disclaimers, monetization, operational survival)
   - Is there any known F1 enforcement history against community fan projects?
9. **Question 6 — What analogous domains teach us**:
   - Composing B8-3's case findings
   - Enforcement triggers (commercial polish, scale, branding visibility, competing-with-official, donation polarization)
   - The donation-specific pattern: does accepting donations itself trigger enforcement in other domains?
   - Relevance to F1: what should we expect from F1 given the pattern from other IP holders?
10. **Cross-lane synthesis findings** — findings that only emerge when you compose across lanes (e.g., "B8-3 shows pattern X in other domains, B8-2 shows pattern Y in F1 fan projects, compose to Z about what's likely true of F1's posture")
11. **"Does B8 change the Phase 01 audit's practical conclusion?"** section — briefly: does anything the B8 program surfaced change what the paused Wave 3 audit synthesis should conclude about prix-guesser's Phase 01 readiness? (The user may fold B8 findings into the audit or keep them separate — answer both paths briefly.)
12. **"What the Research Program Did NOT Cover" section**
13. **"Consolidated OPUS-FOLLOWUP list"** (Legal / Competitive-Product / Empirical subgroups)
14. **"Qualifications" section**

**Length expectation**: 600–1000 lines. This is composition work across 5 lane outputs totaling ~2000–3500 lines of research. Compression ratio of ~1/3 to ~1/5 is reasonable.

## Tool Usage Notes

- **Read**: primary tool. Read each of the 5 lane outputs in full before composing. Open each at the specific section when citing it.
- **Grep**: use to find all OPUS-FOLLOWUP markers across the 5 files for the consolidated list.
- **Glob**: to verify file paths.
- **WebFetch / WebSearch**: **DO NOT USE**. Synthesis is composition only. If a predecessor lane left a gap, name it — do not fill it with new fetches.
- **Bash**: avoid.

## Output File

Write your output to:

`.planning/research/2026-04-11-f1-fan-project-legal-landscape/06-synthesis.md`

Do not return a conversational summary instead of the file. Write the file, then return a brief confirmation (under 200 words) naming the four headline findings:
1. Legal posture for prix-guesser (as currently scoped)
2. Donation threshold reading (with jurisdiction caveats)
3. BoxBoxd differentiation surface (one concrete axis)
4. Whether B8 findings change the audit's practical conclusion
