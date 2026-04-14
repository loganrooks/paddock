# Platform Experience & Social

> See [IDEAS-INDEX.md](IDEAS-INDEX.md) for the global disclaimer, status key, and links to all docs.

---

## Circuit Party Pack (standalone, evergreen)
**Status**: developing
**Research**: none blocking — content comes from other modes' content pipelines
**Origin**: Session 2 — split from Race Weekend Mode

The circuit IS the pack. Every circuit is a natural bundle of content across every mode: geography rounds for that track, WoW from races there, Stewards' Room incidents from its history, strategy dilemmas, maybe audio/visual rounds if available. "Let's play the Monaco pack" works any time, any season.

This elegantly answers the platform composition question — you don't need an abstract bundle structure. The organizing principle is the circuit itself. ~30+ circuits in F1 history = 30+ packs, each containing rounds from every available mode.

Strengths:
- Natural, intuitive organizing principle that F1 fans already think in terms of
- Every new mode automatically has content organized by circuit
- Works as the "party night" unit — "pick a circuit, play the pack"
- Host can still customize (skip modes, adjust difficulty, pick era)
- Natural completionism hook: "You've played 14 of 24 current circuits"

---

## Calendar / Live Layer
**Status**: developing
**Research**: [R3](RESEARCH-TODOS.md) (live curation pipeline)
**Origin**: Session 2 — split from Race Weekend Mode

Sits ON TOP of circuit packs. During race weekends, that circuit's pack is featured + bonus fresh content referencing this year's storylines. Post-race: reactive rounds drop (the controversial call, the dramatic radio, the strategy gamble).

Off-season rhythm: year-in-review rounds, all-time debates, silly prediction games for next season, historical deep dives. Fills the content hunger gap when the subreddit is posting "which driver wins a hot dog eating contest."

Key insight: ~24 race weekends/year = editorial calendar, not content treadmill. Off-season content is less time-pressured (historical, retrospective, predictive).

Reactive post-race content is the strongest retention signal — something happened Sunday, by Monday there's a game about it. But requires fast-turnaround curation → [R3](RESEARCH-TODOS.md). AI-assisted drafts + human review could be the moat vs. BoxBoxd's auto-generated dailies.

**The calendar layer is the retention loop. The circuit packs are the evergreen foundation.**

---

## How Games Relate to Each Other
**Status**: wide open — multiple metaphors, no decision

Candidates:
- **Grand Prix metaphor** — practice → qualifying → race maps to warm-up → competitive → main event
- **Jackbox pack model** — curated bundle, host picks order
- **Mario Party model** — board/progression layer connecting mini-games, meta-game running across
- **Playlist model** — host drags games into queue, reorders, skips on the fly
- **Festival/carnival model** — games are "booths" at virtual paddock, groups wander
- **Season model** — games unlock/rotate tied to F1 calendar
- **Standalone** — no composition, pick one game. BoxBoxd's approach. Simplest but loses party energy.

Deeper questions (all unanswered):
- Does the host control the flow, or does the platform?
- Is there a meta-score across games?
- How long is a session? 20 min? 2 hours? Variable?
- Can you drop in/out mid-session?
- How does the energy arc feel — climax or buffet?

**Research**: [R8](RESEARCH-TODOS.md) (party game composition patterns)

---

## Four Engagement Layers
**Status**: developing — far-future feature but architecturally load-bearing for M1 decisions
**Origin**: Session 2 — emerged from team/competition brainstorming

The platform has four distinct engagement layers. Players opt into whichever they want. The SAME game modes serve all layers — the difference is where scores go, what social context surrounds the play, and who you're matched with.

**Layer 1: Free Play**
Pick a game, play it, casual. Solo or with random opponents. Browse content, try things out. Includes async leaderboards (daily/weekly high scores per mode). Low-commitment entry point. No account needed to start, but scores only persist if you have one.

**Layer 2: Friends / Party (M1 core)**
Local multiplayer, game night, private groups. Online sync with friends. Scores live within your friend group. Inside jokes, group history, group leaderboards. The couch experience. This is what M1 builds.

**Layer 3: Ranked (individual competitive)**
Online sync and async multiplayer with matchmaking by skill tier. Your rank goes up and down based on performance. The LoL-style competitive ladder, but in F1 feeder series language:
- **F4** (entry) — where new ranked players start. Could have sub-tiers (F4 Div 3 → Div 2 → Div 1, mirroring real regional championships)
- **F3** — intermediate
- **F2** — advanced. Eligible for team recruitment into the career mode.
- **F1** — elite
- Underneath: Elo/MMR rating system that determines matchmaking. Visible rank is the tier, hidden rating is the matchmaking engine.
- Matchmaking makes online sync viable — no new player getting demolished by a 500-hour veteran.

**Layer 4: Career / Teams (team competitive, season-long)**
Team-based competitive. Season-long constructors' championship. Structured like a racing game's career mode but multiplayer, online sync and async. Requires minimum rank (F2+) to affiliate with a team.

**How Ranked and Career relate:**
Ranked is the individual proving ground. Career is the team competition. You prove yourself individually in ranked (F4 → F3 → F2), then you're eligible for team recruitment — just like a real junior driver earning an F2/F1 seat through results. Your ranked tier determines which team tier you can join. Your individual ranked performance AND your team contributions both matter.

**Career mode structure:**
- **Feeder series progression**: the ranked tiers (F4 → F3 → F2 → F1) double as team eligibility gates. F2+ players can join teams. F1-tier teams compete in the constructors' championship.
- **Team scoring across modes**: geography → knowledge points, WoW → cultural fluency, fashion → creative, racing → action/skill. Teams develop reputations by category.
- **Race weekend events**: each real F1 weekend has platform-wide competition. Thursday pack drops, scores accumulate, post-race reactive content scores higher (time-limited). Monday: standings update. "After Round 14, Ferrari leads by 47 points."
- **Season structure**: synced to real F1 calendar. Full constructors' championship across ~24 race weekends. End-of-season results, promotion/relegation, silly season recruitment.
- **Draft / team assignment**: balancing mechanisms needed — points-per-member averaging, loyalty lock (no mid-season switching), draft system where F1 teams recruit from F2 tier, promotion/relegation of players between teams.

**Possible transition from M1 (needs proper deliberation — sketches only, not decided):**
Several possible paths, each with different tradeoffs. The actual transition depends on user base size, technical architecture, and priorities that need proper analysis outside a brainstorming session.

- *Option A — Gradual layer addition*: M1 is private groups only → M2 adds public async leaderboards (free play layer) and friend-group-vs-friend-group race weekend competitions (proto-ranked) → M3 adds full ranked tiers, matchmaking, and team/career system. Each layer builds on the previous. Lower risk but slower to reach the competitive vision.
- *Option B — Ranked early, teams late*: M1 is private → M2 adds individual ranked play with tier progression (F4 → F3 etc.) as soon as there's an online multiplayer mode. Teams/career mode comes much later when user base justifies it. Gets competitive play out early but defers the team social dynamics.
- *Option C — Event-driven bridge*: M1 has no public competition. But race weekend events (platform-wide, open to anyone) launch as soon as there's enough content. These are standalone per-weekend competitions with no season accumulation — low commitment, easy to participate. Season-long accumulation, ranked tiers, and teams layer on top once the event cadence is established and the user base is there.
- *Mid-season launch consideration*: if any competitive layer launches mid-F1-season, the first "season" is necessarily partial. Could be framed as pre-season testing, a sprint championship, or just per-event competitions without season context. The first real full-season championship should probably align with a full F1 calendar year.

**Possible M1 architectural considerations (flagged for deliberation — not prescribed):**
The brainstorming surfaced these as things that MIGHT be hard to retrofit if not considered early. Each needs proper analysis to determine whether it's actually load-bearing for M1 or can safely wait. The tradeoff in each case is early complexity vs. later refactoring cost.

1. **Score data structure.** If M1 treats scores as ephemeral (display during the game session, discard after), adding competitive scoring later means building the entire scoring pipeline retroactively. The alternative: every game session produces structured score output — `{player, mode, game_id, scores, timestamp, metadata}` — even if nothing consumes it in M1. The structured data just accumulates. When ranked/teams launch, the pipeline already has data to work with. *Among the open questions*: is this cheap insurance (just a database write per game) or premature complexity (schema design, storage, migration concerns)?

2. **Player identity model.** Party mode (Layer 2) works with ephemeral identity — "Jake on the couch" exists for the game night and disappears. Ranked/career (Layers 3-4) require persistent cross-session accounts. The question is whether M1's identity model should anticipate upgrade: a player who starts as ephemeral "Jake" can later link that identity to a real account, preserving their play history and group associations. *Options*: (a) M1 uses fully ephemeral identity, accept that pre-account play history is lost when accounts launch. (b) M1 assigns a device-linked anonymous ID that can later be claimed by an account. (c) M1 requires lightweight accounts from the start. Each has different UX and engineering tradeoffs.

3. **Score category breakdown.** If modes produce a single opaque "points" number, breaking scores into categories later (knowledge, creative, action, judgment) for team leaderboards means refactoring every mode's scoring logic. The alternative: modes declare what score categories they produce from the start, even if M1's UI just sums them into one number. *Among the open questions*: how stable are the categories? If we pick "knowledge / creative / action / judgment" now and it turns out to be wrong, we're migrating data. The category taxonomy itself needs deliberation.

4. **Session context tagging.** If every play session carries metadata about its context (free play, friends/party, ranked, competitive event), scores can be routed to the right leaderboard/system later. Without this, you can't retroactively distinguish "Jake played this casually on the couch" from "Jake played this as a ranked match." *Among the open questions*: in M1 where there's only one context (friends/party), is tagging valuable or just noise?

5. **Event/calendar content model.** Race weekend events could be modeled as a first-class content type: `{event_id, circuit, dates, eligible_modes, scoring_config, time_limited_content, results}`. Or they could just be "the app features a different circuit pack each weekend" with no structural distinction from any other content. The first-class model enables competitive scoring, event-specific leaderboards, and season accumulation later. The lightweight model is simpler now but may need replacing. *Among the open questions*: is there a middle ground — a content type that's slightly more structured than "featured pack" without the full event infrastructure?

**Open questions:**
- How many players per team for it to feel meaningful? 10? 100? 10,000?
- Can teams have internal structure (team captain, roles)?
- Is there inter-team social — team chat, team strategy for which modes to focus on?
- How visible are team standings to non-competitive players? (Ambient awareness vs. opt-in)
- Could there be team-vs-team direct matchups (head-to-head events)?
- How to prevent toxicity in competitive context while keeping the fun energy?
- Does the team you play for in career mode connect to the driver you pick in party mode? (If you're on the Ferrari competitive team, does your driver select default to a Ferrari driver?)
- Engagement threshold: how many active users before team competition is viable? Don't launch teams at 50 users.

---

## Driver Select — Session Identity Frame
**Status**: developing
**Origin**: Session 2 — emerged from fashion mode discussion, recognized as platform-level concept

**The idea:** Every party session opens with a character select screen. Each player picks a driver on their phone. The host screen reveals the lineup: "Tonight's grid: Logan as Alonso, Sarah as Leclerc, Jake as Hamilton, Emma as Verstappen." Driver avatars represent you on the host screen throughout the session.

**How modes use it:**
Each game mode declares whether the driver pick is mechanically relevant or just cosmetic.
- **Mechanically relevant**: Paddock Fashion (you're dressing your driver), Pit Stop Co-op (you're their crew), Stewards' Room (argue from your team's perspective?), Team Principal's Desk (making calls for your driver's team)
- **Cosmetic only**: Geography (driver avatar on scoreboard), Words of Wisdom (driver face next to your name), any mode where the mechanic doesn't involve driver identity

**What it does for free:**
- Trash talk and investment — real-world rivalries map onto friend group rivalries for the night
- Visual distinctiveness on host screen — spectators track who's who at a glance
- Social energy at selection — two people want the same driver, drama before games start
- Career meta-game potential — "Logan has played as Alonso 14 times, total score: 847"
- Opening ceremony moment — character select IS the tone-setter for the night

**Open questions:**
- **Duplicate drivers**: allow or force unique picks? Unique creates conflict/negotiation (social energy) but limits large groups. Allow duplicates + optional "unique mode" toggle?
- **Driver roster scope**: current grid only? Or include legends (Senna, Schumacher, Kimi)? Legends expand the roster and tap nostalgia but need avatar assets for each
- **Persistence across sessions**: does your driver choice persist ("I'm always Leclerc") or fresh each night? Could offer both — a "main" driver on your profile + per-session override
- **Mechanical depth per mode**: how deep does the driver identity go in modes that use it? Shallow (cosmetic + name) vs. deep (your driver's real attributes affect gameplay — e.g., in strategy mode your driver's actual race pace matters)? Deep is more interesting but harder to balance
- **Team dynamics**: if two players pick drivers from the same team, are they teammates in team-based modes? Could create natural alliances
- **Unlockable drivers**: start with current grid, unlock legends through play? Ties into the hidden discovery architecture and completionism
- **Non-driver characters**: can you be a team principal? A commentator? A steward? Expands identity options and humor — someone playing as Horner all night has a different energy than someone playing as Verstappen
- **Avatar customization**: beyond picking a driver, can you customize them? Hats, accessories, silly additions? The fashion mode's sprite assets could double as avatar customization pieces
- **How does this interact with the circuit-pack frame?** You pick a driver AND the group picks a circuit. "Tonight: the Monaco pack, and your grid is Alonso, Leclerc, Hamilton, Verstappen." That's the full session frame — place + characters.

---

## Community Content Creation
**Status**: seed — identified as important, not yet designed
**Research**: [R12](RESEARCH-TODOS.md) (GeoGuessr UGC model), [R13](RESEARCH-TODOS.md) (moderation patterns)
**Origin**: Session 2 — emerged from content flywheel discussion

**Two layers of community content:**

**Layer 1: Private creation (friends-only)**
Content for YOUR group only. No moderation needed — it never leaves your circle.
- Custom WoW prompts with inside jokes
- Fashion show theme packs specific to your friend group
- Geography rounds from photos of places you've been together
- Custom Quiplash prompts

This is almost free if the content model is right — letting users fill in the same schema that authored content uses is just a form. The key requirement: content schemas must be clean and documented, not embedded in code.

**Layer 2: Public creation (community-shared)**
Content published for everyone. This needs discovery, rating, and moderation.
- Community-designed circuits for racing games (the circuit designer as its own creative game — Mario Maker energy)
- Community-curated Stewards' Room incident packs
- Geography rounds from fans' own race weekend photos
- "Best of" collections curated from community submissions
- Meme prompt packs rated by the community

**Creation tools that could be fun in themselves:**
- **Circuit designer**: draw track layout, set width/corners/elevation, test-drive it, publish. This is Mario Maker energy — creation IS a game. People will spend hours perfecting circuits. Every community circuit = a new map for racing games for free.
- **WoW round builder**: write the radio exchange setup, write the real response, tag metadata (year, GP, driver). Test on friends before publishing.
- **Geography round builder**: upload your own photos from a race weekend. Set the answer, add difficulty tags, write a hint. People who attend GPs become content contributors.

**Content flywheel**: community creation is the strongest answer to "how does the platform keep growing without us authoring everything?" AI-assisted drafts + community curation + editorial review = content at scale.

**Moderation spectrum:**
- Private content: no moderation needed
- Friend-group shared: no moderation needed (social accountability)
- Public community: needs moderation before or after publish — automated filters + community reporting + human review for flagged content
- Featured/official: editorial review

---

## Between-Sessions Social
**Status**: seed — discussed but not designed
**Origin**: Session 2 — emerged from "what goes beyond the game session" discussion

**The idea:** What happens BETWEEN game nights for a friend group that plays regularly?

**Group history and identity:**
Over time, a group builds a record. Who's best at geography? Who writes the funniest fakes? Who's the harshest steward? These are social identities that only exist within the group. Leaderboards that are group-scoped, not global. "Don't let Jake pick the penalty, he gives everyone a drive-through" as an inside joke the platform remembers.

**Shareable moments:**
After a game night, the platform generates shareable cards/screenshots: "Logan wrote 'box box box for feelings' as a fake radio message and 4 people fell for it." Designed to be dropped into WhatsApp/Discord group chats. The game extends into the spaces where the friend group already lives.

**Persistent bets and predictions:**
Before a race weekend, the group makes predictions through the platform. After the race, the platform scores them and the reactive content pack references group predictions.

**How this differs from BoxBoxd's social:**
BoxBoxd's social is feed-based (post, react, follow — a Twitter-like model). This is group-based (your specific friend group's history, jokes, rivalries). The social unit is the group, not the individual.

---

## Platform Branding
**Status**: decision needed before public launch, not blocking development
**Origin**: Session 2 — realization that the project has outgrown its name

"Prix-guesser" is a game name (the geography guessing game), not a platform name. The project is now an F1 party platform with multiple game modes. Calling the platform "prix-guesser" is like calling all of Jackbox Games "Drawful."

Structure: **[Platform Name] → contains prix-guesser (geography), Words of Wisdom, Paddock Fashion, The Verstappen Game, Stewards' Room, etc.**

Prix-guesser is the first game developed, the flagship, probably what people initially know the platform by. The platform name is what everything lives under. Rebranding can happen whenever, but the mental model shift matters for planning: we're building a platform that hosts games, not a single game with extra features.

Not attempting naming here — that's a separate creative exercise.

---

## The Hidden Discovery Architecture
**Status**: concept from Session 1
**Origin**: User's product instinct — meme modes as unlockable easter eggs

Geography anchor is the front door. Meme/radio/creative modes are discovered — hidden, unlockable, rewarding exploration. "Have you found the paddock yet?" as word-of-mouth. Protects serious identity while creating virality.
