# Second-Wave Research Standards

Date: 2026-04-10
Session: `2026-04-10-vision-future-hosting`
Status: active protocol for the next research wave

## Why This Exists

The first research wave was useful for orientation, but it was still too tidy in places.

For the next wave, the standard must be higher. The researchers should not merely answer the stated question well. They should also:

- uncover gray areas not anticipated in the original framing
- notice when one question branches into several dependent questions
- surface live tensions instead of rushing to closure
- make their inquiry path inspectable
- remain open and responsive to what the evidence reveals rather than overfitting to the initial prompt

This protocol exists to make that more responsible style of research explicit.

## Core Research Posture

The next wave should be:

- exploratory, not prematurely narrowing
- self-critical, not merely assertive
- branching, not linear by default
- explicit about dependencies between questions
- willing to mark where the inquiry expanded beyond the original scope

The goal is not to make the researchers unfocused.

The goal is to let them responsibly follow emerging lines of concern without pretending those concerns were already perfectly captured in the initial prompt.

## What Researchers Must Do

### 1. Map the inquiry trajectory

Each researcher must explicitly record the path of inquiry they took.

This should include:

- starting question
- subquestions that emerged
- which branches were followed
- which branches were noted but deferred
- what dependencies between branches became visible

The final write-up should make it possible to see not only the answer, but how the question itself evolved during inquiry.

### 2. Surface gray areas and resist premature closure

Researchers must actively look for:

- cases where evidence is mixed
- cases where multiple models remain viable
- cases where the right answer depends on product-shape choices not yet settled
- cases where technical feasibility diverges from adoption feasibility
- cases where ethical, operational, and architectural answers point in different directions

They should not resolve such tensions too quickly just to produce a neat report.

### 3. Mark scope expansions explicitly

If a researcher encounters an important issue that was not clearly inside the original prompt but becomes relevant through the research, they should not ignore it.

Instead, they must mark it explicitly as:

- `Scope Expansion`
- why it emerged
- how it relates to the original task
- whether it was pursued deeply or only flagged for later

This preserves rigor without punishing good research for discovering that the original framing was incomplete.

### 4. Distinguish kinds of feasibility

Researchers must separate:

- technical possibility
- operational feasibility
- adoption feasibility
- economic feasibility
- ethical or trust feasibility

This is especially important for questions about:

- peer-to-peer or cooperative compute
- funding and access models
- public/private transition paths
- scaling under constrained resources

### 5. Treat practical implications as first-class

Each lane should not stop at abstract analysis.

It must also include practical implications for:

- how to think about the design space
- what should be protected architecturally
- what should be measured experimentally
- what should remain open for now

### 6. Preserve rival models

Each researcher should include rival framings that survive the inquiry.

The standard is not "recommend one thing and move on."
The standard is:

- what seems strongest right now
- what still resists elimination
- what would change the balance between those options

## Required Sections For Each Lane

The next wave should require each findings file to include the following sections:

1. `Question Space`
2. `Method And Sources`
3. `Inquiry Trajectory`
4. `Branching Paths And Dependencies`
5. `Findings`
6. `Gray Areas And Live Tensions`
7. `Scope Expansions`
8. `Rival Models Still Alive`
9. `Practical Implications`
10. `What Would Change This View`
11. `Open Questions Worth A Third Pass`
12. `Source Ledger`

## Section Guidance

### Inquiry Trajectory

Should show how the researcher moved from the initial question into subquestions and why.

### Branching Paths And Dependencies

Should identify which design questions depend on which others.

Example:

- public funding model depends partly on hosting architecture
- hosting architecture depends partly on room/state model
- room/state model depends partly on whether the product is primarily live-room centered or wrapper-centered

### Gray Areas And Live Tensions

This should be a serious section, not a token uncertainty paragraph.

It should attend to places where synthesis is resisted by the material.

### Scope Expansions

This is where the researcher records:

- new areas of concern that emerged
- why they mattered
- whether they were investigated or only flagged

### Rival Models Still Alive

This section should preserve non-dominant but still viable alternatives.

### Practical Implications

This section should be divided into:

- `thinking implications`
- `design implications`
- `implementation implications`
- `measurement or experiment implications`

## Source Expectations

### Primary sources remain mandatory for technical claims

Official docs, standards, and primary platform documentation should remain the base layer for:

- what is technically supported
- browser/network constraints
- infrastructure capabilities
- protocol limitations

### Secondary and practitioner sources are now required where appropriate

For the next wave, official docs alone are not enough.

Researchers should also look for:

- operator writeups
- postmortems
- practitioner discussions
- community governance lessons
- deployment war stories
- case studies

But they must label these carefully for:

- authority
- likely bias
- degree of corroboration

## What Counts As Good Research In This Wave

Good research in the next wave will:

- reveal hidden questions rather than only answering visible ones
- show how one concern leads into another
- make uncertainty legible
- resist collapsing product, technical, and ethical questions into one axis
- help the project navigate the design space rather than pretending to solve it cleanly

## What To Avoid

- false neatness
- vendor-doc parroting
- collapsing possibility into recommendation too early
- treating product shape as fixed when it is part of the question
- ignoring adoption or trust because a system is "technically possible"
- burying scope expansions instead of recording them

## Practical Consequence For The Next Wave

The next wave should likely be narrower in subject than the first wave, but deeper and more dialectical in method.

It should not merely ask:

- "what is the best option?"

It should ask:

- "what are the viable options?"
- "what hidden dependencies shape them?"
- "what tensions remain if we try to choose among them?"
- "what would we need to learn experimentally before deciding responsibly?"
