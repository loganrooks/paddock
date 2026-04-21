# Project Uplift Report

- Generated: 2026-04-21T10:10:15+00:00
- Mode: detect-only
- Project class: cross-runtime uplift
- Secondary signals: mid_phase
- Recommendation: Continue with current routing

## Before-State Posture

- Planning surface present: yes
- Current state status: planning
- Runtime directories present: .codex, .claude
- Prior uplift memory present: yes
- Doctrine reference changed since prior uplift: no
- Phase boundary signal: phase CONTEXT carries explicit rerun-boundary posture
- Phase context carrier: .planning/phases/01-authored-round-contract/01-CONTEXT.md

## Recommendation Reasons

- Current uplift memory and current carrier posture are already carrying ordinary routing cleanly.

## Carrier Posture

| Carrier | Group | State | Fingerprint Shape | Fingerprint | Note |
|---------|-------|-------|-------------------|-------------|------|
| Root AGENTS | doctrine_sensitive | present | content_sha256 | dc19615376fa7163c0cff2768e7be3545a53f945d40a18dd2a72f63468bd4f32 | file carrier present |
| Planning AGENTS | doctrine_sensitive | present | content_sha256 | 2be77d73c4afc70ea987986958d94246c22a6f35a12e0852a248c87dfd35c3ed | file carrier present |
| Root CLAUDE | doctrine_sensitive | present | content_sha256 | 998155e28c715b8184abcbceba63a07e6febe47c81cbd5db86695c83cb06270d | file carrier present |
| Planning CLAUDE | doctrine_sensitive | present | content_sha256 | 5431fbb4b26bc9cd21d10ef762cb44ac87709890a3ae7df4198d43c0e45d666f | file carrier present |
| Claim Types | additive_install | present | content_sha256 | 73a4261f9fb17860f95349aaf7e7bcf69d34d4a2644cf8cbc1c02a850fc5c64a | file carrier present |
| Long Arc | additive_install | present | frontmatter_hash | 2c98d73ba277ca146ac6f83b6b589080ee3507e147af6bdb48b2103e0e9c3eb5 | file carrier present |
| Tooling Inventory | additive_install | present | inventory_item_hash | 6035dd3a48a548cb40f32b3c7f4af8f9c395b34cf5b93aafbd57b429a2f2d342 | file carrier present |
| Runtime Config | runtime_registry | present | normalized_toml_hash | 8cce9c25e0779b2c742275757cca9d9b96c38a6fca32fec31a01659217cb0cb5 | file carrier present |
| Runtime Agent Contract: gsd-advisor-researcher | runtime_registry | present | normalized_toml_hash | ee1d11c2e983b4038b1fb4ae8aeca311fe661f9e3d359c25a282977c144f3fe5 | file carrier present |
| Runtime Agent Contract: gsd-ai-researcher | runtime_registry | present | normalized_toml_hash | 5f3d1da031bdc6e3a79f6e7eb3918b76308747d2bba3a76314ddf47b027178e5 | file carrier present |
| Runtime Agent Contract: gsd-assumptions-analyzer | runtime_registry | present | normalized_toml_hash | 793409f01b3af3750fbce955c58c4a1d12b1fff41f07132136d666aca9f9b772 | file carrier present |
| Runtime Agent Contract: gsd-code-fixer | runtime_registry | present | normalized_toml_hash | a81db37de80bf75bc30479485c139441de3eee09c3e99d6894cd55473bf16d5c | file carrier present |
| Runtime Agent Contract: gsd-code-reviewer | runtime_registry | present | normalized_toml_hash | 419a19ccfb49de6db62a375103fb9a8dfb6e83d1fb7fdf5099c90370a160e1c0 | file carrier present |
| Runtime Agent Contract: gsd-codebase-mapper | runtime_registry | present | normalized_toml_hash | a3ef03f155b54a241585a874ea2936c5b58223fa04c086379786d1e2e6bfe18c | file carrier present |
| Runtime Agent Contract: gsd-debug-session-manager | runtime_registry | present | normalized_toml_hash | 59715c0bd9f5291911a062cf0860a353ca1613aa33e762080b46719bf185c3f9 | file carrier present |
| Runtime Agent Contract: gsd-debugger | runtime_registry | present | normalized_toml_hash | 03e9d0d0693d3c63cf99fec395220b462c36cfea3ea9c7e08bafb56c28ed0622 | file carrier present |
| Runtime Agent Contract: gsd-doc-classifier | runtime_registry | present | normalized_toml_hash | 85265aef5877292c1ff2418b1ff6603e65bd6373ea7501f0cafef0c71bd536ea | file carrier present |
| Runtime Agent Contract: gsd-doc-synthesizer | runtime_registry | present | normalized_toml_hash | eb0b244cda1a95fa880411fb52c8b809724f77b1731994d87387ad5d30751210 | file carrier present |
| Runtime Agent Contract: gsd-doc-verifier | runtime_registry | present | normalized_toml_hash | d7cc5f313c54cb8265d6a777f26027119efa01a71a793e0b0f7a226cf85e628a | file carrier present |
| Runtime Agent Contract: gsd-doc-writer | runtime_registry | present | normalized_toml_hash | ec705b79072f0c5227479b2a3a08b114e9472e380ed59d315bc386b4abc6ffe4 | file carrier present |
| Runtime Agent Contract: gsd-domain-researcher | runtime_registry | present | normalized_toml_hash | 61c992c96e92f569fdb326bd3f9a81cd824e1a5b6fc65c802acd7a9ff4d7bbe5 | file carrier present |
| Runtime Agent Contract: gsd-eval-auditor | runtime_registry | present | normalized_toml_hash | 4668eaf6b81dd5fce074b7210f5b2297c1f735b54debcac5c6914b34b9406224 | file carrier present |
| Runtime Agent Contract: gsd-eval-planner | runtime_registry | present | normalized_toml_hash | e92311a67065b8eb21e135617cc98ba03ecc1364394ce64fc9c5f7779451c6a4 | file carrier present |
| Runtime Agent Contract: gsd-executor | runtime_registry | present | normalized_toml_hash | c30ca3617ab06567adfd45ec8eeaa2a64bea30cba6f21f3f82e870a970a56403 | file carrier present |
| Runtime Agent Contract: gsd-framework-selector | runtime_registry | present | normalized_toml_hash | 395eb58beb248fb3d885d1372beb98972b5d134d32396e7299e90eebf15f7de2 | file carrier present |
| Runtime Agent Contract: gsd-integration-checker | runtime_registry | present | normalized_toml_hash | c5a6921af77bc9062133e501f6656af5da4a270f59e0968a6ac3c7e990e2b499 | file carrier present |
| Runtime Agent Contract: gsd-intel-updater | runtime_registry | present | normalized_toml_hash | 6aa99c229d663dfbe7276c693f672995049a935a61b47131d1a45cc0213b7962 | file carrier present |
| Runtime Agent Contract: gsd-nyquist-auditor | runtime_registry | present | normalized_toml_hash | ff35bf3eb57267e85e25ada191b06ba3a3d2d0bbd4b145b12d7f299f997e049d | file carrier present |
| Runtime Agent Contract: gsd-pattern-mapper | runtime_registry | present | normalized_toml_hash | 8a67e136e76e87ccc77f60b6443077210f4b14a39fb549dbe127b469dd0ff74c | file carrier present |
| Runtime Agent Contract: gsd-phase-researcher | runtime_registry | present | normalized_toml_hash | 6d7ca5bbff323eec1e0dba3ecc54de844d9aa6a96289c03c312fc2f7d3dca208 | file carrier present |
| Runtime Agent Contract: gsd-plan-checker | runtime_registry | present | normalized_toml_hash | ed88501119c1d8ad0606ccee0e6d6cc3e8b3dc7bc6b773876e365916218be95c | file carrier present |
| Runtime Agent Contract: gsd-planner | runtime_registry | present | normalized_toml_hash | 3e76012b038d48b22a5680c565b8c4d3d429aa9b51bb3b61481145c0a1448a34 | file carrier present |
| Runtime Agent Contract: gsd-project-researcher | runtime_registry | present | normalized_toml_hash | c7cbea8a536e16d5a8c57b2745143bc2ff378b56f9f2f8fb5d98f33b22e50ecd | file carrier present |
| Runtime Agent Contract: gsd-research-synthesizer | runtime_registry | present | normalized_toml_hash | 1b58819ab0aca9a64a4a0a53eef113b6bc7ac8bec183402a0b2679ce0ffefec3 | file carrier present |
| Runtime Agent Contract: gsd-roadmapper | runtime_registry | present | normalized_toml_hash | e0caa0b576dd09961007ee0ec248766a2ef32bdb4d10603155cfa72e0b470e10 | file carrier present |
| Runtime Agent Contract: gsd-security-auditor | runtime_registry | present | normalized_toml_hash | 81b18134f08971caac6962214360c657fe02c1a268221da0518b56e82ca8726d | file carrier present |
| Runtime Agent Contract: gsd-ui-auditor | runtime_registry | present | normalized_toml_hash | 7b5da48bdd86c69f829677d500ad844c589dd46ee814b4ebe8302f8eed1d87b4 | file carrier present |
| Runtime Agent Contract: gsd-ui-checker | runtime_registry | present | normalized_toml_hash | b8776907fc159009c7c2949dc88aa7d991ed9db61b7863305d672f43a38911e6 | file carrier present |
| Runtime Agent Contract: gsd-ui-researcher | runtime_registry | present | normalized_toml_hash | db1b6915b64bc18bfe2367d5bbeb1dcce4c7957f34a0397e0ab569eb38e515c5 | file carrier present |
| Runtime Agent Contract: gsd-user-profiler | runtime_registry | present | normalized_toml_hash | d1bc91bb5c84af2fa503933410760d18443a9f11a3c8e48e993abf45ecc7a36d | file carrier present |
| Runtime Agent Contract: gsd-verifier | runtime_registry | present | normalized_toml_hash | 1bb72bd6deeb7b91d3a03e0ad13d9308aeb04bdb741ae6c3f7a59d6152c9a3ba | file carrier present |
| Discuss Strengthening Route | doctrine_sensitive | marker_present | marker_block_hash | 8369ba7506f8fe029f23f1bc0727a9fd5d605f9888e18c94e5f3a476cac68314 | marker present on carrier |
| Context Strengthening Route | doctrine_sensitive | marker_present | marker_block_hash | d81d21022782aa1190400c46c1a55dac7efef39820635ed3bb7fb6b123849f4c | marker present on carrier |
| Plan Strengthening Route | doctrine_sensitive | marker_present | marker_block_hash | 2e4de6da5fdb88db6d6428f878dc305d317286dee03e2a661d071291a3ebbeea | marker present on carrier |
| Research Strengthening Route | doctrine_sensitive | marker_present | marker_block_hash | 5082eb8c50c42a97f182eb75cb3309df942d83ff458cc36836583e9f340c089f | marker present on carrier |

## Additive Install Routes

- No additive carrier install is currently queued.

## Doctrine-Sensitive Proposal Routes

- No doctrine-sensitive proposal route is currently queued.

## Held For Later Families

- required-reading installation practice — held
- cross-runtime uplift composition — held
- upstream-template drift machinery — held
- aged-bespoke deep merge — held
- audit-subtree aging carry — held
- routed-entry hooks beyond `progress` — partially landed: propagation-audit/04-resume-project-second-consumer-implementation.md
- forensics / archived-milestone integration — held
- workstream parent/child posture reconciliation — held
