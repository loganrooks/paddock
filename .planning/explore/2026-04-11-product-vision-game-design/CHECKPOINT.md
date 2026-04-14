# Checkpoint: Product Vision & Game Design Exploration

Updated: 2026-04-12
Status: active exploration, mid-session

## Recovery Path

Read in this order:

1. `HANDOFF.md` — the original exploration entry point with full project context, all six threads, BoxBoxd reference, and session norms
2. `CHECKPOINTS/01-words-of-wisdom-and-game-modes.md` — what the first session actually did, key design decisions, where we left off, and the burst of unfinished ideas

### If resuming the content pipeline

Check extraction status in `scraped-radio/`:
```
tail -5 extraction-run.log
ls v4-*.md | wc -l
```
The `run-extraction.sh` script is resumable — re-run if it crashed.

## Where We Are

The first session went deep on one game mode ("Words of Wisdom" — Fibbage-style team radio game) and built a content sourcing pipeline for it (347 transcripts from racefans.net, Codex agents extracting promising exchanges). The broader exploration threads (multiplayer shapes, platform maturity, substrate architecture, architectural foreclosure) are mostly untouched.

The user was in a burst of rapid-fire ideas when context ran out — sound-based games, driver personality games, cooperative pit stop games, party mode composition ("Grand Prix" style), audio integration for reveals. These are seeds, not designs.

## What Changed From the Handoff

Nothing in the HANDOFF is invalidated. The exploration confirmed and extended the game-design dimensions framework from the triggering session. Key additions:
- The "shared cultural fluency" dimension (meme/radio culture as game content, distinct from trivia)
- The "accessibility through creativity" insight (non-trivia modes are naturally inclusive of mixed-knowledge groups)
- The "hidden discovery" product architecture (meme modes as unlockable easter eggs, not front door)
- The viral + longevity formula (different mechanisms serve different functions)
- A concrete game mode design (Words of Wisdom) with content pipeline
