# Charter 02: Hosting, Distribution, Capacity, And Transition Pathways

Write output to:

`/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`

## Task Type

Initial architecture research/planning.

## Scope

Explore the operational transition space for a web-first Prix Guesser:

- completely local LAN play without public hosting
- self-hosted remote play from personal hardware
- small-scale public hosting
- later scaling under resource constraints

This is not just a hosting comparison. It is a transition-path study under limited money, limited compute, and a desire for transparent, staged growth.

## Starting Context

Read these first:

- `/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/phases/01-authored-round-contract/.continue-here.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`

## Research Instructions

Investigate whether a web-first product can plausibly support all of these stages:

1. local same-WiFi play from one machine
2. self-hosted remote play from personal hardware such as `dionysus`
3. lightweight hosted/public-facing operation later

Explore:

- LAN feasibility and common patterns
- QR join / join URL patterns
- self-hosting options such as direct self-host, Tailscale, Cloudflare Tunnel, VPS/container paths
- what changes when usage grows beyond one personal machine
- what capacity and concurrency limits usually depend on for products of this shape
- what more money buys beyond "more scale"
- transparent queueing, waitlisting, or capacity messaging patterns
- whether "downloadable local-host app", "browser-first website", or "portable local package" can sensibly coexist

Do not turn this into a vendor bakeoff too early.
Map the pathways and their tradeoffs first.

Helpful prompts:

- What are the main staged hosting paths available to an indie project of this kind?
- Where are the real breakpoints that force a transition?
- What kinds of failure modes would users actually experience first?
- What would a transparent capacity-constrained public beta look like?
- Can donation-supported or community-supported access models be done without feeling manipulative or paywalled in the wrong way?

## Output Emphasis

Include:

- `Feasible Staged Paths`
- `Operational Breakpoints`
- `What Resource Constraints Actually Mean In Practice`
- `Transition Patterns That Preserve Trust`
- `Questions Requiring Measurement Rather Than Armchair Guessing`

Do not fabricate concurrency numbers. If numbers are not knowable without benchmarking, say so plainly.

## Source Expectations

- Prefer official docs and primary technical sources for infrastructure claims.
- If discussing capacity, clearly separate benchmark data from inference.
- If discussing funding/access patterns, distinguish actual examples from speculative ideas.

## Collaboration Constraints

You own only the output file listed above.
You are not alone in the codebase.
Do not modify or revert anyone else's files.
