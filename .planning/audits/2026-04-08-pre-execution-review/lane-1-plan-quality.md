# Lane 1: Phase 1 Plan Quality Audit

**Auditor:** Claude (Opus 4.6)
**Date:** 2026-04-08
**Scope:** Plans 01-01 through 01-04 for Phase 1 (Authored Round Contract)
**Baseline:** Committed plans at `3684c2e` plus uncommitted diffs

---

## Overall Verdict: READY WITH CAVEATS

The four plans form a coherent, executable sequence that correctly targets the Phase 1 success criteria and the four assigned requirements (PACK-02, PACK-03, PACK-04, OPS-01). The uncommitted diffs are genuine improvements that should be committed. However, there are several issues -- mostly warnings -- that should be resolved before or during execution to prevent executor confusion.

---

## Phase 1 Success Criteria Coverage

| Success Criterion | Covered By | Status |
|-------------------|-----------|--------|
| SC-1: Author can define a round with explicit answer target, clue steps, accepted answers/aliases, reveal, scoring profile | 01-01 (contracts), 01-02 (schemas + tests), 01-03 (fixtures) | Fully covered |
| SC-2: Pack can mix Street View and non-SV fallback media without changing round contract | 01-01 (MediaKind type), 01-02 (discriminated union), 01-03 (mixed-media fixtures) | Fully covered |
| SC-3: Pack validation rejects incomplete/ambiguous/broken rounds | 01-02 (schema rejection tests), 01-04 (cross-file validation + diagnostics) | Fully covered |
| SC-4: Content workflow records venue coverage class and fallback strategy | 01-01 (contract types), 01-02 (resolve helper), 01-03 (venue profiles), 01-04 (compiled output) | Fully covered |

**Requirement traceability:**

| Requirement | Plan(s) with `requirements:` tag | Implementation location |
|-------------|----------------------------------|------------------------|
| PACK-02 | 01-01, 01-02, 01-03 | 01-01 defines types, 01-02 enforces schemas + tests, 01-03 provides fixtures |
| PACK-03 | 01-01, 01-02, 01-03, 01-04 | 01-01 defines MediaKind, 01-02 creates discriminated union, 01-03 demonstrates mixed media, 01-04 compiles it |
| PACK-04 | 01-01, 01-04 | 01-01 reserves CLI path, 01-04 builds pack-level validation with diagnostic codes |
| OPS-01 | 01-01, 01-02, 01-03, 01-04 | 01-01 defines coverage/fallback types, 01-02 builds resolution, 01-03 authors profiles, 01-04 compiles resolved metadata |

All four Phase 1 requirements are covered. No gaps.

---

## Per-Plan Assessment

### Plan 01-01: Bootstrap workspace and shared content-contract interfaces

**Wave:** 1 (no dependencies)
**Verdict:** Good

Strengths:
- Correctly establishes the shared vocabulary before any schema or fixture work begins
- Freezes exact CLI script names, paths, and package structure
- The `NOT_IMPLEMENTED_PHASE_01` placeholder pattern is a clean approach for pinning root scripts early
- `read_first` entries all point to files that exist now

Issues:
- **(Note)** Plan 01-01 lists `PACK-04` in its `requirements` frontmatter, but its actual work (package scaffolding, type definitions, placeholder CLI) does not meaningfully advance PACK-04 beyond reserving the CLI path. This is not wrong but slightly overstates the plan's direct contribution to that requirement.
- **(Note)** The `key_links` entry linking `package.json` to `content/packs/starter-pack/pack.yaml` is forward-looking -- that file will not exist until Plan 01-03 executes. This is acceptable for a link declaration (it documents intent, not runtime dependency), but an executor who tries to verify the link at plan-completion time will find the file missing.

### Plan 01-02: Strict domain schemas, normalization, and contract tests

**Wave:** 2 (depends on 01-01)
**Verdict:** Good

Strengths:
- TDD-first approach: tests are written before implementation (Task 1 then Task 2)
- Directly maps test files to requirement IDs (PACK-02, PACK-03, OPS-01) for traceability
- `read_first` entries point to existing planning files plus `packages/domain/src/contracts.ts`, which will exist after 01-01 executes (correct chain dependency)
- The `@context` block correctly references `packages/domain/src/contracts.ts` which 01-01 creates

Issues:
- **(Warning)** The `@context` block at line 71 lists `discovery/11-circuit-coverage-audit.md` but the `read_first` for Task 1 (line 79) also includes it. The `@context` reference at line 72 lists `discovery/10-critical-inheritance-geoguessr-core.md` but this file is not in the `read_first` for Task 1 (which uses `01-VALIDATION.md` instead). This is inconsistent but not blocking -- the executor gets the file through `@context` either way.

### Plan 01-03: Venue profiles and starter-pack YAML fixtures

**Wave:** 3 (depends on 01-02)
**Verdict:** Good with one warning

Strengths:
- Clear separation: Task 1 creates venue profiles, Task 2 creates the pack and round fixtures
- Explicit requirement to mirror the "implemented schema" from Plan 01-02 rather than guessing
- Acceptance criteria are concrete and grep-verifiable
- The three venue examples cover all three coverage classes (allow, allow_with_fallback, fallback_first)

Issues:
- **(Warning)** `read_first` for both tasks includes `packages/domain/src/schemas.ts` and `packages/domain/src/normalize.ts`. These files will exist after Plan 01-02 executes, which is correct given the dependency chain. However, `packages/domain/src/contracts.ts` is referenced in the `@context` block (line 67) but NOT in `read_first` for either task. The executor should probably read the contracts file too since it defines the exact type vocabulary.
- **(Note)** The plan does not include any schema-validation step in its `<verify>` blocks. The verify commands only check that files exist and contain expected strings via `rg`. There is no `corepack pnpm exec tsc -b` or schema parse validation. The actual schema validation of these YAML files will only happen in Plan 01-04. This is intentional (the YAML compiler does not exist yet) but means Plan 01-03 fixtures could have schema errors that go undetected until Plan 01-04 runs.

### Plan 01-04: YAML compiler, invariant checks, and compile CLI

**Wave:** 4 (depends on 01-02 AND 01-03)
**Verdict:** Good with one warning

Strengths:
- Dual dependency on both 01-02 and 01-03 is correct -- it needs both the domain schemas and the authored fixtures
- Path traversal defense via `pathPolicy.ts` is a thoughtful security-by-default choice
- Diagnostic codes are explicit and enumerated (`DUPLICATE_YAML_KEY`, `BROKEN_ROUND_REFERENCE`, `ALIAS_CONFLICT`, `MISSING_FALLBACK_STRATEGY`)
- Fixture comparison test (`diff -u` against expected JSON) ensures compiled output stability

Issues:
- **(Warning)** The `@context` block (lines 73-79) lists `@packages/domain/src/contracts.ts`, `@packages/domain/src/schemas.ts`, `@packages/domain/src/normalize.ts`, and four `@content/` files. All of these are created by earlier plans, which is correct. However, the `read_first` entries for both tasks do NOT include any of these domain or content files -- they only reference planning/discovery documents. This means the executor must rely on the `@context` mechanism to receive these files. If the executor implementation treats `@context` and `read_first` differently (e.g., `@context` is optional background and `read_first` is mandatory pre-reading), the executor could miss critical implementation details.

---

## Cross-Plan Consistency Check

### Contract Shape Consistency

| Concept | 01-01 | 01-02 | 01-03 | 01-04 | Consistent? |
|---------|-------|-------|-------|-------|-------------|
| Answer targets: `circuit`, `venue` | `SupportedV1AnswerTarget` type | Schema with literal guards | YAML fixtures use `kind: circuit` / `kind: venue` | Compiled output preserves | Yes |
| Clue families: 4 literals | `ClueFamily` type | Schema enum | YAML fixtures use them | N/A (pass-through) | Yes |
| Media kinds | `MediaKind` type with `map_fragment` | Schema discriminated union with `map_fragment` | YAML fixtures use `media.kind` | N/A (pass-through) | Yes |
| Coverage classes: 3 values | `CoverageClass` type | Schema + resolution helper | Venue YAML profiles | Compiled output carries resolved | Yes |
| Fallback strategies: 3 values | `FallbackStrategy` type | Resolution helper | Venue defaults + round overrides | Compiled output carries resolved | Yes |
| Scoring profile kinds | `circuit_standard`, `venue_standard` | Discriminated union | YAML fixtures | Compiled output preserves | Yes |
| Venue media capabilities: 7 keys | Exact boolean keys listed | Schema requires all 7 | YAML fixtures use them | N/A (pass-through) | Yes |

**No cross-plan contract inconsistencies found.** The vocabulary is frozen in 01-01 and consumed consistently through 01-02, 01-03, and 01-04.

### Naming Consistency: `map_snippet` vs `map_fragment`

**(Warning)** The RESEARCH.md code example at line 142 uses `map_snippet` as the media kind literal. All four plans consistently use `map_fragment` instead. The plans should be considered authoritative since they were written after the research and explicitly freeze the vocabulary. However, if an executor reads the research example code and copies the pattern, they may introduce `map_snippet` instead of `map_fragment`. This is a documentation-level inconsistency in the research file, not in the plans themselves.

### File Production Chain

```
01-01 creates: packages/domain/src/contracts.ts, packages/content-tools/src/cli.ts (placeholder), workspace infra
01-02 creates: packages/domain/src/schemas.ts, packages/domain/src/normalize.ts, packages/domain/src/json-schema.ts, tests/contract/*.test.ts
01-03 creates: content/venues/*.yaml, content/packs/starter-pack/**
01-04 creates: packages/content-tools/src/{pathPolicy,loadYaml,contentGraph,compilePack}.ts, replaces cli.ts placeholder
```

The chain is clean. Each plan's `depends_on` correctly reflects which prior plan creates the files it needs.

---

## Assessment of Uncommitted Diffs

### 01-02-PLAN.md diff: Rewritten `must_haves.truths`

**Change:** Three truths rewritten from implementation-internal language ("The domain package can express semantic rounds...") to author-facing language ("Authors can define a round with explicit answer target...").

**Assessment: Improvement.** The new language directly mirrors the PACK-02 requirement text and Phase 1 success criteria SC-1. The old language was technically accurate but tested an implementation detail rather than the requirement.

### 01-03-PLAN.md diff: Media key alignment

**Changes:**
1. Minor wording cleanup in Task 2 action text (removed "and any authored asset-path fields" from a list)
2. Strengthened verification command: added `rg -nU "media:\n\s+kind: street_view"` and `rg -nU "media:\n\s+kind: (image|map_fragment)"` checks
3. Changed acceptance criterion from `mediaKind: street_view` (flat) to `clueSteps[*].media.kind: street_view` (nested)

**Assessment: Improvement.** This aligns the plan with the research recommendation to use a nested discriminated `media` union under each `clueSteps[]` entry. The old flat `mediaKind` wording was inconsistent with the schema pattern established in 01-02 (discriminated union on `media.kind`). The new multiline `rg -nU` verification commands correctly detect the nested YAML structure.

### 01-04-PLAN.md diff: Test file addition and diagnostic cleanup

**Changes:**
1. Added `tests/contract/content-graph-loading.test.ts` to `files_modified` frontmatter
2. Added the test file to Task 1's `<files>` and `<action>` text
3. Changed Task 1 verify from `corepack pnpm exec tsc -b` only to `corepack pnpm exec vitest run tests/contract/content-graph-loading.test.ts && corepack pnpm exec tsc -b`
4. Added acceptance criterion: the test file must contain `loadPackGraph` and a path-policy failure assertion
5. Removed `UNSAFE_ASSET_PATH` from the diagnostic code list in Task 2's behavior, action, and acceptance criteria

**Assessment: Improvement.** The addition of a dedicated `content-graph-loading.test.ts` file for Task 1 closes a verification gap -- previously Task 1 had no test and relied only on `tsc -b`. Removing `UNSAFE_ASSET_PATH` is justified: the `pathPolicy.ts` module already rejects dangerous paths at the loader level (Task 1), so emitting a redundant diagnostic code at the validate/compile level (Task 2) would create confusion about where path safety is enforced.

### Overall diff verdict

**All three uncommitted diffs are improvements. They should be committed.**

---

## Issues Summary

### Blockers

None.

### Warnings

| # | Plan | Issue | Impact | Recommendation |
|---|------|-------|--------|----------------|
| W1 | 01-03 | No schema validation in verify blocks -- YAML fixture correctness is not checked until Plan 01-04 | If fixtures have structural errors, they will not be caught until one plan later | Accept as-is. Adding schema validation to 01-03 would require the compiler (which does not exist yet). The risk is low because 01-04 depends on 01-03 and will immediately exercise the fixtures. |
| W2 | 01-04 | `read_first` entries omit domain/content files that appear in `@context`; executor must get them through context injection | If context injection fails or is treated differently from `read_first`, executor may lack implementation context | Add `packages/domain/src/schemas.ts` and `packages/domain/src/normalize.ts` to `read_first` for both tasks in 01-04, since these are the most critical implementation references. |
| W3 | Research | `map_snippet` in RESEARCH.md code example vs `map_fragment` everywhere in plans | Executor reading research code might copy wrong literal | Leave as-is for plans (they are correct). Optionally fix RESEARCH.md to use `map_fragment` for consistency, but this is low priority since executors should follow plans over research. |
| W4 | 01-03 | `@context` references `packages/domain/src/contracts.ts` but `read_first` for both tasks omits it | Executor may not read the foundational type file before authoring YAML | Add `packages/domain/src/contracts.ts` to `read_first` for at least one task in 01-03. |

### Notes

| # | Plan | Observation |
|---|------|-------------|
| N1 | 01-01 | `requirements: [PACK-02, PACK-03, PACK-04, OPS-01]` is slightly overscoped -- 01-01's actual deliverables are workspace scaffolding and type definitions, not requirement fulfillment. The attribution is directionally correct (it lays groundwork for all four) but claiming PACK-04 is generous. |
| N2 | 01-01 | `key_links` reference to `content/packs/starter-pack/pack.yaml` documents intent for a file created two plans later. An executor checking links at plan-completion time will find it missing. |
| N3 | All | Every task's `read_first` includes `AGENTS.md` as the first entry. This is good practice -- it ensures the executor respects repo-level constraints. |
| N4 | 01-02 | Plan uses TDD flag (`tdd="true"`) on both tasks. This is well-aligned with the test-first approach described in the action text. |
| N5 | 01-04 | The `diff -u` fixture comparison in Task 2's verify command is a strong approach for compiled-output stability testing. |

---

## Recommendations

1. **Commit the uncommitted diffs.** All three are genuine improvements from checker feedback. They fix media-key naming, add missing test coverage, and remove a redundant diagnostic code.

2. **Consider adding key domain files to `read_first` in Plans 01-03 and 01-04.** Specifically:
   - Add `packages/domain/src/contracts.ts` to at least one `read_first` in Plan 01-03
   - Add `packages/domain/src/schemas.ts` and `packages/domain/src/normalize.ts` to `read_first` in Plan 01-04 tasks

3. **No rework needed.** The plans are execution-ready. The warnings above are recommendations for belt-and-suspenders hardening, not blockers.

4. **During execution, monitor for the `map_snippet`/`map_fragment` inconsistency.** If an executor produces code using `map_snippet`, it should be caught by the strict schema validation in Plan 01-02 (which freezes `map_fragment`), but awareness reduces debugging time.

5. **The `.continue-here.md` file was deleted in the uncommitted diff.** This is correct -- it belongs to the old handoff state and is superseded by the newer `.continue-here-2026-04-08-codex-runtime-handoff.md`. The deletion should be committed alongside the plan fixes.

---

## Conclusion

Phase 1's four plans are well-structured, correctly sequenced, and aligned with the roadmap success criteria and assigned requirements. The troubled Codex session produced plans that, despite the orchestration failures, are substantively sound. The uncommitted checker-feedback diffs are all improvements. The plans are ready for execution.

*Audit completed: 2026-04-08*
