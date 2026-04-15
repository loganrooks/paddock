---
date: 2026-04-14
audit_subject: sensitivity_docket
audit_orientation: exploratory
audit_delegation: direct
scope: "Map hosting-identity branches into the core planning docs without silently crowning first-party hosting as the winner"
triggered_by: "05-pre-sensitivity-challenge-converged-synthesis-output.md"
tags:
  - exploratory-audit
  - gap-closure
  - sensitivity
  - docket
  - hosting
  - provider-hosts
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-docket-c1-hosting-identity-branches-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-control-note.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-docket-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-pre-sensitivity-challenge-converged-synthesis-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-pre-sensitivity-challenge-c-hosting-branches-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-residual-gap-chunk-c-hosting-identity-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
---

# 05 Sensitivity Docket C1: Hosting Identity Branches

## Docket framing

- Mode: `feature-to-doc translation`
- Classification: `initial architecture research/planning`
- Governing question:
  how should the planning docs distinguish `trusted operators`, later `first-party hosted convenience`, later `provider / partner hosts`, and later `unpromoted private operators` without turning `first-party hosted convenience` into an already-chosen winner?
- Non-goals:
  - not choosing a final later hosting winner
  - not deciding collective / mirror governance posture here; that belongs to `C2`
  - not designing final host metadata schema, contracts, or SLA language
  - not turning later hosting identities into roadmap commitments

## Target feature pressure

- `trusted operators` first
- later identities that must stay distinct:
  - `first-party hosted convenience`
  - `provider / partner host`
  - `unpromoted private operator`

## Current gate classification

- `trusted operators` as the first hosting seam: `direct doctrine`
- `first-party hosted convenience` versus `provider / partner host`: `bounded-open`
- `unpromoted private operators` as a distinct later identity from both official and promoted-provider hosting: `direct doctrine about distinction`
- `first-party hosted convenience` as the chosen later winner: `reversal-sensitive`
- `hybrid official-plus-private hosting is naturally clean`: not closed here; hand off to `C2`

## Current survivor and strongest rival(s)

- The strongest survivor is still:
  `trusted operators` as the first transition seam after Logan-only hosting.
- The strongest later rivalry is now:
  `first-party hosted convenience` versus `provider / partner host`, not `first-party hosted convenience` versus `collectives` alone.
- `first-party hosted convenience` remains live and meaningful, but only as a weakened later branch:
  it survives as one possible accountable convenience surface, not as settled doctrine.
- `provider / partner host` is now the strongest under-compared rival:
  it preserves convenience without automatically making Prix the uptime/support operator.
- `unpromoted private operators` still matter as a separate identity:
  they are not the same thing as promoted providers, and they should not be silently treated as failed or obsolete just because later convenience branches remain open.

## Why this pressure matters

- The current canon already talks about `private hosted remote` play, `self-hostable authoritative rooms`, and later `modest hosted operation`.
  If that wording is read loosely, it can silently crown one later host identity without ever saying so.
- The challenge round materially changed the host-branch map:
  `provider / partner host` is now the main later rival to `first-party hosted convenience`.
- The surviving nuance is archetype-sensitive:
  remote recurring private play keeps `provider / partner host` highly live, while bounded showcase or event pressure could later strengthen `first-party hosted convenience`.
- `unpromoted private operators` are still important because the current product center is private-first and operator-led.
  If the docs collapse them into `providers`, they will understate support-owner and promotion differences.
- This docket is load-bearing for later sensitivity because the current docs use high-level hosting language.
  Sensitivity needs a map for when that abstraction is safe and when it quietly forecloses the missing-middle branch.

## Relevant planning surfaces

- [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
- [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
- [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
- [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)

## Per-doc implication map

### [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)

- Safe:
  the document may keep the product center at browser-first private play across local, LAN, and privately hosted remote sessions.
  It may also preserve later remote durability and coordination needs as a Milestone 2 concern.
- Overcommit risk:
  if Milestone 2 language about `private-host durability` or `more persistent remote access patterns` starts reading like an implied official Prix-operated service.
- Silent foreclosure risk:
  if the high-level identity language leaves room only for self-run private hosting now and official first-party hosting later, with no visible space for `provider / partner host` as a serious convenience branch.
- What must remain explicit here:
  this doc should stay high-level, but it must keep later remote-convenience identity unresolved.
  `provider / partner host` must remain compatible with the project story even if the document does not enumerate every later branch.

### [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)

- Safe:
  the document may preserve `self-hostable authoritative rooms` as the main durability seam and keep hosting, visibility, support, and service obligation as separate axes.
- Overcommit risk:
  the current `Hosting And Scaling Ladder` can be misread if `modest hosted operation` is treated as automatically meaning `first-party hosted convenience`.
- Silent foreclosure risk:
  if the ladder implies there is one clean later hosted step after private remote rooms, it will erase the newly important distinction between:
  - official first-party service
  - curated provider / partner hosts
  - continued unpromoted private operators
- What must remain explicit here:
  the later hosting question is about identity and support ownership, not just deployment topology.
  If later host modes become visible, host type, support owner, and compatibility expectations must stay legible.

### [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)

- Safe:
  the roadmap may keep Milestone 1 anchored on `operator-run local or privately hosted deployment`, browser-first guest parity, and repeatable private-room operator flow.
- Overcommit risk:
  if Phase 3 or later deploy language is read as a roadmap promise that Prix will itself become the canonical hosted service owner.
- Silent foreclosure risk:
  if the roadmap treats `private-host parity` and `hosted deployment` as though only creator-run boxes or later official hosting matter, leaving no seam for a provider / partner-host branch.
- What must remain explicit here:
  Milestone 1 is proving operator flow and authoritative-room parity, not choosing the later convenience-bearing host identity.
  Any future roadmap wording about easier remote coordination must stay capability-oriented rather than owner-model-specific.

### [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)

- Safe:
  the current `DEPLOY-*` and `DIST-*` requirements may stay host-identity-neutral.
  They correctly describe browser-first remote capability, HTTPS/WebSocket access, and always-on private-host operation without naming a winner.
- Overcommit risk:
  `DEPLOY-05` or future distribution requirements would become overcommitted if they started to imply an official Prix-run service, official account layer, or official uptime promise.
- Silent foreclosure risk:
  if future requirement additions talk only about `official hosted` convenience, or only about `private remote host`, without preserving `provider / partner host` as a distinct later possibility.
- What must remain explicit here:
  these are deployment-capability requirements, not later hosting-identity commitments.
  If a future hosted-convenience requirement is ever added, it must distinguish official hosting, promoted provider hosting, and unsupported private operators rather than using one flattened `hosted` label.

## What each doc may safely imply

- [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md) may safely imply that the product must work cleanly across local, LAN, and privately hosted remote play, and that later remote durability matters, without deciding who owns later convenience.
- [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md) may safely imply that self-hostable authoritative rooms are the primary seam and that a later convenience-bearing host surface may exist, as long as the owner model stays unresolved.
- [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md) may safely imply that Phase 3 must prove deployable private authoritative rooms and preserve private-host parity.
- [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md) may safely imply that remote browser access, always-on operation, and operator-startable deployment are desired capabilities independent of the final host identity branch.

## What each doc must not imply

- [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md) must not imply that later remote durability naturally equals a Prix-run hosted service.
- [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md) must not let `modest hosted operation` harden into shorthand for `official first-party hosting won`.
- [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md) must not treat Milestone 1 deployment work as a hidden commitment to official hosted convenience, provider-program rollout, or host-directory policy.
- [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md) must not treat `hosted` as if it already means `official Prix service`, and must not erase the difference between promoted provider hosting and unsupported private operators.

## What must remain explicit

- `trusted operators` is the first hosting seam.
- The later convenience-bearing choice remains open between `first-party hosted convenience` and `provider / partner host`.
- `unpromoted private operators` remain a distinct later identity from promoted providers and official service.
- If more than one host form becomes visible later, users will need explicit host-type and support-owner clarity.
- The current private-first center does not settle the later winner.
  It only says official first-party hosting is still live, provider / partner hosts are a serious rival, and unsupported private operators still matter.
- Showcase or event-shell pressure may later strengthen first-party hosting, but that is not current canon.

## Semantic drift watchpoints

- `hosted`:
  do not use it as if it automatically means `official first-party hosted service`.
- `private host`:
  do not use it as if it automatically covers both `trusted operator` and `provider / partner host`.
- `provider / partner host`:
  do not collapse it into either `collective / mirror` or `unpromoted private operator`.
- `operator`:
  do not blur `who runs the room` with `who owns support, compatibility, and service reputation`.
- `remote access` or `always-on`:
  do not treat these capability phrases as proof that official hosting has already won.
- `modest hosted operation`:
  treat this as an unresolved later host shape, not settled first-party doctrine.

## Sensitivity lane routing

- `Lane I: canon doctrine`
  consume this docket for [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md), [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md), and [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md) to protect:
  - `trusted operators` as direct doctrine
  - `first-party` versus `provider / partner` as bounded-open anti-hard-coding
  - `unpromoted private operators` as a distinct identity that must not disappear under generic `hosted` wording
- `Lane II: roadmap and rerun`
  consume this docket for [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md) and any carry-forward notes into rerun artifacts so deploy/operator language stays capability-oriented and does not choose an owner model by accident.
- `Lane III: preserve-only and reversal-sensitive futures`
  do not rely on this docket alone for `collective / mirror governance` or `hybrid official-plus-private is naturally clean`.
  Those belong to `C2`.

## What remains open after this docket

- whether `first-party hosted convenience` or `provider / partner host` becomes the stronger later branch once real remote-recurring pain is observed
- whether `provider / partner host` should later become explicit named canon vocabulary rather than an audit-only branch label
- what the minimum visible host metadata is if more than one host type becomes visible
- how `unpromoted private operators` can stay live without being mistaken for promoted providers
- whether later showcase or event-shell pressure materially shifts the later hosting ranking toward one official service surface
