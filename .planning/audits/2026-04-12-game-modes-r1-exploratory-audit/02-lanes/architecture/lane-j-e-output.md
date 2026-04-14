---
date: 2026-04-13
lane: j-e
lane_name: "Browser authoritative room/state follow-up"
delegation_class: replanning-revision-gap-filling
tags:
  - exploratory-audit
  - lane-j-e
  - browser
  - authoritative-state
  - visibility
  - room-lifecycle
---

# Lane J-E: Browser authoritative room/state follow-up

## Lane framing

This follow-up narrows to direct room/state engineering mechanisms instead of broad browser-session topology.

The strongest primary references in this pass were:

- `Colyseus`
  official docs that directly expose room lifecycle hooks, matchmaking and seat reservation, filtered state views, and reconnect handling
- `boardgame.io`
  official docs plus official source that directly expose player-specific state redaction, turn/phase/stage control, authenticated lobby joins, and log redaction behavior
- `PlayFab Lobby` plus `PlayFab Party`
  official docs that directly expose lobby ownership, discoverability, invites, TTL/expiration, arranged lobbies, connection strings, and secured communication network setup

Important scope note:

- these are mostly `framework/service capability` references, not proof that a shipped browser game used every mechanism in exactly this way
- that still makes them useful here, because the follow-up question is about exposed engineering mechanisms, not vendor selection or shipped-product brag sheets

Source note:

- some Microsoft Learn pages displayed an authorization banner in this browsing surface, but still exposed substantial article text; all claims below are limited to the visible text

## Reference cases and source audit

| Reference case | Source class | Reliability | What it actually exposes | What it does not expose | Direct vs inferred |
| --- | --- | --- | --- | --- | --- |
| `Colyseus` | Class 1 official docs | High | room lifecycle hooks, room metadata/listing controls, server-side auth, seat reservation, matchmaking query/join primitives, reconnect flow, per-client `StateView` filtering | shipped product patterns, moderation/admin product UX, long-term persistence patterns | most conclusions are direct; Prix relevance is inferred |
| `boardgame.io` | Class 1 official docs + official repo source | High | lobby REST flow, authenticated player credentials, seat claiming by `playerID`, `playerView` redaction, server-only moves, phases/turns/stages/active players, log redaction logic | rich realtime room lifecycle, reconnect/session recovery patterns, large-room/browser-audience orchestration | state visibility and turn structure are direct; realtime-room implications are inferred |
| `PlayFab Lobby` | Class 1 official docs, plus one official scenario doc | High | connection-string joins, lobby discovery/search properties, invites, access policy, owner/member privileges, ownership migration, TTL/expiration, arranged lobbies, backfill-oriented room refill flow | authoritative gameplay state model, hidden-info state filtering inside the lobby, browser-native game loop patterns | lifecycle/discovery are direct; gameplay-authority implications are inferred |
| `PlayFab Party` | Class 1 official docs + Class 1 official blog | High | secured communication network creation, network descriptor sharing, invitation security model, endpoint/chat object model, service-side relay provisioning, multi-network tradeoffs | browser-native room UX, authoritative game-state engine, turn/phases/logs abstractions | transport/security facts are direct; browser fit and architecture consequences are inferred |

### Primary sources used

- Colyseus docs:
  - https://docs.colyseus.io/room
  - https://docs.colyseus.io/matchmaker
  - https://docs.colyseus.io/auth/room
  - https://docs.colyseus.io/state/view
  - https://docs.colyseus.io/room/reconnection
- boardgame.io official docs / source:
  - https://github.com/boardgameio/boardgame.io/blob/main/docs/documentation/api/Game.md
  - https://github.com/boardgameio/boardgame.io/blob/main/docs/documentation/secret-state.md
  - https://github.com/boardgameio/boardgame.io/blob/main/docs/documentation/stages.md
  - https://github.com/boardgameio/boardgame.io/blob/main/docs/documentation/api/Lobby.md
  - https://github.com/boardgameio/boardgame.io/blob/main/src/master/filter-player-view.ts
- PlayFab Lobby / Party:
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/lobby/lobby-and-matchmaking
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/lobby/lobby-properties
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/lobby/owner-requirements-and-privileges
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/lobby/ownership-changes
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/lobby/lobby-ttl
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/lobby/find-lobbies
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/lobby/lobby-invites
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/lobby/playfabmultiplayerreference-cpp/pflobby/enums/pflobbyaccesspolicy
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/networking/quickstart
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/networking/reference/structs/partynetworkdescriptor
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/networking/concepts-invitations-security-model
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/networking/concepts-objects
  - https://learn.microsoft.com/en-us/gaming/playfab/multiplayer/networking/concepts-multiple-networks
  - https://developer.microsoft.com/en-us/games/articles/2023/10/playfab-party-request-party-service-launch/

## Concrete engineering mechanisms exposed

### 1. `Colyseus` exposes a clear reserve-then-claim room join model

- Direct fact:
  `matchMaker.joinOrCreate`, `join`, `joinById`, `create`, and `reserveSeatFor` all return a seat reservation, and the docs explicitly say the frontend consumes that reservation with `consumeSeatReservation()`.
- Direct fact:
  room config includes `seatReservationTimeout`, default `15` seconds, which is the wait time for a client to effectively join after reserving a seat.
- Direct fact:
  the room is auto-locked when `maxClients` is reached, and `hasReachedMaxClients()` counts both connected clients and reserved seats.
- Direct fact:
  the matchmaker can search cached rooms with conditions and sorting, find one public unlocked room, or join by explicit room ID.
- Inference:
  this is a much stronger fit for `controller device enters a room but has not fully claimed a slot yet` than systems that only expose a single optimistic join call.

### 2. `Colyseus` separates room lifecycle, room listing, and authority hooks cleanly

- Direct fact:
  the core room hooks are `onAuth`, `onCreate`, `onJoin`, `onDrop`, `onReconnect`, `onLeave`, and `onDispose`.
- Direct fact:
  `onAuth` runs before `onJoin`; returning a truthy value passes auth data through to `onJoin`, returning falsy rejects the join, and the client sends the auth token through `client.auth.token`.
- Direct fact:
  room listing properties can be changed through matchmaking metadata updates including `metadata`, `private`, `locked`, `maxClients`, and `unlisted`.
- Direct fact:
  frontend matchmaking methods can be restricted so the client is allowed to call only `join`, `joinById`, and `reconnect`, rather than `create` or `joinOrCreate`.
- Inference:
  Colyseus is opinionated about `where authority lives` in room/session control even when game rules are left to application code: server hooks and exposed-method control are first-class.

### 3. `Colyseus` has the most explicit per-client state-view mechanism in this pass

- Direct fact:
  `StateView` is assigned to `client.view`.
- Direct fact:
  fields tagged with `@view()` are only visible to `StateView` instances that contain that schema instance.
- Direct fact:
  state can be filtered at object granularity with `client.view.add(instance)` and `client.view.remove(instance)`.
- Direct fact:
  `@view(tag)` supports multiple filtered views for the same schema instance.
- Direct fact:
  on reconnect, Colyseus preserves `client.auth`, `client.userData`, and `client.view`.
- Inference:
  this is directly useful for `host screen vs player phone vs spectator vs moderator` view contracts because it filters serialized state itself, not just UI rendering.

### 4. `Colyseus` reconnect support is stateful enough to preserve a seat and a view contract

- Direct fact:
  disconnect flow is explicit: `onDrop` can call `allowReconnection()`, the client retries automatically with exponential backoff, `onReconnect` fires on success, and `onLeave` fires if reconnect fails or times out.
- Direct fact:
  docs recommend marking players as disconnected in state during `onDrop`, deferring cleanup until `onLeave`, and they note that important messages sent during disconnection are queued automatically.
- Direct fact:
  room config defaults `autoDispose` to `true`, so empty rooms disappear unless intentionally handled otherwise.
- Inference:
  for Prix-style couch-play or private-room sessions, `seat preservation during short disconnects` and `cleanup only on permanent leave` looks like a strong baseline pattern.

### 5. `boardgame.io` exposes player-specific state filtering at the game-state layer

- Direct fact:
  `playerView({ G, ctx, playerID })` returns a player-specific version of `G`, and the docs explicitly say this support exists so secret information is not even sent to the client.
- Direct fact:
  `PlayerView.STRIP_SECRETS` removes a top-level `secret` key and strips other players from `G.players` so a player only receives their own player entry.
- Direct fact:
  the official source filters outgoing `update`, `patch`, and `sync` payloads through `playerView`.
- Direct fact:
  the same source redacts log payload args for everyone other than the acting player when a move is marked `redact: true`.
- Direct fact:
  moves that manipulate hidden state can be marked `client: false`, which prevents them from running on the client.
- Inference:
  boardgame.io is unusually explicit about `visibility rights are part of transport payload shaping`, not just presentation logic.

### 6. `boardgame.io` gives concrete turn/phase/stage machinery, not just room shell

- Direct fact:
  the `Game` config includes `turn`, `phases`, `endIf`, `onBegin`, `onEnd`, `activePlayers`, and optional `deltaState` JSON Patch syncing.
- Direct fact:
  stages allow more than one player to act during a turn, and `setActivePlayers` can target `currentPlayer`, `others`, `all`, or a specific set of player IDs with `minMoves`, `maxMoves`, `revert`, and `next`.
- Direct fact:
  `minPlayers` and `maxPlayers` are enforced by the lobby component.
- Inference:
  for Prix modes that have structured beats like `host reveal -> private submit -> lock -> public reveal -> scoring`, boardgame.io’s phase/stage model is the strongest direct reference in this pass for turn cadence and mutation rights.

### 7. `boardgame.io` lobby/session orchestration is concrete, but thinner than Colyseus on seat reservation and reconnect

- Direct fact:
  the Lobby REST API exposes create, list, get, join, update player metadata, leave, and `playAgain`.
- Direct fact:
  authenticated matches issue per-player credential tokens, and the match will not accept moves on behalf of a player without the proper credential token.
- Direct fact:
  join can target a specific `playerID` seat, or if omitted the framework assigns the first available ordinal.
- Direct fact:
  `playAgain` generates a `nextMatchID`, optionally preserving `numPlayers` and `setupData`.
- Inference:
  boardgame.io exposes `seat claiming` rather than a separate temporary `seat reservation` primitive; compared with Colyseus, it is stronger on turn structure and weaker on pre-join room orchestration.

### 8. `PlayFab Lobby` exposes a strong browser-room-shell pattern: discover, join, lock, migrate ownership, expire

- Direct fact:
  lobbies are joined via an opaque `connectionString`, not the `lobbyId`.
- Direct fact:
  discoverability is controlled through `accessPolicy`, with `Public`, `Friends`, and `Private` semantics; `Private` means the lobby is not visible in queries and a player must receive an invite.
- Direct fact:
  owners can change `maxMemberCount`, `accessPolicy`, `membershipLock`, and global properties; members each have an isolated member property bag.
- Direct fact:
  all lobby members can see every other member’s member properties; custom lobby properties are only visible to members; custom search properties are used for public search.
- Direct fact:
  ownership migration can be `Automatic`, `Manual`, `None`, or `Server`, with different reconnect and owner-loss behavior.
- Direct fact:
  TTL behavior is explicit: default lobby TTL is `1` hour, connected lobbies extend to `4` hours, and when all members disconnect from a client-owned lobby it is hidden from search and drops to a `1` minute grace period before deletion.
- Inference:
  PlayFab Lobby is a strong reference for `room shell` engineering, but not for hidden-info payload filtering because member-property visibility is room-wide, not per-member private.

### 9. `PlayFab Lobby` exposes multiple join/discovery paths but not a first-class seat reservation primitive

- Direct fact:
  players can discover connection strings through in-game invites, platform invites, filtered lobby searches, or any custom out-of-band mechanism.
- Direct fact:
  in-game invites send the lobby’s `connectionString`; invite receipt is a state-change callback; only players can send or receive invites.
- Direct fact:
  `FindLobbies` is recommended for explicit player search, but the docs explicitly say it is not recommended for background matchmaking.
- Direct fact:
  matchmaking can assemble players into an arranged lobby using `lobbyArrangementString`; each matched player joins the same lobby with that string, and the first player to join becomes owner.
- Direct fact:
  the official scenario doc recommends owner-driven removal of inactive players and server backfill tickets to replace them.
- Inference:
  PlayFab exposes `open/closed membership plus replace-via-backfill`, not `hold seat for 15 seconds and then claim it` in the Colyseus sense.

### 10. `PlayFab Party` exposes secured communication-network setup, but not authoritative gameplay state

- Direct fact:
  a Party network is a secured collection of devices and authorized users used to exchange chat or data communication.
- Direct fact:
  `CreateNewNetwork()` returns a `PartyNetworkDescriptor`, which contains the data required for other players to connect.
- Direct fact:
  joining requires deserializing the descriptor, connecting to the network, authenticating the local user, connecting chat controls, and creating an endpoint for game message traffic.
- Direct fact:
  joining a Party network requires four things: the network descriptor, a valid PlayFab entity token, an invitation identifier, and either inclusion in that invitation or an open invitation.
- Direct fact:
  invitations can be created and revoked over the network’s lifetime; a network is always created with an initial invitation.
- Direct fact:
  the Party quickstart recommends using PlayFab Lobby to synchronize the network descriptor.
- Inference:
  Party is a concrete reference for `secure comms substrate` and `network admission control`, but not for authoritative round-state logic.

### 11. `PlayFab Party` also exposes service-side topology control and warns about multi-network complexity

- Direct fact:
  the official `RequestPartyService` blog says developers can provision a Party network from their own services through REST, specifying region, network configuration, and related options, then distribute the returned network descriptor to clients.
- Direct fact:
  the same blog frames this as better policy control and stronger defense against abusive client-side Party creation.
- Direct fact:
  the docs say multiple Party networks are supported, but label them an advanced scenario, note that a single-network redesign is often preferable, and say per-network connectivity billing increases cost.
- Direct fact:
  the docs distinguish endpoint scope from chat scope: endpoints are network-specific, while a single chat control can be connected to multiple networks.
- Inference:
  if Prix ever needs `long-lived private group shell + short-lived round/session network`, the useful lesson is not “always use multiple networks”; it is “treat long-lived social shell and active gameplay transport as separate layers, and only split them when the use case truly demands it.”

## Concrete tradeoffs and limits

### High-confidence tradeoffs

- `Colyseus` is the strongest direct reference for authoritative room/session control in a browser-friendly stack, but it leaves a lot of game-specific policy to application code:
  hidden-info design, score rules, moderation queues, persistence, and room-shell UX are still your problem.
- `boardgame.io` is the strongest direct reference for structured turn/phases/hidden-info transport shaping, but it is less expressive for pre-join room lifecycle and reconnect orchestration than Colyseus.
- `PlayFab Lobby` is the strongest direct reference here for room shell lifecycle and ownership policy, but it does not expose hidden-info per-member views inside the lobby itself.
- `PlayFab Party` exposes secure comms and admission control, not a gameplay authority engine; using it still requires a separate authority model for round state, scoring, and reveal order.

### Limits and cautions exposed by the sources

- `Colyseus`
  room listing and seat reservation are first-class, but product-level room semantics still need to be authored: who owns the room, when seats become audience seats, when moderators can override joins, and how code/link joins map to room objects.
- `boardgame.io`
  the engine clearly supports secret state, move redaction, and turn structure, but the lobby API looks more like authenticated match administration than a rich room/session shell. I did not find first-class published primitives for temporary seat holds, discoverability filters, or reconnect grace comparable to Colyseus.
- `PlayFab Lobby`
  member properties are visible to all lobby members. That is useful for readiness, seat color, team choice, and status, but it means the lobby is not itself a hidden-info substrate.
- `PlayFab Lobby`
  docs explicitly discourage using `FindLobbies` as background matchmaking, which matters if Prix ever mixes public room browsing with auto-fill.
- `PlayFab Party`
  multiple networks increase complexity and cost, and the docs explicitly say a single-network redesign is often better.
- `PlayFab Party`
  the reviewed docs and quickstarts are C++/Unity/Unreal centered, not browser-JS centered. That makes it a less direct browser-first reference than Colyseus or boardgame.io even though the underlying room/comms ideas are still useful.

### Capability vs proven pattern

- `Colyseus StateView`, `boardgame.io playerView`, and `PlayFab ownerMigrationPolicy` are definitely real implemented capabilities.
- It would be overreach to claim that these capabilities prove the best shipped-product pattern for Prix specifically.
- The safer use of this evidence is:
  - `Colyseus` for concrete room-state and per-client filtering primitives
  - `boardgame.io` for concrete phase/turn/private-state mechanics
  - `PlayFab Lobby/Party` for concrete room-shell and transport-security mechanics

## What seems relevant to Prix Guesser

### 1. Split the architecture into three distinct objects early

- `room shell`
  invite/discovery artifact, owner, seats/slots, access policy, rejoin, expiry, moderation shell
- `authoritative round state`
  prompt, submissions, lock states, reveal order, scoring, timers, adjudication
- `per-client view contract`
  what host sees, what each player phone sees, what spectators see, what moderators can override

This split is the clearest recurring lesson across the references.

### 2. Model seats as a first-class thing, not just a member count

Most directly useful precedent:

- `Colyseus`
  reserved seat, timeout, later consumption, reconnect retention

Strong Prix implication:

- Prix likely wants explicit states like `invited`, `reserved`, `joined`, `disconnected-but-held`, `audience`, `removed`
- that is better than a single boolean `in room`

### 3. Treat visibility as serialized-state policy, not only UI policy

Most directly useful precedents:

- `Colyseus StateView`
- `boardgame.io playerView`
- `boardgame.io` log redaction

Strong Prix implication:

- host-screen spectacle, phone-controller privacy, and spectator fairness should not depend on “the client received everything but promises not to render it”
- the architecture should support `same underlying round, different payload contracts`

### 4. Separate `room ownership` from `game authority`

Most directly useful precedent:

- `PlayFab Lobby`
  owner/member distinction, owner migration policies, owner-only mutation rights for room properties

Strong Prix implication:

- the host may own room-level controls like lock/unlock, invites, or kick
- the scoring/reveal/timer engine can still remain server-authoritative and not “host-device authoritative”

### 5. Preserve continuity across rounds without conflating it with one live match

Most directly useful precedents:

- `boardgame.io playAgain`
- `PlayFab` arranged lobby plus return-to-lobby flow
- `Colyseus` auto-dispose / lifecycle hooks

Strong Prix implication:

- a private party session likely wants a stable party shell that can host multiple rounds or mini-modes
- the active round instance should be restartable or replaceable without losing the whole social container

### 6. Prix’s likely browser-first futures point toward a hybrid of these patterns, not one source copied wholesale

High-confidence synthesis:

- for `browser-first room shell and seat lifecycle`, the strongest reference is `Colyseus` or a `PlayFab-Lobby-like` shell
- for `private answers, role views, phased reveals, adjudication`, the strongest reference is `boardgame.io`-style view and phase thinking
- for `secure comms substrate` or future service-side orchestration, `PlayFab Party` is useful conceptually but less directly browser-native

## What remains uncertain

- I still do not have a strong official engineering writeup from a shipped browser party game showing `seat reservation + private phone views + host-screen authority + reconnect` all in one public stack description.
- I did not find a first-class PlayFab Lobby concept equivalent to Colyseus-style short-lived seat reservation; the closest exposed mechanisms are membership lock, connection-string admission, invites, arranged lobbies, and backfill.
- I did not find boardgame.io material that exposes a rich room-shell model comparable to Colyseus or PlayFab Lobby. Its strongest published surface is clearly the turn/hidden-info layer.
- PlayFab Party is useful as a session/comms reference, but the reviewed material does not make it a direct browser-controller reference. If browser-native transport/runtime fit becomes the next question, that likely needs a separate focused pass.
- This pass still says more about `mechanism availability` than `operational cost under real fan-project conditions`.

Most useful follow-up questions from here:

- should Prix’s early substrate treat `room shell` and `active round authority` as separate services/modules from day one?
- is `reserved seat with timeout and reconnect grace` important enough to justify adopting that pattern early rather than bolting it on later?
- for hidden-info rounds, do we want `payload filtering at serialization time` as a non-negotiable rule?
