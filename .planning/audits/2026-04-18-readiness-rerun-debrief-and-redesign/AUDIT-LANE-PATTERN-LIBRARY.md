Date: 2026-04-21
Status: active audit-program infrastructure surface

# Audit Lane Pattern Library

## Purpose

- [g:r:i] This note records the recurring lane structure that now spans multiple audit families in this workspace.
- [d:r:i] It is not a demand that every lane instantiate every possible artifact.
- [d:r:i] Its job is to make recurring audit structure explicit so later lanes can reuse a cleaner pattern instead of rebuilding scaffold from memory or chat.

## Core Lane Objects

### Opening note

- [g:r:i] Use when a family or lane needs a bounded local starting object before packeting or review.
- [d:r:i] It should name:
  - the family
  - the local question
  - scope
  - non-goals
  - why this lane exists now instead of later

### Packet

- [g:r:i] Use when the reviewer should not infer the read set from repo shape alone.
- [d:r:i] The packet should carry:
  - exact read set
  - explicit absolute paths for external or sibling-repo docs when those matter
  - anti-misread framing
  - what the lane should not silently widen into

### Spec

- [g:r:i] The spec owns the governing question and output shape.
- [d:r:i] It should state:
  - what the lane is being asked to map, challenge, or refine
  - what collapse or narrowing it must avoid
  - what output shape later inheritance needs

### Prompt

- [g:r:i] The prompt is the launch surface, not the source of truth for the lane contract.
- [d:r:i] It should remain consistent with the packet and spec rather than improvising new scope.

### Launch-truth note

- [g:r:i] Preserve requested versus effective launch settings whenever external review or spawned review materially steers later inheritance.
- [d:r:i] The note should preserve:
  - basis commit or other frozen boundary
  - packet/spec/prompt paths
  - requested model settings
  - effective model settings
  - any discovered mismatch and how it was handled

### Output

- [g:r:i] Preserve reviewer output as output, not as already-adopted doctrine.
- [d:r:i] Do not rewrite the output to sound more aligned with local preference.

### Inheritance / disposition

- [g:r:i] This is the point where local force is assigned.
- [d:r:i] It should record:
  - what is carried forward
  - what is held later
  - what is not adopted
  - what concrete next move follows

### Comparative disposition

- [g:r:i] Use only when multiple lanes materially diverge or when the comparative view is itself a durable object.
- [d:r:i] Do not force a comparative layer when one lane is clearly secondary or merely corroborative.

### Frozen artifacts

- [g:r:i] Use when the lane yields a bounded structured output that later work should compare against.
- [d:r:i] Examples already used in this workspace:
  - runtime snapshots
  - canary reports
  - propagation registry layers

## Common Lane Shapes

### Widening lane

- [d:r:i] Best when the current terrain is still undernamed.
- [d:r:i] Preferred shape:
  - opening note
  - packet
  - spec
  - prompt
  - launch-truth
  - output
  - inheritance

### Bounded reread or challenge lane

- [d:r:i] Best when a concrete local artifact already exists and the task is to widen, sharpen, or qualify it.
- [d:r:i] Preferred shape:
  - packet or tightly scoped read set
  - spec
  - prompt
  - launch-truth
  - output
  - inheritance

### Change-triggered refresh

- [d:r:i] Best when a real contract-moving slice already landed and a family map or registry should reflect the new state.
- [d:r:i] Preferred shape:
  - refresh note
  - refreshed artifact
  - governance routing update
- [d:r:i] Do not overbuild packet/spec/prompt scaffolding if no external lane is actually being launched.

### Implementation reread

- [d:r:i] Best when a landed slice needs one more adversarial read before further widening.
- [d:r:i] Preferred shape:
  - frozen basis note
  - narrow reread packet/spec/prompt
  - launch-truth
  - output
  - inheritance

## Review And Quality Discipline

- [g:r:i] Prefer a coherent baseline before a substantial lane or bounded edit batch.
- [d:r:i] Preserve launch truth when the lane materially matters.
- [d:r:i] Preserve explicit inheritance before treating output as live doctrine.
- [d:r:i] Keep contextual reread sovereign over heuristic scanner quieting.
- [d:r:i] Use audit/program verification surfaces that fit the slice:
  - `audit_refmap.py verify` for audit-link integrity
  - helper-specific tests for tooling slices
  - runtime/install gates like `harness_canary.py` only when the slice actually changes those families

## Anti-Patterns

- [d:r:i] orphaned outputs with no inheritance note
- [d:r:i] lane outputs treated as canon without explicit absorption
- [d:r:i] repeated recreation of the same packet/spec/prompt logic with no reusable local reference
- [d:r:i] forcing full lane scaffolding onto a local change-triggered refresh that does not need it
- [d:r:i] letting one family's packet, prompt, or launch-truth conventions survive only as chat memory

## Current Local Consequence

- [d:r:i] Later audit families in this workspace should treat this note as the default reusable lane pattern surface.
- [d:r:i] This note does not replace family-specific judgment; it reduces repeated scaffold rediscovery.
