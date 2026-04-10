# Lane 3 Prompt — Stakeholder & Distribution

**Used for:**
- Opus 4.6 agent (first pass, 2026-04-08, non-blind)
- GPT 5.4 xhigh Codex agent (second pass, 2026-04-10, blind)

## GPT Blind-Audit Version (as sent)

```
You are performing an INDEPENDENT BLIND AUDIT of stakeholder fit and distribution for Prix Guesser. Another auditor has already reviewed this; you must NOT read their findings so that your review is uncontaminated.

## Hard Constraints

- DO NOT read any file named `lane-*.md` or `SYNTHESIS.md` in `.planning/audits/`
- DO NOT read `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/` (other lanes)
- Write your report to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/lane-3-stakeholder-distribution.md`
- The shared task spec at `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md` is the only audit file you may read

## Critical stakeholder context

- Creator: Logan Rooks, philosophy PhD student, NOT a professional developer
- Users: Non-technical F1 fan friends
- No commercialization: Private-only, for personal and friend play
- Primary mode (v1): Local party game — host laptop casts to TV, friends use phones as controllers on same network
- Future mode: Online hosted play on a private server called `dionysus` (home server accessible via Tailscale VPN at 100.93.212.44, Intel Xeon W-2125, 32GB RAM, GTX 1080 Ti, Ubuntu 24.04, running Docker/PostgreSQL/Redis)
- Key constraint: Non-technical friends need to be able to use this
- Hosting model question: "Hosted only when we want to play" — what does that look like?

## Your Task (Lane 3: Stakeholder & Distribution)

1. Can a non-technical friend realistically boot this on their laptop to host? What's needed?
2. What's the simplest path for friends to join from their phones? (QR code? Local network discovery?)
3. Cast to TV: What does this mean technically? (Chromecast? HDMI? Does app need to be cast-aware?)
4. How does architecture evolve from "everyone on same WiFi" to "hosted on dionysus via Tailscale or internet"?
5. Could Tailscale-only hosting work? UX implications for non-technical friends who'd need Tailscale?
6. What's needed for friends to connect without Tailscale? (Domain, HTTPS, port forwarding, Cloudflare tunnel)
7. "Hosted only when we want to play" deployment model? (Docker compose up/down? Script?)
8. Does monorepo + pnpm + TypeScript serve or hinder these goals?
9. Packaging options: Electron, Tauri, Docker, or just a hosted web app?

## Files to read

- `.planning/audits/2026-04-08-pre-execution-review/TASK-SPEC.md`
- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `/home/rookslog/CLAUDE.md` (machine context — dionysus server specs and services)

## Output format

Write your markdown report to `.planning/audits/2026-04-08-pre-execution-review/gpt-5.4-parallel/lane-3-stakeholder-distribution.md` with:
- Reality check on each distribution scenario
- Recommended distribution strategy (with phases)
- Architecture implications for the current roadmap
- What needs to change in requirements or roadmap
- Concrete deployment architecture for local play AND future online play
- Priority recommendations (critical / high / medium / low)

Write the report directly to the file. Do not print it as your final message.
```
