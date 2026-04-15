# Recent Open Issues Scout

Date: 2026-04-15
Status: launch-ready

This task extends the existing `2026-04-15-codex-compaction-context-audit` bundle.

It is not a separate research session. It is a follow-up lane prompted by the need to look beyond the first five recent issues and understand whether the unresolved open-issue surface from roughly the last one to two weeks changes how this repo should approach Codex compaction, observability, and workflow resilience.

## Goal

Scout unresolved open issues from approximately the last `14` days in the `openai/codex` issue tracker, prioritizing:

- compaction and context behavior
- AGENTS / instruction loading
- `/status` or context observability
- session continuity
- resumed-thread behavior
- hooks or workflow surfaces that affect recovery or continuity

Where issue comments materially add guidance, workarounds, or clarifications, include those too.

## Questions To Answer

1. What unresolved open issues from roughly the last `14` days are most relevant to this repo's current concerns?
2. Do issue comments provide credible:
   - workarounds
   - maintainer clarifications
   - scope-limiting details
   - indications that a problem is broader or narrower than the issue title suggests?
3. Does the recent unresolved issue surface materially change how this repo should:
   - think about compaction risk
   - use AGENTS and readiness artifacts
   - choose thread/checkpoint boundaries
   - approach observability and trust in `/status` or related UI surfaces?
4. Is one broad takeaway emerging, or do the unresolved issues break into distinct operational themes?

## Scope Rules

- Look at open unresolved issues from approximately the last `14` days.
- Prioritize the last `7` days first if issue volume is high.
- Do not try to exhaustively summarize every issue if the volume is too large.
- Instead, cluster by relevance and pull forward the issues most likely to change repo behavior.
- Include comments only where they materially change interpretation or provide actionable advice.

## Output

Write:

- [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md)

The output should contain:

- short scope note explaining how many issues were scanned and how they were filtered
- grouped relevant unresolved issues
- comment-derived guidance where meaningful
- direct repo-specific implications
- a short conclusion on whether the earlier `01` artifact should be materially qualified by this scout

## Source Priorities

Priority order:

1. `openai/codex` open issues from approximately the last `14` days
2. issue comments on those issues
3. official docs only where needed to contrast issue reports with known documented behavior

## Claim / Citation Requirements

This is a load-bearing planning/process artifact.

Use the repo claim/citation scheme for load-bearing claims where it materially helps:

- `[type:support:basis]`

External-direct claims should use markdown footnotes plus `External Works Cited`.

If a conclusion depends mainly on issue comments rather than issue titles or official docs, make that explicit.

## Relevant Local Inputs

- [00-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/00-launch-bundle-spec.md)
- [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md)
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)

## Non-Goals

- do not drift into a full Codex product review
- do not propose repo changes unrelated to current compaction/context continuity concerns
- do not treat open issue reports as equivalent to official guarantees
