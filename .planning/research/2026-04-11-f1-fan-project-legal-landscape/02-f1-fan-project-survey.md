---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-2
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
fetch_date: 2026-04-11
output_file: 02-f1-fan-project-survey.md
predecessor_lanes:
  - wave-1-lane-1c-external-gap-research.md
  - wave-2-lane-b7-f1-legal-ambiguity.md
scope: "Breadth survey of active F1-themed community fan projects. Catalog 10+ projects; extract pattern across branding, disclaimer, monetization, licensing, operator identity, enforcement history."
---

# B8-2 — F1 Fan Project Survey

**Model:** Claude Sonnet 4.6 (general-purpose agent, WebSearch + WebFetch).
**Lane type:** Breadth over depth. 12 projects cataloged. No single project deep-read beyond catalog template.
**Chain position:** Extends Lane 1C's claim that F1 daily-puzzle games "operate publicly without takedowns." Cross-references Lane B7's verbatim F1 policy text.

---

## Sources Table

| ID | URL | Fetch timestamp | Description |
|----|-----|-----------------|-------------|
| S1 | https://f1dle.com/ | 2026-04-11 | F1DLE homepage (JavaScript-gated; partial content returned) |
| S2 | https://f1dle.com/about | 2026-04-11 | F1DLE about page (JavaScript-gated; partial content) |
| S3 | https://f1dle.com/privacy | 2026-04-11 | F1DLE privacy page (JavaScript-gated; partial content) |
| S4 | https://stewardle.com/ | 2026-04-11 | Stewardle homepage |
| S5 | https://racing.whoareya.games/ | 2026-04-11 | Who Are Ya? F1 driver guesser homepage |
| S6 | https://racing.whoareya.games/privacy-policy.html | 2026-04-11 | Who Are Ya? privacy policy |
| S7 | https://www.formula1points.com/driverle/?type=driverle | 2026-04-11 | Driverle on formula1points.com |
| S8 | https://www.sportsdle.com/f1/daily-guessing-game | 2026-04-11 | Sportsdle F1 Wordle page |
| S9 | https://drivergridgame.com/ | 2026-04-11 | Driver Grid Game homepage |
| S10 | https://www.racegrids.com/ | 2026-04-11 | RaceGrids homepage (minimal content returned) |
| S11 | https://www.guessthef1driver.com/ | 2026-04-11 | Guess the F1 Driver homepage |
| S12 | https://github.com/theOehrly/Fast-F1 | 2026-04-11 | FastF1 GitHub repository README |
| S13 | https://docs.fastf1.dev | 2026-04-11 | FastF1 documentation site |
| S14 | https://github.com/theOehrly/Fast-F1/blob/master/LICENSE | 2026-04-11 | FastF1 MIT license file |
| S15 | https://github.com/jolpica/jolpica-f1 | 2026-04-11 | Jolpica-F1 GitHub repository README |
| S16 | https://jolpi.ca/ | 2026-04-11 | Jolpica-F1 API homepage (minimal content) |
| S17 | https://github.com/BrightDV/BoxBox | 2026-04-11 | BoxBox (Box, Box!) GitHub README |
| S18 | https://www.f1ocean.com/disclaimer | 2026-04-11 | F1 Ocean disclaimer page |
| S19 | https://tracinginsights.com/data/ | 2026-04-11 | TracingInsights F1 data tool page |
| S20 | https://www.formula1.com/en/toolbar/guidelines.html | 2026-04-11 | F1 official guidelines (fan website requirements) |
| S21 | https://thesportsrush.com/f1-news-f1-content-creators-get-cease-and-desists-forced-to-change-usernames/ | 2026-04-11 | SportsRush: F1 C&D letters to creators, Aug 2024 |
| S22 | https://medium.com/full-throttle-femme/the-cease-and-desist-dilemma-how-f1-content-creators-are-growing-the-sport-and-what-f1-could-have-d40a06c5b5aa | 2026-04-11 | Medium: C&D dilemma opinion piece, Aug 2024 |
| S23 | https://formudle.com/privacy-policy | 2026-04-11 | Formudle privacy policy (403 on direct fetch; content reconstructed from search snippet) |
| S24 | WebSearch result set | 2026-04-11 | Search results for Formudle disclaimer text, confirmed from Google snippet |
| S25 | https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt | Previously fetched by B7 | F1 full guidelines page — verbatim passages sourced from Lane B7 |

---

## Catalog

### 1. F1DLE [S1][S2][S3]

- **URL**: https://f1dle.com/ — fetched 2026-04-11; page is JavaScript-gated and returned partial content.
- **What it is**: "The ultimate Formula 1 daily puzzle experience" [S1] — multiple puzzle modes including driver guessing, circuit, car, and season standings challenges.
- **Operational status**: Active. The domain resolves and returns a live page with game modes described. Google Play Store listing (com.f1dle.game) also exists, indicating a mobile app version.
- **Branding**: Uses "F1DLE" as brand name, references "F1" and "Formula 1" throughout. Title is "F1DLE - F1 Daily Puzzles" [S1]. No official F1 logo or licensed asset usage confirmed in accessible content, but F1 wordmark ("F1") appears in the product name itself.
- **Disclaimer**: Absent from all pages fetched [S1][S2][S3]. No "unofficial" or "not affiliated" language found. No F1 trademark acknowledgement found. This is notable because F1's guidelines [S20] require: "This website is unofficial and is not associated in any way with the Formula 1 companies." [OPUS-FOLLOWUP: JavaScript gating prevented full page render; footer content may exist but was not returned. Cannot confirm absence — only non-observation from accessible content.]
- **Licensing disclosure**: None found [S1][S2][S3].
- **Monetization**: None detected on accessible content. No ads, Ko-fi, Patreon, or subscription links visible.
- **Operator identity**: "F1DLE" with contact email contact@f1dle.com [S1]. No individual name disclosed.
- **Notes**: Has a Google Play Store listing (com.f1dle.game) — this places it in the "Apps" category under F1's guidelines [S25], which state "Other Intellectual Property Rights cannot be used in apps." [OPUS-FOLLOWUP: Whether the app uses F1's Other IP Rights (official graphics, artworks, timing data per B7's enumeration) requires inspection of the app itself, not done here.]

---

### 2. Stewardle [S4]

- **URL**: https://stewardle.com/ — fetched 2026-04-11.
- **What it is**: A Wordle-variant F1 driver guessing game — "guess the STEWARDLE in six tries" using a "valid F1 driver name who has raced in the 2014 season or later" [S4]. Despite the name implying steward/penalty content, it is a driver-guessing game, not a penalty-prediction game.
- **Operational status**: Active. Returns full page content.
- **Branding**: Uses the name "Stewardle" (F1-adjacent portmanteau). References F1 driver data (nationality, team, car number, debut year, wins). No F1 logo or official branding assets observed. Color scheme not F1 red.
- **Disclaimer**: Partial. Footer states: "Inspired by Wordle / Created by syhr" [S4]. This credits the Wordle game mechanic and names the creator. It does not include an "unofficial / not affiliated with F1" statement. No F1 trademark acknowledgement.
- **Licensing disclosure**: None [S4].
- **Monetization**: None detected — no ads, donation links, Ko-fi, or Patreon [S4].
- **Operator identity**: Disclosed. "Created by syhr" with link to sy.hr [S4]. Individual operator named.
- **Notes**: Stewardle's creator attribution is unusually transparent for this category — naming an individual. This is one of the few projects with a named human operator.

---

### 3. Who Are Ya? [S5][S6]

- **URL**: https://racing.whoareya.games/ — fetched 2026-04-11.
- **What it is**: "Who Are Ya? is a mystery F1 Racing guessing game" [S5] — players guess a hidden F1 Racing driver in a Wordle-style format with a new driver daily.
- **Operational status**: Active. Page returns content, though JavaScript-dependent for gameplay.
- **Branding**: Title uses "F1 Racing" as a descriptor. No official F1 logo observed. Google Tag Manager embedded.
- **Disclaimer**: Absent from fetched content. Footer links are: "Consent/Cookie Preferences | Privacy Policy | Contact Us" [S5]. No "unofficial" or "not affiliated" language found. No F1 trademark notice.
- **Licensing disclosure**: None [S5][S6].
- **Monetization**: None detected in accessible content [S5].
- **Operator identity**: Privacy policy identifies operator as "Who Are Ya" — the company/project name only, no individual [S6]. No further identity disclosed.
- **Notes**: The privacy policy refers to "the Company" throughout but gives no legal entity name beyond "Who Are Ya" [S6]. This is representative of the category: minimal operator disclosure, no legal entity named.

---

### 4. Driverle / formula1points.com [S7]

- **URL**: https://www.formula1points.com/driverle — redirects to http://www.formula1points.com/driverle/?type=driverle — fetched 2026-04-11.
- **What it is**: "Driverle is a F1 Wordle-like game about finding the right F1 driver!" [S7]. Part of the formula1points.com ecosystem, which also hosts picle, F1Quizle, head2headle, seasonle, and speedle.
- **Operational status**: Active. Returns full page content.
- **Branding**: Site named "formula1points.com" — uses "Formula 1" in the domain. Uses a "Formula1" custom font reference [S7]. References F1 stats throughout.
- **Disclaimer**: Contains an anti-scraping warning: "Oops, it seems you are trying to play from a non-official website! To play Driverle, please go to: www.driverle.com" [S7] — this is a geo/embed protection, not an F1 affiliation disclaimer. No "unofficial/not affiliated with Formula 1" statement found.
- **Licensing disclosure**: None [S7].
- **Monetization**: No direct monetization detected. "Apex Ascent" campaign banner mentioned [S7] but no payment links.
- **Operator identity**: Schema markup identifies author as "Mark Wessel" [S7]. Named individual operator.
- **Notes**: The footer text promotes the broader formula1points.com site: "Brought to you by formula1points.com Check it out to discover unique F1 stats and insights!" [S7]. The "driverle.com" canonical URL noted in the anti-scraping warning — this suggests the game also lives at www.driverle.com (not independently fetched here; treat as same project).

---

### 5. Formudle [S23][S24]

- **URL**: https://formudle.com/ — direct fetch returned 403. Content reconstructed from search snippets and privacy policy search result [S23][S24].
- **What it is**: Multi-game F1 puzzle platform hosting Wordle, Grid (3x3 driver grid), Bingo, and Connections variants. Self-described as "a home for daily F1 challenges where you can test your knowledge of teams, drivers, and iconic F1 moments" [search snippet, S24].
- **Operational status**: Active (search results show current URLs resolving; 403 on direct fetch is likely anti-scraper protection, not site-down).
- **Branding**: Uses "F1" extensively in game naming (F1 Wordle, F1 Grid, F1 Bingo, F1 Connections). Uses driver images and championship imagery.
- **Disclaimer**: Present — partial. Reconstructed from Google snippet [S24]: "Formudle uses images of drivers, championships, and events solely for identification purposes and does not claim ownership rights over them. All rights to these images are held by the drivers and racing organizations, including Formula 1, FIA, and the respective teams." If someone is the owner of any image or trademark and wants it removed, they can contact Formudle for "prompt resolution." This is an image-rights disclaimer, not the full F1-prescribed "unofficial and not associated" text. [OPUS-FOLLOWUP: Could not fetch the page directly to verify. Reconstructed from search snippet — verify verbatim accuracy against live page.]
- **Licensing disclosure**: None found.
- **Monetization**: Unknown due to 403 block. No monetization signals found in search results.
- **Operator identity**: Not disclosed in accessible sources.
- **Notes**: The image-rights disclaimer approach is distinct — it acknowledges others' rights to the imagery used, without explicitly declaring unofficial status. This pattern (image attribution without "unofficial" declaration) is one of two disclaimer sub-types observed in this catalog.

---

### 6. Sportsdle F1 Wordle [S8]

- **URL**: https://www.sportsdle.com/f1/daily-guessing-game — fetched 2026-04-11.
- **What it is**: Daily F1 driver guessing game — "guess the Formula 1 driver using team, nationality, number, and championship clues" [S8]. Part of a multi-sport daily puzzle platform (Sportsdle).
- **Operational status**: Active.
- **Branding**: "Sportsdle" brand with an F1 sub-section. Logo is "sportsdle_logo.png" — not F1-branded [S8]. References F1 driver data throughout.
- **Disclaimer**: None found in fetched content [S8].
- **Licensing disclosure**: None [S8].
- **Monetization**: None detected in accessible content [S8].
- **Operator identity**: "Sportsdle Team" (schema markup author) [S8]. No individual named.
- **Notes**: Sportsdle is a horizontal platform covering multiple sports — F1 is one content category. This is a different organizational pattern from F1-dedicated sites. The F1 data is used incidentally within a broader sports puzzle product.

---

### 7. Driver Grid Game [S9]

- **URL**: https://drivergridgame.com/ — fetched 2026-04-11.
- **What it is**: "A daily motorsport trivia game. Test your knowledge, compete on the leaderboard, and enjoy a premier trivia experience." [S9] — a 3×3 grid format where players match drivers to criteria.
- **Operational status**: Active.
- **Branding**: "Driver Grid Game" — avoids "F1" in the brand name. Uses "motorsport" and "Formula 1" in keyword metadata [S9]. No official F1 logo assets observed.
- **Disclaimer**: None found in fetched content [S9]. No "unofficial" statement visible.
- **Licensing disclosure**: None [S9].
- **Monetization**: Free, price "0" [S9]. No payment links detected. Leaderboard suggests social engagement, not monetization.
- **Operator identity**: "Driver Grid Game" as organization name — no individual named [S9].
- **Notes**: The choice of "motorsport" rather than "F1" or "Formula 1" in the brand name is a notable pattern variant — the site uses F1 data but avoids F1 wordmark branding at the name level, then uses "Formula 1" only in metadata keywords.

---

### 8. RaceGrids [S10]

- **URL**: https://www.racegrids.com/ — fetched 2026-04-11; minimal content returned.
- **What it is**: Multi-game F1 platform: Immaculate Grid (3×3), Connections, and a season-long predictions league [S10 title].
- **Operational status**: Active (resolves; site loads per search results).
- **Branding**: "RaceGrids" — uses neither "F1" nor "Formula 1" in the brand name. Game names (Immaculate Grid, Connections) are genre terms, not F1 trademarked terms.
- **Disclaimer**: Not returned in minimal fetch [S10]. [OPUS-FOLLOWUP: Page likely requires JavaScript to render footer content. Could not verify presence or absence of disclaimer.]
- **Licensing disclosure**: Not found.
- **Monetization**: Not detected.
- **Operator identity**: Not disclosed in accessible content.
- **Notes**: Branding follows the "genre-name rather than F1-name" pattern. "Immaculate Grid" borrows from the Immaculate Grid football game genre, not from F1 directly.

---

### 9. Guess the F1 Driver [S11]

- **URL**: https://www.guessthef1driver.com/ — fetched 2026-04-11.
- **What it is**: Driver identification game — "All F1 Drivers with 30+ Starts" [S11]. Guessing based on profile/helmet images.
- **Operational status**: Active.
- **Branding**: Brand name is "Guess the F1 Driver" — uses F1 wordmark in the game name. Logo is a helmet icon (not F1's official logo) [S11].
- **Disclaimer**: None found in fetched content [S11]. No "unofficial" statement, no trademark notice.
- **Licensing disclosure**: None [S11].
- **Monetization**: Analytics via Plausible.io. No monetization links found [S11].
- **Operator identity**: Not disclosed [S11].
- **Notes**: Uses F1 wordmark directly in brand name without disclaimer. One of the starker examples of F1 trademark incorporation without any offsetting disclosure.

---

### 10. FastF1 (Python library) [S12][S13][S14]

- **URL**: https://github.com/theOehrly/Fast-F1 and https://docs.fastf1.dev — fetched 2026-04-11.
- **What it is**: "FastF1 is a python package for accessing and analyzing Formula 1 results, schedules, timing data and telemetry." [S12] — data access library, not a game.
- **Operational status**: Active. Version 3.8.x current as of fetch. Actively maintained on GitHub and PyPI.
- **Branding**: "FastF1" brand name does not use F1 wordmark directly, but README contains the full trademark notice: "F1, FORMULA ONE, FORMULA 1, FIA FORMULA ONE WORLD CHAMPIONSHIP, GRAND PRIX and related marks are trade marks of Formula One Licensing B.V." [S12].
- **Disclaimer**: Present — full. Both GitHub README and documentation site carry: "FastF1 and this website are unofficial and are not associated in any way with the Formula 1 companies." [S13] This is verbatim the disclaimer text specified in F1's guidelines [S20].
- **Licensing disclosure**: MIT License [S14]. Open source, free to use.
- **Monetization**: None found (library distributed via PyPI, free).
- **Operator identity**: Disclosed. Maintained by Philipp Schäfer; contact email provided [S13].
- **Notes**: FastF1 is the most legally careful project in this catalog — it carries the exact disclaimer text F1's guidelines prescribe for unofficial fan websites, plus the full trademark notice. It is also the only project that publishes a formal open-source license. This appears to be the exemplary compliance case for a data-tools project. [OPUS-FOLLOWUP: FastF1 accesses F1 timing data via the jolpica-f1 API — whether that data access itself is licensed by F1 is not established here.]

---

### 11. Jolpica-F1 API [S15][S16]

- **URL**: https://github.com/jolpica/jolpica-f1 and https://jolpi.ca/ — fetched 2026-04-11.
- **What it is**: "An open source API for querying Formula 1 data, with backwards compatible endpoints for the soon to be deprecated Ergast API." [S15] — community-maintained F1 data API that succeeded the Ergast API (shut down end of 2024).
- **Operational status**: Active. Serving live requests; FastF1 3.x uses it as backend.
- **Branding**: "Jolpica-F1" — does not use F1 wordmark in the brand name. Domain jolpi.ca. Search results surface the trademark notice: "F1, FORMULA ONE, FORMULA 1, FIA FORMULA ONE WORLD CHAMPIONSHIP, GRAND PRIX and related marks are trade marks of Formula One Licensing B.V." [S15 via search snippet].
- **Disclaimer**: Partial. The search-result snippet shows the trademark notice and "content is for fan use, dedicated to the FIA FORMULA ONE WORLD CHAMPIONSHIP" [S15 search snippet]. Full TERMS.md exists in the repository but was not successfully fetched (linked, not displayed). [OPUS-FOLLOWUP: The TERMS.md content was not extracted — whether jolpica-f1 carries a full "unofficial and not associated" disclaimer is not confirmed here.]
- **Licensing disclosure**: Apache-2.0 license [S15].
- **Monetization**: Ko-fi donations solicited to "break-even during the 2026 season" (~$45/month hosting costs) [S15]. This is a minimal cost-recovery model, not commercial.
- **Operator identity**: Partially disclosed — "maintained by a small group of volunteers" [S15]. No individual names surfaced in accessible content.
- **Notes**: Jolpica-F1 is infrastructural — it is the data layer that many of the game projects above implicitly depend on for driver stats, race results, etc. Its disclaimer posture is therefore upstream of the game layer. The Ko-fi donation model is the only example of active fundraising in this catalog at the infrastructure level.

---

### 12. Box, Box! (BoxBox) [S17]

- **URL**: https://github.com/BrightDV/BoxBox — fetched 2026-04-11.
- **What it is**: "Unofficial Android and web app for Formula 1 and Formula E fans!" [S17] — a news/schedule/results viewer app, not a game.
- **Operational status**: Active on GitHub (actively maintained Flutter project).
- **Branding**: "Box, Box!" brand — colloquial F1 phrase but not an official F1 trademark. Does not use F1 wordmark as brand name.
- **Disclaimer**: Present — explicit. "Box, Box! is unofficial software and in no way associated with the Formula 1 group of companies nor the Formula E group of companies." [S17] This is semantically equivalent to F1's prescribed disclaimer text [S20], if not verbatim identical.
- **Licensing disclosure**: GNU General Public License v3.0 [S17]. Open source, free software.
- **Monetization**: None. Developer notes: "I'm developing this app in my free time, so I appreciate feedback and welcome PRs!" [S17].
- **Operator identity**: Disclosed. GitHub user BrightDV — individual developer, open source project.
- **Notes**: This project is notable for (a) carrying a full unofficial disclaimer despite being on GitHub rather than a public-facing website, (b) using GPLv3 rather than MIT — a copyleft license that ensures derivative works remain open source, and (c) covering Formula E as well as F1.

---

### 13. TracingInsights [S19]

- **URL**: https://tracinginsights.com/data/ — fetched 2026-04-11.
- **What it is**: F1 data analytics and visualization tool — "Your one-stop home for unparalleled F1 insights" providing telemetry, lap times, and race results from 1950 to present [S19].
- **Operational status**: Active.
- **Branding**: "TracingInsights" — no F1 wordmark in brand name. References "F1" and "Formula 1" in content.
- **Disclaimer**: Present — detailed. "TracingInsights is not affiliated with Formula 1, FIA, or any F1 team." Plus "unofficial and are not associated in any way with the Formula 1 companies" and "a non-commercial, fan-made application." [S19] Also includes full per-brand trademark notices: "F1, FORMULA ONE, FORMULA 1, FIA FORMULA ONE WORLD CHAMPIONSHIP, GRAND PRIX and related marks are trade marks of Formula One Licensing B.V." plus Ferrari, Mercedes, Red Bull, McLaren trademarks.
- **Licensing disclosure**: Not explicitly stated in fetched content.
- **Monetization**: Present — multi-channel. "Affiliate links" (site receives commission on click-through purchases) [S19]. GitHub Sponsors, Patreon, and "Buy Me a Coffee" listed [S19].
- **Operator identity**: "TracingInsights" organization; GitHub org @TracingInsights. No individual named.
- **Notes**: TracingInsights is the most transparent about monetization in this catalog and simultaneously one of the most careful about disclaimers. The combination of affiliate links + Patreon + GitHub Sponsors represents a non-trivial monetization stack for a "non-commercial, fan-made" application — this is a tension worth flagging. [OPUS-FOLLOWUP: Whether this combination crosses F1's "materially commercial manner" threshold under the Fans definition in B7's Passage 5 is not determinable here. The affiliate link model in particular involves revenue from user traffic, which may intersect with "build traffic and/or following to a website... in order to sell goods or services."]

---

### 14. F1 Ocean [S18]

- **URL**: https://www.f1ocean.com/ — disclaimer page fetched 2026-04-11.
- **What it is**: F1-themed wallpaper site — free wallpapers for personal, non-commercial use [S18].
- **Operational status**: Active.
- **Branding**: "F1 Ocean" — descriptive name without F1 wordmark. Social presence at @f1ocean on Instagram and Threads.
- **Disclaimer**: Present — full. "F1 Ocean is an independent, fan-created project and is not affiliated with, endorsed by, or connected to Formula One, Formula One Management (FOM), the FIA, or any Formula 1 teams, drivers, or sponsors." [S18] Plus image-rights notice: "F1 Ocean does not claim ownership of any photographs or copyrighted materials used to create these wallpapers. All photographs remain the copyright of their original owners." [S18]
- **Licensing disclosure**: Images "offered free for personal, non-commercial use only" [S18]. No open-source license stated (wallpaper site, not code).
- **Monetization**: "Support F1 Ocean" link to buymeacoffee.com/f1ocean — voluntary donations [S18].
- **Operator identity**: Not individually named.
- **Notes**: F1 Ocean's disclaimer is the most comprehensive in the catalog for a non-code project — explicitly names FOM and FIA, explicitly states "independent, fan-created." The buy-me-a-coffee model is cost-neutral intent signaling (as opposed to ad revenue or subscriptions).

---

## Pattern Analysis

### 12-Project Summary Table

| Project | Disclaimer present? | Type | Monetization | Operator named? | F1 wordmark in brand? |
|---------|--------------------|----|-------------|----------------|----------------------|
| F1DLE | Not found (JS-gated) | Game | None | No (email only) | Yes ("F1DLE") |
| Stewardle | Partial (creator credit only) | Game | None | Yes (syhr) | No |
| Who Are Ya? | Not found | Game | None | No | No |
| Driverle/formula1points.com | Not found (anti-scrape notice) | Game | None | Yes (Mark Wessel) | Yes ("formula1points") |
| Formudle | Partial (image attribution) | Game platform | Unknown | No | Yes ("F1 Wordle" etc.) |
| Sportsdle F1 | Not found | Game (multi-sport) | None | No | Yes ("F1 Wordle") |
| Driver Grid Game | Not found | Game | None | No | No |
| RaceGrids | Unknown (JS-gated) | Game platform | None detected | No | No |
| Guess the F1 Driver | Not found | Game | None | No | Yes ("F1 Driver") |
| FastF1 | Full (exact prescribed text) | Data library | None | Yes (Philipp Schäfer) | No |
| Jolpica-F1 | Partial (trademark notice) | Data API | Ko-fi (cost recovery) | Partial (volunteers) | No |
| Box, Box! | Full (unofficial declaration) | News app | None | Yes (BrightDV) | No |
| TracingInsights | Full (detailed) | Data tool | Affiliate + Patreon + BmC | No | No |
| F1 Ocean | Full (detailed) | Wallpapers | Buy Me a Coffee | No | No |

### Modal behavior

The **modal pattern** across the 14 entries is:

1. **No disclaimer** — 7 of 14 projects (F1DLE, Who Are Ya?, Driverle, Sportsdle, Driver Grid Game, Guess the F1 Driver, and RaceGrids unconfirmed) show no disclaimer or "unofficial" statement in accessible content. Of those 7, several could not be fully rendered due to JavaScript gating — absence is non-observation, not confirmed absence for JS-gated sites.

2. **No monetization** — 11 of 14 projects show no monetization in accessible content. Three exceptions: Jolpica-F1 (Ko-fi, cost-recovery), TracingInsights (affiliate + Patreon + BmC), and F1 Ocean (Buy Me a Coffee).

3. **No operator named** — 9 of 14 projects do not disclose an individual operator. Exceptions: Stewardle (syhr), Driverle (Mark Wessel), FastF1 (Philipp Schäfer), Box, Box! (BrightDV).

4. **F1 wordmark used in brand name** — 5 of 14 projects use "F1," "Formula 1," or "Formula" in their project/brand name (F1DLE, Driverle via formula1points, Formudle, Sportsdle "F1 Wordle," Guess the F1 Driver). The other 9 use generic or descriptive names.

### The two disclaimer sub-populations

Among the 7 projects with some form of disclaimer:

- **Full unofficial declaration** (text matches or closely matches F1's prescribed language [S20]): FastF1, Box, Box!, TracingInsights, F1 Ocean.
- **Image-attribution-only disclaimer** (acknowledges IP ownership but does not declare unofficial status): Formudle.
- **Creator credit only** (Wordle inspiration credit, no F1 disclaimer): Stewardle.

The full-disclaimer projects are **all data/tool/content projects**, not games. The game-category projects either have no disclaimer or have only a partial one.

**The split by category:**
- Game-format projects (daily puzzles, guessing games): 9 projects — **0 carry a full F1 unofficial disclaimer** based on accessible content.
- Data/tool/content projects: 5 projects — **4 of 5 carry a full unofficial disclaimer**.

This is the central pattern finding. [OPUS-FOLLOWUP: Pattern is based on 14 projects, several of which could not be fully rendered. JavaScript-gated game sites may have footer disclaimers not returned in fetches. The split may be less clean on full inspection.]

### What the operational survival of game projects implies

All 9 game projects are live and operational as of 2026-04-11. None were found to have been taken down by F1 or to have received public notice of F1 enforcement. Lane 1C's claim that these projects "operate publicly without takedowns" is supported by operational status as observed today, but:

- No evidence of tacit approval was found (no F1 statement, no public acknowledgement, no licensing arrangement disclosed by any game project).
- Operational survival does not equal approval. [OPUS-FOLLOWUP: Whether F1 is aware of these specific projects and has chosen not to act, is unaware, or has a non-public policy of tolerance is not determinable from public sources. This is an inference from non-action, not from evidence of permission.]

---

## Enforcement History

### F1 vs. Content Creators — August 2024 [S21][S22]

In August 2024, Formula 1 sent cease-and-desist letters to US-based content creators (social media, podcast, merchandise) demanding they stop using "F1" in their usernames and branding for monetization purposes. Sources [S21][S22]:

From [S21]: "Formula 1 has been keeping busy during the summer shutdown by shutting down some of your favorite content creators" (paraphrase of creator "Leo"). F1 required creators to stop using "F1" for monetization. Those who did not comply "face having their channels and accounts removed."

From [S22] (author self-qualified as "not fully versed in the intricacies"): "Several content creators in the Formula 1 community have reported receiving cease and desist letters from Formula 1's legal team, demanding that they change their usernames and remove any reference to 'F1' from their branding."

**What this enforcement action targeted**: Username/branding use of "F1" by monetized content creators (social, podcast, merchandise). No specific games or puzzle sites were named in either source.

**What this enforcement action did NOT target** (based on available public record): Any of the 9 game projects in this catalog. No public record was found of F1 serving takedown notices or C&D letters on any of the daily-puzzle or data-tool projects above.

**Caveat**: Absence of public enforcement record does not establish absence of enforcement. Private settlements, informal requests, or voluntary preemptive rebrandings would not appear in public search results. [OPUS-FOLLOWUP: Any creator who received a private C&D and complied quietly would be invisible to this search. The "no enforcement" finding is weak-positive at best.]

### NYT vs. Wordle clones — 2024

In March 2024, the New York Times filed DMCA takedown requests against ~1,900 GitHub repositories forking Reactle (a Wordle clone coded in React). [Source: Axios/PCGamer reporting, surfaced in search but not fetched as these are not F1 enforcement actions.] This is relevant context because several F1 puzzle games (Stewardle, Formudle, F1DLE) use Wordle-derived mechanics, but the takedown was about game code copyright, not about the F1 content layer. No F1 puzzle game was specifically targeted in the NYT action based on search results.

### No documented F1 enforcement against F1 data tools

No public record was found of F1 or FOM acting against FastF1, Jolpica-F1, or similar data-access tools. The Ergast API (which preceded Jolpica-F1) operated for over a decade and was deprecated by its maintainer, not taken down by F1. [OPUS-FOLLOWUP: The Ergast API shutdown reason was operator decision, not F1 pressure — but this is widely reported, not directly verified here.]

---

## Cross-Reference to F1's Guidelines (B7 Findings)

Lane B7 established four load-bearing passages from F1's published guidelines. Below is how the catalog maps against each.

### The Games clause (B7 Passage 3)

F1's text [S25, B7 Passage 3]: "Our Permitted Word Marks cannot be used to brand any game. Other Intellectual Property Rights including those from the Formula 1 companies' official games cannot be used in third party games."

**Catalog mapping**: 5 of the 9 game projects use F1 Permitted Word Marks ("F1," "Formula 1") in their brand name (F1DLE, Formudle, Sportsdle, Guess the F1 Driver, Driverle via formula1points). Under the Games clause's first sentence, this appears to be directly contrary to F1's stated policy. The other 4 games avoid F1 wordmarks in their brand name (Stewardle, Who Are Ya?, Driver Grid Game, RaceGrids) — which is consistent with the first sentence, though the second sentence (about Other IP Rights in the game content itself) still applies if the game uses F1's official data, artworks, or statistics. [OPUS-FOLLOWUP: Whether F1 trivia data (driver career stats, race results, nationality) constitutes "Other Intellectual Property Rights" within the Games clause depends on how "Statistics" in B7's Passage 1 enumeration is scoped. This is not resolvable here.]

### The Apps clause (B7 Passage 4)

F1's text [S25, B7 Passage 4]: "Other Intellectual Property Rights cannot be used in apps."

**Catalog mapping**: F1DLE has a Google Play app (com.f1dle.game). The app uses F1 driver, circuit, and season data — if any of this constitutes F1's "Other IP Rights" (e.g., statistics per B7's list), the Apps clause applies. No licensing disclosure was found for the app. [OPUS-FOLLOWUP: The app's actual assets cannot be inspected from public web pages alone. Whether it uses F1's official timing data, official artworks, or other enumerated Other IP Rights is not established here.]

### The Fans definition (B7 Passage 5)

F1's text defines Fans as acting "without doing so in a materially commercial manner." Commercial markers include "build traffic and/or following to a website... in order to sell goods or services."

**Catalog mapping**: 12 of 14 projects show no monetization. 2 have multi-channel monetization (TracingInsights), 1 has cost-recovery donations (Jolpica-F1), 1 has voluntary coffee donations (F1 Ocean). Based on the Fans definition, the non-monetized game projects fit the "Fan" framing more cleanly than TracingInsights, which has affiliate links. [OPUS-FOLLOWUP: Whether affiliate links on a fan analytics site cross F1's "materially commercial" threshold is a legal interpretation question, not an empirical one.]

### The unofficial disclaimer requirement (F1 guidelines fan website requirement)

F1's guidelines [S20] prescribe: "This website is unofficial and is not associated in any way with the Formula 1 companies. F1, FORMULA ONE, FORMULA 1, FIA FORMULA ONE WORLD CHAMPIONSHIP, GRAND PRIX and related marks are trade marks of Formula One Licensing B.V." — to be placed "in the footer of the landing and/or home page."

**Catalog mapping**: Of the 9 game projects, 0 carry this prescribed text based on accessible content (though JS-gated sites could not be fully confirmed). Of the 5 data/tool projects, 3 carry it (FastF1, TracingInsights, Box, Box!). FastF1's documentation site [S13] carries it verbatim. The prescribed disclaimer text is demonstrably known to some F1 fan project operators — which makes its systematic absence from game-format projects more notable. [OPUS-FOLLOWUP: Absence from JS-rendered pages cannot be confirmed without browser-based fetching. This pattern could be weaker than it appears.]

---

## What I Did NOT Check

- **BoxBoxd** (https://boxboxd.fun/) — scoped out per task spec (B8-1 handles). Search results confirm it exists (App Store, Google Play listings) but it was not cataloged here.
- **Gridle** (if a standalone project distinct from Formudle's Grid game) — search results for "Gridle" returned Formudle's Grid game and generic grid game results, but no standalone "Gridle" project with a separate domain was found. Could be defunct, or the name may not correspond to a live project distinct from what was cataloged.
- **F1Guessr / F1 Guessr** — searches returned GeoGuessr community maps of F1 tracks, not a standalone "F1Guessr" dedicated site. No standalone project matching this name was found. [OPUS-FOLLOWUP: The name may refer to a very small or ephemeral project. Exhaustive search not performed.]
- **F1 Discord bots** — no public documentation for specific F1-themed Discord bots was found in web search. Discord bot projects are typically private to servers and have no web-accessible landing pages.
- **F1 prediction leagues** (community-run, not official) — RaceGrids.com includes a season-long predictions league, cataloged above. Community-only prediction spreadsheets and Discord threads were not cataloged.
- **GitHub repo projects** (e.g., emcrald/F1-Driver-Wordle, surfaced in search) — these are code repositories, not deployed games. Not cataloged as they are development artifacts rather than fan-facing projects.
- **Sporcle F1 quizzes / JetPunk F1 quizzes** — platform-hosted quizzes (user-created content on quiz platforms). Not individually cataloged — they operate under the host platform's legal agreements, not independently.
- **Higher or Lower F1 Grand Prix Wins** (higherorlowergame.com/f1) — surfaced in search, not fetched. Would add to the game tally but was cut for time.
- **Ergast API** — shut down by its maintainer at end of 2024; not operational. Historical context only.
- **f1dataR (R package)** — similar posture to FastF1 (data library with unofficial disclaimer). Not fetched individually; would likely follow the FastF1 pattern.

---

## Flagged for Opus Follow-Up

1. **[OPUS-FOLLOWUP: JS-gating caveat]** — F1DLE, Formudle, Who Are Ya?, and RaceGrids are all JavaScript-rendered single-page apps. Footer content (where disclaimers live) may exist but was not returned in fetches. The "no disclaimer found" findings for these projects are non-observations under JS constraint, not confirmed absences. Browser-based inspection needed to confirm.

2. **[OPUS-FOLLOWUP: F1DLE app IP question]** — F1DLE has a Google Play Store app. Whether the app uses F1's "Other Intellectual Property Rights" (official graphics, artworks, statistics per B7 enumeration) cannot be determined from web fetches alone.

3. **[OPUS-FOLLOWUP: Tacit tolerance vs. non-awareness]** — Operational survival of 9 game projects as of 2026-04-11 is consistent with (a) F1 tacitly tolerating daily-puzzle fan games, (b) F1 being unaware of them, or (c) F1 having no enforcement bandwidth for small projects. No public evidence distinguishes these. Inference from non-action only.

4. **[OPUS-FOLLOWUP: Formudle disclaimer verbatim verification]** — Formudle's image-attribution disclaimer was reconstructed from a Google search snippet, not a direct page fetch (403 on all attempts). Verbatim accuracy needs live-page verification.

5. **[OPUS-FOLLOWUP: TracingInsights commercial threshold]** — TracingInsights claims "non-commercial, fan-made" but has affiliate links + Patreon + GitHub Sponsors. Whether this combination crosses F1's "materially commercial manner" threshold under the Fans definition warrants analysis beyond empirical observation.

6. **[OPUS-FOLLOWUP: F1 statistics as Other IP Rights]** — Whether F1 driver career statistics (wins, nationality, team history, car number) constitute "Statistics" under B7's enumeration of Other IP Rights is unresolved. If yes, every data-driven guessing game in this catalog uses Other IP Rights in a game, triggering the Games clause. If no, the Games clause applies only to assets, not to factual data. This is the most load-bearing ambiguity for any prix-guesser-like project.

7. **[OPUS-FOLLOWUP: Jolpica-F1 TERMS.md content]** — The TERMS.md file in the jolpica-f1 repository was referenced but not fetched. Its content may contain the full unofficial disclaimer or additional legal restrictions on derivative use.

8. **[OPUS-FOLLOWUP: C&D to US creators in Aug 2024]** — The enforcement action against content creators used "F1" in usernames/branding for monetized content. Whether F1 has a separate or coordinated policy toward game projects (as opposed to social media creators) is not established. The two categories may be treated differently by F1's legal team.

---

## Qualifications

- **Fetch date**: All fetches performed 2026-04-11. Project status, disclaimers, and content may change. This is a point-in-time snapshot.
- **JavaScript constraint**: Several major game projects (F1DLE, Formudle, Who Are Ya?, RaceGrids) are JavaScript-rendered single-page applications. The WebFetch tool returns partial content for these — footer text, modals, and dynamically loaded content were not captured. Claims of "no disclaimer found" for JS-gated sites are non-observations, not confirmed absences.
- **Catalog is partial**: 14 projects cataloged from a larger ecosystem. Additional F1 fan projects exist (Discord bots, Reddit tools, GitHub repos, GeoGuessr community maps, Sporcle quizzes) that were not individually cataloged.
- **Only public-facing pages checked**: No attempt to inspect game source code, app bundles, or backend data pipelines. Whether projects use F1's official assets internally cannot be determined from homepage fetches.
- **No legal opinions**: This document records empirical observations about how projects present themselves publicly. It does not determine whether any project infringes F1's IP or falls within any legal protection. Legal interpretation is B8-1 and Opus-level work.
- **Enforcement findings are weak**: No public record of F1 enforcement against game projects was found. This is a weak positive, not a confirmed finding of tolerance. Private or settled actions would be invisible.
- **B7 cross-reference is observational**: The comparison of project behavior to F1's guidelines text describes the gap between stated policy and operational reality. It does not predict F1's enforcement posture or any project's legal risk.
