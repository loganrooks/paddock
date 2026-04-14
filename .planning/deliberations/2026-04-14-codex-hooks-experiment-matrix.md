# Codex Hooks Experiment Matrix

This matrix exists so the current and future hook pilots stay bounded, explainable, and reversible.

| Pilot | Event | Purpose | Preconditions | Success Criteria | Failure Modes | Rollback |
|---|---|---|---|---|---|---|
| Repo startup reminder | `SessionStart` | Remind the operator about repo posture, dirty-tree caution, `main` branch, and current planning boundary | Repo-local `.codex/hooks.json`; message kept short and deterministic | Reminder is useful, low-noise, and does not trigger avoidance behavior | Message fatigue, stale wording, or duplicate guidance vs docs | Remove the hook entry and keep the guidance in docs only |
| Destructive Bash tripwire | `PreToolUse` | Warn or block obviously destructive shell commands such as `git reset --hard` or recursive deletes in repo root | Narrow denylist; no broad shell policing | Prevents obvious foot-guns without blocking normal work | False positives, brittle command matching, false sense of safety | Remove the rule; keep policy in docs and human review |
| Prompt hygiene nudge | `UserPromptSubmit` | Optional reminder about branch discipline or active source-of-truth docs | Only if prompt hook behavior is confirmed stable in this runtime | Nudge helps without cluttering every turn | Constant annoyance, stale reminder text | Disable immediately |
| “One more pass” stop reminder | `Stop` | Remind operator to verify or summarize before ending | Only after the feature is stable and low-loop-risk | Catches genuinely missed verification steps | Auto-continue loops, end-of-turn weirdness, noisy prompts | Do not adopt unless later evidence is clearly positive |

## Boundary Rule

If a candidate hook cannot be explained in one sentence, it is probably too clever for the first pilot.

## Current Status

- `SessionStart` reminder: active
- `PreToolUse` destructive-Bash tripwire: active
- all other rows: still deferred
