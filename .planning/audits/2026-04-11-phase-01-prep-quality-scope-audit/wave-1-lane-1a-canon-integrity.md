---
date: 2026-04-11
wave: 1
lane: 1A
audit_subject: claim_integrity
audit_orientation: investigatory
audit_delegation: self
auditor_model: claude-opus-4-6
agent_type: gsdr-auditor
scope: "Re-verify the 2026-04-08 predecessor audit's claims about the canon (PROJECT.md, LONG-ARC.md, ROADMAP.md, REQUIREMENTS.md, STATE.md) against the actual current canon. Apply the 'three legitimate outcomes' framing to each predecessor recommendation. Investigate whether the canon's apparent coherence is earned convergence or repeated assumption."
triggered_by: "wave-1 parallel dispatch from phase-01-prep-quality-scope-audit-2 orchestrator"
parent_task_spec: phase-01-prep-quality-scope-audit-2-task-spec.md
ground_rules: "core+investigatory+claim_integrity+chain+framework-invisibility"
tags:
  - wave-1
  - lane-1a
  - canon-integrity
  - claim-integrity
  - investigatory
  - opus
---

# Wave 1 / Lane 1A — Canon Claim Integrity

**Classification:** claim_integrity × investigatory × self (Opus 4.6)

## I1 — The Discrepancy, Named Concretely

Two comparison points, both treated as the standard of comparison because both are claims *about* the canon and cannot both be fully true without a reconciling move that neither states directly:

- **Claim A (the narrow initiative, 2026-04-11):** "The broader product posture is already relatively well-aligned across `.planning/PROJECT.md`, `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`" (`.planning/initiatives/vision-alignment-2026-04/README.md:24-31`). The narrow initiative's `PLAN.md:11` reinforces: "The initiative is deliberately small because the repo already has a relatively coherent product doctrine."

- **Claim B (the 2026-04-08 predecessor audit):** "Project artifacts (PROJECT.md, REQUIREMENTS.md, ROADMAP.md): NEED REVISION — three critical gaps identified before execution burns effort in the wrong direction" (`.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md:29`).

The comparison point is load-bearing because an `already-aligned` reading justifies a narrow pre-Phase-01 initiative ("do not reopen private-first posture, host-screen bias, browser-first join, long-arc frame, or anchor-mode identity" — README.md:34-42), whereas a `needs-revision` reading would justify reopening exactly those items. The narrow initiative's out-of-scope list *presupposes* the canon's adequacy on the items it excludes.

The resolution I will show below is that **both claims are partially true, but only because a canon refresh on 2026-04-11 (commit `5dfaa59`) silently absorbed roughly half of the predecessor's recommendations into the canon before the narrow initiative was drafted.** The narrow initiative's "already aligned" reading is reading a refreshed canon without announcing that the refresh was the response to the predecessor. Claim A and Claim B are not contradicting each other across the same canon — they are describing two different canons separated by a refresh. That is a separate failure mode from either "the canon is fine" or "the canon is broken."

**Why the discrepancy matters as framed.** If Claim A is accepted uncritically, several predecessor recommendations that the refresh did *not* actually address will sit invisible under the "already aligned" label. If Claim B is accepted uncritically, the real work the refresh did will be undervalued and the narrow initiative's scope-narrowing will look evasive when it is mostly principled. The audit has to do both: credit the refresh where credit is due, and name what the refresh did *not* do that the narrow initiative's framing assumes is done.

## I2 — How The Investigation Unfolded

The starting file list was useful but the investigation diverged from it twice:

1. After reading `PROJECT.md`, I searched for a canon-refresh audit trail and found `.planning/deliberations/2026-04-11-canon-refresh-change-justification.md` (not on the starting list). This document is **load-bearing for the investigation** because it reconstructs the edits made in commit `5dfaa59` and *explicitly cites which predecessor findings pushed which changes*. Without this document I would have had to infer the chain of influence from diff archaeology. With it, I can re-verify directly whether each cited link holds up.

2. After reading the canon-refresh log, I ran `git show 5dfaa59` against `PROJECT.md` to independently verify the refresh log's account. This surfaced a specific divergence: the refresh log claims to have imported the "hosted game built by a developer" framing (Opus Lane 3's "single most valuable framing"), but the diff shows the phrase itself does not appear in `PROJECT.md`. Only a softer refactor in the direction of the framing exists. This is the kind of finding the starting list alone could not have produced.

3. The `.planning/phases/01-authored-round-contract/01-CONTEXT.md` and `01-DISCUSSION-LOG.md` became load-bearing once I realized the narrow initiative's scope exclusions (venue identity, hierarchical answer targets) were **delegated to Phase 01 planning** rather than closed in the canon. Phase 01 is downstream of the canon but upstream of the narrow initiative, and its content determines whether the narrow initiative's exclusions are principled or evasive.

These three deviations from the starting list are in themselves findings about how the canon's alignment cannot be evaluated from a canon-only read — the alignment claim depends on where decisions live, and some decisions that the canon treats as "protected" have actually been pushed one layer down into Phase 01 without being closed.

## Re-Verification Ledger (Chain Integrity In Its Full Form)

Each row re-verifies a predecessor claim I actually rely on. The format is: *predecessor claim* → *file:line reopened* → *what I found* → *does the predecessor reading still hold, AND should the recommendation have been adopted in the form proposed*.

### REV-1 — "No deployment mechanism exists or is planned" (SYNTHESIS.md:102)

**File reopened:** `.planning/REQUIREMENTS.md:58-69` (Deployment And Access section), `.planning/ROADMAP.md:79` (Phase 3 requirement list).

**What I found:**
- `REQUIREMENTS.md:60-69` contains `DEPLOY-01` through `DEPLOY-05` verbatim, mapped to Phase 3/4/5 in the traceability table at `REQUIREMENTS.md:175-179`.
- `ROADMAP.md:79` references `DEPLOY-01, DEPLOY-04, DEPLOY-05` in Phase 3's requirement list.
- The refresh log at `.planning/deliberations/2026-04-11-canon-refresh-change-justification.md:232-235` explicitly credits the predecessor audit for these additions.

**Predecessor reading holds?** Yes, the *gap* was real as of 2026-04-08. **Was the recommendation adopted?** Yes, DEPLOY-01..05 were added to REQUIREMENTS.md and traced to phases. **Should it have been adopted in the form proposed?** Yes, substantively — the DEPLOY-*s are concrete, testable, and stakeholder-friendly. One reservation: `DEPLOY-02` couples "current deployment mode" to the system in a way that assumes a `party-up.sh`/`party-down.sh` operator model which is not separately canonized anywhere. The requirement is honest about the coupling, but the roadmap does not name the operator-script pattern as a deliverable. This is a soft loose end, not a failure.

**Three-outcome reading:** Outcome 1 (predecessor right, adopted). The refresh was responsive to the substance, not just the label.

### REV-2 — "Update PROJECT.md to frame as 'hosted game that happens to be built by a developer'" (SYNTHESIS.md:242, Opus Lane 3, "the single most valuable framing of the entire audit")

**File reopened:** `.planning/PROJECT.md` in full (lines 1-191); `git show 5dfaa59 -- .planning/PROJECT.md` to check the refresh diff; grep for the exact phrase across `.planning/`.

**What I found:**
- The exact phrase "hosted game that happens to be built by a developer" appears **nowhere** in `PROJECT.md`, `LONG-ARC.md`, `ROADMAP.md`, or `REQUIREMENTS.md`. It exists only in the predecessor audit itself and in a superseded Phase 01 `.continue-here.md`.
- `PROJECT.md:131-137` has a new "Future-Aware Posture" section added by the refresh. The first bullet is "The emotional center of v1 is a watchable private game-night ritual for trusted groups, not ambient public discovery" (`PROJECT.md:133`). This is a *related* framing but is about the product posture, not about stakeholder identity.
- The explicit stakeholder-identity flip that the predecessor audit described — "Stop thinking of this as a developer project that happens to be private. Think of it as a hosted game that happens to be built by a developer. The build toolchain is for Logan. The deployment target is for everyone." — is not encoded anywhere in the canon as a stated framing. The "non-technical friend is the real stakeholder, not the developer" cross-lane pattern (SYNTHESIS.md:200) is also not stated.
- The refresh log (`canon-refresh-change-justification.md:97-146`) claims to have been influenced by this framing but describes its implementation as "browser-first guest surface" and "explicit trust and service-obligation modesty" — softer, posture-level changes rather than the stakeholder-identity inversion the predecessor proposed.

**Predecessor reading holds?** Yes — the framing was not in the canon before and is still not in the canon. The refresh added *adjacent* content (browser-first guest bullet, TV-distance UX-01, DEPLOY-01..05) but did not adopt the stakeholder-identity reframe.

**Was it adopted?** No, not in the form proposed. The refresh treated the framing as a *directional hint* rather than as a load-bearing sentence to import.

**Should it have been adopted in the form proposed?** This is the most contestable cell in the ledger and I will not collapse it.

*Interpretation 1: The refresh was principled in not importing a slogan.* The predecessor's framing is a useful *orchestrator-level* sentence but it is a rhetorical flourish; the operative consequences (browser-first guest experience, TV-distance UX, self-host parity, QR/code/link join, no Supabase dependency) were adopted piecemeal and the slogan itself would not add anything the adoption does not already carry.

*Interpretation 2: The refresh softened the recommendation past its operative core.* The predecessor's framing is not a slogan; it is a **stakeholder-orientation test**. It asks: when you look at a decision, whose experience are you using as the criterion? That test is absent from the canon. Evidence: `PROJECT.md:4-8` still says the game "is being initialized for personal and friend play rather than public release" — the friend appears as a consumer of "play" but not as the implicit criterion for design decisions. `PROJECT.md`'s Audience constraint says "Initial audience is expert-biased long-time fans — the design does not need to flatten itself for casual users first" — this is a content posture, not a stakeholder-orientation. The predecessor's warning was specifically that the project would otherwise drift into a "what does the dev build" orientation, and the canon refresh did not install the counter-anchor the predecessor wanted.

*Interpretation 3: The omission is correct for a private-only friends-only fan project but would be wrong for any other project.* A slogan that flips the stakeholder identity to "game for friends, built by a developer" is ultimately a distribution/adoption frame. In a friends-only fan game with a hand-picked audience, "the developer" and "the audience" overlap enough that the flip carries less weight than in the cases the predecessor was drawing analogies from (hosted-service mindset, platform mindset). The refresh may have correctly detected that the friends-only scope softens the recommendation without making it wrong.

**My reading, stated:** Interpretation 2 has more weight than Interpretation 1 because the operative consequence of the framing is not just browser-first guest plumbing — it is a decision-orientation test the canon does not have. But Interpretation 3 partially carries: the weight of the omission depends on whether the project's scope stays friends-only. If the project ever considers share-by-link, unlisted, or broader visibility surfaces (which `LONG-ARC.md:74-79` explicitly stages as possibilities), the absent stakeholder-orientation test will matter. This is a finding I flag for the synthesizer rather than a verdict.

**Three-outcome reading:** Outcome 3 with residue — the predecessor's recommendation was right in spirit, the refresh adopted it in shape (through browser-first and Future-Aware Posture language) but not in its operative form (as a stakeholder-orientation test), and the project's scope softens but does not eliminate the absence.

### REV-3 — "Watchability is load-bearing but undefined" (SYNTHESIS.md:197-198, Cross-Lane Pattern 1)

**File reopened:** `PROJECT.md:45-50, 158, 168-169`; `ROADMAP.md:26, 104-114`; `LONG-ARC.md:112`; `REQUIREMENTS.md:49` (UX-01).

**What I found:**
- `PROJECT.md:49` defines "watchability layer" as "the host-screen clarity, suspense, and reveal payoff that make a session socially legible." This is *operationalization-adjacent* — it names the constituent parts rather than giving a measurable criterion.
- `PROJECT.md:158` marks "host-screen-friendly private play" as "Adopted for v1", citing watchability as the rationale, and `PROJECT.md:168-169` keeps "watchability vs pure solver challenge balance" as a Medium open question marked "Leaning: watchability is load-bearing, exact balance still open."
- `ROADMAP.md:104` (Phase 3.1 Success Criterion 4) says "Watchability is made concrete as shared-legibility, suspense, and reveal payoff rather than left as an abstract aspiration." This is a *deferral* of operationalization to Phase 3.1.
- `REQUIREMENTS.md:49` (UX-01) strengthens watchability with a TV-distance constraint ("remains legible on a 16:9 TV at couch distance") — this is an observable, testable criterion.
- `LONG-ARC.md:112` says "Streamer-friendliness first means watchability, role clarity, code safety, and spectator seams" — again, constituent-parts framing.

**Predecessor reading holds?** Partially. The predecessor said the term was load-bearing but undefined, and recommended it should either be "defined concretely (Lane 2's visual contract, Lane 3's TV-distance constraints) or removed as a term" (SYNTHESIS.md:198). The TV-distance constraint has been installed in UX-01; the visual contract has been pushed to Phase 3.1. But the *operational definition* of watchability as a concept — "watchability means X, measured by Y" — still does not exist in the canon as an assertable test. The canon has decomposed watchability into (shared-legibility + suspense + reveal payoff) which are themselves undefined.

**Was it adopted?** Half-adopted. The concrete *surface* that the predecessor proposed (TV-distance UX-01) is there; the concrete *definition* the predecessor also implied is still absent and has been pushed to Phase 3.1. Whether the push to Phase 3.1 is principled depends on whether Phase 3.1 has the affordance to close it, which I cannot verify from canon-only reading (this is a cross-lane dependency on Lane 1B's methodological-inheritance investigation).

**Should it have been adopted in the form proposed?** The predecessor's binary ("define concretely or remove") was too strong — operationalizing a design concept like "watchability" at the project-level before having done the design work for it risks freezing the wrong operationalization. A *deferral-with-closure-criteria* is a legitimate compromise and `ROADMAP.md:104` is that compromise. But the canon does not explicitly say "we are deferring watchability operationalization to Phase 3.1 as a principled deferral" — it just says Phase 3.1 will do it. The principled-deferral reading is implicit, not stated.

**Three-outcome reading:** Outcome 1 for the UX-01 surface; Outcome 3 for the definition (deferred for principled reasons, but the principledness is not named as such in the canon).

### REV-4 — "Hierarchical vs flat answer target model — THE most important architectural decision" (SYNTHESIS.md:212, GPT Lane 4)

**File reopened:** `REQUIREMENTS.md:126` (SEAM-01); `ROADMAP.md:11, 48, 64`; `.planning/phases/01-authored-round-contract/01-CONTEXT.md:22` (D-04); `01-DISCUSSION-LOG.md:30` (Answer Surface And Identity Modeling).

**What I found:**
- `REQUIREMENTS.md:126` (SEAM-01): "The authored round model should preserve explicit `venue -> circuit -> section -> corner` relationships rather than collapsing the answer contract to coordinates only or flat labels only." This is a *seam declaration*, not an architectural-decision statement. It says the hierarchy must be preserved; it does not say the schema must model it as a hierarchy rather than as flat targets plus aliases.
- `ROADMAP.md:11`: "v1 answer surfaces are intentionally anchored at `circuit` and `venue`; finer-grained `section` or `corner` answers stay out of scope unless a later inserted phase is justified by playtest evidence, but the answer-target model should preserve that hierarchy now."
- `01-CONTEXT.md:22` (D-04): "Keep active v1 gameplay anchored at `circuit` and `venue`, while preserving explicit `venue -> circuit -> section -> corner` lineage in the authored model so later deeper answer surfaces do not require a flat-contract rewrite."
- `01-DISCUSSION-LOG.md:30`: The Phase 01 discuss pass auto-selected "Hierarchical lineage, narrow v1 scope" as the grounded direction.

**Predecessor reading holds?** The gap was real on 2026-04-08. **Was it adopted?** Partially. SEAM-01 declares the hierarchy must be preserved; D-04 in 01-CONTEXT.md adds "lineage" as the encoding (which is closer to "flat targets with hierarchical relationships as metadata" than to "hierarchical targets as primary structure"). The predecessor's *specific* recommendation — "the schema should model structured relationships: `venue contains circuit contains section contains corner`" (GPT Lane 4) — is in the 01-DISCUSSION-LOG as a selected option but the actual schema shape is still downstream of Phase 01 planning. The schema-driven judging engine recommendation (GPT's corollary) is deferred to Phase 2 and not yet specified.

**Is the placement principled?** The canon has treated this as a seam-protection decision (correct) rather than as an architectural decision (what the predecessor proposed). That is a real category shift: a seam-protection decision says "do not foreclose"; an architectural decision says "here is what we are building." Treating it as seam-protection is defensible for a Phase 01 that is about content contract rather than judging engine, but it also means **the canon does not *close* the predecessor's "most important architectural decision"** — it just protects the possibility of closing it later.

**Should it have been closed in the canon?** Probably not. The predecessor's escalation ("THE most important architectural decision in the audit") was partly rhetorical and partly about leverage — it was the *cheapest* architectural decision to get right in Phase 01, not necessarily the most important in absolute terms. The canon's treatment (preserve the seam, close the specific shape in Phase 01 research) is a legitimate narrower adoption of the recommendation. But it should be named as a narrower adoption, not as a full adoption.

**Three-outcome reading:** Outcome 3 — the predecessor was right that the decision is cheap to make early and expensive to retrofit, but the specific *shape* of the recommendation (hierarchical schema from day one) has been softened to "preserve the hierarchy as a seam, close the exact shape in Phase 01." This softening is principled.

### REV-5 — "F1 GeoGuessr vs F1 Jackbox identity question" (SYNTHESIS.md:Q2, not directly addressed in either pass but flagged as "the most important strategic question in the project")

**File reopened:** `PROJECT.md:5, 41, 163-165`; `LONG-ARC.md:35-46`; `ROADMAP.md:4`.

**What I found:**
- `PROJECT.md:5`: "It starts with grand prix venues, circuits, and race-weekend location literacy, while intentionally leaving room to grow into a broader F1-flavored party game where geography is the anchor rather than the whole product." This is still *Identity B wording* (party game platform with anchor).
- `PROJECT.md:41-43`: "Three tensions need to stay visible: — the seed fantasy is 'GeoGuessr for grand prix locations' — the bigger ambition is 'an F1-flavored party game platform' — the current reality is 'private-only project for personal and friend play'." This is an *explicit refusal to collapse the tension* — all three are preserved.
- `PROJECT.md:163-165`: "Is the best first product a tight geography game or a broader party shell with one anchor mode? — Criticality: Critical — Status: Leaning: anchor-first with future wrappers protected." This is a *leaning, not a decision*.
- `LONG-ARC.md:35-46`: "The mature shape is best understood as one authored F1 substrate plus multiple possible wrappers, not as one frozen app shape." This is Identity B *at the long-arc level* — substrate + wrappers.
- `ROADMAP.md:4`: The v1 overview describes sequencing for "one authored F1 anchor mode and one strong private-room social wrapper" — Identity A *at the v1 level*.
- The word "Jackbox" does not appear in any canon document. The word "GeoGuessr" appears in `PROJECT.md:5, 41, 68` as a fantasy-framing anchor and as a reference to `benlikescode/geohub`.

**Predecessor reading holds?** The predecessor said the project was "documented as identity B but planned as identity A" (SYNTHESIS.md:305). This reading still holds, with one refinement: the current canon *names the tension* explicitly (`PROJECT.md:41-43`) whereas the pre-refresh version did not. The canon is now *aware* of the tension and explicitly refuses to close it. That is a legitimate move, not an unresolved bug.

**Was it adopted?** No — the predecessor recommended adopting Identity B explicitly. The canon instead decided to *hold the tension visible* and lean toward anchor-first with future wrappers protected. This is neither Identity A nor Identity B; it is a third option the predecessor did not offer: "keep both live, resolve at milestone transition."

**Should the predecessor's recommendation have been adopted in the form proposed?** The predecessor's reasoning was: "If v1 architecture assumes identity A, v2 mode expansion becomes a rewrite. If v1 architecture assumes identity B, v1 is more complex than it needs to be for the anchor mode alone" (SYNTHESIS.md:305). The canon's third option (hold tension, protect seams) is defensible if and only if the seam protection is real. SEAM-01..SEAM-05 in REQUIREMENTS.md are the seam protection. `SEAM-04` is the load-bearing one: "The authored content substrate should stay reusable across private-room play and plausible later wrapper surfaces such as async challenges, solo practice, or adjacent expert-facing modes." If this seam is actually preserved in Phase 01 content-contract decisions, Identity B remains viable as a later pivot; if the Phase 01 execution narrows the substrate, the seam is notional only.

**Three-outcome reading:** Outcome 3 — the predecessor's recommendation was right in spirit (the tension needs addressing) but the canon found a better shape (hold it visible, protect the seams, close at milestone boundary). This is a *legitimate disagreement with the predecessor*, not a failure to adopt. The canon's shape is defensible for a private-only friends-only project where locking Identity B would add ceremony that a friends-only scope does not need.

### REV-6 — "Colyseus vs PartyKit as distribution decision, not neutral runtime choice" (SYNTHESIS.md:226, GPT Lane 3)

**File reopened:** `ROADMAP.md:10-11, 94` (Phase 3 Open decisions).

**What I found:**
- `ROADMAP.md:10`: "The roadmap commits v1 to live private rooms as the first social wrapper, but keeps the room runtime choice open until planning clarifies how strong the reconnect and timer guarantees must be."
- `ROADMAP.md:11`: "The room runtime choice is also a deployment and self-host-parity decision, not only a multiplayer-library taste choice."
- `ROADMAP.md:94` (Phase 3 Open decisions): "Choose `Colyseus` if this phase promises strong reconnect and timer correctness or self-host/private-host parity from the start; choose `PartyKit` only if planning explicitly optimizes for private-prototype speed over early durability and deployment parity."

**Predecessor reading holds?** Yes. **Was it adopted?** Yes, in the stronger form the predecessor proposed — the canon explicitly names the runtime choice as a *distribution* choice and names the default bias toward Colyseus on self-host-parity grounds. **Should it have been adopted in the form proposed?** Yes. This is clean Outcome 1.

### REV-7 — "Phase 3.1 inserted phase — is the goal/criteria actually delivering what the predecessor was asking for" (Lane investigatory question LQ-1A.2)

**File reopened:** `ROADMAP.md:26, 96-114`.

**What I found:**
- `ROADMAP.md:26`: The phase exists by name: "Phase 3.1 (INSERTED): UI Direction, Design System, And Interaction Contract."
- `ROADMAP.md:99-103` (Success Criteria): (1) "`UI-SPEC.md` defines visual direction, typography, color system, motion grammar, and separate host-screen versus controller principles." (2) Join flow, controller answer flow, host clue state, answer lock, reveal, standings, replay states specified before implementation. (3) Responsive rules for phone portrait, laptop operator, 16:9 TV or fullscreen host-screen. (4) "Watchability is made concrete as shared-legibility, suspense, and reveal payoff rather than left as an abstract aspiration."
- The predecessor's GPT Lane 2 deliverable list (SYNTHESIS.md:77-83) included: UI-SPEC.md, host/controller principles as separate subsections, key-screen mocks, motion grammar, responsive rules, component inventory. The canon's Phase 3.1 hits all of these *except* the component inventory (timer rail, answer-surface chip, clue card, room-code hero, reveal panel, standings board, replay CTA).
- The **component inventory is not in the canon.** The roadmap Phase 3.1 success criteria list types of content but does not commit to a component inventory as a deliverable.
- `ROADMAP.md:105-108` canonical refs for Phase 3.1 include `REQUIREMENTS.md` (UX-01..UX-04, DEPLOY-02, DEPLOY-03, SEAM-03), `PROJECT.md`, `LONG-ARC.md`, and `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`. The reference to the predecessor audit is interesting — it cites CONVERGENCE.md rather than importing the specific deliverables into the canon.

**Predecessor reading holds?** Half — the predecessor's Option B (inserted phase) was adopted; the specific deliverable list is *referenced* but not fully imported.

**Phantom integration risk?** Partial. A phantom integration would be "phase exists by name but goal/criteria don't match what the predecessor was asking for." The canon's Phase 3.1 goals do match the predecessor's intent at 4-of-5 granularity; the missing 1 is the component inventory, which is operational enough that its absence leaves room for a Phase 3.1 pass that focuses on visual direction without committing to a domain-component contract. This is a real gap but small enough that I would not call it a phantom.

**Should it have been adopted in the form proposed?** Option B (inserted phase) was the higher-ceremony path; Option A (lightweight artifact) was the lower-ceremony path. The canon's choice was principled — the refresh log at `canon-refresh-change-justification.md:190` says "I chose the inserted phase path because the roadmap refresh was already a structural-document pass, and the converged finding was that design debt was load-bearing rather than cosmetic." This is a defensible reason.

**Three-outcome reading:** Outcome 1 for the structural choice (Option B), Outcome 3 with soft residue for the deliverable list (component inventory not imported, unlikely to be a phantom).

### REV-8 — "Cosmetics out of scope warning — protect against misreading" (SYNTHESIS.md:246, GPT Lane 2)

**File reopened:** `REQUIREMENTS.md:147` (Out of Scope table).

**What I found:**
- `REQUIREMENTS.md:147`: "Progression economies, collection systems, or cosmetic unlock loops | Do not strengthen the core expert-fan social loop"
- The phrase "cosmetics out of scope" in isolation does not appear. The actual out-of-scope item is about **cosmetic unlock loops** (progression/collection), not about visual polish or the visual contract.
- The refresh log at `canon-refresh-change-justification.md:239` notes this reframe: "Updated the out-of-scope wording on progression/cosmetics so it reads more like a product-shape exclusion than a throwaway placeholder."

**Predecessor reading holds?** Yes — the predecessor's concern was that "cosmetics out of scope" could be misread as "deprioritize visual polish." **Was it adopted?** Yes — the canon now reads "cosmetic unlock loops" which makes the intent unambiguous.

**Three-outcome reading:** Outcome 1, clean.

### REV-9 — "Supabase wrong-fit, replace with local PostgreSQL" (SYNTHESIS.md:230, Opus Lane 3)

**File reopened:** `research/STACK.md:15, 24, 55`; `research/SUMMARY.md:17`; `canon-refresh-change-justification.md:310-328`.

**What I found:**
- `research/STACK.md:15`: "`Supabase` is optional hosted convenience, not the canonical database or storage assumption."
- `research/STACK.md:24`: Persistence bullet says "provider-neutral object storage or filesystem-backed private media storage, with `Supabase` still acceptable as an optional managed convenience."
- `research/STACK.md:55, 151, 161` continue to reference Supabase but consistently as optional convenience.
- **Note on scope:** `research/STACK.md` is *research canon*, not product canon. The predecessor's recommendation was specifically about the canon (PROJECT.md and STACK.md). The product canon itself does not name Supabase at all — it is "out of scope" in the sense that it lives in the research tier.

**Predecessor reading holds?** Yes on 2026-04-08; resolved by the refresh via annotation rather than removal.

**Was the recommendation adopted in the form proposed?** The predecessor recommended "Replace Supabase with local PostgreSQL in Docker" — an active replacement. The canon's refresh instead softened Supabase to "optional managed convenience." These are operationally similar (both remove Supabase as a hard dependency), but the refresh's shape is gentler: it does not foreclose Supabase, it just removes its canonical status.

**Should it have been adopted in the form proposed?** The softer form is probably better. An outright replacement ("never use Supabase") would foreclose a legitimate future option (a later hosted deployment that *wants* Supabase for the admin/auth plumbing). The softening is principled.

**Three-outcome reading:** Outcome 3 — predecessor's operative concern addressed, shape was softened for good reasons.

### REV-10 — "Venue identity ambiguity in Phase 1" (SYNTHESIS.md:210, GPT Lane 1 G1)

**File reopened:** `.planning/phases/01-authored-round-contract/01-CONTEXT.md:22-23` (D-05); `01-RESEARCH.md:192, 211-212`.

**What I found:**
- `01-CONTEXT.md:23` (D-05): "Make venue and circuit identity explicit and canonical. Downstream implementation should converge on one stable identifier strategy rather than parallel `id`/`venueId`/filename conventions that force executors to invent resolution rules."
- The decision is *named* at the context level ("converge on one stable identifier strategy") but not *closed* (which strategy?). This is delegated to planning.
- `01-RESEARCH.md:192, 211-212` cite the predecessor's finding as `[VERIFIED: .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md]` — the research acknowledges the finding but does not close it.
- The four `01-XX-PLAN.md` files (which the task spec said to treat as stale residue) still contain parallel `id`/`venueId`/`venueRef` usage, but those are slated for deletion, so they are not load-bearing.

**Predecessor reading holds?** Yes. **Was it adopted in the canon?** Partially — the canon (via 01-CONTEXT) states the *requirement* that identity should converge but does not close *how* it converges. **Should it have been closed in the canon or pushed to Phase 01 planning?** The latter is correct — venue identity is a Phase 01 implementation-level decision, not a product-shape decision. The canon's job is to state the constraint, not to pick the key. The canon's treatment is principled.

**Three-outcome reading:** Outcome 3 — predecessor right, canon's response was to push the decision one layer down to where it belongs. The narrow initiative's scope exclusion list does not include venue identity explicitly, but the content-contract in-scope item at `README.md:54` ("Pack/round identity and reference freezing") does own this decision. This is not a gap.

### REV-11 — "PackSourceSchema / roundOrder reference shape not frozen early enough" (SYNTHESIS.md:211, GPT Lane 1 G2)

**File reopened:** `01-CONTEXT.md:20` (D-03).

**What I found:**
- `01-CONTEXT.md:20` (D-03): "Freeze an explicit reference contract between pack entries and rounds early in Phase 1 so later compile and snapshot steps do not rely on filename-only inference or accidental ordering."

**Three-outcome reading:** Outcome 1 — predecessor right, canon adopted the *requirement* at context level (appropriate for canon) and left the exact shape to Phase 01 planning.

### REV-12 — "Stable diagnostic codes for broken venueRef and path-policy failures" (SYNTHESIS.md:218, GPT Lane 1 G4)

**File reopened:** `01-CONTEXT.md` full text (grep for "diagnostic").

**What I found:** The term "stable diagnostic" does not appear in `01-CONTEXT.md` or `01-RESEARCH.md`. The concern is mentioned in `01-RESEARCH.md` as a predecessor-audit finding but not carried into the Phase 01 decisions list.

**Predecessor reading holds?** Yes — this is a real Phase 01 gap. **Was it adopted?** Not at the canon level and possibly not at the Phase 01 context level either. This is a *gap the narrow initiative should own* since the narrow initiative names "Pack/round identity and reference freezing" as in-scope, and diagnostics for broken references is a seam-level concern the narrow initiative should touch.

**Three-outcome reading:** Outcome 2 (or possibly Outcome 3 if the narrow initiative closes it). The narrow initiative's scope list is broad enough to cover it; whether it actually closes it is a Phase 01 planning question.

## LQ-1A.1 Verdict — Earned Convergence Or Repeated Assumption?

**Neither cleanly, but closer to earned convergence than to repeated assumption.** The specific load-bearing claim I tested:

**Test case: "private-only fan project" / "trusted group private play" posture.**

Appearances:
- `PROJECT.md:5` "unofficial, private-only F1 fan game project"
- `PROJECT.md:30` "this is private-only for now"
- `PROJECT.md:133` "watchable private game-night ritual for trusted groups"
- `PROJECT.md:136` "trusted private rooms now, unlisted/share-by-link surfaces later"
- `PROJECT.md:141` "Private-only, unofficial fan project"
- `PROJECT.md:153` "Initialize as a private-only fan project" (marked Adopted)
- `LONG-ARC.md:26` "The current product center is a private, watchable, host-led, browser-first F1 game-night ritual"
- `LONG-ARC.md:30` "private-room use is the primary posture"
- `LONG-ARC.md:58-68` "Transition Doctrine" section
- `ROADMAP.md:4` "without drifting into ... premature public-product obligations"
- `ROADMAP.md:13` "private trusted-room play now, unlisted/share-by-link surfaces later"
- `REQUIREMENTS.md:134-138` DEF-01..DEF-05 deferrals

**Is the claim argued or asserted?** The claim is *asserted* in `PROJECT.md:5, 30, 141, 153` and *argued* in `LONG-ARC.md:58-68` ("Transition Doctrine") and `REQUIREMENTS.md:134-138` (explicit deferrals with reasoning). LONG-ARC.md was canonized on 2026-04-11 explicitly to "ratify the durable parts of that thinking in one place" (`LONG-ARC.md:18-20`) — meaning the private-first posture *used to be* repeated assumption scattered across docs, and LONG-ARC.md was the act of promoting it to earned convergence.

**Do the canon documents agree for the same reasons?** Yes, now. LONG-ARC.md is the reasoning-layer that PROJECT.md, ROADMAP.md, and REQUIREMENTS.md all cite. Before 2026-04-11 they would have been repeated assumption. After 2026-04-11 they are earned convergence — but the earned convergence is *recent* (one day old at time of this audit).

**Are there places where the documents diverge?** Two:

1. **`PROJECT.md:163-165` vs `ROADMAP.md:4`.** PROJECT.md Q1 "Is the best first product a tight geography game or a broader party shell" is marked "Critical — Leaning: anchor-first with future wrappers protected." ROADMAP.md commits v1 to anchor-first in its overview. The canon says "Leaning" at the decision table but "committed" at the roadmap overview. This is a mild divergence — the roadmap is acting on a leaning as if it were a decision.

2. **`PROJECT.md:5` ("fantasy of GeoGuessr for Formula 1 places") vs `PROJECT.md:41` (three tensions: seed fantasy, bigger ambition, current reality).** The framing is not contradictory but the lede uses the anchor-only framing while the context preserves the platform-possible framing. A reader who only reads the first paragraph gets a different weight than a reader who reads the full context section.

**Are there places where documents agree but for different reasons?** Yes, one significant case:

**"Preserve the seam for future wrappers" appears in both PROJECT.md:131-137 (Future-Aware Posture) and LONG-ARC.md:61-68 (Transition Doctrine), and in ROADMAP.md:34-48 (Phase 1's Protects statement).** But:
- `PROJECT.md` grounds it in "emotional center" and "browser-first guest surface"
- `LONG-ARC.md` grounds it in "product obligation threshold" and "preserve the authored substrate first"
- `ROADMAP.md` grounds it in "answer-surface contract and fallback-media model stay extensible"

These are three different reasons for the same conclusion — emotional, operational, and technical. **This is fragile agreement.** If any one of the grounding reasons turns out to be wrong, the conclusion does not automatically re-derive from the other two. This is an *earned convergence* at the document level but an *un-stress-tested one* at the reasoning level.

**Verdict, stated directly:** The canon's apparent coherence is **recent earned convergence stapled onto older repeated assumption, with the earned part concentrated in LONG-ARC.md (new) and the older documents retrofitted to cite it.** The refresh on 2026-04-11 did real work — it installed LONG-ARC.md as the doctrine layer, it wired DEPLOY-*s into REQUIREMENTS.md, it added seam protections, it cross-referenced the predecessor audit in Phase 3.1 and Phase 01 context. But the claim "already relatively well-aligned" in the narrow initiative is reading the canon *as if* the convergence were long-standing, when in fact it is one day old and has not been stress-tested by a cycle of use. The narrow initiative's decision to not reopen private-first posture, host-screen bias, browser-first join, long-arc frame, or anchor-mode identity is **principled but provisional** — the posture is in the canon as convergence, but the convergence has not yet survived its first planning pass.

This verdict cuts against the I3 instinct to offer two interpretations. I will: *Interpretation A:* the convergence is earned and the narrow initiative is correctly trusting it. *Interpretation B:* the convergence is a one-day-old retrofit and the narrow initiative is trusting a document state that has not yet been tested against Phase 01 planning work. The ruling-out logic: I cannot rule out B because the first test of the convergence will be the rerun of `discuss-phase` for Phase 01 (`STATE.md:68`), and that test has not happened. I *can* partially rule out A: the canon-refresh-change-justification's own "Review Questions This Note Should Enable" section at `canon-refresh-change-justification.md:498-503` names several open review questions that the refresh explicitly acknowledges are not yet resolved. The refresh knows it is not done.

## LQ-1A.3 — Untyped Load-Bearing Assumptions (PROJECT.md Key Decisions Honesty Check)

**"Initialize as a private-only fan project" — really decided, or deferring distribution questions by definitional fiat?**

Evidence the decision is substantive:
- `REQUIREMENTS.md:134-138` (DEF-01..DEF-05) explicitly names what is being deferred.
- `LONG-ARC.md:73-81` Visibility ladder gives a staged path forward that does not require re-opening the decision.
- `REQUIREMENTS.md:60-69` (DEPLOY-01..05) commits to concrete private-host operational patterns.

Evidence the decision is definitional fiat:
- The stakeholder-identity reframe (REV-2) is absent. "Private-only" is consumer-facing — it does not answer the question "whose experience is the criterion for design decisions?"
- The "unlisted/share-by-link surfaces later" stage in `LONG-ARC.md:78` is named but has no transition criteria — `LONG-ARC.md:144-154` names the changes-that-would-reopen-doctrine but they are framed as "if the product center changes" rather than as positive readiness tests.
- The v2 requirements at `REQUIREMENTS.md:111-117` include `DIST-01`/`DIST-02` which are *already* about private-remote-host access. The decision to be "private-only for now" is softened in v2 without a named trigger.

**Reading:** Substantively decided for v1, but the v1/v2 transition is load-bearing work that the canon has not scoped. The "Adopted" mark is honest-enough for v1 but is load-bearing on an implicit "for v1" qualifier that the table does not state.

**"Bias toward authored F1 rounds instead of thin location-only rounds" — really decided, or papering over authoring sustainability?**

Evidence the decision is substantive:
- `PROJECT.md:63` "The current bias is strongly toward the authored model."
- `REQUIREMENTS.md:PACK-02` operationalizes authored rounds as the pack schema.
- `research/PITFALLS.md` (cited in `01-CONTEXT.md:98`) names thin-schema drift as a specific risk.

Evidence of unaddressed sustainability question:
- The predecessor audit's biggest risk (`SYNTHESIS.md:186`) was: "Content authoring is too painful → corpus never reaches critical mass (both ranked this #1)".
- The canon *does not address this risk* anywhere. `ROADMAP.md` Phase 6 ("Starter Packs And Calibration") is the closest, but it assumes authoring is viable, not that it is the load-bearing risk.
- The narrow initiative's scope at `README.md:67` explicitly excludes "in-app authoring UI" — this is a legitimate deferral of the *tooling* question, but not of the *sustainability* question.

**Reading:** The authored-round bias is decided; the authoring-sustainability risk is **not named anywhere in the canon as a load-bearing risk**. This is a live untyped assumption. The canon assumes authoring will scale; the predecessor audit said authoring sustainability is the #1 fun risk; the narrow initiative excludes authoring UI from scope without acknowledging that the exclusion does not resolve the risk.

**"Bias toward host-screen-friendly private play" — really decided, or inheriting aesthetic preference without engaging operational requirements?**

Evidence the decision is substantive:
- `UX-01` concretizes "host-screen" to "legible on a 16:9 TV at couch distance."
- `DEPLOY-03` commits to fullscreen presentation without cast-specific integrations.
- `LONG-ARC.md:110-116` names the operational meaning ("watchability, role clarity, code safety, spectator seams").

Evidence the decision is aesthetic:
- The watchability concept itself remains constituent-defined ("shared-legibility + suspense + reveal payoff") without an operational test. See REV-3.

**Reading:** Substantively decided on the surface (TV-distance, fullscreen) but operationally soft on the interior (what makes something watchable). The interior softness is an acknowledged principled deferral to Phase 3.1, not a smuggled assumption.

**Are these the right Open Questions?** The `PROJECT.md:163-171` Open Questions table names 7 questions. Missing from it:

1. **Authoring sustainability as a #1 risk.** The predecessor audit's top risk is not anywhere on the canon's questions or decisions tables.
2. **Stakeholder-orientation test** (REV-2). Not named.
3. **Cross-milestone leverage marking per phase** (SYNTHESIS.md:Q3). The predecessor proposed a `cross_milestone_leverage` field per phase in ROADMAP.md. `grep` returns zero matches. This is a meta-gap the canon did not adopt. Whether it *should* have been adopted is contestable — it is ceremony-heavy for a 7-phase roadmap on a friends-only project. But the absence is not named or justified.

## LQ-1A.4 — The Narrow Initiative's Exclusions As Canon Claims

The narrow initiative's out-of-scope list at `README.md:59-66`:
- frontend framework choice
- room runtime and authority implementation
- deploy topology decisions
- public/share-by-link/public-spectator posture
- adjacent F1 mode expansion
- in-app authoring UI

**frontend framework choice:** `PROJECT.md:156` Key Decisions marks this as "Still open." Canon-level deferral is honest. Legitimate exclusion.

**room runtime and authority implementation:** `PROJECT.md:157` marks as "Still open." `ROADMAP.md:94` (Phase 3 open decisions) names the Colyseus-vs-PartyKit question. Canon-level deferral is honest. Legitimate exclusion.

**deploy topology decisions:** This is the subtle one. The canon *does* own deploy topology now (DEPLOY-01..05 in REQUIREMENTS.md, Phase 3 requirements). The narrow initiative's exclusion is of *further* deploy topology decisions beyond the DEPLOY-* level, but the exclusion list does not distinguish "already-canonized deploy topology" from "further topology decisions." This is a mild boundary ambiguity.

**public/share-by-link/public-spectator posture:** `LONG-ARC.md:70-81` (Visibility And Discovery Ladder) and `REQUIREMENTS.md:134-138` (DEF-01..05) own this. Canon-level deferral is honest. **But the user's stance quoted in the task spec** — "not convinced by momentum/time-pressure arguments; consider deployment/distribution/adoption broadly" — overlaps directly with this exclusion. The narrow initiative is excluding exactly the question the user asked to consider. Whether this exclusion is legitimate depends on whether the *canon* is adequate to support reopening the question later, and on whether the narrow initiative is the right vehicle to address it.

**adjacent F1 mode expansion:** `REQUIREMENTS.md:138` (DEF-04) explicitly defers. Legitimate exclusion.

**in-app authoring UI:** `REQUIREMENTS.md` v2 section has `OPS-V2-02` for this. But the authoring *sustainability* risk (LQ-1A.3) is not named anywhere. The narrow initiative excludes the *tool* without naming the *risk the tool would address*. This is a **real gap** — the exclusion is legitimate at face value but silently treats "UI" as the only response to a risk that also has non-UI responses (authoring workflow, author-facing diagnostics, round-template libraries).

**Gap the exclusion list owns but the canon does not:** The narrow initiative's exclusion of `public/share-by-link/public-spectator posture` is defensible for a Phase 01 content-contract initiative, but it collides with the user's stated stance about considering deployment/distribution/adoption broadly. The canon has the DEF-* deferrals but those are *reasons-not-to-decide*, not *conditions-under-which-to-decide*. The narrow initiative is treating the DEF-* deferrals as if they remove the question from the table for pre-Phase-01 work. That is defensible if the question is genuinely not load-bearing for Phase 01's content contract. The question is: **is the authored content contract independent of distribution posture?** Probably yes for a private-only-for-now project. Probably no for a project that might share packs by link in v2. SEAM-04 in REQUIREMENTS.md:129 says pack substrate should stay reusable across "private-room play and plausible later wrapper surfaces such as async challenges, solo practice, or adjacent expert-facing modes." That mentions wrappers but not **sharing**. Pack sharing is in v2 (`OPS-V2-03`) but is not marked as a seam the content contract must preserve. **This is a real gap the narrow initiative inherits and does not surface.**

## How I Navigated Tensions Between Obligations

**Tension 1: I2 (let the investigation guide artifact selection) vs the task spec's suggested starting file list.**

The task spec's suggested list was explicit that it was a starting list, not a closed list. The tension emerged when I found that the most load-bearing single document — `canon-refresh-change-justification.md` — was not on the starting list. If I had stuck to the starting list, I would have had to infer the refresh's intent from the diff rather than reading the explicit reconstruction. The resolution was to read the unsuggested document first and treat it as a *contestable* document, not as ground truth — my REV-2 finding (the "hosted game" framing was claimed to influence the refresh but does not appear in the canon) is precisely the kind of finding that surfaces when you read a refresh log against the actual canon rather than taking either in isolation.

Navigating this was not "picking" I2 over the starting list — the starting list *said* I could deviate. The navigation was more subtle: the refresh log is a *predecessor-like document* that could itself anchor the investigation in the wrong direction (toward trusting the refresh's self-reported story), and the chain integrity obligation required me to re-verify the refresh log's claims the same way I was re-verifying the predecessor audit's claims. The resolution was to treat the refresh log as a *third* claim source alongside Claim A and Claim B, not as tie-breaker evidence between them.

**Tension 2: Chain integrity's "re-verify each predecessor claim" vs the three-outcome framing's "the predecessor's recommendations are contestable claims."**

Chain integrity says: re-verify the predecessor. The three-outcome framing says: don't treat the predecessor as authoritative. These push in the same direction on Outcome-1 findings ("was it adopted?" — yes or no) but tension on Outcome-3 findings ("should it have been adopted in the form proposed?" — a contestable value question). I navigated this by keeping the two questions separate in every REV-* entry: the re-verification is one act (fact), the adoption-appropriateness is a separate act (judgment), and I do not collapse them. REV-2 is the clearest example — re-verifying that the "hosted game" framing was not adopted is a factual finding; my reading of whether the omission is principled is a judgment I state as my reading while naming the interpretation that would disagree.

**Tension 3: Investigatory orientation's "don't close prematurely" vs the task spec's "direct verdict on LQ-1A.1 — don't hedge."**

The task spec specifically said the LQ-1A.1 verdict should not hedge. But the investigatory orientation says competing interpretations should not be collapsed without ruling out the alternatives. I resolved this by issuing a direct verdict ("recent earned convergence stapled onto older repeated assumption, with the earned part one day old and untested") rather than a hedged one, while naming the specific test that would settle whether Interpretation A or Interpretation B is correct (the rerun of `discuss-phase` for Phase 01). A verdict can be direct and still be qualified by the test that would confirm or disconfirm it.

## What Remains Unknown

- **Whether the rerun of `discuss-phase` for Phase 01** (`STATE.md:68`) will surface canon inadequacies that the narrow initiative's exclusion list assumes do not exist. This is the first test of the one-day-old convergence and it has not happened.
- **Whether Phase 01 will actually close the venue identity and reference-shape decisions** (G1/G2) that the canon delegated to it. The narrow initiative's in-scope list at `README.md:52-56` owns them but the Phase 01 context document does not close them either. If both the narrow initiative and Phase 01 planning leave them delegated to the other, they will be un-owned.
- **Whether the authoring-sustainability risk** (ranked #1 by both predecessor passes) has any other home I did not find. I searched PROJECT.md, ROADMAP.md, LONG-ARC.md, REQUIREMENTS.md, 01-CONTEXT.md for "authoring sustainability," "author workload," "corpus critical mass," "authoring pain." Nothing at the canon level. Phase 6 calibration implicitly touches the response side (evidence to improve rounds) but not the risk side (initial corpus never gets written). If I missed a section that names this risk, I missed it.
- **Whether Lane 1B's methodological-inheritance comparison with f1-modeling** will show that prix-guesser's `RESEARCH-PRINCIPLES.md` and `vision-alignment-2026-04/PLAN.md` discipline inherits or diverges from f1-modeling's in ways that bear on the "already aligned" claim.
- **Whether Lane 1C's external gap research** will surface alternatives that neither the predecessor audit nor the canon considered — especially around the F1-GeoGuessr-vs-Jackbox identity question which neither pass directly closed.

## I4 — Position Of The Investigation

I am Claude Opus 4.6, running as `gsdr-auditor`, dispatched by an orchestrator that is also Opus 4.6 in a claude-code session where the user has stated a stance: "not convinced by momentum/time-pressure arguments; consider deployment/distribution/adoption broadly." I should name, concretely, what that shapes.

**What the Opus-on-Opus self-dispatch is prepared to notice:**

- Surface drift and loose ends (Opus's characteristic reading posture per the predecessor's "Character note" at SYNTHESIS.md:55 — "Opus reads for surface specifics").
- Semantic inconsistencies between documents (I surfaced the PROJECT.md:163-165 "leaning" vs ROADMAP.md:4 "commits" divergence in LQ-1A.1).
- Frames presented as neutral that smuggle a position (I surfaced the watchability constituent-parts decomposition as operationalization-adjacent but not operationalized in REV-3).
- Cases where a recommendation's shape was softened (REV-2, REV-9) — I am attuned to softening because the predecessor audit was Opus-flavored and I can recognize Opus's failure modes.

**What the Opus-on-Opus self-dispatch is *not* prepared to notice:**

- **Structural-contract gaps of the sort GPT 5.4 surfaced in the predecessor audit** (G1/G2/G3/G4). I noticed these only because the predecessor wrote them down — I am re-verifying them, not re-discovering them. If the canon had introduced a new structural-contract gap between 2026-04-08 and 2026-04-11 that neither the predecessor nor my re-verification reading would flag, I would miss it. **A separate Codex GPT-5.4 audit pass on the current canon would probably find at least one structural-contract gap that this report does not.** This is not a hypothetical — the predecessor audit is direct evidence that Opus under-reads structural-contract gaps compared to GPT.
- **Adoption/distribution arguments whose weight scales with *what the user didn't say*.** The user's stance was "consider deployment/distribution/adoption broadly." I am reading that as "the canon should own these broadly." A differently-trained reader might read it as "the canon is wrong to defer these" — a stronger claim. My framing is softer than an adversarial reading would be.
- **The sunk-cost of the refresh work.** The canon refresh on 2026-04-11 was substantial work by the user one day before this audit runs. My posture is attuned to surfacing what the refresh did not do, but I am also susceptible to under-weighting findings that would implicitly recommend *more* refresh work, because the refresh already happened. An adversarial human reviewer would be more willing to call for re-refresh than I am.
- **The gap between "the canon is aware of the tension" and "the canon has closed the tension."** I am treating the awareness as a meaningful move (LQ-1A.1 Identity-A-vs-Identity-B is a clear example). A harder reviewer would say awareness is just deferral-dressed-up.

**What a separate audit by Codex GPT-5.4 would notice differently:** it would probably find at least one structural contract gap in Phase 01 context or research I did not flag; it would probably be harder on the absent component-inventory in Phase 3.1 (REV-7); it would probably name the `DEPLOY-02` coupling to a `party-up.sh` pattern as a loose end more explicitly than I did.

**What an adversarial human reviewer would notice differently:** they would probably push harder on whether the "narrow initiative" framing is itself a way of not doing the refresh work the canon needs; they would probably push harder on the authoring-sustainability risk being absent from the canon; they would probably push back on the Phase 3.1 "watchability operationalization will happen in Phase 3.1" deferral as unaccountable.

## Framework Invisibility

The lane is framed around "verify the predecessor's claims and the narrow initiative's claims." This framing makes invisible: **claims neither the predecessor nor the narrow initiative made about the canon, but that a close reading of the canon would surface.** I looked for one, actively. The one I found:

**The canon does not own the authoring-sustainability risk anywhere, despite the predecessor audit ranking it #1 in both passes.** This is a finding that:
- The predecessor audit *mentioned* but did not frame as a canon-level concern (it framed it as a "biggest risks to project success" item in Lane 4).
- The narrow initiative *silently excludes* via the "in-app authoring UI" out-of-scope item.
- Neither predecessor nor narrow initiative treats as a claim the canon *should* address.
- Is visible if and only if you read PROJECT.md, LONG-ARC.md, ROADMAP.md, and REQUIREMENTS.md looking for a home for "corpus never reaches critical mass" and find none.

This finding would not appear if I had restricted myself to "does the canon address the predecessor's stated recommendations?" — because the predecessor did not state this as a canon-level recommendation. It would also not appear if I had restricted myself to "does the canon deliver on the narrow initiative's scope?" — because the narrow initiative does not scope this. It appears only when the investigation treats the canon as *itself auditable* rather than as a fixed reference point against which the predecessor and the narrow initiative are compared.

**A second framework-invisible finding that I will flag as a candidate:** the `DEPLOY-02` requirement at `REQUIREMENTS.md:62-63` names "the current deployment mode" as a given. The system assumes there is always "a current deployment mode" — but in a local-first private-only project, the operator may start a session without having first chosen a deployment mode. This is a concept gap in the requirements, not a recommendation gap from the predecessor.

## Cross-Lane Notes For The Synthesizer

- **For Lane 1B (methodological inheritance):** my REV-3 finding about watchability being deferred to Phase 3.1 is dependent on whether Phase 3.1 has the methodological affordance to actually close the operationalization. If Lane 1B finds that f1-modeling's vision-alignment discipline produces concrete operationalization at this level and prix-guesser's does not, the REV-3 deferral reading should be downgraded from "principled deferral" to "deferral without affordance."
- **For Lane 1B:** my LQ-1A.1 verdict ("recent earned convergence, one day old, untested") is partially a *methodological* claim — the convergence is in documents but has not been tested by a planning cycle. If Lane 1B can compare this to how f1-modeling's convergence was tested, that comparison is directly relevant.
- **For Lane 1C (external gap research):** my REV-5 finding on the F1-GeoGuessr-vs-Jackbox identity question is a case where the canon holds a tension visible without closing it. Lane 1C's external gap research on "alternatives prix-guesser did not consider" should look at whether there are content-substrate design patterns (authoring workflows, pack shapes, round composability idioms) that *resolve* the Identity-A-vs-Identity-B tension without forcing an either/or choice. If such patterns exist and are known to adjacent projects, the canon's third option ("hold the tension, protect the seams") might be under-informed.
- **For Lane 1C:** my framework-invisible finding about authoring-sustainability is precisely the kind of risk that adjacent projects (GeoGuessr-like games, Jackbox-like party games, authored-content platforms) have presumably hit and solved or failed. External gap research on what those projects did with their authoring pipelines would directly inform whether this is a real canon gap or a well-understood risk that the project can safely delegate.
- **Deduplication note for synthesizer:** I did not cover the f1-modeling comparison (Lane 1B's job) or the external-alternatives research (Lane 1C's job). I did cover the predecessor audit's methodology review (`METHODOLOGY-REVIEW.md`), which is related to but distinct from Lane 1B's methodological-inheritance scope; Lane 1B should feel free to also cite METHODOLOGY-REVIEW.md if helpful.

## Candidates For Wave 2 Follow-Up

If Review Gate 1 decides a Wave 2 pass is warranted, these are the questions this lane raised that it could not answer:

1. **Is the authoring-sustainability risk genuinely absent from the canon, or does it live somewhere I did not look?** Candidate audit shape: `claim_integrity × standard × self` targeting PROJECT.md, LONG-ARC.md, Phase 1/2/6 contexts, research/PITFALLS.md specifically for "authoring" and "corpus" terms. If still absent, propose a canon-level addition.

2. **Does the Phase 3.1 deliverable list need the component inventory imported from the predecessor audit, or does the canon's abstraction level (visual direction, motion grammar, states) cover the operational intent?** Candidate audit shape: `phase_verification × standard × self` on the Phase 3.1 success criteria to test whether a Phase 3.1 planner could produce a usable UI-SPEC.md from the current criteria alone.

3. **Does the `DEPLOY-02` requirement need an explicit operator-script pattern (the `party-up.sh`/`party-down.sh` shape) as a canonical deliverable, or is the requirement honest as written?** Candidate: targeted `requirements_review × investigatory × self` on DEPLOY-01..05 as a cluster.

4. **Does the "Identity A vs Identity B" tension need to be closed explicitly in the canon before Phase 01 planning, or is the "hold the tension, protect the seams" third option sustainable?** Candidate: cross-lane dependency — probably best resolved by Lane 1C's external gap research plus a synthesis pass, not by a separate audit.

5. **Does the "hosted game built by a developer" framing need to be imported into PROJECT.md as an explicit stakeholder-orientation test, or is the browser-first / DEPLOY-* adoption a sufficient substitute?** This is Outcome 3 in my ledger but it is the one I am least confident in. A Codex GPT-5.4 pass might surface evidence I cannot see from my framing.

6. **Does the rerun of `discuss-phase` for Phase 01** actually test the one-day-old convergence, or does it inherit the convergence without testing it? The rerun is pending per `STATE.md:68`; the result of the rerun would be a natural Wave 2 input.

## What The Obligations Didn't Capture

The obligations covered a lot. Three findings exceeded them:

1. **The canon-refresh justification document is itself a predecessor-like document that the chain integrity obligation did not explicitly name.** The obligation named the 2026-04-08 audit as the predecessor. But `canon-refresh-change-justification.md` is a *reconstructed* predecessor — it claims to narrate a refresh that already happened, it was written after the refresh not during it (`line 20: "It should have been logged incrementally while the edits were being made. It was not"`), and it is self-admittedly a best-effort reconstruction. The chain integrity obligation is sized for audit-to-audit inheritance; it does not name "the canon's own self-reconstruction" as an intermediate link in the chain. In this audit, that intermediate link was load-bearing for REV-2 — without the refresh log's claim that the "hosted game" framing influenced the refresh, I would not have had a specific claim to re-verify. A more general version of chain integrity would say: *any document that narrates the provenance of the canon is a chain link and must be re-verified against the canon itself*.

2. **The temporal gap between "canon refresh completed" and "first planning cycle that tests it" is a kind of integrity condition the obligations do not name.** A document state can be internally consistent, chain-integrity-clean, and still be provisional in a way that audits cannot see from a static read. My LQ-1A.1 verdict landed on "earned convergence, one day old, untested," and that "untested" qualifier is real but it does not fit any obligation — it is a property of when an investigation runs relative to the thing it investigates, not a property of the investigation's method.

3. **The friends-only fan-project scope is a contextual modifier that tensions against chain integrity's "re-verify each recommendation" obligation in a way the composition principle only partially handles.** Several predecessor recommendations (REV-2, REV-4, REV-5) were softened by the canon in ways that are principled *if and only if* the project stays friends-only. The obligations let me name this tension but do not give me a way to encode "the principledness is conditional on scope staying what it is" as a structured finding. Re-scope changes (unlisted surfaces, share-by-link, etc.) would un-soften the softening without giving the canon a mechanism to notice. This is a kind of finding that would ideally propagate forward as a conditional commitment, but the audit vocabulary I have does not distinguish "softened-with-condition" from "softened."

## Rule 5 — Frame-Reflexivity (Full Section)

### "If this lane had been classified as a different subject (e.g., `requirements_review` instead of `claim_integrity`, or `artifact_analysis` instead of `claim_integrity`), what would it have looked for that I didn't?"

**Under `requirements_review`:** the lane would have looked for unspecified requirements, negative-space requirements (what should be in REQUIREMENTS.md that is not), and requirement-to-phase traceability gaps. Concrete findings this framing would have surfaced and this claim_integrity framing did not:

- The `DIST-01`/`DIST-02` requirements at REQUIREMENTS.md:111-117 exist in v2 with no criteria for when they become v1. A `requirements_review` audit would have asked: what test moves DIST-01 from v2 to v1, and is that test anywhere in the canon? It is not. This is a readiness-trigger gap that I noticed peripherally but did not frame as a finding.
- The `OPS-V2-*` authoring-tool requirements would have been scrutinized for whether they address the #1 authoring-sustainability risk I flagged in LQ-1A.3. They do not — they are about tooling ergonomics, not about sustainability measurement. I touched this but did not pursue it because claim_integrity directed my attention at claims rather than requirements-shape.

**Under `artifact_analysis`:** the lane would have read each canon document as a *standalone artifact* with its own coherence, conventions, and quality. Concrete findings this framing would have surfaced:

- `PROJECT.md`'s "Evolution" section at lines 175-186 describes a phase-transition update protocol that has not been exercised — the canon is about to go into Phase 01 execution and this protocol has never run in real conditions. An artifact_analysis audit would have asked: can the document actually evolve as promised, or is the evolution section itself un-stress-tested? I did not examine this.
- The "Open Questions" table at `PROJECT.md:163-171` mixes criticality levels (2 Critical, 3 Medium) with status styles (2 "Leaning," 3 "Pending") in a way that does not make it obvious which questions are actually blocking. An artifact-quality read would have flagged the inconsistent status vocabulary. I read the table as content, not as form.

### "If this lane had been classified with a different orientation (e.g., `standard` instead of `investigatory`), what would it have held open that I closed?"

**Under `standard` orientation:** the lane would close on a verdict (pass/fail/defer) and would be pressured to convert my LQ-1A.1 finding into a go/no-go for the narrow initiative.

- Under `standard`, I would have had to answer: "should Phase 01 proceed after the narrow initiative completes?" The investigatory frame let me leave this open (the rerun of `discuss-phase` is the test, and it hasn't happened). A standard frame would have forced me to recommend either "proceed" or "do the rerun first."
- Under `standard`, the REV-2 finding about the stakeholder-orientation framing would have been either closed as "adequately addressed" or as "gap to fix." The investigatory frame let me hold it in three interpretations and flag it as contestable. A standard frame would have forced a collapse.
- The risk of `standard` orientation here is real: the canon genuinely is in a state where a pass/fail verdict would over-resolve the situation. But the risk of `investigatory` orientation is also real: I can leave enough open that Review Gate 1 has too many contingencies to choose between. The investigatory framing's cost is that it trusts Review Gate 1 to actually choose.

### "What about the current classification shapes what I am prepared to notice and what I am not? Name one concrete example."

**claim_integrity × investigatory shapes me toward re-verifying named claims** — I am *best* at taking a claim the predecessor or the narrow initiative stated, reading the cited source, and saying whether the reading still holds. This is visible in my REV-* ledger, which has 12 entries, each tied to a specific stated claim.

**It shapes me away from noticing *unnamed* claims that the canon implicitly makes but does not state**. Concrete example: `REQUIREMENTS.md:111-117` (v2 DIST-* section) makes the implicit claim that "v2 will want remote-host access and always-on private-host mode." This is not verified against anything. No research document or audit document is cited as grounding. My framing treated it as "out of scope for my audit" because neither the predecessor nor the narrow initiative made a claim about it. But DIST-01's existence is itself a claim that v2 will look a certain way, and a reader who asks "is this v2 shape earned or assumed?" would find it assumed — there is no research wave, audit finding, or stated reasoning behind DIST-01 that I can cite.

The investigatory orientation encouraged me to let the investigation drift toward underexplored territory but the claim_integrity subject pulled me back toward claims-already-named. The tension between subject and orientation *should* be generative here, and the most honest thing I can say is that I let subject win on at least the DIST-* example. A lane classified as `requirements_review × investigatory × self` would have pursued this farther than I did.

### Anti-performativity note

This Rule 5 section has three specific answers with specific textual consequences, not a generic "I noticed my biases." Each of the three answers names a finding the current classification did not produce but a nearby classification would have. If this section is empty or rhetorical on a re-read, the ground rules were under-engaged. I have named the DIST-* under-investigation, the PROJECT.md evolution-section stress-test gap, and the authoring-sustainability gap's residue as concrete consequences. Whether that residue is enough is itself a Rule-5-checkable question: the excess section above names the same authoring-sustainability gap, which means the framework-invisibility obligation and the Rule-5 obligation are converging on the same finding from different directions. That convergence is weak evidence that the finding is real and the framing is doing its job.

---

*End of Wave 1 / Lane 1A output. This report is consumed by the Wave 3 synthesis pass and possibly by Review Gate 1. Its findings should be composed with Lane 1B (methodological inheritance) and Lane 1C (external gap research) outputs, not read in isolation.*
