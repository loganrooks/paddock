# Codex Compaction And Context Behavior Research

Date: 2026-04-15  
Status: completed

## Scope

This pass prioritized official OpenAI Codex docs and official `openai/codex` source first, then checked recent public GitHub issue reports from roughly 2026-03-15 onward.

## Direct Answers

- `[e:c:d]` No official compaction-specific hook surface is currently documented for Codex. The public hooks surface lists `SessionStart`, `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, and `Stop`; the public config surface exposes `codex_hooks`, but not a compaction event or post-compaction callback.[^codex-hooks][^codex-config]
- `[e:c:d]` Officially known about Codex compaction: Codex has manual `/compact`; Codex also has automatic compaction driven by a token threshold; model metadata clamps that threshold to at most `90%` of raw context window; usable context is separately discounted by `effective_context_window_percent`, which defaults to `95`; and the context-left UI further normalizes around a fixed `12,000`-token baseline for prompts/tools/compact overhead.[^codex-slash][^codex-openai-models][^codex-protocol][^codex-codex]
- `[o:c:d]` Officially unknown or underspecified: OpenAI's public Codex docs do not give a full product-level prose spec for exactly how CLI/App compaction preserves, drops, or orders prior conversational material in every surface; they do not document a compaction hook; and they do not promise that post-compaction headroom returns to `100%` or that compaction fires only when the visible meter reaches zero.[^codex-hooks][^codex-slash][^api-compaction]
- `[e:c+r:d]` Compaction can happen before the visible meter hits zero for three official reasons. First, auto-compaction triggers at `>= auto_compact_token_limit`, which defaults to `90%` of raw context window rather than `100%`.[^codex-openai-models][^codex-codex] Second, Codex only treats `95%` of the raw window as usable by default, reserving headroom for system/tool/output overhead.[^codex-openai-models][^codex-codex] Third, the UI percentage subtracts a `12,000`-token baseline from both numerator and denominator, so the visible `% left` is already a normalized "user-controllable" number rather than the raw empty space in the model window.[^codex-protocol]
- `[e:c+r:d]` Post-compaction headroom can remain well below `100%` because compaction does not reset the thread to blank state. Official API docs say the returned compacted window can contain more than just the compaction item and should be reused as-is; the Codex source shows replacement history retaining a summary, selected recent user messages, optional reinjected initial context, and ghost snapshots before token usage is recomputed.[^api-compaction][^codex-compact][^codex-compact-remote]
- `[e:c+r:i+d]` Repo-local instruction loading can consume meaningful budget. Official source shows Codex concatenates `AGENTS.md` files from project root to current working directory, truncating only when `project_doc_max_bytes` is exhausted, and merges those docs with configured user instructions plus some feature-generated instruction blocks.[^codex-agents][^codex-project-doc][^codex-config] In this repo, local measurement on 2026-04-15 put `AGENTS.md` at `9,539` bytes, `.planning/AGENTS.md` at `9,496` bytes, and `.planning/readiness/phase-01-rerun/AGENTS.md` at `2,442` bytes. The repo already treats prompt budget as a real constraint when deciding whether durable instruction belongs in `AGENTS.md` at all ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:208)).

## Official Evidence

### Hooks

`[e:c:d]` The official hooks page exposes only five event classes and none of them is compaction-specific.[^codex-hooks] That matters for this repo because the existing hooks pilot is intentionally narrow and experimental ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:138)); there is no official hook surface to "repair" or force post-compaction readiness reloads automatically.

### Instruction Loading

`[e:c:d]` Official AGENTS guidance and Codex source agree on the discovery model: Codex walks from project root to current working directory, prefers `AGENTS.override.md` over `AGENTS.md` where present, concatenates the discovered docs, and caps inclusion with `project_doc_max_bytes`.[^codex-agents][^codex-project-doc][^codex-config]

`[e:c+r:i+d]` In this repo, which instruction layers load depends on where the session starts. A root-started session only needs the root file in scope; a session started under `.planning/` adds `.planning/AGENTS.md`; a session started under `.planning/readiness/phase-01-rerun/` adds that subtree-local `AGENTS.md` too.[^codex-project-doc] See [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:17), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:5), and [.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:3).

### Thresholds And Meter Math

`[e:c:d]` Source-level model metadata sets default usable-window headroom to `95%` and clamps automatic compaction to `90%` of raw context window when a context window is known.[^codex-openai-models] The turn code applies that `95%` reduction before reporting model context window to the UI and token tracker.[^codex-codex]

`[e:c+r:d]` The visible meter is therefore not "time until raw window equals zero." It is time until the normalized user-controllable remainder is exhausted after subtracting the fixed baseline.[^codex-protocol] With the current default math, auto-compaction can plausibly arrive while the UI still shows a few percent remaining rather than `0%`. The exact value varies by model/window, but the mechanism is official.

### What Compaction Keeps

`[e:c:d]` The public API compaction guide explicitly says a compacted window "generally contains more than just the compaction item" and should be passed forward as the next context window rather than pruned.[^api-compaction]

`[e:c:d]` Codex's local compaction path keeps a summary plus selected recent user messages up to a `20,000`-token cap, optionally reinjects initial context for mid-turn compaction, preserves ghost snapshots, replaces history with that compacted set, recomputes token usage, and emits an explicit warning that long threads and multiple compactions can reduce accuracy.[^codex-compact]

`[e:c:d]` Codex's remote compaction path also trims history to fit, preserves ghost snapshots, filters stale developer-message duplication, may reinject initial context, replaces history, and recomputes token usage.[^codex-compact-remote]

### Known Implementation Limits

`[e:c:d]` The current Codex source contains an explicit TODO noting that pre-turn compaction runs before pending context updates and the new user message are recorded, and should eventually estimate those incoming items preemptively.[^codex-codex] That does not prove the full cause of every user-visible surprise, but it is official evidence that compaction timing is not yet modeled as a perfect "visible meter reaches zero, then compact" rule.

## Recent Public Reports

The items below are public user reports, not official product guarantees. They are useful as symptom evidence and workaround evidence only.

- `[e:c:d]` 2026-04-14: issue `#17776` reports that `/status` in `0.120.0` showed `Agents.md: <none>` even though fresh sessions still applied AGENTS rules correctly.[^issue-17776]
- `[e:c:d]` 2026-04-14: issue `#17819` reports a `0.120.0` regression where resumed long-running threads failed during remote compaction with `Unknown parameter: 'prompt_cache_retention'`; the reported workaround was rolling back to `@openai/codex@0.119.0`.[^issue-17819]
- `[e:c:d]` 2026-04-15: issue `#17874` reports that loss of the explicit context percentage made it harder to manage turns before compaction.[^issue-17874]
- `[e:c:d]` 2026-04-15: issue `#17912` reports that auto-compaction near high context usage could cause Codex to answer the previous message instead of the current one.[^issue-17912]
- `[e:c:d]` 2026-04-15: issue `#17940` reports `/compact` and auto-compaction timing out, with the context indicator resetting even though remote compaction did not actually complete.[^issue-17940]

`[e:c+r:d]` Taken together, those reports point to a recent April 2026 cluster around three themes: compaction reliability regressions, weak observability around remaining context, and UI/status surfaces that can mislead users about what instructions or context state are really active.[^issue-17776][^issue-17819][^issue-17874][^issue-17912][^issue-17940]

## Repo-Specific Interpretation

`[e:c:i]` This repo already has direct evidence that "ambient session memory" is not a safe carrier for important rerun state. The readiness package says it exists because the repo now has enough doctrine, governance cleanup, and audit history that a single prose plan is no longer enough to carry the work safely across context compaction ([INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md:5)).

`[e:c:i]` The readiness subtree then doubles down on that posture by stating its job is to keep rerun preparation explicit across context compaction and stop readiness work from drifting back into ambient session memory ([.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:14), [.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:16)).

`[e:c:i+d]` For this repo, the main compaction risk is therefore not just "losing chat history." It is losing the precise governance/readiness distinctions that prevent a rerun from silently flattening doctrine, phase boundaries, or review state. That is why the repo keeps insisting that root and planning AGENTS stay narrow and prompt-budget-aware ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:203), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:208)) while also moving durable continuity into repo files instead of the thread.

## Practical Mitigations For This Repo

1. Do not plan around a post-compaction hook. There is no official compaction hook surface, and this repo's current hooks pilot is intentionally limited to `SessionStart` and `PreToolUse` anyway ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:139), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:141)).
2. Keep durable continuity in repo artifacts, not in the live thread. For rerun work, that means continuing to treat the readiness package as the operational carrier across sessions and compactions, not as optional backup text ([INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md:3), [.planning/readiness/phase-01-rerun/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:20)).
3. Start new threads at coherent checkpoint boundaries rather than letting one thread absorb repeated compactions. That recommendation is consistent with both the repo's checkpoint doctrine and Codex's own warning that long threads and repeated compactions reduce accuracy.[^codex-compact]
4. Be deliberate about starting directory. If a future session starts inside `.planning/` or the readiness subtree, more `AGENTS.md` layers will stack into prompt budget automatically; start at repo root when that extra local doctrine is not needed for the task.[^codex-project-doc]
5. Continue slimming durable instruction files when a rule does not justify prompt-time budget. The repo explicitly asks whether new standing instruction is specific enough to deserve that budget, and this research confirms the budget cost is real ([.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:208), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:141)).
6. Treat `/status` as an imperfect observability surface in current builds. If behavior and `/status` disagree about AGENTS loading, trust direct evidence from behavior or prompt-input inspection more than the header alone.[^issue-17776]
7. If this repo hits the same `0.120.0` remote-compaction failure pattern reported publicly, prefer a version check and fresh-thread fallback before assuming the problem is repo-local. Public issue `#17819` reported rollback to `0.119.0` as an immediate workaround, but that remains public-report evidence rather than official guidance.[^issue-17819]

## External Works Cited

[^codex-hooks]: OpenAI Developers, "Hooks – Codex," https://developers.openai.com/codex/hooks
[^codex-agents]: OpenAI Developers, "Custom instructions with AGENTS.md – Codex," https://developers.openai.com/codex/guides/agents-md
[^codex-slash]: OpenAI Developers, "Slash commands – Codex," https://developers.openai.com/codex/cli/slash-commands
[^api-compaction]: OpenAI API Docs, "Compaction," https://developers.openai.com/api/docs/guides/compaction
[^codex-config]: `openai/codex`, `codex-rs/core/config.schema.json` (`model_auto_compact_token_limit`, `project_doc_max_bytes`, `codex_hooks`, `experimental_compact_prompt_file`), https://github.com/openai/codex/blob/main/codex-rs/core/config.schema.json
[^codex-project-doc]: `openai/codex`, `codex-rs/core/src/project_doc.rs` (AGENTS discovery, concatenation, truncation, merge with user instructions), https://github.com/openai/codex/blob/main/codex-rs/core/src/project_doc.rs
[^codex-openai-models]: `openai/codex`, `codex-rs/protocol/src/openai_models.rs` (`auto_compact_token_limit`, `effective_context_window_percent`), https://github.com/openai/codex/blob/main/codex-rs/protocol/src/openai_models.rs
[^codex-protocol]: `openai/codex`, `codex-rs/protocol/src/protocol.rs` (`BASELINE_TOKENS` and `percent_of_context_window_remaining`), https://github.com/openai/codex/blob/main/codex-rs/protocol/src/protocol.rs
[^codex-codex]: `openai/codex`, `codex-rs/core/src/codex.rs` (effective context window application, token recomputation, pre-turn TODO, pre-turn and mid-turn auto-compaction paths), https://github.com/openai/codex/blob/main/codex-rs/core/src/codex.rs
[^codex-compact]: `openai/codex`, `codex-rs/core/src/compact.rs` (replacement history construction, retained recent user messages, summary retention, ghost snapshots, warning about long threads/multiple compactions), https://github.com/openai/codex/blob/main/codex-rs/core/src/compact.rs
[^codex-compact-remote]: `openai/codex`, `codex-rs/core/src/compact_remote.rs` (remote compaction replacement history processing, ghost snapshot preservation, stale developer-message filtering, initial-context reinjection, token recomputation), https://github.com/openai/codex/blob/main/codex-rs/core/src/compact_remote.rs
[^issue-17776]: `openai/codex` issue `#17776`, created 2026-04-14, "/status no longer reports AGENTS.md in 0.120.0," https://github.com/openai/codex/issues/17776
[^issue-17819]: `openai/codex` issue `#17819`, created 2026-04-14, "0.120.0 regression: resumed threads fail during remote compaction with \"Unknown parameter: 'prompt_cache_retention'\"," https://github.com/openai/codex/issues/17819
[^issue-17874]: `openai/codex` issue `#17874`, created 2026-04-15, "Bring back % for token use in statusline," https://github.com/openai/codex/issues/17874
[^issue-17912]: `openai/codex` issue `#17912`, created 2026-04-15, "Auto-compaction near high context usage can make Codex answer the previous message instead of the current one," https://github.com/openai/codex/issues/17912
[^issue-17940]: `openai/codex` issue `#17940`, created 2026-04-15, "/compact and auto compact always time out," https://github.com/openai/codex/issues/17940
