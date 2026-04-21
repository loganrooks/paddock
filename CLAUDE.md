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
- Do not smuggle threshold logic back in through deficit-oriented pseudo-positive phrasing like `not lacking`, `no longer missing`, or `not the real problem`; prefer direct positive formulations about where carry is already strong, where it thins, and where it can be intensified.
- In planning, discuss, research, and audit lanes, do not ask the leading question in yes/no threshold form when the stronger task is to map what the surface exposes, preserves, thins, intensifies, or leaves open.
- If a lane includes a real gate, keep that gate as one layer only; do not let it replace the stronger question of what more could be carried or opened.
- If a proposal direction is strong but the current packaging is weak, prefer narrowing, splitting, or staged carry over binary accept/reject.
- If a concern is mainly risk and the risk can be reduced through sequencing, tooling, checkpointing, or verification, prefer a mitigation path over a flat veto.
- Before narrowing to the top few options, ask whether the stronger first move is full-field mapping.
- When a lane changes a contract-carrying surface, treat propagation across adjacent producers, consumers, runtime carriers, and durable outputs as part of the work. Update or explicitly hold those neighbors rather than stopping at the local patch.

## What Not To Mirror

Do not import these from `AGENTS.md` as if they applied unchanged under Claude:

- Codex-specific `spawn_agent` or sqlite launch-truth rules
- Codex model-selection policy
- any instruction that assumes Claude should treat `AGENTS.md` itself as unreadable or invisible

If a Claude lane needs launch-truth or wrapper discipline beyond this file, carry it explicitly in the lane packet, brief, or launcher rather than bloating this wrapper into a duplicate doctrine file.
