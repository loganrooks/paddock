# Lane 02 Findings: Hosting Transition XHigh Comparison Rerun

Date: 2026-04-10
Lane: `02-hosting-transition-xhigh-comparison`
Status: complete
Mode: exploratory comparison rerun, not planner-facing

## Question Space

- [CONFIRMED] This rerun is asking whether a browser-first Prix Guesser can move through four materially different operating shapes without becoming incoherent: local LAN play, self-hosted remote play from personal hardware, modest public hosting, and later growth under constrained money, constrained compute, and constrained operator time.
- [CONFIRMED] The question is not only "what hosting vendor should be used." The harder question is whether the product can preserve low-friction join, authoritative room behavior, and user trust while the operator path changes underneath it.
- [INFERRED] The most important hidden subquestion is not raw scale. It is where the first felt break happens: browser constraints, join friction, phone sleep/reconnect, operator burden, or public-service expectation drift.
- [INFERRED] A second hidden subquestion is whether "browser-first website," "portable operator bundle," and "downloadable local-host package" are competing identities or merely different wrappers around the same product surface.

## Method And Sources

- [CONFIRMED] I formed an independent map first from project context plus external sources, and only then read the original first-wave findings for comparison.
- [CONFIRMED] Local project context used before comparison:
  - `.planning/PROJECT.md`
  - `.planning/ROADMAP.md`
  - `.planning/REQUIREMENTS.md`
  - `.planning/phases/01-authored-round-contract/.continue-here.md`
  - `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
  - `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
  - `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md`
  - `.planning/explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md`
  - `.planning/explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md`
- [CONFIRMED] Primary and official external sources used for infrastructure and browser claims:
  - [MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts)
  - [Chrome Local Network Access](https://developer.chrome.com/blog/local-network-access?hl=en)
  - [Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve)
  - [Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel)
  - [Cloudflare Tunnel overview](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/migrate-legacy-tunnels/index.md)
  - [Cloudflare create tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/)
  - [Cloudflare Tunnel FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)
  - [Cloudflare WebSockets](https://developers.cloudflare.com/network/websockets/)
  - [Cloudflare Quick Tunnels / TryCloudflare](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/)
  - [Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/)
  - [Colyseus docs](https://docs.colyseus.io/)
- [CONFIRMED] Secondary pattern sources used cautiously:
  - [Jackbox join support](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game)
  - [Kahoot mobile app / join pattern](https://kahoot.com/mobile-app/)
- [CONFIRMED] The product-support sources above are being used only as join-pattern and expectation precedents. They are not evidence that Prix Guesser should copy those products' backend or business model.
- [CONFIRMED] No Prix Guesser load tests, cold-boot timings, reconnect traces, or real media-delivery measurements existed for this rerun. Capacity claims beyond explicit vendor/framework documentation therefore remain inferential.

## Inquiry Trajectory

1. [CONFIRMED] I started from the simplest stage the project explicitly wants: one host machine, one shared screen, guest phones on the same local network.
2. [INFERRED] That immediately split the problem into two layers that the original framing partly blended together:
   - guest-facing join grammar
   - operator-facing network and deployment posture
3. [CONFIRMED] From there I checked browser and network constraints first, because local play is not actually "just localhost" once guest devices hit a LAN IP and once public pages may later try to talk to local services.
4. [CONFIRMED] I then examined remote self-host paths, especially the difference between tailnet-only sharing, public tunnel sharing, and a more normal public HTTPS hostname.
5. [INFERRED] That pushed the inquiry from pure technical feasibility into adoption and trust feasibility, because asking casual guests to install networking tooling is a very different product than sending them a normal browser link.
6. [CONFIRMED] Only after that did I examine "later scale," and the main result was that the first meaningful breakpoint looks smaller and more operational than "serious scale": scheduled uptime, reconnect behavior, observability, and operator legibility arrive before headline traffic.
7. [CONFIRMED] After the independent map was formed, I read the original first-wave findings and compared where it converged, where it flattened distinctions, and where the stricter standard changes the read.

## Branching Paths And Dependencies

- [INFERRED] The canonical join grammar is upstream of most later decisions.
  - If guests should only need a browser link, tailnet-style guest requirements become a niche branch rather than the main path.
  - If guests can tolerate install/auth friction, a larger self-host/private-mesh branch stays alive.
- [INFERRED] The room runtime choice is downstream of the product's tolerance for long-lived authoritative state and reconnect guarantees.
  - A lightweight prototype path can tolerate more tunnel/tooling fragility.
  - A trust-preserving remote/public path pulls harder toward explicit reconnection handling, shared presence, and better observability.
- [INFERRED] Media posture is a hidden dependency for hosting decisions.
  - If clue payloads are heavy or bursty, the first pain may be media delivery rather than room-state sync.
  - If clue payloads are light and cached well, realtime room behavior becomes the earlier constraint.
- [INFERRED] Publicness level changes the meaning of "available."
  - Private LAN play can tolerate host-driven startup and occasional rough edges.
  - Private remote play creates scheduled-session expectations.
  - Public beta creates service-obligation expectations even at low traffic.
- [INFERRED] Packaging depends on whether the browser experience remains canonical.
  - If browser-first stays canonical, Docker bundles and native wrappers are operator conveniences.
  - If a native wrapper becomes the real product, the project splits its operational and UX surface much earlier.
- [INFERRED] Queueing and access policy depend on both actual capacity limits and product ethics.
  - If demand is modest and personal-hosted, windows and waitlists may be honest.
  - If scarcity is synthetic or monetized before service quality is understood, the same mechanisms become manipulative.

## Findings

### Feasible Staged Paths

- [CONFIRMED] **Stage A: browser-first LAN play from one host machine is technically viable.**
  - Browser-controller products already normalize "big screen plus phones" with code-join and QR-assist patterns. ([Jackbox](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Kahoot](https://kahoot.com/mobile-app/))
  - MDN distinguishes trustworthy loopback origins such as `localhost` and `127.0.0.1` from arbitrary LAN IPs, which means local development and real same-WiFi play are not identical browser environments. ([MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts))
  - [INFERRED] Technical feasibility is strong here.
  - [INFERRED] One-person operability is also strong if startup is boring and fast.
  - [INFERRED] Casual-user friction is low only if the guest path is "open a normal URL, optionally scan QR, enter code."
  - [INFERRED] Ethical risk is low because the service promise is local and explicit.
- [CONFIRMED] **Stage B: private remote play from personal hardware is also technically viable, but it branches immediately into different guest-friction profiles.**
  - Tailscale Serve shares local services with other devices in the tailnet and applies tailnet access controls. ([Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve))
  - Tailscale Funnel exposes a local service to the broader internet, but the official docs still mark it beta and subject to non-configurable bandwidth limits. ([Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel))
  - Cloudflare Tunnel exposes local services through outbound-only connections and supports published browser applications over a public hostname without opening inbound ports. ([Cloudflare Tunnel overview](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/migrate-legacy-tunnels/index.md), [create tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/))
  - [INFERRED] Technical feasibility is good for both Tailscale-centered and Cloudflare-centered remote bridges.
  - [INFERRED] One-person operability is best when Tailscale is treated as the operator/admin path and guests still get normal browser HTTPS.
  - [INFERRED] Adoption feasibility is weak if every guest must install/authenticate into a mesh network.
  - [INFERRED] Economic feasibility is attractive because personal hardware plus tunnel tooling delays VPS spend.
  - [INFERRED] Ethical feasibility is acceptable so long as the project is honest that remote play is private hosted access, not a robust public service.
- [INFERRED] **Stage C: a modest public beta is plausible without a total rewrite, but it is not just "Stage B with more users."**
  - Cloudflare Quick Tunnels are explicitly for testing and development only, with a documented 200 in-flight request limit and no SSE support. ([Quick Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/))
  - Cloudflare's normal tunnel path supports a stable published hostname and access policies. ([create tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/))
  - [INFERRED] Public beta becomes coherent only when the project uses a real hostname, stable HTTPS, websocket-capable ingress, explicit status messaging, and a conscious start/stop or uptime posture.
  - [INFERRED] Technical feasibility is still solid.
  - [INFERRED] One-person operability drops because observability, upgrade safety, and guest support all become public-facing concerns.
  - [INFERRED] Casual-user friction can remain low if the join surface stays browser-native.
  - [INFERRED] Ethical feasibility becomes more delicate because scarcity, outage, and access-policy language now shape trust.
- [INFERRED] **Stage D: later scaling can preserve the same product surface, but only if the early runtime and room model do not hardcode "single box forever."**
  - Colyseus is useful here as an authoritative-room exemplar: it explicitly documents a shift from local in-memory presence to Redis-backed presence once scaling across processes or machines. ([Colyseus docs](https://docs.colyseus.io/))
  - [INFERRED] The important point is broader than Colyseus itself. Any authoritative realtime room stack eventually hits a shared-state and observability breakpoint.
  - [INFERRED] This stage is technically feasible.
  - [INFERRED] One-person operability is much weaker unless deployment and failure handling stay very legible.
  - [INFERRED] Economic feasibility depends less on one "scale number" and more on whether the project can pay for spare headroom, persistence, backups, and diagnostics.
  - [INFERRED] Ethical feasibility depends on whether public access is sold as experimental and capacity-limited, or implied to be durable service before it is.
- [INFERRED] **Operator bundle coexistence is plausible.**
  - A browser-first canonical product can coexist with a Docker bundle or later local-host wrapper if those are treated as operator packaging, not as separate game identities.
  - Docker Compose is explicitly meant to define and run a multi-container app from a versioned YAML file with one startup/shutdown flow. ([Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/))
  - [INFERRED] This keeps the guest experience stable while allowing the operator path to evolve.
  - [HYPOTHESIS] A downloadable local-host wrapper only becomes justified if measured operator pain remains high after a good browser-plus-bundle path exists.

### Operational Breakpoints

- [CONFIRMED] **Breakpoint 1: from `localhost` assumptions to actual LAN guests.**
  - `localhost` is treated as potentially trustworthy by browsers, but `http://192.168.x.x` is not the same class of origin. ([MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts))
  - [INFERRED] If early development quietly relies on secure-context-only browser features, same-WiFi play will reveal that break before any public beta does.
- [CONFIRMED] **Breakpoint 2: from same-WiFi guests to internet guests.**
  - Tailscale Serve is tailnet-only.
  - Tailscale Funnel is public but beta and bandwidth-limited.
  - Cloudflare Tunnel is designed for published outbound-only exposure.
  - [INFERRED] This is less a port-opening problem than a guest-trust and ingress-shape problem.
- [INFERRED] **Breakpoint 3: from "host laptop for tonight" to "people are expecting this to be available at a time."**
  - Sleep states, WiFi changes, browser refreshes, manual restarts, and cold-boot setup become product failures rather than harmless operator quirks.
- [CONFIRMED] **Breakpoint 4: from transient sockets to trust-preserving reconnection.**
  - Cloudflare documents websocket support, but also notes that restarts can terminate websocket connections. ([Cloudflare WebSockets](https://developers.cloudflare.com/network/websockets/))
  - [INFERRED] Reconnect behavior becomes more trust-critical than raw throughput surprisingly early.
- [CONFIRMED] **Breakpoint 5: from one process to shared coordination.**
  - Colyseus documents that once scaling across multiple processes or machines, shared presence is required. ([Colyseus docs](https://docs.colyseus.io/))
  - [INFERRED] Even modest growth can trigger "distributed systems" obligations before anything that feels like large-scale success.
- [CONFIRMED] **Breakpoint 6: from private access to public accountability.**
  - Cloudflare Tunnel does not pass external visitor IPs directly to the origin unless alternative logging is configured. ([Cloudflare Tunnel FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/))
  - [INFERRED] Once public links exist, observability, abuse response, and incident explanation become part of the product surface.

### What Resource Constraints Actually Mean In Practice

- [INFERRED] **Limited money** mostly buys reliability margin, not a different product category.
  - It buys real domain/TLS posture, a VPS or always-on host, backups, room to separate app/data concerns, and better telemetry when something goes wrong.
  - It does not automatically solve awkward join flows, fragile reconnect behavior, or unclear status communication.
- [INFERRED] **Limited compute** is likely to show up first as ugly user symptoms rather than clean benchmarks.
  - Expected first failures include slow join, delayed clue media, timer drift under reconnect bursts, or a room that feels "sticky" after several phones wake at once.
- [INFERRED] **Limited operator time** may be the scarcest constraint of all.
  - A stack that works only when the operator remembers the exact tunnel incantation, firewall exception, or cold-boot order is not truly operable for repeated game nights.
- [INFERRED] **Limited trust budget** is also a resource.
  - In a public or semi-public stage, unexplained downtime, silent queueing, or ambiguous beta promises consume trust faster than modest performance limits do.
- [INFERRED] **What more money actually buys beyond "more scale."**
  - less operator babysitting
  - better persistence and backups
  - safer deployments and rollback options
  - more honest observability
  - more confidence offering scheduled or public access windows
- [CONFIRMED] The rerun cannot honestly state a meaningful max-concurrency number for Prix Guesser from docs alone.
  - Quick Tunnel's 200 in-flight request cap is explicit. ([Quick Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/))
  - Everything else depends on room runtime, message rate, clue payload size, reconnect patterns, and deployment topology.

### Transition Patterns That Preserve Trust

- [INFERRED] **Keep the guest-facing join grammar stable across stages.**
  - Room code, canonical URL, and QR assist should remain recognizable whether the operator path is LAN, personal hardware, or modest public hosting.
- [INFERRED] **Tell users what hosting tier they are entering.**
  - "Local game on host's network," "private hosted session," and "public beta" should not feel operationally identical in the copy if they are not operationally identical in reality.
- [INFERRED] **Do not require guest networking tools unless the product is explicitly for a technical cohort.**
  - Tailscale is strong operator/admin tooling.
  - It is a weak default guest story for casual social play.
- [INFERRED] **If capacity controls appear, make them legible and bounded.**
  - Scheduled windows, waitlists, or "rooms full" states are honest when tied to measured limits and explicit operator intent.
  - Infinite spinners, fake scarcity copy, or paid fast-lanes before the service is stable are trust-destructive.
- [HYPOTHESIS] **Donation or support models are only ethically viable if they fund continuity rather than distort access truth.**
  - Funding uptime, bandwidth, or more hosted play windows can be honest.
  - Selling gameplay advantage or synthetic exclusivity would cut against the project's private-first, expert-fan posture.
- [INFERRED] **Start publicness with bounded promises.**
  - A modest public beta looks more trustworthy as "open during explicit windows while we learn" than as vague always-on service with hidden fragility.
- [INFERRED] **Expose operator-visible health before promising player-visible reliability.**
  - If the host cannot tell whether the room is reachable, healthy, and websocket-capable, the guests will discover that lack first.

### Questions Requiring Measurement Rather Than Armchair Guessing

- [INFERRED] How long does it take from cold boot to a joinable room in each tier:
  - LAN on host laptop
  - personal hardware plus tunnel
  - small VPS or public hostname
- [INFERRED] What join success rate and median join latency do 4, 8, and 12 phones see on a normal home network?
- [INFERRED] What reconnect success rate do sleeping phones achieve after 15 seconds, 60 seconds, and several minutes away?
- [INFERRED] Are clue media payloads or room-state messages the first practical bandwidth bottleneck?
- [INFERRED] What failure do users notice first:
  - QR confusion
  - slow media load
  - room unreachable
  - timer drift
  - reconnect failure
- [INFERRED] Can a non-developer operator follow the start/stop flow without SSH improvisation or ad hoc firewall fixes?
- [INFERRED] What status and queue copy do users read as honest rather than shaky?
- [CONFIRMED] Chrome's Local Network Access direction creates a moving browser-policy surface for public sites that want to talk to local-network services, and that is not something this rerun can close with armchair certainty. ([Chrome Local Network Access](https://developer.chrome.com/blog/local-network-access?hl=en))

## Gray Areas And Live Tensions

- [INFERRED] **Web-first coherence versus operator friendliness** remains live.
  - A single canonical browser product is clean for guests.
  - Operators may still need packaging help long before the guest experience itself needs a native wrapper.
- [INFERRED] **Private-first ethos versus public-service obligation** remains unresolved.
  - A private hosted link for friends is still socially forgiving.
  - A public beta link, even with tiny traffic, creates a different expectation of reliability and explanation.
- [INFERRED] **Self-host control versus observability and abuse response** remains live.
  - Personal hardware plus tunnel preserves control.
  - Public exposure through a proxy/tunnel layer can blur what the operator can easily see and explain.
- [INFERRED] **Technically possible versus socially tolerable** remains a central split.
  - Tailnet-only guest access is technically feasible.
  - It still looks adoption-hostile for the likely social use case.
- [INFERRED] **Queueing can be honest or manipulative depending on context.**
  - The mechanism alone does not determine the ethics.
  - The surrounding capacity truth and monetization posture do.
- [INFERRED] **Downloadable local-host packaging is simultaneously sensible and risky.**
  - It may reduce operator friction.
  - It may also pull the project into packaging and update burdens before the core room loop is proven.

## Scope Expansions

- [CONFIRMED] **Browser policy evolution became part of the inquiry.**
  - The Chrome Local Network Access work surfaced because "browser-first across LAN and public stages" is partly a browser-policy question, not only a hosting question.
  - I pursued this enough to flag it as a real future constraint, not enough to claim a finished browser-compatibility position.
- [CONFIRMED] **Observability and logging surfaced as a hosting-transition issue.**
  - Cloudflare Tunnel's origin-IP behavior means public exposure is also a monitoring and abuse-handling question.
  - This was not explicit in the original charter wording, but it matters to trust.
- [CONFIRMED] **Ethical feasibility expanded the lane beyond pure infrastructure.**
  - Waitlists, access windows, and donation framing emerged because constrained public hosting is not just a technical problem.
  - I pursued these at the level of live tensions, not as a recommendation memo.
- [INFERRED] **Packaging strategy emerged as a separate branch rather than a later implementation detail.**
  - The browser-first versus local-host bundle question is really about whether operator convenience can stay downstream of a stable guest experience.

## Rival Models Still Alive

- [INFERRED] **Model A: one canonical browser product, staged operator paths.**
  - LAN first, then personal hardware plus tunnel, then modest public hostname, with Docker/native packaging treated as operator wrappers.
  - This is the strongest current model.
- [INFERRED] **Model B: browser-first, but remote play stays intentionally private and operator-mediated for a long time.**
  - Public beta is delayed.
  - The project optimizes for friend groups and scheduled sessions rather than general discovery.
  - This keeps service obligations smaller at the cost of slower public learnings.
- [INFERRED] **Model C: move earlier to a real public host and treat self-host parity as secondary.**
  - This may produce smoother public access faster.
  - It risks drifting away from the repo's current local/private posture and from the operator-control story.
- [INFERRED] **Model D: prioritize a local-host appliance or native wrapper earlier than public hosting.**
  - This keeps the project more "couch software" than "website."
  - It may be the right path only if measured operator friction for browser-plus-bundle is higher than expected.

## Practical Implications

### Thinking Implications

- [INFERRED] Use `hosting tier`, `operator path`, `guest join grammar`, and `trust budget` as separate terms rather than collapsing them into "deployment."
- [INFERRED] Treat "self-hosted remote" and "public beta" as different product states, not merely bigger and smaller infra plans.
- [INFERRED] Keep asking two questions together:
  - what is technically possible here
  - what will feel normal to a casual invited guest

### Design Implications

- [INFERRED] The UI should visibly preserve a stable join ritual:
  - human-readable room code
  - canonical join URL
  - QR assist
- [INFERRED] The UI should also disclose tier and confidence honestly:
  - local/private/public
  - starting/updating/healthy/unreachable
- [INFERRED] Reconnect messaging deserves first-class design attention earlier than public scaling features do.
- [INFERRED] If the project ever uses queueing or access windows, the copywriting is part of the trust model, not polish.

### Implementation Implications

- [INFERRED] Do not make core controller play depend on secure-context-only browser APIs.
- [INFERRED] Keep the browser product canonical and treat Docker/native packaging as downstream operator wrappers unless evidence forces a change.
- [INFERRED] Make join URL generation, room code generation, and QR generation explicit capabilities rather than ad hoc conveniences.
- [INFERRED] Treat the room runtime choice as partly a deployment choice.
  - Long-lived authoritative rooms, reconnect semantics, and shared presence are not abstract architecture questions only.
- [INFERRED] Separate media delivery concerns from room-state concerns early enough that the first measured bottleneck can be diagnosed instead of guessed.
- [INFERRED] Plan for boring operator commands and health checks before promising broader access.

### Measurement Or Experiment Implications

- [INFERRED] Run a small measurement matrix across three tiers:
  - same-WiFi LAN
  - personal hardware plus tunnel
  - modest public hostname
- [INFERRED] Measure cold boot, join latency, reconnect success, media load time, and operator steps, not just room count.
- [INFERRED] Test at least one deliberately non-technical operator flow.
- [INFERRED] Test at least one bad-network and phone-sleep scenario before any public beta framing.

## Comparison With Original First-Wave Pass

### What The Original First-Wave Pass Got Right

- [CONFIRMED] The original pass was directionally right that a web-first product can plausibly span LAN play, self-hosted remote play, and later modest public hosting without requiring a different product at each stage.
- [CONFIRMED] It was right to treat Tailscale primarily as an operator tool and not the default guest requirement.
- [CONFIRMED] It was right that Cloudflare Quick Tunnels are not a real public-beta foundation.
- [CONFIRMED] It was right that reconnect trust matters before headline scale does.
- [CONFIRMED] It was right that browser-first and operator packaging can coexist if packaging stays downstream of the canonical web experience.

### What This Rerun Sees More Clearly

- [CONFIRMED] The stricter rerun separates technical, operational, adoption, economic, and ethical feasibility much more explicitly.
- [CONFIRMED] The LAN stage is trickier than the first pass made it sound because local development and real LAN guest access do not share identical browser assumptions, and Chrome's Local Network Access direction adds another moving part for some future hybrid patterns.
- [CONFIRMED] The public transition is not merely "more traffic." It changes observability, accountability, access-policy language, and the ethics of capacity control.
- [INFERRED] The real branch point is less "which tunnel/vendor" and more "what guest friction is acceptable" plus "what service obligation is being implied."
- [INFERRED] The first-wave writeup still leaned slightly toward a neat default path. This rerun sees a more genuinely branching map, especially between:
  - private remote as an operator-mediated friend service
  - modest public beta as an explicitly bounded public service

### Where This Rerun Disagrees Or Narrows

- [INFERRED] The first pass used Colyseus as part of the staged-hosting explanation. This rerun treats Colyseus as a helpful authoritative-room exemplar, not as the decisive architecture commitment for the lane.
- [INFERRED] The first pass used Jackbox and Kahoot as controller precedents. This rerun narrows that claim: they validate join grammar and user expectation more than they validate Prix Guesser's exact hosting or room-state architecture.
- [INFERRED] The first pass's "strongest default path" language was slightly tidier than the evidence really warrants. Model A is still strongest, but the gap between Model A and a deliberately longer private-remote phase is not closed enough to call it solved.

### Why The Difference Exists

- [CONFIRMED] Part of the difference comes from the stronger second-wave standard itself.
  - The rerun is required to preserve gray areas, track branching inquiry, and distinguish kinds of feasibility.
- [INFERRED] Part of the difference comes from changed framing.
  - Asking "what tensions stay alive?" produces a less closure-seeking answer than asking "what path looks best?"
- [INFERRED] Part may also come from reasoning depth, but the bigger shift here looks methodological rather than model-magic.

## What Would Change This View

- [INFERRED] Measured evidence that media payloads, not room-state sync or ingress, are the dominant early failure mode.
- [INFERRED] A runtime choice that meaningfully weakens self-host parity or strongly favors a managed-public-first deployment shape.
- [INFERRED] Real user evidence that invited guests are willing to tolerate tailnet-style install/auth friction.
- [INFERRED] Real operator evidence that a browser-plus-bundle path remains too fragile, making a local-host appliance or native wrapper clearly worth the maintenance cost.
- [INFERRED] A product decision to pursue streamer/public discovery much earlier than the current private-first posture suggests.
- [CONFIRMED] Browser-policy changes around local network access or related secure-context behavior could materially reshape some of the LAN-to-public bridging assumptions. ([Chrome Local Network Access](https://developer.chrome.com/blog/local-network-access?hl=en), [MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts))

## Open Questions Worth A Further Pass

1. [INFERRED] What is the most honest remote bridge for the near term:
   - personal hardware plus Cloudflare Tunnel
   - personal hardware plus VPS/reverse proxy
   - longer private-only mesh-mediated hosting
2. [INFERRED] What exact operator health signals and player-facing status copy would make a constrained public beta feel trustworthy?
3. [INFERRED] Which failure becomes dominant first in real testing:
   - join friction
   - media delivery
   - reconnect churn
   - operator cold-start burden
4. [INFERRED] How much observability and abuse-handling capability is minimally acceptable before any public room links exist?
5. [INFERRED] At what measured pain threshold does a downloadable local-host wrapper become justified?
6. [INFERRED] How do streamer or spectator ambitions alter room secrecy, join-code handling, and public-access expectations?

## Source Ledger

### Primary / official external sources

- [MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts)
  - Authority: primary browser-platform documentation
  - Used for: trustworthy-origin distinction between loopback and arbitrary LAN IPs
  - Limits: not a Prix Guesser-specific operability source
- [Chrome Local Network Access](https://developer.chrome.com/blog/local-network-access?hl=en)
  - Authority: primary Chrome platform guidance
  - Used for: future browser-policy pressure on public sites talking to local-network services
  - Limits: Chrome-specific and still an evolving policy surface
- [Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve)
  - Authority: official vendor docs
  - Used for: tailnet-only sharing, HTTPS requirements, access-control behavior
  - Limits: vendor docs describe capability, not guest tolerance
- [Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel)
  - Authority: official vendor docs
  - Used for: public sharing, beta status, bandwidth-limit warning
  - Limits: vendor docs, not independent ops evidence
- [Cloudflare Tunnel overview](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/migrate-legacy-tunnels/index.md)
  - Authority: official vendor docs
  - Used for: outbound-only tunnel model
- [Cloudflare create tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/)
  - Authority: official vendor docs
  - Used for: public hostname exposure and access-policy hooks
- [Cloudflare Tunnel FAQ](https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/)
  - Authority: official vendor docs
  - Used for: origin-IP / observability wrinkle
- [Cloudflare WebSockets](https://developers.cloudflare.com/network/websockets/)
  - Authority: official vendor docs
  - Used for: websocket support and restart caveat
- [Cloudflare Quick Tunnels / TryCloudflare](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/)
  - Authority: official vendor docs
  - Used for: testing-only status and explicit cap
- [Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/)
  - Authority: official Docker docs
  - Used for: operator-bundle feasibility
- [Colyseus docs](https://docs.colyseus.io/)
  - Authority: official framework docs
  - Used for: authoritative-room and shared-presence breakpoint exemplar
  - Limits: illustrative of one runtime family, not binding on the project

### Secondary / pattern sources

- [Jackbox join support](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game)
  - Authority: official product support doc
  - Used for: browser-controller join precedent
  - Limits: precedent only, not architecture evidence
- [Kahoot mobile app / join pattern](https://kahoot.com/mobile-app/)
  - Authority: official product marketing/support surface
  - Used for: code-join and host-screen/controller expectation precedent
  - Limits: broader product pattern only

### Local project sources

- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/phases/01-authored-round-contract/.continue-here.md`
- `.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
- `.planning/explore/2026-04-10-vision-future-hosting/CHECKPOINT.md`
- `.planning/explore/2026-04-10-vision-future-hosting/04-cross-lane-reading.md`
- `.planning/explore/2026-04-10-vision-future-hosting/05-second-wave-research-standards.md`

### Comparison source read only after the independent map

- `.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`
