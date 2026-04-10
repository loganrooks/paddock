# Prix Guesser Stakeholder / Distribution Audit

## Executive verdict

Prix Guesser should not optimize for “any friend can self-host the software stack from source.” The stakeholder-fit path is simpler:

- a non-technical friend can host the **session** on a laptop and TV
- Logan hosts the **software** either on the laptop over LAN for v1, or on `dionysus` behind a private HTTPS URL later

That is the key distinction. For this project, friend usability comes from **URL + QR + phone browser**, not from asking friends to touch `pnpm`, Docker, Tailscale, or environment setup.

A second reality check: the repository is still planning-stage, not a runnable app. The current docs are strong on content modeling and room authority, but weak on explicit deployment and distribution requirements.

## Reality check on each distribution scenario

| Scenario | Reality check | Stakeholder fit |
|---|---|---|
| Raw repo on a friend’s laptop | Not realistic. It would require Node, `pnpm`, env setup, network binding, and firewall handling. | Poor |
| Browser app hosted on the host laptop over same Wi‑Fi | Best v1 shape. Phones join by QR to a LAN URL. Main risks are Windows/macOS firewall prompts and guest-network client isolation. | Strong |
| Cast to TV by HDMI | Best option. No app-level cast integration needed. Just open the host display route and mirror by cable. | Strongest |
| Cast to TV by Chromecast / Chrome tab cast / AirPlay | Works, but it is a display transport choice, not an app architecture choice. Chrome’s help docs say the laptop and cast device must be on the same Wi‑Fi network. Expect more latency and more setup variance than HDMI. | Good secondary path |
| `dionysus` over Tailscale only | Works technically, but poor for non-technical friends. Tailscale’s invite flow requires sign-in and downloading the Tailscale client. That is too much friction for “show up and play on your phone.” | Weak for players |
| `dionysus` over public HTTPS with a private gate | Best future general path. Friends open one normal URL in mobile Safari/Chrome. You keep it private with an allowlist or identity gate. | Strong |
| Tailscale Funnel | Useful as a fast temporary bridge, but Tailscale’s docs still mark Funnel as beta as of January 20, 2026. I would not make it the main friend-facing strategy. | Temporary only |
| Cloudflare Quick Tunnel | Good for remote playtests or one-off sharing. Too ephemeral for a recurring friend game night flow. | Temporary only |
| Docker Compose | Good for Logan and `dionysus`. Not a friend-facing packaging story. | Ops only |
| Electron / Tauri desktop host app | Only worth it if “offline or portable local hosting on arbitrary laptops” becomes a real product requirement. | Later, not now |

## Recommended distribution strategy

### Phase 1: LAN-first local party mode

Ship the first playable version as a browser game that runs on one laptop on the local network.

- Host opens the display on the laptop and plugs into the TV with HDMI.
- Players scan a QR code and join from phones on the same network.
- No player account.
- No Tailscale.
- No install on phones.

This matches the stated v1 fantasy exactly.

### Phase 2: Private hosted mode on `dionysus`

When you want friends to be able to play from anywhere, or to let a non-technical friend “host” by just opening a browser on a laptop, move the same app to `dionysus`.

- Put it behind a real domain and HTTPS.
- Keep it private with Cloudflare Access or an equivalent allowlist gate.
- Let players join with a normal URL from phones.
- Keep Tailscale for Logan’s admin access, not player access.

This is the best answer to “hosted only when we want to play.”

### Phase 3: Optional desktop packaging

Only add a packaged host app if one of these becomes true:

- you want offline or flaky-internet party sessions
- you want arbitrary friends to run local host mode without Logan
- firewall / LAN setup becomes the main support pain

If that happens, Electron is the more pragmatic fit than Tauri for Logan, because it stays in the same JS/TS ecosystem. Tauri adds Rust and signing/toolchain complexity that this project does not currently need.

## Architecture implications for the current roadmap

The current roadmap is mostly right about content, rules, and room authority. What is missing is explicit deployment shape.

The architecture should lock in these realities:

- The game should remain a **single browser-first web app** with separate host-display and controller surfaces.
- The room server should be **deployment-agnostic**. Local LAN and `dionysus` should be the same app with different base URLs and exposure layers.
- Room creation must generate the **correct join URL and QR code** for the active deployment profile: `lan` or `private-online`.
- The app should prefer **one origin** for web UI and room connectivity, or at least hide multiple services behind one public origin. This avoids mobile cross-origin confusion and makes QR joining simple.
- Tailscale should be treated as an **admin plane**, not as the normal player access path.
- The current stack research is slightly too cloud-default. If `dionysus` is the real future host, do not hardwire Supabase into the architecture. Keep Postgres, storage, and media handling self-host-friendly.

A stakeholder-specific note: `dionysus` is not underpowered for this. For a private browser game with a few friends, the Xeon / 32 GB / Docker / Postgres / Redis environment is ample. Compute is not the bottleneck. Distribution and session launch simplicity are.

## What needs to change in requirements or roadmap

### Requirements to add

Add a deployment/usability requirement set. The current requirements cover join flow and room flow, but not hostability reality.

Recommended additions:

- `DIST-01`: Host can launch a LAN-playable session without developer setup or terminal knowledge.
- `DIST-02`: Room creation produces a QR code and join URL appropriate to the current deployment profile.
- `DIST-03`: The same game supports `lan` and `private-online` deployment profiles without code forks.
- `DIST-04`: Private online access can be restricted without requiring full in-app accounts.
- `OPS-04`: A session can be started and stopped on `dionysus` with one scripted command path.

### Roadmap changes

Insert an explicit deployment/distribution phase before or alongside guest join work.

Best option: insert **Phase 3.1: Deployment Profiles And Join Routing** between current Phases 3 and 4.

Suggested success criteria:

1. The app runs in `lan` mode and `private-online` mode from the same codebase.
2. Room creation generates the correct join URL and QR code for each mode.
3. `dionysus` can start and stop a playable session with one script.
4. Private online mode is gated by simple access control without requiring app accounts.

Also revise the current stack direction so that:

- Supabase is **optional**, not assumed.
- Redis is **optional** until proven necessary.
- Desktop packaging is **not** a v1 requirement.
- HDMI-first host display is an explicit assumption for the first local-play milestone.

## Concrete deployment architecture

### Local play architecture

Recommended v1 local shape:

- Host laptop runs the web app and room server locally.
- The app binds to `0.0.0.0` on the LAN.
- Host opens `/display/:room` on the laptop and connects to the TV by HDMI.
- The room creation screen shows a QR for `http://<lan-ip>:<port>/join/:room`.
- Phones connect to that LAN URL and use WebSocket/HTTP back to the laptop.
- Packs and key media should be bundled or cached enough that a weak internet connection does not kill the session.

Operational realities:

- Same Wi‑Fi is required.
- Guest Wi‑Fi with client isolation can break phone-to-laptop connectivity.
- A personal hotspot fallback is useful.
- If the app depends on live Google-hosted media, “LAN play” still depends on internet quality.

### Future online architecture

Recommended private-online shape on `dionysus`:

- Docker Compose stack with:
  - `web`
  - `room-server`
  - `postgres`
  - optional `redis`
  - object storage or file-backed media
  - `cloudflared` or a reverse proxy such as Caddy
- Public hostname such as `play.<your-domain>`
- HTTPS at the edge
- Access gate via Cloudflare Access or equivalent email allowlist / OTP / Google login
- Tailscale retained for Logan’s SSH/admin/db access only

That gives friends a normal browser flow while keeping the project private.

### “Hosted only when we want to play” model

The clean version is:

- persistent volumes keep packs, media metadata, and session history
- one script starts the playable surface
- one script stops it afterward

Concretely, that means something like:

- `session up`: start `web`, `room-server`, and exposure layer; print URL and QR
- `session down`: stop the public services
- optional: leave Postgres running if you want simpler warm starts

This is a much better fit than “the server is always publicly live” and much better than “everyone installs Tailscale.”

## Packaging options

| Option | Verdict |
|---|---|
| Hosted web app | Best overall distribution model |
| Docker | Best ops packaging for Logan / `dionysus`, not for friends |
| Electron | Best fallback if local desktop hosting becomes required later |
| Tauri | Not recommended now; extra toolchain complexity for little stakeholder value |
| Plain source repo | Developer workflow only, never the user workflow |

## Priority recommendations

### Critical

- Do not make players install Tailscale, Docker, or the repo.
- Treat **QR code + browser URL** as the default player join path.
- Add explicit deployment/distribution requirements to the roadmap now.
- Keep the same app usable in both `lan` and `private-online` modes.
- Treat HDMI as the default TV path. Do not build cast-aware app logic for v1.

### High

- Add a one-command session launch path for local play and `dionysus`.
- Add QR generation and deployment-aware join URLs to room creation.
- Keep Tailscale for admin access, not player access.
- Use a private HTTPS host with Cloudflare Tunnel + Access or equivalent for future online mode.
- Keep storage and media hosting self-host-friendly instead of assuming Supabase.

### Medium

- Keep the monorepo, `pnpm`, and TypeScript, but keep the workspace small.
- Avoid over-slicing into too many packages. `apps/web`, `apps/room-server`, and `packages/domain` are enough.
- Defer Redis until you prove you need it for room scaling or queueing.
- Plan for network failure modes early: LAN firewall prompts, guest Wi‑Fi isolation, phone sleep/reconnect.

### Low

- If desktop packaging becomes necessary later, prefer Electron over Tauri for this project.
- The GPU on `dionysus` is irrelevant to the current product shape.
- Quick Tunnel / Funnel are useful for ad hoc testing, not as the canonical friend-facing launch path.

## Sources

- [README.md](/home/rookslog/workspace/projects/prix-guesser/README.md)
- [PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md)
- [REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md)
- [ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md)
- [STACK.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/STACK.md)
- [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/ARCHITECTURE.md)
- [discovery/09-feasibility.md](/home/rookslog/workspace/projects/prix-guesser/discovery/09-feasibility.md)
- [discovery/12-framework-decision-context.md](/home/rookslog/workspace/projects/prix-guesser/discovery/12-framework-decision-context.md)
- [discovery/13-room-backend-decision-context.md](/home/rookslog/workspace/projects/prix-guesser/discovery/13-room-backend-decision-context.md)
- https://tailscale.com/docs/features/tailscale-serve
- https://tailscale.com/docs/features/tailscale-funnel
- https://tailscale.com/docs/features/sharing/how-to/invite-any-user
- https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/
- https://developers.cloudflare.com/cloudflare-one/access-controls/policies/
- https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/
- https://try.cloudflare.com/
- https://support.google.com/chrome/answer/3228332