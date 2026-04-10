# Lane 2: Frontend Design & Aesthetics Gap Analysis

**Auditor scope**: ROADMAP.md, REQUIREMENTS.md, PROJECT.md, research artifacts, discovery seed
**Date**: 2026-04-08
**Verdict**: Significant gaps exist. The roadmap builds functional systems without any explicit design contract, visual direction, or aesthetic quality gate. Left unaddressed, this will produce a technically correct but visually flat prototype that undermines the core social-experience promise.

---

## 1. Overall Assessment of Design Readiness

**Rating: LOW**

The project has excellent architectural thinking, a clear content model, and well-separated concerns. It has essentially zero design thinking captured anywhere in the planning artifacts. The word "design" appears throughout the documents but always means system design or product design, never visual design, interaction design, or aesthetic direction.

Specific observations:

- **No design phase exists.** The seven-phase roadmap covers content contracts, rules engines, room authority, guest join, host screen, calibration, and reconnect. None of these phases include success criteria related to visual quality, animation, typography, color, or aesthetic coherence.
- **No design system or component library is mentioned.** The stack research recommends Tailwind CSS 4.2.2 as a "pragmatic default" with the note "not strategic; can be swapped." That is the entire extent of visual-layer planning.
- **No visual direction document exists.** There is no mood board, no reference screenshots, no color palette, no typography decision, no discussion of what the game should look or feel like.
- **"Watchability" is named but never defined visually.** The documents repeatedly identify watchability as a core thesis (Pitfall 4, FEATURES.md table stakes, seed document), but every mention is about information architecture ("clue state, lock state, reveal, standings") rather than about how those states look, move, or feel on a TV screen.
- **UI requirements are functional, not experiential.** UX-01 through UX-04 describe what must be present, never how it should feel. UX-01 says the host screen should be "watchable" but provides no criteria for what watchable means aesthetically.

This is a common failure mode in projects with strong technical leadership and no dedicated design voice. The architecture will be clean, but the first time friends see it on a TV, it will look like a developer tool with good data flow.

---

## 2. Specific Gaps Found

### Gap 1: No Visual Identity or Direction (Critical)

The project has a strong product identity ("expert F1 fan game night") but no visual identity. There is no answer to basic questions:

- What does this game look like?
- Is it dark or light? What colors?
- Does it reference F1 broadcast aesthetics, timing boards, team liveries, or circuit maps?
- What typefaces? What spacing? What information density?
- What happens visually when a round starts, when time runs out, when a reveal happens?

Without this, each implementation phase will make ad-hoc visual decisions that accumulate into an incoherent experience.

### Gap 2: No Distinction Between Host-Screen and Controller Design Treatment (High)

The architecture correctly separates host display and player controller as different client surfaces. The design treatment of these surfaces is never discussed. They have fundamentally different constraints:

| Dimension | Host Screen (TV) | Player Controller (Phone) |
|-----------|-------------------|---------------------------|
| Viewing distance | 2-4 meters | 30cm |
| Primary purpose | Shared spectacle | Private input |
| Typography scale | Large, bold, limited text | Standard mobile |
| Information density | Low, theatrical | Functional, task-oriented |
| Color/contrast | TV-optimized, dark backgrounds | Phone-friendly, readable in any lighting |
| Interaction | Host advances phases | Player taps, types, submits |
| Animation budget | High (reveals, transitions, scoring) | Low (responsive, immediate feedback) |

The current requirements treat these as the same design problem. They are not. The host screen is a broadcast production. The controller is a form.

### Gap 3: No Animation or Transition Design (High)

Game-night experiences live or die on the feeling of transitions: the countdown, the reveal, the score change, the leaderboard shuffle. The documents mention "reveal pacing" and "watchability" but never address:

- Countdown animations before clue reveal
- Lock-in confirmation feedback
- Reveal transitions (the moment the answer appears)
- Score tallying / leaderboard animation
- Round-to-round transitions
- Session end / winner celebration

These are not polish. They are the core experience of a party game. Kahoot understood this. A static render of correct answers is not a reveal.

### Gap 4: No Dark-Mode-First / TV-Optimized Thinking (Medium)

The host screen will be cast to a TV in a living room, likely in the evening. This means:

- Dark backgrounds are nearly mandatory (bright white on a 55" TV at game night is hostile)
- High contrast for readability at distance
- Careful color choices that work on consumer TV color profiles
- Font sizes that are legible at 3+ meters

None of this is discussed. The stack mentions Tailwind, which defaults to light mode and requires explicit dark-mode configuration.

### Gap 5: No F1 Visual Language Exploitation (Medium)

The project is steeped in F1 domain knowledge for content and gameplay but completely ignores F1 visual language for the interface. Missed opportunities:

- **Timing-board typography**: F1 broadcast graphics use distinctive monospace and condensed fonts for timing, lap data, and standings. This visual language is instantly recognizable to fans and could make the scoreboard and timer feel native to the sport.
- **Sector colors**: Green, yellow, purple sector timing is part of how F1 fans read performance. This color language could inform round-phase indicators.
- **DRS detection zones, pit lane entry graphics, track maps**: These are all visual elements fans associate with the sport that could inform UI metaphors.
- **Broadcast-style lower thirds and name cards**: Player names and scores could use broadcast overlay aesthetics rather than generic list layouts.
- **Grid position / starting lights**: Countdown and round-start could reference the five-lights-out sequence.
- **Chequered flag / champagne podium**: Session end and winner reveal could reference podium aesthetics.

This is low-hanging fruit that would make the game feel like an F1 product rather than a geography quiz with F1 data.

### Gap 6: No Responsive Design Strategy for the Controller (Medium)

UX-02 says the controller should be "usable on mobile." The current requirements do not address:

- Small phone vs large phone vs tablet
- Portrait vs landscape (phones will likely be in portrait)
- One-handed usability during a party (players are holding drinks, sitting on couches)
- Answer input method (typing circuit names? Selecting from a list? Tapping a map?)
- Touch target sizes for party conditions (slightly drunk, excited, rushed by timer)

### Gap 7: Tailwind Alone Is Not a Design System (Low)

The stack recommends Tailwind CSS as the styling layer. Tailwind is a utility framework, not a design system. Without design tokens (colors, spacing, typography scales, border radii, shadows, animation curves) defined up front, Tailwind will produce inconsistent visual output across phases and across the host/controller surfaces.

---

## 3. Framework & Tooling Recommendations

The stack research already recommends React + Vite + TypeScript. That is a sound foundation. The gap is in the design-layer tooling on top of it.

### Recommended Design Stack

| Layer | Recommendation | Why | Tradeoff |
|-------|---------------|-----|----------|
| **CSS framework** | Tailwind CSS 4 (already recommended) | Utility-first, fast iteration, good dark mode support | Needs design tokens defined manually |
| **Component primitives** | Radix UI or Ark UI | Unstyled, accessible primitives for dropdowns, dialogs, toasts, tabs. No visual opinion imposed. | More styling work than styled component libraries, but total control over aesthetics |
| **Animation** | Framer Motion 12+ | Best React animation library for orchestrated reveals, layout transitions, number counters, staggered lists. Critical for game-night feel. | Bundle size (~30KB), but worth it for the experience quality |
| **Design tokens** | Custom Tailwind theme + CSS custom properties | Define F1-inspired color palette, typography scale, spacing, and animation curves once, consume everywhere | Requires up-front design token work |
| **Typography** | Self-hosted variable fonts: one display face (condensed/bold for timing-board aesthetics), one body face | F1 broadcast feel without licensing issues. Candidates: Inter (body), JetBrains Mono or similar (timing), plus a condensed display face | Font selection requires taste and testing |
| **Icons** | Lucide React or Phosphor Icons | Clean, consistent, tree-shakeable | Minor choice |
| **TV host layout** | CSS Grid for layout, large font scale, minimal density | TV screens need theatrical layouts, not dense dashboards | Different layout system than controller |
| **Mobile controller** | Standard mobile patterns, touch-optimized, portrait-first | Mobile web best practices | Different design constraints than host |

### What NOT to use

- **shadcn/ui**: Often recommended, but its default aesthetic is "developer dashboard." The gray-and-white Vercel look is exactly wrong for a game-night TV experience. The underlying Radix primitives are excellent, but shadcn's default styling would need to be completely overridden.
- **Material UI / Chakra UI / Ant Design**: Enterprise design systems that would impose a non-game aesthetic and bloat the bundle.
- **Game-specific UI libraries (Phaser UI, PixiJS)**: Overkill. This is a web game with forms, lists, maps, and reveals, not a sprite-based game engine project.
- **CSS-in-JS (styled-components, Emotion)**: No advantage over Tailwind for this project shape, and worse for design-token consistency.

### SvelteKit Alternative Note

If the framework decision were reopened, SvelteKit would actually have a slight edge for the design dimension: Svelte's built-in transition/animation primitives (`transition:`, `animate:`, `in:`, `out:`) are more ergonomic than React + Framer Motion for the kind of orchestrated reveals this project needs. However, the ecosystem tradeoff documented in STACK.md still applies. The recommendation is to stay with React + Vite and add Framer Motion.

---

## 4. Recommended Approach: Design Contract Phase vs. Woven-In

### Recommendation: Add a design contract step before Phase 4, not a separate full phase

The current roadmap structure is sound. Phases 1-3 are backend/domain work where visual design is irrelevant. The design gap hits at Phase 4 (Guest Join and Mobile Controller UI) and Phase 5 (Host Screen and Watchable Session Flow). The problem is not that design needs its own multi-week phase. The problem is that Phases 4 and 5 will begin with zero visual direction and produce ad-hoc visuals.

**Proposed intervention**: Insert a lightweight design contract step (a `UI-SPEC.md` or equivalent) as a planning artifact before Phase 4 execution begins. This artifact would lock:

1. **Color palette**: Dark-mode-first F1-inspired palette (dark backgrounds, accent colors drawn from F1 broadcast aesthetics)
2. **Typography scale**: Host screen scale (large, theatrical) and controller scale (mobile-standard)
3. **Core components**: Visual treatment for timer, scoreboard, reveal card, clue display, answer input, countdown, round transition
4. **Animation vocabulary**: What moves, what fades, what counts up, what slides. Specific Framer Motion patterns for reveal, score update, round transition, countdown.
5. **Layout contracts**: Host screen grid (TV-optimized, low density) vs controller layout (phone portrait, touch-first)
6. **Reference mood**: 3-5 screenshots or mockups showing the intended feel. Not pixel-perfect designs, but enough to prevent "developer default" aesthetics.

This is a 1-2 day artifact, not a multi-week design phase. It should be treated as a planning dependency for Phase 4, not as a separate numbered phase.

### Why not a full separate design phase?

- The project is private-only and built by one developer. A formal design phase with wireframes, user testing, and iteration cycles would be disproportionate.
- The visual language for this product is relatively constrained: dark mode, F1 broadcast aesthetics, timing-board typography. The design space is narrow enough to lock with a contract document rather than requiring exploratory design work.
- The real risk is not "wrong design" but "no design." A contract that says "dark background, condensed timing font, Framer Motion reveals, these five colors" prevents 90% of the ugly-prototype failure mode.

### Why not just weave it into Phases 4 and 5 with no contract?

- Without a visual contract, Phase 4 will establish a visual language under time pressure, and Phase 5 will either inherit it (even if it was ad-hoc) or fight it.
- The host screen and controller are different design problems. Without a shared contract, they will diverge aesthetically.
- Animation and transition design is much harder to retrofit than to plan. A reveal that was built as a static render cannot easily become a cinematic moment without restructuring component logic.

---

## 5. Visual Direction Suggestions for an F1 Party Game

### The Core Aesthetic Principle

The game should look like **an unofficial F1 broadcast production**: dark, high-contrast, typographically confident, with the cinematic timing of a live broadcast reveal. It should not look like a quiz app, a geography tool, a dashboard, or a developer prototype.

### Color Palette Direction

```
Background:       #0F0F0F (near-black, TV-friendly)
Surface:          #1A1A1A (cards, panels)
Surface elevated: #252525 (modals, active elements)
Border:           #333333 (subtle separation)

Primary accent:   #E10600 (F1 red — sparingly, for critical actions and branding)
Timer/active:     #00D2BE (teal — Mercedes-era timing feel, high contrast on dark)
Correct/success:  #44D62C (sector green)
Warning/caution:  #FFC700 (yellow flag / sector yellow)
Best/purple:      #9B59B6 (purple sector / fastest lap)
Text primary:     #F0F0F0 (high contrast on dark)
Text secondary:   #888888 (muted labels)
```

This palette is dark-mode-first, TV-optimized, and speaks F1 visual language without being a slavish copy of any team's branding.

### Typography Direction

- **Display / Timing**: A condensed sans-serif for scores, timers, standings, countdowns. Something in the family of F1 broadcast timing graphics. Candidates: Barlow Condensed (free, open source, good condensed weights), or Oswald, or Fira Sans Condensed.
- **Body / UI**: Inter or similar neutral sans-serif for labels, buttons, explanations, mobile controller text.
- **Monospace / Data**: JetBrains Mono or similar for room codes, technical readouts, debug/admin data.

The key principle: the host screen should feel like looking at a timing board or broadcast graphic. The controller should feel like a clean, modern mobile app.

### Key Interaction Moments (Animation Vocabulary)

1. **Round start / countdown**: Inspired by F1 starting lights. Five dots or bars illuminate in sequence, then all go out ("lights out and away we go"). 2-3 seconds. High-energy.

2. **Clue reveal**: Each clue step slides or fades in with purpose. Not instant. The clue ladder should feel like progressive disclosure, building tension.

3. **Timer running**: A visible bar or arc that depletes. Not just a number counting down. The last 25% should change color (green to yellow to red) and possibly pulse.

4. **Lock-in confirmation**: On the controller, a satisfying haptic + visual confirmation. On the host screen, a subtle indicator that another player has locked in (builds tension without revealing the answer).

5. **Answer reveal**: The most important animation in the entire game. This should be theatrical. The correct answer appears with a dramatic transition. Scores animate upward. The reveal explanation fades in. Think of how F1 broadcasts reveal race results or qualifying positions: not instant, but paced for drama.

6. **Standings update**: Positions shift with smooth layout animation. If someone overtakes, the swap should be visible and satisfying, like a position change graphic on a broadcast.

7. **Session end / podium**: The top 3 (or however many) get a podium-style reveal. Names are large. There is a moment of celebration before the "play again" option appears.

### Host Screen Layout Principles

- **Maximum 3-4 pieces of information visible at any time.** A TV screen viewed from a couch cannot handle dashboard density.
- **Current state must be unambiguous at a glance.** A person walking back from the kitchen should be able to look at the TV and know: what round, what phase (clue / locked / reveal), who is winning.
- **Text must be readable at 3+ meters.** This means minimum ~32px equivalent for primary text, ~24px for secondary. Labels and fine print are not readable on a TV and should not be present.
- **Negative space is a feature.** The host screen should breathe. Empty space creates focus and drama.

### Controller Layout Principles

- **Portrait-first, one-handed.** Players are on a couch with a beer. The primary interaction zone should be in the lower 60% of the screen (thumb-reachable).
- **Answer input must be obvious and fast.** Whether it is a searchable dropdown, a tappable grid, or a map tap, the mechanic must work under time pressure with imprecise fingers.
- **Minimal chrome.** The controller should show: current clue (if visible on controller), answer input, timer, submit button. Not a full recreation of the host screen.
- **Status feedback, not full game state.** The controller tells you "your answer is locked" and "round 3 of 8" but does not try to replicate the reveal experience. That happens on the TV.

---

## 6. Concrete Recommendations

### Critical Priority

| # | Recommendation | Rationale |
|---|---------------|-----------|
| C1 | **Create a UI-SPEC.md design contract before Phase 4 begins.** This artifact locks color palette, typography, animation vocabulary, host-screen layout principles, and controller layout principles. | Without this, Phases 4 and 5 will produce visually incoherent output that undermines the game-night promise. The project explicitly identifies "watchability" and "socially alive" as core values but has zero visual-layer planning to deliver on them. |
| C2 | **Add Framer Motion (or equivalent animation library) to the recommended stack.** The current stack has no animation tooling. Static renders of reveals and scores will fail the watchability test. | Reveals, countdowns, score transitions, and standings animations are not polish for a party game -- they are the core experience. Pitfall 4 ("solvable on a phone, unreadable in a room") will materialize without them. |
| C3 | **Add visual quality to Phase 4 and Phase 5 success criteria.** Currently, success criteria are purely functional ("host screen presents clue state"). Add: "Host screen is visually legible at TV viewing distance with dark-mode-optimized styling" and "Reveal transitions include animation that creates dramatic pacing." | Functional success criteria produce functional output. The aesthetic bar matters for this project, and the planning artifacts currently provide no mechanism to enforce it. |

### High Priority

| # | Recommendation | Rationale |
|---|---------------|-----------|
| H1 | **Design the host screen and controller as separate design problems with different constraints, sharing a common design-token foundation.** | Architecture.md already separates these as different client surfaces. The design contract should make this separation explicit at the visual layer too, with different typography scales, information density, and interaction patterns. |
| H2 | **Adopt dark-mode-first / TV-optimized as a hard constraint for the host screen.** Do not build light-mode first and add dark mode later. The primary surface (TV in a living room) demands dark backgrounds from day one. | Retrofitting dark mode is significantly harder than building dark-first. The host screen will never be used in light mode. Controller dark mode can follow. |
| H3 | **Add Radix UI (or Ark UI) for accessible unstyled component primitives.** This prevents reinventing dropdowns, modals, toasts, and similar interaction patterns while maintaining full visual control. | The project needs modals (join room), dropdowns (pack selection), toasts (connection status), and similar patterns. Building these from scratch wastes time; using a styled library (MUI, shadcn defaults) imposes the wrong aesthetic. |

### Medium Priority

| # | Recommendation | Rationale |
|---|---------------|-----------|
| M1 | **Develop an F1-inspired visual language document (mood/reference collection) before Phase 4 planning.** Collect 5-10 reference screenshots from F1 broadcasts, timing screens, and race-graphic overlays to anchor the aesthetic direction. | This costs almost nothing and prevents the most common failure mode: a developer building what "feels right" in the moment, producing generic light-gray-on-white developer UI. |
| M2 | **Select and self-host 2-3 typefaces early.** One condensed display face for timing/scores, one clean body face, one monospace for codes/data. Lock these before Phase 4. | Typography is the single highest-leverage visual decision. The right condensed font on the timing board will do more for the F1 feel than any amount of color or animation work. |
| M3 | **Plan the answer input mechanic for mobile before Phase 4 implementation.** Decide: is it a searchable text field? A scrollable list? A tappable map? A card-selection UI? This affects the entire controller design. | This is a UX design question that the current requirements leave completely open. "Answer entry and submission" (UX-02) does not specify the interaction pattern, and the wrong choice will feel clunky under game-night time pressure. |
| M4 | **Add responsive breakpoints to the design contract.** At minimum: host-screen (1080p+ landscape), phone-portrait (320-428px width), and tablet (optional). | The project will run on at minimum two radically different screen sizes. Without explicit breakpoints, responsive behavior will be improvised. |

### Low Priority

| # | Recommendation | Rationale |
|---|---------------|-----------|
| L1 | **Consider haptic feedback on the controller for lock-in confirmation.** The Vibration API is widely supported on Android and partially on iOS Safari. A short vibration on answer submission adds satisfying tactile feedback. | Low effort, meaningfully improves the controller experience. Not essential, but adds polish. |
| L2 | **Consider sound design as a future concern.** Countdown ticks, lock-in sounds, reveal fanfares, and round-start audio would significantly enhance the party experience. This is out of scope for visual design but should be noted as a future enhancement surface. | Sound is the other half of the "broadcast production" feel. Not critical for v1 but should be on the radar. |
| L3 | **Document the Tailwind theme configuration as a shared package** (`packages/ui` or `packages/design-tokens`). Both `apps/web` host and controller surfaces should consume the same token set. | Prevents color/spacing/font drift between surfaces. Low urgency because the monorepo structure already supports this, but it should be explicit. |

---

## 7. Risk Summary

| Risk | Likelihood Without Intervention | Impact | Mitigation |
|------|--------------------------------|--------|------------|
| Functional-but-ugly UI across Phases 4-5 that needs aesthetic rewrite | **Very High** | High | UI-SPEC.md design contract before Phase 4 |
| Host screen that is readable on a laptop but illegible on a TV | **High** | Critical (undermines primary use case) | TV-first design constraints, dark mode, large typography |
| Reveals that feel administrative rather than dramatic | **Very High** | High (undermines watchability thesis) | Animation library, reveal transition design |
| Controller that is awkward to use during a party | **High** | Medium | Mobile-first design, touch-optimized input, portrait-first |
| Visual incoherence between host and controller surfaces | **Medium** | Medium | Shared design tokens, separate layout contracts |
| Generic quiz-app aesthetic that fails to evoke F1 | **High** | Medium | F1 visual language reference, condensed timing typography, F1-inspired palette |

---

## 8. Summary

The Prix Guesser project has strong architectural, content, and product thinking. It has no design thinking whatsoever. The roadmap will produce a technically sound game that looks like a developer prototype unless visual quality is treated as a first-class concern before the UI phases begin.

The intervention is lightweight: one design contract document (UI-SPEC.md), one animation library addition to the stack, and amended success criteria for Phases 4 and 5. This is not asking for a design agency or a Figma workflow. It is asking for the same level of intentionality about how the game looks and feels that the project already brings to how the content is modeled and how the room state is synchronized.

The aesthetic bar is achievable with the recommended stack (React + Vite + Tailwind + Framer Motion + Radix + good typography + a dark F1-inspired palette). The risk is not technical difficulty. The risk is that nobody asked the question "what should this look like?" before writing the first component.

---

*Audit completed: 2026-04-08*
*Auditor scope: Lane 2 -- Frontend Design & Aesthetics Gap Analysis*
*Input artifacts: PROJECT.md, REQUIREMENTS.md, ROADMAP.md, research/SUMMARY.md, research/STACK.md, research/FEATURES.md, research/ARCHITECTURE.md, research/PITFALLS.md, discovery/14-gsd-seed.md*
