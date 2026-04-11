# Exploration Sessions

This directory holds long-running exploratory conversations that are not yet formal project decisions.

Each session gets its own dated subfolder so the project can preserve:

- conversation moves and pivots
- live tensions and unresolved gray areas
- in-flight research waves
- resumable checkpoints after context clearing or compaction

## Suggested Session Structure

Each session folder should usually contain:

- `SESSION.md` — living narrative log of the conversation and its moves
- `CHECKPOINT.md` — latest resumable handoff for the next session or context window
- `CHECKPOINTS/` — incremental checkpoints that summarize what changed since the previous checkpoint
- optional linked research, notes, or synthesis artifacts

## Usage Rule

These session files are exploratory memory, not ratified product truth.

Nothing in here should be treated as a committed project decision until it is later promoted into canonical artifacts such as:

- `PROJECT.md`
- `ROADMAP.md`
- `REQUIREMENTS.md`
- phase `CONTEXT.md`

## Continuity Pattern

Use all three layers together:

- `SESSION.md` for the full narrative of the exploration
- `CHECKPOINTS/*.md` for stepwise deltas and turning points
- `CHECKPOINT.md` for the latest "resume here" state

## Checkpoint Quality Bar

Exploration checkpoints should preserve the substance of the discussion, not merely the topic headings.

Good checkpoints capture:

- what framing or proposal was introduced
- what the user challenged, corrected, or pushed to expand
- how the shared understanding changed
- what alternatives remained alive at that moment
- what was still unresolved and why

Exploration checkpoints should usually avoid overemphasizing orchestration mechanics unless those mechanics materially affected the discussion itself.

Technical launch details, agent runtime caveats, and similar operational notes should usually live in linked orchestration artifacts, not dominate the conversational checkpoint.
