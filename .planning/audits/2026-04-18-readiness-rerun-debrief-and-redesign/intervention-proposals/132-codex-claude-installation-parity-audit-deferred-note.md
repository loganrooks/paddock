Date: 2026-04-22
Status: deferred next-adjacent audit note

# Codex Claude Installation Parity Audit Deferred Note

## Why This Note Exists

- [d:r:i] A bounded `.codex` / `.claude` installation-parity audit is now earned, but it should not open before the current `update` consumer reread is inherited and the `update + gsd-update` continuity slice is dispositioned.
- [d:r:i] This note keeps that route explicit so it does not remain only in chat memory or get reopened out of sequence.

## What Prompted The Note

- [e:c+i] Upstream GSD already treats installation as runtime-specific rather than as plain reference substitution. Sources: [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md:110), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md:120), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4104), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4204), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4394), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4446).
- [e:c+i] The repo-local installer is currently Codex-first and then applies the repo-local overlay/materialization chain. Source: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:21).
- [e:c+i] The latest repo-local rematerialization still triggers upstream's unreplaced `.claude` path warning for `get-shit-done/workflows/update.md`, but those hits currently sit inside runtime-detection examples and loops rather than an obviously broken local continuity pointer. Sources: [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:53), [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:112), [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:352), [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:438), [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:574).
- [d:r:i] That means the local open question is no longer whether runtime-specific installation differences exist. The sharper question is whether this repo's modifier layer, update/install surfaces, and continuity references stay in tune with the upstream `.codex` / `.claude` split.

## What The Later Audit Should Cover

- [d:r:i] Limit the field to `.codex` and `.claude`.
- [d:r:i] Check runtime-specific differences across:
  - install commands and layout
  - commands versus skills
  - agent conversion and agent config
  - hooks and runtime config surfaces
  - repo-local overlay/materialization behavior
  - workflow/reference wording where provider-specific install shape matters
- [d:r:i] Use upstream runtime-specific install logic as the comparison frontier, then inspect where repo-local overlay or workflow surfaces diverge, flatten, or blur those differences.

## Why It Is Deferred

- [d:r:i] The current bounded cross-vendor boundary is still the `update + gsd-update` consumer reread and inheritance path.
- [d:r:i] Opening the parity audit before that boundary closes would widen terrain on top of an unresolved consumer slice and make it harder to tell which pressure belongs to the current `update` branch versus the later installation-parity branch.
- [d:r:i] The cleaner sequence is:
  1. inherit the current `update` reread
  2. revise or land the `update + gsd-update` continuity slice
  3. then open the bounded `.codex` / `.claude` installation-parity audit

## Next Trigger

- [d:r:i] Open this audit immediately after the current `update` consumer branch settles, unless that inheritance itself absorbs the parity question so fully that only a narrower residual branch remains.
