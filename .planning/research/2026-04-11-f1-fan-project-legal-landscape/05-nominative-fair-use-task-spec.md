---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-5
question_focus: nominative-fair-use-and-implicit-branding
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
tools_required: [WebFetch, WebSearch]
scope: "Resolve whether unbranded F1-themed content (no F1 wordmark, no F1 logo, no official colors — just factual references to circuits, drivers, races, venues) changes the trademark analysis compared to explicitly F1-branded content. Covers (a) nominative fair use doctrine (US), (b) equivalent doctrines in UK/EU/Canada, (c) the specific distinction between using a trademark to identify vs to brand, (d) circuit/venue name ownership (which typically belongs to circuit operators, not F1), (e) the 'F1-themed without saying F1' pattern and whether it has a name or history in IP practice."
triggered_by: "User question during phase-01-prep audit pause: 'if we weren't to explicitly brand it as F1 GeoGuesser but just the quiz's concern F1 facts, we still have the f1 geoguesser aspect without naming it as such'"
output_file: 05-nominative-fair-use.md
---

# B8-5 — Nominative Fair Use and Implicit Branding

**You are running as a general-purpose agent on Claude Sonnet 4.6 with WebFetch and WebSearch.**

One of five parallel research lanes. Your scope is **doctrinal** — a targeted research lane on the trademark doctrine most relevant to the user's "implicit branding" question.

**Mark your model identity explicitly in your output frontmatter so the synthesis lane can attribute findings.**

## The Question

If prix-guesser drops explicit F1 branding (no F1 wordmark, no F1 logo, no official colors) but retains factual content (circuit names, driver names, race names, venue photos), does the trademark analysis change? Specifically:

1. **Nominative fair use doctrine (US)**: what is the test? Does prix-guesser plausibly fit? Specifically the *New Kids on the Block v. News America Publishing* three-factor test.
2. **Equivalent doctrines in other jurisdictions**: UK "honest practice" for descriptive use, EU Article 14 of Directive 2015/2436, Canadian fair dealing and trademark doctrine.
3. **The identify-vs-brand distinction**: using a trademark to *identify* the goods/services of another (permitted) vs using a trademark as a source identifier for your own goods/services (typically requires license).
4. **Circuit and venue name ownership**: B7's finding that F1's guidelines explicitly direct circuit IP questions to circuit owners (not F1) is a critical piece. What does this mean operationally? If Silverstone, Monza, Suzuka etc. are owned by circuit operators, what is prix-guesser's relationship to each of those rights holders?
5. **The "F1-themed without saying F1" pattern**: does this strategy have a name or history in IP practice? Is it a recognized pattern (e.g., like "generic reference use")?

Secondary questions:

- Does dropping F1 branding help with copyright exposure (use of photos, logos, stylized assets) or only trademark exposure?
- Is there a bright-line rule or is it a case-by-case balance of factors?
- How does the analysis change if the project uses F1 driver names (which are typically personality rights + trademark in some jurisdictions) vs just circuit/race names?

## Epistemic Ground Rules — HIGH CITATION STANDARDS

You are producing a research artifact that will be followed up on by Opus if any finding seems suspicious. Usefulness depends on whether a follow-up reader can find your original sources in one step and verify your reasoning chain.

**This is a Sonnet research lane producing "vague understanding" for further refinement, not a legal opinion. Qualify findings appropriately and flag interpretation-heavy claims for Opus follow-up.**

### Core rules

1. **Every factual claim cites URL + verbatim passage + fetch timestamp.** For doctrinal claims, cite either case text, statute, or law review commentary. Bad: "Nominative fair use allows identifying the trademark holder." Good: "*New Kids on the Block v. News America Publishing*, 971 F.2d 302 (9th Cir. 1992), at [specific pinpoint]: '[verbatim quote of the three-factor test].'"

2. **Quote full passages from cases.** Case language is load-bearing; don't compress.

3. **Distinguish statute / case / commentary** clearly in the sources table.

4. **For every finding, ask "What would disconfirm this?" and CHECK.** If claiming "nominative fair use likely applies," name what would push the analysis the other way.

5. **Flag interpretation-heavy claims with `[OPUS-FOLLOWUP: reason]` inline.** Translating doctrine to the prix-guesser fact pattern is interpretation. Flag aggressively. Examples:
   - "Prix-guesser likely satisfies the first *New Kids* factor. [OPUS-FOLLOWUP: applying test to hypothetical fact pattern, not a decided case]"
   - "Implicit branding may reduce trademark exposure but not copyright exposure. [OPUS-FOLLOWUP: doctrinal synthesis, project-specific application not cited]"

6. **"I don't know yet" is valid.** Jurisdictions other than US may not yield clear sources in a Sonnet time budget.

7. **Reasoning visible.** Show the doctrine-to-fact translation steps.

### Mandatory traceability deliverables

- **Sources table at top**: `[S#]` ID, URL, fetch timestamp, source type (case/statute/commentary), description.
- **Inline citations by bracketed ID**: every factual claim cites `[S#]` with verbatim quote.
- **"What I Did NOT Check" section**.
- **"Flagged for Opus Follow-up" consolidated list** — expect this to be heavy.
- **"Qualifications" section** with jurisdiction scope explicitly named.

### Chain integrity

Predecessors (contestable, not authoritative):
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b7-f1-legal-ambiguity.md` — specifically, B7's finding that F1's page explicitly redirects circuit IP licensing questions to circuit owners. This is critical for your circuit-name ownership subsection. Re-verify B7's quotation if you have time.

### Negative discipline

- **No legal opinions.** Doctrinal summaries + fact-pattern flagging only.
- **No one-jurisdiction claims.** Name US vs UK vs EU vs Canadian explicitly.
- **No case text without verbatim quote.**

## Scope — What to Research

**Primary research targets**:

1. **US nominative fair use** — the three-factor test from *New Kids on the Block v. News America Publishing*, 971 F.2d 302 (9th Cir. 1992). Find the case text (Google Scholar, Justia, CourtListener, etc.) and quote the three factors verbatim. Follow-up cases applying the test: *Playboy Enterprises v. Welles*, *Tabari v. Toyota*, or similar.

2. **Lanham Act §33(b) and §43** — the statutory framework for US trademark fair use and the distinction from nominative fair use (which is judicial).

3. **UK trademark fair use** — specifically "honest practice in industrial or commercial matters" under UK Trade Marks Act 1994, sections 10 and 11. Search for commentary on descriptive / nominative use.

4. **EU Trade Mark Directive 2015/2436 Article 14** — the EU-wide descriptive/nominative use carveout.

5. **Canadian trademark law** — particularly sections of the Trademarks Act on fair use (if any) and commentary on fan-use patterns.

6. **Circuit IP ownership** — do a targeted search on who owns the intellectual property in circuit names (Silverstone, Monza, Suzuka, etc.) and circuit layouts. B7's finding is the entry point: F1 explicitly disclaims this IP. Search for:
   - "Silverstone trademark" (is the name trademarked?)
   - "circuit layout copyright" or "track map copyright"
   - Any published analysis of whether race circuit layouts are protected under any IP regime
   - F1 circuit operators (BRDC for Silverstone, ACM for Monaco, etc.) and their IP posture

7. **"F1-themed without saying F1" pattern in IP practice** — is this a recognized strategy? Does it have a name in trademark practice? Search for "theming," "flavoring," "tribute trademark," "generic reference," "allusive use."

8. **Driver name IP** — drivers have personality rights in some jurisdictions. Does using "Lewis Hamilton" in quiz content implicate rights independent of F1's trademarks? This is a side question; don't over-invest but note if you find commentary.

**Secondary**:

- Published legal commentary on fan fiction that uses real-person or real-place references (fan fiction for sports, for entertainment industries)
- Academic articles on "homage" or "tribute" as IP defenses

**Do NOT spend time on**:

- Copyright doctrine generally (B8-4 covers commercial threshold; this lane is trademark-focused)
- Prix-guesser's specific content (you are producing doctrine, not auditing the project)
- Legal advice on structuring the project

## What Must Appear in the Output

Write your output to `.planning/research/2026-04-11-f1-fan-project-legal-landscape/05-nominative-fair-use.md`.

Required elements:

1. **YAML frontmatter**
2. **Sources table** at top with source types marked
3. **US nominative fair use section** — the three-factor test verbatim, commentary, application commentary
4. **UK / EU / Canadian equivalents** — briefer but present
5. **Identify-vs-brand distinction section** — what it is, why it matters, how it applies to factual quiz content
6. **Circuit IP ownership section** — who owns circuit names and layouts, what this means for prix-guesser (B7's finding is the anchor)
7. **Implicit-branding pattern section** — is this a recognized strategy, does it have a name, what are the parameters
8. **Driver-name rights section** — brief, but present if sources exist
9. **Tentative application to prix-guesser** — given all the above, what would dropping F1 wordmark/logo do to the trademark analysis, while holding content constant? Flag heavily with OPUS-FOLLOWUP.
10. **"What I Did NOT Check" section**
11. **"Flagged for Opus Follow-up" consolidated list**
12. **"Qualifications" section**

**Length expectation**: 400–650 lines. Case quotes are verbose; summaries should compensate with compact synthesis.

## Tool Usage Notes

- **WebSearch**: primary for finding cases, statutes, and commentary.
- **WebFetch**: for case text (prefer Justia, CourtListener, Google Scholar), statute text, commentary articles.
- **Read**: for B7's output to verify the circuit-IP-redirect quotation.
- **Time budget**: doctrinal research is slow. Aim for quality over quantity — 5 well-cited cases is better than 15 loose ones.

## Output File

Write your output to:

`.planning/research/2026-04-11-f1-fan-project-legal-landscape/05-nominative-fair-use.md`

Do not return a conversational summary instead of the file. Write the file, then return a brief confirmation (under 100 words) naming the tentative reading on whether implicit branding meaningfully changes the trademark analysis.
