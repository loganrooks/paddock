# Research TODOs

Research questions surfaced during brainstorming. Framing: not "is this possible?" but "is it possible to make this possible, and how?"

---

## R1 — Stewards' Room content sourcing
**Serves**: Stewards' Room, Team Principal's Desk
**Question**: Where do structured steward decisions live? FIA documents, race reports, fan archives? What format are they in? Can we extract incident + decision + context programmatically, or does it require hand curation?
**Why it matters**: These modes need incident descriptions, the actual decision/outcome, and enough context for players to form opinions. If sourcing is manual-only, the content well is shallower than it looks.

## R2 — Audio clip sourcing and legal posture
**Serves**: Words of Wisdom audio reveals, commentator clip identification
**Question**: What's the legal position on using short clips from F1's BROADCAST PRODUCTION (commentary audio, produced team radio feeds that go through FOM's audio mix) in a fan game? Fair use/fair dealing for short clips in transformative context? Distinction between private and commercial use?
**Why it matters**: The legal question is specifically about FOM's broadcast content — not about ambient/fan-recorded audio like engine sounds or crowd noise (those are sounds in public spaces, no rights issue). Commentary and produced radio are the things that need actual legal thinking. If short broadcast clips are defensible, WoW audio reveals and commentator ID games unlock. If not, we design around text and fan-recorded audio only.

Note: engine/car sounds, crowd noise, trackside audio = **not a licensing concern**. Fans record and share these freely. The sourcing question for those is practical (clean labeled files, distinctiveness), not legal. See [R4](#r4).

## R3 — Live/reactive content curation pipeline
**Serves**: Race Weekend Mode, post-race reactive rounds
**Question**: What would a fast-turnaround curation pipeline look like? AI-assisted draft from race data + radio transcripts + steward docs → human review → publish? What's the minimum turnaround time? What's the operational commitment (hours per race weekend)?
**Why it matters**: The live-calendar dimension is the strongest retention loop candidate, but it requires someone (or something) producing curated content on a race-weekend cadence. If that's 10 hours of work per race, it's a different commitment than if it's 1 hour of review on AI drafts.

## R4 — Engine/car sound distinctiveness
**Serves**: Sound-based identification games
**Question**: Are modern F1 cars acoustically distinct enough for a game? (V6 turbo-hybrid era cars sound similar.) Are historical eras more distinct? Do circuits have distinctive acoustic signatures (tunnel at Monaco, crowd noise patterns)? Is there existing fan content (videos, compilations) that tests this?
**Why it matters**: "Identify the car from engine sound" is a compelling concept but may not work if the cars literally sound the same. Need to know if the game mechanic has a foundation before designing around it.

## R5 — Image/visual content sourcing for non-geography modes
**Serves**: Rate the Fit (paddock fashion), car livery identification, historical era visual modes
**Question**: What are sources for paddock photos, livery images, historical F1 photography? What's the rights situation for fan-game usage? Are there open/permissive archives, or is everything Getty/Sutton locked down?
**Why it matters**: Several fun mode ideas (fashion rating, livery identification, era-based visual rounds) need curated images. If images are harder to source than text, that changes the sequencing calculus.

## R6 — Cooperative real-time game mechanics in browser
**Serves**: Pit stop co-op, Grid Walk (information asymmetry)
**Question**: What does real-time cooperative play require technically in a browser-first, phone-as-controller architecture? WebSocket latency, synchronization of timed actions across devices, what frameworks/libraries exist? How does Jackbox handle this (they do timed cooperative rounds)?
**Why it matters**: The pit stop co-op and Grid Walk are structurally different from turn-based or independent-answer modes. They need tight synchronization. If the technical cost is high, they're M2+ modes, not M1.

## R7 — Strategy dilemma content sourcing
**Serves**: Team Principal's Desk
**Question**: Where do detailed race strategy breakdowns live? F1 timing data, fan analysis sites (e.g., f1-tempo, racefans strategy articles), F1TV data feeds? Can we extract "decision point + options + actual outcome" structures?
**Why it matters**: Strategy dilemmas need real data — tire ages, gaps, weather, pit window — to feel authentic. If we can source structured race-moment data, this mode writes itself. If it's all narrative reconstruction, it's more editorial work.

## R9 — BoxBoxd social features deep read
**Serves**: Competitive landscape, social layer design, differentiation strategy
**Question**: What does BoxBoxd's social side actually look like? The B8 research focused on game modes and missed the social networking dimension entirely. User reports: race reviews, daily surveys, opinion polls, accounts, following, posts — "a whole Twitter thing." How deep does this go? Is the social layer the primary engagement driver or secondary to the games? What's the interaction pattern — feed-based, comment-based, reaction-based? How does it integrate with the game modes?
**Why it matters**: Our competitive differentiation story was built on "BoxBoxd has no social architecture" — which is wrong. We need an accurate picture before we can identify what social territory is genuinely unoccupied. The party/group social texture might still be distinct from BoxBoxd's individual/feed social texture, but we can't assume that without seeing what they actually built.
**Priority**: HIGH — this corrects a foundational assumption in our competitive analysis.

## R10 — Browser 3D / Three.js feasibility for PS1-style game
**Serves**: Verstappen Game (all variants)
**Question**: What does a PS1-style 3D browser game actually require? Three.js vs Babylon.js vs other options. How do existing PS1-aesthetic browser games handle: low-poly rendering, PS1 shaders (vertex snap, affine textures, fog), phone-as-controller input latency for real-time movement, WebSocket game state sync, positional audio? Are there starter templates or existing projects to build from? What's the realistic dev effort for a single-circuit prototype of each variant (running on foot vs. car racing)?
**Why it matters**: The Verstappen game is the most technically distinct mode in the brainstorm — it's real-time 3D, not form-submission party game. Need to know whether it's a weekend spike or a multi-month project, and whether the 3D tech stack can coexist with the 2D party game stack or needs to be a separate module/app.

## R11 — Phone-as-steering-wheel: tilt controls + latency feasibility
**Serves**: Verstappen Game, Talibantonelli/Bin Russell game, any future racing mode
**Question**: Can phone gyroscope/accelerometer tilt be used as a steering wheel with acceptable latency for real-time racing in a browser game? What's the input chain: device motion API → WebSocket → game server → host screen render, and what's the realistic round-trip latency on local WiFi? Can client-side prediction compensate? What about acceleration/braking via forward/backward tilt vs. on-screen buttons — which feels better? Are there existing browser racing games using tilt controls we can reference? What's the minimum viable prototype to test this (a phone tilting a car on a screen)?
**Why it matters**: Tilt-to-steer is the most natural "phone as steering wheel" mechanic and would make the racing games feel physical and fun. But if latency makes it unplayable or the gyroscope API is unreliable across devices, we need to know early so on-screen controls become the primary design. This is a spike/prototype question — the answer comes from building it and testing, not from research alone.
**Approach**: Build a minimal spike — phone tilt moves a car on a host screen. Measure latency. Test on multiple phone models. Determine if it's "possible to make possible" through engineering/optimization.

## R8 — Party game composition patterns
**Serves**: Platform composition (Grand Prix mode, playlist model, etc.)
**Question**: How do Jackbox, Mario Party, Warioware, and other multi-game party platforms handle session composition? What research/postmortems exist on what makes a good game-night arc? What's the host's role in pacing? How do they handle drop-in/drop-out?
**Why it matters**: We have multiple metaphors for how games compose into sessions (Grand Prix, Jackbox packs, playlists, carnival). Understanding what existing platforms learned would ground the design.

## R12 — GeoGuessr community features and UGC model
**Serves**: Community content creation, content flywheel, platform community design
**Question**: What community-created content does GeoGuessr support? (Custom maps, challenges, etc.) How do creation tools work — what can users build? How is community content discovered, rated, shared? What moderation exists? What social/community features exist beyond UGC (leagues, competitions, streamer features)? How has community content affected growth and retention? What's the content schema — how are user-created maps structured vs. official maps?
**Why it matters**: GeoGuessr is the closest reference for our geography anchor mode's community potential. Understanding their UGC model informs whether/how we open up content creation across ALL our modes (not just geography). Not to copy, but to understand patterns: what works, what doesn't, what's missing that we could do differently.

## R13 — Community content moderation patterns for game platforms
**Serves**: All community-created content across the platform
**Question**: How do game platforms (GeoGuessr, Jackbox Drawful/Quiplash, Mario Maker, Roblox, LittleBigPlanet, Dreams) handle moderation of user-generated content? Automated vs. human review? Pre-publish vs. post-publish moderation? Reporting systems? How do they handle offensive content in creative/freeform modes (drawings, text prompts)? What's the minimum viable moderation system for a small platform?
**Why it matters**: Multiple modes involve player-created content (custom circuits, WoW prompts, geography rounds, fashion themes, meme game prompts). Moderation is a requirement for any community content that's shared beyond the creator's friend group. Need to understand the spectrum from "no moderation needed for private play" to "full moderation for public sharing" and design the content pipeline to support that spectrum.

## R14 — Large-scale real-time multiplayer in browser: netcode patterns and feasibility
**Serves**: Racing games (Verstappen, Al Mer Qaedes) at scale, any real-time mode with 8+ players, online sync architecture
**Question — multi-part, may need to be split into parallel gathering tasks:**

1. **How do 50-100 player games (Fortnite, Fall Guys, PUBG) handle real-time netcode at scale?** Specifically: interest management / relevance filtering implementation, server tick rate strategies, client-side prediction + rollback at high player counts, spatial partitioning, delta compression, lag compensation. What tradeoffs do they make — what do they sacrifice for player count? How does this differ for racing (predictable movement, high-speed collision accuracy matters) vs. battle royale (unpredictable movement, lower collision precision acceptable)?

2. **What is feasible in a BROWSER specifically?** Native games use UDP (fast, lossy). Browsers have WebSocket (TCP, reliable, more overhead) and WebRTC data channels (can approximate UDP). What's the realistic player ceiling for browser-based real-time multiplayer with physics interaction? Are there existing browser games with 20+ real-time players interacting, and what stack do they use? What are the actual throughput/latency numbers for WebSocket vs. WebRTC data channels under load?

3. **What off-the-shelf multiplayer frameworks exist for browser games?** Colyseus, Socket.io, Photon, Nakama, PlayCanvas networking, others? What do they handle (room management, state sync, matchmaking) vs. what you build yourself (game-specific physics, prediction, rollback)? Which support both local and online play? Which handle the turn-based AND real-time patterns our platform needs?

4. **Client/server separation patterns for games that support both local and online.** How do games that work both locally (host device = server) and online (dedicated server) structure their code? Is there a standard pattern for "the simulation runs as a module that can be deployed locally or remotely"? How does this interact with browser constraints?

**Why it matters**: The racing games are the most technically demanding modes in the platform. Understanding the real ceiling for browser-based multiplayer determines: max player count per mode, whether certain modes need native clients, whether the PS1 3D racing vision is feasible at the scale we're imagining, and what networking infrastructure to invest in. This also directly informs the client/server separation question — probably the most architecturally load-bearing early decision for the platform.

**Note**: Some of this may require hands-on prototyping (spike) rather than desk research to get real answers. A minimal spike — two cars on a circuit, one local one remote, measure actual latency and responsiveness — might be more valuable than any amount of reading.
