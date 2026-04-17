# Audit Program

## Research Frame

- mode: `exploratory comparative audit with investigatory follow-through`
- question:
  how should the repo now compare upstream GSD docs, upstream runtime reality, and the existing readiness-era harness mapping, and what program revision follows from that comparison?
- scope:
  upstream `v1.36.0` docs and adjacent corroboration surfaces; earlier readiness mapping and checkpoint doctrine; the decision of whether to reseed or revise the intervention program from those materials
- non-goals:
  immediate harness code changes, silent canon changes, or assuming that either upstream docs or readiness maps are authoritative before they are comparatively justified
- stop condition:
  we have a reviewable judgment on:
  - whether upstream docs are fresh enough to be a reliable mapping seed
  - how they compare to earlier readiness mapping
  - whether the existing readiness/intervention program should be preserved, revised, restarted, or split

## Audit Stance

- [g:c+i] This program is gap-exposure and completeness-challenge oriented, not pass/fail oriented. It should ask what is under-owned, under-grounded, over-closed, or quietly foreclosed by each possible framing. Sources: `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:50-58,87-100,160-167`.
- [g:c+i] Competing artifacts must be compared by spec quality, source coverage, and claim survivability rather than by prestige, fluency, or mere existence. Sources: `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md:9-10,16-26,42-59,97-119`.
- [g:c+i] Non-promotion is not neutral. If the result of this audit is "keep the old program," that choice must be justified against the anti-regret question rather than treated as the cheap default. Sources: `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:132-140`; `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md:89-95`.

## Why This Program Exists Now

- [e:c:i] The repo's current operational boundary is still pre-rerun Phase 01, and active readiness work is still concentrated in Checkpoint 5 follow-through rather than fresh execution. Sources: `AGENTS.md:41-45`; `.planning/readiness/phase-01-rerun/STATUS.md:7-10,28-33`.
- [e:c:i] Checkpoint 5 is already about bounded harness ownership, review posture, launch-truth capture, and workflow-chain follow-through, which makes a better-grounded harness map materially relevant rather than merely interesting. Sources: `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:8-11,59-63,79-90`.
- [e:c+i] The new upstream-docs discovery creates a real possible reframing: prior readiness mapping may now need requalification, not because it was worthless, but because the evidence base for future mapping may have changed. This possibility should be tested explicitly rather than assumed either way. Sources: `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:67-76,87-100`; current conversation.

## Wave Structure

### Wave 0: Setup

- write this session directory
- define stable lane specs before delegation
- record launch-truth protocol in `LAUNCH-LEDGER.md`

### Wave 1: Baseline Pressure

- `lane-01` upstream docs freshness audit
- `lane-02` docs-vs-readiness crosswalk

Wave-1 purpose:
- test whether the upstream docs are actually reliable enough to matter
- test whether the earlier readiness mapping was wrong, under-grounded, differently scoped, or still uniquely valuable

### Wave 2: Judgment

- `lane-03` reseed / restart / branch judgment

Wave-2 purpose:
- turn the wave-1 evidence into a program judgment
- decide whether the existing readiness mapping program should:
  - stay substantially intact
  - be revised
  - be partially rerun from upstream docs
  - branch into one or more narrower follow-on lanes

### Wave 3: Optional Expansion

Open only if a prior lane proves it necessary.

Allowed directions:
- targeted docs trust / exclusion / supplementation gap map
- cross-vendor large-context independent docs-gap reread
- direct code-first doc drift audit
- ontology reconciliation between upstream docs and readiness-era mapping categories
- readiness-program revision / new subphase design
- targeted upstream-trajectory lane if `main` introduces near-horizon carry-forward pressure not visible in `v1.36.0`

### Wave 4: Synthesis / Consequence

- comparative synthesis across the lane outputs
- explicit consequence statement for readiness package or later audit program
- if warranted, proposal artifact for readiness-plan / checkpoint-sequence changes rather than silent mutation

## Expansion Rules

- expand when a current lane cannot honestly answer its own question without a new bounded read set
- expand when a lane proves that the framing itself is excluding load-bearing evidence
- do not expand only because "more would be interesting"
- current triggered expansion:
  - [e:c+i] `lane-01` established uneven freshness and guarded-seed status, but it did not fully separate trustworthy summary surfaces from explicitly excluded or omitted surfaces, nor did it map a concrete supplementation path for building on the docs instead of rebuilding from scratch. That gap now warrants a bounded follow-up lane before broader program revision. Sources: `lane-01-upstream-docs-freshness.md:23-42,73-92,168-197,216-228`; current conversation.
  - [e:c+i] The user also raised an epistemic-reliability objection against treating the internal `lane-01` / `lane-01b` path as sufficiently independent for a later docs-refresh plan, especially given task breadth and context-window pressure. That now warrants a cross-vendor, large-context reread that treats earlier internal lanes as candidate evidence and possible blindspot seeds rather than as settled truth. Sources: current conversation; `CLAUDE-REVIEW-COMMANDS.md:7-39`; `PROTOCOL.md:59-67`.
- if expansion is warranted, record:
  - why the original frame was insufficient
  - what the new lane would own
  - what remains deferred

## Output Contract

Every lane output should separate:

- direct evidence
- inference / interpretation
- unknowns
- what this lane does and does not justify
- what the spec did not capture
- whether the result pressures the audit program itself

## Readiness Consequence Rule

- if this audit implies a real change to Checkpoint 5 scope or to the wider rerun-readiness sequence, do not patch `.planning/readiness/phase-01-rerun/` opportunistically
- first produce a synthesis or proposal artifact that explains:
  - what changed
  - why the prior framing is no longer sufficient
  - what should be revised, added, or deferred
