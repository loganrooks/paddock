---
date: 2026-04-13
lane: j-f
lane_name: "Real-time sync / authority follow-up"
orientation: exploratory
delegation_class: replanning-revision-gap-filling
---

# Lane J-F: Real-Time Sync / Authority Follow-up

## Lane framing

This follow-up narrows the first-pass lane-j research to concrete synchronization and authority mechanics.

The emphasis here is not "what room sizes do products advertise." It is:

- what authority model is exposed
- what synchronization model is exposed
- what exact mechanisms are described for prediction, rollback, replication, filtering, prioritization, buffering, and resimulation
- what tradeoffs the sources admit directly

The evidence hierarchy from lane-j is kept explicit:

1. official engine docs and official engineering writeups
2. official talks / slide decks
3. classic but credible technical references, clearly marked as secondary

High-confidence conclusion up front:

- the strongest primary-source pattern is still server-authoritative state with aggressive filtering, prioritization, buffering, and selective client prediction
- rollback is very real, but the strongest direct material here places it in tightly scoped, deterministic, input-centric contexts rather than as the default answer for every real-time mode
- for Prix Guesser, the most reusable mechanisms look much more like per-client visibility control, update prioritization, small prediction windows, and explicit local-vs-remote state handling than like full fighter-style rollback

## Reference cases and source audit

| Reference case | Source type | Reliability | What the source directly exposes | What it does not expose | Direct vs inferred |
| --- | --- | --- | --- | --- | --- |
| [Unreal networking overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine?application_version=5.6), [Replication Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/replication-graph?application_version=4.27), [Migrate to Iris](https://dev.epicgames.com/documentation/en-us/unreal-engine/migrate-to-iris-in-unreal-engine?application_version=5.6), [FastArray delta serialization](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/NetCore/Net/Serialization/FFastArraySerializer/FastArrayDeltaSe-) | `1` official engine docs | High | server-authoritative actor replication; remote proxies; relevancy, priority, dormancy, delta serialization, RepGraph node-based scaling, Iris filters/prioritizers, push-vs-poll behavior | Fortnite-specific heuristics and exact game-side replication policy | mostly direct; using these mechanisms as likely precedents for large shared worlds is mild inference |
| [Riot: Peeking into VALORANT's Netcode](https://www.riotgames.com/en/news/peeking-valorants-netcode), [VALORANT's 128-Tick Servers](https://www.riotgames.com/en/news/valorants-128-tick-servers), [Demolishing Wallhacks with VALORANT's Fog of War](https://www.riotgames.com/en/news/demolishing-wallhacks-valorants-fog-war) | `1` official engineering blogs | High | server-authoritative client/server model; client prediction; minimal buffering targets; rewind-based hit registration; bounded lag compensation; CPU/frame-budget pressure; server-side visibility withholding with PVS-based filtering | exact full game protocol and all serialization details | direct for the main mechanisms and goals |
| [Overwatch: Networking Scripted Weapons and Abilities](https://media.gdcvault.com/gdc2017/Presentations/Reed_Dan_NetworkingScriptedWeapons.pdf), [GDC session page](https://www.gdcvault.com/play/1024653/Networking-Scripted-Weapons-and-Abilities) | `2` official slide deck + official talk page | High | server-authoritative scripted gameplay; command-frame deltas; acknowledgement-driven packet retention; local prediction; rollback/replicate/simulate loop; selective remote sync | whole-engine topology outside the scripted gameplay layer; exact transport implementation | direct for the mechanics on the slides |
| [Overwatch Gameplay Architecture and Netcode session page](https://dev.gdcvault.com/play/1024001/-Overwatch-Gameplay-Architecture-and) | `2` official talk page | Medium-High | Blizzard explicitly says the networked simulation leverages determinism for responsiveness and precision | detailed mechanics are not visible from the session page alone | direct for the determinism claim; thin otherwise |
| [GGPO official site](https://www.ggpo.net/), [GGPO README](https://github.com/pond3r/ggpo), [GGPO API header](https://raw.githubusercontent.com/pond3r/ggpo/master/src/include/ggponet.h) | `1` official SDK site + official code/docs | High for SDK requirements | rollback networking via input prediction and speculative execution; save/load whole game state; rollback callbacks; time-sync events; prediction limits; spectator support | large-room scaling, complex relevance filtering, and rich server-authoritative room orchestration | direct for rollback SDK expectations |
| [Gaffer on Games: What Every Programmer Needs To Know About Game Networking](https://gafferongames.com/post/what_every_programmer_needs_to_know_about_game_networking/), [Snapshot Interpolation](https://www.gafferongames.com/post/snapshot_interpolation/), [State Synchronization](https://www.gafferongames.com/post/state_synchronization/), [Networked Physics (2004)](https://www.gafferongames.com/post/networked_physics_2004/) | `4` credible secondary technical analysis | Medium-High | clean articulation of lockstep vs client/server vs snapshots vs state sync; jitter buffers; interpolation buffers; priority accumulators; quantize-both-sides technique; client-side prediction with authoritative server physics | not an official product postmortem | direct for the described models, but still secondary |

## Concrete synchronization / authority mechanisms exposed

### 1. Unreal exposes a server-authoritative replication stack built around per-client filtering and prioritization

Directly exposed by Epic's docs:

- Unreal's default model is server-authoritative: the server holds the true game state, and clients render remote proxies.
- Replicated actors spawn authoritative server instances plus remote client proxies; replicated properties and movement flow from authority to proxies.
- Relevancy culls actors that are not worth sending to a client.
- Priority decides which relevant actors replicate first under bandwidth pressure, and actors that miss replication gain urgency over time.
- Dormancy removes actors from the active replication list until they need to wake up again.
- `Replication Graph` exists specifically to avoid each actor evaluating every client individually. Epic's own example cites Fortnite battle royale starting with `100 connected players` and roughly `50,000 replicated Actors`.
- RepGraph's core pattern is persistent, reusable node state: spatial groups, always-relevant groups, and other actor buckets that let the server share work across frames and clients.
- Iris keeps the server-authoritative model but changes the scaling surface: Epic says RepGraph nodes are replaced by network object filters and prioritizers, and Iris aims to be push-based, falling back to polling by `NetUpdateFrequency` when needed.
- `FastArrayDeltaSerialize` exposes an explicit tradeoff: the standard path is less CPU-intensive but uses more bandwidth.

What problem this solves:

- the `actors x clients x frame` explosion that makes naive authoritative replication too expensive
- keeping the server authoritative without sending every object to every client at the same rate
- preserving client experience without simply lowering update rate everywhere

Relevant direct takeaways:

- the useful seam is not "copy Unreal"
- the useful seam is "treat visibility, priority, dormancy, and wake-up as first-class synchronization concepts"

### 2. VALORANT exposes a very explicit server-authoritative model with local prediction, rewind hit-reg, and server-side visibility withholding

Directly exposed by Riot:

- Riot states that VALORANT uses a server-authoritative networking model and that the server must never trust the client's view of the world.
- Local movement is predicted on the client for responsiveness instead of waiting a round trip.
- Riot targets minimal buffering, stating it aimed for roughly one buffered frame of movement data on clients and about half a frame on servers.
- Riot ties 128-tick servers directly to defender reaction-time goals and competitive fairness.
- Riot's 128-tick engineering article gives the server budget shape very concretely: at `128 Hz`, the frame is `7.8125ms`; at `3 games per core` plus overhead, the effective target budget fell to about `2.34ms` per frame.
- Hit registration is rewind-based: Riot says the server stores historical player positions and animation state, then rewinds to the shot time when a shot packet arrives.
- Riot also states that rewind is bounded. It explicitly notes that without limits, a `500ms` player could kill someone long after they had reached cover.
- Fog of War is an information-filtering mechanism, not just anti-cheat marketing. Riot says the server withholds enemy position information until a client needs it, then describes a shift from repeated raycasts to server-side occlusion culling using precomputed potentially visible sets.
- Riot also says the first Fog of War prototype could drag server frame times from `128 tick` behavior back toward `64 tick`, while the optimized system dropped to under `2%` of server frame time from about `50%` in the prototype.
- The Fog of War article also exposes a practical optimistic-filtering trick: look ahead using actor velocity so information arrives just before line-of-sight would matter, reducing pop-in.

What problem this solves:

- cheating pressure against any client-trusted system
- responsiveness under nonzero RTT
- peekers advantage and hit registration under low time-to-kill
- hidden-information leakage
- server CPU collapse from per-player visibility checks

Important detail:

- Riot is not exposing a generic "real-time multiplayer recipe"
- Riot is exposing a very expensive fairness stack tuned for a precision shooter: authoritative simulation, local self-prediction, historical rewind, bounded lag compensation, and aggressive per-client information withholding

### 3. Overwatch exposes a command-frame replication model with local rollback/replicate/simulate for authoritative scripted gameplay

Directly exposed by Blizzard's slide deck:

- Statescript is explicitly server-authoritative.
- Communication is mostly server-to-client; button input and aim go client-to-server.
- Gameplay scripts are split into synchronized instances and unsynchronized instances.
- The server loop for synchronized gameplay is clear:
  gather client input -> simulate -> store changes in `StatescriptDeltas` -> send deltas to clients
- Each delta is tagged to a command frame and can include creation/destruction flags, changed variables, changed states, and executed actions.
- Deltas are retained until clients acknowledge the relevant command frame.
- Packets union delta ranges together, serialize the current values referenced by that union, and are stored/reused until acknowledged.
- On the client side, the local entity stores input and predictions.
- When a packet arrives, the client acknowledges it, ignores redundant or out-of-order packets, and then:
  - for remote entities: replicate
  - for local entities: rollback -> replicate -> simulate forward
- Blizzard also exposes the historical-data boundary for local prediction: local entities retain button input, aim, local variables/states, and positions/poses for all entities; some remote-only or other component data is not historical.
- Efficiency is selective rather than uniform. Blizzard says remote entities do not simulate Statescript instances, and remote packets only need the states/actions/variables that those remote instances care about.

What problem this solves:

- letting designers author high-level ability logic without manually hand-writing networking logic for each ability
- keeping authoritative truth while preserving local responsiveness
- avoiding sending the full synchronized script state to every remote client
- retaining enough history to repair mispredictions

Important limit:

- this is not a generic public writeup of all Overwatch netcode
- it is a highly useful, very concrete slice of how authoritative scripted gameplay is synchronized

### 4. GGPO exposes rollback as an SDK contract, and the contract is demanding

Directly exposed by official GGPO materials:

- GGPO describes itself as a rollback networking SDK for peer-to-peer games.
- Its official README says rollback networking uses input prediction and speculative execution so local inputs can be applied immediately.
- The public API makes the implementation burden explicit:
  - the game must save the entire game state
  - the game must load a previously saved state at the start of a rollback
  - the game must advance exactly one frame during rollback processing
- The API surface also exposes operational guardrails:
  - `GGPO_MAX_PREDICTION_FRAMES` is `8`
  - there is a `PREDICTION_THRESHOLD` error code
  - there is an explicit `TIMESYNC` event used when one client runs too far ahead
  - spectator support exists, but as a bounded secondary path

What problem this solves:

- hiding round-trip latency for small, twitchy, deterministic or near-deterministic input-driven games
- preserving offline-like input feel online

Important limit:

- GGPO's public material is strong on rollback mechanics and weak on large-room authority/orchestration patterns
- it is best read here as the clearest official expression of rollback's actual implementation demands, not as evidence that rollback is broadly suitable for room-centric party systems

### 5. Gaffer gives the clearest secondary taxonomy for when different sync models break down

This is secondary, but still useful because it is explicit about the mechanics:

- deterministic lockstep:
  - every peer waits for the most lagged player's commands before simulating
  - works when commands are tiny and full state is too expensive to exchange
  - badly resists late join and fast-response action play
- snapshot interpolation:
  - buffer snapshots before rendering
  - tolerate loss/jitter by interpolating between buffered states instead of waiting for retransmit
  - add visible delay in exchange for smoothness
- state synchronization:
  - both sides simulate
  - sender uses priority accumulation to decide which objects get state budget
  - receiver uses a jitter buffer
  - both sides quantize simulation state to reduce divergence and visible pops
- networked physics with authoritative server + client prediction:
  - the client predicts locally from input
  - the server remains authoritative for simulation
  - the protocol must accept the latest input/state without waiting for lost packets to be resent

What problem this solves:

- separating models that are often sloppily collapsed into "real-time multiplayer"
- showing that interpolation, prediction, rollback, and state sync are different tools for different failure modes

## Concrete tradeoffs and limits

### Authority vs responsiveness

- Server authority is the strongest anti-cheat and consistency posture in this source set.
- The cost is constant mitigation work around latency:
  prediction, buffering, correction, rewind windows, historical state, and selective trust boundaries.
- Riot and Overwatch both show that authoritative truth by itself is not enough; you still need explicit local responsiveness paths.

### Filtering vs correctness

- Unreal and Riot both show that per-client filtering is essential once shared state grows.
- The cost is correctness risk:
  stale visibility, pop-in, wrong pose data, or missed wake-up events if filtering is too aggressive.
- Riot's Fog of War article makes this concrete: optimistic look-ahead and generous visibility tests were needed to avoid late reveals and broken pose/hit-reg bugs.

### Rollback vs implementation burden

- GGPO makes rollback's real cost visible: deterministic resimulation, full save/load state hooks, prediction limits, timesync, and frame-by-frame rollback execution.
- Overwatch also shows rollback in a narrower authoritative-client context, but again with command frames, history retention, and explicit repair loops.
- This is not lightweight plumbing. It wants a simulation that can be rewound and replayed cleanly.

### Smoothing vs input delay

- Snapshot interpolation and jitter buffers smooth motion under packet clumping and loss.
- The cost is added presentation delay.
- Riot's position is almost the opposite extreme: minimize buffers because even small timing deltas matter competitively.
- That means the right answer is mode-dependent, not universal.

### CPU vs bandwidth

- Unreal's fast-array docs expose one explicit knob: use more bandwidth to save CPU.
- Unreal RepGraph/Iris and Riot's 128-tick/Fog-of-War material both show the same broader truth:
  scaling real-time sync is often a CPU problem before it is a raw socket problem.
- Prix Guesser should not assume "low player count" automatically means no real-time cost concerns if a mode ever adds many moving entities, per-client visibility, or rewind history.

### What the public sources still do not expose well

- commodity browser transport behavior for these exact mechanisms
- how racing titles like Trackmania or iRacing implement low-level prediction/correction internally
- how far server-authoritative interest management can be simplified before visible quality breaks in phone-controller party contexts

## What seems relevant to Prix Guesser

### Highest-confidence relevant patterns

- Preserve an explicit authoritative room-state seam.
  Even if the eventual authority is a lightweight host or room server rather than a large dedicated fleet, the source set strongly favors one authority deciding truth and then distributing client-specific views.

- Preserve per-client visibility/filtering as a first-class concept.
  This matters for:
  - private phone information
  - spectator vs player views
  - host-screen vs controller-screen asymmetry
  - hidden clues or role-gated data
  - future anti-cheat hardening if any competitive real-time mode appears

- Preserve update classes and priority classes.
  Unreal and Overwatch both suggest a clean future seam between:
  - must-be-immediate state
  - important but lower-frequency state
  - dormant / wake-on-demand state

- If a future action mode needs local feel, start with narrow self-prediction, not full rollback.
  The strongest reusable lesson from Riot is not "build shooter netcode." It is:
  predict only what the local player must feel instantly, keep the server authoritative, and keep the repair loop explicit.

### Likely relevant for modest action branches

- A short history buffer could matter if a mode ever needs authoritative late resolution for:
  - projectile or tag timing
  - overlap/trigger disputes
  - reconciliation after brief packet loss

- Local-vs-remote entity treatment looks reusable.
  Overwatch's split between locally predicted entities and remotely replicated entities is a stronger fit for Prix Guesser than all-entity rollback.

- Selective remote synchronization looks very relevant.
  Overwatch only sends remote clients what those remote instances care about. That general idea maps well to phone-controller party play.

### Probably overkill for the likely near-term product

- full GGPO-style rollback for the whole room simulation
- 128-tick shooter-grade rewind and pose history
- map-wide PVS/occlusion systems unless a future mode becomes genuinely avatar-dense and line-of-sight sensitive
- deterministic whole-sim lockstep outside very narrow, input-only minigames

### Practical translation for plausible Prix Guesser action modes

- For clue-heavy or host-screen action variants:
  authoritative room state + per-client filtered state + sparse local feedback is probably enough.

- For light competitive dexterity variants:
  self-prediction plus authoritative correction may be justified for the active player only.

- For anything like shared-contact vehicle chaos:
  the source set does not justify jumping straight to rollback-heavy netcode. A simpler authoritative or ghosted/no-contact design would likely be a much safer first branch.

## What remains uncertain

- Whether Prix Guesser should use dedicated-server authority, listen-server authority, or a hybrid room host for future real-time modes.
  The source set helps with mechanism choice, not deployment choice.

- How much prediction a browser-first or phone-controller stack actually needs in practice.
  Shooter and engine sources prove the mechanics; they do not prove the threshold at which Prix Guesser would need them.

- Whether any future action mode would involve enough simultaneous moving, colliding entities to justify spatial interest management beyond simple role/view filtering.

- How far hidden-information filtering should go.
  Riot shows an extreme anti-cheat posture. Prix Guesser may only need view separation for private information, not full server-side occlusion logic.

- Whether a very narrow rollback island could still be useful.
  Example: a tiny two-player deterministic reflex microgame embedded inside a broader room-authoritative shell. The current evidence says "possible," but not "default."

- The biggest missing public-primary gap remains racing-specific low-level sync internals.
  Official Trackmania and iRacing materials exposed room structure and participation shaping much better than prediction/correction/rollback internals.
