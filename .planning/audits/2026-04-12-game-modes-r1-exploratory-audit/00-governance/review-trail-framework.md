---
date: 2026-04-13
audit_subject: process_review
audit_orientation: exploratory
audit_delegation: self
scope: "Framework for traceable review, prompt, and output artifacts in the next game-modes audit iterations"
triggered_by: "manual: creator request"
tags:
  - exploratory-audit
  - framework
  - standards
  - conventions
  - guidelines
  - traceability
source_artifacts:
  - /home/rookslog/workspace/projects/get-shit-done-reflect/.claude/get-shit-done-reflect/references/claim-types.md
  - /home/rookslog/workspace/projects/get-shit-done-reflect/.claude/get-shit-done-reflect/references/audit-conventions.md
  - /home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/AUDIT-EXECUTION-PLAN-game-modes-r1.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/round-1-self-eval.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2-prompts.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-output.md
---

# Review Trail Framework

## Purpose

This document governs the next layer of review, prompting, and synthesis artifacts for the game-modes exploratory audit.

Its job is to make the audit trail:

- epistemically clearer
- more traceable across rounds
- less vulnerable to stale carry-forward
- less vulnerable to premature closure
- more explicit about what is binding, what is a strong default, and what is a heuristic

This is not a flat rule sheet. It is a tiered framework.

## Adaptation note

This document is inspired by, but does not mechanically transplant, three outside references:

- `claim-types.md`
- `audit-conventions.md`
- `RESEARCH-PRINCIPLES.md`

Useful inheritances:

- typed claims and verification levels
- frontmatter and audit-artifact discipline
- non-foreclosure, path-of-inquiry, and dependency tracing

Necessary adaptation:

- this audit is not a generic Reflect audit
- not all important claims here will be directly citeable to files
- creator feedback in live conversation is itself a load-bearing source
- some obligations should remain abstract enough to allow judgment
- justification, epistemic reliability, traceability, and adherence need stricter concreteness than other layers

## Intended artifact chain

This framework is meant to govern at least these artifacts:

1. detailed review / critique / gap register
2. next-round prompt or task spec
3. next-round output or synthesis
4. later follow-up reviews that assess whether the requested response actually answered the prior gap

The desired trace chain is:

`gap identified -> why it is a gap -> requested response -> actual response -> later assessment`

## Obligation tiers

This framework uses four tiers of obligation.

### 1. Guiding principles

These are the highest-level commitments.

They are not checklists.
They explain what the audit is trying to preserve or prevent.

Deviation bar:

- very high
- if a principle is materially departed from, the departure should be named plainly and treated as a serious exception

### 2. Standards

These are mandatory requirements for the review-trail artifacts governed by this framework.

They should be followed unless there is a strong, case-specific reason not to.

Deviation bar:

- high
- a deviation must be justified explicitly and traceably

### 3. Conventions

These are strong defaults.

They are meant to produce consistency, clarity, and interoperability across artifacts, but they are not absolute.

Deviation bar:

- moderate
- a short explanation is usually enough if the convention is not followed

### 4. Guidelines

These are heuristics, craft advice, and preferred habits.

They help quality, but they should not be confused for hard requirements.

Deviation bar:

- low
- note the judgment call only when it materially affects interpretation, traceability, or quality

## Qualified adherence language

Use this ladder when writing or interpreting obligations:

- `must`
  standard-level requirement
- `should`
  convention-level default
- `prefer`
  guideline-level preference
- `may`
  allowed option
- `explain if deviating`
  not a loophole; see the deviation protocol below

Do not write obligations in a way that makes every statement sound equally binding.

## Core principles

## Principle P1: Non-foreclosure

Do not collapse the option space prematurely.

Concrete meaning in this audit context:

- do not treat one plausible realization as if it were already the game
- do not treat one imposed ontology as if it were native to every game
- do not confuse current documentation maturity with underlying promise
- do not let one earlier lane overdetermine later exploration

What this should mean in practice:

- review artifacts should distinguish what is closed, what is still terrain, and what remains open
- prompts should ask for alternative realizations where they matter
- outputs should preserve multiple live possibilities when closure is not yet warranted

## Principle P2: Traceability

A later reader should be able to reconstruct how a conclusion emerged.

Concrete meaning in this audit context:

- important critiques should be tied to artifacts, creator feedback, or clear reasoning
- each important gap should have an identifier
- each requested response should be tied back to a gap
- each later output should report what it was responding to

## Principle P3: Epistemic candor

Do not present inference as citation, speculation as finding, or preference as settled truth.

Concrete meaning in this audit context:

- distinguish artifact-supported claims from session-feedback claims and reasoned inferences
- name when a claim is based on creator critique rather than file evidence
- name when a judgment is provisional
- keep uncertainty calibrated rather than evasive

## Principle P4: Responsiveness to creator calibration

The creator's critiques are not decorative commentary. They are part of the evolving audit basis.

Concrete meaning in this audit context:

- later review artifacts must record where the audit was corrected by creator feedback
- later prompts must inherit those corrections rather than silently reverting to earlier frames
- stale artifacts should be treated as stale, not as higher authority merely because they were written earlier

## Principle P5: Fit the framework to the case

The framework should discipline the work without flattening the work.

Concrete meaning in this audit context:

- some obligations should remain abstract enough to allow judgment
- justification, traceability, epistemic reliability, and adherence should be more concrete than stylistic or interpretive guidance
- the framework should create inspectability, not bureaucratic drag

## Standards

## Standard S1: Every load-bearing critique or carry-forward claim must use typed provenance

For review-trail artifacts, important claims must identify both:

- epistemic type
- verification or provenance basis

Use the claim-type ontology as inspiration, adapted here.

Recommended primary types:

- `evidenced`
- `decided`
- `assumed`
- `open`
- `projected`
- `stipulated`
- `governing`

Recommended verification or provenance markers:

- `cited`
  directly tied to a specific artifact or source
- `reasoned`
  argued but not directly cited
- `session`
  grounded in creator feedback or live session correction
- `mixed`
  materially combining cited and session/reasoned support
- `bare`
  use sparingly; usually a signal that the claim needs strengthening

Examples:

- `[evidenced:cited]`
- `[governing:session]`
- `[assumed:reasoned]`
- `[evidenced/governing:mixed]`

Notes:

- `session` is an adaptation for this audit context
- not all important claims here can or should pretend to be file-cited

## Standard S2: Every significant gap must be recorded in a traceable gap register

Each gap entry must include:

- `gap_id`
- `claim`
- `claim_type`
- `evidence_or_provenance`
- `why_this_is_a_gap`
- `downstream_risk_or_dependency`
- `requested_response`
- `status`

Recommended optional fields:

- `affected_artifacts`
- `predecessor_gap_ids`
- `response_id`
- `vulnerability`

The point is not bureaucratic fullness.
The point is to prevent vague critique that later cannot be answered cleanly.

## Standard S3: Requested responses must be distinguishable from conclusions

The review artifact must separate:

- what is wrong, missing, stale, or under-shaped
- what response is being requested
- what later artifact actually responded

Do not collapse:

- critique
- recommendation
- later outcome

into one undifferentiated paragraph.

## Standard S4: Every next-round prompt or task spec must cite the governing gap review

A next-round prompt should not stand alone as if it emerged from nowhere.

It must identify:

- which review artifact it inherits from
- which gap IDs or issue clusters it is answering
- what it is not trying to answer yet

This does not require quoting everything.
It does require traceable inheritance.

## Standard S5: Outputs must report against the requested response, not just restate their own framing

When an output claims to answer a prior critique, it should explicitly say:

- which gap(s) it addressed
- whether the response is full, partial, or unresolved
- what remains uncertain

This is necessary to support later reassessment.

## Standard S6: Scope expansions must be marked, not smuggled in

When a task broadens beyond its initial framing, record:

- original framing
- expansion observed
- response chosen
  `defer`, `follow-and-mark`, or `revisit later`
- why

This inherits directly from the research-principles logic, adapted here.

## Standard S7: Staleness must be named explicitly

If an artifact is materially stale relative to later conversation or later outputs, say so.

Do not:

- treat earlier artifacts as current by default
- silently overwrite earlier framing without saying it changed

Recommended language:

- `still current`
- `partially stale`
- `materially stale`
- `superseded`

## Standard S8: Path and dependency sections are required in major review artifacts

Major review artifacts should include:

- `Path of Inquiry`
- `Dependencies and Relations`

The goal is to make the review inspectable as a line of inquiry, not just a pile of conclusions.

## Conventions

## Convention C1: Keep one stable ID chain across rounds

Prefer reusable IDs such as:

- `GAP-01`
- `RESP-01`
- `OUTCOME-01`

If one response addresses several gaps, record the relation explicitly.

## Convention C2: Prefer one main proposition per gap entry

If a gap entry contains three different complaints, it becomes hard to answer or track.

Split when needed.

## Convention C3: Separate artifact critique from creator-calibration critique

Where possible, distinguish:

- file-level critique
- session-level creator correction
- orchestrator inference

This makes later disagreement easier to interpret.

## Convention C4: Use severity or importance language carefully

Prefer:

- `load-bearing`
- `important`
- `secondary`
- `parking-lot`

over inflated labels unless true severity is needed.

## Convention C5: Preserve room for judgment in interpretive areas

Not every obligation should be reduced to a compliance checkbox.

Examples where some abstraction is healthy:

- tone calibration
- sense of what counts as a live design terrain
- comparative taste judgments
- whether a branching distinction is real or artificially imposed

What matters is that the framework makes these judgments inspectable, not that it falsely mechanizes them.

## Convention C6: Prefer short application notes for abstract obligations

When an obligation is easy to misread, add a brief note:

- what it means here
- what following it would look like
- what violating it would likely look like

This is especially useful for:

- non-foreclosure
- responsiveness
- creator calibration
- "design terrain" language
- "do not over-constrain the exploration"

## Guidelines

## Guideline G1: Use concrete examples when clarifying an abstract obligation

Examples should illuminate rather than overdetermine.

State clearly when an example is:

- a probe
- an illustration
- a plausible branch

and not a required category.

## Guideline G2: Prefer comparative wording over empty assertion

Better:

- "this doc is partially stale because it predates lanes I and J and still frames the next round mainly around family deepening"

Worse:

- "this doc feels outdated"

## Guideline G3: Keep the response ask proportional to the gap

Do not demand a full rerun when a local correction is enough.
Do not ask for a local patch when the framing itself is wrong.

## Guideline G4: Mark uncertainty honestly

Useful confidence vocabulary:

- `known`
- `likely`
- `plausible`
- `speculative`
- `unknown`

## Guideline G5: Distinguish "not yet captured" from "not important"

Some things are underrepresented because the artifact trail is lagging, not because they do not matter.

## Guideline G6: Treat creator examples as openings unless clearly promoted

Do not automatically convert a creator example into:

- a mandatory branch
- a fixed taxonomy
- the center of the next lane

unless the creator clearly wants that.

## Obligation concretization rule

To prevent abstract obligations from becoming vague slogans, any nontrivial obligation in a governed artifact should be concretized when needed.

For an obligation that is likely to shape interpretation or adherence, provide some or all of:

- what it means in this artifact
- what counts as compliance
- what counts as partial compliance
- what likely failure looks like
- what flexibility remains

This rule should be applied most strongly to:

- justification
- epistemic reliability
- traceability
- adherence
- deviation handling

This rule should be applied more lightly to:

- exploratory tone
- interpretive openness
- comparative design judgment

The aim is not to eliminate abstraction.
The aim is to prevent important obligations from becoming too abstract to govern behavior.

## Deviation protocol

`Explain if deviating` has its own minimum bar.

A good deviation justification should answer:

1. what is being deviated from?
2. why is deviation warranted here?
3. what is the substitute approach?
4. why is the substitute better in this case?
5. what is lost by deviating?
6. what downstream artifacts are affected?
7. is this local, temporary, or precedent-setting?

### Deviation bar by tier

- principle deviation
  very high bar; should be explicit and rare
- standard deviation
  high bar; requires concrete justification
- convention deviation
  moderate bar; short explanation usually enough
- guideline deviation
  low bar; note it only when material

### Poor justifications

- "felt better"
- "seemed simpler"
- "the other way was too constraining"
- "I thought this was fine"

### Better justifications

- what the default would have done here
- why that would have been distortive, misleading, or unhelpful
- why the alternative preserves the governing commitments better

## Review-specific application

In a detailed review / critique artifact:

- gap entries should use typed claims
- artifact citations should be used where available
- creator-feedback corrections should be marked as session-grounded
- stale artifacts should be explicitly labeled as such
- path and dependency sections should explain how the review moved from files to critique to response requests

## Prompt-specific application

In a next-round prompt or task spec:

- cite the governing review artifact
- state which gap IDs are being answered
- separate required responses from optional follow-up
- name the anti-goals and non-goals
- do not silently promote one example into a mandatory taxonomy

## Output-specific application

In a next-round output or synthesis:

- report which requested responses were addressed
- mark full, partial, or unresolved coverage
- distinguish new findings from inherited assumptions
- mark scope expansions
- note where the output is still exploratory rather than closure-ready

## Minimal frontmatter convention for framework-governed artifacts

Where practical, use frontmatter that includes at least:

- `date`
- `audit_subject`
- `audit_orientation`
- `audit_delegation`
- `scope`

Recommended additions:

- `triggered_by`
- `source_artifacts`
- `tags`

This keeps the audit trail searchable and auditable.

## Anti-patterns

- using "standards" language for everything and flattening the obligation tiers
- pretending every important claim can be directly cited
- using creator examples as if they automatically define the taxonomy
- silently carrying stale prompts forward
- collapsing critique and requested response into one mushy section
- writing prompts that do not identify what prior gaps they answer
- treating earlier written artifacts as more authoritative than later creator correction
- overconcretizing exploratory obligations until the exploration loses room to move
- underconcretizing justification and traceability obligations until they become decorative

## What this framework does not do

It does not:

- decide the substantive outcome of the next round
- replace judgment with forms
- force one ontology onto every game or every artifact
- require every obligation to be reduced to a checkbox

It does:

- create a clearer tiered discipline
- preserve audit traceability
- support mixed provenance honestly
- make future deviations inspectable
- give the next review and prompt artifacts a shared contract

## Immediate next use

The next artifact after this framework should be a detailed review / gap register that:

- cites this framework
- records the current gap analysis in detail
- marks which claims are file-cited, session-grounded, or reasoned
- identifies the requested response for the next round

The next-round prompt should then inherit from that review rather than from stale carry-forward docs alone.
