# Long-Arc Lifecycle Integration Audit

## Research Frame
- Mode: `solution evaluation`
- Question:
  is the local repo GSD framework, as it currently exists under `.codex/get-shit-done` and `tooling/portable-gsd/overlay/get-shit-done`, capable of carrying long-horizon doctrine into day-to-day work, or is `.planning/LONG-ARC.md` still too phase-local and easy to lose during project and milestone lifecycle work?
- Scope:
  - root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
  - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
  - [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
  - [.planning/PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
  - [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
  - [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
  - lifecycle and phase workflows/templates under `.codex/get-shit-done`
  - repo overlay coverage under `tooling/portable-gsd/overlay/get-shit-done`
- Non-goals:
  - patching the framework
  - auditing every GSD skill
  - evaluating code-execution quality or hallucination guardrails beyond their relation to long-horizon integration
  - deciding whether all recommended changes belong upstream versus repo-local overlay
- Stop condition:
  - identify where long-arc awareness is first-class, where it is indirect, and where it drops out
  - judge whether the framework is robust enough as-is
  - recommend concrete mechanisms that would materially improve lifecycle integration

## Criteria
- `phase-steering strength`
  - does the framework make long-horizon doctrine usable during discuss, research, and planning?
- `lifecycle continuity`
  - does long-arc awareness survive initialization, progress routing, transition, milestone turnover, and milestone completion?
- `default-path safety`
  - does the normal path preserve long-arc awareness, or is it easy to bypass accidentally?
- `operator-memory independence`
  - how much does the system rely on humans remembering to re-inject `.planning/LONG-ARC.md` manually?
- `mechanism explicitness`
  - are preserved seams and non-decisions represented as first-class workflow inputs, or only ambient lore?

## Path Of Inquiry
- Entry point:
  - user request to audit how the local GSD framework integrates `.planning/LONG-ARC.md`, future awareness, preserved seams, and non-decisions
- Branches considered:
  - the framework may already be fully lifecycle-aware and the repo may simply be using it correctly
  - the framework may be strong only in phase-level steering
  - the repo overlay may have already patched lifecycle weak points
  - the repo may be compensating manually through canon docs and AGENTS rules
- Branches pursued:
  - read repo canon and instruction docs to understand expected long-horizon behavior
  - inspect base phase workflows and templates for direct long-arc integration
  - inspect lifecycle workflows and templates for the same
  - inspect overlay coverage and relevant overlay files to see what the repo has actually customized
  - compare current repo practice against framework support
- Branches deferred or abandoned:
  - deep inspection of `gsd-tools.cjs init` internals
  - end-to-end execution trace of a fresh project lifecycle
  - audit of every command unrelated to lifecycle or phase steering
- Unexpected branches / reframings:
  - the current repo canon already compensates for framework weaknesses much more than expected
  - the key problem is not that long-arc support is absent; it is that it is concentrated in `CONTEXT.md` production and consumption, while major lifecycle workflows remain mostly blind to it

## Assumptions Surfaced
- `[assumed:reasoned]` If long-arc awareness lives mainly in `CONTEXT.md`, then project and milestone lifecycle workflows can still drift unless they also read or update `.planning/LONG-ARC.md`.
  - Why it matters:
    phase-level strength is not enough if later milestone framing, progress routing, and canon evolution stop consulting the doctrine.
  - What could falsify it:
    evidence that lifecycle commands independently recover equivalent doctrine from `PROJECT.md` / `ROADMAP.md` without needing explicit `LONG-ARC.md` reads.
- `[assumed:reasoned]` This repo expects `.planning/LONG-ARC.md` to be an active steering source, not just an archival note.
  - Why it matters:
    the audit should judge the framework against the repo's actual operating standard, not generic GSD minimalism.
  - What could falsify it:
    repo canon treating `LONG-ARC.md` as optional background rather than something discuss/planning should consume.
- `[assumed:reasoned]` Overlay coverage is a useful proxy for what the repo has considered important enough to preserve across reinstall.
  - Why it matters:
    if lifecycle files are not in the overlay, long-arc lifecycle support likely has not been made repo-local first-class.
  - What could weaken it:
    if the current runtime has additional untracked local edits outside the overlay.

## Evidence Base
### Direct evidence
- Root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md) explicitly requires agents to think across the repo's horizon stack and treat `.planning/LONG-ARC.md` as part of live operational state.
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md) explicitly says `LONG-ARC.md` carries farther doctrine that current planning must preserve, and says future-flexibility work should distinguish `direct doctrine`, `bounded-open branches`, `preserve-only seams`, `reversal-sensitive boundaries`, and `inquiry debt`.
- [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md) defines durable doctrine for wrappers, memory layering, hosting, visibility, support, and milestone arc, and explicitly says downstream discuss, research, and planning should treat it as durable doctrine rather than re-litigating it phase by phase.
- [.planning/PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md) explicitly tells readers to use `.planning/LONG-ARC.md` for detailed transition doctrine and uses long-arc-aware posture language in both the milestone arc and future-aware posture sections.
- [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md) includes `.planning/LONG-ARC.md` in `Canonical refs` for each active phase, which is a manual project-level mechanism for injecting long-arc doctrine into phase work.
- [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md) says future discuss/planning should cite `LONG-ARC.md` and that replanning should consume it before fresh planning artifacts are treated as authoritative.
- `.codex/get-shit-done/workflows/discuss-phase.md` explicitly:
  - reads `.planning/LONG-ARC.md` when present
  - says `LONG-ARC.md` is durable doctrine about product shape, visibility, hosting, support, and wrapper preservation
  - adds `.planning/LONG-ARC.md` to `canonical_refs` when it materially constrains the phase
  - derives a structured `<future_awareness>` accumulator with `Protected Seams`, `Explicit Non-Decisions`, `Current Posture`, and `Future Shape Notes`
- `.codex/get-shit-done/templates/context.md` makes `<canonical_refs>` mandatory and explicitly tells agents to include durable doctrine docs such as `.planning/LONG-ARC.md` when they constrain the phase. It also defines a normalized `<future_awareness>` section with `Protected Seams`, `Explicit Non-Decisions`, `Current Posture`, and `Future Shape Notes`.
- `.codex/get-shit-done/workflows/research-phase.md` resolves `context_canonical_refs` from `CONTEXT.md`, includes them in the researcher's read list, and tells the researcher to treat `<future_awareness>` and `Protected Seams` as real guardrails.
- `.codex/get-shit-done/workflows/plan-phase.md`:
  - hard-stops planning without `CONTEXT.md` in exploratory mode unless `--allow-no-context` is supplied
  - warns that proceeding without context reduces future-aware guarantees
  - resolves `context_canonical_refs` from `CONTEXT.md`
  - requires downstream agents to include those refs
  - tells planner and checker to preserve `future_awareness`, protect seams, respect explicit non-decisions, and flag plans that violate them
- Search across the lifecycle files and generic templates found no `LONG-ARC`, `future_awareness`, `Protected Seams`, `Explicit Non-Decisions`, or `canonical_refs` matches in:
  - `.codex/get-shit-done/workflows/new-project.md`
  - `.codex/get-shit-done/workflows/new-milestone.md`
  - `.codex/get-shit-done/workflows/progress.md`
  - `.codex/get-shit-done/workflows/transition.md`
  - `.codex/get-shit-done/workflows/complete-milestone.md`
  - `.codex/get-shit-done/templates/project.md`
  - `.codex/get-shit-done/templates/roadmap.md`
- The lifecycle workflow bodies confirm that absence:
  - `new-project.md` scaffolds project/requirements/roadmap and config but does not scaffold or mention `.planning/LONG-ARC.md`
  - `new-milestone.md` reads and updates `PROJECT.md`, `STATE.md`, and later roadmaps/research, but does not mention long-arc review
  - `progress.md` routes from `ROADMAP` and `STATE` and checks for `CONTEXT.md`, but does not surface long-arc posture directly
  - `transition.md` reads `STATE.md`, `PROJECT.md`, `ROADMAP.md`, and phase summaries, but not `.planning/LONG-ARC.md`
  - `complete-milestone.md` requires `ROADMAP.md`, `REQUIREMENTS.md`, and `PROJECT.md`, but not `.planning/LONG-ARC.md`
- Overlay coverage under `tooling/portable-gsd/overlay/get-shit-done` includes:
  - `discuss-phase.md`
  - `plan-phase.md`
  - `research-phase.md`
  - `templates/context.md`
  - `quick.md`
  - `discuss-phase-assumptions.md`
  - `discuss-phase-power.md`
  but does not include overlay copies of:
  - `new-project.md`
  - `new-milestone.md`
  - `progress.md`
  - `transition.md`
  - `complete-milestone.md`
  - `templates/project.md`
  - `templates/roadmap.md`
- The overlay therefore preserves or reinforces phase-steering future-awareness, but it does not presently patch lifecycle weak points.
- `tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs` keeps `workflow.discuss_mode: 'exploratory'` as a default in new-project config construction, which supports stronger future-aware discuss behavior at the phase level.

### Inference and interpretation
- The framework is already strong at `phase steering`:
  - if the project runs `discuss-phase`
  - produces a good `CONTEXT.md`
  - and plans from that context
  then `.planning/LONG-ARC.md`, preserved seams, explicit non-decisions, and future-awareness buckets are part of the normal downstream path.
- The framework is weak at `project and milestone lifecycle continuity`:
  - initialization does not make `LONG-ARC.md` first-class
  - milestone turnover does not explicitly review or refresh long-arc doctrine
  - progress routing does not foreground long-arc consistency
  - phase transition does not consult or evolve long-arc doctrine
  - milestone completion does not require long-arc review or synchronization
- The repo is currently compensating for those framework gaps manually through canon:
  - `AGENTS.md`
  - `.planning/AGENTS.md`
  - `PROJECT.md`
  - `ROADMAP.md`
  - `STATE.md`
  This means the project is more long-arc-aware than the generic lifecycle machinery would be on its own.
- That compensation is useful but brittle. It depends on operator diligence and canon quality. It does not mean the lifecycle workflows themselves are robustly carrying long-horizon thinking.
- The practical result is:
  - long-arc awareness is `first-class` during discuss/research/plan
  - `indirect` during normal project operation when the repo canon happens to remind the operator
  - and `drops out` during several lifecycle transitions unless humans deliberately re-inject it
- The current framework is therefore `capable but not robust` for this repo's standard. It can support excellent long-horizon design, but only when the operator deliberately stays on the phase-steering path and the repo canon remains unusually strong.

### Unknowns
- I did not run a fresh end-to-end lifecycle through `new-project`, `new-milestone`, `transition`, and `complete-milestone`, so this audit is based on workflow definitions and repo canon rather than live command traces.
- I did not inspect every `gsd-tools` init payload, so there may be internal fields that indirectly expose long-arc state without the workflows currently using them.
- I did not audit whether other skills outside the main lifecycle paths already provide partial long-arc review mechanisms.

## Option Comparison

| Option | Description | Strengths | Weaknesses | Evaluation |
| --- | --- | --- | --- | --- |
| A | Current framework as generic lifecycle plus strong phase steering | Good discuss/research/plan integration; explicit future-awareness buckets; canonical refs flow cleanly | Lifecycle work can forget long-arc doctrine; initialization and milestone turnover do not elevate it | Better than generic GSD, not enough for this repo's quality bar |
| B | Current framework plus this repo's manual canon compensation | Works today when operators respect `AGENTS.md`, `PROJECT.md`, `ROADMAP.md`, `STATE.md`, and rerun discuss properly | Highly memory-dependent; long-arc continuity lives in docs and user discipline more than workflow enforcement | This is the repo's actual current state: functional, but brittle |
| C | Framework with first-class long-arc lifecycle integration | Long-horizon doctrine survives project creation, progress routing, milestone turnover, transition, and completion; lower dependence on operator memory | Requires workflow/template and possibly CLI changes | Recommended direction |

## Dependencies And Relations
| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| `.planning/LONG-ARC.md` as active doctrine | Repo canon discipline | Discuss, planning, milestone framing, canon uplift | medium |
| `discuss-phase` future-awareness flow | `workflow.discuss_mode`, good context capture | Research and planning quality | medium |
| `CONTEXT.md` canonical refs and future awareness | Good discuss output and planner consumption | Whether later phase work preserves seams | medium |
| `PROJECT.md` and `ROADMAP.md` manual long-arc references | Human canon upkeep | Current repo compensation for lifecycle blind spots | high |
| Lifecycle workflows (`new-project`, `new-milestone`, `progress`, `transition`, `complete-milestone`) | Base framework design | Whether long-horizon doctrine survives outside phase steering | high |
| Repo overlay coverage | What files the repo chose to patch | Reinstall durability of long-arc integration | medium |

## What The Framework Already Does Well
- It has a real, not cosmetic, future-awareness model at the phase level.
- It treats `CONTEXT.md` as a steering brief rather than a list of locked preferences.
- It distinguishes future-awareness from deferred ideas.
- It requires canonical references rather than leaving doctrine ambient.
- It explicitly tells research and planning agents to preserve seams and respect explicit non-decisions.
- It defaults this repo toward `exploratory` discuss mode, which is the right bias for preserving uncertainty instead of forcing premature closure.
- It gives the repo an extension point, via the overlay, to preserve these stronger phase-steering behaviors across reinstall.
- It already has a fallback warning path in `plan-phase`: if the operator bypasses `CONTEXT.md`, the workflow says future-aware guarantees are reduced instead of pretending nothing changed.

## Lifecycle Blind Spots

### Initialization
- `new-project.md` does not make `.planning/LONG-ARC.md` a first-class artifact.
- `templates/project.md` and `templates/roadmap.md` have no built-in slot for long-arc doctrine, preserved seams, or explicit non-decisions.
- Result:
  a repo can start cleanly without any explicit long-horizon doctrine artifact, and the generic project scaffold will not ask for one.

### Milestone Turnover
- `new-milestone.md` updates `PROJECT.md`, `STATE.md`, and later requirements/roadmap work, but does not require a long-arc carry-forward review.
- Result:
  milestone framing can drift toward near-term goals without a forced check against the doctrine that current work is supposed to preserve.

### Progress And Routing
- `progress.md` is strong at roadmap/phase routing, but it does not surface whether the current phase's steering is long-arc-grounded beyond checking for `CONTEXT.md`.
- Result:
  the route to "next step" can look healthy even when long-arc posture is only weakly encoded or stale in canon.

### Phase Transition
- `transition.md` evolves `PROJECT.md` from summaries, but it does not read `.planning/LONG-ARC.md`.
- Result:
  new learnings can enter project canon while long-arc doctrine remains unchanged or inconsistent, unless humans manually perform a second doctrine pass.

### Milestone Completion
- `complete-milestone.md` performs a full `PROJECT.md` review and archives roadmap/requirements, but it does not require a long-arc doctrine review.
- Result:
  milestone learnings can be archived without deciding whether they belong in the farther doctrine layer.

### Overlay Scope
- The overlay strengthens phase steering and quick-task doctrine carry-forward, but it does not currently patch the lifecycle workflows or generic `PROJECT.md` / `ROADMAP.md` templates.
- Result:
  the repo has improved the place where long-arc awareness enters phase work, but not the places where that awareness should be re-ratified and carried forward over time.

## Recommended Framework Changes
1. **Make `.planning/LONG-ARC.md` a first-class optional project artifact in `new-project`.**
   - Add detection or prompting logic:
     - does this project need durable doctrine beyond the immediate milestone?
   - If yes, scaffold a `LONG-ARC.md` template and seed `PROJECT.md` / `ROADMAP.md` with explicit references to it.
   - Why:
     this removes the current dependence on manual repo-specific retrofitting.

2. **Expose long-arc presence explicitly in `gsd-tools init` payloads.**
   - Add fields such as:
     - `long_arc_exists`
     - `long_arc_path`
     - optionally `long_arc_last_updated`
   - Why:
     lifecycle workflows should not have to rediscover or ignore doctrine by ad hoc file checks.

3. **Add a milestone-start carry-forward gate to `new-milestone.md`.**
   - Require a short review:
     - what in `LONG-ARC.md` still governs?
     - what new milestone goals must preserve?
     - what, if anything, should now be updated in doctrine?
   - Why:
     this is the exact point where near-term planning most easily eclipses long-term posture.

4. **Add long-arc routing visibility to `progress.md`.**
   - Show whether the current phase has:
     - `CONTEXT.md`
     - canonical refs including long-arc doctrine when relevant
     - any explicit future-awareness sections
   - At minimum, warn when exploratory planning is about to proceed with no clear long-arc grounding.
   - Why:
     progress should reflect not just execution readiness, but whether the steering substrate is complete enough for this repo's standards.

5. **Require doctrine triage in `transition.md`.**
   - After reading phase summaries, classify learnings into:
     - `PROJECT.md` compact identity update
     - `ROADMAP.md` sequencing or constraints update
     - `LONG-ARC.md` doctrine update
     - deferred or non-canonical note
   - Why:
     phase completion is one of the best moments to ratify future-aware lessons before they are lost.

6. **Require long-arc review during `complete-milestone.md`.**
   - Add `.planning/LONG-ARC.md` to required reading.
   - Add a milestone-completion checklist item:
     - did this milestone change durable doctrine, preserved seams, or explicit non-decisions?
   - Why:
     milestone completion should be the strongest canon checkpoint, not only a `PROJECT.md` evolution pass.

7. **Extend generic templates to acknowledge long-arc doctrine.**
   - `templates/project.md`:
     add an optional section or explicit pointer for farther doctrine when a project needs it.
   - `templates/roadmap.md`:
     add optional `Canonical refs` and `Protects` / `Carry-forward constraints` support in the generic phase template, or at least document how to include them.
   - Why:
     the current repo had to add these patterns manually; the templates do not help.

8. **Add a dedicated long-arc consistency command or audit mode.**
   - Possible shapes:
     - `gsd-long-arc-review`
     - `gsd-canon-sync --long-arc`
     - an extension to `gsd-progress` or `gsd-complete-milestone`
   - Output should compare:
     - `PROJECT.md`
     - `ROADMAP.md`
     - `REQUIREMENTS.md`
     - `STATE.md`
     - relevant active `CONTEXT.md`
     against `LONG-ARC.md`
   - Why:
     this reduces dependence on expert human rereading to catch doctrine drift.

9. **Keep the current phase-steering future-awareness model; do not replace it with vague “think long term” prose.**
   - The normalized buckets are already good:
     - `Protected Seams`
     - `Explicit Non-Decisions`
     - `Current Posture`
     - `Future Shape Notes`
   - The change needed is lifecycle propagation, not phase-steering reinvention.

## Scope Expansions And Deferrals
- `Follow-and-mark`
  - this audit broadened from "does `LONG-ARC.md` appear in workflows?" to "how does the whole lifecycle retain or lose long-horizon doctrine?"
- `Revisit later`
  - whether `REQUIREMENTS.md` should also gain more generic support for preserve-only or reversal-sensitive statuses
  - whether lifecycle checks belong in existing commands or a dedicated new command
- `Defer`
  - implementation details of new CLI fields or command names
  - broader anti-hallucination guardrail audit beyond long-horizon integration

## What Can Close Now
- The framework already supports long-horizon thinking well in phase steering.
- The repo overlay reinforces that phase-steering path, but mostly does not extend it into lifecycle workflows.
- The current repo is more long-arc-aware than the framework alone because canon docs and AGENTS rules compensate manually.
- Long-arc awareness is still too phase-local and too easy to lose during initialization, milestone turnover, progress routing, transition, and milestone completion.
- Therefore the current framework is `partially capable but not yet lifecycle-robust` for the repo's standard of excellent future-aware design.

## What Must Stay Open
- Whether the right implementation path is:
  - patching existing lifecycle workflows
  - adding a dedicated long-arc audit command
  - or both
- How much of the recommended lifecycle integration belongs upstream in generic GSD versus this repo's portable overlay
- Whether generic templates should stay lightweight with optional long-arc sections, or adopt stronger doctrine hooks by default

## Planning Handoff
- What can now be treated as decided:
  - the framework's main long-arc strength is the `discuss -> context -> research/plan` path
  - the main weakness is lifecycle continuity, not lack of phase-level concepts
  - the overlay does not currently solve the lifecycle problem
- What remains assumed or open:
  - exact command/CLI mechanism for long-arc consistency auditing
  - whether all recommended changes should be repo-local first
- Derived constraints:
  - any framework improvement should preserve the existing `future_awareness` bucket vocabulary
  - improvements should reduce operator-memory dependence rather than adding more ambient prose
  - lifecycle changes should make `LONG-ARC.md` visible without smuggling future scope into every command
- Future-awareness seams to preserve:
  - phase-local preserved seams and non-decisions should remain explicit and normalized
  - `PROJECT.md` compact identity, `ROADMAP.md` sequencing, and `LONG-ARC.md` durable doctrine should remain distinct layers
- Deferred follow-up work:
  - audit the broader guardrail and anti-shortcut story beyond long-arc integration
  - decide whether to implement lifecycle fixes via overlay patches, new skills, or both

## Sources
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
- [.planning/PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
- [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
- [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md)
- [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md)
- [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md)
- [.codex/get-shit-done/workflows/new-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-project.md)
- [.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md)
- [.codex/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md)
- [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md)
- [.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md)
- [.codex/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md)
- [.codex/get-shit-done/templates/project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/project.md)
- [.codex/get-shit-done/templates/roadmap.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/roadmap.md)
- [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md)
- [tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md)
- [tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md)
- [tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md)
- [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md)
- [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-power.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-power.md)
- [tooling/portable-gsd/overlay/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/context.md)
- [tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs)
