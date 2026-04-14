# Audit Execution Plan — Game Modes Round 1

Date: 2026-04-12
Status: Drafted before launch
Companion documents:
- `AUDIT-PROPOSAL-game-modes-r1.md`
- `AUDIT-SPEC-game-modes-r1.md`

## Short answer

The proposal was not yet "perfect to launch" because the operational layer was still implicit.

This file closes the main operational gaps:
- whether subagents are used
- when they are used
- what they are tasked with
- where task specs live
- where outputs land
- how prompts are written
- what the likely roadmap is beyond Round 2
- which clarifying questions are already resolved enough to proceed

## Clarifications already resolved

These points are settled enough to formalize:

- **Multi-round structure:** this is not capped at two rounds. It is an iterative process with at least two rounds and potentially more until the judgments stabilize enough to trust.
- **Round 1 scope:** execute Round 1 only for now. Later rounds are driven by creator feedback on Round 1.
- **Audit orientation:** `no named subject × exploratory × self` remains the right Round 1 framing.
- **Architecture discussion:** allowed, but secondary. Product-and-game-design stays primary; architecture is flagged where it meaningfully pressures a mode.
- **Context framing:** do not force every mode into one primary context. Treat context plurality, tension, variant forks, and category exceedance as part of the audit.
- **Virality vs retention:** explicitly distinguish shareable meme energy from deeper replay/return loops.
- **User-origin / pressure-testing signal:** useful as a reading aid, but not a quality ranking.
- **Calibration terminology:** there are two different things that had been conflated:
  - **Round 1 orientation / initial engagement** — happens inside Round 1, before and during distributed exploration
  - **Between-round recalibration** — happens after the user responds to Round 1 output

## Recommended launch posture

Launch Round 1 with a **hybrid orchestration model**:

1. **Main thread owns the root spec, shared standards, and final synthesis.**
2. **Several subagents should be launched in Round 1 for grouped exploration.**
3. **Subagents handle grouped exploratory work, not the final comparative judgment.**
4. **Subagents remain optional only at the lane level** — if a proposed lane is too small, too entangled, or not worth splitting, keep that work local rather than forcing a lane.

This is the right compromise because:
- the "sense of good" is still being developed in direct conversation with the user
- the grouped middle work is parallelizable
- the final judgment should stay centralized so the audit does not fracture into incompatible value systems
- the main risk is lane drift, which is solved by a root task spec plus a shared lane scaffold

## Proposed artifact layout

If launched, create a session directory here:

`.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/`

Proposed contents:

```text
.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/
├── 01-round-1/game-modes-r1-task-spec.md
├── 01-round-1/lane-common-scaffold.md
├── 01-round-1/round-1-orientation.md
├── 02-lanes/round-1/lane-a-task-spec.md
├── 02-lanes/round-1/lane-a-output.md
├── 02-lanes/round-1/lane-b-task-spec.md
├── 02-lanes/round-1/lane-b-output.md
├── 02-lanes/round-1/lane-c-task-spec.md
├── 02-lanes/round-1/lane-c-output.md
├── 02-lanes/round-1/lane-d-task-spec.md
├── 02-lanes/round-1/lane-d-output.md
├── 01-round-1/round-1-output.md
├── 01-round-1/round-1-self-eval.md
└── 03-next-round/round-2-prompts.md
```

Notes:
- Lane count is provisional. If the early Round 1 work shows only 2 or 3 clean bundles, reduce it.
- If a lane is not used, its files simply are not created.
- `01-round-1/round-1-output.md` is the deliverable for user feedback.
- `01-round-1/round-1-self-eval.md` records what Round 1 thinks it got right, wrong, or left underexplored before your feedback lands.
- `03-next-round/round-2-prompts.md` is not Round 2 itself; it is the structured carry-forward artifact.

## Execution sequence

### Phase 0 — Pre-launch setup

Before any subagents:
- lock the Round 1 classification
- create the session directory
- write the main Round 1 task spec
- write a shared lane scaffold capturing common standards, lenses, anti-goals, and output requirements
- write lane task specs derived from the root spec + shared scaffold

The root Round 1 task spec is the main spec for the audit as a whole.

The lane specs are child specs for the auditors. They should share a common core, but the **actual prompt given to each auditor must still be standalone and complete**. The scaffold is an authoring aid, not a substitute for full lane prompts.

### Phase 1 — Round 1 orientation and distributed exploration

This begins in the main thread, then fans out to the auditors.

Inputs:
- `IDEAS-INDEX.md`
- `HANDOFF.md`
- `IDEAS-game-modes.md`
- `IDEAS-cross-cutting.md`
- `IDEAS-platform.md`
- checkpoint files as needed

Outputs:
- `01-round-1/round-1-orientation.md`

What the orientation pass must do:
- map the current mode families
- identify context profiles and tensions
- identify which modes are already more pressure-tested by the user
- identify where the current category grid is already breaking down

Subagents can and should still launch in Round 1. The point of the orientation pass is not "wait until later to delegate." The point is to make sure the delegation is grounded in the actual current corpus rather than in my first guess from memory.

### Phase 2 — Run lane work

Spawn auditors for the grouped lanes.

Recommended agent policy:
- `gsdr-auditor -> gpt-5.4 -> high`

Reason:
- these are verification/exploration style tasks, not initial architecture planning
- the repo policy prefers `gpt-5.4` with `high` reasoning for execution/verification agents

The main thread should announce the mapping before each spawn using the required format:

`gsdr-auditor -> gpt-5.4 -> high`

The main thread should also explicitly classify each delegated task before spawning it:
- `execution/verification` for grouped audit lanes

### Phase 3 — Central synthesis

This stays local in the main thread.

Inputs:
- `01-round-1/round-1-orientation.md`
- all lane outputs
- direct reads of any load-bearing source files needed to resolve conflicts

Outputs:
- `01-round-1/round-1-output.md`
- `01-round-1/round-1-self-eval.md`
- `03-next-round/round-2-prompts.md`

Why keep synthesis local:
- the comparative judgment across the whole portfolio is the most value-laden part
- it should preserve one coherent evolving standard of what counts as "good"
- it is also where creator-facing communication quality matters most

### Phase 4 — Between-round recalibration

This is the step that happens **after** your feedback on Round 1.

Inputs:
- `01-round-1/round-1-output.md`
- `01-round-1/round-1-self-eval.md`
- your direct responses, objections, corrections, and preference signals

Outputs:
- updated round structure if needed
- `03-next-round/round-2-prompts.md` revised or expanded

This is the correct place for "calibration" in the sense you mean: the project calibrates against your response to what Round 1 produced.

## Default lane responsibilities

These are **provisional templates**, not hard commitments. Early Round 1 work can change them.

### Lane A — Authored prompt / reveal modes

Likely scope:
- `Words of Wisdom`
- `Sound-based Games`

Questions:
- What makes the reveal structure work?
- What replay depends on authored content versus player variation?
- What are the strongest variant forks?
- Which forms are good locally, sync, async, or as event-driven content?

### Lane B — Judgment / information modes

Likely scope:
- `The Stewards' Room`
- `Team Principal's Desk`
- `The Grid Walk`
- `Relive the Moment` as a content lens

Questions:
- How much partial information is needed?
- Is the mode fun because of debate, judgment, cooperation, or all three?
- How niche is the expertise floor?
- Which contexts preserve the tension versus flatten it?

### Lane C — Player-generated expression modes

Likely scope:
- `Paddock Fashion`
- `Meme Prompts`

Questions:
- Do the players really become the content?
- What makes the reveal sing?
- What is immediately funny versus structurally replayable?
- What community/remix potential exists without forcing it?

### Lane D — Real-time action / chaos modes

Likely scope:
- `Pit Stop Co-op`
- `The Verstappen Game`
- `Talibantonelli / Osama bin Russell`

Questions:
- Is the core loop actually fun beyond the pitch?
- How do elimination and spectators work?
- How do vehicle ladders, unlocks, and challenge modes change replay?
- Which contexts are natural, which are stretch, which are distortions?

## Prompt-writing guide

The prompt to any subagent should be the **full task spec contents**, not a short summary.

### Main task spec should include

- classification and fit assessment
- read set
- Round 1 purpose
- explicit anti-goals:
  - not a go/no-go audit
  - not a yes/no fan-likes-it test
  - not a feasibility-first pass
- required audit lenses:
  - context profile / tension map
  - user situation lens
  - virality vs retention
  - community / online potential
  - launch-gap lens
  - category exceedance
- output shape

### Lane task specs should include

- lane scope and excluded scope
- exactly which mode families it owns
- the shared audit questions for that lane
- instruction to treat current entries as possibility families, not fixed designs
- instruction to surface promising variant forks
- instruction to notice where the current category grid breaks
- instruction to distinguish user-origin pressure-testing from actual quality
- required output sections

### Shared lane scaffold should include

- the exploratory orientation and fit assessment
- anti-goals
- common audit lenses
- common formatting/output expectations
- rules about context plurality, virality vs retention, and user-origin signal

The scaffold is where shared prompt language lives.

Each actual lane spec should then add:
- the specific scope
- the specific mode families
- the specific lane questions
- the lane output path

### Prompt style rules

- do not ask for yes/no judgments when a conditional or comparative answer is stronger
- do not collapse to feasibility
- do not assume one ideal fan or one ideal context
- do not optimize every mode for universal compatibility
- do not treat user-origin as authority
- do surface tensions, tradeoffs, and variant forks explicitly

## Output-writing guide

### Lane outputs should contain

- lane framing / orientation
- mode-by-mode findings
- variant / fork opportunities
- context profile / tension map
- virality vs replayability read
- community / online potential
- what to park for later research
- what the current categories did not capture
- recommendations for central synthesis

### Round 1 synthesis should contain

- orientation
- what is here
- possibility expansion
- mode audits
- portfolio gaps and composition
- new proposals
- open threads
- what this round parks for later research
- questions/prompts for the next round

## Roadmap beyond Round 2

The plan should not assume the work ends after Round 2.

Likely roadmap:

### Round 1
- distributed exploratory audit of existing mode families
- bounded first-wave new proposals
- centralized synthesis and self-evaluation

### Round 2
- revisit originals plus best Round 1 additions
- incorporate creator feedback
- apply stronger comparative judgment and self-evaluation

### Round 3 (if needed)
- focused deep dives on the most load-bearing or contested mode families
- possibly one round focused just on context tensions, community potential, or session composition

### Round 4+ (if needed)
- platform-level consolidation:
  - what ships first
  - what belongs to the hidden discovery layer
  - what wants community/UGC
  - what wants event/calendar support
  - what could later justify monetization without forcing it now

Exit condition:
- not "two rounds completed"
- but "judgments feel coherent enough that the next planning decisions would benefit from them rather than still being warped by unresolved confusion"

## Remaining gaps after this execution plan

After this file, the remaining gaps are relatively minor:

- the exact lane count and lane boundaries are still intentionally provisional during the early part of Round 1
- the exact session slug can be adjusted if you want different naming

Those are acceptable remaining gaps. They do not block launch.
