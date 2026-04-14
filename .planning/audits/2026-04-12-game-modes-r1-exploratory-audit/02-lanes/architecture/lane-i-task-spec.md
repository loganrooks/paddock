---
date: 2026-04-13
lane: i
lane_name: "Large-room / high-player-count research lane"
orientation: exploratory
delegation_class: initial-architecture-research-planning
task_variants:
  - 02-lanes/architecture/lane-i-output.md
tags:
  - exploratory-audit
  - round-1-supplement
  - lane-i
  - architecture
  - scaling
  - player-count
  - research
---

# Lane I Task Spec

## What this lane is

This is a separate research lane on large-room and high-player-count possibilities.

It is deliberately separate from the broader architecture-exposure audit.

Its job is not:

- to re-audit the whole game portfolio
- to assume every future game should support `50+` players
- to prescribe a final backend architecture

Its job is:

- to study reference designs that support larger room sizes or higher player counts
- to distinguish different scaling patterns rather than reducing them to one number
- to extract early architectural implications that matter if this project ever wants some modes in the `20-50` or `50+` range

## Why this is separate

The creator explicitly distinguished:

- a general audit of promising game ideas and their architectural implications
- a separate question about larger-room / higher-player-count possibilities

Do not blur those.

This lane should answer:

- what kinds of game structures scale to larger rooms?
- what kinds do not?
- what reference designs or case studies are relevant?
- what early separations or abstractions would keep those options open later?

## Root contract

This lane sits under:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md`

It also carries forward:

- `AGENTS.md`
- `.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/round-1-self-eval.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2-prompts.md`

## Creator steering

Treat the following as direct constraints:

- this is a lane task, not an inline main-thread research dump
- it may be split across multiple agents and synthesized
- the point is to expose implications for early planning, not to force all modes toward massive rooms
- external research matters here; use official or primary sources where possible
- compare different scaling envelopes and interaction patterns, not just raw player-count headlines

## Research split

This lane is split into three sub-lanes:

1. `lane-i-a`
   High-fanout browser / party / audience / submit-and-aggregate patterns
2. `lane-i-b`
   Medium-to-large real-time action / collision / movement-heavy room patterns
3. `lane-i-c`
   Medium-scale hidden-info / social / private-room patterns and topology constraints

The main thread should synthesize those outputs into one final artifact.

## Required lenses

### 1. Scaling pattern, not just player count

Separate at minimum:

- submit-and-aggregate
- hot-seat plus audience
- hidden-info private-room sync
- real-time action / collision / racing
- phased / bracket / heats / tournament composition

### 2. Room-type implications

Ask:

- what kinds of rooms are these games actually supporting?
- one shared room, many small rooms, audience plus players, teams plus spectators, or server-sharded instances?
- what does "50+" actually mean in each case?

### 3. Architectural implications

Ask:

- where does authority live?
- where is state shared versus private?
- how much latency sensitivity exists?
- how much per-player fanout exists?
- what presentation topology is assumed?

### 4. Relevance to this project

Do not just describe the reference designs.

Translate them back into questions like:

- could future F1 modes plausibly live in this scaling pattern?
- if yes, what early substrate choice might matter?
- if no, why not?

## Output target

Final synthesis target:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md`

Sub-lane outputs:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-a-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-b-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-c-output.md`

## Output requirements for the final synthesis

The final synthesis should contain:

1. `Lane framing`
2. `Why large-room research is a separate question`
3. `Reference patterns by scaling shape`
4. `What kinds of future F1 modes might plausibly live in each pattern`
5. `What does not plausibly scale and should not be forced`
6. `Most important early architectural implications`
7. `Cheap early protections vs premature overengineering`
8. `What should feed later architecture deliberation`

## Quality bar

Good output for this lane should:

- use real reference designs rather than pure speculation
- separate scaling patterns clearly
- avoid fake universal player-count targets
- connect findings back to this project's possible futures
- stay useful for early planning without pretending to solve final architecture
