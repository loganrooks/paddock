Date: 2026-04-22
Status: prepared launch-truth record

# Harness Modifier Project Uplift Post-Neutralization Payload-Home Judgment Reread Launch Truth

- [d:r:i] Lane id: `06`
- [d:r:i] Family: `extraction-audit`
- [d:r:i] Frozen launch basis commit: `TBD`
- [d:r:i] Requested reviewer: `Opus 4.7 Max`
- [d:r:i] Requested runtime string: `opus[1m]`
- [d:r:i] Requested reasoning effort: `xhigh`
- [d:r:i] Estimated wall-clock duration: `8-14 minutes`
- [d:r:i] Packet:
  - [../packets/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-packet.md](../packets/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-packet.md)
- [d:r:i] Spec:
  - [../specs/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-spec.md](../specs/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-spec.md)
- [d:r:i] Prompt:
  - [../prompts/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-opus47-max-r1-launch-prompt.md](../prompts/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-opus47-max-r1-launch-prompt.md)
- [d:r:i] Reserved output:
  - [../outputs/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-opus47-max-r1.md](../outputs/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-opus47-max-r1.md)
- [d:r:i] Launch command:

```bash
python3 tooling/codex/run_claude_probe.py \
  --label extraction-audit-06 \
  --model 'opus[1m]' \
  --effort xhigh \
  --dangerously-skip-permissions \
  --output-dir .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/06 \
  --prompt-file .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/prompts/06-harness-modifier-project-uplift-post-neutralization-payload-home-judgment-reread-opus47-max-r1-launch-prompt.md \
  > .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/06/probe-summary.txt
```

- [d:r:i] Probe summary:
  - exit code: `pending`
  - elapsed seconds: `pending`
  - session id: `pending`
  - total cost usd: `pending`
