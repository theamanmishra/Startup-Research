# HBS Baker Library databases — mapped to CM-dive tasks

> **⚠ INCOMPLETE — 28 of 162.** The live A–Z list has **162 databases** (Aman, reading the page directly, 2026-07-26). This file's inventory came from a search-index sweep after the site blocked automated access and covers ~17% — biased toward well-trafficked databases. **Do not treat the inventory section as the list of what HBS has.** The task-mapping tiers below remain valid for the databases they name. Pending: Aman pastes the full 162-entry list into `hbs-databases-raw.txt`; then this file gets reconciled. (This failure is now codified as hard rule 8 in `/CLAUDE.md`.)

**Date:** 2026-07-26. Enumerated via search-indexed library.hbs.edu pages (the A–Z page itself blocks automated access). Each entry verified to exist as a Baker Library database page unless flagged. Master list: https://www.library.hbs.edu/databases-cases-and-more/databases · Baker's own F&B research guide: https://www.library.hbs.edu/Find/Guides/Food-Beverage · "Which company database to choose": https://www.library.hbs.edu/services/help-center/company-databases-which-database-to-choose

## Tier 1 — use immediately (each clears a named gap in our files)

| Database | What it is | Exact job in this dive |
|---|---|---|
| **AlphaSense** (https://www.library.hbs.edu/databases-cases-and-more/databases/alphasense) | Market intelligence + **expert-call transcript library** (buy-side investor interviews with industry operators), with GenAI search (how-to: https://www.library.hbs.edu/services/help-center/locating-expert-call-transcripts-in-alphasense) | **The single highest-value resource here.** Search expert calls: "co-manufacturer", "co-packer", "contract manufacturing food", "Hearthside", "TreeHouse", "Nulogy", "Keychain". Operators talking economics = interviews-before-interviews: margin structure, software spend, audit burden, deduction pain. Feeds P3 deep map + pressure-tests all four whitespace cells before you spend a single coffee. |
| **PitchBook** (https://www.library.hbs.edu/databases-cases-and-more/databases/pitchbook) | Private-company deals, funding, investors | Clears the arena's `[UNVERIFIED]` funding flags: **Takt** (paywalled in our sweep), Semia, Allera, Interlock; Keychain round detail; find co-man-targeting startups we missed (search verticals: "contract manufacturing", "co-packing"). Also: PE owners of CMs (who's consolidating). |
| **IBISWorld** (https://www.library.hbs.edu/databases-cases-and-more/databases/ibisworld) | US industry reports incl. **Industry Spotlight niche reports on small-business industries** | Look for a Contract Packaging / co-manufacturing specialized report → credible market size, growth, **industry-average margins and cost structure** — fixes the missing co-man EBITDA benchmark and replaces our report-mill sizing range. Also NAICS 311 sub-industry reports for per-step cost structure in P3. |
| **D&B Hoovers** (access confirmed by Aman; Baker also lists D&B private-company data) | Company screener with **named contacts + emails** | The sampling frame (recipe in `cm-outreach-playbook.md` §2). |
| **Orbis** (listed at Baker; access confirmed by Aman) | Global private-company DB with **ownership trees** | Tag frame companies family vs PE-owned vs corporate (methodology §2). |

## Tier 2 — supporting

| Database | Job here |
|---|---|
| **Capital IQ** (https://www.library.hbs.edu/databases-cases-and-more/databases/capital-iq) | Financials for the few public/debt-issuing comps (TreeHouse; PE-owned CMs with rated debt → real margin data); M&A comps for the consolidation why-now. |
| **Mergent Intellect** (help-center refs; D&B-data-based) | Backup company screener; company histories. |
| **Mintel Reports** (https://www.library.hbs.edu/databases-cases-and-more/databases/mintel-reports) + Mintel Market Sizes | Demand side: private-label and category trends pulling co-man volume. |
| **Euromonitor Passport** (https://www.library.hbs.edu/databases-cases-and-more/databases/passport) | Cross-country packaged-food data → the honest H1 India↔US comparison. |
| **EMIS** | Emerging-markets company/industry data → India side of H1 if we ever need it sourced properly. |
| **Statista** | Quick sourced stats (e.g., mfg labor shortage numbers to replace the `[re-verify]` 622k figure). |
| **Factiva / ABI-ProQuest / Business Source Complete** | Trade-press archive (Food Business News, Packaging World, Food Dive) for P3 failure-mode evidence and CM↔brand dispute stories. |
| **Bloomberg / LSEG Workspace** (on-campus) | Public comps, analyst reports on TreeHouse/private-label sector. |

## Full inventory of Baker databases verified via indexed pages (28, sweep of 2026-07-26)

**Company/private-company data:** Capital IQ · Orbis · D&B Private Company Listings · Mergent Intellect · Infogroup US Historical Business Data · FactSet · Compustat (via WRDS) · WRDS
**Startup/PE/VC:** PitchBook (+ PitchBook Datafeed dataset) · Preqin · CB Insights *(confirmed — corrects earlier "not confirmed" flag; use for arena cross-check)*
**Industry/market research:** IBISWorld · Mintel Reports · Mintel Market Sizes · Euromonitor Passport · Statista · EMIS · Frost & Sullivan *(manufacturing-tech reports — relevant)* · Gartner *(confirmed — corrects earlier flag)* · eMarketer · S&P NetAdvantage
**Intelligence/transcripts:** AlphaSense
**News/articles:** Factiva · Business Source Complete · ABI/ProQuest
**Markets/terminals:** Bloomberg · LSEG Workspace · Morningstar Direct
Baker help-center comparison pages worth reading: "Company databases: which to choose" · "VCPE Database Comparison" · "Target List: screen for companies by industry, location, and size" (https://www.library.hbs.edu/services/help-center/target-list-screen-for-companies-by-industry-location-and-size — directly relevant to the sampling frame).

**Completeness caveat:** this is what search-engine indexing exposes, NOT the authoritative A–Z list — the live page blocks automated access and archive.org is unreachable from this environment, so the true total is unknown to Claude and the list above is a floor, not a census. **Ground truth in 30 seconds:** open the A–Z page, select-all, and paste into `hbs-databases-raw.txt` in this folder; Claude will reconcile and finalize this mapping. Still unconfirmed either way: PrivCo · Tracxn · Forrester (referenced in help pages but no database page found) · Crunchbase (mentioned only as a third-party data source). Baker also purchases reports on request — ask a librarian for the CPA 2025 State of the Industry Report, the industry's primary source.

## Suggested first session in the library (90 min, in this order)

1. **AlphaSense:** expert-call search "co-manufacturer OR co-packer" → skim 5–10 transcripts; clip margin/software-spend/audit quotes into `research-2026-MM-DD-alphasense-expert-calls.md`.
2. **IBISWorld:** pull the contract-packaging/co-man report PDF → commit key pages' numbers (with report title/year as source) into `cm-market-structure.md` revisions.
3. **PitchBook:** look up Takt, Semia, Allera, Interlock, Keychain → screenshot/fill arena funding gaps; run a "contract manufacturing software" deal search for missed entrants.
4. **Hoovers:** run the frame export (playbook §2) → commit raw CSV.
5. **Orbis:** ownership batch for the export → commit.

Then hand the exports to Claude for cleaning, enrichment, quota application, and the rebuilt outreach list (methodology §8).

## Review flags

- Database availability claims rest on indexed library.hbs.edu pages, not the live A–Z list (blocked); a database could have been dropped since indexing. Verify at first login.
- Whether IBISWorld carries a co-man-specific report is an expectation, not a verified fact — flag if absent and fall back to the CPA report via librarian purchase.
