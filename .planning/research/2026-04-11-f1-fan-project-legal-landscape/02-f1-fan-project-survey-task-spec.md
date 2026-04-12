---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-2
question_focus: f1-fan-project-survey
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
tools_required: [WebFetch, WebSearch]
scope: "Survey active F1-themed community fan projects (daily puzzles, quiz games, community bots, data tools) and catalog how each handles IP: branding choices, disclaimers, licensing disclosures, monetization models, operational posture. Produce a pattern finding across the catalog — what do most projects do, what do outliers do, and is any known enforcement history visible."
triggered_by: "User question during phase-01-prep audit pause: 'are there other f1-themed things that are not officially partnered?'"
output_file: 02-f1-fan-project-survey.md
---

# B8-2 — F1 Fan Project Survey

**You are running as a general-purpose agent on Claude Sonnet 4.6 with WebFetch and WebSearch.**

One of five parallel research lanes in the B8 research program. Your scope is **breadth over depth**: catalog many F1-themed community projects with enough detail per project to extract a pattern. Do not deep-read any single one (that's B8-1's job for BoxBoxd specifically).

**Mark your model identity explicitly in your output frontmatter so the synthesis lane can attribute findings.**

## The Question

What patterns emerge in how active F1 community fan projects handle IP? Specifically:

1. **Branding choices**: do they use F1 wordmark/logo explicitly, implicitly (just circuits/drivers/races), or not at all?
2. **Disclaimers**: do they display "unofficial" / "not affiliated" / "fan-made" language? Where?
3. **Licensing disclosures**: do any projects disclose an F1 licensing arrangement, or is the pattern uniform non-disclosure?
4. **Monetization**: ads, donations, subscriptions, Patreon/Ko-fi, nothing?
5. **Operational status**: are they active? archived? taken down? If archived/taken down, is there a stated reason?
6. **Pattern**: what's the modal behavior? What outliers exist?

The user wants to know whether F1 fan projects operate with formal partnerships (rare), tacit tolerance (common), or something else.

## Epistemic Ground Rules — HIGH CITATION STANDARDS

You are producing a research artifact that will be followed up on by Opus if any finding seems suspicious. Usefulness depends on whether a follow-up reader can find your original sources in one step and verify your reasoning chain.

**This is a Sonnet research lane producing "vague understanding" for further refinement, not a legal opinion. Qualify findings appropriately and flag interpretation-heavy claims for Opus follow-up.**

### Core rules

1. **Every factual claim cites URL + verbatim passage + fetch timestamp.** Bad: "F1DLE has a disclaimer." Good: "Fetched https://f1dle.com at 2026-04-11 [HH:MM] UTC; the footer contains: '[verbatim quote]'. This establishes disclaimer presence."

2. **Quote full sentences minimum.** For catalog entries, a single verbatim sentence per evidential claim is acceptable (this lane is breadth, not depth), but single-word or single-phrase quotes are not.

3. **For every finding, ask "What would disconfirm this?" and CHECK.** If claiming "most projects have no disclaimer," count the projects checked, count the ones with disclaimers, show the ratio, and name which pages you checked on each project. Absence claims require exhausted-search justification.

4. **Flag interpretation-heavy claims with `[OPUS-FOLLOWUP: reason]` inline.** Examples:
   - "This pattern suggests F1 tolerates daily-puzzle fan projects. [OPUS-FOLLOWUP: inferred from operational survival, not enforcement documentation]"
   - "The monetization model is likely donation-driven. [OPUS-FOLLOWUP: based on Ko-fi link, not operator statement]"
   Flag at point of writing.

5. **"I don't know yet" is valid.** If a project is sparse or its key pages don't load, report the negative result and move on.

6. **Reasoning visible.** When you identify a pattern, show the underlying catalog entries that support it.

### Mandatory traceability deliverables

- **Sources table at top**: `[S#]` ID, URL, fetch timestamp, one-sentence description.
- **Per-project entries with inline citations**: every claim about a project cites at least one `[S#]` source with verbatim quote.
- **"What I Did NOT Check" section**: projects you could have cataloged but didn't, and why.
- **"Flagged for Opus Follow-up" consolidated list**: every OPUS-FOLLOWUP marker collected.
- **"Qualifications" section**: "as of fetch date", "catalog is partial", "only public-facing pages checked", etc.

### Chain integrity

Predecessors (contestable, not authoritative):
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md` — found F1DLE, Formudle, Stewardle mentioned as "operating publicly without takedowns." Verify and extend.
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b7-f1-legal-ambiguity.md` — established F1's actual guidelines text; your findings should note how each project's operational reality relates to F1's stated policy.

Lane 1C's "operating without takedowns" claim is contestable. Verify each project's operational status directly.

### Negative discipline

- **No legal opinions.** Empirical observations only.
- **No cherry-picked patterns.** If the catalog is mixed, report the mix; don't smooth it into a clean pattern.
- **No loose-citation consolidation.** Per-project entries keep citations separate.

## Scope — Target Project Set

**Primary catalog targets** (try to find and fetch each):

1. **F1DLE** — daily F1 driver guessing game (Wordle-variant shape)
2. **Formudle** — daily F1 driver guessing game
3. **Stewardle** — daily F1 steward/penalty game (or similar)
4. **Driverle** — driver guessing variant
5. **Who Are Ya?** (sometimes "WhoAreYa" or "whoareya.com") — driver guessing game
6. **Gridle** — grid-prediction or related
7. **F1Guessr** or **F1 Guessr** — if it exists
8. **F1 Game of Life** / **F1 Geography games** — GeoGuessr-style F1 projects
9. **Fastf1** ecosystem — is the Python library's README / website relevant?
10. **Any r/formula1 community projects** — check Reddit for recurring community project posts

**Secondary targets** (add if time permits and the primary set has gaps):

- F1-themed Discord bots (typically hard to catalog without joining servers — report if you find public documentation)
- F1 data dashboards and analytics tools (Fastf1-based projects, lap time comparison tools)
- F1 prediction leagues (community-run, not the official game)

**Do NOT spend time on**:

- BoxBoxd (B8-1 covers this specifically)
- Official F1 products (F1.com, F1 Fantasy official, F1 TV, Formula 1 Clash, F1 Mobile Racing, F1 Manager — these are licensed)
- Commercial F1 betting products
- iRacing / rFactor / Assetto Corsa F1 mods (simulator mods are a different category — they're explicitly inside F1's simulator clause)

## Per-Project Cataloging Protocol

For each project you find, produce a compact catalog entry:

```
### [Project Name] [S#]

- **URL**: [verified URL with fetch timestamp]
- **What it is**: [one sentence describing content/mode, citing the project's own self-description]
- **Operational status**: [active / archived / 404 / unreachable], with evidence
- **Branding**: [F1 wordmark/logo used? circuits/drivers referenced? colors match F1?] — verbatim quote evidence
- **Disclaimer**: [present / absent / partial], where, verbatim quote if present
- **Licensing disclosure**: [present / absent], verbatim quote if present
- **Monetization**: [ads / donations / subscriptions / nothing visible], verbatim quote or URL of payment link
- **Operator identity**: [disclosed / not disclosed], verbatim quote if disclosed
- **Notes**: anything else notable, with citations
```

Compact is fine — this is a catalog, not a series of essays. Budget roughly 20-30 lines per project entry.

## What Must Appear in the Output

Write your output to `.planning/research/2026-04-11-f1-fan-project-legal-landscape/02-f1-fan-project-survey.md`.

Required elements:

1. **YAML frontmatter** identifying the lane, model, agent type, fetch date, output path
2. **Sources table** at top (this will be large given breadth scope — that's fine)
3. **Catalog section** — per-project entries per the template above
4. **Pattern analysis section** — what does the catalog show? What do most projects do? What outliers exist? What's the ratio of projects with/without disclaimers, with/without monetization, etc.?
5. **Enforcement history subsection** — have any of these projects been taken down, cease-and-desisted, or publicly pressured by F1? Search for any public record of such actions.
6. **Cross-reference to F1's guidelines** — given B7's finding that F1's text prohibits third-party games and apps using F1's Other IP Rights, how does the operational reality of these projects compare to the policy text? Flag with OPUS-FOLLOWUP.
7. **"What I Did NOT Check" section** — projects you heard of but couldn't find, catalog scope limits
8. **"Flagged for Opus Follow-up" consolidated list**
9. **"Qualifications" section**

**Length expectation**: 300–600 lines depending on how many projects the catalog surfaces. If the catalog is large, the pattern section can be compact. If the catalog is small, the pattern section needs to show why the sample was small (honest exploration, not failure).

## Tool Usage Notes

- **WebSearch**: primary tool for finding projects. Search for each named target and note what surfaces.
- **WebFetch**: once you have a URL, fetch the homepage + footer + about page if one exists. Don't over-fetch — catalog depth, not essay depth.
- **Read**: for the three predecessor lanes, only if you need a cross-reference.
- **Time budget**: this is a breadth lane. Aim for 10+ projects cataloged. If fewer than 5 projects surface, the catalog section is thin — document why.

## Output File

Write your output to:

`.planning/research/2026-04-11-f1-fan-project-legal-landscape/02-f1-fan-project-survey.md`

Do not return a conversational summary instead of the file. Write the file, then return a brief confirmation (under 100 words) naming the central pattern finding.
