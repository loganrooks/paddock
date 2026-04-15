---
date: 2026-04-14
audit_subject: next_round_gap_opportunity_register
audit_orientation: exploratory
audit_delegation: self
scope: "Granular gap and opportunity register for designing the post-05 remediation research round"
triggered_by: "creator request after 05 verification reruns and epistemic-opening review"
tags:
  - exploratory-audit
  - gap-closure
  - gap-register
  - opportunity-register
  - research-design
  - provenance
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-verification-r2-a-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-verification-r2-b-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-epistemic-opening-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-context-and-plan.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-handoff-gap-review.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-synthesis.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md
---

# 05 Next-Round Gap And Opportunity Register

## Purpose

`[governing:cited:internal]` This register exists so the next remediation-round specs do not justify themselves vaguely by pointing at the whole `05-gap-closure` bundle.

`[governing:reasoned:internal]` Each next-round spec should cite one or more specific gap/opportunity IDs from this register and explain:

- which IDs it is addressing
- why those IDs call for the chosen packet shape
- what the packet is explicitly not trying to close

`[governing:reasoned:internal]` This register is not itself the next-round topology. It is the justification layer that the next-round topology must be built from.

## Reading rules

`[governing:cited:internal]` The key provenance distinctions from the framework apply here:

- `internal`
  grounded only in repo-local artifacts
- `external-direct`
  directly grounded in outside-repo sources engaged in the current artifact
- `external-traceable`
  grounded only through repo-local artifacts that themselves cite outside sources

`[governing:reasoned:internal]` In this register, many entries are intentionally `internal` or `internal+external-traceable`, because the point is to identify where further inquiry is still needed rather than to pretend that the register itself closes those inquiries.

## Status shorthand

- `accepted-doctrine`
  Good enough to carry forward without reopening right now.
- `reopen-for-research`
  Needs a new comparative inquiry packet.
- `patch-only`
  Needs better integration or phrasing, but not a new packet by itself.
- `blocked-for-sensitivity`
  Cannot be treated as closure-grade input to the next sensitivity pass yet.
- `keep-open`
  Should remain explicitly unresolved even after the next packet.

## Scope classes

- `project-facing inquiry gap`
  A substantive Prix Guesser product, architecture-carry-forward, or operating-model gap.
- `research-document / epistemic-quality gap`
  A weakness in how the existing research artifacts are grounded, translated, or exposed.
- `bridge artifact gap`
  A missing synthesis or sequencing artifact needed to move responsibly to the next stage.

## Project-facing inquiry gaps

### GCO-00: Archetype-indexed mature-product synthesis is still missing

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `blocked-for-sensitivity`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  mature-product round as a whole, later converged synthesis, rerun-input canon
- `identified in`
  `05-gap-closure-context-and-plan.md`, `05-handoff-gap-review.md`
- `statement`
  The project still lacks one mature-product answer expressed in archetype and shell terms rather than generic feature buckets.
- `why this is a gap`
  The handoff and later review both established that social topology and lived archetypes are first-class structure, not just context for mode ideas.
- `current foreclosure risk`
  Future closure work could slide back into generic monetization/community language that ignores couch play, private online sync, solo ritual, and bounded event shells.
- `what should be researched`
  Every next-round packet should explicitly state how its findings vary by archetype or where they do not.
- `not yet justified`
  Any mature-product synthesis that speaks as if one default user experience exists.
- `good packet shape`
  governing requirement across all next-round packets, then finalized in the converged synthesis

### GCO-00A: Content flywheel and content-supply model remain underclosed

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  content model, contribution posture, long-arc editorial planning
- `identified in`
  `05-gap-closure-context-and-plan.md`
- `statement`
  The project still does not clearly answer what the actual content supply model is: authored drops, evergreen library expansion, community-assisted contribution, or some intentional mix.
- `why this is a gap`
  Content cadence and content supply are central to both repeat return and long-arc staffing/obligation assumptions.
- `current foreclosure risk`
  The project may imply a content operation it has not actually chosen or resourced.
- `what should be researched`
  Reference designs for evergreen library growth, editorial drops, curated contribution, and how those models shape repeat return.
- `not yet justified`
  A firm commitment to community contribution or a pure internal-only posture.
- `good packet shape`
  either a dedicated content-flywheel packet or a combined packet with curated contribution if scope stays disciplined

### GCO-01: Wrapper sequencing remains underclosed

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `blocked-for-sensitivity`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  community shell packet, mature-product synthesis, later sensitivity
- `identified in`
  `05-gap-closure-verification-r2-a-output.md`, `05-epistemic-opening-output.md`
- `statement`
  The bundle productively identified bounded-public shell families, but it still closes the order of first post-private wrappers too early.
- `why this is a gap`
  The current bundle often moves from “these shell families exist” to “this shell should come first” without enough direct comparative inquiry.
- `current foreclosure risk`
  Quietly ratifying one shell order as doctrine could distort later roadmap, wrapper design, and audience assumptions before that ordering is actually tested.
- `what should be researched`
  Compare `showcase aftermath`, `share-by-link / challenge`, `bounded live audience`, and narrower hybrids as distinct wrapper families rather than as a single ladder.
- `not yet justified`
  Any final rank ordering of those shells.
- `good packet shape`
  one focused comparative packet on post-private wrapper sequencing

### GCO-02: Audience-right granularity is too compressed

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `blocked-for-sensitivity`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  community shell packet, rights model, moderation assumptions
- `identified in`
  `05-epistemic-opening-output.md`
- `statement`
  The bundle separates player rights from audience rights, but still tends to compress audience rights into too simple a ladder.
- `why this is a gap`
  `async read`, `watch live`, `react/predict`, `light co-presence`, and `full participation` are not the same thing and may imply different wrappers, moderation burdens, and product postures.
- `current foreclosure risk`
  A too-simple audience-rights model can overstate live public shells or understate lighter share/read surfaces.
- `what should be researched`
  Comparative rights models and control surfaces for bounded spectatorship, async read/share, and mixed spectator-participant shells.
- `not yet justified`
  A single canonical audience-right ladder beyond the basic player/audience separation.
- `good packet shape`
  either combined with `GCO-01` or as a tightly coupled companion section inside that packet

### GCO-03: "Ambient community layer" is over-compressed

- `scope class`
  `project-facing inquiry gap`
- `type`
  opportunity
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  community shell packet, later community roadmap, long-arc carry-forward
- `identified in`
  `05-epistemic-opening-output.md`
- `statement`
  The phrase `ambient community layer` is currently doing too much work and may be hiding several distinct later surfaces.
- `why this is an opportunity`
  Reopening this category may stop later community work from hardening around one vague terminal rung.
- `current foreclosure risk`
  Treating a bundle of different middle and later community surfaces as one “later community thing.”
- `what should be researched`
  Distinguish durable room/event memory, curated recap/showcase, group-history surfaces, public-light read surfaces, and broader ambient community environments.
- `not yet justified`
  Treating those surfaces as one unified later stage.
- `good packet shape`
  include as a secondary inquiry inside the wrapper/community packet, not as its own lane

### GCO-04: Promise grammar is cleaner than the ranking it now supports

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `blocked-for-sensitivity`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  money/support packet, support posture, premium posture, user expectation management
- `identified in`
  `05-gap-closure-verification-r2-a-output.md`, `05-epistemic-opening-output.md`
- `statement`
  The bundle productively reframed money questions around promise burden and obligation thresholds, but it narrows later money-family ordering too quickly.
- `why this is a gap`
  Separating `support`, `access`, and `service obligation` is a real gain, but it does not by itself justify the later ranking among support-only, support-plus-beta, queue/capacity tools, hosted convenience, and editorial programming.
- `current foreclosure risk`
  Later canon or roadmap work may silently privilege one money-family branch without enough comparative outside inquiry.
- `what should be researched`
  Compare promise surfaces and obligation ladders across support-only, beta-window, queue/capacity, hosted-convenience, and editorial/content families.
- `not yet justified`
  Exact pricing, exact tiering, or a final later premium-family ranking.
- `good packet shape`
  one focused comparative packet on promise grammar and economic ladders

### GCO-05: Earliest ethical support posture vs later premium family remains unresolved

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  money/support packet, public messaging, transition-stage risk
- `identified in`
  `05-epistemic-opening-output.md`
- `statement`
  The bundle does not yet cleanly separate the earliest honest support posture from the later question of which premium/service families are worth preserving long term.
- `why this is a gap`
  These are related but distinct decisions, and collapsing them risks either over-designing money too early or foreclosing later viable families.
- `current foreclosure risk`
  Prematurely treating `hosted convenience` or `editorial programming` as the dominant later branch before the transition-stage posture is clarified.
- `what should be researched`
  What early support/capacity language is honest and low-obligation, and what later branch families remain worth preserving without being chosen now.
- `not yet justified`
  Turning the transition-stage answer into the long-term monetization answer.
- `good packet shape`
  keep inside the promise-grammar packet, but track as a distinct sub-gap

### GCO-06: Contribution posture and discovery are still under-specified

- `scope class`
  `project-facing inquiry gap`
- `type`
  opportunity
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  content/community boundary, content model, community posture
- `identified in`
  `05-epistemic-opening-output.md`, `05-gap-closure-context-and-plan.md`
- `statement`
  The middle space between pure internal authorship and open publishing remains under-described.
- `why this is an opportunity`
  This affects whether outside contributions become curated partners, reviewed submissions, directory-listed but unsupported additions, or something else entirely.
- `current foreclosure risk`
  Later content/community design may default to a binary of `internal only` versus `open platform`.
- `what should be researched`
  Curated contribution postures, endorsement/removal criteria, activation rules, and what discovery actually promises.
- `not yet justified`
  A full creator marketplace or open submission platform.
- `good packet shape`
  a targeted packet or a disciplined section inside the content-supply packet

### GCO-07: Host-ecology comparison is still only partially grounded

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `blocked-for-sensitivity`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  host-ecology packet, transition hosting, long-arc hosting seams
- `identified in`
  `05-gap-closure-verification-r2-a-output.md`, `05-gap-closure-verification-r2-b-output.md`, `05-epistemic-opening-output.md`
- `statement`
  The bundle is strong on rejecting full browser P2P as the main path and on preserving trusted operator-hosted authoritative rooms, but it does not yet adequately close the comparison between trusted operators, sanctioned mirrors / collectives, and official hosted convenience.
- `why this is a gap`
  This is exactly where the current bundle most clearly moves from a valid family space into an under-grounded ranking.
- `current foreclosure risk`
  Hardening one transition ladder too early could distort architecture seams, support obligations, and long-arc hosting posture.
- `what should be researched`
  Real operator models, promoted volunteer/community hosts, host standards, compatibility discipline, backup/recovery obligations, emergency access, shutdown posture, and host-labeling clarity.
- `not yet justified`
  A final ranking between sanctioned mirrors / collectives and official hosted convenience.
- `good packet shape`
  one narrow comparative host-ecology packet

### GCO-08: Promotion thresholds and trigger conditions are missing

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  all project-facing packets, later synthesis
- `identified in`
  `05-epistemic-opening-output.md`
- `statement`
  The bundle often names branches and rough orderings without specifying what empirical conditions would move a branch up or down.
- `why this is a gap`
  Without trigger conditions, rankings become static preferences instead of testable provisional judgments.
- `current foreclosure risk`
  Later planning may treat current preferences as doctrine rather than as thresholds contingent on adoption, burden, moderation, or demand signals.
- `what should be researched`
  For each reopened branch, identify concrete triggers such as operator adoption, room-start reliability, moderation burden, queue frequency, creator burden, or visible audience demand.
- `not yet justified`
  Any ordering that is not tied to named change conditions.
- `good packet shape`
  this should be a required section in every next-round packet, not its own lane

### GCO-08A: Transition identity is still under-described

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  host-ecology packet, long-arc hosting posture, later product identity
- `identified in`
  `05-epistemic-opening-output.md`, `05-gap-closure-verification-r2-a-output.md`, `05-gap-closure-verification-r2-b-output.md`
- `statement`
  The bundle still does not clearly answer whether `trusted operators`, `sanctioned mirrors / collectives`, and `official hosted convenience` are one transition ladder or partially different product identities.
- `why this is a gap`
  Ranking branches is different from deciding whether they are even comparable branches of the same story.
- `current foreclosure risk`
  The next round could overfocus on ordering and miss that different hosting branches may imply different trust, community, or support identities.
- `what should be researched`
  Which hosting branches solve the same problem, which solve different problems, and whether they belong on one ladder or in separate identity families.
- `not yet justified`
  Treating all non-P2P hosting branches as one simple progression.
- `good packet shape`
  required sub-question inside the host-ecology packet

### GCO-08B: Archetype-to-burden translation is still missing

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  all next-round packets, later converged synthesis
- `identified in`
  `05-gap-closure-context-and-plan.md`, `05-handoff-gap-review.md`
- `statement`
  The project now knows archetypes matter, but the remaining closure work still does not consistently translate each branch through those archetypes' different burden profiles.
- `why this is a gap`
  A shell, support posture, or hosting branch that works for a trusted recurring group may be wrong for solo ritual or bounded event use.
- `current foreclosure risk`
  A next-round packet may sound archetype-aware while still silently assuming one burden profile.
- `what should be researched`
  For each reopened branch, how burden, moderation, support expectation, and value shift across private recurring groups, private online sync, solo ritual, and bounded public/event shells.
- `not yet justified`
  Any recommendation that is not explicit about its archetype fit or non-fit.
- `good packet shape`
  required comparative section in every project-facing packet, then reconciled in synthesis

### GCO-08C: First-value versus later-value remains under-separated

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  all project-facing packets, converged synthesis
- `identified in`
  `05-epistemic-opening-output.md`, `05-gap-closure-context-and-plan.md`
- `statement`
  The bundle still slides too easily between `what matters first in the transition phase` and `what might matter later in the mature product`.
- `why this is a gap`
  A branch can be worth preserving long term without being the right first move, and vice versa.
- `current foreclosure risk`
  The next round may either over-design late branches too early or prematurely foreclose them because they are not first.
- `what should be researched`
  For each reopened branch, distinguish `first-value`, `later-value`, and `preserve-without-prioritizing`.
- `not yet justified`
  Treating transition-stage preference as the same judgment as long-term mature-product priority.
- `good packet shape`
  required evaluative split inside every project-facing packet

### GCO-08D: First repeat-return loop is still not decisively chosen

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `blocked-for-sensitivity`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  recurrence packet, retention story, content cadence
- `identified in`
  `05-gap-closure-context-and-plan.md`, `05-handoff-gap-review.md`
- `statement`
  The project still lacks a decisive answer about which repeat-return loop matters first: room folklore, personal mastery, editorial return, league-like recurrence, or replay/review.
- `why this is a gap`
  The audit established that recurrence is layered, but did not close which layer should actually anchor the mature product earliest.
- `current foreclosure risk`
  Roadmap and canon language may smuggle in one recurrence model without having chosen it consciously.
- `what should be researched`
  Compare repeat-return layers across the key archetypes and tie them to content, memory, and burden assumptions.
- `not yet justified`
  Treating `retention` as one generic bucket or assuming a first repeat-return loop by default.
- `good packet shape`
  either a dedicated recurrence packet or an explicit recurrence section inside the content/promise packets

### GCO-08E: Room/group/event memory vocabulary still lacks product-shape translation

- `scope class`
  `project-facing inquiry gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  recurrence, community shells, premium/support posture, later canon updates
- `identified in`
  `05-gap-closure-context-and-plan.md`
- `statement`
  The audit clarified that room, group, event, and content memory are distinct layers, but the mature-product thread has not yet translated that into a concrete product-shape answer.
- `why this is a gap`
  Recurrence, community, and support branches all depend on which memory layer is actually primary in the user-facing story.
- `current foreclosure risk`
  Canon may preserve the seams abstractly while still failing to state what the memory model should feel like in actual play.
- `what should be researched`
  Which memory layer matters for each reopened branch and what surfaces it implies: recap, streaks, room folklore, group history, event carry-over, or library/history views.
- `not yet justified`
  Treating seam language itself as if it already answered the product question.
- `good packet shape`
  required cross-packet translation concern, then explicit synthesis treatment

## Research-document / epistemic-quality gaps

### GCO-09: Internal vs external grounding is still too easy to blur

- `scope class`
  `research-document / epistemic-quality gap`
- `type`
  gap
- `status`
  `patch-only`, `keep-open`
- `source basis`
  `[evidenced:cited:internal]`
- `primary surfaces`
  existing research documents, future specs, future outputs, verification practice
- `identified in`
  `05-gap-closure-verification-r2-a-output.md`, `05-gap-closure-verification-r2-b-output.md`, `review-trail-framework.md`
- `statement`
  The existing research documents repeatedly showed how easy it is for repo-local syntheses to look externally grounded when they are only transitive support.
- `why this is a gap`
  Poorly marked grounding origin encourages false closure and weak downstream review.
- `current foreclosure risk`
  Future packets may repeat the same mistake unless source-basis and directness are called out explicitly.
- `what should be patched`
  Next-round specs and outputs should use typed provenance plus explicit source-basis markers and state whether they are closure-grade or only hypothesis-shaping.
- `not yet justified`
  Treating `not this document` as equivalent to `external research`.
- `good packet shape`
  framework/process carry-forward, not a standalone research lane

### GCO-09A: Reference translation is still too implicit

- `scope class`
  `research-document / epistemic-quality gap`
- `type`
  gap
- `status`
  `patch-only`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  all next-round research packets, especially community/money/hosting
- `identified in`
  `05-epistemic-opening-output.md`
- `statement`
  The bundle still does not consistently expose why a reference design is analogous to Prix Guesser, what transfers, and what does not.
- `why this is a gap`
  Even direct external research can mislead if the translation layer stays implicit.
- `current foreclosure risk`
  Future packets may import polished examples whole instead of extracting only the relevant concern or pattern.
- `what should be patched`
  Every next-round packet should include a short `reference translation` section stating:
  - what is analogous
  - what is not analogous
  - what is borrowed as concern versus as solution
- `not yet justified`
  Treating a cited reference as self-justifying for Prix Guesser.
- `good packet shape`
  packet requirement, not a standalone research lane

### GCO-09B: Failure and negative-case evidence are under-sampled

- `scope class`
  `research-document / epistemic-quality gap`
- `type`
  gap
- `status`
  `reopen-for-research`, `keep-open`
- `source basis`
  `[assumed:reasoned:internal]`
- `primary surfaces`
  next-round external research packets, especially support/community/hosting
- `identified in`
  `05-epistemic-opening-output.md`
- `statement`
  The current source mix still leans toward official docs and intended patterns, and under-samples failure modes, abandonment, burnout, operator pain, and user misread.
- `why this is a gap`
  Product docs are strong on intended roles and weak on what breaks, gets dropped, or creates hidden burden.
- `current foreclosure risk`
  The next round may still overfit to polished reference designs and underweight practical failure.
- `what should be researched`
  Add targeted negative-case material where available: postmortems, incident writeups, operator retrospectives, maintainer lessons, and evidence of middle-model failure.
- `not yet justified`
  Assuming official documentation alone is enough to rank burden-sensitive branches.
- `good packet shape`
  source-class requirement across relevant packets, not a standalone lane

## Bridge artifact gaps

### GCO-10: The converged mature-product synthesis does not exist yet

- `scope class`
  `bridge artifact gap`
- `type`
  gap
- `status`
  `blocked-for-sensitivity`
- `source basis`
  `[evidenced:cited:internal]`
- `primary surfaces`
  post-research synthesis, sensitivity analysis, canon carry-forward
- `identified in`
  `05-gap-closure-verification-r2-a-output.md`, `05-gap-closure-verification-r2-b-output.md`, `05-gap-closure-synthesis.md`
- `statement`
  The current `05-gap-closure-synthesis.md` is a topology setter, not the actual converged mature-product synthesis that the bundle still needs.
- `why this is a gap`
  Sensitivity analysis and later canon updates need one place that states what is settled, what is preferred but challengeable, what is unresolved, and what is conditional.
- `current foreclosure risk`
  Downstream work may consume a planning topology artifact as if it were the final reconciled answer.
- `what should be produced`
  A post-remediation converged synthesis that distinguishes:
  - settled doctrine
  - preferred but challengeable branch
  - unresolved branch
  - empirical trigger
  - possible later spike candidate, if any
- `not yet justified`
  Running the next sensitivity pass as if mature-product closure already exists.
- `good packet shape`
  synthesis artifact after the new packets, not before

### GCO-11: Sensitivity must not outrun closure

- `scope class`
  `bridge artifact gap`
- `type`
  gap
- `status`
  `blocked-for-sensitivity`
- `source basis`
  `[evidenced:mixed:internal+external-traceable]`
- `primary surfaces`
  next sensitivity pass, roadmap/canon carry-forward
- `identified in`
  `05-gap-closure-verification-r2-a-output.md`, `05-gap-closure-verification-r2-b-output.md`, `05-epistemic-opening-output.md`
- `statement`
  The next sensitivity pass should not treat the current mature-product bundle as fully closed.
- `why this is a gap`
  Several ranking and sequencing questions remain deliberately reopened.
- `current foreclosure risk`
  Performing sensitivity too early would give false authority to unresolved branches.
- `what should happen instead`
  Only run sensitivity after the reopened inquiry packets and the converged synthesis exist, or explicitly scope sensitivity to accepted doctrine only.
- `not yet justified`
  Sensitivity over partially reopened material as if it were closure-grade.
- `good packet shape`
  carry-forward constraint, not its own research packet

## Packet design implications

`[governing:reasoned:internal]` A next-round spec should cite specific IDs from this register, not the whole bundle.

`[governing:reasoned:internal]` The current register suggests five likely packet families:

1. `wrapper sequencing and audience-right granularity`
   Primary IDs:
   - `GCO-00`
   - `GCO-01`
   - `GCO-02`
   - `GCO-03`
   Secondary coupling:
   - `GCO-08`
   - `GCO-08B`
   - `GCO-08C`

2. `promise grammar and economic ladders`
   Primary IDs:
   - `GCO-00`
   - `GCO-04`
   - `GCO-05`
   Secondary coupling:
   - `GCO-08`
   - `GCO-08B`
   - `GCO-08C`

3. `host ecology and promotion thresholds`
   Primary IDs:
   - `GCO-00`
   - `GCO-07`
   - `GCO-08`
   Secondary coupling:
   - `GCO-08A`
   - `GCO-08B`
   - `GCO-08C`

4. `curated contribution and discovery posture`
   Primary IDs:
   - `GCO-00`
   - `GCO-00A`
   - `GCO-06`
   Secondary coupling:
   - `GCO-03`
   - `GCO-05`
   - `GCO-08C`

5. `content supply and first repeat-return loop`
   Primary IDs:
   - `GCO-00`
   - `GCO-00A`
   - `GCO-08D`
   Secondary coupling:
   - `GCO-06`
   - `GCO-08B`
   - `GCO-08C`
   - `GCO-08E`

`[governing:reasoned:internal]` Research-document and bridge constraints that every next-round spec should inherit:

- `GCO-09`
  source-basis must be explicit
- `GCO-09A`
  reference translation must be explicit
- `GCO-09B`
  failure / negative-case evidence should be sampled where relevant
- `GCO-08`
  each packet must state trigger conditions
- `GCO-10`
  packet outputs are inputs to a later converged synthesis, not substitutes for it
- `GCO-11`
  no packet may describe itself as making the bundle sensitivity-ready on its own

## Minimum citation rule for the next round

`[standard:reasoned:internal]` Every next-round task spec should include a short section named `Gap justification` or equivalent, and that section should:

- cite the exact `GCO-*` IDs the packet addresses
- summarize why those IDs call for this packet
- say what the packet is *not* trying to close
- state whether the packet is expected to produce:
  - direct external grounding
  - internal synthesis only
  - or a conditional spike-candidate register

`[standard:reasoned:internal]` If a next-round spec cannot name specific `GCO-*` entries, it is probably too vague to launch.
