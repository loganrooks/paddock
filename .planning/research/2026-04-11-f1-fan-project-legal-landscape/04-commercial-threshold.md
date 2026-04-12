---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-4
question_focus: donation-commercial-threshold
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
tools_used: [WebFetch, WebSearch]
predecessor_lanes:
  - wave-2-lane-b7-f1-legal-ambiguity.md
output_file: 04-commercial-threshold.md
fetch_timestamps: "all fetches performed 2026-04-11"
not_legal_advice: true
---

# B8-4 — Commercial / Non-Commercial Threshold Research

**Model:** Claude Sonnet 4.6 (general-purpose agent with WebFetch and WebSearch).
**Research question:** If prix-guesser accepts donations (Patreon, Ko-fi, GitHub Sponsors, or similar) to cover server and hosting costs — no profit, purely cost recovery — does this count as "commercial use" under F1's own policy text, US copyright doctrine, UK fair dealing, and Canadian copyright doctrine?
**Jurisdiction note:** The project owner is Canadian. Analysis covers CA/US/UK doctrine in that order of contextual relevance.
**Not a legal opinion.** Empirical doctrinal observations only. Every interpretation-heavy claim is flagged `[OPUS-FOLLOWUP]`.

---

## Sources Table

| ID  | URL | Fetch date | Source type | Description |
|-----|-----|------------|-------------|-------------|
| S1  | https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt | 2026-04-11 | Policy (private) | F1 Fan & Content Creator Guidelines — full page, two fetches |
| S2  | https://www.copyright.gov/title17/92chap1.html | 2026-04-11 | Statute (US) | 17 U.S.C. §107 verbatim text from copyright.gov |
| S3  | https://supreme.justia.com/cases/federal/us/471/539/ | 2026-04-11 (search-retrieved) | Case law (US) | Harper & Row Publishers v. Nation Enterprises, 471 U.S. 539 (1985) |
| S4  | https://www.law.cornell.edu/supct/html/92-1292.ZS.html | 2026-04-11 | Case law (US) | Campbell v. Acuff-Rose Music, Inc., 510 U.S. 569 (1994) |
| S5  | https://en.wikipedia.org/wiki/Fair_dealing_in_United_Kingdom_law | 2026-04-11 | Commentary/secondary | Wikipedia article on UK fair dealing (citing CDPA 1988 §29) |
| S6  | https://laws-lois.justice.gc.ca/eng/acts/C-42/section-29.html | 2026-04-11 | Statute (CA) | Canadian Copyright Act, section 29 verbatim |
| S7  | https://laws-lois.justice.gc.ca/eng/acts/C-42/section-29.21.html | 2026-04-11 | Statute (CA) | Canadian Copyright Act, section 29.21 (Non-commercial UGC) verbatim |
| S8  | https://creativecommons.org/2009/09/14/defining-noncommercial-report-published/ | 2026-04-11 | Commentary | CC "Defining Noncommercial" study blog post + report data |
| S9  | https://wiki.creativecommons.org/wiki/NonCommercial_interpretation | 2026-04-11 | Commentary | CC wiki on NonCommercial interpretation |
| S10 | https://www.transformativeworks.org/fanworks-fair-use-and-fair-dealing/ | 2026-04-11 | Commentary (OTW) | Organization for Transformative Works — "Fanworks, Fair Use, and Fair Dealing" (2018) |
| S11 | https://www.copyright.gov/fair-use/ | 2026-04-11 | Policy/guidance (US) | US Copyright Office — fair use overview page |
| S12 | https://ir.lawnet.fordham.edu/iplj/vol31/iss2/4/ | 2026-04-11 | Commentary (law review) | Rachel Morgan, "Conventional Protections for Commercial Fan Art Under the U.S. Copyright Act," 31 Fordham IPLJ (2021) — abstract only accessible |
| S13 | https://www.yorku.ca/osgoode/iposgoode/2015/11/11/the-user-generated-content-exception-moving-away-from-a-non-commercial-requirement/ | 2026-04-11 | Commentary (academic) | Mariam Awan, "The User-Generated Content Exception: Moving Away from a Non-Commercial Requirement," IPOsgoode (Nov 11, 2015) |
| S14 | https://www.lib.sfu.ca/help/academic-integrity/copyright/user-generated-content | 2026-04-11 | Commentary (library guide) | SFU Library — "What is non-commercial user-generated content?" — explanation of §29.21 |

**Source type key:** Statute = primary binding authority in jurisdiction. Case law = primary binding or persuasive authority. Policy = F1's own private-party guidelines (not law). Commentary = secondary non-binding analysis.

**Note on UK statute (CDPA 1988 §29):** Direct WebFetch of legislation.gov.uk/ukpga/1988/48/section/29 returned empty content on 2026-04-11. UK statutory text is therefore derived from search results and secondary sources (S5), not a direct statute fetch. Verbatim quotes from CDPA are labeled as such with caveat. [OPUS-FOLLOWUP: UK statute text is not first-hand verified from official source on this fetch date; Opus or lawyer should verify §29 and §29A verbatim text against legislation.gov.uk directly]

---

## Section 1 — F1 Guidelines Re-Read: Commercial Language

**Methodology:** Two targeted WebFetches of [S1] on 2026-04-11 with prompts focused specifically on commercial-related language. B7 (Opus, 2026-04-11) conducted broader fetches on the same day. This lane's fetches found consistent content with B7.

**B7 verification:** B7 stated "F1's text contains no definition of 'commercial' in F1's text." This lane's targeted commercial-language fetch confirms that finding. F1 uses the word "commercial" in multiple places but never defines it. See passages below.

### All commercial-related passages from F1's guidelines (verbatim, with section context)

**Passage F1-A — "Fans" definition, Introduction:**
> "'Fans' in this context mean individuals, groups or collectives including for example not for profit institutions such as fan clubs. For the purposes of these guidelines Fans will be those who follow FORMULA 1 events and are active in supporting the races but without doing so in a **materially commercial manner**, subject to our discretion. A materially commercial manner may include using the FORMULA 1 Rights:
>
> - for clickbait purposes to promote **commercial offers, promotions or activities** either related or unrelated to the FORMULA 1 events;
> - to build traffic and/or following to a website and/or social profiles in order to **sell goods or services** rather than genuinely provide a service for fellow fans;
> - for **advertising and/or promotional purposes** that is excessively repetitive or otherwise intrusive, such as targeted ads directed at a select user base."

[S1, fetch 2026-04-11]

**Passage F1-B — Section 2, Other Intellectual Property Rights (the carveout):**
> "Limited use of our Other Intellectual Property Rights for educational purposes may be acceptable where the use is justified, limited, and **non-commercial**. However, please note, this does not include public postings such as YouTube, websites and social media. It must be for a private, educational purpose only."

[S1, fetch 2026-04-11; verified verbatim by B7]

**Passage F1-C — Section 4, Social Media subsection:**
> "Our Permitted Word Marks can be used editorially for **non-commercial purposes** on social media platforms and on mobile services so long as the use is to inform or report and not to brand…"
> "Our Permitted Word Marks may be used for **non-commercial** social media hashtags for example #F1 #Formula1."

[S1, fetch 2026-04-11]

**Passage F1-D — Section 4, Apps subsection:**
> "Our Permitted Word Marks can be used editorially for **non-commercial purposes** in relation to apps so long as the use is to inform or report and not to brand, i.e. in the paragraphs of accompanying text to describe the app.
>
> Other Intellectual Property Rights cannot be used in apps. For further guidance on timing data please see Timing Data category below."

[S1, fetch 2026-04-11]

**Passage F1-E — Section 4, "Commercial use" subsection (the dedicated subsection):**
> "The FORMULA 1 Rights cannot be used on or in relation to any **goods/services provided for sale**/promotional giveaways without an express licence from the Formula 1 companies."

[S1, fetch 2026-04-11]

**Passage F1-F — Section 4, Merchandise subsection:**
> "You cannot use the FORMULA 1 Rights in respect of your own merchandise in any way."

[S1, fetch 2026-04-11]

**Passage F1-G — Section 4, Endorsement or sponsorship subsection:**
> "The FORMULA 1 Rights cannot be used in any manner, in any medium, that implies the Formula 1 companies' affiliation with or endorsement, **sponsorship**, support of any third party."

[S1, fetch 2026-04-11]

**Passage F1-H — Section 4, Advertisements and Promotions subsection:**
> "The FORMULA 1 Rights cannot be used in **advertisements** or commercials so as to create an unauthorised association between the Formula 1 companies and a third party."

[S1, fetch 2026-04-11]

### What F1's guidelines say and don't say about "commercial"

F1 uses "non-commercial" as a condition in four places (Passages F1-B, F1-C, F1-D, and the Apps subsection). In none of these places does F1 define what "non-commercial" means. The closest F1 comes to a definition is the "materially commercial manner" examples in the Fans definition (Passage F1-A). Those examples are:
1. Clickbait to promote commercial offers
2. Building traffic to sell goods/services
3. Excessively repetitive advertising

**What is absent from F1's text:** F1's guidelines contain no mention of the words "donation," "Patreon," "Ko-fi," "GitHub Sponsors," "hosting," "server," "cost recovery," "profit," "non-profit," "nonprofit," "revenue," "fee," or "charge." The word "free" does not appear in relation to commercial status. The word "unpaid" does not appear at all.

**Finding F1-1:** F1's "Commercial use" subsection (Passage F1-E) defines F1's dedicated "commercial use" prohibition narrowly as: goods/services provided for sale, or promotional giveaways. Cost-recovery donations do not obviously fall within "goods/services provided for sale." A donation button requesting server-cost support is not selling a good or service. [OPUS-FOLLOWUP: this is a textual inference — F1's dedicated "Commercial use" subsection's language suggests a goods/services-for-sale framing, but F1 has not published interpretive guidance on whether donations fall inside or outside this subsection. The conclusion that donations are excluded from the F1-E prohibition is inference, not textual resolution.]

**Finding F1-2:** F1's "materially commercial manner" definition in the Fans definition (Passage F1-A) gives three examples; none of them describes accepting voluntary donations. The third example ("advertising/promotional purposes that is excessively repetitive or otherwise intrusive, such as targeted ads") requires active advertising behavior — a passive donation button is not an advertisement directed at users. [OPUS-FOLLOWUP: "targeted ads directed at a select user base" is listed as an example of "excessively repetitive or otherwise intrusive" advertising. A Patreon/Ko-fi page is not a targeted ad, but whether a donate link on the prix-guesser app constitutes any form of advertising under F1's framing is unclear.]

**Finding F1-3:** The carveout at F1-B requires use to be "non-commercial." F1's text gives no definition of this term in context. Given F1's own commercial examples focus on goods-for-sale, brand promotion, and targeted advertising, a pure cost-recovery donation model appears to fall outside the three examples — but F1 retains discretion ("subject to our discretion" appears in the Fans definition). [OPUS-FOLLOWUP: F1's discretion reservation means the textual analysis of "non-commercial" is ultimately advisory; F1 could re-characterize a donation-funded fan project as "materially commercial" at its own discretion. This cannot be foreclosed by text alone.]

**Finding F1-4:** B7 found no definition of "commercial" in F1's text. This targeted lane confirms that finding with complete agreement. F1's "Commercial use" subsection heading exists but its content is not a definition — it is a specific prohibition (goods/services for sale). The term "non-commercial" in F1's carveout (F1-B) remains undefined.

---

## Section 2 — US Copyright Doctrine: 17 U.S.C. §107

### Statutory text

Section 107 states (full text, verbatim):

> "Notwithstanding the provisions of sections 106 and 106A, the fair use of a copyrighted work, including such use by reproduction in copies or phonorecords or by any other means specified by that section, for purposes such as criticism, comment, news reporting, teaching (including multiple copies for classroom use), scholarship, or research, is not an infringement of copyright. In determining whether the use made of a work in any particular case is a fair use the factors to be considered shall include—
>
> **(1)** the purpose and character of the use, including whether such use is of a commercial nature or is for nonprofit educational purposes;
>
> **(2)** the nature of the copyrighted work;
>
> **(3)** the amount and substantiality of the portion used in relation to the copyrighted work as a whole; and
>
> **(4)** the effect of the use upon the potential market for or value of the copyrighted work."

[S2, copyright.gov, fetch 2026-04-11]

The statute does not define "commercial nature" or "nonprofit educational purposes" in §107 or in §101 (definitions). [S2]

**Observation:** Factor (1) pairs "commercial nature" against "nonprofit educational purposes" as the two poles, but does not treat them as binary or exhaustive. The phrase "including whether" signals that commercial vs. nonprofit is one consideration within the broader "purpose and character" inquiry. [OPUS-FOLLOWUP: whether a cost-recovery donation model is "commercial" or "nonprofit educational" under §107(1) is a doctrinal characterization of a specific fact pattern, not a text-resolved question.]

### Harper & Row Publishers v. Nation Enterprises, 471 U.S. 539 (1985)

The Supreme Court's most quoted passage on the commercial factor from Harper & Row is:

> "The crux of the profit/nonprofit distinction is not whether the sole motive of the use is monetary gain but whether the user stands to profit from exploitation of the copyrighted material without paying the customary price."

[S3, Harper & Row, 471 U.S. 539 (1985), as retrieved via Justia search summary 2026-04-11]

[CAVEAT: This verbatim quote is from a search summary of the case, not a direct first-hand fetch of the opinion. The Justia page returned a 403 error on direct fetch. The quote is widely reproduced across legal sources and is high-confidence, but the citation should be verified against the original opinion. OPUS-FOLLOWUP: Verify Harper & Row verbatim quote from original Supreme Court reporter or law.cornell.edu.]

**Significance for prix-guesser:** Under the Harper & Row test, the question is not whether the project makes money, but whether it "stands to profit from exploitation of the copyrighted material without paying the customary price." A project accepting cost-recovery donations is not profiting from the exploitation — it is recovering operating costs. If no F1 license is being substituted for (because no license would typically be issued for a private fan quiz game), the "customary price" argument weakens. [OPUS-FOLLOWUP: applying Harper & Row's "customary price" test to a fan project that has never been offered a license is a doctrinal extension; this is analytical inference, not a cited holding.]

### Campbell v. Acuff-Rose Music, Inc., 510 U.S. 569 (1994)

The Court stated:

> "The statute makes clear that a work's commercial nature is only one element of the first factor enquiry into its purpose and character."

And:

> "The more transformative the new work, the less will be the significance of other factors, like commercialism, that may weigh against a finding of fair use."

[S4, Campbell v. Acuff-Rose, 510 U.S. 569 (1994), as retrieved via Cornell LII fetch 2026-04-11]

**Significance:** Campbell explicitly rejected treating commercial nature as presumptively fatal to fair use. A commercially-funded use can still be fair; a donation-funded use that might technically be "commercial" does not therefore fail fair use automatically. [OPUS-FOLLOWUP: Campbell addressed a for-profit parody, not a cost-recovery donation model. The holding that commercial nature is "only one element" does not resolve whether cost-recovery donations are "commercial" — it only tells us that if they are, that is not necessarily determinative.]

### US Copyright Office guidance

The US Copyright Office fair use page states:

> "Courts look at how the party claiming fair use is using the copyrighted work, and are more likely to find that nonprofit educational and noncommercial uses are fair."

But also:

> "This does not mean, however, that all nonprofit education and noncommercial uses are fair and all commercial uses are not fair."

[S11, copyright.gov/fair-use/, fetch 2026-04-11]

### US doctrine: tentative synthesis

Under US copyright law, "commercial" in §107(1) means, per Harper & Row, "standing to profit from exploitation of the copyrighted material without paying the customary price." Cost-recovery donations that do not produce profit do not clearly fall within that definition. Campbell confirms that commercial nature is "only one element" even if it is present. The Copyright Office acknowledges the distinction is not binary. [OPUS-FOLLOWUP: No case specifically addresses cost-recovery donation models for fan projects. All application to the prix-guesser fact pattern is inference from general doctrine.]

---

## Section 3 — UK Copyright Doctrine: CDPA 1988 Fair Dealing

**Note on source:** Direct WebFetch of legislation.gov.uk for CDPA 1988 §29 returned empty content on 2026-04-11. UK statutory text is derived from the Wikipedia fair dealing article [S5] and search result summaries citing the statute. Treated as secondary sources; marked accordingly. [OPUS-FOLLOWUP: UK statute text requires verification against legislation.gov.uk or a Westlaw source.]

### CDPA 1988 Section 29 — Research and private study

Per S5 (Wikipedia, citing CDPA 1988):

> "Fair dealing is a valid defence when dealing with copyright infringement for the purpose of non-commercial research or private study."

Section 29 as reported states:

> "Fair dealing with a work for the purposes of research for a non-commercial purpose does not infringe any copyright in the work provided that it is accompanied by a sufficient acknowledgement."

[S5, secondary source, fetch 2026-04-11]

The statute explicitly conditions the research exception on "non-commercial purpose." S5 also reports:

> "Private study being defined by Section 178 as excluding any study directly or indirectly for commercial purpose; it therefore covers most academic purposes, but not things such as the use of a database in market-testing of new drugs."

This means CDPA's private study exception also excludes indirect commercial purposes — the test is not only direct profit-seeking.

The case The Controller of Her Majesty's Stationery Office, Ordnance Survey v Green Amps Ltd is cited in S5 for the proposition that non-academic research must not "be used for a commercial purpose in the future" (forward-looking test). [OPUS-FOLLOWUP: This case citation is from a secondary Wikipedia source. Verify case citation and verbatim holding before relying on it in any production decision.]

### How UK fair dealing differs from US fair use on commercial question

Per S5:

> "This can be contrasted with the United States doctrine of fair use, which provides a general defence rather than rigid and specific categories of acceptable behaviour."

UK fair dealing is categorical: a use must fall within a specific enumerated category (research for non-commercial purposes; private study; criticism/review; news reporting; illustration for instruction; etc.). There is no general fair use balancing test. The commercial/non-commercial question in the UK arises as a threshold gatekeeping condition for the research and study categories — not as a mere factor to weigh. [OPUS-FOLLOWUP: whether a fan quiz game could invoke any UK fair dealing category at all — even research/private study — is a separate antecedent question that this lane has not resolved. UK fair dealing categories for fan works are narrow; "entertainment" is not an enumerated category.]

### UK doctrine: tentative observation

UK fair dealing appears to use a stricter threshold for "non-commercial" than US fair use — the condition is categorical, not merely one factor. A cost-recovery donation model might still satisfy "non-commercial" under UK law if it does not produce profit and the use does not have a "future commercial purpose." However, prix-guesser as a fan game would have difficulty establishing that it falls within any CDPA fair dealing category in the first place; the non-commercial condition is secondary to the question of category eligibility. [OPUS-FOLLOWUP: The primary UK legal question for prix-guesser is not "is cost-recovery commercial?" but "which CDPA fair dealing category, if any, applies to a fan quiz game?" This lane has not answered that antecedent question.]

---

## Section 4 — Canadian Copyright Doctrine

### Section 29 — Fair Dealing (general)

The verbatim text of section 29 of the Canadian Copyright Act [S6]:

> "Fair dealing for the purpose of research, private study, education, parody or satire does not infringe copyright."

Canadian fair dealing includes "education" as a standalone category since the 2012 Copyright Modernization Act amendments. Unlike UK law, "non-commercial" is not an explicit condition of the general research/private study/education fair dealing categories under §29. [OPUS-FOLLOWUP: while "non-commercial" is not stated in §29 itself, Canadian courts apply a multi-factor analysis (CCH Canadian Ltd. v. Law Society of Upper Canada, 2004 SCC 13) that considers the purpose of the dealing. Whether "education" in §29 extends to a party game is not text-resolved.]

### Section 29.21 — Non-commercial User-generated Content

This is the most directly relevant Canadian provision. The verbatim text of section 29.21(1), as fetched from Justice Laws [S7]:

**29.21(1)** It is not an infringement for an individual to use an existing published work to create a new work if:

> **(a)** "the use of, or the authorization to disseminate, the new work or other subject-matter is done **solely for non-commercial purposes**"
>
> **(b)** "the source — and, if given in the source, the name of the author, performer, maker or broadcaster — of the existing work or other subject-matter or copy of it are mentioned, if it is reasonable in the circumstances to do so"
>
> **(c)** "the individual had reasonable grounds to believe that the existing work or other subject-matter or copy of it, as the case may be, was not infringing copyright"
>
> **(d)** "the use of, or the authorization to disseminate, the new work or other subject-matter does not have a **substantial adverse effect, financial or otherwise, on the exploitation or potential exploitation** of the existing work or other subject-matter — or copy of it — or on an existing or potential market for it"

[S7, Justice Laws, fetch 2026-04-11]

**Condition (a): "solely for non-commercial purposes"**

The statute says "solely." This is a stricter word than merely "not primarily commercial." The SFU Library guide [S14] explains: "This means you can't use this provision to create advertising or sell something."

**Significance of "solely":** If a prix-guesser donation model produced any revenue beyond cost recovery — or if the donation mechanism is considered a commercial benefit — the "solely" standard could be difficult to satisfy. [OPUS-FOLLOWUP: Whether a project that accepts Patreon/Ko-fi donations with the stated purpose of covering server costs is acting "solely for non-commercial purposes" under §29.21(1)(a) is not settled by the statute or by any case found in this research. The word "solely" creates a high threshold. Opus or counsel should assess whether cost-recovery donations are consistent with "solely non-commercial" or whether any monetary exchange defeats the standard.]

**Condition (d): no substantial adverse effect on exploitation**

The statute also requires that the new work not have "a substantial adverse effect, financial or otherwise, on the exploitation or potential exploitation of the existing work." This condition is independent of the commercial-use condition. A fan quiz game using F1 circuit images that substitutes for an official F1 quiz product could fail this condition even if the use is non-commercial. [OPUS-FOLLOWUP: whether an F1 official quiz product exists or is contemplated is a factual question; this lane has not investigated F1's official app/game product offerings.]

**Academic commentary on §29.21:** Mariam Awan (IPOsgoode, 2015) [S13] argues:

> "The distinction between amateur non-commercial use and professional commercial use is quite arbitrary and cannot sustain itself in modern technological practices."

Awan proposes that §29.21's non-commercial requirement is analytically weak, and that focus should shift to "originality of the UGC and its effect on the source material." This is a reform argument, not current law.

### Canadian doctrine: tentative synthesis

Under Canadian copyright law, two routes are potentially relevant:

1. **§29 fair dealing for education:** "Non-commercial" is not an explicit statutory condition, but purposive analysis under CCH applies. A fan quiz game invoking "education" as its purpose would need to establish a genuine educational purpose — not entertainment. [OPUS-FOLLOWUP: CCH factors for fair dealing assessment under Canadian law include: purpose, character, amount, alternatives available, nature of the work, and effect on the market. This six-factor analysis has not been applied to the prix-guesser fact pattern in this research.]

2. **§29.21 non-commercial UGC:** The "solely for non-commercial purposes" condition is a strict threshold. Cost-recovery donations that produce any monetary flow create a question about whether the use is "solely" non-commercial. The statute provides no definition of "non-commercial" for this purpose.

**The most relevant Canadian doctrinal uncertainty:** Whether accepting donations that precisely cover costs (no profit) constitutes "non-commercial purposes" under §29.21(1)(a). No case located in this research addresses this directly.

---

## Section 5 — Legal Commentary on Donation-Funded Fan Projects

### Creative Commons "Defining Noncommercial" study (2009)

The CC "Defining Noncommercial" report [S8, S9] defined "noncommercial" in CC licenses as:

> "in any manner that is **primarily intended for or directed toward commercial advantage or private monetary compensation**."

[S9, CC wiki, fetch 2026-04-11]

The study empirically tested specific use cases. One finding is particularly relevant to cost recovery:

> "[A] not-for-profit organization uses work on its site, organization makes enough money from ads to cover hosting costs" received ratings of 59.2 and 71.7 [on a noncommercial scale].

[S8, CC "Defining Noncommercial" blog post, fetch 2026-04-11]

**Significance:** The CC study — the most rigorous empirical examination of what "non-commercial" means to actual creators and users — found that even simple cost-recovery-from-ads scenarios produced ambiguous results (mid-range ratings, indicating no consensus). Pure donation-based cost recovery without advertising is not the same scenario, but the finding signals that "cost recovery" is a gray zone, not a settled non-commercial case. The CC definition's use of "primarily intended for" leaves room for cost-recovery models to be non-commercial if the primary purpose is not monetary gain.

**Important caveat:** The CC "NonCommercial" definition is specific to CC licenses, not to US, UK, or Canadian statutory fair use/dealing analysis. These are different legal regimes. The CC definition is nonetheless useful as a widely-adopted industry standard for what "non-commercial" means in contractual/policy contexts — including, potentially, how F1 might construe its own use of "non-commercial." [OPUS-FOLLOWUP: F1's guidelines are a private policy, not a statute. F1 could in principle adopt the CC definition or a narrower or broader reading. No F1 interpretive guidance exists on this point.]

### Organization for Transformative Works (OTW) on donations

The OTW article [S10] (Retired Personnel, March 2018) stated:

> "Although some fanworks are sold, most fanwork creators want to share their creative work without thinking about commercial gain. Commercialized fanworks may still qualify as fair use — commerciality is only one of the factors that courts consider…"

The article notes that for Canada specifically:

> "In Canada, for example, those categories include parody and satire. They also include criticism, review, and news reporting if the maker attributes their sources. And they include **non-commercial user-generated content** if the maker attributes their sources and the new work does not act as a market substitute for the underlying work."

[S10, OTW, fetch 2026-04-11]

The OTW article does not address whether accepting donations (rather than selling) affects the commercial analysis.

### Fordham IPLJ — Commercial Fan Art (Rachel Morgan, 2021)

The abstract of [S12] (Fordham Intellectual Property, Media and Entertainment Law Journal, Vol. 31, No. 2) states:

> "fans of Japanese anime and manga have made a living selling artwork of their favorite characters at anime conventions… Despite the prevalence of this practice, there is a glaring legal issue: these fictional characters are the intellectual property of the authors who created them, and fan art is blatant copyright infringement. However, there are still many economic advantages to permitting the sale of fan art. This Note will propose a way to apply the fair use defense to commercial fan art in a way that protects the economic interests of both authors and fans."

[S12, Morgan 2021, abstract only, fetch 2026-04-11]

**Note:** The article addresses *selling* fan art, not cost-recovery donations. It is relevant as evidence that legal academia has engaged with the commerciality question for fan works, but full text was not accessible to extract donation-specific analysis.

### No direct case law found

No reported case was found in this research involving an IP holder challenging a fan project specifically on the basis that it accepted cost-recovery donations. The absence of such a case is a negative finding, not a positive confirmation that donations are legally safe. [OPUS-FOLLOWUP: The absence of reported case law on donation-funded fan project challenges could reflect: (a) the scenario being genuinely novel; (b) IP holders settling or sending C&D letters instead of litigating; (c) search limitations of a Sonnet-tier research lane. Opus or a lawyer should attempt a more targeted case law search before treating this as confirmed.]

---

## Section 6 — Synthesis: Does Cost-Recovery Donation Cross the Commercial Threshold?

### Analytical frame

The question has three layers:
1. Does a cost-recovery donation model constitute "commercial use" in F1's own policy text?
2. Does it constitute "commercial" in the fair use/dealing analysis that would govern an IP infringement claim?
3. Do these two questions have the same answer?

Answer to (3) is almost certainly **no** — the definitions are independent and may diverge. See Section 7 on trademark vs. copyright distinctions.

### F1 policy: tentative reading

F1's "Commercial use" subsection restricts "goods/services provided for sale." A donation button is not selling a good or service. F1's Fans definition identifies three commercial behaviors, none of which describes a passive donation mechanism. The carveout requires "non-commercial," but F1 never defines "non-commercial."

**Tentative reading (F1 policy):** A pure cost-recovery donation model (no advertising, no merchandise, no tiered Patreon with deliverables) appears to fall outside F1's three stated examples of "materially commercial manner" and outside F1's "Commercial use" subsection's goods-for-sale prohibition. However:
- F1 retains discretion ("subject to our discretion")
- F1 has not published interpretive guidance on donations
- This reading is based on negative inference (donations don't fit the stated examples), not a positive statement that donations are acceptable

[OPUS-FOLLOWUP: F1 policy reading is inference, not text. F1 could characterize any monetization — even minimal donations — as "materially commercial" under its discretion reservation. The absence of donations from F1's commercial examples is suggestive but not dispositive.]

### US copyright: tentative reading

The Harper & Row "profit from exploitation" test asks whether the user "stands to profit from exploitation of the copyrighted material without paying the customary price." Cost-recovery donations do not produce profit. The connection between the donation and the F1 content is indirect — users donate to support server costs, not to receive F1 content. Campbell confirms commercial nature is "only one element" even if present.

**Tentative reading (US copyright):** Cost-recovery donations probably do not constitute "commercial" use in the Harper & Row sense — there is no profit from exploitation. Even if characterized as technically commercial, Campbell makes this non-determinative under §107(1). However, factors (2)–(4) still apply and are not assessed in this lane.

[OPUS-FOLLOWUP: applying Harper & Row and Campbell to a cost-recovery donation model is doctrinal inference; no case applies these holdings directly to a fan project donation scenario. US doctrine assessment is tentative.]

### UK copyright: tentative reading

UK fair dealing is categorical. The more pressing question is whether prix-guesser falls within any CDPA fair dealing category (research, private study, criticism, news reporting). These categories are narrow and a fan quiz game is unlikely to fit cleanly. The "non-commercial" condition in the research/study exception is a threshold gatekeeping requirement — but the project must first establish category eligibility.

**Tentative reading (UK copyright):** The "non-commercial" condition would likely be satisfied by a cost-recovery donation model if "non-commercial" means "not directed toward commercial advantage or profit" (following the CC definition, which is the closest available industry standard). But UK fair dealing may be largely unavailable to prix-guesser on categorical grounds prior to the commercial question even arising.

[OPUS-FOLLOWUP: UK fair dealing categorical eligibility for a fan quiz game has not been researched by this lane; this observation is preliminary and requires separate analysis.]

### Canadian copyright: tentative reading (most contextually relevant — project owner is Canadian)

The two relevant paths diverge on the "non-commercial" question:

- **§29 (fair dealing for education):** "Non-commercial" is not an explicit condition. A genuine educational purpose could support the dealing; an entertainment-primary purpose is weaker. The six-factor CCH analysis applies.

- **§29.21 (non-commercial UGC):** The "solely for non-commercial purposes" standard is strict. Cost-recovery donations that produce any monetary inflow create uncertainty about whether the use is "solely" non-commercial. The statute says "solely," not "primarily."

**Tentative reading (Canadian):** If prix-guesser proceeds under §29.21, accepting donations — even cost-recovery donations — creates doctrinal risk because of the "solely" language. The project would need to argue that cost recovery (zero profit) still qualifies as "solely non-commercial." This argument is plausible but not settled. If the project accumulates a surplus beyond costs, it likely fails the "solely non-commercial" test. Under §29, educational purpose is available but requires genuinely educational framing, not entertainment.

[OPUS-FOLLOWUP: the "solely non-commercial" threshold under §29.21(1)(a) applied to cost-recovery donations is the single most important unresolved doctrinal question for a Canadian project owner. This should be the top Opus or counsel research priority. No Canadian case found addressing this scenario.]

---

## Section 7 — Trademark "Commercial Use" vs. Copyright "Commercial Use"

These are different doctrines and the distinction matters.

### Copyright "commercial use" (US §107)

As discussed above, copyright's commercial factor (§107(1)) is a sliding-scale factor in a four-factor balancing test. It asks about "the purpose and character of the use, including whether such use is of a commercial nature." Harper & Row's "profit from exploitation" test and Campbell's "one element" framing both apply. Even a commercial use can be fair use if sufficiently transformative or if the other factors weigh in favor.

### Trademark "commercial use" (Lanham Act / Canadian Trade-marks Act)

Trademark law's "commercial use" doctrine operates differently. The Lanham Act requires "use in commerce" as a threshold for trademark infringement claims. This means using a mark "in connection with the sale, offering for sale, distribution, or advertising of any goods or services" (15 U.S.C. §1114). The inquiry focuses on whether there is likelihood of consumer confusion about source or sponsorship in commercial trade.

Per the INTA fact sheet [S, search result 2026-04-11]:

> "Nominative use applies even if the nominative use is commercial. This means commercial activity doesn't automatically prevent fair use in trademark law."

**Key distinction:** Trademark's "commercial use" threshold is about whether the mark is used in connection with goods/services in the marketplace — it is about source identification and consumer confusion in trade, not about profit motive. A fan project that charges for access or accepts donations might use F1 marks in a way that creates consumer confusion regardless of whether the project profits.

By contrast, copyright's commercial factor is about profit and economic exploitation of the copyrighted content itself.

**Implication for prix-guesser donation model:**
- Under **copyright**: cost-recovery donations likely do not constitute "commercial" use because no profit from exploitation
- Under **trademark**: the question is whether using F1 marks (circuit names, driver names, Grand Prix titles) in connection with a service that accepts payment (even donations) creates likelihood of consumer confusion about F1's endorsement — which is a separate analysis from profit-seeking

[OPUS-FOLLOWUP: Trademark "use in commerce" analysis for prix-guesser accepting donations is not resolved by this research. The question of whether a donation-accepting fan project "uses" F1 marks "in commerce" under the Lanham Act or Canadian Trade-marks Act requires separate analysis. This lane's scope did not include trademark "commercial use" in depth.]

**Secondary question: solicited vs. unsolicited donations**

The task spec asked whether there is a distinction between soliciting donations and receiving unsolicited donations. No case or statutory authority found in this research draws this distinction for copyright or trademark purposes. However, solicitation creates an active nexus between the F1 content and the monetary flow — the project is actively leveraging the F1 content to request money. This strengthens the argument that the use is "for" commercial advantage (even if cost-recovery only). Unsolicited donations eliminate that nexus. [OPUS-FOLLOWUP: the solicited/unsolicited distinction may be analytically relevant under both copyright and trademark frameworks but no authority found. This requires Opus or counsel assessment.]

**Secondary question: donations exceeding server costs**

If donations exceed server costs (profit above break-even), the Harper & Row "profit from exploitation" test is more clearly triggered under US law, and the §29.21 "solely non-commercial" standard under Canadian law would be harder to satisfy. Any surplus profit also makes F1's "materially commercial manner" examples more applicable — the project would be generating economic benefit from F1 content beyond cost recovery.

[OPUS-FOLLOWUP: At what level of surplus donation revenue does the analysis shift from "non-commercial" to "commercial"? No authority found. This is an unresolved doctrinal question across all three jurisdictions examined.]

---

## What I Did NOT Check

1. **UK case law on "commercial purpose"** — no specific UK cases on fan project donation models were found or retrieved. The Green Amps case cited in S5 addresses research; no fan-project UK cases examined.
2. **Specific Canadian case law** — the CCH case (2004 SCC 13) on fair dealing factors was not fetched; only its framework was referenced. No Canadian case on donation-funded fan projects was found or examined.
3. **EU law** — the EU Copyright Directive (DSM Directive 2019/790) provisions on user-generated content and parody exceptions were not examined. Not applicable if the project is hosted in Canada/US, but potentially relevant for EU user access.
4. **F1's enforcement history** — whether F1 has pursued action against donation-funded fan projects is not addressed. Enforcement history is a practical (not doctrinal) consideration and was out of scope for this lane.
5. **Australian, New Zealand, and other Commonwealth fair dealing** — not addressed.
6. **Platform-specific policies** — Patreon's copyright policy and Ko-fi's copyright guidelines were identified in search but not fetched in depth for this analysis.
7. **DMCA safe harbor** — whether a donation-accepting fan project changes DMCA safe harbor analysis for the platform host was not examined.
8. **Tax characterization of donations** — whether Canada Revenue Agency treats fan project donations as "income" affects the "non-commercial" characterization in broader policy contexts but was explicitly out of scope per task spec.
9. **Specific F1 trademark registrations** — which specific marks are registered and in which classes was not examined.
10. **US Lanham Act "use in commerce" threshold** — not examined in depth; only surfaced as a doctrinal distinction.

---

## Flagged for Opus Follow-up

**[OF-1]** F1's "non-commercial" condition in the carveout (Passage F1-B) is undefined in F1's text. Opus should assess whether F1's three stated examples of "materially commercial manner" are intended as exhaustive or merely illustrative, and whether a donation model falls outside all three. Priority: HIGH for F1 policy analysis.

**[OF-2]** Harper & Row "profit from exploitation" test applied to cost-recovery donation models — this is doctrinal inference, no case found directly on point. Opus should search for any post-Harper & Row cases addressing the commerciality of cost-recovery models. Priority: MEDIUM.

**[OF-3]** Canadian §29.21 "solely for non-commercial purposes" + cost-recovery donations — the word "solely" creates a higher standard than US or F1 policy. No Canadian case found. This is the highest-priority unresolved doctrinal question for a Canadian project owner. Priority: HIGH.

**[OF-4]** UK CDPA fair dealing categorical eligibility — whether a fan quiz game fits any UK fair dealing category prior to the commercial question. This lane did not resolve this. Priority: HIGH for UK analysis.

**[OF-5]** UK statute text (CDPA 1988 §29 and §29A) — direct fetch returned empty; statute text derived from secondary sources only. Should be verified against legislation.gov.uk. Priority: MEDIUM (procedural).

**[OF-6]** Trademark "use in commerce" analysis — whether a donation-accepting project using F1 marks triggers trademark "commercial use" doctrine separately from copyright. Priority: MEDIUM.

**[OF-7]** Solicited vs. unsolicited donations — no doctrinal authority found for this distinction. May be analytically relevant. Priority: LOW unless the project owner is specifically considering passive (tip jar) vs. active (campaign) donation models.

**[OF-8]** Surplus-over-costs threshold — when does profit above cost-recovery shift the commercial analysis? No authority found. Priority: MEDIUM (for future planning).

**[OF-9]** F1 discretion reservation — F1's "subject to our discretion" language means any textual analysis is advisory; F1 could re-characterize donation-funded projects. Opus should assess whether F1's discretion language has any practical content or limiting principle. Priority: MEDIUM.

**[OF-10]** CC "Defining Noncommercial" study data applied to F1 policy — the CC study found ambiguity on cost-recovery scenarios. Whether F1's policy follows a CC-adjacent definition or a different standard is unresolved. Priority: LOW (contextual).

---

## Qualifications

1. **This is not legal advice.** This document contains empirical observations about legal doctrine and textual analysis of F1's guidelines. No sentences herein constitute legal advice or predict the outcome of any enforcement action or litigation.

2. **Jurisdiction scope:** This research covers US, UK, and Canadian doctrines. The project owner is Canadian; Canadian doctrine is most directly applicable. US and UK doctrines are relevant because (a) F1 operates under UK law (its guidelines reference UK fair dealing), (b) many users may be in US/UK jurisdictions, and (c) F1's rights enforcement may be under UK or US law depending on the forum.

3. **Source type hierarchy:** Statute (binding primary authority in jurisdiction) > Case law (binding or persuasive precedent) > Policy (F1's guidelines are private policy, not law) > Commentary (secondary non-binding analysis). This research found no directly on-point case law and significant commentary gaps.

4. **Model limitations:** This lane ran on Claude Sonnet 4.6. Legal research on nuanced doctrinal questions at this model tier should be treated as "broad strokes" orientation. Factual claims about case holdings are derived from secondary sources and summaries; verbatim quotes from cases should be verified against primary reporters before being cited in any production context.

5. **Date:** All fetches are as of 2026-04-11. F1's guidelines, the Canadian Copyright Act, CDPA, and case law could all change. F1's guidelines page has no last-modified date visible in fetched content, but B7 noted the page references a 2026 calendar suggesting current status.

6. **Tentative reading summary (all caveats above apply):**
   - **F1 policy:** cost-recovery donations appear to fall outside F1's stated "materially commercial" examples and the "Commercial use" subsection's goods-for-sale language; but F1 retains discretion and provides no positive statement that donations are acceptable.
   - **US copyright §107(1):** cost-recovery donations likely do not constitute "commercial nature" under the Harper & Row profit-from-exploitation test; even if they did, Campbell makes commerciality non-determinative.
   - **UK CDPA fair dealing:** cost-recovery donations likely do not constitute "commercial purpose" in the research/study exception; but categorical eligibility of a fan game under any UK fair dealing head is the more pressing prior question.
   - **Canadian §29.21:** the "solely for non-commercial purposes" condition creates the highest doctrinal risk — cost-recovery donations may not satisfy "solely non-commercial" depending on how Canadian courts read the word "solely." This is the most significant unresolved question for the project owner.
