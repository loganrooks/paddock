---
date: 2026-04-13
lane: j-a
lane_name: "Browser / audience systems engineering exposure"
orientation: exploratory
delegation_class: initial-architecture-research-planning
task_variants:
  - 02-lanes/architecture/lane-j-a-output.md
tags:
  - exploratory-audit
  - lane-j
  - browser
  - audience
  - host-screen
  - engineering-exposure
---

# Lane J-A Task Spec

## Focus

Research browser-first, audience-layer, and host-screen-plus-phones systems with emphasis on engineering exposure.

Prioritize:

- engineering blogs
- technical docs
- talks or postmortems
- official support/docs only as secondary evidence for actual limits/topology

## Reference territory

Possible ecosystems include, but are not limited to:

- Jackbox
- GeoGuessr party/live systems
- Kahoot
- Mentimeter
- Slido
- other browser party or event-participation systems if they expose engineering more concretely

## Questions

- What concrete technical problems are actually exposed?
- What room/session topology do these systems use?
- How do they separate active players, audience, moderators, and hosts?
- What do they reveal about joins, room codes, late join, rejoin, moderation, or sharding?
- What do they reveal about prompt scheduling, submission collection, reveal pipelines, or finalist/aggregation flows?
- What tradeoffs are visible?
- Which conclusions are direct versus inferred?

## Output target

Write to:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-a-output.md`

## Required sections

1. `Lane framing`
2. `Reference cases and source audit`
3. `Concrete engineering mechanisms exposed`
4. `Concrete tradeoffs and limits`
5. `What seems relevant to Prix Guesser`
6. `Uncertain but promising leads`
