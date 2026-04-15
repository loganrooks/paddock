# Deferred Readiness Items

This file records real items discovered during readiness work that should not currently block the Phase 01 rerun unless later evidence reactivates them.

## Active Deferrals

| Item | Why deferred now | Reactivation trigger |
|---|---|---|
| `scraped-radio` branch/archive posture | Important for workspace hygiene but not currently the main rerun blocker | if branch posture keeps creating workflow ambiguity during Checkpoint 6 |
| extra external-comparative governance research beyond `08` | current external supplement is good enough for present repo-specific action | if later audit claims need stronger external justification than `08` provides |
| project-wide compact-prompt design | current readiness-specific compact prompt is enough for the immediate rerun-prep session, but the broader project prompt should be designed alongside stable governance, workflow, and harness surfaces | once Checkpoints 1-5 clarify the durable project control surfaces worth preserving across compaction |
| dedicated cross-model-audit skill creation | focused integration research concluded that the near-term gap is a repo-local non-phase external-reread protocol/template, not a dedicated skill; keep skill creation deferred unless cross-vendor rereads become routine across multiple non-phase artifact families and protocol discipline proves insufficient | if later workflow/harness follow-through shows protocol/template guidance is not enough and a stable repeated non-phase review surface has actually emerged |
| portable GSD reproducibility / provenance hardening beyond current live-checkout needs | Checkpoint 4 concluded these are real quality issues, but not all of them are automatically pre-rerun blockers in the current live checkout; keep them deferred unless Checkpoint 5 materially touches reinstall/materialization surfaces or later verification shows current live coherence is not enough | if Checkpoint 5 changes reinstall/materialization paths, or if Checkpoint 6 still depends on unresolved install/provenance truth |

## Rules

- Do not move genuinely blocking work into this file just to keep the active checkpoint moving.
- If a deferred item becomes a real blocker, move it back into `TASKS.md`, `STATUS.md`, and the relevant gate file in the same change.
