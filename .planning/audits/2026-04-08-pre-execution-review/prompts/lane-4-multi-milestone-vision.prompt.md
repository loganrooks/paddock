# Lane 4 Prompt — Multi-Milestone Vision

**Used for:**
- Opus 4.6 agent (first pass, 2026-04-08, non-blind)
- GPT 5.4 xhigh Codex agent (second pass, 2026-04-10, blind)

## GPT Blind-Audit Version (as sent)

```
You are performing an INDEPENDENT BLIND AUDIT of multi-milestone vision for Prix Guesser. Another auditor has already reviewed this; you must NOT read their findings so that your review is uncontaminated.

## Hard Constraints

- DO NOT read any file named `lane-*.md` or `SYNTHESIS.md` in `.planning/audits/`
- DO NOT read `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/` (other lanes)
- Write your report to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/lane-4-multi-milestone-vision.md`
- The shared task spec at `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md` is the only audit file you may read

## Critical stakeholder context

- Private-only project, NO commercialization
- Building for personal use and F1 fan friends (non-technical)
- v1: local party game (cast to TV, phones as controllers)
- v2+: online hosted play, more game modes, team play, daily challenges
- Creator wants to design for maximal success without over-engineering v1
- The content model (authored F1 rounds) is the core asset that should compound over milestones

## Your Task (Lane 4: Multi-Milestone Vision)

1. Does the authored round model from Phase 1 support future mode families (team play, async challenges, daily modes, era-themed packs)?
2. Does the Phase 3 room architecture support transition from local → online → hybrid?
3. Does Phase 2 judging/scoring support future answer surfaces (section, corner, composite)?
4. Will Phase 4-5 UI choices support future modes without rewrites?
5. Does Phase 6 session data capture support long-term content quality feedback loops?
6. What should milestones 2 and 3 look like? Are the v2 requirements the right set?
7. What's missing from v2 requirements? (Content authoring tools, pack sharing, session replays, statistics, themed seasons)
8. Cheap v1 decisions that save expensive v2 rewrites? (Database, state management, content format, API shape)
9. Biggest risks to project being fun and getting used? (Fun risks, effort risks, complexity risks — NOT commercial)

## Files to read

- `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md`
- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md` (especially v2 section)
- `.planning/ROADMAP.md`
- `discovery/14-gsd-seed.md` (if it exists)

## Output format

Write your markdown report to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/lane-4-multi-milestone-vision.md` with:
- v1 architecture risk assessment
- Recommended cheap v1 decisions that protect v2+
- 3-milestone arc sketch
- Missing requirements or phases
- Biggest risks to project success
- Concrete recommendations with priority (critical / high / medium / low)

Write the report directly to the file. Do not print it as your final message.
```
