# Architecture Patterns

**Domain:** Private browser-based F1 geography / party game
**Project:** Prix Guesser
**Researched:** 2026-04-08
**Overall confidence:** HIGH for boundary recommendations, MEDIUM for concrete infrastructure choice

## Recommended Architecture

Build Prix Guesser as a **hybrid system with three hard separations**:

1. **Authored content layer**: packs, rounds, clue media, answer targets, reveal explanations, scoring rules metadata
2. **Pure game-rules layer**: mode logic that evaluates submissions and advances phases from a frozen match snapshot
3. **Live room orchestration layer**: authoritative room/session state, timers, submissions, reconnects, host controls, broadcast

That separation matters more than the frontend framework. It preserves the current open questions:

- live rooms vs challenge links
- host-screen-first vs hybrid controller play
- one anchor geography mode vs future adjacent party modes
- PartyKit-speed prototype vs Colyseus-foundation-first server

The core architecture should therefore be **content-first and room-authoritative**, but **transport-agnostic and clue-type-agnostic**.

### Recommended System Shape

```text
Authoring files / sheets / admin tools
  -> Content compiler + validator
  -> Content store (packs, media manifests, asset refs)
  -> Match snapshot service
  -> Authoritative room service
       -> Host display client
       -> Player controller client(s)
       -> Future solo / challenge runner
  -> Session results / analytics store
```

## Architecture Decision

### Default recommendation

Use a **hybrid architecture**:

- **Shared TypeScript domain package** for content schema, answer payloads, scoring contracts, event contracts
- **Separate content store** for authored packs and media metadata
- **Separate authoritative room runtime** for live sessions
- **Thin client surfaces** that send intents and render server-owned room state

### Concrete implementation bias

For this project shape, the best long-term fit is a **Colyseus-class authoritative room model** even if the first prototype is private-only. Colyseus is explicit about rooms, server-owned synchronized state, matchmaking, and reconnection handling, which matches the hard problems here better than generic app realtime alone. PartyKit remains a credible speed-first implementation if the same boundaries are preserved, because it gives each room server access to per-room state, storage, HTTP handlers, and hibernation hooks.

Recommendation wording matters:

- **Recommend the architecture pattern strongly**
- **Keep the runtime implementation choice open**

In practice that means:

- if optimizing for speed to first playable room: PartyKit can host the room runtime
- if optimizing for correctness and growth from day one: Colyseus is the stronger default

Do **not** let persistence, auth, or a BaaS become the source of truth for active round timers and reveal sequencing.

## Component Boundaries

### 1. Content Model Package

**Responsibility:** Define the stable product vocabulary.

This package should own:

- `PackDefinition`
- `RoundDefinition`
- `ClueAsset`
- `AnswerTarget`
- `RevealDefinition`
- `ScoringProfile`
- `ModeDefinition`
- validation schemas

This package should **not** know about:

- WebSockets
- room codes
- reconnect logic
- frontend routing
- database SDKs

Treat it as framework-neutral domain code.

### 2. Content Repository / Compiler

**Responsibility:** Turn authored source material into validated, versioned playable content.

Inputs:

- markdown/json/yaml files
- spreadsheets exported to structured files
- media asset manifests

Outputs:

- normalized pack JSON
- media manifest with stable asset IDs
- validation reports
- pack version hashes

This is where you prevent product drift. Street View metadata, image crops, text clues, map snippets, and future media types all get normalized here instead of leaking directly into gameplay code.

### 3. Match Snapshot Service

**Responsibility:** Freeze a specific playable session from authored content.

A match snapshot should include:

- selected rounds in fixed order
- normalized answer surfaces for that session
- resolved clue references
- round settings and scoring configuration
- pack/version identifiers

This layer is critical. It keeps:

- fairness for live rooms
- reproducibility for future challenge links
- separation between mutable authoring data and live session execution

The room should receive a **match snapshot** or snapshot reference, not raw editable content.

### 4. Game Rules Engine

**Responsibility:** Pure functions for evaluating submissions and phase transitions.

Inputs:

- match snapshot
- current round phase
- timer/status info
- player submissions

Outputs:

- validity result
- score delta
- reveal payload
- next phase transition

This engine should be mode-based:

```ts
interface ModeRuntime {
  validateSubmission(input: SubmissionInput, round: RoundSnapshot): ValidationResult;
  scoreRound(args: ScoreRoundArgs): ScoreRoundResult;
  buildReveal(args: RevealArgs): RevealPayload;
}
```

That keeps the platform from hard-coding “guess a map pin” as the only possible game shape.

### 5. Authoritative Room Service

**Responsibility:** Run the live room.

This service owns:

- room creation/join
- host permissions
- player presence
- current phase
- timer start/stop/expiry
- submission acceptance window
- reveal progression
- scoreboard state
- reconnect recovery

This service should not own authored content design. It should consume a frozen snapshot and operate on session state only.

### 6. Client Surface Shell

**Responsibility:** Render UI for different surfaces using the same contracts.

Separate surfaces:

- **Host display**: watchable round presentation, pacing, reveal, scoreboard
- **Player controller**: private input, clue view, answer UI, reconnect
- **Future solo/challenge surface**: no room presence, same content and rules engine
- **Future admin/authoring surface**: content preview, validation, pack publishing

Keep these as separate route bundles or apps that share contracts and UI primitives, not as one giant screen-state tree.

### 7. Persistence / Asset Layer

**Responsibility:** Store durable things, not active room authority.

Durable data:

- packs
- round snapshots
- media assets
- session summaries
- analytics
- user/profile metadata later

Non-durable live authority:

- active timer
- reveal phase
- in-flight submissions
- host controls

If durable storage becomes the live truth for those runtime fields, race conditions and recovery bugs get much worse.

## Where To Separate Content Modeling From Live Room State

This is the most important structural line in the system.

### Content side

Content should answer:

- what the round is
- what clue assets exist
- what the allowed answer surfaces are
- how scoring is defined
- what the reveal should explain

Example fields:

```ts
type RoundDefinition = {
  id: string;
  mode: "circuit_guess" | "section_guess" | "approach_guess";
  targets: AnswerTarget[];
  clueSteps: ClueAsset[];
  reveal: RevealDefinition;
  scoring: ScoringProfile;
  tags: string[];
};
```

### Live room side

Room state should answer:

- who is in the room
- what round index is active
- what phase the room is in
- how much time is left
- what each player submitted
- whether reveal has happened
- what the total scores are

Example fields:

```ts
type RoomState = {
  roomId: string;
  snapshotId: string;
  phase: "lobby" | "countdown" | "clue" | "locked" | "reveal" | "results";
  activeRoundIndex: number;
  deadlineAt: number | null;
  players: Record<string, PlayerState>;
  submissions: Record<string, SubmissionState>;
  totals: Record<string, number>;
};
```

### Rule

**Never store authoring-editable content as mutable room state.**

Instead:

- content is authored and versioned
- a match snapshot is frozen at session start
- room state references the snapshot and tracks only live execution

That is what prevents future challenge links, rematches, and additional modes from becoming a rewrite.

## Data Flow

### Content publishing flow

```text
Author / curator
  -> content source files or sheet export
  -> content compiler
  -> schema validation + asset validation
  -> pack registry / content store
  -> preview tool / playable dry-run
```

Direction is one-way until a new content version is published.

### Live room startup flow

```text
Host action
  -> app backend chooses pack + settings
  -> match snapshot service freezes playable rounds
  -> room service creates session with snapshot reference
  -> room state broadcast to host + controllers
```

The room never queries “latest authoring state” mid-session.

### Round play flow

```text
Room server
  -> broadcasts current phase + public round payload

Player client
  -> submits intent payload

Room server
  -> validates phase + player eligibility
  -> stores submission
  -> optionally acknowledges receipt

Timer expiry or host advance
  -> rules engine scores against snapshot
  -> room server builds reveal payload
  -> room server broadcasts reveal + updated totals
```

All authoritative transitions flow **client intent -> room server -> rules engine -> room state update -> client render**.

Clients should never compute final truth independently.

### Session close flow

```text
Room server
  -> final standings
  -> session summary record
  -> analytics/event log
  -> room cleanup / archival
```

## Patterns To Follow

### Pattern 1: Mode Plugin Boundary

**What:** Each playable mode implements a shared runtime interface.

**Why:** The product can grow into adjacent party modes without rewriting room infrastructure.

Use one room shell with pluggable mode logic:

- geography anchor mode
- circuit shape recognition later
- era/history identification later
- debate/bluff modes later

The room layer should know phases and submissions, not F1 clue semantics.

Only introduce a **boardgame.io-style phase engine** for a specific future mode once that mode genuinely needs explicit turns, secret state, or heavy phase scripting. Do not make the geography anchor mode depend on that abstraction first.

### Pattern 2: Public State vs Private State

**What:** Separate what everyone sees from what one player sees.

Public examples:

- timer
- active phase
- reveal payload
- scoreboard

Private examples:

- controller input draft
- secret answer before lock
- reconnect token/session binding

This matters immediately for host-screen plus phone-controller play.

### Pattern 3: Event Contract Plus State Snapshot

**What:** Combine synchronized room state with explicit domain events.

Use state for:

- current truth
- totals
- phase
- connected players

Use events for:

- `submission_received`
- `round_locked`
- `reveal_started`
- `host_skipped_clue`

This keeps clients simpler than message-only systems and more debuggable than implicit UI transitions.

### Pattern 4: Clue Asset as Discriminated Union

**What:** Model clue media generically.

```ts
type ClueAsset =
  | { kind: "streetview_static"; assetId: string; heading?: number }
  | { kind: "map_crop"; assetId: string }
  | { kind: "photo"; assetId: string }
  | { kind: "text"; body: string }
  | { kind: "video"; assetId: string; startMs?: number; endMs?: number };
```

Do not build the entire platform around one clue family. Street View can be important without becoming the schema root.

### Pattern 5: Answer Target as Discriminated Union

**What:** Model answers as target types, not one generic coordinate guess.

```ts
type AnswerTarget =
  | { kind: "circuit"; circuitId: string }
  | { kind: "venue"; venueId: string }
  | { kind: "section"; circuitId: string; sectionId: string }
  | { kind: "map_pin"; lat: number; lng: number }
  | { kind: "composite"; parts: AnswerTarget[] };
```

This avoids coupling the whole game to distance scoring.

## Anti-Patterns To Avoid

### Anti-Pattern 1: Thin GeoClone Core

**What goes wrong:** The domain collapses into `lat/lng + panoId + kilometers`.

**Why bad:** You lose F1-specific authored meaning, reveal quality, and future mode growth.

**Instead:** Put F1-authored target types and reveal logic at the center.

### Anti-Pattern 2: Live Room State Stored in the Database as the Main Authority

**What goes wrong:** Timer and phase truth become race-prone shared documents.

**Why bad:** Reconnect, duplicate submissions, and reveal timing get fragile.

**Instead:** Keep live truth in the room runtime; persist summaries and snapshots around it.

### Anti-Pattern 3: Host UI Owns Game Truth

**What goes wrong:** The “host screen” becomes the server by accident.

**Why bad:** Hybrid play, reconnects, remotes, and future challenge reuse all get messy.

**Instead:** Treat the host screen as a privileged client on top of a room authority.

### Anti-Pattern 4: Media-Type Logic Embedded in Room Transitions

**What goes wrong:** Phase logic starts branching on Street View, photo, text, map crop internals.

**Why bad:** Every new clue type rewrites the loop.

**Instead:** Keep room transitions generic and let mode/clue renderers interpret the assets.

### Anti-Pattern 5: One App-State Tree for Every Surface

**What goes wrong:** Host, controller, admin, and solo flows become one tangled frontend.

**Why bad:** Iteration slows and surface-specific behavior becomes hard to test.

**Instead:** Share contracts and components, not one mega-state model.

## Recommended Build Order

This should inform roadmap phase order.

### Phase 1: Domain and content substrate

Build first:

- shared content schema
- pack/round validation
- media manifest format
- mode and answer target contracts
- a handful of hand-authored packs

Why first:

- this de-risks the actual product identity
- every later surface depends on it
- it prevents building a generic geography shell with no F1-native model

### Phase 2: Rules engine and dry-run runner

Build second:

- pure scoring engine
- reveal payload builder
- round phase reducer
- local simulation tests
- minimal single-round preview runner

Why second:

- the game loop becomes testable without realtime complexity
- room code can call pure functions instead of embedding game logic

### Phase 3: Authoritative room runtime

Build third:

- room lifecycle
- join/create/reconnect
- timer control
- submission collection
- reveal broadcast
- scoreboard progression

Why third:

- after content and rules are stable, the room server is mostly orchestration
- this isolates live-state complexity to one layer

### Phase 4: Host and controller surfaces

Build fourth:

- host display
- phone controller
- lobby/join flow
- basic session summary screen

Why fourth:

- surface work is easier once room contracts exist
- you can test watchability against real session state

### Phase 5: Session durability and admin visibility

Build fifth:

- session summaries
- reconnect polish
- room debug tooling
- event logs
- analytics on round quality

Why fifth:

- private play can start before this is perfect
- these systems become clearer once live sessions exist

### Phase 6: Authoring tooling

Build when needed, not before:

- round preview UI
- asset verification workflow
- pack publishing workflow

Start file-first. Productize authoring only after the schema and round grammar settle.

### Phase 7: Adjacent mode expansion

Only after the anchor loop is good:

- add new `ModeRuntime` implementations
- reuse room shell and content pipeline
- add extra state needs only where justified

## How To Avoid Coupling The Product To One Clue Or Transport Mode

### Keep clue rendering behind asset kinds

The content model should say “here is a clue asset” rather than “open Street View now.”

### Keep answer evaluation behind mode/runtime interfaces

The room asks the mode engine to validate and score. It does not inspect F1 clue semantics directly.

### Keep transport behind a client SDK

Expose:

- `joinRoom`
- `subscribeToState`
- `sendIntent`
- `resumeSession`

Whether that runs over Colyseus, PartyKit, or another room transport later should not change the feature code above the SDK boundary.

### Keep solo and async challenge flows on the same content and rules layers

Live rooms should be one execution wrapper, not the entire product architecture.

## Scalability Considerations

| Concern | At 10 friends | At recurring private sessions | At larger community use later |
|---------|---------------|-------------------------------|-------------------------------|
| Content quality | Hand-authored packs are enough | Need validation and pack versioning | Need stronger editorial workflow |
| Room state | Single room process is enough | Need reconnect and room cleanup discipline | Need stronger room discovery and ops visibility |
| Transport | PartyKit or Colyseus both viable | Colyseus-style authority becomes more valuable | Horizontal room scaling matters |
| Persistence | File + object storage is enough | Session summaries and analytics matter | Durable profiles and history matter |
| Mode expansion | One mode interface | Multiple runtimes share shell | More specialized rule engines may emerge |

## Practical Recommendation

If roadmap needs a concrete directional choice today:

- architect for a **shared domain package + frozen match snapshots + authoritative room service**
- bias implementation toward **Colyseus-style room authority**
- keep **frontend choice open between React + Vite and another lean TypeScript UI shell**
- keep **authoring file-first initially**
- treat **Street View as one clue family, not the platform**

This is the cleanest way to support:

- authored rounds
- clue ladders
- synchronized rooms
- host display plus phone controllers
- future challenge links
- future adjacent party modes

without overcommitting to one framework, one media type, or one transport.

## Sources

- Prix Guesser project context: `/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md`
- Prix Guesser discovery seed: `/home/rookslog/workspace/projects/prix-guesser/discovery/14-gsd-seed.md`
- Critical GeoGuessr-core inheritance notes: `/home/rookslog/workspace/projects/prix-guesser/discovery/10-critical-inheritance-geoguessr-core.md`
- Framework decision context: `/home/rookslog/workspace/projects/prix-guesser/discovery/12-framework-decision-context.md`
- Room/backend decision context: `/home/rookslog/workspace/projects/prix-guesser/discovery/13-room-backend-decision-context.md`
- Colyseus docs: https://docs.colyseus.io/state and https://docs.colyseus.io/room/reconnection
- Colyseus Playground docs: https://docs.colyseus.io/tools/playground
- PartyKit docs: https://docs.partykit.io/reference/partyserver-api/, https://docs.partykit.io/guides/persisting-state-into-storage/, https://docs.partykit.io/guides/scaling-partykit-servers-with-hibernation/
- boardgame.io docs: https://boardgame.io/ and https://github.com/boardgameio/boardgame.io/blob/main/docs/documentation/phases.md

## Confidence Notes

- **HIGH:** Separating authored content, pure game rules, and live room state
- **HIGH:** Avoiding database-first authority for timers and reveal flow
- **HIGH:** Using typed mode and clue boundaries to preserve future expansion
- **MEDIUM:** Choosing Colyseus over PartyKit at initialization time; both can support the recommended structure, but Colyseus is the stronger fit if room authority correctness matters early
