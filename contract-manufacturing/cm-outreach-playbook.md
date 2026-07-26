# P5 outreach — sourcing playbook & interview targeting

**Date:** 2026-07-26. Companion to `cm-outreach-list.csv` (starter list, 20 rows). Goal: 6–10 Mom Test conversations before anything is scored.

## Sources, ranked by expected hit rate

### 1. HBS alumni directory (warm — use first)
Filter: industry *Food & Beverage / Consumer Products / Manufacturing*, titles *Owner / President / CEO / COO*, keyword search "co-pack", "contract manufactur", "private label". Also: HBS Family Business Club and Food & Agriculture Club member networks — co-packers are disproportionately family businesses, and several sit inside HBS family-business networks. A student-researcher ask ("30 min, studying how co-mans win and keep brand business, not selling anything") converts far better than any cold channel.

### 2. D&B Hoovers (you have access) — the contact-details engine
This is the tool that turns the list into named people with emails/phones. Recipe:
- **Build a list:** Location = United States · Industry = NAICS 311 (all food mfg) + 3121 (beverage) · **Keyword in business description:** `"co-pack" OR "co-man" OR "contract manufactur" OR "private label"` (the keyword filter is what isolates CMs — there is no NAICS code for contract manufacturing) · Revenue $10M–$500M · Employees 50–1,000.
- **Contacts tab:** filter titles *Owner, President, CEO, COO, VP Operations, General Manager, Plant Manager, Director of Quality, CFO/Controller* → export with email + direct phone where available.
- Expect a few hundred companies; export to CSV and append to `cm-outreach-list.csv` (keep the same columns; mark source_url = "D&B Hoovers export YYYY-MM-DD").

### 3. Orbis (you have access) — ownership structure, not contacts
Weaker on US contact data than Hoovers, but uniquely good at **ownership**: use it to tag which CMs are PE-owned vs family-owned (BvD ownership tree). PE-owned = professionalized buyer with software budget and a value-creation plan; family-owned = the WTP reality check. Same search logic: US + food NAICS/NACE codes + trade-description keywords. Export shareholder/GUO columns.

### 4. Marketplace & association directories (browse manually — they block bots)
- **PartnerSlate** (https://partnerslate.com) — ~6,000 co-mans; browsable by category after free signup.
- **CPA "Find a Co-Packer" directory** (https://www.contractpackaging.org) — members are exactly the professionalized mid-market; CPA's annual meeting is also the single densest room of interview targets in the industry.
- **Nombase** (https://www.nombase.com/companies?categorySlugs=co-packer-co-manufacturer) and **KokoQuest** directories (beverage, food, private label).
- **ensun** contract-bottling list (https://ensun.io/search/contract-bottling/united-states).

### 5. Certification databases (a proxy list nobody uses)
- **SQF certified-site database** (https://www.sqfi.com — public site search): every SQF-certified US food plant, searchable. An SQF cert ≈ "takes brand/retailer work seriously" — a strong CM proxy and a pre-qualifier for the audit-duplication interview thread.
- BRCGS directory equivalently.

### 6. State & university co-packer directories (small/regional, easy first interviews)
- Minnesota Dept of Agriculture co-packer directory (https://www.mda.state.mn.us/minnesota-co-packer-directory)
- Mass.gov co-packer list (https://www.mass.gov/info-details/co-packer-businesses) — local to HBS
- Cornell Food Venture Center kitchens/co-packers (https://cals.cornell.edu/cornell-agritech/partners-institutes/cornell-food-venture-center/kitchensco-packers)

### 7. Trade press M&A coverage (finds PE-owned CMs + the thesis behind them)
Capstone Partners food M&A updates, PrivSource food & beverage acquisitions, Packaging World contract-packaging section. Each deal announcement names a CM, its segment, and its new owner's growth thesis.

### 8. LinkedIn Sales Navigator
Company keyword `co-packer OR co-manufacturer OR "contract manufacturer"` + industry *Food Production/Beverage* + US; person titles as in Hoovers recipe. Use for the specific person after Hoovers/directories give the company.

## Who to ask for, by whitespace cell (from cm-arena.md)

| Cell to probe | Best informant | Past-behavior question (Mom Test) |
|---|---|---|
| Win-work (RFQ→quote→tech transfer) | Owner / GM / sales lead | "Walk me through the last RFQ you quoted — how long, who touched it, what did you nearly get wrong?" |
| Settle (yield true-ups, chargebacks) | CFO / Controller | "Last quarter, how many customer deductions or true-up disputes did you handle? What did the last one cost you?" |
| Audit duplication | Director of Quality | "How many customer audits did you host last year on top of SQF? What did the last one take out of your team?" |
| Planning/changeovers | Plant Manager | "How was tomorrow's schedule built today? What blew it up last time?" |
| WTP reality (H2) | Owner (family) vs CEO (PE) | "What software have you actually paid for in the last 2 years? What did you cancel?" |

Also on the docket (arena informants, not CM targets): **Interlock founder** (what is xHandle actually? site says code→requirements/audit traceability), **Takt founder** (funding, traction, and *what demand walks in that they turn away*), any **Keychain** user or employee (what does KeychainOS deploy on the manufacturer side, at what price?).

## Outreach mechanics

- Sequence: HBS warm intros → Boston-local visits (Sauces 'n Love in Lynn MA is a drive) → Hoovers cold email (student-researcher framing, 3 sentences, one specific past-behavior question, 20–30 min ask).
- Never pitch a solution; you have none yet (Mom Test rule). You are mapping how co-mans win and keep brand business.
- Log every conversation as `interview-YYYY-MM-DD-company.md` in this folder; update `cm-outreach-list.csv` status column (`not contacted → contacted → scheduled → done → notes filed`).

## Review flags

- CSV rows are compiled from third-party directories and press; locations/segments not independently verified — verify each before citing in outreach. One marked `[UNVERIFIED]` (Ready Foods HQ).
- Directory sites (PartnerSlate, gocpg.ai, Sttark, RealFoodMBA) blocked automated access; their contents were reached via search snippets only — browse manually for full lists.
- No personal emails included by design: desk sources don't reliably expose them; Hoovers is the sanctioned path to named contacts.
