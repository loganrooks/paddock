# Lane 4: Multi-Milestone Vision & Design Space Audit

**Auditor**: Strategic reviewer
**Date**: 2026-04-08
**Scope**: All project artifacts, v2 requirements, discovery context
**Verdict**: The v1 architecture is well-conceived and avoids the most dangerous foreclosures. There are a handful of cheap decisions that should be made now to protect v2+, and the v2 requirements section has meaningful gaps.

---

## 1. v1 Architecture Risk Assessment

### What Is Well-Protected

The three-layer separation (authored content / pure rules / live room orchestration) is the single most important architectural decision in the project, and it is correct. It directly protects:

- **Future solo and async wrappers** can consume the same content and rules layers without touching room code (WRAP-01).
- **Future team play** can be implemented as a room-layer concern without changing content or scoring contracts (WRAP-02).
- **Future adjacent modes** can implement new `ModeRuntime` interfaces against the same room shell (MODE-01).
- **Daily/recurring challenges** can be a thin execution wrapper over frozen match snapshots (RET-01).

The authored round model with explicit answer target types, clue families, scoring profiles, and reveal explanations is the right core asset. It is more expensive to author than thin geo data, but it is the thing that will compound in value across milestones. This is being treated correctly as the project's primary investment.

The content compiler pipeline (YAML source -> Zod validation -> canonical JSON) creates a clean separation between mutable authoring and immutable playable content. This directly enables future pack versioning, pack sharing, and content quality feedback loops.

### What Is At Risk of Foreclosure

**Risk 1: No pack identity or version scheme in the content contract**
Severity: HIGH

The Phase 1 pack schema includes `id`, `slug`, `title`, `version`, and `roundOrder`, but there is no discussion of how pack identity and versioning interact across sessions. If session data (Phase 6) records which pack was played but that pack later changes, the calibration data becomes unreliable. Worse, if packs are ever shared between friends (a natural v2 feature), there is no content-addressing or version-pinning mechanism.

This matters now because the compiled JSON artifact is the unit of play. If the compile output does not carry a content hash or version fingerprint, session records cannot reliably reference "exactly this pack at this state."

**Risk 2: No player identity model at all**
Severity: HIGH

The entire v1 architecture assumes guest nicknames with no persistence. This is fine for v1 party play, but every v2 feature that touches history, profiles, statistics, or cross-session identity (RET-02, team play rosters, daily challenge participation) requires a player identity model. The risk is not that v1 needs accounts -- it does not. The risk is that the session data schema, scoring records, and room state all get built around anonymous ephemeral players, and retrofitting identity becomes a schema migration across multiple layers.

**Risk 3: No event log or replay substrate**
Severity: MEDIUM

OPS-02 says session data should record per-round outcomes sufficient to identify broken or high-value rounds. But the current architecture does not define whether this is a flat summary record or a replayable event log. If it is only a summary (final scores, correct/incorrect per round), it cannot support:
- Session replays (a compelling social feature)
- Detailed calibration (was the round hard because nobody got close, or because one clue was misleading?)
- Spectator catch-up (joining a session in progress)

An event-sourced session log is cheap to add now and expensive to retrofit.

**Risk 4: Room model is tightly coupled to "one host, N players" topology**
Severity: LOW-MEDIUM

The current room model assumes a host who controls pacing and players who submit answers. This is the right v1 shape. But several v2 features imply different topologies:
- Async/solo challenges have no host at all
- Team play may want a team captain with partial host authority
- Daily challenges may want automated pacing with no human host

The room architecture research explicitly recommends keeping the room shell generic and plugging in mode logic, which mitigates this. But the Phase 3/4/5 success criteria are all written in terms of "host does X" language. The recommendation is to ensure the room state machine has a `pacing_authority` concept that can be `host`, `timer_auto`, or `team_captain` rather than hardcoding host control into the state transitions.

**Risk 5: No consideration of offline or degraded-network play**
Severity: LOW

For local party play (cast to TV, phones as controllers), the game depends on local network connectivity. If the room server is on the same machine as the host display, phone controllers need reliable local network access. This is not an architecture problem per se, but it affects deployment topology. The Lane 3 audit likely covers this more directly.

---

## 2. Recommended Cheap v1 Decisions That Protect v2+

These are decisions that cost almost nothing to make now but would be expensive to retrofit later.

### Critical Priority

**C1: Add a content hash to compiled pack output**
In Plan 01-04, the compile step already produces canonical JSON. Add a deterministic content hash (SHA-256 of the normalized JSON, excluding metadata like compile timestamp) to the compiled output. This costs one line of code and enables: reliable session-to-pack references, pack version comparisons, future content-addressed pack sharing.

**C2: Include a `sessionSchema` version field in the session data model**
When Phase 6 defines session recording, include an explicit schema version integer. This is a one-field addition that prevents every future schema change from requiring heuristic migration of historical data.

### High Priority

**H1: Define a `PlayerId` type alias early, even if v1 values are just random UUIDs**
In the domain package, create `type PlayerId = string & { readonly __brand: 'PlayerId' }` (or equivalent). Use it in submission records, score maps, and session data. This costs nothing and means that when persistent identity arrives in v2, the type system guides the migration instead of grep.

**H2: Design the session record to include round-level event arrays, not just outcome summaries**
When Phase 6 arrives, capture `{ roundId, event, timestamp, playerId?, payload? }` arrays per round rather than just `{ roundId, correct: boolean, score: number }`. This enables replays, detailed calibration, and spectator catch-up. The storage cost is negligible for private play volumes.

**H3: Make the room state machine's pacing authority a field, not hardcoded host logic**
In Phase 3, define `pacingAuthority: 'host' | 'auto' | 'team_captain'` in the room config. v1 only implements `host`, but the field exists. This prevents future async/solo modes from requiring a state machine rewrite.

### Medium Priority

**M1: Use stable round IDs that are content-derived, not random**
Round IDs should be deterministic from the round's semantic identity (e.g., `spa-eau-rouge-01`) rather than random UUIDs. The Phase 1 plans already use slug-style IDs in fixtures, which is good. Ensure the compile step preserves these as the canonical identifiers rather than generating new ones.

**M2: Include a `tags` array on rounds, not just packs**
The pack schema includes `tags`, but individual rounds should also carry tags (era, difficulty, clue-family-dominant, circuit, region). This enables future pack generation from round pools, themed daily challenges, and difficulty-based filtering. This is a one-field schema addition.

**M3: Reserve a `metadata` escape hatch on compiled rounds**
Add an optional `metadata: Record<string, unknown>` field to the compiled round output. This lets future milestones attach calibration scores, play counts, difficulty ratings, and other derived data without changing the core schema.

---

## 3. Three-Milestone Arc

### Milestone 1 (v1): "Game Night Works"
**Goal**: One authored F1 anchor mode that is genuinely fun to play with friends on a couch or over a call, with curated content that rewards real F1 knowledge.

**What ships**:
- Authored round packs with circuit and venue answer surfaces
- Private rooms with host pacing, phone controllers, watchable reveals
- Curated starter content (8-15 strong rounds across 3-5 packs)
- Session recording sufficient for basic calibration
- Reconnect handling for phone sleep/wake

**Success signal**: You actually play this with friends on multiple occasions and want to play again. Friends ask "when are we doing another round?"

**Approximate scope**: The current 7-phase roadmap covers this correctly.

### Milestone 2 (v2): "Play Anytime, Anywhere"
**Goal**: The game escapes the requirement for synchronous couch play and supports asynchronous, remote, and recurring play patterns. Content authoring becomes sustainable rather than heroic.

**What ships**:
- Online hosted play via Tailscale/private server (friends connect remotely)
- Async challenge links (play at your own pace, compare scores later)
- Daily or weekly challenge rotation from the content pool
- Player identity with lightweight profiles and session history
- Content authoring tooling (preview, validation feedback, round templates)
- Expanded content: 30+ rounds across themed packs (era packs, difficulty tiers, region packs)
- Section/corner answer surfaces for expert packs
- Basic statistics: personal round history, pack completion, accuracy trends
- Pack sharing between friends (export/import compiled packs)

**Success signal**: Friends play without you being present to host. You get messages about challenge scores. Content creation is measured in hours per pack, not days.

### Milestone 3 (v3): "F1 Party Platform"
**Goal**: The game becomes a genuine F1 party game platform with multiple modes, team play, and a library of content that makes every game night different.

**What ships**:
- Team play variants (pairs, captain mode, expert-carries)
- At least one adjacent non-geography mode (circuit silhouette, era identification, regulation judgment)
- Spectator mode with audience participation hooks
- Themed seasons or curated playlists (e.g., "classic circuits pack," "2024 calendar challenge")
- Richer reveal experiences (animated reveals, historical overlays, era comparisons)
- Session replays and highlight sharing
- Content contribution from trusted friends (moderated authoring)
- Difficulty calibration driven by accumulated play data

**Success signal**: Game nights have variety. Different friends have different favorite modes. The content library is deep enough that repeat packs feel like revisiting, not repetition.

---

## 4. Missing Requirements and Phases

### Missing from v2 Requirements

The current v2 section has 8 requirements across 4 groups. The following are absent and should be added:

**Content Operations (should be a v2 group)**
- **OPS-V2-01**: Author can preview a round in isolation before adding it to a pack (round preview/dry-run UI).
- **OPS-V2-02**: Author can import and validate a pack through a web interface rather than only CLI.
- **OPS-V2-03**: Pack can be exported as a self-contained shareable artifact that another instance can import.

**Player Identity and History (should expand RET group)**
- **RET-03**: Player can see their own round-by-round history and accuracy trends across sessions.
- **RET-04**: Session results are browsable after the session ends (session replay or summary archive).

**Distribution and Access**
- **DIST-01**: The game can be hosted on a private server and accessed by friends over Tailscale or similar private network without per-session setup by the host.
- **DIST-02**: The game can run in "always-on" mode where friends can start sessions without the creator being present.

**Content Scaling**
- **CONTENT-01**: Content pool supports automated pack generation from tagged round pools (e.g., "generate a 10-round pack from era:classic + difficulty:expert").
- **CONTENT-02**: Round-level calibration data (accuracy rate, average score, skip rate) is visible to the author and influences pack curation.

### Missing Phases or Phase Concerns

**Missing from v1 roadmap**: There is no explicit deployment or packaging phase. The current roadmap ends at Phase 7 (reconnect hardening) but does not address how the game actually gets run. For the "cast to TV, phones as controllers" use case, someone needs to:
1. Start a server process
2. Open a browser on the TV
3. Have phone controllers connect

This is an operational concern, not a feature phase, but it deserves at least a sub-phase or explicit task in Phase 5 or 7. A `docker-compose up` or single-command startup script would suffice.

**Missing from v1 roadmap**: There is no explicit "first real playtest" milestone marker. The roadmap treats Phase 6 (starter packs and calibration) as the first place where real play happens, but the game should be playable (with developer-mode rough edges) after Phase 5. An explicit playtest checkpoint between Phase 5 and Phase 6 would help prioritize what actually matters for the first real session.

---

## 5. Biggest Risks to Project Success

These are not commercial risks. They are risks to the project being fun, getting used, and sustaining effort.

### Risk A: Content Authoring Is Too Painful (Effort Risk)
**Severity**: CRITICAL

The entire project depends on a steady flow of authored rounds. If creating one round takes more than 15-20 minutes of focused work, the content corpus will never reach critical mass. The current plan is file-authored YAML, which is appropriate for v1, but the authoring experience needs to be assessed early. Specific pain points to watch:
- Finding and validating Street View panorama references
- Writing reveal explanations that are genuinely informative
- Balancing clue ladders so rounds are neither trivial nor impossible
- Managing media assets (images, map crops) alongside YAML files

**Mitigation**: After the first 5 rounds are authored, do a time audit. If a round takes more than 30 minutes, prioritize authoring tooling over additional game features.

### Risk B: The Game Is Not Actually Fun (Fun Risk)
**Severity**: CRITICAL

The most dangerous scenario is: the architecture is clean, the content is authored, the room works, the reveals are informative -- and it is just not that fun to play. The core loop of "look at this clue, guess the circuit/venue, see the answer" might not generate enough social energy for repeated play. This is inherently uncertain and can only be resolved by actual playtesting.

**Mitigation**: Get to a playable state as fast as possible. Consider whether Phase 2 (rules engine) could produce a playable CLI/terminal dry-run that lets you test round quality with one friend before the room infrastructure exists. The plans mention a "minimal single-round preview/simulation runner" -- this should be treated as a critical deliverable, not a nice-to-have.

### Risk C: The Reveal Is the Whole Game (Design Risk)
**Severity**: HIGH

The discovery and research documents are right that reveals are where the social payoff happens. But there is a risk of underinvesting in reveal quality because it feels like "content work" rather than "engineering work." A mechanically correct reveal ("The answer was Spa-Francorchamps") is worthless. A great reveal ("The distinctive red and white kerbing visible at the bottom of the frame is the exit of Eau Rouge, one of the most famous corners in motorsport. The Kemmel Straight grandstands are visible in the background, confirming this is the uphill run from Eau Rouge to Les Combes") is what makes the game feel like it was made by someone who cares.

**Mitigation**: Write 3-5 reveal explanations before writing any code. If the reveals feel flat, the game will feel flat regardless of architecture quality.

### Risk D: Scope Creep Before First Play (Effort Risk)
**Severity**: HIGH

The project has already produced substantial planning, research, and architecture documentation before a single line of application code exists. This is appropriate for a project that wants to think big picture, but the risk is that planning becomes the project. Seven phases with detailed plans, threat models, and acceptance criteria can feel like momentum without being momentum.

**Mitigation**: Set a hard calendar deadline for the first playable session with a friend. Work backward from that deadline. If Phase 1 takes more than a week of focused work, something is wrong with the execution pace.

### Risk E: The Content Model Is Too Complex for the Actual Game (Complexity Risk)
**Severity**: MEDIUM

The authored round model is impressively thorough: answer targets, clue families, media kinds, coverage classes, fallback strategies, scoring profiles, venue media capabilities, reveal explanations. But the v1 game is "look at a clue, guess the circuit." If the authoring schema requires filling in 15+ fields per round, authors (which is just Logan and maybe one friend) will burn out. The schema should make the common case easy and the complex case possible.

**Mitigation**: After authoring the three starter rounds in Phase 1, honestly assess: how many of these fields actually influenced the gameplay experience? Which fields could have sensible defaults? Can the compile step infer or default values that the author did not explicitly set?

### Risk F: Friends Cannot Actually Run This (Distribution Risk)
**Severity**: MEDIUM

The stakeholder context says non-technical friends should be able to boot this up. A monorepo with pnpm workspaces, TypeScript compilation, YAML content pipelines, and a Colyseus server is not something a non-technical person can run. This is fine if the game is always hosted by Logan, but it limits the "play without me" future.

**Mitigation**: By the end of v1, the deployment story should be one of: (a) a Docker container that runs with one command, (b) a hosted instance on dionysus that friends connect to via Tailscale, or (c) a static build with an embedded room server. Option (b) is the most realistic near-term path.

---

## 6. Concrete Recommendations

### Critical (do before or during Phase 1 execution)

| ID | Recommendation | Effort | Rationale |
|----|---------------|--------|-----------|
| CR-1 | Add a deterministic content hash to compiled pack JSON output | 1 hour | Enables reliable session-to-pack references, pack versioning, and future pack sharing. Without this, calibration data from Phase 6 is fragile. |
| CR-2 | Write 3-5 reveal explanations in prose before any code | 2 hours | Validates the core game feel before engineering investment. If reveals are flat, the project needs a content rethink, not more architecture. |
| CR-3 | Set a hard deadline for first playable session with a real friend | 0 hours | Prevents planning from becoming the project. Recommend: first real play within 4-6 weeks of starting Phase 1 execution. |

### High (do during Phases 2-3)

| ID | Recommendation | Effort | Rationale |
|----|---------------|--------|-----------|
| HR-1 | Define a branded `PlayerId` type in the domain package | 30 min | Every submission, score, and session record that uses a plain string now will need migration later. A branded type costs nothing and guides future work. |
| HR-2 | Make the Phase 2 dry-run runner genuinely playable, not just a test harness | 1-2 days | This is the fastest path to validating whether rounds are fun. Do not wait until Phase 5 for the first real play experience. |
| HR-3 | Add `pacingAuthority` to room config in Phase 3 | 30 min | Prevents the state machine from hardcoding host-only pacing. v1 only implements `host`, but the field exists for future async/auto modes. |
| HR-4 | Include round-level tags in the content schema | 30 min | Enables future pack generation, filtering, and themed challenges. One-field addition with zero v1 complexity cost. |

### Medium (do during Phases 4-6)

| ID | Recommendation | Effort | Rationale |
|----|---------------|--------|-----------|
| MR-1 | Design session recording as event arrays, not just outcome summaries | 1 day | Enables replays, detailed calibration, and spectator catch-up. Much cheaper to design in than to retrofit. |
| MR-2 | Add a deployment task to Phase 5 or 7 | 1-2 days | A `docker-compose.yml` or startup script that gets the game running with one command. Without this, "game night" requires developer setup every time. |
| MR-3 | Track authoring time per round and set a pain threshold | 0 hours | If rounds consistently take >30 minutes, authoring tooling should jump the priority queue ahead of game features. |
| MR-4 | Add v2 requirements for content operations, player identity, and distribution | 1 hour | The current v2 section is mode-focused but missing the operational and identity infrastructure that modes depend on. |

### Low (capture for future milestone planning)

| ID | Recommendation | Effort | Rationale |
|----|---------------|--------|-----------|
| LR-1 | Reserve an optional `metadata` field on compiled rounds | 15 min | Future-proofs the schema for calibration data, play counts, and difficulty ratings without core schema changes. |
| LR-2 | Plan for content-addressed pack sharing in milestone 2 | Planning only | The compiled pack JSON with content hash is the natural unit of sharing. Design the import/export flow around it. |
| LR-3 | Consider a "round quality score" derived from session data | Planning only | After 10+ sessions, some rounds will clearly be better than others. An automated quality signal would help curation. |

---

## 7. Summary Verdict

The v1 architecture is sound. The three-layer separation, authored content model, and content compiler pipeline are the right foundation. The biggest risks are not architectural -- they are about content authoring effort, actual fun factor, and the gap between planning ambition and execution pace.

The most important thing this project can do right now is get to a playable state and put it in front of a friend. Every week spent refining architecture before that happens is a week of compounding risk that the game is not actually fun.

The v2 requirements section needs expansion to cover content operations, player identity, distribution, and content scaling. The three-milestone arc should be: "game night works" -> "play anytime, anywhere" -> "F1 party platform."

The cheapest highest-value v1 decisions are: content hashing on compiled packs, a branded PlayerId type, round-level tags, and a pacing authority field in room config. These cost hours in total and save weeks of migration work later.
