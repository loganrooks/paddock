---
date: 2026-04-13
audit_subject: artifact_analysis
audit_orientation: exploratory
audit_delegation: self
scope: "Round 2B Wave 1 Lane A: room, topology, authority, visibility, and audience-shell pressures"
triggered_by: "manual: Round 2B Wave 1 Lane A"
tags:
  - exploratory-audit
  - round-2b
  - lane-a
  - room-model
  - topology
  - authority
  - visibility
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/next-round-gap-review.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-foreclosure-synthesis-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2b-lane-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-experience-archetypes-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-a-local-party-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-b-private-online-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/03-next-round/round-2a-lane-d-community-event-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-i-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-11-product-vision-game-design/HANDOFF.md
planning_surfaces_inspected:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/01-CONTEXT.md
---

# Round 2B Lane A Output

## Lane framing

`[governing:cited]` This is a Wave 1 pressure-mapping artifact for `RESP-04`. It focuses on `event container` vs `room` vs `active game instance`, room lifecycle mechanics, topology and presentation surfaces, authority boundaries, visibility scopes, and private-room vs public-shell separation.

`[governing:cited]` It is not the final foreclosure ledger. It does not classify anything into `explicit now`, `keep open`, or `defer`, and it does not try to settle long-horizon identity/history/cadence questions except where they directly change room shape.

`[assumed:reasoned]` The central architectural pressure exposed by the sources is not simply "multiplayer." It is the risk of collapsing too many things into one object: `room = active game = host screen = authority = participant truth`. That collapse is survivable for the narrowest couch-reading of Milestone 1, but it distorts private online sync, same-house-separated forms, and bounded event or audience shells quickly.

## Traceability and scope

`[governing:cited]` This lane directly supports `RESP-04` and most strongly informs `GAP-05` and `GAP-08`. It tightens the planning-facing consequences of the experience mapping already produced by `RESP-03`.

`[governing:cited]` Primary steering sources for this lane are:

- `00-governance/review-trail-framework.md`
- `00-governance/next-round-gap-review.md`
- `03-next-round/round-2b-foreclosure-synthesis-task-spec.md`
- `03-next-round/round-2b-lane-common-scaffold.md`
- `03-next-round/round-2a-experience-archetypes-output.md`
- `02-lanes/architecture/lane-i-output.md`
- `02-lanes/architecture/lane-j-output.md`

`[governing:cited]` Corroborative but not controlling sources are:

- `03-next-round/round-2a-lane-a-local-party-output.md`
- `03-next-round/round-2a-lane-b-private-online-output.md`
- `03-next-round/round-2a-lane-d-community-event-output.md`
- `HANDOFF.md`

`[assumed:reasoned]` The canonical planning docs were inspected here for ripple tracing, not as higher-authority solution sources.

`[governing:cited]` This lane is answering:

- which experience classes break if `room` and `game instance` are collapsed
- which experience classes break if everyone is assumed to share one information surface
- where host, operator, judge, moderator, narrator, specialist, and audience roles become structurally important
- which topology differences are load-bearing enough to preserve as first-class possibilities
- which early shortcuts would later make private-sync, same-house-separated, or public-shell futures awkward
- where those judgments would ripple across Milestone 01 and canon docs

`[governing:cited]` This lane is not answering:

- the final Phase 01 decision ledger
- which future wrapper is most strategically important
- exact networking or library choice
- identity/history/cadence architecture except where it changes room topology or lifecycle

## Calibration carry-forward

`[governing:cited]` This output inherits the Round 2B rules that it must stay planning-facing, preserve non-foreclosure, avoid one universal ontology or one universal room shape, and keep lived product language in view instead of replacing it with abstract architecture jargon.

`[governing:cited]` It also inherits the Round 2A creator-corrected posture:

- do not force all ideas into one mode taxonomy
- do not treat local as the only authentic form and remote as a degraded copy
- do not treat publicness as obviously desirable
- do not let one reference product or one engineering pattern harden into product law

`[assumed:reasoned]` The Wave 1 judgment standard here is therefore: which separations look load-bearing to preserve? It is not: which future is most likely to win.

## Path of inquiry

`[evidenced/governing:mixed]` The inquiry order was:

1. governance and gap-review sources to lock scope and anti-goals
2. Round 2B root spec and common scaffold to preserve Wave 1 boundaries
3. Round 2A experience synthesis to identify concrete experience classes
4. Round 2A lane A, lane B, and lane D outputs to sharpen lived room pressures
5. architecture lanes I and J to test whether the experience pressures map to real substrate seams
6. `HANDOFF.md` to confirm original motivating questions
7. `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, and Phase 1 context to trace ripple surfaces

`[assumed:reasoned]` The main comparison was not "offline vs online." It was:

- shared-stage local party
- private-screen synchronous group play
- same-house-separated or hybrid-local forms
- bounded event and audience shells

`[assumed:reasoned]` The recurring question underneath each comparison was: what breaks if the product assumes one room, one shared truth surface, one host role, and one join mechanic?

## Pressure map

### 1. `event container` vs `room` vs `active game instance`

`[evidenced/governing:mixed]` Lane I and Lane J converge strongly that separate shells and states are normal, not exotic. Round 2A then makes clear why that matters for Prix Guesser specifically.

`[assumed:reasoned]` Local recurring party can often present as if `room = active game`, because the social gathering, the current round loop, and the visible shared stage all feel like one thing. But private online sync, same-house-separated play, and event-shell play all push against that simplification:

- a recurring friend-group room may outlive one active game instance
- one event shell may contain one active table plus a passive audience surface
- one race-weekend gathering may want rematch, replay, finalists, or mode switching without becoming a new social room each time

`[assumed:reasoned]` If these layers are collapsed, the experience classes that break first are:

- private online sync groups that want room continuity across multiple games or pauses
- same-house-separated forms that need reconnection and re-convergence without destroying the social room
- community or streamer-adjacent events where the watchable shell is not the same thing as the active contestant field

`[projected:reasoned]` Provisional pressure signal: keep `event container`, `room`, and `game instance` logically distinct, even if Milestone 1 often maps them `1:1` in the visible UI.

### 2. Room lifecycle is a real mechanic, not just "join room"

`[evidenced/governing:mixed]` Lane J directly surfaces seat reservation, reconnect, ownership migration, invites, and lobby lifecycle as concrete mechanisms. The lived-experience lanes explain why these are not backend trivia.

`[assumed:reasoned]` Different archetypes create different lifecycle demands:

- local host-screen play wants low-friction QR/code join and quick rematch
- handset-heavy local variants want seat claim and stable player-to-device mapping
- private online sync wants invite posture, explicit lock state, clean rejoin after refresh or phone sleep, and tolerance for uneven presence
- audience shells want audience-only entry without implicitly granting player rights

`[assumed:reasoned]` If lifecycle is treated as one flat action, several futures get awkward:

- a reconnecting player can be mistaken for a fresh join
- same-house private devices can steal or lose seats
- room locking and invite boundaries become bolted-on flags instead of trust posture
- room owner loss becomes catastrophic because presenter, owner, and authority were silently fused

`[projected:reasoned]` Provisional pressure signal: `join`, `invite`, `seat claim`, `lock`, `rejoin`, and `ownership migration` should be thought of as room-lifecycle primitives, not scattered controller-screen behaviors.

### 3. One information surface is too narrow for the experience map

`[evidenced/governing:mixed]` Round 2A lane A says the best local forms often alternate between shared stage and private commitment. Round 2A lane B says remote sync becomes distinct precisely because per-player private views and mixed visibility are load-bearing. Lane D says event shells want audience-readable but selective visibility.

`[assumed:reasoned]` The experience classes that break if everyone is assumed to share one information surface are:

- local party variants that rely on private submissions until reveal for shame-buffering or bluff
- same-house-separated and hidden-role local forms
- private online sync modes with role-private instructions, secret commitments, or confidence play
- public or semi-public shells where the audience should see the reveal arc without seeing every player secret

`[assumed:reasoned]` This is why "host-screen-friendly" cannot be allowed to drift into "everyone sees the same truth all the time." The former is central to Milestone 1. The latter would silently delete several strong local and remote possibilities.

`[projected:reasoned]` Provisional pressure signal: preserve distinct surface possibilities such as:

- `shared_stage + private handsets`
- `all_private_screens + reveal/meeting phases`
- `same_house_separated` or `hybrid-local` play
- `player surface + host surface + audience surface`

### 4. Authority roles need to be richer than `host` and `player`

`[evidenced/governing:mixed]` Lane I argues directly for richer participant capabilities. Lane J shows operator, co-host, moderation, and room-rights patterns in concrete systems. The Round 2A experience outputs explain where those roles become product-significant.

`[assumed:reasoned]` Structurally important authority roles appear in different places:

- local recurring party: host, narrator, judge, or rotating moderator can shape pacing and embarrassment tolerance
- private online sync: specialist or role-private participants can hold privileged information or asymmetric action rights
- bounded event shell: operator, moderator, co-host, and audience participant rights become distinct from active player rights

`[assumed:reasoned]` The fragile shortcut is to collapse all of that into one enum where the "host" both owns the room socially, advances the game, presents the host screen, moderates anything questionable, and never disconnects.

`[projected:reasoned]` Provisional pressure signal: authority should stay layered across at least these scopes:

- room administration
- game progression
- moderation/operator controls
- narrative or judge-like role rights
- audience participation rights

### 5. Visibility-scoped publication and staged reveal are early seams

`[evidenced/governing:mixed]` Both architecture lanes are explicit that visibility belongs in state publication, not just UI hiding. The experience outputs explain why: reveal timing and selective disclosure are part of the product good, not implementation garnish.

`[assumed:reasoned]` Prix Guesser already has several strong visibility patterns:

- public prompt, private answer, shared reveal
- role-private brief, public debate, private verdict, public reveal
- audience-visible aggregate without leaking player-private details
- moderator-only or operator-only controls in a bounded event shell

`[assumed:reasoned]` If all clients receive one shared blob and the UI merely hides fields, hidden-info local variants, remote secret-state play, and spectator-safe reveal shells all become riskier and more awkward.

`[projected:reasoned]` Provisional pressure signal: keep `authoritative truth`, `projected views`, and `private payloads` conceptually separate. The exact implementation can stay open.

### 6. Public shell is not the same thing as active participation

`[evidenced/governing:mixed]` Lane D is decisive on this point: the public or streamer-adjacent future is most coherent as a bounded shell around private-first play, not as a permanently public core.

`[assumed:reasoned]` That creates a room-topology consequence: the moment Prix Guesser wants audience, watch-party, or semi-public event energy, it needs a boundary between:

- who is actively playing
- who is watching
- who can moderate or operate
- what is discoverable
- what is merely visible

`[assumed:reasoned]` If public shell and active room are treated as the same thing, private-first tone is distorted early, moderation burden arrives everywhere, and spectator readability gets confused with stranger participation.

`[projected:reasoned]` Provisional pressure signal: treat `audience shell` or `public/event shell` as a wrapper boundary with narrower and more selective rights than active room participation.

### 7. Topology-sensitive local forms are not throwaway edge cases

`[evidenced/governing:mixed]` Round 2A lane A and lane B together show that same-house-separated play sits across the local/remote boundary. Physically local does not always mean shared-stage; the decisive variable can be secrecy, role asymmetry, or private screens.

`[assumed:reasoned]` This matters because one tempting shortcut would be:

- local means one shared host screen
- remote means private screens

That binary is too crude. Some of the most promising shame-buffered or role-asymmetric local forms behave more like private-screen remote play than like shared-stage couch play.

`[projected:reasoned]` Provisional pressure signal: same-house-separated and hybrid-local play should be preserved as a real topology family, not dismissed as an implementation oddity.

## Candidate early decisions or seams

`[governing:cited]` These are provisional pressure signals only. They are not Wave 2 classifications.

- `event_container`, `room`, and `game_instance` should remain conceptually distinct even if Milestone 1 commonly maps them together.
- Room lifecycle should be modeled with explicit semantics for invites, join posture, seat claim, lock state, rejoin, and ownership migration.
- Topology should be allowed to vary by mode or wrapper rather than being derived from one platform-default room shape.
- Participant rights should be capability-shaped rather than locked to one `host/player` split.
- Visibility should be treated as scoped publication and staged reveal, not just client-side hiding on a shared state blob.
- Audience/public shells should remain distinct from active play and from public discovery.
- The social host, the current presenter, the room owner, and the authority runner should not be assumed to be the same actor forever.

## Shortcuts likely to cause foreclosure

- Making `room` the only real multiplayer container.
- Assuming every meaningful session has one host, one participant list, and one active truth surface.
- Treating host-screen presentation as the universal source of gameplay truth instead of one possible surface.
- Treating join as one monolithic action instead of separate `invite`, `claim`, `lock`, `rejoin`, and `audience-only` paths.
- Encoding participant roles as only `host` and `player`.
- Publishing one shared state object to all clients and hiding secrets in UI conditionals.
- Assuming same-house-separated play is just a niche bug case rather than a topology sibling of remote hidden-info play.
- Equating "public shell" with "open active room."
- Fusing authority to whichever browser currently renders the host screen.

## Artifact and planning-surface ripple map

| Surface | Ripple class | Why this lane touches it | Likely carry-forward if this judgment lands |
|---|---|---|---|
| `.planning/ROADMAP.md` | `Milestone 01-wide` | Phase 3 currently names authoritative private rooms, but not `room` vs `game instance`, lifecycle semantics, or richer authority scopes. Phase 3.1 currently frames the UI contract mainly as host-screen/controller. | Add carry-forward notes for Phase 3, 3.1, 4, 5, and 7 so room shell, lifecycle, multi-surface visibility, and ownership/rejoin semantics stay visible during planning. |
| `.planning/REQUIREMENTS.md` | `Milestone 01-wide` plus `canonical-doc doctrine` | Current room requirements cover private room creation, join, reconnect, and host pacing, but they do not explicitly name invite/lock posture, seat claim, ownership migration, capability-shaped roles, or visibility-scoped publication as planning anchors. | Likely strengthen seams or add planning-reference anchors around `room shell vs game instance`, participant capabilities, and visibility-scoped state publication without converting all of them into Milestone 1 ship-gates. |
| `.planning/PROJECT.md` | `canonical-doc doctrine` | The current vocabulary distinguishes anchor mode, session wrapper, watchability layer, and platform shell, but it still leaves `event container`, `room`, `game instance`, and participant capability language implicit. The host-screen-friendly bias could be misread as a one-surface assumption. | Add vocabulary and carry-forward notes clarifying that watchable private play can still involve private controllers, role-private views, and bounded audience shells. |
| `.planning/LONG-ARC.md` | `canonical-doc doctrine` | The doctrine already separates visibility and hosting ladders, but it does not yet make `player shell`, `audience shell`, `room shell`, and `active instance` distinctions explicit. | Clarify that later streamer/spectator or showcase shells should wrap bounded active play rather than redefine all rooms as public, and clarify that visibility and role surfaces are separable from the host-led product center. |
| `.planning/phases/01-authored-round-contract/01-CONTEXT.md` | `Phase 01-local` light ripple | This lane is not primarily a Phase 1 lane, but Phase 1 already models reveal semantics and future wrapper notes. A hidden assumption that every reveal is universal and same-surface would be a quiet mismatch. | Carry a light warning only: do not let authored reveal semantics assume one universal viewer or one permanent surface. Do not widen Phase 1 scope beyond that. |
| Future Phase 3 context and plans | `Milestone 01-wide` high ripple | Phase 3 is where authoritative private rooms and room state become concrete. This is the most direct landing zone for room shell, join lifecycle, seat/rejoin, and authority layering. | Planning should explicitly cover room shell vs active instance, invite/lock/rejoin/ownership rules, and the separation of social room ownership from runtime authority. |
| Future Phase 3.1 context and plans | `Milestone 01-wide` high ripple | The interaction contract cannot stop at host screen plus controller if Wave 1 is taken seriously. | UI planning should account for host screen, handset/controller, role-private screen, and possible audience-readable surfaces, even if only some are implemented now. |
| Future Phase 4 context and plans | `Milestone 01-wide` | Join UX is where topology assumptions harden quietly. | Phase 4 planning should distinguish access path, seat claim, reconnect, and audience entry rather than flattening them into one join screen. |
| Future Phase 5 context and plans | `Milestone 01-wide` | Reveal/watchability work can accidentally universalize one surface. | Phase 5 planning should preserve reveal flows that are audience-readable without leaking private submissions or role-private information too early. |
| Future Phase 7 context and plans | `Milestone 01-wide` | Reconnect work is room-lifecycle work, not just browser refresh recovery. | Phase 7 planning should cover seat reclaim, authority continuity, and ownership handoff where relevant, not only state reload after disconnect. |

## Open uncertainties and evidence quality

`[evidenced:reasoned]` Highest-confidence findings:

- collapsing `room`, `game instance`, visibility, and authority into one object would distort multiple lived experience classes
- visibility-scoped publication is a real product seam, not merely a technical nicety
- participant rights richer than `host/player` are strongly supported by both experience and engineering sources

`[assumed:reasoned]` Medium-confidence findings:

- room lifecycle primitives beyond `join/reconnect` should already be visible in Milestone 1 planning, even if not all are first-ship features
- public or audience shell should be treated as wrapper logic rather than active-room default logic
- same-house-separated play is significant enough to justify seam protection now

`[open:reasoned]` Lower-confidence or still-open areas:

- the minimum useful capability set for Milestone 1
- whether ownership migration needs immediate Phase 3 planning prominence or only a carry-forward note
- how much of these room/topology judgments should reflect backward into Phase 1 contract language versus staying Phase 3+ concerns
- whether the first serious topology stress-test should be a same-house hidden-info variant, a private online sync mode, or a bounded audience shell

`[governing:cited]` This uncertainty is acceptable in Wave 1. The lane's job is to surface pressures and ripple, not to freeze the ledger.

## Coverage note

`[evidenced:cited]` `RESP-04`: advanced materially but not closed. This lane maps the room/topology/authority/visibility slice of the foreclosure question and leaves final Wave 2 classification to later synthesis.

`[evidenced:cited]` `GAP-05`: answered strongly for the room/container/authority/visibility side of the missing experience-to-architecture matrix.

`[evidenced:cited]` `GAP-08`: answered strongly for the planning-facing translation of engineering-exposure findings into room/topology seams and likely early-shortcut risks.

`[governing:cited]` Still unresolved by design:

- the identity/history/cadence lane
- the Wave 1.5 cross-lane sensitivity synthesis
- the Wave 2 Phase-01-facing ledger
- any final statement of `explicit now`, `keep open`, or `defer`
