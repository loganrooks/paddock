# Exploratory Research Wave: Vision, Hosting, And Future-Orientation

Date: 2026-04-10
Orchestrator: Codex
Status: in_progress

## Why This Wave Exists

The current discussion is not a narrow implementation question. It is an exploratory product-and-trajectory discussion about what Prix Guesser could become across multiple milestones, how that affects early technical and roadmap decisions, and how to keep the planning system future-aware without prematurely collapsing the option space.

This wave is intentionally exploratory-first. The goal is not to force a recommendation too early. The goal is to widen the solution space responsibly, expose assumptions, identify promising branches, and clarify what later decisions will actually matter.

## Research Posture

This wave is governed by four anti-foreclosure rules:

1. Do not answer a wider question with a prematurely narrow recommendation.
2. Distinguish observations from inferences from proposals.
3. Surface multiple viable trajectories where the evidence supports them.
4. Make uncertainty inspectable rather than hiding it behind confident prose.

## Required Epistemic Hygiene

Every research lane must:

- Prefer primary and official sources for technical and operational claims.
- Use secondary sources only when they add real value and are clearly labeled.
- Mark claims with one of:
  - `[CONFIRMED]` directly supported by cited sources
  - `[INFERRED]` reasoned synthesis from multiple cited facts
  - `[HYPOTHESIS]` plausible but not yet well-supported
- Include inline citations for substantive claims.
- Note source authority and any important reliability limits.
- Include at least one section titled `What Could Change This View`.
- Include at least one section titled `Disconfirming Or Tensioning Evidence`.
- Avoid source laundering. If a claim comes from a blog post, forum, or vendor marketing page, say so.

## Output Contract

Each lane writes exactly one findings file under `findings/`.

Each findings file must include:

1. `Question Space`
2. `Method And Sources`
3. `Findings`
4. `Viable Paths`
5. `Key Tradeoffs And Hidden Assumptions`
6. `Disconfirming Or Tensioning Evidence`
7. `What Could Change This View`
8. `Open Questions Worth A Second Pass`
9. `Source Ledger`

## Lane Map

1. `01-product-futures`
   Focus: end-state vision, mode ecology, watchability, and how different stages of the product relate.

2. `02-hosting-transition`
   Focus: web-first feasibility, local LAN play, self-hosting on personal hardware, hosted transition paths, capacity limits, queueing, and transparent growth models.

3. `03-precedents-and-trajectories`
   Focus: analog products, success stories, cautionary tales, transition patterns, and where Prix Guesser might innovate rather than imitate.

4. `04-future-aware-planning`
   Focus: how to encode future-orientation into roadmap, milestone, phase, context, and agent workflows without turning planning into speculative overreach.

## Launch Ledger

Requested launch settings for this wave:

- Agent type: `gsd-phase-researcher`
- Model: `gpt-5.4`
- Reasoning: `high`

Spawned lanes:

| Lane | Agent ID | Nickname | Spec | Output |
|---|---|---|---|---|
| 01 | `019d78cd-364c-73c1-b579-7ad7e51d9bdd` | `Descartes` | `specs/01-product-futures.md` | `findings/01-product-futures.md` |
| 02 | `019d78ce-5cf4-7dd1-a98f-917a76041d80` | `Russell` | `specs/02-hosting-transition.md` | `findings/02-hosting-transition.md` |
| 03 | `019d78ce-5d2a-7b03-bf32-7d0b39e417d3` | `Leibniz` | `specs/03-precedents-and-trajectories.md` | `findings/03-precedents-and-trajectories.md` |
| 04 | `019d78ce-5d73-7323-b4eb-953889da8449` | `Copernicus` | `specs/04-future-aware-planning.md` | `findings/04-future-aware-planning.md` |

Verification note:

- Requested launch settings are recorded in the Codex log stream.
- Mid-flight effective child-thread verification via `state_5.sqlite` is currently not surfacing live rows from this session through the available read-only methods.
- Because of that, the orchestrator must not overclaim that the effective reasoning setting has been confirmed from runtime state yet.

## Intended Use

This research wave is a decision-support input to the ongoing exploration discussion.

It is not a command to update `PROJECT.md`, `ROADMAP.md`, `REQUIREMENTS.md`, or any workflow file yet.

Any later changes should happen only after the user and orchestrator synthesize these findings together.
