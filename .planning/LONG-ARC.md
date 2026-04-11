---
document: LONG-ARC
created: 2026-04-11
status: canonical
type: strategy-doctrine
scope: Durable long-arc product, transition, visibility, hosting, and support doctrine that current planning should preserve without widening Milestone 1 scope.
related_documents:
  - .planning/PROJECT.md
  - .planning/ROADMAP.md
  - .planning/REQUIREMENTS.md
  - .planning/STATE.md
  - .planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md
  - .planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md
---

# Long-Arc Strategy Doctrine

## Why This Exists

Prix Guesser already has real future-aware thinking, but that thinking has been spread across canon docs, audits, research findings, and exploration logs. This file exists to ratify the durable parts of that thinking in one place so downstream discussion, research, and planning do not depend on remembering which exploratory document mattered last.

This is not a second roadmap and not a back door for importing Milestone 2 or Milestone 3 scope into current work. It is the doctrine layer that explains what the project is trying to preserve while it proves the first real product center.

## Current Product Center

The current product center is a private, watchable, host-led, browser-first F1 game-night ritual for trusted groups. The emotional center is not generic geography play and not ambient public discovery. It is a socially legible shared-screen experience where knowledgeable fans identify circuits and venues, react to reveals, and replay because the round design and reveal grammar feel authored and sport-specific.

That center implies several present-tense truths:

- private-room use is the primary posture
- host-screen clarity and reveal payoff matter as much as raw solver challenge
- browser-first participation matters for guests whether the operator is local, on a LAN, or on a privately hosted remote box
- authored rounds and curated packs matter more than broad scale or procedural novelty

## Mature Product Hypothesis

The mature shape is best understood as one authored F1 substrate plus multiple possible wrappers, not as one frozen app shape. The substrate is the durable center: authored round data, answer-target relationships, judging, reveal logic, session state, and content operations that can survive wrapper changes.

Possible wrappers stay explicitly alive but uncommitted:

- async challenge
- solo support shell
- spectator or streamer-adjacent shell
- broader F1 party platform expansion

Some later surfaces may be true wrappers on the same substrate. Others may become sibling products that share theme, audience, or portions of the authored stack more than they share one exact session shell. This doctrine keeps those futures visible without pretending they are all equally likely or equally imminent.

## Milestone Arc

Milestone 1 proves that the private ritual works. It proves one authored geography-and-circuit anchor mode inside one watchable private-room wrapper. It protects later wrappers by keeping the substrate and seams reusable, but it does not import those later wrappers into current scope.

Milestone 2, if earned, broadens the same substrate into play-anytime surfaces: more durable remote access, lightweight persistence, content operations maturity, and wrapper experiments such as solo or async. That milestone is about proving reuse and durability, not about acting public by default.

Milestone 3, if earned, is where broader party-platform expansion becomes legitimate: adjacent mode families, richer room roles, and showcase or spectator-facing shells. That remains conditional on the substrate proving itself first.

The governing rule across all three milestones is simple: preserve future seams early when cheap, but earn each wrapper before treating it as active product scope.

## Transition Doctrine

Transition should be staged by product surface and obligation threshold, not by one binary jump from private to public. Visibility state, hosting shape, and support promises are separate axes and should remain separate in planning.

The doctrine is:

- preserve the authored substrate first
- move from trusted private rooms to broader visibility only when the project intentionally accepts the next obligation level
- treat publicness as a trust and accountability change, not merely a traffic change

This means Milestone 1 planning should actively avoid smuggling in public-live participation, broad discovery, monetized guarantees, or governance assumptions just because later transitions are visible. It also means current work should not hardcode the first room wrapper so tightly that later wrappers require a second product core.

## Visibility And Discovery Ladder

Visibility and discovery are staged and surface-specific. They should not be flattened into a single "private now, public later" slogan.

The current ladder is:

1. trusted private rooms
2. unlisted or share-by-link surfaces where the audience is still intentionally bounded
3. selectively visible challenge, showcase, or spectator surfaces with narrower interaction rights than full public participation
4. broader public discovery only when moderation, trust language, status communication, and service obligations are accepted deliberately

Different later surfaces may enter this ladder at different levels. A public read or showcase surface is not the same decision as public live participation. A challenge link is not the same decision as stranger-join rooms. Planning should preserve those distinctions instead of collapsing them into one "publicness" switch.

## Hosting And Scaling Ladder

Self-hostable authoritative rooms are the primary branch to preserve. The preferred ladder is:

1. local or LAN operator flow
2. privately hosted remote rooms with standard browser access
3. modest hosted operation if the project later needs easier remote coordination

This doctrine treats browser-first guest access as non-negotiable across the ladder. Guests should not need developer tooling, source checkout, or operator networking software just to join a room.

Full peer-to-peer room authority is not the primary path. It adds trust, authority, reconnect, and operational complexity in the wrong place for this project. Cooperative scaling may matter later, but the main branch worth protecting is authoritative rooms that can be self-hosted and packaged cleanly.

## Support, Access, And Contribution Doctrine

Support, access, and service obligation are distinct concepts.

Support means voluntary backing, donations, or goodwill from people who value the project. Access means who can use which surface under which visibility state. Service obligation means what uptime, reliability, moderation, and response promises the project is actually making.

The current doctrine is:

- optional support can exist without changing room access or service promises
- trusted private access can exist without public discovery
- paid guaranteed access is a later-stage posture, not a Milestone 1 or default Milestone 2 assumption
- contribution and sharing questions should be staged carefully and should not silently imply open publishing or community governance

This separation matters because it prevents premature commercialization logic and premature public-platform behavior from leaking into early architecture.

## Streamer And Spectator Doctrine

Streamer-friendliness first means watchability, role clarity, code safety, and spectator seams. It does not mean optimizing Milestone 1 around public broadcast culture.

The project should preserve the ability to support later streamer-adjacent or spectator-facing shells by making the host screen legible, reveal pacing strong, roles clear, and session state reusable. That is enough for now. Public spectator participation, open showcases, and broad creator ecosystems remain separate future decisions.

In practice, "spectator-friendly" at this stage means the private room is enjoyable to watch, easy to follow, and safe to expose selectively later if the project chooses to build that shell.

## Protected Bets For This Milestone

Milestone 1 should actively protect these bets:

- the authored substrate is more important than premature wrapper variety
- watchable private-room play is the strongest first proof
- browser-first guest participation should survive across local, LAN, and privately hosted remote operation
- visibility state should stay explicit rather than being implied by transport or deployment
- self-hostable authoritative rooms are the correct durability seam
- judging, reveal, room authority, and presentation should stay separable where practical

These are protected bets, not promises that every future surface will be built. They define what current work should avoid foreclosing.

## Explicit Deferrals

The following remain deferred and should not be imported into current planning as if they were already chosen:

- public live participation
- paid guaranteed access
- open creator marketplace or broad public publishing
- broad community-host governance
- full peer-to-peer room authority as the main branch
- adjacent non-anchor F1 party modes before the anchor loop is proven

These deferrals do not mean "never." They mean the project has not earned the obligations and tradeoffs those choices would impose.

## What Changes Would Reopen This Doctrine

This doctrine should be revisited only if the product center or obligation profile materially changes. Examples:

- real playtesting shows the private watchable ritual is not the strongest center after all
- the project deliberately chooses a visibility state beyond trusted private or unlisted sharing
- operational reality makes self-hostable authoritative rooms untenable
- a later wrapper proves so central that the milestone arc itself should be reframed
- support, access, or service promises change enough that the present doctrine would mislead planning

Until one of those changes happens, downstream discuss, research, and planning should treat this file as the durable long-arc doctrine rather than re-litigating it phase by phase.
