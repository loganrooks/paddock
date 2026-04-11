# Public Transition And Discovery Clean-Room XHigh Findings

## Question Space

- [CONFIRMED] The local project documents currently define Prix Guesser as a private-only, unofficial F1 fan project whose strongest near-term proof is a watchable, host-led, curated game-night product built around authored rounds, private rooms, and phone/browser participation rather than public matchmaking or mass distribution. Sources: local starting context in `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/phases/01-authored-round-contract/.continue-here.md`, `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`, `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`, `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md`.
- [INFERRED] The real research question is therefore not "how do we market a public product?" but "which surfaces, if any, should become more visible or shareable without collapsing the trust, intimacy, and operator-manageability that make the first product shape attractive?"
- [INFERRED] The most useful distinctions are between `friends-only`, `selectively public`, and `public product`, and those distinctions appear to be surface-specific rather than app-global.

## Method And Sources

- [CONFIRMED] This was a clean-room rerun. I read only the local files explicitly permitted by the spec and did not read the forbidden prior findings or comparison artifacts.
- [CONFIRMED] External sourcing emphasized primary sources from product/platform documentation and official blogs, then added one secondary academic source for streamer and visibility dynamics.
- [CONFIRMED] The external primary set used here was: GeoGuessr support docs, Jackbox support docs, Discord support docs, and Bluesky official blog posts.
- [CONFIRMED] The external secondary source used here was Felan Parker and Matthew E. Perks, "Streaming ambivalence: Livestreaming and indie game development" (2021), to add non-vendor analysis of how streamability changes product shape.
- [CONFIRMED] Claim labels mean: `[CONFIRMED]` = directly supported by the cited local or external sources, `[INFERRED]` = synthesis grounded in multiple sources plus product context, `[HYPOTHESIS]` = plausible product-direction claim that would require experimentation or later evidence.

## Inquiry Trajectory

- [CONFIRMED] The inquiry started from the spec question of how a private-first niche hobby product might become selectively more public over time.
- [INFERRED] Very quickly, that split into four subquestions: what the likely wrapper progression is, what discovery loops fit each wrapper, what kinds of openness trigger moderation and hosting burden, and which public surfaces would preserve rather than deform the product.
- [INFERRED] The most productive branch was not generic growth advice but comparison across real systems that already separate private join, invited sharing, discoverable participation, and fully public visibility.
- [INFERRED] That branch then made a deeper dependency visible: public transition is partly a hosting question, but even more a trust-and-governance question, because searchable or semi-public surfaces change abuse exposure and user expectation before they necessarily change traffic scale very much.
- [CONFIRMED] A final branch looked specifically at streamer and spectator surfaces, because local context repeatedly treats watchability as load-bearing and because streaming can act as discovery without requiring public lobbies.

## Branching Paths And Dependencies

- [INFERRED] Discovery doctrine depends first on wrapper choice. A live-room product, an async challenge product, a spectator product, and a creator-sharing product do not naturally grow through the same loops.
- [INFERRED] Visibility doctrine depends on whether a surface is merely accessible by link or code, actively discoverable by search or directory, or globally open by default.
- [INFERRED] Trust burden depends on the join and publishing model. Private room invites create one burden profile; public pack directories and public profiles create a different one.
- [INFERRED] Moderation burden depends less on raw audience size than on searchable discovery, user-generated publishing, and whether strangers can enter the same social space without host mediation.
- [INFERRED] Hosting burden depends on which public surface opens first. Public async challenge pages increase read traffic and attribution needs; public live rooms increase concurrency, pacing, abuse, and support burden; streamer surfaces increase spectator visibility and timing sensitivity.
- [INFERRED] Product identity also sits underneath all of this. If Prix Guesser remains primarily a host-led ritual, its publicness should likely emerge through shareable artifacts around that ritual. If it becomes an always-on public game service, discovery and reliability expectations change much earlier.

## Findings

- [CONFIRMED] GeoGuessr already separates multiple visibility modes across different surfaces. Its "Play with Friends" flow uses a private lobby where the host can "share the URL with your friends," its challenge flow can be set to "Only Invited," and its Daily Challenge asks players to "compete with the rest of the world." Sources: [GeoGuessr: What is Play with Friends?](https://geoguessr.zendesk.com/hc/en-us/articles/5428968241681-What-is-Play-with-Friends), [GeoGuessr: How can I delete a Challenge?](https://geoguessr.zendesk.com/hc/en-us/articles/4407930444305-How-can-I-delete-a-Challenge), [GeoGuessr: What is Daily Challenge?](https://geoguessr.zendesk.com/hc/en-us/articles/4407932814737-What-is-Daily-Challenge).
- [CONFIRMED] GeoGuessr also keeps some explicit capacity and moderation controls even on ostensibly private party surfaces; its party support docs note a 100-person invite limit and separate controls for kicking or banning people from a private party. Sources: [GeoGuessr: How many can I invite to my Party?](https://geoguessr.zendesk.com/hc/en-us/articles/4409656812049-How-many-can-I-invite-to-my-Party), [GeoGuessr Party section](https://geoguessr.zendesk.com/hc/en-us/sections/4409656513681-Party).
- [CONFIRMED] Jackbox's official remote-play guidance treats publicness as a broadcast wrapper rather than as public matchmaking. Its support article says that if you want to open your game up to the public, using Twitch or YouTube is the best path, and it recommends low-latency settings so the room stays close to real time. Source: [Jackbox: Can I play Jackbox Games remotely?](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-).
- [CONFIRMED] Jackbox's Twitch Audience Kit exists specifically to reduce participation friction in a streamer surface; the company frames it as avoiding the need to explain room codes or tell people how to get to Jackbox.tv. Source: [Jackbox: The Jackbox Audience Kit Twitch Extension FAQ](https://support.jackboxgames.com/hc/en-us/articles/21010347372951-The-Jackbox-Audience-Kit-Twitch-Extension-FAQ).
- [CONFIRMED] Jackbox also exposes a creator-sharing surface that is not equivalent to a fully public marketplace. Its custom-episode flow generates a unique share URL and allows the creator to refresh the share code, which implies controlled, revocable sharing rather than a permanent global publishing commitment. Source: [Jackbox: Custom Episode - How to Create and Share your Episode](https://support.jackboxgames.com/hc/en-us/articles/23011591925015-Custom-Episode-How-to-Create-and-Share-your-Episode).
- [CONFIRMED] Discord formalizes three join postures for communities: `Invite Only`, `Apply to Join`, and `Discoverable`. It also offers Community Onboarding for self-selection, a "Pause Invites" control to manage growth or raid conditions, and stricter requirements for Server Discovery, including safety requirements, moderator 2FA, age/activity thresholds, and at least 1,000 members. Sources: [Discord: Server Member Applications](https://support.discord.com/hc/en-us/articles/235097487-Server-Member-Applications), [Discord: Community Onboarding FAQ](https://support.discord.com/hc/en-us/articles/25084282205335-Community-Onboarding-FAQ), [Discord: Pause Invites FAQ](https://support.discord.com/hc/en-us/articles/5665228332695-Pause-Invites-FAQ), [Discord: Enabling Server Discovery](https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery).
- [CONFIRMED] Bluesky's official transition from invite-only to open signup was explicitly tied to trust and capability maturity. The company says it used invite codes to manage growth while building moderation tooling and custom feeds, later says it intentionally slowed invite rollout while it built more moderation tooling and capacity, and only then announced that anyone could join. Sources: [Bluesky: Private Beta Update & Roadmap](https://bsky.social/about/blog/6-02-2023-beta-update), [Bluesky: Join Bluesky Today (Bye, Invites!)](https://bsky.social/about/blog/02-06-2024-join-bluesky).
- [CONFIRMED] The same Bluesky materials show that public transition was not a single binary switch. Even while invite-only, Bluesky added custom feeds, moderation controls, and server-side invite distribution; once open, it continued to frame moderation and feed choice as core to user trust rather than as optional polish. Sources: [Bluesky: Private Beta Update & Roadmap](https://bsky.social/about/blog/6-02-2023-beta-update), [Bluesky: Join Bluesky Today (Bye, Invites!)](https://bsky.social/about/blog/02-06-2024-join-bluesky).
- [CONFIRMED] The academic streaming literature used here argues that livestreaming changes what kinds of games are practical to build, market, and sell, and that watching streams and gameplay videos becomes an extension of playtesting and community management. Source: [Parker and Perks, 2021](https://journals.sagepub.com/doi/10.1177/13548565211027809).
- [INFERRED] Taken together, the most relevant pattern is that small or socially shaped products do not responsibly become "more public" by opening everything at once. They usually add narrowly chosen public or semi-public surfaces only after the corresponding trust, moderation, and operator controls exist.
- [INFERRED] The strongest analogs for Prix Guesser are not "viral consumer growth" products but products that separate code-based participation, unlisted sharing, public discovery, and creator publication into different layers with different obligations.
- [INFERRED] For Prix Guesser specifically, discovery is likely to depend more on wrapper choice than on generic marketing tactics. A public async challenge page, a streamer-friendly spectator layer, and a curated featured-pack shelf would each create very different discovery loops and operational costs.

## Growth Loops That Fit The Product

- [INFERRED] **Host-invite loop:** the most native early loop is still "someone hosts a game night, then reuses the product with friends and friend-of-friend guests." This matches the local roadmap's private-room posture and aligns with GeoGuessr private lobbies and Jackbox room-code culture.
- [INFERRED] **Unlisted challenge-link loop:** the cleanest early step toward publicness is likely an async or semi-async challenge page that can be shared by link without becoming globally searchable. GeoGuessr's invited challenge posture and Jackbox's revocable share URLs both support this pattern.
- [INFERRED] **Stream-to-participation loop:** streamer or spectator visibility can create public awareness while keeping actual play controlled by host code, selected entrants, or capped audience interactions. Jackbox is the strongest direct evidence that this kind of wrapper can be public-facing without requiring public matchmaking.
- [INFERRED] **Curated feature loop:** if Prix Guesser later needs broader discovery, a featured shelf of approved packs, challenge highlights, or showcase events fits better than an open marketplace. Bluesky's use of custom feeds and Discord's staged discoverability both suggest that curation can be a growth surface without making the whole system indiscriminately open.
- [HYPOTHESIS] **Club-to-club loop:** because F1 fandom has strong friend-group, group-chat, and niche-community habits, Prix Guesser may grow best through hosts bringing the game into adjacent small circles rather than through anonymous acquisition. This is plausible but needs real play evidence.

## Growth Loops That Would Distort The Product

- [CONFIRMED] The local requirements already treat public matchmaking, ranked ladders, and a broad public UGC marketplace as out of scope for v1. Source: `.planning/REQUIREMENTS.md`.
- [INFERRED] **Public-room browsing** would distort the current product fastest. It would move the game from host-mediated social ritual toward stranger-lobby service operations, which implies earlier moderation, anti-abuse, pacing, and support obligations.
- [INFERRED] **Open marketplace publishing** would also distort the product early. Prix Guesser's current edge is curated authored quality, and the external examples suggest that public creator surfaces become meaningfully different products once discoverability, abuse handling, attribution, and revocation all matter.
- [INFERRED] **Algorithmic daily-content pressure** would likely distort authoring priorities by rewarding volume, repeatable cadence, and broad accessibility over reveal quality, circuit literacy, and game-night payoff.
- [INFERRED] **Streamer-first simplification of the core game** would risk flattening the expert-fan identity into spectacle-friendly gimmicks if mass-watchability becomes the dominant design constraint too early.
- [INFERRED] **Account-social-graph growth tactics** would likely misframe the product as a social network or retention system before it has proven the room ritual that justifies any broader public layer.

## Selective Publicness

- [INFERRED] `Friends-only` in practice means room access by direct invite, link, QR, or spoken code; no searchable room directory; no expectation that strangers will enter the social space; and no requirement that the product explain itself well to cold traffic.
- [INFERRED] `Selectively public` in practice means some surfaces can be shared or discovered publicly while the core play surface remains controlled. Discord's `Invite Only` versus `Apply to Join` versus `Discoverable`, GeoGuessr's invited challenges versus Daily Challenge, and Jackbox's public stream wrapper all point to this middle territory.
- [INFERRED] `Public product` in practice means open signup, searchable discovery, durable public pages or profiles, explicit abuse/reporting paths, and a stronger expectation of reliability, moderation responsiveness, and explanation for strangers.
- [INFERRED] Prix Guesser should likely adopt selective publicness per surface rather than once for the whole app.
- [INFERRED] **Live-room surface:** this should probably stay private the longest. The host-led room is the most socially intimate and the most expensive place to admit strangers or tolerate trolling.
- [INFERRED] **Async challenge surface:** this is the strongest candidate for early semi-public experimentation because it is more inspectable, lower-concurrency, and easier to moderate than live stranger rooms.
- [INFERRED] **Spectator or streamer surface:** this can likely become semi-public earlier than active live play, because visibility can be public while actual participation stays code-gated, capped, or delayed.
- [INFERRED] **Creator or pack-sharing surface:** this should likely begin as curated or approved rather than open submission. Once packs are publicly browsable, Prix Guesser inherits editorial, moderation, attribution, and quality-ranking obligations that do not exist in a purely private corpus.
- [HYPOTHESIS] A useful eventual visibility model may be something like `private`, `unlisted`, and `featured/public`, applied separately to rooms, challenges, and packs rather than globally to the whole account or whole product.

## Gray Areas And Live Tensions

- [INFERRED] The strongest current product fantasy is live, social, and host-led, but the cleanest early public surface may be async challenge sharing. That creates a real tension between the emotional center of the product and the safest discovery surface.
- [INFERRED] Streamer-friendliness can help discovery without public lobbies, but it may also bias the game toward spectacle, immediacy, and audience readability in ways that differ from what makes a private expert-fan room feel satisfying.
- [INFERRED] Curated featured packs could preserve quality, but curation itself becomes work. Editorial surfacing is lighter than an open marketplace, yet it still introduces approval, ranking, attribution, and report-handling burden.
- [INFERRED] Selective publicness preserves intimacy better than full openness, but it can also create product complexity if visibility rules are inconsistent or hard to understand across rooms, challenges, packs, and spectator surfaces.
- [HYPOTHESIS] Prix Guesser's niche specificity may reduce absolute abuse volume relative to general social products, but it probably will not remove the need for reporting, revocation, and moderation once any searchable public surface exists.

## Scope Expansions

- [CONFIRMED] The research question expanded from discovery and invitations into trust burden, moderation burden, hosting burden, and service obligation, because the external examples consistently tied opening up to those concerns.
- [INFERRED] A second scope expansion was from "public versus private" to "which surfaces get which visibility posture," because the most relevant products almost all split those concerns rather than handling them with a single global privacy setting.
- [INFERRED] A third scope expansion was into streamer and creator surfaces. These are not optional side topics here; they appear to be distinct public-transition pathways with different costs and benefits.
- [CONFIRMED] I pursued the surface-specific publicness and trust-burden expansions in this pass. I only flagged, but did not deeply pursue, the legal/commercial implications of public pack sharing and the rights implications of becoming more outward-facing as an unofficial F1 product.

## Rival Models Still Alive

- [INFERRED] **Model A: stay intentionally private for a long time.** The product improves joining, hosting, and replay value, but discovery stays almost entirely friend-network-based.
- [INFERRED] **Model B: selective publicness around the private core.** Live rooms remain private, while publicness first appears through challenge links, spectator streams, or curated featured surfaces. This currently looks strongest.
- [INFERRED] **Model C: gradual transition into a more legible public hobby product.** Over time, packs, creators, profiles, and discovery become more durable and public-facing, but only after moderation and operational tooling matures.
- [HYPOTHESIS] A fourth model also remains possible: Prix Guesser stays private as a room product while a sibling async or creator-facing surface becomes the more discoverable public face. This would preserve the ritual core but split the product family earlier than current roadmap language assumes.

## Practical Implications

### thinking implications

- [INFERRED] Discovery should be treated as a wrapper-design problem, not as a generic marketing layer bolted on later.
- [INFERRED] Public transition should be discussed as a matrix of surfaces and obligations, not as a single launch milestone.
- [INFERRED] The project should explicitly distinguish hosting burden, moderation burden, and trust burden whenever it considers a more public surface.

### design implications

- [INFERRED] Every shareable surface should communicate its visibility state clearly: private, link-shared, or public/featured.
- [INFERRED] The UI for live rooms should bias toward quick trusted joining via code, link, or QR rather than toward browse-and-join behavior.
- [INFERRED] Any public challenge or featured-pack surface should make authorship, curation status, and reporting/revocation paths legible.
- [INFERRED] Streamer surfaces should separate spectators from active players clearly so the public layer does not accidentally rewrite the room contract.

### implementation implications

- [INFERRED] Visibility should likely be modeled at the surface level, with separate policies for rooms, challenge links, packs, and possibly spectator pages.
- [INFERRED] Invite primitives should likely support rotation, expiry, and revocation, because selective publicness is easier to manage when hosts can shut down or refresh exposure paths quickly.
- [INFERRED] If any public or featured pack surface exists, the system will need some combination of attribution metadata, report intake, takedown or unfeature controls, and editorial state.
- [INFERRED] If streamer or spectator surfaces arrive early, timing and latency tooling become more important because public visibility amplifies awkward pacing failures.
- [HYPOTHESIS] A future permissions model might need concepts like `host-controlled`, `link-shared`, `featured`, and `publicly indexed`, rather than a simple boolean `public`.

### measurement or experiment implications

- [INFERRED] The first public-transition experiment should probably be narrower than "open the app." A better sequence is likely: private room reuse, then unlisted challenge links, then curated featured surfaces, then only later any broader public discovery.
- [INFERRED] The project should measure not only audience growth but also host repeat rate, invite acceptance rate, support load, report rate, pack reuse, and whether discovery traffic converts into good game-night sessions rather than shallow one-off clicks.
- [INFERRED] If a streamer-facing surface is tested, the right success measure is not raw viewers; it is whether spectators become qualified future hosts or invited participants without raising moderation/support load disproportionately.
- [HYPOTHESIS] A useful experiment would be a small set of publicly shareable weekly challenges with explicit unlisted or featured status, to learn whether async discoverability helps the live-room product or begins to pull the project toward a different emotional center.

## What Would Change This View

- [HYPOTHESIS] If playtests show that async or solo usage becomes the actual emotional center of the product, then public challenge and creator surfaces should move earlier in the transition sequence.
- [HYPOTHESIS] If curated internal authoring proves too slow, the project may need creator-sharing surfaces sooner than this report prefers, which would increase the value of editorial and moderation tooling earlier.
- [HYPOTHESIS] If streamer visibility produces high-quality host conversion without meaningful abuse or support cost, spectator-first publicness would become more attractive.
- [HYPOTHESIS] If operator burden stays very low and the audience remains small-but-well-behaved, the costs of a featured public shelf may be lower than this report currently assumes.
- [HYPOTHESIS] If the product's legal or commercial posture changes materially, the acceptable public-transition path could change with it.

## Open Questions Worth A Third Pass

- [INFERRED] Which surface is the best first semi-public experiment: unlisted challenge links, a curated featured-pack shelf, or streamer/spectator events?
- [INFERRED] What minimum trust-and-safety tools would be required before any pack or challenge becomes publicly discoverable rather than merely shareable?
- [INFERRED] How much of Prix Guesser's discovery should come from creators versus hosts versus spectators?
- [INFERRED] At what point does a public pack surface stop being a helpful showcase and start becoming a de facto moderated marketplace?
- [INFERRED] Does the project need explicit "application" or approval mechanics for some surfaces, analogous to Discord's `Apply to Join`, or are invite links and curation enough?
- [HYPOTHESIS] Could a sibling public challenge product emerge without weakening the private room product, or would the two begin competing for the same authoring attention and identity?

## Source Ledger

- [CONFIRMED] **Local starting context:** `.planning/PROJECT.md`; `.planning/ROADMAP.md`; `.planning/REQUIREMENTS.md`; `.planning/phases/01-authored-round-contract/.continue-here.md`; `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`; `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`; `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md`; `.planning/explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md`.
- [CONFIRMED] **GeoGuessr support docs** — primary product documentation with high authority for visibility and sharing mechanics, moderate authority for strategic interpretation, low obvious promotional bias on operational details. Used for private lobby, invited challenge, daily challenge, and party-capacity signals.
- [CONFIRMED] **Jackbox support docs** — primary product documentation with high authority for remote-play, stream, and creator-share mechanics, moderate bias toward presenting official best practices. Used for stream-to-public play, audience-friction reduction, and revocable share-link patterns.
- [CONFIRMED] **Discord support docs** — primary platform documentation with high authority for join postures, onboarding, invite controls, and discovery requirements, moderate platform bias on safety framing. Used for staged openness and burden-management controls.
- [CONFIRMED] **Bluesky official blog** — primary company narrative with high authority on its own invite, moderation, and growth decisions, but clear self-presentational bias. Used because the post topic is exactly invite pacing, moderation tooling, and opening to broader signup.
- [CONFIRMED] **Parker and Perks (2021)** — secondary academic source with stronger analytical distance than vendor docs, but not Prix-Guesser-specific. Used only to support the narrower inference that streamability changes not just promotion but product practicality and feedback loops.
