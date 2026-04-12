---
date: 2026-04-11
wave: 2
lane: B7
audit_subject: claim_integrity
audit_orientation: standard_escalated_to_investigatory
audit_delegation: self
auditor_model: claude-opus-4-6
agent_type: general-purpose
fetch_date: 2026-04-11
fetch_url: https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt
fetch_count: 2
parent_task_spec: wave-2-lane-b7-f1-legal-ambiguity-task-spec.md
predecessor_lanes:
  - wave-1-lane-1c-external-gap-research.md
  - wave-2-lane-b4-f1-legal-carveout-citation.md
ground_rules: "core+standard+claim_integrity+chain+framework-invisibility"
output_files:
  - wave-2-lane-b7-f1-legal-ambiguity.md
tags:
  - wave-2
  - lane-b7
  - f1-legal-ambiguity
  - claim-integrity
  - escalated-investigatory
  - opus
  - general-purpose-agent
  - web-research
---

# Wave 2 / Lane B7 — F1 Legal Ambiguity Resolution

**Model:** Claude Opus 4.6 (general-purpose agent with WebFetch).
**Classification at start:** claim_integrity × standard × self.
**Classification by mid-lane:** **Escalated to investigatory** at LQ-B7.3 because the empirical re-fetch surfaced (a) two additional prohibitive passages Lane 1C did not quote and (b) the absence of any definitions for "simulator" or "educational" in F1's text. The text does not close the ambiguity; the lane therefore holds it open with conditions.
**Escalation marker:** see LQ-B7.3 below.

---

## Position of the Lane (I4-equivalent)

I am reading F1's published policy text on 2026-04-11, twice via WebFetch with different prompts to cross-check the returned content. I am not interpreting case law, not reading F1's internal licensing decisions, and not seeing F1's enforcement history. I am bounded by what F1 has published at one specific URL on one specific day, and by the text-reading framing of the task. My findings about Lane 1C and Lane B4's chain of inference are about what is and is not in F1's published text, not about whether the inferred legal conclusions are sound under any country's IP law.

I am Opus, which means I am being asked to hold two passages (and as it turned out, four passages) in tension and judge how their scope boundaries interact. The interpretive load is real and I am explicitly trying not to manufacture either confidence or ambiguity. Where I commit, I show the text. Where I hold open, I name the specific text-level reason.

---

## TL;DR for the synthesizer

1. **Lane 1C's two quoted passages are verbatim accurate** as of 2026-04-11. No divergence on either passage.
2. **Lane 1C and Lane B4 both omitted material passages** from the same guidelines page that bear directly on prix-guesser. Specifically: a "Games" section and an "Apps" section that together constitute a more general prohibition against third-party games and apps using F1's "Other Intellectual Property Rights." These passages are in scope for the claim_integrity check and were not addressed by either predecessor.
3. **F1's text contains no definition of "motorsport simulator," no definition of "software that simulates auto racing," and no definition of "educational."** Two independent WebFetches with targeted definitional prompts confirm this. The terms are used as if their meaning were obvious; nothing in the document scopes them.
4. **The carveout at the heart of Lane B4's draft text is narrower than Lane 1C and Lane B4 read it.** It applies specifically to "Other Intellectual Property Rights" (results/timing data, official typeface, statistics, still images, audio/AV content, official artworks/graphics/textures, written content) — not to a general "private fan use" zone. It is also conditioned on five stacked qualifiers: justified, limited, non-commercial, private, and educational.
5. **The verdict is Reading C, with structure** — the ambiguity is irreducible on F1's current text, but the conditions that push the reading each way are precisely nameable. Reading A is not cleanly available because prix-guesser is not obviously "educational" in the carveout's narrow framing. Reading B is not cleanly available because the simulator clause is not obviously about quiz games. The most accurate framing is that **prix-guesser navigates an under-defined intersection of three prohibitions and one narrow conditional carveout**, and the canon citation should say so honestly rather than confidently invoke the carveout.
6. **Lane B4's draft citation text needs revision.** The phrase "within this licensed zone" overstates what F1's text actually says; the carveout is conditional, the carveout's "educational" condition is not obviously satisfied by a party game, and the carveout is silent on the simulator/games/apps prohibitions. Revised text is proposed in LQ-B7.5.

---

## Methodology

Two WebFetches against `https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt`:

- **Fetch 1 (broad)**: requested the full page text, all sections, all definitions, all passages about education/private/fan/simulator/games/apps. This returned a near-complete dump of the page including the "Fans" definition, the Section 1–5 structure, all of Section 4's subsections (Internet, Social media, Audio/AV, Typefaces, Games, Esports and sim racing, Simulators, Apps, Timing Data, Written Content, Competitions, Ticket Giveaways, Merchandise, Endorsement, Advertisements, Artificial Intelligence, Commercial use, Company name, Variations), and the brandprotection@f1.com contact.
- **Fetch 2 (targeted)**: a narrow re-check asking specifically whether "motorsport simulator" or "educational" are defined anywhere in the document, plus verbatim re-quotation of the Games / Apps / Esports / Simulators sections to verify the broad fetch's wording. This is the closest I can come to a second pair of eyes on the same source within tool constraints.

Both fetches returned consistent text on the four key passages. The fetch is timestamped 2026-04-11. F1's guidelines document is dated by reference to a 2025 logos image and includes a 2026 calendar of Event Titles, which is consistent with a current-as-of-2026 document.

---

## Verbatim text from F1's guidelines (re-fetched, not copied from Lane 1C)

I am reproducing the four load-bearing passages plus the structural context that scopes them. All quotations are verbatim from the WebFetch return on 2026-04-11.

### Passage 1 — The educational-purposes clause (the "carveout")

This passage appears in **Section 2 ("Other Intellectual Property Rights")**, after the section's enumeration of what counts as Other Intellectual Property Rights and after the fair-dealing notice. Verbatim:

> "Limited use of our Other Intellectual Property Rights for educational purposes may be acceptable where the use is justified, limited, and non-commercial. However, please note, this does not include public postings such as YouTube, websites and social media. It must be for a private, educational purpose only."

The immediately preceding sentence is the fair-dealing disclaimer:

> "Fair dealing is a limited defence to copyright infringement in the UK, and while other countries may have similar defences, they are not the same. If you intend to rely on fair dealing as a defence to the use of any of the applicable Other Intellectual Property Rights or the Logos you should seek independent advice in relation to the relevant country."

The immediately following sentence anchors the scope of the term "FORMULA 1 Rights":

> "Where we refer to the FORMULA 1 Rights we are referring to Our Marks and Other Intellectual Property Rights collectively."

**Section 2's enumeration of Other Intellectual Property Rights** (verbatim, the bullet list):

> "Results and Timing data; Official Typeface; Statistics; Still Images; Audio and Audio Visual Content; Official Artworks, Graphics, Assets and Textures; Written Content including articles and news stories used and featured in all our products and services"

This list **does not include** circuit outlines, venue photographs (except as Still Images owned by F1), era-aesthetic visual styles, or trivia about race history. It does include any F1-owned still image, F1's official graphics/artworks/assets/textures, F1's audio/AV content, and F1's statistics.

### Passage 2 — The simulators clause

This passage appears in **Section 4 ("Other uses of FORMULA 1 Rights"), under the subsection heading "Simulators"**. Verbatim, the full subsection:

> "Motorsport simulators and/or software that simulates auto racing (including those that are digital only or those that incorporate physical elements such as racing car chassis) should not make any use of the FORMULA 1 Rights without an express written license.
>
> All rights in third party names and trade marks which may be used on or in association with motorsport simulators are the property of their respective owners. Such rights should not be reproduced without the consent of the relevant third party rights holder."

The Simulators subsection sits between **Esports and sim racing** (above) and **Apps** (below) inside Section 4.

Note that this clause restricts use of "the FORMULA 1 Rights" (Marks plus Other IP Rights collectively, per Passage 1's anchor sentence) without limiting itself to Other IP Rights only. It is a broader prohibition than the carveout's domain.

### Passage 3 — The Games clause (NOT quoted by Lane 1C or Lane B4)

This passage appears in **Section 4 under the subsection heading "Games"**, between Typefaces (above) and Esports and sim racing (below). Verbatim, the full subsection:

> "Our Permitted Word Marks cannot be used to brand any game. Other Intellectual Property Rights including those from the Formula 1 companies' official games cannot be used in third party games."

This is a **two-part prohibition**:

- (a) Permitted Word Marks (F1, Formula 1, Grand Prix, etc.) cannot be used to brand any game.
- (b) Other Intellectual Property Rights — including specifically Other IP Rights *originating from F1's official video games* — cannot be used in third party games.

This passage is NOT quoted by Lane 1C and NOT quoted by Lane B4. It is in scope for any honest legal-text reading of prix-guesser's situation because prix-guesser is, by its own canonical self-description, a game. The Games subsection bears directly on the question.

### Passage 4 — The Apps clause (NOT quoted by Lane 1C or Lane B4)

This passage appears in **Section 4 under the subsection heading "Apps"**, between Simulators (above) and Timing Data (below). Verbatim, the full subsection:

> "Our Permitted Word Marks can be used editorially for non-commercial purposes in relation to apps so long as the use is to inform or report and not to brand, i.e. in the paragraphs of accompanying text to describe the app.
>
> Other Intellectual Property Rights cannot be used in apps. For further guidance on timing data please see Timing Data category below."

This is a **two-part rule**, not a uniform prohibition:

- (a) Permitted Word Marks *can* be used editorially in apps, non-commercial, non-branding only.
- (b) Other IP Rights *cannot* be used in apps, full stop.

The Apps section is the closest thing in F1's text to a recognition that software products distinct from simulators exist; it does not carve out fan or educational app use.

### Passage 5 — The "Fans" definition

This appears in the introductory section before Section 1. Verbatim:

> "'Fans' in this context mean individuals, groups or collectives including for example not for profit institutions such as fan clubs. For the purposes of these guidelines Fans will be those who follow FORMULA 1 events and are active in supporting the races but without doing so in a materially commercial manner, subject to our discretion. A materially commercial manner may include using the FORMULA 1 Rights:
>
> *   for clickbait purposes to promote commercial offers, promotions or activities either related or unrelated to the FORMULA 1 events;
> *   to build traffic and/or following to a website and/or social profiles in order to sell goods or services rather than genuinely provide a service for fellow fans;
> *   for advertising and/or promotional purposes that is excessively repetitive or otherwise intrusive, such as targeted ads directed at a select user base."

This definition is important for the lane because Lane 1C and Lane B4 implicitly relied on "fan use" as a permissive category. F1's text *does* define Fans (favorably for prix-guesser, since the project has none of the materially-commercial markers) — but the Fans definition does not by itself unlock any specific permission. Section 4's Fundamental Principles still apply, and the per-subsection prohibitions (Games, Simulators, Apps) still apply to fan-conducted activity.

### Passage 6 — The Fundamental Principles

Verbatim, from the head of Section 4:

> "Whenever using any of the FORMULA 1 Rights in compliance with these guidelines you must:
>
> *   be clear that what you are doing is not official, approved or endorsed by us or associated or connected with us;
> *   be respectful to the FORMULA 1 Rights;
> *   not be unlawful, deceptive, obscene, harmful or disparaging;
> *   not use our Logos;
> *   not integrate Our Marks into any other marks and sufficiently differentiate the use of Our Marks from other marks;"

These conditions apply to any fan use under Section 4. Prix-guesser appears to satisfy all five (the canon explicitly self-labels as "unofficial," does not use Logos at M1 scope, does not integrate Marks into other marks). But satisfying the Fundamental Principles is necessary, not sufficient — the per-subsection rules still apply.

---

## Findings

### LQ-B7.1 — Verification of Lane 1C's quotations

**Verdict: both Lane 1C quotations are verbatim accurate; both predecessor lanes omitted material passages from the same page.**

Lane 1C's two quotations re-verified word-for-word against the WebFetch return on 2026-04-11:

| Lane 1C quotation | Verification status |
|---|---|
| "Limited use of our Other Intellectual Property Rights for educational purposes may be acceptable where the use is justified, limited, and non-commercial. However, please note, this does not include public postings such as YouTube, websites and social media. It must be for a private, educational purpose only." | **VERIFIED VERBATIM.** No word changes, no reordering, no omitted clauses. |
| "Motorsport simulators and/or software that simulates auto racing (including those that are digital only or those that incorporate physical elements such as racing car chassis) should not make any use of the FORMULA 1 Rights without an express written license." | **VERIFIED VERBATIM.** No word changes, no reordering. |

**However, Lane 1C's selection was not exhaustive on the page.** The two passages Lane 1C extracted are accurate but the page contains additional passages within scope of the question that Lane 1C did not extract. Specifically:

- The **Games** subsection (Passage 3 above) is on the same page in the same section, three subsections away from the Simulators clause. Its rule that "Other Intellectual Property Rights including those from the Formula 1 companies' official games cannot be used in third party games" is independently applicable to prix-guesser as a third-party game.
- The **Apps** subsection (Passage 4 above) is on the same page, immediately below Simulators. Its rule that "Other Intellectual Property Rights cannot be used in apps" is independently applicable to prix-guesser as a browser application.
- The **Fans** definition (Passage 5 above) is in the introduction. It bears on whether "fan use" unlocks any specific permission.
- The **Fundamental Principles** (Passage 6 above) impose five baseline conditions on any fan use within Section 4.

**The carveout's domain is narrower than Lane 1C and Lane B4 read.** The educational-purposes carveout is in **Section 2 ("Other Intellectual Property Rights")** and its first words restrict its scope: "Limited use of our Other Intellectual Property Rights for educational purposes…" — i.e., it is a carveout against Section 2's general prohibition on Other IP Rights, NOT a general carveout against all of Section 4's per-category prohibitions. Section 4's Games, Simulators, Apps, and Esports subsections each have their own rules; the educational-purposes carveout from Section 2 does not by its terms override those Section 4 prohibitions.

This is a structural reading point that neither Lane 1C nor Lane B4 surfaced. It changes the chain integrity of Lane B4's "carveout applies → minimum viable text" inference.

**Chain-integrity ledger entries for LQ-B7.1**: see end-of-document ledger.

---

### LQ-B7.2 — Does F1's text define "motorsport simulator" or "software that simulates auto racing"?

**Verdict: NO. F1's text contains no definition, no examples, no qualifying language, and no cross-reference for either term.**

I asked this question explicitly in Fetch 2 with a targeted prompt. The result was unambiguous: "No definition found. The document uses these terms but does not define them or distinguish between different types of simulators."

I also re-checked the broader fetch return for any sentence anywhere in the document that contains the word "simulator," "simulate," "simulation," or any near-synonym. The only occurrences are:

1. The Esports and sim racing subsection (Passage 2's neighbor): "The Formula 1 companies run an official Sim Racing series and have the exclusive right to licence the official F1 video game for esports and sim racing."
2. The Simulators subsection itself (Passage 2): "Motorsport simulators and/or software that simulates auto racing…"
3. The trailing sentence of the Simulators subsection: "All rights in third party names and trade marks which may be used on or in association with motorsport simulators are the property of their respective owners…"

None of these scope the term. The phrase "software that simulates auto racing" is the closest the document comes to a working definition; it is used as if the meaning is self-evident, in parallel with "motorsport simulators" (which suggests "motorsport simulators" is the noun and "software that simulates auto racing" is a clarifying paraphrase, but the paraphrase is itself undefined). The "(including those that are digital only or those that incorporate physical elements such as racing car chassis)" parenthetical scopes the *form factor* of the simulator (digital vs. physical-rig) but not the *type of game*.

**What F1's text does NOT do**:
- It does not say "such as iRacing, Forza Motorsport, F1 24."
- It does not exclude "trivia games" or "quiz games" or "geography games."
- It does not distinguish between physics simulators and other software that uses F1 content.
- It does not define "auto racing" — leaving open whether the simulation must model the racing activity (driving, lap times, vehicle behavior) or merely use F1 content in a software context.

**The interpretive vacuum is intentional or accidental — but it is not closed.** A reader sympathetic to prix-guesser will read "software that simulates auto racing" narrowly as "software that models the activity of racing" — i.e., physics, vehicle dynamics, driver inputs — and conclude prix-guesser is not in scope because it doesn't model racing as an activity. A reader sympathetic to F1's brand-protection team will read "software that simulates auto racing" broadly as "software that recreates the experience or content of auto racing" and conclude prix-guesser is in scope because it asks players to recognize and engage with F1's circuits, venues, and eras as F1 content. Both readings are textually defensible. The text does not pick one.

**Carrying the undefined state into LQ-B7.3**: this lane has confirmed empirically that F1's text does not resolve the definitional question. Whatever LQ-B7.3 concludes about prix-guesser's fit to the simulator clause must rest on interpretation, not on text-level resolution.

---

### LQ-B7.3 — Does prix-guesser fall under the carveout or the prohibition?

**ESCALATION MARKER:** I am escalating to investigatory orientation at this point, because the empirical re-fetch confirmed that (a) the simulator and educational terms are undefined, (b) two additional prohibitive passages exist that neither predecessor lane surfaced, and (c) the carveout's domain is structurally narrower than the predecessor lanes read it. The question is no longer "which passage applies?" — it is "what specific conditions push the reading each way, and what can the canon honestly say given that F1's text does not close the question?" That is investigatory orientation work.

**Verdict: Reading C, with structure.** F1's text does not resolve whether prix-guesser falls under the carveout or under any of the three relevant prohibitions (Games, Simulators, Apps). The ambiguity is irreducible on F1's current text. But the conditions that push each way are precisely nameable, and the most accurate canon citation describes the navigation rather than confidently invoking one passage.

#### Why Reading A (carveout applies) is not cleanly available

Three obstacles, in order of severity:

1. **Domain mismatch.** The carveout is in Section 2 and its first words restrict it to "Limited use of our Other Intellectual Property Rights for educational purposes…" The Section 2 enumeration of "Other IP Rights" lists data, typeface, statistics, F1-owned still images, audio/AV, F1's official artworks/graphics/assets/textures, and written content. Prix-guesser's authored content per its discovery materials includes circuit geography (NOT in Section 2's list as an F1-owned IP — circuit IP belongs to circuit owners per F1's own page: "If you would like to enquire about licensing any of the circuits' intellectual property rights, such as circuit outlines, please contact the owner of the IP directly"), venue photographs (in Section 2's list IF the photos are F1-owned still images; NOT in Section 2's list if they are third-party photos), and era aesthetics (NOT obviously in Section 2's list unless they reproduce F1's official artworks/graphics/textures). The carveout's domain has uncertain overlap with prix-guesser's actual content types — and the parts that *do* overlap (F1-owned still images) are exactly the parts the project's discovery materials say to handle conservatively.

2. **The "educational" condition is doing real work.** F1's text uses "educational purposes" and "private, educational purpose" — not "educational or fan or entertainment purpose," and not "non-commercial purpose" alone. The text never defines "educational." A party game that asks players to identify F1 venues *can be* characterized as educational (it conveys factual information about F1 geography), but it can also be characterized as entertainment/play that incidentally involves factual content. The plain English meaning of "educational" leans toward formal instruction, classroom use, or content explicitly designed to teach. A trivia/recognition game played at game nights is not obviously educational in that sense; it's a game that uses factual content. The carveout's narrow language is friendly to "I am studying F1 history for my motorsport-engineering thesis and using F1's still images in my private notes" and less obviously friendly to "we're playing a private F1 venue-recognition party game with friends." The latter is plausibly within the carveout under a generous reading, but it is not obviously within the carveout, and Lane 1C / Lane B4 / the orchestrator all treated it as obviously within.

3. **The five stacked qualifiers are stricter than "private fan use."** The carveout requires use to be (i) limited, (ii) justified, (iii) non-commercial, (iv) private (not posted on YouTube, websites, social media), and (v) educational. Prix-guesser plausibly satisfies (i)–(iv) but (v) is the weakest link. Prix-guesser's framing as "private-only" is a strong fit for (iv) but does not by itself supply (v). The conjunction of all five is what the carveout requires; "private only" is one of the five.

Conclusion on Reading A: the carveout *might* apply to prix-guesser's use of F1-owned still images and other Section 2 content, *if* a reasonable reader treats a venue-recognition party game as educational, *and* the use stays strictly off public posting surfaces. That is a chain of three conditions, not a clean fit. Reading A is a defensible argument, not a textual resolution.

#### Why Reading B (simulator clause applies) is not cleanly available

Three obstacles, in order of severity:

1. **The plain reading of "simulator" in 2026 technical and consumer discourse is narrower.** "Motorsport simulator" in current trade and consumer usage refers to physics-modeling software (iRacing, rFactor, Assetto Corsa), official racing games (F1 24, Forza Motorsport), and physical rigs (the parenthetical "racing car chassis" reference confirms this is what F1 had in mind). A browser quiz game that asks "which circuit is this?" does not match the prevailing trade usage. F1's text does not define the term, but if we read by ordinary trade meaning, prix-guesser is not what "motorsport simulator" usually denotes.

2. **The parenthetical example narrows the implied form factor.** "(including those that are digital only or those that incorporate physical elements such as racing car chassis)" is an inclusive parenthetical — it tells us digital-only counts, and physical-rig counts. But the example given for the physical case is "racing car chassis," which signals that the prototypical form factor is something that *physically resembles a racing setup*. This is consistent with the trade meaning. It is not consistent with stretching "simulator" to cover any software that uses F1 content.

3. **The Esports and sim racing subsection is adjacent and defines its scope differently.** The subsection above Simulators talks about "sim racing and/or esports team — including branding of any unofficial sim racing and/or esports team or league." This subsection is clearly about competitive sim-racing as an organized activity. The Simulators subsection is its technical neighbor: it's about the software that sim-racing leagues use. Read in textual context, "Motorsport simulators and/or software that simulates auto racing" naturally pairs with the sim-racing/esports subsection — it's about the racing-simulation software ecosystem, not about any software with F1 content.

Conclusion on Reading B: a brand-protection lawyer with broad reading discretion *could* argue prix-guesser is "software that simulates auto racing" because it uses F1 content to recreate the experience of F1 culture. But the text-internal context, the trade meaning of "simulator," and the parenthetical example all push against that broad reading. Reading B is the less defensible argument, but it is not foreclosed by the text.

#### Why a fourth reading is needed: the Games and Apps subsections

This is the most important finding of LQ-B7.3 and it is independent of the simulator-vs-carveout question. The Games subsection (Passage 3) and the Apps subsection (Passage 4) create their own rules that bear directly on prix-guesser:

**Games subsection rule (a)**: "Our Permitted Word Marks cannot be used to brand any game." This means prix-guesser cannot call itself "Formula 1 Prix Guesser" or "F1 Prix Guesser" or use Permitted Word Marks (F1, Formula 1, Grand Prix, Paddock Club, etc.) as part of its branding. It is silent on whether the game's *internal content* (round prompts, answer text, descriptions) can mention "Formula 1" — but Section 3's editorial rules suggest mentions for informational/reportorial purposes are permitted with specific formatting (BLOCK CAPITALS or Title Case + ™ symbol). Prix-guesser's current canonical name is "Prix Guesser" with the F1 connection in the project's *description* rather than its *brand*, which appears to comply with rule (a). But this is something the canon should be explicit about.

**Games subsection rule (b)**: "Other Intellectual Property Rights including those from the Formula 1 companies' official games cannot be used in third party games." This means F1's Official Artworks, Graphics, Assets and Textures, Audio/AV Content, Still Images, Statistics, Results/Timing data, Official Typeface, and Written Content cannot be used in prix-guesser. The "including those from the Formula 1 companies' official games" qualifier specifically targets people extracting assets from F1's video games — prix-guesser doesn't do that — but the broader rule applies regardless.

**Apps subsection rule**: "Other Intellectual Property Rights cannot be used in apps." Prix-guesser is browser-served software; whether F1 considers it an "app" is itself ambiguous (the term usually denotes mobile apps, but the rule does not say so). If the app rule applies, it is a flat prohibition on Other IP Rights with no carveout.

**The interaction of Games + Apps + the Section 2 educational carveout**: this is where the structural analysis matters. The Section 2 carveout permits limited educational use of Other IP Rights with five conditions. Section 4's Games and Apps subsections prohibit use of Other IP Rights in games and apps, full stop, with no internal carveout. The two are in tension. Two readings of the tension:

- **Resolution X**: the Section 2 carveout is general and the Section 4 prohibitions are specific instances; the specific overrides the general; therefore games and apps cannot rely on the Section 2 carveout. Under this reading, prix-guesser cannot use F1's Other IP Rights at all, even privately and educationally, because games and apps are categorically excluded.
- **Resolution Y**: the Section 2 carveout is a base permission and the Section 4 prohibitions are a baseline that the carveout reads against; the carveout's "limited, justified, non-commercial, private, educational" conditions are the conditions under which the Section 4 prohibitions are softened for educational purposes. Under this reading, prix-guesser *can* use F1's Other IP Rights in private educational ways, even though it's a game/app.

F1's text does not pick. There is no "notwithstanding" or "subject to" cross-reference in either direction. The two sections are presented sequentially without explicit interaction rules. A careful reader has to construct the resolution; the text does not supply it.

**My read**: Resolution X (Section 4 specific overrides Section 2 general) is the more legally conservative reading and is the reading a brand-protection lawyer would default to. Resolution Y is a defensible but more aggressive reading that depends on treating the Section 2 carveout as transversal across all of Section 4's per-category prohibitions. Without F1's official position, prix-guesser cannot rely on Resolution Y as an unambiguous shield. This further weakens Reading A from earlier in this finding.

#### The verdict on LQ-B7.3

**Reading C with structure** is the most accurate framing:

> F1's published guidelines text does not resolve whether prix-guesser falls under the carveout or any of the three relevant prohibitions (Games, Simulators, Apps). The terms "motorsport simulator," "software that simulates auto racing," and "educational" are undefined. The Section 2 educational carveout has uncertain interaction with Section 4's per-category prohibitions and the text contains no cross-reference. Under a conservative reading, the Section 4 Games and Apps prohibitions apply to prix-guesser and the Section 2 carveout does not override them; prix-guesser's use of F1 Other IP Rights would be unpermitted under that reading. Under a more aggressive reading, the Section 2 carveout applies transversally to private educational fan use including in games and apps; prix-guesser's use would be permitted under that reading provided it satisfies all five carveout conditions, including "educational" (which is itself undefined and not obviously a fit for a party game). The simulator clause is plausibly inapplicable on the trade-meaning reading of "motorsport simulator" but is not foreclosed by the text. The most defensible posture is to keep prix-guesser's use of F1-originating IP Rights conservative — content types that are not in Section 2's list, third-party photographs rather than F1-owned still images, no F1 official artworks/graphics/textures, no use of Permitted Word Marks as brand — and to explicitly acknowledge in the canon that this navigates an under-defined intersection rather than confidently invoking the carveout.

This is more honest than either Reading A or Reading B and is a stronger basis for a canon citation than Lane B4's draft text.

---

### LQ-B7.4 — Does the "private, educational purpose" carveout actually cover prix-guesser?

**Verdict: at best, only conditionally and only for some content types; the "educational" label is the weakest link.**

The carveout's five conditions, applied to prix-guesser:

| Condition | Prix-guesser fit | Confidence |
|---|---|---|
| **Justified** | Probably yes (fan use, tribute, play) | Moderate |
| **Limited** | Plausibly yes (M1 scope is narrow) | Moderate |
| **Non-commercial** | Yes (no sales, no ads, no monetization) | High |
| **Private** (not on YouTube/websites/social media) | Yes if friends-only and not publicly posted | High *with operational discipline* |
| **Educational** | Uncertain — see below | Low |

**The "educational" condition is doing the most work and is the least clearly satisfied.** F1's text never defines "educational." Reading by plain English meaning:

- A *narrow* reading of "educational" denotes formal instruction or content designed to teach: classroom materials, study notes, museum exhibits, academic papers, textbook excerpts. Under this reading, prix-guesser is not educational. It is a party game that happens to use educational-style content (factual recognition tasks).
- A *broad* reading of "educational" denotes any use that conveys factual information about a subject. Under this reading, prix-guesser is educational because it conveys facts about F1 venues, circuits, eras, and culture through its quiz format. Many trivia games and quiz apps are framed as "edutainment" under this reading.

F1's text gives no signal which reading they intended. The fact that the carveout is sandwiched between a fair-dealing notice and a "FORMULA 1 Rights" definition — both of which are formal-legal-register language — leans slightly toward the narrow reading. Fair-dealing defenses in UK copyright law (which is the only legal frame F1's document explicitly references) are themselves narrowly construed and require the use to fit a specifically enumerated category (research, private study, criticism, review, news reporting, parody/caricature/pastiche). The fair-dealing context suggests F1's "educational" was written with academic/research use in mind, not trivia entertainment.

**This is the load-bearing finding the orchestrator's framing did not anticipate.** The task spec, Lane 1C, and Lane B4 all implicitly equated "private fan use" with "private educational purpose." F1's text treats them as different things. A party game is plausibly fan use (the Fans definition is favorable) but is not obviously educational use (the carveout's term is narrower than the Fans definition).

**Lane 1C and Lane B4 both implicitly assumed prix-guesser's framing as 'private-only fan game' falls under F1's 'private educational purpose' carveout. If 'private-only' ≠ 'private educational,' the carveout does not actually apply cleanly even under the most favorable reading.** This is true. The carveout does not apply cleanly; it applies *conditionally* under a generous reading and *not at all* under the more text-faithful narrow reading.

**A practical mitigation prix-guesser could adopt** (out of scope for this lane but worth flagging for the synthesizer): the project could explicitly frame the round/answer materials in an instructional register — "this round teaches you how to recognize the Suzuka esses by their crown shape" — which would make the educational characterization more textually grounded. This would convert prix-guesser from "trivia game played by friends" into "private F1 geography study materials used in a quiz format among friends," which is closer to the carveout's term. Whether the project wants to take this on is a separate question; the lane just notes that the carveout's friendliness to prix-guesser is not free, it requires specific framing work.

---

### LQ-B7.5 — Revised canon citation text

**Verdict: Lane B4's draft text overstates the carveout, omits the simulator clause, omits the Games and Apps clauses, and uses a phrase ("within this licensed zone") that does not match F1's text.**

#### Lane B4's draft text (as proposed for the Constraints section)

> "Private-only, unofficial fan project — F1's own trademark guidelines carve out 'limited use for a private, educational purpose only' as permissible fan use, while requiring an express written license for any public use of FORMULA 1 Rights. Early choices should optimize for real play value within this licensed zone rather than incurring public-safe caution or distribution overhead that private use does not require."

Specific problems with this text:

1. **"Carve out as permissible fan use"** misstates the structure. F1's text carves out educational use, not fan use; the Fans definition is separate from the carveout. Prix-guesser is a fan use (definitionally) but the carveout requires educational purpose, not fan purpose.
2. **"Limited use for a private, educational purpose only"** is the carveout's language, but Lane B4's quote elides the "of our Other Intellectual Property Rights" prefix. The carveout's domain is Section 2 content types (data, typeface, statistics, F1-owned still images, audio/AV, official artworks/graphics/textures, written content), not all F1-related content. The elision makes the carveout look broader than it is.
3. **"Requiring an express written license for any public use of FORMULA 1 Rights"** is approximately right but conflates several different prohibitions. F1's text says: simulators need express written license; sim racing/esports teams need express written license; merchandise needs express written license; advertisements/commercials need express written license; commercial use generally needs express written license. There is no single "public use" prohibition; there are several category-specific prohibitions, some of which apply to private use too.
4. **"Within this licensed zone"** is not what F1's text describes. The carveout is conditional permission ("may be acceptable"), not a license. F1's text repeatedly uses "discretion" and "may" language for fan-tolerance items. The phrase "licensed zone" frames the carveout as a clean legal shelter, which it is not.
5. **Omits the simulator clause and the Games and Apps clauses entirely.** Lane B4 explicitly flagged the simulator-vs-carveout tension as out-of-scope for its lane, which was a correct move, but the canon citation Lane B4 drafted does not name the tension or the additional prohibitions. A canon citation that names only the carveout would mislead future readers into thinking the legal posture is settled.

#### Recommended replacement text

The recommendation has three options at different levels of detail. The synthesizer should pick (or compose from) these based on how much weight the canon should give the legal grounding.

**Option 1 — Brief, honest, fits in one Constraints bullet (recommended for the Constraints section)**:

> "Private-only, unofficial fan project — F1's published trademark guidelines (`https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt`) contain a narrow conditional permission for 'limited use of our Other Intellectual Property Rights for educational purposes' that is private, justified, limited, and non-commercial; they also contain category-specific prohibitions on third-party games, apps, and motorsport simulators using F1's Intellectual Property Rights without an express written license. The project's posture navigates an under-defined intersection of these passages by staying private, non-commercial, and bounded to content types F1 does not enumerate as protected (circuit geography belongs to circuit owners; venue references should avoid F1-owned still images, official graphics, or other Section 2 enumerated material). The 'private-only' choice is therefore both a product-quality decision and a risk-reduction decision; it does not constitute a clean legal carveout."

**Option 2 — One sentence, for a Key Decisions table cell augmentation**:

> "Public-safe constraints would distort the early product and reduce fidelity; additionally, F1's trademark guidelines (https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt) contain no clean carveout for fan games even privately played, and the safest posture is to stay private, non-commercial, and bounded to content types F1 does not enumerate as protected."

**Option 3 — Short and modest (if the canon prefers minimal legal language)**:

> "Private-only, unofficial fan project — F1's trademark guidelines (formula1.com/en/information/guidelines) prohibit unlicensed use of F1's Intellectual Property Rights in third-party games and apps, with a narrow conditional carveout for private educational use of certain materials. The project's posture is to stay strictly private and to use content types outside the protected list, treating the legal grounding as risk reduction rather than as a license."

**My recommendation**: Option 1 for the PROJECT.md Constraints section, plus Option 2's last clause appended to the Key Decisions table row. Option 3 is the fallback if the project owner wants the citation to be very small. The crucial change from Lane B4's draft is that all three options name BOTH the carveout AND the prohibitions, and all three drop "within this licensed zone" in favor of language that acknowledges the navigation rather than claiming a clean shelter.

---

### LQ-B7.6 — Anything the search surfaced that the lane questions did not anticipate

Five items:

1. **The Games and Apps subsections.** Already discussed above. These are the most consequential discovery of the lane and were not anticipated by the task spec, Lane 1C, or Lane B4.

2. **The "Fans" definition is favorable to prix-guesser but does not unlock specific permissions.** The task spec implicitly treated "fan use" as if it were a permission category. F1's text defines Fans (and prix-guesser fits) but Section 4's Fundamental Principles and per-category prohibitions still apply to fan-conducted activity. The Fans definition is necessary but not sufficient.

3. **F1's own page directs circuit IP licensing questions to circuit owners.** Verbatim: "If you would like to enquire about licensing any of the circuits' intellectual property rights, such as circuit outlines, please contact the owner of the IP directly." This is a critical finding for prix-guesser: F1's guidelines explicitly disclaim ownership of circuit IP. Prix-guesser's core fantasy ("GeoGuessr for F1 places") is built on circuit and venue recognition, and F1 is telling readers that circuit IP is not theirs. This *strengthens* prix-guesser's posture for the circuit-content side of its work but *redirects* the legal exposure to circuit owners (which prix-guesser would need to think about separately for any specific circuit's protected materials). The orchestrator's framing did not anticipate this redirection.

4. **The Artificial Intelligence prohibition.** F1's text contains a flat prohibition on use of FORMULA 1 Rights "for text and data mining and in or with any artificial intelligence technology, including in connection with training; development; or operation of large language models or other generative artificial intelligence models, tools or systems without an express licence from the Formula 1 companies. All rights reserved." This is out of M1 scope (the project explicitly disclaims AI-generated content as a basis) but is worth flagging for any future M3 scope that involves AI assistance with content generation, prompt drafting, or research using F1 materials. If a future phase uses an LLM to draft round descriptions about F1, that may itself be in the scope of this prohibition.

5. **The "fair dealing" disclaimer in Section 2.** F1's text acknowledges UK fair dealing as a possible defence and notes other countries may differ. This is an interesting structural acknowledgment: F1 is saying "our guidelines are our policy, but if you have a fair-dealing-style legal defence in your jurisdiction, we are not pretending to override that." This means the legal landscape for prix-guesser is partially shaped by general copyright law (fair dealing in UK; fair use in US; varying analogues elsewhere) independent of F1's own policy text. This is a framework-invisibility item — see below.

---

## Framework Invisibility Section

The four specific items the task spec named, addressed in turn.

### 1. Text vs. enforcement gap

This lane reads what F1's guidelines *say*. It cannot see how F1 *enforces* them. The empirical reality is that F1DLE, Formudle, Stewardle, Driverle, Who Are Ya?, and many other public unofficial F1 fan games operate publicly without takedowns. F1's published policy says "public posting on YouTube, websites and social media" disqualifies the educational carveout, and sim-racing software needs an express written license — yet a Google search confirms multiple public fan-game sites that nominally violate these rules and are not enforced against. The de facto enforcement posture is more permissive than the published text. My lane cannot quantify or characterize this gap because I am only reading the text. The synthesizer should treat my finding as "what F1's text would support if applied strictly," not "what F1 will do." Prix-guesser's strict private posture sits on the strict-text side of the gap; F1DLE et al. sit on the lenient-enforcement side. The choice between them is an enforcement-tolerance bet, not a text-reading question.

### 2. F1's text vs. general IP law

F1's published guidelines are one source of legal exposure. Copyright law, trademark law, fair use, fair dealing, and parody/transformative-use doctrines operate independently of F1's policy. F1's text in Section 2 explicitly acknowledges this for fair dealing. My lane cannot evaluate prix-guesser's exposure under any country's general IP law; that would require formal legal analysis I am not equipped to do. The framework invisibility here is that prix-guesser's true legal landscape is broader than this one document. F1's text is the *most directly relevant* source because F1 owns the primary rights at issue, but it is not the *only* source.

### 3. One document vs. the full F1 legal publication landscape

F1 publishes other legal documents I have not read: ticket terms (referenced from this guidelines page at `tickets.formula1.com/en/t-61-terms-and-conditions`), commercial licensing terms presumably available through `brandprotection@f1.com`, and presumably various unpublished internal policies. The page also references the Formula One Licensing B.V. corporate entity that holds the marks, the F1 Esports series at `f1esports.com` (which has its own scope), and the Formula 1 companies' "official games" which presumably have their own EULA terms. All of these are out of scope for this lane. The synthesizer should treat my reading as "the public-facing trademark guidelines document only."

### 4. The "private-only" category vs. the specific shape of prix-guesser

This is the most important framework-invisibility finding for the synthesizer because it ties directly to the orchestrator's blind spot.

The task spec, Lane 1C, and Lane B4 all treated "private-only fan game" as a uniform category that the carveout applies to. My empirical re-fetch shows that F1's carveout language is "private, educational purpose only" — and prix-guesser's fit to "educational" is the most uncertain part of the carveout. The orchestrator's framing of the ambiguity as "carveout vs. simulator" obscures a third question: even if the simulator clause is not the applicable passage, is the carveout actually *applicable* to a party game (as opposed to a private study aid or classroom material)? My lane finds the answer is "uncertain at best" — and the orchestrator's framing did not surface this third question.

The framework invisibility is that "private-only" is doing two different jobs in the predecessor framing. It is operating as (a) the *operational* posture (no public posting), and (b) the *legal* category (private use). These are not the same thing. F1's carveout requires private *educational* use, not just private use. A party game played strictly in private satisfies the operational sense of "private" but does not by itself satisfy the legal-category sense of "private educational." Lane 1C and Lane B4 silently conflated the two; the orchestrator inherited the conflation.

This is a successful lane finding in the sense the task spec prepared for: "if your reading contradicts the orchestrator's framing, that is a successful lane."

---

## Rule 5: Frame-Reflexivity

Three questions, answered concretely.

### Q1 — If classified as `requirements_review` instead of `claim_integrity`, what would I have looked for that I didn't?

A requirements_review would have asked: "Does prix-guesser meet a specific, testable legal-compliance requirement derived from F1's policy?" This framing would have produced concrete requirement-shaped findings I did not produce, for example:

- "REQ: Project content must not include F1-owned still images." (testable: any image source list)
- "REQ: Project content must not include F1's official typeface or close imitations." (testable: any typeface specification)
- "REQ: Project name and brand must not use Permitted Word Marks." (testable: project naming conventions)
- "REQ: Hosted instances must not be accessible from public internet without authentication." (testable: deployment configuration)
- "REQ: Round content must not reproduce F1's official artworks, graphics, assets, or textures." (testable: content authoring rules)
- "REQ: Future AI-assisted content generation phases must obtain F1 licensing or use only non-F1-owned source material." (testable: any AI-using phase)

These are derivable from F1's text but not explicit in it. A requirements_review would have produced this list as its primary deliverable. My claim_integrity lane produced revised citation text instead. The synthesizer should consider whether the project would benefit from a follow-up requirements_review pass that converts F1's text into testable rules for the canon's REQUIREMENTS.md.

### Q2 — If classified with `investigatory` orientation from the start, what would I have held open from the first paragraph?

I escalated mid-lane, so this is partially answered by what I did. But starting investigatory would have changed two things:

- **I would have framed the four passages as a *system* from paragraph one rather than starting with "verify Lane 1C's two quotations."** Standard orientation oriented me toward the citation-verification task first; investigatory orientation would have oriented me toward "what is the structure of F1's policy as a whole and how does prix-guesser sit within it?" The Games and Apps subsections would have come up earlier in my read.
- **I would have held open the question of whether the canon should cite F1's text *at all*.** Standard orientation accepted Lane B4's framing that the citation should be added; the question was just which passage to cite. Investigatory orientation would have asked whether citing F1's text in the canon (a) genuinely strengthens the project's posture, (b) introduces a citation the project might be unable to defend if F1 ever asked for clarification, or (c) is performative legal cover that does not actually reduce risk. Lane B4's standard-orientation answer was "yes, cite it"; investigatory orientation would have left this open longer and considered the case for not citing it at all (e.g., "if the legal landscape is ambiguous and the canon citation cannot honestly resolve the ambiguity, maybe the canon should record the situation in a discovery/decision file rather than as a constraint that implies legal grounding"). I am not retracting my LQ-B7.5 recommendation, but an investigatory lane would have been less quick to commit to "the canon should cite F1's guidelines."

### Q3 — What does claim_integrity × standard × general-purpose (Opus with WebFetch) shape me to notice and not notice?

Concrete example: the framing oriented me toward **the text of the guidelines** (what does F1 say?) and away from **the practice surrounding the guidelines** (how does F1 enforce them; how do similar projects handle the same text; what do brand-protection lawyers actually advise for fan games). I did not search for case law, did not search for F1's published enforcement actions, and did not look for industry guidance on fan-game IP exposure beyond the predecessor lanes' references. This is appropriate for a claim_integrity check (which is about whether the citation is accurate and supported), but it means my read is less grounded in practice than a `risk_assessment` or `due_diligence` lane would be. The synthesizer should treat my findings as "what F1's text says" and not as "what prix-guesser's actual legal exposure is."

A second concrete example: WebFetch shapes what I see by returning processed/summarized text rather than raw HTML. Two fetches with different prompts mitigate but do not eliminate the possibility that something on the page was filtered out by the fetch model's summarization. I am moderately confident I have seen the substantive text of the guidelines; I am less confident I have seen everything (e.g., footnotes, fine print, embedded link text, hover-state legal disclaimers).

**Anti-performativity self-check**: the concrete thing I would have done differently under requirements_review is the testable-rule list above. The concrete thing I would have done differently under investigatory orientation from the start is reading the four passages as a system rather than starting from Lane 1C's two-passage selection. These are real, not nominal.

---

## What the Obligations Didn't Capture

Two items.

**1. The "should the canon cite this at all?" question is outside both standard and investigatory orientation as I am running them.** Lane B4 produced a draft citation and my lane was tasked to verify or revise it. Neither lane was tasked to ask whether the citation should exist. After completing this work, I think there is a real argument that *citing F1's guidelines in the canon is risk-additive rather than risk-reductive*: a canon citation creates a documentary record of the project's awareness of F1's policy, which (in a hypothetical enforcement scenario) could be used to argue that the project knowingly relied on a carveout it did not actually fit. A canon that does not cite F1's text is in a "we made a private fan project, here are the constraints we chose" posture; a canon that cites F1's text and confidently invokes the carveout is in a "we relied on F1's published carveout" posture, and the latter is more vulnerable if F1's text does not actually carve out what the citation claims it carves out. I am not recommending against citation — my LQ-B7.5 text is honest enough that this risk is mitigated — but the obligations did not have a place for this consideration and the synthesizer should hold it.

**2. The lane questions implicitly assumed F1's published text is the right document to read.** It might not be. The most legally relevant document for prix-guesser might be circuit owners' separate IP terms (F1's page redirects to those for circuit outlines), or general copyright law in the UK/US/EU, or the project owner's local jurisdiction's analogue to fair dealing/fair use. Reading F1's text was the assigned task and I did it; but the obligations did not have a place to flag that the assigned task may not be the most decision-relevant question. The Wave 3 synthesizer should consider whether to dispatch a follow-up lane on circuit IP exposure separately.

---

## Cross-Lane Notes for the Synthesizer

### What B7 changes about Lane B4's recommendations

- **Lane B4's LQ-B4.4 minimum viable text (the proposed Constraints annotation) needs revision.** The phrase "carve out 'limited use for a private, educational purpose only' as permissible fan use" misstates F1's carveout. The phrase "within this licensed zone" overstates what the carveout provides. The omission of the simulator clause and (more importantly) the omission of the Games and Apps subsections are material omissions. Use Option 1 from LQ-B7.5 instead.
- **Lane B4's LQ-B4.5 gap-or-choice reading remains valid.** Lane B4's assessment that the absence of legal citation is more likely a gap than a choice is not contradicted by my findings; it is independent of which passage applies.
- **Lane B4's broader finding that the canon should ground "private-only" in something more than a product-quality argument is endorsed and strengthened.** My lane finds that the legal grounding is more complex than Lane B4's draft suggested, but the *need* for a legal grounding is reinforced — not weakened — by the additional prohibitions I surfaced.

### What B7 changes about Lane 1C's findings

- **Lane 1C's two quotations are accurate.** Verified verbatim.
- **Lane 1C's Finding B ("the carveout is the strongest defense the canon is currently not fully leveraging")** is more uncertain than Lane 1C presented it. The carveout exists; whether it is the strongest defense depends on whether it actually covers prix-guesser, which is uncertain at best. Reframing: "the carveout is one passage in F1's guidelines that is potentially relevant to prix-guesser's posture, alongside the Games, Apps, and Simulators prohibitions; the canon's failure to engage F1's guidelines at all leaves the project's posture less grounded than it could be, but engaging the guidelines requires engaging the full structure rather than confidently invoking the carveout."
- **Lane 1C's selection of two passages from a longer page was incomplete.** This is not a quotation error (the quotes are accurate) but it is a selection error that propagated downstream. Lane B4 inherited the incomplete selection in good faith. This is a useful learning for the audit's chain-integrity discipline: even careful WebFetch readings by Opus agents can produce passage-selection blind spots that downstream lanes inherit unless explicitly re-checked.

### What the Wave 3 synthesizer should hold fixed vs. revise

**Hold fixed:**

- The basic shape of the recommendation (the canon should make some kind of legal grounding explicit).
- Lane B4's identification of the right slot (Constraints section of PROJECT.md, possibly augmenting the Key Decisions table row).
- Lane 1C's finding that prix-guesser's "private-only" posture can be grounded in something more than scope management.

**Revise:**

- The specific language of the citation (use my Option 1 text or compose from Options 1–3).
- The framing of the carveout as "permissible fan use" → reframe as "narrow conditional permission for private educational use of Other Intellectual Property Rights."
- The implicit assumption that "private-only" and "private educational" are equivalent → make explicit that they are not, and that prix-guesser's fit to "educational" is uncertain.
- The omission of the Games / Apps / Simulators prohibitions → name them as part of the same legal landscape the carveout sits within.

**Open questions for the synthesizer to route:**

- Should the canon cite F1's guidelines at all, given the risk-additive consideration in "What the Obligations Didn't Capture" item 1? My recommendation is yes with honest language; the synthesizer should weigh the alternative.
- Should a follow-up lane address circuit-owner IP separately from F1 IP? F1's page explicitly redirects circuit IP questions to circuit owners, and prix-guesser's core content depends on circuit recognition. This is a different legal conversation.
- Should a follow-up requirements_review pass convert F1's text into testable canon rules (the list in my Rule 5 Q1)? This is not what my lane produced and would be a useful complement.

---

## Chain-Integrity Ledger

For each load-bearing claim from the predecessor lanes, status: VERIFIED / MODIFIED / CONTRADICTED.

### Lane 1C claims

| # | Claim | Status | Notes |
|---|---|---|---|
| 1C-A | Quoted educational-purposes passage is accurate | **VERIFIED** | Verbatim re-verified 2026-04-11. |
| 1C-B | Quoted simulators passage is accurate | **VERIFIED** | Verbatim re-verified 2026-04-11. |
| 1C-C | The carveout legitimates prix-guesser's "private-only" framing | **MODIFIED** | The carveout exists but its applicability to prix-guesser is conditional on satisfying "educational" (uncertain), and is in tension with Section 4's Games and Apps prohibitions which Lane 1C did not surface. The legitimation is partial, not complete. |
| 1C-D | The carveout is "the strongest defense the canon is not leveraging" (Finding B) | **MODIFIED** | The carveout is *a potentially relevant defense*; whether it is the strongest depends on whether it covers prix-guesser. The "strongest" framing was an over-reach not supported by the text alone. |
| 1C-E | Prix-guesser exits the F1-sanctioned zone the moment it extends to public hosting | **VERIFIED in part** | F1's text does say public posting disqualifies the carveout. But "F1-sanctioned zone" is Lane 1C's framing; F1's text does not describe a sanctioned zone, it describes conditional permission. |
| 1C-F | Lane 1C selected the two relevant passages from the page | **MODIFIED** | The two quoted passages are accurate but the page contains additional in-scope passages (Games, Apps, Esports, Fans definition, Fundamental Principles) that Lane 1C did not extract. |

### Lane B4 claims

| # | Claim | Status | Notes |
|---|---|---|---|
| B4-A | The canon does not cite F1's guidelines | **VERIFIED** | Independent of my fetch; Lane B4's grep work is sound. |
| B4-B | The canon does not cite any legal rationale for private-only | **VERIFIED** | Same. |
| B4-C | The canon frames private-only as a product/scope decision rather than a legal one | **VERIFIED** | Same. |
| B4-D | The right slot for citation is PROJECT.md Constraints section | **VERIFIED** | Same; my recommendations also live in this slot. |
| B4-E | Minimum viable text invoking the carveout is appropriate | **CONTRADICTED** | The minimum viable text overstates the carveout, omits the prohibitions, and uses "within this licensed zone" framing that does not match F1's text. Replacement text proposed in LQ-B7.5. |
| B4-F | The simulator-vs-carveout tension is unresolved (flagged out-of-scope) | **VERIFIED** | The tension is unresolved on F1's text. Lane B4's flag was correct. |
| B4-G | Lane B4 took Lane 1C's quotations in good faith without web access | **VERIFIED** | Appropriate for a Sonnet gsdr-auditor without WebFetch. |

### Task spec / orchestrator claims

| # | Claim | Status | Notes |
|---|---|---|---|
| TS-A | The ambiguity is "carveout vs. simulator" | **MODIFIED** | The actual ambiguity is wider — Games and Apps subsections add prohibitions the orchestrator did not name, and the carveout's "educational" condition is itself ambiguous in a way the orchestrator's framing implicitly closed. |
| TS-B | "Educational purpose" and "motorsport simulator" are not obviously resolved in prix-guesser's favor | **VERIFIED** | The orchestrator's caveat is correct. My lane confirms neither term is resolved in prix-guesser's favor by F1's text. |
| TS-C | Three readings (A: carveout, B: prohibition, C: irreducible) | **MODIFIED** | The verdict is C with structural specifics, including the addition of Games/Apps prohibitions the three-reading framing did not anticipate. |
| TS-D | Lane B4 was Sonnet gsdr-auditor without web access | **VERIFIED** | Confirmed in Lane B4's frontmatter. |
| TS-E | Lane 1C was Opus general-purpose with WebFetch | **VERIFIED** | Consistent with Lane 1C's tooling and methodology. |

---

## Closing note for Wave 3

The most important sentence in this lane is in LQ-B7.4:

> "The orchestrator's framing of the ambiguity as 'carveout vs. simulator' obscures a third question: even if the simulator clause is not the applicable passage, is the carveout actually *applicable* to a party game (as opposed to a private study aid or classroom material)?"

The synthesizer should treat this as the lane's central finding. The canon citation, if added, should be honest about the underdetermined intersection rather than confidently invoking the carveout. The recommended Option 1 text from LQ-B7.5 is the lane's deliverable for that purpose.

— Lane B7 (Claude Opus 4.6, general-purpose, fetched 2026-04-11)
