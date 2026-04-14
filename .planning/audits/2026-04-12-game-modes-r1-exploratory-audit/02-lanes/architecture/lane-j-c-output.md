---
date: 2026-04-13
lane: j-c
lane_name: "Hidden-info / asymmetric comms systems engineering exposure"
orientation: exploratory
delegation_class: initial-architecture-research-planning
tags:
  - exploratory-audit
  - lane-j
  - hidden-info
  - asymmetric-comms
  - engineering-exposure
---

# Lane J-C Output

## Lane framing

This lane was run as an engineering-exposure pass, not a product-idea summary.

The strongest signals here are not "which games have hidden roles," but which published systems expose:

- room authority models
- visibility partitioning between shared and private views
- moderation and safety burden
- discovery / join topology
- whether voice is assumed, integrated, or explicitly externalized

The evidence quality is uneven. `Spaceteam` and `Artemis` expose unusually concrete topology details. `Jackbox`, `Among Us`, and `Blood on the Clocktower` expose more about product constraints, moderation, and room assumptions than about low-level transport. `Keep Talking and Nobody Explodes` exposes the cleanest information-partition pattern, but not much infrastructure.

The most important high-confidence conclusion is:

- hidden-info / asymmetric comms systems are usually bounded by legibility, comms discipline, moderation, and visibility control before they are bounded by raw socket count

That matters for Prix Guesser because `Pit Wall`, `Bad Wall`, `Driver Override`, sabotage, rumor, and other asymmetric branches look much more like `small topology-sensitive rooms` than like generic scalable multiplayer.

## Reference cases and source audit

| Reference case | Source class | Reliability | What the source actually exposes | What it does not expose | Direct or inferred |
|---|---|---|---|---|---|
| [Spaceteam Networking Post](https://spaceteamadmirals.club/blog/the-spaceteam-networking-post/) + [Spaceteam FAQ](https://spaceteam.ca/faq/) | `1` creator-written official engineering post; `3` official FAQ | High | actual discovery flow, ad-hoc host election, Bluetooth and Wi-Fi constraints, Internet mode password flow, voice assumptions, classroom/tournament network advice | authoritative simulation model, cheat handling, persistence | Mostly direct |
| [Artemis manual](https://cdn.akamai.steamstatic.com/steam/apps/247350/manuals/Artemis_Manual_1.70-rev5.pdf?t=) | `1/2` official manual | High | one-server-many-clients topology, station assignment, main-screen sourcing, multi-ship cap, separate Game Master computer/module | lower-level netcode, replication strategy, anti-cheat | Direct |
| [Keep Talking and Nobody Explodes site](https://keeptalkinggame.com/) + [official bomb manual how-to-play](https://www.bombmanual.com/how-to-play-pc.html) | `3` official docs | High | strict role partition, external manual requirement, remote play via external voice, any-number-of-experts claim | session hosting, moderation, state sync details | Direct on topology, weak on infrastructure |
| [Push The Button](https://www.jackboxgames.com/games/push-the-button) + [Fakin' It All Night Long reveal](https://www.jackboxgames.com/blog/jnp-fakin-it-all-night-long-reveal) + [Jackbox home FAQ](https://www.jackboxgames.com/) + [audience article](https://www.jackboxgames.com/blog/how-audience-play-along-differs-in-each-jackbox-game) | `3` official product/support docs | Medium-high | host-screen-plus-phone topology, active-player caps, audience shell, secret-task / deception framing, remote-play acknowledgment, room-code / host-screen assumptions | internal authority model, per-device sync details, moderation internals | Mixed direct + inference |
| [Among Us roles / crossplay announcement](https://www.innersloth.com/among-us-is-out-now-on-xbox-and-playstation/) + [randomized lobby names](https://www.innersloth.com/introducing-randomized-lobby-names/) + [Code of Conduct](https://www.innersloth.com/code-of-conduct/) + [free chat help](https://innersloth.zendesk.com/hc/en-us/articles/6711536647060-How-do-I-turn-on-Free-Chat) | `3` official blog / support / policy docs | High for published policy, medium for engineering exposure | lobby size, role customization, reporting, safer-public-lobby work, age-gated chat, quick-chat filtering, public-search exclusion for modded games | netcode architecture, visibility replication strategy, meeting-state internals | Direct on moderation/policy, inferred on architecture pressure |
| [Blood on the Clocktower safety post](https://bloodontheclocktower.com/blogs/news/stay-safe-there-are-demons-out-there) + official wiki pages for [Artist](https://wiki.bloodontheclocktower.com/Artist), [Savant](https://wiki.bloodontheclocktower.com/Savant), [Gardener](https://wiki.bloodontheclocktower.com/Gardener) | `3` official blog / official wiki | Medium-high | storyteller-mediated private chats, app blocking/flagging, open-lobby vs curated-group assumptions, app-only manual assignment tooling | transport, persistence, sync internals | Direct on moderation and role/authority model |

## Concrete engineering or topology mechanisms exposed

### 1. Self-organizing local room formation is possible, but brittle

`Source fact:` Spaceteam's creator says devices start as clients, search for a server, and if none is found within three seconds they also advertise themselves as a server. A deterministic choice is needed or players split into multiple accidental groups. The post also calls out Bluetooth connection limits, iOS/Android Bluetooth incompatibility, multicast failures on some Wi-Fi routers, and Android cases where explicit `Host` and `Join` modes are needed.

`Why this matters:` this is unusually concrete evidence that "everyone just opens the game and it finds each other" is not magic. It is a room-formation subsystem with fallback cases, deterministic host election, router failure modes, and platform asymmetry.

`Inference:` if Prix Guesser wants couch or private-room phone joins, `best-effort LAN discovery` can be a convenience layer, but it should not be the only join path. Room code / QR / direct share link should be first-class fallback, not an afterthought.

### 2. Station-based asymmetric play benefits from explicit server-client separation

`Source fact:` Artemis' manual describes one server, multiple clients connecting to it, console-role selection per client, up to six officers on a vessel, six vessels per server, and a main screen sourced from the server. It also requires a separate player and separate computer for `Game Master` mode, plus a mission module and instructions.

`Why this matters:` Artemis is one of the clearest published examples of `same simulation, different consoles, different rights`. It separates:

- shared spectacle screen
- role-specific operator screens
- optional human moderator / scenario authority

`Inference:` this looks directly relevant to `Pit Wall` or `Driver Override` style modes where a driver, strategist, engineer, and possible saboteur should not see identical state, and where a host-screen view may need to be deliberately incomplete.

### 3. The cleanest asymmetric-knowledge pattern is often the simplest one

`Source fact:` Keep Talking and Nobody Explodes defines one `Defuser` who sees the bomb and `Experts` who do not; the experts instead use a separate manual. The official how-to-play page explicitly says remote play can use the player's preferred voice chat service and that any number of players can participate as experts if they can work efficiently.

`Why this matters:` the topology is blunt and extremely legible:

- one live actor with privileged perception
- one or more support actors with complementary knowledge
- all progress carried by comms quality

`Inference:` for Prix Guesser, some asymmetric branches may be stronger if they adopt this kind of `hard knowledge partition` instead of trying to keep every player in roughly the same UI. A driver who only sees immediate race state and a pit wall who only sees high-level telemetry / maps / rumors may be better than softer asymmetry.

### 4. Host-screen party systems scale by separating active players from the audience shell

`Source fact:` Jackbox's official docs state that players join with phones or web devices while everyone needs to see the host screen. The site also distinguishes active players from audience play-along. `Push The Button` exposes `4-10` active players with audience capacity up to `10,000`. `Fakin' It All Night Long` exposes `3-8` players, secret tasks, and a new `remote play` mode.

`What is direct:` Jackbox clearly publishes a topology where:

- one display anchors the session
- phones are private input surfaces
- active-room size and audience size are separate numbers

`What is inferred:` the exact authority and sync internals are not exposed, but the room shape implies that high audience count does not mean a high-count hidden-info room. It means a large observation / voting shell around a much smaller active deception core.

`Why this matters:` this is a strong precedent for keeping `watch-party participation` and `active secret-role play` as separate architectural envelopes in Prix Guesser.

### 5. Public hidden-info rooms rapidly become moderation systems

`Source fact:` Among Us official docs expose several safety controls:

- public-lobby names were randomized as part of making public spaces safer
- the team says it is actively improving filtering, matchmaking, moderation, and reporting
- players can kick and report users in-game
- free chat is age-gated, while temporary or child accounts can be restricted to quick chat only
- modded games are excluded from public lobby search and must be friend-invited directly

`Why this matters:` Among Us is one of the clearest signals that once hidden-info play moves beyond trusted private groups, moderation architecture becomes part of the game topology:

- discoverability controls
- text-channel restrictions
- report flows
- sanctioning
- different trust envelopes for public search vs direct invite

`Inference:` if Prix Guesser ever exposes asymmetric comms modes publicly, it will likely need a much narrower comms surface than private-room modes. Open voice or unrestricted rumor channels are a safety and abuse problem, not just a game-design choice.

### 6. Human moderation is a real topology, not just a board-game artifact

`Source fact:` Blood on the Clocktower's official materials repeatedly treat the `Storyteller` as a live authority who:

- gives private information in off-circle conversations
- manually mediates setup and role assignment
- can use app-only tooling such as `Gardener` to assign players characters directly
- can remove people from lobbies
- now sits inside an app that also exposes blocking, flagging, hidden text, warnings on blocked-user lobbies, and planned confidential reports to the storyteller

`Why this matters:` this is not just "a moderator exists." It is a concrete room model where a human authority stabilizes hidden info, edge cases, secrecy, pacing, and trust.

`Inference:` Prix Guesser should not assume that every asymmetric mode must be fully self-running from day one. Some richer sabotage / rumor / insider-information variants may ship faster and feel better if they include a `host/referee` authority lane, even if a later automated version is desirable.

### 7. Visibility partitioning is more important than player count in these systems

`Cross-case synthesis from direct source facts:`

- KTANE partitions by `bomb` vs `manual`
- Artemis partitions by `station console`
- Jackbox partitions by `host screen` vs `phone screen`
- Clocktower partitions by `public table talk` vs `private storyteller whispers`
- Among Us partitions by `role`, `meeting`, and `chat permissions`

`Inference:` the recurring engineering problem is not primarily "how many users can connect?" It is "which view is allowed to know what, when, and through which channel?"

That pushes toward a Prix Guesser substrate with explicit visibility policy, not ad-hoc component hiding.

## Concrete tradeoffs and limits

### 1. Voice is usually assumed, but often externalized

`Source fact:` KTANE explicitly supports remote play through the player's preferred voice chat service. Spaceteam's Internet mode requires bring-your-own voice chat unless players use the Bunch integration. Jackbox assumes everyone can see and hear the host screen.

`Implication:` hidden-info asymmetric modes do not need built-in voice to work, but they do need a clear voice assumption. External voice keeps engineering simpler and may be the right default for private-room Prix Guesser modes.

### 2. Discovery convenience fights network reality

`Source fact:` Spaceteam documents multicast failures, Bluetooth caps, cross-platform restrictions, and accidental split-lobby behavior.

`Implication:` local "it should just find everyone" is a nice-to-have. Codes, QR join, and deterministic host authority are the safer spine.

### 3. Large audience counts do not mean large hidden-info rooms

`Source fact:` Jackbox publishes very high audience capacities while keeping active deceptive play in small rooms. Among Us publishes `4-15` player lobbies, not giant social-deduction fields. Clocktower relies on a storyteller and curated groups even when player count expands.

`Implication:` a large F1 watch-party shell and a small active sabotage / pit-wall room can coexist, but they should not be modeled as the same thing.

### 4. Public hidden-info modes inherit moderation cost very quickly

`Source fact:` Among Us exposes chat restriction, reporting, filtering, matchmaking, randomized public lobby names, and sanction policy. Clocktower's online app has added blocking, flagging, hidden message behavior, and lobby warnings.

`Implication:` the minute Prix Guesser leaves trusted private groups, comms moderation becomes product-defining infrastructure. This is a strong argument for private-room-first posture for asymmetric comms modes.

### 5. Human authority increases richness, but also staffing and trust requirements

`Source fact:` Artemis Game Master mode requires a separate human and separate machine. Clocktower's private-info structure leans heavily on the Storyteller.

`Implication:` host/referee-assisted modes can unlock richer hidden-info play early, but only if the product is comfortable treating host competence and host trust as part of the experience contract.

### 6. Hard information asymmetry can be excellent, but it narrows eligible contexts

`Source fact:` KTANE is built around one player seeing the bomb and everyone else seeing only the manual. Spaceteam and Artemis both assume intense live coordination.

`Implication:` strong asymmetric modes are high-value for private sync and couch play, but are poor fits for async and weaker fits for noisy public lobbies.

## What seems relevant to Prix Guesser

### 1. `Pit Wall` and related branches should be treated as topology-specific modes

High-confidence read: `Pit Wall`, `Bad Wall`, `Driver Override`, sabotage, and rumor modes should not be forced into the same assumptions as geography or poll-based party rounds.

They likely need:

- small active rooms
- explicit role rights
- private views
- a display-safe shared view
- an external-voice-friendly posture

### 2. Prix Guesser probably needs an explicit visibility-policy layer

The reference cases repeatedly separate:

- public shared state
- private role state
- moderator-only state
- spectator-safe state

For Prix Guesser, that suggests a substrate where every game event or state slice can be tagged by audience:

- `host-screen safe`
- `player-private`
- `role-private`
- `referee-only`
- `post-round revealable`

This seems more important than picking a transport stack early.

### 3. `Event container` and `active room` should be separate concepts

Jackbox's audience split and Clocktower / Among Us moderation signals both point the same way:

- a race-weekend event, stream audience, or couch crowd can be much larger than the active hidden-info crew
- the active crew should be modeled as a smaller authority-sensitive room inside the broader session shell

That would let Prix Guesser support "everyone watches, a few people secretly operate" without pretending the whole room shares the same rights.

### 4. A host / referee lane is probably worth keeping open

Clocktower and Artemis both show that some asymmetric systems work well because there is a trusted authority who can:

- assign roles
- trigger secret reveals
- resolve ambiguity
- pace phases
- intervene when players get lost

That looks especially relevant for:

- rumor injection
- sabotage escalation
- secret role variants
- bespoke party-night scenarios

### 5. Join flow should be codes-first, discovery-second

Spaceteam is the strongest evidence here. For Prix Guesser private-room asymmetric modes, the likely durable join order is:

1. room code / QR / share link
2. optional LAN convenience
3. external voice as the default assumption

That is much safer than anchoring the design to multicast discovery.

### 6. Station-based role design looks stronger than pure accusation design

Among Us is useful mainly as a warning about public moderation cost. The more positive engineering precedents for Prix Guesser seem closer to `Artemis` and `KTANE`:

- station roles
- complementary but incomplete knowledge
- structured interdependence
- role-specific consoles

That seems especially promising for F1-flavored asymmetry:

- driver
- strategist
- tire engineer
- race engineer
- rumor source / mole
- safety car / steward / weather wildcard

## Uncertain but promising leads

### 1. Jackbox's actual remote-play adaptation details are still underexposed

Official pages confirm a `remote play` mode for the new Fakin' It, but they do not expose how task design, reveal timing, or anti-leak handling changed. A second pass should look for a dev diary, talk, or interview.

### 2. Among Us exposes moderation pressure, but not much netcode

The official sources are useful for room-policy lessons, not for transport architecture. If deeper engineering exposure is needed, this lane would need a separate source hunt for talks, postmortems, or other primary technical material.

### 3. Clocktower's official app seems to contain more topology detail than the public docs expose

The safety blog and wiki show enough to prove the importance of storyteller authority, lobby warnings, and blocking, but not enough to map app permissions, spectator handling, or role-delivery flows precisely.

### 4. Artemis-style scenario scripting may be a strong analog for host-authored asymmetric sessions

The manual confirms a separate Game Master module and instructions, but this pass did not inspect mission-authoring docs. That could matter if Prix Guesser wants host-authored sabotage scripts or referee-led "special event" rounds.

### 5. There is a meaningful unresolved question about how much secrecy should survive on the host screen

The references expose multiple answers:

- Jackbox keeps the spectacle screen central but uses phones for private input
- KTANE removes the shared knowledge surface entirely
- Artemis uses a main view that is useful but incomplete
- Clocktower allows private side-channel conversations

Prix Guesser should not assume one universal answer. Different asymmetric branches may need different shared-display commitments.
