# Phase 1: Authored Round Contract - Research

**Researched:** 2026-04-08
**Domain:** Authored content contract, validation pipeline, and file-first pack workflow for F1 rounds
**Confidence:** HIGH

<user_constraints>
## User Constraints (from CONTEXT.md)

All items in this section are copied verbatim from `01-CONTEXT.md`. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

### Locked Decisions
- **D-01:** Model rounds as authored semantic objects, not thin `lat/lng + pano` records. A valid round contract must have first-class fields for answer target type, clue steps, accepted answers or aliases, reveal explanation, scoring profile, source references, and venue/circuit identity metadata.
- **D-02:** Model packs as curated authored collections of validated rounds with explicit pack metadata and stable content structure. Packs are not treated as random point buckets or public UGC primitives.
- **D-03:** Keep the active v1 answer-surface contract anchored at `circuit` and `venue`, while leaving the schema extensible enough for later `section`, `corner`, or composite targets.
- **D-04:** Use one provider-agnostic clue-step contract that can carry Street View and non-Street-View clue media without changing round shape.
- **D-05:** Treat Street View as an optional clue family, not the mandatory product substrate. The core round contract must not become Google-specific.
- **D-06:** Keep `circuit_internal`, `circuit_edge`, `venue_approach`, and `city_context` as explicit clue-family distinctions so easier fallback or approach clues do not silently replace circuit-aware play.
- **D-07:** Record venue coverage class and fallback strategy as explicit content metadata rather than as implied author judgment hidden in media assets.
- **D-08:** Reject incomplete or ambiguous content before it becomes playable, including missing answer-surface declaration, missing clue steps, missing accepted-answer data, missing reveal explanation, and undeclared or broken fallback relationships.
- **D-09:** Represent scoring as explicit content configuration in the round contract now, even though runtime judging lands in Phase 2. Scoring semantics should not live only in UI code or prose comments.
- **D-10:** Assume checked-in file-based authoring plus validation/import tooling for the first implementation of this contract rather than requiring an internal authoring UI before the schema is stable.

### Claude's Discretion
- Exact file format for authored packs and rounds (`json`, `yaml`, `ts`, or equivalent typed source)
- Exact validator/compiler package layout
- Exact naming and ID conventions, as long as they are explicit and stable across packs and rounds

### Deferred Ideas (OUT OF SCOPE)
- Internal authoring UI beyond file/import tooling — revisit once 2-3 packs expose repeated workflow pain.
- `section`, `corner`, and composite answer surfaces as active v1 content targets — keep schema extensibility, but treat gameplay rollout as later work unless a new phase is inserted.
- Broader adjacent F1 party modes — intentionally out of scope for Phase 1.
- Unrestricted Street View exploration or generic free-roam play — explicitly out of scope for this contract.
</user_constraints>

<phase_requirements>
## Phase Requirements

Requirement text is copied from `.planning/REQUIREMENTS.md`; research support is this document's planning guidance. [VERIFIED: .planning/REQUIREMENTS.md]

| ID | Description | Research Support |
|----|-------------|------------------|
| PACK-02 | Author can define a round with explicit answer target type, clue steps, accepted answers or aliases, reveal explanation, and scoring profile. | Use strict Zod schemas for `answerTarget`, `clueSteps`, `acceptedAnswers`, `reveal`, and `scoringProfile`, backed by fixture rounds and contract tests. [CITED: https://zod.dev/error-formatting][CITED: https://zod.dev/v4?id=introducing-zod-mini][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] |
| PACK-03 | A round can reference multiple clue media types, including Street View where available and non-Street-View fallback media where needed. | Separate `clueFamily` from `media.kind`, and use one discriminated `media` union so Street View, image, map snippet, and text clues share the same round contract. [CITED: https://zod.dev/v4?id=introducing-zod-mini][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] |
| PACK-04 | Pack validation rejects incomplete, ambiguous, or broken rounds before they become playable. | Add a compile step that checks both per-file schema validity and pack-level invariants such as unique IDs, existing references, alias conflicts, missing fallback metadata, and broken asset references. [CITED: https://zod.dev/error-formatting][VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] |
| OPS-01 | Content workflow records venue coverage class and fallback strategy so rounds do not assume uniform Street View viability. | Store canonical venue coverage in a venue profile and require each round to declare or resolve a fallback strategy explicitly before compile success. [VERIFIED: discovery/11-circuit-coverage-audit.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] |
</phase_requirements>

## Summary

Phase 1 is a content-contract phase, not an app-framework phase. The repository still has no application packages, no package manifest, and no test harness, while the phase brief and roadmap both say later rules, room, UI, and calibration work depend on a transport-agnostic authored substrate. [VERIFIED: repo file scan][VERIFIED: .planning/ROADMAP.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

Inference: the cleanest Phase 1 implementation is file-first YAML authoring compiled by Node/TypeScript tooling into validated canonical JSON artifacts, with Zod 4 as the contract source of truth and Vitest 4 guarding fixture regressions. YAML 2 supports comment-preserving document parsing, unique-key checks, and line/column-aware errors; Zod 4 supports strict objects, discriminated unions, registries, and first-party JSON Schema export; Vitest 4 supports root config plus `test.projects` for multi-package repositories and file/snapshot assertions for compiled fixtures. [CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/metadata][CITED: https://zod.dev/json-schema?id=registries][CITED: https://vitest.dev/config/][CITED: https://vitest.dev/guide/projects.html][CITED: https://vitest.dev/guide/snapshot.html]

The highest-leverage modeling choice is to keep semantic clue family separate from media transport, and to make venue coverage plus fallback posture explicit data instead of hidden author judgment. That directly aligns with PACK-03, PACK-04, OPS-01, the discovery coverage audit, and the phase constraint that fallback-heavy venues must be explicit instead of silent substitutions. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: discovery/11-circuit-coverage-audit.md]

**Primary recommendation:** Use declarative YAML source files under `content/`, validate them with Zod schemas in `packages/domain`, compile them with `packages/content-tools`, and model `clueFamily`, `media.kind`, `venueCoverage`, and `fallbackStrategy` as separate first-class fields. [CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/v4?id=introducing-zod-mini][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| TypeScript | `6.0.2` (published 2026-03-23) [VERIFIED: npm registry] | Shared domain types, compiler package boundaries, and CLI tooling | Project references are the standard TypeScript mechanism for splitting a codebase into smaller referenced pieces, which fits `domain` plus `content-tools` cleanly. [CITED: https://www.typescriptlang.org/docs/handbook/project-references] |
| Zod | `4.3.6` (published 2026-01-22) [VERIFIED: npm registry] | Runtime validation for round, pack, venue, and compiler output schemas | Zod 4 provides `z.strictObject`, upgraded `z.discriminatedUnion`, metadata registries, and first-party `z.toJSONSchema()`, which lets one schema drive validation and future tooling. [CITED: https://zod.dev/error-formatting][CITED: https://zod.dev/metadata][CITED: https://zod.dev/json-schema?id=registries][CITED: https://zod.dev/v4?id=introducing-zod-mini] |
| YAML | `2.8.3` (published 2026-03-21) [VERIFIED: npm registry] | Human-editable authoring format for pack, round, and venue files | The official `yaml` library supports YAML 1.1/1.2, `parseDocument()`, preserved comments/blank lines, `uniqueKeys`, `strict`, and line/column-aware error reporting. [CITED: https://eemeli.org/yaml/] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| tsx | `4.21.0` (published 2025-11-30) [VERIFIED: npm registry] | Run package-local TypeScript CLIs without a prebuild step | Use for `validate-pack`, `compile-pack`, and `check-fixtures` scripts during early file-first development. [ASSUMED] |
| Vitest | `4.1.3` (published 2026-04-07) [VERIFIED: npm registry] | Contract tests, fixture snapshots, and multi-package test orchestration | Use for schema acceptance tests, pack compile regression tests, and file snapshot checks of normalized outputs. [CITED: https://vitest.dev/config/][CITED: https://vitest.dev/guide/projects.html][CITED: https://vitest.dev/guide/snapshot.html] |
| @types/node | `25.5.2` (published 2026-04-03) [VERIFIED: npm registry] | Node typings for CLI/tooling packages | Use with TypeScript because this phase is filesystem and CLI heavy before any browser app exists. [VERIFIED: repo file scan][ASSUMED] |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| YAML source + compiled JSON | JSON source only | JSON is simpler to parse, but the official `yaml` docs explicitly provide comment-preserving documents and better author-facing error surfaces, which are more useful for curated pack editing. [CITED: https://eemeli.org/yaml/][ASSUMED] |
| YAML source + compiled JSON | TypeScript-authored content | TypeScript gives strong editor tooling, but executable content makes the contract less declarative and makes it easier to hide semantics in helper code rather than validated data. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED] |
| Zod 4 | Hand-written validators | Hand-written validation increases schema drift and loses first-party JSON Schema generation plus Zod's structured error formatting. [CITED: https://zod.dev/error-formatting][CITED: https://zod.dev/json-schema?id=registries] |

**Installation:**
```bash
corepack pnpm add -D typescript @types/node zod yaml tsx vitest
```

**Version verification:** Current package versions and publish dates were verified from the npm registry on 2026-04-08. [VERIFIED: npm registry]
```bash
npm view typescript version
npm view zod version
npm view yaml version
npm view tsx version
npm view vitest version
```

## Architecture Patterns

### Recommended Project Structure
```text
content/
├── venues/                    # canonical venue coverage and fallback profiles
│   └── monaco.yaml
└── packs/
    └── starter-pack/
        ├── pack.yaml          # pack metadata + ordered round refs
        └── rounds/
            ├── monaco-harbour-01.yaml
            └── spa-eau-rouge-01.yaml

packages/
├── domain/                    # Zod schemas, types, JSON Schema export
└── content-tools/             # parse/validate/compile CLI

tests/
├── contract/                  # schema and cross-file invariant tests
└── fixtures/                  # authored sample packs + expected compiled outputs
```
This layout follows the repo's file-first phase brief, the absence of any current app/runtime code, and TypeScript project-reference guidance for smaller referenced projects. [VERIFIED: repo file scan][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][CITED: https://www.typescriptlang.org/docs/handbook/project-references]

### Pattern 1: Separate Clue Semantics From Media Transport
**What:** Model `clueFamily` independently from `media.kind` so a `circuit_internal` clue can be delivered by Street View, image, map snippet, or text without changing the round contract. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**When to use:** Always for Phase 1; PACK-03 and D-04 through D-06 require one provider-agnostic clue-step contract and explicit clue-family distinctions. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**Example:**
```typescript
// Source APIs: https://zod.dev/error-formatting and https://zod.dev/v4?id=introducing-zod-mini
import * as z from "zod";

const clueMediaSchema = z.discriminatedUnion("kind", [
  z.strictObject({
    kind: z.literal("street_view"),
    panoRef: z.string().min(1),
    heading: z.number().optional(),
  }),
  z.strictObject({
    kind: z.literal("image"),
    assetId: z.string().min(1),
    alt: z.string().min(1),
  }),
  z.strictObject({
    kind: z.literal("map_snippet"),
    assetId: z.string().min(1),
  }),
  z.strictObject({
    kind: z.literal("text"),
    body: z.string().min(1),
  }),
]);

export const clueStepSchema = z.strictObject({
  id: z.string().min(1),
  family: z.enum([
    "circuit_internal",
    "circuit_edge",
    "venue_approach",
    "city_context",
  ]),
  media: clueMediaSchema,
  revealIntent: z.string().min(1),
});
```

### Pattern 2: Use A Venue Profile Plus Round-Level Resolved Fallback
**What:** Keep canonical coverage posture in a reusable venue profile, but require each round to carry a resolved fallback strategy or explicit override so OPS-01 is visible at the round level too. [VERIFIED: discovery/11-circuit-coverage-audit.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**When to use:** Use immediately if multiple rounds can target the same venue, which is likely for curated F1 packs. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED]

**Example:**
```yaml
# Source posture: discovery/11-circuit-coverage-audit.md and 01-CONTEXT.md
# content/venues/monaco.yaml
id: monaco
coverageClass: allow
defaultFallbackStrategy: street-view-primary
supportedFamilies:
  - circuit_edge
  - venue_approach
  - city_context

# content/packs/starter-pack/rounds/monaco-harbour-01.yaml
id: monaco-harbour-01
venueRef: monaco
coverageClass: allow
fallbackStrategy: street-view-primary
```

### Pattern 3: Compile Authored Files Into Canonical JSON Before Play
**What:** Parse YAML documents, validate with Zod, resolve cross-file references, and emit normalized JSON artifacts or reports before any pack is considered playable. [CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/error-formatting][CITED: https://zod.dev/json-schema?id=registries]

**When to use:** Always; D-08 and PACK-04 explicitly require rejection of incomplete, ambiguous, or broken rounds before play. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**Example:**
```typescript
// Source APIs: https://eemeli.org/yaml/ and https://zod.dev/error-formatting
import { readFile } from "node:fs/promises";
import { parseDocument, LineCounter } from "yaml";
import { z } from "zod";

const lineCounter = new LineCounter();
const roundSchema = z.strictObject({
  id: z.string().min(1),
  answerTarget: z.strictObject({
    type: z.enum(["circuit", "venue"]),
    canonical: z.string().min(1),
    aliases: z.array(z.string().min(1)).min(1),
  }),
});

export async function loadRound(path: string) {
  const source = await readFile(path, "utf8");
  const doc = parseDocument(source, {
    lineCounter,
    prettyErrors: true,
    strict: true,
    uniqueKeys: true,
  });

  if (doc.errors.length) return { ok: false, errors: doc.errors };

  const parsed = roundSchema.safeParse(doc.toJS());
  if (!parsed.success) return { ok: false, errors: z.treeifyError(parsed.error) };

  return { ok: true, round: parsed.data };
}
```

### Anti-Patterns to Avoid
- **Collapsing clue family into media kind:** A non-Street-View clue is not automatically `venue_approach` or easier; the semantic family must stay explicit. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]
- **Shape-only validation:** Validating each YAML file individually but skipping unique IDs, missing references, alias collisions, and fallback completeness will fail PACK-04 in practice. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]
- **Executable content as the source of truth:** Inference: TypeScript-authored packs make it easier to smuggle business logic into content helpers and harder to preserve a stable declarative contract for later tools. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED]
- **Hidden coverage posture:** If coverage class or fallback strategy only live in asset names, comments, or author memory, OPS-01 and later calibration work will have no reliable data to consume. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: discovery/11-circuit-coverage-audit.md]

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| File parsing | A custom YAML parser or regex-based field loader | `yaml` | The official library already handles YAML 1.1/1.2, `parseDocument()`, error arrays, comments, `uniqueKeys`, and line/column reporting. [CITED: https://eemeli.org/yaml/] |
| Runtime validation | Ad hoc `if` chains spread across compiler code | Zod 4 | `z.strictObject`, discriminated unions, registries, and first-party JSON Schema export keep contract logic centralized. [CITED: https://zod.dev/error-formatting][CITED: https://zod.dev/metadata][CITED: https://zod.dev/json-schema?id=registries] |
| Regression diffing | Custom JSON diff scripts for compiled outputs | Vitest snapshots / file snapshots | Official snapshot support is enough for compile-output regression tests and error-report fixtures. [CITED: https://vitest.dev/guide/snapshot.html][CITED: https://vitest.dev/api/expect.html] |
| Package orchestration | One giant root-only TypeScript project | TypeScript project references | References are the standard way to split domain and tooling packages without losing type safety. [CITED: https://www.typescriptlang.org/docs/handbook/project-references] |

**Key insight:** The risky complexity in this phase is schema drift, ambiguous content, and poor validation reporting, not parser novelty; use mature libraries for those edges and keep project-specific effort on the authored round vocabulary. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/error-formatting]

## Common Pitfalls

### Pitfall 1: Letting `media.kind` redefine the game mode
**What goes wrong:** The pack contract silently treats Street View rounds as the "real" anchor mode and fallback media as second-class exceptions. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**Why it happens:** Media provider and clue semantics get collapsed into one enum or one authoring shortcut. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**How to avoid:** Keep `clueFamily` and `media.kind` separate, and validate both independently. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**Warning signs:** Schema reviews or fixtures talk only about `street_view` versus `image` and never about `circuit_internal` versus `venue_approach`. [ASSUMED]

### Pitfall 2: Recording coverage only as author intuition
**What goes wrong:** Later packs cannot tell whether a round is fallback-first by design or by accident, so OPS-01 and calibration become guesswork. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: discovery/11-circuit-coverage-audit.md]

**Why it happens:** Coverage class and fallback strategy live in notes, filenames, or memory instead of first-class fields. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**How to avoid:** Require venue coverage plus fallback posture in source data and fail compile if either is missing. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**Warning signs:** Authors can add a non-Street-View clue without explaining whether it is a fallback, a deliberate clue family choice, or a permanent venue limitation. [VERIFIED: discovery/11-circuit-coverage-audit.md][ASSUMED]

### Pitfall 3: Validating file shape but not pack invariants
**What goes wrong:** Every YAML file parses successfully, but the pack is still broken because of duplicate IDs, missing referenced rounds, ambiguous aliases, or undeclared fallback relationships. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**Why it happens:** Teams stop at per-file schema validation and never add a compile phase that sees the whole pack graph. [ASSUMED]

**How to avoid:** Split validation into two passes: schema parse, then cross-file invariant checks with a compiled report. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED]

**Warning signs:** The contract test suite has round fixtures but no pack fixture containing multiple rounds and venue profiles. [VERIFIED: repo file scan][ASSUMED]

### Pitfall 4: Overfitting scoring before Phase 2 exists
**What goes wrong:** Phase 1 spends time building a mini rules DSL instead of declaring explicit but minimal scoring configuration. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**Why it happens:** The phase correctly wants scoring to be explicit now, but the runtime judging engine still belongs to Phase 2. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/ROADMAP.md]

**How to avoid:** Use a small discriminated union of scoring profile kinds with explicit parameters and examples, not a general-purpose rule language. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED]

**Warning signs:** Authors need expressions, scripts, or arbitrary callback hooks just to encode ordinary `circuit` or `venue` identity scoring. [ASSUMED]

## Code Examples

Verified patterns from official sources:

### Zod 4 Strict Schema + JSON Schema Export
```typescript
// Source: https://zod.dev/json-schema?id=registries
import * as z from "zod";

const roundSchema = z.strictObject({
  id: z.string(),
  answerTarget: z.strictObject({
    type: z.enum(["circuit", "venue"]),
    canonical: z.string(),
  }),
});

const roundJsonSchema = z.toJSONSchema(roundSchema);
```

### YAML Document Parsing With Structured Errors
```typescript
// Source: https://eemeli.org/yaml/
import { LineCounter, parseDocument } from "yaml";

const lineCounter = new LineCounter();
const doc = parseDocument(sourceText, {
  lineCounter,
  prettyErrors: true,
  strict: true,
  uniqueKeys: true,
});

if (doc.errors.length > 0) {
  return doc.errors;
}
```

### Vitest File Snapshot For Compiled Output
```typescript
// Source: https://vitest.dev/api/expect.html
import { expect, it } from "vitest";

it("emits stable compiled pack json", async () => {
  const compiled = JSON.stringify(result, null, 2);
  await expect(compiled).toMatchFileSnapshot("./fixtures/expected-pack.json");
});
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `schema.strict()` on an already-created Zod object | `z.strictObject(shape)` as the explicit strict constructor [CITED: https://zod.dev/v4?id=introducing-zod-mini] | Zod 4 [CITED: https://zod.dev/v4?id=introducing-zod-mini] | Prefer the explicit constructor in new Phase 1 schemas to avoid deprecated-style patterns. [CITED: https://zod.dev/v4?id=introducing-zod-mini] |
| Third-party JSON Schema generation around Zod | First-party `z.toJSONSchema()` [CITED: https://zod.dev/json-schema?id=registries] | Zod 4 [CITED: https://zod.dev/v4?id=introducing-zod-mini] | One schema can now drive validation, future docs, and possible authoring-tool contracts. [CITED: https://zod.dev/json-schema?id=registries] |
| Legacy Vitest workspace naming | `test.projects` in root config [CITED: https://vitest.dev/guide/projects.html] | Current official docs use `test.projects`; the legacy cutoff was not re-verified in this session. [CITED: https://vitest.dev/guide/projects.html][ASSUMED] | Use `test.projects` for `packages/*` from the start; do not introduce legacy workspace config. [CITED: https://vitest.dev/guide/projects.html] |

**Deprecated/outdated:**
- Using Zod's older object strictness style as the default recommendation is outdated for new code; prefer `z.strictObject()` in Phase 1 contracts. [CITED: https://zod.dev/v4?id=introducing-zod-mini]
- Using legacy Vitest workspace naming is outdated for new configs; use `projects`. [CITED: https://vitest.dev/guide/projects.html]

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | YAML is the best initial authoring source over JSON or TypeScript for this repo's first pack workflow. [ASSUMED] | Standard Stack | The planner may over-commit to YAML when the team really wants TS-authored fixtures or spreadsheet export. |
| A2 | A minimum two-package split of `packages/domain` and `packages/content-tools` is the right Wave 0 repo shape. [ASSUMED] | Architecture Patterns | The planner could create more package structure than Phase 1 really needs, adding setup overhead. |
| A3 | Venue coverage should be modeled as a shared venue profile plus round-level resolved fallback posture, not only one or the other. [ASSUMED] | Architecture Patterns | The planner may choose a hybrid model that feels heavier than necessary for the initial corpus. |

## Open Questions

1. **Should venue profiles be global from day one or pack-local at first?**
   What we know: every round must surface coverage class and fallback strategy explicitly, and later calibration phases need stable venue metadata. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]
   What's unclear: whether Phase 1 will author enough packs or reused venues to justify `content/venues/*.yaml` immediately. [VERIFIED: repo file scan][ASSUMED]
   Recommendation: if Phase 1 includes more than one pack or repeated venues, create global venue profiles now; otherwise allow one pack-local venue profile file, but compile to the same resolved round shape either way. [ASSUMED]

2. **How small can the first scoring vocabulary stay without blocking Phase 2?**
   What we know: scoring must be explicit now, but the judging engine is Phase 2 work. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/ROADMAP.md]
   What's unclear: whether one preset is enough or whether Phase 2 needs at least separate `circuit` and `venue` profile kinds from the start. [ASSUMED]
   Recommendation: plan for a tiny discriminated union of scoring profile kinds plus fixture examples, and defer any expression-based or generalized rule DSL. [ASSUMED]

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Node.js | TypeScript compiler and content-tool CLIs | ✓ [VERIFIED: local environment] | `22.22.1` [VERIFIED: local environment] | Node 22 is currently Maintenance LTS and Node 24 is Active LTS upstream, so the local runtime is acceptable for this phase. [CITED: https://nodejs.org/en/about/previous-releases/] |
| npm | Package install and registry checks | ✓ [VERIFIED: local environment] | `10.9.4` [VERIFIED: local environment] | — |
| corepack | Repo-preferred package-manager invocation | ✓ [VERIFIED: local environment] | `0.34.6` [VERIFIED: local environment] | — |
| pnpm | Workspace package manager | ✗ bare command [VERIFIED: local environment] | — | Use `corepack pnpm`, which is available as `10.33.0`. [VERIFIED: local environment] |
| Git | GSD commit flow and fixture history | ✓ [VERIFIED: local environment] | `2.43.0` [VERIFIED: local environment] | — |

**Missing dependencies with no fallback:**
- None. [VERIFIED: local environment]

**Missing dependencies with fallback:**
- Bare `pnpm` is not on `PATH`; use `corepack pnpm` everywhere in this repo. [VERIFIED: local environment][VERIFIED: AGENTS.md]

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | None yet in-repo; recommend Vitest `4.1.3` as Wave 0. [VERIFIED: repo file scan][VERIFIED: npm registry][CITED: https://vitest.dev/] |
| Config file | `none — see Wave 0` [VERIFIED: repo file scan] |
| Quick run command | `corepack pnpm vitest run tests/contract/*.test.ts` [ASSUMED] |
| Full suite command | `corepack pnpm vitest run` [ASSUMED] |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| PACK-02 | Valid round fixtures require answer target, clue steps, accepted answers, reveal explanation, and scoring profile. [VERIFIED: .planning/REQUIREMENTS.md] | unit | `corepack pnpm vitest run tests/contract/round-contract.test.ts -t PACK-02` [ASSUMED] | ❌ Wave 0 [VERIFIED: repo file scan] |
| PACK-03 | Mixed Street View and non-Street-View clues compile through one round contract shape. [VERIFIED: .planning/REQUIREMENTS.md] | unit | `corepack pnpm vitest run tests/contract/mixed-media-round.test.ts -t PACK-03` [ASSUMED] | ❌ Wave 0 [VERIFIED: repo file scan] |
| PACK-04 | Pack compile rejects incomplete, ambiguous, broken, or cross-file-invalid rounds. [VERIFIED: .planning/REQUIREMENTS.md] | integration | `corepack pnpm vitest run tests/contract/pack-validation.test.ts -t PACK-04` [ASSUMED] | ❌ Wave 0 [VERIFIED: repo file scan] |
| OPS-01 | Venue coverage class and fallback strategy are present in compiled round/pack outputs. [VERIFIED: .planning/REQUIREMENTS.md] | unit | `corepack pnpm vitest run tests/contract/venue-profile-resolution.test.ts -t OPS-01` [ASSUMED] | ❌ Wave 0 [VERIFIED: repo file scan] |

### Sampling Rate
- **Per task commit:** `corepack pnpm vitest run tests/contract/*.test.ts` [ASSUMED]
- **Per wave merge:** `corepack pnpm vitest run` [ASSUMED]
- **Phase gate:** Full suite green before `/gsd-verify-work`. [VERIFIED: .planning/config.json][ASSUMED]

### Wave 0 Gaps
- [ ] Root `package.json` and `pnpm-workspace.yaml` — required because the repo currently has neither. [VERIFIED: repo file scan]
- [ ] `tsconfig.json` plus package-level TS configs — required for `packages/domain` and `packages/content-tools`. [VERIFIED: repo file scan][CITED: https://www.typescriptlang.org/docs/handbook/project-references]
- [ ] `vitest.config.ts` — required because no test config exists yet. [VERIFIED: repo file scan][CITED: https://vitest.dev/config/]
- [ ] `tests/contract/round-contract.test.ts` — covers PACK-02. [ASSUMED]
- [ ] `tests/contract/mixed-media-round.test.ts` — covers PACK-03. [ASSUMED]
- [ ] `tests/contract/pack-validation.test.ts` — covers PACK-04. [ASSUMED]
- [ ] `tests/contract/venue-profile-resolution.test.ts` — covers OPS-01. [ASSUMED]

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | no [VERIFIED: .planning/ROADMAP.md][VERIFIED: .planning/REQUIREMENTS.md] | No authentication surface exists in Phase 1 scope. [VERIFIED: .planning/ROADMAP.md] |
| V3 Session Management | no [VERIFIED: .planning/ROADMAP.md][VERIFIED: .planning/REQUIREMENTS.md] | Live room/session work starts later; this phase is offline content validation only. [VERIFIED: .planning/ROADMAP.md] |
| V4 Access Control | no [VERIFIED: .planning/ROADMAP.md][VERIFIED: .planning/REQUIREMENTS.md] | No access-control boundary exists in this phase. [VERIFIED: .planning/ROADMAP.md] |
| V5 Input Validation | yes [VERIFIED: .planning/REQUIREMENTS.md] | `yaml` strict parsing + `uniqueKeys` plus Zod strict schemas and cross-file invariant checks. [CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/error-formatting] |
| V6 Cryptography | no [VERIFIED: .planning/ROADMAP.md][VERIFIED: .planning/REQUIREMENTS.md] | No cryptographic behavior is required in this phase. [VERIFIED: .planning/ROADMAP.md] |

### Known Threat Patterns for file-based authored content

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Unexpected extra keys or wrong field types in authored files | Tampering | Use `z.strictObject()` plus `safeParse()` and fail compile with structured errors. [CITED: https://zod.dev/error-formatting][CITED: https://zod.dev/v4?id=introducing-zod-mini] |
| Duplicate YAML keys or ambiguous key shadowing | Tampering | Parse with `uniqueKeys: true` and `strict: true`; reject documents with parser errors before schema validation. [CITED: https://eemeli.org/yaml/] |
| Broken round, venue, or asset references across files | Tampering | Add a second validation pass that resolves references and fails the pack if any ID or asset link is missing. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] |
| Path traversal in local asset references | Tampering | Inference: resolve asset paths relative to pack root and reject absolute paths or `..` segments before compile. [ASSUMED] |

## Sources

### Primary (HIGH confidence)
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md` - locked decisions, working model, open questions, and future-awareness constraints. [VERIFIED: repo file]
- `.planning/REQUIREMENTS.md` - PACK-02, PACK-03, PACK-04, OPS-01 requirement surface. [VERIFIED: repo file]
- `.planning/ROADMAP.md` - Phase 1 goal, success criteria, and later dependency boundary. [VERIFIED: repo file]
- `.planning/PROJECT.md` - project posture and authored-content bias. [VERIFIED: repo file]
- `discovery/10-critical-inheritance-geoguessr-core.md` - explicit rejection of thin `lat/lng` rounds. [VERIFIED: repo file]
- `discovery/11-circuit-coverage-audit.md` - venue coverage classes and fallback-first posture. [VERIFIED: repo file]
- npm registry - verified versions and publish dates for `typescript`, `zod`, `yaml`, `tsx`, `vitest`, and `@types/node`. [VERIFIED: npm registry]
- https://zod.dev/error-formatting - strict object examples and structured error handling. [CITED: official docs]
- https://zod.dev/metadata - registries and metadata support. [CITED: official docs]
- https://zod.dev/json-schema?id=registries - first-party JSON Schema export. [CITED: official docs]
- https://zod.dev/v4?id=introducing-zod-mini - Zod 4 API changes including `z.strictObject()` and upgraded discriminated unions. [CITED: official docs]
- https://eemeli.org/yaml/ - YAML document parsing, unique-key handling, strict mode, comments, and error behavior. [CITED: official docs]
- https://www.typescriptlang.org/docs/handbook/project-references - package/project split guidance. [CITED: official docs]
- https://vitest.dev/ - Vitest 4 current docs home. [CITED: official docs]
- https://vitest.dev/config/ - root Vitest config guidance. [CITED: official docs]
- https://vitest.dev/guide/projects.html - `test.projects` guidance for multi-package repos. [CITED: official docs]
- https://vitest.dev/guide/snapshot.html - snapshot testing guidance. [CITED: official docs]
- https://vitest.dev/api/expect.html - `toMatchFileSnapshot()` guidance. [CITED: official docs]
- https://nodejs.org/en/about/previous-releases/ - current LTS/maintenance release status for Node 22 and Node 24. [CITED: official docs]

### Secondary (MEDIUM confidence)
- None. [VERIFIED: research process]

### Tertiary (LOW confidence)
- None. [VERIFIED: research process]

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - Core package recommendations and current versions were verified from official docs and the npm registry. [VERIFIED: npm registry][CITED: official docs]
- Architecture: HIGH - The phase boundary, repo state, and discovery docs all point to the same file-first authored-contract pattern. [VERIFIED: repo files]
- Pitfalls: HIGH - Pitfalls map directly to the locked decisions and requirement language for this phase. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

**Research date:** 2026-04-08
**Valid until:** 2026-05-08
