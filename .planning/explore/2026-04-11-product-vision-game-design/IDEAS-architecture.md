# Architectural Surface Area

> See [IDEAS-INDEX.md](IDEAS-INDEX.md) for the global disclaimer, status key, and links to all docs.
>
> These are observations from the brainstorming about what MIGHT need early architectural consideration across the platform. They are not requirements or prescriptions. Each needs proper analysis to determine what's actually load-bearing, what can wait, and what the right approach is. Included here because the brainstorming surfaced them — the planning process owns the decisions.

---

## Display / Host Screen Architecture

The platform doesn't have ONE display model — it has multiple configurations, and each game mode supports a different subset. The brainstorming surfaced at least four:

**Configuration 1: Local Multiplayer**
- Shared display (TV/monitor/laptop, fullscreen browser) showing the spectacle/spectator view
- Phones as controllers, each showing the player's personal input UI
- Shared display and phone UIs are different views of the same game state
- The host may or may not also be a player — both need to work

**Configuration 2: Online Sync**
- No shared display. Each player on their own device (laptop, desktop, tablet, phone)
- Each player sees their OWN perspective on their main screen
- Input varies by device: keyboard + mouse, gamepad, touch, phone tilt
- Optional "stream view" URL for streamers/Discord screenshare, but not required

**Configuration 3: Online Async**
- Single player, single device, no real-time connection
- Play at own pace, scores compared later
- Some modes don't support this at all (racing, co-op, anything real-time)

**Configuration 4: Hybrid**
- Some players local (shared display + phone), some remote (own device)
- Shared display must NOT reveal hidden information (secret hunter roles) that remote players safely see on their private screen
- Hardest configuration, probably later — but shouldn't be made impossible

**How this plays out per mode (examples):**

*Al Mer Qaedes / Verstappen racing games:*
- Local: shared display = overhead/broadcast view of race. Hunter phones = racing controls + hunter-specific UI (targets, abilities). Hunted phones = racing controls + survival UI.
- Online sync: each player sees their own first-person/third-person driving view on their main screen. Hunters see role-specific overlay. Input = keyboard/gamepad/phone (player's choice). No shared display.
- Async: not supported.

*Words of Wisdom:*
- Local: shared display = the radio exchange setup, the reveal, the voting results. Phones = text input for fakes, voting buttons.
- Online sync: each player sees the setup on their own screen, types on their own device, sees reveals when everyone submits.
- Async: possible — submit your fake, come back to vote when everyone's ready (could span hours).

*Paddock Fashion:*
- Local: shared display = the fashion show catwalk, theme reveals, voting results. Phones = drawing canvas.
- Online sync: each player draws on their own screen, fashion show displays on everyone's screen simultaneously.
- Async: possible for creation (draw your outfit whenever), sync needed for the fashion show reveal moment.

*Geography:*
- Local: shared display = the image/clue, the map reveal. Phones = map interaction (pan, zoom, pin placement).
- Online sync: each player sees the image and their own map on one screen.
- Async: fully supported — play the round, submit, compare later.

**The architectural observation:**
The same game STATE drives all configurations — positions, scores, answers, roles, timers. The PRESENTATION diverges based on play context. This suggests a separation:
- **Game state layer**: the simulation, context-agnostic. Doesn't know how it's displayed.
- **View layer**: how a particular screen renders the state. Multiple views can coexist (shared display + N phone views in local; N individual full views in online sync).
- **Input layer**: translates raw device input (touch, keyboard, tilt, gamepad) into abstract game actions ("steer left", "submit answer", "vote for player 3"). The game state receives actions, not raw events.
- **Mode manifest**: each game mode would declare which configurations it supports and describe what each view/input setup looks like.

Whether this separation is the right approach, how deep it goes, and what M1 actually needs vs. what can be deferred — all need proper deliberation. The brainstorming observation is just: if M1 hardcodes "shared display + phone controllers" as THE architecture rather than one configuration, every future play context may require significant rearchitecting.

---

## Room / Session Join Flow

How players connect to a game. The first interaction anyone has with the platform.

Possible approaches for local multiplayer:
- Room code (Jackbox model — host starts game, code appears on shared display, players go to URL + enter code on their phones)
- QR code on the shared display (phone camera → instant join)
- Shared link (host sends a link, players open on any device)
- Some combination

For online sync:
- Invite link / share code
- Friends list + invite from within the platform
- Lobby system (create room, wait for players, start)
- Matchmaking (ranked — automatic pairing by skill tier)

Each of these implies different infrastructure (room management server, friend system, matchmaking algorithm). The question for early architecture: does M1's join flow use an abstraction that can later support online join, or is it a separate system?

---

## Phone Input Abstraction

Each mode needs radically different controls on the player's phone:
- Geography: map interaction (pan, zoom, tap to place pin)
- WoW: text input field
- Fashion: drawing canvas with tool palette
- Stewards' Room: multiple choice / slider / verdict selector
- Racing: tilt steering + buttons, or virtual joystick
- Voting/rating: buttons, number scale

And for online sync on non-phone devices:
- Keyboard + mouse
- Gamepad
- Touch on tablet

If each mode builds its own input UI independently, there's no consistency and the codebase fragments. A shared framework that modes configure (declaring what input components they need) could make new modes cheaper to build. But the framework needs to be flexible enough for drawing canvases AND virtual joysticks AND map interactions without becoming an over-abstracted mess. Whether this is worth building as a framework vs. just building per-mode UIs and extracting patterns later — open question.

---

## 2D + 3D Rendering Coexistence

Party/quiz modes are 2D web UI (forms, text, images, canvas drawing). Racing modes are 3D WebGL (Three.js/Babylon.js). These are different rendering technologies with different asset profiles and performance characteristics.

Options:
- **Single app, lazy-loaded renderers**: one app shell, 3D engine loaded on demand when a 3D mode is selected. Code splitting keeps initial load light.
- **Separate apps/modules**: 2D party platform is one app, 3D racing games are another, linked via shared authentication/session.
- **3D everywhere**: even 2D modes render in a 3D engine (overkill but unified).

The choice affects: initial load time, code architecture, developer experience, how seamless mode-switching feels during a party night.

---

## Content Access Control

If the platform ever has free vs. premium content (paid tiers, season passes, unlockable modes), the content model needs an access-level attribute. Without it, adding monetization later means retrofitting access control onto every content type.

Even if M1 is entirely free, a content item having `{access: "free"}` as a default field is trivial to add. Whether this is worth doing in M1 or is genuinely premature — depends on how early monetization decisions need to happen.

---

## Real-time vs. Turn-based Networking

Quiz/party modes are essentially turn-based: submit answer → wait → reveal. Latency tolerance: 500ms+ is fine. WebSocket message-passing handles it easily.

Racing modes are real-time: continuous input, game state sync at high frequency, latency tolerance: <50ms matters. This might need UDP-style transport, client-side prediction, server-authoritative state reconciliation.

These are fundamentally different networking patterns. A WebSocket layer designed for turn-based message passing won't handle real-time racing well. A real-time game networking layer handles both but is more complex for M1.

Options:
- M1 builds turn-based networking only, adds real-time layer when racing modes are developed
- M1 builds a networking abstraction that can be backed by either turn-based or real-time transport depending on the mode
- The modes that need real-time use a separate networking stack entirely

---

## Player Count Scaling

The interaction pattern determines the scaling ceiling, not the network alone. Different mode types have fundamentally different scaling profiles:

**Quiz/party modes (WoW, Stewards' Room, Geography, Fashion):**
Inherently parallel — everyone submits independently, results aggregated. Technically could handle hundreds of simultaneous submissions. The bottleneck is UX: showing 500 fashion drawings or WoW fakes one by one is unwatchable. At scale, these modes need aggregation mechanics — tournament brackets, top-N filtering by vote, regional heats, phased reveals. The game logic changes at scale even though the submission pattern doesn't.

**Racing modes (Verstappen, Al Mer Qaedes):**
The hard problem. Real-time physics with player-to-player collision scales quadratically: N players = N(N-1)/2 collision pairs. 4 players = 6 pairs, 8 = 28, 16 = 120, 20 = 190. Each additional player also means more position updates to broadcast. Professional reference points: F1 game/iRacing cap at 20-24, Mario Kart at 12, Fall Guys at 60 (but simpler physics). PS1-style simplified physics helps (bounding-box collision is cheap) but networking is still the constraint.

**Mode-declared player limits:**
Rather than a global constant, each mode should declare its own `{min, max, recommended}` range. Geography might support 2-100+. Racing might support 2-8 locally, 2-16 online (depending on what R14 research reveals). Fashion might support 2-12 before the catwalk drags. The session system enforces whatever the active mode declares.

**Local vs. online scaling — different constraints:**

*Local multiplayer:*
- All devices on same WiFi, latency 2-10ms, effectively instantaneous
- Host device runs the simulation — its CPU is the ceiling
- Phone connection management: 8 WebSocket connections over LAN is trivial
- Practical limit probably 4-8 for racing, higher for quiz modes
- Reconnection: social — pause, someone rejoins, continue

*Online sync:*
- Latency 30-150ms, VARIES per player (one at 40ms, another at 120ms)
- Needs server-authoritative state: dedicated server runs the truth simulation
- Client-side prediction for responsiveness (your device predicts your movement, server corrects)
- Interpolation/extrapolation for other players' positions (always slightly in the past due to network delay)
- Rollback when prediction diverges from server truth — complexity scales with player count
- Potentially higher player counts than local (dedicated server has more capacity than a browser tab) but networking overhead is the constraint
- Reconnection: can't pause for everyone. Options include AI takeover, rejoin-in-progress, elimination.

*How large-scale games (50+ players) handle it:*
General patterns known: interest management (only send updates for nearby/relevant players), spatial partitioning, variable tick rates per player, delta compression. But the specifics of how this works in browsers, the real ceiling for WebSocket/WebRTC-based games, and what off-the-shelf frameworks handle — needs research. See [R14](RESEARCH-TODOS.md).

**The most load-bearing early decision: client/server separation.**
- In local M1: the host's browser IS the server. It runs game state. Phones are input-only clients.
- In online: a dedicated cloud server runs game state. All devices are clients.
- If M1 fuses simulation and display in the host's code (intertwined), moving simulation to a dedicated server for online means rewriting the game loop.
- If M1 has a logical client/server separation from the start — the "server" is a distinct module that HAPPENS to run in the host browser but could run anywhere — then online deployment means moving that module to a cloud server. Same simulation code, different deployment target.
- This is a code organization choice that costs nearly nothing in M1 but could save a major refactor later. Whether it's actually the right approach needs proper analysis — it might introduce premature abstraction, or it might be the obvious correct move. Flagged for deliberation.

**Other scaling considerations:**
- Update frequency should be mode-configurable: quiz modes update on events, racing at 30-60Hz. One tick rate doesn't fit all.
- Spatial partitioning for racing at higher counts: only check collisions between nearby cars, only send updates about nearby players.
- Graceful degradation: if a mode is played at higher-than-tested player count, does it degrade gracefully (lower update rate, simplified physics) or break?
- Spectator scaling is a separate axis: 8 players + 1000 spectators is different from 1000 players. Spectators need receive-only connections (much cheaper).

**Research**: [R14](RESEARCH-TODOS.md) — large-scale real-time multiplayer in browser, netcode patterns, feasibility.

---

## Foreclosure Risks

Assumptions that might get baked into M1 implicitly — not because anyone decided them, but because the simplest implementation happens to encode them. Each is worth at least asking "are we assuming this?" during planning.

- **Fixed player count per session.** The simplest implementation sets player count at session creation and assumes it's static. But parties are fluid — people arrive late, leave early, wander back. Drop-in/drop-out during a game night is a real use case. If the session model can't handle dynamic player count, every mode needs workarounds for late joiners. Also: some future contexts have very different player counts (30-person watch party, team events, streamer audiences). The question is whether the session abstraction should support variable player count from the start or whether it's a later addition.

- **One active mode at a time.** Sequential mode switching (geography → WoW → fashion) is the obvious M1 model. But the festival/carnival composition model has players in different games simultaneously. Background games (persistent prediction market running alongside the main mode) need parallel game instances. A "qualifying" phase where everyone does a quick individual challenge before the main event is also parallel. If the session model assumes one active mode, parallel activities need rearchitecting.

- **Singular, fixed host role.** M1 naturally has one host who controls the flow. But future needs include: co-hosting (two friends managing a game night), rotating host (host role passes between games), hostless (the platform manages ranked/competitive flow), AI host (automated game night). If "host" is a hardcoded singular role with specific UI, all of these need refactoring. Modeling host as a set of capabilities (pick modes, start/pause, manage players) that can be assigned, shared, rotated, or given to the platform — more flexible but more complex.

- **"Game night" as the session boundary.** M1 sessions start and end in one sitting. But career mode, team competitions, race weekend events, and async play all span across what we'd call sessions. A race weekend event runs Thursday-Monday. Async WoW has a 24-hour submission window. Team championships span months. If "session" is the fundamental unit and everything must start and end within one, persistent cross-session game state needs a different model on top. Whether "session" is even the right abstraction — vs. something more flexible like "game instance" that can be short-lived (party night) or long-lived (race weekend event) — is a design question.

- **All players have equal display/information access.** The simplest model: everyone sees the same shared display, everyone's phone shows similar input UI. But multiple modes need role-based information visibility: hunters vs. hunted see different things, WoW players shouldn't see which answer is theirs during voting, Grid Walk gives each player different information, spectators might see MORE than active players (omniscient view). The general need: per-role visibility control over game state. If the architecture assumes "shared display shows everything," modes with hidden information hack around it.

- **Content is static and one-directional.** Content authored → published → consumed → scored is the natural M1 flow. But community content means bidirectional flow. Remix/response flows (a player creates a geography round in response to another). Curation flows (community votes on which rounds belong in the "official" pack). Dynamic content (Silverstone pack gains new rounds each year). AI-assisted content pipelines (draft rounds from race data, human review, publish). If content is immutable and author-only in the data model, these flows need pipeline refactoring.

- **Uniform device capability.** Not all phones have gyroscopes, good touch responsiveness, or WebGL support. If a mode REQUIRES a specific capability with no fallback (tilt steering with no virtual joystick alternative), some players can't play. Graceful degradation per input method and per rendering capability — the platform detecting what a device can do and offering appropriate alternatives.

---

## Other Considerations (less developed)

- **Reconnection handling**: phone loses WiFi for 3 seconds mid-game. Different answer for quiz mode (rejoin, catch up) vs. racing mode (car keeps driving? crash? pause?). Mode-specific and context-specific (local = pause is acceptable, online = probably not).
- **Asset loading per mode**: geography needs images, fashion needs drawing tools, racing needs 3D models + audio. Loading strategy (upfront vs. on-demand) affects mode-switching speed during party nights.
- **Replay / moment capture**: multiple modes want replayable moments (kill-cams, fashion show screenshots, funniest WoW fakes). A shared game event log format could serve replays, highlights, shareable clips from one source. Without it, each mode builds its own capture.
- **Voice chat**: social deduction and cooperative modes are dramatically better with voice. Whether to integrate WebRTC voice or rely on external (Discord, phone call). The session model having a slot for an audio channel even if unused keeps the option open.
- **Offline / degraded play**: can any modes work fully offline? Useful for travel, poor connectivity. Geography with pre-cached content? Solo practice modes?
- **Accessibility**: colorblind modes, alternative input, text-to-speech for WoW reveals, difficulty/assist settings. How deeply accessibility is woven into the base vs. added per mode.
- **Content versioning**: if a WoW round or geography round is updated, do old scores against the previous version still make sense? Content might need version tracking.
- **Localization**: F1 is global, fan base speaks dozens of languages. If UI, prompts, and mode instructions are hardcoded English with no localization framework, internationalizing later touches every string. Some content is inherently language-specific (radio transcripts are English) but UI doesn't have to be.
