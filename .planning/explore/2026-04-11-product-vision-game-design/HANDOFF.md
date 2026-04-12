---
date: 2026-04-11
handoff_for: product vision and game design exploration
status: fresh — no exploration has started yet; this is a handoff TO the exploration, not a checkpoint OF one
triggering_session: Phase 01 prep quality & scope audit (Claude Opus 4.6, claude-code)
triggering_event: "User's product vision expanded mid-audit after BoxBoxd research revealed a commercializing multi-mode F1 fan game platform. User wants to deeply explore game modes, engagement patterns, platform maturity vision, and game-design dimensions before continuing the paused audit and Phase 01 planning."
exploration_directory: .planning/explore/2026-04-11-product-vision-game-design/
---

# Product Vision & Game Design Exploration — Session Handoff

> **This file is the entry point for a new session.** Read this first. It contains everything needed to start the exploration without re-reading the triggering conversation. The exploration has NOT started yet — this handoff sets the table.

---

## START HERE — Onboarding for the Exploration Session

If you are a Claude session picking up this exploration fresh:

1. **Read this handoff in full first.** It is the navigational entry point and contains all the context from the triggering session.
2. **Read `.planning/PROJECT.md`** (192 lines) — what the project is, core value, requirements, tensions.
3. **Read `.planning/LONG-ARC.md`** (154 lines) — the milestone arc, mature product hypothesis, transition doctrine. Pay particular attention to the "Mature Product Hypothesis" section — it already frames the substrate-plus-wrappers architecture that this exploration pushes further.
4. **Skim `.planning/research/2026-04-11-f1-fan-project-legal-landscape/01-boxboxd-deep-read.md`** (~397 lines) — BoxBoxd's 9 game modes, product shape, history, legal posture, and the differentiation surface. This is the concrete competitive reference that triggered the exploration.
5. **Skim `.planning/research/2026-04-11-f1-fan-project-legal-landscape/06-synthesis.md`** (~649 lines) — the legal/competitive landscape synthesis. Gives the broader context of F1 fan projects, commercial viability, and how other IP-heavy domains treat fan projects.
6. **Then start the exploration.** Begin at the "Exploration Starting Questions" section below and let the conversation go wherever it leads.

**Important**: this exploration is intentionally unconstrained. The "Aims From the Triggering Session" section at the bottom names what the triggering session hopes this exploration will feed into — read it for awareness, but do NOT treat those aims as constraints or scope boundaries on the brainstorming. The user explicitly asked for these aims to be visible without tainting the breadth and quality of the exploration.

---

## The Project (one paragraph)

**Prix Guesser** is an unofficial F1 fan game project built around the fantasy of "GeoGuessr for Formula 1 places." The anchor mode is authored geography-and-circuit rounds where knowledgeable F1 fans identify circuits and venues, react to reveals, and replay because the round design and reveal grammar feel authored and sport-specific. The current product posture is private-only, friends-on-couch / private-remote / hybrid game nights, browser-first guests, host-screen watchability. The three-milestone long arc is M1 "Game Night Works" → M2 "Play Anytime Anywhere" → M3 "F1 Party Platform," with only M1 on the active execution spine. The project is pre-code; Phase 01 (Authored Round Contract) has not yet started execution.

---

## What Triggered This Exploration

### The triggering session's arc (condensed)

The triggering session was a Phase 01 prep quality & scope audit investigating whether prix-guesser's preparatory work justifies proceeding to Phase 01 planning. During the audit, a research program (B8) was dispatched to investigate the F1 fan project legal and competitive landscape. The research discovered:

1. **BoxBoxd (boxboxd.fun)** is a multi-mode F1 fan game platform with 9 game modes, including F1 versions of NYT Connections, Wordle, Contexto, Elo ranking, and Guess Who. It has a free tier AND a paid tier. It carries a disclaimer ("independent fan platform, not associated with any racing organization") and has operated commercially since 2024 without F1 enforcement. A single developer (Shaina Salmi) built it.

2. **No GeoGuessr-style mode exists on BoxBoxd.** No geography, no location-based play, no spatial/image-recognition mechanic. Prix-guesser's anchor mode occupies entirely unoccupied product space within BoxBoxd's landscape.

3. **Zero F1 fan game projects have faced enforcement.** The modal posture is: F1 wordmarks in brand name, no disclaimer, no monetization, no named operator — all live and untouched. The only documented F1 enforcement (August 2024) targeted monetized social-media creators, not game products.

4. **Cross-domain evidence (Nintendo, Marvel, Star Wars, sports leagues)**: commercial competition with an official product is the strongest enforcement trigger, not monetization level. Small-scale donation funding is not documented as a standalone enforcement trigger anywhere.

### The vision shift these findings triggered

The user's product vision expanded in real-time during the triggering session:

- **Before**: private-only, friends-on-couch, no monetization, cautious legal posture
- **After**: gradual commercialization path (private free → donations → paid tiers as modes and demand grow), BoxBoxd validates this approach empirically, "private-only" reframed from legal requirement to development-stage choice

The user explicitly said: *"once we get enough demand, we can slowly commercialize it more, as we add more gamemodes, etc. offer something genuinely worth paying $3 a month."*

And: *"I wonder if we should brainstorm other games, gamemodes etc. that we haven't thought of in our future orientation that might affect our approach, the way we roadmap plan etc. or not even just the gamemodes but the different game experiences we want to offer (local multiplayer, online synchronous and asynchronous game modes). And while we can do X but for F1, I wonder if we can think of more creative game modes."*

And: *"have we seriously brainstormed about what a mature product would look like? A mature product that would enable us with relative ease to keep perhaps developing, adding content, keep people coming back etc."*

### The game-design dimension framework that emerged

The triggering conversation surfaced a framework for thinking about game-experience dimensions that the authored-round contract (Phase 01) should make first-class:

| Dimension | What it means | Why it matters for the substrate |
|-----------|--------------|--------------------------------|
| **Player roles** | Symmetric (everyone sees everything) vs asymmetric (clue-giver sees answer, guessers don't) vs team-based vs judge-based | If the contract assumes symmetric info, asymmetric party games (Codenames/Taboo/Jackbox model) can't use it |
| **Reveal grammar** | How the answer is revealed — progressive clue ladder, dramatic pause, social comparison (show all guesses then drop answer), narrative (story about the place) | The reveal is the emotional peak; different modes need different reveal shapes |
| **Answer input modality** | Text entry, multiple choice, map click, drag-to-order, drag-to-group, slider/spectrum, drawing, voice | If the contract assumes "answer = text string," richer input modes require refactoring |
| **Session arc** | How rounds compose into a game night — warmup/escalation/peak/cooldown, difficulty curves, scoring climax | A flat sequence of rounds is a quiz; a designed arc is a game night |
| **Spectacle assets** | What the host screen shows — hero images, reveal animations, score tickers, narration cues | The host screen is the "broadcast" — it needs spectacle-quality content, not just quiz UI |

The triggering conversation concluded that Phase 01 should make each dimension **explicit in the contract schema** (as a discriminated union / tagged type with a `type` field), implement ONE value per dimension in M1, and leave the dimension open for future modes to add new values. This is the "open for extension, closed for modification" principle applied to a game-content contract.

**But the user pushed further**: beyond individual dimensions, they want to think about the platform-level experience — party modes, social/community aspects, progression systems, retention mechanics, what makes people come back, what a mature product enables. The dimensions table is a starting framework, not the scope of the exploration.

---

## Exploration Starting Questions

These are the threads the user wants to pull. They are starting points, not a closed scope. Follow the conversation wherever it leads.

### Thread 1 — Game Modes and Game Experiences

The "X but for F1" pattern (taking existing game shapes and applying them to F1 content) is one axis of mode generation. BoxBoxd has done this with Wordle, Connections, Contexto, Elo ranking, and Guess Who. But there might be more creative, original modes that don't map to an existing game:

- What game modes would be uniquely compelling for F1 content that don't exist as general-purpose games?
- What about the spatial/geographic nature of F1 (circuits as places, the global calendar, venue aesthetics) enables game experiences that text-based trivia can't?
- What about the temporal nature of F1 (eras, rule changes, driver careers, team histories, technological evolution) enables game experiences?
- What about the social/dramatic nature of F1 (rivalries, team dynamics, race narratives, controversy) enables game experiences?
- What party-game mechanics from the physical game world (board games, card games, party games) could translate to an F1 digital context?

### Thread 2 — Multiplayer Shapes and Social Experiences

Three multiplayer shapes exist (local party, online synchronous, online asynchronous), and they create fundamentally different social textures:

- **Local party** (the M1 anchor): friends on the same couch, host screen as shared spectacle, immediate social reaction. What game designs are ONLY possible locally?
- **Online synchronous**: friends in different locations playing at the same time. What changes when you can't see each other's faces? What compensates for the lost physical co-presence?
- **Online asynchronous**: daily challenges, leaderboards, "play at your own pace and compare." This is BoxBoxd's primary shape. What are its strengths and limits? What community dynamics does it create?
- **Hybrid**: some players local, some remote. The hardest technical shape but potentially the most socially rich. What does hybrid play look like for an F1 quiz game?
- **What social experiences go BEYOND the game session?** Friend lists, group histories ("remember when..."), season-long competitions, league tables, F1 calendar-tied events (play a Silverstone pack on Silverstone weekend)?

### Thread 3 — Platform Maturity Vision

What does a mature prix-guesser platform look like — one that's worth $3/month and keeps people coming back?

- What is the content flywheel? (How does new content get created, curated, and refreshed? Is there a community authoring path? An editorial calendar tied to the F1 season?)
- What is the retention loop? (Streaks? Seasonal progression? Collection mechanics — "you've identified 45 of 73 circuits"? Achievement badges? Social competition?)
- What is the monetization architecture? (Free tier vs paid: what's free, what's premium? Are premium modes the differentiator, or premium content, or premium social features? Is it subscription or one-time? Could there be a season pass tied to the F1 calendar?)
- What about streamer/spectator integration? (Could someone stream a prix-guesser game night? What would make it watchable for non-players? Is this a growth channel?)
- What about community features beyond gameplay? (Discussion, predictions, opinions, collections, profiles, social sharing?)

### Thread 4 — The Substrate Question (for awareness, not as a constraint)

All of the above feeds back into: what does the authored-round contract need to support? The game-design dimensions table from the triggering conversation is one framework. But the exploration might surface dimensions that table doesn't cover, or might reframe the table entirely.

The substrate question is: **what are the axes of variation across all the game experiences we might want to offer, and which ones should be first-class in the contract?**

This is NOT asking the exploration to produce a final contract schema. It IS asking the exploration to produce a rich understanding of the experience space that the contract must eventually accommodate.

### Thread 5 — Architectural Foreclosure (the audit's deeper question)

The triggering session's final insight before the handoff: the current project setup (canon, LONG-ARC.md, roadmap, vision-alignment initiative, Phase 01 framing) may **silently foreclose** viable future directions. The audit was designed to ask "does the narrow initiative justify proceeding?" but the deeper question is "does the current architecture have structural blind spots that would prevent us from reaching a mature product, even if we execute perfectly within the current framing?"

This thread asks the exploration to specifically check:

- Does LONG-ARC.md's "substrate plus wrappers" framing adequately capture the multi-mode, multi-shape platform the user now envisions? Or does it encode single-mode assumptions (one wrapper type, one play shape, one social texture)?
- Does the M1→M2→M3 milestone sequence close doors? E.g., if M1 builds a local-party-only architecture and M2 adds async — is the M1→M2 transition a refactor or an extension? If it's a refactor, the milestone sequence has a hidden cost.
- Does the vision-alignment initiative's scope boundary (what it includes and excludes) itself foreclose questions that need answering before Phase 01? If "game mode portfolio" is out of scope, and it turns out to be the most load-bearing Phase 01 input, the scope boundary is the problem.
- Does the authored-round contract framing (Phase 01's stated output) already encode assumptions about what a "round" is that would prevent non-round game shapes (open-ended community engagement, persistent collections, season-long arcs)?

The exploration doesn't need to answer all of these definitively. But it should name any foreclosures it discovers, because those foreclosures are first-class findings for the paused audit — they would change what the audit's practical conclusion recommends.

### Thread 6 — Creative Modes Beyond "X but for F1"

The user specifically asked: "I wonder if we can think of more creative game modes." This is an invitation for genuine creative ideation — not just mapping existing games to F1, but inventing new game experiences that exploit what's unique about F1 as a domain:

- The fact that F1 circuits are real PLACES with real geography, real atmosphere, real visual texture
- The fact that F1 has 70+ years of history with distinct visual eras
- The fact that F1 has intense social narratives (rivalries, underdog stories, team dynamics)
- The fact that F1 fans are deeply knowledgeable and enjoy demonstrating that knowledge socially
- The fact that F1 has a global calendar that creates natural event cadence (race weekends)
- The fact that the community is passionate, opinionated, and loves debate

What game experiences could ONLY exist in the intersection of these properties?

---

## BoxBoxd Reference — What We Know

BoxBoxd (boxboxd.fun) is the closest competitive reference design. Here is what B8-1 established:

**Game modes (9 total as of 2026-04-11)**:

| Mode | Shape | Content type |
|------|-------|-------------|
| Boxdle | Wordle variant — guess F1 driver in 8 tries with attribute clues | Driver attributes |
| Gridtexto | Contexto variant — semantic similarity ranking of F1-related words | F1 vocabulary |
| Connections | NYT Connections variant — group 16 F1 items into 4 categories | Mixed F1 facts |
| Elo Ranker | Elo-based ranking — choose between two drivers/tracks/etc. | Community opinions |
| Guess Who F1 | Yes/no clue deduction — narrow down which driver from clues | Driver identification |
| Break Week | Survey/poll — community opinion gathering | Fan opinions |
| 3 personality quizzes | "Which driver are you?" style | Personality mapping |

**Product shape**: daily-solo with one 1v1 multiplayer experiment. No private-room architecture. No host-screen mode. No party-game shape. No geography or spatial mode.

**Differentiation surface**: BoxBoxd operates on F1 knowledge as **propositions** (trivia, vocabulary, semantic similarity). Prix-guesser's anchor operates on F1 knowledge as **spatial experience** (circuits as places). These are non-overlapping cognitive registers. BoxBoxd also has no party-game social architecture.

**Monetization**: free tier + paid tier. Operational since 2024. Single developer (Shaina Salmi, discovered via App Store listing). iOS app launched October 2025.

**Legal posture**: site-wide disclaimer ("BoxBoxd is an independent fan platform. Not associated with any racing organization or championship body. All motorsport-related names and marks belong to their respective owners."). No licensing disclosure.

Full details in `.planning/research/2026-04-11-f1-fan-project-legal-landscape/01-boxboxd-deep-read.md`.

---

## What the Current Canon Already Says About Maturity

The existing LONG-ARC.md (lines 36–47) already has a "Mature Product Hypothesis" section:

> "The mature shape is best understood as one authored F1 substrate plus multiple possible wrappers, not as one frozen app shape. The substrate is the durable center: authored round data, answer-target relationships, judging, reveal logic, session state, and content operations that can survive wrapper changes."

And it names possible wrappers: async challenge, solo support shell, spectator/streamer-adjacent shell, broader F1 party platform expansion.

**This exploration should engage with, challenge, and extend this framing.** The LONG-ARC was written before BoxBoxd research and before the commercial-vision shift. It may still be correct — or it may be too conservative in what "wrappers" it envisions. The exploration should produce a richer understanding of what the platform could become.

---

## The Wider Context — What's Paused and Waiting

### The Phase 01 prep audit

A multi-wave audit of prix-guesser's Phase 01 preparatory work is paused at Review Gate 2. Eight lane outputs (1A, 1B, 1C, B2-Opus, B2-Sonnet, B3, B4, B7) are complete. A Wave 3 synthesis task spec has been written but the synthesis has NOT been dispatched. The audit's emerging conclusion is "the narrow vision-alignment initiative can proceed with specific additions — three canon additions and three PLAN additions — without widening scope." But this was the conclusion BEFORE the commercial-vision shift and the game-design dimensions conversation.

The full audit state is in `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/CLAUDE-SESSION-HANDOFF.md`. The reentry session for the audit should read that file to resume.

**This exploration may change what the audit's synthesis should conclude.** Specifically:
- If the exploration produces a richer understanding of the experience dimensions the substrate needs to support, that understanding is a Phase 01 input that the audit's practical conclusion should reference.
- If the exploration reveals that the vision-alignment initiative's scope is genuinely too narrow (because it doesn't account for multi-mode platform architecture), that's a finding the audit should carry.
- If the exploration confirms that the existing LONG-ARC.md framing is sufficient and the dimensions table covers the gap, the audit can proceed as planned.

### The B8 research program

Five research lanes plus a synthesis were completed during the triggering session:

- `.planning/research/2026-04-11-f1-fan-project-legal-landscape/01-boxboxd-deep-read.md` — BoxBoxd deep read
- `.planning/research/2026-04-11-f1-fan-project-legal-landscape/02-f1-fan-project-survey.md` — F1 fan project survey (9 projects cataloged)
- `.planning/research/2026-04-11-f1-fan-project-legal-landscape/03-analogous-fan-projects.md` — Cross-domain fan project cases (Nintendo, Marvel, Star Wars, etc.)
- `.planning/research/2026-04-11-f1-fan-project-legal-landscape/04-commercial-threshold.md` — Donation/commercial threshold analysis (US/UK/Canadian doctrine)
- `.planning/research/2026-04-11-f1-fan-project-legal-landscape/05-nominative-fair-use.md` — Nominative fair use and implicit branding analysis
- `.planning/research/2026-04-11-f1-fan-project-legal-landscape/06-synthesis.md` — Synthesis of all 5 lanes

These are background context for the exploration, not inputs to consume deeply. The most relevant file is 01-boxboxd-deep-read.md (for the competitive reference design).

### The pending Phase 01 planning

Phase 01 (Authored Round Contract) needs a discuss-phase rerun before planning can proceed. STATE.md says "Replanning required before execution." The discuss-phase rerun should consume:
- The audit's practical conclusion (when the audit synthesis completes)
- This exploration's output (whatever form it takes)
- The refreshed canon (PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md)

The exploration's output is a first-class input to the discuss-phase.

---

## Aims From the Triggering Session

> **READ THIS SECTION FOR AWARENESS. DO NOT TREAT THESE AS CONSTRAINTS ON THE EXPLORATION.**
>
> The triggering session has specific things it hopes this exploration will produce. These are noted here so the exploration session knows what downstream work exists, can optionally speak to those needs, and can flag if the exploration reveals that those needs are wrong-shaped. But the brainstorming itself should be unconstrained — explore widely, think creatively, follow unexpected threads. If the exploration produces something the triggering session didn't anticipate, that's a feature, not a scope violation.

### Aim 1 — Game-design dimensions for the Phase 01 substrate

The triggering session identified 5 candidate dimensions (player roles, reveal grammar, answer input modality, session arc, spectacle assets) that the authored-round contract should make first-class. The exploration may:
- Confirm these 5 are the right dimensions
- Add dimensions the triggering session missed
- Reframe the dimensions table entirely
- Discover that the "dimensions" framing itself is wrong and propose a different way to think about substrate extensibility

### Aim 2 — Input to the vision-alignment initiative scope decision

The audit is evaluating whether the narrow vision-alignment initiative (2 research calls + 1 deliberation + 1 decision anchor) is sufficient for Phase 01 readiness. If this exploration reveals that the initiative should account for multi-mode platform architecture, that's a concrete widening recommendation the audit synthesis should carry.

### Aim 3 — Input to LONG-ARC.md revision

The LONG-ARC.md may need updating to reflect the expanded commercial vision and the richer understanding of what the platform could become. The exploration might produce the raw material for that revision.

### Aim 4 — Creative game-mode ideas

The user genuinely wants to brainstorm — not just analyze. Original, creative, surprising game mode ideas that exploit what's unique about F1 as a domain. These don't need to be fully designed; they need to be compelling enough to inform the product vision.

### Aim 5 — "What does a mature product look like?"

The question of content flywheel, retention loop, monetization architecture, community features, and platform sustainability. This is the most expansive aim and the one most likely to produce unexpected findings.

---

## Exploration Session Norms

Based on the triggering session's communication patterns:

- **The user wants deep, creative engagement, not just analysis.** They pushed back multiple times when the conversation stayed in analysis mode ("is there any interpretation that might ask for more?"). Match their energy with creative depth.
- **The user wants honest uncertainty.** "I don't know yet" and "this might be wrong" are welcome. Don't manufacture confidence.
- **The user wants to think in terms of platform, not individual features.** They consistently pulled the conversation from "here's a specific mode" to "here's a way of thinking about the space of possible modes."
- **The user wants practical grounding.** BoxBoxd is the concrete benchmark. Ideas should be relatable to "how would this compare to what BoxBoxd offers?" or "what experience does this enable that nothing in the F1 fan ecosystem provides?"
- **The user delegates web research to subagents.** Never run WebSearch/WebFetch in the main thread. If the exploration needs external research (e.g., party game design patterns, community platform architectures), delegate to a general-purpose subagent.
- **The user values quality over speed.** Explicitly rejected "loss of momentum" arguments in the audit. The exploration should take whatever time it needs.

---

## File Inventory

### This exploration's directory

`.planning/explore/2026-04-11-product-vision-game-design/`
- `HANDOFF.md` — this file (entry point for the exploration session)

### Canon files (read for product context)

- `.planning/PROJECT.md` (192 lines) — what the project is
- `.planning/LONG-ARC.md` (154 lines) — milestone arc and mature product hypothesis
- `.planning/ROADMAP.md` (205 lines) — phase-level roadmap
- `.planning/REQUIREMENTS.md` (191 lines) — active requirements
- `.planning/STATE.md` (82 lines) — current project state

### B8 research (skim for competitive/legal context)

- `.planning/research/2026-04-11-f1-fan-project-legal-landscape/01-boxboxd-deep-read.md` — BoxBoxd: the reference design
- `.planning/research/2026-04-11-f1-fan-project-legal-landscape/06-synthesis.md` — legal/competitive landscape synthesis

### Audit (for awareness of the wider context, not to consume deeply)

- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/CLAUDE-SESSION-HANDOFF.md` — audit pause state
- `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-3-synthesis-task-spec.md` — the synthesis that hasn't been dispatched yet

### Discovery (pre-GSD exploration, may have relevant product framing)

- `discovery/` directory — the original pre-GSD discovery pass; may contain mode ideas, product framing, or competitive analysis worth revisiting

---

## How to Produce Output

This exploration should follow the `.planning/explore/` conventions:

- **SESSION.md** — living narrative log of the conversation and its moves. Write and update as the exploration progresses. Capture turning points, surprising ideas, tensions, and pivots.
- **CHECKPOINT.md** — latest resumable handoff for the next session or context window. Update when the exploration reaches a natural pause or milestone.
- **CHECKPOINTS/*.md** — incremental checkpoints if the exploration is long enough to warrant them.
- **Optional synthesis artifacts** — if the exploration produces something concrete (a dimensions table, a mode catalog, a platform-maturity framework, a LONG-ARC revision draft), write it as a separate artifact in this directory.

**Nothing produced in this exploration is ratified product truth** until it is later promoted into canonical artifacts (PROJECT.md, LONG-ARC.md, REQUIREMENTS.md, phase CONTEXT files). The exploration is exploratory memory, not committed decisions.

---

*Handoff authored: 2026-04-11, by the orchestrating Claude Opus 4.6 session that ran the Phase 01 prep audit and B8 research program. This file captures the context of the triggering session at the moment the user requested the handoff. If the triggering session produces additional context before this handoff is consumed, update this file in place.*
