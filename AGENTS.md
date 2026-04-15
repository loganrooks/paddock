# AGENTS.md

## Scope

This repository uses regular repo-local GSD for Codex, not GSD Reflect.

- Active local runtime: `.codex/get-shit-done`
- Local install command: `./scripts/setup-portable-gsd.sh`
- Do not use `~/.codex/get-shit-done-reflect` or Reflect-specific workflow/config paths for this repo.

For broader repo workflow, signoff rules, and artifact retention, also read:

- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
- [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)

If you are working anywhere under `.planning/`, also obey:

- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)

If `.planning/` does not exist yet, initialize from:

- `discovery/14-gsd-seed.md`

using:

```bash
$gsd-new-project --auto @discovery/14-gsd-seed.md
```

## Product Posture

- unofficial private-only F1 fan project
- geography/circuit guessing is the anchor mode
- likely social shape is private rooms, couch play, or host-screen plus phone controllers
- long-term expansion into adjacent F1 party modes remains open
- do not brand the product primarily with F1 marks without an explicit decision; public-facing surfaces should carry a non-affiliation disclaimer

## Runtime Rules

- Treat `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/LONG-ARC.md`, `.planning/STATE.md`, and active phase docs as the live operational state.
- Treat `discovery/` as upstream context, not as live implementation workflow state.
- Current boundary: Phase 01 is still at a pre-rerun boundary. Run a fresh discuss + planning pass before treating the existing `01-*` bundle as execution-approved.
- For non-phase-bound research or deliberation, prefer the repo-local `gsd-rigorous-research` skill over ad hoc structure.
- Treat `CONTEXT.md` as a steering brief: decisions, assumptions, open questions, canonical refs, code context, and future awareness all matter downstream.

## Quality Bar

- Do not optimize for `good enough`, `passes review`, or the smallest plausible response when the repo has already earned stronger doctrine, cleaner architecture, or better future guidance.
- When a pass produces substantive doctrine, architectural guidance, or future-seam clarification, do not collapse that work into a thin pass/fail summary if the canon, roadmap, or phase steering should be uplifted to reflect it.
- Always think across the repo's actual horizon stack:
  - the current phase or milestone execution surface
  - the next milestone carry-forward surface
  - the farther long-arc doctrine surface ratified in `.planning/LONG-ARC.md`
- Treat `Milestone 2` as the nearest carry-forward horizon, not the ceiling of future-aware thinking.
- Do not optimize only for Milestone 01 convenience if that creates avoidable ambiguity, doc drift, or re-litigation pressure in Milestone 02 and beyond.
- Assume all substantive work may later be audited by expert software engineers and strong external models. Write artifacts, plans, code, and rationale so they can withstand adversarial rereading without relying on hidden context, good intentions, or hand-wavy summaries.
- Do not take shortcuts by hiding uncertainty, compressing meaningful distinctions into umbrella terms, or calling something settled just because the current artifact can technically pass.

## Project-Specific Guidance

- The most important early architectural decisions are likely the authored round/content model and the room authority model.
- Do not collapse those into a premature frontend-framework choice.
- Preserve and express earned distinctions explicitly. Do not let repeated naming density, shorthand, or omission quietly choose winners between live branches.
- Be especially wary of umbrella terms such as `challenge`, `showcase`, `hosted`, `premium`, `membership`, `event`, `reviewed`, `curated`, and `unsupported`. If the distinction matters, spell it out.
- Distinguish `general architectural exposure` from `large-scale player-count / massive-room research`.
- Questions about `50+` or larger player support often require external comparative research on reference designs, case studies, and latency/topology tradeoffs, not just internal ideation.
- Before launching a mixed-scope architecture lane, discuss the split with the user first.
- Circuit-internal recognition is the primary fantasy; venue-approach clues are secondary and should not silently replace it.

## Delegation And Orchestration

- Codex GSD orchestration must happen at the top level. Do not create recursive GSD call graphs like `orchestrator -> generic agent -> gsd-plan-phase skill -> gsd-planner`.
- Prefer high-reasoning top-level orchestration with an explicit call graph before launching anything.
- Codex-native model policy for this repo:
  - top-level orchestration: prefer `gpt-5.4` with `xhigh`
  - execution and verification: prefer `gpt-5.4` with `high` unless a narrower task justifies less
  - early architecture-setting planning agents may use `gpt-5.4` with `xhigh`
- Before every agent spawn:
  - re-read this file
  - classify the task as one of:
    - `initial architecture research/planning`
    - `replanning/revision/gap-filling`
    - `execution/verification`
  - state the mapping in commentary as `agent -> model -> reasoning`
- Verify effective launch settings after every spawn against `~/.codex/state_5.sqlite`.
- If requested and effective settings differ, stop immediately, kill the agent, and report the mismatch plainly.

## Maintenance

- This file should stay narrow, stable, and agent-facing.
- Broader workflow, devops, signoff, and artifact-retention detail belongs in the governance docs above, not here.
- If a change would mainly affect work inside `.planning/`, prefer updating `.planning/AGENTS.md` instead of bloating this root file.
- If project posture, workflow policy, or source-of-truth references change, update this file in the same change rather than letting it drift.
