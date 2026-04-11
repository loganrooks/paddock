# Canonical Artifacts And Lightweight Doc Levers

## 1. Scope and sources

This memo only examines canonical planning artifacts and the lightest doc-layer steering levers already visible in the repo. It does not inspect the full repo-local GSD harness.

Primary sources read:

- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md:14-20,107-117,123-156`
- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINTS/10-handoff-for-future-awareness-harness-inquiry.md:34-55,57-82,104-115`
- `.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:92-143,145-212,231-250`
- `AGENTS.md:15-18,42-50,51-57`
- `.planning/PROJECT.md:5-7,21-25,34-56,67-98`
- `.planning/ROADMAP.md:5-11,31-111`
- `.planning/REQUIREMENTS.md:6-99`
- `.planning/STATE.md:54-78`
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md:5-11,93-141,151-152`

## 2. Current leverage already present in canonical artifacts

There is already meaningful leverage in the current docs. The issue is less "nothing exists" and more "the signals are distributed and partly non-operationalized."

What is already present:

- `PROJECT.md` already carries the broad long-arc product posture. It explicitly keeps room for broader F1 party-game expansion while holding the current center on private expert-fan play, authored rounds, and host-screen-friendly social shape (`.planning/PROJECT.md:5-7`, `.planning/PROJECT.md:21-25`, `.planning/PROJECT.md:38-56`, `.planning/PROJECT.md:69-75`).
- `PROJECT.md` also already preserves several non-foreclosure decisions and open questions. In particular, it keeps the room/backend choice open, preserves adjacent-mode expansion as a possibility, and asks how much future non-geography party modes should influence v1 architecture (`.planning/PROJECT.md:81-86`, `.planning/PROJECT.md:92-98`).
- `ROADMAP.md` already encodes staged proof logic rather than a flat feature backlog. It says v1 proves one authored anchor mode plus one strong private-room wrapper, while keeping runtime choice and broader mode expansion open (`.planning/ROADMAP.md:5-11`).
- `ROADMAP.md` phase goals and success criteria already do some future-protective work. Phase 1 protects fallback media strategy and explicit answer surfaces; later phases deliberately sequence authority, controller UX, watchability, calibration, and durability rather than collapsing them into one launch (`.planning/ROADMAP.md:31-111`).
- `REQUIREMENTS.md` is already disciplined about present-tense obligations versus later possibilities. v1 focuses on concrete room, content, and watchability requirements, while v2 keeps finer answer surfaces, wrappers, adjacent modes, and recurring/public-facing features separate (`.planning/REQUIREMENTS.md:6-87`).
- `REQUIREMENTS.md` out-of-scope notes already carry some future-awareness by explicitly deferring public matchmaking, public UGC, and commercial/public hardening (`.planning/REQUIREMENTS.md:89-99`).
- `STATE.md` already preserves a small amount of future-aware execution context by surfacing decisions and concerns that should continue steering upcoming phases, especially around answer surfaces, room-runtime choice, watchability, and not widening v1 too early (`.planning/STATE.md:54-72`).
- The local `CONTEXT.md` template is already the strongest doc-layer steering lever. It explicitly tells downstream agents that `future_awareness` matters, and it pairs that with `canonical_refs`, `derived_constraints`, `open_questions`, `epistemic_guardrails`, and `deferred` sections (`tooling/portable-gsd/overlay/get-shit-done/templates/context.md:5-11`, `tooling/portable-gsd/overlay/get-shit-done/templates/context.md:93-141`, `tooling/portable-gsd/overlay/get-shit-done/templates/context.md:151-152`).
- `AGENTS.md` reinforces that this repo expects `CONTEXT.md` to be a steering brief, not a throwaway note, and says future awareness should matter downstream (`AGENTS.md:15-18`, `AGENTS.md:42-50`, `AGENTS.md:51-57`).

What is implied but not fully encoded:

- The exploration materials now imply that future-awareness should mean specific concepts such as visibility state, wrapper type, trust boundary, and service obligation, not just generic "keep options open" language (`.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:145-184`).
- The exploration also implies the canonical split should be: `PROJECT.md` for long-arc thesis, `ROADMAP.md` for staged proofs and protected futures, `REQUIREMENTS.md` for current obligations, and `CONTEXT.md` for active steering (`.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:98-143`).

## 3. Gaps or mismatches in the doc layer

The main gap is not absence of future-aware intent. It is that the current docs do not yet name or normalize the exact future-aware concepts that the latest exploration says matter.

What is missing:

- `PROJECT.md` preserves expansion room, but it still describes the future mostly in broad terms like "broader F1-flavored party game" or "wrappers." It does not yet distinguish wrapper vs stage-shape vs sibling product, even though the exploration now says that distinction matters (`.planning/PROJECT.md:5-7`, `.planning/PROJECT.md:49`, `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md:134-146`).
- `ROADMAP.md` already stages proofs, but it does not systematically record for each phase:
  - what future it protects
  - what it explicitly refuses to decide yet
  - what visibility / trust / service-obligation posture it assumes
  This is a direct mismatch with the current exploration guidance (`.planning/ROADMAP.md:31-111`, `.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:108-118`, `.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:186-201`).
- `REQUIREMENTS.md` cleanly separates v1 from v2, but it does not yet have a place for "protected seams" or "explicitly deferred but important not to foreclose" items. That means the file can express present obligations and later wish-list items, but not the middle category the reflections call out (`.planning/REQUIREMENTS.md:6-87`, `.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:203-212`).
- `STATE.md` is weak as a preservation layer for this problem. It records current concerns, but it is execution-status oriented and too ephemeral to carry nuanced future posture reliably (`.planning/STATE.md:17-78`).
- The `CONTEXT.md` template already has the right slots, but the caution in the handoff is valid: a `Future Awareness` section alone does not guarantee downstream use. At the doc layer, this means the template has leverage, but only if canonical docs give it sharper content to point at (`tooling/portable-gsd/overlay/get-shit-done/templates/context.md:125-141`, `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINTS/10-handoff-for-future-awareness-harness-inquiry.md:57-72`).

What is mismatched:

- The exploration checkpoint says future-aware planning should be encoded with "low-drag fields and checks" (`.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md:123-130`), but the current canonical docs mostly rely on prose interpretation rather than repeatable headings or fields.
- The reflection note argues research artifacts should remain inputs to canonical revision, not canonical law (`.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:135-143`). Right now, some of the freshest future-aware distinctions live only in exploration notes, not in the canonical docs that planners are more likely to rely on.

## 4. Minimal doc-layer changes that would meaningfully help

The highest-value minimal change is a layered one, still entirely in docs:

1. Tighten `PROJECT.md` so the long-arc thesis names the currently live future categories.
   Add a short subsection under `Context` or `Constraints` that says the product may evolve through:
   - wrappers on the shared substrate
   - stage-shape changes to the private room ritual
   - sibling public-facing surfaces
   Also name current non-decisions around visibility/publicness and trust boundary. This would move those distinctions from exploration prose into canonical posture without turning them into immediate requirements.

2. Add one compact future-proofing field to each roadmap phase.
   In `.planning/ROADMAP.md`, each phase could gain a small block such as:
   - `Protects:` [future seams preserved]
   - `Does not decide yet:` [explicit deferrals]
   - `Assumed posture:` [visibility / trust / service level]
   This is the most direct doc-layer answer to the reflections note's recommendation for staged proofs and protected futures (`.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:108-118`).

3. Add a small non-requirements classification to `REQUIREMENTS.md`.
   Keep v1 and v2 requirements, but add one short section such as `Protected Seams And Explicit Deferrals`. That gives canonical space for things that must remain architecturally possible or intentionally postponed without pretending they are in-scope build targets now.

4. Keep `STATE.md` light.
   Do not promote `STATE.md` into the main future-awareness carrier. At most, keep a short pointer to the relevant canonical posture and current deferrals. This file is not the right home for nuanced product-boundary reasoning.

5. Use the existing `CONTEXT.md` template as the bridge, not the source of truth.
   The template already has the right slots. The minimal doc-layer move is to make the canonical artifacts sharper so future phase contexts can cite them directly in `canonical_refs` and restate them in `future_awareness` and `deferred` sections.

## 5. Limits of doc-only changes

Doc-only changes can improve preservation, but they cannot guarantee operational attention.

- The handoff explicitly warns that template changes alone may not be enough if planner and researcher prompts do not actually look for and use those sections (`.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINTS/10-handoff-for-future-awareness-harness-inquiry.md:57-72`).
- The current docs can tell a careful human or agent what matters, but they cannot enforce that downstream planning asks the right questions about visibility state, trust boundary, or protected seams.
- Because `CONTEXT.md` is the active steering layer, doc-only changes work best when they sharpen what should be written there, not when they are expected to replace downstream prompt behavior.
- Exploration artifacts are still needed as pressure tests and reframing tools. Canonical docs should absorb the stable conclusions, but they should not try to encode all the nuance or debate history (`.planning/explore/2026-04-10-vision-future-hosting/08-reflections-on-research-implications-2026-04-10-2021-EDT.md:135-143`).

## 6. Recommendation

The current canonical artifacts already provide enough leverage for a minimal layered solution. They do not justify a docs-only verdict of "nothing exists, patch the harness first."

Recommended judgment:

- Already present: strong long-arc posture in `PROJECT.md`, staged sequencing in `ROADMAP.md`, disciplined concrete obligations in `REQUIREMENTS.md`, and a surprisingly capable `CONTEXT.md` steering template.
- Missing: normalized canonical language for protected futures, explicit non-decisions, visibility/trust posture, and the middle category between "requirement now" and "maybe later."
- Minimal change worth making first: refine `PROJECT.md`, `ROADMAP.md`, and `REQUIREMENTS.md` so they express those distinctions explicitly, then let phase `CONTEXT.md` consume them.
- Likely next conclusion after that: prompt-level or harness-level reinforcement may still be needed, but the doc layer should be tightened first because it defines what the harness would be expected to operationalize.

## Changed files

- `.planning/explore/2026-04-10-future-awareness-harness-inquiry/findings/01-canonical-artifacts-and-lightweight-doc-levers.md`
