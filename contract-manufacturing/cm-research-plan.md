# US Contract Manufacturing — research plan (DRAFT v1, 2026-07-26)

**Status: draft — pending refinement with Aman before research starts.** Supersedes the phase list in `cm-dive-brief.md` once agreed (brief kept for provenance).

## Why this dive, and why differently

The F&B run produced point tools and dashboards, not companies — the record itself concedes it ("top survivors read as modules/dashboards, not companies"). Diagnosis: a problem-list-first desk sweep across a whole vertical surfaces publicly quantified pain (= already-claimed territory) and scores fragments, not businesses.

This dive inverts the unit of analysis: **one customer type — the US contract manufacturer — understood as a business**, then ask where AI collapses a real cost line or creates revenue for that customer. A candidate must clear a company-shaped bar: could this be the *system of record / system of action* for some slice of the CM's P&L, with a wedge and an expansion path — not "a dashboard the ops manager glances at."

## Hypotheses to verify before anything else (source gate applies)

These are Aman's framing inputs — treated as hypotheses, not facts:

- **H1 — Structural difference India↔US:** the two markets differ materially in the number / role of contract manufacturers. `[UNVERIFIED — pin down: count of US CMs by segment vs India; outsourced share of production; direction of the difference]`
- **H2 — WTP:** US CMs have real software paying capacity vs Indian CMs. `[UNVERIFIED — need US co-man gross/EBITDA margins, current software spend per plant, examples of what they pay for today]`
- **H3 — Motion in the space = validated demand:** Project Prometheus (Bezos), interlock-systems.io, Takt, Keychain etc. signal heat. `[VERIFY: what each actually sells, to which CM segment, funding, traction. Note: capital heat ≠ demand at *your* target segment — Prometheus-type plays may target aerospace/deep-tech engineering, not mid-market co-mans]`

## The segment fork (decide before research)

"US contract manufacturer" is four different businesses. Anchor choice drives everything:

| Segment | What they make | Founder edge | Known startup heat |
|---|---|---|---|
| **Food/CPG co-manufacturers & co-packers** | Brands' food products; SQF/BRC world | ★★ (home turf) | Keychain, Nulogy |
| **Discrete job shops / precision machining** | CNC, sheet metal, aerospace parts | · | Paperless Parts, Takt?, Prometheus-adjacent |
| **Electronics (EMS/PCBA)** | Boards, assemblies | · | mature (Jabil→small shops) |
| **Pharma CDMO** | Drugs, biologics | ○ (regulated-ops transfers) | parked as reach |

Default recommendation (from brief): **anchor on food/CPG co-mans, with a 1-day comparison pass on discrete job shops** to steal cross-segment patterns (e.g., AI quoting worked in job shops — does the analog exist in co-man RFQs?).

## Method note — avoiding SISP

"What can I sell CMs using AI?" is solution-first. The engine's discipline still holds: map where the CM's money leaks first. AI enters as a **screen applied after harvest**: for each problem, (a) does AI change the economics 10x vs the pre-2023 answer, (b) why is it newly possible, (c) does it survive the incumbent-adds-a-feature test? Problems that fail the AI screen stay in inventory but are flagged.

## Phases

**P0 · Scope lock (with Aman)** — anchor segment; geography US-only vs US+comparison; define "AI services" (software product only, or tech-enabled service / AI-native agency models also in scope — CMs buy outcomes more readily than seats).

**P1 · Market structure & buyer economics (~1 evening)** — # of US CMs in anchor segment, size distribution, revenue/margin structure, reshoring/China-plus-one tailwind, what software they run today (ERP penetration, spend levels). Verifies H1/H2 with sourced ranges.

**P2 · Arena before harvest (~1 evening)** — funded players mapped to the CM operating loop **before** harvesting problems: win work (RFQ→quote→tech transfer) · plan (materials, customer-supplied inventory, scheduling/changeovers) · make (production, OEE, yield) · prove (QC, FSQA docs, certifications, customer audits) · settle (invoicing, deductions, yield true-ups, chargebacks). Seeds: Keychain, Nulogy, Interlock, Takt, Project Prometheus, Paperless Parts, Tulip, MaintainX, Pico MES, ERPs (SAP, Epicor, Infor, Plex, Aptean). Output: `cm-arena.md` — per step: who's funded, what they charge, what's conspicuously empty, and *why* it might be empty.

**P3 · Deep map of the CM operating loop (~2 evenings)** — per step: cost structure, % of revenue, failure modes, current tooling, 3-yr changes. Explicit attention to the **CM↔brand seam** (spec churn, forecast volatility, audit duplication, chargebacks) — seams were the richest F&B findings. Each pain logged operator-task-level with source or `[UNVERIFIED]`.

**P4 · Harvest + AI screen** — 30–50 problems into `inventory.csv` (IDs `CM-US-nn`), every row with `nearest_funded_competitor` or `none found — searched: [queries]`, plus the AI-leverage flag.

**P5 · Operator voice before scoring** — 6–10 Mom Test conversations (co-man owners/GMs/plant managers; 2–3 brand-side co-man managers; the Interlock and Takt founders Aman knows are *primary sources on the arena*, not competitors to avoid). Nothing is scored into `tracker.csv` before this.

**P6 · Score & converge** — EVALUATE loop per the engine; impact-first weights unless revised; verdicts recorded here.

## Deliverables (all in this folder)

`cm-market-structure.md` (P1) · `cm-arena.md` (P2) · `cm-map.md` (P3) · inventory rows (P4) · `research-YYYY-MM-DD-topic.md` per raw sweep · interview notes (P5) · scored tracker rows (P6).

## Open questions for Aman (refine before P1)

1. Anchor segment — food/CPG co-mans (edge) vs discrete job shops (heat) vs run the 1-day comparison first and then lock?
2. Are tech-enabled services / AI-native agency models in scope, or software product only?
3. Interview access — can you open doors to the Interlock/Takt founders and 2–3 co-man operators early? If yes, P5 conversations can start in parallel with P2–P3 instead of after.
