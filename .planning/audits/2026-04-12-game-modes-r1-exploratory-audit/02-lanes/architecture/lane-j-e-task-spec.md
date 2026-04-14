---
date: 2026-04-13
lane: j-e
lane_name: "Browser authoritative room/state follow-up"
orientation: exploratory
delegation_class: replanning-revision-gap-filling
task_variants:
  - 02-lanes/architecture/lane-j-e-output.md
tags:
  - exploratory-audit
  - lane-j
  - follow-up
  - browser
  - authoritative-state
  - visibility
  - engineering-exposure
---

# Lane J-E Task Spec

## Why this follow-up exists

The first-pass browser/audience lane found useful topology evidence, but comparatively weak direct engineering exposure outside Jackbox.

The source-hunt identified a more promising cluster for a second pass:

- authoritative room/state frameworks
- per-client visibility/state-view mechanisms
- browser-first session orchestration patterns

This follow-up is meant to deepen that weak spot before synthesis.

## Focus

Research browser-first room/state engineering references that expose concrete mechanisms around:

- authoritative room state
- room lifecycle and match-making
- seat reservation / joins
- per-client state filtering or visibility views
- turn/phases/logs where relevant
- optional comms/middleware if directly relevant

Prioritize direct engineering exposure over ecosystem marketing.

## Candidate source territory

Likely relevant sources include, but are not limited to:

- Colyseus room/state/view/matchmaker docs
- boardgame.io docs or engineering material
- PlayFab Party docs where they expose concrete comms/session mechanisms
- other browser-first authoritative room/state sources if they expose more concrete engineering than the above

Do not turn this into an engine-choice comparison.

## Evidence rules

- follow the lane-j evidence hierarchy
- keep fact separate from inference
- explicitly note what is framework capability versus proven product pattern
- prioritize concrete exposed mechanisms over "this framework can do X" marketing

## Questions

- What concrete room/session mechanisms are exposed?
- How do these systems treat authoritative state and mutation rights?
- How do they handle joins, room discovery, seat reservation, or matchmaking?
- What concrete mechanisms exist for per-client visibility or filtered state views?
- What, if anything, do they expose about logs, phases, turn structure, or event sourcing?
- Which aspects look most relevant to Prix Guesser's likely browser-first futures?
- What remains uncertain even after this follow-up?

## Output target

Write to:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-e-output.md`

## Required sections

1. `Lane framing`
2. `Reference cases and source audit`
3. `Concrete engineering mechanisms exposed`
4. `Concrete tradeoffs and limits`
5. `What seems relevant to Prix Guesser`
6. `What remains uncertain`
