# Prix Guesser

Prix Guesser is an F1-themed geography and party-game project.

The core idea is an expert-first, socially playable "GeoGuessr for Formula 1 places" experience centered on circuits, venues, race-weekend texture, and authored reveal logic rather than generic geography scoring.

This repository currently contains the project discovery and initialization artifacts used to shape the build:

- [`discovery/`](./discovery) — exploratory research, option space, feasibility, comparables, and decision context
- [`.planning/PROJECT.md`](./.planning/PROJECT.md) — project context
- [`.planning/REQUIREMENTS.md`](./.planning/REQUIREMENTS.md) — scoped v1 requirements
- [`.planning/ROADMAP.md`](./.planning/ROADMAP.md) — phased implementation roadmap
- [`.planning/STATE.md`](./.planning/STATE.md) — current workflow state

## Current Shape

The current roadmap is intentionally narrow:

- one authored F1 geography-and-circuit anchor mode
- private-room social play
- host-screen plus phone-controller flow
- curated packs and reveal explanations

Broader F1 party-game expansion is still part of the long-term idea, but it is not being forced into v1.

## Workflow

This repo uses regular GSD for Codex, not GSD Reflect.

Operational reference docs:

- [`AGENTS.md`](./AGENTS.md) — agent-facing runtime and delegation rules
- [`WORKFLOW.md`](./WORKFLOW.md) — git, verification, and devops workflow
- [`AI-GUARDRAILS.md`](./AI-GUARDRAILS.md) — solo+AI signoff and autonomy rules
- [`ARTIFACT-GOVERNANCE.md`](./ARTIFACT-GOVERNANCE.md) — artifact classes, staleness, retention, and cleanup policy
- [`.codex/skills/gsd-rigorous-research/SKILL.md`](./.codex/skills/gsd-rigorous-research/SKILL.md) — repo-local research skill for non-phase-bound investigation, deliberation, and source-traceable synthesis

Local install:

```bash
./scripts/setup-portable-gsd.sh
```

That script installs the repo-local regular GSD runtime and reapplies this repo's tracked GSD overlay so exploratory discuss-phase behavior and future-aware `CONTEXT.md` generation stay reproducible across machines.

To inspect the live project state:

```bash
$gsd-progress
```

Phase 01 is currently at a pre-rerun boundary. If you want to start the fresh Phase 1 steering rerun from current canon:

```bash
$gsd-discuss-phase 1
```

Then regenerate fresh planning from that new steering before starting execution work.

## Notes

- This is currently a browser-first project plan, not a finished app.
- The public repository is mainly for the project docs, discovery work, and build scaffolding at this stage.
- No open-source license has been added yet.
