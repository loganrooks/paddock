---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-synthesis
synthesizer_model: claude-sonnet-4-6
agent_type: general-purpose
tools_used: [Read, Grep, Glob]
predecessor_lanes:
  - 01-boxboxd-deep-read.md
  - 02-f1-fan-project-survey.md
  - 03-analogous-fan-projects.md
  - 04-commercial-threshold.md
  - 05-nominative-fair-use.md
audit_chain_predecessors:
  - wave-2-lane-b7-f1-legal-ambiguity.md
output_file: 06-synthesis.md
not_legal_opinion: true
---

# B8 — Research Program Synthesis

**Synthesizer:** Claude Sonnet 4.6 (general-purpose agent, Read/Grep/Glob only).
**Classification:** Composition lane. All web research is complete. This document composes findings from 5 parallel research lanes into a practical answer to the project owner's questions.
**Not a legal opinion.** Every interpretive synthesis is flagged `[OPUS-FOLLOWUP]`. Residual uncertainty is named, not smoothed over.

---

## Lane Sources Table

| ID  | File | Lane | Scope |
|-----|------|------|-------|
| [L1] | `01-boxboxd-deep-read.md` | B8-1 | BoxBoxd legal posture (disclaimer, monetization, licensing), complete game mode inventory, product shape, and differentiation surface vs. prix-guesser |
| [L2] | `02-f1-fan-project-survey.md` | B8-2 | Breadth survey of 14 F1 fan projects; patterns across branding, disclaimers, monetization, enforcement history |
| [L3] | `03-analogous-fan-projects.md` | B8-3 | Cross-domain fan project enforcement history (Nintendo, SEGA, Lucasfilm, WB, motorsport); what triggers vs. tolerates enforcement |
| [L4] | `04-commercial-threshold.md` | B8-4 | Donation/cost-recovery vs. "commercial" under F1's policy text, US §107, UK CDPA, Canadian §§29 and 29.21 |
| [L5] | `05-nominative-fair-use.md` | B8-5 | Nominative/referential use doctrine (US, UK/EU, Canada); identify-vs-brand distinction; circuit IP ownership; driver name rights |
| [B7] | `wave-2-lane-b7-f1-legal-ambiguity.md` | Audit chain | Opus re-fetch of F1's full guidelines; surfaced Games, Apps, Simulators subsections; established circuit IP disclaimer; resolved Lane 1C's two-passage blind spot |

---

## TL;DR for the Project Owner

12 headline findings, organized by the 6 user questions:

**Legal posture (Q1)**
1. Prix-guesser as currently scoped — private, friends-only, no donations, no public access — sits in the lowest-risk posture available for an F1 fan game. No F1 enforcement action against a project of this profile was found anywhere in the research.
2. The risk does not come from F1's enforcement history (no documented action against F1 fan games of any kind found). The risk comes from the possibility that if enforcement *were* ever triggered, F1's published text contains three prohibitions (Games, Apps, Simulators) that apply on their face and a narrow carveout ("private educational use") whose fit to a party game is uncertain. The project navigates a legally ambiguous space, not a legally cleared one.
3. The single largest protective factor is strict private-only access. If the project goes public-facing or achieves mainstream visibility, the enforcement-trigger literature from analogous domains (B7 + L3) shows risk escalates sharply.

**Donation threshold (Q2)**
4. Cost-recovery donations appear to fall outside F1's stated "materially commercial" examples under F1's own policy text — but F1 retains discretion and the text provides no positive confirmation. Under US copyright, cost-recovery is probably not "commercial" under the Harper & Row test. Under **Canadian §29.21**, the word "solely" creates the highest doctrinal risk: any monetary flow creates a question whether the use is *solely* non-commercial. This is the live risk for a Canadian project owner.
5. No documented case was found where small-scale donation (Ko-fi/tip-jar) was the *specific* enforcement trigger in isolation. Enforcement-linked donation cases involved either large-scale crowdfunding ($50K+), explicit IP trademark in the Patreon account name, or platform-level advertising revenue — not modest voluntary tips.

**Implicit branding (Q3)**
6. Dropping the F1 wordmark and logo meaningfully improves the trademark analysis — it removes the clearest infringement vectors and directly addresses F1's Games guideline prohibition on "Permitted Word Marks to brand any game." But it does not produce a safe harbor. What remains: circuit operators' trademark rights (F1 explicitly disclaims these — they belong to each circuit's owner), driver personality/publicity rights, and trade dress confusion if F1's official visual aesthetic is mimicked.

**BoxBoxd (Q4)**
7. BoxBoxd has **no GeoGuessr-style mode** and **no private-room / host-screen architecture**. All 9 modes (6 daily games + 3 quizzes) are knowledge-domain transpositions of existing puzzle formats (Wordle, Connections, Contexto, Elo, Guess Who, survey). Prix-guesser's anchor — authored GeoGuessr-style F1 geography rounds for friends-on-couch/private-room group play — is entirely absent from BoxBoxd's product.
8. BoxBoxd carries a consistent site-wide disclaimer and no disclosed licensing arrangement; it is operating as an implicit fan project. It has a possible B2B commercial layer (For Brands, For Broadcasters) that may complicate its "fan" posture more than prix-guesser's private-room model.

**F1 fan project landscape (Q5)**
9. The modal F1 fan project in this research is: daily puzzle game (Wordle/Connections variant), no disclaimer, no monetization, no named operator, using F1 wordmarks in the brand name — and operating publicly without documented enforcement. Data/tool projects are the opposite: full disclaimers, named operators, some monetization (donations/affiliate). The split correlates with project type, not with risk calibration.

**Analogous domains (Q6)**
10. Commercial competition with an official product, not monetization level, is the dominant enforcement trigger across all domains studied. Being free, non-commercial, and low-visibility does not guarantee immunity (AM2R, Pokémon Prism were both taken down despite being free). Being a GeoGuessr-for-F1 analog sits entirely outside F1's current official product portfolio, which reduces competitive concern as a trigger.
11. F1 has documented one enforcement action: C&D letters to *monetized content creators* (social media, podcast, merchandise) using "F1" in usernames/branding, in August 2024. No documented enforcement action against any F1 fan puzzle game was found.
12. [SYNTHESIS-LEVEL OPUS-FOLLOWUP: L2's finding that 9 F1 game projects operate publicly without documented enforcement, combined with L3's finding that commercial competition is the primary trigger, composes to a tentative picture: F1 is tolerating these projects because they do not compete with any official F1 quiz/puzzle product. This tolerance is not approval and does not predict future behavior, especially if F1 ever launches an official quiz product. Composition is cross-lane inference, not a finding from either lane alone.]

---

## Question 1 — Legal Conclusions and Consequences for Prix-Guesser (As Currently Scoped)

### Current scope

Prix-guesser is currently: private (friends-and-family access only), no donations, no public distribution, no F1 wordmark in branding. The project describes itself as a GeoGuessr-style F1 geography game for private group play.

### The relevant legal structure (composing B7 + L4 + L5)

B7 established the load-bearing structure from F1's guidelines. Four passages bear on prix-guesser:

**The carveout** (B7, Passage 1, Section 2):
> "Limited use of our Other Intellectual Property Rights for educational purposes may be acceptable where the use is justified, limited, and non-commercial. However, please note, this does not include public postings such as YouTube, websites and social media. It must be for a private, educational purpose only."

**The Games prohibition** (B7, Passage 3, Section 4):
> "Our Permitted Word Marks cannot be used to brand any game. Other Intellectual Property Rights including those from the Formula 1 companies' official games cannot be used in third party games."

**The Apps prohibition** (B7, Passage 4, Section 4):
> "Other Intellectual Property Rights cannot be used in apps. For further guidance on timing data please see Timing Data category below."

**The Simulators prohibition** (B7, Passage 2, Section 4):
> "Motorsport simulators and/or software that simulates auto racing (including those that are digital only or those that incorporate physical elements such as racing car chassis) should not make any use of the FORMULA 1 Rights without an express written license."

B7 found that Section 2's carveout is narrow: it permits "limited use of Other Intellectual Property Rights" for *educational* purposes, but it does not override Section 4's per-category prohibitions (Games, Apps, Simulators) by its terms. F1 never defines "educational," and a party game's fit to "educational" is uncertain at best.

**Circuit IP disclaimer** (B7, LQ-B7.6, Item 3; L5, Section 4.1):
> "If you would like to enquire about licensing any of the circuits' intellectual property rights, such as circuit outlines, please contact the owner of the IP directly."

F1 explicitly disclaims circuit IP. Prix-guesser's core geographic mechanic engages circuit operators' IP, not F1's. This is the most favorable single finding for the circuit-content side. The exposure is redirected to individual circuit operators (each is a separate rights holder), not to F1. [L5, §4.1]

### Operational risk posture: private-only, no donations

At this scope, the realistic operational risk is low. Evidence for this reading:

1. **No enforcement history** against any F1 fan puzzle game found anywhere in this research. [L2, Enforcement History section] L2 found 9 F1 daily-puzzle games operating publicly without documented enforcement; a private game is lower-profile than any of them.
2. **Cross-domain enforcement patterns** (L3) show enforcement correlates with: (a) competition with an official product; (b) mainstream platform visibility; (c) large-scale crowdfunding; (d) explicit trademark use. Prix-guesser as currently scoped has none of these.
3. **F1's only documented recent enforcement** (L2, §Enforcement History) targeted *monetized content creators* using "F1" in their social media usernames — not puzzle games.

**What this does NOT mean**: the project is in a "cleared" legal zone. B7's conclusion is that prix-guesser "navigates an under-defined intersection of three prohibitions and one narrow conditional carveout." The private-only posture reduces the enforcement trigger risk to near-zero, but it does not resolve the doctrinal question of whether a strict textual application of F1's Games and Apps prohibitions would apply.

### Risks if scope expands

Per-scenario reading (composing L3 + L4 + B7):

| Expansion | Risk Change | Basis |
|-----------|------------|-------|
| Goes public-facing (anyone can access) | **Significant increase** | B7's carveout explicitly excludes "public postings such as YouTube, websites and social media"; L3's #2 trigger is mainstream visibility. |
| Adds donations (Ko-fi/Patreon) | **Moderate increase (Canadian jurisdiction especially)** | L4's Canadian §29.21 "solely non-commercial" risk; F1's undisclosed interpretation of "materially commercial"; see Q2 below. |
| App Store distribution (iOS/Android) | **Significant increase** | L3's Galaxy in Turmoil case: a Steam distribution announcement triggered a C&D without monetization; the Apps prohibition (B7, Passage 4) applies explicitly. |
| Adds F1 wordmark to branding | **Significant increase** | B7's Games prohibition: "Permitted Word Marks cannot be used to brand any game"; L5's doctrine makes this the clearest infringement vector. |
| Competes with an official F1 quiz product | **Significant increase** | L3's #1 enforcement trigger across all domains; inapplicable currently (no known official F1 quiz product), but status could change. |
| Grows to large public user base | **Scale-dependent increase** | L3's Pokémon Uranium case: 1.5M downloads attracted enforcement that smaller projects had not. |

[OPUS-FOLLOWUP: whether an official F1 quiz/trivia product currently exists or is in development — prix-guesser's competitive concern risk depends on this. L4, §Section 6, found no research on this; it is a gap in the full research program.]

### Content-type rules derivable from B7 + L5

These are not legal requirements — they are what the research suggests is the most defensible posture:

- **Use**: circuit names and driver names as factual identifiers in quiz questions — plausibly nominative/referential use [L5, §3.1–3.2]
- **Use**: third-party venue photographs (not F1-owned still images) — not in Section 2's Other IP Rights enumeration [B7, LQ-B7.3]
- **Use**: publicly available race result data and historical statistics — F1's "Statistics" and "Results and Timing data" are in Section 2's list but fair dealing/nominative use arguments are available; factual data is weakly copyright-protected [L4, L5]
- **Avoid**: F1-owned official artworks, graphics, assets, textures — these are explicitly listed in Section 2's Other IP Rights and are prohibited in games by the Games clause [B7, Passage 3]
- **Avoid**: F1's official typeface — listed in Section 2 [B7, Passage 1]
- **Avoid**: F1's audio/AV content — listed in Section 2 [B7, Passage 1]
- **Avoid**: F1 wordmarks and logos as branding — Games clause prohibition [B7, Passage 3]
- **Consider carefully**: F1-owned photographs labeled as "Still Images" — in Section 2, prohibited in games; use third-party licensed photography instead

[OPUS-FOLLOWUP: this content-type list is synthesizer inference composing B7's Section 2 enumeration with the Games prohibition. It is not reviewed by an IP lawyer and should not be treated as compliant legal guidance. A follow-up requirements_review pass should convert these into testable content-authoring rules.]

---

## Question 2 — Donation-Based Cost Recovery and the "Commercial" Threshold

### F1 policy text reading

L4, Section 1, surveyed all commercial-related language in F1's guidelines. Key findings:

F1's dedicated "Commercial use" subsection (L4, Passage F1-E) restricts "goods/services provided for sale." A donation button is not selling a good or service.

F1's "materially commercial manner" examples (L4, Passage F1-A) are: (1) clickbait to promote commercial offers; (2) building traffic to sell goods/services; (3) excessively repetitive advertising. None describes a passive donation mechanism.

F1's non-commercial carveout (L4, Passage F1-B) requires "non-commercial" use but never defines the term.

**Tentative F1 policy reading**: a pure cost-recovery donation model (no advertising, no merchandise, no tiered Patreon with deliverables) appears to fall outside F1's three stated "materially commercial" examples and outside the goods-for-sale prohibition. But:
- F1 retains explicit discretion: "without doing so in a materially commercial manner, subject to our discretion" [L4, Passage F1-A]
- F1 has published no interpretive guidance on donations
- F1 does not use the words "donation," "Ko-fi," "Patreon," "cost recovery," "profit," or "revenue" anywhere in its guidelines [L4, §Section 1, finding F1-4]

[OPUS-FOLLOWUP L4/OF-1: F1's "non-commercial" condition in the carveout is undefined and F1's discretion reservation means any textual analysis is advisory. F1 could re-characterize any monetization as "materially commercial" at its own discretion. Priority: HIGH.]

### US copyright doctrine

Under Harper & Row (1985), the "crux of the profit/nonprofit distinction is not whether the sole motive of the use is monetary gain but whether the user stands to profit from exploitation of the copyrighted material without paying the customary price." [L4, §Section 2] Cost-recovery donations that produce no profit do not clearly fall within this definition.

Campbell v. Acuff-Rose (1994) confirmed commercial nature is "only one element of the first factor enquiry" and that even commercial use can be fair use if sufficiently transformative. [L4, §Section 2]

**Tentative US reading**: cost-recovery donations probably do not constitute "commercial" use under the Harper & Row test. Even if characterized as technical commerciality, it is non-determinative under Campbell. [L4, §Section 6]

[OPUS-FOLLOWUP L4/OF-2: no case found that directly applies Harper & Row or Campbell to a cost-recovery donation model. This is doctrinal inference.]

### UK copyright doctrine

UK CDPA fair dealing is categorical, not a balancing test. The relevant categories (research, private study) impose "non-commercial purpose" as a threshold gate. [L4, §Section 3] Cost-recovery donations likely satisfy "non-commercial" if no profit is produced. However, the more pressing UK question is whether any CDPA category is available to a fan quiz game in the first place — "entertainment" is not an enumerated fair dealing category. [L4, §Section 3, UK tentative observation]

[OPUS-FOLLOWUP L4/OF-4: UK fair dealing categorical eligibility for a fan quiz game has not been researched; this is the prior question before commercial analysis even arises.]

### Canadian copyright doctrine — the highest doctrinal risk for this project owner

Two paths under Canadian law [L4, §Section 4]:

**§29 fair dealing (research, private study, education, parody, satire):** "Non-commercial" is not an explicit condition of §29. A genuinely educational purpose could support the dealing under the CCH six-factor analysis. Entertainment-primary purpose weakens the argument. [L4, §Section 4]

**§29.21 non-commercial UGC:** This is the most directly relevant Canadian provision. Verbatim text (L4, §Section 4, verbatim from Justice Laws):

> "It is not an infringement for an individual to use an existing published work to create a new work if: (a) the use of, or the authorization to disseminate, the new work or other subject-matter is done **solely for non-commercial purposes**..."

The word "solely" is strict. It is not "primarily" — it is "solely." Any monetary inflow, including cost-recovery donations, creates uncertainty about whether the use is *solely* non-commercial.

**Composition finding (B8 synthesis-level)**: L4's finding that Canadian §29.21's "solely non-commercial" standard is the highest doctrinal risk, combined with the context that the project owner is Canadian, makes this the single most decision-relevant legal research gap in the entire program. No Canadian case was found addressing cost-recovery donations under §29.21. The word "solely" means even zero-profit donations that precisely cover hosting costs face a colorable argument that the use is no longer *solely* non-commercial. [OPUS-FOLLOWUP: this is the top Opus or counsel research priority for the project owner's jurisdiction. L4/OF-3 rated this HIGH priority.]

### Trademark vs. copyright commercial analysis — different doctrines

L4, §Section 7 surfaced a critical distinction the synthesis must preserve:

Copyright's "commercial" factor (§107(1)) is about profit from exploitation of copyrighted material. Trademark's "commercial use" doctrine (Lanham Act "use in commerce") is about whether the mark is used in connection with goods/services in the marketplace — it is about consumer confusion in trade, not profit motive.

**Implication**: accepting donations might not make the use "commercial" for copyright purposes while *simultaneously* potentially constituting "use in commerce" for trademark purposes if the donation creates a nexus between F1 marks and a payment transaction. These are independent analyses. [L4, §Section 7; L5, §7 Application section]

[OPUS-FOLLOWUP L4/OF-6: trademark "use in commerce" analysis for a donation-accepting project was identified as a gap in L4 and is not resolved anywhere in the research program.]

### The solicited vs. unsolicited distinction

L4 (§Section 7, secondary questions) raised the analytical relevance of *soliciting* donations (actively requesting via Ko-fi button) versus *receiving* them passively. Solicitation creates an active nexus between the F1 content and the monetary flow. No authority was found that draws this distinction formally, but it is analytically relevant under the reasoning that solicitation more clearly demonstrates that the F1 content is being leveraged for economic benefit. [L4/OF-7]

### Summary reading for the donation question

| Jurisdiction | Cost-recovery donation reading | Confidence |
|-------------|-------------------------------|------------|
| F1 policy | Tentatively outside "materially commercial" examples; but no positive confirmation, discretion retained | LOW-MEDIUM |
| US copyright | Probably not "commercial" under Harper & Row | LOW-MEDIUM |
| UK fair dealing | Probably satisfies "non-commercial" if cost-recovery only; categorical eligibility is the prior question | LOW |
| **Canadian §29.21** | **Uncertain — "solely" standard; any monetary flow is a risk** | **LOW — highest jurisdictional risk** |
| **Canadian §29** | Less risky — "non-commercial" not explicit; educational framing required | MEDIUM |
| Trademark (all) | Separate analysis; not resolved | UNRESOLVED |

---

## Question 3 — Implicit vs. Explicit F1 Branding

### What dropping the F1 wordmark/logo does

L5, §5.2 summarizes this directly. Dropping explicit marks:
- Eliminates direct infringement of F1's registered word marks (F1™, Formula 1™, Grand Prix™, etc.)
- Directly addresses F1's Games guideline prohibition: "Our Permitted Word Marks cannot be used to brand any game" [B7, Passage 3]
- Eliminates the clearest and most readily-identifiable infringement vector

This is a **meaningful improvement** in the trademark analysis. It is not a safe harbor.

### What dropping explicit marks does NOT eliminate

1. **Circuit operators' trademark rights**: Circuit names (Silverstone, Monza, Suzuka) belong to their respective operators, not F1. F1 explicitly redirects circuit IP inquiries to those operators [B7, LQ-B7.6; L5, §4.1]. Using "Silverstone" to identify a circuit in a quiz question is plausibly nominative/referential use under *New Kids* (L5, §1.2) — the name is necessary to identify the circuit, used minimally, and does not suggest BRDC sponsors the quiz. But this is a per-circuit analysis, not a blanket rule. [L5, §4.4]

2. **Driver name/personality rights**: Driver names as factual identifiers in quiz questions are likely referential/nominative use. Using them to imply endorsement would trigger liability. Using their registered trademarks (e.g., "LH44" logo) would trigger liability. [L5, §6.2]

3. **F1's Other IP Rights remain prohibited regardless of wordmark dropping**: The Games prohibition (B7, Passage 3b) prohibits using "Other Intellectual Property Rights" in third-party games. Dropping the wordmark does not affect this prohibition. F1-owned still images, official artworks/graphics/assets/textures, audio/AV content, and official typeface remain restricted whether or not F1® appears in the project's branding. [L5, §5.2]

4. **Trade dress / overall commercial impression**: If the quiz's visual style, color scheme, or typeface mimics F1's official aesthetic, trade dress claims can arise even without explicit mark use. A clearly unofficial presentation with a disclaimer reduces this risk substantially. [L5, §5.3]

5. **Implicit association concern**: Using accurate team colors, circuit silhouettes, or era-specific visual codes without F1's marks could still create an impression of association if the presentation is sufficiently immersive. [L3, §Does Implicit vs. Explicit Branding Change Enforcement; L5, §3.3]

### The identify-vs-brand distinction (L5, §1.5)

The doctrinal line is:
- **Nominative use** (legally permissible under doctrine): using the mark to refer to the trademark owner's products as the subject matter of your content — "this is Silverstone; can you identify it?"
- **Branding use** (infringement paradigm): using the mark to signal that the trademark owner sponsors or endorses your product — "The Official F1 Quiz: Prix-Guesser, presented by Formula 1™"

For prix-guesser's circuit-recognition mechanic, the identify-vs-brand distinction is favorable. The quiz is asking players to identify circuits — using circuit names as referential identifiers. The question presentation does not imply F1 is the source or sponsor of the quiz.

### The A Fox in Space precedent from cross-domain analogies

L3's most directly relevant analogous case: after Nintendo DMCA'd the "Star Fox: The Animated Series" Patreon account, the creator rebranded to "A Fox in Space" (removing Star Fox from the title) and the project survived. Nintendo's enforcement appeared to track the explicit trademark use in the account name, not the fan activity itself. After rebranding, implicit reference to the Star Fox universe continued in the content. [L3, §A Fox in Space]

**Composition**: the A Fox in Space pattern (implicit reference survives after explicit trademark removal) is consistent with L5's doctrine (dropping explicit marks improves posture but does not eliminate all exposure). This is cross-domain analogy and should not be treated as a prediction about F1's behavior. [OPUS-FOLLOWUP: synthesis-level composition across L3 and L5; needs Opus verification]

### BoxBoxd's branding practice as a real-world parallel

BoxBoxd uses F1-adjacent content implicitly (driver names, team names, circuit names as game content; "F1 Wordle," "F1 tier list," "Guess Who F1" as descriptors) without using the F1 wordmark as platform branding. [L1, §A2] BoxBoxd carries a site-wide disclaimer: "independent fan platform. Not associated with any racing organization or championship body. All motorsport-related names and marks belong to their respective owners." [L1, §A3] BoxBoxd appears to operate under an implicit branding posture that is consistent with the identify-vs-brand doctrine — using F1 content as subject matter, not as platform identity.

[OPUS-FOLLOWUP L1/L2: Whether BoxBoxd's use of "F1" in specific game descriptors ("Guess Who F1") constitutes branding a game under F1's Games prohibition is the most direct analogous legal question for prix-guesser's implicit branding posture. Not resolved by any lane.]

---

## Question 4 — BoxBoxd: Legal Posture, Product Shape, and Differentiation Surface

### Legal posture

**Disclaimer**: BoxBoxd carries a consistent, verbatim site-wide footer disclaimer on every page fetched [L1, §A3]:
> "BoxBoxd is an independent fan platform. Not associated with any racing organization or championship body. All motorsport-related names and marks belong to their respective owners."

This disclaimer is present on the homepage, games hub, about page, terms of service, privacy policy, and every individual game page. [L1, §A3, verified sources S1–S15]

**Licensing disclosure**: None found anywhere on the site. [L1, §A3] No text mentions a license, permission, or arrangement with Formula One Group, FOM, FIA, any team, or any motorsport organization. Absence of disclosure is consistent with either (a) undisclosed license, (b) operating without license under "fan use" posture, or (c) operating without license with no formal posture taken. The research cannot distinguish these. [L1, §A3, OPUS-FOLLOWUP L3]

**Monetization**: No consumer-facing monetization found (no ads, no donations, no subscriptions, no in-app purchases). The platform is described as free. [L1, §A4] However, two commercial pages exist: "BoxBoxd for Brands" and "BoxBoxd for Broadcasters," offering motorsport fan behavior data and fan opinion data to third parties. [L1, §A4] This B2B data offering may constitute "materially commercial" use under F1's Fans definition, which explicitly flags "build traffic and/or following to a website and/or social profiles in order to sell goods or services rather than genuinely provide a service for fellow fans" [B7, Passage 5 / L4, Passage F1-A]. [OPUS-FOLLOWUP L1/OF-L3: BoxBoxd's B2B layer may expose it more than prix-guesser's private-room model under F1's commercial definition — this is synthesis-level inference.]

**Operator identity**: Developer name Shaina Salmi is disclosed via Apple App Store only. The website itself discloses no individual, company name, or contact information beyond social handles. [L1, §A5]

**Founding / history**: Founded 2024 per schema.org structured data on the site. iOS app v1.0 launched October 20, 2025. The gap suggests web-only operation for approximately 1–2 years before mobile app. No definitive web launch date was established. [L1, §B1]

### Complete game mode inventory

**Six daily interactive games** [L1, §B2]:

| Mode | Shape | Content type | Prix-guesser overlap |
|------|-------|--------------|---------------------|
| Boxdle | Wordle variant | F1 driver stats/attributes | None — solo daily word/knowledge puzzle |
| Gridtexto | Contexto variant (semantic similarity) | Motorsport vocabulary (400+ terms) | None — semantic word game |
| Connections | NYT Connections variant | Motorsport terminology groupings | None — word categorization |
| Elo Ranker | Head-to-head Elo comparison | F1 driver rankings | None — opinion/ranking tool |
| Guess Who F1 | Hasbro Guess Who variant | F1 driver deduction (1v1 real-time) | Adjacent but structurally different (see below) |
| Break Week | Daily survey | Fan opinion questions during gap weeks | None — survey/polling |

**Three personality quizzes** [L1, §B2]:

| Mode | Shape | Overlap |
|------|-------|---------|
| Which Driver Are You? | BuzzFeed-style personality quiz | None |
| Which Team Are You? | BuzzFeed-style personality quiz | None |
| Which Duo Are You? | BuzzFeed-style personality quiz | None |

Total: 9 modes. [L1, §B2]

### The critical differentiation finding

**BoxBoxd has NO GeoGuessr-style mode.** No geography mode, no location-based mode, no image-recognition spatial mode, no "where is this?" mode of any kind was found anywhere on the site. [L1, §B5] All BoxBoxd games operate on F1 knowledge as propositions (facts, names, categories, semantic proximity) — not on F1 knowledge as spatial experience (circuits as places, paddock as environment, circuit geography).

**This is the clearest single axis of differentiation.** Prix-guesser occupies the geographic/spatial dimension of F1 fan gaming that BoxBoxd does not occupy.

### Guess Who F1 adjacency — structural difference

Guess Who F1 is the only BoxBoxd mode with real-time multiplayer and F1 content. However [L1, §B2, Guess Who F1]:
- Guess Who F1 is **1v1**; prix-guesser is designed for **group play (3–8 players)**
- Guess Who F1 uses **knowledge-deduction** (yes/no questions about driver characteristics); prix-guesser uses **GeoGuessr-style geography** (place recognition, map pin, clue ladder)
- Guess Who F1 appears to use **platform matchmaking** (finding an opponent); prix-guesser uses **private room codes** for friend groups
- Guess Who F1 has **no authored content packs**; prix-guesser's value proposition is **human-curated geographic clue ladders and location curation**

[OPUS-FOLLOWUP L1/C2: Whether Guess Who F1 supports private room codes (friends choosing each other) vs. only random matchmaking is not confirmed from public page text. If it supports private rooms, the overlap with prix-guesser's group-play positioning is somewhat stronger than this reading suggests — but the geographic vs. knowledge-deduction dimension remains orthogonal regardless.]

### The group-play/private-room gap

BoxBoxd's product architecture is **daily-reset, solo-play, persistent account** (streaks, leaderboards, social feed). It is fundamentally a daily habit product. Prix-guesser's architecture is **session-based, host-mediated, private group play** — a party game / game-night product. [L1, §B3] These are structurally different product categories even setting aside the geographic vs. knowledge content distinction.

**The authored-content-pack gap**: BoxBoxd's games appear to be algorithmically generated or operator-curated daily puzzles. There is no evidence of authored content packs, themed round sets, curated location sequences, or host-designed experiences. [L1, §B4, B5] Prix-guesser's planned human-authored geographic clue ladders have no BoxBoxd equivalent.

### BoxBoxd's "X but for F1" pattern (L1, §B4)

Every BoxBoxd mode adapts an existing well-known game format to F1 content:
- Letterboxd → BoxBoxd (social network)
- NYT Wordle → Boxdle
- Contexto → Gridtexto
- NYT Connections → Connections
- Elo rating system → Elo Ranker
- Hasbro Guess Who? → Guess Who F1
- BuzzFeed personality quiz → Quiz suite
- Daily survey → Break Week

GeoGuessr is notably absent from this pattern of adaptations. Prix-guesser's anchor mode fills exactly the gap BoxBoxd has left.

---

## Question 5 — Broader F1 Fan Project Landscape

### The 14-project catalog (L2)

L2 surveyed 14 F1-related community projects across two categories: 9 game/quiz projects and 5 data/tool/content projects.

**Game/quiz projects**: F1DLE, Stewardle, Who Are Ya?, Driverle/formula1points.com, Formudle, Sportsdle F1, Driver Grid Game, RaceGrids, Guess the F1 Driver

**Data/tool/content projects**: FastF1, Jolpica-F1 API, Box Box! (news app), TracingInsights, F1 Ocean

### Modal behavior across the catalog

Per L2, §Pattern Analysis:

| Pattern | Count | Notes |
|---------|-------|-------|
| No disclaimer | 7 of 14 (game projects) | Several JS-gated; absence may be non-observation |
| Full "unofficial" disclaimer | 4 of 14 (data/tool projects) | FastF1, Box Box!, TracingInsights, F1 Ocean |
| No monetization | 11 of 14 | Exceptions: Jolpica-F1 (Ko-fi), TracingInsights (affiliate + Patreon + BmC), F1 Ocean (BmC) |
| No named operator | 9 of 14 | Most game projects anonymous; data projects more transparent |
| F1 wordmark in brand name | 5 of 14 | F1DLE, Driverle, Formudle, Sportsdle, Guess the F1 Driver |

**The split by category is the central pattern finding** [L2, §Pattern Analysis]:
- **Game-format projects**: 9 projects — 0 carry a full F1 unofficial disclaimer based on accessible content
- **Data/tool/content projects**: 5 projects — 4 of 5 carry a full unofficial disclaimer

The data/tool projects are more careful about disclaimers and more likely to carry monetization (in a cost-recovery context). The game projects are less careful about disclaimers and have no monetization.

[OPUS-FOLLOWUP L2: Pattern is based on 14 projects; JavaScript-gating prevented full page renders for several game sites. The 0-of-9-game-projects disclaimer finding may be less clean on full inspection.]

### Operational survival of game projects

All 9 game projects were live as of 2026-04-11. None were found to have been taken down by F1. [L2, §What the operational survival of game projects implies] L2 explicitly notes: "operational survival does not equal approval."

**What this composition means**: the game projects collectively demonstrate that F1's published policy (Games prohibition, etc.) does not reflect F1's actual enforcement posture toward small-scale public fan puzzle games. The gap between F1's text and F1's enforcement practice is a real and observable phenomenon. But it is not a guarantee, not approval, and not a predictor of future behavior if the landscape changes (e.g., if F1 launches official quiz products).

### F1's documented enforcement action (L2, §Enforcement History)

In August 2024, F1 sent C&D letters to US-based content creators demanding they stop using "F1" in their usernames and branding for monetization purposes [L2, sources S21, S22]. No game projects were named. No puzzle sites were named. The target was monetized social/podcast/merchandise creators using "F1" in their brand identity.

**What this action did NOT target**: Any of the 9 daily-puzzle or data-tool projects in L2's catalog. No public record of F1 enforcement against any F1 fan game of any kind was found.

[OPUS-FOLLOWUP L2: absence of public enforcement record does not establish absence of enforcement. Private settlements or quiet voluntary rebrandings would be invisible to web search.]

### The most carefully-compliant project as a model

FastF1 [L2, §10] carries exactly F1's prescribed disclaimer text, a full trademark notice, MIT license, and named operator (Philipp Schäfer). It is the closest thing to a formally-compliant fan project in the catalog. Prix-guesser could model its disclaimer structure on FastF1's approach.

---

## Question 6 — What Analogous Domains Teach Us

### The enforcement trigger hierarchy (L3, §Pattern Analysis)

Across 15+ cases in Nintendo, Lucasfilm, WB, SEGA, motorsport, and Jagex domains, enforcement correlates with these factors in descending apparent weight:

1. **Commercial competition with an official product** — the clearest trigger. AM2R (official Metroid II remake in development), Galaxy in Turmoil (EA Battlefront franchise), FIA sim modding C&Ds (planned FIA official sim championship), RuneLite HD (Jagex's own planned HD upgrade), Reaper Scans (Kakao's official distribution). When an official product competes with a fan project, enforcement follows regardless of the fan project's monetization status.

2. **Mainstream platform visibility / distribution announcement** — Galaxy in Turmoil received its C&D *after* announcing a Steam distribution deal, not before. The Steam announcement, not monetization, was the trigger. [L3, §Galaxy in Turmoil]

3. **Large-scale crowdfunding** — Axanar ($1.3M raised) triggered a federal copyright lawsuit. Wizarding World Online Kickstarter was targeted before launch. The Star Trek fan film guidelines codified a $50K crowdfunding cap explicitly. [L3, §Axanar; §Wizarding World Online]

4. **Explicit trademark / branding use in the project/account name** — A Fox in Space Patreon was targeted explicitly because "Star Fox" appeared in the account name. After rebranding to "A Fox in Space," the project survived. [L3, §A Fox in Space]

5. **Platform advertising revenue** — Nintendo's 2021 GameJolt sweep explicitly cited GameJolt's advertising revenue as justification, even though individual game developers were not paid. [L3, §Nintendo Mass DMCA]

### What does NOT trigger enforcement

Non-commercial, low-visibility, free-only projects generally survive. Pokémon Revolution Online has operated for years with Nintendo IP and no documented C&D. Project M operated for six years without formal legal action despite large community presence. SEGA explicitly tolerates Sonic fan games "so long as no profit is involved." [L3, §What Does NOT Trigger Enforcement]

### The donation-specific pattern from analogous domains

L3, §Donation-Specific Subsection: **No documented case was found where a fan project accepting modest voluntary donations (Ko-fi/tip jar) was shut down specifically because of those donations, where the project would otherwise have been tolerated.**

Donation-linked enforcement cases involve: (a) $1M+ Kickstarter/Indiegogo campaigns (Axanar); (b) explicit IP trademark in the Patreon account name (A Fox in Space original name); (c) platform advertising revenue (Nintendo GameJolt 2021 — not the creator's donations).

RuneLite HD — the closest case to prix-guesser's profile — accepted ~$300/month in donations during the attempted shutdown. Jagex cited competitive concern, not the donations, as the enforcement trigger. Community pressure reversed the enforcement. [L3, §RuneLite HD]

**Key finding on donations (L3)**: "There is no documented case where a rights holder said explicitly 'we would have tolerated this project if it were not for the donations/Ko-fi/Patreon.'"

### SEGA's documented public policy

SEGA is the only major IP holder with a published, explicit public policy: "So long as no profit is involved, there is usually no issue with y'all using our blue boy to hone your art and dev skills." On donations: "tricky grey area" with the recommendation to "avoid any form of payment altogether if possible." [L3, §SEGA; sources S17, S18]

**Significance**: SEGA draws the line at monetization, not at fan activity generally. The "donations are a grey area" characterization aligns with L4's finding that cost-recovery donations sit in an ambiguous zone — not clearly commercial, not clearly non-commercial.

### F1 relevance — cross-domain inference

[OPUS-FOLLOWUP: all F1-relevance inferences from cross-domain analogies are probabilistic analogies, not predictions about Liberty Media / FOM / FIA behavior. F1's enforcement culture may differ from Nintendo's (aggressive), SEGA's (permissive), or Lucasfilm's (targeted).]

Prix-guesser's enforcement risk profile from cross-domain analogy:
- **Non-commercial, low-visibility, private-only**: very low enforcement risk by analogy
- **Explicit F1® trademark use**: highest single risk factor consistently across all domains — directly addressed by dropping wordmark from branding
- **Ko-fi/tip-jar donations**: not a documented standalone enforcement trigger; risk increases only if donations are tied to explicit trademark in account name or grow to commercial-looking scale
- **Geographic quiz content**: does not appear in the motorsport sim-racing enforcement history (FIA 2014 C&Ds targeted physics-simulation mods, not quiz games) — this content type is outside the documented F1-adjacent enforcement territory

---

## Cross-Lane Synthesis Findings

These findings only emerge from composition across lanes. Each is flagged as synthesis-level interpretation.

### CS-1: The private-only posture is doing double duty (composing B7 + L3 + L4)

B7 found that "private-only" satisfies one of the five carveout conditions but does not by itself satisfy "educational" (the weakest link). L3 found that mainstream platform visibility — going public — is the second-strongest enforcement trigger. L4 found that Canadian §29.21 requires "solely non-commercial" (a stricter standard than mere non-profit). **Composition**: prix-guesser's private-only posture simultaneously (a) satisfies a legal condition (the carveout's "private" requirement), (b) reduces the practical enforcement trigger risk (low visibility), and (c) may be essential for Canadian §29.21 compliance (public dissemination creates the "solely non-commercial" risk). The private-only choice is more over-determined than any single lane suggests.

[SYNTHESIS-LEVEL OPUS-FOLLOWUP: the composition here is correct at each pairwise step but the three-way combination needs Opus verification.]

### CS-2: BoxBoxd's B2B layer may expose it more than prix-guesser under F1's commercial definition (composing L1 + B7)

L1 found BoxBoxd's "For Brands" and "For Broadcasters" pages offer F1 fan behavior data to commercial clients. B7's Passage 5 (F1's Fans definition) flags as "materially commercial" any project that "build[s] traffic and/or following to a website and/or social profiles in order to sell goods or services rather than genuinely provide a service for fellow fans." BoxBoxd's entire free-to-consumer product may exist to generate fan data to sell to brands — which is precisely the traffic-building-to-sell-services pattern F1 identifies as "materially commercial." **Composition**: if F1 were to enforce against any F1 fan game, BoxBoxd's B2B commercial layer would make it a more legally exposed target than prix-guesser's private-room, no-revenue model. Prix-guesser's "genuinely provide a service for fellow fans" framing fits F1's favorable Fans definition more cleanly than BoxBoxd's B2B model does.

[SYNTHESIS-LEVEL OPUS-FOLLOWUP: this is a comparison that neither L1 nor B7 draws explicitly. It should not be read as an assertion that BoxBoxd is violating F1's guidelines — only that prix-guesser's posture under F1's own text appears more favorable.]

### CS-3: The 0-of-9-games-with-disclaimers pattern (L2) combined with the analogous-domain enforcement pattern (L3) suggests F1's tolerance is stable for the current type of fan game but would be fragile if the category grew

L2 found that 9 F1 daily-puzzle games operate publicly without disclaimers and without documented enforcement — despite those projects nominally violating the Games prohibition. L3 found that Reaper Scans was tolerated for years and then shut down when the rights holder built official distribution. **Composition**: F1's tolerance of fan puzzle games is plausibly because no official F1 puzzle game product exists or is in immediate development. If F1 or a licensee launched an official F1 quiz/trivia product, the same logic that drove the AM2R takedown and the Reaper Scans takedown would apply. The 9-game operational survival tells us about today's enforcement posture, not about a future posture where competitive concern exists.

[SYNTHESIS-LEVEL OPUS-FOLLOWUP: whether F1 has an official quiz/trivia product in development is an empirical question no lane in this program investigated. This is a gap that matters for the long-term risk assessment.]

### CS-4: Dropping explicit F1 branding plus adding a clear disclaimer puts prix-guesser at or above the best posture in the observed fan game landscape (composing L1 + L2 + L5)

L2 found that 0 of 9 game projects carry a full unofficial disclaimer. L1 found BoxBoxd carries a clear but not verbatim-F1-prescribed disclaimer. L5 found that the "honest practices" gate under EU and UK doctrine, and nominative fair use Factor 3 under US doctrine, are both substantially strengthened by a clear unofficial disclaimer. **Composition**: if prix-guesser drops explicit F1 wordmarks from branding AND includes a clear unofficial disclaimer (comparable to FastF1's verbatim-accurate text), it would be in a *better* legal posture than any of the 9 observed F1 fan game projects — not because of a legal safe harbor, but because it would have addressed the most clearly problematic practices that those projects have not addressed.

### CS-5: The geographic/spatial gap is the clearest product differentiation axis and is also legally less fraught than knowledge-trivia content

L1 found BoxBoxd has no geographic mode. L5 found that circuit names are F1-disclaimed IP (belonging to circuit operators) and are plausibly used as referential/nominative identifiers in quiz questions. L3 found that the FIA's 2014 sim C&Ds targeted physics-simulation mods, not quiz games or geography games. **Composition**: the geographic/spatial category — showing circuit images or venue photographs and asking players to identify them — is simultaneously (a) prix-guesser's clearest product differentiation axis from BoxBoxd, and (b) a legal area where F1's disclaimed circuit IP removes F1 as the primary rights holder, reducing F1-specific legal exposure relative to using F1's owned artworks or audio/AV content.

[SYNTHESIS-LEVEL OPUS-FOLLOWUP: this composition is favorable but not dispositive — it does not address circuit operators' separate IP rights or the quality of the photographs used (third-party licensed vs. F1-owned still images). The legal favorability is conditional on using appropriate source photography.]

---

## Does B8 Change the Phase 01 Audit's Practical Conclusion?

### What the paused audit concluded

Wave 2 / Lane B7 (the most thorough predecessor) concluded:
> "F1's published guidelines text does not resolve whether prix-guesser falls under the carveout or any of the three relevant prohibitions (Games, Simulators, Apps)... The most defensible posture is to keep prix-guesser's use of F1-originating IP Rights conservative..." [B7, LQ-B7.3]

The practical audit conclusion was: (1) stay private; (2) stay non-commercial; (3) avoid F1's enumerated Other IP Rights; (4) don't use F1 Permitted Word Marks as branding; (5) acknowledge the navigation rather than claim a clean legal shelter.

### What B8 adds on top of B7

The B8 research program extends B7's findings in five material ways:

1. **Cross-domain enforcement confirmation (L3)**: B7 reasoned from text only. L3 now confirms from 15+ analogous cases that commercial competition, not monetization level, is the primary enforcement trigger. This reinforces the private-only + no-competition-with-official posture on empirical grounds, not just textual grounds.

2. **Canadian jurisdiction focus (L4)**: B7 did not address jurisdiction-specific doctrine. L4 now surfaces that Canadian §29.21's "solely non-commercial" language is the highest doctrinal risk for a Canadian project owner if donations are added. The audit's practical conclusion stands but needs a jurisdiction-specific addendum for the donation scenario.

3. **BoxBoxd as reference point (L1)**: B7 had no information about the comparative landscape. L1 now shows a directly comparable project operating publicly with a disclaimer and no license. This does not change the audit's recommendation but it contextualizes it: BoxBoxd operates at a higher risk level than the audit's recommended posture for prix-guesser.

4. **The geographic/spatial content type is lower-risk than knowledge/trivia content (CS-5 above)**: B7 analyzed the Games prohibition broadly. L5 + L3 + CS-5 together now suggest that circuit-geography content — specifically using venue images and circuit names as referential identifiers — sits in a more favorable legal space than using F1's owned statistics, artworks, or audio/AV content. This gives the audit's "avoid F1's enumerated Other IP Rights" conclusion a more granular form: the circuit-geography content type is the most legally defensible category within the game's design space.

5. **Disclaimer recommendation now has an empirical comparator (L2 + CS-4)**: the audit recommended explicit acknowledgment of navigated ambiguity. L2's finding that 0 of 9 fan games carry a full disclaimer gives this recommendation a concrete form: prix-guesser should be in the FastF1 camp (full disclaimer) rather than the game-project camp (no disclaimer), and doing so would differentiate it favorably from the observed landscape.

### Path A: fold B8 into the audit's Wave 3 synthesis

If the user wants B8 incorporated into the Wave 3 synthesis, the audit's practical conclusions hold; B8 provides:
- Empirical grounding for the private/non-commercial posture (L3)
- Jurisdiction-specific risk flag for Canadian §29.21 (L4)
- Granular content-type guidance (circuit-geography is more favorable than F1-owned artworks) (CS-5)
- A benchmark comparison: BoxBoxd's posture, and how prix-guesser can be more defensible than it

### Path B: keep B8 as separate research, reference from audit

If the user wants to keep the research and audit chains separate, B8 can be cited from the audit's Wave 3 synthesis as "B8 research program confirms the private/non-commercial posture on empirical grounds; adds Canadian jurisdiction risk flag; identifies geographic content as the most defensible design axis."

**Net answer**: B8 does not change the audit's practical conclusion. It reinforces it on empirical grounds, adds jurisdictional specificity, and provides a product differentiation finding (BoxBoxd gap) that was absent from the audit chain.

---

## What the Research Program Did NOT Cover

### Gaps inherited from individual lanes

**From L1 (BoxBoxd):**
- Wayback Machine history — actual web launch date in 2024 unestablished; game mode addition chronology unknown
- Twitter/X (@Box_Boxd) — 402 error; tweet history and launch announcements inaccessible
- Login-gated content; direct gameplay observation; blog article full text inaccessible
- BlogBoxd "Letterboxd for F1: Why BoxBoxd Exists" full article — founding narrative not available

**From L2 (F1 fan project survey):**
- Several game sites JS-gated; footer disclaimers may exist but were not returned
- Whether F1 is aware of these projects and choosing not to act, is unaware, or has a non-public tolerance policy
- Private settlements, informal requests, or voluntary rebrandings would not appear in public search

**From L3 (analogous domains):**
- DC/Marvel fan games — no documented C&Ds found (search limitation, not confirmed absence)
- Documented "donation-only" (Ko-fi/tip jar) project shutdowns — no case found; may reflect survivorship bias
- MotoGP/IndyCar/WRC fan enforcement — not searched
- odinlaw.com citation from Lane 1C (LQ-1C.4 Finding 2) — not independently verified

**From L4 (commercial threshold):**
- UK statute text (CDPA 1988 §29) — direct WebFetch returned empty; secondary sources only
- Canadian case law on §29.21 cost-recovery donations — no case found anywhere
- EU DSM Directive 2019/790 user-generated content provisions — not examined
- F1's specific trademark registrations by class — not examined
- Platform-specific policies (Patreon copyright policy, Ko-fi guidelines) — not examined in depth

**From L5 (nominative fair use):**
- Trademark register searches for circuit names (Silverstone, Monza, Suzuka, etc.) — not conducted
- Post-Brexit UK honest-practices test divergence from CJEU — not researched
- Canadian case law on nominative use for fan/quiz content — essentially unresearched
- Per-jurisdiction driver publicity rights / right of publicity by state/country — not researched
- Prix-guesser's actual visual design — not reviewed; trade dress analysis requires design review

### Gaps first identified by this synthesis

- **Whether F1 has an official quiz/trivia product currently or in development** — the most important empirical gap for the long-term competitive concern trigger. No lane in this program investigated F1's official app/game product offerings.
- **Trademark "use in commerce" analysis for a donation-accepting project** — identified by L4 §Section 7 but not resolved by any lane; a separate analysis from copyright
- **Per-circuit operator IP posture** — F1 redirects circuit IP to circuit operators; no lane researched any individual circuit operator's IP terms, trademark registrations, or licensing posture
- **BoxBoxd's actual B2B commercial model** — whether it constitutes "materially commercial" under F1's Fans definition; the For Brands / For Broadcasters pages disclose no pricing or metrics
- **F1's actual internal licensing posture toward fan projects** — public text and enforcement actions are observable; private tolerance policy is not

---

## Consolidated OPUS-FOLLOWUP List

### Legal Follow-ups (route to future Opus legal doctrine dispatch)

**[OF-LEGAL-1]** *(L4/OF-3, rated HIGH)* Canadian §29.21 "solely for non-commercial purposes" + cost-recovery donations: the word "solely" creates a higher standard than US or F1 policy; no Canadian case found addressing this scenario. This is the top doctrinal priority for a Canadian project owner.

**[OF-LEGAL-2]** *(L4/OF-1, rated HIGH)* F1's "non-commercial" condition in the carveout (Passage F1-B) is undefined; F1's discretion reservation ("subject to our discretion") means textual analysis is advisory. Does F1's discretion language have any limiting principle? Can the three "materially commercial" examples be read as exhaustive or are they illustrative?

**[OF-LEGAL-3]** *(L4/OF-4, rated HIGH)* UK CDPA fair dealing categorical eligibility for a fan quiz game — "entertainment" is not enumerated; which CDPA category, if any, applies? This is the prior question before the commercial analysis arises in the UK.

**[OF-LEGAL-4]** *(L4/OF-6, rated MEDIUM)* Trademark "use in commerce" analysis for a donation-accepting fan project using F1 marks — separate from copyright; whether a donation creates the required nexus between the marks and commerce under the Lanham Act or Canadian Trademarks Act.

**[OF-LEGAL-5]** *(L5, §9, item 1)* Whether *Toyota v. Tabari*'s burden-shifting and Sleekcraft-exclusion holdings extend from domain-name/brokerage contexts to a game/quiz context.

**[OF-LEGAL-6]** *(L5, §9, item 2)* Post-Brexit UK honest-practices test — whether UK courts have diverged from CJEU Article 14 "honest practices" interpretation after 2021.

**[OF-LEGAL-7]** *(L5, §9, item 4)* Per-circuit trademark register searches: whether "Silverstone," "Monza," "Suzuka," "Spa-Francorchamps," etc. are registered trademarks and in which classes — each circuit is a separate analysis.

**[OF-LEGAL-8]** *(L5, §9, item 6)* Canadian case law on nominative use for fan/quiz content — essentially unresearched; specific Canadian precedents needed.

**[OF-LEGAL-9]** *(L4/OF-7)* Solicited vs. unsolicited donations — no formal authority draws this distinction for copyright or trademark. May be relevant under both frameworks. Priority: LOW unless the project owner is planning a specific donation model.

**[OF-LEGAL-10]** *(B7, LQ-B7.6, item 5; L4/OF-5)* UK CDPA §29 and §29A verbatim text — direct statute fetch returned empty; verify against legislation.gov.uk.

**[OF-LEGAL-11]** *(L3, OPUS-FOLLOWUP #5)* Whether Nintendo's legal framing in the 2021 GameJolt sweep (platform advertising revenue = unauthorized commercial exploitation of IP) is legally robust or a strategic DMCA framing. A JIPL article argued against this framing; needs assessment.

**[OF-LEGAL-12]** *(L1, OPUS-FOLLOWUP L2)* Does using "F1" as a modifier in game names ("Guess Who F1," "F1 tier list") constitute "branding" a game under F1's Games subsection Games clause? Descriptive/genre vs. branding use — a legal interpretation question with direct relevance to how prix-guesser titles its modes.

**[OF-LEGAL-13]** *(L5, §8, item 10; CS-5 synthesis)* Explicit mapping of which content types remain restricted under F1's guidelines (Games clause, Apps clause, Section 2 prohibitions) even after wordmark dropping — so prix-guesser's content authoring rules can be derived from the analysis.

### Competitive / Product Follow-ups (route to future product/differentiation dispatch)

**[OF-PRODUCT-1]** *(L1, C2)* Guess Who F1 multiplayer architecture: does it support private room codes (friends choosing each other) or only random matchmaking? This matters for the differentiation analysis. Direct observation or app access required.

**[OF-PRODUCT-2]** *(L1, C1)* Wayback Machine retry for boxboxd.fun: establish earliest crawl date (web launch in 2024), when game routes first appeared, and game mode addition chronology.

**[OF-PRODUCT-3]** *(L1, C3)* Individual game mode pages returned hub content; actual game mechanics, puzzle numbering, and whether Connections uses images need direct gameplay observation.

**[OF-PRODUCT-4]** *(L1, C4)* Blog article "Letterboxd for F1: Why BoxBoxd Exists" — founding narrative not accessible; retry with different approach (Google cache, Wayback, alternate fetcher).

**[OF-PRODUCT-5]** *(L1, C5)* Developer Shaina Salmi public profile search — professional background, location, solo vs. team, public statements about BoxBoxd origins.

**[OF-PRODUCT-6]** *(CS-2 synthesis)* BoxBoxd's B2B commercial layer (For Brands / For Broadcasters) — does this constitute "materially commercial" under F1's Fans definition? What are the actual pricing and data products? This affects the competitive and legal comparison between BoxBoxd and prix-guesser.

**[OF-PRODUCT-7]** *(CS-3 synthesis)* Whether F1 has an official quiz/trivia product currently or in development — the most important gap for assessing long-term competitive-concern enforcement trigger.

**[OF-PRODUCT-8]** *(B7, LQ-B7.6, item 5)* F1's AI prohibition ("FORMULA 1 Rights cannot be used in or with any artificial intelligence technology, including in connection with training; development; or operation of large language models") — if any future phase uses LLM assistance for content generation, round description authoring, or research using F1 materials, this prohibition is directly in scope.

### Empirical Follow-ups (route to future landscape/enforcement-history dispatch)

**[OF-EMPIRICAL-1]** *(L2, §Pattern Analysis)* Whether F1 is aware of the 9 publicly-operating fan puzzle games and choosing not to act, is unaware, or has a non-public policy of tolerance. Not determinable from public sources.

**[OF-EMPIRICAL-2]** *(L3, OPUS-FOLLOWUP #8)* Confirming/disconfirming cases of genuinely donation-only (Ko-fi/tip-jar, not Kickstarter) projects shut down specifically because of those donations. Absence of documented cases may be real or survivorship/coverage bias.

**[OF-EMPIRICAL-3]** *(L3, OPUS-FOLLOWUP #6)* FIA vs. FOM/Liberty Media rights split — who controls which rights in sim content (FIA) vs. brand/data (FOM/Liberty). The 2014 C&Ds were in FIA space; quiz/data tools may be in FOM/commercial rights space. This matters for which entity has enforcement standing over prix-guesser.

**[OF-EMPIRICAL-4]** *(L3, OPUS-FOLLOWUP #3)* Pokémon Revolution Online — what distinguishes it from Uranium/Prism from an enforcement perspective. Does PRO accept donations? Does server location matter? A useful data point for the "what survives without enforcement" analysis.

**[OF-EMPIRICAL-5]** *(L3, OPUS-FOLLOWUP #9)* odinlaw.com citation from Lane 1C predecessor (LQ-1C.4 Finding 2) on fan-game legal risks — needs retrieval and assessment.

**[OF-EMPIRICAL-6]** *(L1, OPUS-FOLLOWUP L3)* Whether BoxBoxd has any private agreement, license, or informal arrangement with any motorsport rights holder that is not publicly disclosed. The absence of licensing disclosure is consistent with either no license or an undisclosed license.

**[OF-EMPIRICAL-7]** *(L5, §9, item 4; per-circuit)* Per-circuit operator IP posture: Silverstone (BRDC), Monza (SIAS/ACI), Suzuka (Honda Mobilityland), and others — each circuit's actual trademark registrations, licensing terms, and IP posture are separate empirical questions no lane investigated.

---

## Qualifications

### Inherited qualifications (from individual lanes)

1. **Not a legal opinion.** This synthesis, like all 5 predecessor lanes, contains empirical observations about legal doctrine and textual analysis of public documents. Nothing herein constitutes legal advice or predicts the outcome of any enforcement action or litigation.

2. **All findings are as of 2026-04-11.** F1's guidelines, the Canadian Copyright Act, CDPA, US §107 case law, BoxBoxd's product and legal posture, and the F1 fan project landscape may all have changed since this fetch date.

3. **Sonnet-tier research throughout.** All 5 predecessor lanes ran on Claude Sonnet 4.6 under time-constrained research conditions. The synthesis is also Sonnet-tier composition. Legal doctrine findings are "vague understanding" for Opus refinement; they should not be treated as authoritative legal analysis. The OPUS-FOLLOWUP flags are the mechanism by which Sonnet-level inference is escalated to Opus-level review.

4. **Secondary sources dominate for several key findings.** L3's older Nintendo/WB cases rely on gaming news as secondary sources. L4's UK statute text was not directly fetched from legislation.gov.uk. L5's case law summaries were retrieved from secondary platforms (Harvard metaschool, Cornell LII, OpenJurist), not from original reporters. Verbatim quotes from cases should be verified against primary sources before citation in any production context.

5. **Survivorship bias in enforcement data.** Private settlements, quiet C&D compliance, and informal requests are not visible to web search. The "no enforcement" finding for F1 fan games is positive evidence of what was found, not confirmation of the absence of enforcement activity that didn't generate news coverage.

6. **Nintendo is overrepresented in analogous-domain data.** Nintendo's enforcement history is the most documented in search-accessible corpora; SEGA is notably more permissive. The cross-domain pattern should not be read as predicting Nintendo-style behavior from F1.

7. **F1 guidelines are private policy, not law.** F1's published guidelines express F1's characterization of what it permits. General IP law (copyright fair use/dealing, trademark nominative use) operates independently and may permit more than F1's guidelines concede.

8. **Canadian law is the most relevant jurisdiction** for the project owner; UK and US doctrine are informative for F1's rights-holding structure (UK-based entity) and for the broader IP framework, but Canadian doctrine governs the project owner's primary legal exposure.

### Synthesis-level qualifications

9. **Cross-lane composition is synthesizer-level interpretation.** The CS-1 through CS-5 synthesis findings, and the OPUS-FOLLOWUP flags labeled "synthesis-level," are this synthesizer's inference from composing findings across lanes. They are not individual-lane findings and should be treated as hypotheses for Opus verification, not as conclusions.

10. **The research program does not cover F1's actual internal licensing and enforcement posture.** What F1 has privately done in response to fan projects (undisclosed C&Ds, private tolerance, informal conversations) is invisible to web research. The research program can only characterize what is publicly observable.

11. **The synthesis does not constitute a legal risk assessment for prix-guesser.** It constitutes a research synthesis for the project owner's decision-making. The decision about whether, how, and when to add donations, expand distribution, or modify branding involves risk tolerance and business judgment that this research cannot supply.
