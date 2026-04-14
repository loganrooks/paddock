# Requirements: Prix Guesser

**Defined:** 2026-04-08
**Core Value:** Knowledgeable F1 fans can have a genuinely compelling, social, expert-feeling game night built around authored F1 rounds that reward real sport-specific recognition and interpretation

## v1 Requirements

### Packs And Content

- [ ] **PACK-01**: Host can start a session from a curated F1 pack containing a fixed snapshot of rounds for that session.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Architecture Approach`
- [ ] **PACK-02**: Author can define a round with explicit answer target type, clue steps, accepted answers or aliases, reveal explanation, and scoring profile.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Critical Pitfalls`
- [ ] **PACK-03**: A round can reference multiple clue media types, including Street View where available and non-Street-View fallback media where needed.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Recommended Stack`
- [ ] **PACK-04**: Pack validation rejects incomplete, ambiguous, or broken rounds before they become playable.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Critical Pitfalls`
- [ ] **PACK-05**: The initial release includes a curated starter pack set built around high-recognition circuits and venue contexts rather than exhaustive calendar coverage.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Expected Features`

### Anchor Gameplay

- [ ] **GAME-01**: Player can play an authored anchor round that asks for at least `circuit` or `venue` identification.
  - *Motivation:* `user: discovery/14-gsd-seed.md#Anchor Mode Shape`
- [ ] **GAME-02**: Game judges answers against an explicit answer surface instead of relying only on raw map distance.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Critical Pitfalls`
- [ ] **GAME-03**: Game can award partial correctness according to the round's scoring rules when the player is right in substance but not at maximum specificity.
  - *Motivation:* `research: .planning/research/FEATURES.md#Table Stakes`
- [ ] **GAME-04**: Host can configure or select round pacing rules, including timer length and clue cadence, for a session or pack.
  - *Motivation:* `research: .planning/research/FEATURES.md#Table Stakes`
- [ ] **GAME-05**: Every round ends with a reveal that explains why the answer was identifiable, not only whether the player was correct.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Executive Summary`

### Rooms And Session Flow

- [ ] **ROOM-01**: Host can create a private room and launch a session from a selected curated pack.
  - *Motivation:* `research: .planning/research/FEATURES.md#Table Stakes`
- [ ] **ROOM-02**: Guest can join a private room from phone or browser via room code, join link, or QR flow without needing a full account.
  - *Motivation:* `research: .planning/research/FEATURES.md#What Products In This Space Typically Have`
- [ ] **ROOM-03**: Room maintains canonical round phase, timer, submissions, and scores for all participants.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Architecture Approach`
- [ ] **ROOM-04**: Player can reconnect to an active room after refresh, temporary disconnect, or phone sleep and recover current session state.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Critical Pitfalls`
- [ ] **ROOM-05**: Host can move the room through clue, answer lock, reveal, standings, and rematch or replay flow without manual admin workarounds.
  - *Motivation:* `research: .planning/research/FEATURES.md#Table Stakes`

### Host And Controller Experience

- [ ] **UX-01**: Host display presents clue state, lock state, reveal, and standings in a watchable shared-screen format that remains legible on a 16:9 TV at couch distance.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Expected Features`
- [ ] **UX-02**: Player controller is usable on mobile and supports answer entry and submission within the active round timer.
  - *Motivation:* `research: .planning/research/FEATURES.md#Table Stakes`
- [ ] **UX-03**: Game clearly communicates the required answer surface for the round before the player submits.
  - *Motivation:* `research: .planning/research/PITFALLS.md#Pitfall 8: Ambiguous prompts and scoring contracts`
- [ ] **UX-04**: Session ends with a summary that lets the group review outcomes and immediately replay or switch packs.
  - *Motivation:* `research: .planning/research/FEATURES.md#Table Stakes`

### Deployment And Access

- [ ] **DEPLOY-01**: Host can start a playable local-LAN or privately hosted session from one documented operator flow without requiring guests to install anything beyond a browser.
  - *Motivation:* `research: .planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md#Feasible Staged Paths`
- [ ] **DEPLOY-02**: The system can generate and display a valid join URL and QR code for the current deployment mode.
  - *Motivation:* `research: .planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md#Transition Patterns That Preserve Trust`
- [ ] **DEPLOY-03**: Host display is usable on a 16:9 TV or fullscreen display at couch distance and supports fullscreen presentation without cast-specific integrations.
  - *Motivation:* `research: .planning/research/2026-04-10-vision-hosting-wave/findings/03-precedents-and-trajectories.md#Transferable Patterns`
- [ ] **DEPLOY-04**: Privately hosted remote play supports HTTPS and WebSocket-capable ingress without requiring guest networking tools such as Tailscale.
  - *Motivation:* `research: .planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md#Path 2: Private remote play from personal hardware`
- [ ] **DEPLOY-05**: Operator can start and stop the hosted deployment on demand with one documented command or script.
  - *Motivation:* `research: .planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md#Path 3: Small public hosted operation`

### Content Operations And Calibration

- [ ] **OPS-01**: Content workflow records venue coverage class and fallback strategy so rounds do not assume uniform Street View viability.
  - *Motivation:* `research: .planning/research/PITFALLS.md#Pitfall 6: Treating Street View coverage as uniform, stable, and available at play time`
- [ ] **OPS-02**: Session data records round-level and clue-step outcomes sufficient to identify broken, trivial, misleading, fallback-heavy, or high-value rounds.
  - *Motivation:* `research: .planning/research/PITFALLS.md#Pitfall 9: No calibration loop for authored content`
- [ ] **OPS-03**: The system's core gameplay logic is testable independently of the room transport and UI layers.
  - *Motivation:* `research: .planning/research/SUMMARY.md#Architecture Approach`

## v2 Requirements

### Finer-Grained Answer Surfaces

- **ADV-01**: Player can answer at `section` or `corner` specificity in selected packs or modes.
- **ADV-02**: Game supports composite answer formats such as `circuit + corner`.

### Additional Wrappers

- **WRAP-01**: Player can play async or solo challenge sessions from the same pack substrate.
- **WRAP-02**: Host can run team-based variants on top of the same room and scoring contracts.

### Expanded Mode Families

- **MODE-01**: Product includes at least one adjacent non-anchor F1 mode using the shared content substrate.
- **MODE-02**: Product supports themed expert packs by era, rules context, or race-weekend texture beyond the initial anchor set.

### Retention And Public Features

- **RET-01**: Product supports a daily or recurring challenge format.
- **RET-02**: Product supports lightweight player identity and session history without requiring a heavy public-account posture.
- **RET-03**: Player can review their own round-by-round history and accuracy trends across sessions.
- **RET-04**: Session results remain browsable after play as a replay or structured review surface.

### Content Operations

- **OPS-V2-01**: Author can preview a round in isolation before adding it to a pack.
- **OPS-V2-02**: Author can import, validate, or revise a pack through a more ergonomic interface than raw CLI-only workflows.
- **OPS-V2-03**: Pack can be exported or shared as a stable artifact that another trusted instance can import.

### Distribution And Access

- **DIST-01**: Product can run from a private remote host and accept trusted browser guests over standard HTTPS and WebSocket ingress without requiring guest-side networking tools.
- **DIST-02**: Product can run in an always-on private-host mode where trusted users can start or join sessions without the creator being physically present.

### Content Scaling

- **CONTENT-01**: Content pool supports pack generation or curation from tagged round pools.
- **CONTENT-02**: Round-level calibration data is visible enough to influence curation, balancing, and pack construction.

## Protected Seams And Explicit Deferrals

These are planning-reference anchors, not additional ship-gates. They exist so future-aware seams and deliberate deferrals can be cited directly in roadmap entries, context files, plans, and later reviews.

Where these seams or deferrals are justified mainly by non-foreclosure rather than immediate Milestone 1 scope, they should be read together with `.planning/LONG-ARC.md`. That doctrine explains why the seam is being preserved without implying that the later wrapper, visibility state, or durability layer is already committed product scope.

### Protected Seams

- **SEAM-01**: The authored round model should preserve explicit `venue -> circuit -> section -> corner` relationships rather than collapsing the answer contract to coordinates only or flat labels only.
- **SEAM-02**: Judging, reveal, and scoring contracts should remain separable from room transport and UI surfaces.
- **SEAM-03**: Room authority, active-session ownership, and progression control should remain separable from host-screen and phone-controller presentation, and from any single presenting browser.
- **SEAM-04**: The authored content substrate should stay reusable across private-room play and plausible later wrapper surfaces such as async challenges, solo practice, or adjacent expert-facing modes.
- **SEAM-05**: Wrapper access policy and visibility state should remain separable from the shared content and session substrate so private rooms, unlisted challenges, and later spectator/public read surfaces do not require a second product core.
- **SEAM-06**: `event_container`, `room`, and `active game/session instance` should remain logically separable even when Milestone 1 often renders them 1:1 in the visible UI.
- **SEAM-07**: Visibility publication and staged reveal should remain separable from any one shared participant surface so host-screen plus private devices, same-house-separated play, and bounded audience shells do not require a second product core.
- **SEAM-08**: Presence identity, persistent identity, room/group memory, event memory, and content calibration history should not collapse into one flat profile or one undifferentiated results ledger.

### Explicit Deferrals

- **DEF-01**: Visibility decisions stronger than private rooms or share-by-link flows remain deferred until the private social loop proves itself.
- **DEF-02**: Public participant trust, moderation, and service-obligation surfaces remain deferred.
- **DEF-03**: Paid guaranteed access, public uptime promises, or commercialization hardening remain deferred.
- **DEF-04**: Adjacent non-anchor F1 party modes remain deferred until the anchor geography-and-circuit loop is proven.
- **DEF-05**: Public room discovery, stranger participation, and open creator publishing remain deferred until the project intentionally accepts their moderation and trust obligations.
- **DEF-06**: Exact higher-tempo transport, prediction, rollback, or action-mode authority profiles remain deferred until a future mode family actually earns them.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Public matchmaking and ranked ladders | Misaligned with private-only posture and expensive before the core room loop is proven |
| Broad public UGC publishing or pack marketplace | Curated authored quality matters more than scale at initialization |
| Unrestricted Street View free-roam as the default play mode | Weakens authored pacing, increases dependency risk, and can blur the circuit-focused fantasy |
| Progression economies, collection systems, or cosmetic unlock loops | Do not strengthen the core expert-fan social loop |
| Native mobile apps | Browser-first host and phone-controller play is sufficient for v1 |
| In-app voice or video chat | External voice or couch play already covers the social need with less complexity |
| Public-release legal or commercial hardening | This project is private-only for now |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| PACK-01 | Phase 3 | Pending |
| PACK-02 | Phase 1 | Pending |
| PACK-03 | Phase 1 | Pending |
| PACK-04 | Phase 1 | Pending |
| PACK-05 | Phase 6 | Pending |
| GAME-01 | Phase 2 | Pending |
| GAME-02 | Phase 2 | Pending |
| GAME-03 | Phase 2 | Pending |
| GAME-04 | Phase 3 | Pending |
| GAME-05 | Phase 2 | Pending |
| ROOM-01 | Phase 3 | Pending |
| ROOM-02 | Phase 4 | Pending |
| ROOM-03 | Phase 3 | Pending |
| ROOM-04 | Phase 7 | Pending |
| ROOM-05 | Phase 5 | Pending |
| UX-01 | Phase 5 | Pending |
| UX-02 | Phase 4 | Pending |
| UX-03 | Phase 4 | Pending |
| UX-04 | Phase 5 | Pending |
| DEPLOY-01 | Phase 3 | Pending |
| DEPLOY-02 | Phase 4 | Pending |
| DEPLOY-03 | Phase 5 | Pending |
| DEPLOY-04 | Phase 3 | Pending |
| DEPLOY-05 | Phase 3 | Pending |
| OPS-01 | Phase 1 | Pending |
| OPS-02 | Phase 6 | Pending |
| OPS-03 | Phase 2 | Pending |

**Coverage:**
- v1 requirements: 27 total
- Mapped to phases: 27
- Unmapped: 0

---
*Requirements defined: 2026-04-08*
*Last updated: 2026-04-13 after Round 2B canon patch*
