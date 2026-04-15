# Cross-Model Audit Integration Research

## Problem framing
- Mode: `synthesis`
- Question: how should cross-vendor / cross-model audit be integrated into this repo's workflows, readiness gates, and harness surfaces as follow-through from the multi-layer harness governance audit?
- Scope:
  - [02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:12)
  - [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:145)
  - [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:26)
  - [DEFERRED.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEFERRED.md:5)
  - [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:149)
  - [gsd-review](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md:48)
  - [gsdr-audit](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:6)
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:109)
  - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:58)
  - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:43)
  - [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:13)
- Non-goals:
  - implement a new skill now
  - collapse repo-local regular GSD and Reflect into one generic surface
  - turn this into an active Checkpoint 0 blocker without stronger evidence
- Stop condition: a later reader can tell which harness layer should own which part of cross-vendor audit, what should remain conditional in readiness, and which Reflect-side patterns are worth importing into the repo's regular stack.

- Path of inquiry:
  - Entry point: the readiness plan already treats cross-vendor audit as selectively important, but leaves integration ownership open ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:145), [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:32)).
  - Branches pursued: work-type fit, existing surface fit, harness-layer ownership, protocol versus skill, and Git/checkpoint interaction.
  - Branches deferred: direct implementation, CLI availability verification on this machine, and remote-host PR/CI wiring.
  - Reframing: this is not mainly a "new mechanism" question; it is a cross-layer handoff question inside the larger governance audit.

`[d:c:i]` Current repo policy already prefers cross-vendor audit for high-stakes review when an external lane is available, but readiness work still treats integration design as conditional follow-through rather than an active checkpoint blocker ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:17), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:165), [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:32), [DEFERRED.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEFERRED.md:12)).

`[e:c:i]` The harness distinction is load-bearing: `gsd-review` belongs to the repo's regular GSD / Codex-local stack because it lives under `.codex` and executes the repo-local `.codex/get-shit-done` workflow, while `gsdr-audit` belongs to the Reflect forked harness family because it reads `$HOME/.codex/get-shit-done-reflect/...` references and ships Reflect-side dispatch logic ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:5), [.codex/skills/gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md:48), [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:1), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:14)).

`[e:c+r:i+t]` Because this extends the multi-layer harness audit rather than replacing it, the right question is which layer should own which part of the behavior: Codex orchestration for selective judgment-heavy rereads, repo-local regular GSD for repeatable phase-plan review, Git for baseline and attribution boundaries, and only later remote review/CI surfaces for persistent review routing and gating ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:149), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:167), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:92), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:123)).

`[e:c:i]` Prior cross-model work also shows why the repo needs protocol discipline before it needs another skill: prompt drift, unpersisted first-pass prompts, runtime differences, and orchestrator non-blindness all weakened the independence claim in the 2026-04-08 pre-execution audit ([METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:24), [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:47), [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:59), [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:83), [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:118)).

## Work-type matrix
`[e:c+r:i]` The repo already rejects blanket use: cross-vendor audit is reserved for load-bearing review boundaries and explicitly not required for mechanical citation repair, routine readiness status updates, or other low-consequence cleanup ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:151), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:159)).

| Work type | Cross-vendor status | Why | Best current owner / layer |
| --- | --- | --- | --- |
| Governance-doc normalization | `Strongly preferred` when the audit or patch materially changes standing doctrine; otherwise `optional` ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:250), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:256)) | The risk is doctrinal drift, not mechanical correctness. External reread matters when the output will steer later governance behavior. | `Codex orchestration + Git boundary` |
| High-stakes harness / governance audits | `Necessary` when the output will steer harness ownership or readiness doctrine and an external lane is available ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:17), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:153)) | This is the exact class of artifact the current policy reserves stronger independent review for. | `Codex orchestration now; repo-local protocol later` |
| Canon-sensitive synthesis | `Strongly preferred` ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:21), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:153)) | Major synthesis artifacts can silently flatten open doctrine; external reread is useful adversarial pressure. | `Codex orchestration` |
| Rerun-readiness verification | `Strongly preferred` only when the verdict depends on doctrine-sensitive judgment; otherwise `optional` ([TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:35), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:347)) | Mechanical closure does not need vendor diversity; doctrinal gatekeeping often does. | `Codex orchestration after internal verification` |
| Doctrine-sensitive Phase 01 planning | `Strongly preferred` when ambiguity remains after internal review ([TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:36), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:373)) | This is the place where the repo already has a fit-for-purpose repo-local surface. | `Repo-local regular GSD via gsd-review` |
| Routine execution verification | `Counterproductive` by default; `optional` only if the work stops being routine ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:16), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:159)) | Extra external review here mostly adds ceremony and latency instead of signal. | `Execution/verification lane, later CI` |
| Stubborn debugging | `Strongly preferred` as an escalation lane, not as the default path ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:21)) | Once local debugging stalls, an independent model class is one of the highest-leverage ways to shake a blind spot loose. | `Codex orchestration with external lane` |

## Current surfaces and what they already cover
### Direct top-level orchestration
`[e:c:i]` The current repo already has a viable near-term owner for heterogeneous non-phase external rereads: root `AGENTS.md` keeps orchestration at the top level, requires explicit spawn classification, requires auditable baselines before substantial delegation, and requires explicit disposition after worker return ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:111), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:117), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:124), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:56)).

`[e:c+r:i]` This is already good enough for bounded governance rereads, rerun-readiness verdict rereads, and stubborn debugging escalations because those tasks are context-heavy and do not yet share one stable artifact contract.

### `gsd-review` in the repo's regular GSD / Codex-local stack
`[e:c:i]` `gsd-review` is a real repo-local mechanism, not just doctrine. It invokes external AI CLIs to review phase plans, gathers phase artifacts from the repo-local GSD phase structure, sends a structured review prompt, and writes a phase-local `*-REVIEWS.md` artifact ([.codex/skills/gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md:48), [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:70), [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:141), [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:188)).

`[e:c+r:i]` It already covers the `R5.4` use case well enough: doctrine-sensitive Phase plan peer review against external CLIs, with one prompt sent across reviewers and a synthesized review artifact returned to planning ([TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:36), [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:92)).

`[e:c+r:i]` Its limits are specific rather than fatal:
- phase-number input and phase-artifact gathering make it phase-plan-centric, not a general governance-audit surface ([.codex/skills/gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md:60), [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:73))
- the review rubric is generic plan review, not audit-classification or obligation-driven inquiry ([.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:117))
- the prompt is written to `/tmp`, not preserved as an in-repo audit artifact for later methodology review ([.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:138))
- it does not log runtime/confound metadata that later expert audit would want.

### `gsdr-audit` in the Reflect forked harness family
`[e:c:i]` `gsdr-audit` is useful precedent, not a current repo-local surface. It offers a broader audit orchestrator with explicit classification, obligation composition, copied task-spec rules, output-file discipline, and explicit cross-model dispatch hygiene ([/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:6), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:104), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:124), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:244)).

`[e:c:i]` It also makes clear why it should not be flattened into the repo's current regular stack. Its execution context reads Reflect-family references under `$HOME/.codex/get-shit-done-reflect`, and its `cross_model` path is still explicitly marked experimental with warning, log capture, output-file existence check, and known failure modes ([/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:14), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:258), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:307)).

`[e:c+r:i]` The right import posture is selective:
- good import candidates: audit classification language, copied task-spec obligations, dispatch-hygiene warnings, output/log checks
- bad import candidates: Reflect runtime paths, Reflect commit tooling, and the assumption that a dedicated cross-model audit dispatch surface is already reliable enough for the repo's regular stack.

### Standing doc-level policy
`[d:c:i]` The repo already has enough doctrine to justify selective use without adding a new mechanism first. Model policy prefers external audit for high-stakes review, the readiness plan names the exact readiness gates where external reread may matter, and workflow docs already define checkpoint-before-delegation and explicit review boundaries ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:17), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:151), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:350), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:45), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:47)).

`[e:c+r:i]` What policy does not yet give the repo is one concise operational contract for non-phase external rereads. The missing piece is consistency, not permission.

## Real gaps
### Missing guidance
`[e:c+r:i]` The current guidance is distributed across model policy, readiness sequencing, tasks, deferrals, and general governance docs. There is no single repo-local mapping of `work type -> trigger -> harness owner -> required metadata -> checkpoint sequence` ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:45), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:145), [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:30), [DEFERRED.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEFERRED.md:12)).

### Missing workflow integration
`[e:c+r:i]` The readiness package already knows where cross-vendor rereads may fire, but it still lacks a repeatable handoff rule for when to use direct orchestration versus `gsd-review`, and for whether the external pass happens before or after internal verification and fix integration ([TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:32), [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:35), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:256), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:379)).

### Missing mechanism
`[e:c+r:i]` The real mechanism gap is narrower than "missing audit skill." The repo lacks a reusable repo-local protocol for non-phase external rereads that preserves a prompt/task spec in-repo, records baseline commit and runtime metadata, keeps prompts materially comparable across vendors, records confounds, and separates findings from later fixes. The 2026-04-08 methodology review shows the cost of not having that protocol ([METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:26), [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:49), [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:69), [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:85), [METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:118)).

### Missing vendor / tool availability
`[a:c+r:i]` External review capacity is still conditional, not ambient. The current policy only projects a routine Sonnet/Opus ladder if Anthropic access becomes part of routine workflow, `gsd-review` only works when at least one different external CLI is installed, and `gsdr-audit` still treats cross-model dispatch as experimental ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:52), [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:13), [.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:63), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:258)).

## Near-term readiness recommendation
`[d:c:i]` Keep this lane as conditional follow-through, not as an active Checkpoint 0 blocker. The task spec, readiness tasks, and deferred list all treat integration work as conditional unless later evidence shows existing surfaces cannot carry the needed review modes cleanly ([01-cross-model-audit-integration-task-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-cross-model-audit-integration-research/01-cross-model-audit-integration-task-spec.md:10), [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:32), [DEFERRED.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/DEFERRED.md:12)).

`[e:c+r:i]` I do not find a stronger dependency than the repo currently believes. Checkpoint 0 still needs repair-and-review of the governance audit bundle, but it does not need a new audit mechanism before that work can proceed ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:178), [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:203)).

`[p:r:i]` Near-term readiness should use a split owner model:
- for non-phase doctrine-sensitive rereads tied to the multi-layer governance lane, use direct top-level orchestration after the target artifact is internally coherent
- for a fresh Phase 01 plan reread, use the existing repo-local `gsd-review` surface if `R5.4` actually trips
- do not import `gsdr-audit` as a runtime dependency during readiness work.

`[s:c+r:i]` If a near-term non-phase external reread is run before any repo-local patch exists, manually borrow only the Reflect-side protocol pieces that address known confounds:
- persist the prompt or task spec in-repo before the first pass
- keep vendor prompts materially comparable
- log model, runtime, working directory, and output path
- record confounds and reviewer non-blindness explicitly
- keep findings and later fixes as separate review boundaries ([METHODOLOGY-REVIEW.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/METHODOLOGY-REVIEW.md:41), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:277), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:307)).

## Longer-term project / harness recommendation
`[p:r:i+t]` The right long-term shape is hybrid and layered rather than singular:
- `Codex orchestration layer`: keep ownership of trigger judgment, vendor choice, and disposition for non-phase external rereads
- `repo-local regular GSD layer`: keep ownership of repeatable phase-plan external review now, and likely own any later repo-local generalized review protocol
- `Git / repo boundary layer`: own baseline commits, isolated review artifacts, and attribution boundaries
- `remote review / CI layer`: later own persistent review-routing surfaces such as issue / PR templates, review-owner routing, and merge/deploy gates once those boundaries are real ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:167), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:92), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:123)).

`[p:c+r:i]` If the repo does more than doctrine-plus-orchestration, the next mechanism should be a repo-local reusable task-spec / protocol pattern for non-phase external rereads, not a direct Reflect import and not an immediate dedicated skill. That protocol should live in the repo's regular stack and encode:
- target artifact set
- baseline commit or explicit clean-snapshot statement
- prompt/task-spec path persisted in the repo
- reviewer/vendor/runtime table
- confound log
- output artifact paths
- disposition and integration note.

`[p:c+r:i]` The correct Reflect import policy is selective porting, not wholesale adoption. `gsdr-audit` contributes useful pattern precedent, but the repo should only port the parts that survive contact with the regular stack:
- importable: classification header, obligation/task-spec copying for high-stakes audits, dispatch-hygiene checks, output existence checks
- not importable as-is: Reflect reference paths, Reflect commit tooling, and the assumption that cross-model dispatch is already dependable enough to become a standing repo-local surface.

## Decision on dedicated cross-model-audit skill
`[d:c+r:i]` Do not create a dedicated cross-model-audit skill now.

`[e:c+r:i]` The reasons are specific:
- `gsd-review` already covers one real repeated class of work in the repo's actual stack: phase-plan peer review
- non-phase high-stakes rereads are still heterogeneous and better owned by top-level orchestration plus Git review boundaries
- the real missing piece is methodology and attribution discipline, not invocation syntax
- `gsdr-audit` proves that a richer audit harness is possible, but it also proves that direct import would currently blur the regular-stack / Reflect-stack distinction and pull in an experimental cross-model path as if it were settled ([.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:70), [/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:258)).

`[o:r:i]` A dedicated repo-local skill becomes worth reconsidering only if all of the following become true:
- cross-vendor rereads become routine across more than one non-phase artifact family
- vendor availability becomes ordinary rather than opportunistic
- a repo-local protocol has stabilized enough that the common fields are obvious
- manual orchestration continues to create repeatable failures even after the protocol exists.

## Recommended next actions
1. `Codex orchestration layer`: for the next doctrine-sensitive non-phase external reread, use direct top-level orchestration and persist a repo-local prompt/task spec before the first pass.
2. `repo-local regular GSD layer`: keep `gsd-review` as the default surface for `R5.4`-style Phase 01 plan rereads; do not repurpose `gsdr-audit` directly into readiness work.
3. `repo-local regular GSD layer`: after Checkpoints 1-2 settle, draft a small repo-local non-phase external-reread protocol or template rather than a new skill. The goal is auditable repeatability, not new CLI ceremony.
4. `Reflect import policy`: when that protocol is drafted, port only the proven `gsdr-audit` ideas that solve real gaps: classification framing, copied task-spec obligations when needed, dispatch warnings, and output/log checks.
5. `Git / repo boundary layer`: require, where meaningful, three explicit boundaries for non-phase external rereads: pre-review baseline, findings artifact, and post-fix integration. If the artifact is too unstable for a checkpoint commit, split or park it first rather than forcing a bad baseline ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:49), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:47)).
6. `remote review / CI layer`: once real PR flow or a runnable app exists, add persistent remote surfaces for requesting and recording external rereads, such as issue / PR templates and review routing, instead of keeping the whole practice chat-local ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:85), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:140)).
7. `vendor-availability discipline`: when no independent external lane is available, record that explicitly in the artifact and fall back to same-model reread only as a weaker substitute, not as if it provided the same independence ([02-model-assignment-policy-response.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/02-model-assignment-policy-response.md:17), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:78)).

## How this plugs back into the multi-layer harness audit
`[e:c+r:i+t]` This research reinforces, rather than revises, the main multi-layer governance conclusion: the immediate problem is missing ownership transfer between layers, so cross-vendor audit should be treated as a handoff contract across layers rather than as a free-floating universal harness ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:149), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:231), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:150)).

| Harness layer | Role for cross-vendor audit | Current surface | Follow-through from this research |
| --- | --- | --- | --- |
| `Codex orchestration` | Decide whether a non-phase artifact needs independent reread, choose vendor lane, and disposition results | top-level orchestration rules in [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:111) | Keep as the near-term owner for governance, synthesis, readiness, and stubborn-debug rereads |
| `Repo-local regular GSD` | Carry repeatable external review where the artifact family is stable | `gsd-review` for phase plans ([.codex/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:70)) | Keep using `gsd-review` for plan review; later add a repo-local non-phase protocol or patch only if repetition justifies it |
| `Git / repo boundary` | Materialize baselines, isolate reviewable units, preserve attribution for later audit | checkpoint doctrine in [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:45) | Make prompt, findings, and integration boundaries explicit so later expert audit can reconstruct what happened |
| `Remote review / CI` | Persist review routing and enforce mechanical checks once real PR/runtime surfaces exist | currently thin by design ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:142)) | Defer until real code / PR / deploy boundaries exist; then add templates, routing, and merge/deploy gates |
| `Reflect forked harness` | Provide pattern precedent, not current ownership | `gsdr-audit` ([/home/rookslog/.codex/skills/gsdr-audit/SKILL.md](/home/rookslog/.codex/skills/gsdr-audit/SKILL.md:6)) | Import selectively into the regular stack only where the pattern closes a real repo-local gap |

`[e:c+r:i+t]` In that sense, this artifact is a direct extension of the multi-layer harness governance audit: it sharpens one specific handoff seam, keeps the regular-stack / Reflect-stack distinction explicit, and argues for staged import into the repo's actual harness layers rather than a premature all-in-one audit surface.
