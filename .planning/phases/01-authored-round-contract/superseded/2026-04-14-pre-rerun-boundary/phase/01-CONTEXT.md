# Phase 1: Authored Round Contract - Context

**Gathered:** 2026-04-11
**Status:** Ready for planning

<domain>
## Phase Boundary

Define the authored pack and round substrate for the anchor mode, including answer-target vocabulary, clue-step structure, reveal semantics, validation rules, explicit venue/circuit identity, and media fallback handling. This phase establishes the content contract that later rules, room, UI, and calibration phases will consume. It does not implement live-room behavior, runtime judging, or end-user authoring UI.

</domain>

<decisions>
## Implementation Decisions

### Round And Pack Contract
- **D-01:** Model rounds as authored semantic objects, not thin `lat/lng + pano` records. A valid round contract must have first-class fields for answer target type, clue steps, accepted answers or aliases, reveal explanation, scoring profile, source references, and venue/circuit identity metadata.
- **D-02:** Model packs as curated authored collections of validated rounds with explicit pack metadata and stable content structure. Packs are not random point buckets or public UGC primitives.
- **D-03:** Freeze an explicit reference contract between pack entries and rounds early in Phase 1 so later compile and snapshot steps do not rely on filename-only inference or accidental ordering.

### Answer Surface And Identity Modeling
- **D-04:** Keep active v1 gameplay anchored at `circuit` and `venue`, while preserving explicit `venue -> circuit -> section -> corner` lineage in the authored model so later deeper answer surfaces do not require a flat-contract rewrite.
- **D-05:** Make venue and circuit identity explicit and canonical. Downstream implementation should converge on one stable identifier strategy rather than parallel `id`/`venueId`/filename conventions that force executors to invent resolution rules.
- **D-06:** Represent scoring intent as explicit round content now, even though runtime judging lands in Phase 2. Scoring semantics should not live only in UI copy or code comments.

### Clue Media And Fallback Modeling
- **D-07:** Use one provider-agnostic clue-step contract that can carry Street View and non-Street-View clue media without changing round shape.
- **D-08:** Treat Street View as an optional clue family, not the mandatory product substrate. The round contract must not become Google-specific.
- **D-09:** Keep `circuit_internal`, `circuit_edge`, `venue_approach`, and `city_context` as explicit clue-family distinctions so easier fallback or approach clues do not silently replace circuit-aware play.
- **D-10:** Record venue coverage class and fallback strategy as explicit content metadata rather than as implied author judgment hidden in media assets.

### Validation And Authoring Posture
- **D-11:** Reject incomplete, ambiguous, or broken content before it becomes playable, including missing answer-surface declaration, missing clue steps, missing accepted-answer data, missing reveal explanation, broken references, and undeclared fallback relationships.
- **D-12:** The first implementation should assume checked-in file-based authoring plus validation/import tooling rather than requiring an internal authoring UI before the schema is stable.

### the agent's Discretion
- Exact authored source format for packs and rounds (`yaml`, `json`, `ts`, or equivalent typed source), as long as the format is explicit, stable, and easy to validate.
- Exact package and workspace layout for domain schemas, content tooling, and compiler code.
- Exact naming shape for pack metadata and clue-step internals once the canonical identity and reference rules are frozen.

</decisions>

<working_model>
## Working Model & Assumptions

- The first implementation should prove the contract with checked-in fixture packs and importer or validator tooling before any database-backed or in-app authoring surface.
- Coverage and fallback data may begin as round-level fields, shared venue-profile data, or a hybrid, but planning should keep the media posture explicit and queryable either way.
- The first scoring-profile vocabulary should be rich enough to support Phase 2 rules fixtures and reveal semantics, but should avoid overfitting to unbuilt room or UI flows.

</working_model>

<derived_constraints>
## Derived Constraints

- The product is private-only and expert-first, so authored fidelity and fan-legible reveal logic matter more than generic quiz simplification.
- Circuit-internal recognition is the primary fantasy; venue-approach clues are secondary and must be modeled as such instead of becoming the hidden default.
- Phase 2 and Phase 3 depend on this contract staying transport-agnostic and UI-agnostic.
- Street View coverage is uneven and unstable across venues, so the contract must support non-Google clue media and explicit fallback declarations from the start.
- Later compile, snapshot, calibration, and pack-mix flows need stable round, venue, and circuit identifiers; this phase cannot leave core identity semantics implicit.
- There is no existing application runtime yet, so Phase 1 establishes the first reusable domain boundary for the project.

</derived_constraints>

<open_questions>
## Open Questions

- Should coverage and fallback metadata live directly on each round, in shared venue profiles, or in both places with overrides?
- How granular should the first scoring-profile vocabulary be in Phase 1: simple presets, fully parameterized rules, or a hybrid?
- How much answer-target lineage should be explicit now for later `section`, `corner`, and composite answers without making v1 authoring materially heavier?

</open_questions>

<epistemic_guardrails>
## Epistemic Guardrails

- Treat the discovery field lists as directional, not as a frozen schema. Validate the contract against multiple fixture round families before treating it as settled.
- Treat the coverage audit as venue-strategy guidance, not proof that specific coordinates or panorama IDs are production-safe.
- Preserve the distinction between "the schema must allow future answer surfaces" and "v1 content must actively ship those answer surfaces now."
- Do not let convenience around public-road or fallback-heavy venues silently redefine the anchor mode away from circuit-aware play.

</epistemic_guardrails>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase Scope And Doctrine
- `.planning/ROADMAP.md` — Phase 1 goal, success criteria, scope boundary, and protected seams for the authored round contract.
- `.planning/REQUIREMENTS.md` — `PACK-02`, `PACK-03`, `PACK-04`, `OPS-01`, plus `SEAM-01`, `SEAM-04`, `DEF-01`, and `DEF-04` define the requirement surface and seam posture for this phase.
- `.planning/PROJECT.md` — private trusted-group posture, authored-round bias, geography fidelity, and current product center.
- `.planning/LONG-ARC.md` — durable doctrine on wrapper preservation, private-room posture, visibility ladder, and long-arc seam protection that Phase 1 must preserve without widening scope.
- `.planning/STATE.md` — current replanning status and explicit instruction to rerun discuss-phase for Phase 1 against refreshed canon.

### Research Constraints And Architectural Guidance
- `.planning/research/SUMMARY.md` — content-first architecture recommendation, Phase 1 rationale, and the main product-shape failures to avoid.
- `.planning/research/ARCHITECTURE.md` — hard separation between authored content, pure rules, and room orchestration; content compiler, snapshot, and contract expectations.
- `.planning/research/PITFALLS.md` — especially Pitfalls 1, 2, 5, 6, 8, 10, and 12 covering thin schemas, fallback drift, uneven media coverage, ambiguous answer contracts, room-authority separation, and round-type coupling risk.
- `.planning/research/FEATURES.md` — v1 table stakes around authored packs, `circuit` and `venue` answer surfaces, reveal explanations, and anti-features.
- `.planning/research/STACK.md` — file-first authoring direction, typed validation bias, and provider-neutral media posture.
- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md` — structural Phase 1 findings on venue identity ambiguity, reference-shape freezing, and the need to decide hierarchical answer targets early.
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md` — cross-model confirmation that Phase 1 needs explicit identity, pack reference, and answer-target structure rather than executor guesswork.

### Discovery Grounding
- `discovery/14-gsd-seed.md` — consolidated initialization brief, authored-round direction, and preserved open questions.
- `discovery/10-critical-inheritance-geoguessr-core.md` — rejection of thin `lat/lng` rounds, distance-only truth, and unrestricted free-roam as the default.
- `discovery/11-circuit-coverage-audit.md` — venue classification rubric and fallback-first guidance for mixed-media round design.
- `discovery/04-modes.md` — anchor-mode clue ladder pattern and answer-surface shape.
- `discovery/06-open-questions.md` — preserved uncertainty around clue families, authoring threshold, and answer-surface depth.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- No application runtime code exists yet. The reusable assets for this phase are the canonical planning, research, audit, and discovery documents rather than components or utilities.
- Repo-local GSD tooling under `.codex/get-shit-done` provides the planning workflow and phase-state mechanics, but not domain implementation.

### Established Patterns
- The project is still greenfield; no frontend, backend, package, or content-schema implementation patterns are established yet.
- Research artifacts consistently favor a split between content contract, pure rules, and room orchestration. Phase 1 should preserve that separation instead of baking room or UI assumptions into authored content.
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

### Protected Seams
- Preserve explicit `venue -> circuit -> section -> corner` relationships in the authored model even though v1 gameplay only requires `venue` and `circuit`.
- Keep authored content, pure judging rules, and room orchestration separable so later wrappers and room-runtime choices do not require a content-contract rewrite.
- Preserve authored content identity separately from later session snapshots, event/editorial wrappers, and other future context records so `pack` and `session` do not harden into the only durable nouns.
- Keep clue media provider-agnostic so Street View, static crops, map fragments, authored text, and other clue families can coexist without schema churn.
- Preserve stable identifiers and explicit pack-to-round references so later snapshots, calibration, sharing, wrapper reuse, and layered history records can depend on deterministic content identity.
- Preserve reveal semantics without implying one universal viewer surface so later host-screen plus private-device play or other topology-sensitive wrappers do not require a content-contract rewrite.

### Explicit Non-Decisions
- Do not decide public challenge surfaces, room runtime, account-backed persistence, or adjacent non-anchor modes in Phase 1.
- Do not decide persistent identity, room/group memory, or event-memory structures in Phase 1.
- Do not silently promote `section`, `corner`, or composite answers into active v1 gameplay scope just because the schema preserves room for them.
- Do not decide a full internal authoring product before the file-first contract and validation flow prove where the real authoring pain is.

### Current Posture
- This is a private-only, unofficial fan project for trusted-circle play with no public discovery, moderation, uptime, or paid-access obligation.
- The current product center is one expert-feeling authored geography-and-circuit anchor mode that supports later private-room play without adopting public-platform assumptions now.

### Future Shape Notes
- Later wrappers such as async challenges, solo practice, spectator-facing shells, or adjacent F1 party modes should be able to reuse the authored substrate if they are earned later.
- Future expansion should come from preserving shared vocabulary and seam quality now, not from importing later wrapper features into Phase 1 scope.

</future_awareness>

<deferred>
## Deferred Ideas

- Internal authoring UI beyond file/import tooling — revisit once repeated pack-authoring pain appears.
- `section`, `corner`, and composite answer surfaces as active v1 content targets — keep schema extensibility, but treat gameplay rollout as later work unless a new phase is inserted.
- Broader adjacent F1 party modes — intentionally out of scope for Phase 1.
- Unrestricted Street View exploration or generic free-roam play — explicitly out of scope for this contract.

</deferred>

---

*Phase: 01-authored-round-contract*
*Context gathered: 2026-04-11*
*Carry-forward updated: 2026-04-13 after Round 2B canon patch*
