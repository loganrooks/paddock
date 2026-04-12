---
date: 2026-04-11
wave: 1
lane: 1C
audit_orientation: exploratory
audit_delegation: self
auditor_model: claude-opus-4-6
agent_type: general-purpose
scope: "Use web research (WebSearch / WebFetch / Context7) to identify alternatives the prix-guesser research did not consider and that should have been considered. Specifically: room/state architectures beyond Colyseus/PartyKit/boardgame.io; authored geography-quiz content models beyond geohub/Geo-Locator/react-geofindr; prior F1 community/fan game projects and their content/distribution models; whether 'private-only fan project' is a recognized framing pattern in indie/community game development that legitimately defers distribution questions, or whether it's a known evasion pattern. Surface 'didn't consider promising alternative X' findings with concrete evidence."
triggered_by: "wave-1 parallel dispatch from phase-01-prep-quality-scope-audit-2 orchestrator (Claude Opus 4.6, claude-code session)"
parent_task_spec: phase-01-prep-quality-scope-audit-2-task-spec.md
ground_rules: "core+exploratory+framework-invisibility"
tags:
  - wave-1
  - lane-1c
  - external-gap-research
  - exploratory
  - opus
  - general-purpose-agent
  - web-research
output_files:
  - wave-1-lane-1c-external-gap-research.md
---

# Wave 1 / Lane 1C — External Gap Research (Opus, general-purpose with web tools)

**You are running as a general-purpose agent on Claude Opus 4.6, with full tool access including WebSearch, WebFetch, and (if available) Context7 MCP for library/framework lookups.**

The orchestrator chose Opus for this lane because gap-finding is *generative* — it requires not just retrieving alternatives but judging which ones are *promising* enough that prix-guesser's research should have considered them. That distinction is hermeneutic and benefits from Opus depth. The lane is dispatched to general-purpose rather than gsdr-auditor because gsdr-auditor lacks WebSearch/WebFetch and external research is the lane's whole point.

## Lane Position In The Audit

This lane is one of three parallel agents in Wave 1 of a planned wave-structured audit. The full audit (`phase-01-prep-quality-scope-audit-2-task-spec.md`) was originally drafted as a single-agent dispatch but the orchestrator restructured it into a wave plan after the user asked whether the audit should model the discipline (iterative wave structure) it is evaluating.

The three Wave 1 lanes are:

- **Lane 1A (Opus, gsdr-auditor)** — canon claim integrity. Re-verifying the 2026-04-08 predecessor audit's claims about the canon.
- **Lane 1B (Opus, gsdr-auditor)** — methodological inheritance comparison between prix-guesser's and f1-modeling's vision-alignment files.
- **Lane 1C (this lane, Opus, general-purpose with web tools)** — external gap research. Your job.

You are running in parallel with 1A and 1B. Your output will be consumed by a Wave 3 synthesis pass.

## Lane Fit Assessment

This lane is **exploratory × no subject × self** because the question — "what alternatives might prix-guesser have missed that should have been considered?" — is genuinely open in shape and resists pre-decomposition into a fixed subject. The starting questions (room frameworks, content models, F1 fan games, the "private-only" framing pattern) are *prompts*, not a closed list. If the research surfaces categories of alternatives the orchestrator did not anticipate, follow them — that's the exploratory orientation in action.

The lane's exploratory orientation also means **"I don't know yet" is a valid conclusion** for any question that doesn't yield to web research. Don't manufacture findings to perform productivity.

---

## Epistemic Ground Rules

### Core Rules (every audit)

1. **Every factual claim cites the source.** For web research, cite the URL and the specific passage you found. For repo claims, cite file:line and quote the passage. Bad: "There are other room frameworks for browser games." Good: "WebSearch for 'browser multiplayer room framework 2024 2025' surfaced [framework name] at [URL]. Its README at [URL/README] states '[verbatim quote about its model]'. This is a candidate alternative the prix-guesser research at `.planning/phases/01-authored-round-contract/01-RESEARCH.md` lines [N..M] did not name. Whether it is *promising* (more so than Colyseus/PartyKit/boardgame.io for the prix-guesser use case) is a separate judgment — see [section]."

2. **For every finding, BEFORE writing it, ask "What would disconfirm this?" and CHECK.** Example: if you are about to claim "the project should have considered framework X," first ask: would framework X actually serve the prix-guesser use case (private rooms, browser-first guests, host-screen-friendly, watchable reveals)? If X is great for a different use case but wrong for this one, the "should have considered" claim weakens. The disconfirmation is the project-fit check, not just the existence of the alternative.

3. **Distinguish what you measured from what the measure captures.** Example: "I searched for 'F1 browser game open source' and found N results in the first 3 pages. Result count measures search popularity, NOT relevance. I read the top [K] results and found that [J] were unrelated (mobile native apps, official F1 properties, betting tools); [J−unrelated] were relevant indie/community projects worth examining further."

4. **Rule 4 (escape hatch).** Address in the mandatory **What the Obligations Didn't Capture** section.

5. **Rule 5 (frame-reflexivity).** For exploratory orientation, Rule 5 weaves into "name what you didn't look at" (one of the exploratory obligations below).

   *Specific grounding questions (copy verbatim into your output):*
   1. *"If this lane had been classified with a different orientation (e.g., `investigatory` instead of `exploratory`), what would I have looked for that I didn't? Specifically: a more directed search for confirming or disconfirming a particular hypothesis would have surfaced different alternatives."*
   2. *"If this lane had been given a named subject (e.g., `comparative_quality` against a specific named alternative), what would I have looked for that I didn't?"*
   3. *"What about the current classification shapes what I am prepared to notice and what I am not? Name one concrete example. (E.g., the 'find what they missed' framing orients you toward absences; what *presences* in their research might be load-bearing in a way the absence frame can't see?)"*

   **Anti-performativity warning** applies. An empty Rule 5 means you performed compliance theater.

### Orientation Obligations (exploratory)

The exploratory orientation is occasioned by *possibility* — a question opens, curiosity beckons, no specific discrepancy is driving the work. Each obligation is framed with its "why this matters."

- **State the question or curiosity that initiated the exploration.** *(Why this matters: an exploration without a stated question drifts toward what the auditor already knows. Stating the question anchors the exploration in its occasion.)*

  The starting question: **What alternatives in the broader ecosystem (rooms/state, authored content models, F1 fan games, indie/community game distribution patterns) might prix-guesser's research not have considered, and which of those, if any, should have been considered?**

- **Follow the question wherever it leads.** Permission to change direction is required — if what you find reframes the question, that reframing is itself a finding. *(Why this matters: explorations that stay on their initial track are indistinguishable from standard audits with vague scope.)*

- **Name what you found that you weren't looking for.** *(Why this matters: the most valuable findings of an exploratory audit are often the ones the question didn't anticipate.)*

- **Name what the exploration opened** — new questions, possibilities, directions worth pursuing. *(Why this matters: unnamed openings vanish; named openings become seeds for future work.)*

- **Name what you didn't look at.** Acknowledged partiality, not failure. *(Why this matters: every exploration is partial. Naming the partiality is what distinguishes a useful exploration from one that implicitly claims comprehensiveness.)*

- **"I don't know yet" is a valid conclusion.** *(Why this matters: forcing closure on an exploration destroys its epistemic value. An exploration that ends in "I don't know yet" but has surfaced the right questions is worth more than one that ends in a confident but premature answer.)*

### Cross-Cutting Obligations

#### Framework invisibility

> *"Name a concrete finding that would not appear no matter how rigorously this audit was conducted, because of how this audit's scope was framed. If you can't name one, that's suspicious."*

**Specific to this lane:** the lane is framed in terms of "find what they missed in the named research categories." This framing makes invisible: alternatives in *unnamed* categories. For example, if the most important alternative prix-guesser missed is not a framework or a content model or a fan-game precedent but something like "a method of running playtest sessions before substrate freezing" or "a community-building practice that changes what 'private-only' means," this lane's framing wouldn't surface it. **Name where the most important alternatives might live outside the lane's framing.**

---

## The Lane Situation

### What prix-guesser's research already considered

Read these files briefly to know what the project already named as alternatives — you do not need to read them in depth, just enough to know what's there:

- `.planning/PROJECT.md` lines 67–73 (open-source references already studied: `benlikescode/geohub`, `RasterCrow/Geo-Locator`, `xchau/react-geofindr`, `PartyKit`, `Colyseus`, `boardgame.io`)
- `.planning/phases/01-authored-round-contract/01-RESEARCH.md` (the Phase 01 research, ~418 lines — skim for what alternatives it considers)
- `.planning/initiatives/vision-alignment-2026-04/README.md` lines 49–66 (in scope / out of scope of the narrow initiative — what the initiative declares it will and won't consider)
- `.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md` (what alternatives the principles ask for — note that the prix-guesser principles file does NOT have an explicit "precedent analysis with specific named cases" requirement, which is one of the things Lane 1B is checking)

### What this project actually is

Prix Guesser is a private-only, unofficial F1 fan game project. Per `.planning/PROJECT.md`:
- v1 target: friends-on-couch / private remote / hybrid sessions, browser-first guests, host-screen watchability
- Anchor mode: authored geography-and-circuit rounds (one strong mode, not a multi-mode platform)
- Initial audience: knowledgeable long-time F1 fans who can recognize circuits, venue texture, eras
- Out of scope explicitly: public-release hardening, ranked ladders, AI-generated content, "all F1 party modes" platform in v1

The project has a 3-milestone long arc:
- M1: Game Night Works (the v1 anchor mode + private rooms)
- M2: Play Anytime, Anywhere (async, remote, content ops)
- M3: F1 Party Platform (adjacent modes, team variants, spectator wrappers)

**Keep the use case concrete** as you research. An alternative is *promising for prix-guesser* only if it serves friends-on-couch private play with watchable host screens, not if it serves a different use case well.

### What the user named as load-bearing concerns

The user invoking this audit explicitly named **deployment, scale, distribution, advertising, and adoption** as concerns the narrow initiative may have under-considered. These are the priority research areas for this lane, beyond the named alternatives.

### What this lane is NOT investigating

- **Lane 1A** is checking the canon's claims and the predecessor audit's claims. You do **not** need to read the canon docs in depth or the predecessor audit. You may read them briefly if needed to ground your search.
- **Lane 1B** is comparing methodological inheritance from f1-modeling. You do **not** need to read the f1-modeling files at all.
- The Codex briefing files in `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/` are background — you do not need to read them.

If you need cross-lane work, do it but flag it for the synthesizer.

---

## Lane Investigatory Questions

These are starting questions, not closed.

### LQ-1C.1 — Room/state framework alternatives

The prix-guesser research names `Colyseus`, `PartyKit`, and `boardgame.io` as the room/state architecture candidates. The 2026-04-08 predecessor audit said "Colyseus vs PartyKit is NOT neutral from a distribution standpoint" and recommended Colyseus for self-host/Docker parity.

Use WebSearch and Context7 (for npm package metadata) to identify other browser-multiplayer room frameworks active in 2024-2025 that could serve a private-host private-rooms use case. Candidates to look for include but are not limited to: PartySocket, Liveblocks, Yjs+presence, Hocuspocus, Replicache, Convex, Soketi, Centrifugo, raw WebRTC datachannels with a small signaling server, raw Socket.IO with custom auth, ElectricSQL, custom y-websocket setups.

For each alternative you find:
- Cite the URL and a representative passage about its model
- Assess whether it would actually serve the prix-guesser use case (private rooms, browser-first guests, host authoritative state, host-screen friendly)
- If it's a candidate worth considering, name what it would offer over Colyseus/PartyKit/boardgame.io
- If it's not a candidate, name why (wrong use case fit) — do NOT include alternatives that exist but don't fit

The question is not "give me a long list of frameworks." The question is "did prix-guesser miss any *promising* alternative?"

### LQ-1C.2 — Authored geography-quiz / browser game content model alternatives

The prix-guesser research names `geohub`, `Geo-Locator`, and `react-geofindr` as content/round-loop precedents. These are GeoGuessr-shaped projects.

Use web research to identify other authored-content browser game projects whose content models would be informative for prix-guesser. Categories worth searching:

- **Trivia/quiz frameworks with rich authored content** (Kahoot-like clones, Jackbox-like party game frameworks, OpenTriviaDB consumers, Quizziz alternatives)
- **Other GeoGuessr-shaped projects** beyond the three named (City Guesser, GeoTastic, WikiGuessr, GuessThePlace, etc.)
- **Authored content frameworks for educational quiz games** that handle clue ladders, reveal explanations, partial credit
- **Open-source party game frameworks** that handle host-screen-and-controller architecture (Gartic Phone clones, Drawpile-like collaborative tools)

For each alternative you find that is genuinely promising for prix-guesser's use case:
- Cite URL + representative passage
- Note what its content model offers that the prix-guesser research did not name
- Note specifically anything related to: answer-target hierarchy (the predecessor audit's "THE most important architectural decision"), clue-step structure, reveal grammar, fallback media handling, scoring intent

### LQ-1C.3 — F1 community / fan game prior art

Use web research to identify community/fan F1 game projects (not official F1 products, not betting/fantasy F1 sites). Categories: F1-themed quiz/trivia games, F1 fantasy leagues that include prediction games, F1 community discord bots that play games, F1 emoji/word games, community-run F1 prediction leagues, F1 GeoGuessr communities, F1 streaming broadcast game integrations.

For each finding:
- Cite source
- Note its content model and distribution model
- Specifically: how does it handle authoring (volunteer? curator? AI-assisted?), how does it handle "private group" play vs public play, how does it handle the rights/licensing question (since F1 is heavily branded)

The rights/licensing question is particularly interesting because prix-guesser's "private-only fan project" framing is partly an answer to this question. Prior art on how other unofficial F1 community projects handle the line between fair use and infringement would be informative.

### LQ-1C.4 — The "private-only fan project" framing as a recognized pattern

This is the question with the highest leverage for the user's stated concern about "deployment, distribution, advertising, adoption."

The prix-guesser canon repeatedly invokes "private-only" as both a product positioning and an explicit deferral of distribution concerns. The narrow initiative's `Out of scope` excludes deploy topology, public/share-by-link/spectator posture, etc., partly on the grounds that the project is private-only.

Research questions:
- Is "private-only fan project" a recognized framing in indie / community game development? Are there named patterns or anti-patterns associated with it?
- When private-only fan projects do get used by groups beyond their first authors, what kinds of distribution / hosting / onboarding problems actually arise? (Friends sharing the project with their friends; the original author's friends asking how to host it; the project growing beyond what was anticipated.)
- Are there examples of private-only fan projects that successfully stayed private vs. ones that grew unexpectedly and had to retrofit distribution/adoption work?
- Is there a known pattern where "private-only" is used as an evasion of distribution complexity, with the project later having to address it under worse conditions? Or, conversely, is "private-only" a known healthy framing that legitimately defers distribution until the core product is proven?

This question is the heart of the user's concern. The user said: "we haven't considered enough how we are to deploy at scale, or distribute, or advertise, or make it easy to adopt / share." Is that concern *empirically* justified by what happens to private-only projects in practice, or is the prix-guesser canon's "private-only" framing actually defensible by reference to known patterns?

### LQ-1C.5 — Anything else the search surfaces

Per the exploratory orientation: follow the search where it leads. If you find a category of alternatives the orchestrator didn't anticipate, name it and engage with it. The most valuable findings of an exploratory audit are often the ones the question didn't anticipate.

Specifically be alert for:
- Adjacent products that aren't framework/content/F1 but are about the *practice* of running game nights with friends (party game design literature, indie game dev communities discussing private-only release patterns, community-of-practice writing about how friends actually adopt small private projects)
- Methodological precedents — projects that did substantive vision-alignment work for private-only fan games and what their initiatives looked like
- The opposite of what we expect — examples of private-only fan projects that did NOT need the things the predecessor audit recommended, with concrete reasoning for why

---

## What Must Appear In The Lane Output

Write your output to `.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md`.

Required elements:

- **All obligations addressed in substance** — Core Rules 1–5, all six exploratory orientation obligations (with stated question, named what you found that you weren't looking for, named what the exploration opened, named what you didn't look at, valid "I don't know yet" conclusions where they apply), framework invisibility. Woven, not as labeled containers — though the exploratory obligations have specific shapes that are easier to honor in dedicated sections.

- **An evidence-based summary** for each LQ-1C.1 through LQ-1C.4. For each:
  - What you searched for
  - What you found
  - Which findings are *promising* alternatives prix-guesser should have considered (with project-fit reasoning)
  - Which findings are *not* promising and why
  - An "I don't know yet" or "needs more research" marker if the question doesn't yield to the web research available

- **A "Position of the Investigation" section** addressing I4-equivalent (note: I1-I4 are investigatory obligations; for exploratory, the equivalent is "name where you're looking from"). You are running as Opus general-purpose with web tools — name what that means for what you noticed.

- **A Rule 5 frame-reflexivity section** answering the three specific grounding questions verbatim. The exploratory orientation makes Rule 5 particularly important because exploratory work that doesn't engage frame-reflexivity tends to drift toward what the searcher already knows.

- **A "What you didn't look at" section** — explicit partiality, with reasoning. What categories of alternatives did you NOT search for, and why?

- **A "What the exploration opened" section** — new questions, possibilities, directions for future investigation that this lane surfaced but did not pursue.

- **A "What I found that I wasn't looking for" section** — the unanticipated findings. If you have nothing here, the exploration was probably too narrow.

- **A "What the Obligations Didn't Capture" section** — mandatory.

- **A "Cross-Lane Notes for the Synthesizer" section.**

- **A list of candidates for Wave 2 follow-up.**

---

## Tool Usage Notes

- **WebSearch / WebFetch**: use them. Browse the live ecosystem; don't rely on training-data memory of what frameworks exist. Cite URLs.
- **Context7 MCP** (`mcp__context7__*`): use for any npm package, library, or framework you want to verify the current state of. Context7 returns up-to-date package metadata and documentation.
- **Read/Grep/Glob**: only on the prix-guesser repo files named in the situation section. Do not deep-read the full repo.
- **Bash**: avoid unless you need to run a one-off search or git command.
- **Time budget**: this is a research lane and substantive web research takes effort. Don't rush, but don't pad either. If a search yields nothing useful, name the negative result and move on rather than perseverating.

---

## Output File

Write the lane output to:

`.planning/audits/2026-04-11-phase-01-prep-quality-scope-audit/wave-1-lane-1c-external-gap-research.md`

Do not return a conversational summary instead of the file. Write the file, then exit.
