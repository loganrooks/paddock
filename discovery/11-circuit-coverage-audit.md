# Circuit Coverage Audit

This document is a first-pass coverage audit for the GeoGuessr-style core mode.

Purpose:
- estimate which venues can support `circuit-internal` rounds with Google Street View or equivalent street-level media
- identify where only `venue-edge` or `approach` rounds are practical
- identify where fallback clue media should be treated as the default

This is not a final truth table.

It is an evidence-backed exploration artifact intended to stop us from reasoning in binaries like:
- "Street View works for F1 circuits"
- "Street View is too weak for F1 circuits"

The real picture is circuit-specific.

## Audit Method

This audit was assembled from delegated research on **2026-04-08**.

Evidence used:
- direct Google Maps Street View or panorama entry links where available
- official venue and event pages
- venue or media reports describing Street View or street-level mapping availability
- fallback-media context from official maps, tours, or venue materials

Important limitation:
- the audit does **not** claim a full meter-by-meter interactive crawl of every circuit
- some findings are direct observations from live panorama links
- some findings are inferences from official/secondary evidence plus spot checks

That means the audit is good enough to shape design and corpus strategy, but not yet good enough to guarantee specific corners without later curation.

## Coverage Rubric

### `Allow`

Circuit-internal street-level media appears meaningfully usable for the core mode.

Typical meaning:
- enough on-track or track-edge imagery to author real circuit rounds
- fallback media may still help, but is not the default

### `Allow With Fallback`

Street-level media is usable enough to matter, but not complete or reliable enough to be the sole clue substrate.

Typical meaning:
- some sections are strong
- some segments need map, satellite, official stills, or authored clue ladders

### `Fallback-First`

Do not assume Google Street View can carry the venue for core-mode circuit rounds.

Typical meaning:
- use official maps, satellite, venue imagery, or other street-level providers first
- if street-level media exists at all, it is secondary or uneven

### `Approach-Mode Friendly`

The venue may still be useful for a different mode family focused on:
- approaches
- surrounding roads
- nearby landmarks
- venue-adjacent context

This tag is complementary to the others.

## Strict Schema

Each venue row uses this schema:

- `venue`
- `classification`
- `approach_mode`
- `usable_scope`
- `main_risk`
- `fallback_media`
- `confidence`
- `evidence_type`
- `notes`

## Audit Table

| venue | classification | approach_mode | usable_scope | main_risk | fallback_media | confidence | evidence_type | notes |
|---|---|---|---|---|---|---|---|---|
| Suzuka | Allow With Fallback | Yes | Partial internal + circuit-edge | uncertain full-lap continuity | official seat/outlook images, west-course map media | Medium | direct pano + official venue guidance + secondary | good evidence for usable family resemblance, weaker evidence for blanket full-lap coverage |
| Spa-Francorchamps | Allow | Yes | strong circuit-internal | low | official track map as supplement only | High | official venue statement + direct pano + secondary | strongest candidate for true circuit-internal rounds |
| Monza | Allow | Yes | strong circuit-internal | sparse tree-lined park sections | official circuit map, grandstand views | High | direct pano + official venue pages + secondary | old-banking and park context can become clue assets |
| Imola | Allow With Fallback | Yes | venue-edge and track-adjacent park/public-road context | weaker evidence for internal Street View | walking-tour media, park views, tower/main straight imagery | Medium-High | official venue/tour docs + inference | good for circuit-family rounds, weaker for exact on-track segments |
| Red Bull Ring | Allow | Limited | strong circuit-internal | evidence freshness | official app/site map as backup | Medium-High | direct pano + secondary | looks highly usable for core mode |
| Hungaroring | Fallback-First | Yes | outer-edge and spectator-hillside context | lack of strong current internal evidence | hillside views, official gate maps, track-walk/tour media | Medium | official venue/access pages + secondary | likely better for approach or spectator-context rounds unless better media is found |
| Bahrain International Circuit | Allow With Fallback | Yes | likely approach roads and some outer-edge context | private/controlled internal venue access | official tour imagery, paddock stills, aerials | Medium | official venue docs + policy inference | not a strong default Google-Street-View circuit |
| Jeddah Corniche Circuit | Fallback-First | Yes | weak evidence for dependable public Street View | no strong Saudi Street View support found | official JCC media, aerial maps, promoter imagery | Medium-High | official venue docs + regional Google coverage evidence | public-road nature is not enough without platform coverage evidence |
| Yas Marina | Allow With Fallback | Yes | some Yas Island / venue-adjacent context likely usable | weak venue-specific Google evidence | official venue-tour media, curated trackside shots | Medium-Low | official venue docs + inference | usable as a venue-family clue target, not yet a confident circuit-internal target |
| Singapore Marina Bay | Allow | Yes | strong public-road circuit and city-circuit context | event-build clutter in some segments | official Circuit Park map and event visuals | High | official circuit docs + city Street View context | excellent candidate for circuit + city-texture rounds |
| Baku City Circuit | Allow With Fallback | Yes | route-adjacent street-level media seems usable, continuity weaker | Google evidence weaker than alternative providers | official route maps, landmark clues, Yandex panoramas if allowed | Medium | official circuit docs + alternative panorama source + inference | likely strong for city-circuit identity, less certain for uninterrupted Google-based play |
| Las Vegas Strip Circuit | Allow | Yes | strong public-road corridor coverage | event-time dressing may vary | event visuals if branding/current setup matters | High | direct route evidence + Google city coverage evidence | one of the cleanest public-road candidates |
| Silverstone | Allow | Limited | strong circuit-internal | stale branding in older imagery | recent paddock/grandstand stills | High | secondary coverage report + coverage listing | strong clue potential across complexes and runoff/fencing |
| Barcelona-Catalunya | Allow With Fallback | Limited | partial internal, likely National Circuit bias | not full F1 layout coverage | official circuit photos, satellite for GP-only sectors | Medium-High | venue page + secondary | workable but should not be treated as blanket full-loop coverage |
| Zandvoort | Allow | Yes | strong circuit-internal | low | beach-town approach media for variety | High | secondary reporting on Google refresh | dunes, banking, and pit context make it a rich authored venue |
| Interlagos | Allow With Fallback | Yes | partial internal with older evidence | freshness of evidence | satellite, official maps, perimeter visuals | Medium | older secondary + local map-media | likely usable, but should be curated carefully |
| Montreal | Allow With Fallback | Yes | park-road and some on-circuit edge coverage | race-dressed sections may be weaker | 360 circuit video, event photos | High | official park page + map-media references | particularly strong for venue-complex identity |
| Mexico City | Allow With Fallback | Yes | partial internal and venue-adjacent | uneven section quality | official event maps, trackside/stadium media | Medium-High | secondary + venue-use evidence | good for sports-complex and Foro Sol flavored rounds |
| Monaco | Allow | Yes | strong public-road circuit identity | tunnel continuity / race-week blind spots | satellite, official circuit map | High | direct pano + official circuit-road description | excellent for exact urban-circuit identity |
| Miami | Fallback-First | Yes | mostly approach and venue-adjacent | parking-lot circuit body lacks dependable Street View | aerial/satellite, campus geometry, official visuals | High | direct spot checks + official venue page | useful, but mostly not as a pure Street View circuit-internal venue |
| Austin / COTA | Allow With Fallback | Limited | at least some strong on-circuit/pit-side imagery | uneven internal continuity | satellite and official campus map | Medium-High | direct pano + official venue page | promising, but not yet proven as full-track coverage |
| Melbourne / Albert Park | Allow | Yes | strong public-road circuit coverage | fenced construction zones | satellite for temporary closures | High | direct panos + official local road closures info | very strong hybrid of circuit and park-city identity |
| Shanghai | Fallback-First | No clear Google path | weak Google Street View viability | Google mapping ecosystem mismatch in mainland China | Baidu panorama, satellite, official circuit maps, venue photos | High | direct failed spot checks + regional platform evidence | should be treated as non-Google by default |
| Lusail | Fallback-First | Limited | weak direct Google Street View evidence | standalone venue with poor public street-level support | official circuit maps, aerials, trackside photography | Medium | direct failed spot checks + venue context | better handled with alternative clue media first |

## Recommended Use Bands

### Best Early Core-Mode Candidates

These venues look most promising for authentic circuit-internal rounds:
- Spa-Francorchamps
- Monza
- Red Bull Ring
- Silverstone
- Zandvoort
- Monaco
- Singapore Marina Bay
- Las Vegas Strip
- Melbourne / Albert Park

### Strong But Should Ship With Built-In Fallback Media

These venues look usable, but should not rely on Street View alone:
- Suzuka
- Imola
- Bahrain
- Yas Marina
- Baku
- Barcelona-Catalunya
- Interlagos
- Montreal
- Mexico City
- Austin / COTA

### Fallback-First Venues

These venues should be designed around alternative clue media unless later validation improves the picture:
- Hungaroring
- Jeddah
- Miami
- Shanghai
- Lusail

## What This Means For The Product

### 1. Circuit Coverage Is Not Binary

The product should not assume:
- every circuit can be a pure Street View circuit mode
- or that Street View is too weak to matter

Both are false.

### 2. Each Venue Should Have A Media Profile

Every venue in the corpus should probably declare something like:
- `street_view_internal`
- `street_view_edge`
- `approach_media`
- `map_fragment`
- `satellite`
- `official_stills`
- `authored_text`

Not every venue needs every media type.

### 3. `Circuit-Internal` And `Approach` Should Stay Distinct

This audit reinforces your earlier point:
- some venues can support actual circuit-internal play
- some are stronger for approaches or venue-adjacent context

Those should be explicit clue families, not accidental substitutions.

### 4. The Corpus Should Start Curated

The strongest early path is:
- select the best `Allow` venues first
- then add `Allow With Fallback` venues with deliberate authored media packs
- leave `Fallback-First` venues for later or for alternate clue families

## Recommended Next Validation Step

This audit is good enough for discovery, but not enough for production curation.

Before implementation locks in, do a more rigorous pass:
- define target answer surfaces per venue
- programmatically test candidate coordinates with Street View metadata where possible
- manually verify shortlisted panos
- save usable points as curated authored targets rather than re-discovering them at runtime

## Source Notes

This document consolidates four delegated audit lanes from 2026-04-08.

Representative sources include:
- [Suzuka live pano](https://www.google.at/maps/@34.842527,136.540906,3a,75y,258.38h,90t/data=!3m5!1e1!3m3!1sjOr1uGenntJSWMfhuDjHUg!2e0!3e5)
- [Suzuka West Area page](https://www.suzukacircuit.jp/eng/f1/ticket/west_seat.html)
- [Spa official Street View announcement](https://www.spa-francorchamps.be/de/news/339_lemblematique-circuit-de-spa-francorchamps-bientot-disponible-sur-google-street-view)
- [Monza official circuit page](https://www.monzanet.it/en/circuit/)
- [Red Bull Ring report](https://www.oe24.at/digital/red-bull-ring-in-spielberg-virtuell-mit-google-street-view-erkunden/147852812)
- [Singapore GP circuit update](https://singaporegp.sg/en/news/2022/2022-updates-to-the-marina-bay-street-circuit/)
- [Las Vegas track layout](https://www.f1lasvegasgp.com/track-layout/)
- [Melbourne local information](https://www.grandprix.com.au/community/local-information)
- [Bahrain Street View project note](https://www.slrb.gov.bh/en/our-strategy-and-projects)
- [Jeddah Circuit about page](https://jeddahcircuit.com/about)
- [Shanghai circuit map PDF](https://bo.fiawec.com/assets/fileuploads/5d/ad/5dadafdd459eb.pdf)
- [Lusail venue page](https://www.qatar.gp/en/lusail-international-circuit)

For fine-grained curation, use the delegated lane memos plus direct manual verification.
