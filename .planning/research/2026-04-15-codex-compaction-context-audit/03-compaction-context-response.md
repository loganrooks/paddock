# Compaction Context Response

Date: 2026-04-15  
Status: active response note

This artifact integrates:

- [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md)
- [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md)

Its purpose is not to restate everything. Its purpose is to say what this repo should actually take forward.

## What Still Holds From 01

- `[e:c:i+d]` There is no official compaction-specific hook surface to rely on for post-compaction recovery or forced file injection ([01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:12), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:22)).
- `[e:c:i+d]` Compaction can happen before the visible meter reaches zero because the meter is not showing raw empty context window, and post-compaction headroom does not need to return to `100%` because the thread is replaced with a compacted history rather than reset to blank ([01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:15), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:16)).
- `[e:c:i+d]` Repo-local instruction loading is real prompt-budget pressure. The AGENTS chain from project root to cwd can materially consume budget, so start directory and instruction discipline matter ([01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:17), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:25)).

## Missed Lever: Compaction Prompt Override

- `[e:c:d]` Official Codex configuration also exposes a real compaction-steering surface: `compact_prompt` and `experimental_compact_prompt_file`. These do not provide lifecycle hooks, but they do allow the compaction prompt itself to be overridden from config.[^codex-config-ref]
- `[e:c+r:i+d]` That means the earlier "no hook, therefore only checkpoints/artifacts/fresh threads matter" framing was too narrow. The correct framing is:
  - there is still no official pre/post-compaction hook
  - but there is a documented prompt-level lever that can bias what the compactor preserves
  - and for this repo, that lever is worth using alongside durable artifacts and clean checkpoints

## What 02 Changes

- `[e:c:i+d]` The live unresolved issue surface is narrower than the first pass suggested. Some problems emphasized in `01` are no longer good current unresolved signals because they were fixed, closed, or explicitly addressed ([02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:60), [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:61), [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:62)).
- `[e:c:i+d]` The unresolved open surface now clusters more sharply around:
  - compaction/runtime recovery failures
  - instruction-loading and observability mismatches
  - resume/session-continuity gaps
  rather than just "meter weirdness" or "early compaction" in the abstract ([02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:28), [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:43), [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:51)).
- `[e:c:i+d]` The biggest practical addition from `02` is a stronger warning about resumed-session fidelity. "Resumed thread" and "same effective workspace-derived context" should not be treated as equivalent assumptions for this repo ([02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:54), [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:72)).

## Current Repo Position

- `[e:c:i]` This repo already has the right basic defensive posture: keep important continuity in durable repo artifacts, not in ambient thread memory ([INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md:5), [.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:14)).
- `[e:c:i]` This repo also already treats prompt budget and AGENTS bloat as real risks rather than theoretical ones ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:203), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:208)).
- `[a:r:i+d]` The main remaining weakness is not doctrinal misunderstanding. It is operational discipline: using clean checkpoints, fresh-thread boundaries, explicit re-entry verification, and careful cwd choice consistently enough that compaction and resume quirks do not silently corrupt planning work.

## What We Should Do

1. `[d:c:i]` Keep the readiness package as the durable carrier for pre-rerun continuity, not as optional backup text ([PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md:61), [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md:1)).
2. `[d:c+r:i+d]` Prefer fresh-thread boundaries at meaningful checkpoints rather than letting one thread absorb repeated compactions. This follows both current repo checkpoint doctrine and the unresolved open issue surface around resume/recovery fragility ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:46), [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:72)).
3. `[d:c+r:i+d]` Treat `/status` and similar UI surfaces as advisory. Verify effective behavior when it matters, especially after resume or around compaction-adjacent failures ([02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:40), [02-recent-open-issues-scout.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/02-recent-open-issues-scout.md:73)).
4. `[d:c+r:i+d]` Be deliberate about session start directory. Starting under `.planning/` or the readiness subtree should be a conscious choice, because it changes the AGENTS chain and therefore prompt-budget load ([01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:25), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:72)).
5. `[d:c+r:i+d]` When re-entering a resumed session for load-bearing work, run a short continuity verification:
   - cwd is correct
   - expected AGENTS layer is the one actually needed
   - expected skills/tools/instruction behavior are present
   - no odd compaction or auth failure symptoms are being misread as repo-local state drift
6. `[d:c+r:i+d]` Use a compact-prompt override intentionally. For the current readiness work, the compaction prompt should preserve:
   - active control surface path
   - checkpoint / current task / next action
   - blockers and open questions
   - open vs decided / preserve-only distinctions
   - latest meaningful commit boundary when it is part of current work state
7. `[d:c+r:i+d]` Do not wait for a compaction-hook solution. None is currently documented, and the actionable mitigations already available to this repo are stronger than wishful hook assumptions.

## What We Do Not Need To Do

- `[d:c+r:i]` We do not need to react by stuffing more standing recovery doctrine into root `AGENTS.md`.
- `[d:c+r:i]` We do not need to treat every recent open Codex issue as a blocker for this repo.
- `[d:c+r:i+d]` We do not need to assume compaction itself is malfunctioning just because the meter compacts "early"; that part is largely explained by documented/source-observable behavior.

## Suggested Next Follow-Through

- `[d:c:i]` Operationalize this bundle into a short session re-entry / continuity check that can be used when resumed or post-compaction work feels suspect.
- `[d:c+r:i+d]` Use a temporary readiness-specific compact prompt now, but treat project-wide compact-prompt design as a separate later harness/governance task rather than quietly letting the readiness-specific version become the permanent repo default.
- `[p:r:i]` If later issues or regressions accumulate, append them in this bundle instead of reopening the whole question from scratch.

## External Works Cited

[^codex-config-ref]: OpenAI Developers, "Configuration Reference – Codex", documented keys `compact_prompt` and `experimental_compact_prompt_file`, https://developers.openai.com/codex/config-reference
