# Source register — shop-floor data layer

**Every source used, where it came from, and what depends on it.** Append a row whenever a new
source is used. Grade honestly: `A` primary (government, regulator, company filing, the company's
own site) · `B` credible secondary (trade press, industry body, named expert call) · `C` weak
(report mill, vendor comparison site, aggregator) · `D` model knowledge / inference, no source.

Rule 1 of `../CLAUDE.md` governs: every numeric or named claim carries a source or `[UNVERIFIED]`.
This file is the index of those sources; it is not a substitute for inline citation.

## Register

| # | Source | Grade | Accessed | Used for | Depends on it |
|---|---|:---:|---|---|---|
| 1 | US Census Bureau, **SUSB 2022 — U.S. 6-digit NAICS by receipts size**, `us_6digitnaics_rcptsize_2022.xlsx`, released 2025-04-10 · https://www2.census.gov/programs-surveys/susb/tables/2022/us_6digitnaics_rcptsize_2022.xlsx | **A** | 2026-09-11 | Exact US employer-firm counts by receipts band ($10M–<$100M via bands 09–17) for 51 food/bev NAICS codes | `../contract-manufacturing/research-2026-09-11-census-universe-counts.md`; niche screen |
| 2 | Census SUSB landing pages · https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html · https://www.census.gov/data/datasets/2022/econ/susb/2022-susb.html | A | 2026-09-11 | Confirming a receipts-size table exists for 2022 (the dataset page lists employment-size only) | ↑ |
| 3 | **`cm-companies.csv`** — 1,155-firm frame derived from a **D&B Hoovers export (`fnb_contract_manu.xlsx`) that is LOST**. Filters not documented; inferred from the data as US food/bev manufacturers, revenue floor ~$20M | **C** (provenance broken) | built 2026-07; classified 2026-09-10 | Sampling frame; sub-segment classification | `../contract-manufacturing/research-2026-09-10-coman-subsegment-classification.md` |
| 4 | **eCFR 21 CFR 113.100** — processing and production records for thermally processed low-acid foods · https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-113/subpart-F/section-113.100 | **A** | 2026-09-17 | Mandated recording of temperature, pressure, vent and process times per retort per day, operator-signed, retained 3 years → the desk test for "does data exist" | Niche selection criterion |
| 5 | HighByte (IDC Industrial DataOps MarketScape 2026 Leader) · https://www.highbyte.com/ | B | 2026-09-11 | DataOps layer is a named category with funded leaders — the direct competitive set | Pitch critique; `mdl-arena.md` (pending) |
| 6 | Litmus — $30M strategic funding, industrial edge data platform · https://techfundingnews.com/litmus-industrial-ai-edge-data-platform-funding/ | B | 2026-09-11 | ↑ | ↑ |
| 7 | AlphaSense expert calls + SEC/annual filings, via `../archive/cm-document-thesis-2026-07/` | **B** (named experts) / C (AlphaSense synthesis) | 2026-07-26 → 07-28 | "60% of sub-$1B food companies run on laptops and Excel"; the clean-data warning (former VP Supply Chain, Quality Sterling Group); FoodReady ACV ~$18–60k/yr `[UNVERIFIED, vendor-comparison site]`; Gehl Foods supplier terms on unilateral documentation control | `mdl-research-plan.md` corrections; data-pooling-rights question |
| 8 | Scale AI physical-AI data volumes; XDOF teleoperation data for labs · https://techcrunch.com/2026/06/17/collecting-robot-training-data-is-dirty-unglamorous-work-some-ai-labs-are-already-paying-xdof-to-do-it/ | B | 2026-09-11 | What frontier labs actually buy for physical AI (robot-action data, not process telemetry) — bears on Adarsh's column and on ICP (1) | Pitch critique |

## Not yet used, but named in the plan

- Equipment **OEM manuals and spec sheets** — for which sensors ship standard on a given line. Grade A when it is the manufacturer's own document.
- **SQF / BRCGS scheme documents** — what must be recorded for certification. Grade A.
- **USDA FSIS** HACCP recordkeeping for meat and poultry — the USDA analog of source 4. Grade A.
- **21 CFR 114** (acidified foods) — the acidified analog of source 4. Grade A.
- Vendor **connector/integration docs and job postings** — to extract each competitor's data inputs. Grade A for the company's own posting, B for aggregators.

## Standing warnings

- **Source 3 is the weak link in everything quantitative about the company universe.** The original
  export's filters are lost, so the frame is missing the $10–20M slice entirely, and pet food and
  supplements are near-absent. A fresh, documented D&B Hoovers pull via Baker Library is the fix
  (not yet done).
- Market-size figures in `../contract-manufacturing/cm-market-structure.md` are report-mill grade
  (C) except the Contract Packaging Association figure. Treat as order-of-magnitude.
- Nothing in this register is operator-confirmed for the current thesis. Per rule 6, all of it
  supports hypotheses only.
