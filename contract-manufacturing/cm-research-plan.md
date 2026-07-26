# US Contract Manufacturing — research plan (v2 LOCKED, 2026-07-26)

**Status: locked with Aman 2026-07-26** (merge of two drafts; Aman endorsed the CM-as-its-own-value-chain framing). Supersedes the phase list in `cm-dive-brief.md` (kept for provenance).

## Framing

Unit of analysis = **the US contract manufacturer as a business** — its own operating loop treated as the value chain, walked end-to-end. Not a vertical-wide problem sweep (the F&B failure mode: point tools, claimed territory). A candidate must clear a company-shaped bar: system of record / system of action for a slice of the CM's P&L, with wedge + expansion path.

**Scope locked:**
- **Anchor segment: food/CPG co-manufacturers & co-packers (US).** Founder edge; the S2 cluster from the F&B run was its strongest structural thread.
- **Comparison pass (~1 day): discrete job shops** — confirm or kill the hypothesis that it's already claimed territory (Paperless Parts, Takt et al.), and steal cross-segment patterns (e.g., AI quoting → co-man RFQ analog).
- **Pharma CDMO: parked** as WTP reach option.
- **"AI services" definition: open** — both software product and tech-enabled service / AI-native agency models in scope until evidence picks one; CMs historically buy outcomes more readily than seats.

## The CM operating loop (the value chain we walk)

**win work** (RFQ → quoting → tech transfer/onboarding) → **plan** (materials, customer-supplied inventory, scheduling & changeovers/allergen sequencing) → **make** (production, OEE, yield) → **prove** (QC, FSQA documentation, SQF/BRC + duplicated customer audits) → **settle** (invoicing, deductions, yield true-ups, claims).

Plus the **CM↔brand seam** explicitly — spec churn, forecast volatility, audit duplication, chargebacks — the seam Aman personally sat on from the brand side at ITC.

## Hypotheses to verify first (source gate applies)

- **H1 — Structural India↔US difference** in the number/role of contract manufacturers. `[UNVERIFIED — count of US CMs by segment vs India; outsourced share of production; direction]`
- **H2 — WTP:** US co-mans have real software paying capacity. `[UNVERIFIED — margins, current software spend per plant, what they pay for today]`
- **H3 — Startup motion = demand:** Project Prometheus, Interlock, Takt, Keychain signal heat. `[VERIFY what each sells, to whom, funding, traction; capital heat ≠ demand at the co-man segment]`

## Method note — avoiding SISP

Map where the CM's money leaks first; AI enters as a **screen after harvest**, not the starting point. Per problem: (a) does AI change the economics 10x vs the pre-2023 answer, (b) why newly possible, (c) does it survive the incumbent-adds-a-feature test?

## Phases

**P1 · Market structure & buyer economics (~1 evening)** — # US co-mans/co-packers, size distribution, revenue/margin structure, reshoring tailwind, current software stack & spend. Verifies H1/H2 with sourced ranges. → `cm-market-structure.md`

**P2 · Arena before harvest (~1 evening, the sequence inversion)** — every funded player and incumbent charted by operating-loop step *before* harvesting, so the harvest targets unclaimed cells instead of rediscovering claimed pain. Seeds: Keychain, Nulogy, Interlock, Takt, Project Prometheus, Paperless Parts, Tulip, MaintainX, Pico MES, ERPs (SAP, Epicor, Infor, Plex, Aptean). Per step: who's funded, what they charge, what's conspicuously empty and *why it might be empty*. → `cm-arena.md`

**P3 · Deep map (~2 evenings)** — per step: cost structure, % of revenue, failure modes, current tooling, 3-yr changes; seams in full. → `cm-map.md`

**P4 · Harvest + AI screen** — 30–50 problems into `inventory.csv` (IDs `CM-US-nn`), each with `nearest_funded_competitor` or `none found — searched: [queries]`, plus AI-leverage flag.

**P5 · Operator voice before scoring (the big fix from F&B)** — 6–10 Mom Test conversations *before anything enters the tracker*:
- co-man owners/GMs/plant managers via the HBS network (family-business and PE-owned co-packer connections);
- 2–3 brand-side co-man managers (Aman's native persona, easiest reach);
- coffee with the Interlock and Takt founders — adjacent-startup founders are the best whitespace informants: *what demand walks in the door that they turn away?*

**P6 · Score & converge** — EVALUATE loop per the engine; impact-first weights unless revised.

## Deliverables (this folder)

`cm-market-structure.md` (P1) · `cm-arena.md` (P2) · `cm-map.md` (P3) · inventory rows (P4) · `research-YYYY-MM-DD-topic.md` per raw sweep · interview notes (P5) · scored tracker rows (P6).

All work under the rules in `/CLAUDE.md` (source gate, ranges, no narrative-from-structure, operator-task-level problems, review flags).
