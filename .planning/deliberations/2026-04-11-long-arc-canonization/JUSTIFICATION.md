---
deliberation: 2026-04-11-long-arc-canon-and-harness-justification
created: 2026-04-11T04:43:28-04:00
status: complete
type: justification-sidecar
scope: Explain and justify the proposed long-arc canonization and harness-integration changes, with traceability back to canon, audits, research lanes, exploration notes, and prior harness-patch reasoning.
related_documents:
  - PLAN.md
  - ../../PROJECT.md
  - ../../ROADMAP.md
  - ../../REQUIREMENTS.md
  - ../../STATE.md
  - ../../audits/2026-04-08-pre-execution-review/SYNTHESIS.md
  - ../../audits/2026-04-08-pre-execution-review/CONVERGENCE.md
  - ../../audits/2026-04-08-pre-execution-review/lane-4-multi-milestone-vision.md
  - ../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md
  - ../../explore/2026-04-10-vision-future-hosting/SESSION.md
  - ../../explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md
  - ../2026-04-10-future-awareness-harness-patch.md
---

# Long-Arc Canon And Harness Integration Justification

## Why This Exists

The paired plan proposes real canon and tooling changes.

Those changes should not rely on conversational memory alone. This sidecar exists to:

- show the evidence base behind each proposed change
- explain why the proposed patch is narrow instead of broad
- preserve rejected alternatives for later diagnosis
- provide a review artifact if the resulting planning behavior still drifts

## Core Diagnosis

The repo does not have a shortage of long-range thinking.

It has a shortage of:

- one ratified doctrine document
- one obvious place to look for the mature-product and transition thesis
- one reliable way for that thesis to enter phase steering without depending on a human remembering which research wave mattered

In other words:

- the strategic thinking exists
- parts of it are already canonized
- but the transmission path is still too implicit

## The Evidence Base

## 1. Current Canon Already Wants Future-Aware Planning

`PROJECT.md` already carries a `Milestone Arc` and a `How The Long Arc Constrains v1` section.

`ROADMAP.md` already carries per-phase:

- `Canonical refs`
- `Protects`
- `Does not decide yet`
- `Assumed posture`

`REQUIREMENTS.md` already carries:

- v1 requirements
- v2 requirements
- `Protected Seams`
- `Explicit Deferrals`

This matters because the proposed change is not introducing future-awareness from scratch. It is formalizing and centralizing a posture that canon already wants to express.

## 1.5. This Repo Uses A Local Exploratory Discuss Posture

This repo should not be treated as vanilla upstream GSD behavior.

Evidence:

- `.planning/config.json` sets `workflow.discuss_mode` to `exploratory`
- `AGENTS.md` explicitly says the project uses `workflow.discuss_mode: exploratory`
- the repo-local overlay planning-config reference documents `exploratory`, `discuss`, and `assumptions`
- the base `.codex` reference still shows older discuss-mode language

Why this matters:

- the long-arc doctrine patch must target the repo-local harness reality, not generic upstream defaults
- any plan that assumes only the standard discuss path is active is under-scoped for this repo

## 2. The Exploration Session Explicitly Identified The Same Gap

The future-hosting exploration log repeatedly converged on:

- authored substrate plus wrappers as the right frame
- visibility-state as a better concept than simple private/public
- support/access/service obligation as distinct
- the need to encode future-awareness into planning artifacts and harness behavior rather than leaving it ambient

Relevant artifacts:

- `.planning/explore/2026-04-10-vision-future-hosting/SESSION.md`
- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md`
- `.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md`
- `.planning/explore/2026-04-10-vision-future-hosting/07-public-transition-clean-room-comparison.md`
- `.planning/explore/2026-04-10-vision-future-hosting/06-high-vs-xhigh-comparison.md`

The most direct steering note is the reflections doc, which explicitly says:

- do not pour the research wholesale into `REQUIREMENTS.md`
- `PROJECT.md` should carry the long-arc thesis
- `ROADMAP.md` should carry what each stage proves and protects
- `CONTEXT.md` should remain the active steering layer
- future-awareness should be encoded into workflow machinery

That combination is the direct foundation for the current plan.

## 3. The Research Wave Sharpened Product Doctrine, Not Just Nice-To-Have Ideas

The 2026-04-10 research wave did not merely add optional future brainstorming. It reframed several questions at the doctrine level.

### Product Futures / Wrappers

From:

- `.planning/research/2026-04-10-vision-hosting-wave/findings/01-product-futures.md`

Takeaways:

- the mature space is better understood as multiple wrappers around one authored substrate
- the first strong proof is still the watchable private game-night shell
- later solo, async, streamer, and sibling-mode surfaces remain plausible but not equally imminent

This supports creating one strategy doc that names the likely family shape without forcing all wrappers into the current milestone.

### Hosting / Scaling / P2P

From:

- `.planning/research/2026-04-10-second-wave-scaling-governance/findings/01-cooperative-scaling-and-p2p-feasibility.md`

Takeaways:

- full peer-to-peer room authority is the wrong branch to optimize around
- self-hostable authoritative rooms are the main branch worth protecting
- cooperative scaling is more about operator/community hosting and packaging than browser swarm magic

This supports encoding a hosting-and-scaling ladder into the long-arc doctrine rather than leaving “P2P maybe?” as ambient lore.

### Funding / Access / Support

From:

- `.planning/research/2026-04-10-second-wave-scaling-governance/findings/02-funding-access-and-transparency-models.md`

Takeaways:

- do not collapse support, access, and service obligation into one thing
- optional support is stage-compatible
- paid guaranteed access belongs to a later, more mature operating posture

This supports making support/access doctrine explicit in a long-arc doc while keeping it out of present-tense requirements unless something becomes a real promise.

### Public Transition / Discovery

From:

- `.planning/research/2026-04-10-second-wave-scaling-governance/findings/03-public-transition-and-discovery.md`
- `.planning/explore/2026-04-10-vision-future-hosting/07-public-transition-clean-room-comparison.md`

Takeaways:

- public transition is a surface-layering and visibility-state problem
- wrapper choice affects discovery doctrine
- public read, async challenge, spectator, and live participation are different openings with different obligations

This supports creating a single explicit visibility/discovery ladder instead of letting each later phase reinterpret “publicness” from scratch.

### Security / Trust / Operational Risk

From:

- `.planning/research/2026-04-10-second-wave-scaling-governance/findings/04-security-trust-and-operational-risk.md`

Takeaways:

- scope restraint is itself a trust strategy
- the first trust failures are likely admission, reconnect, log hygiene, unclear room status, and underpowered moderation when widened
- publicness is as much an obligation threshold as a scale threshold

This supports using the long-arc doc to define publicness and trust posture explicitly, not implicitly.

## 4. The Older Audit Still Matters, But Not As The Only Canon

`lane-4-multi-milestone-vision.md` remains important because it:

- articulated the three-milestone arc
- identified cheap compounding investments
- highlighted missing v2 requirement surfaces

But it is not the best single current top-level read anymore.

Why:

- later research sharpened visibility-state, trust-boundary, and support/access distinctions
- some lane-4 content is now partly canonized already
- some lane-4 content remains useful as pressure rather than as direct canon text

This is why the plan proposes a new long-arc doc instead of simply declaring lane 4 canonical.

## 5. Newly Surfaced Harness Coverage Gaps

During plan hardening, two additional workflow surfaces proved too important to leave implicit:

### `quick --discuss`

The live quick workflow supports `--discuss`, writes a quick `CONTEXT.md`, and then feeds that context into quick research and quick planning.

That makes it a real doctrine-transmission surface, not an optional side alley.

### `discuss-phase-assumptions`

Even though the current config is `exploratory`, assumptions mode is a real local workflow path and another `CONTEXT.md` producer.

Leaving it uncovered would mean the plan knowingly preserved a harness gap for later mode changes.

### Why The Plan Now Includes Them

The goal of the current pass is not only to write a doctrine doc. It is to improve doctrine transmission through the repo-local planning machinery.

Once that is the goal, omitting active or latent local context-producing surfaces becomes a real scope gap rather than a nice-to-have cleanup item.

## Why Each Planned Change Exists

## Change Set A: Create `.planning/LONG-ARC.md`

### Why

Because the repo currently lacks one ratified artifact that answers:

- what mature product family we actually think is plausible
- which transition path we are protecting
- what visibility/publicness ladder we believe in
- what support and service promises we are explicitly not making yet

### Why Not Just Expand `PROJECT.md`

Because the reflections doc explicitly warned against pouring all long-arc material into the main canon docs, and because `PROJECT.md` should stay readable as the short project identity.

### Why Not Treat Research Lanes As Canon

Because the exploration notes explicitly distinguish between:

- insightful research artifacts
- canonical product law

The plan therefore introduces a canonized synthesis layer between them.

## Change Set B: Add A Pointer In `PROJECT.md`

### Why

Because `PROJECT.md` is the first canonical read in multiple workflows and reread stacks. If the long-arc doctrine becomes real canon, `PROJECT.md` should tell readers where it lives.

### Why Only A Pointer

Because `PROJECT.md` already contains the short milestone arc and should remain concise.

This matches the current repo pattern:

- `PROJECT.md` is the identity document
- more detailed reasoning can live in dedicated artifacts

## Change Set C: Wire `.planning/LONG-ARC.md` Into `ROADMAP.md`

### Why

Because the current harness uses `ROADMAP.md` phase refs as the first source of `canonical_refs` during discuss-phase.

That is a key implementation detail already present in:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`

If the strategy doc is not cited from the roadmap, discuss-phase may still miss it unless a human adds it manually.

### Why Across All Eight Phases

Because the long-arc doctrine influences all phases in different ways:

- early phases preserve substrate and room seams
- middle phases preserve join/share/watchability doctrine
- later phases preserve calibration, content operations, and trust/durability posture

So the plan intentionally treats the doctrine as milestone-wide, not only early-phase architecture garnish.

## Change Set D: Update `REQUIREMENTS.md` Sparingly

### Why

Because some strategy conclusions do belong in requirements form, but only as:

- a protected seam
- an explicit deferral
- a concrete current-stage obligation

### Why Sparingly

Because the reflections note explicitly said the research should not be poured wholesale into `REQUIREMENTS.md`.

This is also consistent with the earlier harness-patch doctrine:

- preserve future-awareness
- do not inflate speculative futures into requirements

## Change Set E: Patch `discuss-phase`, Not The Whole Harness

### Why

The repo-local harness already has a strong downstream path once `CONTEXT.md` is good:

- discuss builds `canonical_refs`
- research consumes them
- planning consumes them
- plan artifacts preserve future-aware items

That means the weakest point is now the steering-stage load path, not the downstream consumers.

### Why `discuss-phase` Specifically

Current guidance still summarizes prior context too narrowly as:

- `PROJECT.md`
- `REQUIREMENTS.md`
- `STATE.md`
- prior `CONTEXT.md`

Even though the workflow already derives future awareness from `ROADMAP.md` and user-referenced docs.

The proposed patch closes that gap by making the long-arc doc visible at the first steering read.

### Why Not Patch `plan-phase` And `research-phase` Too

Because the current repo-local versions already do the important thing:

- resolve `canonical_refs`
- treat them as mandatory downstream reads

Changing them before proving a real gap would be redundant churn.

## Change Set F: Keep Diagnostics First-Class

### Why

The repo already has a process lesson around planning artifacts drifting from actual workflow behavior.

Relevant artifacts:

- `2026-04-10-future-awareness-harness-patch.md`
- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md`
- `AGENTS.md` notes about not mistaking improvised artifacts for validated planning flow

That makes it important that this plan include:

- explicit verification
- explicit failure inspection order
- explicit dry-run checks

If propagation fails later, we should be able to tell whether the problem was:

- bad doctrine
- bad roadmap refs
- discuss-phase omission
- context-generation omission
- planner omission

## Traceability Matrix

| Planned change | Main supporting sources | Why they matter |
|---|---|---|
| Create `.planning/LONG-ARC.md` | `08-reflections-on-research-implications...`, `SESSION.md`, `lane-4-multi-milestone-vision.md`, `01-product-futures.md` | These establish both the need for a long-arc synthesis layer and the likely family shape it should express. |
| Pointer from `PROJECT.md` | `08-reflections-on-research-implications...`, `PROJECT.md` | Reflection says `PROJECT.md` should carry the long-arc thesis, but the doc should stay concise. A pointer is the clean reconciliation. |
| Add strategy doc to `ROADMAP.md` phase refs | `ROADMAP.md`, `discuss-phase.md`, `plan-phase.md` | The harness derives `canonical_refs` from roadmap phase refs, so roadmap citation is the most reliable canon-to-context path. |
| Only selective `REQUIREMENTS.md` edits | `08-reflections-on-research-implications...`, `REQUIREMENTS.md`, `02-funding-access-and-transparency-models.md`, `03-public-transition-and-discovery.md` | These sources support preserving seams and deferrals without turning every future into a hard requirement. |
| Patch `discuss-phase` only | `2026-04-10-future-awareness-harness-patch.md`, current overlay `discuss-phase.md`, current overlay `research-phase.md`, current overlay `plan-phase.md` | Existing downstream enforcement is already decent; steering-stage loading is the smaller, higher-leverage patch point. |
| Add diagnostics and dry-run gate | `2026-04-10-future-awareness-harness-patch.md`, `CHECKPOINT.md`, `AGENTS.md` | The repo already has explicit lessons about transmission failures and artifact drift, so the new doctrine should land with an audit path. |

## Rejected Alternatives

## Rejected: Put Everything In `PROJECT.md`

Reason:

- too much doctrinal material for the identity document
- increases canon density without improving harness propagation
- contradicts the repo’s own reflections about not flattening all research into one canon file

## Rejected: Treat `lane-4-multi-milestone-vision.md` As The Canonical Long-Arc Doc

Reason:

- it is still valuable, but it predates the later visibility-state, public-transition, trust, and support/access refinements
- it is an audit lane, not a ratified doctrine document
- it mixes enduring structure with older framing that later work sharpened

## Rejected: Patch The Entire Harness Prompt Chain Immediately

Reason:

- current downstream `canonical_refs` behavior is already much better than the steering-stage load path
- broad patching would create more moving pieces before proving a real need
- this plan favors minimum-necessary behavior change

## Rejected: Leave Everything As-Is And Rely On Better Human Memory

Reason:

- that is exactly the failure mode the earlier future-awareness patch was trying to reduce
- the repo now has enough strategic material that oral memory is a bad transmission mechanism

## Rejected: Convert Public Growth, Monetization, Or Contribution Models Into Current Requirements

Reason:

- the research explicitly argues for separating support from guaranteed access
- publicness is staged and surface-specific
- several future models remain deliberately unchosen
- elevating them prematurely would distort current milestone planning

## What To Watch During Implementation

If the implementation based on the paired plan goes wrong, the most likely failure classes are:

### 1. Doctrine Bloat

Symptoms:

- `.planning/LONG-ARC.md` reads like a second roadmap plus a product brainstorm notebook
- discuss outputs become overly verbose without becoming more decisive

Diagnosis:

- the long-arc doc is trying to do research and canon at the same time

### 2. Canon Drift

Symptoms:

- `PROJECT.md`, `ROADMAP.md`, and `LONG-ARC.md` disagree on current posture
- `REQUIREMENTS.md` says more or less than the strategy doc implies

Diagnosis:

- doctrine was added without reconciling surrounding canon carefully enough

### 3. Harness Non-Propagation

Symptoms:

- `LONG-ARC.md` exists but generated `CONTEXT.md` files do not cite it
- future-awareness sections remain generic and unmoored

Diagnosis:

- discuss-phase load path or canonical-ref generation still omits the document

### 4. Over-Patching

Symptoms:

- multiple workflow files changed, but behavior did not improve materially
- debugging becomes harder because too many prompt surfaces changed at once

Diagnosis:

- patch scope exceeded the real gap

## Final Recommendation

Proceed with the paired plan.

The repo has already done the hard conceptual work. The missing step is not another broad future discussion. It is to:

1. ratify the doctrine in one stable place
2. wire that doctrine into canon and steering
3. verify that Phase 1 replanning will actually consume it

That is the smallest change that meaningfully improves long-arc transmission without reopening the whole roadmap.
