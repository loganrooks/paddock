# Lane 3: Stakeholder & Distribution Reality Check

## Executive Read

The project is currently strong on game/content architecture and weak on distribution architecture.

That is a real risk because the stakeholder test here is not "can a developer run the repo?" It is "can Logan or a non-technical F1 friend reliably get a room onto a TV and phones with low ceremony?"

My main conclusion:

- `React + Vite + TypeScript + shared packages` is a good builder-facing substrate.
- A browser-first product surface is the right end-user surface.
- The roadmap does not yet say enough about how hosting actually works in local LAN play or in future `dionysus` hosting.
- `Tailscale-only` is acceptable for operator/admin access, not as the primary guest access model.
- If "friends can host on their own laptop" is a real goal, the source-repo path is not realistic. That requires either a one-click packaged local host app or a hosted web deployment.

## Reality Check By Scenario

| Scenario | Reality check | Implication |
|---|---|---|
| Non-technical friend hosts from this repo on their laptop | No, not realistically. `git clone` + Node + `corepack pnpm` + env vars + room server setup is too much. | Do not treat source checkout as a stakeholder-valid host path. |
| Non-technical friend hosts from a packaged local app | Yes, but only if the app bundles runtime, content, local server, QR generation, and gives clear firewall guidance. | This is a separate packaging/distribution problem, not just "ship the web app." |
| Friends join from phones on same WiFi | Yes. This is the best v1 path. | QR + short room code should be the default join UX. |
| Local network discovery | Nice-to-have, not required. Cross-device discovery is flaky and network-dependent. | Do not spend early effort on mDNS/Bonjour discovery. |
| Cast to TV | Yes, but "cast" should usually mean HDMI or OS-level mirror/extended display from the host laptop. | The app needs a strong fullscreen host route, not Chromecast SDK work. |
| Same-WiFi local mode -> future online mode | Good fit if the architecture stays browser-first and room-authoritative. | Keep one room model and two deployment topologies. |
| `Tailscale-only` remote hosting | Works technically, poor guest UX. Every friend would need Tailscale install/access. | Fine for Logan/admin/dev; bad as the primary distribution path. |
| Remote hosting without Tailscale | Very feasible. Needs stable HTTPS + websocket-capable ingress. | Domain + reverse proxy or Cloudflare Tunnel is the right shape. |
| "Hosted only when we want to play" | Very feasible. | Use scripted app start/stop on `dionysus`, not permanent full-time app ops. |
| Monorepo + `pnpm` + TypeScript | Good for Logan, invisible to end users if kept behind build artifacts. | Helpful internally, harmful only if mistaken for end-user distribution. |
| Electron / Tauri / Docker / hosted web app | Hosted web app is the best default. Docker is operator-only. Electron is the most plausible local-host wrapper if packaging becomes necessary. Tauri is less natural if the runtime stays Node/Colyseus. | Do not overinvest in desktop packaging before proving that multiple people actually need to host locally. |

## Distribution Strategy

### Recommended phase order

1. **Primary v1 distribution: browser-first local LAN play**
   - Host runs one browser-accessible local server on their laptop.
   - Host screen goes to TV via HDMI or OS-level casting.
   - Friends join from phones by scanning a QR code shown on the host screen.
   - Same WiFi is the default assumption.

2. **Primary v1.5/v2 distribution: hosted on `dionysus`**
   - Same web app and same room contracts.
   - Public join URL over HTTPS.
   - Logan starts the app only when the group wants to play.

3. **Optional later distribution: packaged local-host desktop app**
   - Only do this if "friends hosting on their own laptops" becomes a repeated real need.
   - This should wrap the browser-first system, not replace it.

### What should not be the primary strategy

- Do not make every friend install Tailscale.
- Do not make Docker the end-user story.
- Do not make source checkout the host story.
- Do not build Chromecast-specific features before proving that HDMI/mirroring is insufficient.

## Simplest Join Path For Phones

The simplest robust v1 join flow is:

1. Host creates room.
2. Host screen shows:
   - QR code with full join URL
   - short room code as manual fallback
   - short text fallback like `192.168.1.23:3000`
3. Guest scans QR and lands directly in room join flow.
4. Guest enters nickname and is in.

This is better than local network discovery because:

- it works on iPhone and Android without extra app installs
- it does not depend on multicast or Bonjour working correctly
- it still works when the room is remote later
- it matches the eventual hosted flow cleanly

Recommendation:

- Treat QR as required for v1, not optional polish.
- Treat room code as mandatory fallback.
- Treat network discovery as low priority.

## TV Casting Reality Check

Technically, "cast to TV" should mean:

- host laptop is the real host device
- TV is just the display target
- phones are controllers

That means the app needs:

- a fullscreen host display route
- safe 16:9 layout at 1080p from a couch distance
- visible room code and QR from several feet away
- no critical UI hidden behind mouse hover or small desktop affordances

What it probably does **not** need in v1:

- Chromecast receiver support
- Cast SDK integration
- special cast-aware state handling

Recommendation:

- Optimize first for HDMI and OS/browser mirroring.
- Add Chromecast-specific work only if real playtests show HDMI/mirroring is not enough.

## Architecture Implications

### 1. The room runtime should stay self-hostable

The stakeholder/distribution story pushes the project toward a conventional self-hostable runtime.

That means the open `Colyseus` vs `PartyKit` decision is not neutral from a distribution standpoint:

- `Colyseus` fits better if the same code should run on a laptop, in Docker, and on `dionysus`.
- `PartyKit` is still viable, but it is less aligned with the explicit "local host on laptop" plus "home server later" posture.

My bias from this lane:

- if the distribution goal is real, prefer `Colyseus` or another plain Node-hostable room runtime
- only choose `PartyKit` if Logan consciously decides that fastest prototype speed matters more than local/self-host parity

### 2. Local play should not require heavy infrastructure

If local host mode requires PostgreSQL, Redis, Supabase, or multiple operator steps, the stakeholder fit collapses.

For local LAN play, the cleanest shape is:

- compiled packs shipped with the app or repo build
- room state in memory
- optional local persistence only if needed later
- no hard dependency on external auth

This is compatible with the current roadmap and should stay that way.

### 3. Remote hosting should be a topology change, not a product rewrite

The web clients, room contracts, and join flow should be the same in both modes:

- **local mode:** `http://<lan-ip>:<port>/join/<room>`
- **remote mode:** `https://prix.<domain>/join/<room>`

That means the app should explicitly own:

- base URL generation
- room code + QR generation
- websocket origin configuration
- environment-based deployment mode

### 4. Do not make secure-context-only browser APIs mandatory in LAN mode

Local LAN mode will likely be plain HTTP on a private address.

That is acceptable for v1 if the app avoids making critical features depend on HTTPS-only browser APIs. The core loop should not require PWA install, service worker behavior, or other secure-context-only features just to play on the same network.

### 5. Media strategy matters for hostability

If critical clues depend on live third-party media every round, "local host on a laptop" still depends on reliable internet.

The authored fallback/media strategy already exists in the roadmap. Distribution-wise, that is good. Lean into it:

- bundle what can be bundled
- keep Street View optional
- do not make local party play brittle because a remote clue provider is slow or unavailable

## Concrete Deployment Architecture

### Local play architecture

**Best v1 shape**

- One host laptop runs:
  - static web bundle
  - room server
  - compiled pack assets
- Host opens `/host`
- TV displays laptop screen via HDMI or system mirroring
- Guests join `/join/<room>` from phones over same WiFi
- Session state is authoritative on the laptop
- Session persistence can be in memory for v1

**Operational notes**

- QR should encode the actual LAN join URL
- app should detect likely private IPv4 addresses and allow host override
- if home WiFi is awkward, a host-created hotspot is a valid fallback
- first-run firewall prompts are part of the real UX if local hosting is a goal

### Future online architecture on `dionysus`

**Recommended shape**

- `web` container or service for static app assets
- `room-server` container or service for authoritative room runtime
- `caddy` or `cloudflared` ingress layer with websocket support
- optional `postgres` and `redis` backing services if/when needed
- host/admin access to the box via Tailscale/SSH
- guest access over normal HTTPS, not Tailscale

**Recommended guest URL**

- `https://prix.<your-domain>/join/<room>`

**Best ingress options**

1. **Domain + Cloudflare Tunnel**
   - best fit for a private hobby project on a home server
   - avoids router port forwarding
   - stable HTTPS URL for guests
2. **Domain + Caddy/Nginx + router port forwarding**
   - also valid
   - simpler dependency chain once networking is configured
3. **Temporary tunnels**
   - fine for testing
   - poor recurring UX because URLs change

### "Hosted only when we want to play" model

This should mean:

- a stable scriptable deployment
- app services started on demand
- guests join a stable HTTPS URL when the app is up

Recommended operator flow:

1. Logan connects to `dionysus` over Tailscale/SSH.
2. Runs `scripts/party-up.sh` or `docker compose up -d`.
3. Script prints the live public URL.
4. Game night happens.
5. Logan runs `scripts/party-down.sh` or `docker compose down`.

If the project uses Cloudflare Tunnel or a reverse proxy continuously, the ingress can stay up while app services start and stop. That is a good fit for "only when we want to play."

## What Needs To Change In Requirements Or Roadmap

The current artifacts cover room logic and join mechanics, but they under-specify deployment and hostability.

### Requirements to add

- **DEPLOY-01**: Host can start a playable local-LAN session from one guided flow without requiring guests to install anything beyond a browser.
- **DEPLOY-02**: System can generate and display a valid join URL and QR code for the current deployment mode (`local` or `hosted`).
- **DEPLOY-03**: Host display is usable on a 16:9 TV at couch distance and supports fullscreen presentation without cast-specific integrations.
- **DEPLOY-04**: Hosted mode supports HTTPS and websocket-capable ingress for remote guest play without requiring Tailscale on guest devices.
- **DEPLOY-05**: Operator can start and stop the hosted deployment on demand with a single documented command or script.

### Roadmap changes to make

- **Phase 3** should explicitly decide the deployment topology assumptions alongside room authority.
  - Right now it decides room runtime posture, but not enough about how rooms are actually exposed to phones.
- **Insert a phase or explicit plan between Phase 3 and Phase 4** for distribution shell and join topology.
  - This can be a small phase focused on local host startup, environment config, join URL generation, and remote ingress assumptions.
- **Phase 4** should include real-phone validation on same-WiFi join, QR scanning, and nickname entry.
- **Phase 5** should include TV/fullscreen acceptance criteria, not only "watchable shared-screen format."
- **Phase 7** should include sleep/wake on real phones in both local and hosted topologies, because reconnection pain shows up differently in LAN and internet contexts.

## Packaging Recommendation

| Option | Fit | Recommendation |
|---|---|---|
| Hosted web app | Best overall fit | Make this the primary product surface. |
| Docker | Good operator fit, poor friend fit | Use for Logan/devops, not for end users. |
| Electron | Plausible if local-host packaging becomes necessary | Better fit than Tauri if the runtime stays Node/Colyseus. |
| Tauri | Possible, but less natural with Node room runtime | Do later only if desktop packaging becomes a real need and runtime strategy changes. |

## Priority Recommendations

### Critical

- Do not treat source checkout + `pnpm` as a real hosting story for non-technical friends.
- Add explicit deployment/distribution requirements now; the current roadmap underspecifies them.
- Make QR-based join a first-class requirement, not just a Phase 4 hint.
- Do not require Tailscale for guests.

### High

- Prefer a self-hostable room runtime path if local-host-on-laptop and `dionysus` are both real goals.
- Define a concrete local-LAN topology before building join/controller UI.
- Add TV/fullscreen acceptance criteria for the host screen.
- Plan an on-demand hosted deployment script early.

### Medium

- Keep local mode light enough to run without external database dependencies.
- Treat host-created hotspot as a fallback play pattern worth supporting.
- Keep third-party clue/media dependencies optional enough that local play is not brittle.

### Low

- Local network auto-discovery.
- Chromecast-specific integration.
- Desktop packaging before repeated evidence that multiple people need to host locally.

## Bottom Line

The current architecture direction is mostly compatible with the stakeholder context, but only if the project gets much more explicit about distribution.

The winning posture is:

- browser-first for players
- QR-first for join
- HDMI/mirroring-first for TV
- self-hostable room runtime
- local LAN first
- public HTTPS on `dionysus` later
- Tailscale for operator access, not guest access

If the roadmap absorbs that now, the project can grow from couch play to remote play without a major architectural reset.
