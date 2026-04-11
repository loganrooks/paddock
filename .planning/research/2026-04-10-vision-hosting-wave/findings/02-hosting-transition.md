# Lane 02 Findings: Hosting, Distribution, Capacity, And Transition Pathways

Date: 2026-04-10
Lane: `02-hosting-transition`
Status: complete

## Question Space

This lane asked whether a web-first Prix Guesser can plausibly move through all of these stages without a full product rewrite:

1. LAN-only same-WiFi play from one host machine
2. Self-hosted remote play from personal hardware such as `dionysus`
3. Small public hosted operation
4. Later growth under constrained money, constrained compute, and constrained operator time

The project context matters here. The current product posture is private-first, browser-first, room-based, and explicitly aimed at host-screen plus phone-controller social play rather than a solo-first web app (`.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/phases/01-authored-round-contract/.continue-here.md`). That means the hosting question is not just "where do we deploy?" It is "what operational path preserves the room model, the guest join experience, and user trust as the project moves from living-room play to remote play to a possible later public beta?"

## Method And Sources

- Local project context:
  - `/.planning/PROJECT.md`
  - `/.planning/ROADMAP.md`
  - `/.planning/REQUIREMENTS.md`
  - `/.planning/phases/01-authored-round-contract/.continue-here.md`
  - `/.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
  - `/.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
- Primary technical sources:
  - Tailscale Serve/Funnel docs
  - Cloudflare Tunnel/WebSockets docs
  - Colyseus docs on deploy-anywhere, reconnection, and scaling
  - Docker docs on Compose
  - MDN secure-context docs
- Secondary product-pattern sources:
  - Jackbox support docs
  - Kahoot support docs

Authority notes:

- [CONFIRMED] Cloudflare, Tailscale, Colyseus, Docker, and MDN are primary sources for capability and limitation claims. They are strong on "what the platform supports" and weaker on "what players will emotionally tolerate." ([Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve), [Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel), [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/), [Cloudflare WebSockets](https://developers.cloudflare.com/network/websockets/), [Colyseus](https://docs.colyseus.io/), [Colyseus Scalability](https://docs.colyseus.io/scalability), [Colyseus Reconnection](https://docs.colyseus.io/room/reconnection), [Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/), [MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts))
- [CONFIRMED] Jackbox and Kahoot support docs are useful as operational precedents for controller-style join flows, but they are not neutral infrastructure sources. I am using them only for join-pattern precedent, not for backend architecture conclusions. ([Jackbox join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Kahoot join](https://support.kahoot.com/hc/en-us/articles/115016109368-How-to-join-games-in-Kahoot-app))
- [CONFIRMED] No project-specific load tests or bandwidth traces were available in this lane, so any capacity conclusion beyond documented platform limits would be overreach.

## Findings

### Feasible Staged Paths

#### Path 1: Browser-first LAN host on one machine

- [CONFIRMED] A browser-first host/controller model is operationally plausible for same-WiFi play: modern browser-based controller products already use "host screen on one device, phone browser on another device" with room-code join patterns. ([Jackbox join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Kahoot join](https://support.kahoot.com/hc/en-us/articles/115016109368-How-to-join-games-in-Kahoot-app))
- [INFERRED] For Prix Guesser, the minimal LAN shape is straightforward: one device runs the room host and shared screen; guest phones open a join URL on the same local network; the room code remains the human fallback when QR scanning fails. This aligns with the project’s host-screen-friendly private-play posture (`PROJECT.md`, `ROADMAP.md`).
- [CONFIRMED] LAN mode has a subtle browser constraint: `localhost` and loopback origins are treated as potentially trustworthy, but arbitrary LAN IPs are not automatically equivalent secure contexts. Features that rely on secure contexts should therefore not be assumed to work the same way on `http://192.168.x.x` as on `http://localhost`. ([MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts))
- [INFERRED] That makes LAN mode viable, but only if the early architecture avoids depending on HTTPS-only browser features for core controller play. In practice, join, submit, timers, and state sync should work without service-worker magic or other secure-context-sensitive features.

#### Path 2: Private remote play from personal hardware such as `dionysus`

- [CONFIRMED] Tailscale Serve exposes a local service to devices inside the tailnet, and the docs explicitly distinguish it from Funnel for public internet sharing. ([Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve))
- [CONFIRMED] Tailscale Funnel exposes a local service to the public internet, but it is still in beta, only works on specific ports, and is subject to non-configurable bandwidth limits. ([Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel))
- [CONFIRMED] Cloudflare Tunnel publishes local services through outbound-only connections, does not require opening inbound ports, supports multiple published applications per tunnel, and supports proxied WebSocket connections. ([Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/), [Cloudflare Routing](https://developers.cloudflare.com/tunnel/routing/), [Cloudflare WebSockets](https://developers.cloudflare.com/network/websockets/))
- [INFERRED] The clean private-remote progression is therefore:
  1. operator access to `dionysus` over Tailscale/SSH
  2. guest access over normal browser HTTPS
  3. room traffic carried over a tunnel or reverse proxy that supports WebSockets
- [INFERRED] In that model, Tailscale is best treated as an operator tool, not a guest requirement. Requiring every guest to install Tailscale would fight the low-friction join posture already implied by `ROOM-02` and Phase 4.
- [INFERRED] A personal always-on box such as `dionysus` is a realistic bridge stage because it preserves self-host control while avoiding the "host laptop must stay awake on game night" failure mode.

#### Path 3: Small public hosted operation

- [CONFIRMED] Cloudflare Tunnel can take a privately hosted HTTP/HTTPS service and map it to a public hostname; non-HTTP services require `cloudflared` on the client side, but normal browser HTTP/HTTPS traffic does not. ([Cloudflare Routing](https://developers.cloudflare.com/tunnel/routing/), [Protocols for published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/))
- [CONFIRMED] Quick Tunnels are only for testing and development, have a 200 in-flight request limit, and do not support SSE. ([Cloudflare Tunnel setup](https://developers.cloudflare.com/tunnel/setup/), [Quick Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/))
- [INFERRED] That means a public beta should not be built on a "temporary share link" story. It needs a real hostname, stable HTTPS, WebSocket-capable ingress, and an operator flow that can be started and stopped intentionally.
- [CONFIRMED] Docker Compose is designed to define and run multi-container applications from a versioned YAML file and is explicitly positioned as a shareable way for another operator to spin the stack up or down with one command. ([Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/))
- [INFERRED] For Prix Guesser, a small public beta is most plausible as "same browser product, same room model, same backend shape, but now started from a stable deploy bundle on a VPS or personal box" rather than "second product with different deployment assumptions."

#### Path 4: Growth beyond one personal machine

- [CONFIRMED] Colyseus documents a clear breakpoint between single-process and distributed operation: local in-memory presence is fine for single-process deployments, while Redis presence is required once you scale across multiple processes or machines. ([Colyseus Presence](https://docs.colyseus.io/server/presence), [Colyseus Scalability](https://docs.colyseus.io/scalability))
- [CONFIRMED] Colyseus also states that each room belongs to a single process and that each process has a maximum number of players it can handle, but the exact amount depends on many factors. ([Colyseus Scalability](https://docs.colyseus.io/scalability))
- [INFERRED] So the first serious scale transition is not "suddenly millions of players." It is "one box is no longer enough for the room state model we chose, so presence, driver, public addressing, and observability become mandatory."
- [INFERRED] That is a real architecture breakpoint. It changes operations, deployment topology, and debugging burden even if the audience is still modest.

### Operational Breakpoints

1. **From `localhost` assumptions to actual guest devices**
   - [CONFIRMED] Secure-context behavior differs between loopback/local and non-local origins. ([MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts))
   - [INFERRED] If the product quietly depends on secure-context-only APIs during local development, LAN play will be the first place that breaks.

2. **From "friends on my WiFi" to "friends on the internet"**
   - [CONFIRMED] Tailscale Serve is tailnet-only; Funnel is public but beta/bandwidth-limited; Cloudflare Tunnel is designed for public hostname exposure over outbound-only connections. ([Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve), [Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel), [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/))
   - [INFERRED] The guest-access breakpoint is therefore about ingress strategy and operational trust, not just "opening a port."

3. **From one process to many**
   - [CONFIRMED] Colyseus needs shared Redis-backed presence once you move beyond single-process. ([Colyseus Presence](https://docs.colyseus.io/server/presence), [Colyseus Scalability](https://docs.colyseus.io/scalability))
   - [INFERRED] This is where "small indie app" starts needing real distributed-systems discipline.

4. **From recoverable glitches to trust-damaging failures**
   - [CONFIRMED] Cloudflare notes that WebSocket connections can be terminated during network restarts, and Colyseus provides explicit reconnection handling with automatic retry/backoff plus server-side `allowReconnection()`. ([Cloudflare WebSockets](https://developers.cloudflare.com/network/websockets/), [Colyseus Reconnection](https://docs.colyseus.io/room/reconnection))
   - [INFERRED] In practice, the user-visible failure is not "the cluster is underprovisioned." It is "my phone slept, I refreshed, and the game feels broken." Reconnect correctness becomes trust-critical before headline scale does.

5. **From hobby uptime to expected uptime**
   - [INFERRED] Once guests are invited at a scheduled time, home-box sleep, ISP weirdness, certificate drift, and manual startup steps become product issues, not operator quirks.

### What Resource Constraints Actually Mean In Practice

- [INFERRED] **Limited money** does not only mean "fewer concurrent players." It means:
  - less ability to buy always-on infrastructure
  - less tolerance for wasteful architecture
  - less room for managed observability, backups, and failover
  - more pressure to keep the stack legible enough to restart manually during game night
- [INFERRED] **Limited compute** on a personal box means room state, media serving, compilation, database work, and tunnel overhead all compete on the same machine. The pain will likely appear first as join slowness, timer drift under load, or media latency rather than clean CPU exhaustion.
- [INFERRED] **Limited operator time** is probably the scarcest resource of all. A technically elegant deployment that needs handholding every session is worse than a boring one-command stack.
- [INFERRED] **What more money buys beyond more scale**:
  - better uptime and less operator babysitting
  - durable storage and backups
  - easier public HTTPS/domain handling
  - better telemetry when players report "it lagged"
  - safer separation between app server, room state, and persistence
- [CONFIRMED] The only concurrency number this lane can state directly is the Quick Tunnel testing cap from Cloudflare docs; everything else depends on room count, message rate, payload sizes, reconnect behavior, media weight, and the chosen room runtime. ([Quick Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/), [Colyseus Scalability](https://docs.colyseus.io/scalability))

### Transition Patterns That Preserve Trust

- [INFERRED] **Keep the player-facing join grammar stable across stages.** The room code should stay human-readable. The join URL should stay canonical. QR should be a convenience layer, not the only path.
- [CONFIRMED] Both Kahoot and Jackbox use this kind of low-friction join pattern: browser entry, code or QR, minimal account burden. ([Jackbox join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Kahoot join](https://support.kahoot.com/hc/en-us/articles/115016109368-How-to-join-games-in-Kahoot-app))
- [INFERRED] **Tell users what mode they are in.** "Local LAN," "private hosted," and "public beta" should feel operationally distinct in UI copy and status messaging. Hidden topology changes erode trust when something fails.
- [INFERRED] **Treat capacity limits as a communication problem, not just an infrastructure problem.** A transparent beta can say:
  - sessions run in windows
  - rooms may queue at peak times
  - reconnect is supported but not guaranteed under every network condition
  - the service is intentionally small while telemetry is gathered
- [HYPOTHESIS] **Donation-supported or community-supported access can be done non-manipulatively** if money buys hosting continuity, more play windows, or more curated content, and does not buy gameplay power, answer advantage, or permanent exclusion of non-payers. This is product judgment, not a source-backed technical conclusion.
- [INFERRED] **If queueing appears later, make it legible.** "Rooms full, next window in 20 minutes" preserves more trust than infinite spinner behavior or fake "almost in" dark patterns.

### Downloadable Local-Host App, Browser-First Website, And Portable Package

- [INFERRED] These can coexist if browser-first remains the canonical product surface and the others are treated as operator packaging choices rather than separate products.
- [INFERRED] The clean hierarchy is:
  1. **Browser-first website** as the canonical guest experience
  2. **Portable local package / Docker bundle** as the operator-friendly way to self-host
  3. **Downloadable local-host app** only if later evidence shows browser-plus-bundle is still too fragile for game-night setup
- [INFERRED] That keeps guest expectations simple while preserving optionality for "play without Logan" or "run it on a spare box."
- [INFERRED] A native wrapper is therefore plausible, but not the right first answer. It should solve a proven operator pain, not hypothetical future polish.

### Questions Requiring Measurement Rather Than Armchair Guessing

- [CONFIRMED] Exact room concurrency on one personal box cannot be honestly stated from docs alone. Colyseus explicitly says per-process capacity depends on many factors. ([Colyseus Scalability](https://docs.colyseus.io/scalability))
- [INFERRED] The following need measurement before any strong capacity promise:
  - join latency on home WiFi with 4 to 12 phones
  - join latency over tunnel/public HTTPS
  - reconnect success after phone sleep/wake
  - bandwidth and load-time cost of clue media
  - CPU and memory cost per active room
  - score/timer correctness under packet loss or flaky mobile networking
  - operator setup time from cold boot to "room is joinable"
- [INFERRED] The most important first benchmark is probably not "max users." It is "can a real host get a room running in minutes and can real phones stay synchronized through a whole session?"

## Viable Paths

| Path | Shape | Strengths | Main Risks | Best Fit |
|---|---|---|---|---|
| A | Browser-first everywhere, LAN first, then `dionysus`, then VPS/public host | Maximum continuity, one mental model, strongest alignment with current roadmap | Requires early discipline around self-host-friendly room runtime and deploy topology | Strongest default path |
| B | Browser-first app plus tunnels as the bridge stage | Fastest route from private testing to remote play | Tunnel limits, operator dependency, temptation to treat bridge tooling as final infra | Good bridge, weak final home |
| C | Managed public-first realtime stack earlier than self-host maturity | Easiest route to polished remote/public access | Weaker parity with LAN/self-host goals, easier to drift into platform/vendor assumptions | Worth revisiting only if public beta becomes near-term priority |
| D | Native/local-host wrapper early | Could reduce operator friction for non-technical hosts | Creates packaging surface area before the browser-first product is proven | Not first-line; defer until browser-only pain is measured |

- [INFERRED] Path A is the best-fit default for the current posture because it preserves optionality while matching the roadmap’s emphasis on authoritative rooms, controller join, and private social play.
- [INFERRED] Path B is valuable as a transition layer, not as the long-term architecture story.
- [INFERRED] Path C is a legitimate alternative, but it should be chosen deliberately as a product-direction change, not drifted into accidentally.

## Key Tradeoffs And Hidden Assumptions

- [INFERRED] A low-friction guest join experience pushes the stack toward standard browser HTTPS/WebSocket access and away from "everyone install a networking tool."
- [INFERRED] Strong self-host parity pushes the stack toward a runtime and deployment model that can run cleanly on one ordinary machine before it runs on many.
- [INFERRED] Public-beta ambitions push the project toward ingress hardening, status messaging, and queue transparency earlier than the current private-only posture strictly requires.
- [INFERRED] The biggest hidden assumption in many indie hosting discussions is that "scale" is the main problem. For this project, the earlier problems are more likely to be reachability, operator burden, reconnect trust, and media delivery.
- [INFERRED] Another hidden assumption is that "browser-first" and "downloadable app" are mutually exclusive. They are not, if the browser experience stays canonical and packaging is treated as deployment convenience.

## Disconfirming Or Tensioning Evidence

- [CONFIRMED] Tailscale Funnel is in beta and bandwidth-limited. That weakens any argument that it should be the durable public-hosting answer. ([Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel))
- [CONFIRMED] Cloudflare Quick Tunnels are explicitly testing-only and capped at 200 in-flight requests, which makes them inappropriate to treat as a real beta platform. ([Quick Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/))
- [CONFIRMED] Cloudflare supports WebSockets, but also notes that edge restarts can terminate connections. So "tunnel supports websockets" is not the same thing as "realtime sessions never drop." ([Cloudflare WebSockets](https://developers.cloudflare.com/network/websockets/))
- [CONFIRMED] Jackbox-style browser-controller play still depends on cookies, WebSockets, HTML5, and supported browsers. The model is low-friction, not zero-friction. ([Jackbox join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game), [Jackbox connection help](https://support.jackboxgames.com/hc/en-us/articles/15794785923223-I-m-having-trouble-connecting-my-device-to-the-game))
- [CONFIRMED] Colyseus scaling is not magic. Once the project wants multiple processes or machines, Redis-backed presence becomes required. ([Colyseus Presence](https://docs.colyseus.io/server/presence), [Colyseus Scalability](https://docs.colyseus.io/scalability))
- [INFERRED] So the optimistic "just start on one box and scale later" story is true only if the early room core and deployment model are chosen with that transition in mind.

## What Could Change This View

- A measured result showing that media delivery, not room-state sync, is the dominant failure mode
- A decision to prioritize streamer/public discoverability much earlier than the current private-first posture suggests
- Evidence that friends are willing to install operator-adjacent software, which would make Tailscale-centric guest access less costly than it appears now
- A room-runtime decision that deliberately optimizes for managed public infra over self-host parity
- Real benchmark data showing that one-box hosting is either much better or much worse than first-principles reasoning suggests
- A product decision to support asynchronous or challenge-link play earlier, which would reduce some realtime hosting pressure while introducing different storage and identity needs

## Open Questions Worth A Second Pass

1. Should the canonical remote-host bridge be `dionysus` plus Cloudflare Tunnel, or `dionysus` plus a small VPS/reverse-proxy setup?
2. How early should the roadmap formalize deployment/distribution requirements such as LAN startup flow, join URL generation, QR generation, and operator start/stop scripts?
3. Does the chosen room runtime preserve enough self-host parity that "LAN on one machine" and "public beta on a server" still feel like the same product?
4. What exact host-status and queue-status language would make a constrained public beta feel honest rather than shaky?
5. Is the likely first public failure mode media bandwidth, websocket churn, or operator setup friction?
6. How much of "play without Logan" is a real near-term goal versus a nice-to-have future branch?

## Source Ledger

### Primary technical sources

- [Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve)
  - Authority: official vendor docs
  - Used for: tailnet-only sharing behavior
  - Reliability limits: describes product capability, not guest UX quality
- [Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel)
  - Authority: official vendor docs
  - Used for: public-internet sharing, beta status, bandwidth/port limits
  - Reliability limits: vendor docs, not independent ops experience
- [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  - Authority: official vendor docs
  - Used for: outbound-only tunnel behavior, no inbound ports, redundancy, public hostname mapping
  - Reliability limits: Cloudflare-centric perspective
- [Cloudflare Routing](https://developers.cloudflare.com/tunnel/routing/)
  - Authority: official vendor docs
  - Used for: published apps, multi-service tunnel routing
- [Protocols for published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/)
  - Authority: official vendor docs
  - Used for: HTTP vs non-HTTP guest-access differences
- [Cloudflare WebSockets](https://developers.cloudflare.com/network/websockets/)
  - Authority: official vendor docs
  - Used for: WebSocket support and restart caveat
- [Quick Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/)
  - Authority: official vendor docs
  - Used for: explicit testing-only posture and 200 in-flight request cap
- [Colyseus](https://docs.colyseus.io/)
  - Authority: official framework docs
  - Used for: deploy-anywhere posture and authoritative multiplayer framing
- [Colyseus Presence](https://docs.colyseus.io/server/presence)
  - Authority: official framework docs
  - Used for: single-process vs Redis-backed distributed breakpoint
- [Colyseus Scalability](https://docs.colyseus.io/scalability)
  - Authority: official framework docs
  - Used for: room/process model and explicit refusal of one-size-fits-all capacity numbers
- [Colyseus Reconnection](https://docs.colyseus.io/room/reconnection)
  - Authority: official framework docs
  - Used for: reconnect flow and retry behavior
- [Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/)
  - Authority: official Docker docs
  - Used for: one-file multi-container startup/shutdown path
- [MDN Secure Contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Secure_Contexts)
  - Authority: primary documentation for browser behavior
  - Used for: localhost/trustworthy-origin distinction

### Secondary pattern sources

- [Jackbox join](https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game)
  - Authority: official product support doc
  - Used for: room-code plus browser-controller precedent
  - Reliability limits: pattern precedent only
- [Jackbox connection help](https://support.jackboxgames.com/hc/en-us/articles/15794785923223-I-m-having-trouble-connecting-my-device-to-the-game)
  - Authority: official product support doc
  - Used for: practical browser/WebSocket fragility reminders
- [Kahoot join](https://support.kahoot.com/hc/en-us/articles/115016109368-How-to-join-games-in-Kahoot-app)
  - Authority: official product support doc
  - Used for: QR-plus-browser join precedent

### Local project sources

- `/.planning/PROJECT.md`
- `/.planning/ROADMAP.md`
- `/.planning/REQUIREMENTS.md`
- `/.planning/phases/01-authored-round-contract/.continue-here.md`
- `/.planning/audits/2026-04-08-pre-execution-review/SYNTHESIS.md`
- `/.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
