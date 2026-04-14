---
date: 2026-04-13
lane: j-g
lane_name: "Racing / large-event topology follow-up"
orientation: exploratory
delegation_class: replanning-revision-gap-filling
task_variants:
  - 02-lanes/architecture/lane-j-g-output.md
tags:
  - exploratory-audit
  - lane-j
  - follow-up
  - racing
  - heats
  - ghosting
  - engineering-exposure
---

# Lane J-G Task Spec

## Why this follow-up exists

The first-pass real-time lane showed that racing and larger action events often scale through:

- heats
- splits
- ghosting
- qualification
- elimination

But it still needs a more concrete pass on these as engineering/product-topology mechanisms rather than just surface observations.

## Focus

Research how racing or racing-adjacent systems concretely structure large participation without forcing one giant fair-contact field.

Prioritize:

- official docs and sporting-code materials
- official competition or room-setting docs
- official tech or product docs that expose ghosting, splits, qualifiers, divisions, or event shells
- high-quality talks if available

## Candidate source territory

Likely relevant sources include, but are not limited to:

- Trackmania competition / rooms / qualifiers / ghosts
- iRacing sporting code / splits / ghost racing / heats
- Rocket Racing where relevant
- other racing or event-structured competitive systems if they expose concrete mechanisms

Stay focused on the mechanisms that reduce active coupling rather than generic esports structure.

## Questions

- What concrete mechanisms are used to keep large participation tractable?
- How are qualifiers, divisions, heats, ghosting, or feature fields actually structured?
- What exactly is direct evidence and what is product-shape inference?
- Which of these mechanisms look relevant to plausible Prix Guesser racing or action futures?
- Which mechanisms seem more like event-shell solutions than netcode solutions?

## Output target

Write to:
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/02-lanes/architecture/lane-j-g-output.md`

## Required sections

1. `Lane framing`
2. `Reference cases and source audit`
3. `Concrete event-structure and coupling-reduction mechanisms`
4. `Concrete tradeoffs and limits`
5. `What seems relevant to Prix Guesser`
6. `What remains uncertain`
