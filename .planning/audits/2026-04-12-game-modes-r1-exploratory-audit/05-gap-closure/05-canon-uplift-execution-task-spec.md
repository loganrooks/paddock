---
date: 2026-04-15
audit_subject: canon_uplift_execution
audit_orientation: exploratory
audit_delegation: delegated
scope: "Execute the canon-uplift patch pass against the live canon docs using the approved patch manifest, while preserving open branches and producing a traceable execution report"
triggered_by: "user request to execute the canon-uplift patch pass after the manifest was prepared"
tags:
  - exploratory-audit
  - gap-closure
  - canon
  - execution
  - patch-pass
  - milestone-2
  - long-arc
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/AGENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-patch-plan.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-lane-i-canon-doctrine-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-lane-ii-roadmap-rerun-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-lane-iii-preserve-reversal-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-lane-iv-inquiry-debt-anti-hardcoding-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/01-CONTEXT.md
---

# 05 Canon Uplift Execution Task Spec

## Task classification and launch intent

Treat this task as:

- `execution/verification`

Recommended launch policy:

- `gpt-5.4`
- `high`

This is an execution pass, not a new synthesis. The reasoning burden is still high because the edits are doctrine-sensitive, but the worker should execute from the manifest rather than reopen the whole inquiry space.

## Ownership

You own exactly these outputs:

- edits to:
  - `.planning/REQUIREMENTS.md`
  - `.planning/LONG-ARC.md`
  - `.planning/PROJECT.md`
  - `.planning/ROADMAP.md`
  - optionally `.planning/phases/01-authored-round-contract/01-CONTEXT.md` only if the manifest’s consistency trigger is genuinely met
- creation of:
  - `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-report.md`

You are not alone in the codebase. Do not revert unrelated existing changes. Work with the current dirty tree as found.

## Core objective

Execute the canon-uplift patch pass so that the live canon:

- reflects the doctrine already earned by the gap-closure and sensitivity trail
- reduces Milestone 2 carry-forward distortion
- preserves farther long-arc doctrine more explicitly
- keeps still-open rankings visibly open
- does not smuggle preserve-only or reversal-sensitive branches back in as active commitments

## Required onboarding sequence

Read these in order and keep their significance explicit:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
   Why:
   repo-wide runtime policy, quality bar, delegation assumptions, and horizon expectations.

2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
   Why:
   planning-local canon rules, artifact discipline, future-flexibility statusing, and `LONG-ARC.md` handling.

3. [05-canon-uplift-patch-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-patch-plan.md)
   Why:
   this is the governing execution manifest. Follow its source authority stack, cross-file invariants, execution order, and file-by-file patch intents.

4. [05-post-sensitivity-response-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-post-sensitivity-response-plan.md)
   Why:
   explains why this is a canon-uplift response, not a narrow cleanup.

5. [05-canon-uplift-milestone-2-steering-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-milestone-2-steering-proposal.md)
   Why:
   gives the concrete uplift goals and the rationale for each target file.

6. Sensitivity outputs:
   - [05-sensitivity-lane-i-canon-doctrine-output.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-lane-i-canon-doctrine-output.md)
   - [05-sensitivity-lane-ii-roadmap-rerun-output.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-lane-ii-roadmap-rerun-output.md)
   - [05-sensitivity-lane-iii-preserve-reversal-output.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-lane-iii-preserve-reversal-output.md)
   - [05-sensitivity-lane-iv-inquiry-debt-anti-hardcoding-output.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-sensitivity-lane-iv-inquiry-debt-anti-hardcoding-output.md)
   Why:
   these justify the most sensitive distinctions and tell you what must stay open versus what should become more explicit.

7. Live canon files:
   - [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)
   - [LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md)
   - [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
   - [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
   - [01-CONTEXT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/01-CONTEXT.md)
   Why:
   these are the files you are actually editing or deciding not to edit.

## Non-negotiable execution rules

- Follow the execution order in the patch plan unless you discover a concrete conflict that must be reported.
- Do not widen Phase 01 scope.
- Do not add a new roadmap phase or reorder milestones.
- Do not choose final winners for still-open branch questions.
- Do not use umbrella words in a way that reintroduces hidden commitments:
  - `challenge`
  - `showcase`
  - `hosted`
  - `premium`
  - `membership`
  - `event`
  - `reviewed`
  - `curated`
  - `unsupported`
- Do not touch `01-CONTEXT.md` unless the canon edits would otherwise leave rerun vocabulary misleading.
- If you do touch `01-CONTEXT.md`, keep it minimal and rerun-facing only.

## Required edit posture by file

### `REQUIREMENTS.md`

Primary goal:
- reduce quiet future-ranking through example density

What to do:
- add or sharpen a non-ranked framing for later capability families
- separate challenge, recap/review, and event-memory implications more clearly
- keep seam and deferral language doing explicit non-foreclosure work

What not to do:
- do not turn `v2 Requirements` into a long essay
- do not introduce positive commercialization or public-discovery wording

### `LONG-ARC.md`

Primary goal:
- make farther doctrine more explicit and less dependent on audit-memory

What to do:
- sharpen wrapper-family, audience-right, host-identity, money-family, contribution/discovery, and layered-memory doctrine

What not to do:
- do not convert doctrine into roadmap commitments
- do not close rival later branches

### `PROJECT.md`

Primary goal:
- rebalance the compact story so it stops over-naming a subset of futures

What to do:
- widen wrapper examples
- clarify Milestone 2 pressure families
- preserve the open first-post-private-wrapper question

What not to do:
- do not turn `PROJECT.md` into policy detail or a second `LONG-ARC.md`

### `ROADMAP.md`

Primary goal:
- convert earned doctrine into carry-forward constraints without widening the Milestone 01 spine

What to do:
- add clearer overview-level seam protection
- clarify open decisions
- prevent phase language from overcommitting host/service/shell/memory doctrine

What not to do:
- do not add execution scope
- do not make Phase 5 or Phase 6 read like closure of shell or event-memory questions

### `01-CONTEXT.md`

Primary goal:
- only preserve vocabulary alignment if needed

What to do:
- minimal consistency touch only if necessary

What not to do:
- do not import broader canon detail into Phase 1 scope

## Required output report

Write:

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-canon-uplift-execution-report.md`

The report must include:

1. `Files changed`
2. `Files intentionally left untouched`
3. `Patch operations executed by file`
4. `Why each change was justified`
5. `What remained explicitly open`
6. `What was intentionally not introduced`
7. `Whether 01-CONTEXT.md was touched and why`
8. `Residual risks or follow-up checks`

## Stop and report conditions

Stop and report instead of freehanding a solution if:

- the manifest and live canon appear to conflict materially
- a needed edit seems to require choosing a winner the manifest says must stay open
- a change to one canon file appears to force roadmap widening
- `01-CONTEXT.md` seems to need more than a minimal consistency touch

## Completion condition

The task is complete only when:

- the canon docs are patched
- the edits still preserve the open and deferred branches required by the manifest
- the execution report exists
- no unrelated files were reverted
