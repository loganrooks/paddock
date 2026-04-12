---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-1
question_focus: boxboxd-deep-read-legal-and-competitive
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
tools_required: [WebFetch, WebSearch]
scope: "Deep-read boxboxd.fun as both (a) legal posture case (branding, disclaimers, licensing disclosures, monetization, operator identity) AND (b) competitive reference design (history, all game modes, product shape, community, how the 'X but for F1' pattern is executed). Specifically documents all game modes including the F1 Connections mode the user identified, establishes founding history and evolution, and produces the raw material for prix-guesser's differentiation positioning."
triggered_by: "User question during phase-01-prep audit pause. Initial legal question: 'what about BoxBoxd.com? that is entirely F1 Themed'. Expanded scope after correction: 'boxboxd is such a good reference design that we also need to differentiate ourselves from. https://boxboxd.fun/home also I screwed up and its .fun. im curious about its history and what not too. how and when did it come to be? the different game modes etc. because they have the Connections game from NYT but for F1 too!'"
output_file: 01-boxboxd-deep-read.md
---

# B8-1 — BoxBoxd Deep Read (Legal + Competitive Reference Design)

**You are running as a general-purpose agent on Claude Sonnet 4.6 with WebFetch and WebSearch.**

One of five parallel research lanes in the B8 research program. Your scope is **single target, dual dimension**: BoxBoxd is simultaneously (a) a legal-posture case (how does an F1 fan game handle IP?) and (b) the closest adjacent competitive reference design to prix-guesser. Both dimensions must be fully covered because BoxBoxd is the most important project for prix-guesser's positioning and the user has explicitly flagged it as prior art to differentiate from.

**The correct domain is `boxboxd.fun` — NOT `.com`, NOT `.app`.** Start at `https://boxboxd.fun/home`. Confirmed by user.

**Mark your model identity explicitly in your output frontmatter so the synthesis lane can attribute findings.**

## The Two Dimensions

### Dimension A — Legal Posture

How does BoxBoxd handle F1 intellectual property? Specifically:

1. **Branding**: does BoxBoxd explicitly use F1 wordmark/logo/colors, implicitly (circuit names, driver names, race content without F1 wordmark/logo), or some mix? Quote evidence.
2. **Licensing disclosure**: does BoxBoxd disclose any arrangement with F1 / Formula One Group / FIA / individual teams?
3. **Disclaimer**: does BoxBoxd display "unofficial" / "not affiliated" / "fan-made" language, and where?
4. **Monetization**: ads, donations (Patreon/Ko-fi/GitHub Sponsors), subscriptions, merchandise, nothing visible?
5. **Operator identity**: who runs it? Individual, team, company? Disclosed or hidden?

### Dimension B — Competitive Reference Design

BoxBoxd is near-exact prior art for the "X but for F1" pattern prix-guesser sits in (anchor mode: GeoGuessr for F1 places). The user has explicitly flagged it as a reference design to differentiate from. Document:

1. **History**: when was BoxBoxd founded/launched? How has it evolved? Major milestones?
2. **Complete game mode inventory**: every distinct mode available on the site. The user explicitly named "F1 Connections" (F1 version of NYT Connections) — catalog that plus every other mode, with a brief description of each.
3. **Product shape**: is it solo-daily-puzzle like F1DLE/Formudle? Multiplayer? Private-room capable? Host-screen friendly? What platforms (browser only, mobile app, desktop)?
4. **Content depth**: how much authored content exists per mode? Daily new content or static pool? How is content authored — community submissions, AI, operator-authored?
5. **Community/social features**: leaderboards, friend systems, sharing, accounts, profiles, streaks?
6. **The "X but for F1" pattern**: which game shapes does BoxBoxd adapt? (Connections is confirmed; search for more: Wordle variants, Crosswords, Sudoku, geography games, bracket predictions?)
7. **Differentiation opportunity**: given BoxBoxd's current mode list and product shape, where are the gaps prix-guesser could fill? Specifically note whether BoxBoxd has (or lacks) a GeoGuessr-style geography mode, which is prix-guesser's anchor.

## Epistemic Ground Rules — HIGH CITATION STANDARDS

You are producing a research artifact that will be followed up on by Opus if any finding seems suspicious. Usefulness depends on whether a follow-up reader can find your original sources in one step and verify your reasoning chain. **Competitive analysis requires the same citation rigor as legal analysis** — any claim about BoxBoxd's game modes or history must cite a specific page with a verbatim passage, not inference.

**This is a Sonnet research lane producing "vague understanding" for further refinement, not a legal opinion or a product strategy deliverable. Qualify findings appropriately and flag interpretation-heavy claims for Opus follow-up.**

### Core rules

1. **Every factual claim cites URL + verbatim passage + fetch timestamp.** For game mode claims: "Fetched https://boxboxd.fun/[mode-path] at 2026-04-11 [HH:MM] UTC; the page title reads '[verbatim title]' and the instructional text reads: '[verbatim passage].' This establishes the mode as [characterization]." For legal claims: "Fetched https://boxboxd.fun/[legal-page] at [timestamp]; the footer reads: '[full-paragraph verbatim quote].'"

2. **Quote full sentences minimum; full paragraphs for nuance.** Short quotes compress and distort. For game modes, quote enough instructional text to convey the mode's actual shape.

3. **For every finding, ask "What would disconfirm this?" and CHECK.** If claiming "BoxBoxd has no disclaimer," check: homepage, footer, About page, Terms/ToS, Privacy Policy, Contact, FAQ, legal pages, HTML meta tags, "Credits/Acknowledgments" sections. If claiming "BoxBoxd has N game modes," verify you have visited the main navigation and any game-list page exhaustively — it's easy to miss modes hidden behind menus.

4. **Flag interpretation-heavy claims with `[OPUS-FOLLOWUP: reason]` inline.** Examples:
   - "BoxBoxd appears to operate without a formal licensing arrangement. [OPUS-FOLLOWUP: inferred from absence of disclosure, not direct evidence]"
   - "This monetization pattern is consistent with cost-recovery donations rather than profit. [OPUS-FOLLOWUP: inference from Ko-fi link, not operator statement]"
   - "BoxBoxd's shape is clearly differentiated from prix-guesser by X. [OPUS-FOLLOWUP: comparative judgment from single-site reading]"
   Flag at point of writing so a grep finds them.

5. **"I don't know yet" is a valid finding.** Not every question will yield. If you can't find the founding date, say so with what you searched.

6. **Reasoning visible.** When you synthesize the competitive differentiation observation, show the underlying mode-by-mode comparison reasoning.

### Mandatory traceability deliverables

- **Sources table at top**: `[S#]` ID, URL, fetch timestamp, one-sentence description of relevant content. Every inline citation must map to this table.
- **Inline citations by bracketed ID**: every factual claim cites `[S1]`, `[S2]`, etc., with verbatim quote.
- **"What I Did NOT Check" section**: partial coverage named explicitly — game modes you couldn't access (e.g., login-gated), legal pages not found, history details not surfaced.
- **"Flagged for Opus Follow-up" consolidated list**: every `[OPUS-FOLLOWUP: ...]` marker collected with a one-line summary. Group legal follow-ups separately from competitive/product follow-ups.
- **"Qualifications" section**: "as of fetch date X", "public-facing only, private agreements not visible", "game mode catalog may be incomplete if modes are login-gated", etc.

### Chain integrity

Predecessors (contestable, not authoritative):
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md` (did not cover BoxBoxd — this lane is new ground)
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b7-f1-legal-ambiguity.md` (established F1's actual guidelines text including the Games subsection: "Other Intellectual Property Rights including those from the Formula 1 companies' official games cannot be used in third party games" — BoxBoxd is by definition a third party game, so this prohibition is directly relevant to its operational posture)

**The user's project memory names BoxBoxd as the closest reference design to differentiate from**. The user's initial characterization ("entirely F1 themed, doesn't explicitly brand themselves as such I don't think") may or may not be accurate — verify empirically. If BoxBoxd turns out to use F1 wordmark/logo explicitly, surface that as a finding that contradicts the user's current read.

### Negative discipline

- **No legal opinions.** Empirical observations + OPUS-FOLLOWUP markers only.
- **No manufactured confidence.** "Appears to" and "consistent with" are honest; "is definitively" is overreach unless directly cited.
- **No strategic recommendations.** You are producing raw material for prix-guesser's differentiation decisions, not the decisions themselves. Observations like "BoxBoxd does X, prix-guesser does Y, these differ on Z" are fine; "prix-guesser should do W" is out of scope.
- **No loose-citation consolidation.** Two sources with slight differences → report both, don't merge.

## Scope — What to Fetch

**Primary targets (legal posture)**:

1. **Homepage**: `https://boxboxd.fun/home` (user-confirmed URL) and `https://boxboxd.fun` (root)
2. **Footer text** on every page you visit — disclaimers and copyright live here
3. **About / About Us / About BoxBoxd page** if one exists
4. **Terms of Service / Terms of Use / ToS**
5. **Privacy Policy**
6. **Contact / Contact Us** — operator identity disclosure
7. **FAQ or Help pages**
8. **Any "Credits" / "Acknowledgments" / "Legal" / "IP" page**

**Primary targets (competitive / product)**:

9. **Main navigation** — catalog every menu item
10. **Every game mode page** — the user specifically mentioned "F1 Connections" as an example; look for Wordle variants, geography games, trivia, crosswords, prediction games, bracket-style games, and any mode that is "[existing shape] but for F1"
11. **Daily puzzle archive or history** (if any) — shows how long the project has been running
12. **Leaderboards / community / social features** — shows product shape
13. **Account / Login / Profile pages** — shows whether it's account-based and what social features exist
14. **Any "changelog" or "what's new" section** — shows evolution history

**Secondary targets** (fetch if time permits):

- **Wayback Machine snapshots** of boxboxd.fun: `https://web.archive.org/web/*/boxboxd.fun*` — shows founding date and historical versions. **Especially important for the history question** — the Wayback earliest snapshot is usually the most reliable "when did this come to be" source.
- **Twitter/X account** (search "boxboxd" on Twitter) — operator announcements, launch history, community engagement
- **ProductHunt / HackerNews / Reddit launch posts** — founder statements about motivation and history
- **Any blog posts about BoxBoxd** — community coverage that describes history or modes
- **GitHub repository** (if the project is open source) — README often contains history

**Do NOT spend time on**:

- Related F1 projects (B8-2 covers the breadth survey)
- F1's own guidelines (B7 handled this)
- Legal doctrine synthesis (B8-4 and B8-5 cover this)
- Strategic recommendations for prix-guesser (out of scope for this lane)

## Per-Page Investigation Protocol

For each page you fetch, produce:

1. **URL + fetch timestamp + page title**
2. **One-sentence page purpose** (from the page itself, not your inference)
3. **Verbatim quotes of any relevant passages**:
   - Branding language (F1, Formula 1, Grand Prix, specific drivers/circuits/teams)
   - Licensing language (rights, copyright, trademark, license, affiliation, permission)
   - Disclaimer language ("not affiliated," "unofficial," "fan-made," "tribute," "educational," "for fun")
   - Monetization language (subscriptions, ads, donations, Patreon, Ko-fi, sponsorship, merchandise, premium features)
   - Operator identity (names, emails, organizations, social handles)
   - **Mode description language** (for game mode pages — how the mode describes itself, what the goal is, how many rounds, what content)
   - **History language** (for about / FAQ / blog — any dates, milestones, founder statements)
4. **Relevant absence** — if you expected to find legal language or history and didn't, note what the page does contain

## Game Mode Cataloging Protocol

For each game mode on BoxBoxd, produce:

```
### Mode: [Name] [S#]

- **URL path**: [e.g., /connections]
- **Shape / genre**: [e.g., "NYT Connections variant" / "Wordle variant" / "geography quiz"]
- **Self-description** (verbatim from page): "[quote]"
- **Content type**: [drivers, teams, circuits, races, facts, images, etc.]
- **Rounds / length**: [e.g., "one puzzle per day" / "five rounds per session"]
- **Reveal mechanism**: [how does the player learn the answer]
- **Account / social**: [does it track history, streaks, leaderboards?]
- **Prix-guesser relation**: is this overlapping, adjacent, or orthogonal to prix-guesser's anchor mode (GeoGuessr-style F1 geography rounds)? [OPUS-FOLLOWUP if interpretive]
```

Aim to catalog every mode on the site, not just the F1 Connections one. The user may be unaware of how many modes exist.

## What Must Appear in the Output

Write your output to `.planning/research/2026-04-11-f1-fan-project-legal-landscape/01-boxboxd-deep-read.md`.

Required elements:

1. **YAML frontmatter** identifying lane, model, agent type, fetch date, output path
2. **Sources table** at top
3. **TL;DR** (3-6 bullets): what BoxBoxd is, legal posture summary, competitive overview, differentiation opportunity
4. **Dimension A — Legal Posture** section with subsections:
   - What kind of project is BoxBoxd (concrete content/mode characterization)
   - Branding analysis (explicit/implicit/none with evidence)
   - Disclaimer / licensing analysis
   - Monetization analysis
   - Operator identity
   - Relationship to F1's actual guidelines (B7's Games subsection in particular — flag with OPUS-FOLLOWUP)
5. **Dimension B — Competitive Reference Design** section with subsections:
   - **History**: founding date, evolution, major milestones, with Wayback Machine or primary-source citations
   - **Complete game mode catalog** per the Mode template above — including the F1 Connections mode the user specifically identified
   - **Product shape summary**: solo vs multi, daily vs session, account vs anonymous, web vs mobile, social features
   - **The "X but for F1" pattern**: which existing game shapes does BoxBoxd adapt? Catalog the adaptation pattern.
   - **Differentiation surface**: mode-by-mode comparison to prix-guesser's declared anchor (authored GeoGuessr-style F1 geography rounds with clue ladders for friends-on-couch/private-remote/hybrid game nights). Where does BoxBoxd overlap, where doesn't it? Flag interpretive claims with OPUS-FOLLOWUP.
6. **"What I Did NOT Check" section** — explicit partial-coverage acknowledgment (login-gated modes, pages not found, history details not surfaced, etc.)
7. **"Flagged for Opus Follow-up" consolidated list** — split into "Legal follow-ups" and "Competitive/Product follow-ups"
8. **"Qualifications" section**

**Length expectation**: 300–500 lines (expanded from the original narrow scope because this lane now covers both dimensions). Prioritize game mode catalog depth and history accuracy; legal posture is important but empirically straightforward.

## Tool Usage Notes

- **WebFetch**: primary tool. Start with `https://boxboxd.fun/home` (user-confirmed). Fetch each distinct page in the site. Save returned content verbatim before distilling.
- **WebSearch**: use to find the Twitter account, any blog posts about BoxBoxd, ProductHunt launch posts, or community coverage. Also use to find Wayback Machine snapshots if the site doesn't expose history internally.
- **Read**: for B7's output if you need to verify the Games subsection quotation for the cross-reference.
- **Bash / Grep / Glob**: probably not needed.
- **Time budget**: this lane is now deeper than the original narrow scope. Budget more fetches for game mode coverage and history research. If after ~20 fetches you have solid coverage, stop — diminishing returns beyond that.

## Output File

Write your output to:

`.planning/research/2026-04-11-f1-fan-project-legal-landscape/01-boxboxd-deep-read.md`

Do not return a conversational summary instead of the file. Write the file, then return a brief confirmation (under 150 words) naming:
1. BoxBoxd's legal disclosure posture (disclaimer present/absent, licensing disclosed/not)
2. The complete game mode count and whether BoxBoxd has a GeoGuessr-style mode (the prix-guesser anchor)
3. Founding date or best-available history data point
4. One concrete differentiation observation between BoxBoxd and prix-guesser
