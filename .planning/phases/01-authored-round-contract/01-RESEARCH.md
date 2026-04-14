# Phase 01: Authored Round Contract - Research

> Status note (2026-04-14): This memo has been snapshotted at `.planning/phases/01-authored-round-contract/superseded/2026-04-14-pre-rerun-boundary/phase/01-RESEARCH.md`. Keep using it as reference input, but revalidate it against the next live `01-CONTEXT.md` and fresh Phase 01 plan before treating it as current execution guidance. Where its proposed Wave 0 commands or filenames diverge from `01-VALIDATION.md`, treat both as illustrative pre-rerun inputs rather than binding execution truth.

**Researched:** 2026-04-11 [VERIFIED: local date]
**Domain:** Authored content contracts, YAML content compilation, TypeScript schema validation [VERIFIED: .planning/ROADMAP.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]
**Confidence:** HIGH [ASSUMED]

<user_constraints>
## User Constraints (from CONTEXT.md)

Verbatim copy from `.planning/phases/01-authored-round-contract/01-CONTEXT.md`. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

### Locked Decisions
- **D-01:** Model rounds as authored semantic objects, not thin `lat/lng + pano` records. A valid round contract must have first-class fields for answer target type, clue steps, accepted answers or aliases, reveal explanation, scoring profile, source references, and venue/circuit identity metadata.
- **D-02:** Model packs as curated authored collections of validated rounds with explicit pack metadata and stable content structure. Packs are not random point buckets or public UGC primitives.
- **D-03:** Freeze an explicit reference contract between pack entries and rounds early in Phase 1 so later compile and snapshot steps do not rely on filename-only inference or accidental ordering.
- **D-04:** Keep active v1 gameplay anchored at `circuit` and `venue`, while preserving explicit `venue -> circuit -> section -> corner` lineage in the authored model so later deeper answer surfaces do not require a flat-contract rewrite.
- **D-05:** Make venue and circuit identity explicit and canonical. Downstream implementation should converge on one stable identifier strategy rather than parallel `id`/`venueId`/filename conventions that force executors to invent resolution rules.
- **D-06:** Represent scoring intent as explicit round content now, even though runtime judging lands in Phase 2. Scoring semantics should not live only in UI copy or code comments.
- **D-07:** Use one provider-agnostic clue-step contract that can carry Street View and non-Street-View clue media without changing round shape.
- **D-08:** Treat Street View as an optional clue family, not the mandatory product substrate. The round contract must not become Google-specific.
- **D-09:** Keep `circuit_internal`, `circuit_edge`, `venue_approach`, and `city_context` as explicit clue-family distinctions so easier fallback or approach clues do not silently replace circuit-aware play.
- **D-10:** Record venue coverage class and fallback strategy as explicit content metadata rather than as implied author judgment hidden in media assets.
- **D-11:** Reject incomplete, ambiguous, or broken content before it becomes playable, including missing answer-surface declaration, missing clue steps, missing accepted-answer data, missing reveal explanation, broken references, and undeclared fallback relationships.
- **D-12:** The first implementation should assume checked-in file-based authoring plus validation/import tooling rather than requiring an internal authoring UI before the schema is stable.

### Claude's Discretion
- Exact authored source format for packs and rounds (`yaml`, `json`, `ts`, or equivalent typed source), as long as the format is explicit, stable, and easy to validate.
- Exact package and workspace layout for domain schemas, content tooling, and compiler code.
- Exact naming shape for pack metadata and clue-step internals once the canonical identity and reference rules are frozen.

### Deferred Ideas (OUT OF SCOPE)
- Internal authoring UI beyond file/import tooling — revisit once repeated pack-authoring pain appears.
- `section`, `corner`, and composite answer surfaces as active v1 content targets — keep schema extensibility, but treat gameplay rollout as later work unless a new phase is inserted.
- Broader adjacent F1 party modes — intentionally out of scope for Phase 1.
- Unrestricted Street View exploration or generic free-roam play — explicitly out of scope for this contract.
</user_constraints>

<phase_requirements>
## Phase Requirements

Verbatim requirement scope sourced from `.planning/REQUIREMENTS.md` and the phase brief. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/ROADMAP.md]

| ID | Description | Research Support |
|----|-------------|------------------|
| PACK-02 | Author can define a round with explicit answer target type, clue steps, accepted answers or aliases, reveal explanation, and scoring profile. [VERIFIED: .planning/REQUIREMENTS.md] | Use a shared `packages/domain` contract with Zod-backed authored schemas, canonical IDs, explicit clue-step unions, and structured scoring profiles. [ASSUMED] |
| PACK-03 | A round can reference multiple clue media types, including Street View where available and non-Street-View fallback media where needed. [VERIFIED: .planning/REQUIREMENTS.md] | Use one provider-agnostic clue-step discriminated union plus shared venue coverage metadata and per-round fallback declarations. [ASSUMED] |
| PACK-04 | Pack validation rejects incomplete, ambiguous, or broken rounds before they become playable. [VERIFIED: .planning/REQUIREMENTS.md] | Use YAML document parsing with source-aware diagnostics, Zod schema validation, and a second semantic graph pass for broken refs, duplicate IDs, and fallback invariants. [ASSUMED] |
| OPS-01 | Content workflow records venue coverage class and fallback strategy so rounds do not assume uniform Street View viability. [VERIFIED: .planning/REQUIREMENTS.md] | Store baseline coverage on shared venue profiles and require each round to declare active fallback posture or override it explicitly. [ASSUMED] |
</phase_requirements>

## Summary

Phase 1 is the first real implementation boundary in a still-greenfield repo: there is no `package.json`, no workspace, no source tree, and no test harness yet, so the plan must include bootstrap work instead of assuming existing infra. [VERIFIED: repo scan][VERIFIED: .planning/STATE.md] The canonical project docs are consistent that the highest-leverage choice is the authored round/content contract, not frontend or room runtime selection. [VERIFIED: AGENTS.md][VERIFIED: .planning/PROJECT.md][VERIFIED: .planning/research/ARCHITECTURE.md]

The planning-critical contract risks are already visible in project canon and audits: venue identity must be canonical, pack-to-round references must be frozen explicitly, answer-target lineage must stay hierarchical even while v1 gameplay stays at `circuit`/`venue`, and clue media must stay provider-agnostic with explicit fallback posture. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md]

The most defensible Phase 1 implementation shape is checked-in YAML authoring plus a TypeScript workspace that separates domain schemas from content tooling: parse YAML with source-aware diagnostics, validate and normalize with Zod, run a second semantic graph pass for cross-file invariants, and lock the contract with Vitest fixture tests before any live-room or UI work starts. [CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/][CITED: https://vitest.dev/guide/][ASSUMED]

**Primary recommendation:** Plan Phase 1 around `corepack pnpm` workspace bootstrap, YAML-authored content, Zod-backed domain schemas, a graph-aware compiler/validator, and contract tests that freeze identity/reference/fallback behavior early. [VERIFIED: AGENTS.md][VERIFIED: local command][ASSUMED]

## Standard Stack

`corepack pnpm` is the required package-manager entrypoint for this repo, and `corepack pnpm 10.33.0` is already available in the environment. [VERIFIED: AGENTS.md][VERIFIED: local command][VERIFIED: npm registry]

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| `typescript` | `6.0.2` (published 2026-03-23) [VERIFIED: npm registry] | Shared domain contracts, compiler types, fixture typing. [VERIFIED: .planning/research/STACK.md] | Current TypeScript release and the project's existing research already assumes a TypeScript-first shared domain package. [VERIFIED: npm registry][VERIFIED: .planning/research/STACK.md] |
| `zod` | `4.3.6` (published 2026-01-22) [VERIFIED: npm registry] | Runtime validation, normalization, discriminated unions, parse/safeParse flow. [CITED: https://zod.dev/][CITED: https://zod.dev/] | Official docs position Zod as TypeScript-first schema validation with static inference, which fits a file-validated content contract exactly. [CITED: https://zod.dev/] |
| `yaml` | `2.8.3` (published 2026-03-21) [VERIFIED: npm registry] | Authored source parsing with `parseDocument`, comments, source positions, strict parsing, and duplicate-key checks. [CITED: https://eemeli.org/yaml/] | Official docs expose document-level parsing, `prettyErrors`, `lineCounter`, `strict`, and `uniqueKeys`, which are directly useful for author-facing compiler diagnostics. [CITED: https://eemeli.org/yaml/] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| `vitest` | `4.1.4` (published 2026-04-09) [VERIFIED: npm registry] | Contract tests, fixture tests, graph-invariant tests, compiler regression tests. [CITED: https://vitest.dev/guide/] | Use from Wave 0 onward to freeze schema behavior and content-graph rules before Phase 2 consumes the contract. [ASSUMED] |
| `tsx` | `4.21.0` (published 2025-11-30) [VERIFIED: npm registry] | Run compiler/validation CLIs and local scripts in TypeScript without a build step. [VERIFIED: npm registry] | Use for local authoring/compile scripts until the repo grows a fuller build pipeline. [ASSUMED] |
| `@types/node` | `25.6.0` (published 2026-04-10) [VERIFIED: npm registry] | Node typings for CLI/compiler code. [VERIFIED: npm registry] | Use if Phase 1 CLIs and loaders live in Node-based packages, which is the most likely repo shape here. [ASSUMED] |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| YAML-authored source [ASSUMED] | JSON [ASSUMED] | JSON is simpler to parse, but YAML preserves comments and is materially better for small checked-in authored corpora; JSON only wins if authoring becomes tool-driven immediately. [CITED: https://eemeli.org/yaml/][ASSUMED] |
| Zod [CITED: https://zod.dev/] | JSON Schema + Ajv [ASSUMED] | JSON Schema is stronger if cross-language validation/export is an immediate requirement, but this phase is repo-local and TypeScript-first, so Zod keeps type inference and runtime validation in one place. [VERIFIED: .planning/research/STACK.md][ASSUMED] |
| Vitest [CITED: https://vitest.dev/guide/] | Jest [ASSUMED] | Jest is viable, but Vitest's official project/include patterns map cleanly onto a monorepo contract-test setup and align with the project's existing stack research. [CITED: https://vitest.dev/guide/][VERIFIED: .planning/research/STACK.md] |

**Installation:** [ASSUMED]
```bash
corepack pnpm add zod yaml
corepack pnpm add -D typescript vitest tsx @types/node
```

**Version verification:** [VERIFIED: npm registry]
```bash
npm view pnpm version
npm view typescript version
npm view zod version
npm view yaml version
npm view vitest version
npm view tsx version
npm view @types/node version
```

## Architecture Patterns

### Recommended Project Structure
```text
content/                         # Authored source of truth [ASSUMED]
├── venues/                      # Venue profiles, coverage class, media posture [ASSUMED]
├── rounds/                      # Reusable authored round definitions [ASSUMED]
└── packs/                       # Curated pack manifests with explicit round refs [ASSUMED]
packages/
├── domain/                      # Contracts, Zod schemas, diagnostics, normalizers [ASSUMED]
└── content-tools/               # YAML loaders, graph checks, compiler CLI [ASSUMED]
tests/
└── contract/                    # Schema fixtures and compile/graph regressions [ASSUMED]
```

This shape matches the roadmap's Phase 1 split between shared content-contract interfaces, starter fixtures, and a compiler/CLI, while avoiding any premature web-app or room-server directories. [VERIFIED: .planning/ROADMAP.md][ASSUMED]

### Pattern 1: Canonical Identity Graph
**What:** Give `venue`, `circuit`, `section`, and `corner` their own canonical IDs and explicit parent relationships, while keeping active v1 answer targets limited to `venue` and `circuit`. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md]
**When to use:** Use in every authored entity and every pack/round reference; do not allow filename-only or duplicate-identifier conventions. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md]
**Example:** [ASSUMED]
```typescript
type AnswerSurface = "venue" | "circuit";

type IdentityLineage = {
  venueId: string;
  circuitId: string;
  sectionId?: string;
  cornerId?: string;
};

type RoundIdentity = {
  roundId: string;
  answerSurface: AnswerSurface;
  lineage: IdentityLineage;
};
```

### Pattern 2: Shared Venue Profile With Round Override
**What:** Store baseline coverage class and media posture in a shared venue profile, then require each round to declare the fallback strategy it is actively using. [VERIFIED: discovery/11-circuit-coverage-audit.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED]
**When to use:** Use for `OPS-01`, especially where multiple rounds share the same venue but not the same clue ladder. [VERIFIED: .planning/REQUIREMENTS.md][ASSUMED]
**Example:** [ASSUMED]
```typescript
type VenueProfile = {
  venueId: string;
  coverageClass: "allow" | "allow_with_fallback" | "fallback_first";
  supportedClueFamilies: Array<
    "circuit_internal" | "circuit_edge" | "venue_approach" | "city_context"
  >;
};

type RoundFallback = {
  strategy: "primary_only" | "fallback_required" | "fallback_only";
  overrideCoverageClass?: VenueProfile["coverageClass"];
};
```

### Pattern 3: Two-Stage Validation Pipeline
**What:** Parse authored YAML into documents with source-aware diagnostics, then validate/normalize the resulting JS objects with Zod, then run semantic graph checks. [CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/][ASSUMED]
**When to use:** Use for every author-facing compile/load command; schema validation alone is not enough because `PACK-04` includes broken references and undeclared fallback relationships. [VERIFIED: .planning/REQUIREMENTS.md][ASSUMED]
**Example:** [CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/]
```typescript
import { LineCounter, parseDocument } from "yaml";
import * as z from "zod";

const lineCounter = new LineCounter();
const doc = parseDocument(source, {
  lineCounter,
  prettyErrors: true,
  strict: true,
  uniqueKeys: true,
});

if (doc.errors.length) {
  throw new Error(doc.errors.map(err => err.message).join("\n"));
}

const ClueStep = z.discriminatedUnion("kind", [
  z.object({ kind: z.literal("street_view"), panoRef: z.string() }),
  z.object({ kind: z.literal("image"), assetRef: z.string() }),
  z.object({ kind: z.literal("map_fragment"), assetRef: z.string() }),
  z.object({ kind: z.literal("text"), body: z.string().min(1) }),
]);

const parsed = RoundSourceSchema.parse(doc.toJS());
```

### Anti-Patterns to Avoid
- **Filename-only reference resolution:** audits already flagged this as a Phase 1 structural gap. [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md]
- **Parallel `id` / `venueId` / `venueRef` semantics:** keep one canonical identity strategy and one explicit reference shape. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md]
- **TypeScript-authored content files:** this would blur data and code, weaken author-facing validation, and make content ingestion depend on executable source. [ASSUMED]
- **Scoring encoded in prose only:** scoring intent must be structured content before Phase 2 rules work starts. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| YAML parsing and diagnostics | Regex or ad hoc frontmatter parsing [ASSUMED] | `yaml` document parser with `prettyErrors`, `strict`, and `uniqueKeys`. [CITED: https://eemeli.org/yaml/] | Official library already handles comments, source positions, schema modes, and duplicate-key checking. [CITED: https://eemeli.org/yaml/] |
| Runtime schema validation | Manual `typeof` checks scattered through loaders. [ASSUMED] | Central Zod schemas with `parse`/`safeParse`. [CITED: https://zod.dev/] | Official docs make schema definition, unions, preprocess, and transform first-class; duplicating this logic by hand will drift quickly. [CITED: https://zod.dev/] |
| Test harness | Custom `node scripts/check-*.ts` only. [ASSUMED] | Vitest contract tests and fixture suites. [CITED: https://vitest.dev/guide/] | Official projects/include patterns fit schema and compiler regression suites better than bespoke scripts. [CITED: https://vitest.dev/guide/] |
| Reference inference | Implicit filename ordering or directory traversal rules. [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md] | Explicit pack entry refs plus graph-load validation. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED] | The audits already identified this as a rewrite risk if left to executor judgment. [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md] |
| Scoring logic syntax | Free-form expressions or mini DSL in YAML. [ASSUMED] | Structured scoring profile objects with bounded vocabulary. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED] | Phase 2 needs explicit content semantics, but free-form DSLs create unnecessary parser and safety complexity this early. [ASSUMED] |

**Key insight:** Phase 1 should hand-roll project semantics, not commodity parsing/validation/test infrastructure. [ASSUMED]

## Common Pitfalls

### Pitfall 1: Ambiguous Identity Contract
**What goes wrong:** `venueRef` resolves against whichever field or filename seems convenient that day. [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md]
**Why it happens:** Canonical identity is recognized as important in the context, but audits already found ambiguity between `id`, `venueId`, and `venueRef`. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md]
**How to avoid:** Freeze one canonical ID field per entity and one explicit reference field per relationship in Wave 0. [ASSUMED]
**Warning signs:** Multiple loaders or tests normalize refs differently, or packs only work because file ordering is stable. [ASSUMED]

### Pitfall 2: Fallback Posture Hidden In Assets
**What goes wrong:** approach-heavy or fallback-only rounds sneak into the corpus without the contract recording that drift. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: discovery/11-circuit-coverage-audit.md]
**Why it happens:** some circuits are easier to author from public-road or non-Street-View media, so convenience becomes the default if the schema does not force explicit declaration. [VERIFIED: discovery/11-circuit-coverage-audit.md][VERIFIED: .planning/research/PITFALLS.md]
**How to avoid:** keep clue family explicit per step and require round-level fallback strategy plus venue-profile coverage class. [ASSUMED]
**Warning signs:** many rounds have mixed media but no field explaining whether fallback was intentional, required, or incidental. [ASSUMED]

### Pitfall 3: Schema Validation Without Semantic Validation
**What goes wrong:** YAML loads and basic schemas pass, but duplicate IDs, missing refs, undeclared fallback relationships, or pack-order ambiguity survive into playable content. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md]
**Why it happens:** library validation only sees one document at a time. [ASSUMED]
**How to avoid:** run a second graph pass after Zod parsing for cross-file invariants and stable diagnostic codes. [ASSUMED]
**Warning signs:** tests only assert field presence, not graph integrity or deterministic compile output. [ASSUMED]

### Pitfall 4: Flat Answer Targets That Block Later Growth
**What goes wrong:** v1 ships only `circuit` and `venue`, but the contract hardcodes them as an exhaustive flat enum with no lineage support. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/REQUIREMENTS.md]
**Why it happens:** Phase 1 tries to optimize solely for current gameplay scope and ignores the already-protected seam. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md]
**How to avoid:** keep answer-surface enum narrow for v1 gameplay while storing explicit lineage fields now. [ASSUMED]
**Warning signs:** adding `section` later would require changing round identity shape instead of only widening allowed surfaces. [ASSUMED]

## Code Examples

Verified patterns from official sources:

### Zod Object Validation
```typescript
import * as z from "zod";

const User = z.object({
  name: z.string(),
});

const data = User.parse(input);
```
Source: https://zod.dev/ [CITED: https://zod.dev/]

### YAML Document Parsing
```typescript
import YAML from "yaml";

const file = fs.readFileSync("./file.yml", "utf8");
YAML.parse(file);
```
Source: https://eemeli.org/yaml/ [CITED: https://eemeli.org/yaml/]

### Vitest Config
```typescript
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    projects: [
      {
        test: {
          name: "unit",
          include: ["./tests/contract/*.test.ts"],
        },
      },
    ],
  },
});
```
Source: https://vitest.dev/guide/ and https://vitest.dev/config/include [CITED: https://vitest.dev/guide/][CITED: https://vitest.dev/config/include]

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Thin `lat/lng + pano` rounds [VERIFIED: discovery/10-critical-inheritance-geoguessr-core.md] | Authored semantic rounds with answer target, clue ladder, reveal explanation, scoring, and identity metadata. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/REQUIREMENTS.md] | Discovery canon on 2026-04-08 and refreshed phase canon on 2026-04-11. [VERIFIED: discovery/10-critical-inheritance-geoguessr-core.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] | Phase 1 must optimize for contract semantics first, not map-drop convenience. [ASSUMED] |
| Street View as implicit substrate [VERIFIED: discovery/10-critical-inheritance-geoguessr-core.md] | Provider-agnostic clue-step model plus explicit coverage class and fallback strategy. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: discovery/11-circuit-coverage-audit.md] | Strengthened by the 2026-04-08 coverage audit and Phase 1 context refresh. [VERIFIED: discovery/11-circuit-coverage-audit.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] | Keeps circuit-aware play intact even for fallback-first venues. [ASSUMED] |
| Filename or ordering inference for pack membership [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md] | Explicit pack entry reference contract frozen early. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] | Raised explicitly in audit findings on 2026-04-09/10. [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md] | Prevents later compile/snapshot steps from inheriting accidental semantics. [ASSUMED] |

**Deprecated/outdated:**
- Treating `venue_approach` clues as a silent substitute for `circuit_internal` clues is incompatible with current canon. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/research/PITFALLS.md]
- Treating active v1 answer surfaces as proof that lineage can stay flat is explicitly rejected by `SEAM-01` and the Phase 1 context. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Shared venue profile + per-round fallback override is the best initial `OPS-01` shape. [ASSUMED] | Architecture Patterns | Planner may overfit the data model and need a later refactor if duplication or override semantics behave differently. |
| A2 | Scoring should be modeled as bounded structured profiles rather than free-form expressions. [ASSUMED] | Don't Hand-Roll | Phase 2 could need a richer rule vocabulary than planned. |
| A3 | `content/` plus `packages/domain` and `packages/content-tools` is the best minimal repo layout for this phase. [ASSUMED] | Recommended Project Structure | Planner may choose a different but still valid workspace split. |

**If this table is empty:** Not applicable. [ASSUMED]

## Open Questions

1. **How wide should the first scoring-profile vocabulary be?** [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]
   - What we know: scoring semantics must be explicit content in Phase 1, and Phase 2 will consume them in pure rules code. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/ROADMAP.md]
   - What's unclear: whether the initial vocabulary is best expressed as a few named presets, a parameterized object, or a hybrid of both. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md]
   - Recommendation: plan a hybrid with `kind` plus a small parameter bag, and freeze examples in fixtures before widening the vocabulary. [ASSUMED]

2. **What exact pack reference shape should be canonical?** [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md]
   - What we know: audits explicitly flagged late-frozen `roundOrder` / pack reference semantics as a Phase 1 risk. [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md]
   - What's unclear: whether pack entries should always inline per-round overrides or whether overrides should be layered separately. [ASSUMED]
   - Recommendation: freeze a single explicit `roundRef` object in the first plan and require tests proving deterministic pack compilation. [ASSUMED]

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Node.js | TypeScript workspace, compiler CLI, tests [ASSUMED] | ✓ [VERIFIED: local command] | `v22.22.1` [VERIFIED: local command] | — |
| Corepack | Repo-required package-manager entrypoint [VERIFIED: AGENTS.md] | ✓ [VERIFIED: local command] | `0.34.6` [VERIFIED: local command] | — |
| `corepack pnpm` | Workspace/bootstrap/install commands [VERIFIED: AGENTS.md] | ✓ [VERIFIED: local command] | `10.33.0` [VERIFIED: local command][VERIFIED: npm registry] | Do not fall back in committed docs; repo guidance prefers `corepack pnpm`. [VERIFIED: AGENTS.md] |
| npm | Registry lookups and package metadata [VERIFIED: local commands above] | ✓ [VERIFIED: local command] | `10.9.4` [VERIFIED: local command] | — |
| Git | GSD doc commit and normal repo workflow [VERIFIED: .planning/config.json] | ✓ [VERIFIED: local command] | `2.43.0` [VERIFIED: local command] | — |

**Missing dependencies with no fallback:**
- None for Phase 1 research and bootstrap planning. [VERIFIED: local command][ASSUMED]

**Missing dependencies with fallback:**
- None. [VERIFIED: local command]

## Validation Architecture

`workflow.nyquist_validation` is enabled in `.planning/config.json`, and no test framework or config exists yet in the repo. [VERIFIED: .planning/config.json][VERIFIED: repo scan]

### Test Framework
| Property | Value |
|----------|-------|
| Framework | `Vitest 4.1.4` recommended; not yet installed. [VERIFIED: npm registry][ASSUMED] |
| Config file | `vitest.config.ts` — missing, create in Wave 0. [VERIFIED: repo scan][ASSUMED] |
| Quick run command | `corepack pnpm vitest run tests/contract --reporter=dot` [ASSUMED] |
| Full suite command | `corepack pnpm vitest run` [ASSUMED] |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| PACK-02 | Complete authored round validates with explicit answer target, clue steps, aliases, reveal explanation, and scoring profile. [VERIFIED: .planning/REQUIREMENTS.md] | unit | `corepack pnpm vitest run tests/contract/round-schema.test.ts -t "accepts complete authored round"` [ASSUMED] | ❌ Wave 0 [VERIFIED: repo scan] |
| PACK-03 | Mixed clue media validates under one provider-agnostic clue-step contract. [VERIFIED: .planning/REQUIREMENTS.md] | unit | `corepack pnpm vitest run tests/contract/clue-step-schema.test.ts -t "accepts mixed media"` [ASSUMED] | ❌ Wave 0 [VERIFIED: repo scan] |
| PACK-04 | Compiler rejects incomplete, ambiguous, duplicate, and broken-reference content before play. [VERIFIED: .planning/REQUIREMENTS.md] | integration | `corepack pnpm vitest run tests/contract/content-graph-loading.test.ts` [ASSUMED] | ❌ Wave 0 [VERIFIED: repo scan] |
| OPS-01 | Venue coverage class and round fallback strategy are recorded and queryable. [VERIFIED: .planning/REQUIREMENTS.md] | unit | `corepack pnpm vitest run tests/contract/venue-profile-schema.test.ts` [ASSUMED] | ❌ Wave 0 [VERIFIED: repo scan] |

### Sampling Rate
- **Per task commit:** `corepack pnpm vitest run tests/contract --reporter=dot` [ASSUMED]
- **Per wave merge:** `corepack pnpm vitest run` [ASSUMED]
- **Phase gate:** Full contract suite green before `/gsd-verify-work`. [ASSUMED]

### Wave 0 Gaps
- [ ] `package.json` and `pnpm-workspace.yaml` — no JS workspace exists yet. [VERIFIED: repo scan]
- [ ] `tsconfig.json` — required before shared TypeScript packages and strict Zod usage. [VERIFIED: repo scan][CITED: https://zod.dev/]
- [ ] `vitest.config.ts` — required to formalize contract tests. [VERIFIED: repo scan][CITED: https://vitest.dev/guide/]
- [ ] `tests/contract/round-schema.test.ts` — covers `PACK-02`. [ASSUMED]
- [ ] `tests/contract/clue-step-schema.test.ts` — covers `PACK-03`. [ASSUMED]
- [ ] `tests/contract/content-graph-loading.test.ts` — covers `PACK-04` semantic graph failures. [ASSUMED]
- [ ] `tests/contract/venue-profile-schema.test.ts` — covers `OPS-01`. [ASSUMED]
- [ ] Framework install: `corepack pnpm add -D vitest typescript tsx @types/node` and `corepack pnpm add zod yaml`. [ASSUMED]

## Security Domain

Security enforcement is enabled by default because `.planning/config.json` does not disable it. [VERIFIED: .planning/config.json]

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | no [ASSUMED] | Not in Phase 1 scope. [VERIFIED: .planning/REQUIREMENTS.md][VERIFIED: .planning/ROADMAP.md] |
| V3 Session Management | no [ASSUMED] | Not in Phase 1 scope. [VERIFIED: .planning/ROADMAP.md] |
| V4 Access Control | no [ASSUMED] | No live room, auth, or role system exists in this phase. [VERIFIED: .planning/ROADMAP.md][VERIFIED: repo scan] |
| V5 Input Validation | yes [ASSUMED] | `yaml` strict parsing + Zod runtime schemas + graph-invariant checks. [CITED: https://eemeli.org/yaml/][CITED: https://zod.dev/][ASSUMED] |
| V6 Cryptography | no [ASSUMED] | No cryptographic requirement is introduced by the Phase 1 content contract itself. [VERIFIED: .planning/ROADMAP.md] |

### Known Threat Patterns for authored-content tooling

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Duplicate IDs or ambiguous refs compile into the pack graph. [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md] | Spoofing / Tampering [ASSUMED] | Enforce unique canonical IDs and explicit cross-file graph validation with stable diagnostics. [ASSUMED] |
| YAML duplicate keys or implicit parsing surprises mask bad authored data. [CITED: https://eemeli.org/yaml/] | Tampering [ASSUMED] | Parse with `strict: true`, `uniqueKeys: true`, and document-level error handling. [CITED: https://eemeli.org/yaml/] |
| Asset refs or file refs escape the intended content root. [VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md] | Tampering [ASSUMED] | Normalize paths and enforce repo-local allowlisted roots during compile. [ASSUMED] |
| Fallback-heavy rounds silently redefine the anchor mode. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md] | Integrity / Repudiation [ASSUMED] | Require explicit clue-family and fallback metadata in authored content. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][ASSUMED] |

## Sources

### Primary (HIGH confidence)
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md` - locked decisions, open questions, protected seams, derived constraints. [VERIFIED: repo docs]
- `.planning/REQUIREMENTS.md` - `PACK-02`, `PACK-03`, `PACK-04`, `OPS-01`, `SEAM-01`, `SEAM-04`. [VERIFIED: repo docs]
- `.planning/ROADMAP.md` - Phase 1 goal, success criteria, four-plan split, scope boundary. [VERIFIED: repo docs]
- `.planning/PROJECT.md` and `.planning/LONG-ARC.md` - private-only posture, anchor-mode doctrine, future seam protection. [VERIFIED: repo docs]
- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md` and `CONVERGENCE.md` - venue identity ambiguity, explicit reference freezing, hierarchical answer-target pressure, validation gaps. [VERIFIED: repo docs]
- `discovery/10-critical-inheritance-geoguessr-core.md`, `11-circuit-coverage-audit.md`, `04-modes.md`, `06-open-questions.md`, `14-gsd-seed.md` - authored-round bias, clue-family distinctions, venue coverage strategy, preserved open questions. [VERIFIED: repo docs]
- `https://zod.dev/` - Zod 4 intro, schema validation, strict TypeScript guidance. [CITED: https://zod.dev/]
- `https://eemeli.org/yaml/` - YAML v2 parser, document parsing, parse options, diagnostics, comments, strict/unique key settings. [CITED: https://eemeli.org/yaml/]
- `https://pnpm.io/pnpm-workspace_yaml` - official workspace package layout patterns. [CITED: https://pnpm.io/pnpm-workspace_yaml]
- `https://vitest.dev/guide/` and `https://vitest.dev/config/include` - config, projects, include patterns, coverage. [CITED: https://vitest.dev/guide/][CITED: https://vitest.dev/config/include]
- npm registry (`typescript`, `zod`, `yaml`, `vitest`, `tsx`, `@types/node`, `pnpm`) - current versions and publish dates. [VERIFIED: npm registry]
- Local environment commands (`node --version`, `corepack --version`, `corepack pnpm --version`, `npm --version`, `git --version`) - environment availability. [VERIFIED: local command]

### Secondary (MEDIUM confidence)
- Context7 `/websites/zod_dev` - union, preprocess, transform, parse patterns. [CITED: https://zod.dev/]
- Context7 `/websites/pnpm_io` - workspace configuration patterns. [CITED: https://pnpm.io/pnpm-workspace_yaml]
- Context7 `/websites/vitest_dev` - multi-project test configuration patterns. [CITED: https://vitest.dev/guide/]

### Tertiary (LOW confidence)
- None. [VERIFIED: research process]

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - versions are current from npm registry and library usage is backed by official docs. [VERIFIED: npm registry][CITED: https://zod.dev/][CITED: https://eemeli.org/yaml/][CITED: https://vitest.dev/guide/]
- Architecture: HIGH - the core boundary decisions are strongly reinforced by project canon and both audit passes. [VERIFIED: .planning/phases/01-authored-round-contract/01-CONTEXT.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md][VERIFIED: .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md]
- Pitfalls: HIGH - the major failure modes are already explicit in the repo's research, discovery, and audit artifacts. [VERIFIED: .planning/research/PITFALLS.md][VERIFIED: discovery/11-circuit-coverage-audit.md]

**Research date:** 2026-04-11 [VERIFIED: local date]
**Valid until:** 2026-05-11 for package versions and stack assumptions; re-check registry/docs after that. [ASSUMED]
