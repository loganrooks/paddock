---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-5
model: claude-sonnet-4-6
question_focus: nominative-fair-use-and-implicit-branding
auditor_type: general-purpose-agent
tools_used: [WebSearch, WebFetch, Read]
fetch_date: 2026-04-11
output_file: 05-nominative-fair-use.md
predecessor_lanes:
  - wave-2-lane-b7-f1-legal-ambiguity.md (B7 circuit-IP anchor)
qualifications: "Doctrinal research only. US law primary; UK/EU/Canada secondary. Not a legal opinion. Flag OPUS-FOLLOWUP heavily."
---

# B8-5 — Nominative Fair Use and Implicit Branding

**Model:** Claude Sonnet 4.6 (general-purpose agent, WebSearch + WebFetch).
**Scope:** Whether unbranded F1-themed content — no F1 wordmark, no F1 logo, just factual references to circuits, drivers, races, venues — changes the trademark analysis compared to explicitly F1-branded content.
**Classification:** Doctrinal research producing "vague understanding" for Opus refinement. All interpretation-heavy claims flagged.

---

## Sources Table

| ID | URL | Fetched | Type | Description |
|----|-----|---------|------|-------------|
| S1 | https://cyber.harvard.edu/metaschool/fisher/domain/tmcases/newkids.htm | 2026-04-11 | Case | *New Kids on the Block v. News America Publishing*, 971 F.2d 302 (9th Cir. 1992) — full text via Harvard metaschool |
| S2 | https://openjurist.org/971/f2d/302/ | 2026-04-11 | Case | *New Kids* — OpenJurist text for cross-verification |
| S3 | https://law.justia.com/cases/federal/appellate-courts/F3/279/796/506072/ | 2026-04-11 | Case | *Playboy Enterprises, Inc. v. Welles*, 279 F.3d 796 (9th Cir. 2002) |
| S4 | https://www.courtlistener.com/opinion/150282/toyota-motor-sales-usa-inc-v-tabari/ | 2026-04-11 | Case | *Toyota Motor Sales, U.S.A., Inc. v. Tabari*, 610 F.3d 1171 (9th Cir. 2010) |
| S5 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62000CJ0002 | 2026-04-11 | Case | *Hölterhoff v. Freiesleben*, C-2/00 (CJEU, 14 May 2002) — referential use |
| S6 | https://en.wikipedia.org/wiki/Arsenal_Football_Club_v_Reed | 2026-04-11 | Case (secondary) | *Arsenal Football Club v. Reed* [2003] EWCA Civ 696 — badge-of-support vs. source indicator |
| S7 | https://www.law.cornell.edu/uscode/text/15/1115 | 2026-04-11 | Statute | 15 U.S.C. § 1115(b)(4) — Lanham Act statutory (classic) fair use defense |
| S8 | https://www.legislation.gov.uk/ukpga/1994/26/section/11 | 2026-04-11 | Statute | UK Trade Marks Act 1994, s.11 — limits on effect of registered trade mark |
| S9 | https://eur-lex.europa.eu/eli/dir/2015/2436/oj/eng | 2026-04-11 | Statute | EU Directive 2015/2436, Art. 14 — limitation of effects of trade mark |
| S10 | https://laws-lois.justice.gc.ca/eng/acts/t-13/section-22.html | 2026-04-11 | Statute | Canada Trademarks Act, ss. 20, 22 — infringement and goodwill depreciation |
| S11 | https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt | 2026-04-11 | Policy | F1 trademark guidelines — circuit IP redirect passage (B7 anchor), verified by direct WebFetch |
| S12 | https://en.wikipedia.org/wiki/British_Racing_Drivers%27_Club | 2026-04-11 | Commentary | BRDC/Silverstone ownership structure |
| S13 | https://en.wikipedia.org/wiki/Honda_Mobilityland | 2026-04-11 | Commentary | Honda Mobilityland/Suzuka ownership structure |
| S14 | https://www.monzanet.it/en/who-we-are/ | 2026-04-11 | Policy | SIAS/ACI Monza ownership and trademark regulations reference |
| S15 | https://web.law.duke.edu/cspd/casebook/ch08/ | 2026-04-11 | Commentary | Duke Law IP Casebook ch.8 — fair use and nominative use doctrine |
| S16 | https://middlelabs.substack.com/p/drivers-as-ip-when-a-face-becomes | 2026-04-11 | Commentary | Drivers as IP — personality rights and trademark in F1 |
| S17 | https://www.avvo.com/legal-answers/are-driver-codes-ex-ham-ver-etc-from-formula-one-t-5305955.html | 2026-04-11 | Commentary | F1 driver code trademark status |

---

## 1. US Nominative Fair Use Doctrine

### 1.1 Statutory Foundation: Classic Fair Use Under the Lanham Act

The Lanham Act, 15 U.S.C. § 1115(b)(4), provides a statutory affirmative defense to trademark infringement (applicable to incontestable marks) where the use is:

> "a use, otherwise than as a mark, of the party's individual name in his own business, or of the individual name of anyone in privity with such party, or of a term or device which is descriptive of and used fairly and in good faith only to describe the goods or services of such party, or their geographic origin." [S7]

This is **classic** (or **descriptive**) fair use: the defendant uses the term to describe *their own* goods or services. The three elements are: (1) not used as a mark; (2) used fairly and in good faith; (3) used only to describe the defendant's own goods/services or their geographic origin. [S7]

**Critical limitation**: classic fair use does not cover nominative use — using the mark to refer to the *trademark owner's* products, not the defendant's. For that situation, the Ninth Circuit developed a separate judicial doctrine. [S15]

### 1.2 The Nominative Fair Use Doctrine: *New Kids on the Block v. News America Publishing*

*New Kids on the Block v. News America Publishing, Inc.*, 971 F.2d 302 (9th Cir. 1992) [S1, S2] is the foundational case. The *Los Angeles Times* and *USA Today* conducted polls asking readers to vote for their favorite New Kids on the Block band member. The band sued for trademark infringement.

The Ninth Circuit articulated the doctrine:

> "Such nominative use of a mark — where the only word reasonably available to describe a particular thing is pressed into service — lies outside the strictures of trademark law." [S1]

The court held:

> "But, where the defendant uses a trademark to describe the plaintiff's product, rather than its own, we hold that a commercial user is entitled to a nominative fair use defense provided he meets the following three requirements: First, the product or service in question must be one not readily identifiable without use of the trademark; second, only so much of the mark or marks may be used as is reasonably necessary to identify the product or service; and third, the user must do nothing that would, in conjunction with the mark, suggest sponsorship or endorsement by the trademark holder." [S1, S2]

**Factor 1 — Not readily identifiable without the mark.** The first factor asks whether there exists a practical alternative to using the mark. In *New Kids*, the band name was the only reasonable way to refer to the band. [S1]

**Factor 2 — Only as much of the mark as reasonably necessary.** The second factor limits the use to the minimum required for identification. In *New Kids*, using only the band name (not the logo or stylized graphic) satisfied this. [S1]

**Factor 3 — No suggestion of sponsorship or endorsement.** The third factor is typically the decisive one in borderline cases. The court recognized:

> "such use is fair because it does not imply sponsorship or endorsement by the trademark holder." [S1]

The court explained the conceptual underpinning:

> "A defendant's use of a trademark to describe the thing, rather than to identify its source, prevents any reasonable consumer perception of endorsement, even when the use occurs in commercial contexts." [S2]

### 1.3 Application of the Test: *Playboy Enterprises, Inc. v. Welles*, 279 F.3d 796 (9th Cir. 2002)

*Playboy Enterprises, Inc. v. Welles* [S3] applied the *New Kids* test to Terri Welles' use of Playboy trademarks ("Playmate of the Year 1981") on her personal website and in metatags. The Ninth Circuit held that the use was nominative fair use.

On Factor 1: "there is no other way that Ms. Welles can identify or describe herself and her services without venturing into absurd descriptive phrases." [S3, via S15]

On Factor 3: "Welles does nothing in conjunction with her use of the marks to suggest sponsorship or endorsement by PEI" and she included "a clear statement disclaiming any connection to PEI." [S15]

The court also ruled that Welles' use of "PMOY '81" as a repeated background watermark did **not** satisfy the test — "Playmate of the Year 1981" was adequate; the acronym form was not necessary for identification. This illustrates that Factor 2 is case-specific: more than minimally necessary fails. [S3, S15]

### 1.4 The *Toyota v. Tabari* Refinement: Burden Shifting

*Toyota Motor Sales, U.S.A., Inc. v. Tabari*, 610 F.3d 1171 (9th Cir. 2010) [S4] refined the doctrine in the domain-name context. Auto brokers operating buy-a-lexus.com and buyorleaselexus.com prevailed on nominative fair use. Key holdings:

- "The nominative fair use doctrine is a defense that gives individuals the right to use another's trademark to refer to the trademarked good itself. The Tabaris are using the term Lexus to describe their business of brokering Lexus automobiles; when they say Lexus, they mean Lexus. Such use of the trademark is a fair use, namely nominative fair use." [S4 via search]
- The court shifted the burden: Toyota bears the burden of showing use was *not* nominative fair use (overruling prior Ninth Circuit precedent that placed the burden on the defendant). [S4 via search]
- The Sleekcraft likelihood-of-confusion analysis does not apply where the defendant uses the mark to refer to the trademarked good itself. [S4 via search]

[OPUS-FOLLOWUP: *Tabari* is a domain-name / service-broker case. Its burden-shifting holding and Sleekcraft exclusion may or may not extend to game/quiz contexts. Needs circuit-level verification.]

### 1.5 The Identify-vs-Brand Distinction

The *New Kids* court and its progeny draw a structural distinction that is conceptually central to prix-guesser's question:

**Classic use**: defendant uses plaintiff's mark to describe defendant's *own* goods/services.
**Nominative use**: defendant uses plaintiff's mark to refer to *plaintiff's* goods/services.
**Trademark infringement**: defendant uses plaintiff's mark as a source identifier for *defendant's* goods/services — implying the defendant's product is associated with, endorsed by, or sponsored by the plaintiff.

As the Duke Law casebook states:

> "A defendant's use is classic fair use where a defendant has used the plaintiff's mark only to describe his own product, and not at all to describe the plaintiff's product. In contrast, a defendant's use of a plaintiff's mark is nominative where he or she used the plaintiff's mark to describe the plaintiff's product, even if the defendant's ultimate goal is to describe his or her own product." [S15]

The **critical dividing line** is: does the use of the mark signal that the plaintiff *is the source* of the defendant's product? If not — if it merely identifies the subject matter of the defendant's product — nominative fair use applies.

---

## 2. UK / EU / Canadian Equivalents

### 2.1 UK: Trade Marks Act 1994, Section 11

Section 11(2) of the UK Trade Marks Act 1994 provides that a registered trade mark is not infringed by:

> "(b) the use of indications concerning the kind, quality, quantity, intended purpose, value, geographical origin, the time of production of goods or of rendering of services, or other characteristics of goods or services; [and] (c) the use of the trade mark where it is necessary to indicate the intended purpose of a product or service (in particular, as accessories or spare parts), provided the use is in accordance with honest practices in industrial or commercial matters." [S8]

The statute adds:

> "Any use of a registered trade mark otherwise than in accordance with honest practices in industrial or commercial matters shall be treated as infringing the registered trade mark if the use without due cause takes unfair advantage of, or is detrimental to, the distinctive character or repute of the trade mark." [S8]

**The UK equivalent is not a three-factor test.** It is a single overriding standard: was the use "in accordance with honest practices in industrial or commercial matters"? This standard derives from EU Directive 89/104 (now 2015/2436) and is interpreted at EU/CJEU level.

[OPUS-FOLLOWUP: The UK post-Brexit implementation of this test — whether UK courts are now free to diverge from CJEU precedent on "honest practices" — is an open question not researched here.]

### 2.2 EU: Directive 2015/2436, Article 14

Article 14 of EU Directive 2015/2436 provides the EU-wide limitation on trademark effects:

> **Article 14(1):** "A trade mark shall not entitle the proprietor to prohibit a third party from using, in the course of trade: (a) the name or address of the third party, where that third party is a natural person; (b) signs or indications which are not distinctive or which concern the kind, quality, quantity, intended purpose, value, geographical origin, the time of production of goods or of rendering of services, or other characteristics of goods or services; (c) the trade mark for the purpose of identifying or referring to goods or services as those of the proprietor of that trade mark, in particular, where the use of the trade mark is necessary to indicate the intended purpose of a product or service, in particular as accessories or spare parts." [S9]

> **Article 14(2):** "Paragraph 1 shall only apply where the use made by the third party is in accordance with honest practices in industrial or commercial matters." [S9]

Article 14(1)(c) is the EU's closest analogue to US nominative fair use: it permits using the mark to refer to the proprietor's own goods or services. The honest-practices gate applies universally.

**CJEU on referential use**: In *Hölterhoff v. Freiesleben*, C-2/00 (14 May 2002) [S5], the CJEU held that when a trademark is used solely to describe product characteristics in commercial negotiations — not to indicate trade origin — that use does not implicate the trademark proprietor's exclusive rights. The CJEU's "function theory" tests whether the use affects the trademark's essential function of guaranteeing origin. [S5 via search]

**CJEU on confusion**: In *Arsenal Football Club v. Reed* [S6], the ECJ held that where use "jeopardizes the guarantee of origin" it constitutes infringement, even if consumers perceive the mark as a badge of support rather than a source indicator. This limits the availability of the honest-practices defense for uses that confuse about origin even when not used as a traditional brand. [S6]

**EU honest-practices standard** — key considerations courts examine (from *O2 Holdings v. Hutchison 3G*, C-533/06):
- Is the mark used in a way that would be perceived as indicating a commercial connection to the trademark owner?
- Is the use necessary?
- Does it imply endorsement, sponsorship, or affiliation?

[OPUS-FOLLOWUP: The post-2015 CJEU case law on Article 14 "honest practices" is extensive and not fully surveyed here. The honest-practices gate is stricter than the US third factor and has generated substantial EU case law this lane did not cover.]

### 2.3 Canada: Trademarks Act, ss. 20 and 22

Canada's Trademarks Act does not contain an explicit statutory nominative fair use defense equivalent to the Lanham Act or EU Directive. The two principal provisions are:

**Section 20(1)** — infringement by confusion: unauthorized use is infringement when it involves a mark confusingly similar to the registered mark in association with goods or services. [S10 via search]

**Section 22(1)** — depreciation of goodwill:

> "No person shall use a trademark registered by another person in a manner that is likely to have the effect of depreciating the value of the goodwill attaching thereto." [S10]

**Permitted descriptive use**: The Act permits use, otherwise than as a trademark, of an accurate description of the character or quality of goods or services, or a geographical name of the place of business, provided such use does not depreciate goodwill. [S10 via search]

**Canadian position on nominative use**: Canadian courts recognize a form of nominative/referential use permissibility, derived from the principle that trademark law governs *source-indicating* uses. Where a term is used to describe the subject matter rather than claim origin, courts have generally found no infringement. However, Canada has not adopted the New Kids three-factor test explicitly, and case law is thinner than US. [OPUS-FOLLOWUP: Canadian case law on nominative use for fan/quiz content is not well-researched here; specific Canadian precedents needed.]

---

## 3. The Identify-vs-Brand Distinction: Application to Factual Quiz Content

### 3.1 The Structural Distinction

Trademark law's central prohibition is preventing consumer confusion about the *source* of goods or services. Two uses of a mark are conceptually distinct:

**Identifying use**: Using the mark to identify the trademark owner's product as the *subject matter* of your content — e.g., a quiz question asks "What is the name of this F1 circuit?" The mark (if used at all) identifies whose circuit is depicted, not who made the quiz. This is classic referential / nominative use territory.

**Branding use**: Using the mark to signal that the trademark owner *is the source of, sponsors, or endorses* your product — e.g., calling your quiz "The Official F1 Quiz" or using F1's logo on your product packaging. This is the infringement paradigm.

**The decisive question for prix-guesser**: Does a factual quiz about F1 circuits and venues, even without the F1 wordmark or logo, create consumer impression that F1 sponsors or endorses the quiz? The answer depends on presentation, context, and how closely the quiz's aesthetic mimics F1's official style. [OPUS-FOLLOWUP: this is a fact-pattern translation, not a decided case.]

### 3.2 The "Necessary to Identify" Principle

Under both US (Factor 1 of *New Kids*) and EU (Art. 14(1)(c) of Directive 2015/2436), a use is more defensible when the mark is *necessary* to identify the subject matter. For factual quiz content:

- Using "Silverstone" to identify the Silverstone circuit: necessary — no alternative name exists. Factor 1 is typically satisfied for circuit names.
- Using "F1" as a label for the quiz's subject matter (the sport itself): arguably necessary for editorial context, but this is the most contested step. [OPUS-FOLLOWUP: whether using "F1" in quiz prompt text is nominative or branding depends on context and placement — editorial vs. header vs. brand element.]

### 3.3 Implicit Branding Concern

The task question specifically asks whether dropping *explicit* F1 branding (wordmark, logo) while retaining factual F1 content changes the analysis. The answer is: **it changes the analysis but does not eliminate trademark exposure.**

Dropping explicit marks removes the clearest infringement vectors:
- No use of "F1™," "Formula 1™," or official logos eliminates per se infringement of those registered marks.
- F1's Games guideline prohibits using "Permitted Word Marks to brand any game" [S11]; dropping those marks directly addresses this rule.

What remains:
- **Trade dress / overall commercial impression**: If the quiz's visual style, color scheme, or presentation mimics F1's official aesthetic sufficiently to cause confusion about sponsorship, trade dress infringement may arise even without explicit mark use. [OPUS-FOLLOWUP: prix-guesser's actual visual design is not reviewed here.]
- **Implied association**: "Ambush marketing" doctrine (primarily in event-advertising context, not quiz games) recognizes that creating an overall impression of association with a brand without explicit mark use can still be actionable. This is more relevant to commercial advertising campaigns than to a private fan quiz. [OPUS-FOLLOWUP: whether ambush marketing doctrine applies to private non-commercial fan content is not established — this would need jurisdiction-specific research.]
- **Circuit names**: If a circuit name is itself a registered trademark (e.g., "Silverstone" by BRDC/Silverstone Circuits Ltd.), using it in a quiz context to identify the circuit is squarely nominative/referential use. The question becomes: does the use imply that BRDC endorses or sponsors the quiz? Almost certainly not for simple factual identification. [OPUS-FOLLOWUP: applying this analysis to each specific circuit requires trademark register searches per jurisdiction.]

**Net reading**: Dropping explicit F1 marks meaningfully reduces trademark exposure for F1's own registered marks. It does not eliminate: (a) circuit operators' trademark rights, (b) driver personality/publicity rights, (c) trade dress confusion if F1's official aesthetic is mimicked, or (d) copyright exposure for any F1-owned images or assets used. [OPUS-FOLLOWUP: the interplay of these remaining vectors needs per-element analysis.]

---

## 4. Circuit and Venue Name Ownership

### 4.1 B7 Anchor Finding — F1 Explicitly Disclaims Circuit IP

B7 (Opus) found and I directly verified via WebFetch against formula1.com/en/information/guidelines on 2026-04-11:

> "If you would like to enquire about licensing any of the circuits' intellectual property rights, such as circuit outlines, please contact the owner of the IP directly." [S11]

This passage appears in F1's own trademark guidelines. It is a direct disclaimer by F1 that circuit IP — specifically including circuit *outlines* — is not F1's to license. The rights belong to the circuit operators.

**Operational significance**: prix-guesser's core mechanic (recognizing circuits from visual cues) engages circuit-operator IP, not F1's IP, for the circuit-geography component. This is the most favorable single finding for the project's circuit-content side.

### 4.2 Individual Circuit Owners

| Circuit | Owner/Operator | IP-Holding Entity |
|---------|---------------|-------------------|
| Silverstone (UK) | British Racing Drivers' Club (BRDC) | Silverstone Circuits Limited (wholly-owned BRDC subsidiary) [S12] |
| Monza (Italy) | SIAS (Società Incremento Automobilismo e Sport), 90% ACI / 10% ACM | SIAS maintains its own trademark regulations [S14] |
| Suzuka (Japan) | Honda Mobilityland Corporation (Honda subsidiary) | Honda Mobilityland [S13] |
| Others | Varies | Circuit-by-circuit; each retains its own IP |

Each circuit is a separate rights holder. F1's guidelines redirect inquiries to these entities. Prix-guesser's legal relationship for circuit-content purposes is therefore with individual circuit operators rather than with F1. [OPUS-FOLLOWUP: this does not mean circuit operators have permissive IP postures — it means prix-guesser faces a different set of rights holders, not that the content is freely usable.]

### 4.3 Are Circuit Layouts Protected?

The general principle, as reflected in multiple IP forums and practitioner commentary [search results, not independently citable to case text]: **circuit layouts as functional designs are generally not protected by copyright** because copyright protects creative expression, not functional/utilitarian designs (roads, tracks). However:

- **Stylized representations** of circuit layouts (artistic circuit maps, branded outline graphics) may be protected as artworks. These belong to the circuit operator.
- **Circuit names** may be registered trademarks (e.g., "Silverstone," "Monza," "Suzuka") — each would need a trademark register search per jurisdiction to confirm.
- **F1's circuit representation**: F1's own "Official Artworks, Graphics, Assets and Textures" [S11] include any stylized circuit graphics F1 has created. These cannot be used in third-party games per F1's guidelines, even though the underlying circuit IP belongs to the circuit operator.

[OPUS-FOLLOWUP: whether "Silverstone" is in fact a registered trademark in the UK (and in what classes) is not confirmed here — trademark register search needed. Similarly for Monza, Suzuka, and other circuits.]

### 4.4 Practical Impact for Prix-Guesser

A quiz that shows a photograph of the Silverstone circuit and asks players to identify it is:
- Using content whose geographic/factual reference implicates BRDC's trademark in "Silverstone" (if registered in relevant classes).
- Using the identifying function of the name (referential/nominative use).
- Almost certainly **not** implying BRDC endorses or sponsors the quiz.

Under US nominative fair use doctrine, this should satisfy the three *New Kids* factors: (1) the circuit is not readily identifiable without its name; (2) only the name (not BRDC's logo) is used; (3) nothing suggests BRDC's sponsorship. Under EU Article 14(1)(c), referring to the circuit "as goods or services of the proprietor" to identify what is depicted is within scope. Whether the use meets the "honest practices" gate is a fact-pattern question. [OPUS-FOLLOWUP throughout.]

---

## 5. The "F1-Themed Without Saying F1" Pattern in IP Practice

### 5.1 Does This Pattern Have a Name?

Research found no single canonical term for this pattern. Related concepts in IP practice literature include:

- **"Ambush marketing"**: used in event-sponsorship context where advertisers imply association with an event without official sponsorship. This concept is primarily commercial/advertising-oriented and does not map cleanly onto a non-commercial fan quiz. [search]
- **"Tribute" or "homage" use**: fan fiction and fan art contexts where creators reference a property without using its marks. This pattern is familiar in fan-culture IP commentary but lacks a formal legal name.
- **"Theming"**: informal term for designing a product around the aesthetic or subject matter of another brand without using its registered marks. No formal legal doctrine by this name.
- **"Generic reference use"**: where the mark has become descriptive of a category. F1 has not become generic.
- **"Editorial use"**: news, commentary, criticism uses that reference trademarks without implying sponsorship. This is recognized in both US (First Amendment context) and EU (Art. 14(1)(b)).

**Assessment**: The "F1-themed without saying F1" pattern is not a named doctrine or recognized safe harbor. It reduces trademark exposure by eliminating use of specific registered marks, but it operates in the space governed by general nominative/referential use doctrine and trade dress law. [OPUS-FOLLOWUP: legal commentary on sports-themed fan content without explicit marks would be worth a targeted search in law review databases.]

### 5.2 What Dropping Explicit Marks Does and Does Not Do

**Does**:
- Eliminates direct infringement of F1's registered word marks (F1™, Formula 1™, Grand Prix™, etc.).
- Addresses F1's Games guideline rule that "Our Permitted Word Marks cannot be used to brand any game." [S11]
- Eliminates the clearest and most readily-identifiable infringement vector.

**Does not**:
- Eliminate referential use of circuit names (owned by circuit operators, not F1).
- Eliminate referential use of F1 factual content (race results, driver statistics) — which is governed by separate F1 guidelines provisions.
- Eliminate trade dress exposure if the overall visual presentation creates confusion with F1's official style.
- Eliminate driver name / personality rights exposure (separate analysis below).
- Eliminate copyright exposure for any F1-owned images, artworks, or audio-visual content used in the quiz.

### 5.3 The Trade Dress Risk That Remains

Even without explicit marks, courts in both the US and EU have recognized that *overall commercial impression* can create confusion. For a non-commercial private fan game:

- **US**: Trade dress protection requires the overall impression to be distinctive and create likely confusion as to source, sponsorship, or affiliation (15 U.S.C. § 1125(a)). For a private, clearly unofficial fan game, the confusion risk is substantially lower than for a commercial product. [OPUS-FOLLOWUP: the private, non-commercial, unofficial nature of prix-guesser is highly relevant here but is a fact-pattern application, not a decided rule.]
- **EU**: Article 14(2) "honest practices" gate would capture a use that creates an overall misleading impression of association. A clearly unofficial fan quiz with a disclaimer satisfies this gate more comfortably than a commercial product.

---

## 6. Driver Name Rights

### 6.1 Framework

Driver names sit at the intersection of two IP regimes:

**Personality/publicity rights**: In many jurisdictions, using a person's name commercially without consent is actionable. The US "right of publicity" varies by state; the UK has no unified right of publicity but tort law (passing off) may apply; EU has personality rights under civil law traditions.

**Trademark registration**: Some F1 drivers have registered their names as trademarks. Known examples: Lewis Hamilton (44IP Ltd) has registered "LH44" and "LEWIS HAMILTON" in multiple classes including sports gear and media. Max Verstappen has registered "Simply Lovely" and operates Max Verstappen BV for licensing. [S16]

### 6.2 What This Means for a Quiz Context

Using a driver's name in a quiz question — "Who drove for Red Bull in 2021?" or "Name this driver: [image]" — is:

- **Referential/nominative**: using the name to identify the person (not to endorse or imply association with the quiz).
- **Factual/historical**: race results and driver names are historical facts not owned by anyone.
- **Likely non-infringing** for names used purely as factual references in quiz content. [OPUS-FOLLOWUP: this is a doctrinal translation, not a decided case on quiz-game driver names.]

What would trigger liability:
- Using a driver's name/likeness to *imply endorsement* of the quiz (e.g., "Lewis Hamilton recommends Prix-Guesser").
- Using a driver's *registered trademark* (e.g., "LH44" logo) as decoration on the quiz interface.
- Commercially exploiting the driver's name in merchandise tied to the quiz.

For prix-guesser, the factual-reference use of driver names appears squarely within nominative/referential fair use under US doctrine and Article 14(1)(c) equivalent under EU. The non-commercial, private context strengthens this analysis. [OPUS-FOLLOWUP: apply per jurisdiction.]

### 6.3 Driver Code Trademarks

F1 three-letter driver codes (HAM, VER, NOR, etc.) are not clearly trademarked as independent marks per available commentary [S17]. They are widely used across the sports information ecosystem without apparent enforcement. However, no definitive trademark register search was conducted. [OPUS-FOLLOWUP: driver codes are a minor risk but worth a quick register search.]

---

## 7. Tentative Application to Prix-Guesser

**What the above doctrine suggests** — flagged throughout with OPUS-FOLLOWUP:

### Scenario: Prix-guesser drops F1 wordmark and logo; retains factual circuit/race/driver references

**US analysis** (most developed doctrine):
- Circuit names, venue names, driver names used to identify subject matter of quiz questions: plausibly nominative fair use under *New Kids*. Factor 1 (not readily identifiable without the name) satisfied for specific circuits/drivers. Factor 2 (only as necessary) satisfied if names are used in question/answer text, not as branding for the quiz itself. Factor 3 (no suggestion of sponsorship) — critical factor, depends on presentation. A clearly unofficial quiz with a disclaimer is the strongest posture. [OPUS-FOLLOWUP: F1 is not the primary rights holder for circuit names — circuit operators are — so the nominative fair use analysis runs against each circuit operator, not against F1, for the circuit-content component.]
- Dropping F1 wordmark eliminates the Games guideline's prohibition on "Permitted Word Marks branding any game" [S11].
- F1's Other IP Rights (official artworks, F1-owned still images, official graphics/textures, audio/AV content, written content, statistics/timing data) remain prohibited for use in third-party games regardless of wordmark dropping [S11].

**EU analysis** (Article 14(1)(c)):
- Using circuit names and driver names "for the purpose of identifying or referring to goods or services as those of the proprietor" [S9] fits Art. 14(1)(c) for identifying the circuit/driver as the subject.
- The "honest practices" gate (Art. 14(2)) requires that the use not create a misleading impression of association. A clearly unofficial, non-commercial private quiz satisfies this more comfortably than a commercial product.
- Arsenal v. Reed caution: the ECJ held that uses "jeopardizing the guarantee of origin" infringe regardless of consumer perception. If the quiz is presented as an official product, infringement risk rises. [OPUS-FOLLOWUP: this is the EU's stricter test compared to US.]

**UK analysis** (s.11 TMA 1994):
- Parallel to EU (pre-Brexit UK law tracked the EU Directive).
- The "honest practices" standard applies.
- Arsenal v. Reed [S6] originated in the UK court system; the UK approach is generally consistent with the EU framework, though post-Brexit divergence is possible. [OPUS-FOLLOWUP: post-Brexit UK trademark developments not researched.]

**Canada** (ss. 20, 22 Trademarks Act):
- No explicit nominative use safe harbor, but the underlying principle that non-trademark-source-indicating use is not infringement applies.
- The s.22 goodwill depreciation provision is broader; factual quiz references that do not depreciate goodwill (they arguably enhance it, being fan engagement) should not trigger it. [OPUS-FOLLOWUP: Canadian case law on fan use is very thin in this research; specific Canadian cases needed.]

### Key Distinction: Explicit vs. Implicit Branding

Dropping explicit F1 marks shifts the analysis from "per se prohibited branding use" to "nominative/referential use — examine the context." This is a **meaningful improvement** in the trademark analysis, but not a clean safe harbor. The residual questions are:

1. Does the overall presentation imply F1 sponsorship or endorsement? (Trade dress / honest practices concern)
2. Is the project using any F1-owned IP (images, graphics, audio) beyond the wordmark? (These restrictions survive wordmark dropping)
3. Does each circuit operator's name constitute a trademark use that requires separate nominative fair use analysis per circuit?
4. Are driver names used as mere factual identifiers (low risk) or as personality endorsements (higher risk)?

**Tentative reading**: Dropping F1 wordmark/logo improves the trademark posture meaningfully — it eliminates the per se branding prohibition and aligns the use more squarely with nominative/referential use doctrine. The remaining analysis turns on (a) F1's Other IP Rights (unchanged), (b) individual circuit operators' trademark rights (nominative use likely available), and (c) presentation (a clear unofficial disclaimer and avoidance of F1 official visual style materially strengthens the honest-practices analysis). Implicit branding through F1's official aesthetic colors, typeface, or visual style would reintroduce confusion risks even without the wordmark.

[OPUS-FOLLOWUP: every paragraph of this section translates doctrine to a specific fact pattern. All of this requires Opus-level doctrinal-to-fact verification and per-jurisdiction checking.]

---

## 8. What I Did NOT Check

1. **Trademark register searches**: Did not run searches in UKIPO, EUIPO, USPTO, or CIPO for "Silverstone," "Monza," "Suzuka," or individual circuit names. Whether these names are registered trademarks (and in which classes) is unverified.

2. **Post-Brexit UK trademark divergence**: UK courts' post-2021 departure from CJEU precedent on the honest-practices standard is not researched.

3. **Canadian case law**: Canada's specific case law on nominative use and fan projects is essentially unresearched here. The Chambers 2025 Canada chapter and Canadian court decisions on these points were not retrieved.

4. **Personality rights / right of publicity by state/country**: The US right of publicity varies substantially by state (California, New York, others). Not researched per-state.

5. **Passing off (UK/common law)**: UK passing off doctrine as a potential claim beyond registered trademark infringement is not analyzed. An unregistered passing off claim might arise even where registered trademark infringement is avoided.

6. **EU CJEU case law post-2015**: The body of CJEU cases applying Article 14 of Directive 2015/2436 after 2015 is extensive; this lane did not survey it.

7. **Driver collective agreements**: F1's commercial arrangement with the FIA and teams on driver image rights (mentioned in search results as covering F1 video games) is not analyzed.

8. **Ambush marketing doctrine per jurisdiction**: The specific doctrine and case law for "ambush marketing" in each jurisdiction is not researched; only a general flag was possible.

9. **Law review commentary on fan-use trademark**: No academic law review articles were retrieved and cited; the Duke casebook provided the only secondary source.

10. **SIAS (Monza) trademark regulations**: The SIAS trademark regulations document was found (PDF) but the Italian-language PDF was not readable via WebFetch.

---

## 9. Flagged for Opus Follow-Up

All OPUS-FOLLOWUP markers consolidated:

1. **Tabari burden-shifting extension**: Whether *Toyota v. Tabari*'s burden-shifting and Sleekcraft-exclusion holdings apply to a game/quiz context, not just a brokerage-domain context.

2. **Post-Brexit UK honest-practices test**: Whether UK courts have diverged from CJEU's Article 14 interpretation after 2021 and what the current UK standard is.

3. **EU honest-practices case law depth**: The extensive CJEU post-2015 case law on Article 14 "honest practices" was not covered; a targeted survey is needed.

4. **Per-circuit trademark register searches**: Whether "Silverstone," "Monza," "Suzuka," "Spa-Francorchamps," "Interlagos," etc. are registered trademarks and in which classes — each circuit is a separate analysis.

5. **Whether implicit-branding / trade dress analysis applies to private non-commercial fan content**: The trade dress confusion doctrine is primarily commercial; whether it applies to a clearly unofficial private fan quiz is a doctrinal extension that needs Opus-level review.

6. **Canadian case law on nominative use for fan/quiz content**: This lane found almost nothing; a targeted Canadian IP case search is needed.

7. **Driver names in quiz questions — per-jurisdiction application**: Each jurisdiction (US by state for publicity rights, UK for passing off, EU for civil law personality rights, Canada) needs separate analysis.

8. **Prix-guesser's actual visual design**: Whether the project's visual presentation mimics F1's official style (color, typeface, graphical elements) determines trade dress risk. This lane reviewed doctrine only; no design review was conducted.

9. **Arsenal v. Reed's scope**: Whether Arsenal's "guarantee of origin" test — which is stricter than US nominative fair use — applies to quiz content, or whether it is limited to merchandise/goods contexts where origin confusion is more direct.

10. **Dropping explicit marks vs. F1 Other IP Rights remaining**: A follow-up should explicitly map which content types remain restricted under F1's guidelines (Games / Apps / Section 2 prohibitions) even after wordmark dropping, so prix-guesser's content authoring rules can be derived from this.

---

## 10. Qualifications

1. **Not a legal opinion.** This document is doctrinal research for planning purposes. Nothing here constitutes legal advice.

2. **US-primary**: The nominative fair use doctrine is substantially more developed in the US (Ninth Circuit especially). UK, EU, and Canadian equivalents are covered at "vague understanding" level.

3. **Time snapshot**: Research conducted on 2026-04-11. All URLs fetched on that date. Court decisions, statutes, and F1's guidelines may change.

4. **Ninth Circuit doctrine**: US nominative fair use is a Ninth Circuit judicial doctrine. Other circuits (Second, Third, etc.) have approached nominative use differently. Prix-guesser's US exposure would depend on where any action is filed.

5. **F1 guidelines as policy, not law**: F1's guidelines [S11] are not statutes or court decisions. They express F1's own characterization of what it permits. General IP law operates independently, and the honest-practices / nominative fair use doctrines may permit more than F1's guidelines concede.

6. **The "private" context**: The private, non-commercial nature of prix-guesser is a significant factor under multiple analyses (F1's guidelines' educational carveout, trade dress confusion analysis, honest-practices gate). This lane's analysis assumes the project remains strictly private and non-commercial.

7. **Circuit IP disclaimer**: F1's statement that circuit IP belongs to circuit operators is self-serving in one direction (F1 is not the licensor) but does not by itself confirm that circuit names are freely usable — it redirects the question to each circuit operator.
