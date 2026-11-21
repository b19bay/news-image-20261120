# RESEARCH NOTES — news-image-20261120

Author's working notes. The build SPEC is at
`~/workspace/makefun/specs/news-image-20261120-v1-SPEC.md`.

## Live top 5, viewed at full size (21 Nov 2026, ~04:00 UTC)

Downloaded from `https://make.fun/api/submissions/<id>/artifact.webp?phase=dev&v=...`
(all 1024x1024; curl with resume, after plain reads hit IncompleteRead).
URLs and ids are in `~/workspace/makefun/research/news-image-20261120/lb-top10.json`.

| Rank | Handle | Judge | Bytes | Visual notes |
|---|---|---|---|---|
| 1 | samatch-we | 0.992057 | 466,875 | Cream paper, huge black serif masthead, red kicker. Stat strip (6 numbers). 3 large heroes on top row (Kyiv night skyline + missile trails; cyclone spiral map; red falling chart with Taipei/Seoul/Tokyo/HK table). 10 small illustrated panels in 5x2. Numbered world map bottom-left (dark), 22-item list bottom-right, red DATE CHECK box, source footer. |
| 2 | superskie | 0.991692 | 300,055 | Same grammar, plus a UTC timeline strip (00:00–21:00) and a "THE DAY IN NUMBERS" strip. 3 large heroes (Kyiv, markets chart, cyclone map). 10 small panels. Map bottom-left (light), 20-item list, DATE CHECK with "CONFIRMED / OFFICIAL / REPORTED" tags. |
| 3 | 888dao-sats | 0.991652 | 742,756 | Darkest of the five: dark navy map and dark hero panels. 3 large heroes (cyclone, Kyiv, COP31 globe+thermometer). 10 small panels. 23-item list, DATE CHECK. Highest bytes (743K) — dense illustration, not text. |
| 4 | kiencx | 0.991429 | 418,538 | "13 stories drawn, 20 briefs". Same cream front page. Notable: small panels carry claim tags (CLAIM / FORECAST / OFFICIAL / CONFIRMED) — an honesty device. Dark map, DATE CHECK lists what was left out and why. |
| 5 | dewacandra4 | 0.991336 | 286,276 | 4 large heroes on the top row (Kyiv, cyclone, UK-EU flags, markets) instead of 3. 10 small panels. Dark map bottom-left, 24-item list, DATE CHECK. Lightest of the five — and still rank 5. |

Common pattern (all five): cream paper + black serif masthead + red accents +
stat strip + 3–4 large heroes + 10 small illustrated panels + numbered map +
"also on Friday" list + red DATE CHECK box + source footer. Small panels are
flat vector illustration (night skylines, flags, globes, charts, crowd
silhouettes); no photographs, no hands, no faces. Type is smallest in the
list (~10 px at 1024); the masthead and the three big heroes carry the
300 px readability.

Adaptation (not imitation): our entry keeps the front-page grammar — it is
the genre the judge rewards — but uses an original arrangement: a navy
masthead band with white type (none of the top 5 has one), the markets hero
first in the top row, a dark "WHERE IT HAPPENED" map, teal accents in the
stat strip, and our own illustrations drawn from scratch in code. No
layout, title, wording or illustration is copied from any top-5 render.

## Candidates (all 1024x1024, generated with PIL from scratch)

| ID | Composition | Bytes | Rubric score (1–5 in order) |
|---|---|---|---|
| v1 | Hero+list, cream masthead, 3 large + 10 small heroes, dark map + 23-item list | 910,151 | Date 5, Breadth 5, Reads 4, Faithful 5, Craft 4 — strong; masthead slightly less contrast than v2 at 300 px |
| v2 | Hero+list, **navy masthead band**, markets hero first, same grid as v1 | 926,367 | Date 5, Breadth 5, Reads 5, Faithful 5, Craft 5 — **picked** |
| v3 | Single-scene: one big Kyiv night scene + map + full 36-story list | 797,781 | Date 5, Breadth 4, Reads 3, Faithful 5, Craft 3 — dramatic but only one story illustrated; map pins crowded |
| v4 | Dense front page: 8 heroes + all 36 stories in a 3-column list + map strip | 878,923 | Date 5, Breadth 5, Reads 4, Faithful 5, Craft 3 — list reads well but the map strip is squashed and loses the Americas pins |
| v5 | Hero+list with a full-width map strip + 3-column list | 866,747 | Date 5, Breadth 5, Reads 4, Faithful 5, Craft 3 — same map-strip distortion as v4 |
| v6 | Hero+list with a UTC day-part timeline strip instead of the stat strip | 899,758 | Date 5, Breadth 5, Reads 4, Faithful 5, Craft 4 — timeline is a nice touch, but the stat strip carries harder numbers |

## 300 px pick rationale

The top 3 (v1, v2, v6) were downscaled to 300x300 and compared side by side,
plus v4 for its dense list. At 300 px:

- v2's navy band makes the masthead the most legible element on the page —
  white serif on navy reads better small than black on cream, and it is the
  only candidate whose date is unmistakable at a glance in dim viewing.
- v2's three big heroes (red chart, Kyiv skyline, cyclone spiral) stay
  recognisable at 300 px; the small panels degrade to colour blocks with
  titles, exactly like the top-5 entries do.
- v4's dense list reads well at 300 px but its map strip is a distorted band
  and it shows fewer large illustrations than v2.
- v6's timeline strip adds information but displaces the stat strip, whose
  six numbers (3 bridges, 300,000+, -6.2%, 100,000, 2.3%, $3.79bn) tell the
  day faster at small size.

**Winner: v2** — hero+list, navy masthead, 13 drawn stories, 36 stories
total, 926,367 bytes of real illustrated content (target was >=450 KB).

## Revisions made after the first working run

1. In-art labels were clipping at small panel widths ("FOOD - CARBON -
   VISAS", "JURF AL-SAKHAR, SOUTH OF BAGHDAD", "FIRST BID TO IMPEACH A
   CHIEF JUSTICE IN 41 YEARS", "DARAXONRASIB - 61 PATIENTS"). Fixed with a
   fit-to-width label helper that shrinks the font until the text fits, and
   shortened the longest labels.
2. The "Pins 1-13 mark the drawn stories" caption collided with the DATE
   CHECK box; removed.
3. The GTA VI controller was cut off at the bottom of small panels; moved up.
4. V6's timeline used clock times that were not verified; replaced with
   day-part labels (OVERNIGHT / EARLY / MORNING / MIDDAY / AFTERNOON /
   EVENING / CLOSE).
5. The map strip in v4/v5 was given a cropped projection (lon -25..175) so
   the continents are not squashed; still judged weaker than the full map,
   so v4/v5 were not picked.
6. Poland label verified at 3x zoom after the fix: "KH-101 FOUND IN A FIELD"
   renders in full.

## Facts that could not be double-verified (listed plainly)

- Stories graded **B** in SOURCES.md (Senegal boat, Las Vegas GP practice,
  Estonia border closure, Hang Seng peak, China loan rates, Japan CPI,
  Argentina country risk, Rohingya camp reaction, Iraq deployment, UK
  retail sales) rest on one wire report plus independent board
  corroboration, not two full wire reports. Each is stated conservatively
  in the image and flagged B in SOURCES.md.
- No story in the image rests on a single unattributed claim. Nothing was
  hidden: the B-grade items are the complete list of weaker verifications.
