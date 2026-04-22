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
- For repo-local harness self-improvement work that should survive one audit subtree, treat `.planning/HARNESS-IMPROVEMENT-REGISTER.md` as the durable cross-family register rather than relying on one audit workspace alone.
- Treat `discovery/` as upstream context, not as live implementation workflow state.
- Current boundary: Phase 01 is still at a pre-rerun boundary. Run a fresh discuss + planning pass before treating the existing `01-*` bundle as execution-approved.
- For non-phase-bound research or deliberation, prefer the repo-local `gsd-rigorous-research` skill over ad hoc structure.
- Treat `CONTEXT.md` as a steering brief: decisions, assumptions, open questions, canonical refs, code context, and future awareness all matter downstream.
- For headless external CLI runs that instruct a model to read a spec or wrapper file, prefer a repo-local path over `/tmp` and be explicit about the permissions needed to read it.
- For `.planning/` artifact-family moves or topology cleanup, use `python3 tooling/codex/audit_refmap.py` rather than hand-editing reference rewrites; detailed rules live in `.planning/AGENTS.md`.
- For repo-local harness prompts, workflows, and agent contracts that use reading packets, prefer layered packet structure:
  - `required_reading` for irreducible startup context
  - `supporting_reading` for route-local widening
  - `deeper_reading` for bounded later expansion
  - keep contextual reread sovereign rather than flattening every possible context surface into startup burden

## Contract Propagation

- When a change alters a contract-carrying surface such as a workflow, skill, script, manifest, durable output, wrapper, or governing doc, do not stop at the local file diff.
- Identify the direct producers, direct consumers, narrative mirrors, runtime/registry carriers, and durable outputs that should stay in tune with the change.
- Update adjacent live carriers in the same slice when the propagation path is already clear. If some neighbors are intentionally held, record that boundary explicitly in a proposal, disposition, or audit artifact instead of leaving it ambient.
- Use the repo-local propagation tools where they fit:
  - `python3 tooling/codex/audit_refmap.py`
  - `python3 harness_modifier/contract/runtime_visibility.py`
  - `python3 harness_modifier/contract/manifest_install_coherence.py`
  - `python3 harness_modifier/contract/harness_canary.py`
  - `python3 tooling/codex/project_uplift.py`
  - `python3 harness_modifier/contract/portable_gsd_contract.py`
- When the change crosses several producer/consumer families and you want the operator-facing review route rather than another ad hoc reread, use `$gsd-propagation-review`.
- For the current worked example of this repo-local doctrine in action, start with:
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/`
- When one slice crosses several propagation families at once, prefer a clean-boundary runtime snapshot plus `python3 harness_modifier/contract/manifest_install_coherence.py . --snapshot <snapshot.json> --strict` as a bounded coherence gate rather than trusting the local diff alone.
- When the question is whether current runtime/install invariants still hold after a bounded slice, prefer `python3 harness_modifier/contract/harness_canary.py report . --strict` over ad hoc reread of `.codex/` files.
- Do not mistake those partial tools for proof that the whole network stayed aligned. When the change crosses several producer/consumer families, open or update an explicit propagation audit surface.

## Quality Bar

- Do not optimize for `good enough`, `passes review`, or the smallest plausible response when the repo has already earned stronger doctrine, cleaner architecture, or better future guidance.
- When a pass produces substantive doctrine, architectural guidance, or future-seam clarification, do not collapse that work into a thin binary-threshold summary if the canon, roadmap, or phase steering should be uplifted to reflect it.
- Do not let threshold language (`adequate`, `sufficient`, `good enough`, `well enough`, `passes`, `ready`) become the master frame for planning, audit, research, or doctrine work when the real task is to maximize carry, leverage, clarity, and long-horizon intervention yield.
- Do not smuggle threshold thinking back in through deficit-oriented pseudo-positive phrasing.
  - Avoid formulations like `not lacking`, `no longer missing`, `not merely deficient`, `not the real problem`, or `better than before` when a direct positive formulation is available.
  - Prefer comparative or directional formulations like `carry broadens here`, `detail thins here`, `this intensifies future carry`, `this opens more optionality`, or `this raises intervention yield`.
- Do not smuggle threshold thinking back in through static-positive evaluative phrasing either.
  - Avoid formulations like `already strong here`, `strong enough`, `clear enough`, or `the family is strong` when the better wording can say what broadened, sharpened, intensified, or became more durable relative to another form.
- In planning, discuss, audit, and research work, do not frame the leading question as `is this adequate`, `is this ready`, `is this clear enough`, or any similar threshold test when the stronger question is what the surface exposes, flattens, preserves, intensifies, or leaves open.
- Binary or threshold questions belong only to real gate surfaces such as behavioral verification, execution admission, or explicit requirement-gate checks.
  - When a real gate is present, do not let that gate exhaust the thinking.
  - Pair it with the stronger question of what higher-yield form, broader optionality, or clearer future carry is still available.
- Distinguish sharply between:
  - whether an artifact or system can carry work at all
  - how strongly, clearly, and portably it carries that work compared with better available alternatives
- When describing positive results, prefer language like `load-bearing gain`, `higher-leverage surface`, `broader carry`, `clearer authority map`, or `better intervention yield` over threshold praise like `explains well` or `is adequate`.
- Threshold/gate language is allowed only when there is a real gating decision to make. Even then, do not let the gate consume the larger question of how to achieve the strongest available outcome.
- Always think across the repo's actual horizon stack:
  - the current phase or milestone execution surface
  - the next milestone carry-forward surface
  - the farther long-arc doctrine surface ratified in `.planning/LONG-ARC.md`
- Treat `Milestone 2` as the nearest carry-forward horizon, not the ceiling of future-aware thinking.
- Do not optimize only for Milestone 01 convenience if that creates avoidable ambiguity, doc drift, or re-litigation pressure in Milestone 02 and beyond.
- Assume all substantive work may later be audited by expert software engineers and high-capability external models. Write artifacts, plans, code, and rationale so they can withstand adversarial rereading without relying on hidden context, good intentions, or hand-wavy summaries.
- Do not take shortcuts by hiding uncertainty, compressing meaningful distinctions into umbrella terms, or calling something settled just because the current artifact can technically pass.
- Do not confuse compliance with the latest suggestion for quality. Push back when a request, shortcut, framing, or manager instruction would likely degrade architecture, rigor, future viability, or code quality.
- That pushback must be justified, concrete, and scrutiny-resistant:
  - name the risk or loss clearly
  - explain the better alternative
  - make the case in terms that could survive review by expert engineers, not just personal preference
- Pushback does not need to be all-or-nothing.
  - Partial pushback is often the right move:
    - accept the goal but reject the proposed method
    - accept the task but narrow the scope
    - accept the direction but insist on a better sequence or checkpoint first
- When a proposal family has clear directional value but the current packaging is overpacked, do not default to binary `accept/reject`.
  - Prefer narrowing, splitting, staged carry, or consumer-first routing when those preserve the stronger direction with less ceremony and clearer verification.
- When a concern is mainly risk rather than impossibility, do not use risk as a flat veto if sequencing, tooling, checkpointing, bounded rollout, or verification can reduce it.
  - Prefer a mitigation path with explicit quality gates over `too risky` as a stopping point.
- Do not treat extra work by itself as the decisive blocker when the user has explicitly prioritized a stronger organizational, cleanup, or intervention move.
  - Name the real tradeoff instead: blast radius, verification burden, continuity risk, or sequencing cost.
- Before narrowing to the top few options, ask whether the stronger first move is to map the full field.
  - Do not compress full-field mapping into early ranking when the task is terrain disclosure, horizon management, or harness self-transformation.
- Do not be performatively oppositional. Push back when warranted, not as posture.
- For load-bearing planning/process artifacts, load-bearing claims should, where practical, expose terse claim status rather than only sounding generally `cited`.
  - This includes artifacts that can steer canon, phase execution, verification, or workflow policy.
  - Keep the inline layer minimal.
  - Prefer `[type:support:basis]`; use `[type:basis]` only when the support mode is obvious.
  - Minimal reminder:
    - type: `e` evidenced, `d` decided, `a` assumed, `o` open, `p` projected, `s` stipulated, `g` governing
    - support: `c` cited, `r` reasoned, `b` bare
    - basis: `i` internal, `d` external-direct, `t` external-traceable
  - Join multiple support or basis codes with `+` when more than one materially applies.
  - Internal cited grounding must cite the direct file path and line numbers near the claim.
  - External grounding should use markdown footnotes tied to an `External Works Cited` section.
  - Fuller semantics live in:
    - `.planning/CLAIM-TYPES.md`
    - `.codex/skills/gsd-rigorous-research/references/method.md`

## Project-Specific Guidance

- The most important early architectural decisions are likely the authored round/content model and the room authority model.
- Do not collapse those into a premature frontend-framework choice.
- Preserve and express earned distinctions explicitly. Do not let repeated naming density, shorthand, or omission quietly choose winners between live branches.
- Be especially wary of umbrella terms such as `challenge`, `showcase`, `hosted`, `premium`, `membership`, `event`, `reviewed`, `curated`, and `unsupported`. If the distinction matters, spell it out.
- Distinguish general architectural questions from scale-specific topology, latency, or large-room questions.
- When a question depends on external comparative research, case-study evidence, or topology tradeoffs, scope that lane explicitly instead of smuggling it into a generic architecture discussion.
- Before launching a mixed-scope architecture lane, discuss the split with the user first.
- Circuit-internal recognition is the primary fantasy; venue-approach clues are secondary and should not silently replace it.

## Delegation And Orchestration

- Codex GSD orchestration must happen at the top level. Do not create recursive GSD call graphs like `orchestrator -> generic agent -> gsd-plan-phase skill -> gsd-planner`.
- Prefer high-reasoning top-level orchestration with an explicit call graph before launching anything.
- For this repo, when the user invokes or explicitly asks to follow any repo-defined command, skill, workflow, agent contract, reference procedure, or other instruction surface whose contract requires launching an agent (`spawn_agent`), that counts as the user explicitly asking for sub-agents, delegation, or parallel agent work and explicitly authorizes that required `spawn_agent` call.
- If the user explicitly requests delegation to avoid parent-thread context growth, do not duplicate the delegated investigation in the parent thread unless the user explicitly asked for parallel verification.
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
  - state a bounded expected wall-clock duration in commentary when the task is substantial enough to outlive a trivial wait
- Before delegating substantial bounded edits, establish an auditable baseline and clean task boundary.
  - Prefer a checkpoint commit when the current state is coherent and reviewable.
  - If the current state is not yet coherent enough to commit, split, park, or otherwise stabilize it first rather than forcing a bad commit.
  - Do not delegate new substantial edits into an unresolved mixed worktree.
- After an agent returns, review and disposition the result before committing or delegating follow-up work.
  - Use explicit dispositions such as `accept`, `revise`, `park`, or `reject`.
  - Do not auto-commit unreviewed agent output just because the agent finished.
  - If a later verification or fix stage is needed, prefer meaningful checkpoint boundaries between:
    - baseline
    - accepted worker output
    - verification findings
    - fix pass
- Verify effective launch settings after every spawn against `~/.codex/state_5.sqlite`.
- If requested and effective settings differ, stop immediately, kill the agent, and report the mismatch plainly.
- For doctrine-sensitive or otherwise high-stakes spawned work, preserve durable requested-vs-effective launch truth instead of relying on sqlite checks plus memory alone.
  - Prefer `python3 harness_modifier/capture/capture_launch_truth.py --since ...` over weaker `--latest` capture.
  - Preserve the capture in the relevant review, audit, launch-truth, or disposition artifact before accepting the return.
- For substantial external audit lanes or delegated jobs, preserve timing calibration too instead of treating elapsed time as ambient memory.
  - Record an estimated wall-clock duration or bounded range before launch.
  - Record actual elapsed time after completion when the surface already carries launch truth or a durable review/disposition note.
  - Add one short calibration note comparing estimate versus actual so later launches inherit a less naive timing model.

## Maintenance

- This file should stay narrow, stable, and agent-facing.
- Broader workflow, devops, signoff, and artifact-retention detail belongs in the governance docs above, not here.
- If a change would mainly affect work inside `.planning/`, prefer updating `.planning/AGENTS.md` instead of bloating this root file.
- If project posture, workflow policy, or source-of-truth references change, update this file in the same change rather than letting it drift.
