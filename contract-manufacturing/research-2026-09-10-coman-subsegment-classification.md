# Sub-segment classification of cm-companies.csv (Pass 1 of the buying-signal screen)

**Date:** 2026-09-10 · **Task:** classify all 1,155 firms in `cm-companies.csv` into product sub-segments, as Pass 1 of the co-man buying-signal screen (the CPG analog of the healthcare market table Aman shared). Pass 2 = co-man verification during signal sampling. Census universe counts and the signal sample itself are the next steps.

## ⚠ Sampling-frame provenance (read first)

The company list originates from a **D&B Hoovers export (`fnb_contract_manu.xlsx`) whose file and filter settings are lost** — it was never committed to the repo; only per-row citations to it survive inside `cm-companies.csv`. The frame's construction is therefore **inferred from its own distribution**, not documented:

- **Revenue floor ~$20M** [inferred: 0 of 1,038 revenue-carrying firms below $10M; only ~5% below $21.5M; median $35.5M; P95 $116M]
- **US-wide, no state filter** [inferred: national spread — CA 156, IL 86, NJ 51, TX 49, WI 46, …]
- **Food & beverage manufacturing SIC/NAICS codes, exact list unknown** [inferred from D&B SIC-boilerplate descriptions in the rows]

Consequences: (a) the **$10–20M revenue slice is absent** — any "signal rate" measured on this frame speaks for ~$20M+ firms only; (b) sub-segments can be under-represented if their industry code wasn't in the original filter — segment emptiness is a frame artifact until checked against Census counts. A fresh, documented D&B export via Baker Library is the agreed fix (Track 2, pending).

## Method (three passes, all auditable per row)

New columns appended to `cm-companies.csv` (existing columns untouched): `subsegment_p1`, `p1_basis`, `coman_in_desc`.

1. **Keyword pass** — product keywords in `business_description` (regex list in session scratchpad script `classify_p1.py`). Single-category matches assigned (597 rows); multi/zero matches queued. Basis: `kw: <matched patterns>`.
2. **SIC-boilerplate pass** — many D&B descriptions are verbatim SIC-code definitions, not company-specific text (e.g. every SIC-2099 firm "manufactures baking powder, yeast, and other leavening compounds" — including soup and pasta makers). ~50 signature phrases mapped to segments (392 rows). Basis: `sic-boilerplate: <SIC family>`. Note: descriptions are truncated at ~180 chars in the CSV.
3. **Manual judgment pass** — remaining 166 rows classified by reading descriptions, plus 39 corrections where the SIC default or a keyword hit was clearly wrong for a company known from general knowledge (e.g. Taylor Farms → produce-fresh, Martinelli's → beverage, B&G Foods → diversified). Basis: `judgment: <note>`. **These use model knowledge, not sourced verification** — acceptable for an internal sampling frame, but any firm entering the signal sample gets verified from primary sources at that point.

`coman_in_desc = yes` (94 rows) flags explicit contract-manufacturing language ("co-pack", "private label", "contract manufacture", "toll") in the description — a cheap pre-qualifier for Pass-3 sampling, not proof of co-man status.

## Taxonomy decisions (so future passes stay consistent)

- **frozen-prepared-meals** includes refrigerated/deli prepared foods (soups, deli salads, entrees, pizza, meal kits) — the buyer/process cluster, not literal frozen state.
- **supplements-nutraceuticals** includes sports-nutrition bars/powders co-mans (Nellson, Bakery Barn, Century Foods): their buyer is the nutrition brand, not the snack aisle.
- **snacks-confectionery** includes cereal/granola, nuts, candy; **bakery** takes cookies/crackers/tortillas when baking is the core process.
- **ingredients-commodity** = firms selling to other manufacturers (flavors, blends, sweeteners, oils, egg products, fruit preps, dry blending co-packers like PacMoore/Econo-Pak).
- **prepared-foods-nec** = SIC 2099's mixed bag + pasta/noodles + canned specialties. Deliberately kept as its own bucket: descriptions carry no real product info for these firms; many diversified co-mans likely hide here. Do not read it as a product category.
- **diversified / non-manufacturer / non-food** = multi-category giants (TreeHouse, Conagra entities); retailers etc. mis-included in the frame; out-of-food-scope firms.

## Result (all 1,155 rows classified)

| subsegment_p1 | total | $10–100M | ≥$100M | no rev. data | co-man language in desc | tier A (verified co-man, from July) |
|---|---:|---:|---:|---:|---:|---:|
| meat-seafood | 202 | 188 | 15 | 0 | 0 | 0 |
| beverage | 194 | 136 | 18 | 40 | 25 | 47 |
| ingredients-commodity | 136 | 121 | 13 | 2 | 2 | 3 |
| prepared-foods-nec | 121 | 114 | 8 | 0 | 0 | 0 |
| bakery | 118 | 98 | 10 | 10 | 5 | 14 |
| dairy | 95 | 81 | 10 | 4 | 4 | 7 |
| snacks-confectionery | 78 | 54 | 6 | 17 | 16 | 27 |
| sauces-condiments | 60 | 38 | 5 | 17 | 16 | 20 |
| produce-fresh | 57 | 50 | 5 | 2 | 3 | 3 |
| frozen-prepared-meals | 49 | 32 | 6 | 11 | 9 | 15 |
| supplements-nutraceuticals | 18 | 4 | 0 | 14 | 13 | 12 |
| pet-food | 15 | 12 | 3 | 0 | 0 | 0 |
| diversified | 8 | 6 | 1 | 0 | 1 | 1 |
| non-manufacturer | 3 | 2 | 1 | 0 | 0 | 0 |
| non-food | 1 | 1 | 0 | 0 | 0 | 0 |

Reading note: tier-A and co-man-language concentrations (beverage, snacks, sauces, frozen, supplements) largely reflect **where the July verification effort already looked**, not where co-mans concentrate — meat-seafood/prepared-foods-nec/ingredients have 0 tier-A because nobody has checked them yet, not because they contain no co-mans.

## Review flags (rule 7)

1. **Accuracy is sampled, not verified:** a 15-row random spot-check of automated assignments found 2 errors (~13%) — both caused by D&B's own SIC assignment or boilerplate, both fixed. Expect a residual single-digit-% error rate in the 950 automated rows. Sampled firms get re-verified in the signal pass.
2. **Manual/judgment rows rest on model knowledge** (205 rows, basis-tagged `judgment:`) — not source-gated. They are sampling-frame metadata, not deliverable claims.
3. **Frame bias** per the provenance section above: no $10–20M firms; unknown industry-code scope.
4. Ambiguous 2033 (canned fruit/veg/sauces) rows without name/knowledge signal were defaulted to `produce-fresh` — 2 rows note this default explicitly.
5. The segment column `segment` (July, 3 coarse values, 152 rows) was left untouched; `subsegment_p1` is the finer, complete classification.
