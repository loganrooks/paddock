---
audit: 2026-04-08-pre-execution-review
created: 2026-04-09T04:15:00Z
updated: 2026-04-10T02:20:00Z
status: complete
lanes_completed: [1, 2, 3, 4]
passes_completed: [opus-4.6, gpt-5.4-xhigh]
synthesizer: claude-opus-4-6
related_documents:
  - CONVERGENCE.md — detailed dual-pass comparison honoring unique findings from each model
  - METHODOLOGY-REVIEW.md — known confounds and limits of the two-model comparison
  - prompts/ — reproducible prompts used for each lane
---

# Pre-Execution Review — Synthesis

## Context

Phase 1 plans exist but were produced through a troubled Codex session with recursive orchestration failures, manual substitute planning, and checker loops. Before executing, we ran 4 parallel audit lanes to verify readiness and surface gaps across plan quality, frontend design, distribution strategy, and multi-milestone vision.

**This synthesis was updated after a second independent pass.** The original synthesis was based on 4 Opus 4.6 agents. A follow-up pass of 4 GPT 5.4 xhigh agents (via Codex CLI) ran against the same task spec with blind-audit constraints after an unrelated sandbox issue was diagnosed and fixed. The convergence analysis between passes is in `CONVERGENCE.md`. The methodological caveats are in `METHODOLOGY-REVIEW.md`.

**Key update from the second pass:** GPT 5.4 surfaced structural architectural findings that Opus missed — most importantly, hierarchical answer targets in Phase 1, venue identity ambiguity in Phase 1, and DEPLOY-01..05 as concrete new requirements for distribution. These are incorporated below.

## Overall Verdict

**Phase 1 plans: READY WITH CAVEATS** — commit the uncommitted diffs, proceed to execution.

**Project artifacts (PROJECT.md, REQUIREMENTS.md, ROADMAP.md): NEED REVISION** — three critical gaps identified before execution burns effort in the wrong direction.

## Lane 1: Phase 1 Plan Quality — READY WITH CAVEATS

**Both passes agreed:** no blockers. All four Phase 1 plans correctly implement PACK-02, PACK-03, PACK-04, and OPS-01 across a clean production chain. Cross-plan contract consistency is solid — the vocabulary frozen in 01-01 is consumed consistently through 01-02, 01-03, and 01-04.

**Both passes agreed the uncommitted diffs are improvements** and should be committed:
- 01-02: rewritten truths to match requirement language (author-facing voice)
- 01-03: aligned media key naming from flat `mediaKind` to nested `clueSteps[*].media.kind`
- 01-04: added missing `tests/contract/content-graph-loading.test.ts` deliverable, removed redundant `UNSAFE_ASSET_PATH` diagnostic code

### Opus-unique warnings (surface drift)
- **W1:** Plan 01-03 has no schema validation in its verify blocks (YAML errors won't be caught until 01-04)
- **W2:** Plan 01-04's `read_first` omits domain source files that appear in `@context`
- **W3:** RESEARCH.md uses `map_snippet` while all plans use `map_fragment`
- **W4:** Plan 01-03's `read_first` omits `contracts.ts` despite it being in `@context`

### GPT-unique warnings (structural contract gaps)
- **G1: Venue identity ambiguity.** Venue files require both `id` and `venueId`; rounds use `venueRef`; the compiler never states whether `venueRef` resolves against filename, `id`, or `venueId`. If this lands in execution unresolved, the executor will invent a convention or stall.
- **G2: `PackSourceSchema` / `roundOrder` reference shape not frozen early enough.** Plan 01-01 freezes many inner shapes but not the pack reference contract that Plan 01-03 later treats as canonical. This is a structural "vocabulary locked too late" gap.
- **G3: Plan 01-03 verification is non-concrete.** The automated check greps for field names but cannot prove the nested YAML shapes match the implemented schemas. Stronger criteria at lines 109-110 are not provable by the listed `rg` commands at lines 99-100.
- **G4: Plan 01-04 lacks stable diagnostic codes for broken venue references and path-policy failures**, even though PACK-04 requires rejecting these before play. Task 1 implements both; Task 2 only standardizes diagnostics for a subset.

### Combined action
Commit the diffs (both agree). Then resolve G1-G4 first (structural gaps), followed by W1-W4 (surface drift) as lower-priority cleanup. The GPT-unique warnings are more substantive than the Opus-unique warnings but none are blockers.

**Character note:** Opus reads for surface specifics; GPT reads for implicit contracts becoming load-bearing. Both passes are valuable and complementary. See `CONVERGENCE.md` Lane 1 section for the detailed comparison.

## Lane 2: Frontend Design — CRITICAL GAP

**This was the strongest convergence across all 4 lanes.** Both passes independently concluded that design readiness is LOW, Phase 4-5 rewrite risk is HIGH, and that a UI-SPEC / design contract must land before Phase 4 begins.

### Convergent findings (both passes)
1. No visual identity or direction — no colors, typography, mood, or reference points
2. No animation or transition design for reveals, countdowns, and score updates
3. Host-screen (TV) and controller (phone) are fundamentally different design problems that need separate treatment under one shared brand system
4. "Watchability" is load-bearing in the project artifacts but has no visual definition
5. Recommended stack: React + Vite + Tailwind + Motion (Framer Motion) + Radix/shadcn primitives (but NOT shadcn/ui as a visual system)
6. Dark-first, TV-optimized for host screen
7. F1 broadcast aesthetic: timing-screen influence, condensed motorsport typography, sector/marshal-flag color semantics, reveal sequences like race control transitions

### Opus-unique contributions
- Named **Framer Motion** specifically
- Coined the "unofficial F1 broadcast production" framing
- "Bright white on a 55" TV at game night is hostile" — specific ergonomic framing

### GPT-unique contributions
- **Concrete inserted-phase proposal: "Phase 3.5: UI Direction, Design System, And Interaction Contract"** with deliverable list:
  - UI-SPEC.md covering visual direction, tone words, typography, color system, spacing scale, elevation, iconography
  - Host-screen and controller design principles as separate subsections
  - Key-screen mocks for join flow, controller answer flow, host clue state, answer lock, reveal, standings, replay
  - Motion grammar for timer pressure, answer lock, reveal payoff, scoreboard changes
  - Responsive rules for `phone portrait`, `laptop host`, `16:9 TV/cast`
  - Component inventory for domain components
- **Domain-specific component inventory:** timer rail, answer-surface chip, clue card, room-code hero, reveal panel, standings board, replay CTA
- **Explicit framework rejections with reasoning:** Next.js (wrong problem — not SEO/SSR), Astro (wrong center of gravity — content-heavy)
- **"Generic red racing app" cliché warning** — reference should be motorsport broadcast restraint, not arcade cliché
- **"Cosmetics out of scope" misreading risk** — flagged that this phrase could be misinterpreted as "deprioritize visual polish"
- **Harder recommendation:** "I would block Phase 4 implementation from starting until there is at least a lightweight UI-SPEC.md"

### Combined action
Both models recommend the same thing — a UI-SPEC artifact before Phase 4 — but disagree on how to formalize it:
- **Opus framing:** lightweight 1-2 day planning artifact, not a separate phase
- **GPT framing:** inserted Phase 3.5 with structured deliverables

These are the same recommendation at different levels of formality. **User decision required on which framing to adopt.** (See strategic questions section below.)

## Lane 3: Stakeholder & Distribution — CRITICAL GAP

**The roadmap describes building the game but never specifies how it gets packaged or run.** Both passes strongly agreed on the diagnosis and on the general distribution strategy.

### Convergent findings (both passes)
1. No deployment mechanism exists or is planned — Docker Compose should be a Phase 3 deliverable
2. QR code join must be first-class, not polish; belongs in Phase 4
3. Friends cannot realistically self-host from source; hosted web app is the primary product surface
4. Tailscale for operator access ONLY, not for guests
5. Cloudflare Tunnel for future remote play
6. HDMI/mirroring first, Chromecast later if ever
7. Host screen needs concrete 16:9 TV-distance readability constraint for UX-01
8. Monorepo + pnpm + TS is invisible to end users — not a distribution problem if kept behind build artifacts
9. Hosted web app > Docker (operator only) > Electron (if packaging becomes necessary) > Tauri (no)

### Opus-unique contributions
- **Named Supabase specifically** as wrong-fit for private-only offline-capable play
- **The single most valuable framing of the entire audit:** "Stop thinking of this as a developer project that happens to be private. Think of it as a hosted game that happens to be built by a developer. The build toolchain is for Logan. The deployment target is for everyone."

### GPT-unique contributions
- **DEPLOY-01 through DEPLOY-05** — five concrete proposed requirements that formalize the gap:
  - **DEPLOY-01:** Host can start a playable local-LAN session from one guided flow without requiring guests to install anything beyond a browser
  - **DEPLOY-02:** System can generate and display a valid join URL and QR code for the current deployment mode (local or hosted)
  - **DEPLOY-03:** Host display is usable on a 16:9 TV at couch distance and supports fullscreen presentation without cast-specific integrations
  - **DEPLOY-04:** Hosted mode supports HTTPS and websocket-capable ingress for remote guest play without requiring Tailscale on guest devices
  - **DEPLOY-05:** Operator can start and stop the hosted deployment on demand with a single documented command or script
- **Colyseus vs PartyKit is NOT neutral from a distribution standpoint.** The open room runtime decision has distribution implications the roadmap currently treats as neutral. GPT's bias: Colyseus fits better for self-hostable laptop+Docker+dionysus parity. PartyKit is viable only if prototype speed explicitly outweighs local/self-host parity.
- **Secure-context-only browser API warning:** Local LAN mode will likely be plain HTTP on private addresses; core loop features must not depend on HTTPS-only browser APIs (service workers, PWA install behaviors)
- **Hotspot fallback as a valid play pattern** if home WiFi is awkward
- **Firewall prompts as part of real UX** for first-run local hosting
- **Concrete operator flow:** `scripts/party-up.sh` → prints live URL → game night → `scripts/party-down.sh`
- **Explicit reality-check table** mapping each scenario (source checkout host, packaged local host, same-WiFi join, mDNS discovery, HDMI cast, Tailscale remote, Cloudflare Tunnel remote) to reality and implication

### Combined action
Adopt DEPLOY-01..05 verbatim (GPT). Apply the "hosted game built by a developer" framing to PROJECT.md (Opus). Treat the Colyseus vs PartyKit decision as a distribution decision, not a neutral runtime choice (GPT). Replace Supabase with local PostgreSQL if Supabase is currently planned (Opus).

## Lane 4: Multi-Milestone Vision — ARCHITECTURALLY SOUND, MULTIPLE LEVELS OF FIX AVAILABLE

**Both passes agreed:** v1 architecture is directionally sound, but several v2-critical seams are implicit rather than explicit. The difference between the two passes is how ambitious the fixes should be.

### Convergent findings (both passes)
1. v1 architecture is well-conceived — the three-layer separation (content / rules / room) avoids the most dangerous foreclosures
2. Stable IDs and content versioning are required from day one
3. Session data needs event-level capture, not flat summary aggregates
4. Player identity should be lightweight but stable in v1 (not full accounts, but not anonymous either)
5. Room engine must be transport-agnostic
6. SQLite → Postgres migration path is the right database strategy
7. 3-milestone arc shape: **anchor → wrappers → platform**
8. Content authoring pain is the #1 fun risk — if authoring is too expensive, the corpus never reaches critical mass

### Opus contributions (cheap concrete deliverables)
- **Content hash on compiled packs** — 1 hour, Phase 1
- **Branded `PlayerId` type alias** — 30 min, Phase 1
- **`pacingAuthority` field in room config** — 30 min, Phase 3
- **Round-level tags in content schema** — 30 min, Phase 1
- **Append-only event log** for session capture — later phase decision
- Opus framed these as "cheap sub-day investments that compound" with total estimated effort ~3 hours

### GPT contributions (structural architectural recommendations)
- **Hierarchical / composable answer targets** — THE most important architectural observation from either pass. Rather than a flat enum + aliases, the schema should model structured relationships: `venue contains circuit contains section contains corner`. v1 can still ship only `circuit` and `venue`, but the schema must not bake in a flat assumption. Phase 1 work.
- **Schema-driven judging engine** — Phase 2 engine should judge structured submissions against structured targets with specificity rules now, even if v1 content uses only two surfaces. Partial credit from target relationships, not ad hoc mode logic.
- **Deployment-agnostic room core with typed commands and events** — the same room core must run in local-hosted, private-server, and hybrid deployments. Typed `joinRoom`, `submitAnswer`, `advancePhase`, `startSession`, `resumePlayer` commands.
- **Explicit v2 reframing:** "wrapper expansion + content-ops maturity + lightweight persistence + richer answer surfaces + deployment durability" — not player-facing features
- **Criticism of RET-02** (account-backed history) as too heavy for a private-only project — soften to lightweight identity/history
- **Session replay/review as a distinct v2 phase** — not folded into calibration
- **Content tooling and calibration as its own phase** before adjacent mode sprawl
- **"Per-round outcomes" interpreted too narrowly** — needs clue-step performance, answer miss patterns, fallback-media underperformance diagnosis, cross-format evaluation

### Opus vs GPT framing difference
Opus thinks about "cheap fixes that compound" — small, concrete, immediate. GPT thinks about "implicit contracts becoming load-bearing" — structural, architectural, foundational. Both are correct. The Opus fixes are cheaper to execute; the GPT fixes are more architecturally ambitious and higher-leverage long-term.

**The hierarchical answer target recommendation (GPT) is strictly superior to the round-level tags recommendation (Opus).** If forced to choose between the two, pick GPT's. But they are not mutually exclusive — both can land in Phase 1.

### Three-milestone arc (both passes converged)
- **v1 "Game Night Works"** — current 7-phase roadmap (local party game, anchor mode)
- **v2 "Play Anytime, Anywhere"** — online hosted play, async challenges, player identity, content authoring tools, pack sharing, session replay, content calibration dashboards
- **v3 "F1 Party Platform"** — team play, adjacent non-anchor mode families, themed seasons/era packs, pack sharing, spectator mode

### Missing from v2 requirements (combined from both)
- Content operations (authoring UI, pack sharing, preview/validation tooling)
- Content versioning with stable IDs that survive edits
- Pack metadata and taxonomy (era, theme, difficulty, media posture, mode suitability)
- Player identity and history (session archives, accuracy trends) — lightweight, not account-backed
- Session replay or round review
- Distribution (private server hosting, on-demand deployment)
- Content scaling and calibration diagnostics (clue-step performance, miss patterns)
- Hybrid session support (couch + remote simultaneously)
- Seasonal or recurring content programming

### Biggest risks to project success (convergent, both passes)
1. **Content authoring is too painful** → corpus never reaches critical mass (both ranked this #1)
2. **The game is not actually fun** despite clean architecture
3. **Scope creep** — planning becoming the project before first real play
4. **Reveal quality is underinvested** because it feels like "content work" rather than "engine work"
5. **Non-technical friends cannot actually run the game**
6. **(GPT-unique)** Implementation hardcodes the first mode's assumptions everywhere, turning milestone 2 into a rewrite instead of an extension
7. **(GPT-unique)** v2 requirements drift toward public-product thinking (retention framing, account systems) that distorts the private-friends use case

## Cross-Lane Patterns

Three patterns emerged across multiple lanes:

1. **"Watchability" is load-bearing but undefined** (Lanes 2, 3, 4) — the word appears throughout project artifacts but has no operational meaning in design, distribution, or architecture. It should either be defined concretely (Lane 2's visual contract, Lane 3's TV-distance constraints) or removed as a term.

2. **The non-technical friend is the real stakeholder, not the developer** (Lanes 2, 3) — design, distribution, and UX decisions should all start from "what does the friend experience" rather than "what does the dev build". This framing shift affects roadmap priorities.

3. **Cheap v1 investments compound across milestones** (Lanes 1, 4) — the content hash, player identity, event log, and design contract are all sub-day investments that save weeks of rework in v2+. They should be incorporated into Phase 1 and Phase 3 now.

## Recommended Actions Before Phase 1 Execution

Ordered by leverage, with model attribution in parentheses.

### Immediate — blocks Phase 1 execution
1. **Commit the uncommitted plan diffs** (both) — all three are verified improvements
2. **Resolve venue identity ambiguity in Phase 1** (GPT G1) — pick one of `id` / `venueId` / `venueRef` as canonical and remove the others
3. **Freeze `PackSourceSchema` / `roundOrder` reference shape** in 01-01 or 01-02 (GPT G2) — do not leave canonical vocabulary to executor judgment
4. **Decide on hierarchical vs flat answer target model in Phase 1** (GPT) — this is THE most important architectural decision in the audit. If hierarchical, the schema should model `venue → circuit → section → corner` relationships even though v1 only ships with `circuit` and `venue`
5. **Add cheap v1 investments to Phase 1** (Opus):
   - Content hash in compiled pack output → append to 01-04
   - Branded `PlayerId` type → append to 01-01 or 01-02
   - Round-level tags in content schema → append to 01-02
6. **Tighten 01-03 verification** with a schema-backed loader invocation (GPT G3)
7. **Add stable diagnostic codes for broken `venueRef` and path-policy failures** to 01-04 (GPT G4)
8. **Fix `map_snippet` → `map_fragment` in RESEARCH.md** (Opus W3)
9. **Add missing `read_first` entries** in 01-03 and 01-04 (Opus W2, W4)

### Before Phase 2 execution
10. **Define the judging engine as schema-driven, not mode-specific** (GPT) — structured submissions against structured targets with specificity rules

### Before Phase 3 execution
11. **Treat Colyseus vs PartyKit as a distribution decision, not neutral** (GPT) — prefer Colyseus for self-host parity unless prototype speed explicitly outweighs
12. **Define room core with typed commands and events** (GPT) — transport-agnostic from day one
13. **Add Docker Compose deployment as Phase 3 deliverable** (both)
14. **Add `pacingAuthority` field to room config** (Opus)
15. **Replace Supabase with local PostgreSQL in Docker** if Supabase is currently planned (Opus)
16. **Warn explicitly about secure-context-only browser APIs** in LAN mode (GPT)

### Before Phase 4 execution
17. **Write UI-SPEC.md design contract** (both) — either as inserted Phase 3.5 (GPT) or as a lightweight planning artifact (Opus). **See strategic question 1 below.**
18. **Add DEPLOY-01..05 as new requirements** (GPT) and update roadmap traceability
19. **Add QR code join flow as Phase 4 first-class deliverable** (both)
20. **Add visual quality criteria to Phase 4 and Phase 5 success criteria** (both)
21. **Specify host-screen for TV-distance viewing** in UX-01 (both)
22. **Document the `scripts/party-up.sh` / `scripts/party-down.sh` operator pattern** (GPT)

### Roadmap-level additions
23. **Update PROJECT.md** to frame as "hosted game that happens to be built by a developer" (Opus)
24. **Expand v2 REQUIREMENTS.md** with content operations, player identity, session replay, distribution durability, content scaling (both)
25. **Soften RET-02** from account-backed persistence to lightweight identity/history (GPT)
26. **Make cosmetic visual polish explicitly in scope for v1** (GPT) — counter the "cosmetics out of scope" misreading risk
27. **Phase 6 scope expansion** from coarse per-round outcomes to event-level calibration data (GPT)

### Things that are fine as-is (both passes validated)
- Core three-layer architecture (content / rules / room)
- Phase 1 plan structure and sequencing (no rework needed)
- React + Vite + TypeScript baseline stack
- Requirements coverage of v1 (all 22 mapped to phases)
- The 3-milestone arc shape (anchor → wrappers → platform)

## Strategic Questions For Human Deliberation

These questions are LARGER than what the audits can answer. Neither pass engaged deeply with them because they are product strategy questions, not planning quality questions. They need direct human judgment.

### Q1: Should there be a dedicated design phase, and where?

**Both passes say YES, some kind of design contract is needed before Phase 4.** They disagree on formality.

Options:
- **Option A (Opus framing):** Lightweight 1-2 day planning artifact producing `UI-SPEC.md`. No new phase. Woven into existing milestone. Lower ceremony, faster to execute.
- **Option B (GPT framing):** Inserted Phase 3.5 "UI Direction, Design System, And Interaction Contract" with structured deliverables (UI-SPEC.md + key-screen mocks + motion grammar + component inventory + responsive rules). Higher ceremony, more accountability.
- **Option C:** Weave design criteria into Phase 4 as the first task, no dedicated phase. Lowest ceremony, highest risk of design debt accumulating during implementation.

Recommendation: **Option B** (GPT's Phase 3.5) because:
- v1's watchability is core value, not polish
- Design debt in Phase 4 is expensive to fix in Phase 5
- The component inventory (timer rail, answer-surface chip, clue card, etc.) is substantial enough that calling it a "planning artifact" underestimates it
- GSD's phase model already supports inserted phases via decimal numbering
- Phase 3.5 forces a named commit point; a "1-2 day artifact" can slip

But Option A is viable if the user wants to minimize structural overhead.

### Q2: Is Prix Guesser "one strong F1 GeoGuessr" or "Jackbox.tv for F1"?

This question was NOT directly addressed by either audit pass but it is the most important strategic question in the project.

**Two possible identities:**

**Identity A: "F1 GeoGuessr, deep"**
- One anchor mode, enriched iteratively over time
- Content model optimizes for geography/recognition depth
- v2 adds richer answer surfaces (section, corner, era), better calibration, more packs
- v3 adds team play, async challenges, themed seasons — but still within the geography/recognition fantasy
- Architecture optimizes for one very strong mode
- Name "Prix Guesser" fits this identity

**Identity B: "F1 Jackbox — party platform with GeoGuessr as first mode"**
- The authored round model is a substrate for multiple party game types
- v1 ships the geography anchor as the first instance of a broader pattern
- v2 adds non-geography party modes sharing the same session/room/content substrate (trivia, draft/pick modes, live-telemetry guessing, driver prediction games)
- v3 becomes a broader "F1 party night" platform
- Architecture optimizes for mode extensibility from day one
- Name "Prix Guesser" understates the ambition

**What the current artifacts say:**
- PROJECT.md says "F1-flavored party game where geography is the anchor rather than the whole product" (identity B)
- REQUIREMENTS.md v2 includes `MODE-01: adjacent non-anchor F1 mode` (identity B)
- But the v1 requirements and Phase 1-7 sequencing all optimize for identity A — one deep mode
- The roadmap explicitly says "does not widen v1 into adjacent party modes before the anchor room loop is proven" (identity A posture for v1)

**The gap:** The project is documented as identity B but planned as identity A. If v1 architecture assumes identity A, v2 mode expansion becomes a rewrite. If v1 architecture assumes identity B, v1 is more complex than it needs to be for the anchor mode alone.

**GPT's Lane 4 actually hints at the answer without stating it directly:** the hierarchical answer model, schema-driven judging engine, typed room commands, and session shell architecture all make identity B viable from v1 at minimal extra cost. **These are the architectural preconditions for "F1 Jackbox" — they cost almost nothing to add now and are very expensive to retrofit later.**

**Strong recommendation:** Adopt identity B explicitly. The v1 milestone still ships only the anchor mode, but the architecture is explicitly built for mode extensibility. Name the project accordingly (or at least acknowledge in PROJECT.md that "Prix Guesser" is the v1 product name, not the platform name).

This recommendation is a direct consequence of taking GPT's Lane 4 findings seriously.

### Q3: Multi-milestone trajectory and phase importance

**The audit revealed that no phase currently marks its relative importance to the larger arc.** Each phase has a goal and success criteria, but none says "this phase creates the substrate for v2 team play" or "this phase is pure v1 scaffolding that will be replaced in v2."

This is a meta-gap in the roadmap structure itself.

**Proposal:** Add a `cross_milestone_leverage` field to each phase in ROADMAP.md, rating whether each phase is:
- **Substrate** — creates long-lived abstractions that will be reused across milestones (e.g., authored round model, judging engine, room core)
- **Anchor-mode** — specific to the geography/GeoGuessr mode, will be joined by sibling modes later (e.g., Phase 2 round rules for circuit/venue answers)
- **v1 scaffolding** — needed for v1 shipping but likely replaced or superseded in v2 (e.g., file-based pack loading will become authoring UI in v2)

This framing makes the phase-to-milestone relationship explicit and lets future phase planning make informed tradeoffs.

### Q4: How should "hosted only when we want to play" actually work?

Lane 3 proposed the concrete pattern (`scripts/party-up.sh` + Cloudflare Tunnel + Docker Compose on dionysus). This is a good answer. The remaining decision:

- Build the **Tailscale-only** path first (simpler, core friends only) and add Cloudflare Tunnel in v2?
- Or jump straight to **Cloudflare Tunnel** from v2 onward (slightly more setup but zero-friction for all friends)?

Recommendation: **Tailscale first, Cloudflare Tunnel in v2.** Tailscale on dionysus is already running. The core friends who help calibrate v1 can be asked to install Tailscale. Cloudflare Tunnel is more work that should wait until v1 proves the loop is fun.

### Q5: Are the v2 requirements complete?

Both audit passes identified significant v2 gaps. The user should review the expanded v2 set (content operations, player identity, session replay, distribution durability, content scaling) before committing to a specific v2 milestone scope.

This does NOT block Phase 1 execution but should be resolved before any v2 planning begins.

### Q6: Should Supabase be removed?

Lane 3 (Opus) flagged Supabase as wrong-fit for private-only local-first play. If Supabase is a current planning assumption, replace with local PostgreSQL in Docker or SQLite. If Supabase is already a hard commitment (e.g., existing infrastructure), reconsider.

**Need to check:** Is Supabase actually in the current planning docs, or was Lane 3 reacting to a hypothetical? This should be verified before acting.
