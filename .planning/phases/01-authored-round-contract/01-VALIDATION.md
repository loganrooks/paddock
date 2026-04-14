---
phase: 01
slug: authored-round-contract
status: draft
nyquist_compliant: true
wave_0_complete: false
created: 2026-04-11
---

# Phase 01 — Validation Strategy

> Status note (2026-04-14): This validation artifact has been snapshotted at `.planning/phases/01-authored-round-contract/superseded/2026-04-14-pre-rerun-boundary/phase/01-VALIDATION.md`. Treat it as pre-rerun planning input rather than as the final live validation contract until the next Phase 01 discuss + planning pass completes. Where its proposed Wave 0 commands or filenames diverge from `01-RESEARCH.md`, treat both as illustrative pre-rerun inputs rather than binding execution truth.

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Vitest |
| **Config file** | `vitest.config.ts` |
| **Quick run command** | `corepack pnpm run test:contract` |
| **Full suite command** | `corepack pnpm run test` |
| **Estimated runtime** | ~15 seconds |

---

## Sampling Rate

- **After every task commit:** Run `corepack pnpm run test:contract`
- **After every plan wave:** Run `corepack pnpm run test`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 15 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 01-01-01 | 01 | 1 | `PACK-02` | `T-01-02` | Shared contract literals are frozen in one place | unit | `corepack pnpm exec tsc -b` | ❌ W0 | ⬜ pending |
| 01-02-01 | 02 | 2 | `PACK-02`, `PACK-03`, `OPS-01` | `T-02-01`, `T-02-02` | Rounds, clue media, and coverage metadata validate strictly | unit | `corepack pnpm exec vitest run tests/contract/round-contract.test.ts tests/contract/mixed-media-round.test.ts tests/contract/venue-profile-resolution.test.ts` | ❌ W0 | ⬜ pending |
| 01-03-01 | 03 | 3 | `PACK-02`, `PACK-03`, `OPS-01` | `T-03-01`, `T-03-02` | Venue profiles and round fixtures match the implemented schema | integration | `corepack pnpm exec tsx packages/content-tools/src/cli.ts validate content/packs/starter-pack/pack.yaml` | ❌ W0 | ⬜ pending |
| 01-04-01 | 04 | 4 | `PACK-03`, `PACK-04`, `OPS-01` | `T-04-01`, `T-04-02`, `T-04-03` | Broken content fails with stable diagnostics and valid packs compile canonically | integration | `corepack pnpm run test:contract && corepack pnpm run content:validate && corepack pnpm run content:compile` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `package.json` — repo root scripts and devDependencies
- [ ] `pnpm-workspace.yaml` — workspace package discovery
- [ ] `tsconfig.json` — root project references
- [ ] `vitest.config.ts` — contract test runner config
- [ ] `tests/contract/round-contract.test.ts` — `PACK-02`
- [ ] `tests/contract/mixed-media-round.test.ts` — `PACK-03`
- [ ] `tests/contract/pack-validation.test.ts` — `PACK-04`
- [ ] `tests/contract/venue-profile-resolution.test.ts` — `OPS-01`

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Reveal explanations actually read as “why identifiable” rather than restating the answer | `PACK-02` | Requires human judgment on authored content quality | Open the authored round YAML fixtures and confirm each reveal explanation names the distinguishing clue logic rather than only the answer string |

---

## Validation Sign-Off

- [x] All tasks have `<automated>` verify or Wave 0 dependencies
- [x] Sampling continuity: no 3 consecutive tasks without automated verify
- [x] Wave 0 covers all missing references
- [x] No watch-mode flags
- [x] Feedback latency < 20s target
- [x] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
