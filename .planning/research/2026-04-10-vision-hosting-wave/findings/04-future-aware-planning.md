# Future-Aware Planning And Workflow Design

Date: 2026-04-10
Lane: 04-future-aware-planning

## Question Space

This lane asks how Prix Guesser should keep near-term planning aware of its longer arc without turning every phase into speculative architecture work.

More concretely:

- How should future-facing information move from `PROJECT.md` to `ROADMAP.md` to `CONTEXT.md` to `PLAN.md`?
- Where is the current harness already preserving option value well?
- Where does the harness currently compress or drop that information?
- Which additions are cheap and useful, and which would mostly create ceremony?

## Method And Sources

- Primary method: local artifact analysis of the current repo-local GSD harness and current Prix Guesser planning state. No external sources were needed because the core question is about this repository's actual workflow behavior, not general PM theory.
- Primary high-authority sources: `AGENTS.md`, `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/config.json`, `.planning/phases/01-authored-round-contract/01-CONTEXT.md`, current Phase 1 plans, and repo-local workflow/template files under `.codex/get-shit-done/`.
- Secondary medium-authority source: `.planning/phases/01-authored-round-contract/.continue-here.md`. It is useful because it records the exact strategic tension that triggered the pause, but it is still a handoff artifact and explicitly notes that related audit work is uncommitted, so it should not be treated as canonical product state by itself (`.planning/phases/01-authored-round-contract/.continue-here.md:42-61`).
- Reliability limit: the strongest positive example of future-aware context today appears in the actual Phase 1 context file, but the base template does not require those sections. That means some current strengths are repo-practice strengths, not yet harness-guaranteed strengths (`.planning/phases/01-authored-round-contract/01-CONTEXT.md:60-151`; `.codex/get-shit-done/templates/context.md:23-96`).

## Findings

### Current Strengths In The Existing Harness

- [CONFIRMED] Future-orientation already exists at the product level. `PROJECT.md` explicitly preserves three tensions, keeps major architecture choices open, and maintains an `Open Questions` table that is clearly about cross-milestone uncertainty rather than immediate implementation detail (`.planning/PROJECT.md:36-49`, `.planning/PROJECT.md:69-75`, `.planning/PROJECT.md:88-98`).

- [CONFIRMED] The roadmap already carries some non-foreclosure logic. It states that v1 should prove one anchor mode without drifting into premature party-platform breadth, keeps room-runtime choice open, keeps finer answer surfaces out of scope unless later evidence justifies them, and says the content model should still support adjacent F1 party modes later (`.planning/ROADMAP.md:5-11`, `.planning/ROADMAP.md:59-70`).

- [CONFIRMED] Repo policy explicitly says downstream agents should treat `CONTEXT.md` as a steering brief that includes future awareness, and it warns against prematurely locking open design questions preserved in discovery (`AGENTS.md:44-49`).

- [CONFIRMED] The repo is already configured for exploratory context capture rather than narrow requirement extraction. `workflow.discuss_mode` is set to `"exploratory"` in project config (`.planning/config.json:15-31`).

- [CONFIRMED] The current Phase 1 context file is a strong proof-of-concept for future-aware phase steering. It includes `Open Questions`, `Epistemic Guardrails`, `Canonical References`, and a dedicated `Future Awareness` section that names later phases affected, what must stay extensible, and what runtime decisions must remain open (`.planning/phases/01-authored-round-contract/01-CONTEXT.md:60-151`).

- [INFERRED] The best existing pattern is not "more planning"; it is "phase-local future guardrails." Phase 1's current context does not try to design future phases in detail. Instead it preserves a few high-value constraints like transport-agnostic contracts, later calibration needs, and delayed room-runtime choice. That is the right granularity for future-aware planning (`.planning/phases/01-authored-round-contract/01-CONTEXT.md:51-56`, `.planning/phases/01-authored-round-contract/01-CONTEXT.md:137-141`).

- [CONFIRMED] Some Phase 1 plans already encode future protection implicitly. Examples include reserving extensible answer targets while keeping v1 limited to `circuit` and `venue`, keeping the content toolchain transport-agnostic, and making fallback posture explicit in data rather than hidden in author judgment (`.planning/phases/01-authored-round-contract/01-01-PLAN.md:64-69`, `.planning/phases/01-authored-round-contract/01-01-PLAN.md:113-126`, `.planning/phases/01-authored-round-contract/01-03-PLAN.md:20-23`, `.planning/phases/01-authored-round-contract/01-03-PLAN.md:98-112`).

### Current Blind Spots

- [CONFIRMED] The base phase-context template does not require `Open Questions`, `Assumptions`, `Epistemic Guardrails`, or `Future Awareness`. It ends at `Deferred Ideas`, which means the strongest future-aware behavior in the current Phase 1 context is not yet template-enforced (`.codex/get-shit-done/templates/context.md:23-96`).

- [CONFIRMED] The discuss-phase workflow is strong on no-scope-creep discipline, but its framing is still mostly phase-bounded: it says the job is to capture implementation decisions for the current phase and to avoid adding new capabilities beyond roadmap scope (`.codex/get-shit-done/workflows/discuss-phase.md:1-5`, `.codex/get-shit-done/workflows/discuss-phase.md:47-73`). That is useful, but by itself it does not guarantee a place to record "what this phase must not foreclose."

- [CONFIRMED] The plan-phase workflow warns that planning without context loses design preferences, but it does not explicitly warn that planning without future-aware context can harden accidental architecture decisions (`.codex/get-shit-done/workflows/plan-phase.md:202-240`).

- [CONFIRMED] There is no separate milestone artifact in `.planning/` right now. The current harness is effectively project-level plus roadmap-level plus phase-level, so a recommendation like "each milestone should have a `future protected` section" currently has no obvious home except `ROADMAP.md` or a newly introduced milestone document. Local scan on 2026-04-10 found no milestone files under `.planning/`.

- [INFERRED] The main information-loss point is the transition from rich steering context to executable plans. The Phase 1 context explicitly names later dependencies and preserved options, but the plans mostly translate those into immediate deliverables, tests, and outputs. Some non-foreclosure logic survives, but mostly as embedded phrasing inside task actions instead of as an auditable field (`.planning/phases/01-authored-round-contract/01-CONTEXT.md:134-151`; `.planning/phases/01-authored-round-contract/01-01-PLAN.md:89-166`; `.planning/phases/01-authored-round-contract/01-03-PLAN.md:76-150`).

- [CONFIRMED] The handoff documents a concrete version of this problem: product docs preserve a broader platform trajectory while current plans optimize mostly for the deep-anchor-mode path. The handoff is careful to treat that as an open identity decision, not a settled fact (`.planning/phases/01-authored-round-contract/.continue-here.md:65-87`). This is exactly the kind of cross-milestone tension that should be promoted into canonical planning artifacts instead of living primarily in a pause memo.

### Low-Drag Improvements

- [INFERRED] Make `Future Awareness` a mandatory phase-context section in the template, not a nice-to-have overlay. Recommended subfields:
  - `Later phases this phase feeds`
  - `What this phase must not foreclose`
  - `Which decisions stay intentionally open after this phase`
  This is the single highest-leverage improvement because the current Phase 1 context already proves the pattern works (`.planning/phases/01-authored-round-contract/01-CONTEXT.md:134-151`; `.codex/get-shit-done/templates/context.md:23-96`).

- [INFERRED] Add a concise `Protects` or `Must Preserve` field to each roadmap phase entry. Keep it to 1-3 bullets. Example shape:
  - `Protects: future richer answer targets`
  - `Protects: room-runtime choice remains open until reconnect guarantees are clearer`
  - `Does not decide: adjacent non-anchor modes`
  This fits the current roadmap style better than inventing a whole new milestone document immediately (`.planning/ROADMAP.md:7-11`, `.planning/ROADMAP.md:31-111`).

- [INFERRED] Add a plan-level `Non-Foreclosure Checks` section near the top of each PLAN. This should be short and concrete, not visionary prose. Example:
  - "Keep interface transport-agnostic"
  - "Reserve extensible answer-target shapes without shipping them in v1"
  - "Do not hardcode UI flow to anchor mode if Phase 5+ will need a reusable session shell"
  The planner/checker can then verify that each plan either carries one or more such checks or explicitly says `None for this plan`.

- [INFERRED] Treat major future-shaping tensions as canonical only when they are promoted back into `PROJECT.md`, `ROADMAP.md`, or the active phase `CONTEXT.md`. Handoffs and audit docs are useful discovery surfaces, but they should not be the primary place where identity-shaping constraints live (`.planning/phases/01-authored-round-contract/.continue-here.md:55-61`, `.planning/PROJECT.md:100-115`).

- [INFERRED] Keep `AGENTS.md` responsible for enduring repo posture and orchestration policy, not detailed per-phase future protections. It is the right place for rules like "keep open design questions open" and "treat context as a steering brief," but not the right place to store the actual protected future of Phase 3 versus Phase 5 (`AGENTS.md:42-49`, `AGENTS.md:58-83`).

### High-Drag Ideas That Are Probably Not Worth It Yet

- [INFERRED] Do not introduce a mandatory standalone milestone document right now. There is no milestone artifact layer today, and the current project is still in early architecture-setting work. A new document type would likely create more synchronization burden than value until roadmap/phase schema is stable.

- [INFERRED] Do not require every plan task to include a multi-milestone scenario analysis. Most tasks do not deserve that much ceremony. The correct level is plan-level guardrails, not task-level future essays.

- [INFERRED] Do not add blocking hooks that fail planning whenever a future-facing section is missing everywhere. That kind of automation is likely to create cargo-cult filler before the minimal schema is stable.

- [INFERRED] Do not turn every deferred idea into an architecture obligation. The current `Deferred Ideas` mechanism is valuable precisely because it keeps future possibilities visible without forcing immediate abstraction (`.codex/get-shit-done/workflows/discuss-phase.md:64-72`; `.planning/phases/01-authored-round-contract/01-CONTEXT.md:145-151`).

- [HYPOTHESIS] A future "milestone foresight review" might become worthwhile once there are multiple milestones with shipped artifacts and real evidence from playtests. It is probably premature before v1's core loop exists.

### A Minimal Future-Aware Planning Schema

Recommended minimal schema, using existing artifact layers:

| Artifact | What It Should Carry | Why It Belongs There |
|---|---|---|
| `PROJECT.md` | Product tensions, identity question, long-arc trajectories, open questions, evolution triggers | This is the canonical cross-milestone posture document already (`.planning/PROJECT.md:36-49`, `.planning/PROJECT.md:88-115`). |
| `ROADMAP.md` | Phase goal, success criteria, dependencies, plus a short `Protects` or `Does Not Decide Yet` field per phase | This is where sequencing and cross-phase intent meet. It is the lightest current home for milestone-like protection without adding a new artifact type. |
| `CONTEXT.md` | Locked decisions, discretion, open questions, epistemic guardrails, future awareness, deferred ideas | This is the best artifact for phase-specific non-foreclosure logic because it sits between product posture and plan execution (`AGENTS.md:47-49`; `.planning/phases/01-authored-round-contract/01-CONTEXT.md:60-151`). |
| `PLAN.md` | Concrete execution plus a short `Non-Foreclosure Checks` section | This is where future protection becomes testable behavior rather than intent. |
| `AGENTS.md` | Repo posture, orchestration rules, persistent workflow constraints | This should remain policy-level, not phase-detail-level (`AGENTS.md:42-83`). |

Recommended minimal field pattern:

```markdown
## Future Awareness

### Later phases this phase feeds
- Phase X because ...

### What this phase must not foreclose
- Keep Y open

### Still intentionally open after this phase
- Z remains undecided until ...
```

Recommended plan add-on:

```markdown
## Non-Foreclosure Checks

- Preserve: structured answer-target hierarchy even if only `circuit` and `venue` ship now
- Preserve: transport-agnostic room/domain boundaries
- Preserve: host-screen/session shell that can later support adjacent modes
```

## Viable Paths

### Path A: Template Reinforcement Only

- [INFERRED] Standardize the already-good repo practice by updating `CONTEXT.md` and planning templates to require future-awareness fields.
- [INFERRED] Add a short `Protects` field to roadmap phase entries.
- [INFERRED] Add a short `Non-Foreclosure Checks` field to plans and optionally a checker pass that asks whether it is present.
- [INFERRED] This is the recommended path. It captures the long arc with minimal extra process and aligns with how the repo is already behaving at its best.

### Path B: Add A Milestone Layer Later

- [HYPOTHESIS] If the roadmap grows beyond one milestone and future platform questions start spanning many phases, introduce a milestone artifact with:
  - `Future Protected`
  - `Will Not Decide In This Milestone`
  - `Promotion Triggers For Later Work`
- [INFERRED] This is a later move, not an immediate one, because no milestone layer exists today and the current bottleneck is loss between context and plans, not absence of a milestone document.

### Path C: Heavy Governance

- [INFERRED] Formal foresight reviews, mandatory future matrices, or blocking automation could make the process look sophisticated while mostly generating filler.
- [INFERRED] This path is not recommended yet.

## Key Tradeoffs And Hidden Assumptions

- [INFERRED] The central tradeoff is between preserving option value and preserving execution speed. The right answer is not "model the whole future now"; it is "name the few future decisions this phase must avoid collapsing."

- [INFERRED] This recommendation assumes the most expensive foreclosures in this project are architectural boundaries, not low-level implementation choices. Current docs support that assumption by repeatedly naming the round/content model and room authority model as the highest-leverage early decisions (`AGENTS.md:60-63`; `.planning/PROJECT.md:74-75`).

- [INFERRED] This approach also assumes that future-awareness is most valuable when attached to active phase context, because that is the last artifact planners and executors reliably read before turning intent into tasks. Current repo policy supports that assumption (`AGENTS.md:47-49`).

- [HYPOTHESIS] If the project later accumulates many active contributors or parallel workstreams, the lightweight schema proposed here may stop being enough. At that point stronger milestone or ADR discipline may become justified.

## Disconfirming Or Tensioning Evidence

- [CONFIRMED] The existing discuss-phase scope guardrail is doing important work. It prevents accidental capability creep and forces new ideas into `Deferred Ideas` rather than silently expanding the active phase (`.codex/get-shit-done/workflows/discuss-phase.md:47-73`). That means any future-aware addition must not weaken scope discipline.

- [CONFIRMED] Some future-awareness is already encoded in current plans without a dedicated section. For example, Phase 1 plans preserve extensibility and transport-agnostic boundaries inside concrete task language (`.planning/phases/01-authored-round-contract/01-01-PLAN.md:113-126`; `.planning/phases/01-authored-round-contract/01-03-PLAN.md:98-112`). This weakens any claim that the harness is currently "future-blind."

- [CONFIRMED] `PROJECT.md` explicitly says the project should keep decision context explicit without prematurely locking open product questions (`.planning/PROJECT.md:69-75`). So the repo's underlying philosophy is already correct. The problem is consistency of translation, not conceptual absence.

- [INFERRED] Because the repo is still pre-execution in Phase 1, some apparent blind spots may reflect healthy intentional incompleteness rather than workflow failure. A heavier future-planning schema could overreact to an early-stage condition.

## What Could Change This View

- Evidence from later phases showing that current plans reliably preserve future options without any additional schema. If that happens, the recommended changes may be unnecessary.

- A decision to explicitly commit to Identity A for the foreseeable future: "one deep anchor mode first, and broader party-mode ambitions are only aspirational." If the user makes that call clearly, some of the proposed future-protection surface can shrink.

- The creation of a real milestone artifact layer. If milestone docs become canonical, then some recommendations now aimed at `ROADMAP.md` should move there instead.

- Multiple future-aware planning failures in execution, especially cases where an executor followed the plan correctly but still foreclosed an intended later trajectory. That would justify stronger checker or schema enforcement than I recommend here.

## Open Questions Worth A Second Pass

1. [CONFIRMED] The identity question is still open: is v1 mainly "one deep anchor mode" or "the first wrapper inside a broader F1 party shell"? This tension is visible in `PROJECT.md`, `ROADMAP.md`, and the handoff (`.planning/PROJECT.md:40-49`, `.planning/PROJECT.md:92-98`, `.planning/ROADMAP.md:5-11`, `.planning/phases/01-authored-round-contract/.continue-here.md:65-87`).

2. [INFERRED] Which future protections are actually expensive to add later, versus merely nice to have early? The handoff names four candidate cheap-now, expensive-later decisions, but those need explicit user confirmation before they should become locked planning doctrine (`.planning/phases/01-authored-round-contract/.continue-here.md:78-87`).

3. [INFERRED] Should roadmap protection live per phase or per eventual milestone? Because there is no milestone artifact yet, the practical answer today is "per phase in `ROADMAP.md`," but that may not stay optimal.

4. [INFERRED] Should checker workflows fail plans that omit explicit non-foreclosure checks for architecture-setting phases, or merely warn? My current recommendation is warning-first.

## Source Ledger

### Primary Sources (High Authority)

- `AGENTS.md`
  - Repo-local GSD posture, future-aware context expectation, and orchestration policy.
  - Key lines used: `AGENTS.md:44-49`, `AGENTS.md:60-83`.

- `.planning/PROJECT.md`
  - Product posture, tensions, open questions, and document evolution rules.
  - Key lines used: `.planning/PROJECT.md:36-49`, `.planning/PROJECT.md:69-75`, `.planning/PROJECT.md:88-115`.

- `.planning/ROADMAP.md`
  - Sequencing, open decisions still visible, and current per-phase framing.
  - Key lines used: `.planning/ROADMAP.md:5-11`, `.planning/ROADMAP.md:31-111`.

- `.planning/config.json`
  - Confirms exploratory discuss mode and current workflow settings.
  - Key lines used: `.planning/config.json:15-31`.

- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
  - Strongest live example of future-aware phase steering in the repo.
  - Key lines used: `.planning/phases/01-authored-round-contract/01-CONTEXT.md:48-76`, `.planning/phases/01-authored-round-contract/01-CONTEXT.md:134-151`.

- `.planning/phases/01-authored-round-contract/01-01-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-03-PLAN.md`
  - Used to check whether future-protection survives into concrete plans.

- `.codex/get-shit-done/templates/context.md`
  - Used to compare current good repo practice with baseline harness requirements.

- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/plan-phase.md`
  - Used to locate where scope discipline is strong and where future-awareness is not yet explicit.

### Secondary Sources (Medium Authority)

- `.planning/phases/01-authored-round-contract/.continue-here.md`
  - Valuable because it captures the exact strategic pause condition and the identity mismatch risk.
  - Reliability limit: interpretive handoff artifact; related audit outputs are uncommitted (`.planning/phases/01-authored-round-contract/.continue-here.md:42-61`).

### Additional Local Observation

- Local scan on 2026-04-10:
  - `find .planning -maxdepth 2 -type f | rg '/(MILESTONE|milestone)'`
  - Result: no milestone artifact present under `.planning/`.
