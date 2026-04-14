---
date: 2026-04-13
lane: i-c
lane_name: "Hidden-info / private-room topology research"
orientation: exploratory
source_spec: 02-lanes/architecture/lane-i-c-task-spec.md
---

# Lane I-C Output

## Lane framing

This lane is not mainly about how many sockets a server can hold. It is about game shapes where secrecy, trust, voice, moderation, and presentation topology usually cap the room before transport does.

The official source set points to a recurring pattern:

- active hidden-info rooms stay relatively small
- audience or spectator layers can scale much larger than active roles
- same-room and private-room assumptions matter more than generic "multiplayer support"
- higher hidden-info counts usually require either a human moderator/storyteller or a much stricter social contract

Inference: if Prix Guesser wants future F1 modes in this lane, the early substrate should treat `visibility`, `role`, `view`, `authority`, and `communication policy` as first-class concerns rather than assuming "one room, one truth, one screen pattern."

## Reference cases

- `Among Us` ([official game page](https://www.innersloth.com/games/among-us/), [15-player update](https://www.innersloth.com/airship-map-is-now-live-2/), [classic reporting/moderation](https://innersloth.zendesk.com/hc/en-us/articles/6739782626196-How-do-I-report-someone-in-the-game-What-does-reporting-do), [Among Us 3D launch](https://www.innersloth.com/among-us-3d-launch-date-may-6-2025/), [Among Us 3D voice moderation](https://innersloth.zendesk.com/hc/en-us/articles/10686722088212-What-can-I-do-if-another-player-is-being-rude-or-acting-inappropriately-in-Among-Us-3D))
  Official shape: `4-15` players online or local WiFi, private individual screens, one or more hidden Impostors, periodic meeting phases, and explicit moderation/reporting flows. `Among Us 3D` adds native proximity voice chat and AI-assisted voice moderation.
  Inference: the transport model can reach `15`, but the harder limit is accusation readability and moderation burden. Once live voice becomes native, the moderation surface grows materially faster than the state-sync surface.

- `Fakin' It` ([official game page](https://www.jackboxgames.com/games/fakin-it), [Fakin' It All Night Long reveal](https://www.jackboxgames.com/blog/jnp-fakin-it-all-night-long-reveal))
  Official shape: original `Fakin' It` is `3-6` players; each player receives a secret phone instruction except the Faker. The 2024 follow-up `Fakin' It All Night Long` expands to `3-8` and explicitly adds a new remote-play mode.
  Inference: the original ceiling is not network scale; it is same-room bodily legibility. Jackbox did not simply "turn on online." It made a new remote-aware variant, which is a strong signal that topology is part of the game design.

- `Push The Button` ([official game page](https://www-origin.jackboxgames.com/games/push-the-button), [Jackbox remote-play support](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely))
  Official shape: `4-10` active players, hidden aliens, private phone prompts, shared accusation/reveal flow, and `10,000` audience capacity. Jackbox's official remote guidance is screen-share plus personal devices, not native matchmaking.
  Inference: this is a clean `shared stage + private handsets` pattern. Active deception stays small while spectators can scale far beyond the core room because they are downstream from the hidden-info loop, not full participants in it.

- `Keep Talking and Nobody Explodes` ([official remote-play guide](https://keeptalkinggame.com/how-to-play-remotely/), [official home page](https://keeptalkinggame.com/))
  Official shape: intended for the same room, but remote works if players can talk; one Defuser sees the bomb, Experts see only the manual, `2-4` players recommended, and only one Defuser can hold the private action surface at a time.
  Inference: the hard cap is communication bandwidth and role pressure, not rendering or packet fanout. This is a strong reference for asymmetric comms and same-puzzle / split-information play.

- `Artemis Spaceship Bridge Simulator` ([official game info](https://www.artemisspaceshipbridge.com/game-info.html), [official FAQ/licensing page](https://www.artemisspaceshipbridge.com/faq.html))
  Official shape: designed for a group in the same room, LAN-first, no official matchmaking, `2-11` players per ship, separate stations with distinct information rights, and theoretically many ships on one map.
  Inference: the meaningful social unit is still the bridge crew, not the total map population. Even when the simulation can hold more entities, command legibility and role coordination still organize the game around medium-size private crews.

- `Blood on the Clocktower` ([official site](https://bloodontheclocktower.com/), [official digital moderation policy](https://bloodontheclocktower.com/pages/digital-moderation-policy))
  Official shape: `5-20` players plus a Storyteller, in-person circle play in the physical version, and explicit Storyteller-led room control in the digital policy. The digital moderation policy says the majority of in-game moderation should fall to users and Storytellers.
  Inference: larger hidden-info rooms are possible, but they are being stabilized by a human moderator role and a deliberate social contract, not by "better netcode."

- `Spaceteam` ([official home page](https://spaceteam.ca/), [official FAQ](https://spaceteam.ca/faq/))
  Official shape: local multiplayer by default, no automatic matchmaking, internet mode via team password, and BYO voice chat for remote play; the FAQ still says players should ideally be in the same physical location so they can hear each other.
  Inference: this is the lightweight version of the same pattern. Even without hidden roles, private-room comms games often preserve room codes, voice dependency, and trusted-group assumptions instead of trying to become open lobbies.

## Why these rooms cap where they do

The official sources rarely say "we cap at X because Y." The causes below are therefore design inferences from their stated player counts, room assumptions, and moderation systems.

- `Discussion bandwidth` is a primary ceiling. In `Among Us`, `Push The Button`, `Fakin' It`, and `Blood on the Clocktower`, each added active player does not just add one more client; it adds one more alibi, one more suspect, one more interruption source, and one more person who needs time in the accusation loop.

- `Hidden-info stewardship` becomes work. Secret prompts, role assignments, partial truths, moderator powers, and reveal timing all have to be delivered without leakage. `Blood on the Clocktower` solves this with a Storyteller. `Jackbox` solves lighter versions with phones plus a shared screen. `Keep Talking` solves it with a hard role split.

- `Voice and social safety` often outgrow transport needs. `Among Us Classic` has explicit report flows and moderator review. `Among Us 3D` adds mute, kick, reports, and AI-assisted voice analysis. That is a direct example of the communication layer becoming the operational burden.

- `Presentation leakage` constrains topology. Games like `Fakin' It`, `Keep Talking`, `Artemis`, and this repo's own control-room concepts depend on different players seeing materially different truths. A single shared display cannot safely serve every role.

- `Audience scale` is different from `active hidden-info scale`. Jackbox can advertise `10,000` audience members while keeping active deception rooms at `3-10` because audience participation is structurally simpler than maintaining ten extra private-role participants.

- `Moderation can replace infrastructure as the scaling tool`. `Blood on the Clocktower` reaches larger hidden-info groups than many digital deception games, but it does so by putting a human in the loop. That is a topology and authority choice, not a networking win.

## Topology and hidden-info implications

- `Shared stage + private handsets` recurs in Jackbox. The TV/stream handles timing, spectacle, voting, and accusation reveals; phones carry secrets. This is powerful for couch play, host-screen watchability, and streamer-adjacent rooms.

- `All-private screens + synchronized meeting phases` recurs in `Among Us`. Each player has a full private play surface until the room periodically collapses into a shared social phase. This works well for remote private rooms and less well for hybrid shared-screen setups.

- `One private actor + expert/support roles` recurs in `Keep Talking`. The topology is asymmetric by design: one player manipulates the live state, others interpret reference material. This is especially relevant for control-room or driver-vs-wall F1 futures.

- `Multi-station crew play` recurs in `Artemis` and lighter comms games like `Spaceteam`. These modes are not just "multiplayer." They are `information partition` systems where role identity is defined by what you are allowed to see and say.

- `Moderator-led hidden-info rooms` recur in `Blood on the Clocktower`. Once the room gets larger and more socially performative, the topology often needs a Storyteller, emcee, or room controller rather than just more players.

- `Hybrid local/remote secret play` is the most fragile shape. A host screen is great for spectatorship, but it can easily leak secrets that are safe on fully private screens. That matches the existing repo warning that hybrid is probably later and should not be made impossible.

## Relevance to possible F1 modes

- `Pit Wall`, `Split Pit Wall`, `Driver Override`, `Bad Wall`, `Wall of Noise`, and the broader `Trust the Seat` / control-room family look much closer to `Keep Talking`, `Artemis`, and `Spaceteam` than to generic quiz rooms. They want desk-specific information, different permissions, and voice dependency. Their natural active size looks small-to-medium, not large.

- Hidden-hunter or sabotage racing variants in the repo's predator / crash-politics family look closest to `Among Us`: all players on private screens, hidden role assignment, short accusation windows, and a private-room trust boundary. Inference: these probably want an even smaller sweet spot than `Among Us`, because driving noise already consumes cognitive bandwidth before deduction begins.

- `Silly Season War Room`, `Press Room`, rumor-seeding, or sabotage branches of `Words of Wisdom` and `Stewards' Room` fit the `Jackbox` pattern well: shared stage for reveals, private phones for prompts, active room around `4-10`, and a much larger spectator shell if desired.

- The geography anchor mode itself is mostly outside this lane, but hidden-info wrappers around it are plausible. Examples: asymmetric clue-holder variants, team analyst roles, secret sabotage or misdirection packets, or a host/pundit overlay that knows more than players do.

- Public stranger play is a weak fit for much of this territory. The more a mode depends on bluffing, room memory, trust, and voice interpretation, the more the current project posture of trusted private rooms looks like an advantage rather than a temporary limitation.

## Early architectural implications

- Separate `room`, `participant role`, `view`, and `authority`. A person may be a player, spectator, moderator, captain, driver, desk specialist, or host. Those should not collapse into one host-vs-player split.

- Give session state first-class visibility scopes. Secret prompts, role assignments, desk-only telemetry, moderator tools, and partial reveals should be modeled as private or selectively visible data, not merely hidden in the UI.

- Let each mode declare a topology contract. Examples from this lane: `shared_stage + private handsets`, `all_private_screens + meetings`, `one actor + experts`, `multi_station crew`, `storyteller-led room`. This is cheaper and safer than hardcoding one default room shape.

- Treat `communication policy` as a mode capability. Some modes assume in-room speech, some need BYO voice, some may want native voice later, some are safer with structured text or limited prompts. That is not a presentation detail; it changes moderation, hidden-info leakage risk, and play quality.

- Separate `active-player capacity` from `audience/spectator capacity`. `Push The Button` and `Fakin' It` show that active deception can remain small while spectators scale far larger. Future F1 pundit, host-screen, or streamer variants may want exactly that split.

- Preserve a logically authoritative secret distributor even if the first implementation runs locally. If later online-sync or hybrid control-room modes appear, secret role assignment, timed reveals, and private desk views need one consistent source of truth.

- Keep privacy and trust states explicit. Room code, password, invite-only posture, kick/mute/exclude hooks, and role-aware reconnection are cheap seams to preserve now. Full public matchmaking, integrated voice, and automated moderation are not required now.

- Do not assume one shared display is the product. This lane strongly reinforces the repo's existing view that presentation topology must stay separate from core session state.

## Uncertainties and limits

- Most official sources provide counts, roles, and room assumptions, not explicit design postmortems. Several "why this caps here" claims above are inferences from those structures.

- The source set is stronger on party/deception/comms topology than on F1-specific action hybrids. A hidden-hunter racing mode that mixes continuous driving with accusation play still needs prototype evidence.

- `Blood on the Clocktower` shows that larger hidden-info rooms are possible, but it may overstate what a browser-first, low-operator F1 product should try to inherit. Its scale comes with a heavy human-facilitation model.

- Hybrid same-house-plus-remote play remains the most under-evidenced and highest-risk topology for this project. The repo is already right to treat it as something to avoid foreclosing, not something to optimize first.
