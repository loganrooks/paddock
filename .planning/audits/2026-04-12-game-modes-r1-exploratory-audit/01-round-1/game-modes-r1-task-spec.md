---
date: 2026-04-12
audit_orientation: exploratory
audit_delegation: self
scope: "Round 1 exploratory audit of F1 party-platform game mode families, treating current ideas as possibility spaces rather than fixed pitches"
triggered_by: "manual: user-approved root-spec launch prep for the game-modes exploratory audit"
task_spec: 01-round-1/game-modes-r1-task-spec.md
ground_rules: "exploratory-root+context-plurality+virality-vs-retention+user-signal"
output_files:
  - 01-round-1/round-1-orientation.md
  - 01-round-1/round-1-output.md
  - 01-round-1/round-1-self-eval.md
  - 03-next-round/round-2-prompts.md
tags:
  - exploratory-audit
  - game-modes
  - round-1
  - product-vision
---

# Round 1 Root Task Spec

## What this is

This is the root spec for Round 1 of an iterative exploratory audit of brainstormed and emerging game modes for an F1 fan party-game platform.

This is not the final audit output. This is the governing contract for how Round 1 should be run.

Round 1 is allowed to:
- read the current mode corpus closely
- expand the possibility space
- critique weak directions
- strengthen promising ones
- generate bounded first-wave new proposals

Round 1 is not expected to settle the whole design space. Later rounds will revisit the work after creator feedback.

## Classification

Treat Round 1 as:

- `no named subject × exploratory × self`

Why:
- the current written ideas are launch points, not boundaries
- the most important design question may only become visible mid-audit
- the user explicitly wants room for the inquiry to exceed the categories we currently have

Named subjects can still be used locally when useful:
- `artifact_analysis` when grounding claims in the existing docs
- `comparative_quality` when comparing against BoxBoxd or other product shapes
- light `process_review` when the framing itself seems to be hiding important design territory

## Round 1 purpose

Round 1 should answer:

- what is already here
- what is genuinely promising
- what is thin, generic, or underdeveloped
- what hidden variants are already implied
- what different player situations and play contexts these modes afford
- where context tensions, replay loops, community potential, or platform implications are being underexplored
- what new proposals should be added now without dissolving into undisciplined brainstorming

## Anti-goals

Round 1 is explicitly NOT:

- a go/no-go audit
- a feasibility-first pass
- a "will F1 fans like this?" yes/no exercise
- a search for one ideal fan or one ideal play context
- an attempt to make every mode support local couch + sync + async + community-ready all at once
- a user-preference rubber stamp

## Source corpus

Primary read set:
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-INDEX.md`
- `.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md`

Supporting read set:
- `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINT.md`
- `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md`

Conditional read set:
- `.planning/explore/2026-04-11-product-vision-game-design/words-of-wisdom-radio-catalog.md` if needed to judge how much deeper `Words of Wisdom` already is than the other modes
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md` only when a mode pressures architecture in a way that matters to the audit
- `.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md` only when a finding depends on known unresolved research rather than missing ideation

## Governing principles

### 1. Treat the entries as possibility families

Most of the current "modes" are not finished game designs. They are families of possible games, variants, round types, and social shapes.

Do not judge them as if they had already collapsed to one final form.

### 1A. Treat each idea as design terrain, not just its current named pitch

Do not confuse:

- the current writeup
- one plausible realization
- the actual terrain of what the game could become

The audit should explore multiple realizations where useful, especially when local, online sync, async, streamer, community, or persistence affordances might materially change what the best form of the game is.

The question is often not:

- "what is this game, fixed once and for all?"

It is more often:

- "what is the possibility space around this fantasy, and which realizations look strongest?"

### 1B. Do not impose one universal ontology across all games

Do not assume every idea should be described with the same schema such as:

- family
- mode
- round type
- packet
- event layer

Some games may want unlock ladders, vehicle classes, match types, or role asymmetries.
Others may want packet composition, social reveal structures, or persistent group history.

The ontology should be responsive to the game itself. It should be discovered from the shape of the design terrain, not forcibly transplanted onto it.

### 2. Use categories, but let the work exceed them

Current categories like `local`, `online sync`, `async`, `spectator`, `community`, `solo`, and so on are useful heuristics.

They are not a prison.

If a mode reveals a fun and important play shape that exceeds the current category grid, say so. Do not force the mode back into the grid just because the grid came first.

### 3. Do not assume each mode has one true context

Some modes are single-context specialists.
Some balance multiple contexts well.
Some want different variants with different context commitments.
Some contexts genuinely tension against each other.

Round 1 should surface those differences honestly.

### 4. Distinguish virality from retention

Every mode should be read through both questions:
- what makes this immediately legible, funny, intense, surprising, or shareable?
- what makes the same group want another round, another session, another unlock, another pack, or another weekend with it?

Meme energy is good. One-joke exhaustion is not.

### 5. User-origin is a signal, not a ranking

Some ideas were initiated and pressure-tested more directly by the user.
Others were proposed by the assistant or lightly touched.

This affects how carefully the audit should read the idea, but it is not proof that the idea is better.

### 6. Architecture is secondary in Round 1

Architecture can be surfaced where it meaningfully changes what a mode can become.

But product-and-game-design stays primary. Do not collapse this round into substrate triage.

## Required lenses

Round 1 must explicitly apply these lenses:

### A. What is already here

For each mode family:
- what is already concrete
- what is still mostly flavor
- what has already been pressure-tested more by the user
- what has not yet really been interrogated

### B. Possibility expansion

For each mode family:
- what variant forks are already implied
- what different moods or energies it could support
- what player situations it becomes interesting in
- what tuning knobs could broaden or sharpen its appeal
- what materially different realizations of the core fantasy seem available
- which realizations look stronger or weaker across couch, online sync, async, streamer, and community surfaces

### C. Context profile / tension map

For each mode family:
- where it is clearly strong
- where it plausibly balances more than one context well
- where contexts genuinely tension against each other
- where different variants should make different commitments
- where support for a context would feel forced

### D. User situation lens

Test ideas against a plurality of concrete situations, including:
- 4 friends on a couch with mixed F1 knowledge
- 2 hardcore fans plus 2 casual partners
- remote Discord group looking for synchronous play
- solo fan killing 10 minutes between race weekends
- watch-party crowd with non-playing spectators
- recurring friend group that wants persistent history and inside jokes

### E. Community / online potential

For each mode family, ask:
- does it want friend-group history?
- does it want public competition?
- does it want user-generated content?
- does it create good spectator or streamer moments?
- does it benefit from race-weekend or calendar cadence?
- does it have a plausible async form, or would async distort it?
- does online/community potential reveal a better realization of the game than the current pitch surface suggests?

### F. Launch-gap lens

Explicitly check for:
- onboarding / learnability
- session-length fit
- drop-in / drop-out resilience
- mixed-skill-group friendliness
- spectator boredom / elimination dead time
- content supply burden
- moderation / safety needs where relevant
- funny-once versus structurally replayable
- cases where the category grid itself is missing an important play shape

## Round 1 structure

Round 1 should produce:

1. `01-round-1/round-1-orientation.md`
   Purpose: map the current corpus, the strongest early patterns, and the first-pass tensions before final synthesis.

2. `01-round-1/round-1-output.md`
   Purpose: creator-facing Round 1 audit output.

3. `01-round-1/round-1-self-eval.md`
   Purpose: record what Round 1 thinks it did well, what it may have missed, and what should be pressure-tested in the next round.

4. `03-next-round/round-2-prompts.md`
   Purpose: structured carry-forward prompts/questions for the next round after creator feedback.

## Delegation model

This root spec governs the whole round.

If grouped auditors are launched in Round 1:
- they should each receive a standalone full lane spec
- the lane specs should be derived from this root spec plus the shared lane scaffold
- the main thread retains final comparative judgment and final synthesis

The root spec is not replaced by lane specs. It is the parent contract.

## Prompt discipline

Any child prompt derived from this root spec should preserve these anti-failures:

- do not collapse to yes/no judgment
- do not assume a single ideal fan
- do not assume a single primary context
- do not universalize every mode across all contexts
- do not mistake user-origin for authority
- do not overreward virality while ignoring replayability
- do not bury tensions between good variants under tidy prose

## Between-round recalibration

There is a second sense of calibration that happens after Round 1:

- the creator responds to `01-round-1/round-1-output.md`
- the audit compares that response with `01-round-1/round-1-self-eval.md`
- Round 2 then revisits original and newly generated ideas with sharper judgment

That between-round recalibration is real, but it does not replace the need for a strong Round 1 root spec.
