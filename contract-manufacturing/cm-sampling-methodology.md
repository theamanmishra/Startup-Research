# P5 interview sampling methodology (DRAFT — finalize with Aman before sweep)

**Date:** 2026-07-26. Governs how the outreach list is built. The current `cm-outreach-list.csv` (20 rows) is a **convenience sample from search snippets** — kept only as seed examples until this methodology is locked and the list is rebuilt from a proper frame.

## 1 · Principle: sample for evidence, not access

Every interview exists to kill or validate named hypotheses (the four whitespace cells in `cm-arena.md` + H2 paying capacity + the unsourced co-man margin range). The sample is a **purposive, stratified quota sample** — standard for qualitative discovery. It is NOT meant to be statistically representative; it IS meant to cover the strata across which the answers plausibly differ, so we can't be fooled by one corner of the market.

## 2 · Population and sampling frame

- **Population:** US food/CPG co-manufacturers & co-packers (working estimate 5,000–10,000; see `cm-market-structure.md`).
- **Primary frame — D&B Hoovers export** (systematic, filterable, includes contacts): NAICS 311 + 3121 · US · revenue $5M–$500M · business-description keywords `"co-pack" OR "co-man" OR "contract manufactur" OR "private label"`. Expected yield: 200–500 companies.
- **Frame enrichment:** SQF certification flag (SQFI public database) · ownership type from Orbis (family / PE-backed / corporate division).
- **Coverage-bias check:** Hoovers keywords miss CMs that don't self-describe as co-packers. Cross-check against one directory (PartnerSlate or CPA member list, browsed manually) and add missed names.

## 3 · Stratification quotas (for ~10 completed CM interviews)

| Dimension | Quota | Rationale |
|---|---|---|
| Size | ~2 small (<$10M) · 5–6 mid ($10–150M) · ~2 large ($150M+) | Mid-market is the hypothesized buyer (Nulogy's own target band); small = WTP floor; large = benchmark |
| Ownership | ≥3 family-owned · ≥3 PE-backed | The two buying psychologies; PE = budget + mandate, family = the honest WTP test |
| Process type | ≥1 each: dry/snack/bakery · wet/sauces · beverage · frozen/refrigerated | Changeover, allergen, and QA economics differ by process, and the whitespace cells may not |
| Certification | ≥6 GFSI-certified (SQF/BRC) · 1–2 uncertified small | Certified plants carry the audit-duplication hypothesis; uncertified = contrast group |
| Geography | 3–4 drivable from Boston (in-person) · rest remote | Access stratum, not scientific — in-person plant visits yield disproportionate insight |

**Non-CM informant quotas (separate, in parallel):** 2–3 brand-side external-manufacturing/co-man managers (Aman's native persona) · 1–2 brokers/matchmakers (see RFQ flow across hundreds of CMs) · adjacent founders: Interlock, Takt, plus at least one operator who has actually used Keychain/PartnerSlate.

## 4 · Role targeting within each company

Primary: **owner / GM** (economics, WTP, software history). Opportunistic secondary per whitespace cell: QA director (audit duplication), controller/CFO (settle), plant manager (planning/changeovers). One company can yield two conversations.

## 5 · Pipeline math (why the list must be ~60, not 20)

Assumed conversion to a scheduled call: warm intro 40–60%; cold email 5–15% `[both UNVERIFIED — industry folklore; recalibrate after first wave]`. For ~10 completed CM interviews: ~15–20 warm attempts or 60–100 cold contacts; realistically a blend. **Build a ranked pipeline of ~60 companies with named contacts; work it in weekly waves of 10–15, warm paths first.**

## 6 · Prioritization score (rank within strata)

Per company: warm path exists (0–3) · fills an open quota cell (0–2) · mid-market fit (0–2) · Boston-drivable (0–2) · professionalization signal: SQF or PE-backed (0–1). Max 10. Contact top-down, but never let scoring empty a quota cell.

## 7 · Bias controls

- Marketplace-listed CMs (PartnerSlate/Keychain) skew "win-work-pain aware" — balance with SQF-sourced companies never listed on a marketplace.
- PE-backed CMs skew software-receptive — quota cap at ~half.
- Boston-drivable ≠ representative — cap in-person at ~4 of 10.
- Press-covered CMs (how the current seed list was built) skew large and successful — the Hoovers frame corrects this.

## 8 · Process once locked

1. Aman pulls the Hoovers export (recipe in `cm-outreach-playbook.md` §2) + Orbis ownership tags; commits raw CSVs to this folder.
2. Claude cleans/dedupes, enriches with SQF flags, applies quotas + scores → rebuilt `cm-outreach-list.csv` (ranked pipeline of ~60).
3. Wave 1 outreach (warm + top-scored cold), tracked in the status column; conversion rates logged after each wave to recalibrate §5.

## Open decisions (blocking the sweep)

1. **Completed-interview target:** ~10 CM interviews (this draft) vs the plan's 6–10 minimum vs more? Drives frame size.
2. **Frame source commitment:** Hoovers export by Aman (best: systematic + emails) vs Claude hand-building from public directories (slower, no emails, coverage-biased)?
3. **Category overweight:** should snacking/confectionery/coffee get extra quota given the ITC operating scar tissue (S2-IN-01's wedge was chocolate/coffee/snacking), or stay category-neutral to avoid anchoring?
4. **Large anchors:** include 1–2 (Hearthside/TreeHouse via alumni) for benchmark contrast, or pure mid-market focus?

## Review flags

- Conversion-rate assumptions in §5 are folklore, flagged `[UNVERIFIED]`, and self-correcting via wave logging.
- The population count the quotas divide over is itself a triangulation (see `cm-market-structure.md` review flags).
