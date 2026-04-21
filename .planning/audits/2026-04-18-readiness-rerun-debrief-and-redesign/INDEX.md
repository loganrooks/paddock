# Readiness Rerun Debrief And Redesign

- [g:c+i] This workspace exists to prepare a serious debrief and rerun-design audit for the readiness package, not to silently reopen Checkpoint 5, not to declare the old package a failure by reflex, and not to treat the upstream docs work as sovereign replacement truth. Sources: .planning/readiness/phase-01-rerun/PLAN.md:61, .planning/readiness/phase-01-rerun/PLAN.md:65, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:5, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:17, .planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md:50.

## Plain-Language Re-Entry

- [d:r:i] If you have lost the thread, start here before dropping back into the denser audit/program artifacts:
  1. [PLAIN-LANGUAGE-STATE.md](PLAIN-LANGUAGE-STATE.md)
  2. [PLAIN-LANGUAGE-GLOSSARY.md](PLAIN-LANGUAGE-GLOSSARY.md)

## Read Order

1. [AUDIT-CHARTER.md](AUDIT-CHARTER.md)
2. [WORKSPACE-AUTHORITY-AND-ORGANIZATION.md](WORKSPACE-AUTHORITY-AND-ORGANIZATION.md)
3. [PLAIN-LANGUAGE-STATE.md](PLAIN-LANGUAGE-STATE.md)
4. [PLAIN-LANGUAGE-GLOSSARY.md](PLAIN-LANGUAGE-GLOSSARY.md)
5. [CURRENT-STATE.md](CURRENT-STATE.md)
6. [ONBOARDING.md](ONBOARDING.md)
7. [SESSION-FRAMING-BRIEF.md](SESSION-FRAMING-BRIEF.md)
8. [QUESTION-SET.md](QUESTION-SET.md)
9. [EVIDENCE-ARCHITECTURE.md](EVIDENCE-ARCHITECTURE.md)
10. [PLAN-PROPOSALS.md](PLAN-PROPOSALS.md)
11. [STATUS.md](STATUS.md)
12. [OPUS-CARRIAGE-AND-OPERATIONALIZATION-SPEC.md](OPUS-CARRIAGE-AND-OPERATIONALIZATION-SPEC.md)
13. [lane-04-opus47-max-carriage-and-operationalization-review.md](lane-04-opus47-max-carriage-and-operationalization-review.md)
14. [lane-04-gpt54-xhigh-carriage-and-operationalization-review.md](lane-04-gpt54-xhigh-carriage-and-operationalization-review.md)
15. [lane-04-comparative-disposition.md](lane-04-comparative-disposition.md)
16. [lane-04-surface-a-authority-force-proposal.md](lane-04-surface-a-authority-force-proposal.md)
17. [lane-04-surface-d-high-force-carrier-proposal.md](lane-04-surface-d-high-force-carrier-proposal.md)
18. [lane-04-surface-b-prelicensing-judgeability-pass.md](lane-04-surface-b-prelicensing-judgeability-pass.md)
19. [lane-04-surface-b-graded-underreach-trial.md](lane-04-surface-b-graded-underreach-trial.md)
20. [lane-04-local-proposal-and-stress-test-disposition.md](lane-04-local-proposal-and-stress-test-disposition.md)
21. [lane-04-patched-surface-reread.md](lane-04-patched-surface-reread.md)
22. [MAIN-WAVE-LAUNCH-READINESS-DECISION.md](MAIN-WAVE-LAUNCH-READINESS-DECISION.md)
23. [MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md](MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md)
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
44. [PR-DOCS-INTERVENTION-CARRY-AUDIT.md](PR-DOCS-INTERVENTION-CARRY-AUDIT.md)
45. [PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md](PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md)
46. [PR-DOCS-INTERVENTION-TRANSFORMATION-PLAN.md](PR-DOCS-INTERVENTION-TRANSFORMATION-PLAN.md)
47. [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](RUNTIME-MATERIALIZATION-AND-AUTHORITY.md)
48. [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](GOAL-TO-SURFACE-INTERVENTION-INDEX.md)
49. [SURFACE-STATUS-AND-DELTA.md](SURFACE-STATUS-AND-DELTA.md)
50. [intervention-proposals/README.md](intervention-proposals/README.md)
51. [intervention-proposals/05-batch-routing-note.md](intervention-proposals/05-batch-routing-note.md)
52. [intervention-proposals/06-first-tranche-disposition.md](intervention-proposals/06-first-tranche-disposition.md)
53. [intervention-proposals/07-live-vs-overlay-drift-register-pilot.md](intervention-proposals/07-live-vs-overlay-drift-register-pilot.md)
54. [intervention-proposals/08-manifest-semantic-contract-disposition.md](intervention-proposals/08-manifest-semantic-contract-disposition.md)
55. [intervention-proposals/09-final-runtime-visibility-proposal.md](intervention-proposals/09-final-runtime-visibility-proposal.md)
56. [intervention-proposals/10-final-runtime-visibility-first-pass-disposition.md](intervention-proposals/10-final-runtime-visibility-first-pass-disposition.md)
57. [docs-audit/README.md](docs-audit/README.md)
58. [docs-audit/packets/01-pr-docs-intervention-carry-packet.md](docs-audit/packets/01-pr-docs-intervention-carry-packet.md)
59. [docs-audit/specs/01-pr-docs-intervention-carry-spec.md](docs-audit/specs/01-pr-docs-intervention-carry-spec.md)
60. [docs-audit/prompts/01-pr-docs-intervention-carry-opus47-max-r1-launch-prompt.md](docs-audit/prompts/01-pr-docs-intervention-carry-opus47-max-r1-launch-prompt.md)
61. [docs-audit/prompts/01-pr-docs-intervention-carry-gpt54-xhigh-r1-brief.md](docs-audit/prompts/01-pr-docs-intervention-carry-gpt54-xhigh-r1-brief.md)
62. [docs-audit/launch-truth/01-pr-docs-intervention-carry-launch-truth.md](docs-audit/launch-truth/01-pr-docs-intervention-carry-launch-truth.md)
63. [docs-audit/outputs/01-pr-docs-intervention-carry-opus47-max-r1.md](docs-audit/outputs/01-pr-docs-intervention-carry-opus47-max-r1.md)
64. [docs-audit/outputs/01-pr-docs-intervention-carry-gpt54-xhigh-r1.md](docs-audit/outputs/01-pr-docs-intervention-carry-gpt54-xhigh-r1.md)
65. [docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md](docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md)
66. [tranche-audit/README.md](tranche-audit/README.md)
67. [tranche-audit/packets/01-runtime-visibility-tranche-packet.md](tranche-audit/packets/01-runtime-visibility-tranche-packet.md)
68. [tranche-audit/specs/01-runtime-visibility-tranche-cross-vendor-spec.md](tranche-audit/specs/01-runtime-visibility-tranche-cross-vendor-spec.md)
69. [tranche-audit/prompts/01-runtime-visibility-tranche-opus47-max-r1-launch-prompt.md](tranche-audit/prompts/01-runtime-visibility-tranche-opus47-max-r1-launch-prompt.md)
70. [tranche-audit/prompts/01-runtime-visibility-tranche-gpt54-xhigh-r1-brief.md](tranche-audit/prompts/01-runtime-visibility-tranche-gpt54-xhigh-r1-brief.md)
71. [tranche-audit/launch-truth/01-runtime-visibility-tranche-launch-truth.md](tranche-audit/launch-truth/01-runtime-visibility-tranche-launch-truth.md)
72. [tranche-audit/outputs/01-runtime-visibility-tranche-opus47-max-r1.md](tranche-audit/outputs/01-runtime-visibility-tranche-opus47-max-r1.md)
73. [tranche-audit/outputs/01-runtime-visibility-tranche-gpt54-xhigh-r1.md](tranche-audit/outputs/01-runtime-visibility-tranche-gpt54-xhigh-r1.md)
74. [tranche-audit/dispositions/01-runtime-visibility-tranche-comparative-disposition.md](tranche-audit/dispositions/01-runtime-visibility-tranche-comparative-disposition.md)
75. [tranche-audit/artifacts/01-runtime-visibility-report.json](tranche-audit/artifacts/01-runtime-visibility-report.json)
76. [LAUNCH-LEDGER.md](LAUNCH-LEDGER.md)
77. [lane-01-opus47-cross-review-disposition.md](lane-01-opus47-cross-review-disposition.md)
78. [lane-02-opus47-max-resituation-review.md](lane-02-opus47-max-resituation-review.md)
79. [OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md](OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md)
80. [lane-03-opus47-max-corpus-vocabulary-stress-test.md](lane-03-opus47-max-corpus-vocabulary-stress-test.md)
81. [COMMENTARY-CORPUS-READSET.md](corpus/COMMENTARY-CORPUS-READSET.md)
82. [corpus/README.md](corpus/README.md)
83. [intervention-proposals/29-long-horizon-carry-gap-register.md](intervention-proposals/29-long-horizon-carry-gap-register.md)
84. [intervention-proposals/30-opportunity-seeking-and-self-overcoming-companion-layer-proposal.md](intervention-proposals/30-opportunity-seeking-and-self-overcoming-companion-layer-proposal.md)
85. [long-horizon-audit/README.md](long-horizon-audit/README.md)
86. [long-horizon-audit/launch-truth/01-long-horizon-field-mapping-launch-truth.md](long-horizon-audit/launch-truth/01-long-horizon-field-mapping-launch-truth.md)
87. [long-horizon-audit/outputs/01-long-horizon-field-mapping-opus47-max-r1.md](long-horizon-audit/outputs/01-long-horizon-field-mapping-opus47-max-r1.md)
88. [long-horizon-audit/outputs/01-long-horizon-field-mapping-gpt54-xhigh-r1.md](long-horizon-audit/outputs/01-long-horizon-field-mapping-gpt54-xhigh-r1.md)
89. [long-horizon-audit/dispositions/01-long-horizon-field-mapping-comparative-disposition.md](long-horizon-audit/dispositions/01-long-horizon-field-mapping-comparative-disposition.md)
90. [threshold-audit/README.md](threshold-audit/README.md)
91. [threshold-audit/artifacts/01-threshold-language-raw-scan.txt](threshold-audit/artifacts/01-threshold-language-raw-scan.txt)
92. [threshold-audit/artifacts/02-threshold-language-top-files.txt](threshold-audit/artifacts/02-threshold-language-top-files.txt)
93. [threshold-audit/dispositions/01-threshold-language-residue-audit.md](threshold-audit/dispositions/01-threshold-language-residue-audit.md)
94. [threshold-audit/dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md](threshold-audit/dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md)
95. [self-overcoming-audit/README.md](self-overcoming-audit/README.md)
96. [self-overcoming-audit/launch-truth/01-companion-layer-proposal-launch-truth.md](self-overcoming-audit/launch-truth/01-companion-layer-proposal-launch-truth.md)
97. [self-overcoming-audit/outputs/01-companion-layer-proposal-opus47-max-r1.md](self-overcoming-audit/outputs/01-companion-layer-proposal-opus47-max-r1.md)
98. [self-overcoming-audit/outputs/01-companion-layer-proposal-gpt54-xhigh-r1.md](self-overcoming-audit/outputs/01-companion-layer-proposal-gpt54-xhigh-r1.md)
99. [self-overcoming-audit/dispositions/01-companion-layer-proposal-comparative-disposition.md](self-overcoming-audit/dispositions/01-companion-layer-proposal-comparative-disposition.md)
100. [intervention-proposals/31-instruction-surface-hardening-note.md](intervention-proposals/31-instruction-surface-hardening-note.md)
101. [intervention-proposals/32-strengthening-opportunity-first-slice-implementation.md](intervention-proposals/32-strengthening-opportunity-first-slice-implementation.md)
102. [intervention-proposals/33-research-and-planner-strengthening-carry-follow-through.md](intervention-proposals/33-research-and-planner-strengthening-carry-follow-through.md)

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
- current carry-focused audit of the submitted docs PR against intervention-planning goals: `PR-DOCS-INTERVENTION-CARRY-AUDIT.md`
- current explicit next-step sequence for challenging and inheriting that audit: `PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md`
- current transformation plan for how the stable PR docs and companion intervention layer should fit together: `PR-DOCS-INTERVENTION-TRANSFORMATION-PLAN.md`
- current runtime/materialization/authority companion artifact for the intervention layer: `RUNTIME-MATERIALIZATION-AND-AUTHORITY.md`
- current goal-to-surface routing companion artifact for the intervention layer: `GOAL-TO-SURFACE-INTERVENTION-INDEX.md`
- current surface-status and delta companion artifact for the intervention layer: `SURFACE-STATUS-AND-DELTA.md`
- current bounded intervention proposal subtree, routing note, and first-tranche disposition: `intervention-proposals/`
- current bounded drift-register pilot for the second tranche: `intervention-proposals/07-live-vs-overlay-drift-register-pilot.md`
- current manifest semantic correction for the second tranche: `intervention-proposals/08-manifest-semantic-contract-disposition.md`
- current bounded final-runtime visibility proposal for the second tranche: `intervention-proposals/09-final-runtime-visibility-proposal.md`
- current accepted first-pass runtime-visibility implementation for the second tranche: `intervention-proposals/10-final-runtime-visibility-first-pass-disposition.md`
- current full-field long-horizon carry seed register: `intervention-proposals/29-long-horizon-carry-gap-register.md`
- current strengthened first-slice implementation note for the self-overcoming family: `intervention-proposals/32-strengthening-opportunity-first-slice-implementation.md`
- current research/planner follow-through note for the self-overcoming family: `intervention-proposals/33-research-and-planner-strengthening-carry-follow-through.md`
- current long-horizon cross-vendor challenge subtree and lane-01 inheritance: `long-horizon-audit/`
- current threshold-language residue audit subtree and first-pass warning surface: `threshold-audit/`
- current self-overcoming proposal challenge subtree and lane-01 inheritance: `self-overcoming-audit/`
- current bounded docs-audit lane subtree for that challenge work: `docs-audit/`
- current docs-audit launch record: `docs-audit/launch-truth/01-pr-docs-intervention-carry-launch-truth.md`
- current raw docs-audit outputs: `docs-audit/outputs/01-pr-docs-intervention-carry-opus47-max-r1.md`, `docs-audit/outputs/01-pr-docs-intervention-carry-gpt54-xhigh-r1.md`
- current inheritance decision for docs-audit lane-01: `docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md`
- current bounded post-tranche challenge subtree for recently landed intervention work: `tranche-audit/`
- current frozen runtime-visibility tranche packet/spec/prompt set: `tranche-audit/packets/01-runtime-visibility-tranche-packet.md`, `tranche-audit/specs/01-runtime-visibility-tranche-cross-vendor-spec.md`, `tranche-audit/prompts/01-runtime-visibility-tranche-opus47-max-r1-launch-prompt.md`, `tranche-audit/prompts/01-runtime-visibility-tranche-gpt54-xhigh-r1-brief.md`
- current runtime-visibility tranche launch record: `tranche-audit/launch-truth/01-runtime-visibility-tranche-launch-truth.md`
- current raw runtime-visibility tranche outputs: `tranche-audit/outputs/01-runtime-visibility-tranche-opus47-max-r1.md`, `tranche-audit/outputs/01-runtime-visibility-tranche-gpt54-xhigh-r1.md`
- current inheritance decision for the runtime-visibility tranche: `tranche-audit/dispositions/01-runtime-visibility-tranche-comparative-disposition.md`
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
- current carry-focused audit of the submitted docs PR against intervention-planning goals
- current explicit next-step sequence for challenging and inheriting that audit
- current runtime/materialization/authority companion artifact
- current goal-to-surface routing companion artifact
- current surface-status and delta companion artifact
- current first bounded intervention proposal batch, routing note, and first-tranche disposition
- current second-tranche drift-register pilot
- current manifest semantic correction for update-boundary truth versus final-runtime truth
- current bounded follow-through proposal for separate final-runtime visibility
- current accepted first-pass implementation of that follow-through
- current accepted second-tranche sequencing note for cohort typing -> bounded cleanup -> selected-lane snapshots -> cleaner manifest/install coherence
- current live-only agent cohort matrix and targeted reread disposition
- current selected-lane runtime snapshot discipline, first clean-boundary snapshot note, strict manifest/install coherence pass, and cleaner manifest/install coherence follow-through notes
- current clean-boundary snapshot artifact: `intervention-proposals/artifacts/01-second-tranche-clean-boundary-runtime-visibility-snapshot.json`
- current strict coherence artifact: `intervention-proposals/artifacts/02-manifest-install-coherence-report.json`
- current live-only next-tranche proposal: `intervention-proposals/18-live-only-agent-authority-carry-proposal.md`
- current ordered high-leverage authority review: `intervention-proposals/19-high-leverage-live-only-authority-review.md`
- current accepted reviewer carry note: `intervention-proposals/20-gsd-code-reviewer-authority-carry-review.md`
- current reviewer post-carry runtime artifact: `intervention-proposals/artifacts/03-gsd-code-reviewer-post-carry-runtime-visibility.json`
- current accepted fixer carry note: `intervention-proposals/21-gsd-code-fixer-authority-carry-review.md`
- current fixer post-carry runtime artifact: `intervention-proposals/artifacts/04-gsd-code-fixer-post-carry-runtime-visibility.json`
- current accepted intel-updater carry note: `intervention-proposals/22-gsd-intel-updater-authority-carry-review.md`
- current intel-updater post-carry runtime artifact: `intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json`
- current accepted pattern-mapper carry note: `intervention-proposals/23-gsd-pattern-mapper-authority-carry-review.md`
- current pattern-mapper post-carry runtime artifact: `intervention-proposals/artifacts/06-gsd-pattern-mapper-post-carry-runtime-visibility.json`
- current package-truth / parity residue judgment: `intervention-proposals/24-package-truth-and-parity-residue-judgment.md`
- current rerun-floor recomputation: `intervention-proposals/25-rerun-floor-recomputation.md`
- current brake-exit rule proposal: `intervention-proposals/26-brake-exit-rule.md`
- current preserve-only activation-trigger doctrine proposal: `intervention-proposals/27-preserve-only-activation-trigger-doctrine.md`
- current execution-capacity reopen rule proposal: `intervention-proposals/28-execution-capacity-reopen-rule.md`
- next step: turn the recomputed floor into the next actual closure batch rather than reopening parity/materialization work
- later lane outputs for the debrief/audit wave
- later synthesis artifact that recommends a rerun shape or a justified alternative

## Current Session Rule

- [g:c+i] Treat this directory as `audit trail + program design`, not canon. If later conclusions should alter the readiness package, they must be promoted explicitly rather than silently treated as live doctrine. Sources: .planning/AGENTS.md:35, .planning/AGENTS.md:40, .planning/AGENTS.md:98, .planning/AGENTS.md:106.
