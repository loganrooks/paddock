# Lane 10: Partial Stack Underreach Audit

## Scope

Audit the paused local branch stack in `/home/rookslog/workspace/projects/get-shit-done-upstream` after the first autonomous stacked-PR run was stopped and its PRs closed for human review.

## Current Paused State

- No open `docs/pr*` PRs remain on `gsd-build/get-shit-done`.
- The only PR that had been opened, `#2350`, was closed pending review.
- Local/remote branch state at audit time:
  - `docs/pr1-trust-bug-hotfixes` at `88e0169`
  - `docs/pr2-shipped-surface-catchup` at `164cdb7`
  - `docs/pr3-inventory-model-profile-truth` checked out locally, still dirty, and not yet committed

## Findings

### 1. `AGENTS.md` underreach is real and load-bearing

The current PR3 working tree does **not** yet make `docs/AGENTS.md` substantively truthful enough.

What it does:

- adds a note above the category table saying the file covers 21 role cards
- claims 10 additional shipped agents are summarized in an `Advanced and Specialized Agents` section
- points to `docs/INVENTORY.md` as an authoritative roster

What it does **not** do:

- it does not add the `Advanced and Specialized Agents` section it promises
- it does not create `docs/INVENTORY.md`
- it does not add the missing role coverage for the omitted agents
- it does not update the tool-permissions summary to account for those agents or explicitly narrow the table enough to avoid misleading readers

This means the current partial edit introduces a new internal-doc inconsistency instead of resolving the original one. Evidence:

- current `docs/AGENTS.md` has the new pointer text near the category table
- the file still ends at `## Agent Tool Permissions Summary` with no advanced-agents section

### 2. The first Opus execution optimized too hard for claim-weakening

The previous autonomous lane behaved as if “make the claim less wrong” was an acceptable stopping point for inventory truth. For `AGENTS.md`, that is too weak.

The desired outcome is not:

- “say this file is only primary agents”
- “punt to the filesystem”
- “promise another section later”

The desired outcome is:

- materially increase docs coverage so the docs themselves carry the missing surface
- or create the promised inventory document in the same pass
- and make counts, section names, and summaries internally consistent

### 3. PR3 has only partial truthful work so far

The current dirty PR3 working tree does contain some useful truth work:

- `docs/CONFIGURATION.md` has six additional model-profile rows and a fallback note

But that is only part of PR3. It does not by itself close the inventory truth gap that motivated PR3.

### 4. The branch stack is reviewable but semantically incomplete

The paused stack now means:

- PR1 is coherent and reviewable as a small truth-bug patch
- PR2 is committed and likely reviewable as a surface refresh
- PR3 is not reviewable yet because it is mid-edit and under-complete on the most important inventory truth work

## Audit Judgment

The user’s complaint is correct.

The current paused PR3 state is too timid for the actual problem. It weakens claims and gestures toward future inventory truth, but it has not yet done the substantive doc work needed to make `AGENTS.md` and adjacent inventory surfaces meaningfully current.

## Required Correction For The Next Opus Spec

The next Opus lane should be instructed to:

1. treat claim-weakening alone as insufficient for PR3
2. either add the missing-agent coverage in `docs/AGENTS.md` or create `docs/INVENTORY.md` in the same pass, preferably both per the prior proposal
3. ensure every new pointer references something that actually exists in the same branch
4. update counts and summaries so the docs can state the correct number of shipped agents without relying on hand-wavy filesystem disclaimers
5. keep PRs closed until human review explicitly authorizes reopening

## Recommended Next Move

Relaunch `Claude Opus 4.7` on the paused local PR3 branch only, with a stricter spec:

- no PR creation
- no pushing
- substantive `AGENTS.md` / `INVENTORY.md` completion required
- explicit prohibition on stopping at disclaimer-only fixes
