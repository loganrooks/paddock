---
date: 2026-04-11
wave: 1
lane: 1C
audit_orientation: exploratory
audit_delegation: self
auditor_model: claude-opus-4-6
agent_type: general-purpose
lane_task_spec: wave-1-lane-1c-external-gap-research-task-spec.md
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
---

# Wave 1 / Lane 1C — External Gap Research

## Position of the Investigation (I-equivalent for exploratory)

I am running as Claude Opus 4.6 in a general-purpose agent seat with WebSearch, WebFetch, Read, and Grep. I am not the gsdr-auditor agent. What that gives me: live 2026 web access, the ability to fetch GitHub READMEs and official trademark policies directly, and the bandwidth to judge whether the alternatives I find are actually project-fit rather than merely existing.

What that costs me: I have no native MCP library index (Context7 was listed as available in the dispatch but I did not end up invoking it — see "What I didn't look at"); I can only see the surface of any given framework from its README and one or two fetched pages, not from code-reading; and my "project-fit" judgment is made from a light skim of `.planning/PROJECT.md` and `.planning/phases/01-authored-round-contract/01-RESEARCH.md`, not from a deep immersion in prix-guesser's full substrate (the deep-repo read is Lane 1A's and Lane 1B's job per the dispatch). If I had read the canon more deeply, some of my "promising alternative" calls would probably sharpen. I am noting this partiality rather than pretending otherwise.

One framing I want to record up front, because it shaped what I looked at: the Phase 01 research file (`.planning/phases/01-authored-round-contract/01-RESEARCH.md`) is almost entirely about YAML/Zod/Vitest tooling for the authored content contract. It does not itself engage substantively with room framework alternatives, authored content model alternatives in the broader sense, F1 fan game prior art, or the "private-only" framing question. The task spec presumes the *project* considered those questions; the Phase 01 research file actually defers most of them (correctly, since Phase 01 is about substrate freeze, not room transport). So when the task spec asks "what alternatives did the research miss?" I read that as asking about the broader research lineage — the references named in `.planning/PROJECT.md` lines 67–73 and the canon's cumulative position — not strictly about gaps in the Phase 01 research document itself. A stricter reading would yield fewer findings; I've chosen the broader reading because it's the one that actually serves the user's load-bearing concerns about deployment/distribution/adoption.

---

## Stated Question (exploratory obligation 1)

> **What alternatives in the broader ecosystem (rooms/state, authored content models, F1 fan games, indie/community game distribution patterns) might prix-guesser's research not have considered, and which of those, if any, should have been considered?**

This is a generative question, not a retrieval question. An alternative "should have been considered" only if it's promising for the prix-guesser use case (friends-on-couch private play, browser-first guests, host-screen watchability, authored F1 geography content), not merely if it exists.

---

## Core Rules Grounding

**Rule 1 (cite sources):** every factual claim below includes the URL and the specific passage or file:line it came from.

**Rule 2 (disconfirmation before writing):** for every "should have considered" claim below, I ask project-fit first. A framework that is great for a different use case (e.g. collaborative text editing, giant-scale public matchmaking) is *not* a promising alternative for prix-guesser even if it's more popular than Colyseus. Where I include a finding as a candidate, I explain the project-fit reasoning. Where I exclude one, I say so explicitly.

**Rule 3 (what the measure captures):** my search was keyword-driven against WebSearch and a small number of targeted WebFetches. What that measures is *what a 2026 keyword search surfaces to a researcher who already knows Colyseus/PartyKit/boardgame.io/geohub exist*. It does not measure everything in the ecosystem, and it is biased toward projects with active SEO and GitHub stars. Several of my negative results (e.g. "I could not find writeups of private-only fan projects that outgrew their scope") may reflect that bias rather than the absence of the phenomenon.

**Rule 4 (escape hatch):** addressed in its own section below.

**Rule 5 (frame-reflexivity):** addressed in its own section below, with the three verbatim questions answered.

---

## LQ-1C.1 — Room/state framework alternatives

### What I searched

- "browser multiplayer room framework private rooms 2025 alternatives Colyseus PartyKit"
- "Liveblocks vs Colyseus browser multiplayer party game 2025"
- "Convex backend real-time multiplayer game rooms browser 2025"
- "Yjs OR Hocuspocus multiplayer game room private session browser"
- "Socket.IO self-host private room game server alternatives 2025 small party game"
- "Jackbox like party game framework open source host screen controller 2025"
- "Rocketcrab open source party game host platform GitHub architecture"
- "Gartic Phone open source private room lobby architecture clone 2025"

### What I found — genuinely promising alternatives prix-guesser's research did not name

**1. Hackbox** (https://github.com/tomalama/hackbox)

WebFetch of the repo: "a duo of packages to aid in the development of party games that make use of mobile devices or any other device that can open a browser." Split into `hackbox-server` and `hackbox-client`. MIT licensed. Explicitly designed around the "host screen + mobile controller" topology.

Project-fit for prix-guesser: **high, worth considering.** The watchability layer in prix-guesser is exactly a "host screen, clue ladder shown on the big screen, guests answer on phones" shape. This is literally what Hackbox is for. The project's three named room/state references (Colyseus, PartyKit, boardgame.io) are all *generic* multiplayer frameworks; Hackbox is *genre-fitted* to the host+controller split. Whether prix-guesser should *adopt* it depends on maintenance (the repo is small and appears low-activity) but the framework-shape as a reference point for architecture was demonstrably missed.

**2. Rocketcrab** (https://github.com/tannerkrewson/rocketcrab)

WebFetch of the repo (367 commits, 263 stars, MIT): "lobby service and launcher for mobile web party games... generates unique game codes for each party. Games can either provide an API endpoint that creates rooms (e.g., returning `abcd`), or rocketcrab generates random IDs that games accept as valid room codes. The resulting URL opens in iframes across all players' devices simultaneously." Games get automatic query parameters: `rocketcrab=true`, `name=[player name]`, `ishost=true/false`.

Project-fit for prix-guesser: **high for the lobby/launcher pattern, even if not for adoption.** Rocketcrab is *not* a room framework; it's a lobby abstraction above room frameworks. But the iframe-plus-query-params pattern is a genuinely different architectural frame for how "private room" and "individual game" relate — and it sidesteps a category of problems that Colyseus and PartyKit solutions don't even name. Specifically: the host/client role distinction is declared in the URL itself. For prix-guesser's host-screen watchability layer this is a direct precedent.

**3. Party-Box** (https://github.com/hammre/party-box)

WebFetch: three-component split — "Client: Mobile web interface for individual players; Broker: Public web server hosting client assets and managing WebSocket communication; Game: Software running on the display screen, communicating via the broker." JSON messages over WebSockets, room codes, broker removes room state when all participants disconnect.

Project-fit for prix-guesser: **conceptually promising, practically abandoned.** Last commit January 2018 (11 commits total, no visible license). As a runnable dependency it is not a candidate. But its *architecture description* — specifically the "Broker vs Game vs Client" three-role split — is a cleaner mental model than "authoritative server + clients" for prix-guesser's host-screen use case, because it names the watchability surface (the Game / big-screen role) as a distinct participant, not just "another client." The prix-guesser research does not currently carry this three-role vocabulary.

**4. Convex** (https://stack.convex.dev/building-a-multiplayer-game, https://www.efe.dev/blog/convex-multiplayer-game)

From Convex's own multiplayer game walkthrough and a 2025 dev.to post: "Convex provides a backend entirely with TypeScript, including database, backend functions, authentication and real-time syncing... server-side database queries automatically caching and subscribing to data, powering a realtime useQuery hook in React clients... sub-50 millisecond read/write latency even at 5,000 concurrent connections." Real-world examples include GeoWar.io and a real-time RPG.

Project-fit for prix-guesser: **moderately promising, but with a crucial catch.** The catch is Convex is hosted-first — self-hosting is available but less polished. The prix-guesser 2026-04-08 predecessor audit (per the task spec briefing) recommended Colyseus specifically *because* "Colyseus vs PartyKit is NOT neutral from a distribution standpoint" and favored self-host/Docker parity. Convex fails that same test *more* strongly than PartyKit does. So while Convex is a legitimate alternative to name, the project-fit reasoning that already weeded out PartyKit weeds out Convex too. **This is important:** the research file could truthfully say "we considered it and it fails the same distribution-parity test that ruled out PartyKit." That framing is not currently in the research, and naming it would make the exclusion reasoning load-bearing rather than accidentally absent.

### What I found — alternatives that are NOT project-fit for prix-guesser

I am listing these with the reason they fail, because the *exclusion reasoning* is itself the finding:

- **Yjs + Hocuspocus**: CRDT collaborative editing backend. Project fit fails: prix-guesser doesn't need CRDT merge semantics — it needs authoritative host-screen state with ordered reveals and deterministic scoring. CRDTs are optimized for concurrent-edit resolution, which is the wrong problem shape for a quiz/reveal loop. Exclude with reasoning. (Source: https://tiptap.dev/docs/hocuspocus/getting-started/overview)

- **Liveblocks**: "all-in-one toolkit to build collaborative products like Figma, Notion, and more" (from the search result summary). Same mismatch as Yjs — it's optimized for "simultaneous editing of shared state" not "host-authoritative round progression." Also commercial/hosted. Exclude.

- **PocketBase / TrailBase / SignalR / ws / GUN**: low-level real-time primitives or backends that are *alternatives to building on*, not alternatives *to Colyseus-the-game-framework*. Naming them is noise. Exclude.

- **MPG (Multiplayer Party Game, Elixir/Phoenix LiveView, https://github.com/jccr/mpg)**: a specific game (werewolf), not a framework, and uses Elixir which is outside prix-guesser's TypeScript-first stack preference. Exclude as a framework candidate, but keep as a concrete prior-art reference for the host-screen pattern if synthesis wants one.

### Verdict for LQ-1C.1

Prix-guesser's research **did miss a promising category**: the "host-screen + mobile-controller" genre-specific frameworks (Hackbox, Rocketcrab, Party-Box). Colyseus/PartyKit/boardgame.io are all *generic* multiplayer frameworks; the Jackbox-family frameworks are *shape-specific* to prix-guesser's actual use case and carry vocabulary (Broker/Game/Client roles, iframe-based launcher abstractions, automatic host/player URL params) the current research does not carry.

**None of these are necessarily what the project should build on.** The promising-ness is in the *reference value* — the prix-guesser canon currently reasons about rooms as a generic concurrency/state problem, when the closer conceptual neighbors treat rooms as a genre-specific host/controller coordination problem. That reframe matters for D-06 through D-12 in the Phase 01 research not at all, but for the later Phase 2+ room/authority design it matters substantially.

**"I don't know yet" marker:** I did not evaluate Hackbox, Rocketcrab, or Party-Box for actual code quality, recent activity, or whether they survive contact with real F1 content. They are reference-value finds, not build-on-this-today finds. Whether any of them should become a dependency is an open question.

---

## LQ-1C.2 — Authored content model alternatives

### What I searched

- "city guesser OR geotastic OR wikiguessr geography quiz browser game authored content model"
- "Kahoot clone OR Quizizz alternative open source self-hosted trivia quiz authored content schema"
- "Geotastic custom map authored content private lobby friends multiplayer"

### What I found — promising alternatives the research did not name

**1. PBLive** (https://github.com/RunasSudo/PBLive)

WebFetch: "open-source self-hosted live online quiz tool, similar to Kahoot and Socrative." AGPL-3.0. **YAML-based content schema** with question types: Landing, MCQ, Type (short-answer with optional validation), Draw (canvas responses over images), Speed (rapid-fire MCQ with 2-second countdown), Speed_review. Questions can include `prompt`, `answers`, `image`, `answer_form`, `answer_type`, `answer_range`. Image files in `data/img/` directory.

Project-fit for prix-guesser: **very high as a content-model precedent.** This is the single closest reference I found to prix-guesser's Phase 01 authored-content work: YAML source, discriminated question types, image asset references, answer validation with optional constraints. The Phase 01 research file's recommended shape (YAML parsing with `parseDocument`, Zod-backed discriminated unions on clue-step `kind`, fixture-based contract tests) is almost exactly the same architectural shape, arrived at from first principles. **This is a direct prior-art reference prix-guesser's research should name.** It's not about adoption — PBLive is *archived* (read-only since August 2022), which is itself informative as a risk signal — but about validation: the architectural shape prix-guesser is choosing has been tried, and the person who tried it had to stop. Why did PBLive stop? I don't know from the README alone, and the archival without explanation is itself a data point worth knowing.

Additionally: PBLive does not have a `fallback_required` / `fallback_only` / `override_coverage_class` concept (per D-10 in the Phase 01 research). That's a genuine prix-guesser innovation over PBLive. Naming PBLive as the closest prior art makes that innovation *visible as a choice* rather than invisible as "what we did."

**2. ClassQuiz** (https://github.com/mawoka-myblock/ClassQuiz)

WebFetch: "quiz-application like Kahoot!, but open-source... mainly made for teachers... 1,760 commits, 27 open issues, 35 pull requests visible on the master branch... self-hosting documentation exists at classquiz.de/docs/self-host." Monorepo FastAPI/Python backend plus SvelteKit frontend; content is database-driven, not YAML-authored.

Project-fit for prix-guesser: **moderate.** ClassQuiz is actively maintained (which PBLive is not), proves self-hosting of this genre is viable at meaningful scale, and the architecture of having a separate editor UI + database-stored content is the natural Phase 2 / Phase 3 evolution prix-guesser might need. But its content model is *not* file-authored, which is the exact choice D-12 in the Phase 01 research explicitly makes in the opposite direction. ClassQuiz is a **contrast case**, not an alternative to adopt. Naming it as a contrast makes D-12 defensible by reference: "we chose file-based authoring because database-backed editors introduce early complexity we don't yet need; see ClassQuiz for the other branch."

**3. Geotastic** (https://geotastic.net/)

WebSearch results: "free-to-play geography quiz browser game that provides a similar experience to GeoGuessr... custom maps focused on specific themes – like 'European Castles' or 'US National Parks'... Creating custom maps is restricted to supporters of Geotastic... Players can create their own private online lobby and invite their friends... For multiplayer, only the creator needs to have an account. Other players can join the lobby and play without even owning an account."

Project-fit for prix-guesser: **indirectly relevant, not directly adopted.** Geotastic is a product, not a framework — its codebase is not open per what I could see. But its social model is **a direct validation of the prix-guesser posture**: private rooms, single-account host with account-less guests, themed custom content authored by the community. Geotastic ran into monetization pressure (I found a 2024 article "New limitations for free players" — https://annoying-edu.medium.com/new-limitations-for-free-players-d834c5909a60 — which I did not deep-read but which suggests the free-tier model experienced strain). This is weak-signal evidence that the friends-private-lobby pattern has real community traction beyond GeoGuessr, and that the content-authoring-by-community axis is a live design space.

**4. The GeoGuessr "A Community World" map** (https://www.geoguessr.com/maps/62a44b22040f04bd36e8a914)

Per the GeoGuessr search result: "A Community World... world map with 100k+ handpicked locations put together by over a hundred experienced players and map makers from the GeoGuessr community."

Project-fit for prix-guesser: **reference value for the content-ops frame, not the content-schema frame.** Lane 1A is probably examining prix-guesser's content ops posture; I'm flagging for the synthesizer that community-curated geography content at 100k-location scale exists as a proof point that authored content *can* reach that depth if the community-of-practice forms around it. Prix-guesser's M2 "Play Anytime, Anywhere" milestone implicitly assumes content ops is tractable; here is an existence proof, under a different product but the same content shape.

### What I found — alternatives that are NOT promising

- **City Guesser, WorldGuessr, WikiGuessr**: these are GeoGuessr-*style* products, not content-model reference points. They don't expose their content schemas or authoring tools. Including them in a list of references would be noise, not signal. Exclude.

- **Crowdpurr, TriviaNerd, Sporcle Party, GameApart**: commercial trivia products with host-screen + mobile-controller mechanics. None are open source (from what I could see in search results). They validate the *shape* but don't offer architectural precedent for the authored-content contract. Flag as shape-validators if useful, exclude as content-model references.

### Verdict for LQ-1C.2

Prix-guesser's research **did miss PBLive**, which is the single closest architectural prior art I found for YAML-authored quiz content with discriminated question types. The missing here is not "you should adopt PBLive" — the project is archived — but "you should name it as the prior art your chosen shape converges toward, and engage with why PBLive could not sustain itself." The current Phase 01 research (lines 63–90) lists `yaml`, `zod`, `vitest`, `tsx`, `@types/node` as dependencies and calls itself original work arriving at the shape. It is not actually original at the genre level; naming the precedent both honors that and exposes the risk signal (PBLive is archived — why?).

**"I don't know yet" marker:** PBLive's archival reason. I would want to deep-read its commit history and issue tracker before claiming I know why it stopped being maintained. That's a Wave 2 candidate.

**Framework invisibility flag:** This lane's task spec framed the question as "alternatives to geohub / Geo-Locator / react-geofindr." Those three are all *geography-specific* projects. The alternative prix-guesser actually needed to name was from a *different category entirely* — the Kahoot/Quizizz-clone family — because the Phase 01 work is not actually about geography, it's about authored quiz content. The geography is the *domain* of the content; the *shape* of the content contract is a quiz contract. The lane's framing in terms of "geohub-adjacent" projects would have missed PBLive if I had taken it narrowly. I followed the exploratory permission to reframe — see next section.

---

## LQ-1C.3 — F1 community / fan game prior art

### What I searched

- "F1 trivia OR Formula 1 quiz open source community fan game GitHub"
- "guess the grid OR F1 wordle OR F1 geoguessr F1 community fan game browser"
- "F1 quiz daily community game Wordle architecture self-host project"
- "formula 1 discord bot prediction game community fan content"

### What I found

**1. Formudle** (https://formudle.com/): daily F1 games — Grid, Bingo, Wordle, Connections. Public web deployment. No visible open-source repo from what I searched. Content authoring model not disclosed.

**2. Stewardle** (https://stewardle.com/): F1 Wordle-inspired "guess the driver of the day." Public. No open-source repo visible from what I searched.

**3. F1DLE** (https://f1dle.com/): "Driver Puzzle, Circuit Challenge, Car Recognition, Track Puzzle, Season Standings" — so, multiple daily-puzzle types including circuit identification (a direct F1 geography overlap with prix-guesser). WebFetch: "each puzzle is carefully crafted to be challenging yet accessible." Public deployment. **Notably, no visible unofficial disclaimer** on the landing page — the site "appears to present itself as an official or at least legitimate F1 puzzle platform" per my WebFetch read. This is an interesting contrast to what F1's own guidelines require (see LQ-1C.4).

**4. emcrald/F1-Driver-Wordle** (https://github.com/emcrald/f1-driver-wordle): small GitHub project, browser-based driver-name Wordle. Actually open source, but very narrow scope (single game, name-guessing only).

**5. SmCTwelve/f1-bot** and **andrerfcsantos/f1-discord-bot**: Discord bots using the Ergast API and FastF1 library (Python, Pandas, matplotlib). Not game frameworks — they are data-display bots. Prior art for the *data integration* axis but not the game/room/content axis.

**6. CorrosiveKid/fantasy-f1-discord-bot**: leaderboard display for the official F1 Fantasy game. Again, data display, not a game.

### What the F1 fan game ecosystem looks like (pattern-level)

Looking across these: the existing F1 fan game ecosystem is almost entirely **single-player daily-puzzle** in shape (Formudle, Stewardle, F1DLE, Driverle, driver Wordles). I found zero examples of an F1 fan game whose shape is *private-room multiplayer with host-screen watchability*. The circuit-identification puzzle in F1DLE is the closest overlap with prix-guesser's anchor mode, but it is shaped as solo daily puzzle, not as a social game night.

**This is a significant, unanticipated finding.** Prix-guesser's stated product — "F1 GeoGuessr for game nights" — appears to occupy an **unoccupied niche** within the F1 fan game ecosystem. The existing prior art is daily-Wordle-shaped, not party-game-shaped. The project-fit implication: prix-guesser cannot learn its distribution model from existing F1 fan games because existing F1 fan games are not distributing the same thing (solo daily puzzles are a fundamentally different distribution beast than private-room party games).

### Content-authoring model across F1 fan games

None of the F1 fan games I found expose their content authoring in an inspectable way. The daily-puzzle sites are almost certainly hand-curated per day by their authors, but I could not find documented content schemas, open authoring pipelines, or community contribution systems. This is another negative result: **there is no F1-specific authored-content-model prior art** I could locate for prix-guesser to borrow from. The content-shape work in Phase 01 is genuinely frontier relative to F1 fan games, even though it is well-trodden relative to generic quiz tools (PBLive, ClassQuiz).

### Licensing posture across F1 fan games

Not a single one of the F1 fan games I looked at visibly carries the F1-required "unofficial" disclaimer in what I could see from their landing pages via WebFetch or search summaries. F1DLE specifically "contains no disclaimer about being unofficial." Formudle and Stewardle similarly don't appear in search summaries as carrying disclaimers. This is a strong negative signal: **the live F1 fan game ecosystem is operating in technical violation of F1's own stated guidelines**, and has been doing so publicly without visible enforcement. Whether that is because F1 selectively enforces, doesn't care about puzzle-genre games, or simply hasn't noticed is outside my research. See LQ-1C.4 for the load-bearing consequences.

### Verdict for LQ-1C.3

- **Authored-content prior art specifically for F1: absent.** This is a negative finding, not a null result. Prix-guesser is doing something other F1 fan games have not done in the shape it is doing.
- **Game-shape prior art specifically for F1 private-room party games: absent.** The niche is unoccupied.
- **Distribution-model prior art from F1 fan games: ambiguous.** The existing sites are public-facing and appear to ignore F1's unofficial-disclaimer requirement without consequence, which could either validate a "ship and see" posture or be a trap that hasn't sprung yet.

**"I don't know yet" marker:** I don't know whether F1's brand-protection team has ever sent a C&D to a daily-puzzle fan site. A more directed search on legal databases or community forums (plonkit.net-style sources but for F1) would be informative. That's a Wave 2 candidate.

---

## LQ-1C.4 — The "private-only fan project" framing as a pattern

This is the highest-leverage question, per the task spec, for the user's stated concern about deployment/distribution/adoption.

### What I searched

- "private-only indie game development deployment hosting friends distribution pattern"
- "hobby project scope creep private friends outgrew unexpected adoption retrofit distribution"
- "friends only game project viral unexpected shared onboarding lessons learned"
- "small web game self-host friends accidentally popular deployment lessons"
- "hobby project success retrofit scalability monetization friends users blog essay"
- "ship early YAGNI multiplayer infrastructure later refactor cost small team"
- "unofficial fan game cease and desist F1 Nintendo private distribution"
- "Formula 1 trademark fair use fan project unofficial game guidelines 2024"
- "F1 trademark private use fan project infringement non-commercial"

### What I found

**1. F1's own guidelines explicitly legitimize the "private-only" framing.** (https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt — verified via WebFetch)

Verbatim passage from WebFetch:

> "Limited use of our Other Intellectual Property Rights for educational purposes may be acceptable where the use is justified, limited, and non-commercial. However, please note, this does not include public postings such as YouTube, websites and social media. It must be for a private, educational purpose only."

And:

> "Motorsport simulators and/or software that simulates auto racing (including those that are digital only or those that incorporate physical elements such as racing car chassis) should not make any use of the FORMULA 1 Rights without an express written license."

**This is a load-bearing finding.** Prix-guesser's "private-only" framing is not just a YAGNI posture — it is the **exact framing F1's own trademark policy carves out as permissible**, provided the use stays (a) non-commercial, (b) private, (c) not posted on public YouTube/websites/social-media. The moment prix-guesser extends to public hosting — even a free public Docker image on GitHub that strangers can run — it exits the F1-sanctioned zone, and the brand-protection team's written policy says "no use without express written license."

Read against the user's concern ("we haven't considered enough how we deploy at scale, or distribute, or advertise, or make it easy to adopt/share"), this inverts the framing. The user is worried that "private-only" is under-considering distribution. But **F1's own policy turns "private-only" into a legal requirement, not just a product posture.** Distributing prix-guesser at scale means either (a) getting an express written license from F1 (extremely unlikely for a fan project), (b) using only non-infringing content (probably possible — track layouts are less protected than logos and driver names), or (c) accepting direct legal exposure. The prix-guesser canon's "private-only" posture is therefore **defensible by reference to an external policy constraint**, not only by reference to YAGNI scope management. Lane 1B should check whether the canon currently makes this legal rationale explicit or whether the private-only framing reads as purely scope-management — if it's the latter, the canon is under-leveraging the strongest available defense of the posture.

**2. The broader fan-game legal reality validates this.** (https://odinlaw.com/blog-fan-games-legal-risks/ — verified via WebFetch)

Verbatim passage:

> "any fan project that uses these elements without permission may infringe, regardless of whether it is distributed for free... Even free distribution can be subject to takedowns."

And on private vs public:

> "The article provides no meaningful distinction between private, non-commercial, or friends-only distribution... The blog treats all unauthorized uses as legally equivalent under copyright and trademark law. The article doesn't suggest that private distribution eliminates legal exposure. Instead, it notes that rights holders may simply choose not to enforce, while preserving their legal right to do so."

So the legal literature says "free ≠ safe," but also says rights holders' enforcement is discretionary — which is consistent with the F1DLE/Formudle/Stewardle reality of public F1 fan games operating unchallenged. The effective posture is not "private-only is legally necessary" but rather "private-only substantially reduces the surface area at which enforcement decisions would be made." That's a real, measurable risk reduction even if not a formal legal shield.

**3. I did NOT find specific writeups of private-only fan projects that grew unexpectedly and had to retrofit distribution.**

Multiple searches came up dry:
- "hobby project scope creep private friends outgrew unexpected adoption retrofit distribution" — returned generic scope-creep management content.
- "friends only game project viral unexpected shared onboarding lessons learned" — returned unrelated onboarding-for-new-hires content.
- "small web game self-host friends accidentally popular deployment lessons" — returned general self-hosting guides.
- "hobby project success retrofit scalability monetization friends users blog essay" — returned generic monetization content.

**Negative result, honestly reported.** I was unable to find the genre of postmortem the task spec asked about. This is genuinely "I don't know yet" — I don't know whether the phenomenon is rare, whether it's rarely written up, or whether my search queries were wrong-shaped to surface it. I am *not* going to manufacture findings by cherry-picking generic scope-creep advice and pretending it addresses the specific "private fan project that unexpectedly grew" question.

**4. Generic YAGNI literature is consistent with the "private-only is defensible" reading.** (https://martinfowler.com/bliki/Yagni.html and others via search)

Verbatim-summarized: YAGNI discourages speculative features built "just in case." The standard framing is: build for current need, refactor when new need arrives, don't prematurely optimize for scale that may never materialize.

Project-fit for prix-guesser: the canon's private-only framing is consistent with mainstream YAGNI practice. What YAGNI *does not* answer is the specific question the user is raising — "what if the current-need-shape and the future-growth-shape are structurally different, such that the refactor path is not smooth?" That's not a YAGNI question; it's a **reversibility question**. Reversibility is absent from the YAGNI literature I found.

**5. The most honest framing I can offer.** The user's concern about "deployment, distribution, advertising, adoption" has three components with different epistemic statuses:

- **Legal/licensing:** The private-only framing is the *strongest* available defense and is directly supported by F1's own guidelines. The user's concern is **not** justified here — private-only is not under-considering, it's actively leveraging F1's permitted fan-use carveout.
- **Scope management / YAGNI:** The private-only framing is mainstream YAGNI practice. The user's concern is **partially justified** here because YAGNI literature does not address reversibility, and prix-guesser's canon (from what I read of it) does not explicitly name what the reversibility path looks like — the "refactor distribution later when needed" step is assumed rather than designed.
- **Product adoption / friends-sharing-with-friends:** This is where I could not find evidence either way. The negative search result for postmortems of fan projects that outgrew themselves is real — either the phenomenon is uncommon for the genre, or it's uncommon to write up, or my search approach missed it. **"I don't know yet."** The user's concern here is neither confirmed nor disconfirmed by what I can see.

### Verdict for LQ-1C.4

"Private-only fan project" is:

- **Not** a known evasion anti-pattern in any literature I found.
- **Not** a named healthy framing either, in any specifically-theorized way — it's more of an unlabeled default that YAGNI-shaped defaults land on.
- **Specifically legitimated by F1's own trademark guidelines** as the one narrow carveout for educational/fan use. This is the single most important finding in this entire lane for the user's stated concern.
- **Under-documented** as a deliberate strategic choice — the prix-guesser canon (from my light skim) frames it as scope management, not as a legal-risk reduction posture. Making the legal rationale explicit would strengthen the posture substantially.
- **Structurally silent on reversibility.** The canon says "private-only for now" but does not, from what I saw, describe the specific shape of the transition if "now" ends. This is the legitimate core of the user's concern, and I think the user is right to raise it, even though I was unable to find external evidence of how other projects made or failed to make that transition.

**"I don't know yet" markers:**
- I don't know whether fan-project-outgrew-itself postmortems exist and I missed them, or whether they don't exist.
- I don't know whether F1 has ever enforced against puzzle-genre fan sites like F1DLE.
- I don't know the specific technical reversibility cost (private → public) for the prix-guesser stack because that depends on Phase 2+ architecture decisions that haven't been made yet.

---

## LQ-1C.5 — Anything else the search surfaced

The task spec asked me to be alert for unanticipated findings. Here is what I found that didn't fit the pre-named questions:

### Finding A: Prix-guesser occupies an empirically unoccupied niche in the F1 fan game ecosystem

The existing F1 fan game ecosystem (Formudle, Stewardle, F1DLE, Driverle, Who Are Ya?, etc.) is almost entirely single-player daily-puzzle. I found no private-room-multiplayer-party-game F1 project. Prix-guesser's "F1 GeoGuessr for game nights" shape is genuinely novel within the F1 fan ecosystem, even though the underlying shape (private-room party game) is well-established in the broader party-game ecosystem.

**Implication for the project:** the distribution/adoption challenge for prix-guesser is *not* "how do we differentiate from the existing crowded F1 fan game space" — the space is not crowded for this shape. It's "how do we introduce a party-game-shape into a fan community that has been trained by the existing ecosystem to expect solo daily-puzzle-shape." That's a different problem than the user's concern framed, and it may partially answer it: the adoption question is less about distribution infrastructure and more about shape-education.

### Finding B: F1's trademark carveout for private educational fan use is the strongest defense the canon is currently not fully leveraging

Addressed in LQ-1C.4 but deserves its own mention as an unanticipated finding. I went into the research expecting to find that "private-only" was a sloppy YAGNI default. I came out finding that it's directly supported by an external legal constraint the canon may not be explicitly citing. This is the single finding I most want the synthesizer to engage with.

### Finding C: The "host screen is a role, not just a client" architectural reframe from Party-Box

Addressed in LQ-1C.1 but worth highlighting here because it's a vocabulary find. Prix-guesser's current vocabulary (from `.planning/PROJECT.md` lines 46–49) distinguishes:
- anchor mode
- session wrapper
- watchability layer
- platform shell

Party-Box's three-role split (Broker / Game / Client) is a subtly different frame that directly names the watchability layer as a first-class participant with its own network identity. In prix-guesser's current vocabulary "watchability" is a *layer* (a quality of how the session wrapper renders); in Party-Box's vocabulary the equivalent is a *role* (the big-screen node). Whether this is worth importing is a judgment call, but it's the kind of vocabulary distinction that changes what you notice when reasoning about authority and reveal flow.

### Finding D: PBLive as prior art is archived

This was not predicted by the task spec but matters: the single closest architectural prior art I found for the Phase 01 YAML-content-contract work is a project that existed, worked, and was then archived by its maintainer. I do not know why it was archived. But "the thing we are choosing to build stopped being maintained by the person who tried it" is a risk signal worth looking into. This is a Wave 2 candidate.

### Finding E: The Geotastic free-tier monetization strain

Also not predicted. Geotastic is the closest product-model prior art (private lobbies, themed community maps, account-less guest join) and it ran into monetization strain in 2024 according to an author Medium post I surfaced but didn't deep-read. If the economic model for "friends-private-lobby geography game with community content" is structurally hard to sustain, that's informative for prix-guesser's M2/M3 thinking even though the current milestone is M1.

---

## What I didn't look at (exploratory obligation: partiality)

Explicit list of what I did not research, with reasoning:

- **Context7 MCP / npm package metadata.** I had it available and did not invoke it. I chose WebSearch-first because the questions in the task spec are mostly about ecosystem-level alternatives and pattern recognition, not specific package versions or API surface. If the synthesizer wants version-pinned or API-specific answers for any of the frameworks I named, Context7 would be the right follow-up tool.

- **The prix-guesser canon in depth.** I read PROJECT.md, the vision-alignment initiative README, and about the first 250 lines of the Phase 01 research file. I did not read the full Phase 01 research, the canon docs Lane 1A is re-verifying, the pre-execution audit Lane 1A is re-verifying, any discovery/* file, AGENTS.md, LONG-ARC.md, REQUIREMENTS.md, ROADMAP.md, or the f1-modeling comparison files. This was deliberate per the lane boundaries. My project-fit judgments are consequently shaped by a thin read of the project, and some of them might sharpen if I had read more deeply.

- **PBLive's commit history / issue tracker / archive reasoning.** I noted it's archived. I did not dig into *why*. This is a Wave 2 follow-up candidate.

- **Geotastic's free-tier monetization article.** I surfaced it but did not deep-read it. Wave 2 candidate.

- **F1's enforcement history against public F1 fan games.** I searched generically for "F1 trademark cease and desist fan game" and found no specific F1 cases (the results were dominated by Nintendo). I did not search legal databases, community forums, or archived DMCA notices. This is a Wave 2 candidate if the synthesizer wants a harder read on legal risk.

- **Gartic Phone's architecture specifically.** I found a community Angular/Firebase clone but did not deep-read it. The architecture details of how Gartic Phone handles private rooms with 4–30 players could be useful prior art for the prix-guesser room/party-size design, but I did not pursue it.

- **Boardgame.io's current state.** One of the three explicitly named references in prix-guesser's research, but I did not re-verify whether it's still maintained in 2026 or what its current feature set is. Lane 1A might touch this; I did not.

- **Any non-English game-dev literature.** All my searches were in English.

- **Anything about the *practice* of running game nights — the game-design literature as distinct from the game-tech literature.** The task spec's framework-invisibility flag specifically warned that the most important alternatives might live in the game-night practice literature rather than the framework/content/F1 categories. I did not search this literature at all, because the keyword hit rate was too low in my early searches to justify. This is a real gap in the lane's coverage and I am naming it explicitly rather than pretending I covered the framing.

- **Academic research on fan games, community games, party games as a genre.** Possibly informative for LQ-1C.4 but outside the time budget.

---

## What the exploration opened (exploratory obligation: named openings)

New questions / directions / possibilities surfaced but not pursued:

1. **Why was PBLive archived?** If the maintainer publicly explained the decision, that explanation is directly informative for prix-guesser's Phase 01 shape choice.

2. **Is there a game-design literature on the "shape transition" from solo-daily-puzzle to private-room-party-game?** Prix-guesser appears to be introducing a new shape into the F1 fan ecosystem; the shape-introduction question is a design question, not just a tech question.

3. **Does F1's brand-protection team's selective enforcement against fan games follow a pattern?** The existence of F1DLE, Formudle, Stewardle, etc. operating unchallenged suggests puzzle-genre games may be de facto permitted. Whether prix-guesser's party-game shape falls in the same de facto zone is a real question.

4. **What would the "reversibility design" for private → public look like?** The user's concern about deployment/distribution/adoption is, read charitably, a concern that the reversibility path is not designed. A Wave 2 or Phase 1.5 exercise could be "sketch the minimal deploy topology for public-but-low-scale hosting, even if we don't build it, just to confirm the private-only shape is reversible cheaply."

5. **Is there a "Broker/Game/Client three-role" vocabulary worth importing?** Specifically as a refinement of the current "watchability layer" vocabulary. This is a small but real linguistic find.

6. **Does the "host account, account-less guests" pattern (from Geotastic) map cleanly onto prix-guesser's stated posture?** It looks like it does and is probably the single most adoption-friendly identity model for the friends-private use case. Currently not explicitly named in the canon from what I read.

7. **What does the community-content-authoring path look like if M2 "Play Anytime, Anywhere" succeeds?** GeoGuessr's "A Community World" (100k+ locations, 100+ contributors) is an existence proof that community authoring can reach depth, but prix-guesser's authored-content contract is currently designed for a single-author workflow. The contract probably can extend to community authoring without breakage (that's what D-12 ensures), but the extension path is not designed yet.

---

## What I found that I wasn't looking for (exploratory obligation: unanticipated findings)

1. **F1's own trademark guidelines actively legitimize the "private-only" posture.** I expected to find that private-only was a sloppy YAGNI default; I found instead that it's the explicit carveout in F1's policy document. This completely inverts the framing for LQ-1C.4.

2. **The F1 fan game ecosystem is empirically niche-shaped.** I expected to find lots of prior art and to have to filter it. I found that nearly all existing F1 fan games are solo daily-puzzles and that the private-room party-game shape is empirically unoccupied. This is an opportunity-framing finding, not the gap-finding I was dispatched for.

3. **PBLive exists and was archived.** I expected to find that the YAML-authored quiz content contract was prix-guesser's own architectural invention. It isn't. It's well-trodden territory, and the most direct precedent is archived without explanation.

4. **Existing public F1 fan games operate without the disclaimer F1's own policy requires.** This is either a useful data point about how enforcement actually works, or a trap that hasn't sprung. Either way, it's an informative reality check on the assumption that "public hosting = takedown."

5. **Rocketcrab's iframe-launcher abstraction sidesteps problems Colyseus/PartyKit don't even name.** I expected to compare room frameworks head-to-head. I found that the most interesting structural alternative lives *above* the room framework level, not parallel to it.

---

## Rule 5: Frame-Reflexivity

The three verbatim grounding questions from the task spec:

### 1. "If this lane had been classified with a different orientation (e.g., investigatory instead of exploratory), what would I have looked for that I didn't?"

If this lane had been investigatory — testing a specific hypothesis like "prix-guesser's research missed framework X" or "the private-only framing is an anti-pattern" — I would have done directed searches aimed at confirming or disconfirming that hypothesis. I would have evaluated each finding more adversarially. I probably would have spent more time on GitHub stars/commit counts/issue trackers to quantify maintenance signals, and less time on reading landing pages to extract vocabulary. The directed posture would have sharpened my PBLive finding (I would know concretely whether to say "archived therefore failed" or "archived therefore stabilized") but it would have cost me the Finding A "niche is empirically unoccupied" result, which I stumbled into rather than searched for.

Concretely: an investigatory version of this lane would have produced **fewer** findings but each finding would have been more rigorously defended. The exploratory version produces more findings with wider error bars, which is the correct tradeoff for the lane's position in the audit (it feeds into Wave 3 synthesis, which is where rigor can be layered on top).

### 2. "If this lane had been given a named subject (e.g., comparative_quality against a specific named alternative), what would I have looked for that I didn't?"

If the lane had been given, say, "comparative_quality against Hackbox" as its subject, I would have read Hackbox's entire codebase (not just its README), run it locally, compared its type contract to prix-guesser's D-01 through D-12 schemas line by line, and produced a structured gap analysis. I did none of that. What I produced is surface-level: "Hackbox exists, has the right shape, is MIT licensed, and has the host-screen vocabulary prix-guesser lacks." That's fine for a lane whose output is reference-finding, but a named-subject version would have generated directly actionable adoption/no-adoption calls. If the synthesizer wants adoption calls rather than reference pointers, the follow-up is a named-subject Wave 2 lane per framework I flagged.

The converse is also true: a named-subject lane would have completely missed anything outside its named subject. I would not have found Finding A, Finding B, or Finding E under a named-subject framing because those findings came from search queries that weren't aimed at any specific named target.

### 3. "What about the current classification shapes what I am prepared to notice and what I am not? Name one concrete example."

The "find what they missed" framing orients me toward absences. Concretely: my instinct throughout this lane was to ask "what is missing from prix-guesser's research?" That framing made me well-prepared to notice Hackbox (missing framework reference), PBLive (missing content-model precedent), and the F1 guidelines carveout (missing legal justification for the posture). It made me **poorly** prepared to notice what is *load-bearing in prix-guesser's research as it stands* — specifically, what the existing Colyseus/boardgame.io/geohub reference set accomplishes that would be lost if replaced.

Concrete example of the blind spot: the prix-guesser canon's reference to `boardgame.io` specifically (as opposed to Colyseus or PartyKit) is probably load-bearing for the *game-state-as-a-tree* mental model that the Phase 01 authored round contract implicitly inherits. Rounds-with-clue-ladders-with-reveal-steps is naturally tree-shaped, and boardgame.io's architecture assumes tree-shaped game state. If prix-guesser replaced its references wholesale with Hackbox and Rocketcrab (which I just argued are closer to its shape), it would lose the tree-shaped-state framing without necessarily realizing it. I am only able to see this blind spot *now*, at the end of the lane, because I'm writing the frame-reflexivity section and being forced to ask what I wasn't prepared to notice. The "find what they missed" frame would never have surfaced it on its own.

**This is the single most important thing Rule 5 did for this lane.** Without it, my findings would have been a list of things prix-guesser should add, with no engagement with what the existing research is doing right that the additions might disturb. With it, I can flag to the synthesizer that the existing references are not just an incomplete list — they encode a mental model (tree-shaped authoritative state + authored-first content + generic-framework-pluggability) that the "missed alternatives" I surfaced would partially disrupt if adopted without care. The correct synthesis is probably "add these as references, don't replace with them."

---

## Framework invisibility (cross-cutting obligation)

> "Name a concrete finding that would not appear no matter how rigorously this audit was conducted, because of how this audit's scope was framed."

**The most important alternative prix-guesser may have missed is not a framework, not a content model, not a fan-game precedent, and not a deployment pattern. It is a pre-implementation playtesting practice.**

The lane's framing is "alternatives in rooms / content / F1 / private-only-pattern." This framing cannot surface: "the alternative to freezing the authored content contract in Phase 01 is to freeze the authored content contract in Phase 02 and run three manual game-night sessions with paper clue ladders and a whiteboard reveal in Phase 01 first, to discover what the contract actually needs to encode before committing to a shape." That is a methodological alternative, not a framework/content/F1/posture alternative. It would not appear under this lane's framing no matter how rigorously I searched, because none of my keyword queries were shaped to surface it.

I want to flag this specifically because it matches the user's expressed concern pattern. The user's concern is "we haven't considered enough how we will deploy, distribute, advertise, adopt." That's a concern about *what happens after we build*. The symmetric concern is "we haven't considered enough what we learn before we build" — and that concern does not appear in any of the lane's investigatory questions. It's invisible to this lane's frame. If the synthesizer is assembling findings for Phase 01 go/no-go, the pre-build playtesting alternative is the one I can name the frame won't surface.

A secondary framework-invisibility finding: **"private-only as a content-authorship practice, not just a distribution posture"** is invisible to this frame. The canon's "private-only" language is about who can play. But the deeper consequence of private-only is about who can *author* — if the corpus is private, the community-author path (GeoGuessr's 100k community locations) is structurally closed. I surfaced the community-authoring question in "What the exploration opened" but the lane's framing does not treat it as a first-class concern. It's peripheral to the questions I was asked, but it may be central to the questions the project actually needs to answer for M2.

---

## Rule 4: What the obligations didn't capture

The lane's obligations instructed me to find alternatives, judge their project-fit, and surface unanticipated findings. Here is what the obligations did not capture and what I would say if I could step outside them:

1. **The predecessor audit's mandate-shape.** The task spec mentions that a 2026-04-08 predecessor audit said "Colyseus vs PartyKit is NOT neutral from a distribution standpoint" and that the "answer-target hierarchy is THE most important architectural decision." I did not re-verify these claims (Lane 1A's job). But they suggest the predecessor audit had opinions. The way the current task spec is framed — "find what's missing" — treats the predecessor audit's opinions as an implicit baseline. A more honest framing might be: "the predecessor audit had strong opinions about what matters, those opinions shape what the current research considers, and one alternative to name is 'don't inherit the predecessor audit's framing at all and re-derive the question set from current project needs.'" That would be a methodological alternative I could not surface within the lane's framing.

2. **The empirical base rate of this kind of exercise.** I'm an audit agent doing gap-finding research. I don't actually know whether gap-finding research of this kind reliably improves project outcomes, or whether it's a formality that produces findings that sit in audit files. If the honest answer is "this kind of audit often surfaces findings that are never incorporated," then the load-bearing question isn't "what did I find" but "what is the incorporation path for any finding I make." The obligations don't ask me this question, and so the findings above sit in a file with no named integration step.

3. **My own framing bias toward naming things.** I'm trained to produce concrete deliverables and I have a bias toward naming specific alternatives (Hackbox, PBLive, Rocketcrab). The honest alternative to naming specific alternatives might be: "don't add any new references to the canon; instead, deepen engagement with the three references already there (geohub, Geo-Locator, react-geofindr) until the engagement is actually load-bearing." I suspect the existing references are *under-engaged* in the canon — they're named in PROJECT.md line 67–73 as "already studied" but I don't know from my light read whether the study is actually informing the Phase 01 shape. That's a Lane 1A or Wave 3 question, not mine, but I want to name that my instinct to add things may be wrong if what's actually needed is deeper engagement with what's already there.

4. **The emotional/motivational axis.** The user's concern about "adoption" includes the informal concern "will my friends actually want to play this." That's not a framework question or a content-model question or a legal question. It's a social/motivational question. Nothing in this lane's research addresses it. The best reality check on whether prix-guesser's shape works is running a game night with the paper-and-whiteboard Phase 01 prototype I gestured at in the framework-invisibility section. The obligations don't ask about this and I can't investigate it from a WebSearch seat.

---

## Cross-Lane Notes for the Synthesizer

- **For Lane 1A (canon integrity):** the F1 guidelines finding in LQ-1C.4 is the load-bearing external validation of the "private-only" framing. Lane 1A should check whether the current canon explicitly cites this legal carveout as the reason for the private-only posture, or whether it cites scope-management / YAGNI reasoning only. If the latter, the canon is under-leveraging its strongest argument. Quote to use: `https://www.formula1.com/en/information/guidelines.4EOKE9RRqevL4niTK9kWyt`, passage on "limited use... private, educational purpose only" and "motorsport simulators... should not make any use of the FORMULA 1 Rights without an express written license."

- **For Lane 1B (methodological inheritance):** the Finding A "empirically unoccupied niche" observation is relevant to whether prix-guesser should inherit the same research lanes f1-modeling did. The f1-modeling project (per Lane 1B's scope) is presumably about F1 data modeling. Prix-guesser is about F1 *party game shape introduction into a daily-puzzle-dominated ecosystem*. If Lane 1B is checking whether prix-guesser inherits vision-alignment structure from f1-modeling, my finding adds a consideration: the domains are structurally different, not just product-different. Data modeling in a well-trodden domain (F1 stats) has very different uncertainty shape than shape introduction in a barely-trodden domain (F1 party games). The research-lane structures should probably differ accordingly.

- **For Wave 3 synthesis:** the three biggest findings I want engaged with are, in order of importance:
  1. The F1 guidelines carveout legitimizes private-only as a strategic posture (LQ-1C.4).
  2. PBLive exists as near-exact prior art and is archived for reasons I don't know (LQ-1C.2).
  3. The F1 fan game ecosystem is empirically niche-shaped and prix-guesser occupies an unoccupied shape (Finding A).

- **For the orchestrator's scope management:** I did not address the user's concern about "deployment, distribution, advertising, adoption" directly. I addressed the legal-subcomponent of it (private-only is legitimated) and the adoption-subcomponent ("maybe the adoption challenge is shape-education not infra"), but the deployment/distribution infrastructure subcomponent remains open. A dedicated "deployment reversibility sketch" exercise would close it; this lane could not.

---

## Candidates for Wave 2 follow-up

In descending priority order:

1. **"Why was PBLive archived?"** — Single question, can be answered by reading the repo's issue tracker and commit history. ~30 minutes of work. Directly informs the Phase 01 shape choice.

2. **"Does the prix-guesser canon explicitly cite F1's fan-use carveout as the reason for private-only?"** — If no, a 1-2 sentence addition to the vision/rationale docs makes the posture much more defensible. This is a Lane 1A scope extension more than a Wave 2 lane of its own, but flagging it here so it doesn't get lost.

3. **"What does the deployment reversibility path look like for private → public (even if we don't build it)?"** — A short design exercise, not a research exercise. Would directly address the remaining open subcomponent of the user's concern.

4. **"Deep evaluation of Hackbox and/or Rocketcrab as a candidate Phase 2 room substrate"** — Named-subject comparative lane, higher rigor than I could give in an exploratory lane. Only worth doing if the synthesis stage decides the room question is actually open.

5. **"F1 enforcement history against puzzle-genre fan games"** — A more directed legal-history search, probably worth doing only if the project considers relaxing the private-only posture.

6. **"Game-night practice literature"** — The framework-invisibility flag's alternative category. Worth a dedicated exploratory lane specifically framed around "what should happen before the authored content contract freezes" rather than "what should the contract look like."

7. **"Community-authoring path design for M2"** — Not urgent for Phase 01 but the substrate decisions made now constrain this later, and naming it as a deferred question keeps the constraint visible.

---

## Meta-reflection

This lane surfaced roughly what I'd expect an exploratory external-research pass on 2-3 hours of WebSearch time to surface: a small number of load-bearing finds (the F1 guidelines carveout, PBLive as prior art, the empirically unoccupied niche), a larger number of reference-value finds (Hackbox, Rocketcrab, Party-Box, Geotastic, "A Community World"), and a meaningful set of explicit "I don't know yet" conclusions. The load-bearing finds are the ones I hope Wave 3 engages with; the reference-value finds are worth mentioning in the synthesis only if they serve a specific point; the "I don't know yet" conclusions are markers for Wave 2.

The thing I am most uncertain about is whether my light read of the prix-guesser canon is sufficient to judge project-fit well. Several of my "promising alternative" calls might soften or sharpen with deeper canon engagement. The synthesizer should treat my calls as directional, not final.
