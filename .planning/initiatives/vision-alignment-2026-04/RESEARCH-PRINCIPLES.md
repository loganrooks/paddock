# Research Principles For Prix Guesser Vision Alignment

**Required reading:** every research or deliberation call in this initiative must read this file first.

---

## Core Commitment

Do not freeze the authored substrate in a shape that later phases will have to route around.

The point of this initiative is not to maximize decisiveness. The point is to close only the decisions that Phase 01 truly needs, while preserving the seams that later rules, room, calibration, and wrapper work will depend on.

## Project-Specific Risk

This repo is most at risk when a planner quietly treats one of these as "just an implementation detail":

- answer-surface ontology
- clue-family semantics
- fallback and coverage truth
- pack/round identity and reference shape
- scoring-intent contract

Those are not minor details. They are the authored substrate.

## Mode Discipline

Every task must declare which mode it is in:

### Terrain mapping

Map the option space and hidden assumptions. Do not pick a winner just to be tidy.

### Deliberation

Close only what must be closed now. Record deferrals explicitly.

### Synthesis

Translate findings into planning-ready guidance without widening scope.

## Non-Foreclosure Rules

Do not collapse:

- `venue`, `circuit`, `section`, and `corner` into one flat answer concept
- Street View and fallback media into one undifferentiated clue bucket
- active v1 answer surfaces and future-preserved lineage into the same thing
- scoring copy and scoring semantics into the same thing
- pack membership and round identity into filename convention

## Required Questions

Every output in this initiative must answer, explicitly:

1. What is being treated as a durable contract?
2. What hidden assumptions were surfaced?
3. What depends on this decision later?
4. What would become harder to change if we close this now?
5. What is being deferred rather than resolved?

## Gray-Area Handling

When the work hits a gray area, use one of these responses explicitly:

### Defer

The question exists, but it is not load-bearing for the current decision.

### Follow-and-mark

The question is load-bearing and bounded enough to investigate now. Mark the scope expansion explicitly.

### Revisit later

The question is load-bearing but too large to settle in the current round. Record what future work would need to answer it.

Never widen scope silently.

## Prix Guesser-Specific Guardrails

### Guardrail 1: Preserve circuit-aware play

Do not let fallback convenience silently redefine the anchor mode away from circuit-aware recognition.

### Guardrail 2: Preserve future lineage without widening v1

The schema should preserve `venue -> circuit -> section -> corner` relationships even if v1 gameplay only activates `venue` and `circuit`.

### Guardrail 3: Keep content, rules, and room doctrine distinct

Do not let room, transport, or UI assumptions leak into the authored content contract.

### Guardrail 4: Keep provider neutrality honest

Provider-neutral should mean the authored contract can carry multiple clue families without schema churn. It should not mean pretending all clue families are strategically equivalent.

### Guardrail 5: Prefer explicit deferral over fake completion

If the evidence is not strong enough to close a question, say so. A bounded deferral is better than a misleadingly neat contract.

## Required Output Sections

Every research or deliberation output should include:

- `Question`
- `Assumptions Surfaced`
- `Option Space`
- `Dependencies And Relations`
- `What Can Close Now`
- `What Must Stay Deferred`
- `Path Of Inquiry`

## Anti-Patterns

Avoid these:

- picking source format before the ontology is sound
- deciding scoring syntax before deciding scoring semantics
- using fallback-heavy venue reality to flatten the clue taxonomy
- treating "easy to validate" as equivalent to "right contract"
- treating future-aware seam preservation as permission to widen Phase 01 scope

## Success Condition

The work is successful if the next Phase 01 planning pass is more constrained, more honest, and more reversible than it would have been without this initiative.
