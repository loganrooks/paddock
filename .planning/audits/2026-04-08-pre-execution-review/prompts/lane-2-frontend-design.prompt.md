# Lane 2 Prompt — Frontend Design & Aesthetics

**Used for:**
- Opus 4.6 agent (first pass, 2026-04-08, non-blind)
- GPT 5.4 xhigh Codex agent (second pass, 2026-04-10, blind)

## GPT Blind-Audit Version (as sent)

```
You are performing an INDEPENDENT BLIND AUDIT of frontend design planning for Prix Guesser. Another auditor has already reviewed this; you must NOT read their findings so that your review is uncontaminated.

## Hard Constraints

- DO NOT read any file named `lane-*.md` or `SYNTHESIS.md` in `.planning/audits/`
- DO NOT read `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/` (other lanes)
- Write your report to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/lane-2-frontend-design.md`
- The shared task spec at `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md` is the only audit file you may read

## Context

Prix Guesser is an F1-themed party game (like GeoGuessr for Formula 1 locations) — a local game night experience where a host casts to a TV and players use phones as controllers.

## Critical stakeholder context

- Creator building for personal use and friends (non-technical F1 fans)
- NO commercialization — private-only project
- Must look polished, feel like a real game night experience, not a developer prototype
- Primary mode: cast to TV (host screen) + phones (controllers)
- Future mode: online hosted play
- The aesthetic bar matters — social experience, not a utility

## Your Task (Lane 2: Frontend Design & Aesthetics)

Audit the project roadmap, requirements, and design artifacts for frontend design quality as a first-class concern.

1. Does the roadmap account for visual design quality? Any phases for aesthetics, design system, component library, visual direction?
2. Risk of building functional-but-ugly UI across Phases 4-5 that needs rewrite?
3. What would a "design-forward" approach look like? Separate design phase or woven into implementation?
4. What framework/tool choices best serve a polished game-night aesthetic with minimal effort? (Next.js, SvelteKit, Astro, Tailwind, shadcn/ui, game UI libraries, motion libraries)
5. Does host screen need different design treatment than mobile controller?
6. Any F1/motorsport visual language opportunities being missed?
7. Responsive design, dark mode (TV viewing), animation/transitions for reveals?
8. Should there be a UI-SPEC or design contract before implementation phases?

## Files to read

- `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md`
- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `discovery/14-gsd-seed.md` (if it exists)

## Output format

Write your markdown report to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/lane-2-frontend-design.md` with:
- Overall assessment of design readiness
- Specific gaps found
- Framework/tooling recommendations (with tradeoffs)
- Recommended approach (separate design phase vs woven-in)
- Visual direction suggestions for an F1 party game
- Concrete recommendations with priority (critical / high / medium / low)

Write the report directly to the file using Write tool or shell redirection. Do not print it as your final message.
```
