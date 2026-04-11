# Exploration Session: Vision, Future, Hosting

Date opened: 2026-04-10
Status: active
Mode: exploratory discussion

## Purpose

Preserve the evolving discussion about what Prix Guesser is becoming across multiple milestones, how future-orientation should shape present planning, and how local play, remote play, async play, hosting, watchability, and long-term sustainability fit together.

## Context Sources

- `/home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/.continue-here.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md`

## Conversation Moves

### Move 1: Resume correction

The session began by resuming from Phase 1 state. The first interpretation leaned too hard on stale `STATE.md` execution language. This was corrected after re-reading the active `.continue-here.md`.

Important correction:

- the correct continuation was exploratory product discussion, not Phase 1 execution
- the checkpoint explicitly preserved the user's desire to think through identity, online play, streamer-friendliness, and multi-stage product trajectory before more execution

### Move 2: Reconstructed current strategic understanding

The resumed understanding was:

- Prix Guesser is not meant to be "GeoGuessr with F1 paint"
- the stronger current shape is an authored, social, F1-specific game-night product
- the roadmap currently behaves more like one deep anchor-mode product
- the docs and checkpoint imply a broader future, more like an F1 party-platform shell with the geography mode as the first serious proof

### Move 3: User clarified the desired long arc

The user clarified that the product should be thought about across stages:

- private/local play first
- remote private play hosted from personal hardware
- asynchronous single-player and multiplayer formats
- later more public hosting
- possible donation-supported sustainability after thorough private testing

The user also emphasized:

- local party mode remains important
- phone controllers, QR join, and watchability are central
- single-player should likely exist early too, though how it relates to local multiplayer remains open
- future orientation should shape how early versions are built

### Move 4: Reframed the design problem as staged product design

The discussion shifted from "what is the one true core experience?" to:

- how the product should be understood at multiple stages
- how later stages should shape early architecture and planning
- how to avoid foreclosing later futures without overengineering the first iteration

The user pushed back, correctly, against treating the product as reducible to one mode.

### Move 5: Hosting and material constraints surfaced

The user raised concrete questions that widened the exploration beyond abstract product vision:

- can web-first still run fully locally on one WiFi network?
- can it be self-hosted remotely from `dionysus`?
- what are the practical transition paths to public hosting?
- what are the limits of personal hardware?
- can transparent capacity limits, queues, or community-supported access be part of the transition story?
- what does a non-manipulative donation model look like?

This shifted the discussion from pure vision toward operational trajectory.

### Move 6: Research wave requested

The user explicitly asked for research agents, then clarified that the research should not be prematurely narrow.

The orchestration was revised accordingly:

- from narrow question prompts
- to exploratory charters designed to widen the solution space and surface tensions

### Move 7: Exploratory research wave launched

Research workspace created:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/00-ORCHESTRATION.md`

Exploratory charters created:

- `specs/01-product-futures.md`
- `specs/02-hosting-transition.md`
- `specs/03-precedents-and-trajectories.md`
- `specs/04-future-aware-planning.md`

Launched agent lanes:

- lane 01 — product futures
- lane 02 — hosting transition
- lane 03 — precedents and trajectories
- lane 04 — future-aware planning

Requested launch settings for the active wave:

- `gsd-phase-researcher`
- `gpt-5.4`
- `high`

Important runtime note:

- one earlier research spawn was started at `xhigh` before the user overrode that policy
- that agent was shut down immediately
- the current wave was re-launched at requested `high`
- requested launch settings are recorded in the orchestration brief
- effective live child-thread reasoning still has not been positively read back from runtime state during execution, so this session must not overclaim that verification

### Move 8: First exploratory findings landed

Completed findings:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/01-product-futures.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md`

Key takeaways from lane 01:

- the product is better understood as multiple wrappers around one authored F1 substrate than as a binary between local party and solo async
- the likely first privately-tested shape is still a watchable host-screen plus controller experience
- solo play currently looks more like a support shell for onboarding, practice, calibration, and between-session habit than the emotional center
- watchability decomposes into several layers: shared legibility, suspense, participation, diagnostic reveal quality, and broadcastability
- a plausible sequence is: watchable private game night first, async/practice shells second, broader party-platform expansion later

Key takeaways from lane 04:

- the repo already has good future-aware behavior in practice, especially in the active Phase 1 `CONTEXT.md`
- the main failure point is translation: rich future-facing context is not consistently carried into canonical artifacts and executable plans
- the strongest low-drag process improvements are:
  - make `Future Awareness` a required `CONTEXT.md` section
  - add a short `Protects` / `Does Not Decide Yet` field to roadmap phases
  - add a short `Non-Foreclosure Checks` section to plans
- the findings argue against heavy governance for now; the emphasis should be light schema that preserves option value

### Move 9: Research-quality critique and standard raised

After reviewing the first-wave outputs, the discussion turned to the quality of research itself.

The concern was not that the first wave was useless. The concern was that the next wave needs to be more responsible in how it handles gray areas.

The user emphasized that future researchers should:

- uncover gray areas rather than smooth over them
- remain open and responsive to questions that emerge during the inquiry
- explicitly mark when they go beyond the original framing
- map their trajectory of inquiry
- show branching paths, dependencies, and related areas of concern

This materially changed the standard for the next wave.

The working methodological conclusion is now:

- the next wave should be narrower in subject than the first wave
- but deeper, more dialectical, and more self-tracking in its reasoning
- the reports should show how the inquiry evolved, not just what conclusion was reached

### Move 10: Second research wave reframed around transition risk and launched

The discussion then moved from general future-orientation to a more difficult cluster of practical transition questions:

- how to scale without risking too much personal money
- whether transparent capacity communication could be part of the product's public posture
- whether paid, donation, or contribution-backed access models are viable
- whether some kind of peer-assisted or cooperative compute could ever play a role
- how product shape, hosting strategy, and trust/risk management constrain one another

The user did not want these treated as if they could be conclusively answered from abstract reasoning alone. The point was to improve the quality of the exploration around them.

That led to a second-wave design principle:

- the research should not just answer prewritten questions
- it should track how the inquiry branches
- it should surface dependencies between design questions
- it should explicitly note when scope expands because the terrain itself forces expansion

Second-wave workspace created:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/00-ORCHESTRATION.md`

Second-wave lanes:

- `01-cooperative-scaling-and-p2p-feasibility`
- `02-funding-access-and-transparency-models`
- `03-public-transition-and-discovery`
- `04-security-trust-and-operational-risk`

Requested launch settings for this wave:

- `gsd-phase-researcher`
- `gpt-5.4`
- `high`

Important runtime note:

- requested launch settings are recorded in the second-wave orchestration brief
- `codex-tui.log` shows child-thread launches under `model=gpt-5.4`
- SQLite readback of the runtime state again failed in-session due the existing readonly issue
- as a result, this session preserves a distinction between requested settings and positively verified effective persisted settings, rather than overstating certainty

### Move 11: Four second-wave findings landed, and an xhigh comparison attempt failed cleanly

After the four primary second-wave lanes were launched, their findings landed under:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/01-cooperative-scaling-and-p2p-feasibility.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/02-funding-access-and-transparency-models.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/03-public-transition-and-discovery.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/04-security-trust-and-operational-risk.md`

The user then proposed a useful methodological test:

- take one of the hardest research questions
- rewrite or supplement its charter using the stricter second-wave standards
- launch an `xhigh` comparison pass so the results can later be compared against the `high` run

The hardest candidate was judged to be the cooperative-scaling / P2P lane because it compresses many different kinds of feasibility into one question:

- browser and NAT realities
- room authority and cheating
- operator complexity
- casual-user friction
- trust and abuse boundaries

A separate comparison charter was created for that purpose rather than mutating the original lane.

However, after launch, the user observed that the spawn banner for the comparison agent reported:

- `Spawned Bohr [gsd-phase-researcher] (gpt-5.4 high)`

That directly conflicted with the requested `xhigh`.

Per the repo's orchestration policy, this was treated as a launch mismatch rather than rationalized away. The comparison lane was shut down immediately, and it must not be counted as a valid `xhigh` pass.

This matters for the session because it reinforces a practical lesson:

- requested spawn settings are not enough
- launch-state verification has to be treated as a first-class concern
- when the runtime and request appear to diverge, the correct move is to stop and preserve the mismatch plainly

### Move 12: Default-agent xhigh works, and first-wave reruns were relaunched on that basis

The user then pressed on a methodological issue that had been blurred by the spawn investigation:

- why was the exploration using `gsd-phase-researcher` at all?
- was that role's planner-oriented prompt actually a bad fit for open exploratory research?

That challenge was correct.

The `gsd-phase-researcher` role is structured around prescriptive, planner-facing phase research. That is not the same thing as the gray-area-preserving exploratory inquiry this session has been trying to do.

To test whether the reasoning-effort problem was role-specific rather than global, a plain `default` agent was launched for the comparison lane.

The user confirmed from the spawn banner that the `default` agent launched at:

- `gpt-5.4 xhigh`

That materially changed the situation:

- `xhigh` is not globally broken
- the earlier failure looks much more like a role-specific or harness-path-specific issue involving `gsd-phase-researcher`
- for exploratory research in this project, `default` agents are likely the better instrument anyway

Once that was clear, the earlier user request about rerunning first-wave research under the stricter standard came back into focus.

The two highest-value reruns were judged to be:

- product futures
- hosting transition

Those two lanes matter most because they shape both:

- what the product is becoming
- how the project's material transition path should be understood

A new comparison workspace was created:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/00-ORCHESTRATION.md`

And two comparison lanes were launched with:

- `agent_type: default`
- `model: gpt-5.4`
- `reasoning_effort: xhigh`

Comparison lanes:

- `01-product-futures-xhigh-comparison`
- `02-hosting-transition-xhigh-comparison`

These reruns are intentionally not simple copies of the old questions.

They are designed to:

- follow the stricter second-wave exploratory standard
- do an independent inquiry pass first
- only then read the original first-wave findings
- explicitly compare what the old pass got right, what the rerun sees more clearly, and where disagreement remains

The `default` comparison lane on cooperative scaling also completed successfully and wrote:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md`

That completion matters because it turns the earlier methodological inference into something stronger:

- the valid `xhigh` comparison pass for this exploration used a `default` agent
- the failed `high`-appearing attempt used `gsd-phase-researcher`
- that does not prove the exact internal cause, but it strongly reinforces the practical rule that exploratory comparison research should use `default` agents in this repo unless there is a strong countervailing reason

### Move 13: Safe-to-clear checkpoint created while first-wave reruns remain in flight

Before clearing context, the session state was tightened one more time.

Two things were worth preserving explicitly:

- the first-wave reruns are still in flight
- the comparison workspace now has an explicit `findings/` directory so the rerun write targets exist cleanly on disk

Rerun agents currently in flight:

- `Maxwell` — `019d7955-d394-7403-acc3-249e86d2d912`
- `Faraday` — `019d7956-8632-7880-b90f-ac166e1b461c`

At the moment this handoff was updated:

- neither rerun findings file had landed yet
- the valid default-agent `xhigh` cooperative-scaling comparison had already landed
- the next session should therefore resume in a true waiting/comparison state rather than a launch-setup state

### Move 14: The reruns landed, and the continuity question became explicit

After that safe-to-clear checkpoint, both first-wave rerun findings landed:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/findings/01-product-futures-xhigh-comparison.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/findings/02-hosting-transition-xhigh-comparison.md`

Both rerun agents were then closed cleanly.

Substantively, the reruns mostly strengthened the earlier map rather than overturning it, but they made several things less neat and more precise:

- `shared substrate plus wrappers` still looks broadly right, but now needs sharper distinctions between:
  - wrapper
  - stage-shape
  - sibling product
  - cross-cutting spectator branch
- the likely first strong proof still looks like a private, watchable, host-led ritual
- solo or async still look more like extensions than the emotional center
- some later F1 futures may share audience and theme without reusing enough underlying grammar to count as one coherent product
- feasibility has to be split more rigorously across technical, operational, adoption, economic, and ethical axes
- hosting transitions are not only traffic problems; they are expectation, accountability, observability, and trust problems

This led directly to a continuity critique from the user:

- does the checkpointing system actually tell a future session how to recover context up to this point?
- or would a future session still have to reread all checkpoints?

That critique was accepted.

The corrected continuity model is now:

- `CHECKPOINT.md` should carry the main resume burden
- the latest delta checkpoint should summarize what changed since the previous checkpoint
- `SESSION.md` should remain the fuller narrative for argumentative texture
- older checkpoints should be optional deeper reads, not the default path

That is not just a formatting preference.

It reflects a more substantive continuity principle:

- future sessions should be able to recover the current state of the exploration without unnecessarily replaying every earlier argumentative turn
- but the richer argumentative trail should still remain available when nuance, reframing, or disagreement matters

### Move 15: High versus xhigh outputs were compared explicitly

Once the reruns had landed and the continuity docs were repaired, the next natural question was whether the `xhigh` passes were actually better than the earlier `high` ones.

That comparison was performed across three available pairs:

- product futures
- hosting transition
- cooperative scaling / P2P feasibility

The result was important, but not simplistic.

The later passes did not mostly overturn the earlier ones.

They mostly:

- confirmed the broad direction
- made the map less neat
- clarified categories that had been too loose
- surfaced dependencies more explicitly
- treated operational, ethical, trust, and governance dimensions as first-class

The strongest pairwise differences were:

- product futures:
  - the rerun sharpened distinctions between wrappers, stage-shapes, sibling products, and spectator branches
  - it was less willing to assume every future F1-adjacent idea belongs inside one coherent product family
- hosting transition:
  - the rerun treated transition as staged accountability and expectation management, not just infrastructure progression
  - it sharpened breakpoints like LAN versus real guests, private hosting versus scheduled availability, and private links versus public accountability
- cooperative scaling:
  - the rerun most clearly improved the framing itself
  - it moved from "is P2P feasible?" toward "what bottleneck is this actually trying to solve, for which actor, at what trust cost?"

But the comparison also led to an explicit epistemic caution:

- this was not a clean experiment on reasoning effort alone

Three variables changed at once:

- `high` to `xhigh`
- `gsd-phase-researcher` to `default`
- weaker exploratory standard to stronger exploratory standard

So the responsible conclusion is not:

- "`xhigh` alone caused the improvement"

It is:

- the later method was better
- `xhigh` may have contributed
- but the session did not isolate reasoning depth as the sole causal factor

That comparison was written to:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/06-high-vs-xhigh-comparison.md`

### Move 16: One clean-room xhigh rerun was launched for public transition and discovery

After comparing the earlier `high` and later `xhigh` passes, the user raised a fair concern:

- the earlier `xhigh` reruns were useful, but they were not clean independent replications

That concern was accepted.

Rather than rerunning everything, the decision was to run exactly one more lane where a reframing result could still materially change the discussion:

- `public transition and discovery`

This lane was chosen because it sits at a hinge between:

- product identity
- wrapper choice
- selective publicness
- discovery grammar
- hosting burden
- moderation and trust burden

A new clean-room workspace was created:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-clean-room-public-transition-xhigh/00-ORCHESTRATION.md`

And a clean-room charter was written:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-clean-room-public-transition-xhigh/specs/01-public-transition-and-discovery-clean-room-xhigh.md`

The clean-room rule for this rerun is stricter than the earlier comparison reruns:

- do not read prior research findings
- do not read comparison artifacts
- do not read cross-lane synthesis artifacts
- do read only the core project documents, the active strategic checkpoint, and the second-wave research standard

The rerun was launched with:

- `agent_type: default`
- `model: gpt-5.4`
- `reasoning_effort: xhigh`
- `fork_context: false`

Requested launch settings were confirmed from `codex-tui.log`.

However, the runtime-state verification path was still imperfect in-session:

- the `threads` schema in `state_5.sqlite` is readable
- but the expected child-thread row for the new agent did not materialize cleanly at the moment of verification

So the session should preserve the same epistemic discipline as before:

- requested settings are confirmed
- effective launch settings should not be overstated unless the user-visible spawn banner or later runtime state confirms them

Current clean-room agent:

- `Pauli` — `019d79a8-fece-7052-aa9b-ac468cff13d6`

This means the exploration has one fresh methodological branch still running:

- not another broad wave
- one targeted clean-room reframing attempt on public transition and discovery

### Move 17: The clean-room public-transition rerun landed and added one more useful reframing

The clean-room rerun completed at:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-clean-room-public-transition-xhigh/findings/01-public-transition-and-discovery-clean-room-xhigh.md`

And the agent was then closed.

The result did not overturn the earlier public-transition lane.

It largely confirmed that:

- public transition should be thought of as layered surfaces, not one switch
- live-room participation should likely stay private longer than some other surfaces
- async challenge sharing remains the strongest candidate for an early semi-public experiment
- spectator or streamer visibility remains a plausible earlier public edge than open live-room participation

But it did add a useful reframing:

- the issue is not only which surface becomes public first
- it is also which surfaces can become visible or shareable without changing what the product is

That shift matters because it pulls public-transition questions back into product-identity questions rather than letting them drift into generic discovery or growth language.

The clean-room rerun also made one live possibility more explicit:

- the project may eventually split into a mostly private room product and a sibling public-facing challenge, showcase, or creator surface

That possibility was not absent before, but the clean-room rerun made it more thinkable and more discussion-worthy.

In that sense, it did produce a genuine reframing result:

- not a reversal
- but a stronger prompt to ask whether one app-level trajectory is hiding a family of related but not identical futures

That comparison was written to:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/07-public-transition-clean-room-comparison.md`

### Move 18: Reflections were preserved and the next inquiry was reframed as a harness / roadmap investigation

Before pivoting again, the current reflections on what the research implies were written out explicitly with a timestamp:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md`

That note preserves the current synthesis about:

- how the research should be used
- why it should not be naively poured into requirements
- which conceptual distinctions now seem to need explicit treatment
- why the next question is about the workflow machinery itself

The next inquiry was then reframed.

Instead of continuing product exploration in the same broad mode, the next fresh-context investigation should ask:

- whether future-awareness and non-foreclosure should be carried mainly through roadmap and artifact changes
- whether the repo-local GSD harness already offers enough leverage
- whether prompts, templates, overlay patches, or some layered combination should be modified

That pivot was recorded as a dedicated handoff:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINTS/10-handoff-for-future-awareness-harness-inquiry.md`

This means the exploration now has a cleaner stopping point for context clearing:

- the strategic research map is preserved
- the interpretive reflections are preserved
- the next investigation target is explicitly defined

## Current Understanding

At this point in the session, the working understanding is:

- Prix Guesser should be treated as a staged product, not a single static app definition
- v1 may still be a tightly scoped private/local-first experience
- but the product should be built with awareness of plausible later wrappers: remote synchronous play, async challenge play, broader party modes, and streamer-adjacent variants
- "watchability" is probably not one thing; it may need to be decomposed by mode and situation
- future-awareness should likely be encoded into the planning system itself, not left as a vague aspiration
- current exploratory research supports a web-first, wrapper-friendly trajectory without requiring all wrappers to arrive at once
- the next exploration pressure point is no longer just "what might the product become?" but "what transition strategies remain viable as the product becomes more public, more loaded, and more operationally risky?"
- the research question about cooperative or peer-assisted scaling remains especially important, but any future attempt to compare reasoning levels on it must first solve the spawn-setting reliability problem
- the methodological issue is now sharper: exploratory research should probably use `default` agents unless there is a strong reason to accept a more workflow-shaped role prompt
- the first-wave reruns largely strengthened rather than reversed the earlier research, but they made the surviving tensions less tidy and more decision-relevant
- the explicit high-versus-xhigh comparison supports continuing with `default` agents, stronger exploratory charters, and selective `xhigh` for the hardest multi-axis questions
- one additional clean-room rerun is now in flight specifically because public transition and discovery looked like the most likely remaining lane to yield a meaningful reframing
- that clean-room rerun has now landed, and its main added pressure is toward thinking in terms of `visibility states` and possible `sibling public-facing surfaces`, not just wrapper order
- the next inquiry is now explicitly about how to encode that future-aware posture into roadmap structure, templates, prompts, or harness patches rather than leaving it as conversation-only insight

## Decisions Made

No product decision has been finalized.

Process decisions made:

- keep the discussion exploratory rather than prematurely solutioning
- maintain a dedicated exploration-session log
- maintain a resumable checkpoint separate from canonical planning artifacts
- run a parallel exploratory research wave with written charters and traceable outputs

## Decisions Explicitly Not Made Yet

- whether the long-term product identity is best framed as "deep anchor mode" or "party platform shell with anchor mode first"
- whether the first deliverable should be browser-only, packaged local-host, website, downloadable app, or some hybrid
- how single-player and local multiplayer should relate in the first version
- how to define watchability operationally across local, remote, async, and streamer scenarios
- how to encode future-orientation into `ROADMAP.md`, `CONTEXT.md`, `AGENTS.md`, or workflow files
- what funding/sustainability model, if any, should eventually exist
- whether peer-assisted or cooperative compute is feasible, tolerable, or wise at all
- how transparent capacity signaling, queueing, contribution, or guarantee models should relate to trust and adoption
- how public transition strategy and security/risk posture constrain one another
- why requested `xhigh` spawns may be landing as `high` in this runtime, and what trustworthy verification path exists before reattempting such comparisons
- exactly how the rerun findings should change the product-vision discussion and any later roadmap or workflow-artifact revisions

## Live Tensions

1. Preserve future expansion without overengineering v1.
2. Support both local party and solo/async play without making the first version incoherent.
3. Think materially about hosting, capacity, and cost while still allowing imaginative exploration.
4. Keep exploratory ambiguity alive without losing operational clarity.

## Linked Artifacts

- Research wave: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/00-ORCHESTRATION.md`
- Second research wave: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/00-ORCHESTRATION.md`
- Comparison charter: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/specs/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md`
- Product futures findings: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/01-product-futures.md`
- Future-aware planning findings: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md`
- Cross-lane reading: `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md`
- Second-wave standards: `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md`
- First-wave xhigh comparison wave: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-first-wave-xhigh-comparisons/00-ORCHESTRATION.md`
- Valid xhigh cooperative-scaling comparison: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-second-wave-scaling-governance/findings/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md`
- High vs xhigh comparison: `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/06-high-vs-xhigh-comparison.md`
- Clean-room public-transition rerun: `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-clean-room-public-transition-xhigh/00-ORCHESTRATION.md`
- Public-transition clean-room comparison: `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/07-public-transition-clean-room-comparison.md`
- Reflections note: `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md`
- Future-awareness harness handoff: `/home/rookslog/workspace/projects/prix-guesser/.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINTS/10-handoff-for-future-awareness-harness-inquiry.md`
