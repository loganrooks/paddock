# Phase 1: Authored Round Contract - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in `01-CONTEXT.md`; this log preserves the alternatives considered during the `--auto` discuss pass.

**Date:** 2026-04-11T06:32:53-04:00
**Phase:** 01-authored-round-contract
**Mode:** `--auto` with `workflow.discuss_mode = exploratory`
**Areas discussed:** Round and pack contract, answer surface and identity modeling, clue media and fallback modeling, validation and authoring posture

---

## Round And Pack Contract

| Option | Description | Selected |
|--------|-------------|----------|
| Rich authored contract | Round objects carry answer targets, clue steps, reveal explanation, scoring profile, aliases, and source references instead of just coordinates/media. | ✓ |
| Thin geo schema | Start from `lat/lng + pano` and grow semantics later if needed. | |
| Minimal temporary contract | Keep the schema intentionally loose until runtime code proves what is needed. | |

**User's choice:** Auto-selected grounded direction: rich authored contract.
**Notes:** This is directly grounded by `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/research/SUMMARY.md`, `.planning/research/PITFALLS.md`, and `discovery/10-critical-inheritance-geoguessr-core.md`. The thin-schema path is explicitly warned against across canon and discovery.

---

## Answer Surface And Identity Modeling

| Option | Description | Selected |
|--------|-------------|----------|
| Hierarchical lineage, narrow v1 scope | Preserve `venue -> circuit -> section -> corner` lineage in the schema, while keeping active v1 gameplay anchored at `venue` and `circuit`. | ✓ |
| Flat v1-only answer types | Model only `venue` and `circuit` now, add deeper targets later if needed. | |
| Fully widen active scope now | Treat `section`, `corner`, and composite answers as first-class v1 targets immediately. | |

**User's choice:** Auto-selected grounded direction: hierarchical lineage with narrow active v1 scope.
**Notes:** This is grounded by `SEAM-01`, the refreshed roadmap wording, and the pre-execution audit findings. The exact degree of lineage detail remains an open question captured in `01-CONTEXT.md`.

---

## Clue Media And Fallback Modeling

| Option | Description | Selected |
|--------|-------------|----------|
| Provider-agnostic clue contract with explicit fallback metadata | One clue-step shape supports Street View and non-Street-View media, with explicit clue families, coverage class, and fallback posture. | ✓ |
| Street View-centered schema | Optimize the round contract around Google-style pano clues and bolt on fallback media later. | |
| Ad hoc media notes | Keep fallback strategy informal in author notes rather than in validated content data. | |

**User's choice:** Auto-selected grounded direction: provider-agnostic clue contract with explicit fallback metadata.
**Notes:** Strongly grounded by `PACK-03`, `OPS-01`, `.planning/research/PITFALLS.md`, and `discovery/11-circuit-coverage-audit.md`. The exact storage location for fallback metadata remains intentionally open.

---

## Validation And Authoring Posture

| Option | Description | Selected |
|--------|-------------|----------|
| Strict validation plus file-first authoring | Reject incomplete, ambiguous, or broken content early and prove the model with checked-in files plus tooling before building authoring UI. | ✓ |
| Light validation first | Accept partial content and rely on later runtime behavior to expose bad rounds. | |
| Tool-first authoring | Build internal authoring UI before the contract and validator have stabilized. | |

**User's choice:** Auto-selected grounded direction: strict validation plus file-first authoring.
**Notes:** Grounded by `PACK-04`, `.planning/research/SUMMARY.md`, `.planning/research/STACK.md`, and the archived context. Exact source format remains agent discretion.

---

## the agent's Discretion

- Exact authored source format for pack and round files.
- Exact package and workspace layout for schema, compiler, and validation tooling.
- Exact naming details for pack metadata and clue-step internals once canonical IDs and references are frozen.

## Deferred Ideas

- Internal authoring UI after real authoring pain appears.
- Active v1 rollout of `section`, `corner`, and composite answers.
- Broader adjacent F1 party modes.
- Unrestricted Street View free-roam as a default play shape.
