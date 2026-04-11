# Lane 01 Findings: Cooperative Scaling And P2P Feasibility

Date: 2026-04-10
Lane: `01-cooperative-scaling-and-p2p-feasibility`
Status: complete

## Question Space

- [CONFIRMED] Prix Guesser's current posture is private-first, host-screen-friendly, browser-first for guests, and explicitly concerned with authoritative room state, reconnect correctness, and low-friction join rather than public-matchmaking scale. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] That makes this lane's real question narrower and harsher than "can browsers talk directly?" The meaningful question is: can any cooperative or peer-assisted model reduce personal hosting risk without breaking authoritative rooms, casual join, or trust among invited guests? (same sources)
- [INFERRED] "Cooperative scaling" hides at least three different possibilities that need separate evaluation: `cooperative room authority`, `cooperative media distribution`, and `cooperative hosting labor`. Treating them as one category would produce a false answer. ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md), [Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md))

## Method And Sources

- [CONFIRMED] I started from the repo-local product and hosting context, especially the current emphasis on host-screen/controller play, authoritative rooms, self-host parity, and the likely LAN -> self-hosted remote -> modest public path. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [CONFIRMED] Primary technical sources were the W3C WebRTC spec, MDN and webrtc.org documentation on signaling, ICE/STUN/TURN, Chrome's page lifecycle documentation, Colyseus docs, Docker docs, and libp2p's official docs. These are strong for capability and constraint claims. ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [webrtc.org connectivity](https://webrtc.org/getting-started/peer-connections), [MDN WebRTC protocols](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols), [Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api), [Colyseus docs](https://docs.colyseus.io/), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/), [libp2p](https://libp2p.io/))
- [CONFIRMED] Secondary and practitioner sources were used only where the official docs were not enough to characterize operational reality or architectural norms: LiveKit docs for why production WebRTC systems centralize transport/routing, and WebTorrent's official FAQ for browser-based peer distribution constraints. These are useful but not neutral. ([LiveKit About](https://docs.livekit.io/intro/about/), [WebTorrent FAQ](https://webtorrent.io/faq))
- [CONFIRMED] Authority limits: none of these sources prove Prix Guesser's future demand profile, real bandwidth bill, or what Logan's friends will personally tolerate. Those parts remain inference or hypothesis until measured in this project. (same sources)

## Inquiry Trajectory

- [CONFIRMED] I began with the hardest version of the question: could live room authority itself become peer-to-peer without violating the roadmap's bias toward canonical room phase, timer, submissions, and scores? ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [Colyseus docs](https://docs.colyseus.io/))
- [CONFIRMED] That immediately branched into network reality: WebRTC does enable peer connections and data channels, but it still requires signaling and often STUN/TURN/ICE negotiation, so "P2P" does not mean "no servers or no operator infrastructure." ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [webrtc.org connectivity](https://webrtc.org/getting-started/peer-connections), [MDN WebRTC protocols](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols))
- [INFERRED] Once that branch made room-state P2P look structurally awkward, the question shifted to a softer form: even if room authority stays centralized or host-authoritative, could media or pack delivery become peer-assisted? ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md), [WebTorrent FAQ](https://webtorrent.io/faq))
- [CONFIRMED] That second branch then pulled in browser lifecycle reality. Hidden or mobile tabs are not reliable background infrastructure, which matters if guests are supposed to keep serving media to each other. ([Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api))
- [INFERRED] The inquiry then widened again into a governance question: if browser swarm models are weak, does "cooperative scaling" really mean trusted friends running whole room servers or helper nodes instead? That is no longer primarily a networking question; it becomes an operator-packaging and trust-distribution question. ([Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/), [Colyseus docs](https://docs.colyseus.io/))
- [INFERRED] Deferred branch: I did not go deep on federation or identity protocol design because the current repo posture is still private-room-centered and does not yet justify a federated social graph discussion. ([PROJECT](../../../PROJECT.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md))

## Branching Paths And Dependencies

- [INFERRED] `authoritative room-state requirement -> whether clients may be trusted to mutate canon -> whether peer authority is acceptable at all`. Prix Guesser's current roadmap strongly biases this branch toward "no" for default play. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [Colyseus docs](https://docs.colyseus.io/))
- [INFERRED] `browser P2P feasibility -> signaling/ICE/TURN reality -> whether guests must install tools or accept relayed traffic -> whether casual join stays low-friction`. The more NAT traversal and relay logic become visible, the less invisible the experience is. ([webrtc.org connectivity](https://webrtc.org/getting-started/peer-connections), [MDN WebRTC protocols](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols))
- [INFERRED] `peer-assisted media distribution -> whether clue assets are large enough to matter economically -> whether browsers stay awake long enough to seed -> whether dedicated supporters are willing to run helper software`. Without a real egress problem, this branch is easy to overvalue. ([Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api), [WebTorrent FAQ](https://webtorrent.io/faq))
- [INFERRED] `community hosting -> packaging quality + version discipline + content distribution + operator trust -> whether the model is a realistic friend-circle backup or an operational burden multiplier`. This is a governance dependency, not just a deployment one. ([Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/), [Colyseus docs](https://docs.colyseus.io/), [Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md))
- [INFERRED] `ethical feasibility -> IP exposure + battery/bandwidth use + opt-in clarity -> whether "cooperative" feels generous or extractive`. This branch became more important as soon as browser peers entered the picture. ([W3C WebRTC](https://www.w3.org/TR/webrtc/))

## Findings

### Feasibility Snapshot

- [INFERRED] `Pure centralized or single-operator authoritative hosting` is technically strongest, operationally simplest, adoption-friendly for guests, economically concentrated on one operator, and ethically straightforward because the trust boundary is clear. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [Colyseus docs](https://docs.colyseus.io/))
- [INFERRED] `Self-host-your-own-room` is technically credible and compatible with authoritative rooms, operationally moderate, adoption-friendly for guests but not operators, economically distributive, and ethically clean inside a trusted circle. ([Colyseus docs](https://docs.colyseus.io/), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/))
- [INFERRED] `Small cooperative community hosting` is technically plausible, operationally harder than it first sounds, adoption-plausible for supporters not casual guests, economically interesting if operator time is shared, and ethically acceptable only with explicit trust/governance. ([Colyseus docs](https://docs.colyseus.io/), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] `Optional peer-assisted media distribution` is technically plausible but brittle in browsers, operationally finicky, adoption-plausible only as an explicit supporter path, economically unproven for Prix Guesser's likely near-term scale, and ethically suspect if hidden from users. ([WebTorrent FAQ](https://webtorrent.io/faq), [Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api))
- [INFERRED] `Browser-to-browser authoritative room state` is technically possible for tiny trusted groups, but operationally weak, adoption-hostile, economically unclear, and ethically/trust-wise the worst fit for the current product direction. ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [webrtc.org connectivity](https://webrtc.org/getting-started/peer-connections), [ROADMAP](../../../ROADMAP.md))

### Full P2P Room Authority Is A Structural Mismatch

- [CONFIRMED] Colyseus explicitly positions itself as an authoritative multiplayer framework with server-defined state synchronization, which matches Prix Guesser's current room-authority direction much better than peer-mutated canon. ([Colyseus docs](https://docs.colyseus.io/))
- [CONFIRMED] WebRTC does support direct peer connections and arbitrary data channels, but the platform documentation is explicit that signaling is outside the core WebRTC API and that ICE/STUN/TURN are part of connection setup. "Peer-to-peer" therefore does not remove infrastructure complexity. ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [webrtc.org connectivity](https://webrtc.org/getting-started/peer-connections), [MDN WebRTC protocols](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols))
- [CONFIRMED] The W3C spec also notes that connection setup can expose candidate network addresses to the application, and potentially to communicating peers, without separate end-user consent. That is a real trust and privacy cost of direct-browser topologies. ([W3C WebRTC](https://www.w3.org/TR/webrtc/))
- [INFERRED] For Prix Guesser, that means full P2P room authority is not just "technically harder." It moves authority, privacy exposure, cheating surface, and recovery burden in the wrong direction relative to the current product intent. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [INFERRED] Even if the friend group is trusted, authoritative timer flow and canonical scoring are exactly the kinds of things that become socially annoying when one guest device becomes the hidden source of truth and then sleeps, refreshes, or disconnects. ([REQUIREMENTS](../../../REQUIREMENTS.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))

### Browser P2P Is More Viable For Experiments Than For The Default Product

- [CONFIRMED] Browser tabs are not dependable background workers. Chrome's page lifecycle guidance explicitly tells developers to handle frozen and discarded states and to close active WebRTC connections when entering `frozen`. ([Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api))
- [INFERRED] That is a bad substrate for invisible cooperative infrastructure because party-game guests will lock phones, switch apps, or let browsers sleep as a normal part of play. ([CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md), [Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api))
- [INFERRED] A tiny trusted-circle experiment could still use WebRTC data channels for a collaborative mode, a local-only prototype, or a research spike about host migration. But that would be a deliberate experiment, not a credible default operating model. ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [webrtc.org connectivity](https://webrtc.org/getting-started/peer-connections))
- [CONFIRMED] Practitioner documentation from LiveKit is revealing here: production WebRTC systems centralize transport, routing, synchronization, NAT traversal, and quality control in a server-side SFU rather than leaving those burdens to a fully meshed browser swarm. That is not a neutral source, but it does reflect the direction of serious realtime deployments. ([LiveKit About](https://docs.livekit.io/intro/about/))
- [INFERRED] Prix Guesser is not shipping video conferencing, so the media bandwidth pressure is lower than in LiveKit's examples. Still, the architectural lesson survives: once reliability and participant invisibility matter, systems tend to re-centralize coordination. ([LiveKit About](https://docs.livekit.io/intro/about/), [ROADMAP](../../../ROADMAP.md))

### Self-Host-Your-Own-Room Is The Strongest Cooperative Model

- [CONFIRMED] Colyseus documents deploy-anywhere and self-host patterns, and Docker Compose remains the standard low-drag way to package a multi-container application so another operator can run it from a shared definition. ([Colyseus docs](https://docs.colyseus.io/), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/))
- [INFERRED] This makes `friend runs a room server` or `trusted supporter runs the game-night box` the most realistic cooperative scaling story. It preserves one authoritative room per host while distributing who bears uptime and infrastructure burden. ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/))
- [INFERRED] For guests, this model can remain nearly invisible if the join surface stays `QR + room code + normal HTTPS URL`, regardless of whether the room sits on Logan's server, a friend's mini-PC, or a modest VPS. ([ROADMAP](../../../ROADMAP.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] The catch is that this is cooperative only at the operator layer. It does not reduce the need for good packaging, explicit update paths, content sync, version compatibility, or incident handling. It just lets more than one trusted person carry those responsibilities. ([Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/))

### Community Hosting Is Plausible, But It Is Governance More Than Networking

- [CONFIRMED] Colyseus documents the move from single-process to multi-process or multi-machine operation via shared presence, which means the framework does not block a later small-host collective or cluster model. ([Colyseus docs](https://docs.colyseus.io/))
- [INFERRED] That keeps `trusted circle of operators each running their own room service` alive as a later path. In practice, this looks less like decentralized swarm magic and more like a hobby co-op of small authoritative hosts. ([Colyseus docs](https://docs.colyseus.io/), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] Operationally, the hard parts are version drift, schema migration timing, pack distribution, secrets handling, logs, and "whose server failed during game night?" None of those are solved by P2P protocols. ([Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/))
- [HYPOTHESIS] This model becomes attractive if the product reaches a stage where "play without Logan" matters inside a trusted F1-friend circle, but still does not justify a polished public SaaS. That is plausible, but not yet evidenced. ([CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))

### Optional Peer-Assisted Distribution Is More Plausible Than Peer-Assisted Authority

- [CONFIRMED] WebTorrent's own FAQ is explicit that a browser WebTorrent client can only connect to peers that support WebTorrent/WebRTC, and browser downloading requires content to be seeded by a WebRTC-capable client. This is not "free browser CDN." ([WebTorrent FAQ](https://webtorrent.io/faq))
- [CONFIRMED] That means peer-assisted media distribution still needs the right seeders, the right tracker behavior, and peers that remain alive. In the browser it is not enough to publish an ordinary file and expect swarm pickup. ([WebTorrent FAQ](https://webtorrent.io/faq))
- [INFERRED] For Prix Guesser, peer-assisted distribution is most plausible only for static pack assets or larger reveal media, not for live room state. That distinction matters because static media can tolerate delay, retries, and temporary peer scarcity in ways canonical timers and submissions cannot. ([REQUIREMENTS](../../../REQUIREMENTS.md), [WebTorrent FAQ](https://webtorrent.io/faq))
- [INFERRED] Even then, browser-only seeding is fragile because guests are on mobile browsers, background tabs freeze, and party sessions are short. A real supporter path would more likely involve a desktop helper, a Node process, or a dedicated always-on seeder than ordinary guest browsers. ([Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api), [WebTorrent FAQ](https://webtorrent.io/faq))
- [INFERRED] Economically, this only becomes attractive if measurement shows egress for media dominates cost. For the current likely scale, operator time and reachability may still be the bigger problem than bandwidth. ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))

## Could This Ever Be Invisible Enough For Casual Users?

- [INFERRED] `Pure browser P2P room authority`: no. Even if the join UI looked simple, the hidden costs are peer dependence, NAT/relay fragility, IP exposure, and failure modes that surface as "someone's phone broke the room." That is not invisible in the way casual guests need. ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api), [ROADMAP](../../../ROADMAP.md))
- [INFERRED] `Guest-side Tailscale or similar overlay requirement`: maybe for a narrow trusted-friend MVP, but not invisible enough for general casual invites. It adds install, auth, and support burden to the wrong side of the room boundary. ([continue-here](../../../phases/01-authored-round-contract/.continue-here.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] `Self-hosted or community-hosted authoritative room behind normal HTTPS`: yes for guests, no for operators. This is the cleanest path where the cooperative part stays off the guest's critical path. ([ROADMAP](../../../ROADMAP.md), [Colyseus docs](https://docs.colyseus.io/), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/))
- [INFERRED] `Optional peer-assisted media seeding`: maybe partly invisible at play time, but only if it is explicit opt-in for supporters and easy to disable. Silent use of guest battery, bandwidth, or IP exposure would fail the ethical side of "invisible." ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [WebTorrent FAQ](https://webtorrent.io/faq))
- [INFERRED] The strongest current answer is therefore asymmetric: cooperative infrastructure can become invisible enough for casual guests only when the cooperative burden is carried by trusted operators or explicit supporters, not by every invited player. ([PROJECT](../../../PROJECT.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md))

## Gray Areas And Live Tensions

- [INFERRED] `Financial risk vs operational risk`: peer assistance sounds like a way to reduce hosting cost, but in a small private-room product the bigger scarce resource may be maintainer attention, not egress. A cheaper architecture that is harder to debug may be a net loss. ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] `Trust among friends vs trust in infrastructure`: private-friend circles can tolerate more friction and more informal trust than public products, but that does not automatically make peer authority wise. Social trust does not eliminate debugging pain or fairness disputes. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md))
- [INFERRED] `Privacy vs decentralization`: direct peer topologies can lower central hosting dependence, but they also expose more about each participant's network and device behavior to other peers or the application. ([W3C WebRTC](https://www.w3.org/TR/webrtc/))
- [INFERRED] `Optional support vs invisible extraction`: a supporter willingly running a helper node is ethically different from a guest silently becoming part of a swarm. Cooperative compute gets morally blurry when the contribution is hidden. ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api))
- [INFERRED] `Authoritative competition vs collaborative analysis`: a future co-op or analyst mode might tolerate weaker room authority than the competitive anchor mode. That keeps a narrow P2P experimental branch alive, but only in a mode-specific way. ([continue-here](../../../phases/01-authored-round-contract/.continue-here.md), [Product Futures](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))
- [HYPOTHESIS] `Public future vs private present`: if the product later adds public daily challenges or streamer-heavy traffic, media distribution economics may change enough that today's dismissal of peer-assisted distribution becomes too conservative. That remains unmeasured. ([CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md), [Product Futures](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md))

## Scope Expansions

- [CONFIRMED] `Scope Expansion`: the lane began as a networking question and expanded into packaging and governance because the most credible cooperative model turned out to be trusted operators running authoritative rooms, not browsers self-organizing. I pursued this expansion because otherwise the lane would have answered the wrong version of the problem. ([Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/), [Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md))
- [CONFIRMED] `Scope Expansion`: privacy and consent became first-order once WebRTC candidate exposure and hidden peer contribution entered the picture. I pursued this moderately because "technically possible" is not enough for a social product. ([W3C WebRTC](https://www.w3.org/TR/webrtc/))
- [CONFIRMED] `Scope Expansion`: the lane widened from `P2P room state` to `peer-assisted static media` because these are often conflated in decentralization talk but have very different failure tolerance. I pursued this deeply because it is the one branch where some cooperative assistance still seems technically alive. ([WebTorrent FAQ](https://webtorrent.io/faq))
- [INFERRED] `Scope Expansion flagged, not deeply pursued`: federation and cross-host identity. This emerged implicitly once community hosting became plausible, but I deferred it because the current repo posture is still private-room-first and not account-centric. ([PROJECT](../../../PROJECT.md), [REQUIREMENTS](../../../REQUIREMENTS.md))

## Rival Models Still Alive

- [INFERRED] `Model A: keep everything owner-hosted or centrally hosted`. This remains the simplest and strongest default until real cost or uptime pain says otherwise. ([PROJECT](../../../PROJECT.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] `Model B: distribute hosting by letting trusted operators run whole room servers`. This is the strongest cooperative alternative and deserves to stay alive because it aligns with authoritative rooms and guest simplicity. ([Colyseus docs](https://docs.colyseus.io/), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/))
- [INFERRED] `Model C: small cooperative host collective`. This remains viable if the project wants resilience and "play without Logan" before it wants public-scale ops. ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] `Model D: optional supporter-run seeders for large static media`. This is not strong now, but it remains alive if future measurement shows bandwidth-heavy public or semi-public asset distribution. ([WebTorrent FAQ](https://webtorrent.io/faq))
- [HYPOTHESIS] `Model E: tiny-group P2P collaborative mode`. This is still alive only as an experimental side branch for trusted, low-stakes, perhaps co-op analysis play. It is not alive as the main room model. ([W3C WebRTC](https://www.w3.org/TR/webrtc/), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))

## Practical Implications

### Thinking Implications

- [INFERRED] Treat `cooperative scaling` as three separate design questions from now on: `who hosts authority`, `who pays to serve static assets`, and `who carries operator labor`. A single yes/no verdict on "P2P" would mislead future planning. ([Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md))
- [INFERRED] Keep using `authoritative room` as the default mental model unless a later mode deliberately chooses weaker trust guarantees. That keeps the main product honest about fairness and recovery expectations. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))

### Design Implications

- [INFERRED] Protect a stable guest join grammar that does not reveal or care who is hosting the room. If cooperation is ever introduced, it should happen behind the same `URL + code + QR` join pattern. ([ROADMAP](../../../ROADMAP.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] Keep pack and media artifacts packageable, cacheable, and addressable independently from live room state. That is useful for centralized hosting today and any later peer-assisted distribution experiment. ([REQUIREMENTS](../../../REQUIREMENTS.md), [WebTorrent FAQ](https://webtorrent.io/faq))
- [INFERRED] Do not design future live rooms around guest devices serving as infrastructure. Design guest devices as disposable controllers that may vanish, sleep, or reconnect. ([Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api), [REQUIREMENTS](../../../REQUIREMENTS.md))

### Implementation Implications

- [INFERRED] Put effort into authoritative room packaging before any P2P experiment: one-command local host, one-command self-host bundle, clear environment setup, and versioned content sync. That is higher leverage than browser swarming right now. ([Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] If a cooperative experiment happens, constrain it to static asset seeding or supporter-run helper nodes first. Do not entangle the main scoring/timer canon with peer contribution. ([WebTorrent FAQ](https://webtorrent.io/faq), [ROADMAP](../../../ROADMAP.md))
- [INFERRED] Build explicit host metadata and mode labeling early enough that future cooperative-host or community-host models can tell users whether they are in `local`, `private hosted`, or `community-hosted` play. Trust improves when topology is legible. ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))

### Measurement Or Experiment Implications

- [INFERRED] Measure bandwidth by category before discussing peer assistance seriously: `room state traffic`, `clue asset delivery`, `reveal media`, and `spectator/stream traffic` are different cost centers. ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] Run one narrow experiment with a supporter-run seeder or alternate host before designing a general contribution system. The key question is whether cooperation actually removes pain in this project's size regime. (same source)
- [INFERRED] Test a trusted-friend self-host bundle earlier than a browser-swarm prototype. That experiment answers the more plausible branch of the problem. ([Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/), [Colyseus docs](https://docs.colyseus.io/))

### What Different People Can Reasonably Be Asked To Do

- [INFERRED] `Casual invited guest`: open a normal HTTPS link, scan a QR code, enter a room code, maybe keep the tab open while playing. They should not be expected to install Tailscale, manage port forwarding, run a helper process, or silently seed data for strangers. ([PROJECT](../../../PROJECT.md), [continue-here](../../../phases/01-authored-round-contract/.continue-here.md))
- [INFERRED] `Enthusiast supporter`: optionally run a packaged room server, a Docker bundle, or later a dedicated helper/seeder with explicit opt-in and clear off-switches. They might tolerate some setup if it clearly helps the group. ([Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
- [INFERRED] `Technically confident operator`: run authoritative rooms, handle updates, own a tunnel or VPS, manage logs/secrets/backups, and possibly participate in a small cooperative hosting circle. This is the only actor class for whom community-hosting governance is realistic. ([Colyseus docs](https://docs.colyseus.io/), [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/))

## What Would Change This View

- [HYPOTHESIS] Measured evidence that static media egress, not operator labor or room reachability, is the dominant real cost.
- [HYPOTHESIS] Strong evidence that the friend group is comfortable installing a helper app or knowingly contributing bandwidth.
- [HYPOTHESIS] A later mode shift toward collaborative, low-stakes co-op play where weaker authority is acceptable.
- [HYPOTHESIS] A product shift toward public daily challenges or streamer-scale viewership that materially changes the economics of asset delivery.
- [HYPOTHESIS] Clear improvement in browser-native P2P ergonomics across signaling, relay, lifecycle reliability, and privacy handling.

## Open Questions Worth A Third Pass

1. [INFERRED] Is the first real scaling pain for Prix Guesser likely to be `bandwidth`, `room-state reliability`, or `operator time`?
2. [INFERRED] How large are the eventual clue and reveal media artifacts likely to become once the content corpus matures?
3. [INFERRED] Would a trusted-friend self-host bundle actually get used, or would everyone still prefer Logan-hosted sessions?
4. [HYPOTHESIS] Is there a later co-op analyst mode where a small P2P experiment would feel socially right rather than operationally perverse?
5. [INFERRED] What minimum release-signing, versioning, and pack-sync discipline would a small community-host circle need before it becomes trustworthy?
6. [HYPOTHESIS] If supporter-run seeders ever exist, how explicit does opt-in need to be for the model to remain ethically clean?

## Source Ledger

### Primary Internal Sources

- [PROJECT](../../../PROJECT.md)
  - Authority: current product posture, audience, and constraints.
  - Limit: intent, not usage evidence.
- [ROADMAP](../../../ROADMAP.md)
  - Authority: current phase sequencing and authoritative-room direction.
  - Limit: present strategy, not future validation.
- [REQUIREMENTS](../../../REQUIREMENTS.md)
  - Authority: concrete room, reconnect, and join expectations.
  - Limit: requirement targets, not implemented behavior.
- [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md)
  - Authority: current exploration context and unresolved hosting/product tensions.
  - Limit: exploratory synthesis.
- [continue-here](../../../phases/01-authored-round-contract/.continue-here.md)
  - Authority: strong handoff context about likely operating stages and audience expectations.
  - Limit: pause memo, not canonical product doctrine.
- [Product Futures](../../2026-04-10-vision-hosting-wave/findings/01-product-futures.md)
- [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md)
- [Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md)
  - Authority: recent repo-local research directly adjacent to this lane.
  - Limit: previous-lane synthesis, not production telemetry.

### Primary External Sources

- [W3C WebRTC](https://www.w3.org/TR/webrtc/)
  - Used for: baseline platform capability, ICE/STUN/TURN context, privacy implications.
  - Reliability limit: specification-level document, not deployment advice.
- [webrtc.org connectivity](https://webrtc.org/getting-started/peer-connections)
  - Used for: signaling and ICE connection setup realities.
  - Reliability limit: Google-authored guidance, focused on platform usage not business fit.
- [MDN WebRTC protocols](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols)
  - Used for: STUN/TURN/ICE explanations and relay realities.
  - Reliability limit: explanatory documentation, not formal standard text.
- [Chrome Page Lifecycle API](https://developer.chrome.com/blog/page-lifecycle-api)
  - Used for: hidden/frozen/discarded tab behavior and why browsers are weak background infrastructure.
  - Reliability limit: Chrome-focused platform guidance.
- [Colyseus docs](https://docs.colyseus.io/)
  - Used for: authoritative game-server posture, deploy-anywhere, and scaling model.
  - Reliability limit: framework-specific worldview.
- [Docker Compose](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/)
  - Used for: portable self-host packaging implications.
  - Reliability limit: packaging, not user-adoption evidence.
- [libp2p](https://libp2p.io/)
  - Used for: confirming that modern P2P stacks still rely on transports, hole punching, and relay support rather than magical universal direct connectivity.
  - Reliability limit: project-level framing, not Prix Guesser-specific ops guidance.

### Secondary / Practitioner Sources

- [LiveKit About](https://docs.livekit.io/intro/about/)
  - Authority: strong practitioner signal from a production realtime stack.
  - Used for: why serious WebRTC deployments centralize transport/routing rather than rely on full mesh.
  - Reliability limit: vendor/product bias.
- [WebTorrent FAQ](https://webtorrent.io/faq)
  - Authority: official project documentation for browser torrent behavior.
  - Used for: browser peer restrictions and seeding requirements.
  - Reliability limit: project-specific and optimistic toward its own approach.

## Bottom Line

- [INFERRED] The strongest current answer is not "P2P is impossible." It is "full peer-to-peer room authority is the wrong fit, while operator-level cooperation and maybe later supporter-level asset distribution remain alive."
- [INFERRED] If Prix Guesser wants cooperative scaling without betraying its likely room model, the first serious branch to protect is `self-hostable authoritative rooms`, not `browser swarm magic`.
