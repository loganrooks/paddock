# Product Futures XHigh Comparison Rerun

Date: 2026-04-10

## Question Space

- [CONFIRMED] Prix Guesser's current canonical posture is still `private-only`, `authored`, `social-first`, and `geography-anchor`, while the roadmap still sequences v1 around live private rooms, phone/browser join, host-screen flow, and reveal quality before async or adjacent mode expansion. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] The most useful question is not "which single mode wins?" but "what stays invariant across plausible futures, and which futures are merely new wrappers versus genuinely different product lines?" ([PROJECT](../../../PROJECT.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md), [04-cross-lane-reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md))
- [INFERRED] The first-wave insight that this is a `shared substrate plus wrappers` story still looks directionally right, but the rerun suggests that `mode`, `session format`, `wrapper`, `stage-shape`, and `platform shell` need to be treated as separate layers or the future map becomes too tidy too fast. ([CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))
- [HYPOTHESIS] The mature-product question may not resolve to either "deep F1 GeoGuessr" or "full F1 Jackbox." It may instead resolve to a narrower but still multi-wrapper authored F1 occasion product whose first version only proves one ritualized shell. (same sources)

## Method And Sources

- [CONFIRMED] I followed the rerun charter order: orchestration brief, shared starting context, stricter second-wave standard, then the original first-wave `01-product-futures` spec. I formed an independent map before reading the original first-wave findings. ([00-ORCHESTRATION](../00-ORCHESTRATION.md), [05-second-wave-research-standards](../../../explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md), [original spec](../../2026-04-10-vision-hosting-wave/specs/01-product-futures.md))
- [CONFIRMED] Internal sources were treated as authoritative for current project intent, tensions, and sequencing, not for validated player behavior. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md))
- [CONFIRMED] External claims were grounded in official product/help pages from GeoGuessr, Jackbox, and Kahoot to verify how adjacent products actually structure live rooms, browser controllers, async challenges, audience layers, and reused content banks. ([GeoGuessr Multiplayer Mode](https://geoguessr.zendesk.com/hc/en-us/categories/360003342678-Multiplayer-Mode), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [GeoGuessr Create Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz), [GeoGuessr Duels](https://geoguessr.zendesk.com/hc/en-us/articles/4411221768465-What-are-Duels), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work), [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform), [Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play), [Kahoot Tallest Tower](https://support.kahoot.com/hc/en-us/articles/14892571933203-How-to-play-Tallest-tower))
- [CONFIRMED] I did not rely on community chatter for decisive claims in this lane because the key disputed questions were mostly about current product behavior, shell structure, and role patterns, which official sources were sufficient to establish. The main missing evidence remains Prix Guesser playtests and telemetry, not more precedent scraping. (same sources)
- [CONFIRMED] Source limits remain important: official product docs show what those products support, not which future Prix Guesser users will prefer, and not which tradeoffs are economically or operationally wise for this project. (same sources)

## Inquiry Trajectory

- [CONFIRMED] I started from the repo's explicit tension set: one authored geography anchor, one likely watchable host-screen shell, but an intentionally preserved possibility that the broader arc becomes more than one geography game. ([PROJECT](../../../PROJECT.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))
- [INFERRED] The first branch was `what is the substrate?` Candidate answers were: authored content only, judging/reveal grammar, room shell, and host/player/audience role choreography. The repo and audit material pushed toward a combined substrate rather than one of those layers alone. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [04-cross-lane-reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md))
- [INFERRED] The second branch was `which later futures still feel like the same product?` This branch widened after checking current GeoGuessr and Kahoot behavior because both show that one family can contain shells with meaningfully different pacing, rewards, and social posture. That made the simple wrapper story look incomplete. ([GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work), [Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play), [Kahoot Tallest Tower](https://support.kahoot.com/hc/en-us/articles/14892571933203-How-to-play-Tallest-tower))
- [INFERRED] The third branch was `what kinds of watchability are actually being discussed?` The repo language and precedent set pushed this away from one vague quality word toward several distinct concerns: legibility, suspense, participation, teaching value, and spectator safety. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [INFERRED] The fourth branch was `which futures are feasible in which sense?` The stricter second-wave standard made it necessary to separate technical feasibility from operational, adoption, economic, and ethical feasibility rather than letting "could build" stand in for "should treat as alive." ([05-second-wave-research-standards](../../../explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md))
- [CONFIRMED] Only after those branches were mapped did I read the original first-wave findings and compare them against the rerun. ([original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))

## Branching Paths And Dependencies

- [INFERRED] Whether `adjacent F1 modes` belong inside one product family depends less on thematic similarity and more on whether they can reuse the same answer grammar, reveal grammar, role choreography, and session shell. Theme alone is not enough. ([PROJECT](../../../PROJECT.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play))
- [INFERRED] Whether `solo/async` is a support shell or a co-equal identity depends on scheduling friction, content cadence, and whether users want between-session habit loops more than shared-screen occasions. That is partly a product question and partly an adoption question. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform))
- [INFERRED] Whether `streamer/spectator` is late polish or an early protected seam depends on role boundaries, room-code safety, spoiler control, and audience participation affordances, not just on having a prettier host screen. ([Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [INFERRED] Whether one substrate can honestly support multiple futures depends on preserving stable content identity, structured answer targets, reusable reveal logic, and event/state boundaries early. If those seams are not protected, later futures become rewrites rather than extensions. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))
- [INFERRED] The significance of `watchability` depends on wrapper context. Local couch play, remote live play, async challenge, and broadcast viewing each ask for different kinds of legibility and pacing, so a single global watchability judgment is misleading. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-))

## Findings

### The Product Space Still Looks Like A Family, But The Family Has Different Layers

- [CONFIRMED] The internal project artifacts still point to a family of futures rather than a forced binary. v1 is a live-room watchable shell; v2 requirements already mention async wrappers and adjacent modes; the exploratory notes explicitly moved toward `shared substrate plus wrappers` language. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md))
- [CONFIRMED] GeoGuessr currently presents a real product family containing competitive multiplayer, private party/quiz structures, daily challenge patterns, and a newer singleplayer shell rather than only one dominant social format. ([GeoGuessr Multiplayer Mode](https://geoguessr.zendesk.com/hc/en-us/categories/360003342678-Multiplayer-Mode), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [GeoGuessr Create Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz), [GeoGuessr Duels](https://geoguessr.zendesk.com/hc/en-us/articles/4411221768465-What-are-Duels), [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work))
- [CONFIRMED] Jackbox still exemplifies a durable host-run shared-screen product family where browser-based controllers, remote participation, and audience-specific overlays coexist without collapsing the core join ritual. ([Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [CONFIRMED] Kahoot shows that one authored content bank can support live-hosted, self-paced, and several materially distinct collaborative or team-first live shells. That is useful precisely because it shows both reuse and divergence. ([Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform), [Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play), [Kahoot Tallest Tower](https://support.kahoot.com/hc/en-us/articles/14892571933203-How-to-play-Tallest-tower))
- [INFERRED] The rerun's sharper conclusion is that `family resemblance` does not remove the need for layer distinctions. Prix Guesser likely has one growing family, but within that family some futures are best understood as `wrappers on one substrate`, some as `new stage-shapes built on shared substrate`, and some as `adjacent sibling products` that only partially reuse the substrate. (all sources above)
- [INFERRED] The safest working model is therefore: `authored F1 content + structured answer/reveal semantics + room/session choreography + role model` as the likely durable core, with future shells evaluated by how much of that core they truly reuse. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))

### The Likely First Strong Shape Is Still A Watchable Private Ritual

- [CONFIRMED] The repo still centers private expert-fan social play, host-screen legibility, mobile/browser controllers, and reveal-rich pacing before any public or persistence-heavy future. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] The first serious proof is still most plausibly `private F1 game-night software`: one host, one shared screen, a few knowledgeable players, authored rounds, explicit answer surfaces, visible lock/reveal phases, and reveals that teach as much as they score. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))
- [INFERRED] Jackbox remains the clearest precedent for the join ritual and role split, but not for the knowledge fantasy. Prix Guesser is trying to produce a more diagnostic and sport-literate reveal culture than Jackbox usually needs. ([Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [PROJECT](../../../PROJECT.md))
- [HYPOTHESIS] Remote live play still looks more like the first expansion of this ritual than the emotional center of v1 itself, unless actual friend scheduling pain proves more decisive than the current artifacts imply. ([PROJECT](../../../PROJECT.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md))

### Kinds Of Watchability

- [INFERRED] `Shared-legibility watchability` means every person can understand what phase the session is in, what the question asks, and what changed after the reveal. This is the watchability most explicitly encoded in the current roadmap and requirements. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] `Suspense watchability` means visible countdown, answer lock, leaderboard movement, and reveal cadence create anticipation rather than just information display. This matters differently in local party play than in self-paced challenge formats. ([ROADMAP](../../../ROADMAP.md), [GeoGuessr Duels](https://geoguessr.zendesk.com/hc/en-us/articles/4411221768465-What-are-Duels), [Kahoot Tallest Tower](https://support.kahoot.com/hc/en-us/articles/14892571933203-How-to-play-Tallest-tower))
- [INFERRED] `Participation watchability` means observers still feel implicated in the round, either because they are waiting on their own answer, discussing with a team, or contributing as audience/viewers. Kahoot team modes and Jackbox audience affordances show that "watching" can still be active. ([Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [INFERRED] `Diagnostic watchability` means the reveal pays off because it explains the recognition logic and deepens sport literacy, not only because it announces a winner. This appears unusually important for Prix Guesser compared with generic party trivia. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] `Broadcast watchability` means external viewers can follow the state cleanly, join when invited, and avoid accidental spoilers or room-code leakage. Jackbox's audience and remote-play guidance makes clear that streamer-friendliness is a role-and-safety problem, not only a visual-style problem. ([Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [INFERRED] The rerun sees more clearly that these watchability types can conflict. A faster suspense loop can weaken diagnostic reveals; a spectator-safe shell can constrain how much player-state is shown; an async challenge can preserve score drama while losing shared-room ritual. Optimizing "watchability" in the abstract is therefore not a serious design instruction. (same sources)

### What Must Be Protected Early If The Product Expands Later

- [INFERRED] Protect `structured authored content` with stable IDs, metadata, and explicit pack/round identity. Later challenge links, calibration loops, replay, and mode suitability all depend on knowing what content object is being reused. ([ROADMAP](../../../ROADMAP.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md))
- [INFERRED] Protect `hierarchical answer and reveal semantics`. The audit's structured answer-target warning remains the cleanest way to keep future depth expansions from turning into bespoke mode hacks. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))
- [INFERRED] Protect `role boundaries` between host, player, audience, and viewer. If those roles are blurred too early, later remote, spectator, or stream-safe shells become much harder to add coherently. ([REQUIREMENTS](../../../REQUIREMENTS.md), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [INFERRED] Protect a reusable `session shell` with explicit phase/state transitions. Wrappers can vary, but they need a stable grammar for join, prompt, submit, reveal, standings, and replay/review. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] Protect `join surfaces and lightweight identity` from the start. A future that may include remote private rooms, daily challenges, or audience viewers cannot leave room code, link, QR, nickname, and resume/rejoin semantics implicit. ([REQUIREMENTS](../../../REQUIREMENTS.md), [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform))
- [INFERRED] Protect `event and telemetry boundaries`. Even if full replay and public leaderboards stay later, the project needs room to inspect what happened at clue-step, answer, and reveal level if it wants calibration and wrapper variation without guesswork. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))

### What The Mature Product Might Be That The First Version Is Not Yet

- [INFERRED] The mature product still plausibly looks broader than one geography game, but the rerun is less comfortable calling it a neat stack of wrappers. A better current description is: `an authored F1 game-night substrate that may eventually host several distinct but related shells`. ([PROJECT](../../../PROJECT.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md), [original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))
- [INFERRED] The first version is not yet that mature product. It is much closer to a proof that one host-screen-centered ritual can feel genuinely expert, social, and replayable without flattening into generic quiz software. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md))
- [HYPOTHESIS] If the project matures successfully, geography may remain the flagship and emotional anchor without remaining the only mode family. That is a narrower and more plausible claim than saying the product is already on an inevitable march to full F1 party platform status. ([PROJECT](../../../PROJECT.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))
- [HYPOTHESIS] The mature product may eventually need a `house identity` above the geography flagship, but this emerged as a scope expansion rather than as a decision the current artifacts are ready to make. (same sources)

### Feasibility Is Not One Axis

- [CONFIRMED] `Technical feasibility`: the internal architecture direction and external precedents both support the idea that one substrate can power several wrappers if content identity, answer semantics, session state, and role boundaries are protected early. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md), [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform))
- [INFERRED] `Operational feasibility`: private watchable rooms look operationally lighter than recurring async or multimode expansion because the main burden is still content authoring and reveal quality, not ongoing programming cadence or moderation. ([PROJECT](../../../PROJECT.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md))
- [INFERRED] `Adoption feasibility`: the current audience and repo posture fit private expert-fan sessions best, but async challenge futures may be more schedulable and therefore more sustainable if real friend groups cannot convene often. That means the strongest technical path and the easiest adoption path may diverge. ([PROJECT](../../../PROJECT.md), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform))
- [INFERRED] `Economic feasibility`: private/local or selectively remote play imposes much lower ongoing burden than daily challenges, public-facing leaderboards, or a broader party platform, all of which imply sustained content operations and more persistent infrastructure. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] `Ethical and trust feasibility`: streamer/audience and public challenge futures introduce spoiler, room-code, abuse, fairness, and moderation concerns that do not dominate private couch play. These futures can remain alive without being socially or ethically cheap. ([Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))

## Gray Areas And Live Tensions

- [INFERRED] `Social ritual versus return-loop frequency` remains unresolved. The strongest emotional fantasy still looks social and shared-screen, but the easiest recurring habit may come from async challenge slices rather than scheduled game nights. ([PROJECT](../../../PROJECT.md), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform))
- [INFERRED] `Wrapper ecology versus platform overreach` remains a live tension. The substrate idea is clarifying, but Kahoot and GeoGuessr both show that a product family can drift far enough that "same family" does not mean "same experience." ([GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work), [Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play))
- [INFERRED] `Teaching reveal quality versus fast competition` remains live. The more the product leans into daily challenge, duel, or leaderboard loops, the more pressure there will be to compress reveal richness that currently looks central to Prix Guesser's identity. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [GeoGuessr Duels](https://geoguessr.zendesk.com/hc/en-us/articles/4411221768465-What-are-Duels))
- [INFERRED] `Streamer friendliness versus private-room safety` remains live. Stream growth and audience interaction are enticing, but official Jackbox guidance shows that room-code hiding, passwording, and latency choices become part of the actual product surface. ([Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [INFERRED] `Expert-fan specificity versus wider accessibility` remains live. Prix Guesser's current value is expert recognition and interpretation, but some future shells may only scale if they soften that entry barrier. The current research does not resolve how far that softening can go before the fantasy weakens. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] `One product family versus adjacent sibling products` remains live. Some F1-themed future modes may share enough substrate to belong together; others may only share theme and should not be forced into one shell for narrative convenience. ([continue-here](../../../phases/01-authored-round-contract/.continue-here.md), [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md))

## Scope Expansions

- [CONFIRMED] `Scope Expansion`: the inquiry moved from "what futures are plausible?" to "what actually counts as the same product?" because official precedent behavior showed that shared content or shared theme is not enough to settle sameness. This was pursued meaningfully. ([GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work), [Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play))
- [CONFIRMED] `Scope Expansion`: brand or house-identity questions surfaced because a geography flagship and a broader F1 game-night substrate may eventually need different naming layers. This was flagged, not deeply pursued. ([continue-here](../../../phases/01-authored-round-contract/.continue-here.md))
- [CONFIRMED] `Scope Expansion`: recurring programming and content-operations cadence surfaced because async challenge futures are not merely a UI shell; they depend on ongoing authored supply and curation rhythm. This was flagged more than deeply pursued. ([REQUIREMENTS](../../../REQUIREMENTS.md), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform))
- [CONFIRMED] `Scope Expansion`: spectator governance surfaced because streamer-facing futures imply room-code safety, spoiler boundaries, and moderation posture. This was partially pursued because it materially affects the "watchability" concept. ([Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))

## Rival Models Still Alive

### Model A: Private F1 Game-Night Software

- [INFERRED] This model keeps the emotional center in curated shared-screen sessions with browser/phone controllers, high-value reveals, and replayable expert-fan social ritual. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md))
- [INFERRED] `Technical feasibility` looks strong, `operational feasibility` looks decent for a private project, `adoption feasibility` looks strongest for the current audience, and `economic/ethical feasibility` looks simplest because the product remains mostly private and occasion-based. (same sources)
- [INFERRED] Its weakness is that it may underperform on repeat frequency if scheduling turns out to be the main obstacle. ([PROJECT](../../../PROJECT.md))

### Model B: Authored Challenge Network

- [INFERRED] This model treats frozen authored rounds or pack slices as the center of gravity, with local or live-room play remaining important but not singular. Daily challenge, friend challenge links, and lightweight identity/history become more central. ([REQUIREMENTS](../../../REQUIREMENTS.md), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform))
- [INFERRED] `Technical feasibility` also looks plausible, but `operational` and `economic feasibility` are worse because recurring content rhythm and challenge administration become first-class burdens. `Adoption feasibility` may be better than Model A if players like the idea but cannot convene often. (same sources)
- [INFERRED] Its weakness is identity drift: the product may become more schedulable but less distinctively social or reveal-rich. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))

### Model C: F1 Party Platform

- [INFERRED] This model treats the geography anchor as the first proof of a broader host/controller/reveal substrate for several F1 game families. ([PROJECT](../../../PROJECT.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))
- [INFERRED] `Technical feasibility` is only strong if early seams are protected well; `operational` and `economic feasibility` are weaker because content operations, tool breadth, and design coherence all get harder; `adoption feasibility` is uncertain because the current audience is here for the geography/circuit fantasy first. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))
- [INFERRED] Its strength is long-arc optionality; its weakness is premature platform ambition. (same sources)

### Model D: Creator/Spectator Show Layer

- [HYPOTHESIS] This looks less like a standalone destiny and more like a cross-cutting branch that can attach to Model A or C if audience participation, streaming, or spectator-safe reveals become important. ([Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [INFERRED] `Technical feasibility` is plausible, but `ethical/trust feasibility` is weakest here because spoiler control, room safety, and harassment/moderation issues arrive sooner. (same sources)
- [INFERRED] This model should stay alive as a branch, but the rerun does not support treating it as inevitable or near-term. (same sources)

## Practical Implications

### Thinking Implications

- [INFERRED] Future discussion should stop using `mode` as a catch-all. The more useful vocabulary is `substrate`, `wrapper`, `stage-shape`, `role`, and `watchability type`. ([04-cross-lane-reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md))
- [INFERRED] New ideas should be tested with two questions: `what does this reuse?` and `what emotional center does this privilege?` That is more clarifying than asking only whether something is "in scope for the platform." (all sources above)

### Design Implications

- [INFERRED] A future UI/design brief should treat watchability as a matrix across local shared-screen, remote live, async challenge, and spectator contexts rather than as one aesthetic directive. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] Reveal grammar should be treated as product core, not as presentational garnish, because it is where Prix Guesser most strongly differentiates from generic quiz or map-guess products. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] Streamer or audience futures imply explicit spoiler and room-safety design, not just nicer motion and contrast. ([Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))

### Implementation Implications

- [INFERRED] The highest-leverage protected seams still look like: structured content identity, hierarchical answer targets, reusable reveal semantics, explicit session phases, role-aware join flows, and event-level telemetry. ([SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md), [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md))
- [INFERRED] If adjacent modes are explored later, each should be forced to declare which substrate layers it reuses and which it wants to replace. That makes "same family or sibling product?" an inspectable question rather than a vibe check. (same sources)

### Measurement Or Experiment Implications

- [HYPOTHESIS] The next high-value experiments are not broad roadmap decisions but small contrastive tests: one local watchable session, one remote/hybrid session, and one minimal async challenge shell using the same authored substrate. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [HYPOTHESIS] Measurements that would materially change this map include: scheduling friction, replay desire after one session, reveal discussion quality, willingness to replay old packs, solo completion rates, and whether players ask for more session nights or more between-session challenge content. (same sources)
- [HYPOTHESIS] If an adjacent non-geography mode is ever prototyped, the critical measure is not only whether it is fun, but whether it honestly reuses the geography-mode substrate or quietly demands new tools, new reveal logic, and new pacing grammar. ([continue-here](../../../phases/01-authored-round-contract/.continue-here.md))

## Comparison With Original First-Wave Pass

### What The Original Pass Got Right

- [CONFIRMED] The original pass was right that the product space is not a binary and that the likely first strong proof is still a watchable private game-night shell rather than a solo-first web quiz. ([original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))
- [CONFIRMED] It was also right to decompose watchability, preserve at least three long-arc paths, and identify early seams like reveal grammar, answer extensibility, and join flow as the most important things to protect. (same source)
- [CONFIRMED] Its conclusion that solo/async currently look more like extensions than the emotional center still holds up under the rerun. (same source)

### What This Rerun Sees More Clearly

- [INFERRED] The rerun sees more clearly that `shared substrate plus wrappers` is necessary but not sufficient language. It needs a sharper distinction between wrappers, stage-shapes, and sibling products because current precedents contain meaningful shell drift inside one product family. ([GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work), [Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play), [original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))
- [INFERRED] The rerun is more explicit that feasibility splits across technical, operational, adoption, economic, and ethical axes. The original pass mostly implied those differences; this one treats them as first-class. ([05-second-wave-research-standards](../../../explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md), [original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))
- [INFERRED] The rerun also sees more clearly that some future adjacent modes may only share theme and not enough underlying grammar to belong inside one product without distortion. The original pass acknowledged that possibility, but the rerun treats it as a central live tension rather than a side caveat. (same sources)

### Where This Rerun Disagrees Or Reframes

- [INFERRED] The original pass's `Path A -> Path B -> Path C` sequencing still looks plausible, but now feels slightly too neat. If scheduling friction is severe, Model B could become strategically important earlier than that ordering suggests. ([original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md), [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge), [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform))
- [INFERRED] The original pass treated streamer/spectator mostly as another wrapper. The rerun reframes it as a cross-cutting branch that may attach to several futures but introduces distinct trust and safety constraints. ([original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md), [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-), [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch))
- [INFERRED] The original pass used the wrapper ecology language confidently. The rerun keeps that language but is less willing to assume every future F1 shell is "still the same product" just because it sounds adjacent. ([original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))

### Why The Difference Seems To Exist

- [INFERRED] Part of the difference comes from the stricter second-wave standard, which explicitly asked for inquiry trajectory, scope expansion, rival models, and feasibility splits rather than a cleaner map with a bottom line. ([05-second-wave-research-standards](../../../explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md))
- [INFERRED] Part of it also comes from changed framing rather than pure reasoning depth. Once the rerun took seriously the possibility that "same family" and "same product" are not interchangeable, some previously neat relationships naturally became more conditional. (same sources)
- [INFERRED] The original pass still looks strong. The rerun is more a sharpening and de-neatening pass than a reversal. ([original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))

## What Would Change This View

- [HYPOTHESIS] Repeated friend playtests could show that the local watchable ritual is fun but too hard to convene, which would move async challenge or lightweight solo shells up the priority stack.
- [HYPOTHESIS] Conversely, playtests could show that reveal-rich social sessions create unusually strong replay desire, reducing the need for early challenge-network expansion.
- [HYPOTHESIS] A credible adjacent non-geography prototype could prove that more of the substrate is reusable than this rerun currently assumes.
- [HYPOTHESIS] Strong early streamer or community demand could make spectator-safe role boundaries and broadcast ergonomics more central than this map currently treats them.
- [HYPOTHESIS] If content authoring cost proves worse than expected, several currently alive futures may become operationally much less plausible regardless of technical elegance.

## Open Questions Worth A Further Pass

1. [INFERRED] What is the smallest async or solo shell that strengthens the social ritual instead of competing with it?
2. [INFERRED] Which one or two candidate adjacent F1 modes reuse enough answer/reveal/session grammar to count as genuine substrate extensions?
3. [INFERRED] What does a spectator role for this product actually want: passive viewing, spoiler-safe co-guessing, audience voting, or something else?
4. [INFERRED] Is there one reveal grammar that can survive across local, async, and adjacent modes, or will there need to be a family of reveal grammars?
5. [HYPOTHESIS] Does the mature product eventually need a house identity above the geography flagship, and if so, when does that become worth naming explicitly?
6. [HYPOTHESIS] Which measurements most cleanly distinguish a strong social ritual from one-time novelty: replay demand, discussion quality, scheduling repeatability, or something else?

## Source Ledger

### Primary Internal Sources

- [PROJECT](../../../PROJECT.md)
  - Authority: current declared product identity, value, constraints, and open questions.
  - Limit: intent only, not validated behavior.
- [ROADMAP](../../../ROADMAP.md)
  - Authority: current sequence of what the project plans to prove first.
  - Limit: narrow near-term commitment, not proof of best long-arc ordering.
- [REQUIREMENTS](../../../REQUIREMENTS.md)
  - Authority: current explicit v1/v2 requirement map.
  - Limit: carries current framing biases.
- [continue-here](../../../phases/01-authored-round-contract/.continue-here.md)
  - Authority: strongest direct record of the strategic questions that triggered this exploration.
  - Limit: session synthesis, not canonical product contract.
- [SYNTHESIS](../../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md)
- [CONVERGENCE](../../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md)
  - Authority: strongest current internal analysis of futures-sensitive architectural risk.
  - Limit: audit outputs, not play evidence.
- [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md)
- [04-cross-lane-reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md)
- [05-second-wave-research-standards](../../../explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md)
  - Authority: governing standard and current synthesis posture for this rerun.
  - Limit: methodological guidance, not product evidence.
- [original findings](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md)
  - Authority: direct comparison target for this rerun.
  - Limit: first-wave framing was somewhat tidier and less explicit about gray areas.

### Primary External Sources

- [GeoGuessr Multiplayer Mode](https://geoguessr.zendesk.com/hc/en-us/categories/360003342678-Multiplayer-Mode)
  - Authority: official category view showing multiplayer, party, and quiz structures inside one family.
  - Limit: category structure, not analysis of relative importance.
- [GeoGuessr Daily Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge)
  - Authority: official description of a recurring challenge shell.
  - Limit: narrow mode description only.
- [GeoGuessr Create Challenge](https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz)
  - Authority: official description of customizable challenge creation and public leaderboard options.
  - Limit: feature-level, not strategic.
- [GeoGuessr Duels](https://geoguessr.zendesk.com/hc/en-us/articles/4411221768465-What-are-Duels)
  - Authority: official description of competitive synchronous shell and timer/health structure.
  - Limit: mode rules only.
- [GeoGuessr Singleplayer](https://geoguessr.zendesk.com/hc/en-us/articles/20716960093329-How-does-the-new-Singleplayer-game-work)
  - Authority: official description of the newer solo shell.
  - Limit: one current solo format, not the whole product strategy.
- [Jackbox Join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game)
  - Authority: official controller/join ritual and device requirements.
  - Limit: narrow support article.
- [Jackbox Remote Play](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-)
  - Authority: official remote-play guidance including streaming, room-code handling, and latency considerations.
  - Limit: official help guidance, not neutral research.
- [Jackbox Audience Kit](https://support.jackboxgames.com/hc/en-us/articles/15794775761047-How-do-I-use-the-Audience-Kit-extension-for-Twitch)
  - Authority: official spectator/audience participation extension reference.
  - Limit: one particular integration path, not all streamer possibilities.
- [Kahoot Assign](https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform)
  - Authority: official self-paced assignment/challenge flow.
  - Limit: one wrapper, not the whole platform.
- [Kahoot Lost Pyramid](https://support.kahoot.com/hc/en-us/articles/20642557926035-The-Lost-Pyramid-Kahoot-game-mode-how-to-play)
  - Authority: official example of a discussion-first collaborative live shell built on existing kahoot content.
  - Limit: one specific game mode.
- [Kahoot Tallest Tower](https://support.kahoot.com/hc/en-us/articles/14892571933203-How-to-play-Tallest-tower)
  - Authority: official example of a team-first live shell with different pacing and host-screen behavior.
  - Limit: one specific game mode.

### Qualified Secondary Or Practitioner Material

- [CONFIRMED] No non-official external source materially changed the conclusions in this lane.
- [INFERRED] That is acceptable here because the disputed questions were primarily about product/menu shape, role patterns, and wrapper structure, which official sources could substantiate directly.
- [INFERRED] The more pressing missing evidence is Prix Guesser's own play behavior, not additional third-party commentary.
