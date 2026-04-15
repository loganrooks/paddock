---
date: 2026-04-14
audit_subject: sensitivity_docket
audit_orientation: exploratory
audit_delegation: delegated
scope: "Map audience-right thresholds and first audience bundle pressure into the core planning docs"
triggered_by: "05-sensitivity-docket-a2-audience-right-thresholds-task-spec.md"
tags:
  - exploratory-audit
  - gap-closure
  - sensitivity
  - docket
  - audience
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-docket-a2-audience-right-thresholds-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-control-note.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-docket-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-pre-sensitivity-challenge-converged-synthesis-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-pre-sensitivity-challenge-a-wrapper-audience-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/01-CONTEXT.md
---

# 05 Sensitivity Docket A2: Audience-Right Thresholds Output

## 1. Docket framing

- Mode: `synthesis`
- Classification: `initial architecture research/planning`
- Question: what may the live planning docs safely say about later audience ladders without implying that stronger audience rights are already chosen, cheap, or near-term?
- Scope:
  - `bounded live audience` as a real later wrapper family
  - the still-open `first audience bundle`
  - the threshold between `watch`, light `react / vote / predict`, and `submit / speak`
  - ripple into canon doctrine and rerun-facing planning surfaces
- Non-goals:
  - no final first audience bundle
  - no final ranking between low-burden wrappers and bounded audience shells
  - no commitment to public spectator participation
  - no audience moderation or role model design
- Stop condition: enough mapped guidance exists for later sensitivity lanes to tell what each doc may imply, must not imply, and must keep explicit.

`[governing:cited]` The gate artifact allows sensitivity to assume that audience rights have a meaningful ladder and that `submit / speak` is not obviously a cheap add-on. It does **not** allow sensitivity to assume the first audience bundle is closed or that `submit / speak` is safely just a later in-family extension.

## 2. Target feature pressure

- `bounded live audience` is a real wrapper family and not the same burden class as low-burden recap or challenge surfaces.
- `first audience bundle` still begins as an in-family staging question inside that family.
- The safe staging picture is now narrower:
  - `watch`
  - light `react / vote / predict`
  - `submit / speak`
- The first two may still be described as bundle staging inside one family.
- The third now looks `shell-significant` because moderation, role control, and content-safety expectations jump.

## 3. Current gate classification

- `direct doctrine`
  - `bounded live audience` is real.
  - audience rights are laddered rather than flat.
  - watchability and spectator-facing future seams must not be mistaken for one shared participant-rights model.
- `bounded-open`
  - whether the first audience bundle stops at `watch` or includes light `react / vote / predict`
  - whether `bounded live audience` becomes earlier than expected for some hosted-night or bounded-event archetypes
- `inquiry debt`
  - the exact point where `submit / speak` becomes a different shell instead of a later bundle extension
  - the minimum moderation, authority, and role-control bundle that stronger audience rights would require in Prix Guesser specifically
- `reversal-sensitive`
  - any wording that quietly treats stronger interactive audience rights as cheap, default, or already-earned
  - any wording that smuggles public-live participation back in through vague `spectator` or `interactive audience` language

## 4. Current survivor and strongest rival(s)

### Current survivor

`[assumed:reasoned:cited]` Carry forward the laddered view:

- `watch` and light `react / vote / predict` may still be treated as possible in-family staging inside `bounded live audience`
- `submit / speak` should be treated as threshold pressure, not as an ordinary extension that later docs can casually assume

### Strongest rivals

- `bounded live audience` is the obvious next wrapper after private rooms across all archetypes
- all audience rights can be discussed as one generic `spectator` or `interactive audience` bucket
- `submit / speak` is just a later feature toggle on the same shell and does not change obligation class

`[assumed:reasoned]` The docket does not accept those rivals as current steering, but it must keep them visible enough that later sensitivity can catch accidental hard-coding in either direction.

## 5. Why this pressure matters

- `PROJECT.md` and `LONG-ARC.md` already use terms such as `watchable`, `spectator-facing`, `audience-readable`, and `bounded public`. Without threshold discipline, those terms can drift from `legibility and narrower rights` into `strong participation is expected later`.
- `ROADMAP.md` already carries `later audience-only entry`, `spectators in the room`, and `bounded audience shells that may be earned later`. That makes roadmap wording especially vulnerable to flattening audience rights into one generic future.
- `REQUIREMENTS.md` preserves visibility and presentation seams, but if those seams are read too casually they can be mistaken for a commitment to audience interactivity rather than a protection against foreclosure.
- `01-CONTEXT.md` is Phase 1 steering input. If it starts importing audience-role nuance beyond seam protection, it will widen Phase 1 in the wrong place.

`[assumed:reasoned]` The real risk is not only wrong vocabulary. It is silent burden drift on:

- join-flow design
- role and authority modeling
- moderation and trust assumptions
- visibility-state promises
- later shell ordering

## 6. Relevant planning surfaces

- `PROJECT.md`
  - owns the project-center, milestone-arc, and future-aware posture language where `spectator-facing shells`, `watchability`, and `visibility state` are already named
- `LONG-ARC.md`
  - owns the durable doctrine for room/wrapper layering, visibility ladders, streamer/spectator posture, and obligation thresholds
- `ROADMAP.md`
  - owns the practical carry-forward notes where audience-only entry, spectators in the room, and bounded audience compatibility can accidentally become implied commitments
- `REQUIREMENTS.md`
  - owns the protected seams and deferrals that should preserve audience-right flexibility without upgrading it into shipping scope
- `01-CONTEXT.md`
  - owns the active rerun input posture for Phase 1 and therefore must stay strict about what later wrappers are preserved versus what later audience rights are actually in scope

## 7. Per-doc implication map

| Doc | What is safe | What would overcommit | What would silently foreclose | What must remain explicit |
| --- | --- | --- | --- | --- |
| `PROJECT.md` | It may describe later spectator-facing or bounded-public shells as wrappers around private-first play, and may imply that later audience surfaces could have narrower rights than full players. | Treating `spectator-facing shell` as if it already includes `submit / speak`, or as the likely first proved wrapper after private rooms. | Treating watchability as either one permanent shared truth surface or mere passive viewing forever, with no room for later rights staging. | The first audience bundle is still open; stronger rights are a different burden class; public-live participation is not chosen. |
| `LONG-ARC.md` | It may state that visibility and audience rights are staged, that publicness is an obligation shift, and that later audience-readable shells can exist without becoming the default identity model. | Using `spectator` or `streamer-adjacent` language as if participation rights are already broad, cheap, or close to Milestone 1/2 scope. | Talking only about visibility levels while omitting rights ladders, which would let `audience`, `participant`, and `speaker` drift back together. | `watch` and light `react / vote / predict` may stay in-family; `submit / speak` remains threshold pressure; stronger audience rights pull moderation and service obligations forward. |
| `ROADMAP.md` | It may preserve `later audience-only entry` as distinct from player join, keep the host screen compatible with bounded audience shells, and treat spectators as readability pressure rather than a promised role set. | Letting Phase 4 or Phase 5 wording imply audience controllers, audience submissions, speaking rights, or public spectator participation as already-earned product scope. | Removing or weakening the join-vs-audience distinction, which would harden future audience shells into the same lifecycle as player seats. | v1 remains private-room first; future audience seams are preserved, not selected; any stronger audience rights require later explicit planning. |
| `REQUIREMENTS.md` | It may preserve audience-right flexibility indirectly through `SEAM-05`, `SEAM-07`, and the visibility/public-trust deferrals without adding a new audience-specific ship gate. | Turning spectator or audience participation into an explicit near-term requirement, or using seam language as proof that interactive audience rights are on the committed path. | Reducing the seam language to mere display compatibility, which would hide the fact that rights and access policy must remain separable too. | Visibility, staged reveal, and shared-surface compatibility are preserved seams; stronger participation, public trust, and moderation remain deferred. |
| `01-CONTEXT.md` | It may preserve topology-sensitive future wrappers and non-universal viewer surfaces as future-awareness notes only. | Importing audience-role models, moderation controls, or public challenge surfaces into Phase 1 steering as if they were relevant execution scope now. | Treating future wrapper preservation as if only async or spectator read-surfaces matter, with no later audience-right threshold at all. | Phase 1 keeps only non-foreclosure protection here; audience-right laddering belongs to later wrapper and room doctrine, not current phase scope. |

## 8. What each doc may safely imply

- `bounded live audience` is a real later family and is heavier than low-burden recap or share-by-link surfaces.
- `watchability`, `spectator-facing`, and `audience-readable` language may preserve later shells without deciding that those shells are next, broad, or interactive.
- Later audience rights may be narrower than full player rights and may require distinct entry or role flows.
- Light audience interaction such as `react / vote / predict` may remain thinkable inside one family without being chosen as the committed first bundle.

## 9. What each doc must not imply

- `submit / speak` is already part of the chosen first audience bundle.
- `interactive audience` is a cheap generic add-on to any spectator-facing shell.
- public-live or public-light audience participation is already on the roadmap just because watchability and spectator seams are preserved.
- player join, rejoin, seat claim, and audience-only entry are functionally the same lifecycle.
- `spectator`, `audience`, `participant`, and `speaker` are interchangeable nouns.

## 10. What must remain explicit

- the first audience bundle is still open
- the safe in-family staging picture currently covers `watch` and possibly light `react / vote / predict`, not stronger rights by default
- `submit / speak` remains a shell-significant threshold question
- stronger audience rights would change moderation, role-control, and obligation posture
- preserving future audience shells is not the same as committing to them

## 11. Semantic drift watchpoints

- `watchable`
  - means shared legibility and reveal payoff, not proof that a later audience can actively affect play
- `spectator-friendly` or `spectator-facing`
  - means a later shell seam is preserved, not that spectator rights are already broad or chosen
- `audience`
  - should not be used without clarifying whether it means `watch`, `react / vote / predict`, or `submit / speak`
- `interactive audience`
  - is too vague unless the actual rights bundle is named
- `join`
  - must stay distinct across `player join`, `rejoin`, `seat claim`, and `audience-only entry`
- `bounded public`
  - describes visibility and trust scope, not a guaranteed participation model

## 12. Sensitivity lane routing

- `Lane I: canon doctrine`
  - inspect `PROJECT.md`, `LONG-ARC.md`, and `REQUIREMENTS.md` for places where `spectator`, `watchable`, or `bounded public` language could imply stronger audience rights than the gate allows
- `Lane II: roadmap and rerun`
  - inspect `ROADMAP.md` and `01-CONTEXT.md` for places where join-flow, host-screen, or later-wrapper wording could flatten player and audience roles or quietly promote stronger interactive rights
- `Lane IV: inquiry debt and anti-hard-coding`
  - protect the still-open questions around whether the first bundle stops at `watch` or includes light `react / vote / predict`, and whether `submit / speak` is a threshold into a meaningfully different shell

`[assumed:reasoned]` This docket is not a primary input to `Lane III`. The main preserve-only and reversal-sensitive burden here is already captured as anti-hard-coding and doctrine protection rather than as a preserved rival branch that should be promoted separately.

## 13. What remains open after this docket

- whether the first audience bundle stops at `watch` or includes light `react / vote / predict`
- whether `bounded live audience` becomes earlier than expected for some hosted-night or bounded-event archetypes
- whether `submit / speak` should ultimately be modeled as `same family, later bundle` or as a threshold into a different shell
- what minimum moderation, authority, and role-control commitments stronger audience rights would require
- how later audience-right decisions interact with the `first explicit shell` and `event-memory` dockets without collapsing those questions together
