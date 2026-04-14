# Artifact Governance

This document defines how planning, audit, exploration, and generated artifacts should be treated in this repo.

The goal is to keep the workspace development-ready without erasing the reasoning trail that produced important decisions.

## Artifact classes

### Canon

These are the live planning source-of-truth documents.

Examples:

- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- active phase `CONTEXT.md` and related live phase docs

Canon artifacts should stay current, stable, and relatively small.

### Phase work

These are current implementation-phase artifacts that directly guide active development.

Examples:

- active phase plans
- active phase research
- active validation artifacts

### Audit trail

These are structured review, verification, and synthesis artifacts that justify or critique planning and execution.

Examples:

- `.planning/audits/...`

Audit artifacts should be organized and indexed, not left as a flat dump.

### Exploration

These are upstream ideation, discovery, and possibility-space artifacts.

Examples:

- `.planning/explore/...`

Exploration artifacts are valuable, but they are not automatically current steering.

### Generated corpus

These are bulky, reproducible, or semi-reproducible research outputs.

Examples:

- scraped corpora
- mass transcript dumps
- extracted article bodies
- large generated comparisons

Generated corpora are the first candidates for archive, relocation, sample-only retention, or ignore rules.

## Status expectations

Any artifact that is likely to be consulted later should be legible as one of:

- active
- historical
- superseded
- generated/reference
- archived

If an artifact becomes stale but still matters historically, prefer adding a note that points to the newer authority rather than silently abandoning it.

## Staleness protocol

When a file is no longer the right steering artifact:

1. Do not delete it reflexively.
2. Mark its status if it is likely to be reopened later.
3. Point to the replacement artifact.
4. Update indexes/readmes if the file remains part of the trail.

Good examples:

- historical-status note
- superseded-by note
- README or INDEX pointer to the authoritative replacement

## Workspace-readiness rule

`Organized` is not the same as `ready`.

For the workspace to be considered ready for development:

- canon docs must be current enough to steer work
- active planning surface must be navigable
- stale steering ambiguity must be reduced
- bulky generated corpora should not dominate the active working tree without an explicit reason

## Generated corpus policy

When a large generated corpus exists, choose one of these explicitly:

- keep in repo as a long-lived reference set
- keep only manifest/spec/sample in repo and archive the full corpus elsewhere
- keep only manifest/spec/provenance in the active branch and move the full corpus to a dedicated archive branch
- mark it ignored because it is reproducible
- trim it to a curated subset

Do not leave a large corpus sitting in the active working tree without deciding which of those it is.

## Archive-branch strategy

When a bulky corpus is useful but should not dominate active development:

- keep the active branch focused on canon, live planning, and curated reference material
- preserve the full corpus on a dedicated `archive/` or `research-archive/` branch
- keep a manifest, extraction spec, provenance note, and retrieval instructions in the active branch
- never treat “move to archive branch” as silent deletion; the active branch should still point clearly to the retained archive location

## Repo-specific current guidance

At the moment:

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/` is a curated audit trail and should stay organized and indexed if retained.
- `.planning/explore/2026-04-11-product-vision-game-design/` contains important upstream exploration and should not be treated as disposable scratch.
- `.planning/explore/2026-04-11-product-vision-game-design/scraped-radio/` is a bulk generated corpus and should be treated as an explicit archive-branch or curated-subset decision, not as an accidental permanent resident of the active working tree.

## Cleanup sequence after a large audit or exploration run

1. Decide what became canon.
2. Decide what remains valuable as historical trail.
3. Mark stale or superseded steering artifacts.
4. Organize and index retained audit artifacts.
5. Decide the fate of any large generated corpora.
6. Only then try to make the working tree development-ready.

## Maintenance rule

Update this document when:

- a new artifact class starts appearing often
- archive/retention expectations change
- large generated corpora become common
- the team decides on a standard archive location or ignore strategy
