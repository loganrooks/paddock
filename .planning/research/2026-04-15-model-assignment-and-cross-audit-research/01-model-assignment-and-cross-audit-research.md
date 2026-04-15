# Model Assignment And Cross-Audit Research

Date: 2026-04-15  
Status: completed research synthesis

## Research Frame
- Mode: `solution evaluation`
- Question: what model-assignment policy is best justified for this repo's agentic work as of 2026-04-15, and how much of that policy is official guidance versus repo-specific inference?
- Scope:
  - current repo model policy and workload shape
  - official OpenAI guidance on recent GPT/Codex models and reasoning effort
  - official Anthropic guidance on current Claude Sonnet/Opus models and thinking controls
  - a small recent external supplement where it materially helps
- Non-goals:
  - building a local eval harness in this artifact
  - ranking every peripheral or legacy model family
  - pretending public benchmark coverage is complete for every task family or effort tier
- Stop condition:
  - state what can be treated as a justified repo policy now
  - mark what remains conditional, anecdotal, or open
  - produce a task-family assignment matrix with caveats

## Path Of Inquiry
- Entry point:
  - the launch bundle asked for a repo-facing answer about orchestration, research, canon synthesis, planning, execution, debugging, validation, and cross-model audit, with official vendor guidance first ([00-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/00-launch-bundle-spec.md:6)).
- Branches considered:
  - whether the answer should stay almost entirely inside current repo defaults
  - whether public evidence actually supports claims that a Codex-specialized model can beat the main GPT line on execution
  - whether "reasoning level" can be treated as a reliable cross-audit axis
  - whether cross-vendor audit is materially more useful than same-family cross-tier or cross-effort review
- Branches pursued:
  - current repo policy and operational constraints
  - official OpenAI model pages, guides, and release notes
  - official Anthropic model and thinking docs
  - recent external benchmark and technical-comparison sources that materially sharpen task-family differences
- Branches deferred or abandoned:
  - non-OpenAI / non-Anthropic primary assignment policy
  - older GPT-4 / Claude 3 generation comparisons
  - local benchmark construction
  - detailed pricing analysis
- Reframings:
  - the core question is not "best model overall"
  - the core question is "best default and best escalation path by task family, given this repo's mix of planning, doctrine, coding, and audit work"

## Assumptions Surfaced
- `[d:c:i]` The repo already treats `gpt-5.4` as the default Codex family and explicitly prefers `xhigh` for top-level orchestration and `high` for execution / verification ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:113), [tooling/portable-gsd/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/README.md:28), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:33)).
  - Why it matters: the burden of proof is on changing that default, not merely finding an interesting alternative.
  - What could weaken it: strong external evidence or repo-local eval evidence that another model family wins more often on the repo's real task mix.
- `[a:r:i]` This repo's workload is not pure code completion; it mixes product/canon synthesis, planning doctrine, coding, debugging, and adversarial rereading ([00-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/00-launch-bundle-spec.md:18), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:60)).
  - Why it matters: benchmark wins on narrow coding tasks do not automatically imply a better repo-wide default.
  - What could weaken it: if work shifts toward mostly bounded code-edit/test loops.
- `[a:r:i]` Audit value depends partly on independence of failure modes, not just raw capability.
  - Why it matters: a second pass with the same family at a different effort may improve depth without giving much real disagreement.
  - What could weaken it: repo-local evidence that same-family cross-effort review catches nearly all meaningful misses at much lower cost.

## Criteria
The options were compared against these repo-relevant criteria:

1. mixed-task capability across coding, planning, canon synthesis, and review
2. performance on bounded implementation and debugging loops
3. controllable reasoning depth versus latency
4. usefulness as an auditor rather than only as a primary worker
5. fit with current Codex-native repo policy and delegation style

## Official Baseline By Vendor

### OpenAI
- `[e:c:d]` OpenAI's current guidance positions `gpt-5.4` as the general default frontier model for coding, agentic tasks, complex reasoning, and long-context work, with `gpt-5.4-pro` for the hardest problems and `gpt-5.4-mini` / `gpt-5.4-nano` for cheaper or higher-volume work.[^openai-models][^openai-latest-model][^openai-gpt54]
- `[e:c:d]` OpenAI also preserves a specialized coding lane: `gpt-5.3-codex` is described as specifically designed for coding environments and agentic coding, but the later `gpt-5.4` guidance says `gpt-5.4` replaces `gpt-5.3-codex` as the default model in Codex and incorporates its coding capabilities with stronger broad performance.[^openai-gpt53-codex][^openai-latest-model][^openai-gpt54]
- `[e:c:d]` Official OpenAI reasoning control for the current GPT-5 line is a same-model effort dial, not a different-model switch. The public guidance exposes `none`, `low`, `medium`, `high`, and `xhigh` effort choices and recommends starting lower, then raising effort only when task complexity justifies it.[^openai-latest-model]

### Anthropic
- `[e:c:d]` Anthropic's current model overview positions `Claude Opus 4.6` as its most intelligent broadly available model for agents and coding, with `Claude Sonnet 4.6` as the faster balance point for high capability with lower latency.[^anthropic-models]
- `[e:c:d]` Anthropic's current thinking controls are also same-model effort controls rather than separate model families. Official docs describe `extended thinking`, `adaptive thinking`, and effort levels such as `minimal`, `low`, `medium`, `high`, and `max`, with adaptive mode recommended for current Sonnet 4.6 and Opus 4.6 because the model decides when deep thinking is actually needed.[^anthropic-extended-thinking][^anthropic-adaptive-thinking]
- `[e:c:d]` Anthropic's official Claude 4 release framing still matters for task-family interpretation: Opus is framed as the stronger long-running or more complex agentic worker, while Sonnet is framed as the more practical, lower-latency default for many coding and agent workflows.[^anthropic-claude4]

## Reasoning Levels: Official Evidence Versus Inference

### What the official docs establish
- `[e:c:d]` OpenAI officially exposes effort levels as a single-model control surface and explicitly ties lower effort to lower latency and higher throughput, while reserving `high` / `xhigh` for deeper reasoning and stronger eval performance.[^openai-latest-model][^openai-gpt54]
- `[e:c:d]` Anthropic officially exposes thinking as a single-model control surface too. Its docs say lower effort may skip extended thinking, while `high` and especially `max` push the model toward more deliberate thought; adaptive mode is positioned as the preferred default on the newest Sonnet/Opus models.[^anthropic-extended-thinking][^anthropic-adaptive-thinking]
- `[e:c:d]` Neither vendor publicly decomposes these effort levels into a precise operational account of what internal mechanisms change beyond more or less deliberate reasoning budget. So the "what effort really does" question is only partially answerable from official sources.[^openai-latest-model][^anthropic-extended-thinking]

### What can be reasonably inferred for this repo
- `[a:c+r:i+d]` Higher effort appears to buy more search breadth, more self-checking, and more persistence on ambiguous multi-step tasks. That makes it a better fit for orchestration, exploratory research, canon synthesis, difficult debugging, and adversarial review than for crisp grep-edit-test loops.[^openai-latest-model][^anthropic-adaptive-thinking]
- `[a:c+r:i+d]` Lower effort appears to buy iteration speed more than it buys a fundamentally different problem-solving style. For bounded execution tasks, especially where acceptance criteria are concrete and tooling provides fast feedback, lower or medium effort can plausibly outperform higher effort on total wall-clock productivity even if not on single-shot "best answer" quality.[^openai-latest-model][^anthropic-extended-thinking]
- `[a:r:i+d]` Cross-effort review within one family is therefore useful mainly as a cheaper depth adjustment, not as a strongly independent audit lane.

### Evidence limits
- `[o:r:d]` There is no public cross-vendor matrix that cleanly answers "what is the best reasoning level for orchestration, execution, review, and debugging under the same harness" across recent GPT/Codex and Claude families.
- `[o:c:d]` There is also no strong public evidence that `xhigh` or `max` are universally best for coding execution. The official docs point more toward "use more thinking when the task is hard" than toward a simple always-higher-is-better rule.[^openai-latest-model][^anthropic-adaptive-thinking]

## External Supplement: What It Adds Beyond The Official Vendor Story
- `[e:c:d]` GitHub's current Copilot model-comparison page is one of the more useful non-vendor practical maps because it places recent OpenAI and Anthropic models side by side by workflow. It characterizes `GPT-5.3-Codex` as strong for agentic software development and general coding, `GPT-5.4` as the stronger deep-reasoning and debugging choice, `Claude Opus 4.1` as strongest on complex architecture / refactoring, and `Claude Sonnet 4.5` as a fast balanced coding option. The exact version numbers lag the newest Anthropic 4.6 pages, but the workload split is still informative.[^github-model-comparison]
- `[e:c:d]` Recent public Scale leaderboards show that benchmark leadership varies by scaffold and task type. On Scale's public SWE-Bench Pro page, `GPT-5.4-pro` leads and `Claude Opus 4.6` follows; on Scale's Codebase QnA leaderboard, `Claude Opus 4.6` edges out `GPT-5.2 High` while other GPT variants still rank strongly. That is a useful reminder that "best model" is benchmark- and harness-sensitive rather than universal.[^scale-swebench][^scale-codebase-qna]
- `[a:c+r:i+d]` These external signals materially strengthen a task-family policy, but they still do not justify a universal one-model-fits-all rule for this repo.

## Model Family Comparison

`[a:c+r:i+d]` The table below is a repo-facing synthesis, not a claim that public benchmarks settle every row.[^openai-latest-model][^anthropic-models][^github-model-comparison][^scale-swebench][^scale-codebase-qna]

| Model / mode | Best-supported role in this repo | Why it fits | Main caveat |
| --- | --- | --- | --- |
| `gpt-5.4 xhigh` | top-level orchestration, exploratory research, canon synthesis, phase planning | strongest official OpenAI default for mixed reasoning + coding + tool use; aligns with current repo policy | slower and likely over-invested for simple execution loops |
| `gpt-5.4 high` | default execution, debugging, verification, mixed implementation + review | keeps broad reasoning while avoiding some `xhigh` drag; aligns with current repo policy | may still be slower than a coding-specialized model on crisp edit/test loops |
| `gpt-5.4-mini high` | high-volume bounded subagents, cheap codebase mapping, repetitive verification | official positioning favors high-volume coding and agent workflows | weaker choice for doctrine-sensitive synthesis or adversarial review |
| `gpt-5.3-codex high` | optional specialist for bounded code-heavy execution experiments | official positioning and GitHub comparison both preserve a coding-specialist niche | public evidence does not support making it the repo-wide default over `gpt-5.4` |
| `claude-sonnet-4.6` adaptive `high` | fast cross-vendor execution / review / routine audit | good speed-capability balance; useful when a second vendor's perspective matters but cost and latency still matter | less likely than Opus to be the strongest choice on the hardest architecture or debugging tasks |
| `claude-opus-4.6` adaptive `high` or `max` | hardest debugging, architecture review, canon-sensitive cross-audit | strongest current Anthropic option for agents/coding; likely best external auditor lane | highest cost and latency; unnecessary for many routine checks |

## Task-Family Assignment Matrix

`[a:c+r:i+d]` This matrix is the strongest actionable policy supported by the current evidence base for this repo.[^openai-latest-model][^anthropic-models][^github-model-comparison][^scale-swebench][^scale-codebase-qna]

| Task family | Recommended default | Strong secondary / escalation path | Rationale | Evidence strength |
| --- | --- | --- | --- | --- |
| top-level orchestration | `gpt-5.4 xhigh` | `claude-opus-4.6` adaptive `high` for major architecture cross-check | mixed reasoning, long horizons, and tool orchestration dominate | strong official + strong repo fit |
| ambiguity-heavy exploratory research | `gpt-5.4 xhigh` | `claude-opus-4.6` adaptive `high` / `max` for adversarial reread | ambiguity handling and synthesis matter more than raw patch speed | strong official, moderate external |
| mature-product / canon synthesis | `gpt-5.4 xhigh` | cross-vendor audit with `claude-opus-4.6` | doctrine-sensitive writing benefits from depth and independent rereading | moderate, partly reasoned |
| phase planning | `gpt-5.4 xhigh` | `claude-sonnet-4.6` or `opus-4.6` audit depending stakes | planning is closer to orchestration than to execution | strong internal + moderate external |
| execution / implementation edits | `gpt-5.4 high` | pilot `gpt-5.3-codex high` on bounded code-only lanes; `claude-sonnet-4.6` when vendor diversity matters | mixed repo work still favors breadth; crisp code loops may justify a specialist | moderate and conditional |
| debugging | `gpt-5.4 high` | escalate to `gpt-5.4 xhigh` or `claude-opus-4.6` for stubborn failures | debugging crosses code, inference, and hypothesis testing | strong official, moderate external |
| validation / checking / review | `gpt-5.4 high` | `claude-sonnet-4.6` for routine cross-vendor review, `claude-opus-4.6` for high-stakes review | reviews benefit from a second perspective more than from raw patch speed | moderate and partly reasoned |
| adversarial / cross-model audit | primary work by current default, audit by a different vendor | `claude-opus-4.6` first; `claude-sonnet-4.6` if cheaper pass is enough | independence of failure modes matters more than tiny benchmark deltas | moderate and partly reasoned |

## Is "`gpt-5.3-codex` May Outperform `gpt-5.4` For Execution" Real?

### What is directly supported
- `[e:c:d]` A blanket claim that `gpt-5.3-codex` is broadly better than `gpt-5.4` is not supported by current official OpenAI material. OpenAI's later `gpt-5.4` positioning says it replaces `gpt-5.3-codex` in Codex and absorbs its coding strengths while posting stronger broad eval results, including coding-adjacent agent and tool-use evaluations.[^openai-gpt54][^openai-latest-model]
- `[e:c:d]` A narrower claim that a Codex-specialized model can still be attractive for certain execution workloads is supported. OpenAI still describes `gpt-5.3-codex` as specifically designed for coding environments, and GitHub's model comparison still maps the Codex-specialized line toward agentic software-development tasks while mapping `gpt-5.4` toward deeper reasoning and debugging.[^openai-gpt53-codex][^github-model-comparison]

### Best current reading
- `[a:c+r:i+d]` The strongest justified reading is: the claim is conditionally real at the workload-family level, but mostly unproven at the exact-version repo-policy level.
  - "Conditionally real" because a coding-specialized model may still win on bounded code-edit/test loops where planning and synthesis burden are low.
  - "Not proven as a repo-wide rule" because the public evidence now points to `gpt-5.4` as the stronger general default once the workflow spans execution plus debugging, review, writing, or orchestration.
  - "Still partly anecdotal" because there is no public repo-matched eval showing `gpt-5.3-codex` beats `gpt-5.4 high` on this repo's actual edit/debug/verify loops.

### Thin or anecdotal parts
- `[e:c:d]` There are anecdotal Codex issue-thread reports about noticeable latency or behavior differences between GPT and Codex-specialized models, but those reports do not establish a stable quality hierarchy; they are too confounded by harness settings, reasoning effort, task shape, and runtime conditions to carry repo policy by themselves.[^codex-issue-4350]

## Cross-Model Audit: Across Vendors, Across Tiers, Across Effort Levels

### Across vendors
- `[a:c+r:i+d]` This appears to be the highest-value audit axis for this repo.
  - Different vendor families are more likely to disagree for meaningful reasons than different effort settings of the same family.
  - This matters most for canon-sensitive planning, architecture, difficult debugging, and adversarial review.
  - Current best pair: primary `gpt-5.4`, external audit `claude-opus-4.6`, with `claude-sonnet-4.6` as a cheaper routine alternative.[^anthropic-models][^github-model-comparison]

### Across tiers within a vendor
- `[a:c+r:d]` This appears moderately useful.[^openai-latest-model][^anthropic-models]
  - Examples: `gpt-5.4-mini` escalating to `gpt-5.4`, or `claude-sonnet-4.6` escalating to `claude-opus-4.6`.
  - This is a good cost-control pattern and can catch under-reasoned misses.
  - It is still less independent than a cross-vendor audit because the family priors remain more correlated.

### Across reasoning levels within one model
- `[a:c+r:d]` This appears lowest-value as an audit axis, though still useful as a cheap depth check.[^openai-latest-model][^anthropic-extended-thinking]
  - It is better treated as "same worker, more or less thinking time" than as a genuine second reviewer.
  - Use it when vendor access is constrained or when a quick second pass is enough.
  - Do not treat it as the only audit mechanism for high-stakes planning or doctrine work.

### Likely failure modes
- `[a:r:i+d]` Same-family audit under different effort can produce fake comfort because the model often preserves the same framing error.
- `[a:r:i+d]` Cross-vendor audit can still mislead if the harness, system prompt, or tool permissions differ enough that the comparison is no longer about the models.
- `[a:r:i+d]` Benchmark transfer is fragile. A model that wins on one agent scaffold or benchmark slice may lose on another, so audit pairings should follow task family and harness similarity, not leaderboard worship.

## Dependencies And Relations

| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Keep `gpt-5.4` as repo default | official OpenAI positioning, current repo policy, mixed-task workload | orchestration, planning, execution, verification defaults | medium |
| Treat `gpt-5.3-codex` as optional specialist, not default replacement | coding-specialist niche remains real, but broad default evidence favors `gpt-5.4` | execution experiments and subagent tuning | high |
| Use Anthropic mainly as cross-vendor audit and hard-problem escalation lane | access to Claude models, audit independence value | review workflow, architecture checks, stubborn debugging | medium |
| Do not use effort-only changes as sole audit on high-stakes work | same-model effort is correlated, not strongly independent | review quality and false confidence risk | low |

## Scope Expansions And Deferrals
- Defer: repo-local benchmark harness. This artifact can justify a policy default, but it cannot close exact local crossover points without controlled local runs.
- Defer: fine-grained pricing policy. The current question is assignment quality, not spend optimization.
- Revisit later: if the repo begins using Anthropic routinely inside Codex-native workflows, create a local eval lane for `gpt-5.4 high`, `gpt-5.4 xhigh`, `gpt-5.3-codex high`, `claude-sonnet-4.6 high`, and `claude-opus-4.6 high/max` under the same task corpus.

## What Can Close Now
- `[d:c:i]` Keeping `gpt-5.4` as the repo's primary default is still justified and does not currently require reversal ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:113), [tooling/portable-gsd/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/README.md:32)).
- `[a:c+r:i+d]` The repo should continue to map `xhigh` to top-level orchestration / research / planning and `high` to execution / verification unless a task is clearly bounded enough to justify less effort.[^openai-latest-model][^anthropic-adaptive-thinking]
- `[a:c+r:i+d]` The strongest cross-audit recommendation is cross-vendor, not merely cross-effort.[^openai-latest-model][^anthropic-models][^github-model-comparison]
- `[a:c+r:i+d]` If `gpt-5.3-codex` is introduced at all, it should enter as a bounded execution specialist behind a task-shape rule, not as a blanket replacement for `gpt-5.4 high`.[^openai-gpt53-codex][^openai-latest-model][^github-model-comparison]
- `[a:c+r:i+d]` `claude-opus-4.6` is the best current candidate for high-stakes cross-vendor audit; `claude-sonnet-4.6` is the better routine audit compromise.[^anthropic-models][^github-model-comparison]

## What Must Stay Open
- `[o:r:i+d]` The exact local crossover point where `gpt-5.3-codex` beats `gpt-5.4 high` on this repo's bounded execution tasks remains open.
- `[o:r:i+d]` The exact best Anthropic effort defaults for routine audit versus high-stakes audit remain open.
- `[o:r:i+d]` Whether same-vendor cross-tier review is "good enough" for this repo when Anthropic access is absent remains open.
- `[o:r:i+d]` Whether `gpt-5.4-mini` is good enough for any recurring subagent lanes in this repo remains open.

## Planning Handoff
- What can now be treated as decided:
  - keep `gpt-5.4` as repo default
  - keep `xhigh` for orchestration / research / planning
  - keep `high` for execution / verification
  - prefer cross-vendor audit over same-model effort-only audit when the work is doctrine-sensitive or architecture-setting
- What remains assumed or open:
  - whether a coding-specialist OpenAI lane should be added at all
  - whether `claude-sonnet-4.6` is enough for most routine review, reserving Opus for escalations
  - whether `gpt-5.4-mini` can safely absorb cheap repetitive subagent work
- Derived constraints:
  - do not justify model policy from anecdotal issue threads alone
  - do not let narrow execution benchmarks silently pick the repo-wide default
  - do not treat reasoning-effort variation as a full substitute for an independent audit lane
- Future-awareness seams to preserve:
  - a later local eval harness can reopen bounded execution defaults without reopening the orchestration default
  - the audit policy should remain task-family-aware rather than collapsing to one universal "best model"

## Sources

### Local paths
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
- [tooling/portable-gsd/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/README.md)
- [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
- [00-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-model-assignment-and-cross-audit-research/00-launch-bundle-spec.md)

## External Works Cited
[^openai-models]: OpenAI Developers, "Models", https://developers.openai.com/api/docs/models
[^openai-latest-model]: OpenAI Platform Docs, "Latest model", https://platform.openai.com/docs/guides/latest-model
[^openai-gpt54]: OpenAI, "Introducing GPT-5.4", https://openai.com/index/introducing-gpt-5-4/
[^openai-gpt53-codex]: OpenAI, "Introducing GPT-5.3-Codex", https://openai.com/index/introducing-gpt-5-3-codex/
[^anthropic-models]: Anthropic Docs, "All models", https://docs.anthropic.com/en/docs/about-claude/models/all-models
[^anthropic-extended-thinking]: Anthropic Docs, "Extended thinking", https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
[^anthropic-adaptive-thinking]: Anthropic Docs, "Adaptive thinking", https://platform.claude.com/docs/en/docs/build-with-claude/thinking#adaptive-thinking
[^anthropic-claude4]: Anthropic, "Introducing Claude 4", https://www.anthropic.com/news/claude-4
[^github-model-comparison]: GitHub Docs, "AI model comparison", https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/ai-models/model-comparison
[^scale-swebench]: Scale, "SWE-Bench Pro Public Leaderboard", https://labs.scale.com/leaderboard/swe_bench_pro_public
[^scale-codebase-qna]: Scale, "Codebase QnA SEAL Leaderboards", https://scale.com/leaderboard/sweatlas-qna
[^codex-issue-4350]: openai/codex GitHub issue #4350, "gpt-5 is much slower than gpt-5-codex in terminal and coding tasks", https://github.com/openai/codex/issues/4350
