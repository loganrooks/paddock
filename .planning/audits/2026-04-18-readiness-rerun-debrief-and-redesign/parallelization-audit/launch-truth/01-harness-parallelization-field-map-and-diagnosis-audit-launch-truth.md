Date: 2026-04-22
Status: launched capture

# Harness Parallelization Field Map And Diagnosis Audit Launch Truth

## Frozen Basis

- [g:r:i] Frozen launch basis commit: `6f2dc74`
- [e:c+i] Packet:
  - [../packets/01-harness-parallelization-field-map-and-diagnosis-audit-packet.md](../packets/01-harness-parallelization-field-map-and-diagnosis-audit-packet.md)
- [e:c+i] Spec:
  - [../specs/01-harness-parallelization-field-map-and-diagnosis-audit-spec.md](../specs/01-harness-parallelization-field-map-and-diagnosis-audit-spec.md)
- [e:c+i] Opus prompt:
  - [../prompts/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-launch-prompt.md](../prompts/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-launch-prompt.md)

## Requested Output

- [e:c+i] Final lane output:
  - [../outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md](../outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md)
- [e:c+i] Local inheritance:
  - [../dispositions/01-harness-parallelization-field-map-and-diagnosis-audit-inheritance.md](../dispositions/01-harness-parallelization-field-map-and-diagnosis-audit-inheritance.md)

## Requested Launch Mode

- [d:r:i] Requested operator-facing model / reasoning: `Opus 4.7 Max` / `xhigh`
- [d:r:i] Effective Claude model string: `opus[1m]`
- [d:r:i] Launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label parallelization-audit-01 --model 'opus[1m]' --effort xhigh --dangerously-skip-permissions --output-dir .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01 --prompt-file .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/prompts/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-launch-prompt.md > .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/probe-summary.txt`

## Timing

- [d:r:i] Pre-launch estimate: `14-22 minutes`
- [d:r:i] Timing calibration note:
  - this lane is broader than the recent extraction rereads because it spans upstream vanilla surfaces, modified-harness surfaces, and harness-improvement-program overlap doctrine rather than one bounded local family only

## Probe Status

- [e:r:i] Local monitoring session:
  - `23887`
- [e:r:i] Current state:
  - `running`
- [e:r:i] Repo-local artifacts:
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/probe-summary.txt`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/parallelization-audit-01-20260422-222056.dkqbcr7b.stream.jsonl`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/parallelization-audit-01-20260422-222056.l0sg6lnx.stderr.log`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/parallelization-audit-01-20260422-222056.ajq2b5wh.debug.log`

## Current Consequence

- [d:r:i] The lane is now reading on a frozen basis.
- [d:r:i] While it runs, safe companion work must stay off the packet/spec/prompt and off the governed read-set surfaces the lane is currently using.
