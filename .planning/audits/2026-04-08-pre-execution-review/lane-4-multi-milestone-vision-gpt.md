# Prix Guesser Architecture Audit

Overall verdict: the project is pointed in the right direction. The current plan already centers the two decisions that matter most, authored F1 content and authoritative room state. The main long-term risks are under-specification, not wrong direction: the round contract needs stronger canonical taxonomy, the room model needs earlier durability primitives, and v2 needs more content-operations infrastructure than the current requirements list admits.

## v1 architecture risk assessment

| Area | Verdict | Risk | Audit |
|---|---|---:|---|
| Phase 1 authored round model | Good direction, not fully future-safe yet | Medium | It can support team play, async challenges, daily modes, era packs, and adjacent modes only if it is implemented as a canonical content graph, not as a flat round blob with one `answer_target_type` string and loose aliases. |
| Phase 2 judging and scoring | Directionally strong, rewrite-prone if narrowed | Medium-High | It supports `section`, `corner`, and composite answers only if judging returns structured outcomes, partials, and rationale, not just a scalar score attached to `circuit` or `venue`. |
| Phase 3 room architecture | Correct center of gravity | Medium-High | Frozen session snapshots plus authoritative rooms are the right bridge from local to online to hybrid. The risk is deferring session identity and reconnect primitives too far and accidentally making the host screen the real authority in v1. |
| Phase 4-5 UI choices | Promising split, still fragile | Medium | Separate host and controller surfaces are the right move. They will still force rewrites later if the UI hard-codes one answer widget, one clue renderer, or one giant app-state tree. |
| Phase 6 session data capture | Under-scoped | High | Per-round outcomes are not enough for long-term content compounding. The system needs round-versioned telemetry, wrong-answer capture, clue-step usage, pacing signals, and disconnect/rejoin context. |

The biggest architectural positive is that the roadmap already avoids the worst failure mode: a thin GeoGuessr clone with F1 paint. The biggest architectural gap is that the future-proofing is implied, but not yet required by the requirements.

## Recommended cheap v1 decisions that protect v2+

- Treat local couch play as one wrapper of the same authoritative room model you will use online later. Do not build a special local-only host-is-the-server path.
- Define canonical entities now: `venue`, `circuit`, `section`, `corner`, `era`, `pack`, `round`, `clue_family`, and stable aliases.
- Keep authoring file-first if you want, but put a compile/lint boundary in front of runtime content immediately.
- Model `ClueAsset`, `AnswerTarget`, `Submission`, `JudgingOutcome`, and `RevealPayload` as discriminated unions, not ad hoc per-mode objects.
- Version every playable session against frozen pack and round snapshot hashes. That one decision unlocks async challenges, dailies, replays, and trustworthy analytics later.
- Split room state into public room state and player-private state from the first multiplayer implementation.
- Give every player a stable room-session token in Phase 3. Full reconnect hardening can wait, but identity and resume hooks should not.
- Use Postgres for canonical content, snapshots, summaries, and telemetry, but keep active timer and phase truth out of the database.
- Keep client state libraries limited to local UI state and draft input. Server room state should remain the single source of truth.
- Define a transport-agnostic room API now: join, resume, submit, advance, reveal, rematch, end-session.

## 3-milestone arc sketch

### Milestone 1: Prove the party-night anchor
Ship phases 1-5 plus a thin slice of 6. The outcome should be one genuinely replayable authored room experience: host screen, phone controllers, authoritative room flow, strong reveal grammar, and 2-3 polished starter packs. Success metric: the same friend group wants another session immediately.

### Milestone 2: Build the content engine and secondary wrappers
This is where v2 should really live. Keep the current v2 ideas, but center the milestone on authoring throughput and content reuse: import/preview/lint tooling, pack versioning, richer telemetry, async/private challenges, daily rotations, session replays, player stats, private pack sharing, and finer answer surfaces where the taxonomy is strong enough.

### Milestone 3: Expand into hosted hybrid play
Only after milestone 2 proves content compounding should the project widen into hosted online rooms, team play, spectators, hybrid couch-plus-remote sessions, themed seasons, and the first adjacent non-anchor mode family. Success metric: the same content substrate supports live rooms, async challenges, and at least one adjacent mode without architectural rewrite.

## Missing requirements or phases

- Canonical content taxonomy is missing as an explicit requirement. Without it, `corner`, composite answers, era packs, and adjacent modes become special cases.
- Authoring pipeline is missing as a first-class phase. Validation alone is not enough; the project needs import, preview, lint, asset checks, and publishing flow.
- Snapshot/versioning is missing as an explicit requirement. Replays, dailies, pack sharing, and statistics all depend on frozen content versions.
- Earlier room durability primitives are missing. Stable player tokens, resume protocol, host disconnect policy, and public/private state split should begin in Phase 3, not Phase 7.
- Replay/event timeline is missing. This is valuable for both sync debugging and content review.
- Team/seating model is missing. Team play should extend the room model, not fork it later.
- Private pack sharing is missing. For a private-only project, this matters more than public UGC.
- Statistics are under-specified. `profile persistence` is not the same thing as meaningful per-pack, per-venue, and per-answer-surface stats.
- Themed seasons or recurring series are missing as a requirement if daily modes are meant to matter long-term.

## Biggest risks to project success

- The content library grows too slowly, so the game has good architecture but not enough great rounds to become a habit.
- Venue-approach and city-context clues silently overpower circuit-internal recognition, weakening the core fantasy.
- Live-room reliability on real phones is shaky, which kills social momentum faster than content flaws do.
- The host screen is functional but not watchable, so only the active solver feels engaged.
- Expansion pressure arrives too early and v2 breadth outruns v1 fun.
- Judging and UI hard-code one answer surface, turning future milestones into rewrites.
- Telemetry is too thin to tell whether a bad session came from content, pacing, or synchronization.

## Concrete recommendations with priority

| Priority | Recommendation |
|---|---|
| Critical | Make Phase 1 entity-based and union-based: canonical IDs, clue families, answer contracts, reveal contracts, and scoring contracts. |
| Critical | Move session identity, resume hooks, and public/private room state into Phase 3. Leave full reconnect hardening in Phase 7, but do not leave the model itself until then. |
| Critical | Keep v1 couch/local play on the same authoritative room architecture as future online/hybrid play. |
| Critical | Add a content compiler plus preview/lint workflow before serious pack growth begins. |
| High | Design Phase 2 judging around structured graded outcomes, not a single score formula. |
| High | Make Phase 4-5 UI surfaces role-based shells with target-type widgets and mode-specific renderers, not one monolithic app. |
| High | Capture telemetry by round version: wrong answers, clue-step usage, time-to-submit, reveal dwell, disconnects, and pack/venue class. |
| High | Recast v2 as “content engine + wrappers + stats” rather than only “more answer types + more modes.” |
| High | If online/hybrid play is a near-term goal, bias toward Colyseus-style room authority now; only take a speed-first PartyKit path if you explicitly accept lighter durability in v1. |
| Medium | Add session replay/event timeline and private pack sharing in milestone 2. |
| Medium | Add team/seating abstractions before shipping team mode. |
| Medium | Gate `section` and `corner` expansion on canonical section taxonomy and authoring confidence, not just ambition. |
| Low | Delay profiles, streaks, seasons, and adjacent non-geography modes until content supply and room reliability are already compounding. |

The central recommendation is simple: keep v1 small in product surface, but not thin in data contracts. If the project invests early in canonical authored content, frozen snapshots, authoritative rooms, and content-versioned telemetry, it can grow cleanly into async play, daily challenges, team variants, and adjacent F1 modes without betraying the original “GeoGuessr for F1 places” fantasy.