# Census universe counts by co-man sub-segment (Phase 1 of the buying-signal screen)

**Date:** 2026-09-11 · **Prior step:** `research-2026-09-10-coman-subsegment-classification.md` (D&B frame classified into sub-segments). This file adds the official universe ceiling per sub-segment.

**Source (single, primary):** US Census Bureau, *SUSB 2022 — U.S., 6-digit NAICS by receipts size*, release 2025-04-10, built from 2022 County Business Patterns + 2022 Economic Census. File: https://www2.census.gov/programs-surveys/susb/tables/2022/us_6digitnaics_rcptsize_2022.xlsx (landing page: https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html). Receipt-size bands 09–17 sum to exactly **$10M–<$100M** — the same revenue-qualified band used in the healthcare screen Aman shared. Counts are **employer firms** (enterprises), not establishments.

## The one caveat that governs everything

**Census counts ALL manufacturers in a code — brand plants and contract manufacturers mixed.** NAICS has no co-man code. These are **ceilings** on the co-man universe, not co-man counts. The co-man share per sub-segment is unknown at desk level (working overall estimate from P1: ~5,000–10,000 US food/CPG co-mans `[UNVERIFIED — triangulated]`); the buying-signal sample (next phase) verifies co-man status firm-by-firm.

## Universe by sub-segment (US employer firms, 2022)

| Sub-segment | Total firms | **$10M–<$100M** | $100M+ | D&B frame in $10–100M (for coverage feel) |
|---|---:|---:|---:|---:|
| beverage — *incl. breweries/wineries/distilleries, see notes* | 12,311 | 575 | 210 | 136 |
| meat-seafood | 3,383 | 508 | 361 | 188 |
| bakery — *incl. 8,628 retail storefront bakeries* | 12,031 | 410 | 194 | 98 |
| ingredients-commodity | 1,546 | 280 | 294 | 121 |
| pet-food | 1,212 | 279 | 193 | 12 |
| snacks-confectionery | 2,384 | 242 | 172 | 54 |
| frozen-prepared-meals (incl. refrigerated prepared) | 1,312 | 231 | 139 | 32 |
| dairy | 1,250 | 206 | 234 | 81 |
| produce-fresh (frozen/canned/dried fruit & veg) | 1,055 | 200 | 140 | 50 |
| prepared-foods-nec | 875 | 118 | 88 | 114 |
| sauces-condiments (NAICS 311941 only — narrow) | 342 | 59 | 39 | 38 |
| supplements — *REFERENCE ONLY: NAICS 325411/325412 mixes supplements with pharma* | 1,888 | 326 | 295 | 4 |

Illustrative annual software TAM at the screen's **$10,000/firm/yr convention** (not an estimate — real food-mfg software ACVs span ~$5k QMS tools to $250k+ ERP `[UNVERIFIED range — vendor pricing to be captured in the signal sample]`): $10–100M-band firms × $10k ⇒ e.g. beverage ~$5.8M/yr, meat-seafood ~$5.1M/yr … sauces ~$0.6M/yr. Total across food/bev sub-segments (excl. supplements reference row): **~$31M/yr** in the revenue-qualified band — an order-of-magnitude reality check: **a co-man-only software product in one sub-segment is a niche; the company-shaped bar from `cm-research-plan.md` (system of record for a P&L slice, expansion path) matters more than sub-segment choice.**

## Full NAICS-level table

| NAICS | Description | Sub-segment | Total | $10–<100M | $100M+ |
|---|---|---|---:|---:|---:|
| 311111 | Dog & cat food | pet-food | 337 | 45 | 49 |
| 311119 | Other animal food | pet-food | 875 | 234 | 144 |
| 311211 | Flour milling | ingredients | 204 | 41 | 50 |
| 311212 | Rice milling | ingredients | 63 | 9 | 17 |
| 311213 | Malt | ingredients | 27 | 0 | 5 |
| 311221 | Wet corn milling | ingredients | 32 | 0 | 10 |
| 311224 | Soybean/oilseed | ingredients | 102 | 19 | 30 |
| 311225 | Fats & oils refining | ingredients | 95 | 12 | 23 |
| 311230 | Breakfast cereal | snacks | 74 | 0 | 14 |
| 311313 | Beet sugar | ingredients | 16 | 0 | 8 |
| 311314 | Cane sugar | ingredients | 44 | 4 | 17 |
| 311340 | Nonchocolate confectionery | snacks | 505 | 58 | 36 |
| 311351 | Chocolate from cacao | snacks | 250 | 17 | 19 |
| 311352 | Confectionery from purchased chocolate | snacks | 927 | 63 | 23 |
| 311411 | Frozen fruit/juice/veg | produce | 139 | 27 | 35 |
| 311412 | Frozen specialty food | frozen-prepared | 460 | 102 | 56 |
| 311421 | Fruit & vegetable canning *(mixed: incl. pickles, some sauces/juice)* | produce | 691 | 115 | 73 |
| 311422 | Specialty canning | prepared-nec | 104 | 7 | 20 |
| 311423 | Dried & dehydrated | produce | 225 | 58 | 32 |
| 311511 | Fluid milk | dairy | 223 | 60 | 73 |
| 311512 | Butter | dairy | 43 | 0 | 11 |
| 311513 | Cheese | dairy | 410 | 86 | 71 |
| 311514 | Dry/condensed/evaporated | dairy | 122 | 25 | 49 |
| 311520 | Ice cream & frozen desserts | dairy | 452 | 35 | 30 |
| 311611 | Animal slaughtering | meat-seafood | 1,232 | 99 | 89 |
| 311612 | Meat processed from carcasses | meat-seafood | 1,421 | 240 | 143 |
| 311613 | Rendering | ingredients | 76 | 18 | 17 |
| 311615 | Poultry processing | meat-seafood | 295 | 68 | 83 |
| 311710 | Seafood prep & packaging | meat-seafood | 435 | 101 | 46 |
| 311811 | Retail bakeries *(storefronts — exclude from co-man math)* | bakery | 8,628 | 82 | 34 |
| 311812 | Commercial bakeries | bakery | 2,447 | 200 | 97 |
| 311813 | Frozen cakes/pastries | bakery | 192 | 43 | 27 |
| 311821 | Cookies & crackers | bakery | 375 | 34 | 27 |
| 311824 | Dry pasta, dough & flour mixes *(mixed)* | ingredients | 328 | 66 | 38 |
| 311830 | Tortillas | bakery | 389 | 51 | 9 |
| 311911 | Roasted nuts & peanut butter | snacks | 228 | 50 | 46 |
| 311919 | Other snack food | snacks | 400 | 54 | 34 |
| 311920 | Coffee & tea | beverage | 1,014 | 69 | 38 |
| 311930 | Flavoring syrup & concentrate | ingredients | 149 | 23 | 22 |
| 311941 | Mayo, dressing & prepared sauces | sauces | 342 | 59 | 39 |
| 311942 | Spice & extract | ingredients | 410 | 88 | 57 |
| 311991 | Perishable prepared food | frozen-prepared | 852 | 129 | 83 |
| 311999 | All other misc food | prepared-nec | 771 | 111 | 68 |
| 312111 | Soft drinks | beverage | 396 | 53 | 67 |
| 312112 | Bottled water | beverage | 213 | 27 | 13 |
| 312113 | Ice *(caveat: not a software buyer segment)* | beverage | 254 | 6 | 6 |
| 312120 | Breweries *(mostly brand producers)* | beverage | 4,922 | 148 | 21 |
| 312130 | Wineries *(mostly brand producers)* | beverage | 4,286 | 200 | 37 |
| 312140 | Distilleries *(mostly brand producers)* | beverage | 1,226 | 72 | 28 |
| 325411 | Medicinal & botanical *(supplements + pharma mixed)* | supplements-REF | 709 | 103 | 69 |
| 325412 | Pharmaceutical preparation *(mostly pharma)* | supplements-REF | 1,179 | 223 | 226 |

## Readings (desk-level, to be distrusted until sampled)

1. **The $10–100M food/bev manufacturing universe is ~3,000–3,700 firms** (sum of food sub-segments, minus retail bakeries and alcohol caveat rows ≈ 2,900–3,400; alcohol co-pack adds some back). The D&B frame (1,038 revenue-carrying firms, floor ~$20M) covers very roughly a third of it — consistent with its inferred ~$20M floor cutting the band's bottom half.
2. **Beverage's non-alcohol core is small and the frame already covers most of it:** Census non-alcohol beverage codes (soft drinks, water, coffee/tea) hold ~149 firms in-band vs 136 in the D&B frame. `Hypothesis:` the original export leaned heavily on beverage codes; kill-test against a fresh documented export (Track 2).
3. **Frame gaps vs Census:** pet-food (279 in-band vs 12 in frame) and supplements (326 REF vs 4) are near-absent from the D&B frame — industry-code scope artifacts, exactly as the provenance warning predicted. If either sub-segment matters, it needs its own frame pull.
4. **prepared-foods-nec anomaly:** D&B frame has 114 in-band vs Census 118 — near-total coverage of a code family that D&B's SIC boilerplate says is where diversified/multi-line co-mans live. `Hypothesis:` co-mans are over-represented in NEC codes relative to brand plants (a co-man's multi-product reality fits no specific code); would explain why the export favored it. Confirmable in the signal sample by the co-man hit-rate per sub-segment.
5. Sub-segment mapping is many-to-one and two codes are structurally mixed (311421, 311824) — treat their sub-segment placement as approximate.

## Review flags (rule 7)

- Firm counts are exact from one primary source (no ranges needed; no conflicting source consulted). The *interpretations* above are hypotheses, labeled.
- The $10k/firm TAM is a labeled convention carried over from the healthcare screen for comparability, not an estimate.
- "D&B frame in $10–100M" column compares my CSV segmentation (13% sampled error rate in automated rows) against NAICS buckets that don't align one-to-one — coverage ratios are indicative, not measured.
- Supplements row is deliberately non-comparable (NAICS 325 mixes pharma); flagged in both tables.
- Co-man share per sub-segment remains `[UNVERIFIED]` — the central unknown this screen exists to resolve by sampling.
