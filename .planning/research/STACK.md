# Technology Stack

**Project:** Prix Guesser  
**Dimension:** Stack  
**Researched:** 2026-04-08  
**Overall confidence:** MEDIUM-HIGH

## Executive Recommendation

Use a **split web-game stack**, not a monolithic app-framework-by-default stack:

- **Frontend:** `React 19.2.5` + `Vite 8.0.7` + `TypeScript 6.0.2`
- **Realtime rooms:** `Colyseus 0.17.8` for the serious host-screen + phone-controller path
- **Persistence and assets:** `PostgreSQL 18` + `Drizzle ORM 0.45.2` + `Supabase` (`@supabase/supabase-js 2.102.1`, Storage, optional Auth later)
- **Maps/media:** `MapLibre GL JS 5.22.0` for answer/reveal maps, with **Google Maps JavaScript API Street View** as a clue provider where coverage is good
- **Client state / validation:** `Zod 4.3.6`, `TanStack Query 5.96.2`, `Zustand 5.0.12`
- **Testing:** `Vitest 4.1.3` + `Playwright 1.59.1`

This is the strongest default because the product’s real complexity is not SSR or marketing pages. It is:

- authored round data and reveal logic
- synchronized room/timer state
- multi-surface UX across host display and phone controllers
- map/media abstraction that can survive uneven Street View coverage

The main unresolved decision is still **how durable and authoritative the first room experience must be**. If v0 is explicitly a fast private prototype, `PartyKit 0.0.115` is the speed-first alternative. If live rooms are core from the start, prefer `Colyseus`.

## Recommended Default Stack

| Layer | Technology | Confidence | Why it fits this product | Main caveat |
|------|------|------|------|------|
| Runtime | `Node.js 24` Active LTS | HIGH | Stable production target with current LTS support; good fit for Vite, React, Colyseus, and tooling. | None beyond normal Node upgrade discipline. |
| Workspace | `pnpm` workspaces | MEDIUM | Prix Guesser wants shared packages for round schemas, scoring rules, room messages, and admin tooling. A workspace keeps those explicit. | Not a product decision, just repo hygiene. |
| Frontend UI | `React 19.2.5` | HIGH | Strongest ecosystem leverage, easiest reuse from the React-based GeoGuessr-like references already studied, and best AI editability in 2026. | React alone does not solve architecture; state discipline still matters. |
| Frontend build shell | `Vite 8.0.7` | HIGH | Keeps the client-heavy game simple, fast, and framework-light. Better default than adopting a full server-first app shell before it is justified. | You must choose your own routing and server boundaries instead of inheriting them from Next. |
| Types | `TypeScript 6.0.2` | HIGH | Shared types across room server, client, pack importer, and authored round schema are high leverage here. | Requires discipline to keep runtime validation aligned. |
| Domain validation | `Zod 4.3.6` | HIGH | Best fit for explicit authored round schemas, importer validation, room message parsing, and pack linting. | Keep schemas centralized; duplicated schemas will drift. |
| Server data fetching | `TanStack Query 5.96.2` | HIGH | Good for packs, profiles, authoring/admin screens, and non-live API data. | Do not use it as your live room state engine. |
| Local client state | `Zustand 5.0.12` | MEDIUM-HIGH | Small, explicit, good for UI-local state like controller inputs, reveal panels, settings, and transient lobby UX. | Keep authoritative game state out of Zustand. |
| Realtime room engine | `Colyseus 0.17.8` | HIGH | Best fit when timer correctness, reconnects, room lifecycle, and authoritative server state matter early. Its room/state model maps cleanly onto host-screen plus phone-controller play. | More upfront structure than PartyKit. |
| Database | `PostgreSQL 18` | HIGH | Strong relational fit for authored rounds, packs, media references, reveals, rooms, and analytics. Postgres is the right substrate for content-rich game data. | Requires schema design up front. |
| ORM / SQL layer | `Drizzle ORM 0.45.2` | MEDIUM-HIGH | Stronger here than Prisma because it keeps SQL and migrations explicit, which matters for authored content, pack imports, and AI-assisted maintenance. | Slightly less batteries-included than Prisma. |
| Managed platform | `Supabase` | MEDIUM-HIGH | Good default for hosted Postgres, file storage, dashboard/admin convenience, and optional auth later. Useful app plumbing without pretending to be the room authority. | Do not confuse Supabase Realtime with a solved game-loop authority model. |
| Asset storage | `Supabase Storage` | HIGH | Fits curated media packs, image crops, reference assets, and reveal images with CDN delivery and access control. | If you later move to a Cloudflare-heavy stack, storage location may be revisited. |
| Answer / reveal map | `MapLibre GL JS 5.22.0` | HIGH | Strong default for interactive answer placement and cinematic reveal maps without locking the whole product to Google Maps pricing and styling constraints. | Requires choosing a tile provider separately. |
| Street View clue provider | `Google Maps JavaScript API` / Street View | MEDIUM | Best supported browser Street View integration. Needed if the game really wants pano-style clues where coverage exists. | Coverage, cost, and product dependency should remain explicit; not every circuit should depend on it. |
| Styling layer | `Tailwind CSS 4.2.2` | MEDIUM | Pragmatic default for rapidly shipping distinct host and controller surfaces without committing to a component framework too early. | Not strategic; can be swapped if a stronger design system emerges. |
| Testing | `Vitest 4.1.3` + `Playwright 1.59.1` | HIGH | Good split between fast domain/unit tests and multi-client browser flows for rooms, reconnects, timers, and reveals. | E2E setup will require deliberate multi-client fixtures. |

## Best Full-Stack Shapes

### 1. Recommended Foundation-First Stack

**Use this unless you are intentionally optimizing only for the fastest possible room prototype.**

- `React 19.2.5`
- `Vite 8.0.7`
- `TypeScript 6.0.2`
- `Colyseus 0.17.8`
- `PostgreSQL 18`
- `Drizzle ORM 0.45.2`
- `Supabase` for hosted Postgres + Storage
- `MapLibre GL JS 5.22.0`
- `Google Maps JavaScript API` only for Street View clue types

Why this is strongest here:

- Keeps the **authoritative room model** separate from app plumbing.
- Supports **host screen + phone controllers** cleanly.
- Gives the authored round model a proper relational home instead of flattening it into document blobs.
- Preserves room to expand into adjacent party modes without forcing a rewrite into turn-engine abstractions.
- Matches the existing discovery conclusion that **room authority model** and **authored round model** matter more than a fashionable frontend shell.

### 2. Fastest Private-Prototype Stack

**Use this only if proving room energy fast matters more than durability.**

- `React 19.2.5`
- `Vite 8.0.7`
- `TypeScript 6.0.2`
- `PartyKit 0.0.115`
- `PostgreSQL 18` via Supabase
- `MapLibre GL JS 5.22.0`
- `Google Maps JavaScript API` for Street View clues

Why it is strong:

- Very fast route to private rooms and browser multiplayer.
- Good fit for host orchestration with multiple controller clients.
- Lower ceremony than Colyseus.

Why it is weaker than the default:

- `partykit` is still on a `0.x` package line as of 2026-04-08.
- Recovery and persistence require more house discipline.
- Easier to ship quickly than to keep clean once room logic becomes richer.

**Recommendation:** keep PartyKit as the explicit speed-first fallback, not the default recommendation.

### 3. Lean Alternative If You Intentionally Reject React

**Viable, but not the best inheritance path here.**

- `Svelte 5.55.2`
- `SvelteKit 2.57.0`
- `TypeScript 6.0.2`
- `Colyseus` or `PartyKit`
- `PostgreSQL 18`
- `Drizzle ORM`
- `MapLibre GL JS`

Why it is credible:

- Lean mental model.
- Good fit for animated, media-heavy UI.
- Smaller component surface can be attractive for a curated game.

Why it is not the default:

- Less direct reuse from React-based OSS references already researched.
- Smaller ecosystem around this exact geography/realtime/game shape.
- Lower agent familiarity than React in practice.

**Recommendation:** only choose this if the team consciously values Svelte’s mental model over React ecosystem inheritance.

## Alternatives Considered

| Category | Recommended | Alternative | Why not default here |
|------|------|------|------|
| Frontend baseline | `React + Vite` | `Next.js 16.2.3` | Next is strong, but this product is primarily client-driven and room-driven. Adopting server-first app machinery early is not justified unless internal authoring/admin surfaces become first-class immediately. |
| Frontend alternative | `React + Vite` | `SvelteKit 2.57.0` | Credible lean option, but weaker OSS inheritance and lower ecosystem leverage for this exact problem. |
| Vue-family option | `React + Vite` | `Nuxt 4.4.2` / `Vue 3.5.32` | Technically viable, but brings less direct leverage from the geography/realtime references already studied. |
| Room authority | `Colyseus` | `PartyKit` | PartyKit is faster, but Colyseus is better when reconnects, timers, and authoritative room state matter early. |
| Future party-mode engine | `Colyseus` | `boardgame.io 0.50.2` | boardgame.io is optimized for turn-based / phase-based games. Useful later if bluffing or secret-state modes dominate, but it is the wrong center of gravity for the geography anchor mode. |
| Database / data model | `PostgreSQL + Drizzle` | `PostgreSQL + Prisma 7.7.0` | Prisma is viable, but Drizzle keeps the data model and SQL more explicit, which is better for authored content imports and AI editability. |
| Live plumbing | `Colyseus + Supabase` | `Supabase Realtime` or `Firebase` as primary room engine | Presence and broadcast are useful, but they are not a substitute for authoritative game timing and room state transitions. |
| Primary map | `MapLibre GL JS` | `Leaflet 1.9.4` | Leaflet is fine for simple slippy maps, but MapLibre is a better fit for styled vector maps and richer reveal presentation. |
| Street View dependency | `Google Street View as one media type` | `Google Maps as the whole map stack` | Google is the strongest Street View provider, but it should not own the whole product surface if only one clue family truly needs it. |

## What Not To Use

### Do not default to `Next.js` just because the frontend is React

`Next.js 16` is a strong framework. It is not the strongest default for this product as currently framed. Prix Guesser is not a content-marketing site or server-rendered dashboard product first. The core experience is a synchronized, client-heavy game with distinct host and controller surfaces. Add Next only if the roadmap deliberately makes internal tools, content-backed server rendering, or integrated app/admin surfaces a first-wave priority.

### Do not use `Supabase Realtime` or `Firebase` as the primary game-loop authority

Use them for presence, app events, or convenience plumbing if helpful. Do not let them become the hidden timer authority for live rounds. That is how race conditions and reconnect ambiguity creep in.

### Do not center the anchor mode on `boardgame.io`

Its strengths are phases, turns, logs, and turn-order abstractions. That becomes attractive for later party variants, but it is not the natural backbone for map-centric, timer-driven, reveal-heavy geography rounds.

### Do not make Google Maps the mandatory substrate for every clue and every map

Street View is useful. It should stay a **media provider**, not an architectural dictator. Keep the clue model provider-agnostic enough to support:

- Street View panoramas
- static image crops
- map snippets
- text clues
- reveal images

### Do not start with a headless CMS as the source of truth for rounds

The authored round model is too game-specific: clue ladders, answer surfaces, scoring rules, reveal explanations, and media variants. Start with **typed schemas + import tooling + Postgres**. Build authoring UI later against that substrate.

## Unresolved Decisions The Roadmap Must Preserve

1. **Colyseus vs PartyKit depends on room durability, not taste.**  
   If the first serious build promises reconnect safety, host authority clarity, and reliable timer sync, pick Colyseus. If the goal is pure speed for a private friend prototype, PartyKit remains defensible.

2. **Google Street View should stay optional at the schema level.**  
   Circuit-internal recognition is the fantasy, but circuit coverage is uneven. The round model must support non-Google clue media without schema churn.

3. **Authoring may begin file-first before UI-first.**  
   The stack should support checked-in packs and importer scripts before committing to a full internal authoring product.

4. **Live rooms may arrive before formal auth.**  
   Private rooms, ephemeral identities, and host-controlled sessions are enough at first. Full auth should not distort the initial stack.

## Suggested Package Set

```bash
# frontend
pnpm add react react-dom @tanstack/react-query zustand zod maplibre-gl @googlemaps/js-api-loader @supabase/supabase-js
pnpm add -D vite typescript tailwindcss vitest @playwright/test

# room server + shared backend
pnpm add colyseus @colyseus/schema drizzle-orm postgres
pnpm add -D drizzle-kit tsx

# speed-first alternative room engine
pnpm add partykit
```

## Practical Repo Shape

Keep the repo as a workspace with explicit shared packages:

- `apps/web` for host screen, phone controller, solo/challenge surfaces
- `apps/room-server` for Colyseus if chosen
- `packages/domain` for round schemas, scoring, reveal logic, message contracts
- `packages/content-tools` for pack import, validation, linting, and preview transforms

That structure is more important than whether the UI lives in Vite or Next.

## Confidence By Decision

| Decision | Confidence | Notes |
|------|------|------|
| `React + Vite` as default frontend baseline | HIGH | Strong ecosystem, explicit architecture, best fit for client-heavy gameplay. |
| `Colyseus` as default live-room engine | HIGH | Best match if synced rooms matter from the start. |
| `PartyKit` as speed-first alternative | MEDIUM | Strong prototype fit, but still a 0.x package line and requires more custom discipline. |
| `PostgreSQL + Drizzle + Supabase` | HIGH | Best fit for authored content + media + room metadata. |
| `MapLibre` for primary map and Google only for Street View | HIGH | Strong technical and product separation. |
| `SvelteKit` as a viable non-React alternative | MEDIUM | Credible, but not the strongest inheritance path here. |
| `Next.js` as default | LOW | Only strong if the roadmap prioritizes integrated admin/content tooling earlier than currently implied. |

## Sources

Primary sources used for this recommendation. Package versions were checked against the npm registry on **2026-04-08**.

- React 19.2 blog: https://react.dev/blog/2025/10/01/react-19-2
- React package: https://www.npmjs.com/package/react
- Vite guide: https://vite.dev/guide/
- Vite 8 announcement: https://vite.dev/blog/announcing-vite8
- Vite package: https://www.npmjs.com/package/vite
- Next.js 16 release: https://nextjs.org/blog/next-16
- Next package: https://www.npmjs.com/package/next
- Svelte docs: https://svelte.dev/docs/svelte/overview
- SvelteKit docs: https://svelte.dev/docs/kit/introduction
- Svelte package: https://www.npmjs.com/package/svelte
- `@sveltejs/kit` package: https://www.npmjs.com/package/@sveltejs/kit
- Vue docs: https://vuejs.org/guide/introduction.html
- Vue package: https://www.npmjs.com/package/vue
- Nuxt docs: https://nuxt.com/docs/4.x/guide
- Nuxt package: https://www.npmjs.com/package/nuxt
- PartyKit docs: https://docs.partykit.io/
- PartyKit storage guide: https://docs.partykit.io/guides/persisting-state-into-storage
- PartyKit package: https://www.npmjs.com/package/partykit
- Colyseus docs: https://docs.colyseus.io/
- Colyseus reconnection guide: https://docs.colyseus.io/room/reconnection
- Colyseus room docs: https://docs.colyseus.io/room
- Colyseus package: https://www.npmjs.com/package/colyseus
- PostgreSQL 18 release: https://www.postgresql.org/about/news/postgresql-18-released-3142/
- PostgreSQL 18 docs: https://www.postgresql.org/docs/18/index.html
- Drizzle docs: https://orm.drizzle.team/
- Drizzle package: https://www.npmjs.com/package/drizzle-orm
- Prisma docs: https://www.prisma.io/docs/orm
- Prisma package: https://www.npmjs.com/package/prisma
- Supabase database docs: https://supabase.com/docs/guides/database/overview
- Supabase realtime docs: https://supabase.com/docs/guides/realtime
- Supabase storage docs: https://supabase.com/docs/guides/storage
- Supabase JS package: https://www.npmjs.com/package/@supabase/supabase-js
- MapLibre GL JS docs: https://maplibre.org/maplibre-gl-js/docs/
- MapLibre GL JS package: https://www.npmjs.com/package/maplibre-gl
- Google Maps JavaScript API Street View: https://developers.google.com/maps/documentation/javascript/streetview
- boardgame.io site: https://boardgame.io/
- boardgame.io package: https://www.npmjs.com/package/boardgame.io
- Node.js release schedule: https://nodejs.org/en/about/previous-releases
