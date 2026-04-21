Date: 2026-04-21
Status: active registry policy

# Propagation Registry Generation And Seeding Policy

## Purpose

- [g:r:i] The propagation registry should not be treated as a purely automatic dependency extractor.
- [g:r:i] It should also not remain an unstructured prose-only memory surface once the family already has richer maintained docs and runtime evidence to draw from.
- [g:r:i] The intended shape is hybrid:
  - maintained docs and live repo evidence seed the field
  - AI authors the registry layer
  - code-generated helpers validate or enrich selected parts
  - later reread and disposition still decide what the registry means

## Registry Classes

### AI-Authored Mapping Layer

- [d:r:i] The propagation registry's `families`, `carriers`, and `edges` are meaning-bearing structures.
- [d:r:i] Those structures should be AI-authored from current source surfaces, not treated as something determinate code can infer exhaustively.
- [d:r:i] Human correction remains allowed, but is optional rather than assumed.

### Code-Generated Evidence Layer

- [e:c+i] Several adjacent registry-like surfaces are already generated from live repo state:
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
  - runtime-visibility reports and snapshots from [runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:1)
  - overlay contract validation from [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:1)
- [d:r:i] These are evidence inputs for the propagation registry, not replacements for it.

### Hybrid Contract Layer

- [e:c+i] Some registries are authored as explicit contracts and then machine-validated, especially [OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json) through [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:1).
- [d:r:i] This is the right model for ownership or intent surfaces: authored declaration plus tool-backed validation.

## Seeding Order

- [d:r:i] Future propagation-registry refreshes should seed from maintained docs first, then runtime/tooling evidence, then the prose audit family.

### 1. Maintained Inventory Surfaces

- [e:c+i] The current upstream inventory explicitly declares itself the authoritative roster of shipped surfaces and says new surfaces should land there first, then propagate to broader docs. Source: [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:1).
- [d:r:i] That means the first seed for shipped-surface discovery should now be the maintained inventory frontier, not stale counts or remembered topology.

### 2. Maintained Broad Docs

- [d:r:i] Broad docs such as upstream `AGENTS.md`, `COMMANDS.md`, `ARCHITECTURE.md`, and local governance/tooling docs should then help cluster the roster into candidate families and consumer chains.
- [d:r:i] These are not enough by themselves, but they are the right second seed because they express intended surface roles more compactly than raw tree traversal.

### 3. Live Runtime / Tooling Evidence

- [d:r:i] Runtime and helper outputs should then test or enrich the seeded map:
  - `UPLIFT-MANIFEST.json`
  - runtime-visibility snapshots
  - overlay manifest / portable contract validation
  - manifest/install coherence outputs
- [d:r:i] This layer tells us which declared surfaces are actually materialized, sampled, routed, or held.

### 4. Prose Audit Family

- [d:r:i] The prose family in `08-13` remains the richer interpretive layer.
- [d:r:i] It should continue to explain why a family split matters, what kind of edge is being named, and where uncertainty or later widening still lives.

## Required Discipline

- [d:r:i] Do not claim the registry is complete just because the inventory seed is current.
- [d:r:i] Do not claim the registry is semantically correct just because live code can enumerate files or hashes.
- [d:r:i] Every refresh still requires:
  - contextual reread
  - explicit inheritance/disposition
  - naming of held or still-unmapped relations

## Current Consequence

- [d:r:i] The current `v1` propagation registry remains a curated first slice.
- [d:r:i] The next stronger refresh should not start from that file alone.
- [d:r:i] It should start from:
  - maintained upstream `docs/INVENTORY.md`
  - maintained broad docs
  - local runtime/tooling evidence
  - then the existing propagation prose family
