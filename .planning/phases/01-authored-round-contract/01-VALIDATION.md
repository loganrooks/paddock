---
phase: 1
slug: authored-round-contract
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-08
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | `vitest` (recommended Wave 0 install; none exists in-repo yet) |
| **Config file** | `none — Wave 0 installs vitest.config.ts` |
| **Quick run command** | `corepack pnpm vitest run tests/contract/*.test.ts` |
| **Full suite command** | `corepack pnpm vitest run` |
| **Estimated runtime** | ~15 seconds |

---

## Sampling Rate

- **After every task commit:** Run `corepack pnpm vitest run tests/contract/*.test.ts`
- **After every plan wave:** Run `corepack pnpm vitest run`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 15 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 01-W0-01 | TBD | 0 | PACK-02 | T-01-01 | Invalid round fixtures fail if `answerTarget`, `clueSteps`, `acceptedAnswers`, `reveal`, or `scoringProfile` are missing or malformed. | unit | `corepack pnpm vitest run tests/contract/round-contract.test.ts -t PACK-02` | ❌ W0 | ⬜ pending |
| 01-W0-02 | TBD | 0 | PACK-03 | T-01-02 | One discriminated clue contract accepts Street View and non-Street-View clue media without changing required semantic fields. | unit | `corepack pnpm vitest run tests/contract/mixed-media-round.test.ts -t PACK-03` | ❌ W0 | ⬜ pending |
| 01-W0-03 | TBD | 0 | PACK-04 | T-01-03 | Compile step rejects duplicate keys, broken refs, alias collisions, and incomplete fallback declarations before packs are playable. | integration | `corepack pnpm vitest run tests/contract/pack-validation.test.ts -t PACK-04` | ❌ W0 | ⬜ pending |
| 01-W0-04 | TBD | 0 | OPS-01 | T-01-04 | Venue coverage class and fallback strategy resolve into canonical compiled outputs for each round and pack. | unit | `corepack pnpm vitest run tests/contract/venue-profile-resolution.test.ts -t OPS-01` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `package.json` — root workspace scripts and dev dependencies for `typescript`, `@types/node`, `zod`, `yaml`, `tsx`, and `vitest`
- [ ] `pnpm-workspace.yaml` — workspace definition for `packages/*`
- [ ] `tsconfig.json` — root TypeScript config with project references enabled
- [ ] `packages/domain/tsconfig.json` — package-local TS config for schema/types package
- [ ] `packages/content-tools/tsconfig.json` — package-local TS config for compiler/CLI package
- [ ] `vitest.config.ts` — root Vitest configuration
- [ ] `tests/contract/round-contract.test.ts` — PACK-02 contract coverage
- [ ] `tests/contract/mixed-media-round.test.ts` — PACK-03 mixed-media coverage
- [ ] `tests/contract/pack-validation.test.ts` — PACK-04 pack invariant coverage
- [ ] `tests/contract/venue-profile-resolution.test.ts` — OPS-01 venue coverage/fallback coverage

---

## Manual-Only Verifications

All phase behaviors should have automated verification once Wave 0 lands.

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 15s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
