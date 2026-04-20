# Readiness Rerun Debrief And Redesign

- [g:c+i] This workspace exists to prepare a serious debrief and rerun-design audit for the readiness package, not to silently reopen Checkpoint 5, not to declare the old package a failure by reflex, and not to treat the upstream docs work as sovereign replacement truth. Sources: .planning/readiness/phase-01-rerun/PLAN.md:61, .planning/readiness/phase-01-rerun/PLAN.md:65, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:5, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:17, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:50.

## Read Order

1. [AUDIT-CHARTER.md](AUDIT-CHARTER.md)
2. [WORKSPACE-AUTHORITY-AND-ORGANIZATION.md](WORKSPACE-AUTHORITY-AND-ORGANIZATION.md)
3. [CURRENT-STATE.md](CURRENT-STATE.md)
4. [ONBOARDING.md](ONBOARDING.md)
5. [SESSION-FRAMING-BRIEF.md](SESSION-FRAMING-BRIEF.md)
6. [QUESTION-SET.md](QUESTION-SET.md)
7. [EVIDENCE-ARCHITECTURE.md](EVIDENCE-ARCHITECTURE.md)
8. [PLAN-PROPOSALS.md](PLAN-PROPOSALS.md)
9. [STATUS.md](STATUS.md)
10. [OPUS-CARRIAGE-AND-OPERATIONALIZATION-SPEC.md](OPUS-CARRIAGE-AND-OPERATIONALIZATION-SPEC.md)
11. [lane-04-opus47-max-carriage-and-operationalization-review.md](lane-04-opus47-max-carriage-and-operationalization-review.md)
12. [lane-04-gpt54-xhigh-carriage-and-operationalization-review.md](lane-04-gpt54-xhigh-carriage-and-operationalization-review.md)
13. [lane-04-comparative-disposition.md](lane-04-comparative-disposition.md)
14. [lane-04-surface-a-authority-force-proposal.md](lane-04-surface-a-authority-force-proposal.md)
15. [lane-04-surface-d-high-force-carrier-proposal.md](lane-04-surface-d-high-force-carrier-proposal.md)
16. [lane-04-surface-b-prelicensing-judgeability-pass.md](lane-04-surface-b-prelicensing-judgeability-pass.md)
17. [lane-04-surface-b-graded-underreach-trial.md](lane-04-surface-b-graded-underreach-trial.md)
18. [lane-04-local-proposal-and-stress-test-disposition.md](lane-04-local-proposal-and-stress-test-disposition.md)
19. [lane-04-patched-surface-reread.md](lane-04-patched-surface-reread.md)
20. [MAIN-WAVE-LAUNCH-READINESS-DECISION.md](MAIN-WAVE-LAUNCH-READINESS-DECISION.md)
21. [MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md](MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md)
22. [lane-05-opus47-max-main-wave-contract-cross-review.md](lane-05-opus47-max-main-wave-contract-cross-review.md)
23. [lane-05-gpt54-xhigh-main-wave-contract-cross-review.md](lane-05-gpt54-xhigh-main-wave-contract-cross-review.md)
24. [lane-05-comparative-disposition.md](lane-05-comparative-disposition.md)
25. [WAVE-1-PACKET-MANIFESTS.md](WAVE-1-PACKET-MANIFESTS.md)
26. [wave-1/README.md](wave-1/README.md)
27. [wave-2/README.md](wave-2/README.md)
28. [wave-2/launch-truth/05-suppressed-opportunity-and-non-intervention-launch-truth.md](wave-2/launch-truth/05-suppressed-opportunity-and-non-intervention-launch-truth.md)
29. [wave-2/outputs/05-suppressed-opportunity-and-non-intervention-opus47-max-r1.md](wave-2/outputs/05-suppressed-opportunity-and-non-intervention-opus47-max-r1.md)
30. [wave-2/outputs/05-suppressed-opportunity-and-non-intervention-gpt54-xhigh-r1.md](wave-2/outputs/05-suppressed-opportunity-and-non-intervention-gpt54-xhigh-r1.md)
31. [wave-2/dispositions/05-wave-2-lane05-comparative-disposition.md](wave-2/dispositions/05-wave-2-lane05-comparative-disposition.md)
32. [wave-2/prompts/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-brief.md](wave-2/prompts/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-brief.md)
33. [wave-2/outputs/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-r1.md](wave-2/outputs/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-r1.md)
34. [wave-2/launch-truth/06-rerun-design-launch-truth.md](wave-2/launch-truth/06-rerun-design-launch-truth.md)
35. [wave-2/outputs/06-rerun-design-opus47-max-r1.md](wave-2/outputs/06-rerun-design-opus47-max-r1.md)
36. [wave-2/outputs/06-rerun-design-gpt54-xhigh-r1.md](wave-2/outputs/06-rerun-design-gpt54-xhigh-r1.md)
37. [wave-2/dispositions/06-wave-2-lane06-comparative-disposition.md](wave-2/dispositions/06-wave-2-lane06-comparative-disposition.md)
38. [wave-2/dispositions/07-accepted-program-first-slice-tranche.md](wave-2/dispositions/07-accepted-program-first-slice-tranche.md)
39. [wave-2/dispositions/08-r5-18-executed-bundle-review-pair-inheritance.md](wave-2/dispositions/08-r5-18-executed-bundle-review-pair-inheritance.md)
40. [wave-2/dispositions/09-r5-18-materialization-and-package-truth-fix-slice.md](wave-2/dispositions/09-r5-18-materialization-and-package-truth-fix-slice.md)
41. [wave-2/dispositions/10-r5-18-materialization-proof.md](wave-2/dispositions/10-r5-18-materialization-proof.md)
42. [HARNESS-INTERVENTION-UPDATE-LANE.md](HARNESS-INTERVENTION-UPDATE-LANE.md)
43. [HARNESS-INTERVENTION-ONBOARDING.md](HARNESS-INTERVENTION-ONBOARDING.md)
44. [LAUNCH-LEDGER.md](LAUNCH-LEDGER.md)
45. [lane-01-opus47-cross-review-disposition.md](lane-01-opus47-cross-review-disposition.md)
46. [lane-02-opus47-max-resituation-review.md](lane-02-opus47-max-resituation-review.md)
47. [OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md](OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md)
48. [lane-03-opus47-max-corpus-vocabulary-stress-test.md](lane-03-opus47-max-corpus-vocabulary-stress-test.md)
49. [COMMENTARY-CORPUS-READSET.md](corpus/COMMENTARY-CORPUS-READSET.md)
50. [corpus/README.md](corpus/README.md)

## Source-Of-Truth Hierarchy

- charter and governing posture: `AUDIT-CHARTER.md`
- authority / artifact-class map for this directory: `WORKSPACE-AUTHORITY-AND-ORGANIZATION.md`
- current framing and bridge-state summary: `CURRENT-STATE.md`
- onboarding read path for later reviewers: `ONBOARDING.md`
- primary distilled record of this session's added framing: `SESSION-FRAMING-BRIEF.md`
- substantive questions and required output shapes: `QUESTION-SET.md`
- corpus split, packeting, and sizing discipline: `EVIDENCE-ARCHITECTURE.md`
- competing audit-program shapes and recommended main path: `PLAN-PROPOSALS.md`
- live mutable state for this audit setup: `STATUS.md`
- current main-wave contract-level design artifact: `MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md`
- current contract-level cross-review outputs: `lane-05-opus47-max-main-wave-contract-cross-review.md`, `lane-05-gpt54-xhigh-main-wave-contract-cross-review.md`
- current inheritance decision for lane-05: `lane-05-comparative-disposition.md`
- current concrete Wave-1 packet companion: `WAVE-1-PACKET-MANIFESTS.md`
- current forward-looking topology for new main-wave artifacts: `wave-1/README.md`
- current forward-looking topology for Wave-2 artifacts: `wave-2/README.md`
- current Wave-2 lane-05 launch record: `wave-2/launch-truth/05-suppressed-opportunity-and-non-intervention-launch-truth.md`
- current raw Wave-2 lane-05 outputs: `wave-2/outputs/05-suppressed-opportunity-and-non-intervention-opus47-max-r1.md`, `wave-2/outputs/05-suppressed-opportunity-and-non-intervention-gpt54-xhigh-r1.md`
- current inheritance decision for Wave-2 lane-05: `wave-2/dispositions/05-wave-2-lane05-comparative-disposition.md`
- current bounded runtime-authority follow-up brief: `wave-2/prompts/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-brief.md`
- current bounded runtime-authority follow-up output: `wave-2/outputs/05a-runtime-authority-materialization-drift-probe-gpt54-xhigh-r1.md`
- current Wave-2 lane-06 launch record: `wave-2/launch-truth/06-rerun-design-launch-truth.md`
- current raw Wave-2 lane-06 outputs: `wave-2/outputs/06-rerun-design-opus47-max-r1.md`, `wave-2/outputs/06-rerun-design-gpt54-xhigh-r1.md`
- current inheritance decision for Wave-2 lane-06: `wave-2/dispositions/06-wave-2-lane06-comparative-disposition.md`
- current bounded first-slice tranche: `wave-2/dispositions/07-accepted-program-first-slice-tranche.md`
- current `R5.18` review-pair inheritance note: `wave-2/dispositions/08-r5-18-executed-bundle-review-pair-inheritance.md`
- current bounded `R5.18` materialization / package-truth fix slice: `wave-2/dispositions/09-r5-18-materialization-and-package-truth-fix-slice.md`
- current bounded `R5.18` materialization proof note: `wave-2/dispositions/10-r5-18-materialization-proof.md`
- current harness-update correction lane and active upstream/docs probe record: `HARNESS-INTERVENTION-UPDATE-LANE.md`
- current purpose-built harness intervention onboarding/map artifact: `HARNESS-INTERVENTION-ONBOARDING.md`
- current frozen first-lane packet files: `wave-1/packets/`
- current frozen first-lane specs: `wave-1/specs/`
- current drafted second-wave packet files: `wave-2/packets/`
- current drafted second-wave specs: `wave-2/specs/`
- current drafted second-wave prompts: `wave-2/prompts/`
- current inheritance record for lane-04: `lane-04-comparative-disposition.md`
- current draft local proposals from lane-04: `lane-04-surface-a-authority-force-proposal.md`, `lane-04-surface-d-high-force-carrier-proposal.md`
- current bounded Surface B stress tests: `lane-04-surface-b-prelicensing-judgeability-pass.md`, `lane-04-surface-b-graded-underreach-trial.md`
- current local inheritance decision after those proposals/tests: `lane-04-local-proposal-and-stress-test-disposition.md`
- current reread of the landed lane-04 local patches: `lane-04-patched-surface-reread.md`
- current decision on whether pre-main-wave external review is still needed: `MAIN-WAVE-LAUNCH-READINESS-DECISION.md`
- current main-wave design artifact: `MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md`
- older lane-specific specs and outputs: scoped challenge material, not current authority
- requested-versus-actual external launch history: `LAUNCH-LEDGER.md`

## Planned Outputs

- governance/onboarding suite in this directory
- authority and organization note for this workspace
- concrete Wave-1 packet manifests for the first main-wave lanes
- first Wave-1 lane specs under `wave-1/specs/`
- Wave-2 lane specs under `wave-2/specs/`
- corresponding Wave-2 prompts under `wave-2/prompts/`
- current accepted Wave-2 lane-05 outputs under `wave-2/outputs/`
- current Wave-2 lane dispositions under `wave-2/dispositions/`
- current Wave-2 launch-truth records under `wave-2/launch-truth/`
- next step: turn the highest-rank harness intervention surfaces into bounded proposal artifacts, then decide whether one more narrow residue pass is needed before rerun-floor recomputation
- later lane outputs for the debrief/audit wave
- later synthesis artifact that recommends a rerun shape or a justified alternative

## Current Session Rule

- [g:c+i] Treat this directory as `audit trail + program design`, not canon. If later conclusions should alter the readiness package, they must be promoted explicitly rather than silently treated as live doctrine. Sources: .planning/AGENTS.md:35, .planning/AGENTS.md:40, .planning/AGENTS.md:98, .planning/AGENTS.md:106.
