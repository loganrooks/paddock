# Framework Decision Context

This note exists to clarify what we should care about when choosing a stack for Prix Guesser.

It does not recommend a winner yet.

## Why This Needs A Separate Note

The usual framework question is often asked too narrowly:
- what is fastest to build in
- what has the nicest DX
- what is currently popular

That framing is too weak for this project.

Because agentic AI compresses raw implementation time, the more important questions are:
- which stack keeps the product model clear
- which stack gives us the best leverage on maps, realtime, and media
- which stack is easiest for humans and agents to extend without drift
- which stack fits the actual prototype shape we want to prove first

## What The Framework Decision Is Not

This is not one decision.

We should keep these layers separate:
- UI framework and rendering model
- app framework or routing shell
- realtime room infrastructure
- map and Street View integration layer
- content authoring and internal tooling layer

Example:
- `React` does not imply `Next`
- `SvelteKit` does not imply a particular room backend
- `Colyseus` or `PartyKit` decisions matter independently of the frontend choice

If we blur these together, we will over-argue about the wrong thing.

## What Actually Matters

### 1. Product Model Clarity

Can the stack express the real shape of the product cleanly?

That means:
- authored F1 rounds, not just generic lat/lng drops
- multiple answer surfaces
- reveal and explanation states
- room state, timer state, scoring state, and admin state

We should prefer a stack that makes those models explicit rather than clever.

### 2. Ecosystem Leverage

The biggest technical dependencies are not generic buttons and forms. They are:
- maps
- Street View or clue media delivery
- realtime room sync
- storage
- asset handling

Framework choice matters partly because of library ecosystem, examples, and how painful these integrations are.

### 3. AI Editability

The codebase should be easy for agents to:
- inspect
- patch
- refactor
- extend across multiple surfaces

This usually favors:
- explicit TypeScript
- predictable state flow
- low magic
- conventional project structure

### 4. Multi-Surface UX Fit

This is probably not a single-screen app.

Likely surfaces include:
- host display
- player controller on phone
- solo or challenge page
- authoring or admin surface later

We should care about how well the stack supports coordinated but distinct frontends, not just one polished gameplay page.

### 5. Content Authoring Fit

The product will live or die on authored rounds and curated clue assets.

So the stack should make it straightforward to build:
- content pack viewers
- round preview tools
- verification or moderation utilities
- internal authoring aids

### 6. Operational Simplicity

Fast local iteration, easy preview deploys, and straightforward debugging matter more than ideological purity.

AI can generate code quickly.
It cannot make ambiguous deployment or runtime behavior disappear.

### 7. Debuggability

This game will have bugs around:
- timers
- room synchronization
- reconnects
- partial scoring
- reveal transitions
- media failures

We should prefer a stack that makes runtime state easy to inspect.

## Criteria To Evaluate Any Candidate

When we compare stack options later, the useful criteria are:
- clarity of state and data flow
- quality of maps and media integration
- ease of building host and phone-controller surfaces
- ease of building internal authoring tools
- suitability for private-room multiplayer
- ease of local development and deployment
- ease of agent-driven maintenance
- quality of TypeScript and testing ergonomics
- ability to grow into adjacent party modes without rewrite

## Candidate Frontend Shapes

These are not recommendations. They are the current serious candidates.

### React + Vite

Strengths:
- large ecosystem
- abundant maps and realtime examples
- easy inheritance from open-source GeoGuessr-style references
- likely easiest for agent collaboration because the patterns are common

Risks:
- can sprawl without discipline
- easy to accumulate too many abstractions
- not inherently better unless we actively benefit from the ecosystem

### Next.js

Strengths:
- strong app shell if we want integrated routing, server actions, and deploy conventions
- good if internal tools, admin surfaces, or content-backed pages become important early

Risks:
- can add complexity we do not need for a private game prototype
- SSR and app-framework machinery may be unnecessary if the main experience is highly client-side and room-driven

### SvelteKit

Strengths:
- lean mental model
- less boilerplate
- can be attractive for authored, animated, media-rich UI
- smaller code surface for some classes of interaction

Risks:
- smaller ecosystem around maps and game-specific examples
- less direct inheritance from existing GeoGuessr-style OSS references

### Vue + Vite or Nuxt

Strengths:
- good middle ground between structure and approachability
- viable for multi-surface applications
- strong enough ecosystem to remain practical

Risks:
- fewer direct reference implementations for this exact problem shape
- lower reuse from the OSS examples already studied

### Minimal Web App

Examples:
- plain TypeScript with Vite
- tiny framework footprint

Strengths:
- low surface area
- attractive if the first prototype is deliberately narrow

Risks:
- likely to become awkward once rooms, authoring tools, and multiple surfaces expand
- may optimize for the first week rather than the first real iteration cycle

## Non-Frontend Decisions That Matter More Than People Think

Two choices may matter more than the UI framework:

### 1. Realtime Room Model

Likely candidates:
- `PartyKit` for speed and lightweight room infrastructure
- `Colyseus` for stronger authoritative state and synchronization
- `boardgame.io` more for future turn-structured party modes than the core GeoGuessr-like loop

For the actual room/backend decision framing, see `13-room-backend-decision-context.md`.

If this choice is weak, the frontend framework will not save the product.

### 2. Round And Content Model

The deepest product choice is whether the app is built around:
- thin location drops
or
- rich F1-authored rounds with multiple answer surfaces and reveal logic

If this model is clear, several frontend frameworks remain viable.
If this model is unclear, no frontend choice will feel stable.

## What We Should Not Overweight

Do not over-index on:
- which framework feels fastest to type in
- which one is currently fashionable
- superficial performance claims before we know the actual bottlenecks
- the idea that one framework choice will magically settle architecture

Those are weak proxies for this project.

## Reasonable Decision Triggers

The framework decision should probably happen when we can answer these questions more concretely:
- is the first prototype solo-first, host-screen-first, or hybrid from day one
- do we want internal authoring tools in the first implementation wave
- do we want authoritative room state immediately or can that wait
- how much do we want to inherit from React-based OSS references versus diverge from them

Until then, "keep the option set small and explicit" is enough.

## Current Non-Binding Read

The current decision context points to this:
- `React` is defensible because of ecosystem leverage and reference inheritance
- `Next` is not automatically justified
- `React + Vite` may be a better baseline than a heavier app framework if the first version is mostly client-side
- `SvelteKit` remains a credible lean alternative if we value a smaller mental model over ecosystem inheritance
- the more consequential early decision is probably room architecture plus round/content modeling

This should be read as a framing aid, not a stack decision.
