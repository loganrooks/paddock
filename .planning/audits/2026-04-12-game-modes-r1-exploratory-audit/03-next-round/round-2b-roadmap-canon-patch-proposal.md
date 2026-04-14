---
date: 2026-04-13
audit_subject: artifact_analysis
audit_orientation: standard
audit_delegation: self
scope: "Execution-ready patch proposal for ROADMAP.md and canon docs after Round 2B foreclosure synthesis"
triggered_by: "manual: follow-on from Round 2B closure"
tags:
  - exploratory-audit
  - round-2b
  - patch-proposal
  - roadmap
  - canon-docs
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-foreclosure-synthesis-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-sensitivity-map-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-c-phase-01-ledger-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/01-CONTEXT.md
---

# Round 2B Roadmap And Canon Patch Proposal

## Proposal summary

This proposal does **not** recommend:

- a new milestone phase
- roadmap reordering
- widening Phase 01 scope
- importing public-shell or higher-tempo implementation into Milestone 01

It **does** recommend a canon-doc patch set that makes the Round 2B non-foreclosure posture explicit and durable.

The stable conclusion from Round 2B is:

- there is no justified missing phase
- there is no justified phase reorder
- there **are** missing carry-forward constraints and vocabulary clarifications across the canon docs

The most important architectural shortcut to guard against remains:

- collapsing `event_container`, `room`, `game_instance`, and `recurrence unit` into one object

That shortcut is not just a Phase 03 problem. It quietly distorts topology, watchability, lifecycle, identity, recurrence, content history, and future bounded public shells across the whole Milestone 01 spine.

## Patch goals

The patch set should do five things:

1. make the `explicit now` seams from Round 2B visible in canon docs
2. add carry-forward constraints to the roadmap phases most likely to harden the wrong assumptions
3. strengthen seam language in requirements without turning those seams into new ship-gates
4. keep under-justified areas explicitly open
5. avoid creating the false impression that later wrappers are now active scope

## Governing patch posture

The patch must preserve these distinctions:

- `explicit now` means "name the seam now," not "implement the future now"
- `keep open` means do not silently close the question in canon wording
- `defer` means later-arc or later-milestone work should remain deferred even if the seam is preserved now

The patch should therefore **not**:

- invent final capability bundles
- choose a final durable noun for recurring group identity
- choose a final wrapper taxonomy for editorial/event surfaces
- formalize higher-tempo transport specifics
- sneak public-shell mechanics into current milestone scope

## Execution order

This patch set should be executed **sequentially**, not in parallel.

Reason:

- the same vocabulary has to stay aligned across `REQUIREMENTS.md`, `PROJECT.md`, `LONG-ARC.md`, `ROADMAP.md`, and `01-CONTEXT.md`
- `ROADMAP.md` should inherit seam anchors that are first stabilized in `REQUIREMENTS.md`
- `01-CONTEXT.md` should be updated last so its future-awareness language reflects the finalized canon vocabulary

Recommended order:

1. `.planning/REQUIREMENTS.md`
2. `.planning/PROJECT.md`
3. `.planning/LONG-ARC.md`
4. `.planning/ROADMAP.md`
5. `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
6. quick consistency pass across all five files

## File-by-file patch proposal

### 1. `.planning/REQUIREMENTS.md`

**Why patch this file**

This is the cleanest place to add planning-reference seam anchors without widening scope. Round 2B showed that the current seam set is directionally good but thinner than the current evidence warrants.

**Target section**

- `Protected Seams And Explicit Deferrals`

**Required patch operations**

1. Strengthen `SEAM-03` so it protects authority and active-instance ownership more explicitly.
2. Add a seam for `event_container` vs `room` vs `game_instance`.
3. Add a seam for visibility-scoped publication / staged reveal, not just wrapper visibility state in the abstract.
4. Add a seam for layered identity/history rather than one flat profile or results ledger.
5. Optionally add one new deferral clarifying that higher-tempo transport/authority profiles remain deferred.

**Recommended wording direction**

Revise:

- `SEAM-03`
  Current shape is too presentation-focused.
  Proposed direction:
  `Room authority, active-session ownership, and progression control should remain separable from host-screen and phone-controller presentation, and from any single presenting browser.`

Add:

- `SEAM-06`
  `Event container, room, and active game/session instance should remain logically separable even when Milestone 1 often renders them 1:1 in the visible UI.`

- `SEAM-07`
  `Visibility publication and staged reveal should remain separable from any one shared participant surface so host-screen + private devices, same-house-separated play, and bounded audience shells do not require a second product core.`

- `SEAM-08`
  `Presence identity, persistent identity, room/group memory, event memory, and content calibration history should not collapse into one flat profile or one undifferentiated results ledger.`

Optional add:

- `DEF-06`
  `Exact higher-tempo transport, prediction, rollback, or action-mode authority profiles remain deferred until a future mode family actually earns them.`

**Important constraint**

Do **not** convert these into new milestone ship-gates. They belong in `Protected Seams`, not the top-level milestone requirements list.

### 2. `.planning/PROJECT.md`

**Why patch this file**

This is the concise identity document. It already contains the right broad posture, but it currently under-specifies the distinctions Round 2B judged as load-bearing.

**Target sections**

- `Context`
- `Milestone Arc`
- `Future-Aware Posture`
- optionally `Key Decisions`
- optionally `Open Questions`

**Required patch operations**

1. Extend the current vocabulary block so the session structure is clearer.
2. Clarify that host-screen-friendly is a watchability posture, not a one-surface ontology.
3. Clarify that private-first is compatible with bounded public/spectator shells.
4. Add explicit mention that identity/history/cadence are layered concerns.
5. Keep wrapper taxonomy and capability bundles open.

**Recommended wording direction**

In the vocabulary block under `Context`, add concepts alongside the current:

- `event container`
  a higher-level social or programmed shell that may outlive one active game
- `room`
  the participant/trust shell
- `game instance`
  the active playable loop within a room

Also add one explicit sentence after the current host-screen-friendly bullets:

- host-screen-friendly should be read as a watchability and shared-legibility bias, not as a claim that every participant always shares one truth surface

In `Milestone 2` expected additions, broaden the persistence language slightly so it does not sound like one flat player-history layer:

- lightweight player identity and session history
- room/group memory and recurrence surfaces, if earned
- content/history and calibration reuse across wrappers

In `Future-Aware Posture`, add bullets like:

- preserve `presence identity` separately from later persistent identity
- preserve layered memory: player, room/group, event, and content history are not assumed to be one ledger
- preserve layered cadence: session pacing, editorial cadence, and later event rhythm should not be flattened into one model

**Optional but good**

Add one or two `Key Decisions` if you want the canon to state them plainly:

- preserve `event_container` / `room` / `game_instance` separation as doctrine
- treat host-screen-friendly as watchability posture rather than one-surface truth

Do **not** add too many. This file should stay compact.

### 3. `.planning/LONG-ARC.md`

**Why patch this file**

This is the best place to encode the doctrine that Round 2B found missing: room-shell vs active-instance separation, bounded public shells, and layered memory/cadence.

**Target sections**

- `Mature Product Hypothesis`
- `Transition Doctrine`
- `Protected Bets For This Milestone`
- possibly a new short doctrine section

**Recommended patch shape**

Add a new doctrine section after `Mature Product Hypothesis`:

- `Room, Wrapper, And Memory Layer Doctrine`

That section should explicitly say:

- `event container`, `room`, and `game instance` are not assumed to be the same thing
- host-screen watchability does not imply one permanent participant truth surface
- bounded public or spectator shells wrap private-first play rather than replace it
- memory is layered:
  - player memory
  - room/group memory
  - event memory
  - content calibration/history
- cadence is layered:
  - session pacing
  - editorial/content rhythm
  - later event cadence

**Secondary patch operations**

In `Transition Doctrine`, strengthen the idea that publicness is not the only layering problem:

- visibility, hosting, memory, and cadence should remain separate axes where practical

In `Protected Bets For This Milestone`, add or extend bullets so the doctrine explicitly protects:

- room shell vs active instance separation
- bounded audience/public shells
- layered memory and cadence

**Important constraint**

Do not make this section read like Milestone 2 or Milestone 3 scope import. It should stay doctrinal and protective, not feature-like.

### 4. `.planning/ROADMAP.md`

**Why patch this file**

This is where the Round 2B results most obviously matter. The roadmap does not need a new phase, but Phases 3 through 7 need stronger carry-forward notes so later planning cannot silently flatten the protected seams.

**Target sections**

- `Overview`
- `Open Decisions Still Visible`
- Phase 3 through Phase 7 entries

**Top-level roadmap changes**

Add one sentence to `Overview` making the milestone-level posture explicit:

- Milestone 01 should preserve separation between room shell, active game instance, visibility surface, and later recurrence layers even when the first playable wrapper renders them simply.

Add 2-3 bullets to `Open Decisions Still Visible`:

- the first useful capability/lifecycle bundle remains open
- the final durable noun for recurring group identity remains open
- exact higher-tempo transport/authority profiles remain deferred

**Per-phase carry-forward changes**

Phase 3:

- expand `Protects` so it explicitly covers:
  - room shell vs active game instance
  - authority portability
  - presence-vs-persistence identity seam
- expand `Does not decide yet` so it explicitly keeps open:
  - exact capability bundles
  - exact lifecycle primitive set

Phase 3.1:

- expand the goal or `Protects` so it explicitly says:
  - the interaction contract must allow multi-surface visibility and topology-sensitive reveal
  - host-screen watchability does not imply one universal truth surface

Phase 4:

- add a carry-forward note that this phase must distinguish:
  - join
  - rejoin
  - seat claim
  - later audience-only entry

Phase 5:

- add a carry-forward note that reveal/watchability must remain compatible with private-state modes and should not universalize one truth surface

Phase 6:

- add a carry-forward note that calibration and replay history must stay distinct from broader player, room/group, and event memory

Phase 7:

- expand the durability framing so reconnect is explicitly about:
  - lifecycle continuity
  - authority continuity
  - not only browser refresh state reload

**Important roadmap constraint**

Do **not** add a new inserted phase for any of this. The correct patch is stronger carry-forward language inside the existing phases.

### 5. `.planning/phases/01-authored-round-contract/01-CONTEXT.md`

**Why patch this file**

Round 2B explicitly said Phase 01 should stay narrow, but it still needs light future-awareness wording so it does not accidentally imply the wrong long-term nouns and surfaces.

**Target section**

- `future_awareness`

**Required patch operations**

Add protected-seam language covering:

- authored artifact vs later session snapshot vs later wrapper/context nouns
- reveal semantics that do not imply one universal viewer surface
- stable identifiers reusable across later session snapshots, wrapper reuse, and layered history

**Recommended wording direction**

Under `Protected Seams`, add or strengthen bullets like:

- preserve authored content identity separately from later session snapshots or wrapper/context records
- preserve reveal semantics without implying one permanent participant truth surface
- preserve stable identifiers so later snapshots, editorial/event wrappers, and layered history records can point at authored content without contract churn

Under `Explicit Non-Decisions`, consider one extra clarification:

- do not decide persistent identity, room/group memory, or event memory structures in Phase 01

This should be phrased as non-scope protection, not as a new feature omission section.

## What should remain explicitly open after the patch

These should stay open in canon wording even after the patch:

- first useful capability bundle
- exact lifecycle primitive set
- final group-identity noun
- final wrapper taxonomy
- final cadence taxonomy
- higher-tempo substrate specifics

If the patch accidentally hardens any of those, it has gone too far.

## Validation checklist

The patch is good if all of the following are true:

- no new roadmap phase is added
- no milestone reordering is introduced
- `ROADMAP.md` now makes the Phase 3–7 carry-forward constraints visible
- `REQUIREMENTS.md` gains seam anchors without creating new ship-gates
- `PROJECT.md` and `LONG-ARC.md` both clearly distinguish room shell, active instance, bounded public shells, and layered memory/cadence
- `01-CONTEXT.md` gains light protective notes without widening Phase 01 scope
- the docs do not pretend exact capability bundles, wrapper taxonomy, or higher-tempo specifics are decided

## Execution note

This proposal should be executed as a single canon-doc patch pass, followed by one short review pass checking:

- vocabulary consistency
- no accidental scope widening
- no hidden contradiction between `PROJECT.md`, `LONG-ARC.md`, and `ROADMAP.md`
- no roadmap wording that implies the exact implementation is already chosen

## Bottom line

The roadmap does **not** need a new phase.

The canon **does** need a stronger non-foreclosure layer. The best patch is:

- no new phase
- no reorder
- stronger seam anchors in `REQUIREMENTS.md`
- stronger doctrine in `PROJECT.md` and `LONG-ARC.md`
- stronger carry-forward notes in `ROADMAP.md`
- lighter Phase 01 future-awareness reinforcement in `01-CONTEXT.md`
