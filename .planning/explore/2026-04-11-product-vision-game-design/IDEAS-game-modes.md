# Game Mode Designs

> See [IDEAS-INDEX.md](IDEAS-INDEX.md) for the global disclaimer, status key, and links to all docs.

---

## Words of Wisdom
**Status**: designed (core mechanic), developing (round type variety)
**Research**: [R2](RESEARCH-TODOS.md) (audio reveals)
**Origin**: Session 1 — user brought up meme/radio culture as game content
**User engagement signal**: user-initiated, explored — one of the most pressure-tested ideas in the current set

Core mechanic (Fibbage-style): show real radio exchange setup, everyone writes a fake response, mix with real, vote. Points for spotting real + fooling others. Replayability comes from friends' fakes, not memorizing answers.

Key design decisions:
- Setup shows ACTUAL preceding radio message, not narrative description
- Complete exchanges, same conversation moment, speaker attribution, lap numbers
- Creative/performative rounds should dominate over knowledge rounds (~3:1)

Round type variety (WarioWare pacing, switch between types):
1. **Complete the exchange** — Fibbage core (designed)
2. **One-liner identification** — iconic standalone quotes, who/where/when (seed)
3. **Phrase-first** — funny line comes first, guess the context (seed)
4. Fibbage variants of each type (seed)
5. Adjustable settings: round count, type mix, difficulty

Content pipeline: 347 racefans.net transcripts scraped, Codex extraction running (~234/347 as of session 2 start).

**Audio integration**: If we can source actual radio audio clips, the reveal transforms — text setup → players write fakes → ACTUAL AUDIO plays. Party moment. Blocked on [R2](RESEARCH-TODOS.md).

---

## The Stewards' Room
**Status**: developing
**Research**: [R1](RESEARCH-TODOS.md) (content sourcing)
**Origin**: Session 2 — structured argument as game mechanic
**User engagement signal**: not yet meaningfully pressure-tested by user

Famous controversial incident presented with partial information (as stewards would see it). Each player renders a verdict — penalty type, severity. Reveal everyone's decisions, then reveal actual steward decision. Points for matching real decision, but social layer is the real game — who's the harshest steward in your group?

Strengths:
- Taps into something F1 fans already do (argue about decisions)
- Real answer exists but is often "wrong" — so matching isn't automatically winning
- The argument AFTER the reveal is the actual game
- Decades of controversial incidents = deep content well
- Text-describable, no audio/video dependency

Open questions:
- Content sourcing — how structured is steward decision data? → [R1](RESEARCH-TODOS.md)
- How much context is enough for a good round? Too little = random guessing, too much = obvious
- Does this work for mixed-knowledge groups? (Maybe: the incident description levels the field, but deep fans have more context for edge cases)

---

## Team Principal's Desk
**Status**: seed → developing
**Research**: [R7](RESEARCH-TODOS.md) (strategy data sourcing)
**Origin**: Session 2 — extension of Stewards' Room into strategy space
**User engagement signal**: not yet meaningfully pressure-tested by user

Race situation presented mid-race (position, tire age, gap data, safety car status). Each player decides: pit or stay out? Reveal simultaneously, then see what the team actually did and how it played out. Points for the strategy that would have gained the most positions.

Strengths:
- Fantasy sports logic applied to individual race moments
- Rewards F1 understanding but also gut instinct
- Different from trivia — it's a judgment call, not a fact recall

Open questions:
- Needs real data (tire ages, gaps, weather, pit windows) to feel authentic → [R7](RESEARCH-TODOS.md)
- Is this too niche? Strategy nerds love it, but does it work at a party?
- Could simplify: binary choice (pit/stay) with confidence bet, rather than full strategy design

---

## Pit Stop Co-op
**Status**: seed
**Research**: [R6](RESEARCH-TODOS.md) (real-time browser mechanics)
**Origin**: Session 1 user burst — "ridiculous and fun and stupid"
**User engagement signal**: assistant-proposed, user-positive — liked by the user but not yet deeply explored together

Overcooked-style chaos: each player has a pit crew role on their phone (wheel gunner, jack operator, lollipop person). Tap/swipe in the right sequence, team pit stop time is the score. Cooperative, frantic, skill-based, hilarious when it goes wrong.

Strengths:
- Genuinely original — nothing like this exists in F1 fan games
- Cooperative (most other modes are competitive/individual)
- Accessible — no F1 knowledge needed, pure coordination skill
- Viral potential — watching pit stops go wrong is inherently funny
- Could work as palette cleanser in a party night arc

Open questions:
- Real-time synchronization across devices → [R6](RESEARCH-TODOS.md) — likely M2+ complexity
- How many roles are fun vs. overwhelming?
- Does it have replay depth or is it "fun three times"?

---

## The Verstappen Game (working title)
**Status**: developing — multiple variants brainstormed, not narrowed to one
**Research**: [R6](RESEARCH-TODOS.md) (real-time browser mechanics), [R10](RESEARCH-TODOS.md) (browser 3D/Three.js feasibility), [R11](RESEARCH-TODOS.md) (phone-as-steering-wheel)
**Origin**: Session 2 — user pitched "Max as unkillable predator," evolved through several iterations
**User engagement signal**: user-initiated, explored — heavily worked through as a comic-but-replayable mode family

**Core concept**: Max Verstappen as an unstoppable threat on a GP circuit. Players try to survive/finish while Max divebombs. PS1-era 3D graphics. The "tutututu Max Verstappen" meme song plays with proximity-based volume (louder = closer) or triggers on line-of-sight. Comedy from juxtaposition of horror game tension with goofy F1 meme.

**The tutututu audio mechanic** (constant across all variants):
- Proximity-based volume: closer to Max = louder
- Possibly directional (spatial audio via Web Audio API)
- Could trigger on line-of-sight instead of / in addition to proximity
- The audio IS the threat indicator — the Jaws principle
- Escalation: tempo increases as game progresses or as Max gets closer

**Variant A: Running on foot, Max in car**
Players are tiny people sprinting around a GP circuit trying to complete a lap. Max is in his Red Bull driving the racing line at race speed. He's not hunting — he's just driving. You're the one who shouldn't be there. If he hits you, DNF.
- *The comedy*: scale difference between a person and an F1 car
- *Circuit geometry as game design*: straights = dangerous (fast, exposed), chicanes = opportunities (Max slows), corners = blind (can't see him coming), pit lane = safe detour (no Max but adds distance), run-off areas = duck off track when he approaches
- *Goal*: complete a lap. First to finish wins.
- *Multiplayer dynamics*: stick together (Max can only hit one) or spread out (don't be near someone who gets divebombed)?

Architectural requirements:
- Three.js 3D rendering with PS1 shaders (vertex jitter, affine textures, fog, color depth reduction)
- PS1 fog: built-in Three.js `scene.fog` for basic, vertex shader for chunky PS1 look — lightweight
- Low-poly 3D circuit model (one per circuit, simple geometry: flat track, box barriers, blocky grandstands)
- Low-poly character models (player characters on foot)
- Low-poly car model (Max's Red Bull)
- Player movement: walking/running speed, virtual joystick on phone
- Max AI: follows racing line, laps circuit at fixed high speed
- Collision detection: car vs. characters
- Phone screen: third-person behind character, limited visibility (fog)
- Host screen: wide/overhead camera showing full circuit — spectators see everything players can't
- WebSocket for real-time multiplayer
- Web Audio API for positional tutututu
- Latency: walking speed is forgiving, phone-as-controller should be fine (~5-20ms on local network)

**Variant B: Everyone in cars, Max as periodic divebomber**
Players are all racing in slow cars, fog, PS1 graphics. Normal-ish racing. Periodically Max blitzes through the pack at max speed, divebombing the lead driver, continuing off. If you get hit off track, DNF. Creates tension about being in the lead — leading is dangerous.
- *The comedy*: slow foggy race punctuated by Max tearing through at 10x your speed
- *Strategic layer*: do you WANT to be in first? Leading makes you the target. Hanging back is safer but you need to finish well.
- *Max behavior*: off-screen between attacks, periodic appearances, targets the racing line / lead positions

Architectural requirements:
- Everything from Variant A, PLUS:
- Car physics/handling — even simplified arcade handling (steering, acceleration, braking) needs to feel decent. This is the BIG additional complexity.
- Player input on phone: tilt to steer? virtual wheel? Swipe? Needs tuning for feel.
- Collision: car vs. car (player vs. Max), car vs. barriers, possibly car vs. car (players)
- Split screen on host: could show broadcast-style camera angles, or each player's view, or overhead
- **Latency sensitivity**: car racing at speed is MORE sensitive to input lag than walking. Phone-as-controller might need client-side prediction (phone predicts movement locally, server corrects). This is solvable but adds complexity.
- This is the hardest variant technically. Car feel is notoriously difficult to get right even in simple arcade racers.

**Variant C: Running on foot, Max on foot (horror)**
Back to simpler. Low-poly character model of Max slowly approaching you. Not in a car — walking, Slenderman-style. You're on foot too. The pace is slower, the tension is about Max gradually closing in. More pure horror, less racing.
- *The comedy*: low-poly PS1 Verstappen model slowly walking toward you is inherently unsettling and funny
- *Doesn't require car physics at all*
- *Environment could be simpler*: doesn't need to be a full circuit — could be a paddock, pit lane complex, or tunnel section
- *Could combine with item collection*: collect car parts to build your car and escape, collect DRS tokens, etc.

Architectural requirements:
- Three.js with PS1 shaders
- Low-poly environment model (could be smaller/simpler than full circuit)
- Low-poly character models (players + Max)
- Player movement: walking/running, virtual joystick
- Max AI: pathfinding toward players, possibly teleporting (Slenderman-style)
- Flashlight mechanic (optional): limited visibility cone, flashlight battery
- Simpler collision detection (character vs. character)
- Latency: very forgiving at walking speed
- Easiest 3D variant to build

**Cross-cutting architectural requirements (ALL variants):**
- WebGL via Three.js (or Babylon.js) for 3D rendering in browser
- PS1 shader pack: vertex snapping, affine texture mapping, fog, color banding — documented, ready-made shaders exist for Three.js
- WebSocket server for real-time game state sync
- Web Audio API for positional/proximity tutututu
- Phone-as-controller: touch input on phone → WebSocket → game server → host screen render
- Host screen: different camera view of same game state (omniscient view for spectators)
- At least one 3D circuit/environment model (low-poly)
- Character/vehicle models (low-poly PS1 style)

**The elimination problem:**
First person hit has the worst experience if they just watch. Solutions:
- **Ghost mode**: eliminated players can still move, place obstacles, warn/haunt survivors
- **Spectator powers** (strongest option): eliminated players get host-screen controls — vote on Max's direction, trigger rain, deploy safety car, mess with survivors. Elimination makes you MORE powerful, not less. Twitch Plays energy.
- **Infection**: hit by Max = become a Max. No one ever just watches. (Already in variant list above.)

**Round duration and circuit scale:**
Real circuits on foot would take forever. Options:
- Scaled-down toy versions of real circuit layouts
- Absurdly fast running speed (funny in itself — tiny PS1 people sprinting cartoonishly)
- Goal isn't a full lap (reach a specific point, survive for 90 seconds, etc.)
- This is a fundamental parameter: 90-second rounds with spectator powers = party game. 5-minute rounds with passive elimination = bad product.

**Scoring beyond survive/die:**
- Points for distance covered (even if eliminated)
- Near-miss bonus (Max passes close, you survive — rewarding risky play)
- Time survived
- Personal best lap time per circuit (persistent leaderboard)
- Style points for deliberately risky behavior (running ON the racing line)

**Vehicle ladder / unlock progression:**
- Same core mode could play very differently across unlockable vehicle classes: barefoot, e-scooters, golf carts, sedans, supercars, F1 cars
- This creates a natural replay ladder: the same circuit/encounter recontextualized by movement speed, turning radius, fragility, visibility, and comedy
- Unlock rhythm could work more like *Ultimate Chicken Horse* than a grind-heavy live-service system: new vehicles, modifiers, challenge modes, and possibly levels/circuits unlock as you keep playing with the group
- Challenge variants could radically change the same map: "barefoot Monaco survival," "golf cart Monza," "supercar fog mode," "F1 car hard mode where everyone is fast enough to overcommit"
- Important design question: are these unlocks just rewards, or are they the real source of long-term replayability?

**F1 power-ups / items:**
- **DRS**: speed boost on specific straights
- **Safety car**: slows Max temporarily
- **VSC**: everything slows, breathing room
- **Red flag**: full pause, position reset
- **Blue flag**: Max redirected away briefly
- **Pit stop**: temporary invulnerability in pit box, costs time
- **Rain/wet tires**: wet patches appear, Max aquaplanes
- All map naturally from real F1 concepts — fans already know what they do

**Alternative predators (variant/content expansion):**
Each predator has different AI behavior + their own audio signature:
- **Schumacher**: calculated, optimal lines, never mistakes, relentless
- **Senna**: rain specialist, appears in wet-weather variants
- **Maldonado**: erratic, unpredictable pathing — scarier because you can't predict
- **Montoya**: rage mode, specifically targets nearest player

**Replay/highlights:**
Each divebomb should trigger a kill-cam style instant replay — slow-motion, dramatic angle. Highlight reel at end of round showing best near-misses and eliminations. These are the viral/shareable moments.

**Phone considerations:**
- Portrait vs. landscape: 3D movement more natural in landscape, but people default to portrait. Support both or force landscape?
- Performance floor: PS1 graphics are light but phone browsers vary in WebGL capability

**Solo mode:**
Single player vs. Max. "Complete a lap of Monaco while Max hunts you." Personal records, circuit leaderboards. Gives the game life outside party nights. Daily challenge variant: "Today's Verstappen challenge: Suzuka."

**Open questions:**
- Part of the platform (hidden discovery architecture — the "secret game") — confirmed as platform mode, not standalone
- Which variant to prototype first? C is simplest, A is the cleanest concept, B is hardest but most game
- Can the same Three.js foundation serve multiple variants? (Probably yes — shared renderer, different game logic)
- How many circuit models are needed for launch vs. how many can come later?
- Does the PS1 3D tech stack coexist with the 2D party game tech stack, or is this a separate app/module?
- Phone-as-controller latency for Variant B specifically — needs a spike/prototype to validate
- 3D model creation pipeline: who makes the low-poly circuits and characters? Is there a procedural/algorithmic approach using real circuit data?
- Could Variant A or C work in 2D top-down as a simpler fallback if 3D proves too costly?
- How much of the replayability should come from unlockable vehicle classes, challenge modes, and circuit unlocks versus pure one-round chaos?
- Potential shared racing engine with Talibantonelli / Bin Russell game (see below) — open possibility, likely makes sense, exact sharing TBD based on how different the games want to be

---

## Talibantonelli / Osama bin Russell (Demolition Derby + Social Deduction)
**Status**: developing — multiple modes brainstormed
**Research**: overlaps with Verstappen game [R10](RESEARCH-TODOS.md) (browser 3D); shared racing engine is an open possibility
**Origin**: Session 2 — user pitched based on real F1 meme (Antonelli and Russell both known for crashing into others in their early careers)
**User engagement signal**: user-initiated, explored — discussed enough to generate multiple submodes and replay hooks

**Core concept**: Multiplayer racing where some players are secretly (or openly) designated as hunters whose goal is to crash other players off the track. Everyone else is trying to finish the race. Demolition derby meets social deduction. Each hunter identity has their own associated meme theme song.

**Game modes within this game:**

**Mode 1: Known Hunters**
Everyone knows who the hunters are. Open pursuit. Hunted players try to finish while dodging. Hunters try to crash everyone out. Simple, chaotic, immediate.
- Hunted can cooperate — draft together, block hunters, sacrifice one person so others escape
- Hunter theme songs play when they're closing in
- Simplest mode, good starting point

**Mode 2: Hidden Hunters (Among Us Racing)**
Everyone's racing. 1-2 players are secretly hunters. Goal: crash others but make it look accidental. "Was that a racing incident or was George trying to kill me?"
- After each crash-out: brief vote phase (10 seconds, keep pace up). Who's the hunter? Correct accusation = hunter revealed/penalized. Wrong = accuser loses time.
- **The jank is a feature**: in a game where everyone's struggling with phone controls, every crash is plausibly accidental. Provides natural cover for hunters. If driving was perfect, any crash would be obviously intentional.
- Genuinely novel — "Among Us but racing" doesn't seem to exist
- Social deduction through DRIVING BEHAVIOR, not discussion — a different read skill than verbal Among Us

**Mode 3: Hot Potato / Rotating Roles**
Everyone starts normal. Randomly, one player gets the hunter power-up — car glows, theme song plays, 15 seconds to crash everyone. Then it passes to someone else. You never know when YOU'LL become the hunter.
- Scoring: most crash-outs as hunter + most survival time as hunted
- Constant tension — the power could hit you any moment
- Quick, chaotic, good for short rounds

**Mode 4: Escalation**
Starts as a normal race. Each lap, more players get converted to hunters. By the final lap: one survivor vs. everyone else.
- Natural dramatic arc — early laps feel safe, late laps feel desperate
- The moment you get converted and turn on your friends is a betrayal moment
- Theme songs layer as more hunters appear (like infection tutututu choir)

**Mode 5: Free-for-all (Maldonado Mode)**
No hunters/hunted. Everyone is trying to crash everyone. Last car running wins. Pure demolition derby. Simple, stupid, fun.

**Hunter character profiles:**
Each hunter isn't just a skin — they have distinct driving behavior (whether AI-controlled or as player abilities):

| Hunter | Meme origin | Driving behavior | What makes them distinct |
|--------|------------|-----------------|------------------------|
| Talibantonelli | Antonelli's crash-heavy first year | Erratic, unpredictable, crashes come from nowhere | You can't anticipate where the hit comes from |
| Osama bin Russell | Russell's early crash incidents | Calculated, targets specific players, methodical | He picks a victim and hunts them specifically |
| The Torpedo | Vettel named Kvyat this on live radio | Divebombs specifically at braking zones | Straights are safe, corners are lethal |
| Pastor Crashnado | Maldonado, the OG crash meme | Pure random chaos, might crash into barriers too | Unpredictable — might miss you entirely, might take out three people |
| Magnussen | "Suck my balls" dirty defender | Doesn't crash head-on, squeezes you into walls, blocks escape routes | Sustained pressure, not sudden impact |
| Al Mer-Qaedes | Mercedes team mashup | Team-based variant? Two hunters working together | Coordinated attacks, pincer movements |

Each hunter has their own associated theme song / audio signature. Different hunters create different gameplay: "Let's do a Torpedo round" vs. "Crashnado mode" feel fundamentally different even on the same circuit.

**Shared elements across modes:**
- Crash/collision mechanics: bumping cars off track, spinning, barrier impacts
- Kill-cam replays for dramatic crashes (shared concept with Verstappen game)
- Theme songs per hunter identity with proximity-based audio
- Circuit environments (same tracks available across modes)
- Respawn mechanics for modes that need them (Mode 3, Mode 5)
- Post-round highlight reel of best crashes

**Vehicle ladder / unlock progression:**
- This mode is especially compatible with unlockable vehicle classes because the same hunter/hunted logic can become funnier and more strategic when the vehicles change
- Possible ladder: barefoot running, e-scooters, golf carts, beat-up sedans, supercars, F1 cars
- Different vehicle classes create different reads of the same mode: hidden hunters on scooters is slapstick; F1-car hunter rounds are high-speed terror; sedans make bumping and blocking feel heavier
- Unlockables do not need to be only vehicles: challenge mutators, hunter powers, circuits, and special mode variants could also unlock over time
- This creates a return loop beyond "play another round" and gives the mode a discovery cadence rather than exhausting its joke immediately

**Architectural requirements:**
- Car-to-car collision physics (the Verstappen game only needs car-to-player or car-to-AI)
- Role assignment system (random hunter selection, secret vs. revealed)
- Voting/accusation UI for Mode 2 (brief, doesn't interrupt racing flow)
- Power-up/role-switch system for Mode 3
- Respawn mechanics
- Otherwise overlaps heavily with Verstappen game requirements: car movement, circuit environments, real-time multiplayer, PS1 3D, phone-as-controller, audio

**Relationship to Verstappen game:**
Likely shares a racing engine — both need cars on circuits with collisions. The key difference: Verstappen is players-vs-AI-predator (horror/survival), this is players-vs-players (competitive/social/chaotic). How much engine sharing happens depends on how different the driving feel should be between the two. Open question for later.

**Early architectural decisions that would foreclose variations if gotten wrong:**

1. **Parameterized vehicle model**: if every car handles identically, you can never add asymmetric hunter abilities or per-character driving feel. The car physics needs adjustable parameters from day one: speed, weight, grip, acceleration, turning radius, durability. Even if v1 makes everyone the same, the parameters must exist.

2. **Collision angle and force detection**: simple "bounce off" forecloses scoring T-bones vs. sideswipes, Magnussen's sustained-squeeze mechanic, and impact-force-based crash severity. The collision system should capture: angle of impact, relative speed, force vector, duration of contact. Even if v1 treats all collisions the same, RECORD the data.

3. **Structured game event log**: every crash, near-miss, elimination, role-switch, accusation, vote as a timestamped event with metadata. Required for: replay system, highlight reels, cross-game statistics, shareable moments, analytics. If events are just physics side-effects rather than first-class logged objects, all of the above requires retrofitting.

4. **Generic role/identity system**: hunter role can't be a boolean. Future needs: multiple role types, secret vs. revealed, role switching mid-game, partial information, teams of roles. Schema: `{type, visibility (public/secret/partial), assignment_method (random/voted/conditional), switch_trigger (timer/event/manual)}`.

5. **Spectator interaction channel**: passive-viewer assumption forecloses eliminated-player powers, voting, audience participation. Having an empty "spectator actions" channel from day one = cheap insurance.

6. **Track interaction layer**: static-geometry-only tracks foreclose closeable doors, deployable barriers, triggerable hazards, weather patches, persistent crash debris. A simple "interactive objects" layer in track data format keeps all of this open.

7. **Audio event system**: hardcoded sounds foreclose per-hunter themes, proximity audio, dynamic layering (more hunters = more audio layers), impact-force-based crash sounds. Need generic "audio events tied to game state" — shared requirement with Verstappen game's tutututu.

8. **Item/projectile system**: if the physics engine only supports cars, you can never add Mario Kart-style items (oil slicks, dropped front wings as debris, DRS boost pickups, brake-failure infliction). The engine should support "objects that aren't cars that affect cars" even if v1 is ramming-only.

**Open questions:**
- How to make crashing feel satisfying and funny, not frustrating? Sound design, screen shake, slow-mo, kill-cam — the crash needs to feel like a MOMENT
- Balance: how fast/maneuverable are hunters vs. hunted? Same speed? Hunters slightly faster? Hunted more agile? Per-hunter-character balance?
- Player count sweet spot: 4 players? 8? Social deduction mode needs enough players that 1-2 hunters aren't obvious
- Can eliminated players spectate with powers (same question as Verstappen game)?
- How does this integrate with driver select? If you picked Russell, are you more likely to be the hunter? Or is it always random?
- Map design: do circuits need specific "ambush spots" or "escape routes" designed in, or does natural circuit geometry suffice?
- Can hunter characters be unlocked over time? Start with one or two, discover more? Ties into hidden discovery architecture.
- Should vehicles/circuits/challenge modes unlock in an *Ultimate Chicken Horse*-style drip so groups keep discovering new combinations over time?

---

## Sound-based Games
**Status**: seed (multiple sub-ideas)
**Research**: [R2](RESEARCH-TODOS.md) (audio sourcing/legal), [R4](RESEARCH-TODOS.md) (car sound distinctiveness)
**Origin**: Session 1 user burst — inspired by real F1 driver challenge video
**User engagement signal**: user-initiated, lightly explored — especially around race-start / track-audio guessing as a promising direction

Sub-ideas:
- **Engine identification** — play car sound, identify era/car/circuit. Blocked on [R4](RESEARCH-TODOS.md) (do modern cars even sound different enough?)
- **Commentator clip ID** — play commentary audio, guess race + year, bonus for lap. Strong because F1 commentary has its own meme layer ("IS THAT GLOCK?!")
- **Crowd reaction ID** — play crowd sound, guess the moment. Monza roar vs. Silverstone vs. Suzuka. Simpler variant that might be more feasible.

Session 2 assessment: genuinely novel territory (nobody doing audio in F1 fan games), but infrastructure bet. Audio sourcing, browser playback, legal position all need answering. Probably sequenced after text-content modes.

Note on engine sound licensing: car engine sounds recorded at races are sounds in public spaces — not a licensing concern. The legal question is specifically about FOM's broadcast production (commentary, produced team radio feeds). Fan-recorded trackside audio is freely shareable. See [R2](RESEARCH-TODOS.md) for details.

---

## Paddock Fashion — The Mode
**Status**: developing (rich design space, multiple round types emerging)
**Research**: [R5](RESEARCH-TODOS.md) (image sourcing for real outfit photos)
**Origin**: Session 1 burst (Hamilton fashion), Session 2 expanded into full mode
**User engagement signal**: user-initiated, explored — began from the Hamilton/fashion direction and grew into a broader mode family

A fashion/drawing/creativity mode built around F1 paddock culture. Multiple round types, all sharing the fashion show catwalk as the reveal mechanic (silly slideshow, figures hopping/sliding across screen).

**Creation tiers** (not exclusive — different round types use different tiers):
1. **Draw** (zero assets, ships immediately) — finger drawing on phone touchscreen. Awfulness IS the comedy. Drawful-proven.
2. **Draw-over** (low cost) — draw ON TOP of a cutout of a driver in their racing suit. Contrast between professional photo base and crude scrawls is inherently funny. More accessible than blank canvas.
3. **Photo cutout mix-and-match** (medium cost) — real outfit pieces cropped from photos, layered on a base. Janky ransom-note aesthetic fits the tone.
4. **Illustrated sprites** (highest investment) — polished house-style assets. The premium version. Ships when platform justifies art pipeline.

**Round types brainstormed:**

*Theme-based creation:*
- **Dress for the Theme** (Drawful core) — secret F1-flavored theme ("FIA hearing — you're in trouble", "sneaking into Ferrari motorhome"), create outfit, others guess which theme is which. Points for communicating theme + guessing others.
- **Same Theme Showdown** — everyone gets the SAME theme + driver. Divergence in interpretation IS the content. Multiple voting categories: "Most Realistic," "Most Creative," "Most Cursed." Different people win different categories.
- **Driver-specific challenge** — theme is a real event ("Draw what Hamilton wore to the 2021 Met Gala"). Draw from memory or imagination. Real photo drops after. Dual scoring: popular vote (creativity/humor) AND accuracy (closeness to reality). Can win either track independently.

*Reference-based:*
- **Reference Recreation** — real paddock arrival photo shown for 10 seconds, disappears, 60 seconds to recreate from memory. Before/after comparison is the content.

*Social/performance dynamics (layer on any round type):*
- **Runway Commentary** — as each creation walks the catwalk, everyone simultaneously types a one-liner on their phone. Comments appear under outfit. Vote on best. Makes the fashion show interactive, not just a reveal. Like MST3K for fashion.
- **The Pitch** — your creation shown on host screen, you verbally sell it with a straight face. "Note the asymmetric hemline — it represents the chaos of turn 1." Vote on best pitch. Performance-based, rewards being funny. Best for local play.
- **Worst Dressed Awards** — invert the vote, celebrate the disaster. Winner gives acceptance speech.
- **Who Drew It?** — anonymous creations, guess who made which. Meta-game that improves over multiple game nights as you learn friends' styles.

*Chain/collaborative:*
- **Fashion Telephone** (Gartic Phone mechanic) — A draws outfit for theme, B sees it 10 seconds then redraws from memory, C sees B's version... reveal full chain. Degradation is the comedy. Proven mechanic.
- **The Makeover** — cooperative/asymmetric: "client" describes what they want verbally, artist draws based on description alone. Client rates closeness to vision. Communication gap is the mechanic.

*Judgment-only (no creation):*
- **Rate the Real Fit** — actual paddock arrival photo, everyone rates 1-10, reveal spread. 30 seconds per photo. Quick palette cleanser.
- **Spot the Real Fit** — mix player creations with illustrated version of a real outfit (works best with sprite tier). Guess which is real.
- **The Auction** — all creations shown, everyone gets fake money, bid on outfits. Creator's score = total bid value of their work. (Weakest dynamic — complexity without proportional fun. Parked.)

**Key properties:**
- Fully accessible — zero F1 knowledge needed for most round types
- "Your friends are the content" — every game is unique
- Scales from zero-asset (drawing) to premium (sprites) over time
- Fashion show catwalk is a natural shareable/viral moment
- Works both local multiplayer and online synchronous
- The Draw tier can ship in M1 with no art pipeline dependency

**F1-flavored theme examples:** "Monaco yacht party," "wet Silverstone but make it fashion," "post-championship Vegas celebration," "grid walk interview with Brundle," "you just got a 10-second penalty and you're furious," "undercover at a rival team's factory tour," "Kimi's retirement party (he doesn't want to be there)"

---

## Meme Prompts (Quiplash-style)
**Status**: seed
**Research**: none blocking — player-generated content, no sourcing needed
**Origin**: Session 2 — emerged from discussion of Talibantonelli/Russell memes and F1 meme culture
**User engagement signal**: not yet meaningfully pressure-tested by user

**Core concept**: Quiplash-style prompt-response game with F1-flavored prompts. Everyone gets the same prompt, writes their funniest answer on their phone, answers revealed on host screen, group votes on funniest. The platform provides the prompts; the players provide the content.

**Example prompts:**
- "Antonelli's rapper name"
- "George Russell's secret double life"
- "What does Horner's search history look like"
- "Stroll's Tinder bio"
- "What's actually in Hamilton's briefcase on race day"
- "The first line of Verstappen's autobiography"
- "What Kimi said when they told him he had to do the FIA gala"

**Variations:**
- **Head-to-head**: two answers shown at a time, group picks the funnier one (classic Quiplash format)
- **Free-for-all**: all answers shown at once, vote on best
- **Themed rounds**: all prompts in a round are about one driver, one team, or one incident
- **Custom prompts**: host or players write their own prompts for the group (inside jokes, group-specific humor)
- **Wanted Posters**: given a driver, draw their mugshot AND write their crime/alias/last known location. Combines drawing from Fashion mode with writing from Quiplash.
- **Cursed Wikipedia**: write a fake one-paragraph Wikipedia intro for a driver in an alternate universe. Read aloud or display on host screen.
- **Meme Court**: controversial take presented, one player defends, one prosecutes, group votes. Structured debate.

**Key properties:**
- Zero content sourcing needed — players ARE the content
- Fully accessible — no F1 knowledge needed to be funny (though F1 knowledge adds layers)
- The prompts steer the humor anywhere from PG to unhinged depending on how they're written — the platform doesn't ship edgy content, players bring their own comfort level
- Proven mechanic (Quiplash is one of Jackbox's most successful games)
- Custom prompts let friend groups personalize

**Product positioning:**
This is part of the **deepest layer of the hidden discovery architecture**. The geography anchor is the front door. This lives behind the last curtain — the thing you find after you've been on the platform a while.

---

## The Grid Walk
**Status**: seed
**Research**: [R6](RESEARCH-TODOS.md) (real-time cooperative mechanics)
**Origin**: Session 2 — cooperative information asymmetry
**User engagement signal**: not yet meaningfully pressure-tested by user

Each player gets a DIFFERENT piece of information about a race (qualifying results, weather, tire data, a key radio message). Nobody sees the full picture. Together reconstruct or predict what happened. Cooperative, rewards communication.

Structurally different from everything else — closer to Mysterium/Hanabi than Fibbage/trivia. "You each have a piece and have to talk."

Open questions:
- Is this too cerebral for a party? Or does the forced communication create energy?
- How do you design the information splits so they're meaningful?
- Technically similar to pit stop co-op — real-time cooperative sync → [R6](RESEARCH-TODOS.md)

---

## Relive the Moment
**Status**: merged into Stewards' Room / TP's Desk as a content dimension
**Research**: [R1](RESEARCH-TODOS.md) (incident sourcing, overlaps with Stewards' Room)
**Origin**: Session 1 user burst (Abu Dhabi 2021, historical events)
**User engagement signal**: user-initiated, lightly explored — the framing mattered, but it has already been partially absorbed into other modes

Dropped into a key moment with partial information. Make calls as driver/TP/steward. Compare with what actually happened. Argue about it.

Session 2 assessment: the "relive" framing is a content lens (curated famous moments), the mechanics are verdict/strategy/debate. Better as a CONTENT PACK that feeds into Stewards' Room and TP's Desk modes, not a separate mode.
