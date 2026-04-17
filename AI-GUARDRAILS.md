# AI Guardrails

This document defines how agentic AI should be used on this project.

It is intentionally broader than `AGENTS.md`. `AGENTS.md` should tell agents what rules to obey while acting. This file explains the operating guardrails and signoff expectations behind those rules.

## Core principle

Use AI to increase rigor and speed, not to bypass judgment.

The failure mode to avoid is not only bad code. It is bad decisions landing quickly and looking authoritative because they were written fluently.

## Human signoff required

The following should not be treated as autonomous agent territory:

- legal posture changes
- branding decisions involving F1 marks or public-facing identity
- monetization, donations, paid tiers, or access model changes
- roadmap or milestone restructuring
- canon-doc changes that materially alter project scope or doctrine
- destructive cleanup of large artifact sets
- database/schema migrations or irreversible content rewrites
- infrastructure, hosting, or secrets-management changes
- public copy that makes safety, legal, or affiliation claims

Agents may help prepare these decisions, but the final decision should remain explicitly human-owned.

## Safe agent autonomy

The following are generally safe for bounded autonomous execution:

- narrow code changes with clear verification paths
- documentation drafting grounded in local source-of-truth docs
- gap reviews, audit setup, and traceability scaffolding
- research synthesis where evidence quality is explicitly labeled
- localized refactors, tests, and cleanup that do not change product doctrine

## Required shape for non-trivial agent tasks

Before delegating non-trivial work, make sure the task has:

- a bounded scope
- named target files or artifact outputs
- a clear classification
- a stated verification method
- a clear distinction between evidence, inference, and recommendation

For coding work, also make clear whether the agent is:

- reading only
- proposing
- editing
- verifying

## Planning and research hygiene

- Treat ideas as design terrain when the creator is still exploring possibility space.
- Do not force one universal ontology across different games or systems.
- Treat creator examples as probes unless the creator explicitly promotes them into categories or requirements.
- When a user repeatedly corrects the same narrowing tendency, promote that correction into a governing artifact instead of rediscovering it lane by lane.
- For non-phase-bound research or deliberation, prefer the repo-local `gsd-rigorous-research` skill so evidence, inference, and open questions stay visibly separated.
- Distinguish:
  - exploratory artifact
  - planning/canon artifact
  - implementation plan
  - code or runtime artifact

## Canon update rules

- Do not silently turn exploratory conclusions into canon.
- If a canon patch is broad, prefer a proposal artifact first.
- If a newer artifact supersedes an older steering artifact, add a note or status marker rather than leaving both equally live and ambiguous.
- Do not widen current scope by citing long-term possibility unless the seam/non-foreclosure reason is explicit.

## Destructive-action rule

Agents should not autonomously:

- delete large directories
- archive large corpora
- rewrite large doc trees for cleanliness alone
- revert user-created or pre-existing changes

Those operations require an explicit decision or a documented retention rule in [ARTIFACT-GOVERNANCE.md](./ARTIFACT-GOVERNANCE.md).

## Verification and honesty rule

- Never present requested runtime settings as if they prove effective launch settings.
- For doctrine-sensitive spawned-worker launches, preserve a requested-versus-effective launch-truth capture with `tooling/codex/capture_launch_truth.py` or an equally reviewable artifact instead of relying on private sqlite queries alone.
- Treat missing runtime fields in that capture as unresolved, not as implied matches.
- Never present inferred closure as if it were verified closure.
- If a result is mixed, say so.
- If a doc is stale, say so or mark it.
- If a command/test/verification step was not run, say so.
- Never present repo-internal canon, audit, or synthesis support as if it were equivalent to fresh external grounding.
- When a research or governance output makes load-bearing recommendations, expose whether those recommendations are:
  - internally supported by repo artifacts
  - directly externally grounded
  - or still primarily reasoned judgment

## Solo-developer risk posture

As a solo developer, assume the weak point is not “lack of ideas.” It is decision overload and context drift.

That means the repo should bias toward:

- strong review boundaries
- explicit source-of-truth docs
- small branches
- additive traceability
- minimal irreversible actions without explicit signoff

## Maintenance rule

Update this file when:

- signoff expectations change
- the project becomes public-facing
- monetization becomes active scope
- agents gain or lose autonomy in practice
- a repeated AI failure mode appears often enough to deserve a standing rule
