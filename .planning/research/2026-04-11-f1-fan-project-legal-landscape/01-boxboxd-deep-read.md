---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-1
question_focus: boxboxd-deep-read-legal-and-competitive
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
fetch_date: 2026-04-11
output_path: .planning/research/2026-04-11-f1-fan-project-legal-landscape/01-boxboxd-deep-read.md
primary_domain: https://boxboxd.fun
fetch_count: 18
---

# B8-1 — BoxBoxd Deep Read: Legal Posture + Competitive Reference Design

**Model:** Claude Sonnet 4.6 (general-purpose agent with WebFetch/WebSearch).
**Lane type:** Single-target, dual-dimension. Sonnet research lane — findings are "vague understanding" for further Opus refinement. Qualify findings; flag interpretive claims.

---

## Sources Table

| ID  | URL | Fetch Timestamp | Content Description |
|-----|-----|-----------------|---------------------|
| S1  | https://boxboxd.fun/home | 2026-04-11 | BoxBoxd homepage; navigation inventory, game mode summaries, footer disclaimer, founding year, social handles |
| S2  | https://boxboxd.fun/games | 2026-04-11 | Games Hub page; complete game mode listing with descriptions |
| S3  | https://boxboxd.fun/about | 2026-04-11 | About page; mission statement, founding date, disclaimer text |
| S4  | https://boxboxd.fun/terms-of-service | 2026-04-11 | Terms of Service page; IP/trademark language, disclaimer, footer |
| S5  | https://boxboxd.fun/privacy-policy | 2026-04-11 | Privacy Policy page; operator identity, contact absence, footer |
| S6  | https://boxboxd.fun/connections | 2026-04-11 | Connections game page (returned hub content — mode description extracted from hub) |
| S7  | https://boxboxd.fun/boxdle | 2026-04-11 | Boxdle game page (returned hub content — mode description extracted from hub) |
| S8  | https://boxboxd.fun/guess-who | 2026-04-11 | Guess Who F1 page (returned hub content — mode description extracted from hub) |
| S9  | https://boxboxd.fun/gridtexto | 2026-04-11 | Gridtexto page (returned hub content — mode description extracted from hub) |
| S10 | https://boxboxd.fun/elo-ranker | 2026-04-11 | Elo Ranker page (returned hub content — mode description extracted from hub) |
| S11 | https://boxboxd.fun/blog | 2026-04-11 | Blog index; post titles listed, no publication dates visible, no full article text returned |
| S12 | https://boxboxd.fun/quizzes | 2026-04-11 | Quizzes page; three personality-quiz modes listed |
| S13 | https://boxboxd.fun/for-brands | 2026-04-11 | For-brands page; B2B positioning, no pricing/metrics disclosed |
| S14 | https://boxboxd.fun/for-broadcasters | 2026-04-11 | For-broadcasters page; "Fan Opinion Data" offering, no metrics disclosed |
| S15 | https://boxboxd.fun/all-pages | 2026-04-11 | Complete site page index; exhaustive list of all routes |
| S16 | https://boxboxd.fun/blog/letterboxd-for-f1-why-boxboxd-exists | 2026-04-11 | Blog article slug fetch; returned hub content only, full article body not accessible to WebFetch |
| S17 | https://apps.apple.com/us/app/boxboxd/id6754217984 | 2026-04-11 | Apple App Store listing; developer name Shaina Salmi, version history with dates, app description |
| S18 | WebSearch: "boxboxd app store review 2024 F1 racing social network" | 2026-04-11 | Search results confirming developer identity, app store IDs, user review excerpt about viral Twitter moment |

**Note:** Wayback Machine (web.archive.org) was not accessible — all fetch attempts returned errors. Twitter/X account (@Box_Boxd) returned a 402 status. Instagram returned CSS-only content. B7 Games subsection quoted from: `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-2-lane-b7-f1-legal-ambiguity.md` (local file read, not a web source; this is the Opus re-fetch of F1's guidelines from 2026-04-11).

---

## TL;DR

- **What BoxBoxd is**: A "Letterboxd for F1" fan platform — race-logging social network plus a suite of daily puzzle games, personality quizzes, and community rankings. Free on iOS, Android, and web. Launched in 2024; iOS app v1.0 went live October 20, 2025, under developer name Shaina Salmi.
- **Legal posture**: BoxBoxd carries a consistent site-wide footer disclaimer ("independent fan platform. Not associated with any racing organization or championship body. All motorsport-related names and marks belong to their respective owners.") with no licensing disclosure, no formal affiliation, and no named operator beyond the app store developer credit. It uses F1-related content implicitly (driver names, circuit names, team names) without using the F1 wordmark/logo as branding. [OPUS-FOLLOWUP: whether implicit use of driver/circuit/team names constitutes use of F1's "Other IP Rights" under B7's Games subsection needs legal reading]
- **Game mode inventory**: 6 daily games (Boxdle, Gridtexto, Connections, Elo Ranker, Guess Who F1, Break Week) + 3 personality quizzes (Which Driver Are You?, Which Team Are You?, Which Duo Are You?) = 9 distinct interactive modes. No GeoGuessr-style geography or location-based mode found anywhere in the site.
- **Product shape**: Solo daily-puzzle architecture for most modes; one real-time multiplayer mode (Guess Who F1). Account-based with leaderboards/streaks. Browser + mobile app. No private-room or hosted-session architecture. No authored multi-round content packs.
- **Differentiation surface vs. prix-guesser**: BoxBoxd is entirely word/trivia/knowledge-pattern games about drivers, teams, and motorsport terms. Prix-guesser's anchor mode (authored GeoGuessr-style F1 geography rounds for private-room friends-on-couch play) is entirely absent from BoxBoxd. The product shapes differ at a structural level: BoxBoxd is daily-solo; prix-guesser is session-based, host-driven, multi-player.

---

## Dimension A — Legal Posture

### A1. What Kind of Project Is BoxBoxd

BoxBoxd is a fan-made platform with two layers: (1) a race-logging social network explicitly inspired by Letterboxd (per the blog post title "Letterboxd for F1: Why BoxBoxd Exists" [S11]) and (2) a suite of daily browser/mobile puzzle games and personality quizzes built on top of that social layer. All content on the site centers on motorsport knowledge: driver stats, team names, circuit names, race history, livery designs, helmet designs. The platform covers F1 race calendars from 2020–2026 [S1]. It is free to use, distributed as a mobile app (iOS and Android) and as a web application [S17].

The platform is publicly described as: "Think of BoxBoxd as a racing diary meets social network. Log every race you watch, give it a rating from half a star to five stars, write a review and see how your taste compares with fans around the world." [S1]

### A2. Branding Analysis

**Finding: BoxBoxd uses F1-adjacent content implicitly but does not brand using the F1 wordmark or official F1 logos.**

Observed implicit usage across the site [S1, S2]:
- "F1 Wordle" as a game descriptor for Boxdle: "Boxdle is the F1 Wordle: six guesses to identify the mystery driver using clues about nationality, age, team and career stats."
- "F1 tier list" in Elo Ranker description: "produces your personal F1 tier list powered by Elo scoring"
- "F1 driver deduction" and "F1 semantic word game" as game descriptors
- "Guess Who F1" as a game name
- Content covers "drivers, teams, circuits and technical terms" across all game modes — these necessarily involve real driver names, real team names, real circuit names

No evidence found of: official F1 logo used as site branding, Formula 1 wordmark in the site header or title, any official team logos, any official F1 visual identity elements. The site uses motorsport content as subject matter rather than as brand identity.

[OPUS-FOLLOWUP: using "F1" as a modifier in game names like "Guess Who F1" and "F1 tier list" may constitute use of F1's Permitted Word Marks under B7's Games subsection ("Our Permitted Word Marks cannot be used to brand any game"). Whether descriptive/genre use of "F1" differs from "branding" a game is a legal interpretation question this lane cannot resolve.]

### A3. Disclaimer and Licensing Analysis

**Finding: BoxBoxd carries a consistent, site-wide footer disclaimer on every page fetched. No licensing disclosure is present anywhere on the site.**

Verbatim disclaimer, present identically on every page fetched (S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15):

> "BoxBoxd is an independent fan platform. Not associated with any racing organization or championship body. All motorsport-related names and marks belong to their respective owners."

Verified locations:
- Homepage footer [S1]
- Games Hub [S2]
- About page [S3]
- Terms of Service [S4]
- Privacy Policy [S5]
- Every individual game page visited [S6–S10]

**No licensing disclosure found.** No text on any fetched page mentions a license, permission, arrangement, or agreement with Formula One Group, FOM, FIA, any individual team, or any motorsport organization. [OPUS-FOLLOWUP: absence of licensing disclosure is consistent with either (a) operation under a license not publicly disclosed, (b) operation without a license under a "fan use" posture, or (c) operation without a license with no formal posture taken. This lane cannot distinguish between these scenarios from public-facing content alone.]

**No Terms of Service effective date found.** The Terms of Service page [S4] does not state when it was last updated or when it became effective. [OPUS-FOLLOWUP: absence of ToS date is a minor flag for legal document completeness standards — may indicate informal origin.]

### A4. Monetization Analysis

**Finding: No visible monetization mechanism on public-facing pages. The platform is positioned as free. B2B data services are offered to brands and broadcasters.**

Confirmed free positioning: "BoxBoxd is free on iOS, Android and the web." [S1, S2]

No evidence found of: ads, donation links (Patreon, Ko-fi, GitHub Sponsors), subscriptions, premium features, paywalled content, merchandise shop, or in-app purchases.

B2B positioning exists: two commercial pages are present — "BoxBoxd for Brands" [S13] and "BoxBoxd for Broadcasters" [S14], described as "Motorsport Fan Data" and "Fan Opinion Data" respectively. No pricing, metrics, or case studies are disclosed on these pages. [OPUS-FOLLOWUP: B2B data services may constitute the primary commercial model. Whether offering F1 fan opinion/behavior data to brands constitutes "materially commercial" use under F1's Fans definition in B7's guidelines is an open question. F1's Fans definition explicitly flags "build traffic and/or following to a website and/or social profiles in order to sell goods or services rather than genuinely provide a service for fellow fans" as potentially "materially commercial."]

### A5. Operator Identity

**Finding: Developer name Shaina Salmi is disclosed only via the Apple App Store listing. The website itself discloses no individual, team, company name, or contact information.**

Disclosed via Apple App Store [S17]:
- **Developer name**: Shaina Salmi
- **App ID**: 6754217984
- **Android package**: com.raceboxboxd [S18]
- **Twitter handle**: @Box_Boxd [S1]
- **Instagram handle**: @Box.Boxd [S1]
- **TikTok handle**: @BoxBoxdApp [S1]

Not disclosed anywhere on the website: individual founder names, company legal name, registered address, email address, phone number. The /support page references the social handles above but provides no direct contact method. [OPUS-FOLLOWUP: lack of operator contact information beyond social handles may be relevant to GDPR / data protection compliance depending on jurisdiction — flag for any European user base analysis.]

**Organization type**: Cannot be determined from available evidence. The App Store lists "Shaina Salmi" as an individual developer, not a company entity. This is consistent with a solo indie project, but does not confirm it. [OPUS-FOLLOWUP: App Store individual developer credit is not conclusive — some companies submit apps under personal developer accounts.]

### A6. Relationship to F1's Guidelines (B7 Cross-Reference)

The B7 lane (Opus re-fetch of F1's guidelines, 2026-04-11) established the relevant Games subsection:

> "Our Permitted Word Marks cannot be used to brand any game. Other Intellectual Property Rights including those from the Formula 1 companies' official games cannot be used in third party games." (B7, Passage 3 — verbatim from F1 Guidelines)

BoxBoxd is, by definition, a third-party operator running games that use F1 driver names, team names, circuit names, and motorsport terminology. [OPUS-FOLLOWUP: whether driver names, circuit names, and team names fall under F1's "Other IP Rights" enumeration in B7's Passage 1 is not conclusively resolvable from B7's text. B7's enumeration of Other IP Rights lists: "Results and Timing data; Official Typeface; Statistics; Still Images; Audio and Audio Visual Content; Official Artworks, Graphics, Assets and Textures; Written Content." Driver/circuit/team names are not in this list explicitly. However, team names and circuit names may be protected as trademarks in their own right by their respective owners — which BoxBoxd's disclaimer acknowledges ("All motorsport-related names and marks belong to their respective owners"). This is a complex multi-party IP question beyond this lane's scope.]

BoxBoxd's disclaimer satisfies B7's Fundamental Principles requirement to "be clear that what you are doing is not official, approved or endorsed" — the footer language does exactly this.

BoxBoxd's apparent lack of licensing disclosure, combined with its implicit use of F1-adjacent content, is consistent with the pattern the B7 lane characterized as "navigating an under-defined intersection of three prohibitions and one narrow conditional carveout." [OPUS-FOLLOWUP: this cross-reference is Sonnet-level inference; Opus should review whether BoxBoxd's specific content types fall under the enumerated Other IP Rights or fall outside them.]

---

## Dimension B — Competitive Reference Design

### B1. History

**Finding: Founding year 2024 confirmed via structured data on the website. iOS app v1.0 launched October 20, 2025. No earlier launch date or web-only pre-app history established. No founder statement or origin narrative accessible.**

Confirmed data points:
- `"foundingDate": "2024"` — schema.org structured data in site HTML [S3, S4]
- iOS app v1.0 release: **October 20, 2025** [S17]
- iOS app v1.01 patch: October 22, 2025 [S17]
- iOS app v1.02: December 3, 2025 [S17]
- iOS app v1.03: approximately April 6, 2026 [S17]

The gap between founding year (2024) and iOS app v1.0 (October 2025) suggests the platform existed as a web-only product for approximately 1–2 years before the mobile app launched. [OPUS-FOLLOWUP: this timeline inference is based on two data points with a ~12-month gap; the actual web launch date in 2024 is not established. Wayback Machine was inaccessible for this lane — an Opus follow-up should check earliest Wayback snapshots for boxboxd.fun to establish whether the web launch was early 2024, mid-2024, or late 2024.]

One App Store user review noted: "Has some bugs, but that hardly matters when this is exactly what I want and I didn't even know it until it started going a bit viral on Twitter today." [S18] — This suggests a Twitter-driven initial discovery moment, consistent with a grassroots F1 fan project launch. The date of this review is not surfaced by WebFetch.

Blog post titles suggest evolution beyond a simple race-log at some point: the games suite (Boxdle, Connections, etc.) and community ranking features (Livery Championship, Helmet Championship) represent additions beyond the core Letterboxd-style logging concept. [OPUS-FOLLOWUP: no timeline for when specific game modes were added is available from public-facing pages. B7 or a future Opus lane should check Wayback Machine to identify when game routes first appeared.]

The blog post titled "Best F1 Daily Games 2026" [S11] suggests the games suite has been running long enough to warrant a "best of 2026" guide — consistent with games being present through at least the 2025 season.

### B2. Complete Game Mode Catalog

Six daily interactive games and three personality quizzes were confirmed across the site [S1, S2, S15]. No additional modes were found on /all-pages [S15] or any other route accessed.

---

#### Mode: Boxdle [S1, S2]

- **URL path**: /boxdle
- **Shape / genre**: NYT Wordle variant adapted to F1 drivers
- **Self-description** (verbatim from site): "Boxdle is the F1 Wordle: six guesses to identify the mystery driver using clues about nationality, age, team and career stats."
- **Content type**: F1 drivers (nationality, age, team, career statistics as clue attributes)
- **Rounds / length**: One puzzle per day; six guesses per puzzle
- **Reveal mechanism**: Each guess reveals how close you are on each attribute (implied by "clues about nationality, age, team and career stats")
- **Account / social**: Leaderboard tracking top streaks at /boxdle/leaderboard [S1]; streak tracking implies account-based persistence
- **Prix-guesser relation**: Orthogonal. Boxdle is a solo daily word/knowledge puzzle; prix-guesser is a hosted multi-round geography session. No overlap.

---

#### Mode: Gridtexto [S1, S2]

- **URL path**: /gridtexto
- **Shape / genre**: Contexto variant (semantic similarity game) adapted to motorsport vocabulary
- **Self-description** (verbatim from site): "Gridtexto is the motorsport Contexto: type any racing word and get a semantic rank over 400 drivers, teams, circuits and technical terms."
- **Content type**: Motorsport vocabulary — drivers, teams, circuits, technical terms (word pool of 400+ items)
- **Rounds / length**: Daily puzzle; "New puzzles every day" [S2]
- **Reveal mechanism**: Each word typed returns a semantic rank indicating proximity to the hidden target word
- **Account / social**: General account features on platform; no specific Gridtexto leaderboard mentioned
- **Prix-guesser relation**: Orthogonal. A semantic word-guessing game with no geographic or location component. No overlap with prix-guesser's anchor mode.

---

#### Mode: Connections [S1, S2]

- **URL path**: /connections
- **Shape / genre**: NYT Connections variant adapted to motorsport terminology
- **Self-description** (verbatim from site): "Connections is the word-grouping puzzle where you sort sixteen motorsport terms into four hidden categories."
- **Content type**: Motorsport terminology (drivers, teams, circuits, race events, technical terms)
- **Rounds / length**: Daily puzzle; 16 terms sorted into 4 categories
- **Reveal mechanism**: Player groups words into categories; each correct grouping is revealed
- **Account / social**: General platform account features; no dedicated Connections leaderboard surfaced
- **Prix-guesser relation**: Orthogonal. A word-categorization knowledge puzzle. No geographic or location component. This is the mode the user specifically named — confirmed as present and accurately characterized as an NYT Connections adaptation.

---

#### Mode: Elo Ranker [S1, S2]

- **URL path**: /elo-ranker
- **Shape / genre**: Head-to-head comparison ranker using Elo scoring algorithm
- **Self-description** (verbatim from site): "Elo Ranker runs you through twenty head-to-head driver duels and produces your personal F1 tier list powered by Elo scoring."
- **Content type**: F1 drivers in head-to-head pairings
- **Rounds / length**: Twenty head-to-head duels per session
- **Reveal mechanism**: After 20 duels, personal Elo-ranked tier list is produced
- **Account / social**: Results presumably saved to profile; platform has general social features
- **Prix-guesser relation**: Orthogonal. An opinion/ranking tool, not a geography or knowledge-guessing game. No overlap.

---

#### Mode: Guess Who F1 [S1, S2]

- **URL path**: /guess-who
- **Shape / genre**: Hasbro "Guess Who?" adapted to F1 drivers — real-time asynchronous multiplayer
- **Self-description** (verbatim from site): "Guess Who F1 is the real-time multiplayer driver deduction game: pick a secret driver, chat yes/no questions with your opponent, eliminate the grid."
- **Content type**: F1 drivers as the subject of deduction
- **Rounds / length**: One-on-one session; duration determined by question-answer exchange
- **Reveal mechanism**: Players ask yes/no questions; elimination narrows down the secret driver
- **Account / social**: Real-time multiplayer requires opponent matching; social/account features implied
- **Platform**: iOS, Android, web [S1]
- **Private rooms**: Not described — the mode mentions "your opponent" suggesting one-on-one matchmaking, but no evidence of private-room creation or host-screen features [OPUS-FOLLOWUP: whether Guess Who F1 supports private room codes (friends choosing their own opponent) or only random matchmaking is not determinable from public page text. This distinction matters for the prix-guesser differentiation analysis.]
- **Prix-guesser relation**: Adjacent but structurally different. Guess Who F1 is 1v1 real-time, knowledge-deduction. Prix-guesser is authored-content, GeoGuessr-style geography, group-play (3–8 players), host-mediated. Both support multiplayer but the shape, scale, and content type are different. [OPUS-FOLLOWUP: comparative judgment from single-site reading]

---

#### Mode: Break Week [S1, S2]

- **URL path**: /break
- **Shape / genre**: Daily fan survey / opinion polling, available during F1 calendar gap weeks
- **Self-description** (verbatim from site): "Break Week - Daily fan survey during calendar gaps"
- **Content type**: Fan opinion questions about racing (specific question types not visible from public pages)
- **Rounds / length**: Daily, during calendar gaps only
- **Reveal mechanism**: Survey responses presumably aggregate into community results
- **Account / social**: Presumably tied to account for participation tracking
- **Prix-guesser relation**: Orthogonal. A survey/polling mechanism, not a geography or guessing game.

---

#### Mode: Which Driver Are You? [S12]

- **URL path**: /personality (linked from /quizzes)
- **Shape / genre**: BuzzFeed-style personality quiz
- **Self-description** (verbatim from site): "Personality Quiz" (label only; no description text available)
- **Content type**: F1 driver personality matching
- **Rounds / length**: Not specified
- **Account / social**: Not specified
- **Prix-guesser relation**: Orthogonal.

---

#### Mode: Which Team Are You? [S12]

- **URL path**: /which-team (linked from /quizzes)
- **Shape / genre**: BuzzFeed-style personality quiz
- **Self-description**: Team personality matching (no description text available)
- **Prix-guesser relation**: Orthogonal.

---

#### Mode: Which Duo Are You? [S12]

- **URL path**: /which-duo (linked from /quizzes)
- **Shape / genre**: BuzzFeed-style personality quiz
- **Self-description**: Driver duo personality matching (no description text available)
- **Prix-guesser relation**: Orthogonal.

---

### B3. Product Shape Summary

| Dimension | BoxBoxd |
|-----------|---------|
| Primary product type | Race-logging social network + daily games suite |
| Game architecture | Solo daily puzzle (5 of 6 games); 1v1 real-time multiplayer (Guess Who F1) |
| Session structure | Daily reset; persistent streaks/leaderboard via account |
| Account requirement | Account encouraged; streaks/leaderboard require account |
| Private rooms | Not evidenced |
| Host-screen / group play | Not evidenced |
| Platform | Web browser + iOS app + Android app |
| Content authored by | Operator (daily puzzles auto-rotate); no user-authored content rounds visible |
| Social features | Follow/feed, race reviews, community rankings, leaderboards, sharing |
| Founding | 2024 (web); October 2025 (iOS app) |
| Operator identity | Shaina Salmi (individual developer, iOS App Store) |
| B2B layer | For Brands + For Broadcasters data offerings |

### B4. The "X but for F1" Pattern

BoxBoxd adapts a specific and identifiable set of existing game shapes:

| Source Shape | BoxBoxd Adaptation | BoxBoxd Game |
|---|---|---|
| Letterboxd (film diary / social network) | Race diary / racing social network | Core platform |
| NYT Wordle | Driver guessing with attribute clues | Boxdle |
| Contexto (semantic word similarity) | Motorsport vocabulary semantic ranker | Gridtexto |
| NYT Connections | Motorsport term word-grouping | Connections |
| Elo rating system / tier list | F1 driver personal tier list builder | Elo Ranker |
| Hasbro Guess Who? | F1 driver deduction, 1v1 real-time | Guess Who F1 |
| BuzzFeed personality quiz | Which driver/team/duo are you? | Quiz suite |
| Daily survey/break content | Fan opinion polling during gap weeks | Break Week |

**Pattern observation**: Every BoxBoxd game mode adapts an existing well-known game format to F1 driver/team/term trivia. All adaptations are knowledge-domain-transpositions — they replace the original content (film vocabulary, general vocabulary, general nouns, generic Guess Who figures) with F1 content. None are spatial, geographic, or authored-content based. [OPUS-FOLLOWUP: this pattern characterization is a Sonnet-level synthesis from single-site reading; verify by direct gameplay access]

**Notably absent game shapes**: GeoGuessr (location/geography guessing), NYT Crossword, Wordle (exact word spelling), Bracket/prediction tournament, Head-to-head prediction, Trivial Pursuit / multi-topic trivia, Jigsaw/image reconstruction.

### B5. Differentiation Surface: BoxBoxd vs. Prix-Guesser

**Prix-guesser anchor mode (per task spec)**: authored GeoGuessr-style F1 geography rounds with clue ladders, designed for friends-on-couch / private-remote / hybrid game nights (private-room play, host-mediated, group of 3–8, session-based multi-round authored content packs).

**Direct overlap assessment — mode by mode**:

| BoxBoxd Mode | Overlap with Prix-Guesser Anchor | Assessment |
|---|---|---|
| Boxdle | No overlap — solo daily word/knowledge puzzle | Orthogonal |
| Gridtexto | No overlap — solo daily semantic word game | Orthogonal |
| Connections | No overlap — solo daily word grouping | Orthogonal |
| Elo Ranker | No overlap — opinion/ranking tool | Orthogonal |
| Guess Who F1 | Partial adjacency — 1v1 multiplayer, F1 content | Adjacent but structurally different (see below) |
| Break Week | No overlap — opinion survey | Orthogonal |
| Personality quizzes | No overlap — entertainment personality matching | Orthogonal |

**Guess Who F1 adjacency detail**: Both Guess Who F1 and prix-guesser involve multiple players and F1 content. The structural differences are significant: (a) Guess Who F1 is 1v1; prix-guesser is group (3–8); (b) Guess Who F1 uses knowledge-deduction (yes/no questions about driver characteristics); prix-guesser uses GeoGuessr-style geography (place a pin on a map, or identify a location from images/clues); (c) Guess Who F1 appears to use random/platform matchmaking; prix-guesser uses private room codes for friends; (d) Guess Who F1 has no authored content packs; prix-guesser's value proposition is the human-authored clue ladder and location curation. [OPUS-FOLLOWUP: comparative structural judgment; Guess Who F1 gameplay details need direct observation to confirm]

**The geographic/spatial gap**: BoxBoxd has no geography mode, no location-based mode, no image-recognition mode, no "where is this?" mode of any kind. All BoxBoxd games operate on F1 knowledge as propositions (facts, names, categories, semantic proximity) rather than on F1 knowledge as spatial experience (circuits as places, paddock as environment, circuit geography). Prix-guesser's anchor explicitly occupies this spatial/geographic category. [OPUS-FOLLOWUP: this differentiation observation is the most material one for prix-guesser's positioning; it is a Sonnet-level reading from public page text and should be confirmed by direct gameplay access to BoxBoxd and by checking if any BoxBoxd modes include image-recognition elements not described in their text descriptions]

**The group-play/private-room gap**: BoxBoxd has no private-room architecture, no host-screen mode, no "play with your specific friend group" infrastructure (beyond the 1v1 Guess Who which may or may not support private invites). Prix-guesser's friends-on-couch / private-remote framing is structurally differentiated from BoxBoxd's daily-puzzle/leaderboard architecture. [OPUS-FOLLOWUP: same caveat — Guess Who F1 private room question unresolved]

**The authored-content-pack gap**: BoxBoxd's games appear to be algorithmically generated or operator-curated daily puzzles that reset automatically. There is no evidence of authored content packs, themed round sets, curated location sequences, or host-designed experiences. Prix-guesser's planned authored-round model (human-curated geographic clue ladders with narrative structure) has no BoxBoxd equivalent. [OPUS-FOLLOWUP: whether BoxBoxd has any curator/creator tools or user-generated content is not determinable from public pages]

---

## What I Did NOT Check

1. **Wayback Machine**: All web.archive.org fetches failed with errors. Cannot establish the web-only launch date in 2024 or the history of game mode additions. This is the single most significant gap in the history section. Opus follow-up should retry with a different approach.

2. **Twitter/X account @Box_Boxd**: Fetch returned 402 (payment required). Cannot see tweet history, announcement posts, game launch dates, or follower count. Twitter presence is confirmed (social handle present on site) but content is inaccessible.

3. **Instagram @Box.Boxd**: Returned CSS-only content (JavaScript-rendered page). Cannot see post history or launch announcements.

4. **Login-gated content**: Any content behind BoxBoxd account login was not accessed. Profile pages, personal dashboards, account-specific game histories, and potentially login-gated game modes are out of scope.

5. **Direct gameplay**: No game was played. Descriptions are from landing-page/hub text. Actual puzzle mechanics, clue types, difficulty, daily puzzle archive depth (puzzle #s), and the actual content of Connections categories were not observed firsthand.

6. **Game mode pages returning hub content**: Every individual game URL (/boxdle, /gridtexto, /connections, /elo-ranker, /guess-who, /break) returned the same hub page content rather than a standalone game page. This may mean the games are fully app-native (mobile app required for actual play), or that the web game pages require JavaScript rendering that WebFetch cannot execute. The game descriptions available are from the hub, not from in-game instruction screens.

7. **Blog article full text**: The blog article "Letterboxd for F1: Why BoxBoxd Exists" was not accessible as full article text — fetches returned the same hub content. This article would likely contain the richest founding narrative available on the site.

8. **Google Play Store listing**: The Android Play Store page returned obfuscated JavaScript and no useful metadata. Developer name and exact Android launch date not confirmed independently.

9. **ProductHunt / HackerNews**: Not checked in this lane. May contain founding narrative or launch announcement.

10. **GitHub repository**: Not checked. BoxBoxd may or may not be open source; no GitHub link was found on the site.

---

## Flagged for Opus Follow-up

### Legal Follow-ups

**[OPUS-FOLLOWUP L1]**: Does BoxBoxd's implicit use of driver names, team names, and circuit names as game content fall under F1's "Other IP Rights" enumeration in B7? The enumeration does not list these names explicitly — but team names and circuit names may be independently trademarked by their owners. BoxBoxd's disclaimer ("All motorsport-related names and marks belong to their respective owners") acknowledges this. Resolution requires trademark-by-trademark analysis beyond this lane's scope.

**[OPUS-FOLLOWUP L2]**: Does using "F1" as a modifier in game names ("Guess Who F1," "F1 tier list," "F1 Wordle" as a genre descriptor) constitute "branding" a game with F1's Permitted Word Marks under B7's Games subsection? This is the most direct legal question BoxBoxd raises. The site does not use "Formula 1" or "F1" as the name of the platform or as a standalone brand element — only as a content-genre descriptor. Whether descriptive use of "F1" differs from branding is a legal interpretation question.

**[OPUS-FOLLOWUP L3]**: BoxBoxd's B2B data service offerings ("For Brands," "For Broadcasters") may constitute "materially commercial" use under F1's Fans definition. If BoxBoxd is aggregating F1 fan behavior data and selling access to brands, it may no longer fit the "Fans" definition's carveout for non-commercial fan activity. This needs review alongside whatever B7's full Fans definition holds.

**[OPUS-FOLLOWUP L4]**: The absence of a ToS effective date and the absence of any GDPR-style operator contact information raises questions about whether BoxBoxd is operating compliant data handling for a platform with user accounts, if it has a meaningful European user base. Out of scope for prix-guesser's planning but worth flagging.

### Competitive / Product Follow-ups

**[OPUS-FOLLOWUP C1]**: Wayback Machine access failed in this lane. The 2024 web launch date is confirmed only by structured data. An Opus retry with Wayback CDX API or alternative history source should establish: when was boxboxd.fun first crawled? When were game routes (/boxdle, /connections, etc.) first available? This would tell us the chronological order of feature additions.

**[OPUS-FOLLOWUP C2]**: Guess Who F1's multiplayer architecture needs direct gameplay observation. Does it support private room codes (friends choosing each other) or only random matchmaking? If it supports private rooms with friend codes, the overlap with prix-guesser's group-play positioning is stronger than this lane's reading suggests.

**[OPUS-FOLLOWUP C3]**: Individual game mode pages returned hub content rather than standalone game UI. This suggests the actual gameplay is mobile-app-native or requires JavaScript rendering. An Opus follow-up should attempt these pages with a JavaScript-capable fetch or via mobile app direct observation to: (a) confirm game mechanics, (b) check puzzle numbers (which would establish how long each daily game has been running), (c) identify any content types not described in hub text (e.g., whether Connections uses images, whether Boxdle uses circuit images or driver photos).

**[OPUS-FOLLOWUP C4]**: The blog article "Letterboxd for F1: Why BoxBoxd Exists" is the most likely source of founding narrative and origin story. It returned hub content rather than article text. Opus should retry this fetch or find a cached version to surface the founding story.

**[OPUS-FOLLOWUP C5]**: Developer Shaina Salmi is named in the Apple App Store but no additional public profile was found. A targeted search for Shaina Salmi (F1 developer, BoxBoxd) might establish professional background, location, whether solo or team, and any public statements about the project's origins and goals.

---

## Qualifications

1. **All findings are as of fetch date 2026-04-11.** BoxBoxd is a live product; game modes, disclaimers, and monetization may have changed since this fetch.
2. **Public-facing only.** Private agreements between BoxBoxd and any motorsport rights holder are not visible from the public website. The absence of a disclosed license does not prove the absence of a license.
3. **Game mode catalog confidence: HIGH for mode names; LOW for gameplay mechanics.** The six daily games and three quizzes are confirmed from /all-pages and cross-referenced against the site hub. Gameplay mechanics are based on hub text descriptions only — no direct gameplay was observed.
4. **WebFetch limitations.** Several key pages (individual game pages, the founding blog article, Instagram, Twitter/X) returned either hub content, CSS-only renders, or HTTP errors. The findings from these sources are therefore limited to what the hub pages disclose.
5. **History confidence: LOW.** The 2024 founding year is established by schema.org structured data (reliable as self-reported data but not independently verified). The October 2025 iOS app launch is established by App Store version history (high confidence). No web-only launch date is confirmed. No game-mode addition chronology is available.
6. **This is a Sonnet-lane research artifact.** All synthesis and comparative judgments are flagged with [OPUS-FOLLOWUP] markers. The differentiation surface analysis in B5 represents this lane's best reading from available text — it should be validated by direct gameplay access and by an Opus-level review of the BoxBoxd game mode descriptions against prix-guesser's canonical mode design.
