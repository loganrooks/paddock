---
date: 2026-04-12
lane: c
lane_name: "Player-generated expression"
orientation: exploratory
delegation_class: execution/verification
output_file: 02-lanes/round-1/lane-c-output.md
tags:
  - exploratory-audit
  - round-1
  - lane-c
  - expression
  - player-generated
---

# Lane C Task Spec

## What this lane owns

This lane handles the player-generated expression part of Round 1 for the game-mode exploratory audit.

Owned scope:
- `Paddock Fashion`
- `Meme Prompts`

Out of scope:
- final portfolio ranking across all modes
- final cross-lane synthesis
- treating player creativity as automatically sufficient for replay
- reducing evaluation to “this will go viral” or “this is shallow”

This is a provisional Round 1 bundle. If the main thread decides one of these modes is better handled elsewhere or needs to stand alone, the boundary may be revised.

## Root contract

This lane is a child spec under:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md`

This lane must remain compatible with that root spec.

## Purpose

Your job is to explore where the players themselves become the content engine: their taste, jokes, performance, submissions, or creative interpretation.

You should:
- distinguish modes that merely invite expression from modes that shape expression into a repeatable game loop
- identify what makes the reveal structure funny now versus durable later
- map how these modes change across local, sync, async, private-group, and public/community contexts
- surface where remix/UGC helps and where it becomes moderation or quality burden

## Source read set

Required:
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-INDEX.md`
- `.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md`
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md`
- `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINT.md`
- `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md`

Conditional:
- `.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md` only when a finding turns on deferred moderation, content-supply, or social-system research
- `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md` only when UGC, persistence, or room-model implications materially change the shape of the mode

## Anti-goals

Do NOT:
- assume “player-generated” means design problems disappear
- assume “memey” means disposable
- assume public internet virality is automatically desirable
- assume every expressive mode should become community/UGC-first
- treat user-origin as proof the mode is already solved

## Lane-specific questions

You must pressure this lane with questions like:

- what makes player expression legible, funny, or dramatic enough to reveal well?
- what scaffolding is needed so “players make the content” does not become blank-page anxiety or low-quality sludge?
- what makes the same group want another round rather than exhausting the joke immediately?
- where do friend-group history and inside jokes deepen the mode?
- what variant forks exist between private-group fun, streamer/spectator fun, async remix fun, and public/community forms?
- where does voting/judgment structure matter?
- how much authored curation is still needed even in a player-generated lane?
- what moderation or safety burdens emerge only if the mode crosses from private room to public community?

## Required lenses

Address each of these explicitly:

1. `What is already here`
   What is concrete, what is thin, and what has or has not been pressure-tested with the user.

2. `Possibility expansion`
   Variant forks around prompts, submission systems, reveal formats, judging systems, recurring packs, private history, and public/remix layers.

3. `Context profile / tension map`
   Where private local play is strongest, where sync or async works well, where public/community features help, and where they would distort the core appeal.

4. `User situations`
   At minimum consider:
   - mixed-knowledge couch group
   - recurring friend group
   - remote Discord group
   - watch-party/stream/spectator contexts
   - solo or semi-solo async remix contexts where relevant

5. `Community / online potential`
   Friend-group history, public remix, UGC, spectator value, event cadence, async viability, and moderation implications.

6. `Virality vs replayability`
   What gets clipped/shared versus what sustains repeat play, repeat prompting, or evolving group culture.

7. `Launch-gap lens`
   Onboarding, blank-page risk, moderation/safety, content burden, session-length fit, mixed-skill-group friendliness, and funny-once risk.

8. `Category exceedance`
   What good play shape appears here that the current context grid does not capture well.

## Output requirements

Write:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/round-1/lane-c-output.md`

Your output must contain these sections:

1. `Lane framing`
2. `What is already strong`
3. `What is weak / thin / generic`
4. `Variant forks and possibility expansion`
5. `Context profile / tensions`
6. `Virality vs replayability`
7. `Community / online / spectator potential`
8. `What to park for later research`
9. `What the categories did not capture`
10. `Recommendations for central synthesis`

## Quality bar

Good output for this lane should:
- distinguish expressive freedom from game-shaping structure
- identify when friend-group history is the real engine
- expose where public/community extensions help or cheapen the mode
- preserve multiple viable versions instead of flattening them into one content model
