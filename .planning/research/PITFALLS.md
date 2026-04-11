# Domain Pitfalls: Prix Guesser

**Domain:** Private-only F1 geography-and-circuit party game  
**Researched:** 2026-04-08  
**Overall confidence:** HIGH for content/media and room-state pitfalls, MEDIUM for broader product-shape pitfalls

## Refresh Note (2026-04-11)

The later 2026-04-10 research wave did not overturn these pitfalls, but it sharpened three of them:

- watchability should be read as shared-legibility, suspense, and reveal payoff, not just as visual style
- visibility state and trust boundary are staged product choices, not one binary private/public switch
- scope restraint is itself a trust and safety strategy while the product remains host-led and private-first

This file is intentionally specific to Prix Guesser's current shape:
- expert-first F1 audience
- authored rounds rather than generic geography drops
- host-screen-friendly private rooms
- circuit-internal recognition as the core fantasy

## Practical Phase Labels

These are phase topics for roadmap planning, not locked roadmap numbers.

| Phase Topic | Meaning |
|-------------|---------|
| Anchor Mode | Define the first playable fantasy, round contract, scoring, reveal grammar |
| Content Pipeline | Build the curated corpus, venue media profiles, validation, fallback ladder |
| Live Room Foundation | Choose authority model, room lifecycle, timers, host/controller flow |
| Hardening + Calibration | Reconnect behavior, analytics, playtest loops, fairness tuning |
| Authoring Tools + Expansion | Improve content throughput and add wrappers or adjacent modes |

## Product Pitfalls

### Pitfall 1: Shipping a generic geo quiz with F1 paint

**Severity:** Critical  
**What goes wrong:** The game looks like "GeoGuessr, but motorsport-themed" instead of feeling like knowledgeable fans are reading circuit identity, venue texture, and era-specific signals. The product may still work mechanically, but it misses the main fantasy.  
**Why it happens:** GeoGuessr-like loops are easy to copy, and the simplest implementation path rewards location precision more than F1-specific interpretation. Discovery already flagged that generic geography fluency can dominate domain fandom if left unchecked. [S1][S2][S6][S7]  
**Warning signs:**
- Playtesters mostly talk about signage, compass orientation, or general geography tricks.
- Reveals explain only distance error, not why the venue was identifiable as Monaco, Spa, Suzuka, etc.
- Rounds feel interchangeable with a generic travel game after removing F1 labels.
**Prevention strategy:**
- Make `answer_target_type`, `reveal_explanation`, and clue intent first-class in the round model from the start.
- Require every pack to contain rounds that reward F1-specific recognition, not only map placement skill.
- Validate the first pack against a blunt question: "Would this still feel special if the player were good at geography but weak on F1?"
**Likely phase:** Anchor Mode  
**Sources:** [S1][S2][S6][S7]

### Pitfall 2: Letting venue-approach clues silently replace circuit-internal recognition

**Severity:** Critical  
**What goes wrong:** The product drifts from "recognize the circuit or circuit section" toward "recognize the city, marina, park, or access road." That may still produce playable rounds, but it erodes the core promise.  
**Why it happens:** Circuit coverage is uneven, and approach media is often easier to source than on-track or track-edge clues. Without explicit guardrails, the easier clue family wins. [S1][S2][S4][S7]  
**Warning signs:**
- The strongest early packs rely mostly on skylines, waterfronts, transit, or venue-adjacent roads.
- "Circuit-internal" rounds are rare outside Monaco, Singapore, Melbourne, or Las Vegas.
- Playtest feedback says the game feels more like host-city recognition than circuit literacy.
**Prevention strategy:**
- Split clue families explicitly: `circuit_internal`, `circuit_edge`, `venue_approach`, `city_context`.
- Track pack composition and cap approach-heavy rounds in the anchor mode.
- Treat fallback-first venues as a different authored challenge, not a silent substitute for on-circuit recognition.
**Likely phase:** Anchor Mode, Content Pipeline  
**Sources:** [S1][S2][S4][S7]

### Pitfall 3: Expanding into a party platform before the anchor mode is proven

**Severity:** High  
**What goes wrong:** The roadmap spreads into daily modes, trivia sidecars, ranking, training, and adjacent F1 party ideas before the geography-and-circuit core is delightful. The result is breadth without a strong front door.  
**Why it happens:** The project legitimately has expansion headroom, but that makes premature mode sprawl tempting. Discovery repeatedly flags this as an open design choice, not a solved direction. [S1][S2][S6]  
**Warning signs:**
- More design energy goes into mode menus and wrappers than into round quality and reveal quality.
- New mode ideas appear before the first pack and room loop feel replayable.
- Different modes start asking for incompatible content structures.
**Prevention strategy:**
- Make the first milestone prove one anchor mode and one social wrapper.
- Reuse a shared clue substrate later, but do not build every wrapper at once.
- Delay adjacent modes until the first corpus shows repeat play value with friends.
**Likely phase:** Anchor Mode  
**Sources:** [S1][S2][S6]

### Pitfall 4: Solvable on a phone, unreadable in a room

**Severity:** High  
**What goes wrong:** Individual players can submit answers, but the host-screen experience is flat. Spectators cannot follow clue state, lock-in state, reveal logic, or score swings, so the game loses party energy.  
**Why it happens:** Geo-guess loops are easy to optimize for the active solver and easy to neglect as theatre. Discovery's comp work shows motion, reveal pacing, and watchability are major differentiators for room play. [S2][S3][S6]  
**Warning signs:**
- People go quiet during rounds because only the controller holder has meaningful context.
- Reveals feel administrative instead of dramatic.
- Host-screen layouts emphasize forms and maps, not shared comprehension.
**Prevention strategy:**
- Design the host reveal grammar early: clue, lock, answer, why-identifiable, standings.
- Treat "watchability" as a success criterion in playtests, not a visual polish task.
- Prototype large-screen states before polishing solo/controller UX.
**Likely phase:** Anchor Mode, Live Room Foundation  
**Sources:** [S2][S3][S6]

## Content Pitfalls

### Pitfall 5: Using a thin `lat/lng + pano` schema and discovering too late that the game needs authored semantics

**Severity:** Critical  
**What goes wrong:** The content model starts as generic geography data and later has to absorb circuit, section, era, clue ladder, aliases, partial-credit logic, and reveal explanation. That rewrite hits content, scoring, and room logic simultaneously.  
**Why it happens:** Thin schemas are fast for prototypes, but Prix Guesser's core loop depends on authored meaning. Local discovery identified this as one of the highest-leverage architecture choices in the project. [S1][S2][S7]  
**Warning signs:**
- Round objects only store coordinates plus media settings.
- New answer types require special-case code instead of data-driven behavior.
- Reveal text is optional or absent because the schema has nowhere natural to put it.
**Prevention strategy:**
- Start with an authored round contract even if the first corpus is tiny.
- Require fields for `answer_target_type`, `accepted_aliases`, `season_or_era`, `clue_steps`, `source_refs`, and `reveal_explanation`.
- Write fixtures for at least three round families before locking the schema.
**Likely phase:** Anchor Mode  
**Sources:** [S1][S2][S7]

### Pitfall 6: Treating Street View coverage as uniform, stable, and available at play time

**Severity:** Critical  
**What goes wrong:** Rounds break because a pano vanished, a point returns a generic image, a venue never had dependable internal coverage, or a fallback-first circuit was mistaken for a Street View-friendly one. Players experience this as broken content, not as a mapping nuance.  
**Why it happens:** F1 venue coverage is circuit-specific, not binary, and Google explicitly documents that pano IDs can change and that unavailable imagery can return generic results unless metadata or `return_error_code=true` is used. [S3][S4][E1]  
**Warning signs:**
- Rounds occasionally load blank or generic imagery.
- The same circuit behaves differently across curated points.
- Authors rely on manual spot checks without a reusable validation step.
**Prevention strategy:**
- Give every venue a media profile before it enters the corpus.
- Validate candidate coordinates with Street View metadata and `return_error_code=true` before release.
- Store fallback media and fallback clue flavor alongside the primary clue.
- Re-check curated Google-dependent rounds periodically because pano references can drift over time.
**Likely phase:** Content Pipeline  
**Sources:** [S3][S4][E1]

### Pitfall 7: Letting easy public-road venues distort the corpus

**Severity:** High  
**What goes wrong:** The first playable corpus over-indexes on the circuits that are easiest to map with public-road imagery. The game then teaches players that Prix Guesser is mainly about city circuits and approach context, not the broader F1 venue landscape.  
**Why it happens:** Monaco, Singapore, Las Vegas, and Melbourne are naturally easier to ship than fallback-first venues like Shanghai, Jeddah, Miami, or Lusail. That convenience can quietly become product direction. [S4]  
**Warning signs:**
- The best rounds are overwhelmingly from public-road circuits.
- Permanent circuits require much more manual work and stay unshipped.
- Difficulty balance is driven by venue availability rather than by design intent.
**Prevention strategy:**
- Set explicit pack-mix targets across `Allow`, `Allow With Fallback`, and `Fallback-First` venues.
- Ship some deliberately authored fallback-media rounds early so the corpus does not equate "good round" with "good Street View."
- Maintain a visible backlog of deferred venues instead of pretending the early corpus is representative.
**Likely phase:** Content Pipeline  
**Sources:** [S4]

### Pitfall 8: Ambiguous prompts and scoring contracts

**Severity:** Critical  
**What goes wrong:** A player recognizes the right circuit but loses because the round secretly wanted the corner, era, or venue complex. Post-round debate becomes about judging ambiguity instead of knowledge.  
**Why it happens:** Prix Guesser has multiple plausible answer surfaces, but generic geo games assume one obvious scoring surface. Without explicit contracts, the UI and scoring engine will disagree with player expectations. [S1][S2][S7]  
**Warning signs:**
- Players say "I was right, just not in the way the game wanted."
- Authors keep adding one-off alias rules by hand.
- Reveals do not explain what counted as correct, partially correct, or wrong.
**Prevention strategy:**
- Make the answer surface explicit before the round starts or in the round rules for that pack.
- Define partial-credit tables per round family.
- Store accepted aliases and reveal bounds in content, not code comments.
- Add regression fixtures for scoring examples before the first multiplayer playtest.
**Likely phase:** Anchor Mode, Content Pipeline  
**Sources:** [S1][S2][S7]

### Pitfall 9: No calibration loop for authored content

**Severity:** High  
**What goes wrong:** Difficulty, clue quality, and reveal quality drift wildly because there is no structured way to learn which rounds are dead, misleading, trivial, or brilliant.  
**Why it happens:** Hand-authored content can look "done" as soon as it loads, but the real work is calibration. Expert-biased games are especially vulnerable because authors know too much. [S2][S3][S6]  
**Warning signs:**
- Round feedback is anecdotal and hard to compare across sessions.
- Certain rounds produce all-or-nothing outcomes with no explanation.
- The same confusion keeps reappearing in playtests.
**Prevention strategy:**
- Record per-round guess spread, time-to-lock, clue-step usage, and common wrong answers.
- Add a simple author QA rubric: identifiable signal, intended answer surface, expected confusion, reveal payoff.
- Retire or rework rounds that fail repeatedly instead of patching them ad hoc.
**Likely phase:** Hardening + Calibration  
**Sources:** [S2][S3][S6]

## Architecture Pitfalls

### Pitfall 10: Treating "backend choice" as the decision instead of room authority

**Severity:** Critical  
**What goes wrong:** The project debates PartyKit vs Colyseus vs BaaS, but never clearly defines who is authoritative for timers, scoring, reveal transitions, and reconnect recovery. The result is fragile room logic regardless of framework choice.  
**Why it happens:** "Backend" sounds concrete, but for this product the hard problem is authoritative session state. The local decision context explicitly warns against conflating transport, persistence, auth, and game-loop authority. [S5]  
**Warning signs:**
- Clients compute their own timers or scores.
- Host state is canonical in some places and server state is canonical in others.
- Room bugs are fixed by adding more messages rather than clarifying state transitions.
**Prevention strategy:**
- Decide the authority model before selecting the room stack.
- Keep canonical round phase, timer, submissions, and score in one place.
- Use explicit state transitions and message types; treat client devices as views and input sources, not independent referees.
- If using BaaS for storage or presence, do not let it masquerade as authoritative live-game logic.
**Likely phase:** Live Room Foundation  
**Sources:** [S5][E4][E5][E6][E7]

### Pitfall 11: No first-class reconnect and sleep/wake story for phone controllers

**Severity:** Critical  
**What goes wrong:** A player refreshes, a phone sleeps, or the host drops, and the session becomes unrecoverable or unfair. This is especially damaging in a host-screen-plus-controller format because mobile devices are the least reliable clients in the room.  
**Why it happens:** Reconnect is easy to postpone in early prototypes, but private-room party play depends on it much more than a static quiz app does. Colyseus documents reconnection flows directly; PartyKit allows stateful rooms but requires explicit reconnect design. [S3][S5][E4][E6][E7]  
**Warning signs:**
- QA is mostly desktop-tab based.
- Rejoining sends a player back to the lobby instead of restoring current state.
- The host has no visibility into who disconnected, rejoined, or missed a lock-in.
**Prevention strategy:**
- Test every milestone on real phones with screen sleep and network toggles.
- Assign persistent player tokens within a room session.
- Define host disconnect behavior explicitly: resume, host migration, or abort.
- Build a room snapshot/rejoin path before adding advanced room features.
**Likely phase:** Live Room Foundation, Hardening + Calibration  
**Sources:** [S3][S5][E4][E6][E7]

### Pitfall 12: Coupling the room engine to one round type

**Severity:** High  
**What goes wrong:** The live-room logic assumes every round is a single map drop with one score formula. As soon as the game wants `circuit + corner`, era-aware judging, clue ladders, or partial credit, the room protocol becomes a blocker.  
**Why it happens:** Generic geography implementations often hard-code one answer loop. Prix Guesser needs a room model that tolerates richer authored rounds without becoming abstract mush. [S1][S2][S5][S7]  
**Warning signs:**
- New round types require new room phases rather than using a shared submission/judging contract.
- Scoring logic is embedded in UI code.
- Reveal payloads differ wildly by round because the protocol has no generic reveal structure.
**Prevention strategy:**
- Separate room phases from round semantics.
- Define one submission envelope and one reveal envelope that can carry different judged outcomes.
- Test the room contract against at least three distinct round families before freezing it.
**Likely phase:** Live Room Foundation  
**Sources:** [S1][S2][S5][S7]

## Execution Pitfalls

### Pitfall 13: Trying to prove every wrapper at once

**Severity:** High  
**What goes wrong:** The project tries to prove solo play, challenge links, live private rooms, couch play, and hybrid remote play in the same implementation wave. Complexity rises faster than learning.  
**Why it happens:** The clue substrate may eventually support all of these, but that does not mean the first milestone should implement them. Discovery explicitly kept "which shared format comes first?" open. [S1][S2][S3][S5]  
**Warning signs:**
- The same milestone includes deep work on async challenges and live rooms.
- Progress is measured by infrastructure completeness rather than by good sessions with a real group.
- Core loop bugs are hard to localize because too many wrappers are in motion.
**Prevention strategy:**
- Pick one first proof target. Current evidence favors host-screen private rooms for this product shape.
- Keep the pack snapshotting and round contract reusable, but postpone additional wrappers until the first one produces strong sessions.
- Use later phases to generalize only after the first wrapper exposes the real constraints.
**Likely phase:** Anchor Mode, Live Room Foundation  
**Sources:** [S1][S2][S3][S5]

### Pitfall 14: Delaying content validation and authoring support until the corpus is already painful

**Severity:** High  
**What goes wrong:** Every new round requires code edits, manual image rescue, and fragile spreadsheet habits. Content velocity collapses right when the project needs more packs to learn.  
**Why it happens:** It is correct not to build a heavy admin tool too early, but it is a mistake to skip import validation, schema checking, and repeatable author workflow entirely. Those are different decisions. [S1][S2][S3]  
**Warning signs:**
- Engineers are hand-editing runtime code to add or fix rounds.
- The same fields are missing or interpreted differently across content files.
- One bad source URL or bad pano breaks a pack late in QA.
**Prevention strategy:**
- Start with files or spreadsheets, but put a validator/import step in front of the app.
- Add preflight checks for media availability, required fields, aliases, and scoring contract.
- Build internal authoring UI only after 2-3 packs reveal repeated friction patterns.
**Likely phase:** Content Pipeline, Authoring Tools + Expansion  
**Sources:** [S1][S2][S3][S4]

### Pitfall 15: Flying blind in playtests

**Severity:** High  
**What goes wrong:** The team cannot tell whether a bad round failed because of clue ambiguity, poor room pacing, sync issues, or wrong audience targeting. Roadmap decisions then get made off vibes.  
**Why it happens:** Early private projects often treat playtests as informal hangouts, but Prix Guesser's main risks are highly confounded across content, UX, and synchronization.  
**Warning signs:**
- Session notes say "fun but rough" without isolating the cause.
- There is no consistent record of disconnects, lock-in timing, score spread, or round confusion.
- The same debates reappear in planning because past sessions are not comparable.
**Prevention strategy:**
- Log both content signals and room signals from the first multiplayer prototype.
- After every session, capture which rounds landed, which ones confused, and whether the problem was clue design or systems behavior.
- Treat telemetry and structured notes as part of the product loop, not as ops garnish.
**Likely phase:** Hardening + Calibration  
**Sources:** [S2][S3][S5]

## Open Design Choices That Are Not Pitfalls Yet

These should stay open unless later research or prototyping forces a decision.

- **PartyKit vs Colyseus is not itself the pitfall.** The pitfall is avoiding an authority-model decision while pretending framework choice solved it. [S5][E4][E6]
- **Spreadsheet-driven authoring vs internal tooling is not itself the pitfall.** The pitfall is having no validation/import discipline while waiting for a future tool. [S1][S2][S3]
- **Location-first game vs broader party shell is not itself the pitfall.** The pitfall is broadening scope before the anchor mode has clear repeat play value. [S1][S2]
- **Private-only posture is not itself the pitfall.** The real operational risk is building a media pipeline that assumes stable Google imagery, zero billing friction, or unrestricted caching. [E1][E2][E3]

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Anchor Mode | Generic geo-clone drift | Lock the authored round contract and reveal grammar before scaling content |
| Anchor Mode | Ambiguous answer surfaces | Define round families and scoring contracts with fixtures |
| Content Pipeline | Street View brittleness | Add venue media profiles, metadata checks, and fallback ladders |
| Content Pipeline | Corpus distortion toward easy city circuits | Track venue-class mix intentionally |
| Live Room Foundation | Split authority between host and clients | Put canonical timer/score/phase in one authority layer |
| Live Room Foundation | Reconnect ignored | Test sleep/wake and refresh on real phones from the first room prototype |
| Hardening + Calibration | No way to separate content failures from sync failures | Log round outcomes and room events together |
| Authoring Tools + Expansion | Tooling arrives only after content velocity collapses | Build validation/import first, UI tooling second |

## Sources

### Project-Specific Sources

- [S1] `.planning/PROJECT.md`
- [S2] `discovery/14-gsd-seed.md`
- [S3] `discovery/09-feasibility.md`
- [S4] `discovery/11-circuit-coverage-audit.md`
- [S5] `discovery/13-room-backend-decision-context.md`
- [S6] `discovery/03-reference-designs.md`
- [S7] `discovery/10-critical-inheritance-geoguessr-core.md`

### External / Official Sources

- [E1] Google Maps Platform, Street View Static API metadata and request docs: <https://developers.google.com/maps/documentation/streetview/metadata>, <https://developers.google.com/maps/documentation/streetview/request-streetview>
- [E2] Google Maps Platform, Street View usage and billing: <https://developers.google.com/maps/documentation/streetview/usage-and-billing>
- [E3] Google Maps Platform, Street View policies: <https://developers.google.com/maps/documentation/streetview/policies>
- [E4] PartyKit docs, "How PartyKit works": <https://docs.partykit.io/how-partykit-works/>
- [E5] PartyKit docs, persisting room state: <https://docs.partykit.io/guides/persisting-state-into-storage/>
- [E6] Colyseus docs, room reconnection: <https://docs.colyseus.io/room/reconnection>
- [E7] Colyseus docs, room/state patterns: <https://docs.colyseus.io/state>
