Date: 2026-04-22
Status: active launch-truth record

# Harness Modifier First Overlay Filesystem Rehome Reread Launch Truth

## Frozen Basis

- [g:r:i] Frozen launch basis commit: `ed3a17b`
- [e:c+i] Packet: [../packets/03-harness-modifier-first-overlay-filesystem-rehome-reread-packet.md](../packets/03-harness-modifier-first-overlay-filesystem-rehome-reread-packet.md)
- [e:c+i] Spec: [../specs/03-harness-modifier-first-overlay-filesystem-rehome-reread-spec.md](../specs/03-harness-modifier-first-overlay-filesystem-rehome-reread-spec.md)
- [e:c+i] Opus prompt: [../prompts/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1-launch-prompt.md](../prompts/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1-launch-prompt.md)

## Requested Output

- [e:c+i] Final lane output:
  - [../outputs/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1.md](../outputs/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1.md)

## Requested Launch Mode

- [d:r:i] Requested operator-facing model / reasoning: `Opus 4.7 Max` / `xhigh`
- [d:r:i] Effective Claude model string: `opus[1m]`
- [d:r:i] Launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label extraction-audit-03 --model 'opus[1m]' --effort xhigh --dangerously-skip-permissions --output-dir .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/03 --prompt-file .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/prompts/03-harness-modifier-first-overlay-filesystem-rehome-reread-opus47-max-r1-launch-prompt.md > .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/03/probe-summary.txt`

## Timing

- [d:r:i] Pre-launch estimate: `10-16 minutes`
- [o:r:i] Actual elapsed seconds: pending return
- [o:r:i] Timing calibration: pending return

## Launch Note

- [d:r:i] This lane is intentionally narrower than the earlier overlay-carrier reread: the question is not whether overlay extraction remains the right family, but what the landed first specialist source split now actually clarifies and what exact next slice it now earns.
- [d:r:i] Standalone repo split, package distribution, and second-host exercise remain explicitly outside this lane.

## Return Summary

- [o:r:i] Exit code: pending return
- [o:r:i] Session id: pending return
- [o:r:i] Total cost usd: pending return
- [e:c+i] Repo-local artifacts reserved or active:
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/03/probe-summary.txt`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/03/extraction-audit-03-20260422-171221.lakfwtu5.stream.jsonl`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/03/extraction-audit-03-20260422-171221.289tdxux.stderr.log`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/03/extraction-audit-03-20260422-171221.6tk25w9u.debug.log`
