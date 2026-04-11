# Lane 03 Findings: Public Transition And Discovery

Date: 2026-04-10
Lane: `03-public-transition-and-discovery`
Status: complete

## Question Space

- [CONFIRMED] Prix Guesser's current documented posture is private-first, browser-first, authored, and socially oriented around live rooms, host-screen legibility, and phone/browser participation rather than around public matchmaking or account-first retention loops. [PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md)
- [INFERRED] The real question is not "how do we market it?" It is "which surfaces become public, in what order, and with what access rules, without turning the product into a different thing."
- [INFERRED] For this product, `friends-only`, `selectively public`, and `public product` are not just audience-size labels. They are different operating modes with different expectations around discoverability, moderation, reliability, and identity.
- [INFERRED] The answer depends materially on what Prix Guesser becomes. If the durable center is `watchable live rooms`, discovery should stay host- and invite-led longer. If `async challenges` become an equal wrapper, broader public discovery becomes more coherent earlier. If `streamer/spectator play` becomes central, audience tooling and moderation become first-order product concerns rather than later polish.

## Method And Sources

- [CONFIRMED] I grounded the lane first in repo-local intent and roadmap posture so the research would answer the actual project question rather than a generic "indie growth" question. [PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [.continue-here](../../../phases/01-authored-round-contract/.continue-here.md), [Cross-Lane Reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md)
- [CONFIRMED] I then used official product/help/docs pages from GeoGuessr, Jackbox, Kahoot, Steamworks, and Twitch to verify current patterns around private lobbies, challenge links, public-vs-limited access controls, streamer overlays, and moderation requirements. These are strong for feature and policy facts. They are weaker for proving what users will emotionally prefer. [GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends), [GeoGuessr Private Lobby](https://geoguessr.zendesk.com/hc/en-us/articles/4413903235729-How-do-I-set-up-a-Private-Lobby), [GeoGuessr Create Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz), [GeoGuessr Only Invited](https://geoguessr.zendesk.com/hc/en-us/articles/28237315964177-How-do-I-create-a-challenge-for-a-set-number-of-users), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch), [Jackbox Custom Episodes](https://support.jackboxgames.com/hc/en-us/articles/15794763590167-Using-custom-or-user-created-episodes), [Jackbox Moderation](https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work), [Kahoot Live Host](https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot), [Kahoot PIN](https://support.kahoot.com/hc/en-us/articles/360000109048-Kahoot-game-PIN-how-to-find-Kahoot-PIN), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform), [Kahoot Preview](https://support.kahoot.com/hc/en-us/articles/29968568026131-How-to-preview-a-kahoot), [Steam Playtest](https://partner.steamgames.com/doc/features/playtest), [Twitch Extensions Overview](https://dev.twitch.tv/docs/extensions), [Twitch Extension Policies](https://dev.twitch.tv/docs/extensions/guidelines-and-policies/)
- [CONFIRMED] I also used one medium-authority public company-direction signal from GeoGuessr's career site and job materials. Those are useful for trajectory hints, but they are partly promotional and should not be treated like neutral postmortems. [GeoGuessr Career Site](https://career.geoguessr.com/), [GeoGuessr Party Team Job Post](https://career.geoguessr.com/jobs/6950938-senior-product-manager-party-team)
- [CONFIRMED] I did not find a high-quality independent postmortem that cleanly matches "small curated browser party game moving from trusted-circle use to selective public discovery." That absence matters. Some transition judgments here remain synthesis rather than direct precedent.

## Inquiry Trajectory

1. [INFERRED] I started with the surface question: what actually changes when a private-first product becomes "more public"?
2. [INFERRED] That immediately branched into join/discovery grammars, because room-code products, challenge-link products, and streamer-visible products do not spread the same way.
3. [INFERRED] That in turn exposed a second branch: selective publicness is not just about who can see the product, but about who can enter, who can post content, and who can affect live sessions.
4. [INFERRED] Researching selective publicness forced a moderation branch. As soon as public viewers or semi-public participants can submit text, names, or prompts, moderation and identity stop being optional side systems.
5. [INFERRED] From there, the inquiry widened again into trust and capacity communication: once access is public-facing, the product owes users clearer expectations about uptime, queueing, invite limits, and experiment status.
6. [INFERRED] The end result is that discovery strategy cannot be separated cleanly from wrapper choice, moderation model, and hosting posture. The path is not linear: product shape determines discovery surfaces, and discovery surfaces feed back into what moderation and operations must exist.

## Branching Paths And Dependencies

- [INFERRED] `Discovery path` depends first on `which wrapper is being promoted`.
  - [INFERRED] `Live room / host-screen wrapper` depends on direct host invitations, fast join, and trust within the session.
  - [INFERRED] `Async challenge wrapper` depends on frozen sessions, shareable links/codes, and clear result boundaries.
  - [INFERRED] `Streamer / spectator wrapper` depends on audience interaction affordances, latency tolerance, and moderation/identity controls.
- [INFERRED] `Selective publicness` depends on `what is public`.
  - [INFERRED] Public `marketing/read` surfaces are much cheaper than public `play` surfaces.
  - [INFERRED] Public `spectating` is cheaper than public `participation`.
  - [INFERRED] Public `challenge intake` is cheaper than public `live room entry`.
- [INFERRED] `Discovery expansion` depends on `operational honesty`.
  - [INFERRED] If signups become public, capacity gating, waitlists, or windows become product features rather than backstage logistics. [Steam Playtest](https://partner.steamgames.com/doc/features/playtest)
- [INFERRED] `Semi-public pack sharing` depends on `content governance`.
  - [INFERRED] Bounded creator sharing is feasible earlier than open publishing because moderation surface area is smaller. [Jackbox Custom Episodes](https://support.jackboxgames.com/hc/en-us/articles/15794763590167-Using-custom-or-user-created-episodes)
- [INFERRED] `Public streamer discovery` depends on `identity and moderation`.
  - [CONFIRMED] Twitch requires user-content extensions to have broadcaster review/remove controls and Twitch-linked user identity for submitters. [Twitch Extension Policies](https://dev.twitch.tv/docs/extensions/guidelines-and-policies/)

## Findings

### Public Transition Is Better Understood As Surface Layering Than As A Single Launch

- [CONFIRMED] GeoGuessr, Jackbox, Kahoot, Steam Playtest, and Twitch all expose different combinations of public visibility and gated participation rather than a simple private/public binary. [GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends), [GeoGuessr Only Invited](https://geoguessr.zendesk.com/hc/en-us/articles/28237315964177-How-do-I-create-a-challenge-for-a-set-number-of-users), [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform), [Steam Playtest](https://partner.steamgames.com/doc/features/playtest)
- [INFERRED] The strongest reading for Prix Guesser is:
  - [INFERRED] `Friends-only`: no ambient discovery; nearly all play enters through direct host invitation, room code, QR, or explicit challenge link.
  - [INFERRED] `Selectively public`: some discovery surfaces are public, but access to actual play is still bounded by invites, signups, capacity windows, or specific wrapper rules.
  - [INFERRED] `Public product`: broad signups and ambient discovery exist, and users reasonably expect reliable access, visible status, and stronger moderation.
- [INFERRED] For Prix Guesser, the least distorting transition is likely `public read surfaces first`, `public async or challenge surfaces second`, and `public live-room participation last`.

### Room-Code, Challenge-Link, And Streamer Products Have Different Discovery Grammars

- [CONFIRMED] Jackbox and Kahoot show a host-led grammar: one person starts a session, others join via code/link/QR, and the host or shared screen anchors the social context. [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Kahoot Live Host](https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot), [Kahoot PIN](https://support.kahoot.com/hc/en-us/articles/360000109048-Kahoot-game-PIN-how-to-find-Kahoot-PIN)
- [CONFIRMED] GeoGuessr shows a challenge-link grammar alongside live party play: private lobbies, shareable URLs, public leaderboard options, anonymized nicknames, and "only invited" challenges coexist. [GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends), [GeoGuessr Private Lobby](https://geoguessr.zendesk.com/hc/en-us/articles/4413903235729-How-do-I-set-up-a-Private-Lobby), [GeoGuessr Create Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz), [GeoGuessr Only Invited](https://geoguessr.zendesk.com/hc/en-us/articles/28237315964177-How-do-I-create-a-challenge-for-a-set-number-of-users)
- [CONFIRMED] Jackbox's Twitch Audience Kit shows a third grammar: the stream itself becomes the discovery and participation surface, collapsing some join friction for viewers inside Twitch. [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch)
- [INFERRED] Prix Guesser should not assume these grammars can be merged without tradeoffs. A product can support all three over time, but each one changes which user is the growth agent:
  - [INFERRED] `host` for room-code products
  - [INFERRED] `artifact/link` for challenge products
  - [INFERRED] `broadcaster` for spectator products

### Growth Loops That Fit The Product

- [INFERRED] **Host-brings-the-table loop.** One enthusiastic host gets a room running, invites a few friends with a code/link/QR, and the group returns for another session because the live experience itself was good. This fits the current roadmap best because it preserves the watchable private-room center. [ROADMAP](../../../ROADMAP.md), [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Kahoot Live Host](https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot)
- [INFERRED] **Post-session challenge loop.** A live session creates enough enthusiasm that someone shares a frozen challenge or replayable pack slice afterward with adjacent friends or the same group between sessions. This is a better bridge into selective publicness than opening live rooms to strangers. [GeoGuessr Create Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform)
- [INFERRED] **Reveal/clip-to-waitlist loop.** Public social artifacts should point first to curiosity and interest capture, not immediately to open room participation. For a niche product, a reveal clip, scoreboard screenshot, or authored pack teaser can recruit future interested players without promising instant open access.
- [INFERRED] **Limited-signup beta loop.** Steam's playtest tooling is a strong precedent for "visible enough to gather interest, gated enough to preserve capacity control." The usable lesson is not Steam-specific; it is that public interest can accumulate while access is still batched, paused, or geographically limited. [Steam Playtest](https://partner.steamgames.com/doc/features/playtest)
- [INFERRED] **Streamer audience-to-invite loop.** If a streamer/spectator wrapper ever exists, the strongest first use is probably not "open the whole game to anyone." It is "let the public watch and occasionally participate in bounded ways, then convert the most interested viewers into later challenges, signups, or curated test groups." [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch), [Twitch Extensions Overview](https://dev.twitch.tv/docs/extensions)

### Growth Loops That Would Distort The Product

- [INFERRED] **Open public lobby discovery early.** For a hobby-scale, curated, expert-biased product, a public room directory would push operations and moderation costs up before the product has earned them.
- [INFERRED] **Daily-challenge-first identity.** GeoGuessr's daily and global competition loops are real and effective for GeoGuessr, but if Prix Guesser promotes public daily competition too early, it risks recentering around generic repeatability instead of authored reveal-rich social play. [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge)
- [INFERRED] **Referral pressure and invite farming.** Steam's experimental friend-invite controls explicitly warn that invite growth can compound quickly and should be used only with robust server capacity. For Prix Guesser, hard incentive loops around invites would likely create pressure, hype, and queue pain faster than they create healthy community. [Steam Playtest](https://partner.steamgames.com/doc/features/playtest)
- [INFERRED] **Open UGC marketplace logic.** Jackbox's custom-episode precedent is bounded, code-based, and supported by reporting/moderation. Prix Guesser would likely distort itself if it jumped from curated authored content straight to fully public pack publishing and discovery. [Jackbox Custom Episodes](https://support.jackboxgames.com/hc/en-us/articles/15794763590167-Using-custom-or-user-created-episodes)
- [INFERRED] **Public ranked ladders as the first real retention loop.** This would import a public-competition center of gravity before the room/challenge substrate and moderation posture are mature enough to support it honestly.

### Selective Publicness

- [INFERRED] **Selective publicness should be surface-specific.** A useful staged model is:
  - [INFERRED] Public `landing`, `clips`, `waitlist`, and `status` surfaces
  - [INFERRED] Semi-public `async challenges` or `playtest signup` surfaces
  - [INFERRED] Private `live room entry` surfaces for longer
  - [INFERRED] Bounded `creator sharing` surfaces before any open pack directory
- [CONFIRMED] Steam Playtest explicitly supports showing or hiding playtest signup, limited or open signup modes, country gating, direct key distribution without a public signup, and pausing or ending access later. [Steam Playtest](https://partner.steamgames.com/doc/features/playtest)
- [CONFIRMED] GeoGuessr explicitly supports "only invited" challenges, private lobby URLs, public leaderboards, and anonymized nicknames on shared challenges. [GeoGuessr Private Lobby](https://geoguessr.zendesk.com/hc/en-us/articles/4413903235729-How-do-I-set-up-a-Private-Lobby), [GeoGuessr Create Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz), [GeoGuessr Only Invited](https://geoguessr.zendesk.com/hc/en-us/articles/28237315964177-How-do-I-create-a-challenge-for-a-set-number-of-users)
- [INFERRED] The closest Prix Guesser analogue is therefore not "private until sudden launch." It is "public enough to gather the right people, bounded enough that live trust and operator capacity are not silently overpromised."
- [INFERRED] Selective publicness also lets the project keep different wrappers at different openness levels:
  - [INFERRED] `Local/private live rooms`: mostly invitation-driven
  - [INFERRED] `Async challenges`: selectively shareable
  - [INFERRED] `Spectator/streamer layer`: potentially public earlier than live-room participation
  - [INFERRED] `Pack authorship`: trusted-circle or code-based before directory-style browsing

### Discovery Paths Depend On Wrapper Choice More Than On Marketing Cleverness

- [INFERRED] If the product remains primarily `host-screen-first`, discovery should optimize for making one host successful with a group, then making repeat hosting easy.
- [INFERRED] If the product grows an `async challenge` wrapper, discovery can broaden via shareable artifacts because async play tolerates looser timing, looser coordination, and more selective public exposure.
- [INFERRED] If the product grows a `spectator/streamer` wrapper, discovery becomes partly a broadcasting problem. Then overlay ergonomics, latency, audience moderation, and in-stream participation design become part of the discovery strategy itself. [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch), [Twitch Extensions Overview](https://dev.twitch.tv/docs/extensions)
- [INFERRED] This is why a single "growth plan" is the wrong abstraction here. Prix Guesser likely needs separate discovery doctrines for `live-room`, `challenge`, and `spectator` wrappers.

### Publicness Changes The Burden Of Trust

- [CONFIRMED] Steam explicitly warns developers to communicate before taking away playtest access and to be deliberate about changing access states. [Steam Playtest](https://partner.steamgames.com/doc/features/playtest)
- [CONFIRMED] Jackbox's public-stream guidance says to hide room codes, use private messages for preferred players, and use passworded rooms and moderation features to reduce troll risk. [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Moderation](https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work)
- [CONFIRMED] Twitch requires identity and broadcaster controls once extensions allow user-submitted content. [Twitch Extension Policies](https://dev.twitch.tv/docs/extensions/guidelines-and-policies)
- [INFERRED] The trust burden therefore ratchets upward in stages:
  - [INFERRED] `Private rooms` mainly owe smooth join and social clarity.
  - [INFERRED] `Selective public beta` owes honest access/status/capacity communication.
  - [INFERRED] `Public spectator or participant surfaces` owe moderation, identity handling, and clearer behavioral boundaries.

### Feasibility By Surface

| Surface | Technical Feasibility | Operational Feasibility | Adoption Feasibility | Economic Feasibility | Ethical / Trust Feasibility |
|---|---|---|---|---|---|
| Invite-only live rooms | [INFERRED] High | [INFERRED] Medium-high | [INFERRED] High for existing friend groups | [INFERRED] High for hobby scale | [INFERRED] High |
| Public waitlist / limited signup beta | [INFERRED] High | [INFERRED] Medium | [INFERRED] Medium-high | [INFERRED] Medium-high | [INFERRED] Medium-high if limits are explicit |
| Public or semi-public async challenges | [INFERRED] High | [INFERRED] Medium | [INFERRED] Medium-high | [INFERRED] Medium | [INFERRED] Medium if identity/privacy/result controls exist |
| Streamer / spectator participation | [INFERRED] Medium | [INFERRED] Low-medium | [INFERRED] Uncertain and product-shape dependent | [INFERRED] Uncertain | [INFERRED] Medium-low until moderation is strong |
| Open public live rooms / lobby discovery | [INFERRED] Medium | [INFERRED] Low for hobby scale | [INFERRED] Uncertain | [INFERRED] Low | [INFERRED] Low unless product posture changes substantially |

- [INFERRED] The asymmetry matters. The technically easiest surface to add is not always the most operationally or ethically feasible one.

## Gray Areas And Live Tensions

- [INFERRED] **Discovery wants visibility; the product's current soul wants bounded intimacy.** The more ambiently discoverable live rooms become, the more Prix Guesser risks drifting from expert-fan game night into generic online game service.
- [INFERRED] **No-account join and moderation pull against each other.** Jackbox-like frictionlessness is powerful, but public or streamer-adjacent participation quickly creates pressure for stronger identity, blocking, and moderation controls. [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Jackbox Moderation](https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work), [Twitch Extension Policies](https://dev.twitch.tv/docs/extensions/guidelines-and-policies)
- [INFERRED] **Async discoverability may be healthier than live discoverability, but it may also slowly recenter the product away from its watchable-room identity.**
- [INFERRED] **A waitlist can be honest capacity management or manipulative scarcity theater.** The difference is not mechanical. It depends on how transparently constraints, windows, and admission logic are communicated. [Steam Playtest](https://partner.steamgames.com/doc/features/playtest)
- [INFERRED] **Streamer visibility can widen discovery while making players feel performative.** That may help some wrappers and weaken others. The right answer probably depends on whether the core fantasy remains solver-centric, reveal-centric, or audience-centric.
- [HYPOTHESIS] **The strongest long-term discovery loop may not be the one with the highest top-of-funnel reach.** For a niche expert-fan product, the better loop may be the one that preserves trust and repeat hosting, even if it looks slower.

## Scope Expansions

- [CONFIRMED] **Scope Expansion: moderation and identity.** This emerged because publicness is not only about seeing the product; it is about who can submit content or influence live sessions. I pursued this branch enough to establish that streamer/public participation surfaces carry real moderation requirements. [Jackbox Moderation](https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work), [Twitch Extension Policies](https://dev.twitch.tv/docs/extensions/guidelines-and-policies)
- [CONFIRMED] **Scope Expansion: capacity communication and playtest governance.** This emerged because selective publicness quickly becomes a queueing/access problem. I pursued it because Steam offers unusually explicit official language about gating, pausing, and expectation-setting. [Steam Playtest](https://partner.steamgames.com/doc/features/playtest)
- [INFERRED] **Scope Expansion: creator-surface governance.** This emerged because challenge sharing and public discovery naturally raise the question of who gets to publish content. I investigated bounded precedents but did not push into a full UGC-governance design, which belongs more to future moderation/governance work. [Jackbox Custom Episodes](https://support.jackboxgames.com/hc/en-us/articles/15794763590167-Using-custom-or-user-created-episodes)
- [INFERRED] **Scope Expansion: wrapper-specific discovery doctrine.** This emerged because "discovery" meant different things in live-room, async, and spectator contexts. I pursued this deeply because it materially changes the research answer.
- [INFERRED] **Flagged but not pursued deeply: legal/IP posture under public visibility.** This became faintly visible, but the lane brief focused on trust/product/public transition rather than rights risk, so I am only flagging it.

## Rival Models Still Alive

- [INFERRED] **Model A: Private rooms stay central; publicness is mostly read-only plus waitlist.** This is the most conservative model and best preserves the current social center.
- [INFERRED] **Model B: Public async edge, private live core.** Live rooms remain invite-led, while challenge links and limited public playtests become the main discovery surfaces.
- [INFERRED] **Model C: Streamer/spectator wrapper becomes the main public edge.** The game stays socially legible and private at its core, but public discovery happens through audience-compatible broadcasts and bounded audience participation.
- [INFERRED] **Model D: Public game service earlier than currently planned.** If daily play, broad remote participation, or public competition become strategic priorities sooner, the product may rationally move toward more GeoGuessr-like discovery and less tightly curated selective openness. This remains viable, but it is not the strongest fit to current posture.

## Practical Implications

### Thinking Implications

- [INFERRED] Think in terms of `surface openness`, not one global `private/public` switch.
- [INFERRED] Use different vocabulary for `room access`, `challenge access`, `spectator access`, and `creator access`. They should not be silently coupled.
- [INFERRED] Treat "discovery" as wrapper-specific. A room-code product does not discover itself the same way a challenge-link product does.

### Design Implications

- [INFERRED] Design separate join and share grammars for:
  - [INFERRED] live room
  - [INFERRED] async challenge
  - [INFERRED] spectator or stream interaction
- [INFERRED] If public-facing interest capture exists, the UI should make mode/state legible: private test, limited beta, waitlist-only, or public challenge.
- [INFERRED] If streamer surfaces are explored later, the room code and participation surface should be intentionally hideable or role-gated rather than assuming "public stream = public room."

### Implementation Implications

- [INFERRED] Build room/session/share primitives so access policy can vary by wrapper rather than being one global boolean.
- [INFERRED] Preserve frozen-session or frozen-pack semantics for any future challenge-link surface. Discovery gets easier when the shared artifact is stable.
- [INFERRED] Leave room for role distinctions like `host`, `player`, `audience`, `spectator`, and later `moderator`.
- [INFERRED] Plan for public-status and capacity language before large public discovery surfaces, even if the first version is simple.

### Measurement Or Experiment Implications

- [INFERRED] The first discovery experiment should probably not be "open it to everyone." It should be one of:
  - [INFERRED] invited host cohort test
  - [INFERRED] bounded async challenge sharing test
  - [INFERRED] read-only waitlist interest capture
- [INFERRED] Metrics that matter early:
  - [INFERRED] host-to-second-session rate
  - [INFERRED] invited-player-to-new-host conversion
  - [INFERRED] challenge-link completion rate
  - [INFERRED] waitlist-to-active-tester conversion
  - [INFERRED] moderation incidents per public-facing session
- [INFERRED] If a streamer wrapper is ever tested, measure not only clicks or viewers but also whether players still report that the game feels like expert recognition rather than audience performance.

## What Would Change This View

- [INFERRED] Strong playtest evidence that async challenges produce more authentic delight and repeat use than live-room hosting
- [INFERRED] Strong evidence that streamer discovery produces high-quality participants rather than low-trust audience spillover
- [INFERRED] A strategic decision that public daily play or persistent public competition matters much sooner than current documents suggest
- [INFERRED] Operational evidence that moderation and queue/status handling are easier to support than this pass assumes
- [HYPOTHESIS] Evidence that the product's most durable emotional center is not the shared-screen room, but a different wrapper entirely

## Open Questions Worth A Third Pass

1. [INFERRED] What is the lightest-weight public waitlist or signup model that feels honest rather than hype-driven for a tiny hosted hobby product?
2. [INFERRED] If Prix Guesser exposes async challenges publicly, what privacy defaults should govern names, standings, and replay visibility?
3. [INFERRED] What is the smallest viable moderation model for semi-public spectator participation without forcing full account systems too early?
4. [INFERRED] Which wrapper is most likely to create new good hosts rather than merely one-off curious visitors?
5. [HYPOTHESIS] Is there a viable middle state where pack/reveal artifacts are widely visible but actual play remains mostly trusted-circle for a long time?
6. [HYPOTHESIS] If the project eventually supports trusted external authors, what discovery surface preserves curation without quietly becoming a marketplace?

## Source Ledger

| Source | Authority | Used For | Reliability Limits |
|---|---|---|---|
| [PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [.continue-here](../../../phases/01-authored-round-contract/.continue-here.md), [Cross-Lane Reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md) | High for repo intent | Current product posture, wrapper assumptions, roadmap center of gravity | Internal planning artifacts; not user telemetry |
| [GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends), [Private Lobby](https://geoguessr.zendesk.com/hc/en-us/articles/4413903235729-How-do-I-set-up-a-Private-Lobby), [Create Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz), [Only Invited](https://geoguessr.zendesk.com/hc/en-us/articles/28237315964177-How-do-I-create-a-challenge-for-a-set-number-of-users), [Remove Challenge Results](https://geoguessr.zendesk.com/hc/en-us/articles/28237329276049-How-do-I-remove-someone-from-the-leaderboard-of-a-Challenge), [Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge) | High for current product behavior | Invite surfaces, challenge sharing, selective publicness controls, public challenge precedent | Product-specific; does not prove transferability |
| [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch), [Custom Episodes](https://support.jackboxgames.com/hc/en-us/articles/15794763590167-Using-custom-or-user-created-episodes), [Moderation](https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work), [Profanity Filtering](https://support.jackboxgames.com/hc/en-us/articles/15794794632983-How-does-Profanity-Filtering-work) | High for current product behavior | Host-screen join grammar, public-stream precautions, bounded creator sharing, moderation precedent | Support docs are instructional, not postmortems |
| [Kahoot Live Host](https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot), [Kahoot PIN](https://support.kahoot.com/hc/en-us/articles/360000109048-Kahoot-game-PIN-how-to-find-Kahoot-PIN), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform), [Kahoot Preview](https://support.kahoot.com/hc/en-us/articles/29968568026131-How-to-preview-a-kahoot) | High for current product behavior | Distinguishing live host-led vs learner-paced challenge wrappers, join-link/QR/PIN patterns, preview/testing | Education use case biases some design assumptions |
| [Steam Playtest](https://partner.steamgames.com/doc/features/playtest) | High for official access-control tooling and policy | Limited/open signup, country gating, friend invites, expectation-setting, selective publicness mechanics | Steam-specific implementation; analogy rather than direct product match |
| [Twitch Extensions Overview](https://dev.twitch.tv/docs/extensions), [Twitch Extension Policies](https://dev.twitch.tv/docs/extensions/guidelines-and-policies/) | High for technical/policy facts | Spectator/public-participation architecture, moderation and identity requirements | Twitch-specific; applies mainly if a stream-facing wrapper exists |
| [GeoGuessr Career Site](https://career.geoguessr.com/), [GeoGuessr Party Team Job Post](https://career.geoguessr.com/jobs/6950938-senior-product-manager-party-team) | Medium | Public trajectory signal, browser-social-entry framing | Promotional/company-facing materials, not neutral retrospective analysis |
