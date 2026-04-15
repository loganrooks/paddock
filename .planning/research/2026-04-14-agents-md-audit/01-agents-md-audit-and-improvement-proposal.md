# AGENTS.md Audit And Improvement Proposal

## Research Frame
- Mode: `solution evaluation`
- Question:
  how should this repo improve its `AGENTS.md` and overall Codex instruction mechanism so that it is more effective, less stale, more auditable, and better aligned with official Codex guidance while still enforcing this project's unusually high quality bar?
- Scope:
  - current root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
  - local governance docs that define what belongs in `AGENTS.md`
  - official OpenAI Codex `AGENTS.md` guidance
  - a sampled external examples corpus as comparative, non-authoritative input
- Non-goals:
  - direct editing of `AGENTS.md` beyond the small changes already made this session
  - exhaustive review of every community example
  - inventing a full new repo workflow
  - replacing `WORKFLOW.md`, `AI-GUARDRAILS.md`, or `ARTIFACT-GOVERNANCE.md`
- Stop condition:
  - a concrete recommendation exists for:
    - what should stay in root `AGENTS.md`
    - what should move out
    - whether nested `AGENTS.md` files should be adopted
    - how to use the Codex mechanism better in this repo

## Criteria
- `official-alignment`
  - does the proposal fit Codex’s documented discovery and override model?
- `repo-specificity`
  - does root `AGENTS.md` actually tell agents how to behave in *this* repo rather than reciting generic engineering advice?
- `stability vs staleness`
  - is the file likely to stay accurate, or is it carrying transient state that will rot?
- `actionability`
  - can an agent actually follow the rule at runtime without guessing?
- `non-duplication`
  - is `AGENTS.md` carrying material that belongs in broader governance docs?
- `future-friction reduction`
  - does the mechanism reduce repeated misreads and re-litigation in later milestones?
- `auditability`
  - can a later reviewer tell whether the file is shaping behavior well, or is it too fuzzy to inspect?

## Path Of Inquiry
- Entry point:
  - user request to run a proper audit and improvement pass on `AGENTS.md`, using official Codex docs and example corpora, with research best practices
- Branches considered:
  - keep one root `AGENTS.md` and just polish wording
  - keep a root file but split durable subdomain instructions into nested `AGENTS.md`
  - aggressively proliferate many nested `AGENTS.md` files
  - rely mostly on global `~/.codex/AGENTS.md` or overrides instead of repo-local guidance
- Branches pursued:
  - compare current root file against official Codex discovery model
  - compare current root file against local governance docs defining intended scope
  - sample external example corpus for common structural patterns and failure modes
  - evaluate mechanism options against explicit criteria
- Branches deferred or abandoned:
  - exhaustive community-example benchmarking
  - direct patching of the full root file before the research verdict exists
  - designing phase-specific nested instruction trees beyond the first durable layer
- Unexpected branches / reframings:
  - the main issue is not that the current file is bad; it is that the repo now has enough planning/audit complexity that a single root file is becoming the wrong *mechanism* for all agent-facing guidance
  - the sampled external examples are useful mostly as a warning about generic bloat, not as strong positive templates

## Assumptions Surfaced
- `[assumed:reasoned]` Root `AGENTS.md` should stay relatively stable and durable.
  - Why it matters:
    if root instructions carry too much transient state, they become noisy and untrustworthy.
  - What could weaken it:
    if this repo genuinely changes posture every day and there is no better place for live state.
- `[assumed:reasoned]` The official OpenAI guide is the primary source for mechanism shape, but not for repo-specific content.
  - Why it matters:
    it should determine *how* the mechanism works, not the whole content model.
  - What could weaken it:
    if the official guidance were extremely prescriptive about document structure. It is not.
- `[assumed:reasoned]` The local governance docs are authoritative about what belongs in `AGENTS.md` in this repo.
  - Why it matters:
    [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md), and [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md) already define a separation of responsibilities.
  - What could weaken it:
    if those docs are themselves stale or contradictory.
- `[assumed:reasoned]` Nested `AGENTS.md` files are valuable only when the subdirectory rules are durable and local to that subtree.
  - Why it matters:
    otherwise nested files become hidden instruction traps.
  - What could weaken it:
    if the repo had many stable, high-traffic subtrees with sharply different workflows.

## Evidence Base
### Direct evidence
- Official OpenAI Codex guidance says Codex reads `AGENTS.md` files before work and merges global plus project/nested files from root to current directory, with closer files overriding earlier ones and a default combined cap of 32 KiB. Source: OpenAI, “Custom instructions with AGENTS.md”  
  https://developers.openai.com/codex/guides/agents-md
- The same official guide explicitly recommends layering repository-level instructions and using nested overrides close to specialized work, plus verifying which instruction sources were loaded. Source: OpenAI  
  https://developers.openai.com/codex/guides/agents-md
- This repo’s [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md) says `AGENTS.md` is intentionally narrower and should contain only agent-facing runtime rules, model/delegation policy, and source-of-truth pointers; broader git/devops/artifact process should live elsewhere.
- This repo’s [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md) says `AGENTS.md` should tell agents what rules to obey while acting, while broader operating guardrails and signoff expectations live outside it.
- Current root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md) is `11,324` bytes and `123` lines. It already does several things well:
  - points to broader docs instead of duplicating them entirely
  - encodes repo-specific orchestration and model-policy rules
  - encodes real project-specific failure modes and quality expectations
- Current root `AGENTS.md` also carries several categories at once:
  - runtime rules
  - initialization bootstrap
  - current product posture
  - research-quality doctrine
  - orchestration policy
  - maintenance guidance
- Sampled external example corpus:
  - the agentsmd site positions its collection as “carefully curated” and “production-ready”
  - a sampled example from its linked GitHub repository (`react-project.md`) is a 339-line generic frontend development guide with tech stack, project structure, and component standards, rather than a tight repo-specific runtime instruction file. Sources:
    - https://agentsmd.net/agents-md-examples/
    - https://github.com/gakeez/agents_md_collection/blob/main/examples/react-project.md

### Inference and interpretation
- The official OpenAI source gives strong mechanism guidance:
  - layering and precedence matter
  - nested files are supported
  - verification of loaded sources matters
  - byte budget matters
  It does **not** prescribe a single canonical section layout.
- The repo’s own governance docs already want a narrower root `AGENTS.md` than the file is drifting toward.
- The current root file is not too large for Codex discovery, but it is large enough that signal competition is becoming a quality risk:
  - very stable runtime rules
  - transient current-posture reminders
  - high-level doctrine
  - detailed orchestration policy
  are all competing in one place.
- The sampled external examples are lower-confidence guidance for this repo’s problem.
  They appear optimized for broad template reuse and SEO/distribution, not for high-signal repo-specific Codex runtime behavior.
- The strongest improvement is therefore not “copy better examples.”
  It is:
  - keep root `AGENTS.md` sharper and more durable
  - move local planning/artifact-specific instructions into a durable nested file where they belong
  - keep ephemeral state out of root where possible

### Unknowns
- It is still unknown whether this repo needs one nested planning-level `AGENTS.md` or more than one. The evidence supports *at least* a `.planning/AGENTS.md` consideration, but not yet a larger instruction tree.
- It is unknown how much current developer/system prompting in this environment will continue to supply live state that makes some root reminders redundant.
- It is unknown whether all current root `AGENTS.md` content can be compressed without losing valuable repo-specific nuance; some of it may need careful migration rather than deletion.

## Option Comparison

| Option | Description | Strengths | Weaknesses | Evaluation |
| --- | --- | --- | --- | --- |
| A | Keep one root `AGENTS.md`, polish wording only | Lowest migration cost; no discovery complexity | Root file keeps accumulating mixed concerns; staleness and signal competition likely continue | Better than current drift, but not the best mechanism |
| B | Keep a sharper root `AGENTS.md` and add one durable nested `.planning/AGENTS.md` | Matches official layered model; reduces root clutter; puts audit/research/planning rules near actual work | Requires one-time design discipline so nested file does not become a dump | Best current fit |
| C | Create many nested `AGENTS.md` files across audits, phases, and subtrees | Maximum locality | High hidden-context risk; instruction sprawl; hard to audit | Too heavy for now |
| D | Minimize repo-local AGENTS and rely on global `~/.codex/AGENTS.md` or overrides | Good for personal defaults | Wrong for shared repo-specific posture; weak auditability in repo history | Not appropriate as the main mechanism |

## Dependencies And Relations
| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Root `AGENTS.md` narrowing | Official layering model; repo governance docs | Daily agent behavior, prompt clarity, future staleness | medium |
| `.planning/AGENTS.md` addition | Need for durable planning/audit-local rules | Research quality, artifact handling, canon patch hygiene | medium |
| Keeping live state out of root | Reliable alternate homes for live state (`STATE.md`, hooks, developer guardrails) | Root file durability | medium |
| Explicit self-audit criteria for AGENTS changes | Repo willingness to maintain instruction quality | Long-term instruction drift | low |

## Scope Expansions And Deferrals
- `Follow-and-mark`
  - the question broadened from “improve AGENTS.md wording” to “improve the repo’s Codex instruction mechanism,” because the mechanism problem is now load-bearing.
- `Revisit later`
  - whether to add more nested `AGENTS.md` files below `.planning/`
  - whether to introduce a dedicated AGENTS self-audit checklist doc or just fold it into maintenance rules
- `Defer`
  - auditing every example in the external corpus
  - redesigning the whole repo governance stack around AGENTS

## What Can Close Now
- The primary source for AGENTS mechanism should be the OpenAI Codex guide, not community example sites.
- The current root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md) is useful but overloaded.
- The repo’s own governance docs and the current root file are partially misaligned:
  - governance says root `AGENTS.md` should stay narrower
  - root file is gradually carrying more doctrine and workflow explanation
- The best next mechanism is:
  - keep a sharper root `AGENTS.md`
  - add one durable nested `.planning/AGENTS.md`
  - avoid aggressive proliferation beyond that until a real need appears

## What Must Stay Open
- Exact final root-file length target.
  - A practical target is “meaningfully shorter and more stable,” not a magical byte count.
- Exact boundary between root `AGENTS.md` and `.planning/AGENTS.md`.
  - This needs one implementation pass, not just theory.
- Whether any current root rules are still too transient to track in versioned instructions at all.

## Concrete Proposal

### 1. Restructure root `AGENTS.md`

Root should keep only:

- repo identity and runtime scope
- source-of-truth pointers
- non-negotiable runtime behavior
- delegation/model policy
- high-value repo-specific failure-mode guards
- maintenance/update rules

Root should likely shed or compress:

- bootstrap detail that matters only when `.planning/` is absent
- broader explanatory prose already stated in governance docs
- long lists of planning/audit-specific distinctions that belong closer to `.planning/`
- transient state reminders when they can live in:
  - `STATE.md`
  - session-start hooks
  - developer/system guardrails

### 2. Add `.planning/AGENTS.md`

This is the strongest mechanism improvement.

It should own:

- planning/audit/research artifact hygiene
- evidence vs inference expectations
- canon patch and supersession discipline
- status marking for historical/stale artifacts
- instruction for how to work inside audits, research, and phase docs without flattening them into canon

Why this is a good fit:

- the official Codex model supports nested instructions
- `.planning/` is a durable subtree with a genuinely different local workflow
- moving those rules there reduces root bloat without hiding them in irrelevant directories

### 3. Do **not** create many nested AGENTS files yet

Avoid:

- per-audit-session AGENTS files
- per-phase AGENTS files by default
- instruction trees that change every few days

Reason:

- they are harder to audit
- they create hidden override risk
- they are likely to go stale

Only add deeper nested files when the subtree is both:

- durable
- meaningfully different in workflow

### 4. Add an explicit AGENTS self-audit rule

Every meaningful future change to `AGENTS.md` should answer:

- Is this agent-facing runtime guidance?
- Is it stable enough for a durable instruction file?
- Is it already governed elsewhere?
- Is it repo-specific enough to deserve prompt budget?
- Would a nested file be a better fit?
- What stale-state risk does this addition create?

### 5. Treat community examples as suggestive, not normative

The sampled examples are useful for:

- seeing section shapes
- seeing how others package broad instructions

They are weak for:

- deciding what this repo’s root file should contain
- deciding how much generic engineering guidance belongs in AGENTS

For this repo, the stronger pattern is:

- official Codex mechanism guidance
- repo-local governance separation
- repo-specific lessons and failure modes

## Planning Handoff
- What can now be treated as decided:
  - root `AGENTS.md` should be narrower and more durable
  - `.planning/AGENTS.md` is the best next structural improvement
  - community example corpora should not be treated as primary guidance
- What remains assumed or open:
  - exact content split between root and `.planning/AGENTS.md`
  - whether any later nested files below `.planning/` are justified
- Derived constraints:
  - keep root stable
  - avoid duplicating governance docs
  - prefer durable subtree-local instructions over a bloated root file
  - avoid transient audit-session instruction sprawl
- Future-awareness seams to preserve:
  - explicit quality bar
  - model/delegation auditability
  - anti-shortcut and anti-staleness posture
  - milestone-2-aware quality expectations
- Deferred follow-up:
  - a concrete implementation pass that:
    - audits current root content line by line
    - proposes a root slim-down
    - drafts `.planning/AGENTS.md`
    - only then patches the files

## Sources
- Local:
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
  - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
  - [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
  - [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md)
- External:
  - OpenAI Codex guide: https://developers.openai.com/codex/guides/agents-md
  - Agents.md examples index: https://agentsmd.net/agents-md-examples/
  - Sampled example source: https://github.com/gakeez/agents_md_collection/blob/main/examples/react-project.md
