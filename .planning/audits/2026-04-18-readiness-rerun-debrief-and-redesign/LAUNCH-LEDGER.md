# Launch Ledger

## 2026-04-18 `lane-01`

- date: `2026-04-18`
- purpose: first external cross-review of the new audit-setup suite before launching the main wave
- requested model / reasoning: `opus[1m]` / `xhigh`
- requested launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`, repo-local prompt/spec path, `--dangerously-skip-permissions`
- prompt artifact: [lane-01-opus1m-cross-review-launch-prompt.md](lane-01-opus1m-cross-review-launch-prompt.md)
- governing spec: [OPUS-CROSS-REVIEW-SPEC.md](OPUS-CROSS-REVIEW-SPEC.md)
- output artifact: [lane-01-opus47-audit-setup-cross-review.md](lane-01-opus47-audit-setup-cross-review.md)
- probe summary:
  - exit code: `0`
  - elapsed seconds: `356.069`
  - session id: `da4dd51e-d4a0-47c1-b9e5-cc56fba694e4`
  - total cost usd: `1.711486`
  - stdout/stderr/debug artifacts:
    - `/tmp/readiness-rerun-debrief-opus1m-r1-20260418-001810.kb_0gv9g.stream.jsonl`
    - `/tmp/readiness-rerun-debrief-opus1m-r1-20260418-001810.0dd8bq0s.stderr.log`
    - `/tmp/readiness-rerun-debrief-opus1m-r1-20260418-001810.1v5pzkay.debug.log`
- disposition:
  - `accept as challenge input`
  - main-wave launch is `not justified yet`
  - first six revisions in the review artifact are treated as blockers for immediate launch

## 2026-04-19 `lane-02`

- date: `2026-04-19`
- purpose: situated resituation review after the commentary corpus, to judge what the workspace has actually earned, what remains untested, and what should come next without authorizing rewrites
- requested model / reasoning: `opus[1m]` / `max`
- requested launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`, repo-local prompt/spec path, `--dangerously-skip-permissions`
- prompt artifact: [lane-02-opus47-max-resituation-review-launch-prompt.md](lane-02-opus47-max-resituation-review-launch-prompt.md)
- governing spec: [OPUS-RESITUATION-REVIEW-SPEC.md](OPUS-RESITUATION-REVIEW-SPEC.md)
- output artifact: [lane-02-opus47-max-resituation-review.md](lane-02-opus47-max-resituation-review.md)
- probe summary:
  - exit code: `0`
  - elapsed seconds: `582.765`
  - session id: `5a1c94f0-74ef-4d2b-a0f2-5033523d9836`
  - total cost usd: `5.114649250000001`
  - stdout/stderr/debug artifacts:
    - `/tmp/readiness-resituation-opus47-max-r4-20260419-064320.hap99al9.stream.jsonl`
    - `/tmp/readiness-resituation-opus47-max-r4-20260419-064320.wrodx7yo.stderr.log`
    - `/tmp/readiness-resituation-opus47-max-r4-20260419-064320.zv6fv9jh.debug.log`
- disposition:
  - `accept as challenge input`
  - commentary corpus is treated as `real interpretive gain, not yet case-tested operational doctrine`
  - main-wave launch is still `not justified yet`
  - no rewrite of `CLAIM-TYPES.md`, `POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`, or readiness `PLAN.md` is justified from this lane alone
  - strongest proposed next move is a `bounded vocabulary-stress-test lane` on concrete readiness-era cases

## 2026-04-19 `lane-03`

- date: `2026-04-19`
- purpose: bounded stress-test of whether the commentary corpus changes judgment on concrete readiness-era cases or mainly supplies reviewer-register vocabulary
- requested model / reasoning: `opus[1m]` / `max`
- requested launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`, repo-local prompt/spec path, `--dangerously-skip-permissions`
- prompt artifact: [lane-03-opus47-max-corpus-vocabulary-stress-test-launch-prompt.md](lane-03-opus47-max-corpus-vocabulary-stress-test-launch-prompt.md)
- governing spec: [OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md](OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md)
- output artifact: [lane-03-opus47-max-corpus-vocabulary-stress-test.md](lane-03-opus47-max-corpus-vocabulary-stress-test.md)
- probe summary:
  - exit code: `0`
  - elapsed seconds: `965.655`
  - session id: `be61e171-00e4-47e3-886c-7129b9ead05e`
  - total cost usd: `4.517299500000001`
  - stdout/stderr/debug artifacts:
    - `/tmp/lane-03-opus47-max-corpus-vocabulary-stress-test-r1-20260419-070348.qz8jaq_0.stream.jsonl`
    - `/tmp/lane-03-opus47-max-corpus-vocabulary-stress-test-r1-20260419-070348.ge5vh0hj.stderr.log`
    - `/tmp/lane-03-opus47-max-corpus-vocabulary-stress-test-r1-20260419-070348.bu47sk1o.debug.log`
- disposition:
  - `accept as challenge input`
  - commentary corpus remains `reviewer-register only` on this evidence
  - no bounded doctrine-supplementation lane is justified from this result
  - accepted next move is `proceed with lane-01 setup revisions without corpus uplift`

## 2026-04-19 `lane-04`

- date: `2026-04-19`
- purpose: bounded carriage-and-operationalization review to test what the commentary corpus lets the workspace carry better, and which gains justify local proposal, bounded stress test, reviewer-register use, or no inheritance
- requested model / reasoning: `opus[1m]` / `max`
- requested launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`, repo-local prompt/spec path, `--dangerously-skip-permissions`
- prompt artifact: [lane-04-opus47-max-carriage-and-operationalization-launch-prompt.md](lane-04-opus47-max-carriage-and-operationalization-launch-prompt.md)
- governing spec: [OPUS-CARRIAGE-AND-OPERATIONALIZATION-SPEC.md](OPUS-CARRIAGE-AND-OPERATIONALIZATION-SPEC.md)
- output artifact: [lane-04-opus47-max-carriage-and-operationalization-review.md](lane-04-opus47-max-carriage-and-operationalization-review.md)
- probe summary:
  - exit code: `0`
  - elapsed seconds: `861.450`
  - session id: `58337010-93f4-4180-b024-05455948d63e`
  - total cost usd: `4.78199575`
  - stdout/stderr/debug artifacts:
    - `/tmp/lane-04-opus47-max-carriage-and-operationalization-r1-20260419-154747.c4x9auj9.stream.jsonl`
    - `/tmp/lane-04-opus47-max-carriage-and-operationalization-r1-20260419-154747.p9cp_6e5.stderr.log`
    - `/tmp/lane-04-opus47-max-carriage-and-operationalization-r1-20260419-154747.e8p4i9ku.debug.log`
- parallel local reviewer:
  - launch mode: `spawn_agent`
  - effective settings verified against `~/.codex/state_5.sqlite`: `worker / gpt-5.4 / xhigh`
  - brief artifact: [lane-04-gpt54-xhigh-carriage-and-operationalization-brief.md](lane-04-gpt54-xhigh-carriage-and-operationalization-brief.md)
  - output artifact: [lane-04-gpt54-xhigh-carriage-and-operationalization-review.md](lane-04-gpt54-xhigh-carriage-and-operationalization-review.md)
- disposition:
  - [lane-04-comparative-disposition.md](lane-04-comparative-disposition.md)
  - `partial accept / synthesis accept`
  - both reviews are inherited through the comparative disposition rather than treated as unresolved challenge outputs
  - accepted overlap: Surface A proposal now, Surface B bounded stress tests, Surface C no rewrite on this evidence, Surface D bounded carrier-level experimentation

## 2026-04-19 `lane-05`

- date: `2026-04-19`
- purpose: contract-level cross-review of the drafted main-wave launch contract, including pre-Wave-1 organization and version-control / change-management concerns
- requested model / reasoning: `opus[1m]` / `max`
- requested launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`, repo-local prompt/spec path, `--dangerously-skip-permissions`
- prompt artifact: [lane-05-opus47-max-main-wave-contract-cross-review-launch-prompt.md](lane-05-opus47-max-main-wave-contract-cross-review-launch-prompt.md)
- governing spec: [OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md](OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md)
- output artifact: [lane-05-opus47-max-main-wave-contract-cross-review.md](lane-05-opus47-max-main-wave-contract-cross-review.md)
- probe summary:
  - exit code: `0`
  - elapsed seconds: `340.343`
  - session id: `d2701eda-7264-4552-aadc-1ac65313a7ab`
  - total cost usd: `2.16682925`
  - stdout/stderr/debug artifacts:
    - `/tmp/lane-05-opus47-max-main-wave-contract-cross-review-r1-20260419-173645.0b77712t.stream.jsonl`
    - `/tmp/lane-05-opus47-max-main-wave-contract-cross-review-r1-20260419-173645.7gx71156.stderr.log`
    - `/tmp/lane-05-opus47-max-main-wave-contract-cross-review-r1-20260419-173645.yv0eq1al.debug.log`
- parallel local reviewer:
  - launch mode: `spawn_agent`
  - effective settings verified against `~/.codex/state_5.sqlite`: `worker / gpt-5.4 / xhigh`
  - brief artifact: [lane-05-gpt54-xhigh-main-wave-contract-cross-review-brief.md](lane-05-gpt54-xhigh-main-wave-contract-cross-review-brief.md)
  - output artifact: [lane-05-gpt54-xhigh-main-wave-contract-cross-review.md](lane-05-gpt54-xhigh-main-wave-contract-cross-review.md)
- disposition:
  - [lane-05-comparative-disposition.md](lane-05-comparative-disposition.md)
  - `synthesis accept`
  - no further pre-contract meta lane justified
  - accepted now: concrete Wave-1 packet manifests, stronger contract carry for switch triggers and anti-tame obligations, bounded launch-discipline carry
  - blocked later: first external Wave-1 launch remains blocked until the audit workspace has an auditable checkpoint commit and frozen-packet SHA recording
  - not earned: broad pre-Wave-1 directory reorganization, repo-wide workflow redesign, or readiness-package mutation
