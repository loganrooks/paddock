---
date: 2026-04-14
audit_subject: pre_sensitivity_challenge_packet
audit_orientation: exploratory
audit_delegation: self
scope: "Stress-test the current wrapper ordering, first audience bundle, and daily/programmed challenge placement before sensitivity"
triggered_by: "05-residual-gap-converged-synthesis-output.md"
tags:
  - exploratory-audit
  - gap-closure
  - challenge-round
  - wrappers
  - audience
  - cadence
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-pre-sensitivity-challenge-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-residual-gap-converged-synthesis-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-residual-gap-chunk-a-wrapper-ordering-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-residual-gap-chunk-e-event-memory-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-remaining-gap-response.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-next-round-gap-opportunity-register.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
external_sources:
  - https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends
  - https://geoguessr.zendesk.com/hc/en-us/articles/28237315964177-How-do-I-create-a-challenge-for-a-set-number-of-users
  - https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz
  - https://geoguessr.zendesk.com/hc/en-us/articles/28237329276049-How-do-I-remove-someone-from-the-leaderboard-of-a-Challenge
  - https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges
  - https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge
  - https://geoguessr.zendesk.com/hc/en-us/articles/4407923951249-How-does-Event-work
  - https://geoguessr.zendesk.com/hc/en-us/articles/9785960760977-What-are-Tournaments
  - https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot
  - https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform
  - https://www.jackboxgames.com/blog/how-audience-play-along-differs-in-each-jackbox-game
  - https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-
  - https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work
  - https://support.jackboxgames.com/hc/en-us/articles/15794756085015-How-many-players-can-join-each-game
  - https://support.discord.com/hc/en-us/articles/1500005513722-Stage-Channels-FAQ
  - https://support.discord.com/hc/en-us/articles/360047132851-Enabling-Your-Community-Server
  - https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery
  - https://support.chess.com/en/articles/8708990-how-do-i-find-the-daily-puzzle
  - https://support.chess.com/en/articles/9714718-what-are-streaks
  - https://support.chess.com/en/articles/8705920-how-do-i-see-my-tournament-stats-and-past-tournaments
---

# 05 Pre-Sensitivity Challenge A: Wrapper Ordering, Audience Bundle, And Daily/Programmed Challenge Placement Output

## 1. Challenge framing

- Mode: `hypothesis testing`
- Classification: `initial architecture research/planning`
- Question:
  - does the current stronger-default framing survive direct adversarial comparison, or is it prematurely compressing a real rival branch at the boundary between wrapper, audience rights, cadence, and proto-event shell?
- Scope:
  - stress-test three promoted/defaulted claims from `05-residual-gap-converged-synthesis-output.md` and `05-residual-gap-chunk-a-wrapper-ordering-output.md`:
    - the low-burden first-wrapper competition is mainly `showcase aftermath` versus `share-by-link / challenge`
    - `first audience bundle` is an ordering question inside `bounded live audience`
    - `daily/programmed challenge` is `editorial/programmed cadence` by default rather than a peer wrapper or true event shell
  - pull pressure from `05-residual-gap-chunk-e-event-memory-output.md` where `event memory` was tightened into an `event object threshold`
- Non-goals:
  - not a universal first-wrapper winner
  - not a final first audience bundle
  - not a final cadence taxonomy
  - not a final event-object or event-memory product decision
  - not a roadmap commitment
- Stop condition:
  - enough direct external comparison exists to say whether the current hypothesis survives intact, survives only with narrower wording, or should be materially re-ranked before sensitivity

## 2. Target hypothesis

`[assumed:reasoned:internal]` The current stronger-default framing under test is:

- `showcase aftermath` and `share-by-link / challenge` are still the real low-burden first-wrapper competition after private rooms
- `bounded live audience` is a real wrapper family, but `first audience bundle` is still mainly an in-family staging question
- `daily/programmed challenge` should be treated as `editorial/programmed cadence` by default, and only later as event-like if stronger event-object traits are actually present

## 3. Why this hypothesis matters

`[governing:cited:internal]` This hypothesis is load-bearing because it affects whether later sensitivity:

- silently hardcodes the wrong first post-private wrapper order
- understates how much audience rights and moderation controls change shell identity
- treats official recurring challenge as harmless cadence language when it may already be borrowing event-shell logic
- muddies the `room / wrapper / event-container` and `cadence / event` separations protected by `LONG-ARC.md`, `PROJECT.md`, and `REQUIREMENTS.md`

`[assumed:reasoned:internal]` If the framing is wrong, the cost is not just bad vocabulary. It is wrong non-foreclosure pressure on:

- wrapper seams
- audience-right controls
- event-memory thresholds
- future editorial and hosting obligations

## 4. Gap justification

`[governing:cited:internal]` This packet directly stress-tests:

- `RGR-01`
- supporting pressure from `RGR-05` and `RGR-06`
- underlying register anchors:
  - `GCO-01`
  - `GCO-02`
  - `GCO-03`
  - `GCO-08C`
  - `GCO-08E`

`[evidenced:cited:internal]` Exact local claims being challenged:

- `05-residual-gap-converged-synthesis-output.md`
  - the open wrapper question is "mostly the low-burden order" between `showcase aftermath` and `share-by-link / challenge`
  - `first audience bundle` is "bounded inside one family"
  - `daily/programmed challenge` is "editorial/programmed cadence by default rather than a true wrapper or event shell"
- `05-residual-gap-chunk-a-wrapper-ordering-output.md`
  - findings `2`, `3`, and `6`
  - the `Recommended carry-forward`
  - the `Sensitivity implications`
- `05-residual-gap-chunk-e-event-memory-output.md`
  - `event memory` becomes real only when an `event object threshold` is crossed
  - `editorial / programmed pulse` remains a later overlay rather than the base engine

`[assumed:reasoned:internal]` Why these belong together:

- the real challenge surface is the boundary where `bounded live audience`, `audience bundle`, `daily/programmed challenge`, and `event shell` can quietly blur into each other
- if that boundary is misread, sensitivity will protect the wrong distinctions

## 5. What is already settled and not being relitigated

`[decided:cited:internal]` This packet does **not** reopen:

- private-first, trusted-group product center
- substrate-plus-wrappers posture
- staged visibility and audience-right distinctions
- `showcase aftermath`, `share-by-link / challenge`, `bounded live audience`, and `ambient community` as meaningfully different families
- `ambient community` as a later, discoverable, moderation-bearing branch rather than a synonym for recap, challenge, or bounded audience
- `event memory` as distinct from player history, room/group memory, and content calibration history

`[evidenced:cited:internal]` The packet is testing ordering and boundary placement, not re-running family discovery from scratch.

## 6. Strongest rival framing(s)

### Rival A: `bounded live audience` should be treated as the first real post-private wrapper pressure, not as a heavier later branch

`[assumed:reasoned:internal+external-direct]` Because Prix Guesser is already host-led and watchability-heavy, the strongest rival says the first non-private extension is not deferred replay but `watch live with bounded audience`:

- host-led social products often move naturally from private players to audience viewers and play-along
- public-light watchability may matter earlier than recap or challenge if the product's emotional center is already shared-screen ritual

### Rival B: `daily/programmed challenge` is not merely cadence; it is a proto-event shell

`[assumed:reasoned:internal+external-direct]` The strongest cadence rival says:

- official recurring challenge can create common time, shared comparison, history, and habit loops strong enough to function like a shell
- once official programming becomes visible and repeatable, it may deserve wrapper-level or event-level treatment earlier than the residual synthesis admits

### Rival C: `first audience bundle` is not just in-family ordering once it crosses from passive or reactive rights into submission or speaking

`[assumed:reasoned:internal+external-direct]` The strongest bundle rival says:

- `watch`, `react/predict`, and `submit/speak` are not small gradients
- some bundle changes materially alter moderation posture, role control, and session identity
- that could make the "first bundle" more than a simple parameter inside one family

## 7. Path of inquiry

- Entry point:
  - `05-pre-sensitivity-challenge-a-wrapper-audience-task-spec.md`
  - the promoted defaults in `05-residual-gap-converged-synthesis-output.md`
  - the carry-forward from `05-residual-gap-chunk-a-wrapper-ordering-output.md`
- Branches considered:
  - async/share challenge versus live audience as first non-private pressure
  - passive audience versus reactive audience versus speaking/submission bundles
  - daily/programmed challenge as cadence, wrapper, or proto-event shell
- Branches pursued:
  - `GeoGuessr` for private party, invite-only challenge, public-light challenge leaderboard, live challenge, daily challenge, events, and tournaments
  - `Kahoot` for clean live-versus-assigned distinction
  - `Jackbox` for live public-light audience, remote play, audience-bundle variation, and moderation burden
  - `Discord` for explicit audience/speaker/moderator staging and the jump from bounded live audience to community/discovery obligations
  - `Chess.com` for daily puzzle, streak, and tournament history as cadence-versus-event comparison
- Branches deferred or abandoned:
  - money-family ranking
  - host-identity ranking
  - contribution/discovery identity
  - concrete event-memory UI design
- Reframing:
  - the sharpest challenge is not whether `bounded live audience` exists; that already looks secure
  - the sharper challenge is where audience-bundle escalation stops being "same family, different bundle" and starts becoming a shell threshold
  - the second sharp challenge is whether official recurring challenge stays "cadence" until an explicit event object appears

## 8. Direct external source register

| Source family | Direct sources | What it directly grounds here | Challenge pressure | Limits |
| --- | --- | --- | --- | --- |
| `GeoGuessr private, challenge, live, daily, event` | `Play with Friends`, `Only Invited challenge`, `Create Challenge`, `remove leaderboard result`, `Live Challenges`, `Daily Challenge`, `Event`, `Tournaments` | separate private party, invite/share challenge, live party, global daily challenge, time-boxed events, and scheduled tournaments | strongest pressure on whether daily challenge is just cadence or starts acting like event shell | geography product with stronger global competition than Prix Guesser currently wants |
| `Kahoot live versus assigned` | `How to host a live kahoot`, `How to assign a kahoot in web platform` | strong split between host-led live session and learner-paced assigned session | strengthens the idea that async challenge/share is a real low-burden wrapper family rather than just a feature toggle on live play | classroom/training posture is stronger than Prix Guesser's social ritual posture |
| `Jackbox audience and public-light remote play` | `How Audience Play-Along Differs In Each Jackbox Game`, `Can I play Jackbox Games remotely?`, `How does Moderation work?`, `How many players can join each game?` | live audience is a real shell; audience bundles vary a lot; streaming/public-light play creates moderation and room-code burden immediately | strongest pressure against underrating `bounded live audience` and against treating all audience bundles as cheap in-family variants | streamer and text-input party culture are not a one-to-one match |
| `Discord staged audience and community jump` | `Stage Channels FAQ`, `Enabling Your Community Server`, `Enabling Server Discovery` | explicit staging from audience to speaker with moderator approval; much heavier obligations once a space becomes community/discoverable | strengthens in-family audience staging, while also showing how public/discoverable community is a different obligation class | voice/community platform rather than game wrapper |
| `Chess.com daily cadence and tournament history` | `Daily Puzzle`, `Streaks`, `tournament stats and past tournaments` | daily cadence, archival revisit, public streak counter, and separate tournament history/trophies | strongest pressure on the claim that daily/programmed challenge is "only cadence" | skill/progression product with heavier identity posture than current Prix center |

## 9. Reference translation

| Reference | What is analogous here | What is not analogous here | What is borrowed as concern versus solution |
| --- | --- | --- | --- |
| `GeoGuessr` | private party, URL-shared challenge, invite-only challenge, live challenge, daily challenge, time-boxed events, tournament shells | larger public competition surface and global rank culture | `solution`: distinct wrapper/event surfaces. `concern`: daily/global comparison can become shell-like faster than local wording implies. |
| `Kahoot` | host-led live session versus learner-paced assigned session, each with different join and timing rules | classroom authority and learning context | `solution`: do not collapse live and async into one wrapper. `concern`: live entry controls appear immediately once host-led session is exposed. |
| `Jackbox` | host-led party product with audience overflow and public-light remote play | stronger streamer/public assumptions and heavier UGC burden | `solution`: `bounded live audience` is a real family. `concern`: bundle escalation and trolling controls are not cheap. |
| `Discord Stage + Community` | passive audience, request-to-speak, moderator approval, later discovery/community obligations | server identity is broader than Prix Guesser likely needs | `solution`: audience bundles can be staged inside one family. `concern`: public/discoverable community is a separate obligation jump. |
| `Chess.com` | official daily cadence, puzzle archive, streaks, tournament history | stronger account, profile, and optimization posture | `concern` mainly: daily cadence can become a serious retention and identity surface without being a full event shell. |

## 10. Negative-case / counterexample note

`[evidenced:cited:external-direct]` The rival framing is not synthetic. Direct counterexamples exist:

- `Jackbox` treats remote and even public play as standard enough to document directly; the public flow is to stream the game and let people "watch, join, and play along"
- `Jackbox` audience participation is not one thin `watch` mode; official guidance says it ranges from voting to more involved interaction
- `Chess.com` daily puzzle includes archive access and streak pressure; this is more than one-off editorial flavor text
- `GeoGuessr` separates `Daily Challenge`, `Event`, and `Tournaments`, but the daily challenge is still a world-scale competition surface rather than a private recap tool

`[assumed:reasoned:internal]` So the packet cannot honestly say:

- `bounded live audience` is obviously later everywhere
- `first audience bundle` is merely cosmetic
- `daily/programmed challenge` is always only cadence and never shell pressure

## 11. Evidence that strengthens the current hypothesis

1. `[evidenced:cited:external-direct]` `Kahoot` keeps `Host live` and `Assign` sharply separate.
   - Live play uses host-led start, screen sharing, join controls, and warning not to share the PIN publicly.
   - Assigned play is learner-paced, link/PIN/QR shared, host-not-present, deadline-based, and explicitly "instead of playing in a live session."
   - This supports `share-by-link / challenge` as a real low-burden family rather than a small live-room variant.

2. `[evidenced:cited:external-direct]` `GeoGuessr` keeps private party, link/invite challenge, live challenge, daily challenge, event, and tournament surfaces distinct.
   - `Play with Friends` groups private lobby and shared-URL challenge together without treating them as the same as live challenge or daily challenge.
   - Invite-only challenges and challenge leaderboard cleanup show that async/share surfaces already have their own bounded-access and results-management grammar.
   - This strengthens the claim that the first low-burden competition can stay mostly between `showcase aftermath` and `share-by-link / challenge`.

3. `[evidenced:cited:external-direct]` `Discord Stage` strongly supports the current `audience bundle inside one family` picture.
   - Members join as muted audience by default.
   - Speaking requires invitation or moderator approval.
   - Moderators can move people between speaker and audience, enable/disable requests, and disconnect members.
   - That is exactly an in-family staging model: same shell, different audience-right bundles.

4. `[evidenced:cited:external-direct]` `GeoGuessr` and `Chess.com` both preserve a real distinction between `daily/programmed challenge` and stronger event shells.
   - `GeoGuessr Daily Challenge` is a recurring global competition.
   - `GeoGuessr Events` are custom maps with custom settings for a specific time frame.
   - `GeoGuessr Tournaments` are scheduled, tiered, bracketed, and trophy-bearing.
   - `Chess.com` daily puzzle and streaks sit beside separate tournament pages, completed tournaments, and trophies.
   - This strengthens the current translation that daily/programmed challenge is cadence by default and event shell only once event-object traits appear.

5. `[evidenced:cited:external-direct]` `Jackbox` supports the claim that `bounded live audience` is real but not low-burden in the same sense as challenge/share or showcase.
   - Public-light remote play requires hiding room codes, considering low-latency settings, and sometimes using passworded rooms.
   - Moderation exists to approve or reject user content before it appears on screen.
   - This makes live audience pressure feel meaningfully heavier than async/share reuse.

## 12. Evidence that weakens or complicates it

1. `[evidenced:cited:external-direct]` `Jackbox` weakens any overly casual reading that `bounded live audience` is a marginal later branch.
   - It explicitly frames remote and public-light play as normal usage patterns for a host-led party game.
   - For a watchability-first product, that makes live audience more central than the residual framing sometimes sounds.

2. `[evidenced:cited:external-direct]` `Jackbox` also weakens the idea that `first audience bundle` is always just a small in-family ordering question.
   - Official guidance says audience play-along differs per game and can range from voting/liking to more involved play-along behavior.
   - Once the bundle crosses into more expressive or game-affecting rights, the shell starts feeling materially different.

3. `[evidenced:cited:external-direct]` `Chess.com` weakens any reading of `daily/programmed challenge` as merely decorative editorial cadence.
   - Daily puzzle resets on a concrete schedule, supports replay of past days, and connects to streak maintenance.
   - Streaks are a public counter shown on the home screen and profile.
   - That is still not a tournament shell, but it is stronger than a thin content calendar.

4. `[evidenced:cited:external-direct]` `GeoGuessr Daily Challenge` also complicates the current wording.
   - It is not just "new content today"; it is a shared global competition surface.
   - That means daily/programmed challenge can become shell-like in social meaning before it becomes a full event object.

5. `[evidenced:cited:external-direct]` The boundary between cadence and event is conditional, not absolute.
   - `GeoGuessr Events` and `Tournaments` show that once custom settings, time windows, eligibility, or trophies are attached, the surface clearly becomes event-like.
   - So a naive "daily challenge is not a shell" rule would be too blunt.

## 13. Comparative verdict

`[assumed:reasoned:internal+external-direct]` Hypothesis status: `survives, but only with narrower wording`.

### 13.1 Wrapper ordering

- `showcase aftermath` and `share-by-link / challenge` still look like the right low-burden first-wrapper competition for this repo's private-first posture.
- `bounded live audience` remains a true wrapper family, but the direct comparisons keep showing it drags room-code safety, moderator controls, latency, and audience-right management forward much faster than the low-burden surfaces do.
- The rival branch therefore weakens the current framing only if Prix Guesser chooses to optimize much sooner for hosted nights, streaming, or public-light watchability beyond the already-private room core.

### 13.2 First audience bundle

- The packet does **not** overturn the residual conclusion that `first audience bundle` begins as an in-family ordering question inside `bounded live audience`.
- But the comparison does sharpen one threshold:
  - `watch`
  - `react / vote / predict`
  - `submit / speak`
- The first two still read as bundle staging inside one family.
- The third begins to look like a shell-significant threshold because moderation, role control, and content-safety expectations jump.

### 13.3 Daily/programmed challenge placement

- `daily/programmed challenge` should still be carried forward as `editorial/programmed cadence by default`.
- But the safe version of that claim is conditional:
  - if it is just recurring official content with shared comparison, archives, or streaks, it is still primarily cadence/return-loop pressure
  - if it gains explicit time windows, event-scoped settings, eligibility, trophies, or separate event history, it crosses into `proto-event shell` or true `event shell` territory
- So the challenge does not reverse chunk A. It forces chunk A and chunk E to be joined by an explicit threshold rule.

## 14. What would falsify or materially re-rank the hypothesis

`[open:reasoned:internal+external-direct]` The current verdict would be materially weakened by any of the following:

- direct comparable evidence that host-led social products usually earn their first non-private value through `bounded live audience` with modest burden, while recap/share challenge surfaces remain secondary
- evidence that `submit / speak` audience rights can be added without a real moderation/control jump
- internal Prix Guesser evidence that recurring hosted nights or watch-live demand appears much earlier than async/share reuse
- internal or external evidence that official recurring challenge becomes the dominant return surface only when it is treated as its own shell rather than as cadence on top of existing wrappers
- a deliberate product-center shift away from private-first trusted groups toward public-light recurring programming

## 15. What remains challengeable

`[open:reasoned:internal]` Keep these explicitly challengeable:

- the exact low-burden order between `showcase aftermath` and `share-by-link / challenge`
- whether `bounded live audience` becomes earlier than expected for the `bounded event shell` archetype
- whether the first audience bundle stops at `watch` or includes `react / vote / predict`
- whether `submit / speak` should still be modeled as `same family, later bundle` or treated as a threshold into a meaningfully different shell
- whether official programmed challenge in Prix Guesser stays cadence-only or reaches the event-object threshold sooner because of weekend framing, hosted nights, or official boards

## 16. Sensitivity implications

`[assumed:reasoned:internal+external-direct]` A later sensitivity pass may now safely protect:

- the low-burden first-wrapper contest is still mostly between `showcase aftermath` and `share-by-link / challenge`
- `bounded live audience` is a real family, but not the same burden class as low-burden recap/challenge surfaces
- `first audience bundle` starts as an in-family staging question
- `daily/programmed challenge` is cadence by default, but only until explicit event-object traits appear

`[assumed:reasoned:internal]` Sensitivity should explicitly flag any prose that:

- treats `bounded live audience` as the universal next wrapper for all archetypes
- treats `interactive audience` as a cheap add-on instead of a thresholded rights bundle
- uses `daily`, `featured`, `programmed`, or `weekend` language as if that alone proves a new wrapper family
- uses `event` language without event-object traits

## 17. What should remain out of sensitivity

`[governing:cited:internal]` Sensitivity should **not** use this packet to force:

- a final global first-wrapper winner
- a final first audience bundle
- a final rule for when every future programmed challenge becomes an event shell
- a concrete event board, event-memory UI, or cadence taxonomy
- a roadmap commitment toward public-light audience or official recurring challenge

## 18. What later converged challenge synthesis must reconcile

`[assumed:reasoned:internal]` Later converged challenge synthesis still needs to reconcile this packet with:

- `05-pre-sensitivity-challenge-e-event-shell-memory-*`
  - because this packet now depends on an explicit `cadence -> proto-event shell -> event shell` threshold
- `05-pre-sensitivity-challenge-b-money-service-*`
  - because official programmed challenge can strengthen the later `editorial/content` branch without proving it
- `05-pre-sensitivity-challenge-c-hosting-branches-*`
  - because live audience and official recurring programming pull different kinds of hosting and moderation obligation forward
- the existing chunk A / chunk E split
  - because `daily/programmed challenge` can no longer be described safely without also naming the event-object threshold from chunk E

## Sources

Local artifacts:

- `05-pre-sensitivity-challenge-a-wrapper-audience-task-spec.md`
- `05-pre-sensitivity-challenge-common-scaffold.md`
- `05-residual-gap-converged-synthesis-output.md`
- `05-residual-gap-chunk-a-wrapper-ordering-output.md`
- `05-residual-gap-chunk-e-event-memory-output.md`
- `05-remaining-gap-response.md`
- `05-next-round-gap-opportunity-register.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`

Direct external sources:

- `GeoGuessr`
  - https://geoguessr.zendesk.com/hc/en-us/articles/4407930336145-What-is-Play-with-Friends
  - https://geoguessr.zendesk.com/hc/en-us/articles/28237315964177-How-do-I-create-a-challenge-for-a-set-number-of-users
  - https://geoguessr.zendesk.com/hc/en-us/articles/18580988424721-How-do-i-Create-a-Custom-Quiz
  - https://geoguessr.zendesk.com/hc/en-us/articles/28237329276049-How-do-I-remove-someone-from-the-leaderboard-of-a-Challenge
  - https://geoguessr.zendesk.com/hc/en-us/articles/4477015980945-What-are-Live-Challenges
  - https://geoguessr.zendesk.com/hc/en-us/articles/360017720198-What-is-the-Daily-Challenge
  - https://geoguessr.zendesk.com/hc/en-us/articles/4407923951249-How-does-Event-work
  - https://geoguessr.zendesk.com/hc/en-us/articles/9785960760977-What-are-Tournaments
- `Kahoot`
  - https://support.kahoot.com/hc/en-us/articles/360039422694-How-to-host-a-live-kahoot
  - https://support.kahoot.com/hc/en-us/articles/360039411334-How-to-assign-a-kahoot-in-web-platform
- `Jackbox`
  - https://www.jackboxgames.com/blog/how-audience-play-along-differs-in-each-jackbox-game
  - https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely-
  - https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work
  - https://support.jackboxgames.com/hc/en-us/articles/15794756085015-How-many-players-can-join-each-game
- `Discord`
  - https://support.discord.com/hc/en-us/articles/1500005513722-Stage-Channels-FAQ
  - https://support.discord.com/hc/en-us/articles/360047132851-Enabling-Your-Community-Server
  - https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery
- `Chess.com`
  - https://support.chess.com/en/articles/8708990-how-do-i-find-the-daily-puzzle
  - https://support.chess.com/en/articles/9714718-what-are-streaks
  - https://support.chess.com/en/articles/8705920-how-do-i-see-my-tournament-stats-and-past-tournaments
