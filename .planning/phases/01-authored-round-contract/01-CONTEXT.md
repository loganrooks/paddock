# Phase 1: Authored Round Contract - Context

**Gathered:** 2026-04-11
**Status:** Ready for planning

<domain>
## Phase Boundary

Define the authored pack and round substrate for the anchor mode, including answer-target structure, clue-step vocabulary, reveal semantics, explicit fallback-media handling, and compile-time validation strong enough that later rules, room, UI, and calibration phases inherit stable content rather than improvising around ambiguous fixtures. This phase establishes the authored content contract and compiler boundary. It does not implement live-room behavior, public challenge surfaces, runtime judging execution, or an end-user authoring product.

</domain>

<decisions>
## Implementation Decisions

### Authored Round And Pack Substrate
- **D-01:** Model rounds as authored semantic objects, not thin `lat/lng + pano` records. A valid round contract must carry first-class answer-target meaning, clue steps, accepted answers or aliases, reveal explanation, scoring profile, and venue/circuit identity semantics.
- **D-02:** Keep active v1 answer surfaces anchored at `circuit` and `venue`, but preserve the explicit relationship chain `venue -> circuit -> section -> corner` in the schema boundary instead of flattening everything to coordinates or unrelated labels.
- **D-03:** Model packs as curated authored collections with stable round identity and explicit pack structure suitable for later session snapshotting, replay, and calibration work.

### Clue Media And Coverage Posture
- **D-04:** Use one provider-agnostic mixed-media clue contract that separates clue semantics from media transport, so `circuit_internal`, `circuit_edge`, `venue_approach`, and `city_context` remain explicit even when the media kind changes.
- **D-05:** Treat Street View as optional clue media, not the product substrate. The contract must support Street View, image, map fragment, text, and fallback-first venues without silently redefining the game.
- **D-06:** Record venue coverage class and fallback strategy as explicit, queryable content data. Easier venue-approach or fallback-heavy clues must not silently replace circuit-aware play.

### Validation And Compile Contract
- **D-07:** Reject incomplete, ambiguous, or broken content before it becomes playable. This includes missing answer-surface declaration, unresolved references, missing reveal/scoring data, alias ambiguity, and undeclared or broken fallback relationships.
- **D-08:** The validation/compiler path must make content identity and reference resolution explicit enough that planning can freeze one canonical venue/round/pack reference system and emit stable diagnostics for broken authored content.
- **D-09:** Represent scoring as explicit authored configuration now, even though runtime judging lands in Phase 2.
- **D-10:** First implementation should use checked-in file authoring plus compiler/import tooling rather than an internal authoring UI.

### Future-Aware Phase 1 Posture
- **D-11:** Phase 1 should absorb cheap future-preserving seams now where they directly protect the authored substrate: stable content identity, explicit hierarchy-aware answer targets, and compiled artifacts that later rules and rooms can trust.
- **D-12:** Phase 1 must stay anchor-first in shipped scope even while protecting later wrappers and adjacent-mode possibilities. Do not widen current content authoring into a broad multi-mode platform schema.

### the agent's Discretion
- Exact authored source format (`yaml`, `json`, `ts`, or equivalent) as long as it stays declarative enough for strict validation and curated editing.
- Exact validator/compiler package layout.
- Exact field names for canonical pack/round/venue identifiers once one reference system is frozen.
- Exact representation of tags, content hash/version metadata, and other cheap seam-protection fields.

</decisions>

<working_model>
## Working Model & Assumptions

- Current best assumption: venue profiles should hold canonical coverage posture, while rounds should carry resolved fallback expectations or overrides so authored packs remain locally inspectable and later calibration can reason at round granularity.
- Current best assumption: compiled playable artifacts should be distinct from raw authored source so later room snapshots, validation, and calibration operate on normalized content rather than mutable author files.
- Current best assumption: hierarchy-aware answer targets are worth protecting in Phase 1 even if most early authored rounds only ship `venue` and `circuit` answer surfaces.

</working_model>

<derived_constraints>
## Derived Constraints

- The product center is a private, browser-first, watchable F1 game-night ritual for trusted groups, so authored fidelity and reveal quality matter more than public-platform convenience.
- Circuit-internal recognition remains the primary fantasy; venue-approach clues are a secondary explicit family, not a silent replacement.
- There is still no application runtime code or package manifest in the repo, so this phase must establish the first concrete domain boundary and project structure rather than plugging into an existing app.
- Phase 2 needs deterministic judging inputs, Phase 3 needs frozen session snapshots, and Phase 6 needs calibration-ready metadata; Phase 1 cannot leave identity, fallback posture, or core authored semantics implicit.
- The shared content substrate must remain transport-agnostic and UI-agnostic. It cannot assume a room runtime, controller shape, or host-screen rendering model.
- Long-arc doctrine now explicitly protects later wrappers, visibility-state separation, and browser-first private hosting posture, but those future concerns must constrain seams rather than expand current scope.

</derived_constraints>

<open_questions>
## Open Questions

- Should coverage and fallback metadata live primarily in shared venue profiles, primarily on rounds, or in a hybrid model with explicit round-level resolution?
- How rich should the initial scoring-profile vocabulary be in Phase 1: presets, parameterized rules, or a hybrid that stays readable to authors?
- How much structure beyond the explicit `venue -> circuit -> section -> corner` hierarchy should be encoded now for future sibling modes without making anchor-mode authoring meaningfully heavier?

</open_questions>

<epistemic_guardrails>
## Epistemic Guardrails

- Treat the coverage audit as strategy guidance, not production proof of exact playable coordinates or panorama safety.
- Treat the audit’s structural findings as pressure on replanning, not as proof that exact schema field names or compiler APIs are already decided.
- Validate any hierarchy-aware answer-target model against actual authored fixtures before treating it as settled ergonomics.
- Preserve the distinction between "protect a future seam now" and "import future feature scope now." Adjacent modes, public challenges, and spectator shells remain deferred.
- Do not let fallback-heavy or venue-approach-friendly venues redefine the anchor mode away from authored circuit-aware recognition.

</epistemic_guardrails>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase Scope And Canon
- `.planning/ROADMAP.md` — Phase 1 goal, success criteria, protected seams, and the current milestone sequencing.
- `.planning/REQUIREMENTS.md` — `PACK-02`, `PACK-03`, `PACK-04`, `OPS-01`, plus `SEAM-01`, `SEAM-04`, `DEF-01`, and `DEF-04` that constrain how Phase 1 should preserve future seams without widening scope.
- `.planning/PROJECT.md` — product center, anchor-versus-platform posture, expert-fan bias, and the current private trusted-room framing.
- `.planning/STATE.md` — current project position, rerun requirement, and canonical note that the superseded Phase 1 snapshot is not authoritative.
- `.planning/LONG-ARC.md` — durable doctrine for long-arc product shape, visibility ladder, hosting ladder, and seam preservation.

### Current Rerun Inputs
- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md` — cross-lane pre-execution findings that triggered the Phase 1 rerun.
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md` — strongest convergent findings and GPT-unique structural gaps relevant to Phase 1 replanning, especially hierarchical answer targets and identity ambiguity.

### Research And Discovery Grounding
- `.planning/research/SUMMARY.md` — content-first architecture rationale and main product-shape pitfalls.
- `.planning/research/PITFALLS.md` — pitfalls around thin schemas, fallback drift, ambiguous answer contracts, and delayed validation.
- `.planning/research/ARCHITECTURE.md` — separation between authored content, pure rules, and room orchestration.
- `discovery/14-gsd-seed.md` — initialization brief for the authored anchor-mode and party-platform tension.
- `discovery/04-modes.md` — anchor-mode clue ladder and answer-surface design space.
- `discovery/06-open-questions.md` — preserved uncertainty around product shape, watchability, authoring burden, and answer-surface depth.
- `discovery/10-critical-inheritance-geoguessr-core.md` — rejection of thin geography inheritance and distance-only semantics.
- `discovery/11-circuit-coverage-audit.md` — venue classification rubric and fallback-first corpus strategy.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- No application runtime code exists yet. The reusable assets for this phase are planning, research, and discovery artifacts rather than components or utilities.
- Repo-local GSD workflow tooling under `.codex/get-shit-done` already provides phase-state, commit, and workflow orchestration support.

### Established Patterns
- The repo is still greenfield from an implementation standpoint; there is no established frontend, backend, or package layout to conform to yet.
- Current canon consistently prefers separation between authored content, pure rules, and room/session orchestration.
- Environment guidance already assumes `corepack pnpm` rather than bare `pnpm` if package work begins.

### Integration Points
- Phase 2 will consume the authored contract in a pure judging/reveal engine.
- Phase 3 will consume compiled authored content through frozen session snapshots rather than raw mutable author files.
- Phase 3.1, Phase 4, and Phase 5 depend on the authored contract preserving clear answer-surface semantics and reveal payloads without UI coupling.
- Phase 6 will depend on stable IDs, coverage posture, fallback strategy, and calibration-ready content metadata.

</code_context>

<specifics>
## Specific Ideas

- Best current clue ladder pattern remains `ambient clue` -> `technical clue` -> `narrative clue`.
- Reveals should explain why the answer was identifiable, not only whether it was correct.
- Early corpus strategy should start with the strongest `Allow` venues, then add `Allow With Fallback` venues with deliberately authored fallback media instead of pretending all venues are equivalent.
- The authored content contract should support a watchable host-screen ritual later by making reveals and answer surfaces explicit, not by baking UI choices into the schema now.

</specifics>

<future_awareness>
## Future Awareness

### Protected Seams
- Preserve explicit `venue -> circuit -> section -> corner` relationships in the authored boundary.
- Keep authored source, compiled playable artifacts, judging inputs, and room/session presentation separable.
- Preserve stable round/pack/venue identity and version/hash-friendly compiled outputs for later snapshots, replay, and calibration.
- Keep clue-family semantics separate from media transport and fallback posture.

### Explicit Non-Decisions
- Do not decide the room runtime in Phase 1.
- Do not commit Phase 1 to active `section`, `corner`, or composite answer-surface gameplay rollout.
- Do not encode adjacent non-anchor F1 modes as first-class shipped Phase 1 scope.
- Do not choose public visibility, public leaderboards, or stronger service-obligation surfaces here.
- Do not require an internal authoring UI before the file-first contract proves itself.

### Current Posture
- Current posture is private-only, trusted-circle, browser-first play with modest service obligations and no public uptime or moderation commitment.
- The emotional center remains a watchable expert-fan game night rather than a generic public geography product.

### Future Shape Notes
- Later wrappers such as async challenges, solo practice, spectator shells, or sibling F1 party modes should remain possible if the substrate earns them, but current work should only protect seams for them.
- Phase 3 room-authority planning and Phase 3.1 UI contract work will inherit this substrate; Phase 1 should avoid hardcoding assumptions that force those later phases into one host/controller or deployment model.
- Calibration and content-ops phases will need richer metadata than raw correctness alone, so Phase 1 should prefer explicit authored meaning over thin fixture convenience.

</future_awareness>

<deferred>
## Deferred Ideas

- Internal authoring UI beyond file/compiler workflows.
- Active rollout of `section`, `corner`, and composite answer surfaces in v1 gameplay.
- Adjacent non-anchor F1 party modes, even if the substrate preserves room for them.
- Public challenge surfaces, public leaderboards, and spectator-facing product shells.
- Unrestricted Street View free-roam or generic geography-first play.

</deferred>

---

*Phase: 01-authored-round-contract*
*Context gathered: 2026-04-11*
