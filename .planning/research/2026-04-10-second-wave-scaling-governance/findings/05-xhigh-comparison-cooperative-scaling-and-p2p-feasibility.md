# Lane 05 Findings: XHigh Comparison On Cooperative Scaling And P2P Feasibility

Date: 2026-04-10
Lane: `05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility`
Status: complete

## Question Space

- [CONFIRMED] Prix Guesser's current posture is still private-first, host-screen-friendly, browser-first for guests, and explicitly concerned with authoritative room state, reconnect correctness, and low-friction join rather than public-matchmaking scale. ([PROJECT](../../../PROJECT.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md))
- [CONFIRMED] This lane exists as a deliberate comparison pass on the same broad problem as lane `01`, with the explicit goal of surfacing materially different tensions, hidden assumptions, or dependency structures rather than "correcting" the first pass. ([00-ORCHESTRATION](../00-ORCHESTRATION.md), [charter](../specs/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md), [lane 01](./01-cooperative-scaling-and-p2p-feasibility.md))
- [INFERRED] The biggest hidden question is not "can peers help?" It is "which real bottleneck is cooperative scaling supposed to relieve: authoritative room cost, static asset egress, uptime resilience, operator labor, or community ethos?" Until that is named, P2P discussion stays too abstract to guide strategy. ([lane 01](./01-cooperative-scaling-and-p2p-feasibility.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md), [Funding](./02-funding-access-and-transparency-models.md))
- [INFERRED] Once that bottleneck question is explicit, "P2P feasibility" stops being one answer. It becomes three actor-specific questions: what a casual invited guest can be asked to do, what an enthusiast supporter can opt into, and what only a technically confident operator can carry. ([base charter](../specs/01-cooperative-scaling-and-p2p-feasibility.md), [charter](../specs/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md))

## Method And Sources

- [CONFIRMED] I read the required internal context first, then the base cooperative-scaling charter, the session checkpoint, and the completed lane `01` findings because they already existed and this lane is explicitly comparative. ([00-ORCHESTRATION](../00-ORCHESTRATION.md), [charter](../specs/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md), [base charter](../specs/01-cooperative-scaling-and-p2p-feasibility.md), [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md), [lane 01](./01-cooperative-scaling-and-p2p-feasibility.md))
- [CONFIRMED] I treated lane `01` as a baseline and looked specifically for three things: where deeper reasoning changed the framing, where it exposed a hidden dependency, and where it separated models that a shallower pass would lump together. ([lane 01](./01-cooperative-scaling-and-p2p-feasibility.md))
- [CONFIRMED] Primary external sources were official documentation on WebRTC signaling and ICE/TURN behavior, browser lifecycle constraints, WebRTC data channels, WebRTC privacy tradeoffs, Colyseus room/auth/reconnect/scaling behavior, and Docker Compose packaging. These are strong for capability and constraint claims. ([WebRTC Peer Connections](https://webrtc.org/getting-started/peer-connections), [MDN WebRTC protocols](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols), [MDN Using WebRTC data channels](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels), [RFC 8828](https://datatracker.ietf.org/doc/rfc8828/), [Chrome Page Lifecycle API](https://developer.chrome.com/docs/web-platform/page-lifecycle-api), [Colyseus Room Authentication](https://docs.colyseus.io/auth/room), [Rooms](https://docs.colyseus.io/room), [Reconnection](https://docs.colyseus.io/room/reconnection), [Presence](https://docs.colyseus.io/server/presence), [Scalability](https://docs.colyseus.io/scalability), [Docker Compose](https://docs.docker.com/compose/intro/features-uses/))
- [CONFIRMED] Secondary or practitioner-facing sources were used only to sharpen operational realism where official standards alone are too abstract. LiveKit is useful as a vendor-shaped signal about how production WebRTC systems recentralize connection complexity, and WebTorrent's FAQ is useful as an official-project signal about browser swarm limits. Neither is neutral. ([LiveKit Transport](https://docs.livekit.io/transport/), [WebTorrent FAQ](https://webtorrent.io/faq))
- [CONFIRMED] Limits remain important: there is still no Prix Guesser telemetry for asset sizes, TURN usage, egress cost, self-host adoption, or operator time. That means the strategic claims here are mostly inferences about likely pain order, not measured proof. ([Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md), [Funding](./02-funding-access-and-transparency-models.md), [Security](./04-security-trust-and-operational-risk.md))

## Inquiry Trajectory

1. [CONFIRMED] I began by re-testing lane `01`'s harshest conclusion: that browser-to-browser authoritative rooms are a poor default fit for Prix Guesser's room contract. ([lane 01](./01-cooperative-scaling-and-p2p-feasibility.md), [ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
2. [INFERRED] Instead of stopping at "WebRTC is complicated," I asked what exact problem cooperative scaling is meant to solve. That immediately exposed a hidden dependency: if the scarce resource is operator time, moderation, or reconnect trust rather than egress, peer distribution may be technically clever but strategically irrelevant. ([Funding](./02-funding-access-and-transparency-models.md), [Security](./04-security-trust-and-operational-risk.md))
3. [CONFIRMED] I then split the topology question into three layers: canonical gameplay state, static clue or reveal assets, and hosting labor or uptime. ([lane 01](./01-cooperative-scaling-and-p2p-feasibility.md), [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md))
4. [INFERRED] That split surfaced a deeper asymmetry: the more central a function is to fairness, timers, and recovery, the worse the fit for ad hoc peer contribution; the more peripheral and cacheable it is, the more experimentation remains alive.
5. [INFERRED] The next branch was actor-specific. "Invisible enough" means one thing for a casual guest, another for a supporter who opts in, and another for an operator willing to run infrastructure. Averaging those actors hides the real adoption boundary.
6. [INFERRED] From there the lane widened into governance. Multiple authoritative hosts, mirrored content, or supporter-run seeders are not just network topologies; they decide who is accountable when privacy, moderation, version skew, or uptime problems occur. ([Funding](./02-funding-access-and-transparency-models.md), [Security](./04-security-trust-and-operational-risk.md))
7. [INFERRED] I ended by asking whether these extra branches overturn lane `01`. They do not. They mostly explain why lane `01`'s answer is directionally right, while making the dependency structure more explicit and less network-centric.

## Branching Paths And Dependencies

- [INFERRED] `Which wrapper becomes primary -> how strong room authority must be -> whether plural authorities or host migration are acceptable`. A competitive, host-screen, private-room anchor mode pushes strongly toward canonical server authority; a later collaborative analyst mode might not.
- [INFERRED] `Which cost dominates -> whether peer assistance matters economically`. If the real pain is operator setup, moderation, or reconnect debugging, peer media distribution does very little.
- [INFERRED] `Who is being asked to help -> whether adoption survives`. Casual guest tolerance is near zero; supporter tolerance is conditional and must be explicit; operator tolerance can be high but is scarce.
- [INFERRED] `Whether asset delivery is separable from live state -> whether P2P can be confined to the periphery`. Static pack assets can tolerate retries, cache misses, and temporary seed scarcity; authoritative timer or scoring state cannot.
- [INFERRED] `How many authoritative hosts exist -> how much governance surface appears`. Once more than one authoritative host exists, versioning, pack sync, disclosure, moderation posture, and support ownership stop being side issues.
- [INFERRED] `How public the product becomes -> how much identity, telemetry, and trust process is required`. A cooperative topology that feels acceptable in a known-circle context may become ethically or operationally unacceptable in streamer-visible or semi-public rooms.
- [INFERRED] `How much privacy is traded for performance -> whether direct peer paths are tolerable`. RFC 8828 makes clear that WebRTC path selection can expose more network information than plain HTTP. That cost matters more when contribution is hidden or participation is casual. ([RFC 8828](https://datatracker.ietf.org/doc/rfc8828/))

## Findings

### What This Pass Changes Relative To Lane 01

- [INFERRED] This pass agrees with lane `01`'s main answer: full peer-to-peer room authority remains the weakest fit for Prix Guesser's likely anchor mode. ([lane 01](./01-cooperative-scaling-and-p2p-feasibility.md))
- [INFERRED] The main difference is framing. Lane `01` still treated the space partly as a menu of deployment options. This pass makes a stronger claim: the first-order question is not topology but bottleneck identity. If cooperative scaling is not aimed at the actual scarce resource, it is mostly architectural theater.
- [INFERRED] The deepest newly visible dependency is `product wrapper -> authority contract -> acceptable plurality of hosts -> governance burden`. That dependency is stronger and more explanatory than the simpler `centralized versus decentralized` framing.
- [INFERRED] This pass is also harsher about actor averaging. A model can be technically feasible and ethically acceptable for operators while still being adoption-hostile for the actual guest journey. That mismatch is where shallower reasoning most often goes wrong.

### Feasibility By Model

- [INFERRED] `Owner-hosted or officially hosted authoritative rooms`: technical feasibility is highest; operational feasibility is highest for the guest path; adoption feasibility is strongest because join remains normal HTTPS plus room code; economic feasibility is concentrated on one operator; ethical feasibility is highest because responsibility is clear.
- [INFERRED] `Self-host-your-own-room authoritative model`: technical feasibility remains high because it preserves a single room authority rather than peer-mutated canon; operational feasibility is medium because packaging, updates, and content sync matter; adoption feasibility is high for guests but low for operators; economic feasibility is attractive if trusted friends actually host; ethical feasibility is good because contribution is explicit.
- [INFERRED] `Trusted-circle cooperative hosting or sanctioned mirrors`: technical feasibility is medium-high; operational feasibility is medium-low because plural hosts create versioning and accountability work; adoption feasibility is low for general users but medium for a small technical circle; economic feasibility can reduce sole-operator burden; ethical feasibility depends on very clear official and unofficial host boundaries.
- [INFERRED] `Optional supporter-run static asset seeding`: technical feasibility is medium; operational feasibility is low-medium because browser peers are brittle and WebTorrent-style browser distribution only works with WebRTC-capable peers and seeders; adoption feasibility is low for casuals and medium only for opt-in supporters; economic feasibility is unproven until asset egress is actually measured; ethical feasibility is weak if contribution is silent and better if it is explicit, bounded, and easily disabled. ([WebTorrent FAQ](https://webtorrent.io/faq))
- [INFERRED] `Browser-to-browser authoritative room state`: technical feasibility exists in the narrow sense that browsers can exchange encrypted data over data channels, but operational feasibility is poor, adoption feasibility is poor, economic feasibility is unclear, and ethical feasibility is weak because privacy, debugging, and responsibility all get worse at once. ([MDN Using WebRTC data channels](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels), [RFC 8828](https://datatracker.ietf.org/doc/rfc8828/), [Chrome Page Lifecycle API](https://developer.chrome.com/docs/web-platform/page-lifecycle-api))

### Canonical State And Peripheral Assistance Must Be Kept Separate

- [CONFIRMED] Colyseus's room model keeps each room attached to a single process, with room auth, message limits, reconnect handling, and distributed scaling handled explicitly by the server-side room lifecycle rather than by peer consensus. ([Colyseus Room Authentication](https://docs.colyseus.io/auth/room), [Rooms](https://docs.colyseus.io/room), [Reconnection](https://docs.colyseus.io/room/reconnection), [Scalability](https://docs.colyseus.io/scalability))
- [INFERRED] That makes the main anchor mode's fairness contract structurally server-shaped. The more the product cares about canonical timer state, submissions, scores, reconnect recovery, and host-screen legibility, the less sensible it is to place canon on an invited guest device or browser swarm. ([ROADMAP](../../../ROADMAP.md), [REQUIREMENTS](../../../REQUIREMENTS.md))
- [CONFIRMED] MDN's data-channel docs do confirm that peer-to-peer data can be encrypted and bypass the application server once established. ([MDN Using WebRTC data channels](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels))
- [INFERRED] That is a real technical advantage, but it is not the advantage Prix Guesser most urgently needs. Privacy-preserving direct transport is not the same thing as reliable authoritative session control.

### Networking Reality Still Pushes Toward Coordination Infrastructure

- [CONFIRMED] webrtc.org and MDN both state that WebRTC connection setup still needs signaling plus ICE/STUN/TURN logic, and that TURN relay is often needed when direct paths fail. webrtc.org goes further and notes that most commercial WebRTC services use TURN. ([WebRTC Peer Connections](https://webrtc.org/getting-started/peer-connections), [MDN WebRTC protocols](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols))
- [CONFIRMED] RFC 8828 makes clear that WebRTC path selection involves privacy and media-quality tradeoffs and can expose more network information than a normal HTTP interaction. ([RFC 8828](https://datatracker.ietf.org/doc/rfc8828/))
- [INFERRED] So "P2P" is not an escape hatch from infrastructure. It mostly relocates infrastructure from obvious app servers to signaling, relay, NAT-traversal, and privacy-management machinery.
- [CONFIRMED] LiveKit's transport docs, while vendor-shaped, explicitly present server and client SDKs as handling WebRTC connection complexity, network adaptation, and state synchronization for production-ready realtime apps. ([LiveKit Transport](https://docs.livekit.io/transport/))
- [INFERRED] That is not neutral proof, but it is a useful practitioner signal: once invisibility and cross-platform reliability matter, serious realtime systems tend to re-centralize the hard parts rather than leave them in a browser mesh.

### Browser Lifecycle Reality Is A Product Constraint, Not Just A Technical Detail

- [CONFIRMED] Chrome's lifecycle guidance says modern browsers may suspend or discard pages and explicitly advises developers to close active WebRTC connections when a page freezes. ([Chrome Page Lifecycle API](https://developer.chrome.com/docs/web-platform/page-lifecycle-api))
- [INFERRED] That means guest browsers should be modeled as disposable controllers that may vanish, sleep, or background themselves at any time.
- [INFERRED] A shallower pass might treat this as an implementation nuisance. In this lane it is more serious: it undercuts the fantasy that ordinary party guests can invisibly double as reliable infrastructure.

### The Economic Case For Peer Assistance Is Much Narrower Than The Technical Case

- [INFERRED] The economic story for peer assistance only becomes compelling if clue or reveal asset egress, relay spend, or some later large-scale media pattern is one of the first real bottlenecks.
- [INFERRED] The current repo and adjacent second-wave lanes still point elsewhere: operator time, packaging quality, reconnect trust, moderation, and host clarity are more likely early pain points than raw bandwidth. ([Funding](./02-funding-access-and-transparency-models.md), [Security](./04-security-trust-and-operational-risk.md))
- [INFERRED] That does not kill cooperative distribution forever. It does mean that early enthusiasm for it is likely to be misallocated effort unless measurement later shows static media costs dominating.
- [INFERRED] In other words: the most plausible cooperative move in the near to medium term is distributing who runs authoritative rooms, not distributing every round's traffic.

### Topology And Governance Are Coupled

- [CONFIRMED] Docker's Compose docs explicitly frame Compose as one YAML-defined way to share and run multi-container apps, including production deployments on single hosts. ([Docker Compose](https://docs.docker.com/compose/intro/features-uses/))
- [CONFIRMED] Colyseus's scalability and presence docs likewise assume explicit shared presence, shared drivers, and publicly reachable processes when scaling beyond one process or machine. ([Presence](https://docs.colyseus.io/server/presence), [Scalability](https://docs.colyseus.io/scalability))
- [INFERRED] That makes operator-level cooperation realistic. But once multiple hosts can run the stack, the problem is no longer just deployment; it is version discipline, pack distribution, support ownership, privacy disclosure, and trust labeling.
- [INFERRED] This is the strongest xhigh-only emphasis: `community hosting` is not a cheaper version of centralized hosting. It is a different governance model wearing a deployment costume.
- [INFERRED] That means the funding, trust, and public-transition lanes are not external to cooperative scaling. They partially determine whether cooperative scaling even counts as success. ([Funding](./02-funding-access-and-transparency-models.md), [Security](./04-security-trust-and-operational-risk.md))

## Could This Ever Be Invisible Enough For Casual Users?

- [INFERRED] `Casual invited guest`: the ceiling is low. Opening a normal HTTPS link, scanning a QR code, entering a room code, and maybe keeping the tab in the foreground is reasonable. Installing overlay networking, running a helper process, accepting battery or bandwidth donation as a default, or depending on their device to preserve room canon is not.
- [INFERRED] `Enthusiast supporter`: optional contribution can be broader. A supporter might reasonably run a packaged room server, maintain a small always-on host, or opt into bounded static asset seeding if the value is concrete and the off-switch is clear.
- [INFERRED] `Technically confident operator`: the highest burden fits here. Running authoritative rooms, managing updates and secrets, monitoring logs, publishing a host behind normal HTTPS, or participating in a trusted host collective are all plausible.
- [INFERRED] The asymmetry matters. Cooperative infrastructure becomes invisible enough for casual users only when the cooperative burden is carried entirely by supporters or operators outside the guest's critical path.
- [INFERRED] So the right answer is not simply "yes, P2P can be invisible" or "no, it cannot." It is: only operator-layer cooperation can plausibly be invisible enough for the default guest journey.

## Where A Shallower Pass Might Go Wrong

- [INFERRED] It may confuse `browsers can exchange data` with `guest devices can be relied on as invisible infrastructure`.
- [INFERRED] It may assume the problem to be solved is raw compute or bandwidth cost, when the earlier real bottlenecks are more likely operator labor, reconnect correctness, moderation, and support clarity.
- [INFERRED] It may treat `community hosting`, `browser peer relays`, and `supporter-run authoritative rooms` as one family of decentralization, even though they create different trust and governance shapes.
- [INFERRED] It may blur static asset delivery together with authoritative gameplay state. The first can tolerate scarcity and retries; the second cannot.
- [INFERRED] It may average together casual guests, enthusiasts, and operators and then report a misleading middle answer.
- [INFERRED] It may interpret encrypted peer transport as an unqualified privacy win while overlooking address exposure, debugging blind spots, and responsibility ambiguity.
- [INFERRED] It may assume that if a peer-assisted branch is technically possible, it is strategically wise for the current stage. That step is not justified by the evidence.

## If This Were Tried, What Would Need To Be Proven Experimentally?

- [INFERRED] `Self-hostable authoritative rooms` would need proof that a trusted non-Logan operator can start the stack, publish a stable join surface, keep pack versions aligned, and recover common failures without direct maintainer intervention.
- [INFERRED] `Trusted-circle host collective` would need proof that users can tell which hosts are official or sanctioned, that version skew is manageable, and that privacy and support expectations remain legible.
- [INFERRED] `Opt-in static asset seeding` would need proof that static media egress is actually a meaningful cost center, that supporter seeders stay online long enough to matter, and that the swarm meaningfully reduces origin cost or latency without confusing guests.
- [INFERRED] `Any guest-side peer contribution` would need proof that users understand what is happening, can opt out without penalty, and do not experience battery, backgrounding, or privacy surprises.
- [INFERRED] `Any weakened-authority peer mode` would need proof that the social format actually benefits from looser canon. A future co-op analyst mode might pass that test; the competitive anchor mode probably will not.
- [INFERRED] Across all branches, the most important measurements are not "maximum peers" first. They are operator minutes per session, reconnect success, asset egress mix, host-label comprehension, and whether the cooperative branch removes more pain than it creates.

## Gray Areas And Live Tensions

- [INFERRED] `Personal financial risk versus canonical trust`: distributing hosting can lower sole-operator cost and availability risk, but it also weakens one-clear-authority trust unless host boundaries are extremely clear.
- [INFERRED] `Privacy versus observability`: peer delivery can keep some traffic off the app server, but it can also expose more network metadata between peers and reduce the operator's ability to diagnose failures cleanly.
- [INFERRED] `Cooperative ethos versus product legibility`: asking supporters to help can feel aligned and communal; asking casual guests to help by default can feel extractive even if technically elegant.
- [INFERRED] `Private trusted-circle tolerance versus future public transition`: a friend circle can survive more informal trust and operational mess than a semi-public hosted beta. A cooperative model that works socially now may become unacceptable later.
- [INFERRED] `Single canonical service versus plural host ecology`: a self-host or host-collective story preserves autonomy, but it also changes what the product is. Users stop interacting with one canonical service and start interacting with a family of hosts.
- [HYPOTHESIS] `Competitive anchor mode versus future collaborative mode`: it remains plausible that a later analyst or co-op wrapper could make narrower peer experiments feel right. That possibility should stay alive without being smuggled into the default room model.

## Scope Expansions

- [CONFIRMED] `Scope Expansion`: the comparison pass moved from `is P2P technically feasible?` to `what bottleneck is cooperative scaling actually trying to relieve?` I pursued this because the answer changes completely depending on whether the scarce resource is bandwidth, operator time, or trust.
- [CONFIRMED] `Scope Expansion`: the lane widened from topology into governance. I pursued this deeply because the most plausible cooperative path is not browser swarm logic but plural authoritative hosts, which is primarily a responsibility-distribution question.
- [CONFIRMED] `Scope Expansion`: the lane became more actor-specific than lane `01`. I pursued this because "invisible enough" is meaningless unless the beneficiary and the contributor are different named roles.
- [INFERRED] `Scope Expansion flagged, not deeply pursued`: content signing, pack-mirror verification, and cross-host moderation policy. These emerged once plural hosts stayed alive, but they deserve a third-pass governance lane more than deeper treatment here.

## Rival Models Still Alive

- [INFERRED] `Model A: single official authoritative hosting path`. This remains the cleanest baseline and the easiest to reason about honestly.
- [INFERRED] `Model B: self-hostable authoritative rooms for trusted operators`. This is still the strongest cooperative branch because it preserves canonical room authority and keeps guest friction low.
- [INFERRED] `Model C: sanctioned trusted-circle host collective`. This remains alive if the project later wants resilience and "play without Logan" without becoming a full public SaaS.
- [INFERRED] `Model D: opt-in supporter seeding for large static assets`. This stays alive only as a later peripheral experiment, contingent on measured asset-delivery pain.
- [HYPOTHESIS] `Model E: mode-specific peer experiment`. A future co-op or analyst wrapper might justify a small-scale peer-authority or host-migration experiment, but only as a deliberate side branch.

## Practical Implications

### Thinking Implications

- [INFERRED] Stop using `P2P` as the main category. The more useful categories are `who owns canon`, `who serves static assets`, `who carries operator labor`, and `who is accountable when something breaks`.
- [INFERRED] Treat cooperative scaling as a staging question, not a permanent architecture question. Different wrappers may justify different answers later.
- [INFERRED] Treat topology choices as trust and governance choices. A second host is not just more capacity; it is another authority surface.

### Design Implications

- [INFERRED] Preserve a guest join grammar that does not care which trusted operator is hosting the room, but do make hosting and privacy mode legible enough that users know whether they are in an official, self-hosted, or community-hosted environment.
- [INFERRED] Keep live room state clearly separate from cacheable pack and media artifacts so that any later asset-distribution experiment can stay outside the fairness-critical path.
- [INFERRED] Design guest controllers as disposable and reconnectable, not as infrastructure participants.

### Implementation Implications

- [INFERRED] Invest first in a robust self-hostable authoritative bundle: versioned deployment, clear secrets and config handling, pack sync, reconnection logic, and health or status visibility.
- [CONFIRMED] Colyseus already exposes the right explicit hooks for room auth, message limits, reconnection windows, and distributed scaling through shared presence rather than peer consensus. ([Colyseus Room Authentication](https://docs.colyseus.io/auth/room), [Rooms](https://docs.colyseus.io/room), [Reconnection](https://docs.colyseus.io/room/reconnection), [Presence](https://docs.colyseus.io/server/presence), [Scalability](https://docs.colyseus.io/scalability))
- [INFERRED] Do not let guest-side P2P experiments contaminate the core room contract. If an experiment happens, keep it outside canonical scoring, timer, and submission state.
- [INFERRED] If plural hosts ever exist, add explicit host identity, version, and compatibility metadata before expanding discovery or contribution paths.

### Measurement Or Experiment Implications

- [INFERRED] Measure room-state traffic, static clue asset delivery, reveal media delivery, TURN or relay usage, and operator minutes separately. "Bandwidth" is too coarse to guide this decision.
- [INFERRED] Measure whether trusted friends will actually self-host when given a clean bundle. If they will not, the strongest cooperative branch weakens materially.
- [INFERRED] Measure whether users understand host mode and privacy mode. Trust failures often come from mistaken mental models, not only technical bugs.
- [INFERRED] If asset seeding is ever tested, compare actual origin savings against added support and consent overhead before treating it as a strategy.

## What Would Change This View

- [HYPOTHESIS] Clear measurements showing that static media egress or TURN costs dominate earlier than operator labor and trust costs.
- [HYPOTHESIS] Repeated evidence that trusted friends eagerly run their own authoritative hosts when given a polished bundle.
- [HYPOTHESIS] A deliberate product shift toward public daily challenges, heavy spectator traffic, or larger downloadable media packages that move the cost center away from realtime room control.
- [HYPOTHESIS] Browser or runtime changes that materially improve background reliability, privacy defaults, or user-visible consent for peer traffic.
- [HYPOTHESIS] A later product decision that one important wrapper is collaborative enough to tolerate weaker authority and more experimental topology.

## Open Questions Worth A Third Pass

1. [INFERRED] What is the first real scarce resource once remote play becomes normal: operator time, reconnect trust, asset egress, TURN spend, or moderation labor?
2. [INFERRED] How large do pack and reveal assets become once the authored corpus matures, and do those sizes ever justify supporter-assisted distribution?
3. [INFERRED] What minimum signing, compatibility, and disclosure rules would a sanctioned host-collective model need before it is trustworthy?
4. [HYPOTHESIS] Would a trusted-circle self-host bundle actually be used often enough to matter, or would official hosting remain the social default even if self-hosting is technically easy?
5. [HYPOTHESIS] Is there a future analyst or co-op wrapper whose fun depends on looser authority enough to reopen a peer-to-peer branch honestly?
6. [INFERRED] How should official, self-hosted, community-hosted, and experimental modes be labeled so users do not over-trust the wrong environment?

## Source Ledger

### Primary Internal Sources

- [PROJECT](../../../PROJECT.md)
  - Authority: current product posture, audience, and scope constraints.
  - Limit: declared intent, not measured behavior.
- [ROADMAP](../../../ROADMAP.md)
  - Authority: current authoritative-room and reconnect direction.
  - Limit: present strategy, not validated player preference.
- [REQUIREMENTS](../../../REQUIREMENTS.md)
  - Authority: concrete expectations for join, room authority, and reconnect.
  - Limit: requirement targets, not implemented evidence.
- [CHECKPOINT](../../../explore/2026-04-10-vision-future-hosting/CHECKPOINT.md)
  - Authority: current exploratory framing and research-wave state.
  - Limit: exploratory synthesis, not canonical product doctrine.
- [00-ORCHESTRATION](../00-ORCHESTRATION.md)
  - Authority: lane mandate, output contract, and wave standards.
  - Limit: orchestration artifact, not product evidence.
- [base charter](../specs/01-cooperative-scaling-and-p2p-feasibility.md)
- [charter](../specs/05-xhigh-comparison-cooperative-scaling-and-p2p-feasibility.md)
  - Authority: exact lane constraints and special requirements.
  - Limit: task framing only.
- [lane 01](./01-cooperative-scaling-and-p2p-feasibility.md)
  - Authority: the direct baseline this comparison lane is testing against.
  - Limit: still a first-pass research synthesis, not telemetry.
- [Hosting Transition](../../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md)
- [Future-Aware Planning](../../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md)
- [Funding](./02-funding-access-and-transparency-models.md)
- [Security](./04-security-trust-and-operational-risk.md)
  - Authority: adjacent research lanes that surfaced relevant dependency structure.
  - Limit: internal syntheses rather than direct platform measurements.

### Primary External Sources

- [WebRTC Peer Connections](https://webrtc.org/getting-started/peer-connections)
  - Used for: signaling being outside the spec, ICE candidate exchange, and the practical role of STUN and TURN.
  - Reliability limit: Google-authored platform guidance rather than neutral product strategy advice.
- [MDN WebRTC protocols](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Protocols)
  - Used for: NAT, TURN relay overhead, and the fact that multi-party scaling commonly inserts an intermediary server.
  - Reliability limit: explanatory browser documentation, not a deployment recommendation by itself.
- [MDN Using WebRTC data channels](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels)
  - Used for: DTLS encryption, peer-to-peer server bypass once connected, and message-size or head-of-line caveats.
  - Reliability limit: transport behavior guidance, not governance analysis.
- [RFC 8828](https://datatracker.ietf.org/doc/rfc8828/)
  - Used for: WebRTC privacy and media-performance tradeoffs, including additional address exposure relative to plain HTTP.
  - Reliability limit: standards-track guidance on browser behavior, not product-specific ethics.
- [Chrome Page Lifecycle API](https://developer.chrome.com/docs/web-platform/page-lifecycle-api)
  - Used for: hidden or frozen tab behavior and the explicit recommendation to close active WebRTC connections on freeze.
  - Reliability limit: Chrome guidance, though directionally representative of modern browser resource management.
- [Colyseus Room Authentication](https://docs.colyseus.io/auth/room)
  - Used for: explicit room auth behavior and the fact that unimplemented auth permits any client to connect.
  - Reliability limit: framework-specific worldview.
- [Rooms](https://docs.colyseus.io/room)
  - Used for: room lifecycle, reconnection hooks, and message-limit controls.
  - Reliability limit: framework docs do not guarantee a given app will use the controls well.
- [Reconnection](https://docs.colyseus.io/room/reconnection)
  - Used for: explicit reconnection windows and recovery semantics.
  - Reliability limit: still application-dependent.
- [Presence](https://docs.colyseus.io/server/presence)
- [Scalability](https://docs.colyseus.io/scalability)
  - Used for: the single-process default, Redis-backed scaling, and the fact that each room belongs to one Colyseus process.
  - Reliability limit: framework docs describe one architectural family, not all possible multiplayer shapes.
- [Docker Compose](https://docs.docker.com/compose/intro/features-uses/)
  - Used for: shareable single-host deployment packaging and operator-level cooperation plausibility.
  - Reliability limit: packaging guidance, not adoption evidence.

### Secondary / Practitioner Sources

- [LiveKit Transport](https://docs.livekit.io/transport/)
  - Authority: official vendor docs for a production realtime stack.
  - Used for: practitioner signal that production WebRTC deployments centralize connection complexity, adaptation, and state handling rather than relying on browser mesh logic.
  - Reliability limit: explicitly product-shaped and not neutral.
- [WebTorrent FAQ](https://webtorrent.io/faq)
  - Authority: official docs for the WebTorrent project.
  - Used for: browser swarm constraints, including the fact that browser WebTorrent peers only connect to WebRTC-capable peers and require WebRTC-capable seeders.
  - Reliability limit: project-specific and partly optimistic toward its own model.
