# Session Re-Entry Checklist

Use this checklist before trusting a resumed or compaction-affected session for load-bearing work.

Run it when:

- a session was resumed rather than started fresh
- compaction just happened or is suspected to have happened
- `/status` or UI state seems inconsistent with observed behavior
- the next work is load-bearing for canon, planning, verification, workflow policy, or major code changes

## 1. Working Context

- confirm current `cwd`
- confirm current branch
- confirm whether the worktree is clean
- confirm you are in the repo you think you are in

## 2. Control Surface

- identify the active control surface for the current work:
  - readiness package
  - active phase package
  - research bundle
  - direct code task with no special package
- read the relevant entrypoint again instead of relying on thread memory

Minimum examples:

- readiness work: `.planning/readiness/phase-01-rerun/INDEX.md`
- phase rerun work: active `CONTEXT.md` plus `STATE.md`
- research bundle work: bundle launch spec and latest response/synthesis artifact

## 3. Instruction Scope

- verify which `AGENTS.md` layers are actually needed for this session
- if you do not need `.planning/` or a deeper subtree, prefer repo-root scope only
- do not assume `/status` accurately reflects effective instruction state if behavior contradicts it

## 4. Tooling / Harness Sanity

- verify expected skills or harness surfaces are available if the task depends on them
- verify any repo-local hook or config expectation that matters for the current task
- if behavior looks wrong, assume runtime state may be suspect before assuming repo doctrine is wrong

## 5. Continuity Facts To Recover Explicitly

- current checkpoint or task
- next action
- current blockers
- latest meaningful commit boundary
- whether any worker output is still awaiting review/disposition
- open vs decided distinctions that must not be flattened by summary drift

## 6. Escalation Rule

If two or more of the above checks fail, or if the session feels semantically "off":

- stop relying on the resumed thread as authoritative
- reopen the control surface from repo artifacts
- prefer a fresh thread at the latest clean checkpoint boundary

This checklist is a continuity aid, not a substitute for commits, durable artifacts, or explicit review boundaries.
