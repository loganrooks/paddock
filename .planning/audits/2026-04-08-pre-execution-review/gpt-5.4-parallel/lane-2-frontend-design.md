# Lane 2 Audit: Frontend Design & Aesthetics

## Overall Assessment Of Design Readiness

Design intent is present, but design execution planning is not ready yet.

The current artifacts clearly understand that Prix Guesser should feel social, watchable, host-screen-first, and more like a polished game-night product than a utility app. That intent is visible in the project thesis and roadmap framing: the product should be "socially alive," "legible to watch," and built around a "watchable host-screen plus phone-controller loop" (`discovery/14-gsd-seed.md:19-29`, `discovery/14-gsd-seed.md:201-209`, `.planning/PROJECT.md:46-49`, `.planning/ROADMAP.md:5`).

The problem is that this intent is not translated into concrete frontend planning. The roadmap has UI phases, but no phase for visual direction, no component/design-system work, no motion grammar, no TV-specific layout contract, and no UI acceptance criteria beyond basic usability/watchability (`.planning/ROADMAP.md:71-91`, `.planning/REQUIREMENTS.md:47-56`).

My assessment: the product is conceptually design-aware, but artifact-level design readiness is low. If Phase 4 starts as currently written, the likely outcome is a functional controller and host screen that satisfy requirements while still looking and feeling like an internal prototype.

## Specific Gaps Found

1. No explicit design foundation before UI implementation.
   Phase 4 and Phase 5 are where UI appears, but nothing earlier defines visual direction, tokens, layout principles, motion, or reusable primitives (`.planning/ROADMAP.md:71-91`).

2. Requirements treat UX as functional, not aesthetic.
   `UX-01` through `UX-04` cover watchability, usability, clarity, and summary flow, but nothing covers polish, visual coherence, animation quality, typography, or party-game presentation (`.planning/REQUIREMENTS.md:49-56`).

3. No host-screen vs controller design split.
   The product thesis already implies two distinct surfaces, but the artifacts do not define different design goals for spectator TV viewing versus active phone input (`discovery/14-gsd-seed.md:93-100`, `.planning/ROADMAP.md:72-89`).

4. No UI-SPEC or design contract.
   There is no artifact that fixes visual principles, component inventory, screen states, responsive behavior, or motion cues before implementation starts.

5. No motion/reveal grammar.
   The game depends heavily on pacing, clue cadence, answer lock, reveal, standings, and replay. Those are inherently temporal UI moments, but no artifact specifies transition behavior, emphasis hierarchy, or animation rules (`.planning/ROADMAP.md:63-67`, `.planning/ROADMAP.md:83-89`).

6. No TV-first ergonomics.
   "Watchable shared-screen format" is the right requirement, but it is underspecified. There is no guidance around 16:9 layout, safe zones, distance legibility, dark-room contrast, or host-on-laptop fallback (`.planning/REQUIREMENTS.md:49-50`).

7. Stack openness is good, but too open for Phases 4-5.
   The seed correctly keeps the framework decision open and lists viable candidates, but there is no narrowed frontend recommendation before UI work begins (`discovery/14-gsd-seed.md:124-148`, `.planning/PROJECT.md:84-86`).

8. "Cosmetics" being out of scope could be misread.
   The out-of-scope note about cosmetics/progression is sensible, but without a separate design requirement it creates room for someone to deprioritize visual polish accidentally (`.planning/REQUIREMENTS.md:96`).

## Risk Of Functional-But-Ugly UI Rewrite

This risk is high across Phases 4 and 5.

The current sequence makes it easy to build:
- a basic mobile controller in Phase 4 that is clear but generic
- then a host screen in Phase 5 that needs a completely different level of theatricality, motion, and visual hierarchy

That creates a classic rewrite trap: Phase 4 ships utilitarian primitives, then Phase 5 reveals the need for a real design system, forcing rework across colors, typography, spacing, shared components, state treatments, and responsive rules.

The risk is amplified because the host screen and controller should not look like the same app scaled to different breakpoints. They need a shared brand language but different interaction priorities.

## Framework / Tooling Recommendations

### Recommended Baseline

Use `React + Vite` for the frontend shell, with `Tailwind CSS`, CSS custom properties for design tokens, selective `shadcn/ui` or `Radix` primitives for accessibility, and `Motion` for reveals/transitions.

Why this is the best fit here:
- fastest path to a polished browser-first host/controller app
- strongest ecosystem for maps, realtime clients, animation, and component primitives
- aligns with the seed's current non-binding preference for `React + Vite` over heavier frameworks (`discovery/14-gsd-seed.md:137-148`)
- easier to keep local/private deployment simple than a heavier full-app framework

Tradeoffs:
- easy to produce utility-class sprawl unless tokens and component boundaries are defined early
- `shadcn/ui` can quickly make the app look like a dashboard if used as a visual system instead of a primitive layer

### Strong Alternative

`SvelteKit` is a credible second choice if the primary goal is a leaner codebase and highly polished interactions with less React ceremony.

Tradeoffs:
- smaller ecosystem for off-the-shelf accessible primitives and inherited OSS patterns
- weaker continuity with the discovery's React-oriented reference set

### Not Recommended As Default v1 Choice

`Next.js` is not the best default here.

Reasons:
- the project's first hard problem is not SEO, SSR, or content publishing
- the main product shape is a realtime, room-based, browser-first game surface
- App Router/server-action complexity is likely overhead for this milestone

`Astro` is an even worse fit for the main app surface.

Reasons:
- excellent for content-heavy sites
- wrong center of gravity for a synchronized host/controller game flow

### Library Guidance

- `Tailwind CSS`: yes, but only with named semantic tokens from day one
- `shadcn/ui` or `Radix`: yes for dialogs, drawers, selects, sheets, toasts, and accessibility primitives
- `Motion`: yes for lock/reveal/standings/join-state transitions
- heavy game/canvas UI libraries: no, unless a later feature truly needs canvas-driven spectacle

This product is still mostly an app UI with game-show pacing, not a canvas game.

## Recommended Approach

Use both:
- a short explicit design-foundation phase before Phase 4
- then design criteria woven into Phase 4 and Phase 5 execution

I would not recommend a long standalone design milestone that tries to freeze the whole product. The product is still learning. But I do recommend an inserted phase between Phase 3 and Phase 4, because otherwise the first real UI work will establish accidental visual defaults.

### Recommended Inserted Phase

Add an inserted phase such as:

`Phase 3.5: UI Direction, Design System, And Interaction Contract`

Minimum deliverables:
- `UI-SPEC.md` covering visual direction, tone words, typography, color system, spacing scale, elevation, and iconography
- host-screen and controller design principles as separate subsections
- key-screen mocks for join flow, controller answer flow, host clue state, answer lock, reveal, standings, and replay
- motion grammar for timer pressure, answer lock, reveal payoff, and scoreboard changes
- responsive rules for `phone portrait`, `laptop host`, and `16:9 TV/cast`
- component inventory for domain components, not just generic UI parts

Then update Phase 4 and Phase 5 to require implementation against that contract, not just against functional acceptance criteria.

## Host Screen vs Mobile Controller

These surfaces need different design treatment.

### Host Screen

Design for spectatorship:
- large type and large state changes readable from across a room
- strong pacing and reveal choreography
- information hierarchy built around clue, timer, status, reveal, and standings
- dark-first presentation for TV/night play
- restrained but noticeable animation

### Mobile Controller

Design for speed and confidence:
- one-thumb interaction
- very clear answer contract
- large tap targets
- high timer visibility without visual clutter
- immediate submission confidence and lock-state feedback
- minimal flourish during timed input

Shared tokens should tie them together, but they should not share the same layout language.

## Visual Direction Suggestions For An F1 Party Game

The planning artifacts already leave room for a much richer motorsport visual language than they currently name.

Strong directions worth capturing in the UI contract:
- dark-first "pit wall at night" base with bright telemetry accents
- timing-screen influence rather than generic gamer neon
- condensed, motorsport-adjacent display typography for timers, standings, and headers
- track-outline silhouettes, sector-line graphics, grid-light countdown motifs, and marshal-flag color semantics
- asphalt, carbon, LED, and paddock-signage cues used sparingly as texture, not wallpaper
- reveal sequences that feel like race control or broadcast transitions instead of modal popups

Opportunities currently being missed:
- no explicit mention of F1/motorsport visual references in the roadmap
- no requirement for reveal theatrics despite reveal being a core game beat
- no concept of pack or mode theming that could later give different circuits/eras distinct visual identity

One caution: do not default to "generic red racing app." The better reference is modern motorsport timing and broadcast restraint, not arcade cliché.

## Responsive Design, Dark Mode, And Motion

These should be first-class constraints, not polish passes.

- Responsive design should be modeled as distinct surfaces, not generic breakpoints.
- Dark mode should be treated as the canonical host-screen presentation, not an optional late toggle.
- Motion should be purposeful and state-driven: join success, countdown pressure, answer lock, reveal emphasis, standings movement, replay reset.

If these are left until after functional implementation, the product will almost certainly need layout and component rework.

## Concrete Recommendations With Priority

### Critical

- Insert a design-foundation phase before Phase 4 or make `UI-SPEC.md` a required first task of Phase 4 before any controller UI build.
- Add explicit design deliverables to the roadmap: visual direction, token system, component library, motion grammar, and host/controller surface contracts.
- Add at least one requirement that defines visual polish as in scope for v1, separate from monetization-style "cosmetics."
- Choose and record a frontend baseline before Phase 4. My recommendation is `React + Vite + Tailwind + Radix/shadcn primitives + Motion`.

### High

- Treat host screen and controller as two designed surfaces under one brand system, not one responsive app.
- Make dark-first TV-safe layout rules explicit.
- Define domain-specific components early: timer rail, answer-surface chip, clue card, room-code hero, reveal panel, standings board, replay CTA.
- Require high-fidelity mocks for the core game loop before implementation of Phase 5.

### Medium

- Add motorsport visual-language guidance to the future UI contract so the product does not drift into generic SaaS/game-jam styling.
- Consider pack-level theming hooks later, once the shared token system exists.
- Add a small visual review checkpoint after Phase 4 so the controller UI does not set weak defaults for Phase 5.

### Low

- Explore richer visual flourish later only after the core host/controller system is stable.
- Defer light-mode variants unless real host usage proves they are necessary.

## Bottom Line

The roadmap understands that Prix Guesser needs to be watchable and social, but it does not yet plan frontend design quality as a first-class deliverable. For this project, that is a material gap, not a cosmetic one.

I would block Phase 4 implementation from starting until there is at least a lightweight `UI-SPEC.md` and a deliberate design-foundation pass. The right move is not "big design first" or "just code and polish later." It is a short explicit design phase before UI implementation, followed by design-aware execution in both controller and host-screen phases.
