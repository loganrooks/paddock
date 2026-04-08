# Reference Designs

## Lane A Memo

Research refresh date: 2026-04-08

Frame for this pass:
- private-only fan project
- personal use
- do not optimize around publication-safe constraints
- stay exploratory rather than converging on one product shape

This changes the read of the comps. The question here is not "what is safest to ship publicly?" It is "what creates the strongest play, watchability, fan delight, and mode expansion headroom if legal publishing constraints are temporarily set aside?"

## Comparable Products

### GeoGuessr

- Product + link: [GeoGuessr](https://www.geoguessr.com/)
- Core loop: Drop the player into a street view panorama, let them hunt for clues, and score the guess by distance from the real location. The official homepage also foregrounds private parties, competitive play, tournaments, events, daily challenge, and streak-like variants.
- Strongest pattern worth borrowing: one clue substrate, many wrappers. GeoGuessr gets a lot of mileage from reusing the same base interaction across solo play, private rooms, ranked competition, and daily ritual.
- What it does badly or leaves open: the base loop can become solitary, slow, and mechanically repetitive. Street View fluency can dominate over theme-specific knowledge, and the game often rewards general geolocation craft more than domain fandom.
- Direction it suggests for an F1-flavored version: keep the precision and scoring drama of "place the pin," but do not stop at a pure location clone. Build one strong clue substrate and then wrap it in private party, duel, streak, and daily variants tuned for F1-specific knowledge.

### City Guesser

- Product + link: [City Guesser](https://cityguesser.eu/)
- Core loop: Show a moving video of a real place, ask players to infer the location from motion, signage, architecture, and atmosphere, then score by map accuracy. Official pages emphasize private rooms, social play, no-account access, and a rebuilt version with better mobile support and 250-player rooms.
- Strongest pattern worth borrowing: motion creates watchability. Video makes the game feel alive in a way static panoramas often do not, which matters a lot for party energy and spectator appeal.
- What it does badly or leaves open: content quality can vary, precision can suffer versus Street View, and the format is strongly biased toward urban or tourism-friendly footage. It is also more dependent on curating strong clips than strong maps.
- Direction it suggests for an F1-flavored version: lean into moving clue media for room play. Think fan-walk footage, metro-to-circuit approaches, marina or harbor movement, airport arrivals, grandstand ambience, or a simulated broadcast-camera drift around recognizable venue features.

### GeoTastic

- Product + link: [GeoTastic](https://geotastic.net/)
- Core loop: Official product materials and UI strings show a free crowdfunded multiplayer geo quiz app with singleplayer and multiplayer entry points, plus highscore hunts, challenges, streak hunts, pinpointing, country battle, distance battle, flag battle, satellite cityscape, popular landmarks, and fun-with-flags style variants.
- Strongest pattern worth borrowing: mode breadth on top of a shared foundation. GeoTastic feels less like one game and more like a geo-quiz toolbox, which is useful when the audience ranges from hardcore solvers to friend groups who want lighter rounds.
- What it does badly or leaves open: the mode surface can sprawl. This broadens replayability, but it can also blur the product's identity and make the front door less legible than GeoGuessr's cleaner pitch.
- Direction it suggests for an F1-flavored version: use this as a model for expansion, not for the initial hook. An F1 version could eventually support weekend pinpointing, circuit recognition, flag/team battles, satellite paddock hunts, and trivia hybrids, but the anchor needs to stay crisp.

### TimeGuessr

- Product + link: [TimeGuessr](https://timeguessr.com/)
- Core loop: Guess where and when a historic photo was taken. Official copy describes it as a game testing both geography and history knowledge, and the live settings page shows timer options plus a "challenge a friend" flow.
- Strongest pattern worth borrowing: one artifact can power two intertwined deductions. The date and place hypotheses reinforce each other, which is a strong pattern for expert-fandom games where era knowledge matters.
- What it does badly or leaves open: static-photo play is usually less watchable than moving or explorable media, and time scoring can feel secondary unless the date clue is deeply integrated into the fiction of the round.
- Direction it suggests for an F1-flavored version: combine venue recognition with era recognition. Ask players to infer not just "which grand prix?" but "which year, session type, or rules era?" from one clue package. This opens a strong lane for deep-fandom memory play.

### GeoGrid

- Product + link: [GeoGrid](https://www.geogridgame.com/)
- Core loop: Fill a daily geography grid by naming a country that satisfies both the row and column constraints. Official FAQ text says lower score is better because rarer answers score better, and official UI strings show achievements and daily streak structures.
- Strongest pattern worth borrowing: combinatorial deduction plus rarity scoring. The grid does not just ask for correctness; it asks for stylish correctness and deep catalog knowledge.
- What it does badly or leaves open: this is a brilliant daily ritual but a weak centerpiece for a live room. It is clever, not cinematic. The fun is in constraint solving and bragging rights more than spectacle.
- Direction it suggests for an F1-flavored version: make this a side mode or daily companion. A grid crossing driver, team, circuit, era, weather, nationality, and incident categories could be excellent for expert players, especially if rarity scoring stays intact.

### Worldle

- Product + link: [Worldle](https://worldle.teuteuf.fr/)
- Core loop: Show a country silhouette, then let the player iterate within six guesses using direction, distance, and proximity clues. The official FAQ is explicit and mechanically clean about how the clue language works.
- Strongest pattern worth borrowing: radical compression. Worldle proves that a tiny input surface and a deterministic clue grammar can still produce a strong daily habit loop.
- What it does badly or leaves open: there is little social theatre, little audiovisual identity, and relatively little room for deep thematic texture.
- Direction it suggests for an F1-flavored version: use this pattern for ultra-light daily modes. Circuit silhouette, sector shape, or partial-outline guessing could work well as a quick companion mode alongside a richer main game.

### Seterra

- Product + link: [Seterra](https://www.seterra.com/)
- Core loop: Browse from a large library of map quizzes and practice specific geography domains such as countries, capitals, rivers, flags, cities, and regions. The official homepage leans into breadth, teaching utility, and repeatable practice.
- Strongest pattern worth borrowing: taxonomy and mastery scaffolding. Seterra is good at making a giant body of content feel traversable and learnable rather than amorphous.
- What it does badly or leaves open: it reads more like a study tool than a party game. The loop is useful and sticky, but it does not carry much room-energy on its own.
- Direction it suggests for an F1-flavored version: build a strong training layer around the party product. Circuit packs, host-city packs, calendar-era packs, flag packs, corner-name packs, and paddock-language drills could help expert and non-expert players coexist.

## Cross-Product Patterns Worth Stealing

### 1. One Core Substrate, Multiple Shells

GeoGuessr and GeoTastic both show the value of building one reliable clue-and-guess loop and then expressing it as:
- solo practice
- private party
- head-to-head duel
- streak mode
- daily ritual

For an F1 version, this argues for a reusable clue engine rather than one-off modes built from scratch.

### 2. Motion Beats Static For Social Play

City Guesser's big lesson is that moving media produces a room-readable experience. Even if the main mode includes stills or maps, the party-facing modes probably benefit from motion, transitions, and reveal pacing that feel closer to live sport than to a quiz database.

### 3. Time Is A Powerful Second Axis

TimeGuessr is the strongest signal that "where?" is not enough for a fandom product. F1 fans often recognize places through era markers:
- runoff style
- pit building design
- sponsor palette
- night-race lighting
- halo or pre-halo cars
- podium or parc ferme aesthetics

A private-use version can lean harder into exact era clues than a cautious public-first design would.

### 4. Daily Compact Modes Are Useful, But Not A Substitute For The Main Event

GeoGrid and Worldle are excellent evidence that daily ritual matters, but they feel like support structures, not the whole fantasy. They suggest companion modes, warm-up modes, and retention hooks more than the full identity of the product.

### 5. Practice And Party Can Coexist If The Product Admits Both

Seterra is useful because it reminds us that not every player wants the same thing at the same time. There is room for:
- a serious solo mastery lane
- a room-first spectacle lane
- a low-friction daily lane

The mistake would be pretending one of those automatically covers the others.

## Open Directions For An F1-Flavored Version

None of these should be treated as the answer yet. They are viable directions opened up by the comps.

### Direction A: GeoGuessr But Sport-Specific

Keep the central map-pin precision loop, but feed it F1-flavored clues:
- circuit adjacency
- host-city landmarks
- transport approaches
- terrain and weather
- recognizable venue infrastructure

Best if the goal is a clean hook and clear scoring drama.

### Direction B: City Guesser For Race Weekend Atmosphere

Bias toward moving, watchable clue media:
- fan arrival walks
- neighborhood approach shots
- skyline and waterfront motion
- transit cues
- circuit perimeter footage

Best if the goal is couch play, spectatorship, and room energy.

### Direction C: TimeGuessr For F1 Memory Nerds

Make rounds ask for both place and era:
- which venue
- which year or rules era
- which session type
- maybe which race-weekend context

Best if the goal is deep-fandom delight rather than broad onboarding.

### Direction D: GeoGrid Sidecar For Daily Expert Flexing

Use a compact grid format for daily return:
- driver x circuit
- team x weather condition
- era x country
- winner x venue trait

Best as a companion mode, not the flagship.

### Direction E: Seterra-Like Training Layer

Give the product a practice spine:
- circuit packs
- host country and city packs
- calendar-by-era packs
- corner and sector drills
- flag, team, or livery recognition

Best if the product wants to support both experts and friends who are learning.

## Current Take

The comps do not point to one obvious answer. They point to a promising shape:
- a precise clue-to-map core like GeoGuessr
- a watchable media layer like City Guesser
- an era-memory axis like TimeGuessr
- compact daily side modes like GeoGrid or Worldle
- a training shell like Seterra

For a private-only fan project, the most interesting opportunity may be to combine higher-fidelity F1-specific clue types than a publication-safe version would tolerate:
- real circuit outlines
- exact grand prix names
- year-specific venue states
- broadcast-like reveal cadence
- team and sponsor era texture

That does not mean all of this belongs in v1. It means the design space is richer than "GeoGuessr clone, but F1."
