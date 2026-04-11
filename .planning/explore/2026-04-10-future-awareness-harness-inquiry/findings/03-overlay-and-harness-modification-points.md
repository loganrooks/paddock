# Overlay And Harness Modification Points

## 1. Scope and sources

This memo only maps the repo-local overlay and harness surfaces that can carry future-awareness into downstream planning with reasonable durability. It does not survey the whole GSD runtime.

Sources read for this memo:

- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md:123-156,179-191`
- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINTS/10-handoff-for-future-awareness-harness-inquiry.md:34-82,94-115`
- `.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:98-143,145-212`
- `AGENTS.md:7-18,42-57`
- `scripts/setup-portable-gsd.sh:8-25`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:16-26,48-78,466-483,934-1080,1320-1323`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:37-43,115-171,203-239,314-333,618-640,767-777`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md:44-72`
- `tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs:14-31,90-159`
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md:5-11,93-141`
- `tooling/portable-gsd/overlay/get-shit-done/templates/config.json:1-47`
- `tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md:221-257,293-297`

## 2. Real modification points in the repo-local overlay

The real control path is:

- `scripts/setup-portable-gsd.sh:8-25` installs regular repo-local GSD into `.codex/get-shit-done` and then copies every tracked overlay file from `tooling/portable-gsd/overlay/` into `.codex/`, replacing `__PROJECT_ROOT__` on the way.
- That means the durable repo-local levers are the overlay files that the runtime actually executes from `.codex/get-shit-done`, not every file that merely looks like a template or reference.

Concrete modification points that actually affect downstream behavior:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
  This is the strongest upstream lever. It already tells the discuss pass to derive future awareness from `ROADMAP.md`, `PROJECT.md`, requirements, backlog/todos, and prior context, then write it into `CONTEXT.md` (`.../discuss-phase.md:466-483`, `.../discuss-phase.md:934-1080`). If future-awareness needs to become more specific, this is where the shaping logic belongs.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
  This is the strongest downstream propagation lever. It loads `CONTEXT.md`, warns when planning proceeds without it, and passes the steering brief to researcher, planner, and checker with explicit instructions to preserve `<future_awareness>`, `<derived_constraints>`, `<open_questions>`, and `<epistemic_guardrails>` (`.../plan-phase.md:203-239`, `.../plan-phase.md:314-333`, `.../plan-phase.md:618-640`, `.../plan-phase.md:767-777`).
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`
  This is the parity lever for the standalone research path. It separately spawns `gsd-phase-researcher` and tells it to treat `CONTEXT.md` as a steering brief and preserve `<future_awareness>` (`.../research-phase.md:44-72`). If only integrated planning is patched, direct research runs can drift.
- `tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs`
  This is the real config control plane. It defines valid keys and the hardcoded defaults for new projects, including `workflow.discuss_mode`, `workflow.research_before_questions`, and `hooks.context_warnings` (`.../config.cjs:14-31`, `.../config.cjs:90-159`). If a new toggle or enforced default is needed, this is the file that makes it real.

Important supporting surfaces:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:115-171`
  The PRD express path writes `CONTEXT.md` itself. If future-aware structure changes, this branch must stay aligned with `discuss-phase.md`, or PRD-driven phases will bypass the new semantics.
- `AGENTS.md:15-18,42-57`
  This is not part of the overlay runtime, but it is a real repo-local steering layer. It already states that this repo expects exploratory discuss mode and that `CONTEXT.md` should carry future awareness downstream. It is worth keeping aligned, but it is not the enforcement point.

## 3. Dependency and fragility notes

Key dependency relations:

- The overlay does nothing by itself until `scripts/setup-portable-gsd.sh` reapplies it into `.codex/get-shit-done` (`scripts/setup-portable-gsd.sh:8-25`).
- `discuss-phase.md` is the main producer of future-aware `CONTEXT.md`.
- `plan-phase.md` and `research-phase.md` are the main consumers.
- `plan-phase.md` also has a second producer path through the PRD express flow (`.../plan-phase.md:115-171`).
- `config.cjs` governs which workflow flags are valid and what new projects default to; it does not itself guarantee the prompts will use a new concept correctly.

Fragility points worth calling out:

- Patching only the `CONTEXT.md` template is fragile because `discuss-phase.md` writes the actual `CONTEXT.md` body inline in its `write_context` step. The template is not the active generator (`.../discuss-phase.md:934-1080`).
- Patching only `templates/config.json` is fragile because new-project config is materially produced by `buildNewProjectConfig()` in `config.cjs`, not by reading that template file (`.../config.cjs:90-159`).
- Patching only `planning-config.md` is documentation-only. It explains settings; it does not define them (`.../planning-config.md:221-257`).
- Future-awareness propagation is conditional on `CONTEXT.md` existing at all. `plan-phase.md` explicitly allows planning to continue without it, which means any future-aware scheme that depends entirely on context generation can still be bypassed (`.../plan-phase.md:203-239`).
- Cross-phase consistency is stronger only when `CONTEXT_WINDOW >= 500000`, because only then does the planner also pull prior phase `CONTEXT.md` files (`.../plan-phase.md:37-43`, `.../plan-phase.md:618-626`). A scheme that depends on prior contexts being present everywhere will therefore be uneven.

## 4. Robust versus brittle patch options

Easy to patch but not actually worth patching alone:

- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
  Easy to edit, but deceptively weak. It documents the intended `CONTEXT.md` shape, yet `discuss-phase.md` and the PRD path in `plan-phase.md` each generate their own inline structure. Template-only edits are likely to look good and do little.
- `tooling/portable-gsd/overlay/get-shit-done/templates/config.json`
  Also deceptively weak. It looks like the config source, but the runtime defaulting path is in `config.cjs`. Template-only edits are unlikely to change the live behavior of an initialized repo.
- `tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md`
  Worth syncing after a behavior change, not before. It improves operator clarity but cannot carry future-awareness into planning by itself.
- `AGENTS.md`
  Useful as a repo-local reminder, but brittle as the primary lever. It relies on agent discipline rather than workflow enforcement.

Actually worth patching:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
  Best place to make future-awareness concrete. If the repo wants normalized concepts such as protected seams, explicit non-decisions, visibility state, trust boundary, wrapper type, or service obligation, this is where those should be derived and written into `CONTEXT.md`.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
  Best place to make those concepts operational. Planner and checker guidance can require that plans preserve protected seams, surface non-decisions intentionally, and flag scope-foreclosing choices.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`
  Needed for behavioral parity, so standalone research does not become a blind spot.
- `tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs`
  Worth patching only if the project wants a durable switch or default, not just stronger prompts. Good for a small repo-local flag, bad for encoding all semantics here.

## 5. Best layered change path

The best path is layered, with behavior first and templates/docs second.

1. Patch `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`.
   Make the future-aware output more explicit and reusable. The likely win is not adding more prose, but tightening what gets accumulated and written, for example:
   - protected seams to preserve now
   - explicit non-decisions that must stay open
   - current trust / visibility / obligation posture
   - which future candidates are wrappers versus sibling surfaces

2. Patch `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`.
   Keep the integrated research, planner, checker, and PRD-generated `CONTEXT.md` path aligned with the new structure. This is what turns future-awareness from a note into a plan-shaping constraint.

3. Patch `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`.
   Mirror the same semantics for standalone research so direct `research-phase` runs cannot quietly ignore them.

4. Patch `tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs` only if a switch is really needed.
   If the repo wants this behavior always on, prompt changes are probably enough. If it wants an explicit repo-local policy knob, add it here and then carry it into `.planning/config.json`.

5. Only after the behavior is settled, sync:
   - `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
   - `tooling/portable-gsd/overlay/get-shit-done/templates/config.json`
   - `tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md`

This order minimizes the risk of documentation drifting ahead of the actual harness.

## 6. Recommendation

The best repo-local lever is the workflow prompt layer, not the template layer.

Recommended judgment:

- Patch `discuss-phase.md`, `plan-phase.md`, and `research-phase.md` as the primary future-awareness path.
- Treat `config.cjs` as optional support for a small policy toggle or stronger default, not as the main semantic layer.
- Treat `templates/context.md`, `templates/config.json`, and `planning-config.md` as follow-up synchronization work, not as first-line behavior changes.
- Do not rely on `AGENTS.md` or a new `Future Awareness` heading alone. Both are easy to add and easy to bypass.

The deceptively simple patches are the ones most likely to fail this inquiry's goal. The robust path is to change where `CONTEXT.md` is generated and where research/planning/checking prompts are told how to use it.

## Changed files

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/03-overlay-and-harness-modification-points.md`
