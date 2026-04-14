---
date: 2026-04-13
lane: j-f
lane_name: "Real-time sync / authority follow-up"
orientation: exploratory
delegation_class: replanning-revision-gap-filling
task_variants:
  - 02-lanes/architecture/lane-j-f-output.md
tags:
  - exploratory-audit
  - lane-j
  - follow-up
  - realtime
  - authority
  - prediction
  - engineering-exposure
---

# Lane J-F Task Spec

## Why this follow-up exists

The first-pass real-time lane surfaced useful room-shape and orchestration patterns, but it did not go deep enough into the concrete engineering of:

- server authority
- prediction
- rollback or resimulation
- relevancy/filtering
- state synchronization tradeoffs

This follow-up is for the actual technical mechanics.

## Focus

Research concrete real-time synchronization and authority mechanisms from high-quality sources.

Prioritize:

- official engineering blogs
- official engine docs
- official technical talks / slide decks
- classic but credible technical references when direct official product material is thin

## Candidate source territory

Likely relevant sources include, but are not limited to:

- Unreal replication / Iris / relevancy / prioritization docs
- Riot VALORANT netcode article
- Overwatch networking talks/slides
- GGPO official material
- Gaffer on Games networking models
- other strong real-time synchronization references if they expose mechanics clearly

Do not turn this into a general shooter-history survey. Stay on the concrete mechanisms.

## Questions

- What exact authority model or synchronization model is exposed?
- What concrete technical problems is it solving?
- What mechanisms are described:
  prediction, rollback, delta serialization, filtering, prioritization, dormancy, interest management, etc.?
- What tradeoffs are acknowledged?
- Which claims are direct versus inferred?
- Which aspects are actually relevant to plausible Prix Guesser action modes, and which are likely overkill?

## Output target

Write to:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-f-output.md`

## Required sections

1. `Lane framing`
2. `Reference cases and source audit`
3. `Concrete synchronization / authority mechanisms exposed`
4. `Concrete tradeoffs and limits`
5. `What seems relevant to Prix Guesser`
6. `What remains uncertain`
