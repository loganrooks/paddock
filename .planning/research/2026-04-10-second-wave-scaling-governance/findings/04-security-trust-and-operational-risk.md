# Lane 04 Findings: Security, Trust, And Operational Risk

Date: 2026-04-10
Lane: `04-security-trust-and-operational-risk`
Status: complete

## Question Space

- [CONFIRMED] This lane asks what new security, trust, abuse, moderation, privacy, and operational risks appear as Prix Guesser moves from local private hosting to self-hosted remote rooms, then possibly to modest public hosting, and maybe later to cooperative or community-supported infrastructure. (`00-ORCHESTRATION.md`, `specs/04-security-trust-and-operational-risk.md`)
- [CONFIRMED] The current product posture still matters: Prix Guesser is presently framed as a private-first, browser-first, host-screen-plus-phone-controller project, with public-release hardening explicitly out of scope for v1. (`.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`)
- [INFERRED] Because of that posture, the relevant risk question is not "how do we secure a mass public platform?" but "which risks become real at each step-change in publicness, and which scary-sounding problems are still mostly theoretical until the project widens its scope?"

## Method And Sources

- [CONFIRMED] I grounded this lane first in repo-local intent and first-wave findings so that risk analysis stayed attached to Prix Guesser's actual staged path rather than a generic multiplayer-web-app threat model. (`.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/REQUIREMENTS.md`, `.planning/phases/01-authored-round-contract/.continue-here.md`, `../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`, `../2026-04-10-vision-hosting-wave/findings/03-precedents-and-trajectories.md`, `../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md`)
- [CONFIRMED] Primary technical claims are based on official or standards-track sources: Colyseus docs, Cloudflare docs, OWASP cheat sheets, MDN, and IETF RFC 8828. (https://docs.colyseus.io/auth/room, https://docs.colyseus.io/room, https://developers.cloudflare.com/network/websockets/, https://developers.cloudflare.com/waf/rate-limiting-rules/, https://developers.cloudflare.com/fundamentals/reference/connection-limits/, https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html, https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html, https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html, https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels, https://www.ietf.org/rfc/rfc8828.html)
- [CONFIRMED] Product-trust and moderation precedent claims are based primarily on official Jackbox support pages and current EU/UK regulator materials, not on fan recollection. (https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game, https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work, https://support.jackboxgames.com/hc/en-us/articles/15794764378519-What-if-I-encounter-trolls-while-playing-Jackbox-Games-titles, https://digital-strategy.ec.europa.eu/en/factpages/user-rights-under-digital-services-act, https://digital-strategy.ec.europa.eu/en/news/commission-harmonises-transparency-reporting-rules-under-digital-services-act, https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/transparency-reporting)
- [CONFIRMED] I also used practitioner/security-research sources where they materially improved realism rather than replacing primary documentation. The most useful example was Snyk Labs' Gitpod writeup because it turns OWASP's WebSocket-origin warnings into a concrete modern exploit chain. (https://labs.snyk.io/resources/gitpod-remote-code-execution-vulnerability-websockets/)
- [CONFIRMED] Reliability limits remain important here: official docs are strong on supported behavior and explicit limits, but weak on what a solo hobby operator can emotionally or socially sustain; vendor moderation pages are strong on current controls, but weaker on failure rates; regulatory sources are relevant for "future publicness" but should not be read as legal advice for Prix Guesser's current private stage.

## Inquiry Trajectory

1. [CONFIRMED] I started from the staged hosting path established in the first wave: LAN play, then self-hosted remote play, then modest public hosting, then only later more distributed operation. (`../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`)
2. [INFERRED] That immediately split the lane into two different questions that are easy to blur together: "what can be attacked technically?" and "what will make players stop trusting the room even without an actual exploit?"
3. [INFERRED] The technical branch then split again into transport/runtime issues, especially WebSocket auth/origin/validation/observability, versus privacy/logging issues.
4. [INFERRED] The trust branch then widened into moderation, operator burden, transparent capacity/status communication, and the point at which "private hobby room" becomes "platform users will expect process."
5. [INFERRED] Cooperative contribution did not stay a pure scaling question. Once I followed that branch, it became mostly a trust-boundary question: who can see traffic, who can mishandle logs or secrets, who users think they are trusting, and whether peer-assist introduces privacy leakage that contradicts the project's likely social expectations.

## Branching Paths And Dependencies

| Branch | Depends On | Why The Dependency Matters |
|---|---|---|
| Public-room security posture | Whether join remains near-anonymous and account-light | [INFERRED] Fast anonymous join lowers friction but weakens repeat-offender control, moderation escalation, and abuse attribution. (https://support.jackboxgames.com/hc/en-us/articles/15794764378519-What-if-I-encounter-trolls-while-playing-Jackbox-Games-titles) |
| Reconnect trust | Room runtime and ingress behavior | [CONFIRMED] WebSocket infrastructure can terminate connections during restarts, and Colyseus reconnect handling is explicit, not magical. (https://developers.cloudflare.com/network/websockets/, https://docs.colyseus.io/room) |
| Moderation burden | Whether the product allows stranger participation, visible text input, or public discovery | [INFERRED] Private trusted circles can survive with lighter controls; streamer-public or semi-public rooms cannot. |
| Telemetry/privacy tradeoff | Whether the operator needs abuse forensics, calibration, or transparency reporting | [CONFIRMED] OWASP recommends logging enough security events to investigate abuse while excluding tokens, session identifiers, and sensitive personal data. (https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html, https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) |
| Cooperative compute risk | Whether "cooperative" means peer-to-peer traffic, volunteer-operated servers, or merely community contribution around content/testing | [INFERRED] Those are not the same trust model, and the peer-to-peer variant introduces privacy and routing tradeoffs that ordinary community authorship does not. |
| Compliance/process burden | How public, persistent, and jurisdictionally exposed the service becomes | [INFERRED] Complaint handling, moderation explanation, and transparency duties rise with publicness faster than with raw player count. (https://digital-strategy.ec.europa.eu/en/factpages/user-rights-under-digital-services-act, https://digital-strategy.ec.europa.eu/en/news/commission-harmonises-transparency-reporting-rules-under-digital-services-act, https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/transparency-reporting) |

## Findings

### Overall Risk Shape

- [INFERRED] For Prix Guesser's near-term path, the highest-probability trust failures are not exotic remote compromise. They are room-admission mistakes, brittle reconnect behavior, overshared logs, unclear host-status communication, and underpowered moderation when stranger access widens.
- [INFERRED] The sharpest step-change is not "one box versus two boxes." It is "trusted invited group" versus "participants the operator does not personally know." That is the point where abuse handling, transparent room rules, and identity/moderation tradeoffs become product-defining instead of incidental.
- [INFERRED] Cooperative or peer-assisted infrastructure looks less like a clean way to dodge hosting cost and more like a new trust surface that must justify itself very carefully.

### Feasibility Split

- [CONFIRMED] **Technical feasibility:** A conventional browser-room stack can be materially hardened with explicit room auth, message validation, ingress rate limiting, reconnect handling, and careful logging. The relevant controls are documented and available, but several are opt-in rather than automatic defaults. (https://docs.colyseus.io/auth/room, https://docs.colyseus.io/room, https://developers.cloudflare.com/waf/rate-limiting-rules/, https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)
- [INFERRED] **Operational feasibility:** A solo or tiny-team operator can likely sustain private rooms and bounded self-hosted remote play, but public or streamer-visible use will create moderation, incident-response, and support burdens before infrastructure cost becomes the dominant pain.
- [INFERRED] **Adoption feasibility:** Account-light browser join remains the best fit for Prix Guesser's social shape, but the same low-friction posture weakens bans, appeals, repeat-offender handling, and other trust controls once rooms are opened beyond known circles. (https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game, https://support.jackboxgames.com/hc/en-us/articles/15794764378519-What-if-I-encounter-trolls-while-playing-Jackbox-Games-titles)
- [INFERRED] **Economic feasibility:** Early client-server rooms on one machine are economically plausible; public moderation workflows, better observability, and any serious TURN/relay or support burden are the more meaningful cost multipliers than raw compute alone.
- [INFERRED] **Ethical and trust feasibility:** Honest disclosure about room privacy, telemetry, reconnect guarantees, and moderation boundaries is not optional once strangers can join. If the operator cannot prevent misuse of logs or cannot explain what is and is not protected, OWASP's privacy guidance suggests the product should tell users plainly rather than imply safety it cannot deliver. (https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html)

### Serious Early-Stage Risks, Later-Stage Risks, And Lower-Priority Scares

| Risk | Stage | Why It Belongs There |
|---|---|---|
| [INFERRED] Missing or weak room admission controls | Early | Public or semi-public room joins are unsafe to treat as "just room codes" if auth/origin/rate limits are weak. |
| [INFERRED] Reconnect fragility and silent disconnects | Early | Players feel these immediately in remote sessions; they read as "the game is broken" rather than "the network is subtle." |
| [INFERRED] Over-collection or over-retention of room logs | Early | Small operators often over-log because it feels safer; OWASP warns this can itself create privacy and secrets exposure risk. (https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) |
| [INFERRED] Abuse and moderation workload from stranger access | Mid-stage, but arrives fast once publicness begins | The burden is social and operational before it is technical. |
| [INFERRED] Formal complaint, transparency, and moderation-review expectations | Later-stage unless publicness widens materially | These become more real when the service starts resembling a platform rather than a hobby room tool. |
| [INFERRED] Sophisticated anti-cheat, ranked-play abuse prevention, adversarial economics | Lower priority for current posture | These are expensive problems, but the current roadmap explicitly avoids the product shapes that make them urgent. (`.planning/REQUIREMENTS.md`, `.planning/PROJECT.md`) |

### User-Felt Failure Modes

- [INFERRED] **"The room keeps dropping people."** Cloudflare explicitly notes that server restarts can terminate WebSocket connections, and Colyseus documents reconnect as an explicit room concern rather than an invisible guarantee. If reconnection feels flaky, players experience that as distrust in the session itself. (https://developers.cloudflare.com/network/websockets/, https://docs.colyseus.io/room)
- [INFERRED] **"I don't know whether I'm actually in a private room."** Once hosting expands beyond same-room LAN play, users need legible signals about whether the room is local-only, privately hosted, or more public. Hidden topology changes create false expectations about privacy and reliability.
- [INFERRED] **"Someone toxic got in and ruined the vibe before the host could react."** Jackbox's own support history is a useful warning that low-friction browser join and minimal identity are great for participation but make troll control harder, especially in streamed or stranger-facing contexts. (https://support.jackboxgames.com/hc/en-us/articles/15794764378519-What-if-I-encounter-trolls-while-playing-Jackbox-Games-titles, https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work)
- [INFERRED] **"The system acted on me and I don't know why."** If profanity filters, join throttles, or anti-abuse gates eventually exist, unexplained rejections will feel arbitrary unless the room communicates what happened in ordinary language.
- [INFERRED] **"I joined a public or semi-public session and now my participation feels more exposed than I expected."** That risk becomes sharper if telemetry, moderation logs, or future audience/streamer features grow before the product has a clear disclosure norm.

### Operator-Felt Failure Modes

- [CONFIRMED] **Open-by-default room admission mistakes.** Colyseus states that if `onAuth()` is left unimplemented, it always returns `true`, allowing any client to connect. That is an acceptable dev convenience and a dangerous public-hosting default. (https://docs.colyseus.io/auth/room)
- [CONFIRMED] **Message-layer blind spots.** Cloudflare documents that the initial HTTP 101 upgrade is inspected by WAF and rate limiting, but once the WebSocket is established, the WAF does not inspect further messages. OWASP separately warns that normal HTTP logs only capture the upgrade request, not message traffic. Together, those two facts mean room-level abuse and validation cannot be outsourced to the edge. (https://developers.cloudflare.com/network/websockets/, https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)
- [CONFIRMED] **Optional validation being treated as implicit safety.** Colyseus supports Zod-backed message validation and per-client `maxMessagesPerSecond`, but both are choices the application must make. (https://docs.colyseus.io/room)
- [INFERRED] **Forensics-versus-privacy tension.** Colyseus exposes token/header/IP context for auth and provides reconnection tokens; OWASP warns against logging session identifiers, access tokens, and sensitive personal data directly. A small operator will feel real pressure to over-log during incidents. (https://docs.colyseus.io/auth/room, https://docs.colyseus.io/room, https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [INFERRED] **Status debt.** Once other people arrange time around a hosted room, unclear queueing, downtime, or "is this the operator's box or a public service?" ambiguity becomes reputational debt even if nobody was actually attacked.

### Risks Introduced By More Publicness

- [CONFIRMED] **Cross-site WebSocket hijacking and session abuse become more important when browser sessions become durable or privileged.** OWASP recommends explicit origin allowlists, SameSite cookies, session revalidation, and server-side expiry for long-lived WebSocket connections. (https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html)
- [CONFIRMED] **This risk is not theoretical.** Snyk Labs documented a Gitpod case where WebSocket hijacking plus a practical SameSite bypass led to full takeover after visiting a link. That exact exploit chain may not map 1:1 to Prix Guesser, but it proves the class of mistake remains live in modern browser/WebSocket systems. (https://labs.snyk.io/resources/gitpod-remote-code-execution-vulnerability-websockets/)
- [INFERRED] **Room codes become bearer capabilities, not real identity.** That is often fine for private friend groups. It becomes weak once room links or codes are visible on streams, shared publicly, or brute-forced at scale. Rate limiting can slow this down, but it does not create trust or accountability by itself. (https://developers.cloudflare.com/waf/rate-limiting-rules/, https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game)
- [INFERRED] **Moderation ceases to be a streamer-only edge case.** The moment public rooms, semi-public room discovery, or public pack sharing appear, users start expecting report paths, appeal paths, consistent enforcement, and explanations for moderation outcomes. EU and UK public-policy materials show how quickly transparency and complaint handling become part of the platform conversation once a service becomes broadly public. (https://digital-strategy.ec.europa.eu/en/factpages/user-rights-under-digital-services-act, https://digital-strategy.ec.europa.eu/en/news/commission-harmonises-transparency-reporting-rules-under-digital-services-act, https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/transparency-reporting)
- [INFERRED] **Capacity and security become socially entangled.** In a modest public beta, "service full," "moderation delayed," and "room unavailable" are not merely ops metrics; they signal whether the project is honest about its limits or quietly overpromising.

### Risks Introduced By Cooperative Contribution

- [CONFIRMED] **Peer-assisted transport has real privacy/performance tradeoffs.** IETF RFC 8828 says WebRTC can reveal additional public and private IP address information to web applications, can bypass proxies in some cases, and creates explicit privacy-versus-media-quality tradeoffs. (https://www.ietf.org/rfc/rfc8828.html)
- [CONFIRMED] **Peer-assisted transport also has real privacy benefits.** MDN notes that `RTCDataChannel` traffic is encrypted with DTLS and, because it is peer-to-peer, the data does not pass through the web or application server. (https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels)
- [INFERRED] **That means cooperative transport is neither obviously safer nor obviously riskier.** It shifts trust: less centralized traffic visibility, more participant-network visibility, harder observability, and more user confusion about who can see what.
- [INFERRED] **"Community compute" and "peer-to-peer room traffic" should not be treated as one idea.** Trusted volunteers operating a known server is a governance problem. End users relaying one another's live room traffic is a privacy, routing, abuse, and support problem.
- [INFERRED] **Economically tempting does not mean trust-feasible.** Peer-assisted delivery can look attractive if hosting cost becomes painful, but if the price is exposing participant network information, weakening supportability, or requiring subtle consent flows, the trust cost may dominate the compute savings.
- [HYPOTHESIS] **The safest cooperative contribution shapes are probably not live traffic relays.** They are more likely to be authored packs, test hosting inside trusted circles, bug triage, translation, or operator-reviewed community mirrors rather than end-user peer relays.

### Some Risks Are Better Mitigated By Product-Scope Restraint Than By Technical Complexity

- [INFERRED] **Keeping v1 private-room-only is itself a security control.** It avoids the need to pretend Prix Guesser has solved stranger moderation, appeals, transparency reporting, repeat-offender identity, or public-room abuse when it has not.
- [INFERRED] **Avoiding open text chat, public room discovery, and anonymous public pack publishing early is more honest than shipping thin filters and calling the problem solved.**
- [INFERRED] **Not adding payments or entitlement tiers early also avoids a whole class of fraud, chargeback, access-control, and fairness disputes that are orthogonal to proving the game-night loop.**
- [INFERRED] **Scope restraint is not permanent strategy.** It is a way to avoid converting unsolved governance and trust problems into technical debt disguised as "features."
- [INFERRED] **Scope restraint stops helping once the product explicitly seeks stranger participation, streamer-public rooms, or community hosting.** At that point, the hidden risk becomes a mismatch between the product's public posture and its actual operational maturity.

## Gray Areas And Live Tensions

- [INFERRED] **Fast guest join versus meaningful accountability** is still live. Jackbox-like no-account browser join is socially strong, but the same choice makes bans, moderation history, and public-room abuse handling much weaker. (https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game, https://support.jackboxgames.com/hc/en-us/articles/15794764378519-What-if-I-encounter-trolls-while-playing-Jackbox-Games-titles)
- [INFERRED] **Better observability versus privacy minimization** is still live. OWASP is right that security teams need logging; OWASP is also right that tokens, session identifiers, PII, and opt-out data should not simply be dumped into logs. (https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html, https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [INFERRED] **Peer-to-peer privacy benefit versus peer-to-peer exposure** is still live. WebRTC can remove central interception opportunities and still expose more network information or create fingerprinting surfaces. (https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels, https://www.ietf.org/rfc/rfc8828.html)
- [INFERRED] **Technical possibility versus operator sustainability** is still live. A solo operator can technically run a semi-public service sooner than they can sustain the moderation, explanations, and trust repair work that publicness creates.
- [INFERRED] **Future regulatory expectations versus current private-only posture** is still live. It would be premature to build full public-platform governance now; it would also be reckless to assume those expectations appear only at "big tech" scale.

## Scope Expansions

- [INFERRED] **Scope Expansion: moderation transparency and complaint handling.** This emerged because once the research followed "more publicness" seriously, moderation stopped being only a profanity-filter question and became a trust-and-process question. I pursued this enough to establish that complaint and explanation expectations are structurally real, but not enough to produce jurisdiction-specific legal guidance. (https://digital-strategy.ec.europa.eu/en/factpages/user-rights-under-digital-services-act, https://digital-strategy.ec.europa.eu/en/news/commission-harmonises-transparency-reporting-rules-under-digital-services-act, https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/transparency-reporting)
- [INFERRED] **Scope Expansion: logging minimization as part of trust, not just security.** This emerged because WebSocket abuse investigation and small-operator debugging both push toward over-collection. I pursued it because it directly affects whether users can reasonably trust a hobby-hosted room service. (https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [INFERRED] **Scope Expansion: peer-to-peer privacy tradeoffs.** This emerged because "cooperative contribution" initially sounded like a hosting-cost question, but primary sources quickly made it a privacy and consent question as well. I pursued this branch to the point of clarifying that cooperative hosting and peer-assisted traffic are materially different ideas. (https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels, https://www.ietf.org/rfc/rfc8828.html)

## Rival Models Still Alive

- [INFERRED] **Model A: private-room software with deliberate scope restraint.** This remains the cleanest fit for the current roadmap and postpones several hard trust problems honestly.
- [INFERRED] **Model B: modest public beta with bounded publicness.** This is still viable if the product adds explicit room-admission policy, rate limiting, reconnect transparency, manual moderation controls, and honest capacity/status messaging before broad discovery.
- [HYPOTHESIS] **Model C: community-operated mirrors without peer relays.** This remains viable in principle if trust boundaries are explicit and operator responsibilities are narrow, but I do not yet have enough evidence to recommend it.
- [HYPOTHESIS] **Model D: peer-assisted or cooperative traffic relay.** This is still technically alive, but it currently looks like the weakest fit because it multiplies privacy and support ambiguity before solving Prix Guesser's more immediate trust problems.

## Practical Implications

### Thinking Implications

- [INFERRED] Trust should be treated as a composite of reliability, moderation containment, privacy clarity, and honest status communication, not merely "absence of hacks."
- [INFERRED] The project should talk about "publicness levels" explicitly: trusted private room, self-hosted remote room, bounded public beta, and only later wider public surfaces.

### Design Implications

- [INFERRED] Room UI should eventually communicate hosting/privacy mode, reconnect state, and room-admission expectations plainly instead of treating them as invisible infrastructure details.
- [INFERRED] If public or streamer-facing participation is ever added, hosts need proactive controls, not only reactive cleanup. Jackbox's moderation and kick tooling are good precedent for that shape even if Prix Guesser's content differs. (https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work)
- [INFERRED] Design should assume host-screen trust and player-controller trust are different. The player needs clarity about privacy and join state; the host needs clarity about admissions, moderation, and room health.

### Implementation Implications

- [CONFIRMED] Implement explicit room auth instead of relying on framework defaults, because Colyseus otherwise allows any client to connect. (https://docs.colyseus.io/auth/room)
- [CONFIRMED] Validate room messages and set sane per-client message limits because Colyseus documents both features as available and optional. (https://docs.colyseus.io/room)
- [CONFIRMED] Treat ingress rate limiting as necessary but insufficient. Cloudflare can protect request entry points, but app code still has to validate and police in-room traffic. (https://developers.cloudflare.com/waf/rate-limiting-rules/, https://developers.cloudflare.com/network/websockets/)
- [CONFIRMED] Plan for reconnect as a first-class trust feature, because the network edge may terminate WebSockets and Colyseus reconnect depends on explicit room logic and reconnection tokens. (https://developers.cloudflare.com/network/websockets/, https://docs.colyseus.io/room)
- [INFERRED] Keep telemetry narrow by default: room lifecycle, auth outcomes, disconnect/reconnect outcomes, rate-limit hits, and moderation events are likely the highest-value early events; raw player submissions and raw tokens are much more dangerous to retain.
- [INFERRED] If cooperative hosting is explored later, prefer explicit operator-run servers or sanctioned mirrors long before any experiment that asks end users to relay one another's live traffic.

### Measurement Or Experiment Implications

- [INFERRED] Measure reconnect success and user comprehension, not just disconnect counts.
- [INFERRED] Measure operator minutes per session spent on setup, moderation, and recovery, because those are likely earlier bottlenecks than CPU.
- [INFERRED] Measure how often room codes or links leak outside the intended circle during playtests if the project ever experiments with streamer-friendly sessions.
- [INFERRED] If any cooperative experiment happens, explicitly test whether users understand what traffic is direct peer-to-peer, what metadata may be exposed, and whether they can opt out without losing the core experience.

## What Would Change This View

- [INFERRED] Evidence that Prix Guesser will remain a trusted-circle tool for much longer than current exploration implies would lower the urgency of moderation-process and public-trust work.
- [INFERRED] A decision to adopt a more managed runtime with stronger built-in identity, moderation, or public-room governance features would shift some recommendations away from scope restraint and toward managed controls.
- [INFERRED] Playtest evidence showing that stranger participation is rare while room-link leakage is common would raise the priority of join-surface hardening but lower the priority of broader moderation systems.
- [HYPOTHESIS] Strong evidence that users are willing to accept clearly explained peer-assisted delivery in exchange for lower latency or lower cost could reopen the cooperative-relay branch. I do not currently have such evidence.
- [INFERRED] Concrete legal/product decisions about public discovery, payments, public pack sharing, or streamer-facing rooms would make the currently "later-stage" governance risks more immediate.

## Open Questions Worth A Third Pass

1. [INFERRED] What is the lightest identity layer that preserves browser-first join while still enabling repeat-offender controls if rooms become semi-public?
2. [INFERRED] Which public surface arrives first, if any: public room discovery, semi-public pack sharing, spectator access, or streamer-facing sessions?
3. [INFERRED] What exact telemetry fields are actually needed for round calibration and abuse forensics, and which tempting fields should be prohibited by default?
4. [HYPOTHESIS] Is there a narrow cooperative-hosting model that adds resilience without diffusing trust boundaries too far, such as sanctioned friend-circle mirrors rather than volunteer public mirrors?
5. [INFERRED] What status-copy and privacy-copy would make a constrained hosted beta feel honest rather than amateurishly vague?
6. [INFERRED] How much moderation burden disappears if Prix Guesser keeps user-generated text surfaces extremely narrow, and how much still remains simply from public join?

## Source Ledger

### Primary Technical Sources

- [CONFIRMED] `Colyseus Room Authentication` — used for the fact that `onAuth()` is optional, that unimplemented auth allows any client to connect, and that auth context includes token, headers, and IP.  
  https://docs.colyseus.io/auth/room  
  Reliability limits: framework docs describe capabilities and defaults, not complete app-security posture.

- [CONFIRMED] `Colyseus Rooms` — used for message validation, `maxMessagesPerSecond`, reconnect tokens, room privacy/listing controls, and room lifecycle details.  
  https://docs.colyseus.io/room  
  Reliability limits: framework docs do not prove a given Prix Guesser implementation will use these features correctly.

- [CONFIRMED] `Cloudflare WebSockets` — used for the fact that WAF inspects only the initial upgrade, that Cloudflare may restart servers and terminate WebSockets, and that WebSocket usage is counted largely at connection level.  
  https://developers.cloudflare.com/network/websockets/  
  Reliability limits: Cloudflare-centric view of ingress; does not solve application-layer abuse.

- [CONFIRMED] `Cloudflare Rate Limiting Rules` — used for rate-limiting/brute-force-abuse claims at ingress.  
  https://developers.cloudflare.com/waf/rate-limiting-rules/  
  Reliability limits: only covers request-level controls, not in-room message semantics.

- [CONFIRMED] `Cloudflare Connection Limits` — used for connection timeout/idle-limit operational risk context.  
  https://developers.cloudflare.com/fundamentals/reference/connection-limits/  
  Reliability limits: infrastructure-specific, not whole-system behavior.

- [CONFIRMED] `OWASP WebSocket Security Cheat Sheet` — used for origin allowlists, SameSite/session management, DoS, and monitoring/logging guidance.  
  https://cheatsheetseries.owasp.org/cheatsheets/WebSocket_Security_Cheat_Sheet.html  
  Reliability limits: best-practice guidance, not product-specific evidence.

- [CONFIRMED] `OWASP Logging Cheat Sheet` — used for "do not log tokens/session IDs/PII" guidance.  
  https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html  
  Reliability limits: generic guidance; retention specifics remain product/jurisdiction dependent.

- [CONFIRMED] `OWASP User Privacy Protection Cheat Sheet` — used for honesty/transparency guidance when protections are incomplete.  
  https://cheatsheetseries.owasp.org/cheatsheets/User_Privacy_Protection_Cheat_Sheet.html  
  Reliability limits: normative guidance, not implementation detail.

- [CONFIRMED] `MDN Using WebRTC data channels` — used for DTLS encryption and the nuance that peer-to-peer traffic does not pass through the app server.  
  https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels  
  Reliability limits: MDN is high-quality browser documentation, but not a governance guide.

- [CONFIRMED] `IETF RFC 8828` — used for WebRTC IP exposure, proxy bypass, fingerprinting, and privacy/performance tradeoffs.  
  https://www.ietf.org/rfc/rfc8828.html  
  Reliability limits: standards-track guidance on browser/network behavior, not a product recommendation by itself.

### Primary Product, Governance, And Trust Sources

- [CONFIRMED] `Jackbox join/moderation/troll-support docs` — used for low-friction browser join precedent and the tradeoff between anonymous participation and moderation difficulty.  
  https://support.jackboxgames.com/hc/en-us/articles/15794759479959-How-do-I-join-a-game  
  https://support.jackboxgames.com/hc/en-us/articles/15794773430295-How-does-Moderation-work  
  https://support.jackboxgames.com/hc/en-us/articles/15794764378519-What-if-I-encounter-trolls-while-playing-Jackbox-Games-titles  
  Reliability limits: good precedent for social-room tradeoffs, but Jackbox's runtime and content model differ from Prix Guesser's browser-hosted ambitions.

- [CONFIRMED] `European Commission DSA user-rights and transparency materials` — used to show that complaint handling, explanations, and transparency become part of the expectations landscape once a service is public enough.  
  https://digital-strategy.ec.europa.eu/en/factpages/user-rights-under-digital-services-act  
  https://digital-strategy.ec.europa.eu/en/news/commission-harmonises-transparency-reporting-rules-under-digital-services-act  
  Reliability limits: relevant to future publicness, not direct legal advice for current private use.

- [CONFIRMED] `Ofcom Online Safety transparency-reporting statement` — used as an additional regulator signal that transparency and safety-process burden are real operational concerns for public online services.  
  https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/transparency-reporting  
  Reliability limits: UK-specific regulatory context; applicability depends on service shape and jurisdiction.

### Secondary Practitioner Sources

- [CONFIRMED] `Snyk Labs Gitpod WebSocket Hijacking writeup` — used as practitioner evidence that missing origin validation plus cookie/session assumptions can become a modern real-world exploit chain, not just a checklist item.  
  https://labs.snyk.io/resources/gitpod-remote-code-execution-vulnerability-websockets/  
  Reliability limits: one concrete case study in a very different product category; useful for plausibility, not for direct architectural equivalence.

- [CONFIRMED] `Microsoft Game Dev / Community Sift article` — used as a practitioner/vendor signal that moderation at scale is operationally costly, policy-specific, and increasingly entangled with transparency expectations.  
  https://developer.microsoft.com/en-us/games/articles/2024/03/community-sift-and-the-future-of-content-moderation/  
  Reliability limits: explicitly vendor-framed and partly promotional; treated here as directional rather than dispositive.

### Local Project Sources

- [CONFIRMED] `.planning/PROJECT.md` — current posture and out-of-scope framing.
- [CONFIRMED] `.planning/ROADMAP.md` — staged room/reconnect plan and current absence of public-platform goals.
- [CONFIRMED] `.planning/REQUIREMENTS.md` — current requirements and explicit avoidance of public matchmaking/ranked infrastructure.
- [CONFIRMED] `.planning/phases/01-authored-round-contract/.continue-here.md` — strategic pause and future-breadth tensions.
- [CONFIRMED] `../2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md` — hosting stages and operator-trust framing.
- [CONFIRMED] `../2026-04-10-vision-hosting-wave/findings/03-precedents-and-trajectories.md` — precedent framing for join, moderation, and public-transition analogies.
- [CONFIRMED] `../2026-04-10-vision-hosting-wave/findings/04-future-aware-planning.md` — where future-protection belongs in planning rather than hidden assumption.
