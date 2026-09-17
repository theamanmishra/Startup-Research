# Hyper-niche screen — Q1, step 1 (2026-09-17)

**Board line served:** Q1, sub-branch (a) — *study process flows of hyper-niches*. This file decides
**which** hyper-niches to study. It does not yet answer Q1 itself.

**Unit of analysis:** a hyper-niche is a set of plants sharing a **production process**, because
process determines both what sensors exist and what fails. NAICS 6-digit is used as the practical
proxy, with the caveat that two codes are internally mixed (311421 blends retort canning, freezing
and pickling; 311999 is a catch-all).

## Column provenance — read before using the ranking

| Column | Source | Status |
|---|---|---|
| **Firms** | Census SUSB 2022, receipts bands 09–17 = $10M–<$100M (source 1 in `mdl-sources.md`) | **Hard data, exact** |
| **Reg** | Named rule per row: 21 CFR 113, 21 CFR 114, Grade A PMO, 9 CFR 417, 21 CFR 123, FSMA 21 CFR 117 | **Rule verified; the 1–5 translation is judgment** |
| **Auto** | none | **`[UNVERIFIED]` — judgment** |
| **Fail** | none | **`[UNVERIFIED]` — judgment** |
| **Edge** | read against `../founder-profile.md` | judgment |
| **Score** | arithmetic | derived |

Three of five scored columns are judgment. The ranking is **directional**. Its load-bearing column
(Reg, 35.3% weight) is the sourced one; Auto gets corrected by the process-flow work in Q1, which
measures exactly that.

**Weights.** Agreed with Aman: Reg 30 · Auto 25 · Fail 20 · Arena 15 · Edge 10. **Arena crowding is
deferred** — scoring it before the arena pass would be circular — so the remaining four are
renormalised to Reg 35.3% · Auto 29.4% · Fail 23.5% · Edge 11.8%. Arena will be applied as a
**disqualifier** on the final three, not as a score.

Score = weighted mean of the four 1–5 scores × 20, on a 0–100 scale. **Firm count does not enter the
score** — it is already the Stage 1 filter, so counting it again would let big-but-unpromising
categories through.

## The regulatory tiering — the screen's main finding

This is the part that answers the board's first asterisk (*data exists*) from a desk.

| Tier | What is legally required | Verified source |
|---|---|---|
| **5 — continuous instrument records mandated** | Retort: temperature, pressure, vent and process times per retort per day, operator-signed, retained 3 years | [21 CFR 113.100](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-113/subpart-F/section-113.100) |
| | Dairy HTST/UHT: safety thermal limit recorder (STLR) + flow recorder/controller charts mandatory; instruments tested at install and every 6 months | [Grade A PMO](https://www.fda.gov/media/114169/download), [FDA dairy inspection guide](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/inspection-guides/dairy-product-manufacturers-495) |
| | Meat & poultry: actual times, temperatures and other quantifiable CCP values recorded at the time the event occurs, dated and signed; retained 1 yr (slaughter) / 2 yrs (other) | [9 CFR 417.5](https://www.ecfr.gov/current/title-9/chapter-III/subchapter-E/part-417/section-417.5) |
| | Seafood: HACCP monitoring records | 21 CFR 123 `[UNVERIFIED — rule named, recordkeeping text not read]` |
| **4 — critical values per batch** | Acidified foods: pH measurements and other critical factors per lot, with product code, date, container size; retained 3 years | [21 CFR 114.100](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-114/subpart-F/section-114.100) |
| **2–3 — preventive-control records only** | FSMA preventive controls: monitoring records exist, but CCPs are typically discrete (metal detection, allergen changeover, sanitation) rather than continuous process traces | 21 CFR 117 `[UNVERIFIED — inferred application per niche]` |

**Read:** wet and thermal processes carry legally mandated, dated, signed, multi-year process
records. Dry processes largely do not. That is the sharpest desk-available predictor of whether
shop-floor data exists at all.

## Stage 1 — eligibility

Applied to all 51 food and beverage NAICS codes in
`../contract-manufacturing/research-2026-09-11-census-universe-counts.md`.

Filters: **≥50 firms** in the $10M–<$100M band · **is a plant**, not a storefront · **in F&B scope**
(NAICS 311–312).

**25 codes passed. Excluded for cause:**

| NAICS | Niche | Firms in band | Why excluded |
|---|---|---:|---|
| 311811 | Retail bakeries | 82 | Storefront operations, not shop floors |
| 312113 | Ice manufacturing | 6 | Not food processing; also below the floor |
| 311111 | Dog & cat food | 45 | Outside F&B scope |
| 311119 | Other animal food | 234 | Outside F&B scope (animal feed) |

**Notable drops on the 50-firm floor** (worth revisiting if the floor is ever lowered): 311422
Specialty canning — **7 firms but Reg tier 5**, the highest-regulation niche in all of F&B; 311813
Frozen cakes and pastries (43); 311211 Flour milling (41); 311520 Ice cream (35, PMO applies);
311821 Cookies and crackers (34); 312112 Bottled water (27); 311514 Dry and condensed dairy (25,
PMO applies). Codes with **zero** firms in band: cereal, butter, malt, wet corn milling, beet sugar.

## Stage 2 — the full ranking, all 25

| # | NAICS | Niche | Firms | Reg | Auto | Fail | Edge | Score |
|---:|---|---|---:|:---:|:---:|:---:|:---:|---:|
| 1 | 311511 | Fluid milk | 60 | 5 | 5 | 5 | 4 | 97.6 |
| 2 | 311513 | Cheese | 86 | 5 | 4 | 5 | 4 | 91.8 |
| 3 | 311421 | Fruit & vegetable canning | 115 | 5 | 4 | 5 | 3 | 89.4 |
| 4 | 311615 | Poultry processing | 68 | 5 | 3 | 5 | 2 | 81.2 |
| 5 | 311941 | Mayo, dressing & prepared sauces | 59 | 4 | 4 | 4 | 3 | 77.6 |
| 6 | 311710 | Seafood prep & packaging | 101 | 5 | 2 | 5 | 2 | 75.3 |
| 7 | 311612 | Meat processed from carcasses | 240 | 5 | 2 | 5 | 2 | 75.3 |
| 8 | 311611 | Animal (exc. poultry) slaughtering | 99 | 5 | 2 | 5 | 2 | 75.3 |
| 9 | 312111 | Soft drinks | 53 | 3 | 5 | 3 | 4 | 74.1 |
| 10 | 311911 | Roasted nuts & peanut butter | 50 | 3 | 3 | 4 | 4 | 67.1 |
| 11 | 311412 | Frozen specialty food | 102 | 3 | 3 | 4 | 3 | 64.7 |
| 12 | 311919 | Other snack food | 54 | 3 | 3 | 3 | 4 | 62.4 |
| 13 | 311999 | All other misc food | 111 | 3 | 3 | 3 | 3 | 60.0 |
| 14 | 311830 | Tortillas | 51 | 3 | 3 | 3 | 3 | 60.0 |
| 15 | 311812 | Commercial bakeries | 200 | 3 | 3 | 3 | 3 | 60.0 |
| 16 | 311423 | Dried & dehydrated food | 58 | 3 | 3 | 3 | 3 | 60.0 |
| 17 | 311352 | Confectionery from purchased chocolate | 63 | 2 | 3 | 3 | 5 | 57.6 |
| 18 | 311340 | Nonchocolate confectionery | 58 | 2 | 3 | 3 | 5 | 57.6 |
| 19 | 311991 | Perishable prepared food | 129 | 3 | 1 | 4 | 3 | 52.9 |
| 20 | 311942 | Spice & extract | 88 | 2 | 3 | 3 | 3 | 52.9 |
| 21 | 311824 | Dry pasta, dough & flour mixes | 66 | 2 | 3 | 3 | 3 | 52.9 |
| 22 | 312120 | Breweries | 148 | 2 | 4 | 2 | 2 | 51.8 |
| 23 | 311920 | Coffee & tea | 69 | 2 | 3 | 2 | 4 | 50.6 |
| 24 | 312140 | Distilleries | 72 | 2 | 3 | 2 | 2 | 45.9 |
| 25 | 312130 | Wineries | 200 | 2 | 3 | 2 | 2 | 45.9 |

Reg basis per row is in the screen script (`niche_screen.py`, session scratchpad); the tier table
above gives the governing rule for each group.

## Stage 3 — the spanning pick (recommendation, pending Aman's decision)

Selection logic: this is a **research sample, not a market choice.** Pick three that *differ* on the
key uncertainty (does data exist), so the answer comes back as a range. Three data-rich niches would
teach us nothing about generalisability; three data-poor ones could kill the thesis wrongly.

| Slot | Recommended | Firms | Rationale |
|---|---|---:|---|
| **High** | **Retort-canned low-acid vegetables & soups** — narrowed subset of 311421 | 115 (code total) | Two mandated recording regimes (113 retort + 114 acidified). A retort room is the most instrumented spot in any food plant. Best case for "data exists." |
| **Mid** | **Mayo, dressings & prepared sauces** (311941) | 59 | Acidified rule mandates pH per batch but not continuous traces. Kettle/batch wet-fill — where much of mid-market food actually sits. |
| **Low** | **Perishable prepared food** (311991) | 129 | Largely hand assembly, Auto scored 1. The genuine floor: if the thesis works here it works anywhere. |

**Open decisions for Aman:**
1. **Low slot — prepared food or confectionery?** Prepared food is the harder test of the thesis.
   Confectionery (311340 + 311352, 121 firms combined) is where his edge scores 5 — the ITC
   chocolate background. Thesis-testing argues prepared food; actionability argues confectionery.
2. **Meat and poultry rank 4th and 6th–8th and are not in the recommended three.** They carry the
   strongest mandated records in F&B, but fabrication is manual and founder edge is 2. Take a slot,
   or park?

## Review flags (rule 7)

1. **Rule 1 breach, disclosed:** Auto, Fail and Edge columns carry no source. They are judgment and
   should read `[UNVERIFIED]`. Reg is anchored to a named rule per row; the 1–5 translation of those
   rules is still my judgment.
2. **Two mixed codes.** 311421 blends retort canning, freezing and pickling — three different
   instrumentation stories under one code; the recommendation therefore narrows it to retort-canned
   low-acid products. 311999 is an explicit catch-all and its Reg/Auto scores are near-meaningless.
3. **Seafood (21 CFR 123) and FSMA 117 applications were not read in full** — the rules are named
   and their existence is certain, but the specific recordkeeping text was not verified. Flagged in
   the tier table.
4. **The PMO chart *retention* period was not found** in the sources consulted. The requirement to
   *record* is verified; how long charts must be kept is not.
5. **No operator confirmation of anything here.** Per rule 6 this is a hypothesis-ranking, and the
   Auto column in particular is the thing most likely to be wrong — a mid-market plant may have a
   mandated recording chart that is a paper circle in a drawer, which satisfies the law and is
   useless as data. That distinction is exactly what Aman's calls must resolve.
