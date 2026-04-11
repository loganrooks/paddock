# Lane 02 Findings: Funding, Access, And Transparency Models

Date: 2026-04-10
Lane: `02-funding-access-and-transparency-models`
Status: complete

## Question Space

- [CONFIRMED] Prix Guesser's current documented posture is still private-first, host-screen-friendly, browser-first, and not yet a public commercial product. The roadmap invests first in authored content, authoritative rooms, guest join, and watchable session flow, not in public monetization infrastructure. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] That means the funding question here is not "how should this game monetize?" It is "how can a small hosted hobby service accept support, ration limited capacity honestly, and compare money with other forms of contribution without accidentally making service promises it cannot yet keep?" ([00-ORCHESTRATION](../00-ORCHESTRATION.md), [charter](../specs/02-funding-access-and-transparency-models.md), [cross-lane reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md))
- [INFERRED] The live design tension is between three goods that do not automatically align:
  - financial sustainability
  - low-friction fair access
  - trust-preserving communication
- [INFERRED] The strongest models for this project will likely be the ones that let support exist without silently converting support into entitlement before the hosted product is operationally mature enough to bear that weight. ([hosting-transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))

## Method And Sources

- [CONFIRMED] I grounded the lane first in repo-local posture documents and the first-wave hosting/product findings, because this lane only makes sense relative to Prix Guesser's actual stage and room model. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [01-product-futures](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md), [02-hosting-transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [CONFIRMED] I then used official platform documentation to inspect what different support systems and access systems actually permit: GitHub Sponsors, Ko-fi, Patreon, Open Collective, Kahoot pricing, Cloudflare Waiting Room, Steam Early Access, and FTC dark-pattern guidance. These are strong for capability and policy claims, weaker for proving what indie hobby audiences will emotionally tolerate. ([GitHub Sponsors tiers](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers), [GitHub Sponsors goals](https://docs.github.com/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-goal), [Ko-fi memberships](https://help.ko-fi.com/hc/en-us/articles/4402945994001-Ko-fi-Memberships-and-Membership-Tiers), [Ko-fi fees](https://help.ko-fi.com/hc/en-us/articles/360002506494-Does-Ko-fi-take-a-fee), [Patreon tiers and benefits](https://support.patreon.com/hc/en-us/articles/203913559-I-m-a-creator-what-are-tiers-and-benefits-), [Patreon pricing](https://support.patreon.com/hc/en-us/articles/36426991446797-A-standard-platform-fee-for-new-creators-effective-after-August-4-2025), [Patreon edit tiers](https://support.patreon.com/hc/en-us/articles/218202363-How-to-edit-your-membership-tiers), [Open Collective budgets](https://documentation.opencollective.com/collectives/managing-money/budgets), [Open Collective goals and tiers](https://documentation.opencollective.com/collectives/raising-money/setting-goals-and-tiers), [Open Collective recurring contributions](https://documentation.opencollective.com/giving-to-collectives/making-a-recurring-contribution), [Open Collective contributing as guest](https://documentation.opencollective.com/giving-to-collectives/contributing-as-a-guest), [Kahoot pricing](https://kahoot.com/schools/plans/), [Cloudflare Waiting Room](https://developers.cloudflare.com/waiting-room/), [Steam Early Access](https://partner.steamgames.com/doc/store/earlyaccess), [FTC dark-pattern subscriptions enforcement](https://www.ftc.gov/news-events/news/press-releases/2021/10/ftc-ramp-enforcement-against-illegal-dark-patterns-trick-or-trap-consumers-subscriptions), [FTC dark patterns workshop/report entry](https://www.ftc.gov/consumer-protection?field_mission_tid=All&page=68&type=All))
- [CONFIRMED] Source limits matter here:
  - official funding-platform docs are mostly creator-facing and can overstate ease of operation
  - official product pricing pages show how mature services gate access, but not whether that model is wise for a tiny private-first hobby service
  - no Prix Guesser audience interviews or real support-demand data were available
- [INFERRED] Because of those limits, most of the prescriptive claims below are stage-sensitive inferences, not universal rules.

## Inquiry Trajectory

1. [CONFIRMED] I started with the narrow lane question: what funding and access models can support a tiny hosted service without sliding into manipulative scarcity or premature commercialization? ([charter](../specs/02-funding-access-and-transparency-models.md))
2. [INFERRED] That immediately branched into a promise question: which models merely accept support, and which models imply durable access rights, support obligations, queue priority, or refund expectations?
3. [CONFIRMED] I then examined support platforms that explicitly separate money, tiers, rewards, and transparency:
   - GitHub Sponsors for lightweight recurring/one-time support with optional rewards
   - Ko-fi and Patreon for support-plus-tier-benefit structures
   - Open Collective for transparent public budgets and contribution ledgers
4. [INFERRED] The next branch was capacity communication rather than payment itself: if Prix Guesser ever needs queueing, windows, or waitlists, what distinguishes honest traffic management from scarcity theater?
5. [CONFIRMED] That led into Cloudflare Waiting Room and FTC/Steam materials because they say more directly than "monetization" docs what kinds of user communication and expectation-setting are acceptable or risky. ([Cloudflare Waiting Room](https://developers.cloudflare.com/waiting-room/), [Steam Early Access](https://partner.steamgames.com/doc/store/earlyaccess), [FTC dark-pattern subscriptions enforcement](https://www.ftc.gov/news-events/news/press-releases/2021/10/ftc-ramp-enforcement-against-illegal-dark-patterns-trick-or-trap-consumers-subscriptions))
6. [INFERRED] A final branch emerged around non-monetary contribution: community hosting, operator help, and compute contribution are not just "another payment option." They alter trust boundaries, support expectations, and product topology. That became a required comparison branch rather than a side note. ([02-hosting-transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))

## Branching Paths And Dependencies

- [INFERRED] `Paid access` depends on `operational maturity`.
  - If the service cannot reliably start rooms, keep sessions alive, and communicate incidents, selling access pulls obligation forward faster than the product is ready.
- [INFERRED] `Queueing or waiting rooms` depend on `real instrumentation`.
  - Honest queues require real capacity knowledge, approximate wait logic, and stable session handling; otherwise the queue is cosmetic theater.
- [INFERRED] `Donation-led support` depends on `language discipline`.
  - The technical implementation is easy, but the trust outcome depends heavily on whether support copy avoids implying guaranteed access or reciprocal priority.
- [INFERRED] `Community hosting or infrastructure contribution` depends on `official-versus-unofficial host boundaries`.
  - Without that boundary, users cannot tell who is responsible for uptime, privacy, moderation, or version compatibility.
- [INFERRED] `Public financial transparency` depends on `what kind of transparency is actually intended`.
  - Open budgets are useful if the project wants public accountability for hosting spend or contributor compensation.
  - They are much less obviously suitable if this remains a personal hobby project with private finances and irregular ad hoc spending.
- [INFERRED] `Invite-only/public-beta hybrids` depend on `what the beta is for`.
  - If the beta is for learning and capacity control, invite gating can be coherent.
  - If the beta is for synthetic urgency, it becomes scarcity theater.

## Findings

### Model Comparison

| Model | What it is really selling or requesting | Best-fit stage | Technical feasibility | Operational feasibility | Adoption feasibility | Economic feasibility | Ethical / trust feasibility |
|---|---|---|---|---|---|---|---|
| Donation jar / recurring support with no access guarantee | "Help keep this alive" | Private-first and early hosted friend beta | [CONFIRMED] High. GitHub Sponsors, Ko-fi, and Open Collective all support one-time and/or recurring contributions without requiring hard feature gating. ([GitHub Sponsors](https://docs.github.com/sponsors/getting-started-with-github-sponsors/about-github-sponsors), [Ko-fi fees](https://help.ko-fi.com/hc/en-us/articles/360002506494-Does-Ko-fi-take-a-fee), [Open Collective recurring contributions](https://documentation.opencollective.com/giving-to-collectives/making-a-recurring-contribution)) | [INFERRED] High, if framed plainly. Minimal entitlement burden. | [INFERRED] Moderate. Fans often understand "tip jar" support, but many users still assume paying earns some operational privilege. | [INFERRED] Low to moderate. Sustainable only if costs stay small or support sentiment is unusually strong. | [INFERRED] Strongest early model because it minimizes false promises. |
| Donation tiers with symbolic perks but no gameplay access guarantee | "Support gets you recognition, updates, maybe behind-the-scenes or pack previews" | Small hosted beta once there is enough ongoing work to justify updates/perks | [CONFIRMED] High. Patreon, Ko-fi, GitHub Sponsors, and Open Collective all allow tiers/rewards/messages. ([Patreon tiers and benefits](https://support.patreon.com/hc/en-us/articles/203913559-I-m-a-creator-what-are-tiers-and-benefits-), [Ko-fi memberships](https://help.ko-fi.com/hc/en-us/articles/4402945994001-Ko-fi-Memberships-and-Membership-Tiers), [GitHub Sponsors tiers](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers), [Open Collective goals and tiers](https://documentation.opencollective.com/collectives/raising-money/setting-goals-and-tiers)) | [INFERRED] Medium. Even symbolic perks create recurring fulfillment work. | [INFERRED] High if perks stay legible and light. | [INFERRED] Moderate. Better than pure donation for recurring support, but still unlikely to finance serious public operations. | [INFERRED] Acceptable only if perks do not imply service priority by implication. |
| Invite-only or scheduled free beta plus optional support | "Access is limited because the service is small; support is optional and separate" | Transition from private-friend hosting to selective public testing | [CONFIRMED] High. No special payment stack required. Steam explicitly recommends smaller focused testing before broader release when the game is not ready. ([Steam Early Access](https://partner.steamgames.com/doc/store/earlyaccess)) | [INFERRED] Medium-high. Still requires admission logic and communication discipline, but avoids paid-service obligations. | [INFERRED] Medium. Some users accept invite waves; others read them as status signaling. | [INFERRED] Low unless paired with optional support. | [INFERRED] Strong if the reason for limits is real and explained clearly. |
| Capacity windows / waitlist / queue | "Access is constrained by real room capacity" | Only after measured public demand exceeds comfortable room capacity | [CONFIRMED] Medium-high. Cloudflare Waiting Room supports estimated wait times, remembered place in line, and branded queue pages. ([Cloudflare Waiting Room](https://developers.cloudflare.com/waiting-room/)) | [INFERRED] Medium. Requires accurate ops signals and incident handling. | [INFERRED] Medium if waits are short and rules are legible; poor if opaque. | [INFERRED] Medium. It can stretch limited infrastructure, but does not itself fund the service. | [INFERRED] Defensible only when it reflects actual capacity rather than growth theater. |
| Paid/free split with guaranteed access, larger player caps, or reservation rights | "Payment buys dependable participation or materially better service" | Later public stage, only after stable hosted operations exist | [CONFIRMED] High. Mature products like Kahoot openly gate participant limits and modes by plan. ([Kahoot pricing](https://kahoot.com/schools/plans/)) | [INFERRED] Low early, higher later. This model creates real support, refund, and reliability expectations immediately. | [INFERRED] High once the service is real and legible; brittle if launched too early. | [INFERRED] Strongest direct revenue model. | [INFERRED] Weak early, potentially acceptable later. Charging for guaranteed access before reliability is proven is the clearest trust trap in this lane. |
| Monetary or infrastructural contribution as parallel support paths | "Support us with money, hosting, operator labor, or infrastructure" | Trusted-circle stage or advanced community phase | [CONFIRMED] Medium. Self-hosting and private remote hosting are plausible technically, but they alter topology and responsibility. ([02-hosting-transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md)) | [INFERRED] Medium-low unless roles are explicit. Community hosting creates support fragmentation. | [INFERRED] Low-medium for general users, higher for technical friends or close collaborators. | [INFERRED] Potentially good for cost relief, but lumpy and hard to standardize. | [INFERRED] Mixed. Cooperative ethos is attractive, but only if users can tell which hosts are official, trusted, and supported. |

### Sustainable Support Models

- [INFERRED] The most coherent early support posture is:
  - optional one-time or recurring support
  - no gameplay power or answer advantage
  - no silent guarantee of room access
  - plain explanation of what support funds
- [CONFIRMED] GitHub Sponsors, Ko-fi, and Open Collective all support low-ceremony recurring or one-time contribution patterns without requiring heavy subscription entitlements. GitHub Sponsors allows optional one-time and monthly tiers; Ko-fi supports one-time tips, memberships, and commissions; Open Collective supports one-time and recurring contributions including guest one-time contributions. ([GitHub Sponsors tiers](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers), [Ko-fi fees](https://help.ko-fi.com/hc/en-us/articles/360002506494-Does-Ko-fi-take-a-fee), [Ko-fi memberships](https://help.ko-fi.com/hc/en-us/articles/4402945994001-Ko-fi-Memberships-and-Membership-Tiers), [Open Collective recurring contributions](https://documentation.opencollective.com/giving-to-collectives/making-a-recurring-contribution), [Open Collective contributing as a guest](https://documentation.opencollective.com/giving-to-collectives/contributing-as-a-guest))
- [INFERRED] For Prix Guesser specifically, the donation-led model is attractive because it matches the current reality: the service is still proving whether hosted rooms are even a durable habit, not yet proving that a paid hosted tier deserves to exist.
- [INFERRED] If a recurring support layer exists, it should likely fund:
  - hosting continuity
  - domain and infra costs
  - content-authoring time
  - occasional closed testing windows
  not "premium competitive status."

### Extractive Or Trust-Eroding Models

- [CONFIRMED] FTC guidance on subscriptions centers clear upfront information, informed consent, and easy cancellation, and warns against sign-up tactics that trick or trap users. ([FTC dark-pattern subscriptions enforcement](https://www.ftc.gov/news-events/news/press-releases/2021/10/ftc-ramp-enforcement-against-illegal-dark-patterns-trick-or-trap-consumers-subscriptions))
- [CONFIRMED] Steam's Early Access rules say not to make specific promises about future events, not to ask customers to bet on the future of the game, and to be transparent about known limitations. ([Steam Early Access](https://partner.steamgames.com/doc/store/earlyaccess))
- [INFERRED] For this project, the most trust-eroding patterns would therefore be:
  - charging for "support" when the actual user takeaway is "I paid for reliable access"
  - using waitlists or limited slots mainly to generate FOMO
  - selling high-priced supporter tiers that silently function as priority access without explicitly saying so
  - treating opaque queueing as acceptable because "capacity is hard"
  - calling community-hosted instances "official enough" without clear responsibility boundaries
- [CONFIRMED] Platform tooling itself can drift toward persuasion design. Open Collective explicitly offers logarithmic goal bars that make progress look larger to incentivize contributions, and Patreon offers tier highlighting. ([Open Collective goals and tiers](https://documentation.opencollective.com/collectives/raising-money/setting-goals-and-tiers), [Patreon tier highlighting](https://support.patreon.com/hc/en-us/articles/9446293583501-Tier-highlighting))
- [INFERRED] That does not make those tools illegitimate, but it does mean "transparent funding" can still contain manipulation pressure if the project is not careful.

### Models That Only Make Sense After A Different Product Stage

- [INFERRED] A true paid/free split with guaranteed access, reservation rights, or materially larger room capacity only makes sense after all of the following become true:
  - room-start reliability is good enough to promise
  - public capacity is measured, not guessed
  - cancellation/refund norms are defined
  - incidents can be explained without panic or silence
- [CONFIRMED] Kahoot's public pricing openly ties plans to participant limits and additional modes, which is exactly the kind of explicit promise surface a mature paid/free split creates. ([Kahoot pricing](https://kahoot.com/schools/plans/))
- [INFERRED] Prix Guesser is not there yet. Importing that model now would force a later-stage commercial contract onto an earlier-stage social prototype.

### Monetary Support Versus Infrastructural Contribution

- [INFERRED] Money and infrastructure are not interchangeable currencies.
- [INFERRED] Monetary support mainly preserves one canonical hosted experience.
- [INFERRED] Infrastructural contribution, by contrast, can create:
  - extra operator burden
  - host-to-host drift
  - version fragmentation
  - privacy ambiguity
  - unclear support ownership
- [INFERRED] That means community hosting is best treated as a trusted-circle extension or advanced contributor path, not as the default "free tier" equivalent.
- [INFERRED] A person donating $10 to one official hosted service and a person running a community instance are helping in very different ways. The first increases continuity; the second changes topology and governance.

## Ethically Tolerable Scarcity

- [INFERRED] Scarcity is ethically tolerable here only when it describes a real constraint that the operator is willing to name plainly.
- [CONFIRMED] Cloudflare Waiting Room is designed to manage peak traffic while showing estimated wait times, remembering a visitor's place in line, and preserving the origin from overload. ([Cloudflare Waiting Room](https://developers.cloudflare.com/waiting-room/))
- [INFERRED] That is the right ethical baseline for any future Prix Guesser queue:
  - the queue exists because room capacity is actually constrained
  - users can see they are queued
  - users get a rough sense of wait or next window
  - their position is not arbitrarily discarded
- [CONFIRMED] FTC and Steam both lean toward the same normative lesson from a different angle: do not hide material information, do not trap users in misleading subscription states, and do not sell the future as if it were already real. ([FTC dark-pattern subscriptions enforcement](https://www.ftc.gov/news-events/news/press-releases/2021/10/ftc-ramp-enforcement-against-illegal-dark-patterns-trick-or-trap-consumers-subscriptions), [Steam Early Access](https://partner.steamgames.com/doc/store/earlyaccess))
- [INFERRED] So the ethically tolerable forms of scarcity are:
  - real beta capacity windows
  - real temporary queueing under load
  - real limited slots for one-to-one or labor-intensive perks
  - real invite waves for learning or moderation reasons
- [INFERRED] The ethically suspect forms are:
  - artificial countdown urgency
  - fake sold-out states
  - vague "limited access" language with no operational explanation
  - perpetual invite scarcity used mainly to make the project feel prestigious
  - payment-linked queue skipping before the service is stable enough to justify it

## What Users Might Hear Versus What We Mean

| If we say this | Users may hear this | Risk | Better interpretation discipline |
|---|---|---|---|
| "Support the project" | "If I pay, I should be able to play when I want" | [INFERRED] Donation becomes quasi-subscription in the user's mind. | [INFERRED] Explicitly state whether support changes access at all. |
| "Supporters help keep hosting alive" | "Paid supporters get priority if capacity is tight" | [INFERRED] Priority is inferred even if never promised. | [INFERRED] Say whether support affects access priority, and if not, say so directly. |
| "Limited beta access" | "This is scarce and desirable, so I should hurry" | [INFERRED] Honest capacity language gets read as marketing urgency. | [INFERRED] Pair the limit with the real reason: room stability, moderation, or measured capacity. |
| "Community-hosted" | "This is still official and equally supported" | [INFERRED] Responsibility becomes blurry when something breaks. | [INFERRED] Label official hosts, unofficial hosts, and support boundaries distinctly. |
| "Membership tier" | "I am buying durable recurring value" | [INFERRED] Light symbolic support perks get overread as service entitlement. | [INFERRED] Keep tier perks concrete and low-ambiguity. |
| "Queueing during peak times" | "The service is unstable or unfair" | [INFERRED] Even honest traffic control can look arbitrary if users see only the result. | [INFERRED] Show current status, approximate timing, and what determines admission. |
| "Paid supporter rooms" | "The project is now a commercial service with customer obligations" | [INFERRED] A stage shift happens in user expectations immediately. | [INFERRED] Do not use this language until the project actually wants that obligation set. |

## Promises Each Model Forces Us To Keep

| Model | Implicit promise | Minimum thing that must be true | Likely failure mode if not true |
|---|---|---|---|
| Donation jar / optional support | "We will be honest about what your money does and does not buy" | [INFERRED] Copy is explicit that support does not equal guaranteed access. | [INFERRED] Supporters feel quietly downgraded or misled. |
| Symbolic support tiers | "We will actually deliver the named perks and updates" | [CONFIRMED] Patreon and Ko-fi both center defined benefits, welcome messages, and terms. ([Patreon tiers and benefits](https://support.patreon.com/hc/en-us/articles/203913559-I-m-a-creator-what-are-tiers-and-benefits-), [Ko-fi memberships](https://help.ko-fi.com/hc/en-us/articles/4402945994001-Ko-fi-Memberships-and-Membership-Tiers)) | [INFERRED] Tier drift, burnout, stale rewards, or "what am I paying for?" confusion. |
| Invite-only or scheduled beta | "Admission limits are real, not theatrical, and we will explain them" | [INFERRED] Invite rules and timing are legible enough to feel principled. | [INFERRED] Invite system feels arbitrary, clique-ish, or manipulative. |
| Queueing / waiting room | "We are managing real peak load and not wasting your time blindly" | [CONFIRMED] Accurate enough queue state, wait estimates, and remembered position. ([Cloudflare Waiting Room](https://developers.cloudflare.com/waiting-room/)) | [INFERRED] Queue feels fake, broken, or unfair. |
| Paid guaranteed access | "We can reliably deliver access, support, and remedies when we fail" | [INFERRED] Uptime/support/capacity are measured and incidents are communicated clearly. | [INFERRED] Money converts outages into customer-trust crises. |
| Community-hosted path | "You will know who runs this, who supports it, and what data/rules apply" | [INFERRED] Official/unofficial host labeling and compatibility policy exist. | [INFERRED] Users blame the core project for third-party failure or misuse. |

## Gray Areas And Live Tensions

- [INFERRED] **Donations are ethically cleaner but economically weaker.**
  - A donation model best preserves hobby honesty.
  - It may also fail to cover even modest public-hosting costs once real demand appears.

- [INFERRED] **Tiered support can stay light, but platform defaults lean toward stronger benefit framing.**
  - Patreon, Ko-fi, GitHub Sponsors, and Open Collective all make it easy to attach tiers, goals, rewards, and welcome messages.
  - That can help clarity.
  - It can also nudge the project toward making more promises than a small service should make.

- [INFERRED] **Transparency builds trust, but not every kind of transparency fits a personal hobby project.**
  - Open Collective-style public budgets are excellent if the project wants contribution accountability and shared stewardship.
  - They are less obviously appropriate if the operator does not want to publish personal spending patterns or receive public scrutiny for every hosting choice.

- [INFERRED] **Queueing can be both honest and alienating.**
  - Honest queueing says "we are small and we know it."
  - It can also make the product feel flimsy or exclusionary if users encounter it too often or without context.

- [INFERRED] **Community hosting aligns with cooperative ethos but weakens canonical trust.**
  - It reduces sole-operator cost pressure.
  - It also makes it harder to preserve one coherent room standard, moderation posture, and support surface.

- [INFERRED] **Charging may actually be fairer than hidden subsidy, but only after a stage shift is real.**
  - There is nothing inherently more ethical about silently self-subsidizing a public service forever.
  - But asking for money before access quality is dependable creates the exact premature commercial contract this lane was asked to avoid.

## Scope Expansions

### Scope Expansion 1: Funding UI Is Also Governance

- [CONFIRMED] Open Collective goal bars, GitHub sponsorship goals, and Patreon tier highlighting all show that support tooling is not neutral plumbing; it shapes what contributors feel invited or pressured to do. ([Open Collective goals and tiers](https://documentation.opencollective.com/collectives/raising-money/setting-goals-and-tiers), [GitHub Sponsors goals](https://docs.github.com/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-goal), [Patreon tier highlighting](https://support.patreon.com/hc/en-us/articles/9446293583501-Tier-highlighting))
- [INFERRED] I pursued this because "transparent support" can still drift into persuasion design, which is directly relevant to the lane's anti-manipulation constraint.

### Scope Expansion 2: Early-Access Communication Rules Matter More Than Generic Monetization Advice

- [CONFIRMED] Steam's Early Access rules about not making specific promises and not asking customers to bet on the future turned out to be more relevant to Prix Guesser's stage than most pure pricing guidance. ([Steam Early Access](https://partner.steamgames.com/doc/store/earlyaccess))
- [INFERRED] I pursued this because Prix Guesser is closer to "small evolving hosted thing with uncertain public future" than to "mature SaaS pricing optimization."

### Scope Expansion 3: Payment Acceptance Implies Policy Surface

- [CONFIRMED] Ko-fi memberships encourage standard terms, including cancellations and refund policies; Patreon pricing and benefits also pull creators toward defined recurring offerings. ([Ko-fi memberships](https://help.ko-fi.com/hc/en-us/articles/4402945994001-Ko-fi-Memberships-and-Membership-Tiers), [Patreon tiers and benefits](https://support.patreon.com/hc/en-us/articles/203913559-I-m-a-creator-what-are-tiers-and-benefits-), [Patreon pricing](https://support.patreon.com/hc/en-us/articles/36426991446797-A-standard-platform-fee-for-new-creators-effective-after-August-4-2025))
- [INFERRED] I investigated this enough to conclude that any paid recurring model creates policy obligations quickly.
- [HYPOTHESIS] I did not deeply research tax, consumer-law, or jurisdiction-specific obligations for a hobby operator taking money. That remains a third-pass topic if the project seriously considers paid hosted access.

## Rival Models Still Alive

### Model A: Support-Only, No Access Guarantees

- [INFERRED] Optional donations or recurring support with extremely light perks remain the strongest early-stage model.
- [INFERRED] This best matches the current product stage and minimizes promise debt.

### Model B: Support Tiers With Symbolic Or Community Perks

- [INFERRED] This is still viable if the perks are things like credits, dev updates, behind-the-scenes notes, or occasional supporter-visible content.
- [INFERRED] It becomes risky if the perks start functioning as access classes by implication.

### Model C: Invite-Only Public Beta Plus Optional Support

- [INFERRED] This remains a strong transition model because it separates the question of "who can enter right now?" from "who is helping fund this?"
- [INFERRED] It works only if invite scarcity is treated as operational truth, not mystique.

### Model D: Later Paid Hosted Tier

- [INFERRED] This is still alive, but it belongs to a later stage where the project is willing to become a real service provider for at least one official hosted path.

### Model E: Trusted-Circle Community Hosting

- [INFERRED] This remains viable as an adjunct path for technical friends, collaborators, or clubs.
- [INFERRED] It does not look viable as the main answer to broad public access unless the project intentionally embraces a more federated or multi-operator identity.

## Practical Implications

### Thinking Implications

- [INFERRED] Separate these concepts in future discussion:
  - `support`
  - `access`
  - `priority`
  - `official hosting`
  - `community hosting`
  - `beta capacity`
- [INFERRED] Avoid saying "monetization" when the real question is often "what promise burden are we taking on?"

### Design Implications

- [INFERRED] Keep support UX separate from join UX unless the project intentionally wants payment to affect access.
- [INFERRED] If waitlists or windows exist, make the reason visible in-product.
- [INFERRED] If community-hosted rooms ever exist, label official versus unofficial hosts clearly in join surfaces.
- [INFERRED] If any recurring support tier exists, publish plain-language terms:
  - what the tier includes
  - what it does not include
  - what happens if the project pauses or changes shape

### Implementation Implications

- [INFERRED] Build room-capacity instrumentation before building queues.
- [INFERRED] Preserve a place to expose service state:
  - current hosted mode
  - beta window status
  - queue status
  - known incidents
- [INFERRED] Treat official-host metadata as first-class if any semi-community-hosted future remains on the table.
- [INFERRED] Keep payment and entitlement logic decoupled unless a deliberate later stage merges them.

### Measurement Or Experiment Implications

- [INFERRED] Before choosing any paid-access path, measure:
  - hosted room-start success rate
  - reconnect success rate
  - peak concurrent room count
  - user-visible queue abandonment
  - operator intervention frequency
  - actual monthly hosting cost under realistic use
- [INFERRED] Before choosing any support model, test:
  - whether users will support without access perks
  - whether supporter copy is misread as entitlement
  - whether invite windows feel fair or clique-ish
  - whether community-hosted sessions create confusion about responsibility

## What Would Change This View

- [HYPOTHESIS] If real hosting costs turn out trivial at the intended scale, the project may be able to stay donation-led much longer.
- [HYPOTHESIS] If supporter demand is weak unless tied to tangible access value, the project may need a later paid/free split sooner than this lane prefers.
- [HYPOTHESIS] If repeated public-beta demand overwhelms capacity but users tolerate honest wait windows well, queueing may become an ethically fine bridge stage.
- [HYPOTHESIS] If technical friends or clubs strongly want to host their own rooms and do not need canonical official support, infrastructural contribution could become more important than monetary support.
- [HYPOTHESIS] If the project decides it explicitly wants to become a durable hosted niche service rather than a lightly supported hobby game, then some of the caution around paid guaranteed access weakens substantially.

## Open Questions Worth A Third Pass

1. [INFERRED] What are the actual monthly cost bands for:
   - private friend hosting
   - modest public beta hosting
   - a queue-managed small public service?
2. [INFERRED] What cancellation, refund, and pause language would be fair if recurring support tiers ever imply operational continuity?
3. [INFERRED] How much public transparency is actually desired:
   - plain status page and capacity notes
   - monthly "what your support funded" posts
   - full public ledger?
4. [INFERRED] If community-hosted instances exist, should they be:
   - unofficial and loosely compatible
   - directory-listed but unsupported
   - or part of a more explicit federation model?
5. [HYPOTHESIS] Will knowledgeable F1 fans actually support the project financially without access differentiation, or will they mainly interpret payment as buying a stronger claim on playability?
6. [HYPOTHESIS] Could a contribution system fairly compare money, pack-authoring labor, moderation help, and hosting labor without producing resentment or status ambiguity?

## Source Ledger

### Primary Internal Sources

- [PROJECT](../../../PROJECT.md)
  - Authority: current product posture and constraints.
  - Used for: private-first posture, social-first scope, non-commercial current reality.
  - Limit: intent only, not tested demand.

- [ROADMAP](../../../ROADMAP.md)
  - Authority: current phase sequencing and what is not yet being built.
  - Used for: evidence that monetization/access infrastructure is not yet a v1 focus.
  - Limit: roadmap may later change as hosted realities emerge.

- [REQUIREMENTS](../../../REQUIREMENTS.md)
  - Authority: current requirement inventory.
  - Used for: room, join, and authority expectations that payment models must not distort.
  - Limit: product requirements, not business policy.

- [00-ORCHESTRATION](../00-ORCHESTRATION.md)
- [charter](../specs/02-funding-access-and-transparency-models.md)
  - Authority: lane scope and required questions.
  - Used for: anti-manipulative-scarcity and support-model framing.

- [01-product-futures](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md)
- [02-hosting-transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md)
- [cross-lane reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md)
  - Authority: strong internal synthesis of stage shape and hosting transitions.
  - Used for: transition staging and trust/capacity context.
  - Limit: still interpretive research, not canonical commitments.

### Primary External Sources

- [GitHub Sponsors](https://docs.github.com/sponsors/getting-started-with-github-sponsors/about-github-sponsors)
- [GitHub Sponsors tiers](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-tiers)
- [GitHub Sponsors goals](https://docs.github.com/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-sponsorship-goal)
  - Authority: official docs for lightweight support tiers, rewards, and public funding goals.
  - Used for: low-ceremony support models, optional tiers, benefits, and public goals.
  - Limit: open-source sponsorship context differs from hosted hobby-game operations.

- [Ko-fi fees](https://help.ko-fi.com/hc/en-us/articles/360002506494-Does-Ko-fi-take-a-fee)
- [Ko-fi memberships](https://help.ko-fi.com/hc/en-us/articles/4402945994001-Ko-fi-Memberships-and-Membership-Tiers)
- [Ko-fi commissions](https://help.ko-fi.com/hc/en-us/articles/360016170433-Using-Ko-fi-for-Commissions-)
  - Authority: official docs for tip jars, recurring support, limited slots, terms, and member-only offerings.
  - Used for: how quickly support platforms let creators turn support into perks, limits, or services.
  - Limit: creator-help framing may understate fulfillment burden.

- [Patreon tiers and benefits](https://support.patreon.com/hc/en-us/articles/203913559-I-m-a-creator-what-are-tiers-and-benefits-)
- [Patreon pricing](https://support.patreon.com/hc/en-us/articles/36426991446797-A-standard-platform-fee-for-new-creators-effective-after-August-4-2025)
- [Patreon edit tiers](https://support.patreon.com/hc/en-us/articles/218202363-How-to-edit-your-membership-tiers)
- [Patreon tier highlighting](https://support.patreon.com/hc/en-us/articles/9446293583501-Tier-highlighting)
  - Authority: official docs for tier limits, recurring benefits, fees, and presentation nudges.
  - Used for: promise burden, sustainability reminders, and persuasion surfaces.
  - Limit: creator economy context is broader than Prix Guesser's likely support shape.

- [Open Collective budgets](https://documentation.opencollective.com/collectives/managing-money/budgets)
- [Open Collective goals and tiers](https://documentation.opencollective.com/collectives/raising-money/setting-goals-and-tiers)
- [Open Collective recurring contributions](https://documentation.opencollective.com/giving-to-collectives/making-a-recurring-contribution)
- [Open Collective contributing as a guest](https://documentation.opencollective.com/giving-to-collectives/contributing-as-a-guest)
  - Authority: official docs for public ledgers, recurring support, guest contributions, and contribution tiers.
  - Used for: transparency models and the gray area between transparency and contribution incentivization.
  - Limit: collective/public-ledger assumptions may not fit a private hobby operator.

- [Kahoot pricing](https://kahoot.com/schools/plans/)
  - Authority: official current pricing and participant-limit page.
  - Used for: mature example of explicit plan-based access and participant-cap promises.
  - Limit: mature education product, not indie hobby service.

- [Cloudflare Waiting Room](https://developers.cloudflare.com/waiting-room/)
  - Authority: official docs for queueing and peak-traffic communication features.
  - Used for: ethically tolerable scarcity and honest queue design.
  - Limit: tool capability, not product ethics by itself.

- [Steam Early Access](https://partner.steamgames.com/doc/store/earlyaccess)
  - Authority: official distribution rules for unfinished games.
  - Used for: promise discipline, transparency norms, and focused early testing precedent.
  - Limit: paid game distribution context, not browser-hosted room service.

- [FTC dark-pattern subscriptions enforcement](https://www.ftc.gov/news-events/news/press-releases/2021/10/ftc-ramp-enforcement-against-illegal-dark-patterns-trick-or-trap-consumers-subscriptions)
- [FTC dark patterns workshop/report entry](https://www.ftc.gov/consumer-protection?field_mission_tid=All&page=68&type=All)
  - Authority: official US consumer-protection framing.
  - Used for: anti-trick/trap subscription guidance and dark-pattern caution.
  - Limit: broad consumer-protection guidance, not product-specific design advice.

### Secondary Sources

- [cross-lane reading](../../../explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md)
  - Authority: internal synthesis note.
  - Used for: preserving live tensions rather than over-resolving them.
  - Limit: explicitly exploratory, not canonical.

## Bottom Line

- [INFERRED] The strongest current position is not "never charge" and not "pick a monetization model now."
- [INFERRED] It is:
  - use optional support-first models early
  - separate support from access unless and until the project consciously wants service-provider obligations
  - treat scarcity as ethical only when it describes a real operational constraint
  - make any future paid access model wait until the product can actually keep the promises users will hear in it
