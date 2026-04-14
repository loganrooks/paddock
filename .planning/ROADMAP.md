# Roadmap: Prix Guesser

## Overview

Prix Guesser v1 is sequenced to prove one authored F1 anchor mode and one strong private-room social wrapper without drifting into generic geography, premature public-product obligations, or premature party-platform breadth. The roadmap starts by locking the authored content and scoring contract, then proves rules truth, then freezes sessions into authoritative private rooms with a browser-first operator and join spine, then formalizes the host-screen/controller interaction contract before implementation widens into UI work, and only after that expands into the watchable session loop, starter calibration, and reconnect hardening needed for repeat real-world play. Milestone 01 should preserve separation between room shell, active game instance, visibility surface, and later recurrence layers even when the first playable wrapper renders them simply.

## Open Decisions Still Visible

- The roadmap commits v1 to live private rooms as the first social wrapper, but keeps the room runtime choice open until planning clarifies how strong the reconnect and timer guarantees must be.
- The room runtime choice is also a deployment and self-host-parity decision, not only a multiplayer-library taste choice.
- v1 answer surfaces are intentionally anchored at `circuit` and `venue`; finer-grained `section` or `corner` answers stay out of scope unless a later inserted phase is justified by playtest evidence, but the answer-target model should preserve that hierarchy now.
- The content model is designed to support later async, spectator, and adjacent-mode wrappers, but none of those wrappers are on the v1 spine until the geography-and-circuit loop proves repeat-play value.
- Visibility state stays explicit: private trusted-room play now, unlisted/share-by-link surfaces later, and broader public discovery only when stronger moderation and service obligations are chosen deliberately.
- The first useful room-lifecycle and capability bundle remains open; planning should preserve the seam without pretending the final role model is already known.
- The durable noun for recurring group identity remains open; planning should not silently collapse player history, room/group memory, event memory, and content history into one default ledger.
- Higher-tempo transport and authority specifics remain deferred unless a later mode family actually earns them.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Authored Round Contract** - Define the authored pack and round substrate with validation and media fallback rules.
- [ ] **Phase 2: Core Round Rules** - Make the anchor mode playable and judgeable outside live-room transport.
- [ ] **Phase 3: Session Snapshots, Room Authority, And Operator Launch** - Launch fixed pack sessions in authoritative private rooms with explicit pacing rules and a repeatable private-host operator flow.
- [ ] **Phase 3.1 (INSERTED): UI Direction, Design System, And Interaction Contract** - Freeze the host-screen, controller, join, and reveal interaction contract before UI implementation.
- [ ] **Phase 4: Guest Join, QR Entry, And Mobile Controller UI** - Let guests join quickly and submit the right answer type from phones or browsers.
- [ ] **Phase 5: Host Screen And Watchable Session Flow** - Turn the room into a shared-screen game night loop with reveals, standings, and replay flow.
- [ ] **Phase 6: Starter Packs And Calibration** - Prove the core loop with curated packs and record enough session data to improve round quality.
- [ ] **Phase 7: Reconnect And Session Durability** - Harden active-room recovery for refreshes, disconnects, and phone sleep.

## Phase Details

### Phase 1: Authored Round Contract
**Goal**: Authors can define validated F1 rounds and packs that preserve circuit-aware meaning, answer-target relationships, clue ladders, reveal explanations, and fallback media strategy before any live-room work begins.
**Depends on**: Nothing (first phase)
**Requirements**: PACK-02, PACK-03, PACK-04, OPS-01
**Success Criteria** (what must be TRUE):
  1. Author can define a round with an explicit answer target type, clue steps, accepted answers or aliases, reveal explanation, and scoring profile.
  2. A pack can mix Street View clues and non-Street-View fallback media without changing the round contract.
  3. Pack validation rejects incomplete, ambiguous, or broken rounds before they become playable.
  4. Content workflow records each round's venue coverage class and fallback strategy so fallback-first venues are explicit instead of silent substitutions.
**Canonical refs**:
- `.planning/REQUIREMENTS.md` — `PACK-02`, `PACK-03`, `PACK-04`, `OPS-01`, `SEAM-01`, `SEAM-04`, `DEF-01`, `DEF-04`
- `.planning/PROJECT.md` — future-aware posture, private trusted-group product stance, geography fidelity
- `.planning/LONG-ARC.md` — long-arc product, visibility, hosting, support, and wrapper doctrine that current work must preserve without widening v1 scope
**Plans**: 4 plans
**Protects**: The authored round substrate, answer-surface contract, and fallback-media model stay extensible enough for later `venue -> circuit -> section -> corner` growth or wrapper expansion without rewriting the pack contract.
**Does not decide yet**: Public challenge surfaces, room runtime, account-backed persistence, and adjacent non-anchor modes.
**Assumed posture**: Private authored packs for trusted-circle play, with no public service or moderation obligation.
Plans:
- [ ] 01-01-PLAN.md — Bootstrap the workspace and shared content-contract interfaces
- [ ] 01-02-PLAN.md — Implement strict domain schemas, normalization, and contract tests
- [ ] 01-03-PLAN.md — Author venue profiles and starter-pack YAML fixtures
- [ ] 01-04-PLAN.md — Build the YAML compiler, invariant checks, and compile CLI

### Phase 2: Core Round Rules
**Goal**: Testers can run the anchor round loop against frozen authored content with explicit judging, partial credit, and reveal grammar independent of room transport and UI layers.
**Depends on**: Phase 1
**Requirements**: GAME-01, GAME-02, GAME-03, GAME-05, OPS-03
**Success Criteria** (what must be TRUE):
  1. Tester can play an authored anchor round that asks for at least `circuit` or `venue` identification.
  2. The game judges answers against the round's explicit answer surface instead of relying only on raw map distance.
  3. The game awards partial correctness according to the round's scoring rules when a submission is substantively right but not maximally specific, preserving room for later answer-surface hierarchy.
  4. Every round ends with a reveal that explains why the answer was identifiable, not only whether the player was correct.
  5. The core gameplay logic is testable independently of the room transport and UI layers.
**Canonical refs**:
- `.planning/REQUIREMENTS.md` — `GAME-01`, `GAME-02`, `GAME-03`, `GAME-05`, `OPS-03`, `SEAM-01`, `SEAM-02`, `DEF-04`
- `.planning/PROJECT.md` — anchor-mode posture, authored-round bias, geography fidelity
- `.planning/LONG-ARC.md` — long-arc product, visibility, hosting, support, and wrapper doctrine that current work must preserve without widening v1 scope
**Plans**: TBD
**Protects**: Structured judging, reveal grammar, and gameplay logic that can survive later room, controller, or wrapper changes.
**Does not decide yet**: Live-room transport, public challenge modes, account systems, or finer-grained answer surfaces as default v1 scope.
**Assumed posture**: Private testing and trusted-group play, still centered on the anchor loop rather than public retention features.

### Phase 3: Session Snapshots, Room Authority, And Operator Launch
**Goal**: Hosts can create authoritative private-room sessions from curated packs through one repeatable local or privately hosted operator flow, with fixed round snapshots and explicit pacing rules.
**Depends on**: Phase 2
**Requirements**: PACK-01, GAME-04, ROOM-01, ROOM-03, DEPLOY-01, DEPLOY-04, DEPLOY-05
**Success Criteria** (what must be TRUE):
  1. Host can bring up a joinable private-room session from one documented operator flow in local-LAN mode while preserving a clear path to privately hosted remote play.
  2. Starting a session freezes a fixed snapshot of rounds for that room so every participant plays the same session definition.
  3. Host can configure or select pacing rules, including timer length and clue cadence, for the session or chosen pack.
  4. The room maintains the canonical round phase, timer, submissions, and scores for all participants.
  5. The chosen room runtime and deploy shape support private browser guest access without requiring guests to install operator networking tools or use source-checkout workflows.
**Canonical refs**:
- `.planning/REQUIREMENTS.md` — `PACK-01`, `GAME-04`, `ROOM-01`, `ROOM-03`, `DEPLOY-01`, `DEPLOY-04`, `DEPLOY-05`, `SEAM-03`, `SEAM-05`, `DEF-01`, `DEF-02`, `DEF-03`
- `.planning/PROJECT.md` — future-aware posture, private-room bias, room authority remains open until planning
- `.planning/LONG-ARC.md` — long-arc product, visibility, hosting, support, and wrapper doctrine that current work must preserve without widening v1 scope
**Plans**: TBD
**Protects**: Room authority, room-shell versus active-instance separation, frozen session definitions, presence-vs-persistence identity seams, and pack-to-session boundaries that later controllers, host screens, async wrappers, or reconnect logic can rely on.
**Does not decide yet**: Public rooms, monetized hosting, ambient discovery flows, or stronger public reliability promises than private-room play needs.
**Carry-forward constraints**:
- Do not plan this phase as if `room`, `event container`, `active game instance`, and `recurrence unit` are the same object.
- Do not fuse `host`, `authority`, `presenter`, and future operator/moderation rights into one permanent role model.
**Still open**: The first useful capability bundle and exact room-lifecycle primitive set remain open even though the seam must stay visible.
**Assumed posture**: Host-created private rooms with a limited trust boundary, modest service obligation, and an operator-run local or privately hosted deployment.
**Open decisions**: Choose `Colyseus` if this phase promises strong reconnect and timer correctness or self-host/private-host parity from the start; choose `PartyKit` only if planning explicitly optimizes for private-prototype speed over early durability and deployment parity.

### Phase 3.1 (INSERTED): UI Direction, Design System, And Interaction Contract
**Goal**: The project has a frozen interaction contract for host screen, controller, join, and reveal states before Phase 4 or Phase 5 implementation begins.
**Depends on**: Phase 3
**Requirements**: UX-01, UX-02, UX-03, UX-04, DEPLOY-02, DEPLOY-03
**Success Criteria** (what must be TRUE):
  1. `UI-SPEC.md` defines visual direction, typography, color system, motion grammar, and separate host-screen versus controller principles.
  2. The join flow, controller answer flow, host clue state, answer lock, reveal, standings, and replay states are specified before implementation work begins.
  3. Responsive rules explicitly cover phone portrait, laptop operator, and 16:9 TV or fullscreen host-screen contexts.
  4. Watchability is made concrete as shared-legibility, suspense, and reveal payoff rather than left as an abstract aspiration.
**Canonical refs**:
- `.planning/REQUIREMENTS.md` — `UX-01`, `UX-02`, `UX-03`, `UX-04`, `DEPLOY-02`, `DEPLOY-03`, `SEAM-03`
- `.planning/PROJECT.md` — watchability bias, browser-first guest experience, private trusted-room posture
- `.planning/LONG-ARC.md` — long-arc product, visibility, hosting, support, and wrapper doctrine that current work must preserve without widening v1 scope
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md` — converged design-gap diagnosis
**Plans**: TBD
**Protects**: The host/controller split, motion grammar, room-legibility contract, and multi-surface interaction assumptions from being improvised file-by-file during implementation.
**Does not decide yet**: Final art polish scope beyond the phase contract, native apps, or public spectator tooling.
**Carry-forward constraints**:
- Host-screen-friendly means watchability and shared legibility, not one permanent truth surface for every participant.
- The interaction contract should stay compatible with staged reveal, private submissions, and topology-sensitive variants rather than silently hardcoding one shared-state display model.
**Assumed posture**: TV-legible private sessions with phone/browser controllers and a distinct shared-screen ritual.
**UI hint**: yes

### Phase 4: Guest Join, QR Entry, And Mobile Controller UI
**Goal**: Guests can enter live rooms with minimal friction and use a responsive controller surface that makes the required answer contract obvious before submission.
**Depends on**: Phase 3.1
**Requirements**: ROOM-02, UX-02, UX-03, DEPLOY-02
**Success Criteria** (what must be TRUE):
  1. Guest can join a private room from phone or browser via room code, join link, or QR flow without needing a full account or operator-side networking setup.
  2. The active deployment mode exposes a current join URL and QR code that the host can present to the room.
  3. The mobile controller UI supports answer entry and submission within the active round timer.
  4. The controller clearly communicates the required answer surface for the round before the player submits.
**Canonical refs**:
- `.planning/REQUIREMENTS.md` — `ROOM-02`, `UX-02`, `UX-03`, `DEPLOY-02`, `SEAM-03`, `DEF-01`, `DEF-02`
- `.planning/PROJECT.md` — future-aware posture, browser-first private social play
- `.planning/LONG-ARC.md` — long-arc product, visibility, hosting, support, and wrapper doctrine that current work must preserve without widening v1 scope
**Plans**: TBD
**Protects**: A reusable controller contract, answer-entry surface, and lifecycle-sensitive join spine that can survive later room wrappers or teammate variants.
**Does not decide yet**: Native apps, public onboarding, spectator participation, or account-linked identity flows.
**Carry-forward constraints**:
- Do not flatten `join`, `rejoin`, `seat claim`, and later audience-only entry into one identical flow.
- Keep low-friction presence identity separable from later persistent identity and progression surfaces.
**Assumed posture**: Trusted guests joining private rooms quickly from phones or browsers without a public-user platform commitment.
**UI hint**: yes

### Phase 5: Host Screen And Watchable Session Flow
**Goal**: The shared-screen experience becomes a coherent social game loop from clue presentation through answer lock, reveal, standings, and replay.
**Depends on**: Phase 4
**Requirements**: ROOM-05, UX-01, UX-04, DEPLOY-03
**Success Criteria** (what must be TRUE):
  1. The host screen presents clue state, lock state, reveal, and standings in a watchable shared-screen format that remains legible on a 16:9 TV or fullscreen display at couch distance.
  2. Host can move the room through clue, answer lock, reveal, standings, and rematch or replay flow without manual admin workarounds.
  3. A session ends with a summary that lets the group review outcomes and immediately replay or switch packs.
  4. Motion and visual emphasis make answer lock, reveal payoff, and score movement legible to active players and spectators in the room.
**Canonical refs**:
- `.planning/REQUIREMENTS.md` — `ROOM-05`, `UX-01`, `UX-04`, `DEPLOY-03`, `SEAM-02`, `SEAM-03`, `DEF-01`, `DEF-02`
- `.planning/PROJECT.md` — watchability bias, host-screen-friendly social format
- `.planning/LONG-ARC.md` — long-arc product, visibility, hosting, support, and wrapper doctrine that current work must preserve without widening v1 scope
**Plans**: TBD
**Protects**: A watchable shared-screen ritual that could later support stream-friendly or showcase-adjacent wrappers without changing the core room contract.
**Does not decide yet**: Public spectator flows, open showcases, or asynchronous viewing/replay products.
**Carry-forward constraints**:
- Preserve staged reveal and audience readability without universalizing one shared truth surface.
- Keep the host screen compatible with private-state modes and bounded audience shells that may be earned later.
**Assumed posture**: Shared-screen private sessions where host-led pacing and group readability matter more than public broadcast scale.
**UI hint**: yes

### Phase 6: Starter Packs And Calibration
**Goal**: The first release proves the core loop with curated starter content and captures enough structured session evidence to improve the corpus instead of guessing.
**Depends on**: Phase 5
**Requirements**: PACK-05, OPS-02
**Success Criteria** (what must be TRUE):
  1. The initial release includes a curated starter pack set built around high-recognition circuits and venue contexts rather than exhaustive calendar coverage.
  2. Session data records round-level and clue-step evidence sufficient to identify broken, trivial, misleading, fallback-heavy, or high-value rounds.
  3. Authors can use recorded session evidence to decide which rounds to keep, revise, retire, or rebalance by venue class and clue type.
**Canonical refs**:
- `.planning/REQUIREMENTS.md` — `PACK-05`, `OPS-02`, `SEAM-04`, `DEF-02`, `DEF-03`, `DEF-04`
- `.planning/PROJECT.md` — curated-quality posture, shared substrate remains reusable
- `.planning/LONG-ARC.md` — long-arc product, visibility, hosting, support, and wrapper doctrine that current work must preserve without widening v1 scope
**Plans**: TBD
**Protects**: Content curation, calibration seams, and content-history separation that can later power broader pack libraries or other wrappers without assuming a marketplace now.
**Does not decide yet**: Public UGC publishing, pack marketplace logic, or large-scale telemetry/service obligations.
**Carry-forward constraints**:
- Do not treat content calibration, replay history, player history, room/group memory, and event memory as one flat ledger.
- Keep cadence layering visible: session pacing, editorial/content rhythm, and later event cadence should not be collapsed into one model by default.
**Assumed posture**: Curated private release with enough evidence capture to improve quality, not a public content platform.

### Phase 7: Reconnect And Session Durability
**Goal**: Active private-room sessions stay recoverable when browsers refresh, networks wobble, or phone controllers sleep and wake mid-game.
**Depends on**: Phase 5
**Requirements**: ROOM-04
**Success Criteria** (what must be TRUE):
  1. Player can reconnect to an active room after a refresh and recover current session state without manual host repair.
  2. Temporary disconnects or phone sleep restore the player's current round context, timer context, and score state correctly.
  3. Recovery behavior is reliable enough that active sessions continue cleanly after common controller interruptions.
**Canonical refs**:
- `.planning/REQUIREMENTS.md` — `ROOM-04`, `SEAM-03`, `DEF-03`
- `.planning/PROJECT.md` — private-room posture, modest but real durability expectations
- `.planning/LONG-ARC.md` — long-arc product, visibility, hosting, support, and wrapper doctrine that current work must preserve without widening v1 scope
**Plans**: TBD
**Protects**: Session durability and lifecycle-continuity seams that later wrappers or stronger hosting promises can build on without rewriting room state ownership.
**Does not decide yet**: SLA-like uptime guarantees, paid access, or public-scale reliability commitments.
**Carry-forward constraints**:
- Treat reconnect as room-lifecycle and authority continuity work, not only browser refresh state reload.
- Preserve continuity for active round context, ownership, and role/state recovery without assuming the presenter surface is the only state-bearing surface.
**Assumed posture**: Modest private-hosting expectations where common refresh and sleep interruptions should recover cleanly.

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 3.1 → 4 → 5 → 6 → 7

> Operational note (2026-04-14): Phase 1 remains at a pre-rerun boundary. The current `01-*` phase artifacts are useful inputs and historical steering, but fresh discuss + planning output is still required before execution resumes.

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Authored Round Contract | 0/4 | Replanning required | - |
| 2. Core Round Rules | 0/TBD | Not started | - |
| 3. Session Snapshots, Room Authority, And Operator Launch | 0/TBD | Not started | - |
| 3.1 (INSERTED) UI Direction, Design System, And Interaction Contract | 0/TBD | Not started | - |
| 4. Guest Join, QR Entry, And Mobile Controller UI | 0/TBD | Not started | - |
| 5. Host Screen And Watchable Session Flow | 0/TBD | Not started | - |
| 6. Starter Packs And Calibration | 0/TBD | Not started | - |
| 7. Reconnect And Session Durability | 0/TBD | Not started | - |

---
*Last updated: 2026-04-14 after rerun-boundary and governance cleanup*
