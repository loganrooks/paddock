# 03 Guardrails, Mechanisms, And Command Proposals

## Research Frame
- Mode: solution evaluation
- Question: What concrete guardrails, workflow modifications, commands, skills, and automation changes would make this repo's local GSD/Codex setup better at subagent-led exploration, cleaner task transitions, stronger `LONG-ARC.md` carry-forward, and lower shortcut or hallucination risk without requiring constant expert supervision?
- Scope: Repo-local GSD/Codex setup as it exists now: repo policy, `.planning/` canon, `.codex/get-shit-done` workflows, the repo overlay under `tooling/portable-gsd/overlay/get-shit-done/`, current hooks, and current failure signals.
- Non-goals:
  - redesigning GSD as a general-purpose product for all repos
  - recommending broad blocking hooks for nuanced judgment calls
  - deciding specific product doctrine for Prix Guesser itself
- Stop condition: Enough evidence to recommend a prioritized mechanism set, with clear tradeoffs, for this repo's next guardrail iteration.

## Criteria
- `exploration depth`: pushes scope-shaping work into dedicated subagents instead of shallow main-thread reasoning
- `transition hygiene`: prevents silent movement from one substantive task to another with a mixed or ambiguous worktree
- `long-arc carry-forward`: makes `LONG-ARC.md` and preserved seams matter beyond phase-local discussion
- `epistemic reliability`: lowers hallucination, premature closure, transitive-citation drift, and "sounds-finished" failure modes
- `operator burden`: improves autonomy without turning every step into constant human review
- `runtime fit`: works with this repo's actual Codex/GSD setup, including narrow hooks and repo-local overlay

## Path Of Inquiry
- Entry point: The user flagged repeated orchestrator underdelegation, shallow exploration, and dirty task transitions, then requested concrete mechanism proposals grounded in the repo's actual framework.
- Branches considered:
  - pure repo-policy fixes
  - hooks-heavy enforcement
  - workflow/template changes
  - new command/skill additions
  - config/profile changes
- Branches pursued:
  - repo policy because many current failures are already named but weakly operationalized
  - lifecycle workflow changes because `LONG-ARC.md` is strong in phase steering but weak in project/milestone lifecycle
  - command/skill additions because some missing behavior is too nuanced for hooks and too reusable for ad hoc prompts
  - narrow automation because dirty-tree and destructive-command reminders already exist
- Branches deferred or abandoned:
  - broad blocking hooks for task-boundary or doctrine checks; too brittle and too context-dependent
  - a recommendation to remove autonomous workflows altogether; that would solve the wrong problem
- Unexpected branches / reframings:
  - The biggest gap is not "lack of guardrails" in general. It is that the strongest existing guardrails live in phase-local discuss/research/plan flows, while lifecycle/orchestration boundaries remain under-specified.
  - The repo's actual config (`mode: yolo`, `workflow.auto_advance: true`, `git.branching_strategy: none`) is materially looser than the rigor bar expressed in `AGENTS.md`, `WORKFLOW.md`, and recent signals.

## Assumptions Surfaced
- `[assumed:reasoned]` This repo will continue using repo-local GSD plus the local overlay rather than switching frameworks entirely.
  - Why it matters: most recommendations are incremental overlay/workflow changes, not a replacement architecture.
  - What could weaken it: a deliberate move away from repo-local GSD.
- `[assumed:reasoned]` Narrow hooks should remain the preferred hook posture for this repo.
  - Why it matters: several tempting fixes are better implemented as commands or workflow gates than as opaque command denials.
  - What could weaken it: if future Codex hook capabilities become much richer and more explainable.
- `[assumed:reasoned]` Exploratory and audit work in this repo is usually high-stakes enough that subagent fan-out is worth the latency.
  - Why it matters: several proposals make subagent-led exploration the default for scope-shaping work.
  - What could weaken it: if certain exploration classes turn out to be reliably trivial.
- `[evidenced:cited]` The repo wants autonomy with rigor, not autonomy at any cost.
  - Why it matters: recommendations should reduce expert supervision load without removing meaningful human gates.
  - Support: `AGENTS.md`, `.planning/AGENTS.md`, `WORKFLOW.md`, `AI-GUARDRAILS.md`, `LONG-ARC.md`, and the 2026-04-15 orchestration-failure signal all point in this direction.

## Evidence Base
### Direct evidence
- `AGENTS.md` and `.planning/AGENTS.md` already set a high bar for future-aware planning, subagent use, and anti-shortcut honesty, but those rules are still mostly prompt-level norms rather than enforced workflow steps.
- `WORKFLOW.md` explicitly says "Use agents for bounded work with clear outputs" and that hooks are not the primary enforcement layer.
- `AI-GUARDRAILS.md` requires bounded scope, explicit evidence/inference distinction, and human ownership for canon/roadmap/monetization/legal/public-facing changes.
- `ARTIFACT-GOVERNANCE.md` requires artifact class distinctions and warns that "organized" is not the same as "ready."
- `.planning/config.json` currently sets:
  - `"mode": "yolo"`
  - `"workflow.auto_advance": true`
  - `"git.branching_strategy": "none"`
  - `"workflow.discuss_mode": "exploratory"`
- `.codex/hooks.json` only runs:
  - `SessionStart` reminder hook
  - `PreToolUse` destructive-Bash deny hook
- `.codex/hooks/session_start_guardrail.py` reports dirty-tree, `main` branch, and pre-rerun-boundary context, but does not classify mixed concern buckets or stop cross-task drift.
- `.codex/hooks/pre_tool_use_guardrail.py` blocks obviously destructive commands only.
- `.planning/knowledge/signals/prix-guesser/2026-04-15-orchestrator-underdelegation-dirty-transitions.md` records the actual current failure:
  - exploratory work stayed in the main thread
  - canon-uplift was not cleanly checkpointed before a new audit started
  - the worktree mixed multiple concern buckets
- `.planning/knowledge/signals/prix-guesser/2026-04-08-recursive-gsd-orchestration.md`, `...manual-substitute-planning.md`, and `...premature-stall-diagnosis.md` show earlier failures around broken delegation chains, manual substitutes, and impatience with quiet agents.
- `.planning/LONG-ARC.md` is now strong doctrine about wrappers, visibility, hosting, support, memory layers, and preserve-only seams.
- `.codex/get-shit-done/workflows/discuss-phase.md`, `plan-phase.md`, `research-phase.md`, `quick.md`, and `templates/context.md` already support:
  - `canonical_refs`
  - `future_awareness`
  - `Protected Seams`
  - explicit `LONG-ARC.md` loading when relevant
- `.codex/get-shit-done/workflows/new-project.md`, `new-milestone.md`, `progress.md`, `transition.md`, and `complete-milestone.md` do not show comparable first-class `LONG-ARC.md` handling.
- `.codex/get-shit-done/references/checkpoints.md` says auto-mode bypasses verification and decision checkpoints when auto-chain or auto-advance is active.
- `.codex/skills/gsd-next/SKILL.md` supports `--force` to bypass safety gates.

### Inference and interpretation
- The repo is already better than generic GSD at phase-level future-awareness because the local overlay and current templates normalize `future_awareness` and `canonical_refs`.
- The repo is still weak at lifecycle carry-forward because `LONG-ARC.md` has not been made a first-class participant in milestone start, transition, progress reporting, or milestone completion.
- The current failure pattern is not just "the orchestrator made a bad choice." It is also that the framework lacks a first-class `task boundary` concept between substantive work packages.
- Narrow destructive hooks are working at the right layer. Dirty-worktree classification, mixed-concern transitions, and doctrine-sensitive gating are too contextual to live primarily in a deny hook.
- Current autonomy defaults are too loose for this repo's actual quality bar. `mode: yolo`, `workflow.auto_advance: true`, and a command like `$gsd-next --force` fit throughput-oriented repos better than a doctrine-heavy, future-aware planning repo.

### Unknowns
- It is still unknown whether all recommended command additions should live in the repo-local overlay or whether some should remain repo-specific skills only.
- It is still unknown how much of the lifecycle guidance should be hard-enforced versus surfaced as strong warnings and review artifacts.
- It is still unknown whether the right long-term unit is one new orchestration command or a set of smaller composable commands.

## Dependencies And Relations
| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Subagent-first exploration | runtime subagent support, launch discipline, artifactized bundle specs | research depth, orchestration quality, main-thread context health | medium |
| Task-transition gate | git status visibility, concern-bucket heuristics, explicit active-task model | dirty-worktree hygiene, cross-task contamination | medium |
| LONG-ARC lifecycle integration | project/milestone workflows reading doctrine docs, stable long-arc vocabulary | milestone carry-forward, future seam protection, roadmap clarity | high |
| Provenance/closure audit | research templates, verifier rules, claim/source-basis discipline | hallucination risk, internal-citation drift, fake closure | high |
| Narrow hooks posture | explainable small scripts, operator tolerance for reminders | destructive safety, lightweight context warnings | low |
| Config tightening | user willingness to trade some speed for rigor | autonomy defaults, checkpoint behavior, branch discipline | medium |

## High-Leverage Near-Term Changes

### 1. Make exploratory and scope-shaping work subagent-first by default
- Type: repo-policy change plus workflow/orchestration convention
- Mechanism:
  - Add a standing rule: if a task is exploratory, audit-shaping, scope-shaping, or ambiguity-heavy, the orchestrator must default to a subagent bundle rather than main-thread exploration.
  - Require a lightweight launch bundle artifact before the first spawn for non-trivial parallel exploration. The current `00-launch-bundle-spec.md` should become the normal pattern, not a retroactive repair.
  - Require each exploration bundle to name:
    - lane purpose
    - required reading
    - owned output file
    - stop condition
    - verified runtime settings
- Why this is high leverage here:
  - It directly addresses the 2026-04-15 underdelegation failure.
  - It builds on a repo that already has strong subagent-based phase workflows.
- Tradeoffs:
  - More setup time per exploration bundle.
  - Can feel heavy for genuinely small questions.
- Failure modes:
  - Over-delegation of trivial questions.
  - Creating bundles so broad that they reproduce the same "mushy lane" failure in parallel.
- Near-term implementation cost: low

### 2. Introduce a mandatory task-transition gate before any new substantive task
- Type: repo-policy change, then framework/workflow change
- Mechanism:
  - Before starting a new substantive task, require an explicit transition checkpoint that answers:
    - what task is being closed, paused, or handed off
    - whether its outputs were reviewed/accepted
    - whether the worktree is clean enough to proceed
    - what concern buckets the remaining changes belong to
    - whether the next task can safely share the same branch/worktree
  - This should eventually be operationalized as a command, not just a norm.
- Why this is high leverage here:
  - It directly targets the dirty mixed-worktree transition that the user had to interrupt.
  - Current hooks only report a dirty tree at session start; they do not protect mid-session transitions.
- Tradeoffs:
  - Adds friction between tasks.
  - Requires discipline around what counts as "substantive."
- Failure modes:
  - Becomes box-checking if not tied to concrete concern buckets and acceptance state.
  - If implemented only as documentation, it will drift.
- Near-term implementation cost: low as policy, medium as command

### 3. Tighten repo-local autonomy defaults to match the repo's rigor bar
- Type: repo-policy change plus config change
- Mechanism:
  - Revisit `.planning/config.json` for this repo:
    - change `workflow.auto_advance` from `true` to `false`
    - reconsider `mode: "yolo"` for a doctrine-heavy repo
    - reconsider `git.branching_strategy: "none"` if dirty-transition failures keep recurring
  - Keep `workflow.discuss_mode: "exploratory"`; that part is aligned with the repo's needs.
- Why this is high leverage here:
  - Current autonomy defaults lean toward silent continuation and checkpoint bypass at the same time the repo is asking for more deliberate, future-aware control.
  - `references/checkpoints.md` explicitly says auto-mode bypasses verification/decision checkpoints.
- Tradeoffs:
  - Slower throughput.
  - More explicit operator involvement at boundaries.
- Failure modes:
  - Over-correcting into friction for narrow coding tasks.
  - Confusing repo policy if docs and config diverge.
- Near-term implementation cost: low

### 4. Lift `LONG-ARC.md` into project and milestone lifecycle workflows
- Type: framework/workflow change
- Mechanism:
  - Update `new-project.md`, `new-milestone.md`, `progress.md`, `transition.md`, and `complete-milestone.md` so `LONG-ARC.md` is read when present and relevant, not only during phase-local discuss/research/plan flows.
  - Add explicit prompts/checklists such as:
    - "What current milestone choice affects long-arc doctrine?"
    - "What preserved seams or reversal-sensitive boundaries remain live?"
    - "What changed enough that `LONG-ARC.md` needs an update?"
  - Add a lightweight `long_arc_delta` or `future_doctrine_check` step to milestone start/completion and phase transition.
- Why this is high leverage here:
  - The repo already did the hard doctrinal work in `LONG-ARC.md`.
  - Right now that doctrine is too easy to leave ambient outside phase planning.
- Tradeoffs:
  - More lifecycle verbosity.
  - Risk of pulling long-arc concerns into near-term execution if phrased badly.
- Failure modes:
  - Turning `LONG-ARC.md` into a second roadmap.
  - Forcing irrelevant doctrine into every phase when it does not materially constrain the work.
- Near-term implementation cost: medium

## Additional Mechanisms Grouped By Type

### Repo-policy changes

#### 5. Formalize an `active substantive task` model
- Mechanism:
  - Keep one explicit active substantive task at a time in the planning surface.
  - A second substantive task requires one of:
    - task closed
    - task paused with handoff
    - task split into parallel lanes under one parent bundle
- Why:
  - The current failure was partly "there was no active-boundary object to violate."
- Tradeoffs:
  - Less casual multitasking.
- Failure modes:
  - Artificially blocks legitimate tightly related follow-up work if the parent objective is defined too narrowly.
- Cost: low

#### 6. Restrict shallow modes for doctrine-sensitive work
- Mechanism:
  - For canon, research, audit, or cross-phase orchestration work:
    - do not use `gsd-fast`
    - do not use bare `gsd-quick` without `--discuss`, `--research`, and `--validate` or an equivalent stronger lane
  - Treat those fast paths as implementation conveniences only.
- Why:
  - The repo's failure modes come from exactly the tasks that look "docs-only" but are actually architecture- and doctrine-shaping.
- Tradeoffs:
  - Less convenience.
- Failure modes:
  - Operators route everything through heavyweight flows, including trivial tasks.
- Cost: low

### Framework/workflow changes

#### 7. Add provenance and closure linting to research-to-canon transitions
- Mechanism:
  - Extend research or verification workflows so they check whether a research artifact that is about to drive canon or roadmap changes:
    - distinguishes direct external grounding from internal or traceable support
    - separates evidence, inference, and unknowns
    - states what must remain open
  - Use the repo's current source-basis distinctions rather than generic citation counts.
- Why:
  - The large 2026-04-12 audit repeatedly found "well-written but under-grounded" doctrine and internal-citation drift.
- Tradeoffs:
  - More work before canon uplift.
- Failure modes:
  - Overly rigid linting of exploratory artifacts that are not actually canon inputs.
- Cost: medium

#### 8. Add cross-task worktree classification to progress and next-step routing
- Mechanism:
  - `progress` and `next` should not only say what phase or plan is next.
  - They should also surface:
    - dirty tree summary
    - whether changes appear to belong to one concern bucket or many
    - whether starting the next workflow would cross a task boundary
  - This should be a warning/gate step, not a generic hook denial.
- Why:
  - The repo already has the information to know when the tree is dirty, but not when that dirtiness is semantically dangerous.
- Tradeoffs:
  - Requires heuristics and maybe a little operator judgment.
- Failure modes:
  - False positives on branches that intentionally hold one coherent multi-file objective.
- Cost: medium

#### 9. Add a long-arc consistency check to milestone start and completion
- Mechanism:
  - `new-milestone` should ask what the milestone is preserving from `LONG-ARC.md`.
  - `complete-milestone` should ask what was learned that:
    - validates long-arc doctrine
    - weakens it
    - should be promoted into it
  - `transition` should optionally record if a completed phase created a `LONG-ARC`-relevant delta.
- Why:
  - Right now `PROJECT.md` evolution exists, but long-arc evolution is still too manual.
- Tradeoffs:
  - Slightly heavier milestone ceremonies.
- Failure modes:
  - Treating every phase summary as long-arc doctrine input.
- Cost: medium

### Hook / automation ideas

#### 10. Keep hooks narrow, but enrich `SessionStart` with task-boundary context
- Mechanism:
  - Expand the existing `SessionStart` message to include:
    - whether there is an unresolved active substantive task
    - whether the dirty tree spans multiple concern buckets
    - whether a handoff/transition checkpoint is missing
  - Keep this informational, not blocking.
- Why:
  - Current hook already proves the repo tolerates light contextual reminders.
  - This is the right layer for reminding, not the right layer for nuanced adjudication.
- Tradeoffs:
  - More startup noise.
- Failure modes:
  - If the heuristic is poor, the warning becomes ambient sludge.
- Cost: low to medium

#### 11. Do not add broad blocking hooks for doctrine, mixed tasks, or long-arc reasoning
- Type: explicit anti-recommendation
- Why:
  - Those checks are too contextual and too likely to produce false positives or opaque denials.
  - The repo itself already says hooks are not the main enforcement layer.
- Better alternative:
  - explicit workflow commands
  - launch bundle artifacts
  - transition gates
  - progress/next warnings

## Candidate New Commands Or Skills

### `gsd-launch-bundle`
- Purpose:
  - Create a launch-bundle artifact before subagent research/audit fan-out.
  - Spawn the bundle, verify effective runtime settings, and track expected outputs.
- Why current setup is insufficient:
  - The current bundle spec had to be written retroactively after launch.
  - Launch discipline is currently a prompt habit, not a mechanism.
- High-value features:
  - lane manifest generation
  - required-reading capture
  - expected output paths
  - spawn verification against runtime state
  - status table for open/complete lanes
- Tradeoffs:
  - More ceremony before exploration.
- Failure modes:
  - Operators use it mechanically and still write mushy lanes.

### `gsd-task-boundary`
- Purpose:
  - Run the mandatory transition gate between substantive tasks.
- Why current setup is insufficient:
  - SessionStart warns about dirtiness only at session start, not at task handoff.
  - No workflow today owns "am I allowed to start a new substantive objective on this tree?"
- High-value features:
  - concern-bucket summary
  - active-task close/pause/handoff choice
  - branch/worktree suitability warning
  - output note written to `.planning/` when the task is paused or deferred
- Tradeoffs:
  - Another command to remember.
- Failure modes:
  - Poor bucket heuristics create false safety or false alarm.

### `gsd-long-arc-review`
- Purpose:
  - Review whether a milestone, phase transition, or canon change has consequences for `LONG-ARC.md`.
- Why current setup is insufficient:
  - `LONG-ARC.md` is strong doctrine but not a first-class lifecycle actor.
- High-value features:
  - identify doctrine deltas
  - classify them as:
    - canon uplift now
    - preserve-only note
    - inquiry debt
    - no change
  - produce a small patch proposal rather than silently editing doctrine
- Tradeoffs:
  - Can feel heavy if run after every tiny phase.
- Failure modes:
  - Becomes a ritual that always says "no change."

### `gsd-research-closure-audit`
- Purpose:
  - Check whether a research or audit artifact is actually strong enough to support canon or roadmap changes.
- Why current setup is insufficient:
  - The repo has already seen multiple cases where "well-cited enough" and "actually grounded enough" diverged.
- High-value features:
  - source-basis classification
  - evidence/inference split check
  - identify what must remain open
  - say whether follow-up research is required
- Tradeoffs:
  - Adds another gate before canon edits.
- Failure modes:
  - If overused, slows down low-risk documentation work.

### `gsd-orchestration-health`
- Purpose:
  - Audit whether the current workspace and orchestration posture are healthy before a major run.
- Why current setup is insufficient:
  - The repo has signals about recursive orchestration, manual substitute planning, premature stall diagnosis, and underdelegation, but no command that synthesizes them into a preflight.
- High-value features:
  - detect dirty mixed worktree
  - detect risky config posture
  - detect missing launch bundle for active multi-agent work
  - detect stale handoffs or broken anti-pattern acknowledgments
- Tradeoffs:
  - Could duplicate `progress` if not scoped tightly.
- Failure modes:
  - Turns into a noisy checklist unless it is sharply bounded.

## Recommended Package By Leverage And Cost

### Near-term, low cost
- Adopt subagent-first exploration as a standing repo rule.
- Require a launch-bundle artifact before non-trivial multi-agent exploration.
- Add a mandatory task-transition gate as policy.
- Tighten repo config defaults away from `yolo` + auto-advance for this repo.
- Enrich `SessionStart` warnings, but keep them non-blocking.

### Medium-term, medium cost
- Implement `gsd-task-boundary`.
- Implement `gsd-launch-bundle`.
- Lift `LONG-ARC.md` review into `new-milestone`, `transition`, `progress`, and `complete-milestone`.
- Add research-closure/provenance audit support before canon uplift.

### Later, conditional
- Add `gsd-long-arc-review` if lifecycle integration via existing workflows still feels too diffuse.
- Add `gsd-orchestration-health` if repeated orchestration failures persist after the simpler gates land.
- Revisit broader branch/worktree automation only if current branch-discipline conventions keep failing.

## What Should Remain Human-Gated
- Any choice that moves a preserve-only seam or reversal-sensitive boundary into active doctrine.
- Monetization, access, support, or service-obligation changes.
- Legal posture, branding, affiliation language, and public launch posture.
- Major canon rewrites that materially change project identity, milestone arc, or long-arc doctrine.
- Destructive cleanup, archive decisions, or deletion of large artifact sets.
- Any use of bypass paths such as `--force` when they would skip meaningful review.
- Decisions to collapse currently live rivals into one winner when the evidence is still challengeable.

## Scope Expansions And Deferrals
- Follow-and-mark:
  - Repo config posture should be audited separately once the current canon-uplift branch stabilizes; it likely deserves actual changes, not just memo treatment.
- Revisit later:
  - Whether these mechanisms should move upstream into generic GSD or stay repo-local.
  - Whether Codex-native runtime APIs will eventually make some of the launch verification and task-boundary tracking easier to automate.
- Deferred:
  - CI or remote-host enforcement. This memo is about local GSD/Codex mechanics first.

## What Can Close Now
- `[decided:reasoned]` The repo should not rely on the main thread for most exploratory or scope-shaping work; subagent-led exploration should be the default.
- `[decided:reasoned]` Dirty-task-transition control should be implemented primarily as explicit workflow/command gating, not as broad deny hooks.
- `[decided:reasoned]` `LONG-ARC.md` integration is currently too phase-local and should be lifted into milestone/project lifecycle workflows.
- `[decided:reasoned]` Current autonomy defaults are looser than this repo's actual rigor bar and should be revisited.
- `[decided:reasoned]` The highest-leverage additions are a launch-bundle mechanism, a task-boundary mechanism, and lifecycle `LONG-ARC` integration.

## What Must Stay Open
- The exact split between repo-local overlay changes and repo-specific skill additions.
- The exact threshold that should trigger mandatory subagent fan-out.
- Whether `gsd-long-arc-review` should be a standalone command or a capability folded into milestone/transition workflows.
- Whether branch automation should be strengthened through config or kept as convention plus guardrails.

## Planning Handoff
- What can now be treated as decided:
  - future-aware rigor for this repo needs stronger mechanisms, not just stronger prose rules
  - subagent-led exploration and task-boundary hygiene are the two most urgent orchestration fixes
  - lifecycle handling of `LONG-ARC.md` is a structural gap
- What remains assumed or open:
  - exact implementation location for the new commands and workflow changes
  - exact config posture after the repo stabilizes
- Derived constraints:
  - keep hooks narrow and explainable
  - prefer command/workflow gates for nuanced judgment
  - avoid generic best-practice inflation; keep proposals tied to the actual local overlay and signals
- Future-awareness seams to preserve:
  - long-arc doctrine should inform day-to-day planning without turning into ambient scope creep
  - preserve-only and reversal-sensitive boundaries should not disappear inside shorthand workflow outputs
- Follow-up research or implementation lanes suggested:
  - implement `gsd-task-boundary`
  - implement `gsd-launch-bundle`
  - audit and patch lifecycle workflows for `LONG-ARC.md` integration
  - audit repo config against the repo's actual rigor bar

## Sources
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.codex/hooks.json`
- `.codex/hooks/session_start_guardrail.py`
- `.codex/hooks/pre_tool_use_guardrail.py`
- `.planning/config.json`
- `.planning/LONG-ARC.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-orchestrator-underdelegation-dirty-transitions.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-recursive-gsd-orchestration.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-manual-substitute-planning.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-premature-stall-diagnosis.md`
- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/plan-phase.md`
- `.codex/get-shit-done/workflows/research-phase.md`
- `.codex/get-shit-done/workflows/quick.md`
- `.codex/get-shit-done/workflows/new-project.md`
- `.codex/get-shit-done/workflows/new-milestone.md`
- `.codex/get-shit-done/workflows/progress.md`
- `.codex/get-shit-done/workflows/transition.md`
- `.codex/get-shit-done/workflows/complete-milestone.md`
- `.codex/get-shit-done/templates/context.md`
- `.codex/get-shit-done/references/checkpoints.md`
- `.codex/skills/gsd-next/SKILL.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md`
