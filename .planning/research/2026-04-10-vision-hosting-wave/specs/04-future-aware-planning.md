# Charter 04: Future-Aware Planning And Workflow Design

Write output to:

`/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md`

## Task Type

Initial architecture research/planning.

## Scope

Investigate how Prix Guesser could encode future-orientation into roadmap, milestone, phase, context, and agent workflows without turning planning into speculative paralysis.

This is partly a local-artifact analysis lane and partly a workflow-design lane.

## Starting Context

Read these first:

- `/home/rookslog/workspace/projects/prix-guesser/AGENTS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/config.json`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/01-CONTEXT.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/.continue-here.md`
- `/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/explore.md`

## Research Instructions

The question here is not simply "add more planning."

The real question is:

- how can milestone and phase planning stay aware of longer-term trajectory
- without freezing open questions too early
- and without converting every near-term task into overengineered abstraction work

Investigate:

- what future-facing information each artifact should carry
- where the current docs already do this well
- where they currently lose the long arc
- what lightweight workflow modifications would preserve future-awareness
- what heavier process changes would likely create drag

Helpful prompts:

- Should each milestone have an explicit `future protected` section?
- Should each phase/context file state `what this phase must not foreclose`?
- Should roadmap entries include both immediate goal and later trajectories they are intended to preserve?
- What belongs in `AGENTS.md` versus workflow templates versus `CONTEXT.md`?
- What kinds of hooks or guards are useful, and what kinds are cargo-cult process?

## Output Emphasis

Include:

- `Current Strengths In The Existing Harness`
- `Current Blind Spots`
- `Low-Drag Improvements`
- `High-Drag Ideas That Are Probably Not Worth It Yet`
- `A Minimal Future-Aware Planning Schema`

You may propose concrete artifact-field patterns, but do not edit any workflow files yourself.

## Source Expectations

- Ground claims about the current harness in the actual local files.
- If you bring in external planning/process ideas, cite them and label them appropriately.
- Distinguish local observation from general workflow recommendation.

## Collaboration Constraints

You own only the output file listed above.
You are not alone in the codebase.
Do not modify or revert anyone else's files.
