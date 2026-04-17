# Support Note: Claude CLI Session Persistence Forensics

Status: `active support note`

Scope: recover the stuck `lane-01c` Claude Code CLI run and preserve a future audit trail about where Claude Code does and does not persist session state.

## Official Baseline

- [e:c:d] Claude Code's default storage root is `~/.claude`, and `CLAUDE_CONFIG_DIR` relocates the whole config tree rather than only one subpath.[^1]
- [e:c:d] The official `.claude` inventory explicitly includes `projects/`, `projects/<project>/<session>/tool-results/`, `debug/`, `session-env/`, and `shell-snapshots/`.[^2]
- [e:c:d] Official session transcripts are written as JSONL under `projects/<encoded-cwd>/<session-id>.jsonl`, and official hooks docs expose subagent transcript paths under the parent session's `subagents/` directory.[^3][^4]
- [e:c:d] Headless `claude -p` runs still participate in the normal session model unless persistence is explicitly disabled via `--no-session-persistence` or `CLAUDE_CODE_SKIP_PROMPT_HISTORY=1`.[^1][^5]
- [e:c:d] Official checkpointing and changelog material warns that resume depends on matching the original absolute working directory and that transcript persistence has had real failure modes rather than perfect reliability.[^6][^7]

## Unofficial Pressure

- [e:c:d] Public issue history adds three recovery-relevant hazards that the official docs do not spell out cleanly: headless runs can hang after useful work is effectively done, `--resume` can fail or fork continuity for headless sessions, and transcript files themselves can hit `ENOENT` or open failures under `~/.claude/projects/...`.[^8]
- [a:c:d] Community tooling repeatedly treats `sessions-index.json` as a sidecar that can desync from raw transcript JSONL files and can sometimes be rebuilt from them, but this remains undocumented and should be treated as a recovery hypothesis rather than canonical storage truth.[^9]
- [e:c:d] I did not find strong unofficial evidence for a stable alternate default transcript root outside the active Claude config tree; even the community workarounds still center `~/.claude/projects/...`.[^8][^9]

## Session-Local Cross-Check

Observed during this audit session for stuck PID `328265`:

- the cmdline does not include `--no-session-persistence`
- `/proc/328265/environ` showed no values for `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_SKIP_PROMPT_HISTORY`, `CLAUDE_CODE_DEBUG_LOGS_DIR`, or `CLAUDE_ENV_FILE`
- [lane-01c-claude-opus-1m-execution-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01c-claude-opus-1m-execution-prompt.md) is still `0` bytes
- [lane-01c-claude-opus-1m-prompt-writer.stderr.log](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-01c-claude-opus-1m-prompt-writer.stderr.log) is still `0` bytes

## Working Judgment

- [e:r:i+d] The highest-confidence first inspection target remains `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/-home-rookslog-workspace-projects-prix-guesser/`, because both official docs and unofficial recovery tooling center that tree.[^1][^2][^3][^9]
- [e:r:i+d] If the raw transcript file is absent there, the next better hypotheses are not "the output must be hiding in some other normal default location" but rather: the run stalled before or during transcript persistence, the session landed under a different config root, or an undocumented sidecar/index layer diverged from raw JSONL state.[^1][^7][^8][^9]
- [o:r:i+d] If later recovery work is needed, inspect raw JSONL before trusting resume UIs or community sidecar indexes, and inspect debug files only if debug logging was enabled for that run.[^2][^4][^9]

## What This Does Not Justify

- it does not prove the current stuck `lane-01c` run produced a recoverable transcript
- it does not prove `sessions-index.json` exists in every install or version
- it does not identify a hidden official alternate default transcript root for `claude -p`

## External Works Cited

[^1]: Anthropic, "Environment variables," Claude Code docs. https://code.claude.com/docs/en/env-vars
[^2]: Anthropic, "The .claude Directory," Claude Code docs. https://code.claude.com/docs/en/claude-directory
[^3]: Anthropic, "Agent SDK Sessions," Claude Code docs. https://code.claude.com/docs/en/agent-sdk/sessions
[^4]: Anthropic, "Hooks," Claude Code docs. https://code.claude.com/docs/en/hooks
[^5]: Anthropic, "Run Claude Code non-interactively," Claude Code docs. https://code.claude.com/docs/en/headless
[^6]: Anthropic, "Checkpointing," Claude Code docs. https://code.claude.com/docs/en/checkpointing
[^7]: Anthropic, "Changelog," Claude Code docs. https://code.claude.com/docs/en/changelog
[^8]: Public issue reports: `#1920`, `#3187`, `#3188`, `#1519`, `#2410`, `#5768`, and `#9188` in `anthropics/claude-code`. https://github.com/anthropics/claude-code/issues/1920 https://github.com/anthropics/claude-code/issues/3187 https://github.com/anthropics/claude-code/issues/3188 https://github.com/anthropics/claude-code/issues/1519 https://github.com/anthropics/claude-code/issues/2410 https://github.com/anthropics/claude-code/issues/5768 https://github.com/anthropics/claude-code/issues/9188
[^9]: Community recovery scripts and session managers discussing `sessions-index.json` and raw `.jsonl` recovery. https://gist.github.com/tirufege/0720c288092c1a3a4750f7c198aa524b https://gist.github.com/GMNGeoffrey/77e8115bf11fa91fee953b374f0c8737
