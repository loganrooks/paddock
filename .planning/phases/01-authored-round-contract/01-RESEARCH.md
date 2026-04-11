# Phase 1: Authored Round Contract - Research

**Researched:** 2026-04-11
**Domain:** Authored content contract, validation pipeline, and file-first pack workflow for F1 rounds
**Confidence:** HIGH

## Summary

Phase 1 is a content-contract phase, not an app-framework phase. The repository still has no application packages or runtime code, while the roadmap and context both say later rules, room, UI, and calibration work depend on a transport-agnostic authored substrate. The highest-leverage implementation path is therefore:

- checked-in file-authored content under `content/`
- shared domain schemas and normalization in `packages/domain`
- compile and validation tooling in `packages/content-tools`
- strict validation before any pack is considered playable

The key modeling choices that should be treated as settled for planning are:

- preserve explicit `venue -> circuit -> section -> corner` lineage even though v1 only ships `venue` and `circuit`
- freeze one canonical venue identifier and one canonical pack round-reference shape early
- separate clue semantics from media transport so Street View remains optional
- store coverage class and fallback posture explicitly in data rather than in author notes or asset naming

## Planning Recommendations

### Standard Stack

| Layer | Recommendation | Why |
|-------|----------------|-----|
| Authoring format | YAML source files | Human-editable, comment-friendly, and suitable for curated file-first content workflows |
| Runtime validation | Zod 4 | One schema source of truth for contracts, normalization boundaries, and later JSON Schema export |
| Tooling runtime | TypeScript + `tsx` | Simple repo-local CLIs without a prebuild step |
| Test framework | Vitest | Fast contract tests from the repo root and easy multi-package growth later |

### Structural Patterns

1. Keep `clueFamily` separate from `media.kind`.
This prevents fallback media from redefining the semantic clue family.

2. Use reusable venue profiles plus round-level overrides.
Coverage class and default fallback belong at the venue level; rounds should still be able to declare an explicit override when needed.

3. Compile authored files into canonical JSON before play.
Pack validation should reject broken or ambiguous content up front rather than letting runtime code discover invalid content later.

### Planning Implications

- Plan 01 should bootstrap workspace and freeze contract vocabulary before fixture authoring.
- Plan 02 should implement strict schemas, normalization, and contract tests.
- Plan 03 should author real venue and round fixtures that exercise the approved schema.
- Plan 04 should build the loader/compiler path and stable diagnostics that block broken content before play.

## Resolved For Planning

- Canonical venue identity should be one explicit field, not `id` plus `venueId` plus filename inference.
- Pack round references should use one explicit shape such as `{ roundId, path }`.
- The first scoring vocabulary should stay small and explicit rather than turning into a DSL in Phase 1.
- Bare `pnpm` should not be assumed available; use `corepack pnpm`.

## Still Open But Safe To Plan Around

- Whether coverage metadata lives only in venue profiles or in a hybrid venue-plus-round model.
- The exact authored source format details beyond “checked-in, declarative, and easy to validate.”
- The exact depth of reserved lineage fields beyond what Phase 1 needs for `venue` and `circuit`.

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Vitest |
| Config file | `vitest.config.ts` |
| Quick run command | `corepack pnpm run test:contract` |
| Full suite command | `corepack pnpm run test` |
| Estimated runtime | ~15 seconds |

### Phase Requirements -> Test Map

| Req ID | Behavior | Test Type | Automated Command |
|--------|----------|-----------|-------------------|
| `PACK-02` | Round fixtures require semantic answer target, accepted answers, clue steps, reveal explanation, and scoring profile | unit | `corepack pnpm exec vitest run tests/contract/round-contract.test.ts -t PACK-02` |
| `PACK-03` | Mixed Street View and non-Street-View clues compile through one round contract shape | unit | `corepack pnpm exec vitest run tests/contract/mixed-media-round.test.ts -t PACK-03` |
| `PACK-04` | Pack validation rejects broken or ambiguous authored content | integration | `corepack pnpm exec vitest run tests/contract/pack-validation.test.ts -t PACK-04` |
| `OPS-01` | Venue coverage class and fallback strategy resolve onto compiled output explicitly | unit | `corepack pnpm exec vitest run tests/contract/venue-profile-resolution.test.ts -t OPS-01` |

### Wave 0 Gaps

- Root `package.json`, `pnpm-workspace.yaml`, and `tsconfig.json`
- `vitest.config.ts`
- `packages/domain` and `packages/content-tools`
- Contract tests under `tests/contract/`

## Security Posture For This Phase

The relevant risk in Phase 1 is authored-content input handling, not auth or live-session security. Planning should therefore emphasize:

- strict object validation
- duplicate-key rejection in YAML parsing
- broken cross-file reference detection
- path traversal rejection for content inputs
- stable diagnostic codes for blocking validation failures

## Canonical Local Inputs

- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/research/SUMMARY.md`
- `.planning/research/ARCHITECTURE.md`
- `.planning/research/PITFALLS.md`
- `discovery/10-critical-inheritance-geoguessr-core.md`
- `discovery/11-circuit-coverage-audit.md`

---

## RESEARCH COMPLETE
