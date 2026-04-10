# Lane 3: Stakeholder & Distribution Reality Check

**Audit date:** 2026-04-08
**Scope:** PROJECT.md, REQUIREMENTS.md, ROADMAP.md, research artifacts, machine context (dionysus)
**Verdict:** The current planning documents describe an excellent game architecture but are almost entirely silent on how the finished product actually reaches the player. Distribution, deployment, and operational simplicity are not mentioned in any requirement, phase, or success criterion. This is the single largest gap between what the project plans to build and what the stakeholders actually need.

---

## 1. Local Play Distribution

### The question
Can a non-technical F1 fan friend realistically start a game on their own laptop?

### Reality check

**No, not with the current stack as planned.** The recommended stack (React + Vite + Colyseus + PostgreSQL + Drizzle + Supabase) assumes a developer-operated environment. To run this locally, a user would need:

- Node.js 24 installed
- pnpm (via corepack) installed
- PostgreSQL running locally or a Supabase project configured
- Environment variables set for database connection, Google Maps API key, and Supabase credentials
- `pnpm install` + `pnpm dev` for both the web client and the Colyseus room server

This is a developer workflow, not a friend workflow. Even Logan would need to remember multiple terminal commands each time.

**What "easy local play" actually requires:**

| Approach | Effort to use | Effort to build | Best for |
|----------|---------------|-----------------|----------|
| `docker compose up` | Install Docker, one command | Medium | Logan hosting on his own machines |
| Single start script (`./start.sh`) | Clone repo, run script | Low | Logan hosting on his own machines |
| Pre-built Electron/Tauri app | Double-click an app | High | Friends hosting on their own laptops |
| Hosted web app (Logan runs server) | Open a URL | Zero for friends | The real answer for non-technical friends |
| Static site + serverless | Open a URL | Medium-high | Public hosting without a persistent server |

**Assessment:** The project documents treat "private-only" as meaning "no public release hardening," but they have not confronted the distribution implication: if the product cannot be trivially accessed by non-technical friends, the social play fantasy does not work. The most realistic path for v1 is that Logan hosts it, and friends connect to it. Asking friends to install Node.js and run a dev server is not viable.

### Recommendation

**Do not plan for friends to self-host.** Plan for Logan to host, and friends to connect via browser. The distribution question then collapses to: "How do friends reach Logan's server?"

---

## 2. Phone Controller Join Flow

### The question
What is the simplest path for friends to join from their phones?

### Reality check

ROOM-02 correctly identifies the need: "Guest can join a private room from phone or browser via room code, join link, or QR flow without needing a full account." This is good. The gap is that the planning documents do not specify HOW the phone discovers the server address.

**The join flow has two parts:**

1. **Finding the server** -- getting the right URL into the phone browser
2. **Joining the room** -- entering a code or tapping a link

Part 2 is well-specified. Part 1 is completely unaddressed.

**For local (same-WiFi) play:**

The host laptop's local IP address (e.g., `192.168.1.42:3000`) must reach the phone. This works if:
- The host laptop runs the server
- Both devices are on the same WiFi network
- No aggressive network isolation (some corporate/hotel WiFi blocks device-to-device traffic)

The best UX for this: the host screen displays a QR code containing the local URL. Friends scan it with their phone camera. No typing, no app install, no account creation.

**For online (dionysus-hosted) play:**

Friends need to reach the dionysus server. The URL depends on the hosting strategy (see sections 5 and 6 below).

### Recommendation

- **QR code on host screen is the correct primary join mechanism.** It should encode the full URL including room code.
- **The host screen should auto-detect and display the correct server address** based on whether play is local or remote.
- **No app install should ever be required for guests.** Browser-only is correct.
- **Add a requirement** (or amend ROOM-02) to specify that the join flow must work without any prior setup on the guest's device beyond a modern phone browser.

---

## 3. Cast to TV

### The question
What does "cast to TV" actually mean technically?

### Reality check

The project documents repeatedly reference "host-screen-friendly," "watchable shared-screen," and "cast to TV" without specifying the casting mechanism. There are several options, and they have different implications:

| Method | How it works | Requirements | UX quality |
|--------|-------------|--------------|------------|
| HDMI cable from laptop | Direct display mirroring/extension | HDMI cable + adapter | Best: zero latency, full resolution |
| Chromecast tab cast | Chrome "Cast" tab to Chromecast | Chromecast device on same WiFi | Good: slight latency, easy |
| AirPlay mirroring | macOS/iOS screen mirror to Apple TV | Apple TV on same WiFi | Good: slight latency, easy |
| Smart TV browser | Open the host URL directly on the TV's browser | Smart TV with decent browser | Variable: TV browsers are unreliable |
| HDMI from dionysus | Run headless, open browser remotely | Long HDMI run or nearby TV | Niche |

**Assessment:** The app does not need to be "cast-aware." It just needs to render a good full-screen host display in a standard browser. The casting is handled by the OS/hardware, not the application. The one design implication: the host display should be designed for TV-distance readability (large text, high contrast, no tiny UI elements, 16:9 aspect ratio assumption).

**The most common real scenario:** Logan opens a browser on his laptop, plugs in HDMI to the TV, and opens the host screen in full-screen mode. Friends scan the QR code displayed on the TV.

### Recommendation

- **No cast-aware application code is needed.**
- **The host display UI should be explicitly designed for TV-distance viewing** -- this is a design requirement, not a technical one.
- **UX-01 should be strengthened** to include readability at 3+ meters, 16:9 layout assumption, and full-screen mode support.
- **Phase 5 (Host Screen) should include a design constraint** for TV-distance readability.

---

## 4. Local to Online Transition

### The question
How does the architecture evolve from "everyone on same WiFi" to "hosted on dionysus"?

### Reality check

**This is actually straightforward if the architecture is server-authoritative from the start,** which it is. The Colyseus room server model means:

- A server process runs the room state machine
- Clients connect via WebSocket
- The server URL is the only thing that changes between local and remote

The transition is:

| Mode | Server runs on | Clients connect to | What changes |
|------|---------------|-------------------|--------------|
| Local couch play | Logan's laptop | `192.168.x.x:3000` | Nothing in code |
| Remote online play | dionysus | `<public-or-tailscale-url>:3000` | Server address only |
| Hybrid | dionysus | Mix of local and remote friends | Server address only |

**The architecture does not need to change.** The deployment target changes. This is a strength of the Colyseus-based server-authoritative model.

**What does need to exist:**

1. A deployment mechanism for dionysus (Docker Compose, systemd service, or just a shell script)
2. A way for remote friends to reach dionysus (Tailscale, domain, or tunnel)
3. The client must not hardcode `localhost` -- it needs to discover or be configured with the server URL

### Recommendation

- **The architecture is correct for this transition.** No structural changes needed.
- **Add a deployment/distribution phase or requirement** to address the server URL configuration and deployment automation.
- **The client should read the server URL from configuration or auto-detect** (same-origin for hosted, or an environment variable / build-time config for local dev).

---

## 5. Tailscale-Only Hosting

### The question
Could this work with just Tailscale and no domain?

### Reality check

**Yes, but only if all players install Tailscale.** This is a significant barrier for non-technical friends.

| Aspect | Reality |
|--------|---------|
| Logan accessing dionysus | Already works. Tailscale is installed on all Logan's devices. |
| Friends installing Tailscale | Requires: create account, install app, accept invite to tailnet. This is 5-10 minutes of friction per friend. |
| Ongoing UX | Once installed, friends access `http://100.93.212.44:3000` or a Tailscale MagicDNS name like `http://dionysus:3000`. Clean. |
| Phone play via Tailscale | Tailscale mobile app exists for iOS and Android. Works, but drains battery and some friends may find the VPN indicator confusing. |
| Network reliability | Tailscale is excellent. DERP relay handles NAT traversal. Very reliable. |

**The Tailscale UX problem is a one-time cost per friend.** Once set up, it works seamlessly. But the initial ask -- "install this VPN app and join my network before we can play" -- is real friction for a casual game night.

**Hybrid approach:** For local couch play, no Tailscale needed (same WiFi). For remote play with tech-comfortable friends, Tailscale works well. For remote play with truly non-technical friends, a public tunnel is better.

### Recommendation

- **Tailscale is a good Phase 1 remote play solution** for the core friend group willing to set it up once.
- **Do not make Tailscale the only remote play path.** Plan for a public-access alternative.
- **Provide a one-page setup guide** for friends who need to install Tailscale.

---

## 6. Domain and Public Hosting

### The question
What if Logan wants friends to connect without Tailscale?

### Reality check

There are several approaches, ranked by simplicity:

### Option A: Cloudflare Tunnel (Recommended)

| Aspect | Detail |
|--------|--------|
| How it works | `cloudflared` daemon on dionysus creates an outbound tunnel to Cloudflare's edge. Friends connect to `prix.loganrooks.com` (or similar). Cloudflare proxies traffic back through the tunnel. |
| Requirements | Domain name (~$10/year), free Cloudflare account, `cloudflared` installed on dionysus |
| HTTPS | Automatic via Cloudflare |
| No port forwarding | Correct. No router config needed. |
| WebSocket support | Yes, Cloudflare proxies WebSockets |
| On-demand hosting | Start `cloudflared` when you want to play, stop when done |
| Cost | Domain only. Tunnel is free tier. |
| Complexity | Low. One config file, one systemd service. |

This is the strongest option because it gives friends a clean URL with HTTPS, requires zero setup on their end, and does not expose dionysus directly to the internet.

### Option B: Tailscale Funnel

| Aspect | Detail |
|--------|--------|
| How it works | Tailscale can expose a local port to the public internet via `tailscale funnel` |
| Requirements | Tailscale installed on dionysus (already done), enable Funnel in admin console |
| HTTPS | Automatic via Tailscale |
| URL | `https://dionysus.<tailnet-name>.ts.net` (long but works) |
| Limitations | Funnel is still somewhat limited. Port restrictions, less control over caching. WebSocket support exists but is newer. |
| Cost | Free with Tailscale |

A simpler alternative if Logan does not want to buy a domain. The URL is ugly but functional.

### Option C: Direct Port Forwarding

Not recommended. Exposes dionysus directly to the internet, requires router configuration, no automatic HTTPS, and is fragile if the ISP changes the IP.

### Option D: Cloud VPS

Run the game server on a cheap cloud VPS (Hetzner, DigitalOcean, etc.) instead of dionysus. This would provide a stable public IP and domain, but costs money monthly and moves away from the "use my own hardware" model. Only worth considering if dionysus becomes unreliable.

### Recommendation

- **Phase 1 (local play):** No domain needed. Same-WiFi only.
- **Phase 2 (remote with close friends):** Tailscale. Friends install it once.
- **Phase 3 (remote with any friend):** Cloudflare Tunnel + a domain. The gold standard for "hosted only when we want to play" with zero friction for guests.
- **Tailscale Funnel as a quick fallback** if the domain approach is delayed.

---

## 7. "Hosted Only When We Want to Play"

### The question
What does this deployment model look like?

### Reality check

This is a solved pattern. The question is just which automation level to target.

### Level 1: Manual (Minimal)

```bash
# SSH into dionysus
ssh dionysus

# Start the game
cd ~/workspace/projects/prix-guesser
docker compose up -d

# When done
docker compose down
```

Pros: Simple, Logan already knows SSH.
Cons: Requires SSH access, remembering the commands.

### Level 2: One-Command Script

```bash
# From any device on Tailscale
ssh dionysus "cd ~/workspace/projects/prix-guesser && docker compose up -d"

# Or a convenience script
ssh dionysus prix-start   # alias or script in ~/scripts/
ssh dionysus prix-stop
```

Pros: One command from phone or laptop.
Cons: Still requires SSH access.

### Level 3: Systemd Timer or On-Demand

A systemd service that is not always running but can be started on demand:

```bash
# From dionysus
sudo systemctl start prix-guesser

# Auto-shutdown after 6 hours of no activity (optional timer)
```

Pros: Clean OS integration, can add auto-shutdown.
Cons: Slightly more setup.

### Level 4: Phone Shortcut (Best UX)

An iOS Shortcut or Tasker automation that SSHes into dionysus and starts/stops the server. Logan taps one button on his phone to spin up game night.

Pros: Zero-friction for Logan. "Hey Siri, start game night."
Cons: Initial setup of the shortcut.

### Recommendation

- **Target Level 2 for v1:** A `prix-start` / `prix-stop` script pair on dionysus.
- **Include Docker Compose** as the deployment format. It bundles the web server, room server, and database into one unit.
- **Add auto-shutdown** (either via timer or idle detection) so Logan does not accidentally leave the server running.
- **Consider Level 4** as a quality-of-life improvement after the core game works.

---

## 8. Current Tech Stack Fit

### The question
Does the monorepo + pnpm + TypeScript approach serve or hinder these goals?

### Reality check

**The monorepo and TypeScript approach is correct for development. It is irrelevant to distribution.** The end user never sees pnpm, never runs TypeScript, never clones a repo. What they see is a URL in their phone browser.

| Stack element | Development impact | Distribution impact |
|---------------|-------------------|---------------------|
| Monorepo (pnpm workspaces) | Good: shared types, one repo | None: build artifacts are what ship |
| TypeScript | Good: safety, shared contracts | None: compiles to JS |
| React + Vite | Good: fast dev, good ecosystem | Good: produces static assets that can be served from anywhere |
| Colyseus | Good: authoritative rooms | Deployment: needs a Node.js process running on the server |
| PostgreSQL | Good: relational content | Deployment: needs a database process |
| Supabase | Convenient for dev | **Concern: adds an external dependency for what could be a self-contained local deployment** |

**The Supabase question is the only real tension.** For a "hosted only when we want to play" model, depending on Supabase means:

- The game requires internet connectivity even for local play (to reach Supabase)
- Supabase free tier has cold-start pauses
- If Supabase changes terms or has an outage, the game breaks

**Alternative:** Use PostgreSQL directly (no Supabase) for the self-hosted model. SQLite could even work for v1 given the small data scale, and would eliminate the database process entirely.

### Recommendation

- **Monorepo + pnpm + TypeScript is correct.** Keep it.
- **Reconsider the Supabase dependency for v1.** A local PostgreSQL in Docker (or even SQLite) is better for a self-hosted private game that should work without internet.
- **Supabase can be added later** if the project needs cloud storage, auth, or a public-facing mode.
- **The build output should be a Docker image** (or Docker Compose config) that bundles everything needed to run.

---

## 9. Packaging Options

### The question
Should we think about Electron, Tauri, Docker, or just a hosted web app?

### Assessment

| Option | What it gives you | What it costs | Verdict |
|--------|------------------|---------------|---------|
| **Hosted web app** (Logan runs server, friends open URL) | Zero install for friends, works on any phone/laptop, one deployment target | Logan must run a server | **The correct v1 answer** |
| **Docker Compose** (for server packaging) | One-command deploy on dionysus, reproducible, includes all dependencies | Logan needs Docker (already installed on dionysus) | **The correct deployment mechanism** |
| **Electron** (desktop app) | Double-click to run, could embed server | Huge binary (~150MB+), platform-specific builds, maintains two deployment modes | **Not worth it** for this project |
| **Tauri** (lighter desktop app) | Smaller than Electron, native feel | Still platform-specific builds, still two deployment modes | **Not worth it** unless friends need offline solo play |
| **Static site + serverless** | No server to maintain, CDN-distributed | Cannot run Colyseus (needs persistent WebSocket server), would require architecture change | **Incompatible with current architecture** |
| **Progressive Web App (PWA)** | "Add to home screen" on phones, app-like feel | Minimal extra effort on top of web app | **Good enhancement** for the phone controller |

### Recommendation

- **Ship as a hosted web app with Docker Compose deployment.** This is the only answer that serves both stakeholder realities: Logan can deploy it, friends can use it with zero friction.
- **Add PWA manifest to the phone controller surface** so friends can "install" it to their home screen for faster access on subsequent game nights.
- **Do not build desktop apps.** The problem is not "friends need an app" -- it is "friends need a URL."

---

## Recommended Distribution Strategy

### Phase map

| Phase | Distribution milestone | Mechanism |
|-------|----------------------|-----------|
| During development | Logan tests locally | `pnpm dev` (existing workflow) |
| First playtest (local) | Logan hosts on laptop, friends join on WiFi | Laptop runs server, QR code on screen, friends scan |
| Repeat local play | Same but smoother | `docker compose up` on laptop or dionysus via HDMI |
| First remote play | Friends on Tailscale | dionysus runs server, Tailscale connects friends |
| Frictionless remote play | Friends open a URL | Cloudflare Tunnel + domain, dionysus runs server |
| Game night ritual | One-tap start | `prix-start` script or phone shortcut |

### What this means for the roadmap

The current roadmap has no phase, requirement, or success criterion for:

1. **How the game is deployed** (Docker, systemd, scripts)
2. **How friends discover the server address** (QR code, URL, auto-detection)
3. **How remote friends connect** (Tailscale, domain, tunnel)
4. **How Logan starts and stops the server** (scripts, shortcuts)
5. **Whether the game works without internet** (Supabase dependency)
6. **PWA support for phone controllers** (add-to-home-screen)

These are not polish items. Points 1-3 are prerequisites for the first real playtest. If Phase 5 delivers a "watchable host screen" but there is no way for friends to actually reach the server from their phones, the playtest cannot happen.

---

## Architecture Implications

### Changes needed in current plans

| Current assumption | Problem | Recommended change |
|-------------------|---------|-------------------|
| Supabase for persistence and storage | External dependency breaks offline/local play, adds latency, unnecessary for private game | Use local PostgreSQL (in Docker) for v1. Supabase optional for future cloud features. |
| No deployment specification | Game cannot be playtested without manual developer setup | Add Docker Compose config as a Phase 3 or Phase 4 deliverable |
| No server URL configuration | Client cannot find the server in different network configurations | Build-time or runtime server URL configuration in the web client |
| No QR code join flow | The simplest phone join mechanism is unspecified | Add QR code generation to host screen as part of Phase 4 (ROOM-02) |
| PostgreSQL as hard requirement | Heavy for a game with ~100 rounds and 5 players | Consider SQLite for v1 content storage (packs are read-only at runtime), PostgreSQL for session data only if needed |

### What should NOT change

- **Colyseus as room authority** -- correct for the host+controller model
- **React + Vite for frontend** -- produces static assets, framework-agnostic at deployment time
- **TypeScript monorepo** -- good for development, invisible to end users
- **Authored content model** -- the right product decision regardless of distribution

---

## Specific Requirement and Roadmap Changes

### New requirements to add

| ID | Requirement | Priority | Phase |
|----|------------|----------|-------|
| **DIST-01** | Game server and all dependencies can be started with a single command on dionysus | Critical | Phase 3 or 4 |
| **DIST-02** | Host screen displays a scannable QR code and join URL for the current room | Critical | Phase 4 |
| **DIST-03** | Game functions on a local network without requiring external internet services for core gameplay | High | Phase 3 |
| **DIST-04** | Remote friends can connect via Tailscale without additional per-session setup | High | Phase 5 or 6 |
| **DIST-05** | Phone controller supports "add to home screen" (PWA) for repeat game nights | Medium | Phase 5 |
| **DIST-06** | Remote friends can connect via a public URL without installing Tailscale (Cloudflare Tunnel or equivalent) | Medium | Phase 7 or v2 |

### Roadmap changes

**Option A (Minimal disruption):** Add distribution deliverables to existing phases.

- **Phase 3 (Session Snapshots and Room Authority):** Add success criterion: "The server (room + web) can be started with a single command via Docker Compose."
- **Phase 4 (Guest Join):** Add success criterion: "Host screen displays a QR code encoding the join URL. A phone on the same network can scan it and join within 30 seconds."
- **Phase 5 (Host Screen):** Add success criterion: "Host display is readable at 3+ meters distance on a TV screen."

**Option B (New phase):** Insert a deployment and distribution phase (e.g., Phase 3.5 or fold into Phase 3) that specifically addresses Docker packaging, server URL configuration, and local network discovery.

**Recommendation:** Option A. Distribution should be woven into existing phases rather than treated as a separate concern. The game is not shippable without these, so they belong in the phases that build the features they enable.

### Supabase reconsideration

The STACK.md recommendation of Supabase should be revisited. For a private game:

- **Content storage (packs, rounds):** Compiled YAML/JSON files served from the filesystem or embedded in the Docker image. No database needed for read-only content at runtime.
- **Session state:** Colyseus room state (in-memory). No database needed during play.
- **Session history / analytics:** SQLite file or PostgreSQL in Docker. No external service needed.
- **Media assets:** Local filesystem in the Docker image or a volume mount. No CDN needed for 5-10 players.

Supabase solves problems this project does not have in v1. Its value emerges only if the project later needs: cloud-hosted database, CDN for many concurrent users, authentication beyond room codes, or a public-facing admin interface.

---

## Priority Summary

| Priority | Finding | Action |
|----------|---------|--------|
| **Critical** | No deployment mechanism exists or is planned | Add Docker Compose to Phase 3 deliverables |
| **Critical** | No way for phones to discover the server | Add QR code join URL to Phase 4 deliverables |
| **Critical** | Friends cannot self-host; Logan must host | Acknowledge this in PROJECT.md and plan accordingly |
| **High** | Supabase dependency breaks offline/local play | Replace with local PostgreSQL or SQLite for v1 |
| **High** | Host screen not specified for TV-distance viewing | Add TV readability constraint to Phase 5 / UX-01 |
| **High** | No remote play path specified | Document Tailscale as Phase 1 remote path, Cloudflare Tunnel as later upgrade |
| **Medium** | No start/stop automation for dionysus | Add `prix-start`/`prix-stop` scripts as Phase 6 deliverable |
| **Medium** | No PWA support for phone controller | Add to Phase 5 as UX enhancement |
| **Low** | No public domain for frictionless remote play | Plan for Cloudflare Tunnel + domain in v2 or late v1 |
| **Low** | No auto-shutdown for idle server | Add as operational convenience after core game works |

---

## Concrete Deployment Architecture

### Local play (v1 target)

```
Logan's laptop (or dionysus via HDMI)
  |
  +-- Docker Compose
  |     +-- prix-web (Vite build served by nginx or Node static server, port 3000)
  |     +-- prix-rooms (Colyseus server, port 2567)
  |     +-- prix-db (PostgreSQL or SQLite volume, if needed)
  |
  +-- Browser: http://localhost:3000/host  (full-screen on TV via HDMI)
  |
  +-- QR code on screen: http://192.168.x.x:3000/join/ROOM-CODE
  |
Friends' phones (same WiFi)
  +-- Scan QR -> phone browser -> controller UI
```

### Remote play via Tailscale

```
dionysus (100.93.212.44)
  |
  +-- Docker Compose (same as above)
  |
  +-- Browser: http://100.93.212.44:3000/host or http://dionysus:3000/host
  |
Friends' phones/laptops (Tailscale installed)
  +-- http://100.93.212.44:3000/join/ROOM-CODE
```

### Remote play via Cloudflare Tunnel (future)

```
dionysus
  |
  +-- Docker Compose (same as above)
  +-- cloudflared tunnel (prix.loganrooks.com -> localhost:3000)
  |
  +-- Browser: https://prix.loganrooks.com/host
  |
Friends' phones/laptops (no special software)
  +-- https://prix.loganrooks.com/join/ROOM-CODE
```

Note: In all three scenarios, the application code is identical. Only the URL and network path change.

---

## Summary

The project's game architecture is thoughtful and well-researched. The gap is that the planning documents describe how to build the game engine but not how the game reaches real players in a living room. For a project whose entire value proposition is social play among non-technical friends, distribution is not a phase 7 concern -- it is a phase 3-4 concern that determines whether the first playtest can happen at all.

The good news: the server-authoritative Colyseus architecture naturally supports the local-to-remote transition. The web-based approach means no app installs for friends. The changes needed are primarily about packaging (Docker), discovery (QR codes), and reducing external dependencies (Supabase) -- not about rethinking the game architecture itself.

The single most important shift: **stop thinking of this as a developer project that happens to be private, and start thinking of it as a hosted game that happens to be built by a developer.** The build toolchain is for Logan. The deployment target is for everyone.

---
*Audit completed: 2026-04-08*
*Auditor: Lane 3 — Product & Distribution Reality Check*
