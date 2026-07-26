# HBS Baker Library databases — mapped to CM-dive tasks

**Authoritative, reconciled 2026-07-26.** Source: full A–Z export (162 databases) provided by Aman from the live page; raw list with descriptions committed as `hbs-databases-raw.csv` in this folder. This supersedes the earlier search-index partial (28 entries, ~17% coverage — that failure is codified as hard rule 8 in `/CLAUDE.md`).

## Reconciliation vs the earlier partial

- **Wrongly listed before, actually absent from Baker's list:** Mintel Market Sizes (only Mintel Reports exists) · "Mergent Fixed Income" was right but irrelevant. **PrivCo, Tracxn, Forrester: confirmed NOT at Baker** (previously "unconfirmed").
- **Previously unconfirmed, now confirmed:** Crunchbase (#40) · D&B Hoovers itself (#41, directly listed).
- **Missed entirely by the partial and relevant to this dive:** Leadership Connect · Ward's Business Directory · Revelio · BoardEx · BCC Research · Technavio · RKMA Market Research · S&P Capital IQ Pro · SDC Platinum · ProQuest TDM Studio · Prowess · EIU · Nexis Uni (see below).

## Tier 1 — use immediately (each clears a named gap in our files)

| Database | Job in this dive |
|---|---|
| **AlphaSense** (#8) | Expert-call transcripts on "co-manufacturer / co-packer / Hearthside / TreeHouse / Nulogy / Keychain" = interviews-before-interviews on margins, software spend, audit burden. Baker how-to: https://www.library.hbs.edu/services/help-center/locating-expert-call-transcripts-in-alphasense |
| **PitchBook** (#115) | Clear arena `[UNVERIFIED]` funding flags (Takt, Semia, Allera, Interlock, Keychain detail); deal search for missed co-man-software entrants. ⚠ Baker's note: automated scraping prohibited — manual lookups only. |
| **IBISWorld** (#77) | Contract-packaging / NAICS 311 sub-industry reports → credible market size + industry cost structure/margins (fixes our two weakest numbers). |
| **D&B Hoovers** (#41) | The sampling frame: NAICS 311+3121 · US · $5–500M rev · description keywords "co-pack / contract manufactur / private label" → export with contacts (recipe in `cm-outreach-playbook.md` §2). |
| **Orbis** (#109) | Ownership trees → tag frame companies family vs PE-owned (methodology §3 quota). |

## Tier 2 — supporting, by task

**Outreach & people (new finds):**
- **Leadership Connect** (#88) — background + **contact info** for US business leaders; check coverage of mid-market CM executives before buying LinkedIn InMail credits.
- **BoardEx** (#18) — board/senior-manager networks → find warm paths from HBS-connected directors into CMs.
- **Revelio** (#130) — workforce database from public profiles → headcount/role mix of private CMs (validates size tiers; sizes the QA/maintenance labor-pain hypothesis).
- **Ward's Business Directory** (#157) — 100k+ US public/private firms → frame cross-check against the Hoovers export (coverage-bias control from methodology §2).

**Industry & market reports:** BCC Research (#14) · Technavio (#147) · RKMA Market Research (#131) · Frost & Sullivan (#67) · Statista (#145) · Mintel Reports (#99 — note: in-person access currently broken per Baker) · Passport/Euromonitor (#111) · S&P NetAdvantage (#142) · EIU (#48). Try each for contract-manufacturing/private-label coverage; report titles + years go into `cm-market-structure.md` as sources.

**Financials & M&A (consolidation why-now):** Capital IQ (#25) · **S&P Capital IQ Pro** (#133) · **SDC Platinum** (#136) · FactSet (#59) · Preqin (#118 — access currently broken per Baker) · CB Insights (#27) · Crunchbase (#40) · Private Equity International (#119).

**News & text-mining:** Factiva (#58) · Nexis Uni (#106) · Business Source Complete (#22) · ABI/ProQuest (#2) · **ProQuest TDM Studio** (#123 — text-mine trade press at scale; optional P3 tool for quantifying failure-mode mentions like "chargeback", "customer audit").

**H1 India comparison (now properly doable):** **Prowess** (#124 — 40k+ Indian companies incl. private) · Indiastat (#80) · CapExdx (#23) · EMIS (#51) · States of India (#144).

**Misc. confirmed & mostly out of scope for this dive:** the remaining ~100 entries are finance/markets academic data (WRDS, CRSP, Compustat, TAQ, OptionMetrics…), region/sector news, ESG, real estate, healthcare, historical archives — full list in `hbs-databases-raw.csv`.

## Access notes from the export (as of 2026-07-26)

Preqin: HarvardKey access down · Mintel: in-person access down · Bloomberg: new-account setup down · Capital Changes: down · VitalLaw: visitor access down · PitchBook: no automated scraping.

## Suggested first library session (90 min, in order)

1. AlphaSense expert-call sweep → clip quotes into `research-2026-MM-DD-alphasense-expert-calls.md`.
2. IBISWorld contract-packaging report → numbers into `cm-market-structure.md` revision.
3. PitchBook lookups (Takt, Semia, Allera, Interlock, Keychain) → fill arena funding gaps.
4. Hoovers frame export + Orbis ownership batch → commit raw CSVs.
5. (5 min) Leadership Connect: spot-check whether it has contacts for 3 CMs from the seed list.

Also: ask a librarian to purchase the **CPA 2025 State of the Industry Report** (industry's primary source; not in any Baker database).
