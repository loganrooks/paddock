---
date: 2026-04-14
audit_subject: external_reference_patterns
audit_orientation: exploratory
audit_delegation: delegated
scope: "Comparative grounding for bounded audience shells, curated contribution posture, support/access obligation transitions, and grassroots hosting ladders"
triggered_by: "05-gap-closure-reference-patterns-task-spec.md"
tags:
  - exploratory-audit
  - gap-closure
  - reference-patterns
  - community
  - support
  - hosting
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-reference-patterns-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-synthesis.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md
---

# 05 Gap Closure Reference Patterns

## Research Frame

- Mode: `terrain mapping`
- Classification: `initial architecture research/planning`
- Question: Which external reference patterns most usefully ground the repo's still-open questions around bounded audience shells, curated contribution posture, support/access/obligation transitions, and grassroots transition hosting?
- Scope: narrow comparative memo for the mature-product closure bundle, especially Lanes C, D, and E
- Non-goals:
  - not a broad market study
  - not a pricing or business-plan recommendation
  - not a legal memo
  - not a blueprint for copying any one product whole
- Stop condition: enough primary or official evidence to describe the major pattern families and the obligations they create

## Traceability And Scope

This memo most directly helps answer these still-open gaps from `05-gap-closure-synthesis.md`:

- `handoff-relative gaps`
  - streamer / spectator growth shape
  - community features beyond gameplay / contribution posture
  - monetization / premium posture
- `emergent audit-revealed gaps`
  - community / public future needs shell ordering and audience-rights posture
  - monetization must be modeled as support / access / service-obligation transitions
  - transition-phase grassroots hosting needs a real ladder, not a binary between solo forever and immediate formal service

Steering local doctrine used as governing input:

- `.planning/PROJECT.md` keeps the center on a watchable private ritual, browser-first join, explicit visibility states, and modest service obligations.
- `.planning/LONG-ARC.md` separates support, access, and service obligation; keeps streamer/spectator posture as later shells; and treats authoritative self-host/private-host ladders as the main branch worth preserving.
- `.planning/REQUIREMENTS.md` explicitly defers paid guaranteed access, public trust/moderation surfaces, public discovery, and open creator publishing.

## Path Of Inquiry

- Entry point: the reference-patterns task spec plus the gap-closure synthesis
- Branches considered:
  - direct party-game references
  - community-event / spectator-shell references
  - self-hosted software with optional paid convenience
  - ecosystem models with curated contribution rather than open publishing
  - federated or distributed hosting examples
- Branches pursued:
  - `Jackbox` for bounded audience shells around a private host-screen core
  - `Discord Stage Channels` for explicit speaker / moderator / audience rights and the public-obligation step-up
  - `Home Assistant / Nabu Casa` for optional support plus hosted convenience without forcing a public-first product
  - `Foundry VTT` for self-host, partner-hosted, premium-content, and sanctioned-contributor patterns
  - `Mastodon` for community-operated instances, curated server discovery, and the obligations attached to being promoted as a trusted host
- Branches deferred or abandoned:
  - broad creator-platform examples such as Roblox or Steam Workshop because they over-index on open publishing
  - generalized donation platforms such as Patreon/Ko-fi because they are too abstract on their own
  - pure P2P references because the spec explicitly scoped this memo toward authoritative-host ladders instead
- Unexpected branch / reframing:
  - the most useful contribution and hosting references were not direct party-game competitors; they came from software ecosystems that expose their operator and support obligations more plainly

## Assumptions Surfaced

- `[governing]` The repo's private-first center is already decided. This memo is only about later wrappers, support ladders, and transition paths.
- `[assumed:reasoned]` Pattern fit matters more than genre fit. A non-game reference can still be highly relevant if it exposes the same obligation boundary.
- `[assumed:reasoned]` Official product and documentation pages are sufficient for pattern comparison even when they do not expose underlying unit economics.
- `[open]` The exact obligation threshold where a private tool becomes a public service is context-sensitive. The memo can identify boundary signals, not a universal cutoff.

## Option Space

The pursued external terrain clusters into four pattern families:

1. `bounded audience shell` around a private or host-led core
2. `sanctioned contribution + curated discovery` instead of default open publishing
3. `optional support + hosted convenience` as a different rung from paid guaranteed access
4. `grassroots hosting ladder` from personal hardware to managed hosting, with operator burden made explicit

## Evidence Base

### Pattern 1: Audience Shells Wrap The Core Instead Of Replacing It

#### Direct evidence

- Jackbox says its games do not offer online matchmaking; remote play works by screen-sharing the game while players join on their own devices through `jackbox.tv`, and public play is typically done by streaming to Twitch or YouTube. It recommends hiding room codes and using passworded rooms when opening play to the public.  
  Sources: [Can I play Jackbox Games remotely?](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely), [How many players can join each game?](https://support.jackboxgames.com/hc/en-us/articles/15794756085015-How-many-players-can-join-each-game)
- Jackbox's own player-count guide says the vast majority of its games support `Audience`, meaning the audience is an extension around the core player count rather than the primary room model.  
  Source: [How many players can join each game?](https://support.jackboxgames.com/hc/en-us/articles/15794756085015-How-many-players-can-join-each-game)
- Jackbox's public-stream guidance for `The Jackbox Survey Scramble` recommends profanity filtering, moderation, and hiding full answer displays in public streaming contexts.  
  Source: [How To Stream The Jackbox Survey Scramble](https://www.jackboxgames.com/blog/how-to-stream-the-jackbox-survey-scramble)
- Discord Stage Channels are a Community-server-only feature where moderators, speakers, and audience members have distinct rights. Audience members join muted by default, can request to speak, and public Stages create extra moderation and permission obligations.  
  Sources: [Stage Channels FAQ](https://support.discord.com/hc/en-us/articles/1500005513722-Stage-Channels-FAQ), [Stage Channel Guidelines](https://support.discord.com/hc/en-us/articles/1500010879761-Stage-Channel-Guidelines)

#### Inference and interpretation

- What they did: both references made `audience` a separate shell with narrower rights than the core player/speaker role, instead of flattening everyone into one participant class.
- What problem it solved: it lets a watchable room or event absorb extra people without redesigning the core interaction contract around public participation.
- What obligations it created: as soon as the shell becomes public or discoverable, moderation, entry control, code safety, and permission hygiene become first-class operational work.
- What may be relevant here:
  - later spectator or showcase shells should probably be modeled as `audience rights layered around a private room`, not as proof that the product has become public-first
  - audience joins, request-to-speak, and selective visibility are meaningfully different from full participant joins
  - the repo's current doctrine that public-facing shells raise moderation and status obligations is strongly reinforced by these references

### Pattern 2: Sanctioned Contribution And Curated Discovery Sit Between Closed Authorship And Open Publishing

#### Direct evidence

- Foundry says its official marketplace centralizes creators and publishers into one shopping and discovery surface, highlights spotlighted content, and auto-adds marketplace purchases to the buyer's Foundry account.  
  Source: [Foundry Partnerships](https://foundryvtt.com/article/partnerships/)
- Foundry's premium-content docs say products can either go through the official marketplace or remain `external premium content` purchased elsewhere and then activated through a Foundry account, including Patreon-linked access.  
  Source: [Premium Content](https://foundryvtt.com/article/premium-content/)
- Foundry's `Pathfinder Second Edition` system page describes the ruleset as a volunteer-developed project supported by an official partnership with Paizo and Foundry, and published for free with Foundry's endorsement.  
  Source: [Pathfinder Second Edition for Foundry VTT](https://foundryvtt.com/packages/pf2e)
- Mastodon's Server Covenant requires manual submission and review for inclusion in the official server picker, and listed servers must commit to active moderation, daily backups, at least one additional person with emergency access, and advance shutdown notice. Mastodon explicitly moved away from simply listing every submitted server because that produced no quality control.  
  Sources: [Mastodon Server Covenant](https://joinmastodon.org/covenant), [Introducing the Mastodon Server Covenant](https://blog.joinmastodon.org/2019/05/introducing-the-mastodon-server-covenant/)

#### Inference and interpretation

- What they did: both ecosystems kept room for external or volunteer contribution, but treated official discovery, endorsement, or account integration as curated and review-bound.
- What problem it solved: they captured community energy without immediately inheriting the full moderation, quality-control, and trust burden of unrestricted open publishing.
- What obligations it created: staff or trusted-reviewer time, clearer support boundaries, endorsement rules, listing criteria, and explicit removal / exclusion decisions.
- What may be relevant here:
  - the repo does not need to choose between `creator is the only author forever` and `open publishing now`
  - a middle posture is viable: trusted contributors, sanctioned partner authors, curated submissions, or manually reviewed mirrors/surfaces
  - official discovery is itself a promise; the moment the project lists, promotes, or blesses third-party contributions, it inherits quality and trust obligations that should be named explicitly

### Pattern 3: Optional Support And Hosted Convenience Are Distinct From Paid Guaranteed Access

#### Direct evidence

- Nabu Casa markets `Home Assistant Cloud` as remote access, voice-assistant integration, backups, and other extras while also saying the subscription supports Home Assistant development. It explicitly frames the offer as `get the best extras ... while supporting its development`.  
  Source: [Home Assistant Cloud](https://www.nabucasa.com/)
- Nabu Casa publishes explicit recurring subscription pricing by region.  
  Source: [Nabu Casa Pricing](https://www.nabucasa.com/pricing/)
- Home Assistant's own security docs say the easiest path to secure remote access is Home Assistant Cloud, but also document manual alternatives such as VPN, TLS, and SSH tunnels.  
  Source: [Securing Home Assistant](https://www.home-assistant.io/docs/configuration/securing/)
- Nabu Casa will block insecure Home Assistant versions from using Remote UI until users upgrade or manually override the protection at their own risk.  
  Source: [Insecure Home Assistant instance detected](https://www.nabucasa.com/more-info/insecure-instance/)
- Foundry's hosting-partner docs describe managed hosts as a paid convenience on top of the self-hosted product: hosting-partner fees are additional to the one-time Foundry license, and the managed hosts sell always-on availability, backups, storage, and operational convenience.  
  Source: [Foundry Partnerships](https://foundryvtt.com/article/partnerships/)

#### Inference and interpretation

- What they did: they monetized `convenience, persistence, and reduced operator burden` rather than locking the base product behind a mandatory hosted plan.
- What problem it solved: users who value ease, remote access, or always-on availability can pay for those benefits without forcing the whole product into a public-service posture.
- What obligations it created: billing, account support, upgrade/support expectations, backup promises, and in some cases active security policy enforcement.
- What may be relevant here:
  - the repo's doctrine separating `support`, `access`, and `service obligation` is strongly supported by these examples
  - a plausible future ladder is `optional support` -> `hosted convenience` -> `premium content/programming`, with `paid guaranteed access` staying a distinct later rung
  - if the project sells a convenience surface, it should expect more support and incident-response expectations than a pure donation tier would create

### Pattern 4: Grassroots Hosting Works Best As A Ladder, Not A Leap

#### Direct evidence

- Foundry's hosting guide says a game session has one host and several clients; the host does not need to be the GM; hosting can be self-hosted, cloud hosted, or partner hosted; and cloud hosting keeps the world always online for browser access between sessions.  
  Source: [Hosting Options Guide](https://foundryvtt.com/article/hosting/)
- Foundry's requirements page describes distinct requirements for self-hosted, dedicated-server, and partner-hosted setups, and explicitly notes Raspberry Pi dedicated-server support for some models.  
  Source: [Minimum Requirements](https://foundryvtt.com/article/requirements/)
- Mastodon's `Running your own server` docs say an operator can run a personal server, an invite-only family/friends community, or a public server; they also say public internet service involves moderation and community management, and list the domain, VPS, email, and optional object storage needed to operate it. The same docs note that dedicated hosting providers exist for operators who do not want to run the stack themselves.  
  Source: [Running your own server](https://docs.joinmastodon.org/user/run-your-own/)
- Mastodon's backup docs say that for real-world use the server should be backed up regularly and that off-site backups are best practice; the Server Covenant adds daily backups, multi-admin emergency access, and shutdown notice as listing requirements.  
  Sources: [Backing up your server](https://docs.joinmastodon.org/admin/backups/), [Mastodon Server Covenant](https://joinmastodon.org/covenant)

#### Inference and interpretation

- What they did: they exposed a ladder from personal operation to managed operation while making the trade-offs legible instead of pretending all hosting modes are equivalent.
- What problem it solved: communities can distribute cost and operational burden gradually rather than choosing only between `creator runs everything` and `fully centralized service`.
- What obligations it created: more persistence means more backup, failover, succession, support, and incident-response expectations; community-operated or promoted hosts also need trust rules and minimum standards.
- What may be relevant here:
  - the project's likely useful ladder is:
    - creator-hosted private authoritative rooms
    - trusted volunteer authoritative hosts
    - sanctioned mirrors or small host collectives with minimum standards
    - supporter-funded or partner-managed hosted convenience
  - this is materially different from `full peer-to-peer room authority`; the useful comparison is about who runs authoritative rooms and how much install/ops burden shifts
  - browser-first guest simplicity should remain the invariant across the ladder, because every reference that expands host flexibility still tries to keep participant access simple

### Unknowns Across The Evidence Base

- None of the official sources expose enough financial detail to determine which rung is commercially best for this repo.
- These references show obligation boundaries clearly, but they do not settle which later shell should come first after trusted private rooms.
- Community-operated-host examples become public-service-heavy quickly; that strengthens caution, but it does not by itself prove that a tightly bounded private host-collective model would be too costly here.

## Dependencies And Relations

| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Bounded audience shell | explicit visibility states, role separation, code / invite safety | Lane C shell ordering, join-flow design, later spectator surfaces | medium |
| Curated contribution posture | review capacity, IP/licensing posture, endorsement policy | content flywheel, Lane C community surfaces, later discovery surfaces | high |
| Optional support vs hosted convenience | billing/account spine, hosting model, support appetite | Lane D obligation ladder, trust promises, future pricing posture | high |
| Grassroots hosting ladder | authoritative-room model, browser-first guest access, backup / recovery posture | Lane E transition-hosting closure, Phase 3 authority/deploy choices | high |

## Scope Expansions And Deferrals

- `Deferred`: broad open-publishing platforms and marketplace-heavy ecosystems. They were too far from the repo's current deferrals to add clean signal.
- `Deferred`: full peer-to-peer reference study. The current memo only needed authoritative-host ladder grounding.
- `Follow-and-mark`: Mastodon and Home Assistant are outside party games, but they were kept because they expose support, hosting, and curation obligations more directly than most game examples do.

## What Can Close Now

- A `spectator` or `showcase` future should be treated as a separate audience-rights shell around the private core, not as a reason to collapse everyone into one participant role.
- There is a real middle ground between `fully curated internal authorship` and `open creator publishing`: sanctioned contributors, curated listings, and manually reviewed partner surfaces are all viable postures.
- `optional support`, `hosted convenience`, and `paid guaranteed access` are meaningfully different rungs and should stay separate in later closure work.
- `grassroots authoritative hosting` is a legitimate transition family distinct from browser P2P, and it can be reasoned about as a ladder with explicit minimum standards.

## What Must Stay Open

- Which shell should arrive first after trusted private rooms: spectator/showcase, frozen challenge/share-by-link, or something else
- Whether sanctioned mirrors or host collectives are worth the policy and review burden before a simpler hosted-convenience tier
- Exact pricing, packaging, and which benefits, if any, should ever be attached to payment
- The exact contribution workflow, rights model, and vetting standard for non-core authors

## What This Memo Cannot Establish

- It cannot tell the repo which exact later shell should come next; it only shows the pattern families and their obligation gradients.
- It cannot validate the economics of any hosted or premium path.
- It cannot answer the legal or trademark implications of third-party contribution or external hosting.
- It cannot prove that any one reference's scale, audience, or moderation burden maps cleanly onto this project.

## Planning Handoff

- For `Lane C`:
  - treat audience shells as rights and visibility design, not just as feature add-ons
  - assume public discoverability materially changes moderation and safety posture
- For `Lane D`:
  - compare `donation/support`, `hosted convenience`, `premium content/programming`, and `paid guarantees` as distinct rungs
  - do not let support tiers quietly inherit service promises that only make sense for hosted convenience
- For `Lane E`:
  - evaluate a ladder from creator-hosted to trusted-volunteer-hosted to sanctioned collective to managed convenience
  - make backups, emergency access, shutdown posture, and guest-install friction explicit evaluation criteria
- For later synthesis:
  - do not cite these references as blueprints
  - do cite them as evidence that the repo's current separation between private core, bounded shells, support/access/obligation, and curated discovery is a real pattern space rather than a purely internal theory

## Sources

### Local

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-reference-patterns-task-spec.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-synthesis.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/REQUIREMENTS.md`

### External

- Jackbox Games:
  - [Can I play Jackbox Games remotely?](https://support.jackboxgames.com/hc/en-us/articles/15794770038423-Can-I-play-Jackbox-Games-remotely)
  - [How many players can join each game?](https://support.jackboxgames.com/hc/en-us/articles/15794756085015-How-many-players-can-join-each-game)
  - [How To Stream The Jackbox Survey Scramble](https://www.jackboxgames.com/blog/how-to-stream-the-jackbox-survey-scramble)
- Discord:
  - [Stage Channels FAQ](https://support.discord.com/hc/en-us/articles/1500005513722-Stage-Channels-FAQ)
  - [Stage Channel Guidelines](https://support.discord.com/hc/en-us/articles/1500010879761-Stage-Channel-Guidelines)
- Home Assistant / Nabu Casa:
  - [Home Assistant Cloud](https://www.nabucasa.com/)
  - [Nabu Casa Pricing](https://www.nabucasa.com/pricing/)
  - [Securing Home Assistant](https://www.home-assistant.io/docs/configuration/securing/)
  - [Insecure Home Assistant instance detected](https://www.nabucasa.com/more-info/insecure-instance/)
- Foundry Virtual Tabletop:
  - [Hosting Options Guide](https://foundryvtt.com/article/hosting/)
  - [Minimum Requirements](https://foundryvtt.com/article/requirements/)
  - [Premium Content](https://foundryvtt.com/article/premium-content/)
  - [Partnerships](https://foundryvtt.com/article/partnerships/)
  - [Pathfinder Second Edition for Foundry VTT](https://foundryvtt.com/packages/pf2e)
- Mastodon:
  - [Running your own server](https://docs.joinmastodon.org/user/run-your-own/)
  - [Backing up your server](https://docs.joinmastodon.org/admin/backups/)
  - [Mastodon Server Covenant](https://joinmastodon.org/covenant)
  - [Introducing the Mastodon Server Covenant](https://blog.joinmastodon.org/2019/05/introducing-the-mastodon-server-covenant/)
