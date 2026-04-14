---
date: 2026-04-13
lane: i-b
lane_name: "Real-time action / collision room research"
orientation: exploratory
delegation_class: initial-architecture-research-planning
task_variants:
  - 02-lanes/architecture/lane-i-b-output.md
tags:
  - exploratory-audit
  - lane-i
  - action
  - racing
  - scaling
  - research
---

# Lane I-B Task Spec

## Focus

Research reference designs for:

- medium-to-large real-time action rooms
- movement / collision / racing / chase patterns
- games where many simultaneous active players materially change latency and authority demands

This lane should use official or primary sources where possible.

## What to study

Prefer cases that help distinguish:

- smaller private lobbies vs much larger active rooms
- party-race / obstacle / chase structures
- action-heavy games with different server-authority assumptions
- games where the room size is achieved by sharding, heats, or looser interaction zones

Representative case types may include:

- large multiplayer action / battle / race formats
- party-race / elimination formats
- real-time chase or vehicle-heavy rooms

Do not assume this project's future modes need those exact scales; study them as pressure examples.

## Questions

- What kinds of action patterns scale cleanly, and which do not?
- How do these games manage authority, collision, or movement consistency?
- Where do they rely on sharding, elimination, heats, or instancing instead of one fully shared room?
- What does “50+” actually mean in these designs?
- Which future F1 modes might plausibly want this pattern?
- Which ones probably should not be pushed here?
- What early architectural implications follow if even one future mode wants this class?

## Output target

Write to:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-b-output.md`

## Required output sections

1. `Lane framing`
2. `Reference cases`
3. `What scales and what breaks first`
4. `How these designs avoid one giant fully-shared problem`
5. `Relevance to possible F1 modes`
6. `Early architectural implications`
7. `Uncertainties and limits`
