# Project Research Summary

**Project:** Prix Guesser
**Domain:** Private browser-based F1 geography / circuit party game
**Researched:** 2026-04-08
**Confidence:** MEDIUM-HIGH

## Refresh Note (2026-04-11)

This file remains canonical for the content/rules/room separation and the private-first, authored-round product thesis.

Read it with these later refinements from the 2026-04-10 research wave and the refreshed canon:

- live private rooms remain the first wrapper, but future async, spectator, and public-read surfaces are explicit later wrappers rather than rejected futures
- browser-first operator launch, join URL and QR flow, and TV-distance host readability are now explicit v1 concerns
- the UI and interaction contract is a formal gate before Phase 4 implementation, not an implicit polish task
- `Supabase` should be read as one optional managed convenience, not the canonical hosting posture

## Executive Summary

Prix Guesser is not best understood as a generic geography game with Formula 1 theming. The research consistently points toward an authored, expert-first F1 game in which the core value comes from recognizing circuits, venue texture, sections, eras, and clue logic that feel native to fandom. The product shape experts build for this is content-first and room-aware: authored packs, explicit answer surfaces, reveal explanations, and a host-friendly private session loop that works across a shared screen and phone controllers.

The strongest implementation direction is a split architecture rather than a monolithic web framework choice. Research across stack and architecture recommends a shared TypeScript domain model, frozen match snapshots, a pure rules layer, and an authoritative room runtime, with `React + Vite + TypeScript` as the practical frontend baseline and `PostgreSQL + Drizzle` plus provider-neutral media storage as the durable content substrate. `Supabase` can remain a later hosted convenience, but it should not be treated as the canonical runtime assumption. There is still a real implementation fork on live rooms: `Colyseus` is the stronger default if reconnect safety, timer correctness, and self-host parity matter early, while `PartyKit` remains credible if the first milestone is explicitly optimizing for the fastest private prototype. That disagreement should stay open until roadmap planning decides how durable the first room promise really is.

The biggest risks are not cosmetic. They are product-shape failures: shipping a thin geo clone, letting venue-approach clues quietly replace circuit-internal recognition, and broadening into a party platform before the anchor mode proves repeat play value. The roadmap should therefore prove one authored anchor mode and one social wrapper first, with content validation, scoring clarity, and watchable reveals treated as foundational work rather than later polish.

## Key Findings

### Recommended Stack

The stack research is confident about the product shape even where one runtime choice remains open. The recommended baseline is a TypeScript workspace with `React 19.2.5`, `Vite 8.0.7`, `TypeScript 6.0.2`, `Zod 4.3.6`, `TanStack Query 5.96.2`, and `Zustand 5.0.12` on the client side; `PostgreSQL 18`, `Drizzle ORM 0.45.2`, and `Supabase` for durable data and assets; `MapLibre GL JS 5.22.0` for answer/reveal maps; and Google Street View only as one clue provider rather than the root platform dependency.

The main stack disagreement is deliberate, not accidental. `Colyseus 0.17.8` is the better fit if the roadmap promises authoritative room state, reconnect handling, and reliable timers from the start. `PartyKit 0.0.115` is faster to prototype with, but the research rates it as a speed-first fallback rather than the default because room recovery and long-term cleanliness rely on more house discipline. Stack confidence is therefore high on boundaries and medium on the initial room runtime pick.

**Core technologies:**
- `React + Vite + TypeScript` — frontend shell for host and controller surfaces; recommended because gameplay is client-heavy and this stack maximizes ecosystem leverage without forcing a server-first app model.
- `Colyseus` or `PartyKit` — realtime room runtime; `Colyseus` for correctness-first live rooms, `PartyKit` only for a speed-first private prototype.
- `PostgreSQL + Drizzle + Supabase Storage` — durable substrate for authored packs, media manifests, snapshots, and session summaries; recommended because content is relational and needs explicit schemas.
- `Zod` — domain validation for authored packs, imports, and room messages; recommended because schema drift is one of the highest-risk failure modes.
- `MapLibre GL JS` — primary answer and reveal map layer; recommended to avoid making Google Maps the whole product surface.
- Google Street View — optional clue family only; recommended selectively because coverage, billing, and pano stability remain uneven.
- `Vitest + Playwright` — test split for rules/domain logic and multi-client room flows; recommended because reconnects, timers, and reveals need automated coverage.

### Expected Features

The feature research is clear that v1 table stakes are mostly about making private expert-fan play actually work, not about matching the full breadth of geography or party-game products. The product needs authored F1 round packs, circuit-aware answer handling, private rooms with host control, fast join on phones and browsers, pacing controls, and satisfying reveal/score flows. It does not need public ladders, broad UGC, daily retention loops, or a buffet of unrelated side modes at launch.

The most important differentiator near v1 is not “more modes.” It is richer F1-native answer surfaces and clue ladders: circuit, venue, and eventually section/corner-level answers with reveal cards that explain why the round was identifiable. That makes the product feel expert and authored rather than like a world-geo clone with a motorsport skin.

**Must have (table stakes):**
- Authored F1 round packs with layered clue ladders and reveal explanations.
- Circuit-aware answer surfaces, at minimum `circuit` and `venue`.
- Private room flow with host control, join by link/code/QR, and guest nicknames.
- Phone-friendly controller participation alongside a watchable shared-screen flow.
- Round pacing controls: timer, clue cadence, and exploration restrictions.
- Round-by-round results, reveal states, scoreboard, and session summary/rematch flow.
- A curated starter pack set built around high-recognition circuits and venue contexts.

**Should have (competitive):**
- Finer-grained answer surfaces such as `section` or `corner`.
- Mixed-media clue ladders beyond Street View: crops, map snippets, text, atmosphere, era cues.
- Rich reveal cards that explain the identification logic.
- Expert difficulty lanes and themed packs by era or venue texture.
- Team and hybrid couch-play structures once the base room loop is stable.

**Defer (v2+):**
- Public matchmaking, ranked ladders, serious anti-cheat, and mass multiplayer.
- Broad public UGC publishing or a map marketplace.
- Daily challenge and streak systems as roadmap drivers.
- Unrestricted Street View free-roam as the default experience.
- Accounts, cosmetics, progression economies, and collection systems.
- Adjacent non-geography party modes until the shared content substrate is proven.

### Architecture Approach

The architecture research is the clearest of the four inputs: separate authored content, pure game rules, and live room orchestration as hard boundaries. That separation matters more than frontend framework choice because it preserves the project’s real open decisions: whether the first serious wrapper is live rooms or challenge links, how far host-screen-first play goes, and whether `Colyseus` or `PartyKit` is the better room runtime for the first milestone. The room layer should consume a frozen match snapshot, own timers and phase truth, and treat clients as intent senders plus renderers.

**Major components:**
1. Content model package — owns pack, round, clue, answer target, reveal, scoring, and validation vocabulary.
2. Content repository / compiler — normalizes authored files or sheet exports into validated, versioned playable content.
3. Match snapshot service — freezes a specific session so live rooms never read mutable authoring state mid-game.
4. Game rules engine — pure functions for validating submissions, scoring rounds, and building reveal payloads.
5. Authoritative room service — owns room lifecycle, host authority, timers, submissions, reveals, reconnects, and scoreboard state.
6. Client surfaces — separate host display, player controller, and later solo/admin surfaces built on shared contracts instead of one giant app-state tree.
7. Persistence / asset layer — stores packs, media, snapshots, and summaries, but does not become the live timer or phase authority.

### Critical Pitfalls

1. **Shipping a generic geo quiz with F1 paint** — avoid this by making answer target type, clue intent, and reveal explanation first-class in the round model from the start.
2. **Letting venue-approach clues replace circuit-internal recognition** — avoid this by explicitly classifying clue families and tracking pack composition so easy city-context rounds do not become the silent default.
3. **Using a thin `lat/lng + pano` schema** — avoid this by starting with authored round contracts that support aliases, era, clue ladders, reveal explanation, and partial-credit logic.
4. **Ambiguous answer surfaces and scoring contracts** — avoid this by declaring the answer surface up front, storing accepted aliases and partial-credit rules in content, and regression-testing sample judgments.
5. **Avoiding the room-authority decision** — avoid this by deciding where timers, score, reveal flow, and reconnect truth live before debating transport or backend branding.
6. **Ignoring reconnect and phone sleep/wake behavior** — avoid this by assigning stable room-session player tokens and testing real phones early, not just desktop tabs.
7. **Expanding into a broader party platform too soon** — avoid this by proving one anchor mode and one social wrapper before adding daily loops, side modes, or async wrappers.

## Implications for Roadmap

**Update 2026-04-11:** Treat the numbered phase sketch below as ordering rationale, not as the active roadmap. The canonical phase list now lives in `.planning/ROADMAP.md`, which keeps the same private-room spine but uses a 7-phase roadmap plus a formal Phase `3.1` UI contract gate.

Based on the combined research, the roadmap should prove the authored F1 substrate before it tries to prove scale, breadth, or long-term retention systems. The right grouping is not “frontend, backend, content” in isolation; it is “content grammar, rules truth, live-room orchestration, then playability hardening.”

### Phase 1: Anchor Domain and Content Contract
**Rationale:** Every other decision depends on the round model, answer taxonomy, clue grammar, and reveal contract. Research treats this as the highest-leverage choice in the whole project.
**Delivers:** Shared domain schemas, validation rules, round fixtures for multiple round families, initial authored pack structure, and a starter corpus plan.
**Addresses:** Authored round packs, circuit-aware answer surfaces, curated starter content.
**Avoids:** Generic geo-clone drift, thin-schema rewrites, ambiguous scoring contracts.

### Phase 2: Rules Engine and Playable Dry-Run
**Rationale:** The game loop should become testable before realtime complexity arrives. This phase converts the content contract into deterministic scoring and reveal behavior.
**Delivers:** Match snapshot format, pure scoring logic, reveal payload builder, phase reducer, regression fixtures, and a minimal single-round preview/simulation runner.
**Addresses:** Reveal quality, scoring clarity, pack-level rules, difficulty calibration groundwork.
**Avoids:** Room logic absorbing game semantics, scoring ambiguity hidden in UI code.

### Phase 3: Live Room Foundation
**Rationale:** Once content and rules are stable, the room layer can focus on orchestration. This is the phase where the roadmap must resolve whether the first serious runtime is `Colyseus` or `PartyKit`.
**Delivers:** Room create/join flow, host authority, canonical timer and phase state, submissions, reconnect tokens, rematch skeleton, and transport contracts shared by host/controller clients.
**Uses:** `Colyseus` by default if correctness-first; `PartyKit` only if the milestone is explicitly speed-first.
**Implements:** Authoritative room service, event contracts, public/private state separation.
**Avoids:** Split authority between host and server, no reconnect story, backend-choice theater without an authority model.

### Phase 4: Host Screen, Phone Controller, and Watchable Session Loop
**Rationale:** The product promise is social and watchable, not just technically multiplayer. This phase turns the room foundation into an actual session that works in a living room or remote friend group.
**Delivers:** Host display states, phone-friendly answer UI, join by code/link/QR, clue/reveal/standings presentation, and one polished end-to-end anchor mode session.
**Addresses:** Low-friction join, shared-screen plus personal-device play, reveal pacing, scoreboard, rematch loop.
**Avoids:** Solvable-on-phone but unreadable-in-room UX, flattening reveal quality into admin screens.

### Phase 5: Content Pipeline, Validation, and Calibration
**Rationale:** The project cannot learn fast if each round is a bespoke rescue operation. After the first playable loop exists, the next leverage point is reliable content throughput and structured playtest learning.
**Delivers:** Import/compile workflow, venue media profiles, Street View validation and fallback checks, pack linting, session logs, round-quality signals, and pack-mix tracking across venue classes.
**Addresses:** Curated corpus growth, mixed-media clue ladders, fairer difficulty curation, reveal tuning.
**Avoids:** Street View brittleness, corpus distortion toward easy city circuits, flying blind in playtests, late content-tooling pain.

### Phase 6: Hardening, Session Durability, and Targeted Expansion
**Rationale:** Only after the anchor loop has repeat-play value should the roadmap expand the shell. This phase should harden reliability first, then selectively widen the game.
**Delivers:** Better reconnect recovery, session summaries, room debug visibility, analytics-informed round pruning, and one carefully chosen extension such as team play or finer-grained section answers.
**Addresses:** Replayability, couch/hybrid depth, stronger expert-fan differentiation.
**Avoids:** Premature party-platform sprawl, adding breadth before the core loop is trustworthy.

### Phase Ordering Rationale

- The content contract must precede room and UI work because the core product risk is semantic, not rendering-related.
- The rules engine should precede live rooms so realtime code orchestrates pure functions instead of hiding product logic in transport handlers.
- The room-authority decision belongs before polished host/controller surfaces because reconnect, timers, and submission truth shape both UX and test strategy.
- Watchability is not a polish layer; it belongs in the first end-to-end playable milestone because the product is explicitly social.
- Content pipeline and calibration follow the first playable loop because they need real sessions to reveal where authoring and media workflows hurt.
- Expansion should happen only after the anchor mode and one social wrapper show repeat-play value with real groups.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 3: Live Room Foundation** — the roadmap must decide how much durability the first room promise includes, because that determines `Colyseus` versus `PartyKit`.
- **Phase 5: Content Pipeline, Validation, and Calibration** — Google Street View coverage, metadata validation, billing/policy constraints, and fallback-media strategy need venue-specific operational planning.
- **Phase 6: Hardening, Session Durability, and Targeted Expansion** — section/corner answer surfaces, team play, and any async or challenge wrapper should only be planned after observing real session behavior.

Phases with standard patterns that likely do not need a separate research phase:
- **Phase 1: Anchor Domain and Content Contract** — the main work is project-specific modeling, but the implementation tools (`TypeScript`, `Zod`, workspace packages) are established.
- **Phase 2: Rules Engine and Playable Dry-Run** — pure-function domain logic, fixtures, and test harnesses follow well-known patterns.
- **Phase 4: Host Screen, Phone Controller, and Watchable Session Loop** — the UI is product-specific, but the technical patterns around shared contracts, responsive views, and browser join flows are conventional enough to proceed directly.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | MEDIUM-HIGH | Strong on boundaries and default technologies; medium on the initial room runtime because `Colyseus` vs `PartyKit` depends on the first milestone’s durability promise. |
| Features | MEDIUM-HIGH | Strong agreement on v1 table stakes and anti-features from comparable products; some differentiators remain intentionally sequenced later rather than fully decided now. |
| Architecture | HIGH | The separation between content, rules, and live room state is the most consistent conclusion across sources and should be treated as settled direction. |
| Pitfalls | HIGH for content/media and room-state risks; MEDIUM for broader product-shape risks | The most critical failure modes are well-specified, but broader questions around long-term expansion remain intentionally open. |

**Overall confidence:** MEDIUM-HIGH

### Gaps to Address

- **First wrapper choice remains open:** research leans toward host-screen private rooms first, but the roadmap should still explicitly choose between live rooms first and any challenge-link wrapper before planning deep implementation.
- **Room runtime remains open:** decide whether v1 promises reconnect and timer correctness strongly enough to justify `Colyseus` immediately.
- **Answer-surface depth is unresolved:** `circuit` and `venue` are clearly first-wave; `section` and `corner` need explicit milestone placement based on authoring burden and UI clarity.
- **Street View dependence needs per-venue validation:** do not assume the same clue strategy works across all circuits; the content plan needs visible fallback classes.
- **Authoring workflow threshold is unresolved:** file-first is recommended now, but the roadmap should define the trigger for when internal authoring UI becomes worth building.

## Sources

### Primary project research
- `.planning/PROJECT.md` — product posture, open questions, constraints, and current decisions.
- `.planning/research/STACK.md` — recommended technologies, alternatives, version requirements, and decision confidence.
- `.planning/research/FEATURES.md` — table stakes, differentiators, anti-features, and dependency structure.
- `.planning/research/ARCHITECTURE.md` — system boundaries, data flow, build order, and confidence notes.
- `.planning/research/PITFALLS.md` — phase-specific risks, prevention strategies, and open decisions that should remain open.

### Primary external / official sources carried through from research
- React, Vite, Colyseus, PostgreSQL, Drizzle, Supabase, MapLibre, and Google Maps official docs and package references cited in `STACK.md`.
- GeoGuessr and Kahoot help/docs plus the cited open-source references (`geohub`, `Geo-Locator`, `react-geofindr`) carried through from `FEATURES.md`.
- Colyseus and PartyKit official docs cited in `ARCHITECTURE.md` and `PITFALLS.md`.
- Google Maps Street View metadata, request, billing, and policy docs cited in `PITFALLS.md`.

### Confidence framing preserved from source documents
- `STACK.md`: **MEDIUM-HIGH overall**, with high confidence on boundaries and lower confidence on the first room-runtime choice.
- `FEATURES.md`: **MEDIUM-HIGH overall**, with strong confidence on private-room table stakes and deliberate deferral of breadth.
- `ARCHITECTURE.md`: **HIGH for boundary recommendations**, **MEDIUM for concrete infrastructure choice**.
- `PITFALLS.md`: **HIGH for content/media and room-state pitfalls**, **MEDIUM for broader product-shape pitfalls**.

---
*Research completed: 2026-04-08*
*Ready for roadmap: yes*
