---
date: 2026-04-12
lane: a
lane_name: "Authored prompt / reveal"
delegation_class: execution/verification
output_file: 02-lanes/round-1/lane-a-output.md
audit_subject: lane-a-authored-prompt-reveal
audit_orientation: exploratory
audit_delegation: self
scope: "Lane A for Round 1 of the game-modes exploratory audit: authored prompt / reveal family, focused on Words of Wisdom and Sound-based Games"
auditor_model: gpt-5.4
triggered_by: "pilot dispatch for Round 1, Lane A only"
task_spec: "lane spec provided in user prompt"
root_task_spec: 01-round-1/game-modes-r1-task-spec.md
ground_rules: "exploratory-root+context-plurality+virality-vs-retention+user-signal"
tags:
  - exploratory-audit
  - round-1
  - lane-a
  - authored-prompt
  - reveal
---

# Lane A: Authored Prompt / Reveal

## Lane framing

This lane is running under the Round 1 root instruction to treat mode entries as "possibility families" rather than fixed pitches, to avoid a single ideal context, and to keep virality distinct from retention (`.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md:97-126`). The source corpus also explicitly warns that these documents are speculative scratchpads and that `designed` means "clear enough for feasibility/substrate analysis," not "ready to build" (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-INDEX.md:3-16`).

Lane A is internally uneven. `Words of Wisdom` is the only entry here already marked `designed (core mechanic)` and also carries the strongest user-engagement signal in the set (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:7-18`). `Sound-based Games` is still a seed bundle of three sub-ideas with open sourcing and distinctiveness questions (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:353-366`). That asymmetry matters: this lane is less "two competing modes" than "one real mode family plus one promising but not-yet-shaped frontier."

The initiating question for this lane was: in authored prompt / reveal play, what actually carries the fun? The checkpoint material says the key move in this exploration was from trivia toward "cultural fluency," especially radio culture, and that the best candidates were the ones with a social mechanic F1 fans already perform informally (`.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:12-32`). I therefore read the conditional radio catalog, research todo file, and architecture notes as part of this lane, because depth, deferred research, and reveal-structure pressure all materially affect the judgment (`.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md:90-93`).

## What is already strong

- `Words of Wisdom` already has a closed core loop: show the actual preceding radio message, have everyone write a fake continuation, shuffle the real answer with the fakes, then vote. The mode's own writeup says replayability comes from "friends' fakes, not memorizing answers," and the checkpoint deep dive reinforces that this was the explicit fix for the one-joke exhaustion problem (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:13-19`; `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:50-82`).

- `Words of Wisdom` has more than premise depth. It has a 347-transcript sourcing pipeline, a resumable extraction workflow, and a 50-moment exploratory catalog with tiering based on how "unguessable" or guessable the real line is (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:27-29`; `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:84-103`; `.planning/explore/2026-04-11-product-vision-game-design/words-of-wisdom-radio-catalog.md:13-18`). That does not make it finished, but it does mean this lane has at least one entry where the content engine is already being treated concretely.

- The best version of `Words of Wisdom` is not just "Fibbage with F1 nouns." The checkpoint says the exploration reframed the design question from fact quiz to "the bonding ritual of quoting radio at each other into structured play" (`.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:14-18`). That is a stronger lane identity than a generic clip quiz because it connects reveal satisfaction to tone, social recognition, and player performance rather than mere recall.

- This lane inherits a strong accessibility advantage. The cross-cutting notes state that creative/non-trivia formats are naturally mixed-skill friendly because they ask for humor, opinion, or performance rather than encyclopedic recall (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:60-65`). `Words of Wisdom` is the clearest expression of that principle in the current corpus.

- `Sound-based Games` is thin as a family, but there is one concrete promising wedge already visible: commentary and crowd-reaction identification feel more mode-like than engine identification. The checkpoint explicitly says commentary clips are strong because commentary has its own meme layer, and it already proposes crowd-reaction rounds as a simpler, more feasible variant (`.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:111-120`). That is enough to keep the lane alive without pretending the whole family is equally mature.

- This lane also plugs naturally into the broader platform scaffolds. Circuit packs can bundle venue-specific radio, commentary, and crowd moments under one circuit identity, while the calendar layer can keep both `Words of Wisdom` and audio modes fresh around live race weekends (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md:7-21,25-38`).

## What is weak / thin / generic

- `Sound-based Games` is still a bundle of prompts, not a designed game family. The current doc lists three sub-ideas, then immediately notes that sourcing, browser playback, and legal posture all remain open and that the family is "probably sequenced after text-content modes" (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:359-366`). There is no settled round flow, no scoring grammar, and no social mechanic yet.

- Engine identification is the thinnest branch. The underlying question of whether modern cars sound distinct enough for play is not a polish issue; it is the mechanic's foundation, and it already has its own research ticket asking whether the concept is even acoustically viable (`.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md:24-27`). Right now it is a cool fantasy more than a durable mode.

- `Words of Wisdom` has a strong core but a weak perimeter. The current writeup names `one-liner identification`, `phrase-first`, and "Fibbage variants of each" as seeds, and the checkpoint explicitly says these were not fully designed yet (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:20-25`; `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:73-82`). So the family is strong at its center and still fuzzy about how much variety it can carry without collapsing back into quiz filler.

- `Words of Wisdom` is more dependent on authored content quality than some other player-generated modes. The catalog's tier system exists because not every memorable radio line is good Fibbage material; some are "unguessable," some are only good as warm-up or knowledge reward rounds (`.planning/explore/2026-04-11-product-vision-game-design/words-of-wisdom-radio-catalog.md:13-18`). That means the mode's engine is hybrid: social performance matters, but bad curation still weakens the room.

- Async fit is real but unstable. The architecture notes say `Words of Wisdom` can work async as "submit your fake, come back to vote when everyone's ready," while fashion has a similar async-creation / sync-reveal split (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:42-50`). That keeps the mode alive across contexts, but it also exposes the tension: if the reveal is delayed too long, the shared "room laugh" turns into mailbox cleanup.

- The lane is at risk of genericity whenever it reduces itself to "identify the clip." Commentary clip ID and crowd-reaction ID are promising because the audio itself has culture and energy; engine ID risks becoming a narrow sensory trivia test unless it gains a stronger social or staged-reveal structure.

## Variant forks and possibility expansion

- `Words of Wisdom` should stay alive as at least three forks, not one. First: the social Fibbage core already described in the docs. Second: reverse-context rounds such as `phrase-first`, where the line drops first and the group reconstructs the setup. Third: an audio-enhanced reveal version where the room writes from text but the reveal lands through the actual voice, which the checkpoint calls out as transformative (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:29`; `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:172-178`).

- `Words of Wisdom` has obvious authored-pack expansion surfaces. The cross-cutting `era as content dimension` note makes 1990s radio, post-hybrid radio, wet-weather meltdowns, Ferrari strategy packs, or engineer-banters-as-a-subgenre all feel natural rather than bolted on (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:9-13`). This lane already wants editorial curation, and eras give that curation a durable spine.

- There is a cleaner trivia-like fork for `Words of Wisdom`, but it should be treated as a side branch, not the flagship. One-liner ID can work as a warm-up or bonus round, especially because the catalog already distinguishes warm-up-tier material from main-event Fibbage material (`.planning/explore/2026-04-11-product-vision-game-design/words-of-wisdom-radio-catalog.md:15-18`). Central synthesis should not mistake that side branch for the family center.

- There is also a stronger performance fork available than the docs currently name: after the reveal, let players briefly pitch or defend why their fake line should have been the real one. That is not in the current writeup, but it follows directly from the checkpoint's move from trivia to cultural performance and from the general "performance / reveal" taxonomy the exploration already mapped (`.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:20-30`).

- `Sound-based Games` should probably split into separate live options rather than remain one bag. `Commentator clip ID` and `crowd reaction ID` belong together as "event recognition" audio games. `Engine identification` is a different beast with a different research dependency and likely a different social ceiling (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:359-366`; `.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md:24-27`).

- The most promising sound fork is probably not pure identification but progressive reveal. Very short audio snippet, lock in a guess or confidence level, then reveal a longer slice, then the full answer. That keeps the reveal dramatic instead of flat and gives the family a tuning knob for mixed-knowledge groups. This is an inference from the lane evidence rather than an explicit source claim, but it is responsive to the root spec's demand for hidden variants and tuning knobs (`.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md:153-168`).

- A stronger cross-lane hybrid is already implied: "audio WoW." The checkpoint explicitly frames commentary and radio audio as part of the same cultural surface and argues that actual radio audio would transform the WoW reveal (`.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:172-178`). That suggests the sound family may be more valuable as an enhancement layer or submode generator for `Words of Wisdom` than as a standalone ranked portfolio item.

## Context profile / tensions

- Mixed-knowledge couch group: `Words of Wisdom` is the strongest fit in this lane because the cross-cutting accessibility principle directly applies and because the room gets both text entry and shared reveal spectacle (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:60-65`; `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:42-44`). Commentary and crowd-reaction rounds can work as quick punchy interstitials. Engine ID is the weakest fit because it privileges narrow sensory expertise and has less room for player creativity.

- Remote Discord group: `Words of Wisdom` survives well in synchronous remote play because the architecture already imagines each player seeing the setup and reveal on their own device (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:44-45`). The mode loses some couch-laugh immediacy but not its structure. Sound rounds also survive, but they depend more on reliable synchronized playback and the group already having voice chat or stream audio in place.

- Solo fan between race weekends: this is where the lane splits hardest. `Words of Wisdom` core loses its main engine when the "friends' fakes" disappear (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:69-74`). Sound rounds, especially crowd/commentary daily challenges, fit solo async much better because quick recognition tasks scale down cleanly. Solo `Words of Wisdom` probably only works as an authored challenge derivative, not as the main family form.

- Watch-party crowd: this lane is unusually strong here. The handoff explicitly asks what streamer/spectator integration would make the platform watchable, and the architecture notes already define local WoW around a shared spectacle screen (`.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md:108-114`; `.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:42-44`). Commentary clips, crowd roars, and radio reveals all make sense in a room where some people are more audience than active player.

- Recurring friend group with inside jokes/history: `Words of Wisdom` is the lane's clearest winner because the platform notes already imagine group-scoped identity and shareable cards around "who writes the funniest fakes" (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md:202-218`). Sound rounds can contribute, but they do not yet have the same built-in memory-making engine.

- The main tension is not local vs remote. It is synchronous room-energy vs delayed reveal. The root spec says not to universalize every mode across all contexts (`.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md:111-126,232-240`). This lane shows why: `Words of Wisdom` can plausibly fork into local/sync party play and async derivatives, but the same design should not pretend both preserve the same kind of fun.

## Virality vs replayability

- `Words of Wisdom` has both. Its clip/share value comes from absurd real lines and from the funniest player-authored fakes. Its replay value comes from a structural social loop the cross-cutting notes describe plainly: "your friends are the content" (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:69-74`). That makes it stronger than a pure quote-recognition mode because the same prompt plays differently with every group.

- The lane's strongest viral upgrade is audio reveal. The docs already say actual audio would turn text setup into a "party moment" (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-game-modes.md:29`; `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:176-178`). That is clip fuel. But audio reveal is not the replay engine; player-authored variation and fresh packs are.

- The current cross-cutting formula is especially useful here: virality hooks, return loops, retention architecture are not the same thing (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-cross-cutting.md:34-56`). `Words of Wisdom` already has all three in embryonic form: outrageous lines, repeatable social fabrication, and a path to editorial freshness through circuit packs and race-weekend cadence.

- `Sound-based Games` currently skews the other way. Commentary and crowd-reaction rounds have obvious clip/share energy because recognition is immediate and spectator-friendly. Replay is shakier. Once you know the call or the roar, many versions risk burning out unless they use broader packs, progressive snippets, confidence mechanics, or calendar cadence to keep the loop alive.

- Engine identification is the funniest-once / weakest-replay branch. Even if R4 says the sounds are distinct enough, the current concept still lacks a player-expression loop. It may become a good micro-round, but nothing in the current corpus suggests it can currently sustain another pack, another night, or another weekend without heavy editorial novelty (`.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md:24-27`).

## Community / online / spectator potential

- `Words of Wisdom` has the clearest community-content path in the lane. The platform doc already imagines a `WoW round builder` for public and private creation, and it notes that private friend-group content is "almost free if the content model is right" (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md:170-192`). That is a strong sign that the family can eventually scale through creator/community authored packs rather than only in-house curation.

- The friend-group history layer fits `Words of Wisdom` unusually well. The between-sessions social notes already imagine the platform remembering "who writes the funniest fakes" and generating shareable cards for exactly this kind of moment (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md:208-213`). This is not incidental polish for the lane; it is one of its main retention surfaces.

- `Words of Wisdom` also has plausible async community forms, but they should be eventized. The architecture notes permit async submission and later voting (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:42-46`), yet the lane evidence suggests the reveal still wants a social moment. That points toward scheduled batch reveals, daily friend-group drops, or race-weekend challenge windows rather than pure anytime-solo play.

- `Sound-based Games` has strong spectator and streamer potential because audio recognition creates immediate audience reaction, but its community-authoring story is much worse. `Words of Wisdom` can turn a clean schema into a form-based builder; sound modes need clip capture, trimming, labeling, and rights/source confidence. The research notes make that asymmetry explicit by splitting commentary/radio legality from engine/crowd practicality (`.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md:12-17,24-27`).

- Race-weekend cadence is especially promising for this lane. The calendar layer says reactive post-race content is the strongest retention signal, and this family is one of the best fits for that structure because radio, commentary, and crowd moments are among the first cultural artifacts a fan base shares after a race (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md:30-38`).

- Moderation/safety burden is lower here than in open-ended drawing or public text-prompt games, but not absent. Private WoW packs are low-friction. Public WoW or public sound packs still inherit the moderation spectrum the platform doc describes for community content (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md:194-198`). The burden is curation-heavy more than abuse-heavy.

## What to park for later research

- `R2` should stay parked as research, not be smuggled into design judgment. The lane can credibly say audio reveal/commentary variants are promising, but the legal position on broadcast-production audio is still unresolved and is explicitly tracked as a later question (`.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md:12-17`). This is a known deferred research item, not a sign the mode family is empty.

- `R4` is the gate for engine-identification seriousness. Until that question is answered, central synthesis should treat engine ID as a live curiosity, not as evidence that the full sound family is robust (`.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md:24-27`).

- `R3` matters more to this lane than it may first appear. If race-weekend freshness is one of the main replay levers for radio/commentary/crowd material, then the fast-turnaround curation pipeline is part of this lane's eventual product reality, even if Round 1 correctly keeps architecture and operations secondary (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md:30-38`; `.planning/explore/2026-04-11-product-vision-game-design/RESEARCH-TODOS.md:19-22`).

- The architecture note about sessions vs longer-lived instances should also be deferred rather than settled here, but it is relevant. Async WoW and race-weekend audio events both strain a simple one-sitting session model (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:204-206`). That is a later platform question, not a reason to flatten the lane now.

## What the categories did not capture

- The current category grid under-describes a crucial split inside this lane: authored-content-as-spark versus player-authored-performance-as-engine. `Words of Wisdom` works because authored radio sets the table and player fabrication drives variation. `Sound-based Games`, in its current form, mostly lives on authored clip quality alone. Treating both as just "authored prompt / reveal" hides that difference.

- The lane also exposes a play shape that is not cleanly "sync" or "async": appointment reveal. The architecture already sketches async creation with later voting (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-architecture.md:42-50`), but the fun here often lives in a scheduled drop, a shared listening moment, or a race-weekend social beat rather than permanent anytime availability. The current grid does not quite name that.

- Spectator-reactive play is also more central here than the usual local/online distinction suggests. This family is unusually good when some people are mainly watching, shouting, and recognizing. That is not the same thing as passive spectating; it is a semi-playing audience shape.

## Recommendations for central synthesis

- Treat `Words of Wisdom` as the strongest lane-A candidate, but synthesize it as a family with three live branches: the social Fibbage core, an audio-enhanced reveal branch, and an async/eventized derivative. Do not collapse it to "radio Fibbage" and lose the family surface.

- Do not keep `Sound-based Games` as one portfolio entry in later ranking. Split it at minimum into `commentary/crowd recognition` versus `engine identification`. The former is a credible lane-A continuation. The latter is still conditional on R4.

- When comparing this lane against others, use the question "is authored content the engine, or is social interpretation the engine?" `Words of Wisdom` is a hybrid with a real replay loop. Sound rounds are currently much more authored-content dependent.

- Preserve the lane's asymmetry in any central writeup. `Words of Wisdom` is already pressure-tested and partially operationalized; sound is lightly explored and should be compared as a frontier, not as a peer at equal maturity (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-INDEX.md:18-30`).

- Carry forward that this lane is strongest for couch/watch-party/sync-social play, plausibly extendable to eventized async, and weaker when forced into universal anytime-solo parity. The root spec explicitly warns against universalizing every mode across all contexts (`.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md:232-240`).

- Flag for possible lane-boundary revision later: if Round 2 wants sharper comparison, commentary/crowd audio may belong closer to `Words of Wisdom` and other cultural-fluency modes than to engine-identification as a shared "sound" lane.

## Framework Invisibility

This lane framing makes one concrete thing hard to see: session-arc role. Because the lane isolates the authored prompt / reveal family for depth, it does not tell us whether `Words of Wisdom` is best as a headliner, as a two-round palate cleanser inside a larger circuit pack, or as a watch-party interstitial. A composition-focused audit would notice that differently (`.planning/explore/2026-04-11-product-vision-game-design/IDEAS-platform.md:42-61`; `.planning/explore/2026-04-11-product-vision-game-design/CHECKPOINTS/01-words-of-wisdom-and-game-modes.md:34-38`).

The lane also hides comparative opportunity cost. A whole-night portfolio audit could conclude that even a strong authored-reveal family should remain secondary because other modes produce better escalation, physicality, or drop-in resilience. No amount of rigor inside this lane alone can surface that tradeoff cleanly.

## What the Obligations Didn't Capture

One thing the required lenses did not directly capture is acoustic environment. This lane is unusually sensitive to room speakers, stream compression, voice-chat overlap, and how silence/timing land in a living room or Discord call. The docs discuss sourcing and legality, but not how much the fun depends on audio playback quality and social listening conditions.

Another excess is tonal risk. Radio culture is affectionate fandom material, but it can also slide into "mock the driver" energy if the curation or UI over-rewards humiliation. That is not the dominant concern in the current docs, yet it could materially change how warm or mean the lane feels in repeated play.

## Rule 5: Frame-Reflexivity

If this had been classified under a different subject, `process_review` would have looked less at the mode family itself and more at why the corpus gave `Words of Wisdom` a pipeline, a catalog, and checkpoint depth while `Sound-based Games` stayed a sketch. That would surface documentation/process imbalance rather than game-shape quality.

If this had been run under `standard` orientation, it would have pushed toward a keep/cut judgment and probably collapsed the lane too early: `Words of Wisdom` up, sound games down. The exploratory frame is what kept commentary/crowd audio, audio-enhanced WoW, and eventized async derivatives open as distinct possibilities rather than burying them under one verdict.

The current frame also shapes attention away from hard viability thresholds. Because Round 1 explicitly keeps architecture secondary and refuses feasibility-first collapse (`.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/01-round-1/game-modes-r1-task-spec.md:135-139`), this audit preserves audio-heavy variants as live options. A different framing could reasonably close some of them sooner. That is not a flaw in this audit; it is what this orientation was chosen to do.
