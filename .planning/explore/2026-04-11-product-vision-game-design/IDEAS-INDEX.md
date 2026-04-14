# Ideas Index

> **NOTHING IN THESE DOCUMENTS IS A DECISION, REQUIREMENT, OR COMMITMENT.**
>
> These are brainstorming scratchpads from an exploration session (2026-04-11/12). Everything is speculative — ideas at various stages of development, possible variations, open questions, and early observations about what MIGHT have architectural implications. The status labels indicate how developed an *idea* is, not how committed we are to it.
>
> When entries mention "architectural decisions," "M1 implications," or "transition paths," these are **flags for future deliberation** — things that probably need proper analysis before being locked in, not conclusions reached here. The brainstorming identified them; the planning process decides what to do with them.
>
> Entries that describe how something "works" or "should" behave are describing the brainstormed concept, not prescribing implementation. All of this feeds into future discuss-phase, planning, and deliberation as raw input — not as pre-decided scope.

## Status key
- **seed** — named but not developed
- **developing** — actively being shaped, still speculative
- **designed** — mechanic concept is clear enough for feasibility/substrate analysis (NOT "ready to build")
- **parked** — interesting but not strong enough yet, or blocked on research
- **merged** — folded into another idea

## Provenance / engagement signal

Some mode entries also carry a **user engagement signal**. This is not a priority ranking and not a proxy for quality. It is just a note about how much direct user initiation and conversational pressure-testing an idea has already received.

Useful distinctions:
- **user-initiated, explored** — the user brought it in and spent real time shaping it
- **user-initiated, lightly explored** — the user brought it in but it still has large unexplored surface area
- **assistant-proposed, user-positive** — the user liked it or adopted it, but did not spend much time pressure-testing it yet
- **not yet meaningfully pressure-tested by user** — present in the brainstorm, but still relatively untested in direct conversation

The audit should use this as a reading aid:
- higher-engagement ideas deserve more careful reading because they already survived some conversational pressure
- lower-engagement ideas should not be dismissed, because they may still contain strong unrealized territory

## Documents

### [IDEAS-game-modes.md](IDEAS-game-modes.md) — Individual Game Mode Designs
All brainstormed game modes with their mechanics, variations, round types, content sourcing, and mode-specific open questions.

Modes covered:
- **Words of Wisdom** (designed) — Fibbage-style team radio game
- **The Stewards' Room** (developing) — structured argument / verdict game
- **Team Principal's Desk** (developing) — strategy dilemma game
- **Pit Stop Co-op** (seed) — Overcooked-style cooperative pit stop
- **The Verstappen Game** (developing) — PS1 horror/survival, Max as unkillable predator, 3 variants
- **Talibantonelli / Al Mer Qaedes** (developing) — demolition derby + social deduction racing, 5 modes, hunter character profiles
- **Sound-based Games** (seed) — engine ID, commentator clips, crowd reactions
- **Paddock Fashion** (developing) — drawing/creation + fashion show, 12+ round types, 4 creation tiers
- **Meme Prompts / Quiplash** (seed) — Quiplash-style creative prompt game for F1 meme culture
- **The Grid Walk** (seed) — cooperative information asymmetry
- **Relive the Moment** (merged into Stewards' Room / TP's Desk)

### [IDEAS-platform.md](IDEAS-platform.md) — Platform Experience & Social
Platform-level concepts: how games compose into sessions, engagement layers, competitive/ranked systems, community features, content delivery patterns, social architecture.

Topics covered:
- Circuit Party Packs (evergreen multi-game bundles organized by circuit)
- Calendar / Live Layer (race weekend content cadence, reactive post-race content, off-season)
- Platform composition (how games relate — Grand Prix, Jackbox, playlist, carnival models)
- Four engagement layers (free play, friends/party, ranked, career/teams)
- Ranked system (F4→F3→F2→F1 tiers, matchmaking, Elo/MMR)
- Career / team mode (constructors' championship, season-long, draft/recruitment)
- Driver Select as session identity frame
- Community content creation (circuit designer, round builders, theme packs)
- Between-sessions social (group history, shareable moments, inside jokes)
- Platform branding (prix-guesser is a game name, not a platform name)
- The Hidden Discovery Architecture
- Viral + Longevity Formula

### [IDEAS-cross-cutting.md](IDEAS-cross-cutting.md) — Cross-cutting Design Concepts
Design principles and insights that apply across multiple modes rather than belonging to any single one.

Topics covered:
- Era as content dimension
- Personality as flavor vs. mechanic
- Content sequencing insight (text → audio → visual)
- Accessibility through creativity (non-trivia modes are naturally inclusive)
- "Your friends are the content" principle

### [IDEAS-architecture.md](IDEAS-architecture.md) — Architectural Surface Area
Observations about what MIGHT need early architectural consideration. Flagged for deliberation — not requirements.

Topics covered:
- Display / host screen architecture (4 configurations: local, online sync, async, hybrid)
- Per-mode configuration examples (how each mode works in each context)
- Room / session join flow
- Phone input abstraction
- 2D + 3D rendering coexistence
- Content access control
- Real-time vs. turn-based networking
- Player count scaling (interaction patterns, local vs. online, client/server separation)
- Foreclosure risks (7 implicit assumptions that could lock out future possibilities)
- Other considerations (reconnection, assets, replay, voice, offline, accessibility, localization)

## Supporting documents

- [RESEARCH-TODOS.md](RESEARCH-TODOS.md) — 14 research questions flagged for Codex investigation
- [HANDOFF.md](HANDOFF.md) — original exploration entry point with full project context
- [CHECKPOINTS/01-words-of-wisdom-and-game-modes.md](CHECKPOINTS/01-words-of-wisdom-and-game-modes.md) — session 1 checkpoint
