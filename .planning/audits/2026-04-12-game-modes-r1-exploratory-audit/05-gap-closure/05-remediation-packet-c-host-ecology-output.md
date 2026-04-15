---
date: 2026-04-14
audit_subject: remediation_packet
audit_orientation: exploratory
audit_delegation: self
scope: "Reopen host ecology, transition identity, and promotion thresholds with direct external grounding"
triggered_by: "05-next-round-gap-opportunity-register.md"
tags:
  - exploratory-audit
  - gap-closure
  - remediation
  - host-ecology
  - hosting
  - transition
  - operators
source_artifacts:
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-remediation-packet-c-host-ecology-task-spec.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-remediation-packet-common-scaffold.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-lane-e-grassroots-transition-hosting-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-reference-patterns-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-epistemic-opening-output.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-next-round-gap-opportunity-register.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md
  - /home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md
---

# 05 Remediation Packet C: Host Ecology And Promotion Thresholds

## Packet framing

- Mode: `synthesis`
- Classification: `initial architecture research/planning`
- Question: Which host branches are actually comparable, which solve different transition problems, and what trigger conditions should govern promotion from trusted operators toward sanctioned mirrors / collectives or official hosted convenience?
- Scope:
  - trusted technical supporters running the canonical authoritative bundle
  - sanctioned mirrors / small host collectives
  - official hosted convenience
  - operator burden, host identity, standards, recovery, and promotion thresholds
- Non-goals:
  - not reopening browser P2P as the main branch
  - not deciding a final paid hosting business model
  - not designing legal agreements, pack-signing, or final trust-policy text
  - not ranking public-scale infrastructure strategies
- Stop condition: enough direct external grounding to decide whether these branches belong on one ladder, where they do not, and what concrete conditions would justify promoting or deferring each one

Direct external grounding used here is intentionally narrow and explicit:

- `Foundry VTT` for self-host, cloud-host, partner-host, and shared trusted-host patterns
- `Mastodon` for promoted host standards, metadata, manual review, backup/emergency/shutdown obligations, and the negative case for “list every host”
- `Home Assistant / Nabu Casa` for official hosted convenience, separate service identity, subscription-backed service obligations, and security-enforcement burden

## Gap justification

This packet directly addresses:

- `GCO-00`
- `GCO-07`
- `GCO-08`
- `GCO-08A`
- `GCO-08B`
- `GCO-08C`
- `GCO-09`
- `GCO-09A`
- `GCO-09B`

Why these belong together:

- `GCO-07` is the core host-ecology gap: the prior bundle did not close the comparison between trusted operators, sanctioned mirrors / collectives, and official hosted convenience.
- `GCO-08`, `GCO-08A`, `GCO-08B`, and `GCO-08C` are all the missing comparison discipline around that gap:
  - what counts as a promotion trigger
  - whether these are even one ladder
  - how they vary by archetype
  - what matters first versus later
- `GCO-09`, `GCO-09A`, and `GCO-09B` are required because this packet was explicitly asked to repair grounding quality, make reference translation visible, and sample negative-case/operator-burden evidence.
- `GCO-00` remains relevant because host ecology only becomes planning-grade if its burden is translated through the project’s different archetypes rather than assumed to fit one default user story.

This packet is not trying to close:

- browser P2P as a main branch
- generic large-scale scaling
- final pricing or entitlement design
- public discovery / stranger participation
- exact legal / policy machinery for third-party host agreements

## What is already settled

Direct local evidence:

- The project center remains private-first, watchable, host-led, and browser-first for guests rather than public-first or infra-maximal.
- The long-arc doctrine already preserves self-hostable authoritative rooms as the main branch and keeps full peer-to-peer room authority out of the preferred ladder.
- The current doctrine already separates support, access, and service obligation.

Inference carried forward:

- This packet is not deciding whether authoritative self-host/private-host is still the right core. It is only reopening what kinds of non-solo host ecology can sit on top of that core without smuggling in the wrong product identity.

## Path of inquiry

- Entry point:
  - `05-next-round-gap-opportunity-register.md` explicitly called host ecology under-grounded and required a narrow comparative packet.
- Branches considered:
  - Logan-only authoritative hosting
  - trusted private operators running the same canonical bundle
  - sanctioned mirrors / small host collectives promoted by the project
  - official hosted convenience
  - broader public/community-host ecosystems
- Branches pursued:
  - trusted operators
  - sanctioned mirrors / collectives
  - official hosted convenience
- Branches deferred or abandoned:
  - browser P2P authority as a main answer
  - open federation as a direct product target
  - exact commercialization / tier design
  - detailed trust contracts or legal mechanics
- Reframing:
  - the important question is not `centralized vs decentralized`
  - the important question is `which burden is being relieved, who becomes accountable, and what product identity is created by promoting that host form`

## Direct external source register

| Source | Host family or burden it grounds | Direct evidence used here | Limits |
| --- | --- | --- | --- |
| [Foundry Hosting Options Guide](https://foundryvtt.com/article/hosting/) | trusted operators, cloud-hosted convenience, partner-hosted convenience | self-hosted is cheap but offline when app is closed and may require connectivity setup; cloud and partner hosting make the service always online but add setup cost or vendor fees; hosting can be done by someone other than the GM | TTRPG session hosting is not the same as Prix Guesser room ecology |
| [Foundry FAQ](https://foundryvtt.com/article/faq/) | trusted-circle shared hosting | one license can be used across different hosts so long as only one player-accessible server is active at a time; example includes one friend hosting on Saturdays and another on Wednesdays | license policy is not product doctrine, but it shows a bounded trusted-operator pattern |
| [Foundry Minimum Requirements](https://foundryvtt.com/article/requirements/) | operator burden | dedicated-server hosting still requires explicit runtime, storage, memory, and firewall/network configuration | this is technical burden, not community-governance burden |
| [Foundry Content Packaging Guide](https://foundryvtt.com/article/packaging-guide/) | compatibility discipline | content packages expose explicit `version` and `compatibility` metadata and require testing in clean environments | module packaging is not identical to room-host compatibility, so this is a concern translation rather than a blueprint |
| [Running your own server - Mastodon](https://docs.joinmastodon.org/user/run-your-own/) | host identity, private/invite-only/public host families, public-service burden | server owners can run a personal server, invite-only server, or public server; public service brings moderation and community-management work; managed hosts exist for operators who do not want to run the stack themselves | Mastodon is public/social by default more often than Prix Guesser intends to be |
| [Mastodon Server Covenant](https://joinmastodon.org/covenant) | promoted/sanctioned host standards and promotion thresholds | promoted servers must meet backup, emergency-access, shutdown-notice, metadata, contact, and manual-review requirements; submissions are reviewed manually and unproven servers are not promoted | strongest analogy is promoted host standards, not federation itself |
| [Introducing the Mastodon Server Covenant](https://blog.joinmastodon.org/2019/05/introducing-the-mastodon-server-covenant/) | negative-case evidence for promoted host networks | Mastodon explicitly moved away from automatically listing every submitted server because automated listing gave no quality control and did not serve the project’s goals | public social-network context is heavier than Prix Guesser’s likely private-first posture |
| [Backing up your server - Mastodon](https://docs.joinmastodon.org/admin/backups/) | backup/recovery burden | real-world use requires regular backups; failure modes include total loss of accounts/posts and loss of secrets; off-site backups are recommended | stronger than Prix Guesser’s likely early obligations, but useful for promoted-host thresholds |
| [Setting up your new instance - Mastodon](https://docs.joinmastodon.org/admin/setup/) | host labeling and contact clarity | promoted or legible hosts need contact username, business email, description, and server rules | again, more public than the current product center |
| [Securing - Home Assistant](https://www.home-assistant.io/docs/configuration/securing/) | self-host vs official hosted convenience | the easiest secure remote access is Home Assistant Cloud; manual remote access means TLS/SSL, VPN, or SSH-tunnel setup | device/home-automation context differs from game-night hosting |
| [Do you offer a lifetime subscription or a one time fee?](https://support.nabucasa.com/hc/en-us/articles/26179725282461-Do-you-offer-a-lifetime-subscription-or-a-one-time-fee) | official hosted convenience economics and obligation | Home Assistant Cloud is recurring because it funds ongoing development and stable, reliable service | support article, not an independent business analysis |
| [Cannot login to Home Assistant](https://support.nabucasa.com/hc/en-us/articles/33070434152221-Cannot-login-to-Home-Assistant) | separate service identity | the local Home Assistant login and the Nabu Casa cloud account are distinct and have different functions | strong on identity split, weak on gameplay/community translation |
| [Insecure Home Assistant instance detected](https://www.nabucasa.com/more-info/insecure-instance/) | negative-case/service-enforcement burden | cloud remote access can be blocked when the underlying instance is too insecure/outdated | vendor-specific enforcement pattern |
| [Cancelling the subscription and deleting the account](https://support.nabucasa.com/hc/en-us/articles/26167476727581-Cancelling-the-subscription-and-deleting-the-account) | service-bound convenience and later-value obligations | ending the cloud subscription removes secure remote access and cloud backup | support-service specifics do not transfer 1:1 |

## Reference translation

### Foundry

- What is analogous:
  - one host with many browser clients
  - self-host, cloud-host, and partner-host are explicitly distinct operating modes
  - a trusted non-creator operator can host the canonical software bundle
- What is not analogous:
  - TTRPG campaigns are GM-centric and world-persistent in different ways
  - Foundry licensing and module ecosystem are not Prix Guesser’s product model
- What is borrowed as concern:
  - operator burden differs sharply by self-host / cloud / partner host
  - “someone else can host” is a real bounded pattern, not a fantasy
  - always-on convenience and simplified setup are different value propositions from grassroots autonomy
- What is borrowed as solution:
  - none directly; this packet is borrowing distinction and burden grammar, not Foundry’s exact product sequence

### Mastodon

- What is analogous:
  - if the project promotes third-party hosts, it inherits standards, review, and metadata obligations
  - promoted hosts need backup, emergency-access, shutdown, and contact discipline
  - “list every host” is a real negative case
- What is not analogous:
  - Mastodon is far more public, moderation-heavy, and federation-native than Prix Guesser should assume
  - Prix Guesser does not currently want open public host growth as a default
- What is borrowed as concern:
  - sanctioned mirrors / collectives are not “just more hosts”; they are a promoted network with review burden
  - host labeling and minimum standards become part of the product identity once hosts are promoted
- What is borrowed as solution:
  - not federation
  - not public server discovery
  - only the idea that promoted hosts require explicit standards and ongoing curation

### Home Assistant / Nabu Casa

- What is analogous:
  - a self-hostable product can coexist with official hosted convenience
  - official convenience creates a separate service identity, account layer, and support obligation
  - official convenience may enforce security/update posture rather than staying a passive donation channel
- What is not analogous:
  - home automation is not a synchronous game-night room system
  - cloud backup and voice-assistant features do not map literally
- What is borrowed as concern:
  - official hosted convenience is not just “supporting the project”; it is a service relationship with reliability and policy implications
  - recurring service can be honest without becoming the only access path
- What is borrowed as solution:
  - not the specific feature mix
  - only the pattern of keeping self-host viable while offering official convenience as a distinct service surface

## Negative-case / failure evidence note

Direct evidence:

- Mastodon explicitly changed from automated host listing to manual curation because simply listing every submitted server gave no quality control.
- Mastodon’s promoted-server rules require daily backups, another person with emergency access, and advance shutdown notice because otherwise users can lose data or lose their host overnight.
- Mastodon’s backup docs say “for any real-world use” regular backups are necessary and describe catastrophic failure modes for database and secret loss.
- Foundry’s self-hosted mode stops being available when the app is not running, and remote internet play introduces home-network, bandwidth, and setup burdens.
- Foundry’s partner-hosted mode reduces setup burden but charges more and reduces infrastructure flexibility.
- Nabu Casa’s remote UI may be blocked when the underlying Home Assistant instance is too insecure, and ending the subscription removes remote access and cloud backup features.

Inference:

- The negative case is not subtle. Every reference that promotes plural or more-convenient hosting also introduces one or more of:
  - stronger recovery obligations
  - version/compatibility discipline
  - explicit contact/metadata requirements
  - support and shutdown expectations
  - account/service identity that is no longer “just the local product”
- This weakens the prior tendency to treat sanctioned mirrors or official hosted convenience as a simple later rung after trusted operators. They are burden shifts, not just distribution upgrades.

## Live alternatives

| Branch | Primary transition problem solved | Guest burden | Operator burden | New governance / identity burden | Comparative judgment |
| --- | --- | --- | --- | --- | --- |
| Logan-only authoritative hosting | preserves maximum control and one clear authority | lowest | highest on Logan | none beyond current doctrine | still the baseline, but not the only live option |
| Trusted operators running the same canonical bundle | reduces Logan-only dependence inside bounded trusted contexts | low if join grammar stays stable | medium on each technical operator | requires host-mode clarity and a usable operator runbook, but not a promoted host program | genuinely comparable to the baseline; strongest first transition seam |
| Official hosted convenience | reduces join friction, scheduled-room fragility, and always-on coordination pain while keeping one accountable service identity | lowest | centralized on one service operator path | creates service/account/support expectations and likely recurring cost | comparable on the `access/convenience` axis, but not identical in identity to trusted operators |
| Sanctioned mirrors / small host collectives | spreads resilience or geography across multiple promoted hosts | low for guests only if labels are clear | medium per host plus high central review burden | requires standards, review, compatibility discipline, contact metadata, backup/recovery policy, and shutdown posture | not just a later rung; this is a different promoted-host identity family |

## Findings

### Direct evidence

- Foundry’s hosting docs and FAQ support a real `trusted non-creator operator` pattern. Hosting can be done by someone other than the GM, and the FAQ explicitly permits one friend to host on one day and another on another day so long as only one player-accessible server is live at a time.
- Foundry’s self-host / cloud / partner-host split also shows that “someone else hosts” and “the service is always online” are different value propositions.
- Mastodon’s docs and covenant show that once a project promotes third-party hosts, minimum standards become unavoidable: backups, emergency access, shutdown notice, contact metadata, rules, manual review, and checks for whether a promoted host is actually up and accepting new users.
- Mastodon’s own blog provides a direct negative case against uncurated host promotion.
- Home Assistant and Nabu Casa show that official hosted convenience creates a distinct service identity, not just a more convenient version of self-hosting:
  - separate cloud account
  - recurring subscription
  - remote-access and backup features tied to that service
  - security-enforcement authority over remote access

### Inference and interpretation

1. `Trusted operators`, `sanctioned mirrors / collectives`, and `official hosted convenience` should not be treated as one simple progression.

   - `Trusted operators` solve bounded continuity and Logan-dependence inside trusted circles.
   - `Official hosted convenience` solves always-on access and lower-friction coordination under one accountable service identity.
   - `Sanctioned mirrors / collectives` solve promoted multi-host resilience or distributed community operation, but only by turning the project into a curator and reviewer of hosts.

2. The strongest first transition branch is `trusted operators running the canonical authoritative bundle`.

   Why this got stronger after direct external grounding:

   - Foundry directly grounds that trusted shared hosting is a real bounded pattern.
   - It adds operator burden without immediately forcing the project to become a service provider or a host-directory curator.
   - It preserves the existing doctrine best: one canonical bundle, browser-first guest join, and explicit host authority.

3. `Official hosted convenience` remains alive, but it is not just “the next rung after trusted operators.”

   What the external evidence changed:

   - Home Assistant/Nabu Casa makes clear that official convenience introduces a service contract, separate identity layer, and enforcement posture.
   - That means official hosted convenience is comparable to trusted operators only on one axis:
     - both can preserve guest simplicity and one canonical authority model
   - It is not comparable on another axis:
     - official convenience creates stronger uptime/support/security obligations than private trusted operators do

4. `Sanctioned mirrors / collectives` got weaker as a near-term branch after direct external grounding.

   Why:

   - Mastodon provides a concrete example that promoted hosts are not just additional capacity. They require standards, review, contactability, backup discipline, shutdown notice, and ongoing checks.
   - That is much closer to `running a promoted host network` than to `letting a trusted friend host the same bundle`.
   - The packet therefore does not support treating sanctioned mirrors as the obvious next rung after trusted operators.

### Dependencies and relations

| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Trusted operators | canonical bundle packaging, stable join grammar, operator runbook, explicit host-mode labeling | early remote-play resilience, non-Logan continuity, future room-authority seams | medium |
| Official hosted convenience | willingness to operate a service, account/billing/support posture, security/update enforcement, always-on hosting | support/access doctrine, later money model, host identity clarity | high |
| Sanctioned mirrors / collectives | published standards, compatibility metadata, backup/recovery rules, contact metadata, manual review and monitoring | long-arc host ecology, public trust, support boundaries, promoted-host identity | high |

## First-value vs later-value

| Branch | First-value in the transition phase | Later-value in a broader mature product | Preserve without prioritizing? |
| --- | --- | --- | --- |
| Trusted operators | high: best early way to reduce Logan-only hosting without changing the product’s identity too much | medium: still useful as a resilience seam, but may matter less if one official hosted path becomes dominant | no; this is the main carry-forward branch |
| Official hosted convenience | medium: only becomes first-value when scheduling friction, always-on demand, or host-availability failures become the main pain | high: strong later path if the project wants one official, low-friction, browser-first remote surface | yes; keep alive even if not first |
| Sanctioned mirrors / collectives | low: too governance-heavy for an early transition unless the project deliberately wants promoted plural hosts | medium-high only if the product later wants a real multi-host ecology and can police standards | yes; preserve as a deferred branch, not a priority |

## Archetype-to-burden translation

| Archetype | Trusted operators | Official hosted convenience | Sanctioned mirrors / collectives |
| --- | --- | --- | --- |
| Private recurring group | strongest fit; social trust already exists and operator burden can stay bounded | useful only if the host being offline becomes a recurring pain | usually overkill; promotion/governance burden exceeds value |
| Private online sync across known friends | strong fit if a few technical supporters can host | becomes attractive if “someone needs to be online” is the main failure mode | possible later, but only if there are multiple recurring groups and a reason to promote hosts rather than just let them exist privately |
| Solo ritual / async personal use | low relevance; host ecology should not drive this archetype | modest relevance later if persistence/sync across devices becomes valuable | almost no first-order value |
| Bounded event / host-screen showcase shell | weaker unless the event already trusts the operator socially | stronger later because one official hosted surface is easier to explain to a broader audience | only viable if host labeling, support boundaries, and standards are explicit enough that attendees do not mistake promoted third-party hosts for one official service |

Inference:

- This packet strengthens `trusted operators` mainly for the `private recurring group` and `private online sync` archetypes.
- It weakens any silent assumption that the same answer is right for bounded event/showcase shells.
- It also shows why host ecology should not drive early `solo ritual` planning at all.

## Trigger conditions

| Branch or shift | Promote when | Hold / defer when |
| --- | --- | --- |
| Logan-only -> trusted operators | at least a small number of technically confident non-Logan operators actually want to host; the canonical bundle can be started, updated, and recovered without direct maintainer intervention; join grammar stays the same for guests | operator demand is hypothetical; the runbook is still maintainer-only; host labels would confuse guests |
| Trusted operators -> official hosted convenience | most friction is now `host availability`, `scheduled room start reliability`, or `always-on remote access`; repeated room-start failures or coordination pain outweigh the value of staying purely grassroots; the project is willing to own a service identity | demand is still mostly bounded trusted groups; distributing operator burden privately solves the real pain; the project does not want stronger service/support expectations yet |
| Trusted operators -> sanctioned mirrors / collectives | there is a real need for more than one promoted host; the project is willing to publish and enforce minimum host standards; host metadata, contact routes, compatibility/version discipline, backups, emergency access, and shutdown notice can be required and checked | the project lacks review capacity; “community host” is still mostly an informal private arrangement; one official or private-trusted host model remains clearer for users |
| Sanctioned mirrors / collectives -> later prominence | promoted hosts repeatedly prove stable, legible, and well-governed; the product actually wants a promoted multi-host identity rather than one canonical service | the governance burden remains higher than the resilience benefit; users over-trust promoted third-party hosts as if they were one official service |

Concrete signals the later synthesis should watch:

- non-Logan operator adoption
- room-start reliability
- host-availability failures
- support burden from setup/recovery
- demand for always-on remote rooms
- user comprehension of host mode
- appetite and capacity for host review / policy enforcement

## Recommended carry-forward

1. Carry forward `trusted operators running the canonical authoritative bundle` as the primary transition seam.

2. Carry forward `official hosted convenience` as a separate live branch, not as an automatic next rung after trusted operators.

3. Reclassify `sanctioned mirrors / small host collectives` as a different host-identity family rather than a simple progression step.

4. Preserve one canonical authoritative bundle and stable browser-first join grammar across all live branches.

5. Protect these carry-forward seams in later planning and canon work:
   - explicit host-mode labeling
   - compatibility/version metadata before plural promoted hosts
   - backup and recovery posture
   - emergency contact / emergency access posture if hosts are promoted
   - support-boundary clarity between private trusted operators, promoted community hosts, and official service

6. Treat any future ranking between `official hosted convenience` and `sanctioned mirrors / collectives` as trigger-dependent rather than already closed.

## Explicit deferrals

This packet does not settle:

- whether official hosted convenience should be first-party operated or vendor/partner managed
- exact subscription, donation, queue, or entitlement design
- exact UI copy for host-mode labels
- legal agreements, trust policy, or compliance requirements for third-party hosts
- pack-signing or exact update-channel design
- public discovery or stranger-access hosting
- whether any later public shell would need a different hosting answer

## What should remain open

- Whether official hosted convenience ever becomes first-value before the product has a broader remote-play or event shell
- Whether sanctioned mirrors / collectives are worth their governance cost at all
- What the minimum viable operator runbook is for a trusted non-Logan host
- How much host-mode metadata users actually need in join flows and room UI
- Whether later wrapper families create a different host-ecology answer than the private recurring group does

## What later converged synthesis must reconcile

- host ecology with the separate `support / access / service obligation` ladder from the money/promise lane
- host ecology with later visibility and audience-shell decisions
- whether `official hosted convenience` and `trusted operators` should coexist as different answers to different pains, or whether one should later dominate
- how much compatibility/version discipline must be promoted from “nice to have” into canon once plural hosts become real
- whether the mature product wants one canonical service identity, a bounded private operator ecology, or a promoted multi-host identity

## Sources

### Local

- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-remediation-packet-c-host-ecology-task-spec.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-remediation-packet-common-scaffold.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-lane-e-grassroots-transition-hosting-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-gap-closure-reference-patterns-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-epistemic-opening-output.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-next-round-gap-opportunity-register.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`

### External

- Foundry VTT:
  - [Hosting Options Guide](https://foundryvtt.com/article/hosting/)
  - [Frequently Asked Questions](https://foundryvtt.com/article/faq/)
  - [Minimum Requirements](https://foundryvtt.com/article/requirements/)
  - [Content Packaging Guide](https://foundryvtt.com/article/packaging-guide/)
- Mastodon:
  - [Running your own server](https://docs.joinmastodon.org/user/run-your-own/)
  - [Mastodon Server Covenant](https://joinmastodon.org/covenant)
  - [Introducing the Mastodon Server Covenant](https://blog.joinmastodon.org/2019/05/introducing-the-mastodon-server-covenant/)
  - [Backing up your server](https://docs.joinmastodon.org/admin/backups/)
  - [Setting up your new instance](https://docs.joinmastodon.org/admin/setup/)
- Home Assistant / Nabu Casa:
  - [Securing](https://www.home-assistant.io/docs/configuration/securing/)
  - [Do you offer a lifetime subscription or a one time fee?](https://support.nabucasa.com/hc/en-us/articles/26179725282461-Do-you-offer-a-lifetime-subscription-or-a-one-time-fee)
  - [Cannot login to Home Assistant](https://support.nabucasa.com/hc/en-us/articles/33070434152221-Cannot-login-to-Home-Assistant)
  - [Insecure Home Assistant instance detected](https://www.nabucasa.com/more-info/insecure-instance/)
  - [Cancelling the subscription and deleting the account](https://support.nabucasa.com/hc/en-us/articles/26167476727581-Cancelling-the-subscription-and-deleting-the-account)
