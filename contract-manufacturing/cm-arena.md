# P2 — Arena map: who is funded, by operating-loop step

**Date:** 2026-07-26 (v1 — desk sweep; refine with founder coffees in P5). Chart before harvest, per plan. Steps: **win work → plan → make → prove → settle**, plus cross-step platforms.

## WIN WORK (RFQ → quoting → tech transfer/onboarding)

| Player | What (searched evidence) | Funding/scale | Source |
|---|---|---|---|
| **Keychain** | Brand/retailer↔manufacturer matching; expanding into **KeychainOS**, an "AI operating system" explicitly positioned to *replace or integrate with legacy ERP* for CPG manufacturers. Claims 30k manufacturers, 20k brands, $1B/mo project flow; customers incl. 7-Eleven, Whole Foods, General Mills. | **$68M total; $30M Series B (Aug 2025, Wellington)** | https://www.prnewswire.com/news-releases/keychain-raises-30-million-series-b-and-launches-keychainos-an-ai-operating-system-set-to-power-the-future-of-cpg-manufacturing-302532859.html |
| **PartnerSlate** | Marketplace: brands post projects, matched to ~6,000 co-mans; $199/project + 2% of first-year production value. | **$4M seed (2023)** | https://www.foodnavigator-usa.com/Article/2023/06/12/PartnerSlate-connects-food-brands-with-co-manufacturers-raises-4-million-in-funding/ |
| *(job-shop analog)* **Paperless Parts** | AI quoting for machine shops — geometry interrogation, "Wingman" AI extracting quote-package data; claims 90% quote-setup time cut. | **$30M Series B + Hexagon partnership** | https://www.paperlessparts.com/press/paperless-parts-cuts-quote-setup-time-by-90-with-new-ai-supported-workflow/, https://hexagon.com/company/newsroom/press-releases/2024/hexagon-and-paperless-parts-slash-quoting-times-for-americas-precision-manufacturers-with-advanced-software-solutions |

**Cell read:** brand-side discovery is claimed twice over (Keychain at scale, PartnerSlate cheap). But everything found sells the *brand's* search problem. The **CM-side of win-work** — responding to RFQs, costing/quoting a formulation run, tech-transfer/onboarding execution after the match — has no dedicated funded player found this sweep. `none found — searched: "co-manufacturer RFQ quoting software food CPG", "AI food manufacturing software 2025 funding"`. **Hypothesis:** empty because Keychain intends to own it from the marketplace side (KeychainOS), and because co-man quoting is spreadsheet+tribal knowledge with a fragmented, low-ACV buyer. Kill-test: what does Keychain actually charge/deploy on the manufacturer side today? (Founder-coffee question; also demo KeychainOS.)

## PLAN (materials, customer-supplied inventory, scheduling, changeovers/allergen sequencing)

| Player | What | Funding/scale | Source |
|---|---|---|---|
| **Semia** | "AI employee" for F&B production planning — reads orders/stock/attendance/machine status, drafts next-day schedule with allergen/FEFO sequencing for a human to approve; targets mid-size plants that outgrew Excel but won't buy APS. | Funding not found — appears early/seed `[UNVERIFIED]` | https://semia.ai/food-production-planning-software |
| **PlanetTogether** (incumbent APS) | F&B scheduling with allergen/sanitation constraints. | — | https://www.planettogether.com/aps-software-for-food-beverage |
| Enterprise APS: o9, Blue Yonder, RELEX | Serve large manufacturers, not mid-market co-mans (carried from F&B run, S2-IN-04). | — | fnb record |

**Cell read:** the exact "AI scheduler for mid-size F&B plant" wedge already has at least one entrant (Semia) plus APS incumbents. Not empty — but nobody found is co-man-*specific* (customer-supplied inventory, multi-brand changeover economics, short-run SKU churn). `[Hypothesis: co-man planning ≠ brand-plant planning; would need operator confirmation that the difference is painful enough to buy on]`

## MAKE (production execution, OEE, yield)

| Player | What | Funding/scale | Source |
|---|---|---|---|
| **Tulip** | Frontline-ops/MES app platform; AI push. | **$291M total; $120M Series D at $1.3B (Jan 2026)** | https://www.media.mit.edu/posts/tulip-raises-120m-series-d-at-1-3b-valuation-to-scale-ai-for-frontline-manufacturing/ |
| **MaintainX** | CMMS/EAM, mobile-first, AI maintenance; 11k+ customers incl. F&B. | **$254M total; $150M Series D at $2.5B (Jul 2025)** | https://www.getmaintainx.com/newsroom/maintainx-raises-150m |
| **Pico MES** | No-code MES for assembly environments. | — | https://www.picomes.com/comparisons/picomes-vs-tulip-interfaces |
| **Takt** (SF, 2025) | "Manufacturing intelligence": aggregates machine/process data, dashboards, natural-language queries, digitizes paper workflows. Funding not public. `[UNVERIFIED — PitchBook paywalled; ask founder directly]` | — | https://pitchbook.com/profiles/company/1232311-42, https://tracxn.com/d/companies/takt/__xTx3Ufq_pn_5RshC41f0dHjGAHu2xo6eSGfPw4Sg81o |
| Augury (PdM), Formic (RaaS), Chef Robotics | Carried from F&B run — machine health & automation claimed. | — | fnb record |

**Cell read:** the most heavily funded step by far — horizontal players at $1B+ valuations. Anything here must answer "why not Tulip/MaintainX + a feature." Claimed territory unless a co-man-specific angle survives (e.g., per-run yield true-up against the brand contract — which is really a *settle* problem surfacing on the floor).

## PROVE (QC, FSQA docs, SQF/BRC certification, duplicated customer audits)

| Player | What | Funding/scale | Source |
|---|---|---|---|
| **Allera** | AI-powered FSQA: digital forms, doc control, supplier mgmt, audit readiness (FSMA/SQF/BRCGS); claims 500+ F&B manufacturer customers. Funding not found `[UNVERIFIED]` | — | https://www.alleratech.com/ |
| **TraceGains** | Supplier/ingredient compliance network (upstream docs). | established | fnb record; https://tracegains.com/blog/co-manufacturers-ride-private-label-sales-wave/ |
| FoodLogiQ, Safefood 360, audit firms (SGS, TÜV, NSF) | Point-in-time audit & compliance infrastructure. | — | https://www.alleratech.com/blog/food-safety-software |

**Cell read:** FSQA digitization is being claimed (Allera et al. + FSMA 204 tailwind). What was **not found**: anything attacking **audit duplication across brand customers** — a co-man running N brands endures N overlapping customer audits + SQF/BRC; the F&B run found the same gap in India (S2-IN-05: continuous verification vs periodic audits). `none found — searched: "AI startup food manufacturing quality FSQA compliance 2025 2026 funding"`. **Hypothesis:** empty because the trust boundary is hard — brands don't accept each other's audits; GFSI schemes were supposed to fix this and only partially did. This is a seam problem (CM↔brand), the kind desk research undersells. Interview target.

## SETTLE (invoicing, deductions, yield true-ups, claims/chargebacks)

| Player | What | Funding/scale | Source |
|---|---|---|---|
| **Glimpse** | AI deduction recovery for CPG **brands** vs retailers — autonomous agents, full revenue workflow; 200+ brands. | **$35M Series A (a16z)** | https://www.tamradar.com/funding-rounds/glimpse-series-a-35m, https://www.tryglimpse.com/ |
| **SupplyPike** | Retailer-deduction disputing for vendors. | established | https://supplierwiki.supplypike.com/articles/trade-deductions-and-chargebacks |

**Cell read:** deductions AI is proven and funded — **but only on the brand↔retailer edge**. The **CM↔brand settle edge** (yield true-ups, materials reconciliation on customer-supplied inventory, quality chargebacks flowing from brand to co-man) has no player found. `none found — searched: "CPG deductions chargebacks software SupplyPike Glimpse", "co-manufacturer settlement software"`. **Hypothesis:** structurally analogous to Glimpse's wedge one hop up the chain; empty possibly because each co-man's disputes are smaller and idiosyncratic per contract. Aman sat on the brand side of exactly this seam at ITC. Strong interview target.

## CROSS-STEP (ERP / system of record)

Deacom (ECI) — explicitly sells to co-packers/contract manufacturers; Aptean Food & Beverage; Plex; Infor; SAP; NetSuite; Wherefour (https://www.ecisolutions.com/industries/manufacturing/erp-software-for-contract-manufacturing/, https://wherefour.com/best-food-beverage-manufacturing-erp-software/). **Nulogy** is the co-pack-specific incumbent: 20+ yrs, shop-floor + brand-collaboration network (Unilever, Kraft Heinz, Colgate use it to see into their co-pack network), contracts ~$80k–250k/yr brand-side (https://nulogy.com/industries/contract-packaging-manufacturing/, https://logicatalog.com/vendors/nulogy/). **Keychain's KeychainOS is aimed squarely at this layer.**

## Named seeds that turned out NOT to be in this arena

- **Project Prometheus (Bezos):** "artificial general engineer" — AI for design-to-manufacturing in aerospace/semiconductors/automotive; $12B raised at $41B valuation (Jun 2026). Signals capital heat in AI×manufacturing, but a different buyer entirely. (https://www.axios.com/2026/06/11/prometheus-bezos-industrial-ai, https://www.geekwire.com/2026/bezos-ai-startup-prometheus-raises-12b-at-41b-valuation-and-the-ceos-explain-what-theyre-doing/)
- **Interlock Systems (interlocksystems.io):** site blocks automated access; search snippet describes "xHandle — architecture, risks, requirements generated from code, audit-ready" → reads as dev-workflow/compliance tooling for regulated software, not co-man ops. `[UNVERIFIED — resolve at founder coffee]`

## Job-shop comparison verdict (the 1-day pass, abbreviated)

Quoting (Paperless Parts + Hexagon), shop management, and MES are all claimed in discrete job shops by funded players — confirming the plan's hypothesis that the job-shop segment is **claimed territory**, and validating the *pattern* (AI on quote-package → quote) as transferable. Food co-man remains the better anchor: same pattern, unclaimed cell, founder edge.

## Where the desk map says the whitespace is (to be distrusted until interviews)

1. **CM-side win-work** (RFQ response/costing/tech-transfer execution) — vs Keychain expansion risk.
2. **CM↔brand settle** (yield true-ups, chargebacks, customer-supplied-inventory reconciliation) — Glimpse-for-co-mans analog.
3. **Audit duplication across brand customers** — seam/trust problem, hardest and least claimed.
4. Co-man-specific planning (multi-brand changeover economics) — partially claimed by Semia/APS from the generic side.

Per CLAUDE.md known-failure-modes: this is **whitespace-by-elimination** — "least crowded," not "most demanded." P5 interviews decide.

## Review flags (rule 7)

- Semia, Allera, Takt funding: not found, marked `[UNVERIFIED]` rather than assumed small.
- Keychain's 30k-manufacturer and $1B/mo figures are company PR claims, not audited.
- All four "empty cells" are inferences from search absence; each carries its search queries and a why-empty *hypothesis*, not a fact claim.
- Interlock characterization rests on a single search snippet; site 403'd.
