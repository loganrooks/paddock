---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-4
question_focus: donation-commercial-threshold
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
tools_required: [WebFetch, WebSearch]
scope: "Resolve the specific question of whether accepting donations to cover server/hosting costs crosses the 'commercial use' threshold, under (a) F1's own guidelines text, (b) US trademark/copyright doctrine on 'commercial use,' (c) UK fair dealing doctrine on 'commercial purpose,' and (d) any published legal commentary specifically addressing Patreon/Ko-fi/GitHub Sponsors as fan-project funding mechanisms."
triggered_by: "User question during phase-01-prep audit pause: 'if we aren't commercializing but merely monetizing in a donation capacity to keep servers running, would this be violating anything?'"
output_file: 04-commercial-threshold.md
---

# B8-4 — Commercial/Non-Commercial Threshold Research

**You are running as a general-purpose agent on Claude Sonnet 4.6 with WebFetch and WebSearch.**

One of five parallel research lanes. Your scope is **doctrinal and textual**: the question is specifically about whether donations-for-server-costs cross the "commercial use" line. This is simultaneously a question about F1's own policy text, general IP doctrine, and published legal commentary on fan-project funding.

**Mark your model identity explicitly in your output frontmatter so the synthesis lane can attribute findings.**

## The Question

If prix-guesser accepts donations (Patreon, Ko-fi, GitHub Sponsors, or similar) to cover server and hosting costs — no profit, purely cost recovery — does this count as "commercial use" under:

1. **F1's own guidelines** (the page at https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt that B7 analyzed)? F1's carveout requires "non-commercial" — is cost-recovery donation consistent with this?
2. **US copyright/trademark doctrine**? The US Copyright Act §107 fair-use factor includes "commercial or nonprofit educational purposes" — is cost-recovery donation "commercial"?
3. **UK fair dealing**? UK law has a "commercial purpose" threshold for some fair dealing defenses — is cost-recovery donation "commercial"?
4. **Published legal commentary on fan-project funding**? Have any legal analysts specifically addressed Patreon/Ko-fi/donation-funded fan projects and whether they cross the commercial line?

Secondary questions:

- Is there a legal or doctrinal distinction between (a) soliciting donations and (b) receiving unsolicited donations?
- Does the legal analysis change if donations exceed server costs (profit above break-even)?
- Does trademark "commercial use" and copyright "commercial use" mean the same thing? (Hint: they often don't.)

## Epistemic Ground Rules — HIGH CITATION STANDARDS

You are producing a research artifact that will be followed up on by Opus if any finding seems suspicious. Usefulness depends on whether a follow-up reader can find your original sources in one step and verify your reasoning chain.

**This is a Sonnet research lane producing "vague understanding" for further refinement, not a legal opinion. Qualify findings appropriately and flag interpretation-heavy claims for Opus follow-up.**

### Core rules

1. **Every factual claim cites URL + verbatim passage + fetch timestamp.** For doctrinal claims, cite either (a) statutory text, (b) a published legal commentary, or (c) a court case. Do not rely on general "legal websites say" summaries without naming the specific source. Bad: "US law says donation funding is non-commercial." Good: "Copyright.gov's fair-use page at [URL] states: '[verbatim passage about commercial use factor].' Additionally, [specific law review article at URL] argues: '[verbatim passage on donation-funded fan works].'"

2. **Quote full sentences minimum; full paragraphs for doctrinal nuance.** Legal text is particularly sensitive to compression distortion.

3. **Distinguish statute / case law / commentary.** These are different kinds of sources with different authority levels. Do not conflate.

4. **For every finding, ask "What would disconfirm this?" and CHECK.** If claiming "donation funding is widely considered non-commercial," check whether any legal commentary disagrees or whether courts have found otherwise.

5. **Flag interpretation-heavy claims with `[OPUS-FOLLOWUP: reason]` inline.** Legal doctrine translated to a specific fact pattern is almost always interpretation. Flag aggressively. Examples:
   - "This suggests prix-guesser's donation model is likely non-commercial. [OPUS-FOLLOWUP: applying doctrine to fact pattern, not a cited conclusion; lawyer follow-up required for production decision]"
   - "F1's 'non-commercial' condition appears to be broader than US copyright 'commercial use.' [OPUS-FOLLOWUP: doctrinal synthesis, single-source]"

6. **"I don't know yet" is valid.** If the doctrinal question doesn't yield clear sources, report the negative result.

7. **Reasoning visible.** When you translate doctrine to the prix-guesser fact pattern, show the translation steps.

### Mandatory traceability deliverables

- **Sources table at top**: `[S#]` ID, URL, fetch timestamp, source type (statute/case/commentary/policy), description.
- **Inline citations by bracketed ID**: every factual claim cites `[S#]` with verbatim quote.
- **"What I Did NOT Check" section**: jurisdictions, doctrines, cases you didn't engage.
- **"Flagged for Opus Follow-up" consolidated list**.
- **"Qualifications" section**: particularly note US-vs-UK jurisdiction scope, since the doctrines differ meaningfully.

### Chain integrity

Predecessors (contestable, not authoritative):
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b7-f1-legal-ambiguity.md` — B7 fetched F1's guidelines and found no definition of "commercial" in F1's text. Verify. B7 also surfaced that F1's carveout conditions include "justified, limited, and non-commercial." Your lane's core task is understanding what each of those conditions means operationally, particularly "non-commercial."

B7's re-fetch is recent and thorough; you may rely on B7's verbatim quotations unless your targeted re-read reveals additional "commercial"-related passages B7 didn't highlight. **Do a targeted second fetch of F1's guidelines specifically for commercial-related language** — B7 was broader-focused.

### Negative discipline

- **No legal opinions.** Doctrinal summaries + fact-pattern flagging only. Every sentence that reads like advice must be rephrased as an observation + OPUS-FOLLOWUP marker.
- **No one-jurisdiction claims.** Explicitly note whether each source is US, UK, EU, or other. The project owner is in Canada (per environmental context), so Canadian doctrine is also relevant if accessible.
- **No statutory text without verbatim quote.** If you cite §107 or any statute, quote the relevant subsection verbatim.

## Scope — What to Research

**Primary research targets**:

1. **F1's guidelines, targeted re-fetch for commercial language** (same URL as B7: https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt). Specifically search for:
   - "commercial" and "non-commercial"
   - "profit" or "non-profit"
   - "donation" or "gift"
   - "free" or "unpaid"
   - Any other language that scopes what "non-commercial" means in F1's framing
   - B7's quoted educational carveout contains "justified, limited, and non-commercial" — your lane defines the third condition

2. **US 17 USC §107 (fair use) text and commentary** — specifically the first factor, "the purpose and character of the use, including whether such use is of a commercial nature or is for nonprofit educational purposes." Fetch the statute text from copyright.gov or law.cornell.edu. Fetch major legal commentary on how this factor applies to donation-funded works (if available).

3. **UK Copyright, Designs and Patents Act 1988** — fair dealing provisions, specifically sections addressing commercial vs non-commercial. The 2014 amendments added "non-commercial research" as a defense.

4. **Canadian Copyright Act fair dealing** — if accessible, since the project owner is Canadian.

5. **Legal commentary on Patreon/Ko-fi/donation-funded fan works**. Search for:
   - Law review articles
   - Legal blogs (including the odinlaw.com piece Lane 1C cited)
   - Electronic Frontier Foundation (EFF) commentary
   - Academic commentary on fan fiction economics and IP

6. **Case law, if accessible** — any reported case involving a donation-funded fan project and an IP holder's challenge to it. This is the highest-authority source if findable, but may not surface in a Sonnet time budget.

**Secondary targets**:

- The distinction between trademark "commercial use" (likelihood of confusion in trade) and copyright "commercial" (factor in fair use analysis)
- The "nominal consideration" doctrine (if you incidentally encounter it)
- EU law on "non-commercial" — since many fan projects have international reach

**Do NOT spend time on**:

- Specific F1 fan projects (other lanes)
- Legal advice on how to structure donations (out of scope)
- Tax law or business structure (out of scope)

## What Must Appear in the Output

Write your output to `.planning/research/2026-04-11-f1-fan-project-legal-landscape/04-commercial-threshold.md`.

Required elements:

1. **YAML frontmatter**
2. **Sources table** at top with source type clearly marked
3. **F1 guidelines re-read section** — targeted second read for commercial-related language, with verbatim quotes and comparison to B7's earlier findings
4. **US doctrine section** — §107 text, commercial-use factor commentary, any applicable cases
5. **UK doctrine section** — CDPA 1988 fair dealing, commercial purpose threshold
6. **Canadian doctrine section** — if findable
7. **Legal commentary section** — published analysis of donation-funded fan projects specifically
8. **Synthesis section** — how these sources compose into a tentative reading of whether cost-recovery donations cross the commercial line, for each jurisdiction's doctrine and for F1's own policy
9. **Trademark vs copyright "commercial" distinction** — subsection explicitly addressing this, since they often differ
10. **"What I Did NOT Check" section**
11. **"Flagged for Opus Follow-up" consolidated list** — this lane will likely be heavy on OPUS-FOLLOWUP flags because doctrine-to-fact translation is almost always interpretation
12. **"Qualifications" section** with explicit jurisdiction scope, "not legal advice" disclaimer, source types

**Length expectation**: 400–700 lines. Doctrinal research is dense but compact; flag heavy, synthesize lightly.

## Tool Usage Notes

- **WebSearch**: primary for finding commentary sources.
- **WebFetch**: for statute text (copyright.gov, legislation.gov.uk), commentary articles, F1 guidelines re-fetch.
- **Read**: for B7's output if you need to verify its "no commercial definition in F1's text" claim.
- **Time budget**: be deliberate — doctrinal research rewards slow careful reading. Aim for 8–15 well-sourced citations across jurisdictions, not 30+ loose ones.

## Output File

Write your output to:

`.planning/research/2026-04-11-f1-fan-project-legal-landscape/04-commercial-threshold.md`

Do not return a conversational summary instead of the file. Write the file, then return a brief confirmation (under 100 words) naming the tentative reading on whether cost-recovery donations cross the commercial threshold.
