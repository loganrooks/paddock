# Checkpoint 01: Words of Wisdom Deep Dive and Game Mode Landscape

Date: 2026-04-12
Session: `2026-04-11-product-vision-game-design`

## What This Session Did

This was the first exploration session spawned from the HANDOFF.md written during the Phase 01 prep audit. The HANDOFF laid out six threads to explore. This session went deep on Thread 1 (Game Modes and Experiences) and Thread 6 (Creative Modes Beyond "X but for F1"), touched Thread 2 (Multiplayer Shapes) and Thread 3 (Platform Maturity Vision), and didn't reach Thread 4 (Substrate Question) or Thread 5 (Architectural Foreclosure) in any meaningful way.

The session's arc was: broad game-mode brainstorming → the user pulling toward memes, radio culture, and shared F1 cultural fluency → deep dive into a specific game mode ("Words of Wisdom") → building a content sourcing pipeline for that mode → the user firing off a burst of further game ideas just before context ran out.

## The Key Move: From Trivia to Cultural Fluency

The exploration started by asking what game experiences are uniquely enabled by the intersection of F1's properties (places + history + drama + knowledgeable fans + calendar + opinion culture). The initial framing separated these from BoxBoxd's approach: BoxBoxd treats F1 content as interchangeable tokens (swap the dataset and the game still works), while the most interesting prix-guesser modes would be ones that **can only exist because of F1's specific cultural texture**.

The user pushed this further by bringing up memes, radio culture, and "words of wisdom" — the verbal layer of F1 fandom. This is the dimension that makes F1 fandom feel different from other sports: you hear the private conversations (team radio), drivers are characters performing personality in public, and fans absorb all of it into shared reference language. The memes aren't decoration — they're how fans process the emotional reality of the sport.

This reframed the game design question: not "what F1 facts can we quiz people on?" but "what game shapes turn the bonding ritual of quoting radio at each other into structured play?"

## Beyond Trivia: The Taxonomy of Play

We mapped out game mechanic types that aren't trivia:
- **Performance** — you DO something and the group reacts (narrate, argue, act)
- **Debate/Argument** — no single right answer, the disagreement IS the fun
- **Social deduction** — someone has hidden information/role, you're reading people
- **Bluffing/Creation** — you MAKE something (fake headline, fake radio message) and others detect the fake
- **Cooperative/Asymmetric** — players have different information, must work together
- **Drafting/Strategy** — make choices under constraint, live with consequences
- **Confidence/Calibration** — not "what's the answer" but "how sure are you?"
- **Expression/Reveal** — everyone answers privately, all revealed simultaneously, disagreements are the content

The user's reaction to initial concrete mode proposals was that some were "kind of lame" — the bar for creative quality is high. The modes that landed well were ones with a clear social mechanic that F1 fans would recognize as something they already do informally.

## Accessibility Insight

A critical design insight emerged: **non-trivia modes are naturally more accessible**. If the game asks you to write a fake radio message, you don't need to know F1 history — you just need to be funny. If the game asks you to rank circuits by vibe, a newcomer's opinion is as valid as an expert's. This means the creative/performative modes solve the mixed-knowledge-group problem that pure trivia creates.

This connects to the session arc framework (the Jackbox insight): a game night should be a curated sequence — warm-up (accessible, everyone laughing) → escalation → main event (the geography anchor, where expertise matters) → palette cleanser (creative/silly, everyone contributes equally) → finale (dramatic). The host picks or the platform composes.

## The Meme Corner / Hidden Discovery

The user had a sharp product instinct: meme-adjacent modes should NOT be the front door. The geography anchor is what the product IS. The meme corner should be **discovered** — hidden, unlockable, rewarding exploration. "Have you found the paddock yet?" as word-of-mouth. This protects the serious identity while creating the virality mechanism.

The viral-with-longevity formula: meme modes get people in the door (shareable moments), the geography anchor gives them a skill to develop (you genuinely get better), the social layer gives them a reason to come back with their specific friends (inside jokes, group history), and the F1 calendar gives them a reason to come back this weekend (natural content cadence).

## Words of Wisdom: The Deep Dive

The bulk of the session was spent designing a specific game mode called "Words of Wisdom," named after a Leclerc radio moment from the 2025 Australian GP. Leclerc's seat was filling with water, his engineer Bozzi said "Must be the water," and Leclerc replied "Let's add that to the Words of Wisdom."

### The core mechanic (Fibbage-style)

The user landed on a Fibbage (Jackbox) mechanic after I initially over-designed with too many round types:
1. Host screen shows a radio exchange setup — the year, GP, who's talking to who, and the preceding message
2. Everyone writes what they think the response was (or a convincing fake)
3. All player answers + the real response are shuffled together on screen
4. Everyone votes on which they think is real
5. Points for picking the real one AND for fooling others

The user's key correction: the setup MUST show the actual preceding radio message (not a narrative description). "Leclerc: 'I have the seat full of water.' Engineer responds: ???" — not "Leclerc complained about water and his engineer replied."

### Design decisions

- Preserve COMPLETE exchanges (full back-and-forth, not cherry-picked)
- Lines must be from the SAME conversation moment (same lap, directly adjacent in transcript)
- Skip routine strategy filler unless the response is genuinely surprising
- Include the lap number for context
- Capture who says what to whom

### The replayability problem and solution

The user identified a critical issue: if it's purely a quiz on famous meme moments, you learn the answers and it's over. The Fibbage mechanic solves this because **your friends' fake answers are the content** — the same setup plays completely differently with different groups. The real radio message is just the reveal; the game is in what your friends write. This means creative/performative rounds should dominate over knowledge rounds (maybe 3:1 ratio).

### Round type variety (brainstormed but not fully designed)

The user wants Words of Wisdom to have MULTIPLE round types within it, switching between them for variety (WarioWare energy):
1. **Complete the exchange** — the Fibbage core (what we designed)
2. **One-liner identification** — iconic standalone quotes that aren't part of exchanges. Who said it? What GP? What year?
3. **Phrase-first** — the funny/dramatic line comes FIRST, guess the context that prompted it
4. Possibly Fibbage variants of each
5. Adjustable settings (round count, round type mix, difficulty)

These are NOT fully designed yet — the user explicitly wanted to continue brainstorming these.

## Content Pipeline

We built a pipeline to source Words of Wisdom content from racefans.net's team radio transcript archive:

### What was built
1. `scrape-all.py` — Python script: fetches all 18 index pages, collects all article URLs (not just "team-radio" slug — the newer editorial articles use different URL patterns), downloads HTML, strips to clean text. Files named `YYYY-MM-DD-slug.txt`.
2. `EXTRACTION-SPEC.md` — shared spec that Codex agents read before processing a transcript. Contains the rules (same conversation moment, full exchanges, speaker attribution, lap numbers, quality bar).
3. `run-extraction.sh` — bash script that runs Codex `gpt-5.4-mini` agents 2 at a time through all transcripts, waits for each pair, skips already-processed files. Resumable.

### What was learned about tooling
- **Codex agents can't do bulk scraping** — they waste tokens reading raw HTML, get rate-limited with >2 concurrent, and `nohup codex exec` doesn't work (use `nohup bash -c 'codex exec ...' &`)
- **Separate the scraping from the AI judgment** — Python for download/extraction, Codex only for identifying promising exchanges
- **`gpt-5.4-mini` is sufficient and much cheaper** than `gpt-5.4` for this extraction task. `gpt-5.4-medium` not available on user's ChatGPT account.
- Write common instructions to a shared spec file; keep per-agent prompts minimal

### Current state
- 347 transcripts downloaded spanning 2013-2026 (2017 has 79, 2024-2025 have 120 combined)
- Extraction running in background: `run-extraction.sh` processing via Codex, 2 at a time
- **Check progress**: `tail -5 extraction-run.log` and `ls v4-*.md | wc -l` in `scraped-radio/`
- The script is resumable — re-run if it crashes

## Open Brainstorm — Seeds, Not Decisions

The user ended the session firing off ideas rapidly. The framing matters: this was NOT an exhaustive list or a prioritized feature request. The user was **opening the design space** — giving permission and momentum for the next session to brainstorm freely alongside them, critique and improve ideas, add new ones, and explore territory beyond what was named. The user explicitly said "I don't even know how much and in what form this stuff is feasible" — the posture is creative exploration first, feasibility grounding second.

**The next session should treat these as conversation starters, not a checklist. Push back on weak ideas. Build on strong ones. Add ideas the user didn't think of. The user wants a creative collaborator, not a transcriptionist.**

### Sound-based games

**User's seeds:**
- Identify tracks from car engine sounds (inspired by a real F1 driver challenge video where drivers did this)
- Commentator/announcer clip identification — play audio, guess race + year, bonus for lap
- Playing with sound at various difficulty levels

**Agent's read on these:** The sound direction is genuinely novel — nobody in the F1 fan game space is doing audio-based play. The commentator clip idea is especially strong because F1 commentary has its own meme layer ("AND IT'S LIGHTS OUT AND AWAY WE GO", "IS THAT GLOCK?!", Brundle's grid walks, Crofty's screaming). The car sound identification is a harder design problem (how do you source clean audio? do modern cars sound distinct enough?) but would feel incredible if it worked. There might also be a simpler version: play a CROWD reaction clip and guess the moment — crowd sounds are highly distinctive (Monza's roar when a Ferrari leads vs. Silverstone's when Hamilton does something).

Questions worth exploring: where does audio content come from? F1TV has the archive but licensing is the constraint from the legal research. Fan-captured audio, commentary compilations on YouTube, and podcast clips might be more accessible. The technical question is also real: serving audio in a browser-first party game adds complexity the geography mode doesn't have.

### Driver/team personality games

**User's seeds:**
- Games themed around specific driver personalities (including meme-culture versions — "Talibantonelli", "Osama bin Russell")
- Lewis Hamilton fashion game (rating outfits, dressing drivers up)
- Max Verstappen game
- Games associated with the personality of different drivers and teams

**Agent's read:** The personality-as-game-theme idea is interesting but needs sharper framing. "A Max Verstappen game" isn't a game yet — what IS Max's game? Is it his bluntness? His simracing? His "just drive faster" energy? The Hamilton fashion angle is funnier and more concrete — F1 paddock arrivals are already a meme genre. A "Rate the Fit" round where you see a driver's paddock outfit and score it, then see what everyone else scored, could genuinely work as a party round. It's accessible (no F1 knowledge needed), social (everyone has an opinion), and taps into a real fan behavior (arguing about Hamilton's outfits is a whole subculture).

The meme-personality games ("Talibantonelli") are the user's humor and might work as flavor/naming within a game rather than as standalone modes. The risk is building games that are funny once but don't have a loop. The question to explore: what's the repeatable mechanic underneath the personality flavor?

### Cooperative/physical games

**User's seeds:**
- Mini pit stop cooperative game — "ridiculous and fun and stupid"
- Games around key historical events (Abu Dhabi 2021)
- Homage to old-era greats in a fun way

**Agent's read:** The pit stop coop idea has real legs. A real pit stop is a team of ~20 people doing precise coordinated actions under 2 seconds of pressure. As a party game, this could be a Overcooked-style chaos game: each player on their phone has a role (wheel gunner, jack operator, lollipop person), they have to tap/swipe in the right sequence, and the team's pit stop time is the score. It's cooperative, it's frantic, it's skill-based, and it's hilarious when it goes wrong. This is the kind of mode that would be a breakout viral hit if the execution is good — Overcooked for F1 pit stops.

The Abu Dhabi 2021 / historical events idea could be a "Relive the Moment" mode — you're dropped into a key moment with partial information and have to make calls (as a driver, team principal, or steward). What do you do? Then compare with what actually happened and argue about it. This is the debate/argument mechanic applied to specific famous incidents.

The old-era homage is the vaguest seed. Could be a "Legends" content pack for the geography mode (black-and-white photos of 1960s circuits, cars without wings, gravel traps everywhere). Could be a trivia/narrative mode about the history of the sport. Needs more shape.

### Platform composition — how games relate to each other

**User's seeds:**
- Are games offered individually or via party modes?
- One idea floated: a "Grand Prix" style party mode — curated multi-game session
- But also: what's the trajectory from small/current to mature platform? How do we get there?

**Agent's read:** This is wide-open design territory, not a settled question. The "Grand Prix" metaphor (practice → qualifying → race mapping to warm-up → competitive → main event) is one option worth exploring, but there are many other shapes:

- **Jackbox pack model** — a curated bundle of 4-5 different games, play them in sequence, the host picks the order
- **Mario Party model** — a board/map/progression layer that connects mini-games, with a meta-game running across them
- **Playlist model** — the host drags games into a queue like a music playlist, reorders on the fly, skips if the energy is wrong
- **Festival/carnival model** — games are "booths" at a virtual F1 paddock, groups wander between them, some are drop-in
- **Season model** — games unlock or rotate tied to the F1 calendar, creating a reason to come back each race weekend
- **No composition at all** — games are standalone, you pick one and play it. BoxBoxd's approach. Simplest to build, but loses the party-night energy the earlier session was excited about.

The deeper questions here aren't about which metaphor to use but about what the EXPERIENCE feels like:
- Does the host control the flow, or does the platform?
- Is there a meta-score that runs across games, or does each game stand alone?
- How long is a "session"? 20 minutes? 2 hours? Variable?
- Can you drop in/out mid-session (someone arrives late, someone leaves early)?
- How does the energy arc feel — does it build to a climax, or is it a buffet you graze?

None of these are answered. All are worth exploring.

### Audio integration for Words of Wisdom

**User's seed:** Can we use actual radio audio clips in the reveals? Research needed.

**Agent's read:** This would transform the mode. Text-based setup → players write fakes → text reveal is good. But text-based setup → players write fakes → ACTUAL AUDIO of the real radio message playing through the speakers? That's a party moment. The emotional texture of someone's voice — the cracking, the fury, the deadpan — is irreplaceable.

Sources to research: F1TV broadcasts include team radio. YouTube has thousands of radio compilation clips. The racefans.net transcripts we scraped are text-only but reference broadcasts that exist as audio. The legal question: using short radio clips in a private fan game is different from republishing them. Fair use / fair dealing arguments are stronger for short clips in a transformative context (a game, not a rebroadcast). This needs real research but the payoff if it works is enormous.

## What the Next Session Should Do

1. **Check the extraction** — is it done? How many entries total? Quick quality scan of a few files to verify the pipeline worked.
2. **Continue Words of Wisdom round type brainstorming** — the user was mid-flow on this. Multiple round types within the mode, WarioWare pacing, adjustable settings. The user specifically mentioned one-liner identification and phrase-first rounds as ideas they hadn't fleshed out.
3. **Pick up the brainstorm seeds above** — but as a creative collaborator, not a transcriptionist. Critique weak ideas, build on strong ones, propose new ones. The user wants to be surprised and challenged, not just reflected back.
4. **The platform composition question** — how do games relate to each other? Explore multiple framings (Grand Prix metaphor, Jackbox packs, Mario Party, playlists, festival/carnival, calendar-tied, standalone). The deeper questions are about experience feel: who controls the flow, is there a meta-score, how long is a session, what's the energy arc. This is wide-open territory — explore broadly before committing to a shape.
5. **Threads not yet reached**: the substrate question (what does the content model need to look like to support all this) and architectural foreclosure (does the current plan prevent us from getting here). These are the most load-bearing for Phase 01 but need the creative exploration to be further along before they're productive.

## Files

- `HANDOFF.md` — original exploration entry point, still the canonical context doc
- `SESSION.md` — session narrative log (was initialized but not updated during session)
- `words-of-wisdom-radio-catalog.md` — 50 curated radio moments from web research (Claude agents, pre-scraping)
- `scraped-radio/transcripts/` — 347 clean text transcript files (`YYYY-MM-DD-slug.txt`)
- `scraped-radio/articles/` — 347 raw HTML source files
- `scraped-radio/v4-*.md` — Codex extraction output (one per transcript, ~200+ done, possibly still running)
- `scraped-radio/EXTRACTION-SPEC.md` — shared Codex agent spec
- `scraped-radio/run-extraction.sh` — batching script
- `scraped-radio/extraction-run.log` — progress log
