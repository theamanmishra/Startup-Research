# Data-extraction runbook — HBS databases → this repo

**Date:** 2026-07-26. For execution by Aman in the browser (HarvardKey-gated; the cloud session cannot reach these — CLAUDE.md rule 8). A local Claude Code session + Claude in Chrome may assist navigation and extraction **page by page**, but:

> **⚠ No bulk scraping.** PitchBook permanently disables accounts that automate scraping (Baker's own warning). Library licenses prohibit systematic downloading across all these databases. Use only native export buttons, report downloads, and manual lookups. Human-paced. If a task feels like crawling, stop.

Every artifact lands in `contract-manufacturing/` via upload to the cloud session or direct git commit. The cloud session then parses, reconciles, and updates the research files.

## Priority order (what → how → destination)

| # | Database | Extract | Method (native) | Destination file |
|---|---|---|---|---|
| 1 | **D&B Hoovers** | Sampling frame: US cos, NAICS 311+3121, rev $5–500M, description keywords "co-pack / co-man / contract manufactur / private label"; then contacts (Owner/President/COO/VP Ops/GM/Plant Mgr/QA Dir/CFO) | Build List → **native CSV export** | `hoovers-frame-YYYY-MM-DD.csv` |
| 2 | **Orbis** | Same companies: GUO/shareholder type (family vs PE vs corporate) | Search → add ownership columns → **native Excel export** | `orbis-ownership-YYYY-MM-DD.xlsx` |
| 3 | **AlphaSense** | 5–10 expert-call transcripts: search "co-manufacturer", "co-packer", "contract manufacturing food", "Hearthside", "TreeHouse", "Nulogy", "Keychain" | Read; clip/save relevant transcripts or paste key passages | `research-YYYY-MM-DD-alphasense-expert-calls.md` |
| 4 | **IBISWorld** | Contract-packaging or closest NAICS 311 sub-industry report(s): market size, cost structure, margins | **Native PDF download** | `ibisworld-<report>-YYYY.pdf` |
| 5 | **PitchBook** | Profiles: Takt, Semia, Allera, Interlock Systems, Keychain (funding, investors, headcount). Then one search: "contract manufacturing" software deals 2023–26 | **Manual lookups only — automation explicitly banned** | `pitchbook-arena-notes.md` (paste) |
| 6 | **Leadership Connect** | Spot-check: does it hold contacts for 3 seed-list CMs? If yes, pull contacts for frame companies missing emails in Hoovers | Search + native export if available | append to frame CSV |
| 7 | **Capital IQ / S&P Capital IQ Pro** | TreeHouse financials; M&A screen: food co-man/co-packer deals 2022–26 (the consolidation why-now) | Screener → **native Excel export** | `ciq-coman-ma-YYYY-MM-DD.xlsx` |
| 8 | **BCC Research / Technavio / RKMA / Frost & Sullivan** | Search "contract packaging", "contract manufacturing food", "co-packing" — download any real report found | Native PDF download | `<vendor>-<report>.pdf` |
| 9 | **BoardEx** *(after frame built)* | Warm paths: directors/execs of frame CMs with Harvard/HBS ties | Manual network lookups | `boardex-warm-paths.md` |
| 10 | **Revelio** *(optional)* | Headcount + role mix for 10–20 frame CMs (size-tier validation; QA/maintenance labor data) | Native export/report | `revelio-cm-workforce.csv` |
| 11 | **Prowess / Indiastat** *(H1, low priority)* | Count + size distribution of Indian food-processing/CM companies | Native export | `prowess-india-cm.xlsx` |

Also (not a database): ask a Baker librarian to purchase the **CPA 2025 State of the Industry Report**.

## Round-trip protocol

1. Aman runs items 1–5 (the 90-minute session; items 6–11 are follow-ups).
2. Files come back via **upload into the cloud session** (proven path — the 162-list xlsx worked) or `git add` + push from a local session.
3. Cloud session (Claude) then: parses exports → applies sampling quotas + scores (methodology §6) → rebuilds `cm-outreach-list.csv` as the ranked ~60-company pipeline → revises `cm-market-structure.md` and `cm-arena.md` with the better-sourced numbers → logs which `[UNVERIFIED]` flags died.

## If using a local Claude Code session with Claude in Chrome

Scope it to: navigating to the right screens, filling search filters, reading results aloud into notes, and clicking native export buttons. Give it this file as the brief. Do not let it loop over result pages harvesting rows — that is the banned pattern. PitchBook: keep Claude in Chrome away entirely; do those five lookups by hand.
