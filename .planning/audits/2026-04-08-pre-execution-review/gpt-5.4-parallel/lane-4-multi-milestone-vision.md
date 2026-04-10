# Lane 4: Multi-Milestone Vision Audit

## Overall Read

The current project artifacts are pointed in the right direction. They correctly identify the authored round model and the room authority model as the two highest-leverage architecture choices, and they avoid the biggest early mistake: collapsing the product into a thin GeoGuessr clone.

The main strategic risk is not that v1 is over-engineered today. It is that several v2-critical seams are still implicit rather than explicit:

- whether answer targets are a flat enum or a composable hierarchy
- whether room logic is transport-specific or deployment-agnostic
- whether UI is a hardcoded anchor-mode flow or a reusable session shell
- whether content calibration is simple aggregate logging or a true round-improvement loop

If those seams are handled cheaply in v1, the current roadmap can support a strong 3-milestone arc without a rewrite. If they are handled narrowly, v2 will become a sequence of avoidable migrations.

## v1 Architecture Risk Assessment

### 1. Authored round model

Assessment: promising foundation, but under-specified for future mode families.

What works:
- Phase 1 already centers the right substrate: explicit answer target type, clue ladder, reveal explanation, scoring profile, validation, and media fallback.
- That is the right base for team play, async play, daily modes, and era-themed packs because those are mostly wrappers around shared authored content.
- The requirement that packs are curated fixed snapshots is especially important; it gives the project a compoundable content asset instead of ephemeral room state.

Risk:
- The docs do not yet make clear whether an answer target is a single flat value or a structured target with relationships.
- Future answer surfaces like `section`, `corner`, `approach context`, and `circuit + corner` will get awkward fast if Phase 1 bakes in a single-surface or string-alias model.
- Era-themed packs also need round metadata beyond current v1 wording: era tags, thematic tags, difficulty, media provenance, and possibly explainability flags.

Judgment:
- v1 is on the right track, but there is a high rewrite risk if Phase 1 uses a flat answer model instead of a hierarchical/composable one.

### 2. Judging and scoring

Assessment: conceptually right, but must become schema-driven rather than mode-specific.

What works:
- Phase 2 correctly isolates gameplay logic from room transport and UI.
- Explicit answer-surface judging plus partial credit is exactly the right long-term posture.

Risk:
- The roadmap language still reads like v1 judging may be implemented around `circuit` and `venue` first and generalized later.
- That is fine for content scope, but dangerous for engine scope.
- If judging logic becomes a pile of special cases for `circuit` and `venue`, future `section`, `corner`, and composite answers will likely force a rewrite.

Judgment:
- The engine should be generic now even if v1 only ships with simpler surfaces. This is a high-priority cheap decision.

### 3. Room architecture

Assessment: the roadmap is directionally correct, but the local-to-online transition is still the largest systems risk.

What works:
- Phase 3 defines the right core room responsibilities: canonical phase, timer, submissions, scores, and frozen session snapshots.
- That model can support local, online, and hybrid play if the room engine is authoritative and deployment-agnostic.

Risk:
- Phase 7 pushes reconnect and durability later. That is fine as a shipped capability, but dangerous if Phase 3 chooses a room runtime or state model that assumes a purely ephemeral local session.
- Online and hybrid play need stable player identity, resumable state, idempotent commands, and a clear room/session boundary even if v1 does not fully harden them yet.
- If UI components talk directly in runtime-specific socket messages instead of a typed room command/event contract, migration from local party play to private hosted play gets expensive.

Judgment:
- Moderate-to-high risk. The roadmap can support local to online to hybrid, but only if Phase 3 preserves transport and deployment boundaries from day one.

### 4. UI architecture

Assessment: current roadmap likely supports future modes only if Phase 4-5 are implemented as a reusable session shell.

What works:
- Splitting controller UI and host-screen flow is sensible for the product fantasy.
- The emphasis on answer-surface clarity, watchability, reveal, standings, and replay is aligned with both v1 fun and future expansion.

Risk:
- The docs do not yet require a generic round-rendering contract or answer-input abstraction.
- If the controller is built as a one-off `circuit/venue` form and the host screen is a one-off geography reveal loop, future modes will require a substantial UI rewrite.

Judgment:
- Medium risk in the documents, high risk in implementation if not called out explicitly.

### 5. Session data and content feedback loops

Assessment: Phase 6 is correct but currently too thin for long-term quality compounding.

What works:
- OPS-02 and Phase 6 correctly identify that round-level evidence must drive content revision.
- This is strategically important because curated content is the core asset.

Risk:
- "Per-round outcomes" may be interpreted too narrowly.
- Long-term content quality work needs more than final score totals. It needs enough structure to answer questions like:
- which clue step made the round solvable
- which accepted answers players tried but the system missed
- whether a fallback-media round underperformed for good reasons
- whether a round is fun in couch play but weak in async challenge format

Judgment:
- Medium risk today, but it becomes high later if Phase 6 records only coarse analytics.

## Recommended Cheap v1 Decisions That Protect v2+

### Critical

- Model answer targets as a structured hierarchy, not a flat enum plus aliases.
  - A round should be able to declare canonical targets and relationships such as `venue contains circuit`, `circuit contains section`, `section contains corner`, plus composite targets.
  - v1 can still ship only `circuit` and `venue`, but the schema should not assume those are the only meaningful surfaces.

- Make judging schema-driven.
  - The scoring engine should judge structured submissions against structured targets and specificity rules.
  - Partial credit should come from target relationships, not ad hoc mode logic.

- Freeze sessions as immutable compiled snapshots.
  - A room should point at a compiled pack/session snapshot with stable round IDs and content version identifiers.
  - This protects async challenges, daily modes, replays, and later content revisions.

- Keep the room engine independent from transport and UI.
  - Treat room actions as typed commands and room changes as typed events or state transitions.
  - The same room core should be usable in local-hosted, private-server, and hybrid deployments.

### High

- Give rounds and packs stable IDs, schema versions, and metadata from the start.
  - Include difficulty, theme, era, media strategy, and coverage class.
  - This is cheap now and expensive later.

- Record event-level session telemetry, then derive simple summaries from it.
  - Capture clue-step progression, submission timing, normalized answers, judge outcome, reveal timing, and round completion state.
  - A lightweight local event log is more future-proof than only storing aggregate scoreboard summaries.

- Build UI around a generic session shell.
  - Shared shells: lobby, active round, lock, reveal, standings, end-of-session.
  - Swappable widgets: answer input, clue presentation, reveal explanation, round summary.
  - This keeps future modes additive instead of requiring a UI rewrite.

- Choose database and tooling with a clean SQLite-to-Postgres path.
  - SQLite is appropriate for v1 portability and private use.
  - Use a migration/tooling layer that can move to Postgres later if the private hosted server becomes persistent and multi-session.

### Medium

- Prefer compiled content files over runtime-authored loose data.
  - Keep authored source human-editable, but compile into validated runtime artifacts.
  - This supports pack sharing, versioning, and future authoring tools.

- Keep API shape generic.
  - Avoid tying the app to framework-specific server actions or view-specific RPC names.
  - Prefer commands like `joinRoom`, `submitAnswer`, `advancePhase`, `startSession`, `resumePlayer`, and reads shaped around session/round state.

- Keep player identity lightweight but stable.
  - Guest-first is correct, but future async/history/team features need persistent player tokens or profile handles, even if that starts as low-friction local identity rather than full accounts.

### Low

- Reserve room in schemas for non-anchor mode families now, but do not implement them.
  - For example, allow round or pack metadata to declare `mode_family`, even if v1 only uses one value.

## 3-Milestone Arc Sketch

### Milestone 1: Prove the Anchor Social Loop

Purpose:
- make the core F1 geography/circuit party experience genuinely fun, legible, and replayable for friend groups

What belongs here:
- authored round contract
- generic judging engine with v1-limited surfaces
- authoritative room/session model
- guest join and mobile controller
- host screen and watchable reveal loop
- starter packs
- calibration telemetry
- practical reconnect for common interruptions

Success condition:
- a friend group can boot it up, cast it, join from phones, play a full session, understand the reveals, and want another pack

### Milestone 2: Expand the Same Substrate Into More Wrappers

Purpose:
- prove that the authored content substrate and room/session model can support more ways to play without forking the product

What should belong here:
- async challenge sessions
- daily/recurring challenge scheduling
- team play on the same judging/session substrate
- session history and replay review
- lightweight persistence/profile history
- internal content operations improvements: tagging, versioning, calibration views, and author preview tools
- stronger online/private-host deployment path

Success condition:
- the same core content can drive local game night, remote hosted sessions, and solo/async recurrence with minimal duplication

### Milestone 3: Broaden Into a Small F1 Party Platform

Purpose:
- add adjacent modes and stronger social recurrence only after the anchor mode and wrappers are proven

What should belong here:
- one or two adjacent F1 mode families using shared session shell and shared content identity
- themed seasons or era packs
- private pack sharing/import/export
- deeper statistics and pack performance views
- hybrid play refinements
- optional richer identity/history if the group actually uses it

Success condition:
- Prix Guesser feels like a compact F1 party-night platform rather than a single-mode prototype, without losing the geography anchor

## Are the Current v2 Requirements the Right Set?

Assessment: directionally right, but incomplete and too feature-list-shaped.

What is right:
- finer answer surfaces belong in v2 rather than v1
- async/solo wrappers and team play are the correct first expansion families
- themed packs and recurring challenges fit the product well

What is weak:
- v2 requirements focus on player-facing features but underweight content operations and architecture support
- `RET-02 account-backed history or profile persistence` is too heavy as written for a private-only project and slightly premature as a requirement
- the set does not distinguish "same substrate, new wrapper" from "new mode family" from "content pipeline maturity"

Better framing for v2:
- wrapper expansion
- content operations maturity
- lightweight persistence/history
- richer answer surfaces
- deployment durability for remote private play

## Missing Requirements or Phases

### Missing requirements

- Content versioning and stable IDs
  - Packs and rounds should be versioned so session results remain interpretable after content edits.

- Authoring workflow and preview tooling
  - Even if v1 authoring stays file-based, v2 needs requirements for previewing rounds, validating reveals, and checking difficulty before live play.

- Pack metadata and taxonomy
  - Era, theme, difficulty, media posture, and mode suitability should be queryable.

- Session replay or round review
  - Not necessarily full audiovisual replay, but enough state/history to review what happened and why a round landed badly or well.

- Private pack sharing/import-export
  - This is more aligned with the project's private-friend posture than public UGC publishing.

- Hybrid session support
  - The current docs mention couch, remote, and hybrid socially, but no v2 requirement explicitly protects that transition.

- Telemetry and content quality diagnostics
  - There should be requirements for clue-step performance, miss patterns, and difficulty calibration, not only generic "history."

- Seasonal or recurring content programming
  - Daily challenges are mentioned, but themed seasons or curated recurring rotations likely matter more for this audience than generic retention framing.

### Potential missing phases

- A content tooling and calibration phase
  - This should probably happen before major adjacent mode expansion.

- A session history/replay phase
  - Especially if the product is going to support daily or async formats.

- A deployment/durability phase for remote private hosting
  - Separate from basic reconnect. This is about hosted-room persistence, operational simplicity, and continuity across play nights.

## Biggest Risks to Project Success

### Fun risks

- The anchor mode is technically correct but not socially legible.
  - If the host screen and reveal flow are not watchable, the game may feel like parallel phone trivia instead of a party experience.

- Judging feels arbitrary.
  - Expert-fan audiences are tolerant of difficulty, not of scoring contracts that feel vague or unfair.

- The reveal layer is too thin.
  - If rounds end with "correct answer" rather than "why this was identifiable," the authored model loses its advantage.

- Too few standout rounds.
  - The first milestone lives or dies on content quality density, not breadth.

### Effort risks

- Authoring good rounds is more expensive than expected.
  - This is the most likely hidden production cost in the whole project.

- Media fallback and venue coverage management become manual pain.
  - If fallback-first venues are awkward to author and test, the content corpus will stall.

- Lack of preview and calibration tools makes iteration slow.
  - Without lightweight tooling, content improvements will depend too much on memory and manual inspection.

### Complexity risks

- The project over-rotates into online-system complexity before proving local fun.
  - This is the classic trap for a private social game.

- The implementation hardcodes the first mode's assumptions everywhere.
  - That turns Milestone 2 into a rewrite instead of an extension.

- v2 requirements drift toward public-product thinking.
  - Account systems, retention framing, and generic feature breadth can distort the private-friends use case.

## Concrete Recommendations With Priority

### Critical

1. Define answer targets as hierarchical and composable in Phase 1, even if v1 content only uses `circuit` and `venue`.
2. Treat the Phase 2 judge as a generic engine, not a v1-mode implementation.
3. Define the Phase 3 room core as a transport-agnostic authoritative state machine with immutable session snapshots.
4. Add stable IDs and content versioning to packs, rounds, and compiled session snapshots before execution proceeds.

### High

1. Expand Phase 6 expectations from coarse outcomes to event-level calibration data and answer miss diagnostics.
2. Make Phase 4-5 UI implementation explicitly session-shell-based with pluggable answer-input and reveal components.
3. Reframe v2 around wrapper expansion plus content-ops maturity, not only player-facing features.
4. Add explicit v2 requirements for authoring preview, pack taxonomy, private pack sharing/import-export, and session replay/review.
5. Keep the storage layer SQLite-friendly for v1 but choose tooling and schema discipline that can migrate to Postgres later without upheaval.

### Medium

1. Soften `RET-02` from full account-backed persistence to lightweight identity/history unless real usage proves stronger identity is necessary.
2. Add a future phase for remote-host durability and operational simplicity distinct from basic reconnect.
3. Add a future phase for content tooling and calibration dashboards before adjacent mode sprawl.

### Low

1. Reserve schema fields for `mode_family`, `theme`, and `era` now, but do not build mode-platform mechanics yet.
2. Keep adjacent non-geography modes explicitly gated on evidence that the anchor loop gets repeat voluntary use.

## Bottom Line

The current vision is fundamentally sound. It does not appear to be foreclosing the future on paper. The risk is that several of the most important cross-milestone abstractions are currently implied rather than mandated.

If v1 execution makes four cheap decisions correctly now, the roadmap can grow cleanly:

- hierarchical answer model
- generic judging engine
- deployment-agnostic room core
- versioned content and session snapshots

Those choices are enough to protect the likely Milestone 2 and 3 arc without over-engineering the first release.
