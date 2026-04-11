# Feature Landscape: Prix Guesser

**Domain:** Private browser-based F1 geography / party game  
**Researched:** 2026-04-08  
**Overall confidence:** MEDIUM-HIGH

## Refresh Note (2026-04-11)

Read this file as product-shape guidance, not as the active phase list.

Later research and the refreshed canon kept the live private-room wrapper first, but made three additions explicit:

- browser-first operator launch and join flow are v1 concerns, not backstage implementation details
- TV-distance host readability and room-code/link/QR join are first-class requirements, not polish
- public discovery, async challenge, and streamer-facing surfaces remain later wrappers rather than rejected futures

## Executive Take

Products adjacent to Prix Guesser tend to cluster into three families:

1. Geography guessing products: private challenges, custom maps/quizzes, timer and movement restrictions, score/reveal loops, daily/streak retention layers.
2. Browser party games: host-controlled lobbies, join codes or links, no-account guest entry, shared-screen play, team modes, lock/kick/rejoin controls.
3. F1 fan puzzle products: compact daily modes, niche category depth, multiple sub-games, mobile-friendly play, educational or archival framing.

Prix Guesser should inherit the first two families aggressively and the third selectively. The v1 product is not "generic GeoGuessr but F1-themed." Its table stakes are the pieces that make private expert-fan play actually work: authored F1 rounds, private room flow, watchable reveals, and low-friction phone/browser participation. Daily retention loops, public competitive systems, and a broad buffet of side modes are common in the broader market, but they are not core to this project's first proof.

The anchor-mode bar is higher than a normal quiz game. A generic map pin alone is not enough. The round has to encode circuit identity, clue sequencing, reveal explanation, and at least one answer surface that feels native to F1 fandom rather than generic world geography.

## What Products In This Space Typically Have

| Common feature in the market | Evidence in sources | Prix Guesser decision |
|---|---|---|
| Private lobby / play-with-friends flow | GeoGuessr private lobbies and live challenges; Kahoot live host flow | **v1 table stake** |
| Join by link, PIN, or QR; low-friction guest entry | GeoGuessr shared links; Kahoot PIN/link/QR and no-account joining | **v1 table stake** |
| Shared-screen plus personal-device participation | Kahoot host-screen + participant-device pattern | **v1 table stake** |
| Scoreboard and reveal between rounds | GeoGuessr live challenges; Geo Locator results screen | **v1 table stake** |
| Timer and round-rule controls | GeoGuessr quiz setup includes round time and move/pan/zoom rules | **v1 table stake** |
| Custom maps / custom quizzes / authored content | GeoGuessr map maker + quiz builder; GeoHub custom maps/challenges | **internal-only v1 table stake**, not public UGC |
| Daily challenge / recurring puzzle loop | GeoHub daily challenge; Formudle/F1DLE daily F1 puzzles | **not v1 table stake** |
| Multiple game modes around one content base | GeoGuessr quiz/maps/party; Formudle multi-mode hub | **differentiator later**, not launch breadth |
| Team mode / couch-friendly group play | Kahoot team mode | **differentiator**, likely early post-v1 |
| Public ladders / mass multiplayer / anti-cheat | Common in large geography products | **anti-feature for now** |

## Table Stakes

These are the features Prix Guesser should treat as required for a credible v1.

| Feature cluster | Scope | Why it matters specifically here | Complexity | Dependencies |
|---|---|---|---|---|
| Authored F1 round packs with layered clue ladders | Anchor v1 | This project lives or dies on "why a real fan could know this." A thin `lat/lng + pin` model will not deliver the circuit-recognition fantasy described in project discovery. | High | Round schema, content authoring workflow, media storage, reveal UI |
| Circuit-aware answer surfaces at least at `circuit` and `venue` level | Anchor v1 | A pure distance guess makes the product feel generic. Prix Guesser needs answer handling that matches how fans actually recognize places. | High | Answer taxonomy, scoring model, controlled vocab/search UI |
| Private room flow with host control | Shell v1 | The project posture is private-only friend play, not solo-first mass market play. Easy room creation, start flow, rematch, and between-round control are foundational. | High | Room/session state, host authority, guest identity, reconnect behavior |
| Low-friction join on phones and browsers | Shell v1 | Host-screen-friendly play only works if guests can join quickly from whatever device they already have. This matters more here than account depth or long-term profiles. | Medium | Responsive UI, join link/code/QR, nickname flow |
| Round pacing controls: timer, clue cadence, and exploration restrictions | Anchor v1 | F1 venue coverage is uneven and the difficulty target is expert-biased. Prix needs per-pack or per-round controls over time pressure and how much the player can inspect. | Medium | Timer system, clue scheduler, media-view rules |
| Results and reveal explanation after every round | Anchor v1 | Watchability is a core thesis. The reveal is where the game pays off socially and teaches why the clue was identifiable to expert fans. | Medium | Scoring, reveal content, room flow transitions |
| Curated starter content library with themed packs | Anchor v1 | Unlike a general quiz platform, this product cannot hide behind infinite generic question supply. It needs a deliberately small but high-quality pack set that proves the fantasy. | High | Content schema, tagging, pack metadata, editorial review |
| Lightweight scoreboard and session summary | Shell v1 | Friend-group replay value depends on clear round-by-round feedback, bragging rights, and a clean "play again / swap pack" loop. | Medium | Score model, room state, end-of-session UI |

### Notes on table stakes

- "Authored content" is a product feature, not only a content-operations concern. In this project, authored reveal quality is part of the gameplay.
- "Mobile-friendly" should mean guests can comfortably join and answer from phones. It does not require a separate native-app posture.
- The v1 starter set should bias toward circuits and venue contexts with reliable recognition value, not exhaustive calendar coverage.

## Differentiators

These are features that can make Prix Guesser stand out, but they should sit on top of the table-stakes substrate rather than replace it.

| Feature cluster | Scope | Why it is valuable for Prix Guesser | Complexity | Dependencies |
|---|---|---|---|---|
| `circuit + corner` or exact section answers | Anchor-plus | This is the cleanest way to make the game feel expert-fan and F1-native instead of geography-skinned. It rewards real circuit literacy. | High | Fine-grained circuit taxonomy, section metadata, richer scoring and answer UI |
| Mixed-media clue ladders: track crops, map snippets, text, atmosphere, era cues | Anchor-plus | Circuit recognition is not always best served by Street View alone. Mixed media reduces coverage risk and better matches how fans remember venues. | High | Media ingestion, per-clue rendering, editorial tooling |
| Rich reveal cards that explain the identification logic | Anchor-plus | Basic reveals are table stakes; rich reveals that unpack corner geometry, era changes, or event context make the game feel authored and collectible. | Medium | Authoring depth, reveal templates, optional archival media |
| Expert difficulty lanes and themed packs by era/weekend texture | Anchor-plus | The audience is knowledgeable long-time fans. Strong difficulty curation can be a real selling point instead of a niche tax. | Medium | Tagging, pack metadata, clue difficulty calibration |
| Team structures for couch and hybrid play | Party expansion | Formats like partners, captains, or expert-carries-one-team-member fit the friend-group use case better than anonymous free-for-all play. | High | Team scoring, team join flow, UI for shared answers |
| Adjacent micro-modes built on the same content substrate | Expansion | Circuit silhouettes, weekend-texture rounds, or history-and-place rounds can turn the product into a broader F1 party night without throwing away the anchor. | Medium | Shared taxonomy, modular scoring, mode framework |
| Spectator and audience participation hooks | Expansion | Strong for host-screen watchability and larger friend groups, but only after the core round loop is solid. | Medium | Room roles, lightweight audience input, pacing design |

### Best differentiator for early roadmap shaping

If only one differentiator is carried close to v1, it should be **finer-grained F1 answer surfaces** rather than "more modes." Exact section, corner, or composite answers reinforce the product fantasy more directly than a broad side-mode catalog.

## Anti-Features

These are common or tempting features that Prix Guesser should deliberately not treat as early requirements.

| Anti-feature | Why to avoid it now | Do instead |
|---|---|---|
| Public matchmaking, ranked ladders, and anti-cheat-heavy competition | Misaligned with private-only posture and expensive in both engineering and moderation complexity. | Build robust private rooms first. |
| Broad public UGC publishing and map marketplace | Geography products often expose public map creation, but Prix needs curated quality before scale. Public UGC would dilute the expert-fan bar. | Support internal authoring and maybe private pack import later. |
| Daily challenge / streak retention as a primary roadmap driver | This is common in geography and F1 puzzle products, but it optimizes for habit loops instead of proving the social anchor mode. | Keep the first roadmap centered on private sessions and replayable curated packs. |
| Unrestricted Street View free-roam as the default experience | Circuit coverage is uneven, API cost can spike, and free-roam can make rounds less authored and less watchable. | Use controlled clue ladders and selective exploration rules. |
| Generic distance-only scoring as the main identity | It collapses the game into a thin geography clone and underuses F1-specific knowledge. | Score around correctness, specificity, speed, or confidence where appropriate. |
| Launching with many equal-weight party modes | Discovery already flagged the risk of becoming a pile of unrelated F1 trivia. | Ship one clear geography/circuit anchor, then add adjacent modes on the same substrate. |
| Accounts, cosmetics, progression economies, or collection systems | These are common in larger consumer games but irrelevant to the project's first proof of value. | Use guest nicknames, lightweight session history, and strong reveals. |
| AI-generated or fully procedural round creation | The project requirement explicitly favors authored quality first. Procedural output would likely flatten the expert-fan texture. | Use curated hand-authored rounds and packs. |
| In-app voice/video social layer | Browser party products work fine with external voice or shared-room play. This would add complexity without strengthening the core fantasy. | Assume Discord, couch play, or screen share externally. |

## Feature Dependencies

```text
Round schema + answer taxonomy
  -> curated pack authoring
  -> clue ladder rendering
  -> reveal explanations

Round schema + scoring model
  -> leaderboard
  -> session summary
  -> team play later

Room/session authority
  -> private lobby
  -> timers and lock-in
  -> rematch/rejoin
  -> spectator and audience roles later

Shared taxonomy + media model
  -> exact corner answers
  -> themed packs by era/weekend texture
  -> adjacent F1 mini-modes later
```

## MVP Recommendation

Prioritize:

1. Authored private-room anchor mode with `circuit` or `venue` answers, layered clues, and reveal explanations.
2. Fast join flow for guests on phones and browsers, with host-controlled round pacing.
3. A small curated starter pack set built around high-recognition circuits and venue contexts.
4. Scoreboard, rematch, and pack-swap flow that makes a friend group want to run another room immediately.

Defer:

- Daily challenge and streak systems.
- Public community content.
- Large team/spectator systems.
- Adjacent non-geography party modes until the shared authored-content substrate is proven.

## Why This Split Fits Prix Guesser

The project's strongest early promise is not breadth. It is that a knowledgeable F1 fan can look at a clue, argue about what corner or venue they are seeing, lock in an answer on a phone, and then get a satisfying reveal that validates or sharpens their sport-specific intuition. Features that strengthen that loop are table stakes. Features that broaden retention or market scale without strengthening that loop should wait.

## Sources

### High-confidence

- GeoGuessr, "What are Live Challenges?" https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges
- GeoGuessr, "How do I set up a Private Lobby?" https://geoguessr.zendesk.com/hc/en-us/articles/4413903235729-How-do-I-set-up-a-Private-Lobby
- GeoGuessr, "How do I setup a quiz?" https://geoguessr.zendesk.com/hc/en-us/articles/5114923799057-How-do-I-setup-a-quiz
- GeoGuessr, "How do I create a Map?" https://geoguessr.zendesk.com/hc/en-us/articles/360017720578-How-do-I-create-a-Map
- Kahoot!, "How to join a Kahoot! game" https://support.kahoot.com/hc/en-us/articles/360039890713-Kahoot-join-How-to-join-a-Kahoot-game
- Kahoot!, "How to host a live kahoot" https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot
- Kahoot!, "Live game settings" https://support.kahoot.com/hc/en-us/articles/115016055107-Live-game-settings
- benlikescode/geohub README https://github.com/benlikescode/geohub
- GeoGuess/GeoGuess README https://github.com/GeoGuess/GeoGuess
- RasterCrow/Geo-Locator README https://github.com/RasterCrow/Geo-Locator
- xchau/react-geofindr README https://github.com/xchau/react-geofindr

### Medium-confidence

- Formudle homepage https://formudle.com/
- F1DLE homepage https://f1dle.com/
- formula1.plus games hub https://formula1.plus/games/

### Project-local context

- `/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md`
- `/home/rookslog/workspace/projects/prix-guesser/discovery/14-gsd-seed.md`
- `/home/rookslog/workspace/projects/prix-guesser/discovery/04-modes.md`
- `/home/rookslog/workspace/projects/prix-guesser/discovery/06-open-questions.md`
- `/home/rookslog/workspace/projects/prix-guesser/discovery/08-open-source-comparables.md`
