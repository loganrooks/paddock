# Lane 1 Prompt — Phase 1 Plan Quality

**Used for:**
- Opus 4.6 agent (first pass, 2026-04-08, non-blind — no explicit blind constraints)
- GPT 5.4 xhigh Codex agent (second pass, 2026-04-10, blind)

**Differences between Opus and GPT versions:** The GPT version added explicit blind-audit hard constraints (DO NOT read lane-*.md or SYNTHESIS.md, write to gpt-5.4-parallel/ subfolder). The Opus version wrote directly to the main folder. The core audit questions are identical.

## GPT Blind-Audit Version (as sent)

```
You are performing an INDEPENDENT BLIND AUDIT of Phase 1 plans for the Prix Guesser project. Another auditor has already reviewed this phase; you must NOT read their findings so that your review is uncontaminated.

## Hard Constraints

- DO NOT read any file named `lane-*.md` or `SYNTHESIS.md` in `.planning/audits/`
- DO NOT read `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/` (other lanes)
- Write your report to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/lane-1-plan-quality.md`
- The shared task spec at `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md` is the only audit file you may read

## Your Task (Lane 1: Phase 1 Plan Quality)

Audit all four Phase 1 plans for quality, correctness, and execution-readiness.

These plans were produced through a troubled Codex session with recursive orchestration failures and checker loops. The plans were revised multiple times. There are uncommitted diffs to plans 01-02, 01-03, and 01-04 that represent gap-fix edits from checker feedback that were never independently re-verified.

## What to check

1. Do the plans correctly implement the Phase 1 success criteria from ROADMAP.md?
2. Are there cross-plan contract inconsistencies (e.g., Plan 01-03 referencing schema shapes that Plan 01-02 hasn't defined)?
3. Are all `read_first` entries pointing to files that exist or will exist by the time that plan executes?
4. Is any plan underspecified (executor won't know what to build) or overspecified (locks implementation unnecessarily)?
5. Are the `must_haves.truths` testable and aligned with Phase 1 success criteria?
6. Are acceptance criteria concrete enough to verify?
7. Are there any anti-patterns from known Codex issues: invalid read_first targets, assumptions about files that don't exist yet?

## Files to read

- `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md`
- `.planning/ROADMAP.md` — Phase 1 section for success criteria
- `.planning/REQUIREMENTS.md` — PACK-02, PACK-03, PACK-04, OPS-01
- `.planning/phases/01-authored-round-contract/01-CONTEXT.md`
- `.planning/phases/01-authored-round-contract/01-RESEARCH.md`
- `.planning/phases/01-authored-round-contract/01-VALIDATION.md`
- `.planning/phases/01-authored-round-contract/01-01-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-02-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-03-PLAN.md`
- `.planning/phases/01-authored-round-contract/01-04-PLAN.md`

Run `git diff .planning/phases/01-authored-round-contract/` to see uncommitted changes and assess whether they are improvements.

## Output format

Write your markdown report to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/lane-1-plan-quality.md` with:
- Overall verdict (ready / ready-with-caveats / needs-rework)
- Per-plan assessment
- Cross-plan consistency check
- Assessment of uncommitted diffs
- Specific issues found (severity: blocker / warning / note)
- Recommendations

Write the report directly to the file. Do not print it as your final message — use Write tool or shell redirection to save it to the specified path.
```

## Launch Command (Codex)

```bash
codex exec -m gpt-5.4 -c model_reasoning_effort=xhigh --full-auto \
  -C /home/rookslog/workspace/projects/prix-guesser \
  "$(cat .planning/audits/2026-04-08-pre-execution-review/prompts/lane-1-plan-quality.prompt.md)"
```
