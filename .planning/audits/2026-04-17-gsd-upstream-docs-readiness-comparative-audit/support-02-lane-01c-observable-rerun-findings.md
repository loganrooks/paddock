# Support Note: Lane 01c Observable Rerun Findings

Status: `active support note`

## What Happened

- [e:c:i] The observable rerun started a real Claude session and emitted `system/init`, so the rerun did not die before session start. Source: `lane-01c-claude-opus-1m-observable-rerun.stream.jsonl`.
- [e:c:i] The rerun then failed immediately with `authentication_failed` and assistant text `Not logged in · Please run /login`. Source: `lane-01c-claude-opus-1m-observable-rerun.stream.jsonl`.
- [e:c:i] The init event reported `apiKeySource: "none"`, which the debug log corroborates with `Could not resolve authentication method` and `No API key available`. Sources: `lane-01c-claude-opus-1m-observable-rerun.stream.jsonl`; `lane-01c-claude-opus-1m-observable-rerun.debug.log`.
- [e:c:i] The dedicated stderr log remained empty, which means the useful diagnosis came from the stream-json and debug channels rather than plain stderr. Source: `lane-01c-claude-opus-1m-observable-rerun.stderr.log`.

## Session Identity

- session id: `6a7937a5-6010-4a9d-a005-f8eb422ab8bd`
- Claude version: `2.1.112`
- model string from init event: `claude-opus-4-7[1m]`

## Consequence

- [e:r:i] The original "pre-transcript / pre-first-byte stall" judgment is no longer the best global explanation for the environment. Under a more observable launch shape, Claude reaches init and then fails on missing authentication rather than hanging indefinitely.
- [o:r:i] This does not fully prove the first run failed for the exact same reason, because the observable rerun changed startup conditions with `--bare`, closed stdin, `stream-json`, and a dedicated debug file. But it does establish a concrete blocking issue that must be fixed before the prompt-writer can succeed.

## Practical Next Step

- complete Claude authentication in this shell environment, either by `/login` or by providing a valid API key/token path that Claude Code can resolve
- then rerun `lane-01c-claude-opus-1m-observable-rerun.sh`

## Falsifier Kept Explicit

- if a post-login rerun still hangs before producing either assistant text or a result event, then the auth failure was not the whole story and the next diagnosis should focus on startup/discovery differences between the observable and original launches
