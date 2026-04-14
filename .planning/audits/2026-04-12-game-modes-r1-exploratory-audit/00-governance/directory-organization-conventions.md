---
date: 2026-04-13
audit_subject: process_review
audit_orientation: standard
audit_delegation: self
scope: "Directory organization conventions for this audit session shape and similar future sessions"
triggered_by: "manual: post-hoc organization cleanup"
tags:
  - exploratory-audit
  - organization
  - conventions
  - directory-layout
---

# Directory Organization Conventions

## Purpose

This file records the organization principles used to clean up this session directory so later sessions do not drift back into a flat-file pile.

These are conventions and standards for organization, not substantive design conclusions.

## Core organizational principles

### 1. Keep the session root light

The session root should contain:

- `README.md`
- `INDEX.md`
- a small number of top-level directories

It should not contain dozens of loose task specs and outputs.

### 2. Group by function first, then by work area

The primary top-level grouping should be:

- governance
- round core
- lanes
- next-round prep

This is better than one giant folder or one flat list because it separates:

- rules from content
- synthesis from distributed lane work
- historical round outputs from upcoming-round prep

### 3. Group lanes by thematic work area

Inside `02-lanes/`, prefer subfolders such as:

- `round-1/`
- `ideation/`
- `architecture/`

This keeps related lane bursts together without requiring a separate folder for every single lane unless the lane becomes especially large.

### 4. Prefer session-root-relative paths in artifacts

Inside artifacts in this session, prefer references like:

- `00-governance/review-trail-framework.md`
- `01-round-1/round-1-output.md`
- `02-lanes/architecture/lane-j-output.md`

Do not rely on bare filenames once a session has subdirectories.

### 5. Preserve traceability over aesthetic neatness

Organization is not just about making the listing prettier.

The layout should help answer:

- what governs this work?
- what was Round 1?
- what was lane work?
- what is next-round prep?
- what artifact is the current source of truth?

## Required top-level layout for sessions of this shape

For a multi-round exploratory audit session like this one, the preferred layout is:

```text
SESSION/
├── README.md
├── INDEX.md
├── 00-governance/
├── 01-round-1/
├── 02-lanes/
├── 03-next-round/
└── 04-closeout/
```

Optional later additions:

- `04-round-2/` when another substantive round, rather than closeout, is what follows next
- `04-closeout/` for verification, debrief, and workspace-readiness artifacts after the substantive rounds are done
- `99-archive/`

## Folder responsibilities

### `00-governance/`

Put here:

- framework documents
- organization rules
- gap reviews
- sequencing documents
- other cross-artifact governance files

Do not put ordinary lane outputs here.

### `01-round-1/`

Put here:

- root task specs
- shared scaffolds
- round-level orientation
- round-level synthesis
- round-level self-evaluation

This folder is for the round's main spine, not for every lane file.

### `02-lanes/`

Put here:

- lane task specs
- lane outputs
- lane comparisons
- lane-local synthesis artifacts

Subgroup by thematic area when there are many lanes.

### `03-next-round/`

Put here:

- stale or legacy carry-forward prompt files kept for history
- current next-round task specs
- later next-round prep docs that are not themselves governance docs

### `04-closeout/`

Put here:

- end-to-end verification artifacts
- debrief documents
- cleanup or workspace-readiness notes
- final closeout summaries that synthesize the session after substantive rounds are finished

## Naming conventions

### Folder names

Use numeric prefixes for major top-level groups:

- `00-...`
- `01-...`
- `02-...`

This preserves intended reading order.

### File names

Keep existing file names stable where possible.

Do not rename a file just to make it prettier if doing so would unnecessarily complicate traceability.

When a file already has established meaning, prefer moving it into a better folder rather than renaming it.

## When to introduce a new folder

Create a new subgroup when at least one of these becomes true:

- the root or parent folder becomes visually noisy
- several artifacts share the same function or work area
- readers would otherwise struggle to tell governance from outputs
- later rounds are beginning to collide with earlier rounds

Do not create folders so aggressively that navigation becomes deeper than necessary.

## How to handle older flat references

If an older artifact or planning doc still references a pre-cleanup flat path:

- update it when the reference is still active or likely to mislead
- if the old description is historically accurate but now outdated, note that it reflects the earlier state rather than silently pretending it is current

## Recommended preservation documents

For a session of this size, keep these root-level navigation docs:

- `README.md`
- `INDEX.md`

And keep these governance docs together:

- framework
- organization conventions
- gap review
- sequence/dependency map

## Anti-patterns

- letting the session root accumulate every artifact
- mixing governance files with lane outputs
- relying on bare filenames after introducing subdirectories
- renaming established artifacts without a strong reason
- creating deeply nested folder trees for tiny gains
- treating organization as separate from traceability

## Current application in this session

This session now uses:

- `00-governance/`
- `01-round-1/`
- `02-lanes/round-1/`
- `02-lanes/ideation/`
- `02-lanes/architecture/`
- `03-next-round/`
- `04-closeout/`

That layout should be preserved unless a later round creates a strong reason to revise it.
