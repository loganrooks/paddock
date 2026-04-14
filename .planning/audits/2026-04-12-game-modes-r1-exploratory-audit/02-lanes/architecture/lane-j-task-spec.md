---
date: 2026-04-13
lane: j
lane_name: "Engineering-exposure research lane"
orientation: exploratory
delegation_class: initial-architecture-research-planning
task_variants:
  - 02-lanes/architecture/lane-j-output.md
tags:
  - exploratory-audit
  - round-1-supplement
  - lane-j
  - engineering-exposure
  - architecture
  - research
---

# Lane J Task Spec

## What this lane is

This is a dedicated engineering-exposure research lane.

It is not:

- a generic architecture memo
- a solution-first decomposition around the orchestrator's preferred abstractions
- a product-ideation lane

It is:

- a reference-design research lane focused on what relevant products and ecosystems actually expose about their engineering
- a source-traceable investigation into concrete problems, mechanisms, tradeoffs, and limits
- a way to surface promising technical precedents and open questions before later architecture deliberation

## Why this lane exists

The creator explicitly asked for:

- reference designs
- practical concrete solutions
- what they actually did
- engineering exposure in general, not just product help-page counts
- proper epistemic guardrails, research hygiene, source traceability, and source auditing

This lane should therefore prioritize evidence quality and traceability over fast synthesis.

## Evidence hierarchy

Use this evidence ladder explicitly:

1. official engineering blogs, technical docs, engine docs, technical postmortems
2. official talks, GDC/conf talks, team presentations, architecture notes
3. official product/support docs that expose topology, limits, moderation, or room shape
4. credible secondary technical analysis, clearly marked as secondary
5. promising but inaccessible or only partially accessible sources, logged for follow-up

Every important claim should be tied back to a source class.

## Research hygiene rules

- prefer primary sources whenever possible
- distinguish `published product limit` from `engineering mechanism`
- distinguish `source fact` from `researcher inference`
- do not oversell a conclusion when the evidence is thin
- log promising uncertain areas instead of laundering them into conclusions
- when a source is secondary, label it clearly
- if a claim appears to be widely repeated without a reliable source, mark it as unverified

## Source auditing rules

For each major reference case, capture:

- source type
- source reliability
- what the source actually exposes
- what it does not expose
- whether the key conclusions are direct or inferred

## Split strategy

This lane should be split broadly across multiple `high` agents first, then leave follow-up hooks for uncertain or promising areas.

Sub-lanes:

1. `lane-j-a`
   Browser / audience / host-screen systems engineering exposure
2. `lane-j-b`
   Real-time action / racing / large-room systems engineering exposure
3. `lane-j-c`
   Hidden-info / asymmetric comms / private-room systems engineering exposure
4. `lane-j-d`
   Source hunt for promising talks, books, papers, technical writeups, and partially inaccessible material

The main thread should synthesize the first-pass returns and identify:

- what is high-confidence
- what is promising but uncertain
- what deserves a second research wave

## Root contract

Carry forward:

- `AGENTS.md`
- `.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md`

But do not let the prior synthesis overdetermine this lane. The reference cases come first.

## Output targets

Sub-lane outputs:

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-a-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-b-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-c-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-d-output.md`

Final synthesis:

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-output.md`

## Required output sections for final synthesis

1. `Lane framing`
2. `Evidence quality and source audit summary`
3. `Concrete engineering patterns exposed by reference designs`
4. `Concrete problems and concrete mechanisms`
5. `What seems most relevant to Prix Guesser`
6. `What remains uncertain but promising`
7. `Candidate follow-up research questions`
8. `What should and should not influence early architecture decisions`

## Quality bar

Good output for this lane should:

- expose actual engineering choices where sources allow
- clearly separate fact from inference
- distinguish topology, authority, visibility, transport, moderation, and scaling mechanisms
- surface concrete reference mechanisms instead of generic advice
- identify good follow-up targets rather than pretending all open questions are settled
