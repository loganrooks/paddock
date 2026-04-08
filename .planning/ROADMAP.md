# Roadmap: Prix Guesser

## Overview

Prix Guesser v1 is sequenced to prove one authored F1 anchor mode and one strong private-room social wrapper without drifting into generic geography or premature party-platform breadth. The roadmap starts by locking the authored content and scoring contract, then freezes sessions into authoritative live rooms, then turns that foundation into a watchable host-screen plus phone-controller loop, and only after that expands the curated corpus, calibration, and reconnect hardening needed for repeat real-world play.

## Open Decisions Still Visible

- The roadmap commits v1 to live private rooms as the first social wrapper, but keeps the room runtime choice open until planning clarifies how strong the reconnect and timer guarantees must be.
- v1 answer surfaces are intentionally anchored at `circuit` and `venue`; finer-grained `section` or `corner` answers stay out of scope unless a later inserted phase is justified by playtest evidence.
- The content model is designed to support future adjacent F1 party modes, but no non-anchor mode is planned until the geography-and-circuit loop proves repeat-play value.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Authored Round Contract** - Define the authored pack and round substrate with validation and media fallback rules.
- [ ] **Phase 2: Core Round Rules** - Make the anchor mode playable and judgeable outside live-room transport.
- [ ] **Phase 3: Session Snapshots And Room Authority** - Launch fixed pack sessions in authoritative private rooms with explicit pacing rules.
- [ ] **Phase 4: Guest Join And Mobile Controller UI** - Let guests join quickly and submit the right answer type from phones or browsers.
- [ ] **Phase 5: Host Screen And Watchable Session Flow** - Turn the room into a shared-screen game night loop with reveals, standings, and replay flow.
- [ ] **Phase 6: Starter Packs And Calibration** - Prove the core loop with curated packs and record enough session data to improve round quality.
- [ ] **Phase 7: Reconnect And Session Durability** - Harden active-room recovery for refreshes, disconnects, and phone sleep.

## Phase Details

### Phase 1: Authored Round Contract
**Goal**: Authors can define validated F1 rounds and packs that preserve circuit-aware meaning, clue ladders, reveal explanations, and fallback media strategy before any live-room work begins.
**Depends on**: Nothing (first phase)
**Requirements**: PACK-02, PACK-03, PACK-04, OPS-01
**Success Criteria** (what must be TRUE):
  1. Author can define a round with an explicit answer target type, clue steps, accepted answers or aliases, reveal explanation, and scoring profile.
  2. A pack can mix Street View clues and non-Street-View fallback media without changing the round contract.
  3. Pack validation rejects incomplete, ambiguous, or broken rounds before they become playable.
  4. Content workflow records each round's venue coverage class and fallback strategy so fallback-first venues are explicit instead of silent substitutions.
**Plans**: TBD

### Phase 2: Core Round Rules
**Goal**: Testers can run the anchor round loop against frozen authored content with explicit judging, partial credit, and reveal grammar independent of room transport and UI layers.
**Depends on**: Phase 1
**Requirements**: GAME-01, GAME-02, GAME-03, GAME-05, OPS-03
**Success Criteria** (what must be TRUE):
  1. Tester can play an authored anchor round that asks for at least `circuit` or `venue` identification.
  2. The game judges answers against the round's explicit answer surface instead of relying only on raw map distance.
  3. The game awards partial correctness according to the round's scoring rules when a submission is substantively right but not maximally specific.
  4. Every round ends with a reveal that explains why the answer was identifiable, not only whether the player was correct.
  5. The core gameplay logic is testable independently of the room transport and UI layers.
**Plans**: TBD

### Phase 3: Session Snapshots And Room Authority
**Goal**: Hosts can create authoritative private-room sessions from curated packs with fixed round snapshots and explicit pacing rules.
**Depends on**: Phase 2
**Requirements**: PACK-01, GAME-04, ROOM-01, ROOM-03
**Success Criteria** (what must be TRUE):
  1. Host can create a private room and launch a session from a selected curated pack.
  2. Starting a session freezes a fixed snapshot of rounds for that room so every participant plays the same session definition.
  3. Host can configure or select pacing rules, including timer length and clue cadence, for the session or chosen pack.
  4. The room maintains the canonical round phase, timer, submissions, and scores for all participants.
**Plans**: TBD
**Open decisions**: Choose `Colyseus` if this phase promises strong reconnect and timer correctness from the start; choose `PartyKit` only if planning explicitly optimizes for private-prototype speed over early durability.

### Phase 4: Guest Join And Mobile Controller UI
**Goal**: Guests can enter live rooms with minimal friction and use a responsive controller surface that makes the required answer contract obvious before submission.
**Depends on**: Phase 3
**Requirements**: ROOM-02, UX-02, UX-03
**Success Criteria** (what must be TRUE):
  1. Guest can join a private room from phone or browser via room code, join link, or QR flow without needing a full account.
  2. The mobile controller UI supports answer entry and submission within the active round timer.
  3. The controller clearly communicates the required answer surface for the round before the player submits.
**Plans**: TBD
**UI hint**: yes

### Phase 5: Host Screen And Watchable Session Flow
**Goal**: The shared-screen experience becomes a coherent social game loop from clue presentation through answer lock, reveal, standings, and replay.
**Depends on**: Phase 4
**Requirements**: ROOM-05, UX-01, UX-04
**Success Criteria** (what must be TRUE):
  1. The host screen presents clue state, lock state, reveal, and standings in a watchable shared-screen format.
  2. Host can move the room through clue, answer lock, reveal, standings, and rematch or replay flow without manual admin workarounds.
  3. A session ends with a summary that lets the group review outcomes and immediately replay or switch packs.
**Plans**: TBD
**UI hint**: yes

### Phase 6: Starter Packs And Calibration
**Goal**: The first release proves the core loop with curated starter content and captures enough round-level evidence to improve the corpus instead of guessing.
**Depends on**: Phase 5
**Requirements**: PACK-05, OPS-02
**Success Criteria** (what must be TRUE):
  1. The initial release includes a curated starter pack set built around high-recognition circuits and venue contexts rather than exhaustive calendar coverage.
  2. Session data records per-round outcomes sufficient to identify broken, trivial, misleading, or high-value rounds.
  3. Authors can use recorded session evidence to decide which rounds to keep, revise, or retire.
**Plans**: TBD

### Phase 7: Reconnect And Session Durability
**Goal**: Active private-room sessions stay recoverable when browsers refresh, networks wobble, or phone controllers sleep and wake mid-game.
**Depends on**: Phase 5
**Requirements**: ROOM-04
**Success Criteria** (what must be TRUE):
  1. Player can reconnect to an active room after a refresh and recover current session state without manual host repair.
  2. Temporary disconnects or phone sleep restore the player's current round context, timer context, and score state correctly.
  3. Recovery behavior is reliable enough that active sessions continue cleanly after common controller interruptions.
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6 → 7

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Authored Round Contract | 0/TBD | Not started | - |
| 2. Core Round Rules | 0/TBD | Not started | - |
| 3. Session Snapshots And Room Authority | 0/TBD | Not started | - |
| 4. Guest Join And Mobile Controller UI | 0/TBD | Not started | - |
| 5. Host Screen And Watchable Session Flow | 0/TBD | Not started | - |
| 6. Starter Packs And Calibration | 0/TBD | Not started | - |
| 7. Reconnect And Session Durability | 0/TBD | Not started | - |
