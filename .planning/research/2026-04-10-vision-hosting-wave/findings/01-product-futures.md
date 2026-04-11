# Lane 01 Findings: Product Futures, Stage Shapes, And Watchability

Date: 2026-04-10

## Question Space

- [CONFIRMED] Prix Guesser's current documented posture is "private-only, authored, social-first, geography-anchor," and its v1 roadmap is sequenced around live private rooms, guest join, mobile controllers, and a host-screen loop before async wrappers or adjacent modes. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] The real design question is not "local party or solo async?" It is "what is the durable substrate here: authored F1 rounds, a watchable room shell, or a future F1 party platform that happens to start with geography?" ([PROJECT](../../../PROJECT.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))
- [INFERRED] The useful distinction is between `game mode`, `session wrapper`, `watchability layer`, and `platform shell`. Several future-facing disagreements in the repo become clearer once those are treated as different layers rather than one product choice. ([PROJECT](../../../PROJECT.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))

## Method And Sources

- [CONFIRMED] I reviewed the required internal project artifacts first, especially the current product posture, roadmap sequencing, requirements map, and the pre-execution audit synthesis. Those are the best sources for "what this repo currently thinks it is." ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))
- [CONFIRMED] I then checked official product/help pages from GeoGuessr, Jackbox, and Kahoot to ground claims about live rooms, controller patterns, async/self-paced wrappers, co-op affordances, and streamer-facing features. ([GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends), [GeoGuessr Live Challenges](https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges), [GeoGuessr Bulls-Eye](https://geoguessr.zendesk.com/hc/en-us/articles/4420338264849-What-is-Bulls-Eye), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work), [Jackbox Party Pack 2 product page](https://checkout.jackboxgames.com/products/the-jackbox-party-pack-2), [Jackbox remote play guide](https://www.jackboxgames.com/blog/how-to-play-party-pack-nine-remotely), [Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available), [Kahoot how it works](https://kahoot.com/schools/how-it-works/))
- [CONFIRMED] Source authority limits: internal docs are authoritative for current intent but not yet validated by playtest evidence; GeoGuessr/Jackbox/Kahoot official pages are authoritative for feature/menu shape but not for proving which wrapper is most loved or most profitable; no user telemetry or Prix Guesser playtest data was available in this lane. (same sources)

## Findings

### The Product Space Is An Ecology, Not A Binary

- [CONFIRMED] The repo already contains evidence of an ecology rather than a single-mode destiny: v1 is a live-room watchable loop, while v2 requirements already name async challenges, additional wrappers, and adjacent non-anchor modes. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [CONFIRMED] GeoGuessr officially groups "Play with Friends" party modes, private lobbies, challenge URLs, co-op Bulls-Eye, and a separate singleplayer experience under one product family rather than treating them as mutually exclusive products. ([GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends), [GeoGuessr Live Challenges](https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges), [GeoGuessr Bulls-Eye](https://geoguessr.zendesk.com/hc/en-us/articles/4420338264849-What-is-Bulls-Eye), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work))
- [CONFIRMED] Kahoot explicitly supports live-hosted play, self-paced challenges, team play, timer tuning, reports, and shared content organization from one authored content system. ([Kahoot how it works](https://kahoot.com/schools/how-it-works/))
- [CONFIRMED] Jackbox explicitly centers the shared-screen-plus-device-controller pattern, supports remote participation, and offers audience/streamer-specific layers rather than only "players in one room." ([Jackbox Party Pack 2 product page](https://checkout.jackboxgames.com/products/the-jackbox-party-pack-2), [Jackbox remote play guide](https://www.jackboxgames.com/blog/how-to-play-party-pack-nine-remotely), [Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available))
- [INFERRED] The mature public-facing space for Prix Guesser is therefore best understood as a stack of wrappers around one authored F1 substrate: `watchable live room`, `solo/practice shell`, `async challenge shell`, and later `streamer/spectator shell`. The open question is ordering and emphasis, not whether only one may exist. (all sources above)

### The Likely First Privately-Tested Shape

- [CONFIRMED] Internal docs already bias strongly toward host-screen-friendly private play, room authority, guest join, controller clarity, reveal flow, and watchability. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] Given that posture and the adjacent-product evidence, the most likely first privately-tested shape is: one host launches a curated authored pack, the room follows a shared-screen clue/reveal flow, and phones/browsers act as low-friction controllers. That is closer to "private F1 game night software" than to "solo web quiz with optional multiplayer." ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [Jackbox Party Pack 2 product page](https://checkout.jackboxgames.com/products/the-jackbox-party-pack-2), [Jackbox remote play guide](https://www.jackboxgames.com/blog/how-to-play-party-pack-nine-remotely), [Kahoot how it works](https://kahoot.com/schools/how-it-works/))
- [HYPOTHESIS] The best initial social test is probably 2-6 knowledgeable fans in couch-or-hybrid conditions rather than a fully remote internet-first test, because the repo's current emotional center is shared recognition, reveal payoff, and spectator legibility more than persistence or public competition. ([PROJECT](../../../PROJECT.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))

### Which Future Wrappers Still Feel Like The Same Product

- [INFERRED] `Local party`, `private remote synchronous`, and `host-screen plus phone controllers` all still feel like the same product if they share the same authored round contract, judging grammar, reveal grammar, and room progression. The wrapper changes, but the round fantasy stays intact. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [Jackbox remote play guide](https://www.jackboxgames.com/blog/how-to-play-party-pack-nine-remotely))
- [INFERRED] `Solo practice`, `daily challenge`, and `friend challenge link` also still feel like the same product if they are frozen-session or frozen-pack views of the same authored rounds rather than a different content model. Kahoot's live vs self-paced split and GeoGuessr's party vs singleplayer split both support that reading. ([Kahoot how it works](https://kahoot.com/schools/how-it-works/), [GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work))
- [INFERRED] `Streamer mode` still feels like the same product if it mainly removes friction around participation, spectating, or audience response. Jackbox's Twitch extension is exactly that kind of wrapper: the game is not replaced, but the access path and viewing ergonomics change. ([Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available))
- [INFERRED] `Adjacent F1 party modes` only remain the same product if they can reuse the same content substrate, room shell, reveal grammar, and host/controller role split. If they require a different answer grammar, different pacing grammar, and different content tooling, that is closer to a second product line than a wrapper. ([PROJECT](../../../PROJECT.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))

### The Role Of Single-Player

- [CONFIRMED] The current project documents do not frame solo play as the emotional center; they frame social expert-fan play as the core value and treat async/solo as later wrappers. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] In this product, single-player is best thought of as a support shell with four jobs: onboarding, practice, calibration, and habit formation between social sessions. It makes the social core easier to return to; it does not have to replace it. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [Kahoot how it works](https://kahoot.com/schools/how-it-works/), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work))
- [HYPOTHESIS] If Prix Guesser later needs a high-frequency retention wrapper, the most coherent first solo format is likely a frozen authored challenge or daily pack slice rather than a deeper campaign/metagame. That keeps the content substrate unified and avoids inventing a second emotional core too early. ([REQUIREMENTS](../../../REQUIREMENTS.md), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work))

### Kinds Of Watchability

- [INFERRED] `Shared-legibility watchability` means everyone in the room can tell what phase the game is in, what is being asked, and what the reveal just taught. This is the kind of watchability the repo already prioritizes with host-screen, lock-state, reveal, and standings requirements. ([REQUIREMENTS](../../../REQUIREMENTS.md), [ROADMAP](../../../ROADMAP.md))
- [INFERRED] `Suspense watchability` means a round creates visible anticipation before resolution: timer pressure, answer lock, leaderboard movement, or a staged reveal. GeoGuessr Live Challenges exposing within-round leaderboard progress and Kahoot exposing timer/points tuning both show this is a distinct property from simple visual clarity. ([GeoGuessr Live Challenges](https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges), [Kahoot how it works](https://kahoot.com/schools/how-it-works/))
- [INFERRED] `Participation watchability` means non-host and non-winner people still have something to do or anticipate. Jackbox's audience layer and GeoGuessr Bulls-Eye's co-op pings/teleports show that "watching" can include guided participation rather than passive observation. ([Jackbox Party Pack 2 product page](https://checkout.jackboxgames.com/products/the-jackbox-party-pack-2), [Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available), [GeoGuessr Bulls-Eye](https://geoguessr.zendesk.com/hc/en-us/articles/4420338264849-What-is-Bulls-Eye))
- [INFERRED] `Diagnostic watchability` means the reveal is satisfying because it explains the clue logic, not merely the answer. This matters more for Prix Guesser than for many trivia products because the fantasy is expert recognition and interpretation. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] `Broadcast watchability` means the product can be understood and joined from outside the active room with minimal friction. Jackbox's Twitch Audience Kit shows that streamer-friendliness is partly a join-surface problem, not only a visual-style problem. ([Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available))
- [INFERRED] "Watchability" is therefore not one property. It is at least these four layers: clarity, suspense, participation, and broadcastability. Optimizing one does not automatically optimize the others. (same sources)

### What Must Be Protected Early If The Product Expands Later

- [INFERRED] Protect the separation between `authored round substrate` and `session wrapper`. If solo, live-room, and streamer shells all require separate content definitions, expansion gets expensive immediately. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [Kahoot how it works](https://kahoot.com/schools/how-it-works/))
- [INFERRED] Protect a reusable `reveal grammar`. If reveals are treated as ad hoc UI polish instead of part of the round contract, later watchable, async, and streamer wrappers will all feel thinner than the social fantasy requires. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] Protect role distinctions between `host`, `player`, `audience`, and later `viewer`. Jackbox demonstrates that audience/viewer affordances can become product-defining without changing the core round loop. ([Jackbox Party Pack 2 product page](https://checkout.jackboxgames.com/products/the-jackbox-party-pack-2), [Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available))
- [INFERRED] Protect frozen session definitions and replayable event/state boundaries. Without that, async challenges, reconnect, remote spectatorship, and later review/replay features all become harder. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md))
- [INFERRED] Protect answer-surface extensibility early. The audit's hierarchical-answer warning matters here because `venue -> circuit -> section -> corner` progression is one of the cleanest ways to grow depth without redefining the whole product. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))
- [INFERRED] Protect low-friction join surfaces from the start. A product that eventually wants remote private rooms and streamer participation cannot treat room code, join URL, QR, and role entry as afterthoughts. ([REQUIREMENTS](../../../REQUIREMENTS.md), [Jackbox remote play guide](https://www.jackboxgames.com/blog/how-to-play-party-pack-nine-remotely), [Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available))

## Viable Paths

### Path A: Watchable Private Game Night

- [INFERRED] Early shape: curated authored packs, host-controlled room flow, big reveal payoffs, and phone/browser controllers.
- [INFERRED] Mid shape: same room shell, but remote/hybrid hosting becomes first-class.
- [INFERRED] Later shape: audience overlays, spectator participation, and replay/review features.
- [INFERRED] If this path dominates, the real product core is `session choreography` more than `map guessing`. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [Jackbox Party Pack 2 product page](https://checkout.jackboxgames.com/products/the-jackbox-party-pack-2), [Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available))

### Path B: Authored Practice And Async Challenge Network

- [INFERRED] Early shape: the same packs can be run alone or shared as challenge links.
- [INFERRED] Mid shape: daily/weekly authored slices, personal history, lightweight comparison, and calibration loops.
- [INFERRED] Later shape: club-style leagues or repeatable expert ladders without full public-product overhead.
- [INFERRED] If this path dominates, the real product core is `frozen authored challenge objects` plus identity/history, not the live room itself. ([REQUIREMENTS](../../../REQUIREMENTS.md), [GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work), [Kahoot how it works](https://kahoot.com/schools/how-it-works/))

### Path C: F1 Party Platform

- [INFERRED] Early shape: the geography/circuit mode proves the room shell, authored reveal grammar, and host/controller contract.
- [INFERRED] Mid shape: additional F1 modes arrive that reuse those same shells.
- [HYPOTHESIS] Later shape: "F1 game night" becomes the brand, and geography is the flagship mode rather than the whole identity.
- [INFERRED] If this path dominates, the product core is `shared session shell + content tooling + role choreography`, and every new mode must be judged by how much of that substrate it reuses. ([PROJECT](../../../PROJECT.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))

### Path Relationship

- [INFERRED] These paths are not mutually exclusive. The most coherent sequencing is A first, B second, C only after A proves the social fantasy and B proves the substrate can survive outside one room. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))

## Key Tradeoffs And Hidden Assumptions

- [INFERRED] Centering the host-screen room creates stronger immediate social payoff, but it also assumes the product can earn repeat use without a solo habit loop. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] Centering solo/async too early could improve repeatability, but it risks flattening the product back toward "F1 GeoGuessr variant" instead of "expert-fan game night software." ([PROJECT](../../../PROJECT.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))
- [INFERRED] Protecting future adjacent modes is valuable, but over-weighting them too early can cause shell-first overengineering before the anchor mode feels great. ([PROJECT](../../../PROJECT.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md))
- [INFERRED] Streamer-friendliness may sound like a later marketing concern, but the hardest part is often role/join ergonomics and reveal legibility, which overlap heavily with local-room quality. ([Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [HYPOTHESIS] The project may be tempted to equate "watchable" with "TV-friendly visual design." That would be too narrow; watchability is also pacing, reveal quality, and role clarity. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))

## Disconfirming Or Tensioning Evidence

- [CONFIRMED] GeoGuessr has expanded beyond one social wrapper into both co-op and deeper singleplayer structures. That tensions any claim that the enduring center must remain a shared-screen party shell. ([GeoGuessr Bulls-Eye](https://geoguessr.zendesk.com/hc/en-us/articles/4420338264849-What-is-Bulls-Eye), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work))
- [CONFIRMED] Jackbox shows that very strong social/watchable products can stay relatively light on persistent identity and asynchronous structure. That tensions any assumption that Prix Guesser needs a fast path to accounts, ladders, or deep retention systems to be compelling. ([Jackbox Party Pack 2 product page](https://checkout.jackboxgames.com/products/the-jackbox-party-pack-2), [Jackbox remote play guide](https://www.jackboxgames.com/blog/how-to-play-party-pack-nine-remotely))
- [CONFIRMED] Kahoot shows that one content bank can support live-hosted, self-paced, and team-based play without becoming incoherent. That tensions any claim that adding async or solo later would necessarily split Prix Guesser into a different product. ([Kahoot how it works](https://kahoot.com/schools/how-it-works/))
- [CONFIRMED] GeoGuessr Bulls-Eye allows untimed co-op exploration, peer teleport, and pinging. That tensions the current repo bias toward tightly staged authored pacing and suggests that collaborative expert discussion could itself be a later watchable format. ([GeoGuessr Bulls-Eye](https://geoguessr.zendesk.com/hc/en-us/articles/4420338264849-What-is-Bulls-Eye))

## What Could Change This View

- [HYPOTHESIS] Real friend playtests could show that the social reveal loop is fun but too hard to schedule, pushing solo/async wrappers earlier than this map assumes.
- [HYPOTHESIS] Content authoring cost could prove so high that the product needs lower-ceremony repeatable wrappers sooner to justify the corpus investment.
- [HYPOTHESIS] Technical hosting friction for live rooms could prove low enough that remote-first private rooms become the actual first strong format, not couch-first play.
- [HYPOTHESIS] Streamer/community demand could appear earlier than expected, making audience/viewer ergonomics part of milestone-one thinking rather than later polish.
- [HYPOTHESIS] If adjacent F1 modes cannot honestly reuse the same authored/reveal/session shell, then the "F1 party platform" future becomes less compelling and should be treated as a separate initiative, not latent v2 scope.

## Open Questions Worth A Second Pass

1. [INFERRED] What is the smallest possible solo wrapper that strengthens the social core instead of competing with it?
2. [INFERRED] Which parts of watchability matter most to this audience: suspense, explanation, audience participation, or broadcast friendliness?
3. [INFERRED] Does streamer-friendliness here mean "good on a shared screen" or "direct audience input from Twitch/Discord viewers"?
4. [INFERRED] Which future adjacent F1 modes would actually reuse the same round/reveal/session shell, and which only sound adjacent at the fantasy level?
5. [HYPOTHESIS] Is there a distinct collaborative-coop branch, analogous to GeoGuessr Bulls-Eye, that would feel more "F1 analysts in a room" than "players competing for points"?

## Source Ledger

### Primary Internal Sources

- [PROJECT](../../../PROJECT.md)
  - Authority: current declared product posture and constraints.
  - Limit: intent, not validated play behavior.
- [ROADMAP](../../../ROADMAP.md)
  - Authority: current sequencing and near-term strategic commitments.
  - Limit: roadmap assumes one current direction and may underrepresent latent futures.
- [REQUIREMENTS](../../../REQUIREMENTS.md)
  - Authority: current requirement inventory, including later wrapper aspirations.
  - Limit: requirements encode current thinking, not proven demand.
- [continue-here](../../../phases/01-authored-round-contract/.continue-here.md)
  - Authority: direct handoff of the strategic questions that triggered this research wave.
  - Limit: interpretive synthesis from a prior session.
- [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md)
- [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md)
  - Authority: strongest existing internal analysis of futures-sensitive architectural risk.
  - Limit: audit documents, not product tests.

### Primary External Sources

- [GeoGuessr Play with Friends](https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends)
  - Authority: official help doc for social wrapper structure.
  - Limit: older help article; good for feature shape, not current strategic emphasis.
- [GeoGuessr Live Challenges](https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges)
  - Authority: official help doc for private-party competitive play.
  - Limit: older help article.
- [GeoGuessr Bulls-Eye](https://geoguessr.zendesk.com/hc/en-us/articles/4420338264849-What-is-Bulls-Eye)
  - Authority: official help doc for co-op play affordances.
  - Limit: mode description, not evidence of popularity.
- [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work)
  - Authority: official help doc for current solo shell.
  - Limit: one specific solo mode, not the full product strategy.
- [Jackbox Party Pack 2 product page](https://checkout.jackboxgames.com/products/the-jackbox-party-pack-2)
  - Authority: official product page showing the stable host-screen plus device-controller plus audience pattern.
  - Limit: older pack page, useful as a durable pattern reference rather than a current roadmap statement.
- [Jackbox remote play guide](https://www.jackboxgames.com/blog/how-to-play-party-pack-nine-remotely)
  - Authority: official explanation of remote participation framing.
  - Limit: marketing/help hybrid.
- [Jackbox Audience Kit](https://www.jackboxgames.com/blog/the-jackbox-audience-kit-twitch-extension-is-now-available)
  - Authority: official streamer/audience integration reference.
  - Limit: blog announcement, not a neutral product analysis.
- [Kahoot how it works](https://kahoot.com/schools/how-it-works/)
  - Authority: official product overview for live, self-paced, team, reporting, and sharing layers.
  - Limit: broad feature page with marketing framing.

## Bottom Line

- [INFERRED] The strongest current read is not "Prix Guesser should become X." It is "Prix Guesser can plausibly become an authored F1 substrate with multiple coherent wrappers, and the first wrapper should probably be a watchable private game-night shell."
- [INFERRED] The highest-value future-awareness move is to protect shared substrate seams early so that solo, async, streamer, and later multimode futures remain extensions instead of rewrites.
