---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-3
question_focus: analogous-fan-projects-other-domains
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
tools_required: [WebFetch, WebSearch]
scope: "Survey fan-project precedents in other IP-heavy domains (Nintendo/Pokemon, Marvel/DC, Star Wars, NFL/NBA/Premier League, other motorsports, Disney, Harry Potter) to extract patterns about (a) what kinds of fan projects get cease-and-desisted vs tolerated, (b) donation-funded fan projects specifically and their legal histories, (c) what branding/disclaimer/monetization strategies have been tested and what happened to them."
triggered_by: "User question during phase-01-prep audit pause: 'we could potentially look at other related / analogous cases, products, situations as well'"
output_file: 03-analogous-fan-projects.md
---

# B8-3 — Analogous Fan Projects in IP-Heavy Domains

**You are running as a general-purpose agent on Claude Sonnet 4.6 with WebFetch and WebSearch.**

One of five parallel research lanes. Your scope is **comparative**: F1 is not the only IP-heavy domain where fan projects exist. Nintendo/Pokemon, Marvel/DC, Star Wars, major sports leagues, and other motorsports all have rich fan-project ecosystems with known enforcement histories. Patterns from these domains inform the F1 case.

**Mark your model identity explicitly in your output frontmatter so the synthesis lane can attribute findings.**

## The Question

What can fan-project precedents from other IP-heavy domains tell us about:

1. **What kinds of fan projects get cease-and-desisted vs. tolerated?** The pattern is not random; there are signals (content type, monetization, scale, branding visibility).
2. **How do donation-funded fan projects fare legally?** Are there precedents where a project accepted Patreon/Ko-fi support and was (a) tolerated, (b) taken down, (c) forced to change its funding model?
3. **Does the "implicit branding" strategy (don't use the IP holder's logo/wordmark but use other protected content) change how IP holders respond?**
4. **Are there documented cases where a rights-holder tolerated fan activity under specific conditions and enforced when those conditions broke?** (E.g., "we tolerate free private use but not commercial or publicly-promoted use.")

## Epistemic Ground Rules — HIGH CITATION STANDARDS

You are producing a research artifact that will be followed up on by Opus if any finding seems suspicious. Usefulness depends on whether a follow-up reader can find your original sources in one step and verify your reasoning chain.

**This is a Sonnet research lane producing "vague understanding" for further refinement, not a legal opinion. Qualify findings appropriately and flag interpretation-heavy claims for Opus follow-up.**

### Core rules

1. **Every factual claim cites URL + verbatim passage + fetch timestamp.** Historical cases (e.g., "Pokemon Uranium was taken down in 2016") need a primary source — the creator's public statement, a news article quoting Nintendo, a court filing, etc. Bad: "Nintendo is aggressive about fan games." Good: "[Verbatim quote from news article at URL dated X, describing the specific enforcement action taken against Pokemon Uranium]."

2. **Distinguish primary from secondary sources.** A news article reporting on a takedown is secondary; the creator's statement or the legal notice itself is primary. Prefer primary where available; flag secondary-only sourcing.

3. **For every finding, ask "What would disconfirm this?" and CHECK.** If claiming "donation-funded fan projects generally get taken down," name counter-examples you checked (donation-funded projects that survived). Patterns require both sides.

4. **Flag interpretation-heavy claims with `[OPUS-FOLLOWUP: reason]` inline.** Examples:
   - "This pattern suggests Nintendo enforces most aggressively on projects that approach commercial polish. [OPUS-FOLLOWUP: pattern extraction from ~5 cases, not systematic]"
   - "The absence of enforcement here may indicate tacit tolerance. [OPUS-FOLLOWUP: inference from operational survival, not direct statement]"
   Flag at point of writing.

5. **"I don't know yet" is valid.** Not every question yields to web search in a Sonnet time budget. If you can't find a documented case matching a question, say so.

6. **Reasoning visible.** When you extract a pattern from multiple cases, show the cases and the extraction reasoning.

### Mandatory traceability deliverables

- **Sources table at top**: `[S#]` ID, URL, fetch timestamp, description.
- **Inline citations by bracketed ID**: every factual claim cites `[S#]` with verbatim quote.
- **"What I Did NOT Check" section**: cases you heard of but couldn't verify, domains you didn't touch.
- **"Flagged for Opus Follow-up" consolidated list**.
- **"Qualifications" section**.

### Chain integrity

Predecessors (contestable, not authoritative):
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md` — specifically LQ-1C.4 Finding 2 cited odinlaw.com on fan-game legal risks. Verify and extend.
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b7-f1-legal-ambiguity.md` — for contrast with F1's specific policy text.

### Negative discipline

- **No legal opinions.** Case summaries + OPUS-FOLLOWUP markers only.
- **No over-generalization.** If you find 3 Pokemon cases, don't claim "Nintendo always enforces like this." Name the sample.
- **No loose synthesis.** Per-case citations kept separate from pattern claims.

## Scope — Target Domains and Cases

**Primary domains to survey**:

1. **Nintendo / Pokemon fan projects** — perhaps the most documented enforcement history. Known cases: AM2R (Another Metroid 2 Remake), Pokemon Uranium, Pokemon Prism, Pokemon Reborn, Pokemon Revolution Online, Chrono Resurrection, Project M. Famous for aggressive C&Ds.

2. **Nintendo / Mario / Zelda fan projects** — Super Mario 64 PC port, Zelda Breath of the Wild PC, Mario Maker community content, romhacks.

3. **Marvel / DC fan games and animations** — fan games, fan-made trailers, enforcement patterns.

4. **Star Wars fan projects** — Disney's stance post-acquisition vs. Lucasfilm's earlier stance. Fan films tolerated; fan games more mixed.

5. **Harry Potter fan projects** — Hogwarts fan games, text adventures.

6. **Major sports leagues**: NFL, NBA, MLB, Premier League, La Liga, FIFA. Community tools, data dashboards, fantasy alternatives. Known enforcement history (especially NFL and its aggressive brand protection).

7. **Other motorsports**: Formula E, IndyCar, NASCAR, MotoGP, WRC. For direct analogy to F1 — do their fan communities operate similarly? Are their rights-holder stances documented?

8. **Simulator modding communities**: iRacing, Assetto Corsa, rFactor, Forza Motorsport, Gran Turismo. These interact with F1's simulator clause directly and have their own rights-holder relationships.

9. **Famous donation-funded fan projects**: the ones where Patreon/Ko-fi became the focal point of enforcement. Ones that were forced to shut down donation pipelines specifically.

**Secondary domains** (add if primary set is thin):

- Disney (Mickey Mouse, Disney IPs generally)
- Anime/manga fan translations (scanlations) and their legal history
- Game of Thrones / HBO fan projects
- Dr Who fan films

**Do NOT spend time on**:

- F1 specifically (other lanes cover this)
- Legal doctrine synthesis (B8-4 and B8-5 cover this)
- Cases without public documentation (rumors, unconfirmed takedowns)

## Per-Case Investigation Protocol

For each case you cite, produce:

```
### [Case Name] ([Domain], [Year if known]) [S#]

- **What happened**: one-to-two-sentence summary, citing primary source
- **Rights-holder action**: cease-and-desist? lawsuit? tacit tolerance? negotiated settlement? verbatim quote from source
- **Project response**: continued / shut down / forked / rebranded
- **Monetization model at time of action**: was the project accepting donations? selling? free-only?
- **Branding**: did the project use explicit trademarks? implicit references?
- **Outcome**: current status as of source date
- **Why this case matters for F1 fan projects**: one-sentence relevance note
```

## What Must Appear in the Output

Write your output to `.planning/research/2026-04-11-f1-fan-project-legal-landscape/03-analogous-fan-projects.md`.

Required elements:

1. **YAML frontmatter**
2. **Sources table** at top
3. **Case catalog** — per-case entries per the template, grouped by domain
4. **Pattern analysis** — across cases, what patterns emerge?
   - What triggers enforcement? (Commercial polish? Scale? Branding visibility? Competing-with-official?)
   - What does NOT trigger enforcement? (Free, small, private, non-competitive)
   - How does monetization (donations specifically) affect rights-holder response?
   - Does "implicit branding" change anything compared to explicit branding?
5. **F1-relevance section** — given the patterns, what should we expect from F1 if it were to engage with community projects? Flag with OPUS-FOLLOWUP since this is cross-domain inference.
6. **Donation-specific subsection** — any documented cases where donation funding became the enforcement trigger? (E.g., a project tolerated as free was forced to drop Patreon.)
7. **"What I Did NOT Check" section**
8. **"Flagged for Opus Follow-up" consolidated list**
9. **"Qualifications" section**

**Length expectation**: 400–700 lines. Case catalogs can be substantial; pattern section should be compact and evidence-linked.

## Tool Usage Notes

- **WebSearch**: primary tool. Search for specific cases by name + "cease and desist" or "takedown" or "legal."
- **WebFetch**: for each case, try to fetch a primary source (creator's statement, news article, court filing snippet). Avoid Wikipedia as the sole source — it's aggregated and can be wrong.
- **Read**: for predecessor lanes, only if cross-referencing.
- **Time budget**: breadth over depth. Aim for 15+ cases across 5+ domains. If a domain yields nothing, document why.

## Output File

Write your output to:

`.planning/research/2026-04-11-f1-fan-project-legal-landscape/03-analogous-fan-projects.md`

Do not return a conversational summary instead of the file. Write the file, then return a brief confirmation (under 100 words) naming the central pattern finding.
