# Lane 01c Observable Rerun Notes

Status: `active support note`

Purpose: rerun the `lane-01c` Claude prompt-writer with stronger observability so the repo can distinguish:

- pre-session / pre-first-byte stall
- startup-side stall from hooks, discovery, auth, or open stdin
- post-init failure with hidden stream events
- target-file write failure despite successful model output

## Deliberate Diagnostic Changes

- add `--bare`
  - strips hooks, skills, plugins, MCP auto-discovery, and CLAUDE.md loading from the startup path
- add `--output-format stream-json`
  - exposes `system/init`, assistant, tool, and result events if the session actually starts
- add `--include-partial-messages`
  - preserves partial assistant output if the run fails mid-stream
- add `--verbose`
  - increases visible diagnostic signal
- add `--debug-file`
  - forces a dedicated debug log file for this rerun
- close stdin with `</dev/null`
  - rules out a caller-side hang caused by an open input stream

## Observable Outputs

- stream events:
  - `lane-01c-claude-opus-1m-observable-rerun.stream.jsonl`
- stderr:
  - `lane-01c-claude-opus-1m-observable-rerun.stderr.log`
- debug:
  - `lane-01c-claude-opus-1m-observable-rerun.debug.log`
- extracted assistant text:
  - `lane-01c-claude-opus-1m-execution-prompt-rerun.md`

## Interpretation Rule

- if `system/init` or a session-style event appears in the stream log, the failure is not pre-session
- if the stream log stays empty while the debug file grows, the failure is happening before or around stream setup
- if the stream log contains assistant text but the extracted prompt file stays empty, the failure is in the target-output path rather than the model run itself
