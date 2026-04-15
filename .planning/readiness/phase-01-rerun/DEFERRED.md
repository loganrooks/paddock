# Deferred Readiness Items

This file records real items discovered during readiness work that should not currently block the Phase 01 rerun unless later evidence reactivates them.

## Active Deferrals

| Item | Why deferred now | Reactivation trigger |
|---|---|---|
| `scraped-radio` branch/archive posture | Important for workspace hygiene but not currently the main rerun blocker | if branch posture keeps creating workflow ambiguity during Checkpoint 4 |
| extra external-comparative governance research beyond `08` | current external supplement is good enough for present repo-specific action | if later audit claims need stronger external justification than `08` provides |
| project-wide compact-prompt design | current readiness-specific compact prompt is enough for the immediate rerun-prep session, but the broader project prompt should be designed alongside stable governance/harness surfaces | once governance normalization and harness follow-through clarify the durable project control surfaces worth preserving across compaction |
| dedicated cross-model-audit skill creation | existing surfaces like [gsd-review](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md) and [gsdr-audit](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md) already cover adjacent terrain; decide actual ownership first instead of adding another standing mechanism by reflex | once focused integration research shows the needed high-stakes review modes cannot be carried cleanly by existing workflow, orchestration, or skill surfaces |

## Rules

- Do not move genuinely blocking work into this file just to keep the active checkpoint moving.
- If a deferred item becomes a real blocker, move it back into `TASKS.md`, `STATUS.md`, and the relevant gate file in the same change.
