# Generated Corpus Archive Strategy

## Scope

Define how the repo should treat bulky generated corpora, especially:

- `.planning/explore/2026-04-11-product-vision-game-design/scraped-radio/`

## Decision

Use a hybrid retention posture with an archive branch.

## Main-Branch Posture

Keep in the active branch:

- extraction specs
- provenance notes
- manifests or URL lists
- any curated subset that is actively being cited
- decision records explaining where the full corpus lives

Do not let the full corpus remain an accidental permanent resident of the active development branch without an explicit decision.

## Archive-Branch Posture

Preferred target:

- `archive/scraped-radio-2026-04`

Acceptable alternative:

- `research-archive/scraped-radio-2026-04`

The goal is to preserve the full corpus without making it the ambient default working surface for normal development.

## Preconditions Before Moving

1. Keep the extraction spec and provenance files in the active branch.
2. Keep at least one pointer doc in the active branch naming the archive branch.
3. Make the move as preservation, not deletion.
4. Do not mix the archive move into unrelated code or canon branches.

## Why This Beats The Two Extremes

- Better than deleting the corpus: it remains available for later content work.
- Better than leaving it in the active branch forever: it stops dominating workspace cleanliness and review boundaries.

## Operational Reminder

This is a branch strategy recommendation, not yet a completed archive move.
