# Phase 1: Authored Round Contract - Context

**Gathered:** 2026-04-08
**Status:** Ready for planning

<domain>
## Phase Boundary

Define the authored pack and round substrate for the anchor mode, including validation rules, answer-target vocabulary, clue-step structure, reveal semantics, and explicit media fallback handling. This phase establishes the content contract that later rules, room, UI, and calibration phases will consume. It does not implement live-room behavior, runtime scoring execution, or end-user authoring UI.

</domain>

<decisions>
## Implementation Decisions

### Round And Pack Contract
- **D-01:** Model rounds as authored semantic objects, not thin `lat/lng + pano` records. A valid round contract must have first-class fields for answer target type, clue steps, accepted answers or aliases, reveal explanation, scoring profile, source references, and venue/circuit identity metadata.
- **D-02:** Model packs as curated authored collections of validated rounds with explicit pack metadata and stable content structure. Packs are not treated as random point buckets or public UGC primitives.
- **D-03:** Keep the active v1 answer-surface contract anchored at `circuit` and `venue`, while leaving the schema extensible enough for later `section`, `corner`, or composite targets.

### Clue Media And Fallback Modeling
- **D-04:** Use one provider-agnostic clue-step contract that can carry Street View and non-Street-View clue media without changing round shape.
- **D-05:** Treat Street View as an optional clue family, not the mandatory product substrate. The core round contract must not become Google-specific.
- **D-06:** Keep `circuit_internal`, `circuit_edge`, `venue_approach`, and `city_context` as explicit clue-family distinctions so easier fallback or approach clues do not silently replace circuit-aware play.
- **D-07:** Record venue coverage class and fallback strategy as explicit content metadata rather than as implied author judgment hidden in media assets.

### Validation Posture
- **D-08:** Reject incomplete or ambiguous content before it becomes playable, including missing answer-surface declaration, missing clue steps, missing accepted-answer data, missing reveal explanation, and undeclared or broken fallback relationships.
- **D-09:** Represent scoring as explicit content configuration in the round contract now, even though runtime judging lands in Phase 2. Scoring semantics should not live only in UI code or prose comments.
- **D-10:** Assume checked-in file-based authoring plus validation/import tooling for the first implementation of this contract rather than requiring an internal authoring UI before the schema is stable.

### the agent's Discretion
- Exact file format for authored packs and rounds (`json`, `yaml`, `ts`, or equivalent typed source)
- Exact validator/compiler package layout
- Exact naming and ID conventions, as long as they are explicit and stable across packs and rounds

</decisions>

<working_model>
## Working Model & Assumptions

- The first implementation should likely prove the contract with checked-in fixture packs and importer/validator tooling before any database-backed or in-app authoring surface.
- Coverage and fallback data may begin as round-level fields, shared venue-profile data, or a hybrid, but planning should keep the media posture explicit and queryable either way.
- The scoring-profile vocabulary should be rich enough for Phase 2 rules fixtures and reveal semantics, but it should avoid overfitting to unbuilt room or UI flows.

</working_model>

<derived_constraints>
## Derived Constraints

- The product is private-only and expert-first, so authored fidelity and fan-legible reveal logic matter more than generic quiz simplification.
- Circuit-internal recognition is the primary fantasy; venue-approach clues are secondary and must be modeled as such instead of becoming the hidden default.
- Phase 2 and Phase 3 depend on this contract staying transport-agnostic and UI-agnostic.
- Street View coverage is uneven and unstable across venues, so the contract must support non-Google clue media and explicit fallback declarations from the start.
- Later room and calibration phases need deterministic, validated content structures and stable identifiers; this phase cannot leave core content semantics implicit.
- There is no existing application code yet, so this phase establishes the first reusable domain boundary for the project.

</derived_constraints>

<open_questions>
## Open Questions

- Should coverage and fallback metadata live directly on each round, in shared venue profiles, or in both places with overrides?
- How granular should the first scoring-profile vocabulary be in Phase 1: simple presets, fully parameterized rules, or a hybrid?
- How much answer-target extensibility should be encoded now for later `section`, `corner`, and composite answers without making v1 authoring meaningfully heavier?

</open_questions>

<epistemic_guardrails>
## Epistemic Guardrails

- Treat the discovery field list as directional, not as a frozen schema. Validate the contract against multiple fixture round families before treating it as settled.
- Treat the coverage audit as venue-strategy guidance, not proof that specific coordinates or panorama IDs are production-safe.
- Preserve the distinction between "the schema must allow future answer surfaces" and "v1 content must actively ship those answer surfaces now."
- Do not let convenience around public-road or fallback-heavy venues silently redefine the anchor mode away from circuit-aware play.

</epistemic_guardrails>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase Scope And Requirements
- `.planning/ROADMAP.md` — Phase 1 goal, success criteria, and scope boundary for the authored round contract.
- `.planning/REQUIREMENTS.md` — `PACK-02`, `PACK-03`, `PACK-04`, and `OPS-01` define the concrete requirement surface for this phase.
- `.planning/PROJECT.md` — product posture, authored-model bias, and the circuit-internal recognition priority.

### Research Constraints And Boundaries
- `.planning/research/SUMMARY.md` — content-first architecture recommendation, Phase 1 rationale, and the main product-shape pitfalls to avoid.
- `.planning/research/PITFALLS.md` — especially Pitfalls 1, 2, 5, 8, and 14 covering thin schemas, fallback drift, ambiguous answer contracts, and delayed validation.
- `.planning/research/FEATURES.md` — v1 table stakes around authored packs, `circuit` and `venue` answer surfaces, reveal explanations, and anti-features.
- `.planning/research/ARCHITECTURE.md` — hard separation between authored content, pure rules, and live room orchestration; content compiler and snapshot expectations.
- `.planning/research/STACK.md` — file-first authoring direction, typed validation bias, and Street View optionality at the schema level.

### Discovery Grounding
- `discovery/14-gsd-seed.md` — consolidated initialization brief, authored-round direction, and preserved open questions.
- `discovery/10-critical-inheritance-geoguessr-core.md` — rejection of thin `lat/lng` rounds, unrestricted free-roam as default, and distance-only semantics.
- `discovery/11-circuit-coverage-audit.md` — venue classification rubric and fallback-first guidance for mixed-media round design.
- `discovery/04-modes.md` — anchor-mode clue ladder pattern and answer-surface shape.
- `discovery/06-open-questions.md` — preserved uncertainty around clue families, authoring threshold, and answer-surface depth.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- No application runtime code exists yet. The reusable assets for this phase are planning and research artifacts rather than components or utilities.
- Repo-local GSD workflow tooling under `.codex/get-shit-done` already provides phase-state, commit, and session-recording support for the planning workflow.

### Established Patterns
- The project is still greenfield; no frontend, backend, or content-package implementation patterns are established yet.
- Research artifacts consistently favor a split between content contract, pure rules, and room orchestration. The Phase 1 contract should preserve that separation.
- Environment guidance already assumes `corepack pnpm` rather than bare `pnpm` if package work begins during planning.

### Integration Points
- Phase 2 will consume the authored round and scoring contract in a pure rules engine.
- Phase 3 will consume validated content through frozen session snapshots rather than raw mutable authoring files.
- Phase 6 will depend on coverage classes, fallback declarations, and stable round identities for calibration and pack-mix analysis.

</code_context>

<specifics>
## Specific Ideas

- Best current clue ladder pattern: `ambient clue` -> `technical clue` -> `narrative clue`.
- Reveals should explain why the answer was identifiable, not only whether the player was correct.
- Early corpus planning should start with stronger `Allow` venues and deliberately authored fallback media for `Allow With Fallback` venues rather than pretending all circuits are equivalent.
- No specific UI or in-app authoring surface is required in this phase; standard typed-schema and file-workflow approaches remain acceptable.

</specifics>

<future_awareness>
## Future Awareness

- Phase 2 needs content and scoring contracts rich enough for deterministic judging and reveal payloads, but the contract should stay independent of room transport and UI concerns.
- Phase 3 needs validated authored content to become frozen session snapshots, so the contract should separate mutable authoring data from playable session data.
- Phase 6 will need pack-mix and calibration signals across venue classes, so coverage metadata, fallback strategy, and stable identifiers should not be afterthoughts.
- Future non-anchor F1 modes remain possible, so the contract should stay extensible enough for richer clue media and answer-target types without pulling those modes into current scope.
- The live-room runtime choice stays open until Phase 3 planning; Phase 1 should not couple content contracts to `Colyseus`, `PartyKit`, or any other transport-specific runtime.

</future_awareness>

<deferred>
## Deferred Ideas

- Internal authoring UI beyond file/import tooling — revisit once 2-3 packs expose repeated workflow pain.
- `section`, `corner`, and composite answer surfaces as active v1 content targets — keep schema extensibility, but treat gameplay rollout as later work unless a new phase is inserted.
- Broader adjacent F1 party modes — intentionally out of scope for Phase 1.
- Unrestricted Street View exploration or generic free-roam play — explicitly out of scope for this contract.

</deferred>

---

*Phase: 01-authored-round-contract*
*Context gathered: 2026-04-08*
