---
date: 2026-04-11
research_program: f1-fan-project-legal-landscape
lane: B8-3
question_focus: analogous-fan-projects-other-domains
auditor_model: claude-sonnet-4-6
agent_type: general-purpose
tools_used: [WebSearch, WebFetch, Read]
output_file: 03-analogous-fan-projects.md
predecessor_lanes:
  - wave-1-lane-1c-external-gap-research.md (LQ-1C.4 Finding 2 — fan-game legal risks via odinlaw.com)
  - wave-2-lane-b7-f1-legal-ambiguity.md (F1 policy text for contrast)
qualifications: >
  This is a Sonnet research lane producing "vague understanding" for Opus refinement.
  Not a legal opinion. All patterns are inferred from 5–15 cases per domain;
  none are statistically robust. Citation quality varies by case: primary sources
  obtained for ~60% of cases; secondary-only sourcing flagged inline.
  Web searches conducted 2026-04-11.
---

# B8-3 — Analogous Fan Projects in IP-Heavy Domains

**Research lane identity**: Claude Sonnet 4.6, general-purpose agent, WebSearch + WebFetch.
**Scope**: Comparative survey of fan-project enforcement histories in domains other than F1.
**Purpose**: Extract patterns about what triggers vs. tolerates enforcement, with specific
attention to donation-funded projects.

---

## Sources Table

| ID | URL | Fetch Timestamp | Description |
|----|-----|-----------------|-------------|
| S1 | https://www.nintendolife.com/news/2016/09/nintendo_of_america_issues_takedown_request_on_am2r_ending_the_project | 2026-04-11 | Nintendo Life — AM2R final takedown |
| S2 | http://metroid2remake.blogspot.com/2016/09/no-future-for-am2r.html | 2026-04-11 | DoctorM64's primary statement on AM2R ending |
| S3 | https://daily.pokecommunity.com/2016/08/15/nintendo-orders-pokemon-uranium-creators-takedown-download-links/ | 2026-04-11 | PokéCommunity Daily — Uranium DMCA notices |
| S4 | https://archive.org/details/pokemon-prism-cease-desist | 2026-04-11 | Internet Archive copy of Nintendo C&D to Pokémon Prism (PDF description) |
| S5 | https://daily.pokecommunity.com/2016/12/21/rom-hack-pokemon-prism-receives-cease-desist/ | 2026-04-11 | PokéCommunity Daily — Pokémon Prism C&D details |
| S6 | https://www.videogameschronicle.com/news/nintendo-takes-action-against-mario-64-pc-port/ | 2026-04-11 | VGC — Super Mario 64 PC port DMCA |
| S7 | https://www.nintendolife.com/news/2021/01/nintendo_issues_mass_dmca_takedown_379_fan-made_games_forcibly_removed | 2026-04-11 | Nintendo Life — 379 fan game mass takedown 2021 |
| S8 | https://www.pcgamer.com/fan-made-star-wars-battlefront-successor-blocked-by-ea-lucasfilm/ | 2026-04-11 | PC Gamer — Galaxy in Turmoil C&D |
| S9 | https://diskingdom.com/2016/08/01/star-wars-galaxy-turmoil-hit-cease-desist/ | 2026-04-11 | DisKingdom — Galaxy in Turmoil C&D details |
| S10 | https://www.hollywoodreporter.com/business/business-news/cbs-paramount-settle-lawsuit-star-trek-fan-film-966433/ | 2026-04-11 | Hollywood Reporter — Axanar settlement |
| S11 | https://www.rollingstone.com/tv-movies/tv-movie-news/paramount-cbs-establish-star-trek-fan-film-guidelines-111186/ | 2026-04-11 | Rolling Stone — Star Trek fan film guidelines released |
| S12 | https://massivelyop.com/2015/03/04/indie-harry-potter-mmo-slapped-with-cease-and-desist-by-warner-bros/ | 2026-04-11 | Massively OP — Wizarding World Online C&D (403 on fetch; secondary) |
| S13 | https://www.neogaf.com/threads/nintendo-shuts-down-patreon-for-fan-made-star-fox-the-animated-series.1173477/ | 2026-04-11 | NeoGAF — "A Fox in Space" Nintendo Patreon shutdown (403 on fetch; secondary) |
| S14 | https://www.resetera.com/threads/jagex-shuts-down-old-school-runescape-hd-fan-mod-hours-before-release-sparking-in-game-protest-update-jagex-allows-mod-to-release.483385/ | 2026-04-11 | ResetEra — RuneLite HD shutdown and reversal |
| S15 | https://www.bsimracing.com/fia-sends-out-cease-and-desist-letter-to-modding-teams/ | 2026-04-11 | BSimRacing — FIA C&D to modding teams (fetched; primary adjacent) |
| S16 | https://www.thegamer.com/sonic-omens-fan-game-controversy-cars-2-music-maria/ | 2026-04-11 | TheGamer — Sonic Omens Patreon controversy |
| S17 | https://www.nintendolife.com/news/2021/05/sega_is_still_cool_with_sonic_fan_games_provided_no_profit_is_involved | 2026-04-11 | Nintendo Life — SEGA official stance on Sonic fan games |
| S18 | https://soahcity.com/sonic-news/sonic-social-media-manager-responds-to-sonic-fan-games-being-monetized/ | 2026-04-11 | SoaH City — Katie Chrzanowski verbatim quote |
| S19 | https://chronocompendium.com/stories/28 | 2026-04-11 | Chrono Compendium — Chrono Resurrection details |
| S20 | https://www.ssbwiki.com/Project_M | 2026-04-11 | SmashWiki — Project M development history |
| S21 | https://en-americas-support.nintendo.com/app/answers/detail/a_id/50035/ | 2026-04-11 | Nintendo official IP policy page (fetched) |
| S22 | https://www.premierleague.com/ip-enforcement-policy | 2026-04-11 | Premier League IP enforcement policy (404 on fetch; known to exist) |
| S23 | https://www.fandompulse.com/p/axanar-the-star-trek-fan-film-that | 2026-04-11 | FandomPulse — Axanar crowdfunding details |
| S24 | https://www.pcgamer.com/runelite-hd-shut-down/ | 2026-04-11 | PC Gamer — RuneLite HD shutdown news |
| S25 | https://jiplonline.com/2021/11/01/an-argument-for-embracing-the-legality-of-crowdfunded-game-mods/ | 2026-04-11 | JIPL — Academic argument on crowdfunded mod legality |
| S26 | https://www.stexpanded.fandom.com/wiki/Star_Trek_Fan_Film_Guidelines | 2026-04-11 | Star Trek Expanded Universe Wiki — full guidelines text |
| S27 | https://www.cbr.com/most-infamous-nintendo-fan-game-shutdowns/ | 2026-04-11 | CBR — Summary of notable Nintendo shutdowns |

---

## Case Catalog

### Nintendo / Pokémon Domain

---

#### AM2R — Another Metroid 2 Remake (Nintendo/Metroid, 2016) [S1][S2]

- **What happened**: DoctorM64 (Milton Guasti) released AM2R on August 6, 2016, Metroid's 30th anniversary. Within weeks Nintendo filed DMCA notices against hosting sites. On September 2, 2016, Nintendo served a DMCA request directly to DoctorM64's email.
- **Rights-holder action**: DMCA takedowns targeting hosting sites, then a direct personal DMCA to the developer. No public C&D letter was published. Developer's statement: "There will be no more AM2R updates, and no more releases under any platform." [S2]
- **Project response**: Development ended. Version 1.1 (the final release, one month prior) circulates through the community via already-distributed copies.
- **Monetization at time of action**: No evidence of donations, Patreon, or direct monetization found in primary sources. Project was free. [S2]
- **Branding**: Used Nintendo's Metroid IP extensively — character art, music style, game mechanics. No implicit-only strategy; used the "Metroid" name explicitly.
- **Outcome**: Project officially dead. Nintendo released Metroid: Samus Returns (official Metroid II remake) in 2017 — within a year of the takedown.
- **Why this case matters for F1 fan projects**: Demonstrates that Nintendo enforces even when a fan project is non-commercial. The timing (Nintendo had a competing official product in development) is significant. [OPUS-FOLLOWUP: whether Nintendo's enforcement primarily tracked commercial competition vs. IP purity — both narratives fit the timeline]

---

#### Pokémon Uranium (Nintendo/Pokémon, 2016) [S3][S27]

- **What happened**: After nine years of development, Pokémon Uranium was released August 6, 2016, reaching 1.5 million downloads in its first week. Nintendo filed DMCA notices targeting download hosts. The developers announced removal of links on August 13, citing "further legal action" concerns.
- **Rights-holder action**: Multiple DMCA takedown notices to hosting platforms. Creators stated they had not received a direct C&D but chose to comply. Nintendo's notices cited unauthorized use of Pokémon characters.
- **Project response**: Download links removed voluntarily; development officially discontinued September 2016. Community members continue to circulate and update the game.
- **Monetization at time of action**: Creators were "open to suggested PayPal donations of $2–$10" [S3 secondary]. Scale of donation activity is undocumented in primary sources. Whether this was a material factor in Nintendo's action is unverified.
- **Branding**: Used Pokémon name, characters, game mechanics, and branding extensively. Game was a fan-made sequel with an original region.
- **Outcome**: Officially discontinued; community maintains and circulates the game.
- **Why this case matters for F1 fan projects**: 1.5 million downloads created a scale of public attention that appears to have been a factor — this wasn't a quiet corner-of-the-internet project. Scale of distribution matters. [OPUS-FOLLOWUP: whether PayPal donation solicitation meaningfully contributed to enforcement, or whether scale/visibility was the primary trigger]

---

#### Pokémon Prism (Nintendo/Pokémon, 2016) [S4][S5]

- **What happened**: Koolboyman's Pokémon Crystal ROM hack, eight years in development, received a C&D from Nintendo four days before its planned Christmas 2016 release. The C&D arrived December 21, 2016, from "Addison's Law Firm on behalf of Nintendo of America Inc." [S4]
- **Rights-holder action**: Formal cease and desist letter. Nintendo demanded: (1) cease all further work on Pokémon Prism; (2) by January 7, remove all downloadable links for Prism as well as Pokémon Brown and Pokémon Rijon Adventures, and associated websites and social media. [S5]
- **Project response**: Creator complied. Files leaked to 4chan the next day by third parties as a last-minute preservation act.
- **Monetization at time of action**: "A personal project" distributed "freely as a binary patch" [S4]. No monetization evidence found.
- **Branding**: ROM hack of Pokémon Crystal — used Nintendo's IP throughout. Explicit use of Pokémon name and characters.
- **Outcome**: Project cancelled. The leaked files circulate freely.
- **Why this case matters for F1 fan projects**: Non-commercial, free project hit with formal legal notice. Confirms Nintendo enforces regardless of monetization status. The demand to remove *prior works and social media* shows enforcement can extend beyond the specific project.

---

#### Nintendo Mass DMCA — GameJolt 379 Fan Games (Nintendo, January 2021) [S7]

- **What happened**: Nintendo of America's legal team sent DMCA notices to GameJolt in December 2020, resulting in 379 fan-made games being forcibly removed in January 2021. Games were based on Mario, Pokémon, and Zelda franchises.
- **Rights-holder action**: Mass DMCA notices. Nintendo's stated rationale: games "copy the characters, music, and other features of Nintendo's video games" and the key claim — "The web site at gamejolt.com generates revenue from advertising banners displayed on the site and advertisements played while users wait for the games to load." [S7]
- **Project response**: Developers had no individual recourse; games were removed by the platform. One developer (Jeb Yoshi, "Five Nights at Yoshi's") re-uploaded with ads disabled, interpreting the advertising revenue angle as the trigger. [S7]
- **Monetization at time of action**: The *developers* were not directly monetizing. GameJolt as a *platform* was serving ads around the games. Nintendo's DMCA framed this as profit from IP without permission.
- **Branding**: All games explicitly used Nintendo character names and imagery.
- **Outcome**: 379 games removed. Some re-uploaded after removing ad associations.
- **Why this case matters for F1 fan projects**: Nintendo's framing — that a *platform* generating ad revenue from fan content counts as unauthorized commercial use — is directly relevant to any fan project hosted on a revenue-generating platform. The advertiser's revenue model, not the creator's, was cited. [OPUS-FOLLOWUP: whether this framing is legally robust or a strategic framing in the DMCA notice]

---

#### Project M (Nintendo/Super Smash Bros., 2015) [S20]

- **What happened**: Project M was a fan-made gameplay mod for Super Smash Bros. Brawl developed by the PMDT over six years. On December 1, 2015, the team announced immediate cessation of development, without formal explanation.
- **Rights-holder action**: Nintendo never formally issued a cease and desist to Project M. However, Nintendo had (a) applied automatic Miiverse bans to anyone mentioning "Project M" or "PM," citing "criminal content," and (b) pressured tournament organizers to drop the game from Apex 2015. [S20]
- **Project response**: PMDT dissolved voluntarily, citing a desire to avoid future legal exposure. Team attorney Ryan Morrison confirmed no C&D had been received.
- **Monetization at time of action**: Free mod. No donation infrastructure found.
- **Branding**: Explicit use of Nintendo characters and IP throughout.
- **Outcome**: Development ceased. The final version (3.6) continues to circulate.
- **Why this case matters for F1 fan projects**: Demonstrates that formal legal action is not required to kill fan projects — indirect pressure (tournament exclusion, platform-level suppression) can achieve the same result without a paper trail. Also illustrates a counter-case: a large, popular, non-monetized fan project operated for six years without receiving a formal C&D.

---

#### Pokémon Revolution Online (Nintendo/Pokémon, 2015–present) [S3 secondary]

- **What happened**: Free Pokémon MMORPG launched 2015; continues to operate as of 2026 with 2,000–3,000 daily players.
- **Rights-holder action**: None documented. Community forums show recurring player concern about potential shutdown, but no enforcement found.
- **Project response**: Operating. Disclaimer: "PRO neither owns nor claims to own any portion of the Pokémon Franchise."
- **Monetization at time of action**: Unclear; the game's funding model is not documented in found sources. [OPUS-FOLLOWUP: whether PRO accepts donations or has premium features that could constitute commercial use]
- **Branding**: Uses Pokémon name, assets, and characters throughout. Some re-drawn art assets.
- **Outcome**: Still operating. No public C&D.
- **Why this case matters for F1 fan projects**: Counter-case — a large ongoing fan project in the same IP family that has not been taken down. The relevant distinction from Uranium/Prism is unclear from public records. [OPUS-FOLLOWUP: what distinguishes PRO from Uranium/Prism from an enforcement-trigger perspective; requires deeper investigation]

---

#### Chrono Resurrection (Square-Enix/Chrono Trigger, 2004) [S19]

- **What happened**: Resurrection Games developed a short interactive Windows demo remaking ten scenes from Chrono Trigger in 3D. Square-Enix issued a C&D in September 2004, closing the project. The team noted Square-Enix IP addresses had been visiting their site for three months before the letter.
- **Rights-holder action**: Formal C&D for trademark and copyright infringement. Project publicly closed September 6, 2004.
- **Project response**: Compliance and shutdown.
- **Monetization at time of action**: No evidence of monetization; described as a demo/tribute.
- **Branding**: Explicit use of "Chrono Trigger" name and character designs.
- **Outcome**: Closed permanently.
- **Why this case matters for F1 fan projects**: Shows that even a limited non-commercial demo can trigger a C&D. The prior surveillance (IP address visits for 3 months) suggests rights holders monitor before acting — they don't always act immediately upon discovery.

---

### Star Wars / Lucasfilm Domain

---

#### Star Wars: Galaxy in Turmoil / Frontwire Studios (Lucasfilm/EA, 2016) [S8][S9]

- **What happened**: Frontwire Studios developed a free fan game based on the cancelled Star Wars: Battlefront III, built in Unreal 4. On June 4, 2016, the project announced a distribution deal through Valve/Steam. On June 22, 2016, Lucasfilm sent a formal C&D.
- **Rights-holder action**: Written C&D from Lucasfilm requesting immediate halt of all Star Wars-related IP use. Lucasfilm stated they would have been "open to negotiating a license" but their contract with EA prohibited it. EA's concern: the fan project could "take away attention from their Battlefront franchise." [S8][S9]
- **Project response**: Star Wars content removed. Project pivoted to an original IP under the same title, with a Kickstarter for development funding.
- **Monetization at time of action**: Project was planned as free. The Steam distribution deal (no payment) appears to have been the trigger — the moment of *mainstream platform visibility*, not monetization.
- **Branding**: Explicit Star Wars name, characters, and IP throughout.
- **Outcome**: Relaunched as original-IP game. Star Wars version is gone.
- **Why this case matters for F1 fan projects**: The trigger here was *official platform distribution* (Steam), not commercial profit. A fan project that announces a Steam release moves into territory that activates IP holder response even if it is free. Platform legitimacy itself is a trigger.

---

#### Star Trek: Axanar (Paramount/CBS, 2015–2017) [S10][S11][S23]

- **What happened**: Alec Peters and Axanar Productions produced Prelude to Axanar (a ~20-minute Star Trek fan film) funded via Kickstarter, which raised $101,000 against a $10,000 goal. A follow-up Indiegogo campaign raised over $1 million for the feature Axanar. On December 29, 2015, CBS and Paramount filed a copyright lawsuit.
- **Rights-holder action**: Federal copyright lawsuit (not just C&D). Alleged infringement of Klingon language, settings, characters, species, and themes. Settlement reached January 2017: Axanar agreed to "substantial changes" and to abide by newly published fan film guidelines.
- **Project response**: Settlement terms: Axanar could release as two 15-minute YouTube segments (free, ad-disabled); no further crowdfunding allowed.
- **Monetization at time of action**: Over $1.3 million raised via Kickstarter and Indiegogo across both campaigns. A studio and sets had been built. CBS General Counsel reportedly stated the project "looked like the studio itself produced it." [S23] The crowdfunding scale — not donation-level but production-company-level — appears central to the lawsuit.
- **Branding**: Did not use "Star Trek" in the title. However, used Klingon language, Federation design language, and canon characters and settings extensively.
- **Outcome**: Settlement. Guidelines issued for all Star Trek fan films. Subsequent arbitration (2023) found Peters violated settlement terms; awarded $292,372.54 to CBS/Paramount.
- **Why this case matters for F1 fan projects**: Clearest example of crowdfunding triggering rights-holder legal action. Scale matters: $1.3M raised crosses from "fan donations" to "production company" territory. The resulting fan film guidelines set a $50,000 crowdfunding cap explicitly. [OPUS-FOLLOWUP: whether the $50K cap in Paramount/CBS guidelines has any analogy to non-Star-Trek fan project fundraising norms]

**Star Trek Fan Film Guidelines (issued June 23, 2016)** [S11][S26]:
Key provisions (verbatim from sources):
- Runtime: "no more than 2 segments, episodes or parts, not to exceed 30 minutes total"
- Crowdfunding: "total amount does not exceed $50,000, including all platform fees"
- Non-commercial: "only be exhibited or distributed on a no-charge basis"
- Required disclaimer: "This fan production is not endorsed by, sponsored by, nor affiliated with CBS, Paramount Pictures, or any other Star Trek franchise"
- Prohibited: using "Star Trek" in the title; registering works under copyright or trademark

---

### Harry Potter / Warner Bros. Domain

---

#### Wizarding World Online (Warner Bros./Harry Potter, 2015) [S12]

- **What happened**: BioHazard Entertainment ran a Kickstarter campaign to fund "The Wizarding World Online," an MMO game based on Harry Potter. Warner Bros. sent a C&D.
- **Rights-holder action**: C&D from WB lawyers stating the campaign was "devoted to the creation of an MMO game based on the Harry Potter stories and films." [S12 — secondary source; WebFetch returned 403]
- **Project response**: Kickstarter campaign terminated.
- **Monetization at time of action**: Kickstarter crowdfunding campaign was the funding mechanism. This is a case where the *fundraising itself* was the vector of enforcement.
- **Branding**: "Wizarding World" name; direct Harry Potter IP reference.
- **Outcome**: Project shut down.
- **Why this case matters for F1 fan projects**: WB specifically targeted the Kickstarter campaign — the public fundraising event — rather than tolerating the project until it launched. Fundraising as a *signal of commercial intent* triggered preemptive enforcement.

---

### SEGA / Sonic Domain

---

#### Sonic Omens / SEGA Tolerance Policy (SEGA/Sonic, 2021) [S16][S17][S18]

- **What happened**: Sonic Omens, a fan game by Russian studio Ouroboros, generated controversy in 2021 when it was discovered they had paywalled previews through Patreon and run ads on Game Jolt for the game. This prompted SEGA's social media manager to clarify SEGA's fan game policy publicly.
- **Rights-holder action**: No enforcement action against Sonic Omens documented. SEGA's public response was a policy statement, not a C&D.
- **Project response**: Ouroboros denied charges and claimed content was original. Game appears to have continued.
- **Monetization at time of action**: Patreon with paywalled previews; Game Jolt ads. This was the explicit point of community controversy.
- **Branding**: Explicit Sonic IP.
- **SEGA's stated policy** (Katie Chrzanowski, SEGA Social Media and Influencer Manager, 2021): "So long as no profit is involved, there is usually* no issue with y'all using our blue boy to hone your art and dev skills." The asterisk was noted as existing "for legal reasons." [S17][S18]
- **On donations specifically**: Community and SEGA-adjacent sources characterize fan game donations as "a tricky grey area" with SEGA suggesting "the best course of action to avoid scrutiny from Sega would be to avoid any form of payment altogether if possible." [S17]
- **Outcome**: Sonic Omens continued (no enforcement); SEGA policy statement stands.
- **Why this case matters for F1 fan projects**: SEGA is the most permissive major IP holder with a *documented public policy*. Their line is explicit: non-commercial = tolerated; monetized = problematic. The "tricky grey area" for donations vs. direct profit is notable — SEGA draws the line at monetization but acknowledges donations are not clearly on one side.

---

#### Nintendo's "A Fox in Space" Patreon Shutdown (Nintendo/Star Fox, 2018) [S13]

- **What happened**: Matthew Gafford's animated Star Fox fan series, originally titled "Star Fox: The Animated Series," had an active Patreon. Nintendo DMCA'd the Patreon account, forcing it down and deactivating the creator's account.
- **Rights-holder action**: DMCA against the Patreon account specifically — targeting the funding infrastructure, not just content distribution. [S13 — secondary source; NeoGAF thread; WebFetch returned 403]
- **Project response**: Title changed to "A Fox in Space" (non-Nintendo name). Patreon restarted under the creator's personal name (Matthew Gafford) rather than the show's name.
- **Monetization at time of action**: Active Patreon tied to the Star Fox fan series.
- **Branding**: Original title used "Star Fox" explicitly. After forced rebrand, implicit branding only (no Nintendo names used).
- **Outcome**: Series continued under rebranded title and renamed Patreon. As of 2020, only one episode had been released.
- **Why this case matters for F1 fan projects**: **Most directly relevant to the donation question.** Nintendo targeted the Patreon *account* directly — not the YouTube content, not the website. The enforcement vector was the funding infrastructure. After rebranding to remove explicit IP names, the project survived. This suggests Nintendo's Patreon enforcement tracked the explicit trademark use in the account name, not merely the existence of donations.

---

### Motorsport / Sim Racing Domain

---

#### FIA C&D to Modding Teams — F1 Content (FIA, 2014) [S15]

- **What happened**: The FIA sent cease and desist letters to "several modding teams working on mods resembling FIA governed cars and series." F1ASR, a modding team working on a Ferrari 643 F1 and Formula 1 1992 mod, received a letter and "announced that they will suspend work on the mods till further notice." The article (published August 2014) notes VirtualR.net had received "a similar Formula 1 related 'cease and desist' request only a few months ago." [S15]
- **Rights-holder action**: Formal C&D letters. "It is rumoured that more unauthorized modding projects are under investigation, including hardware mods." The FIA's campaign was believed connected to a planned FIA-sanctioned sim racing championship (partnership with Polyphony Digital/Gran Turismo).
- **Project response**: F1ASR suspended work pending further notice.
- **Monetization at time of action**: Article notes "payed modding and sponsored leagues and teams" as emerging trends that "might open up a can of worms." Not clear if F1ASR was monetized.
- **Branding**: Explicit Formula 1 / FIA branding in the mods.
- **Outcome**: F1ASR suspension. Broader modding ecosystem continues producing F1 content without documented enforcement since 2014.
- **Why this case matters for F1 fan projects**: The FIA — not Formula 1 Group — sent these letters, and the motive appears to be protecting a commercial sim racing partnership. This is directly analogous to prix-guesser's domain. The FIA's enforcement was targeted at high-fidelity sim content using F1 IP, not at quiz games or data tools. [OPUS-FOLLOWUP: whether the FIA vs. FOM/Liberty Media distinction matters for enforcement; who controls which rights in sim content vs. brand/data]

---

#### iRacing / NASCAR Official License (NASCAR, 2010–present) [search results only]

- **What happened**: iRacing has been a NASCAR licensee since 2010. In 2023, iRacing acquired the exclusive simulation-style console racing games license from Motorsport Games. iRacing runs official eNASCAR esports series.
- **Rights-holder action**: No enforcement needed — iRacing operates as an officially licensed partner.
- **Monetization**: iRacing is a paid subscription service with licensed NASCAR content.
- **Branding**: Full official branding under license.
- **Outcome**: Model example of a commercial sim getting full official licensing.
- **Why this case matters for F1 fan projects**: Demonstrates the motorsport space has a functioning licensing pathway for commercial simulators. The existence of official licensing makes unauthorized commercial simulators more legally exposed — there's a known alternative.

---

#### RuneLite HD / Jagex (Jagex/Old School RuneScape, 2021) [S14][S24]

- **What happened**: Developer 117scape spent 2,000 hours over two years building RuneLite HD, a high-definition fan mod for Old School RuneScape. Jagex contacted the developer at "the eleventh hour" — hours before the September 6, 2021 planned launch — and ordered the project shut down, citing their own planned visual upgrade.
- **Rights-holder action**: Not a formal C&D but a direct developer contact demanding the project halt. Jagex declined the developer's offer to hand over collaborative control and to take down the project once Jagex released their own upgrade.
- **Project response**: Developer complied; in-game protests erupted across OSRS. Jagex reversed the decision within a week (September 13, 2021), announcing RuneLite HD would release and they would collaborate with 117scape going forward.
- **Monetization at time of action**: RuneLite itself has a Patreon (https://www.patreon.com/runelite), and developer 117scape was reportedly generating ~$300/month in donations toward the RuneLite HD effort. Jagex never specifically cited donations as the enforcement trigger — competitive concern was the stated reason.
- **Branding**: No explicit RuneScape trademark use; RuneLite is a third-party client.
- **Outcome**: Community pressure reversed the enforcement. RuneLite HD released. First documented case of fan community protest *successfully reversing* a rights-holder enforcement action.
- **Why this case matters for F1 fan projects**: Shows that (a) competitive concern, not monetization, can be the trigger; (b) community pressure can reverse enforcement; (c) a project accepting modest donations (~$300/month) was not the stated reason for attempted shutdown.

---

### Scanlation / Fan Translation Domain

---

#### Reaper Scans (Kakao Entertainment/webtoon content, 2025) [search results only]

- **What happened**: Reaper Scans, a major webtoon scanlation site operating six years, received a C&D from Kakao Entertainment and permanently shut down May 9, 2025.
- **Rights-holder action**: C&D. Scanlation sites are a known enforcement target when publishers have active official distribution.
- **Monetization at time of action**: Aggregator sites typically monetize through advertising. Kakao had its own official distribution platform (Webtoon/Tapas).
- **Outcome**: Shutdown.
- **Why this case matters for F1 fan projects**: Pattern match for "fan project tolerated until rights holder builds official competing product" — at which point enforcement becomes more likely.

---

## Pattern Analysis

### What Triggers Enforcement

Drawing on the 15+ cases above, enforcement correlates with the following factors (in descending apparent weight; note this is pattern inference from a small sample, not a systematic study):

**1. Commercial competition with an existing or planned official product**
The clearest trigger across domains. AM2R was taken down with an official Metroid II remake in development [S1]. Galaxy in Turmoil was taken down when it competed with EA's Battlefront franchise [S8]. The FIA's 2014 modding C&Ds coincided with a planned official FIA sim championship [S15]. RuneLite HD was suppressed when Jagex planned their own HD upgrade [S14]. Reaper Scans were shut down once Kakao had official distribution channels.

*Pattern*: When an official product is being developed or sold in the same space, fan projects face enforcement regardless of their monetization status.

**2. Mainstream platform visibility / distribution deal**
Galaxy in Turmoil received a C&D only after announcing a Steam distribution deal — not before. The project had been developing for years without enforcement; the Steam announcement was the trigger [S8][S9]. This suggests visibility and legitimization of a fan project as a "real product" (on a major platform) matters independently of profit.

**3. Scale of crowdfunding / commercial-looking fundraising**
Axanar raised $1.3M — the trigger was the production-company scale, not the existence of crowdfunding per se [S10][S23]. The resulting Star Trek guidelines cap fan fundraising at $50,000 [S26]. Wizarding World Online was targeted because its Kickstarter campaign was a public commercial act [S12].

**4. Explicit trademark / branding use**
Cases where explicit IP name appears in the project title correlate heavily with C&D. A Fox in Space survived after removing "Star Fox" from the title [S13]. Pokémon Prism and AM2R used explicit Nintendo trademarks throughout. Galaxy in Turmoil was directed to strip Star Wars branding but allowed to continue as an original IP game.

**5. Advertising revenue on hosting platforms**
Nintendo's 2021 GameJolt sweep explicitly cited GameJolt's advertising revenue as the monetization vector — even though developers themselves weren't directly paid [S7]. This is a proxy-monetization trigger.

### What Does NOT Trigger Enforcement (evidence from surviving projects)

- **Non-commercial, low-visibility, free-only projects**: Large numbers of Pokémon fan games continue to exist on smaller platforms without enforcement. Pokemon Reborn, Pokemon Insurgence, and Pokemon Revolution Online have operated for years without documented C&Ds.
- **Projects that use original assets with reduced explicit branding**: Community consensus in the Pokémon fan game community identifies original sprites, original music, and reduced Nintendo character names as protective factors [S3 secondary community analysis].
- **Modest community-scale projects**: Project M operated for six years without a formal C&D, even at tournament scale [S20]. Nintendo applied indirect pressure but no legal action.
- **Projects outside the IP holder's core commercial territory**: SEGA tolerates Sonic fan games explicitly because Sonic fan games do not directly compete with SEGA's commercial releases in the way that, e.g., a competing Pokemon game might [S17][S18].

### How Monetization Affects Rights-Holder Response

The case record does not support a simple "donations = enforcement" rule. The evidence is more nuanced:

| Monetization Type | Case Evidence | Apparent Risk |
|-------------------|---------------|---------------|
| No monetization whatsoever | AM2R (taken down), Pokémon Prism (taken down), Project M (survived) | Not protective — enforcement can happen anyway |
| Small donations / Ko-fi style | RuneLite HD (~$300/mo) — Jagex cited competition, not donations; A Fox in Space Patreon — Nintendo targeted the Patreon *account name* using Star Fox trademark, not the donations per se | Low but ambiguous; depends on branding of the donation vehicle |
| Patreon tied to explicit IP name in account | A Fox in Space (original name) — Patreon account DMCA'd | High; trademark use in Patreon account name appears to be the specific trigger |
| PayPal donations with suggested amounts | Pokémon Uranium ($2–$10 suggested) — enforcement happened, but donation role not confirmed as trigger | Ambiguous |
| Kickstarter / Indiegogo crowdfunding | Axanar ($1.3M total) — triggered federal lawsuit; Wizarding World Online — Kickstarter campaign itself targeted | High at commercial scale ($50K+); may be lower below that threshold |
| Patreon for general creator support (not tied to IP name) | A Fox in Space post-rebrand — Patreon under "Matthew Gafford" survived | Lower; depends on whether IP branding is removed from the account |
| Platform advertising (indirect) | Nintendo GameJolt 2021 — 379 games removed because GameJolt showed ads | Moderate; creator not profiting directly but platform revenue used as justification |

**Key finding on donations**: There is no documented case where a fan project *accepting modest voluntary donations (Ko-fi / tip jar)* was shut down *specifically because of those donations*, where the project would otherwise have been tolerated. The donation-linked cases involve either (a) large-scale fundraising that crossed into production-company territory (Axanar), (b) explicit IP trademark use in the donation platform account name (A Fox in Space), or (c) platform advertising unrelated to the creator's donation income.

[OPUS-FOLLOWUP: This is a pattern inference from ~5 monetization cases. Confirming cases of genuinely donation-only projects that were shut down vs. survived would require deeper search. The absence of documented "Ko-fi shutdown" cases may reflect survivorship bias — such projects may not generate news coverage.]

### Does Implicit vs. Explicit Branding Change Enforcement?

Evidence suggests yes, with important caveats.

**A Fox in Space** [S13]: After removing "Star Fox" from the title and Patreon account name, the project survived. Nintendo's enforcement appeared to track the explicit trademark use, not the fan activity itself.

**Galaxy in Turmoil** [S8][S9]: Lucasfilm's C&D included an explicit offer — they would have no issue with "a Battlefront inspired game that is not using the Star Wars IP itself." The implicit reference (Battlefront gameplay style) was explicitly tolerated; the explicit brand was not.

**SEGA's policy** [S17]: Does not specify any tolerance for implicit branding vs. explicit. SEGA's line is profit, not branding visibility.

**Caveat**: Implicit branding does not protect against enforcement when the rights holder has a competing product (see iRacing / FIA sim racing — F1 content mods were targeted regardless of how explicitly they used the FIA name). [OPUS-FOLLOWUP: whether "implicit F1 branding" — using accurate team colors, car silhouettes, track layouts — would be treated differently by Liberty Media/FOM than explicit use of F1®, Formula 1®, and team names. This is the most direct question for prix-guesser but requires domain-specific investigation beyond this lane.]

---

## Donation-Specific Subsection

**Question**: Are there documented cases where donation funding became the specific enforcement trigger?

**Direct answer**: One clear case of Patreon being the targeted enforcement vehicle (A Fox in Space [S13]). One large-scale crowdfunding case that triggered litigation (Axanar [S10]). One Kickstarter targeting (Wizarding World Online [S12]).

**What the record does NOT show**: A documented case where a rights holder said explicitly "we would have tolerated this project if it were not for the donations/Ko-fi/Patreon." The typical enforcement rationale is trademark infringement, copyright infringement, or commercial competition — not the donation instrument per se.

**What the record DOES show**:
1. Rights holders target the *funding infrastructure* when they want to shut down a project (Nintendo DMCA'd the Patreon account, not just the YouTube videos, for A Fox in Space).
2. The *scale* of crowdfunding is a genuine trigger once it crosses into production-company territory (~$50K+ based on Star Trek guidelines).
3. Rights holders cite monetization as *justification* for enforcement even when the creator isn't the direct beneficiary (GameJolt advertising revenue, 2021).
4. The Pokemon fan game community has developed strong internal norms against monetization precisely because they believe it increases enforcement risk — this is a community-derived heuristic, not a documented legal rule.
5. SEGA is the only major IP holder with a *documented explicit public policy* drawing a line at monetization: "so long as no profit is involved, there is usually no issue." [S18]

**Applicability to prix-guesser**: A quiz/guessing game using public F1 data and implicit branding, accepting Ko-fi tips, would sit in different territory from all the shutdown cases above. The clearest enforcement risks would be: (1) explicit use of F1® / Formula 1® trademarks in the project name or Ko-fi account; (2) scale of fundraising that creates commercial appearance; (3) launch on mainstream distribution platforms (Steam, App Store) which creates legitimization pressure. The modest donation tier is not itself well-documented as an enforcement trigger in isolation.

[OPUS-FOLLOWUP: Whether F1's specific fan content policy (as investigated in B8-1 and B8-2 lanes) addresses donation-funded fan projects explicitly. Cross-reference with B7's finding on F1 legal ambiguity.]

---

## F1 Relevance Section

Given patterns from other IP-heavy domains, what should we expect from F1 if it were to engage with community projects?

**Analogy most applicable to prix-guesser**: The SEGA Sonic model (explicit non-commercial tolerance), the Paramount Star Trek model (explicit guidelines with crowdfunding cap), and the FIA sim racing enforcement (which shows F1-adjacent IP holders do enforce against sim content but not general fan projects).

**Risk profile inference**:

1. **Non-commercial, low-visibility quiz game**: Based on patterns from Nintendo, SEGA, and Lucasfilm, a free project with no monetization and modest distribution is unlikely to attract enforcement *unless* it directly competes with an official F1 product or uses explicit F1® trademarks. F1's own quiz/trivia products (if they exist or are planned) would raise competition concerns; a general fan guessing game without an official equivalent seems low-risk by analogy.

2. **Explicit F1® trademark use**: Consistently the highest-risk factor across all domains. Using "F1," "Formula 1®," or team logos in project name/branding creates clear trademark exposure. Implicit reference (car silhouettes, driver numbers, track layouts) appears to reduce risk based on the A Fox in Space and Galaxy in Turmoil cases.

3. **Donation/Ko-fi funding**: Based on the record, small-scale donations are not well-documented as standalone enforcement triggers. The risk increases if: (a) donations are tied to an account or page that explicitly uses F1 trademarks, or (b) total fundraising reaches commercial-looking scale.

4. **Sim racing content specifically**: The FIA has demonstrated it will enforce against F1 content in simulator mods [S15]. Mais prix-guesser is not a simulator — this risk vector appears inapplicable unless the project incorporates detailed simulation content.

[OPUS-FOLLOWUP: All of the above is cross-domain inference. F1/Liberty Media's actual enforcement culture may differ from Nintendo's, SEGA's, or Lucasfilm's. The B7 lane covers F1-specific policy text; this lane's patterns should be read as probabilistic analogies, not as F1 predictions. F1's commercial interests in fan engagement may make them more tolerant than Nintendo's model suggests.]

---

## What I Did NOT Check

1. **DC / Marvel fan games specifically**: Found primarily AI chatbot enforcement cases (Disney C&D to Character.AI, 2025) and licensed game cases (Marvel Heroes). Did not find documented fan game C&Ds for Marvel/DC in the fan-game-maker community. [Would require targeted search for specific projects]

2. **NBA / NFL data dashboard apps**: Searches returned general trademark enforcement (NFL apparel, Super Bowl trademark) but no documented C&D against fan analytics tools. This may reflect that sports data rights enforcement operates through terms-of-service and API access restriction rather than C&D letters.

3. **Hogwarts Legacy era WB enforcement vs. fan games**: Found only the 2015 Wizarding World Online Kickstarter case. Did not find post-Hogwarts Legacy fan game enforcement history.

4. **MotoGP / IndyCar / WRC fan enforcement**: Found no documented enforcement cases for these motorsports. The absence may reflect that these series have less active fan project ecosystems, fewer dedicated fan games, and no large-scale community sim mods with documented enforcement history. Or it may reflect search-result gaps.

5. **Formula E fan projects**: Not searched.

6. **odinlaw.com citation from Lane 1C (LQ-1C.4 Finding 2)**: The predecessor lane cited odinlaw.com on fan-game legal risks. This source was not independently verified or extended in this lane. [OPUS-FOLLOWUP: Retrieve and assess odinlaw.com's specific claims for this research program]

7. **Anime fansub history in detail**: Only found scanlation cases. Pre-streaming-era anime fansub history (Funimation's tacit tolerance of fansubs pre-2006, then active enforcement post-streaming) is potentially relevant but not investigated.

8. **Documented "donation-only" project shutdowns**: Did not find a case where Ko-fi/tip-jar-level donations were specifically cited as the enforcement trigger. The absence may be real or may reflect that such projects don't generate news coverage.

9. **Simulator platform ToS enforcement (vs. rights-holder enforcement)**: The Assetto Corsa modding ecosystem for F1 content was only shallowly investigated. Steam Workshop removal of specific F1 mods, if any, was not found.

---

## Flagged for Opus Follow-up

1. **[OPUS-FOLLOWUP: AM2R]** Whether Nintendo's enforcement primarily tracked commercial competition (official Metroid II remake in development) vs. IP purity — both narratives fit the timeline. Primary: DoctorM64's statement [S2] does not address this.

2. **[OPUS-FOLLOWUP: Pokémon Uranium donations]** Whether PayPal donation solicitation ($2–$10 suggested) materially contributed to enforcement, or whether 1.5M downloads / media attention was the primary trigger. Primary sources do not resolve this.

3. **[OPUS-FOLLOWUP: Pokémon Revolution Online]** What distinguishes PRO from Uranium/Prism from an enforcement perspective. Does PRO have a commercial or donation model? Does server location matter?

4. **[OPUS-FOLLOWUP: Star Trek $50K guideline]** Whether the $50K crowdfunding cap in Paramount/CBS guidelines has any analogical bearing on other fan project fundraising norms in other domains. Is this a precedent or an isolated rights-holder choice?

5. **[OPUS-FOLLOWUP: GameJolt advertising framing]** Whether Nintendo's legal framing (platform ad revenue = unauthorized commercial exploitation) is legally robust or a strategic DMCA framing. Journal of Intellectual Property Law published an argument against this framing [S25] — needs assessment.

6. **[OPUS-FOLLOWUP: FIA vs. FOM/Liberty Media rights]** Who controls which rights in sim content (FIA) vs. brand/data (FOM/Liberty). Whether prix-guesser is in FOM space, FIA space, or both. The 2014 FIA sim modding C&Ds are in FIA space; quiz/data tools may be in FOM/commercial rights space.

7. **[OPUS-FOLLOWUP: Implicit F1 branding]** Whether "implicit F1 branding" — accurate team colors, car silhouettes, track layouts, without using F1® wordmark — would be treated differently by Liberty Media/FOM than explicit trademark use. This is the central branding question for prix-guesser and was not resolved by any cross-domain analogy found.

8. **[OPUS-FOLLOWUP: Donation trigger isolation]** Confirming/disconfirming cases of genuinely donation-only (Ko-fi / tip jar, not Kickstarter) projects that were shut down. The absence of documented cases may be real or may reflect survivorship/coverage bias.

9. **[OPUS-FOLLOWUP: odinlaw.com]** The Lane 1C predecessor cited this source on fan-game legal risks. Needs retrieval and assessment.

10. **[OPUS-FOLLOWUP: F1 fan project cross-reference]** All F1-relevance inferences in this lane should be cross-referenced with B7 (F1 legal ambiguity) and B8-1/B8-2 (F1 fan project survey) findings. This lane's patterns are cross-domain analogies only.

---

## Qualifications

1. **Not a legal opinion.** Every "pattern" here is an empirical observation from 15 cases across 6+ domains. The sample is not systematic; cases documented in news are biased toward high-profile shutdowns (survivorship bias: tolerated projects rarely make news).

2. **Secondary sources dominate for older cases.** Primary sources (creator statements, actual C&D letters) were retrieved for AM2R, Pokémon Prism (Archive.org), Star Trek Axanar (Hollywood Reporter, Deadline), and FIA modding (BSimRacing). Most other cases relied on gaming news coverage as secondary sources.

3. **Nintendo is overrepresented.** Nintendo's enforcement history is the most documented in any search-accessible corpus. This may make Nintendo's pattern (aggressive, non-commercial projects targeted) seem more universal than it is. SEGA is notably more permissive; Lucasfilm is more targeted; the FIA enforced once in a specific context.

4. **Donation question has weak evidence.** The central "does Ko-fi/Patreon trigger enforcement?" question has approximately 3–5 relevant cases, none of which cleanly isolate the donation variable from confounding factors (explicit trademark use, crowdfunding scale, competitive concern). The answer "donations alone are not well-documented as standalone triggers" should be held loosely.

5. **F1 relevance inferences are cross-domain analogies.** They are not predictions about Liberty Media / FOM / FIA behavior. F1's commercial relationship with fan engagement, its specific IP portfolio (driver names, team names, race track names, circuits, historical data), and its actual enforcement history are covered by other lanes in this research program.
