# Room / Backend Decision Context

This note exists to clarify what we should care about when choosing the realtime room and backend shape for Prix Guesser.

It does not recommend a winner yet.

## Why This Needs A Separate Note

"Backend" is too vague to be useful on its own.

For this project, the important questions are not just:
- where data is stored
- what server framework we use

The more consequential questions are:
- who is authoritative for round state
- how timers and reveals are synchronized
- how reconnects work
- how private rooms are created and joined
- how much future mode expansion the room model can tolerate

If we do not separate those concerns, we will talk past the real tradeoffs.

## What This Decision Is Not

This is not a single binary choice.

We should separate:
- realtime transport
- room authority model
- persistent storage
- auth or identity
- pack and round content serving
- analytics and operational logging

Examples:
- `PartyKit` does not decide the database
- `Colyseus` does not force a specific frontend
- `Firebase` or `Supabase` do not automatically solve real authoritative game timing
- a private prototype may not need formal auth at all

## What The Room Layer Must Actually Do

At minimum, the room/backend layer needs to support some version of:
- room creation and join
- host authority or server authority
- synchronized round start and round end
- timer progression
- guess submission
- reveal progression
- scoreboard updates
- reconnect behavior
- room cleanup after the session ends

Possible later responsibilities:
- team modes
- challenge links
- rematches
- spectators
- moderation or host controls
- analytics on round quality and player outcomes

## What Actually Matters

### 1. Authority Model Clarity

The deepest backend question is:
- is the host effectively authoritative
or
- is the server authoritative

This affects:
- fairness
- timer trust
- anti-cheat potential
- reconnect behavior
- complexity of implementation

For a private game, host-biased authority may be acceptable early.
For a competitive or expandable game, stronger server authority may matter sooner.

### 2. Synchronization Reliability

This game depends on synchronized:
- round starts
- timer expiration
- reveal transitions
- score updates

If synchronization is sloppy, the core experience feels broken even if the UI is good.

### 3. Reconnect And Recovery Story

Private play still needs a reasonable answer to:
- what happens when a player refreshes
- what happens when a phone sleeps
- what happens when the host disconnects

This matters more here than in a static quiz app because room state is live and sequential.

### 4. Development And Ops Simplicity

We should care about:
- how much custom server code is needed
- how painful local multiplayer testing is
- how easy deployment is
- how easy runtime debugging is

AI can write room code quickly.
It does not remove the cost of understanding a fragile realtime system.

### 5. Growth Path

The room model should not be so narrow that it blocks likely expansions such as:
- couch plus remote hybrid play
- team scoring
- secret-answer or bluff modes
- multi-phase party variants
- richer host control surfaces

This does not mean building for all of that now.
It means not choosing a model that obviously fights it.

### 6. Content Model Compatibility

The room/backend layer has to work cleanly with the authored round model.

That means it should tolerate:
- different answer target types
- partial-credit scoring
- clue ladders
- reveal explanations
- different round media types

If the room system assumes every round is the same generic location drop, it will push the design in the wrong direction.

### 7. Agent Editability And Inspectability

The room code should be easy for humans and agents to inspect.

This usually favors:
- explicit message types
- explicit room state
- predictable transition functions
- minimal hidden magic around synchronization

## Criteria To Evaluate Any Candidate

When we compare candidate room stacks later, the useful criteria are:
- clarity of room lifecycle
- clarity of authority model
- timer and state synchronization reliability
- reconnect and recovery ergonomics
- ease of private-room setup
- host control ergonomics
- ease of local development and multi-client testing
- ease of integrating with frontend and content model
- ease of adding logging and admin visibility
- ability to grow into adjacent party modes

## Candidate Room / Backend Shapes

These are not recommendations. They are the current serious candidates or useful comparison shapes.

### PartyKit

Strengths:
- fast path to room-based browser multiplayer
- lightweight private-room setup
- lower ceremony for early prototypes
- strong fit for host-screen orchestration and controller clients

Risks:
- may need more custom discipline as complexity grows
- can be easier to ship quickly than to structure well
- long-term authority and recovery patterns need deliberate design, not assumption

Best fit when:
- proving room energy quickly matters most
- the first version is private and moderately scoped

### Colyseus

Strengths:
- strong room abstraction
- better fit for authoritative state and timer control
- better reconnection and matchmaking story
- more natural if fairness and sync correctness matter early

Risks:
- higher upfront structure and complexity
- more server-shape thinking from the start
- may be heavier than needed if the first prototype is intentionally lightweight

Best fit when:
- we want a sturdier long-term room foundation
- hybrid couch plus remote or fairness-sensitive play is important early

### boardgame.io

Strengths:
- good fit for phases, turns, secret state, logs, and server-managed transitions
- potentially strong for future party variants beyond the core GeoGuessr-like mode

Risks:
- less natural for the geography/reveal loop itself
- can push the design toward turn-engine abstractions that are not the best fit for map-centric rounds

Best fit when:
- the product starts leaning toward structured party modes with explicit phases

### BaaS-Led Realtime Shape

Examples:
- `Firebase`
- `Supabase`

Strengths:
- fast path for persistence, presence, and simple synchronization
- attractive if we want storage, auth, and app plumbing with low ceremony

Risks:
- easy to confuse "shared data" with "authoritative game state"
- timers and race conditions may become awkward if the game loop needs strong authority
- may look simpler at first than it feels once live room sequencing gets real

Best fit when:
- we want a broad app substrate quickly
- the first prototype tolerates softer authority

### Hybrid Shape

Example pattern:
- authoritative room server for live session state
- separate storage layer for packs, authored rounds, analytics, and profiles

Strengths:
- keeps live gameplay concerns separate from content and persistence concerns
- likely the cleanest long-term shape if the project grows

Risks:
- more moving parts
- easiest to over-engineer too early

Best fit when:
- we are consciously building a foundation rather than only a toy prototype

## What We Should Not Overweight

Do not over-index on:
- whichever option sounds most "scalable" in the abstract
- generic backend fashion
- auth or database convenience being mistaken for game-loop fit
- the hope that one product handles transport, authority, persistence, and growth with no tradeoffs

Those are weak shortcuts.

## Reasonable Decision Triggers

The room/backend decision should probably happen when we can answer these more concretely:
- is the first proof solo-first, host-screen-first, or hybrid from day one
- how much fairness do we actually need in v0
- how much reconnect tolerance do we want immediately
- whether live rooms or challenge links are the first-class shared format
- how soon adjacent party modes need stronger phase or secret-state support

Until then, it is enough to keep the candidate set explicit and the criteria sharp.

## Current Non-Binding Read

The current decision context points to this:
- `PartyKit` is the cleanest speed-first candidate for a private prototype
- `Colyseus` is the strongest foundation-first candidate if room authority and recovery matter early
- `boardgame.io` looks more valuable for later phase-heavy party modes than for the GeoGuessr core
- a BaaS-led approach may help with app plumbing, but should not be confused with a solved room-authority model
- the decisive question is less "which backend is best" and more "how authoritative and durable does the first live-room experience need to be"

This should be read as a framing aid, not a backend decision.
