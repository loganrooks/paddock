---
audit: 2026-04-08-pre-execution-review
created: 2026-04-10T02:00:00Z
type: methodology-review
author: claude-opus-4-6
purpose: Document known biases, confounds, and reproducibility gaps in the audit methodology so findings are interpreted with appropriate epistemic humility.
---

# Methodology Review

## Why This Document Exists

This audit ran two passes — Opus 4.6 agents (first) and GPT 5.4 xhigh Codex agents (second) — intended as an independent A/B comparison. Several methodological issues affect how confidently we can treat the comparison as "two independent opinions":

1. Prompts were not persisted until after the first pass ran
2. The two passes used slightly different prompts, not identical ones
3. The second pass has knowledge of the first pass's existence (via "blind audit" framing)
4. Runtime environments differ (Opus via Claude Code Agent tool vs GPT via Codex CLI)

Documenting these upfront lets future readers — including future conversations — judge the findings with the right amount of trust.

## Known Confounds

### Confound 1: Prompt Drift Between Passes

**What happened:** The Opus prompts were constructed inline in Agent tool calls on 2026-04-08. The GPT prompts were constructed inline in Codex CLI calls on 2026-04-10. Neither was saved as a reproducible artifact until after the first pass was complete. The prompts saved in `prompts/` are the GPT versions only.

**The delta between Opus and GPT prompts:**
- GPT prompts add a `## Hard Constraints` section with explicit "DO NOT read lane-*.md or SYNTHESIS.md" rules
- GPT prompts open with "You are performing an INDEPENDENT BLIND AUDIT" — framing not in Opus prompts
- GPT prompts write to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/` subdirectory instead of the main folder
- GPT prompts include the sentence "Another auditor has already reviewed this; you must NOT read their findings so that your review is uncontaminated" — priming the model that a prior review exists
- The core audit questions, file lists, and output format sections are identical

**Why this matters:** The GPT pass is NOT a clean independent replication. It is a blind replication with explicit knowledge that a prior review exists. A model primed with "another auditor already reviewed this" may:
- Try to differentiate its findings to feel useful
- Anchor on expected differences between Opus and GPT
- Over-emphasize novel observations to justify its existence
- OR conversely, feel pressure to converge with the (invisible) prior review

**What a clean replication would require:**
- Identical prompts with no "another auditor" framing
- Both passes writing to sibling directories with no visibility
- Prompts saved BEFORE the first pass runs, then reused verbatim for the second pass
- Both passes using the same runtime (e.g., both via Codex, or both via Claude Code Agent tool) to eliminate runtime confounds

### Confound 2: Opus Prompts Not Persisted

**What happened:** The original Opus prompts were constructed inline in the `Agent` tool calls and exist only in the Claude Code session transcript. They are not saved as standalone artifacts.

**Impact:**
- Cannot verify after-the-fact exactly what the Opus agents were asked
- Cannot re-run the Opus pass with identical inputs
- Cannot do a true A/B comparison where the prompts are known-identical
- Future methodology reviews must rely on the `prompts/` directory's reconstruction note that "the Opus versions were essentially the body content minus the Hard Constraints sections and wrote to the main folder"

**Mitigation:** The Opus prompt content should be reconstructed from this session's transcript when the session is still available, and saved to `prompts/lane-N.opus-as-sent.md` files. This has not yet been done.

### Confound 3: Runtime Environment Differences

**Opus pass (2026-04-08):**
- Runtime: Claude Code `Agent` tool (Sonnet/Opus native)
- Model: Claude Opus 4.6
- Sandbox: Claude Code's native filesystem access (no bwrap, no Landlock)
- File tools: Read, Write, Edit, Grep, Glob, Bash
- Tool result injection: Automatic
- Context window: Full Claude Code parent window

**GPT pass (2026-04-10):**
- Runtime: Codex CLI `exec` command
- Model: GPT 5.4 with `model_reasoning_effort=xhigh`
- Sandbox: Codex `workspace-write` (Landlock after fix)
- File tools: shell-based (sed, cat, rg, tee, etc.) + Codex internal edit tools
- Tool result injection: Codex CLI protocol
- Context window: Fresh process per lane

**Why this matters:**
- Different models have different default behaviors (verbosity, confidence calibration, section structure)
- Different tool access patterns produce different evidence gathering (Opus may grep strategically, GPT may sed through whole files)
- Different sandbox models affect what the agent can actually do — e.g., GPT initially failed entirely due to the bwrap issue, required a fix (documented in `codex-sandbox-diagnostic.md`)
- A finding present in both passes is strong evidence of convergence. A finding present in only one pass could be model-specific, runtime-specific, or a real gap.

### Confound 4: Timing and Session Context

**What happened:** The Opus pass ran on 2026-04-08 in a session that had just explored the Codex session history and was still loaded with context about the troubled Phase 1 planning. The GPT pass ran on 2026-04-10 in a fresh Codex session with no prior context. The same Claude Code session drove both passes and orchestrated the synthesis.

**Impact:**
- The Opus agents may have inherited framing from the parent session (my synthesis of the handoff files, my interpretation of signals) through prompt construction
- The GPT agents received only what I explicitly wrote into their prompts — but I wrote those prompts after having already read the Opus findings
- **The orchestrator (me) is not blind to either pass.** My framing of the GPT prompts could reflect Opus findings implicitly even where I tried to avoid it
- My synthesis is not independent of either pass

**What a truly independent audit would require:** A third-party orchestrator, or a pre-committed prompt template that cannot be edited between passes.

## Scope of Valid Claims

Given the above confounds, here is what we can and cannot claim about the audit findings:

### Strong claims (well-supported)
- Findings that appear in BOTH the Opus and GPT passes represent robust concerns — two models with different architectures and different tool access converged on the same observation
- The Phase 1 plan quality finding (Lane 1) is strongest because the questions are most objective (cross-plan consistency, read_first validity, acceptance criteria concreteness)
- Specific factual findings (e.g., "01-03 previously had flat `mediaKind` but uncommitted diff fixes it to nested `clueSteps[*].media.kind`") are verifiable against the actual diff and do not depend on either model's judgment

### Moderate claims (supported but confounded)
- Findings about design quality (Lane 2), distribution (Lane 3), and multi-milestone vision (Lane 4) are more opinion-loaded and therefore more susceptible to model-specific biases
- Convergent findings across both passes in these lanes are still meaningful but should be treated as "two reasonable reviewers agreed" rather than "objective gaps"

### Weak claims (should not be overstated)
- Any finding that appears in only ONE pass could be:
  - A real insight that the other model missed
  - A model-specific bias
  - An artifact of the prompt delta
  - An artifact of the runtime environment
- Claiming "both Opus AND GPT identified this" implies more independence than actually exists, given the orchestrator is shared and the GPT pass was primed with "another auditor reviewed"

## Recommendations for Future Audits

1. **Persist prompts BEFORE running any audit pass.** Save to `prompts/` directory, then `cat` them into the CLI invocation.
2. **Use identical prompts across passes.** If blind-audit constraints are needed, include them in BOTH passes (write Opus output to `opus/` and GPT output to `gpt/` siblings so neither can see the other).
3. **Do not include "another auditor already reviewed" framing.** If blind replication is the goal, the second pass should not know about the first. Hide the other pass's reports by moving or renaming, not by instruction.
4. **Document runtime environment per pass.** What model, what reasoning effort, what sandbox, what tools available.
5. **Log timestamps.** When was each agent spawned, how long did it run, what was the token count.
6. **Consider using three passes with majority rule** for high-stakes findings. Two passes can confound each other; three independent passes with a tiebreaker surface real signal more reliably.
7. **Orchestrator blindness** — if possible, have a different person/session orchestrate each pass. When impossible (as here), document the orchestrator's non-blindness explicitly.

## What This Means for the Synthesis

The `SYNTHESIS.md` in this directory was written based on Opus pass findings only. Once the GPT pass completes, the synthesis should be updated with:

- Convergence analysis (findings in both passes)
- Divergence analysis (findings in only one pass, with honest uncertainty about why)
- This methodology review's caveats applied per-finding

The synthesis should NOT claim "two independent models confirmed X" without referring back to this document.

## Open Methodology Questions

1. Was the bwrap sandbox fix (switching Codex to Landlock) a confound in itself? Landlock has different filesystem access semantics than bwrap. Could this affect what files the GPT agents could read?
2. Did the GPT agents actually comply with the `DO NOT read lane-*.md` constraint, or did they read the Opus reports anyway? This should be verifiable by examining the Codex session transcript for file read events.
3. Is there a systematic bias in which model (Opus vs GPT) tends to over-report vs under-report issues? Without ground truth, we can't tell.
