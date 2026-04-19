# Lane 07: Upstream Docs Update Proposal

You are producing a concrete, proposal-grade docs update plan for the upstream `get-shit-done v1.36.0` docs corpus.

This is **not** another freshness audit and **not** another abstract gap map. The question now is:

> given the audited docs gaps and the convergences/divergences between the internal and cross-vendor lanes, what exactly should be changed, added, split, created, deferred, or explicitly left undocumented in the upstream docs corpus?

Your output must be concrete enough to seed actual upstream docs edits and PR planning.

## Output Path

Write the artifact to:

`/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-07-upstream-docs-update-proposal-opus-1m-r1.md`

Do not produce any other output.

## Required Inputs

### Prior lane artifacts

Read these fully:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01-upstream-docs-freshness.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01b-docs-gap-map.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01c-claude-opus-1m-independent-gap-reread.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01c-claude-opus-1m-independent-gap-reread-opus-1m-r3-bypass.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-03-reseed-judgment.md`

### Primary upstream docs + code surfaces

Read at minimum:

- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/README.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/ARCHITECTURE.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/AGENTS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/CONFIGURATION.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/COMMANDS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/CLI-TOOLS.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/FEATURES.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/docs/USER-GUIDE.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/README.md`
- `/home/rookslog/workspace/projects/get-shit-done-upstream-v1.36.0/CHANGELOG.md`

And whatever command / agent / template / test files you need in order to make specific edit recommendations.

## What This Lane Must Do

You must make **independent normative judgments**. Do not stop at "could be updated" or "might need supplementation."

This lane must answer:

1. What exact existing docs should be modified?
2. What exact sections or claims in those files should be corrected, weakened, expanded, or restructured?
3. Which omissions should be added into existing files versus spun into a new doc file?
4. Are there any new docs files you recommend creating to capture complexity that does not fit cleanly into the existing broad docs?
5. What is the smallest credible PR sequence that improves truthfulness quickly without overcommitting to an unreviewed giant docs rewrite?
6. Which unresolved gaps from the prior reread **must** be addressed before an upstream PR, and which can be handled as explicit follow-up?

## Major Gap-Closure Requirement

The previous Opus reread explicitly left several gaps / uncertainties. This lane must address the major ones **to the extent needed for a concrete proposal**.

At minimum, you must explicitly disposition:

- whether omitted surfaces should be treated as likely drift, likely intentional exclusion, or uncertain enough that the proposal should offer alternative documentation architectures
- whether there is evidence from upstream git history that some defects are old drift vs very recent breakage
- whether upstream `main` or local git history already appears to have fixed some of the `v1.36.0` defects
- whether localization should be part of the first PR sequence or explicitly deferred
- whether the `security_*` placement issue and model-profile coverage issue are doc bugs, schema bugs, ambiguous-spec issues, or proposal-blocking uncertainties

You do **not** need to fully solve maintainer intent. But you must not leave all of these as generic "open questions." Make a judgment about what should happen in the proposal in spite of uncertainty.

## Proposal Stance

- Prefer explicit recommendations over neutrality.
- If there are two plausible documentation architectures, recommend one and name the alternative.
- If you think a new doc file should exist, name it and explain why existing files are the wrong home.
- If you think a topic should remain intentionally undocumented in broad user docs, say so and recommend where its existence should at least be acknowledged.
- Optimize for a proposal that could actually seed one or more upstream PRs, not just a local note.

## Required Output Structure

Use exactly these sections:

1. `# Lane 07: Upstream Docs Update Proposal`
2. `## Question And Decision Posture`
3. `## What This Proposal Is Trying To Achieve`
4. `## Prior Audit Convergence And What I Treat As Settled`
5. `## Gaps From Prior Runs That I Addressed Here`
6. `## Recommended Documentation Architecture`
   - make a concrete judgment about whether to keep broad docs + add an advanced/inventory surface, or to patch only existing files, or another architecture
7. `## File-By-File Modification Plan`
   - one subsection per existing file you recommend changing
   - for each file, include:
     - why it needs change
     - exact claims/sections that should be corrected
     - exact additions or restructures recommended
     - whether this belongs in PR 1, 2, 3, etc.
8. `## Recommended New Doc Files`
   - if none, say so explicitly
   - if any, name each file, state its purpose, and outline its sections
9. `## Concrete Edit Inventory`
   - a punch-list level inventory, suitable for turning into tasks
   - include specific commands/agents/config keys/modules/doc claims to add or fix
10. `## Proposed PR Sequence`
   - recommended PR tracks with ordering rationale
   - explicitly say what should be in the first PR vs later PRs
11. `## What Should Not Be Done`
   - name tempting but bad moves
12. `## Residual Uncertainties And How The Proposal Handles Them`
13. `## PR-Readiness Judgment`
   - is this ready to drive upstream docs updates now, and under what checks?
14. `## Net Recommendation`

## Specificity Requirements

- When you recommend changing an existing file, cite the specific existing lines/sections you are reacting to.
- When you recommend adding a missing surface, name the exact command/agent/config key/module/doc page involved.
- If you recommend a new file, give it a specific proposed path under `docs/` and explain why patching existing docs is insufficient.
- If you recommend alternative architectures because maintainer intent is uncertain, mark one as recommended and one as fallback.

## Anti-Patterns To Avoid

- Do not merely restate the earlier lanes.
- Do not stop at "trust bug corrections + drift prevention" without saying exactly where they land.
- Do not say "submit a PR" without saying what the PR(s) contain.
- Do not treat uncertainty as an excuse to avoid a recommendation.
- Do not assume the upstream maintainers want exhaustive user docs unless you argue for it.
- Do not silently turn this into a request to actually edit the upstream repo; this lane is a proposal artifact.

Begin by reading the required inputs, closing the major gaps that matter for proposal quality, and then write the proposal artifact to the specified path. Do not produce any other output.
