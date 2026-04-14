---
date: 2026-04-13
lane: i-a
lane_name: "High-fanout browser / audience pattern research"
orientation: exploratory
delegation_class: initial-architecture-research-planning
task_variants:
  - 02-lanes/architecture/lane-i-a-output.md
tags:
  - exploratory-audit
  - lane-i
  - browser
  - audience
  - scaling
  - research
---

# Lane I-A Task Spec

## Focus

Research reference designs for:

- browser-first party games
- host-screen plus phone-controller patterns
- audience / submit-and-aggregate / high-fanout participation
- large private rooms or event-like participation

This lane should look for relevant official or primary sources where possible.

## What to study

Prefer cases that help distinguish:

- active players vs audience
- synchronous submission vs real-time action
- private rooms vs public participation
- browser/mobile device assumptions

Representative case types may include:

- party-room games
- browser quiz / prediction / crowd-vote systems
- geography or guessing games with room play
- audience-participation formats

Do not overfit to any one brand if better representative cases emerge.

## Questions

- What player counts are actually supported, and in what form?
- How do these systems handle audience vs core-player distinction?
- What latency demands do they appear to have?
- What topology do they assume:
  host screen, per-player screens, browser rooms, stream plus audience, or something else?
- What parts of those patterns might matter for this project?
- Which future F1 modes could plausibly use this pattern?
- What early substrate separations would preserve that option?

## Output target

Write to:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-a-output.md`

## Required output sections

1. `Lane framing`
2. `Reference cases`
3. `What scales well in this pattern`
4. `What the counts actually mean`
5. `Relevance to possible F1 modes`
6. `Early architectural implications`
7. `Uncertainties and limits`
