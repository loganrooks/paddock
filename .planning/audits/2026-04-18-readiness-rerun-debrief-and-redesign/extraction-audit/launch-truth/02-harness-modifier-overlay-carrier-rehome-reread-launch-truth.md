Date: 2026-04-22
Status: active launch-truth record

# Harness Modifier Overlay Carrier Rehome Reread Launch Truth

## Frozen Basis

- [g:r:i] Frozen launch basis commit: `d6b7989`
- [e:c+i] Packet: [../packets/02-harness-modifier-overlay-carrier-rehome-reread-packet.md](../packets/02-harness-modifier-overlay-carrier-rehome-reread-packet.md)
- [e:c+i] Spec: [../specs/02-harness-modifier-overlay-carrier-rehome-reread-spec.md](../specs/02-harness-modifier-overlay-carrier-rehome-reread-spec.md)
- [e:c+i] Opus prompt: [../prompts/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1-launch-prompt.md](../prompts/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1-launch-prompt.md)

## Requested Output

- [e:c+i] Final lane output:
  - [../outputs/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1.md](../outputs/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1.md)

## Requested Launch Mode

- [d:r:i] Requested operator-facing model / reasoning: `Opus 4.7 Max` / `xhigh`
- [d:r:i] Effective Claude model string: `opus[1m]`
- [d:r:i] Launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label extraction-audit-02 --model 'opus[1m]' --effort xhigh --dangerously-skip-permissions --output-dir .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/02 --prompt-file .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/prompts/02-harness-modifier-overlay-carrier-rehome-reread-opus47-max-r1-launch-prompt.md > .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/02/probe-summary.txt`

## Timing

- [d:r:i] Pre-launch estimate: `12-18 minutes`
- [o:r:i] Actual elapsed seconds: pending
- [o:r:i] Timing calibration: pending completion

## Launch Note

- [d:r:i] This lane explicitly asks Opus to keep harness-uplift horizons distinct from host-product planning horizons because co-location confusion is now one of the extraction pressures.
- [d:r:i] The question at this boundary is the overlay/workflow/skill/reference tranche, not repo split or npm packaging.

## Return Summary

- [o:r:i] Exit code: pending
- [o:r:i] Session id: pending
- [o:r:i] Total cost usd: pending
- [o:r:i] Repo-local artifacts: pending completion
