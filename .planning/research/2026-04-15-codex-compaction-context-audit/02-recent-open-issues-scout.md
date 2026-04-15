# Recent Open Issues Scout

Date: 2026-04-15  
Status: completed

## Scope And Scan Method

This scout extended the existing `2026-04-15-codex-compaction-context-audit` bundle by checking unresolved `openai/codex` issues from approximately the last `14` days, with priority on the last `7` days.

Scan method:

- searched the `60` most recent open issues created from `2026-04-01` onward
- prioritized issues created from `2026-04-08` to `2026-04-15`
- deep-read `12` issues and comments on the ones that materially affected interpretation
- clustered rather than exhaustively summarizing every issue because the recent open volume is already high

Branches deliberately deferred:

- older duplicate chains surfaced only by the GitHub bot
- broad desktop/UI bugs without clear compaction, instruction-loading, observability, or recovery relevance
- non-compaction workflow bugs that did not materially change repo guidance

## Official Baseline Used For Comparison

`[e:c:i+d]` `01` already established the official baseline that matters here: Codex does not document a compaction-specific hook, AGENTS loading is path-based, context indicators are not a perfect measure of raw remaining window, and compaction is not a blank-state reset ([01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:12), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:13), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:15), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:16)).

`[e:c:d]` Official app-server docs also already distinguish `thread/read` from `thread/resume`: `thread/read` returns stored thread data without resuming or subscribing to events, while `thread/resume` reopens an existing thread so later work continues on it.[^codex-app-server]

`[s:c:i]` Everything else below is issue-report evidence unless explicitly marked as maintainer clarification or official documentation.

## Cluster 1: Open Compaction And Recovery Failures

### Evidence

`[e:c:d]` Issue `#17928` remains open and reports that the first auto-compaction attempt can freeze the thread with `Error running remote compact task: timeout waiting for child process to exit`, after which `/compact` and even `/feedback` stop working.[^issue-17928][^comment-17928-feedback]

`[e:c:d]` Issue `#17860` remains open and reports that ChatGPT-auth Codex on Linux/WSL2 can get Cloudflare `403` responses across `chatgpt.com` endpoints, including plugin loading and auth refresh. That is not a pure compaction bug, but it is directly recovery-relevant because it can break session renewal and make other failures look like generic Codex instability.[^issue-17860]

`[e:c:d]` Issue `#17951` remains open and reports that when `skills/list` receives proxy-injected HTML instead of JSON, the TUI can crash rather than degrade gracefully. This is adjacent rather than central, but it matters because it turns a network/auth failure into loss of an important continuity surface.[^issue-17951]

`[e:c:d]` Issue `#17880` is still open, but its root-cause narrative is not confirmed. A maintainer explicitly said the report mixed too many symptoms and was not actionable as filed.[^issue-17880][^comment-17880-maintainer]

### Comment-Derived Guidance

`[e:c:d]` In `#17928`, the reporter added that switching to `gpt-5.3-codex` allowed compaction to succeed once, after which switching back to `gpt-5.4` let work continue.[^comment-17928-model-switch] That is a public anecdotal workaround, not a product guarantee.

### Inference

`[e:c+r:d]` The unresolved compaction risk is now narrower than the first-pass `01` issue sweep implied. The still-open surface is not mainly "early compaction because the meter is weird"; it is a runtime-recovery class where remote compaction, ChatGPT-auth, proxy/Cloudflare interference, and failure handling can leave a thread frozen, misleadingly reset, or unable to recover cleanly.[^issue-17928][^issue-17860][^issue-17951]

### Unknowns

- No open maintainer comment in this scout confirmed the root cause of `#17928`.
- `#17880` may describe a real failure mode, but the current issue text is too conflated to treat its causal chain as established.
- It is still unclear how much of this cluster is model-specific, auth-path-specific, or environment-specific.

## Cluster 2: Open Instruction-Loading And Observability Mismatches

### Evidence

`[e:c:d]` Issue `#17776` remains open and reports that `/status` can show `Agents.md: <none>` even when fresh sessions still load and obey AGENTS rules.[^issue-17776]

`[e:c:d]` Issue `#17939` remains open and reports the inverse failure mode in Codex Desktop: a stale `Non-Git Workspace` developer instruction block can be injected inside a real Git repository, overriding project/user formatting expectations with incorrect higher-priority instructions.[^issue-17939][^comment-17939-bundle]

### Inference

`[e:c+r:d]` For this repo, the live observability problem is therefore broader than "`/status` may under-report AGENTS loading." Recent open evidence includes both under-reporting of real instruction state (`#17776`) and over-injection of false developer instruction state (`#17939`).[^issue-17776][^issue-17939]

`[e:c+r:i+d]` That strengthens `01`'s advice to treat status surfaces as advisory rather than authoritative, but it does not justify stuffing more standing text into AGENTS files. This repo already treats prompt budget and stale instruction risk as first-class concerns ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:203), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:208)).

### Unknowns

- `#17939` is desktop-specific, so it is not direct evidence about the CLI path this repo usually uses.
- There was no maintainer clarification in the open `#17776` thread during this scout window.

## Cluster 3: Open Resume And Session-Continuity Gaps

### Evidence

`[e:c:d]` Issue `#17560` remains open and reports that resumed sessions in WSL can restore a different effective project context than a fresh session in the same directory, including an empty `$` skill picker and diverged project-local MCP/skill behavior.[^issue-17560]

`[e:c:d]` The reporter later clarified that the resumed path can change case inside `/mnt/...` (`/mnt/<drive>/Program/...` becoming `/mnt/<drive>/program/...`), which could plausibly affect project-local state restoration on case-sensitive path handling.[^comment-17560-path]

`[e:c:d]` Issue `#17900` remains open as a docs request, but it does not show an undocumented hidden capability. It instead highlights that integrators still misread `thread/read` as if it were enough to reattach to live session flow, even though official docs already distinguish `thread/read` from `thread/resume`.[^issue-17900][^codex-app-server][^comment-17900-docs]

### Inference

`[e:c+r:i+d]` For this repo, the important risk is that "resume the thread" and "get the same effective workspace-derived execution context back" are not currently equivalent claims. That lines up with the repo's existing readiness posture: important Phase `01` rerun state should live in files, not ambient session memory or assumed resume fidelity ([INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md:5), [.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:14), [.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:16)).

### Unknowns

- `#17560` is WSL-path-specific on the current evidence.
- `#17900` is about docs semantics, so it does not itself prove a runtime defect beyond user confusion or integration drift.

## Maintainer Clarifications That Narrow What `01` Should Still Lean On

These are not unresolved open issues, but they materially change how the earlier `01` artifact should be read.

`[e:c:d]` The `0.120.0` resumed-thread remote-compaction regression from `#17819` is no longer an active unresolved signal for this scout. A maintainer said the causing change was rolled back and "should be addressed now."[^issue-17819][^comment-17819-rollback]

`[e:c:d]` The missing context percentage complaint from `#17874` is also no longer an active unresolved signal for this scout. A maintainer said it was "already fixed on main."[^issue-17874][^comment-17874-fixed]

`[e:c:d]` Two other issues emphasized in `01` are also no longer unresolved open evidence as of this scout: `#17912` and `#17940` are now closed.[^issue-17912][^issue-17940]

## Repo-Specific Implications

`[e:c:i+d]` The repo's artifact-first continuity posture remains correct and is slightly strengthened. Open issue evidence still says resumed or status-visible state can diverge from actual effective context (`#17560`, `#17776`, `#17939`), while the repo already treats rerun readiness as something that must survive context compaction explicitly in files, not in thread memory ([INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md:5), [.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:14), [.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:16)).

`[p:r:i+d]` When a future session is resumed rather than started fresh, this repo should assume a verification step is required before trusting continuity:

- confirm the working directory is what the repo expects
- sanity-check instruction/application behavior rather than trusting `/status` alone
- verify expected skills/MCP surfaces if the task depends on them
- treat odd behavior near compaction as possibly auth/proxy/runtime related, not automatically as repo-local prompt-budget failure

`[p:r:i+d]` Because the repo already asks whether new standing instruction is specific enough to deserve prompt budget, the correct response to this open-issue surface is not "put more hidden recovery rules in AGENTS." It is "keep the durable recovery protocol in repo files and verify runtime state when re-entering a session." ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:203), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:208))

## Should `01` Be Materially Qualified?

`[e:c+r:i+d]` Yes, but the qualification is about current unresolved weighting, not about overturning `01`'s core doctrine.

What should change:

1. `01` should stop treating the `0.119.0` rollback from `#17819` as a live default mitigation. That is now a historical incident note, not the best current generic advice ([01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:77)).[^comment-17819-rollback]
2. `01` should stop weighting the missing context percentage issue as unresolved current evidence. That signal was real for the `0.120.0` snapshot, but it is no longer a live open-issue blocker after the maintainer clarification.[^comment-17874-fixed]
3. `01` should add or strengthen a distinct `resume-state-restoration` lane. The newly emphasized unresolved issue surface is not only about compaction timing or meter visibility; it also includes "resume may not reconstruct the same workspace-derived context as a fresh session" (`#17560`) and "status/instruction surfaces may not reflect true effective context" (`#17776`, `#17939`).[^issue-17560][^issue-17776][^issue-17939]

What should not change:

- `01`'s official-baseline section remains sound.
- `01`'s larger repo-level posture remains sound or slightly stronger: do not rely on undocumented hooks, do not trust UI/status surfaces blindly, and keep durable rerun continuity in repo artifacts rather than ambient thread memory ([01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:71), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:72), [01-codex-compaction-context-behavior-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-codex-compaction-context-audit/01-codex-compaction-context-behavior-research.md:76)).

## External Works Cited

[^codex-app-server]: OpenAI Developers, "App Server – Codex," section covering `thread/resume` and `thread/read`, https://developers.openai.com/codex/app-server
[^issue-17560]: `openai/codex` issue `#17560`, open, created 2026-04-12, "Resume does not restore the same project context as a fresh session in WSL (project-local MCP/skills diverge, `$` skill picker becomes empty)," https://github.com/openai/codex/issues/17560
[^comment-17560-path]: `openai/codex` issue `#17560` comment on WSL path-case change, https://github.com/openai/codex/issues/17560#issuecomment-4232567631
[^issue-17776]: `openai/codex` issue `#17776`, open, created 2026-04-14, "/status no longer reports AGENTS.md in 0.120.0," https://github.com/openai/codex/issues/17776
[^issue-17819]: `openai/codex` issue `#17819`, closed, created 2026-04-14, "0.120.0 regression: resumed threads fail during remote compaction with \"Unknown parameter: 'prompt_cache_retention'\"," https://github.com/openai/codex/issues/17819
[^comment-17819-rollback]: `openai/codex` issue `#17819` maintainer comment stating the regression-causing change was rolled back, https://github.com/openai/codex/issues/17819#issuecomment-4246256107
[^issue-17860]: `openai/codex` issue `#17860`, open, created 2026-04-15, "Linux/WSL2: Cloudflare 403 blocks all chatgpt.com API requests — rustls TLS fingerprint detected as bot while macOS native-tls works fine on same network," https://github.com/openai/codex/issues/17860
[^issue-17874]: `openai/codex` issue `#17874`, closed, created 2026-04-15, "Bring back % for token use in statusline," https://github.com/openai/codex/issues/17874
[^comment-17874-fixed]: `openai/codex` issue `#17874` maintainer comment stating the change was already fixed on main, https://github.com/openai/codex/issues/17874#issuecomment-4248577388
[^issue-17880]: `openai/codex` issue `#17880`, open, created 2026-04-15, "[Bug] ChatGPT Plus integration/DesktopApp/IDE loses chat history and triggers false rate limits due to unresolved Cloudflare CAPTCHAs," https://github.com/openai/codex/issues/17880
[^comment-17880-maintainer]: `openai/codex` issue `#17880` maintainer comment rejecting the issue as too conflated to act on as filed, https://github.com/openai/codex/issues/17880#issuecomment-4248864627
[^issue-17900]: `openai/codex` issue `#17900`, open, created 2026-04-15, "Clarify thread/read vs thread/resume semantics in integration docs," https://github.com/openai/codex/issues/17900
[^comment-17900-docs]: `openai/codex` issue `#17900` maintainer comment pointing to the official app-server docs, https://github.com/openai/codex/issues/17900#issuecomment-4249773389
[^issue-17912]: `openai/codex` issue `#17912`, closed, created 2026-04-15, "Auto-compaction near high context usage can make Codex answer the previous message instead of the current one," https://github.com/openai/codex/issues/17912
[^issue-17928]: `openai/codex` issue `#17928`, open, created 2026-04-15, "Threads freeze and errors for 2 days already Error running remote compact task: timeout waiting for child process to exit," https://github.com/openai/codex/issues/17928
[^comment-17928-feedback]: `openai/codex` issue `#17928` reporter comment noting `/feedback` was also unusable after the failure, https://github.com/openai/codex/issues/17928#issuecomment-4251615641
[^comment-17928-model-switch]: `openai/codex` issue `#17928` reporter comment describing a one-time workaround by switching models, https://github.com/openai/codex/issues/17928#issuecomment-4251650826
[^issue-17939]: `openai/codex` issue `#17939`, open, created 2026-04-15, "Codex Desktop injects stale Non-Git Workspace citation instructions inside a Git repo," https://github.com/openai/codex/issues/17939
[^comment-17939-bundle]: `openai/codex` issue `#17939` follow-up comment locating the prompt block in the app bundle, https://github.com/openai/codex/issues/17939#issuecomment-4252577800
[^issue-17940]: `openai/codex` issue `#17940`, closed, created 2026-04-15, "/compact and auto compact always time out," https://github.com/openai/codex/issues/17940
[^issue-17951]: `openai/codex` issue `#17951`, open, created 2026-04-15, "TUI crashes when skills/list fails behind corporate proxy," https://github.com/openai/codex/issues/17951
