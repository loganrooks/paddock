---
date: 2026-04-13
lane: h
lane_name: "Architecture-pressure lane"
orientation: exploratory
delegation_class: initial-architecture-research-planning
task_variants:
  - 02-lanes/ideation/lane-h-output.md
tags:
  - exploratory-audit
  - round-1-supplement
  - lane-h
  - architecture
  - scaling
  - player-count
  - room-model
---

# Lane H Task Spec

## What this lane is

This is a dedicated architectural run to surface early technical and structural considerations that could materially affect planning.

It exists because some product questions are no longer merely "later implementation details." In particular:

- different games want radically different room/session shapes
- hidden information and authority splits change display and join assumptions
- some possible futures may want 50+ players or otherwise unusual scale
- these pressures can quietly foreclose options if ignored too long

This lane is not meant to collapse product exploration into feasibility triage. It is meant to expose:

- what early architectural choices are load-bearing
- what needs to stay open
- what game shapes most strongly pressure those decisions

## Why this should happen now

The project has repeatedly surfaced architectural stressors:

- host-screen + phones
- private online sync
- hybrid play
- hidden information
- spectator roles
- real-time racing
- large-player possibilities
- community / ranked / team futures

The architecture notes already flag several of these, but this lane should connect them back to the evolving game portfolio and ask:

- which possible games actually pressure early planning?
- which pressures are real versus speculative noise?
- where does 50+ player potential materially change what we should preserve architecturally?

## Root contract

This lane sits under:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md`

It should carry forward:

- design terrain rather than fixed pitch
- context plurality
- the warning against premature collapse into one display model
- the importance of authored round/content model and room authority model

from:
- `AGENTS.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md`
- `.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/round-1-self-eval.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2-prompts.md`

## Source read set

Required:
- `AGENTS.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md`
- `.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/round-1-self-eval.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2-prompts.md`

Conditional:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/ideation/lane-g-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/ideation/lane-g2-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/ideation/lane-f2-output.md`

Use those only when a specific game shape from those lanes materially pressures architecture.

## Creator steering

Use these as direct constraints:

- large-player possibilities (50+) should be treated as a serious pressure example, not a novelty mention
- the lane should ask which game types actually want many more players and why
- the output should surface architectural considerations that affect early planning and decision making
- architecture should be discussed in relation to game shapes, not in isolation
- do not assume all future games fit small private rooms
- do not assume all future games want large public lobbies either
- identify where early decisions should remain deliberately open rather than prematurely fixed

## Anti-goals

Do NOT:

- reduce this to a pure feasibility report
- assume every possible game must support 50+ players
- treat architecture as generic web-app scaling rather than game-shape-sensitive
- prescribe a full final architecture stack
- ignore the difference between:
  network scale,
  room/session scale,
  reveal UX scale,
  spectator scale,
  and social-legibility scale

## Required lenses

### 1. Player-count classes

Analyze at least these broad classes:

- `2-8`
- `8-20`
- `20-50`
- `50+`

For each, ask:

- what kinds of game structures fit naturally?
- what breaks first:
  networking, reveal UX, social readability, collision complexity, moderation, or room authority?
- which current or plausible future modes belong here?

### 2. Room / session / authority model

Ask:

- what assumptions about rooms, hosts, player identity, spectators, and active mode count get pressured by larger or stranger game types?
- what should remain flexible early?
- where does hidden info or asymmetric authority force different session abstractions?

### 3. Display / information model

Ask:

- which futures depend on host-screen + phones?
- which depend on per-player private screens?
- which need unusual local separation?
- what cannot be made impossible early without regret later?

### 4. Scaling by interaction pattern

Separate:

- parallel submit-and-aggregate games
- real-time collision / racing games
- asymmetric hot-seat + support games
- spectator-heavy or audience-mediated games
- tournament / heat / bracket / phased-reveal games

The scaling ceiling is not one number across all of these.

### 5. Foreclosure risk

For each major architectural pressure, ask:

- what early shortcut would quietly foreclose this later?
- what cheap early separation or abstraction might preserve the option?
- what would be genuine overengineering right now?

### 6. Early-planning implications

Make the final output actionable for early planning:

- what needs to be discussed before Phase 01 / near-term planning hardens?
- what can stay explicitly open?
- what should be documented as architectural watchpoints?

## Output target

Write to:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/ideation/lane-h-output.md`

## Output requirements

Your output must contain these sections:

1. `Lane framing`
2. `Why architecture needs to come forward here`
3. `Player-count classes and what fits them`
4. `Current and plausible future game shapes that pressure scale`
5. `Room / session / authority implications`
6. `Display / hidden-info / input implications`
7. `Networking / simulation / transport implications`
8. `Reveal UX / aggregation / spectator implications`
9. `Foreclosure risks and cheap early protections`
10. `Most important implications for early planning`
11. `What should feed into Round 2 and later architecture deliberation`

## Quality bar

Good output for this lane should:

- connect architecture to game shapes rather than speaking in generic systems language
- take 50+ player possibilities seriously without forcing them onto every mode
- distinguish different kinds of scale clearly
- surface a few early decisions that genuinely matter
- avoid fake certainty about final architecture while still being useful
