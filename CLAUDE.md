# CLAUDE.md

This is a thin cross-vendor wrapper, not a second canon surface.

For vendor-neutral repo doctrine, treat [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md) as the authoritative source. This wrapper only carries the Claude-side translation needed so cross-vendor Claude lanes do not have to infer repo rules from stale defaults.

## Read Order

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. If your work touches `.planning/`, also read [.planning/CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAUDE.md) and [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. For broader repo workflow and governance surfaces, use:
   - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
   - [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
   - [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)

## Claude-Specific Translation

- This repo uses repo-local regular GSD, not Reflect.
- Runtime truth lives in `.codex/get-shit-done` plus `./scripts/setup-portable-gsd.sh`.
- Live planning canon lives in `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/LONG-ARC.md`, `.planning/STATE.md`, and active phase docs.
- Phase 01 is still at a pre-rerun boundary; do not treat older `01-*` artifacts as execution-approved just because they exist.
- Use repo-local prompt/spec paths for headless Claude lanes. Do not rely on `/tmp` copies when the repo can carry the same artifact directly.
- The quality bar is anti-threshold. Do not let `adequate`, `sufficient`, `good enough`, `passes`, or similar language become the master frame when the real task is stronger carry, leverage, clarity, and long-horizon intervention yield.

## What Not To Mirror

Do not import these from `AGENTS.md` as if they applied unchanged under Claude:

- Codex-specific `spawn_agent` or sqlite launch-truth rules
- Codex model-selection policy
- any instruction that assumes Claude should treat `AGENTS.md` itself as unreadable or invisible

If a Claude lane needs launch-truth or wrapper discipline beyond this file, carry it explicitly in the lane packet, brief, or launcher rather than bloating this wrapper into a duplicate doctrine file.
