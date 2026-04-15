# Readiness Protocol

This file defines how to operate the readiness package without relying on ambient session memory.

## Read Order

1. [INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md)
2. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
5. the active checkpoint file under [GATES/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES)

## Mandatory Updates

Update `STATUS.md` and `STATE.yaml` whenever:

- the active checkpoint changes
- the next action changes
- a blocker is found or cleared
- commit readiness changes

Update the active gate file whenever:

- evidence is reviewed
- a gate is reopened
- a gate is provisionally or strongly satisfied
- a gate is closed

Update `TASKS.md` whenever:

- a readiness-relevant task changes status
- a new blocking task is discovered
- a task is deferred or reactivated

Update `DEVIATIONS.md` whenever:

- the sequence changes materially
- a checkpoint is skipped, split, or reordered

Update `CHECKPOINT-LEDGER.md` whenever:

- a readiness checkpoint commit is created
- a planned boundary is intentionally postponed

## Commit Protocol

- Prefer checkpoint commits at meaningful reasoning or scope boundaries.
- Before delegating substantial bounded edits, establish an auditable baseline.
- Prefer a checkpoint commit when the current state is coherent and reviewable.
- If the state is not coherent enough to commit, split or park it rather than forcing a bad baseline.
- Do not merge unrelated readiness concerns into one checkpoint just because they happened close together in time.

## Stop / Escalate Conditions

Stop and escalate instead of pushing through if:

- the active checkpoint reveals a deeper checkpoint should become active first
- current canon looks inconsistent enough that readiness work is no longer the right next layer
- the rerun begins reintroducing asymmetries already corrected in `05-gap-closure`
- a worker output cannot be cleanly accepted, revised, parked, or rejected

## Quality Standard

The target is not mere pass/fail clearance.

Each gate should be judged in terms of:

- whether the work is strong enough to carry forward
- whether it would survive later stringent audit
- whether it reduces future re-litigation rather than merely unblocking the next step
