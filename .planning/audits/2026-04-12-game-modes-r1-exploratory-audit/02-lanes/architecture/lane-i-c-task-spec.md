---
date: 2026-04-13
lane: i-c
lane_name: "Hidden-info / private-room topology research"
orientation: exploratory
delegation_class: initial-architecture-research-planning
task_variants:
  - 02-lanes/architecture/lane-i-c-output.md
tags:
  - exploratory-audit
  - lane-i
  - hidden-info
  - topology
  - scaling
  - research
---

# Lane I-C Task Spec

## Focus

Research reference designs for:

- hidden-information multiplayer games
- medium-scale social / deception / role-asymmetry rooms
- private-room and same-house / remote hybrid topologies
- systems where room topology matters more than raw player count

This lane should use official or primary sources where possible.

## What to study

Prefer cases that help distinguish:

- per-role private information
- spectators vs active participants
- voice-chat/social dependency
- private-room caps and why those caps exist
- designs where "more players" changes legibility or moderation more than transport cost

Representative case types may include:

- social deduction
- asymmetric comms
- same-house but split-information local play
- private-room sync games

## Questions

- What tends to cap these rooms before raw network scale does?
- How much of the constraint is social readability, moderation, or hidden-info management rather than transport?
- What topologies recur:
  private lobby, separate screens, voice-layered play, audience-plus-core, hybrid local/remote?
- Which future F1 modes could plausibly want this pattern?
- What early substrate decisions matter if some future modes live here while others live in higher-fanout patterns?

## Output target

Write to:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-c-output.md`

## Required output sections

1. `Lane framing`
2. `Reference cases`
3. `Why these rooms cap where they do`
4. `Topology and hidden-info implications`
5. `Relevance to possible F1 modes`
6. `Early architectural implications`
7. `Uncertainties and limits`
