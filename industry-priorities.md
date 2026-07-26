# Industry Priorities — current search space (v1: industrial & supply-chain tech)

> **What this file is:** the *industry input* to the Problem-Statement Engine — which industries/verticals to run MAP mode on, and in what order. It is **separate from the framework by design**: `problem-statement-engine.md` is industry-agnostic and never changes when the search space does; *this* file is revisable and can be extended or replaced as the search evolves (new verticals added, order reshuffled, or a different meta-sector adopted entirely).
>
> **Current scope (v1):** the intersection of frontier tech (AI/robotics) and the physical value chain — manufacturing / supply chain / commerce. Everything below documents this space and ranks its verticals by founder edge.
>
> **Other project docs:** `problem-statement-engine.md` = the agnostic process (MAP → EVALUATE). `founder-profile.md` = edges, the evaluation filter. `shortlist-tracker.xlsx` = scored candidate log. One **Industry Map** doc per mapped vertical (produced by MAP mode).

---

## How the space is classified — and why "manufacturing + supply chain" isn't one industry

**Formal taxonomies split it across sectors:**
- **NAICS** (the US government's production-based system): **Manufacturing = sectors 31–33**; **Transportation & Warehousing = sectors 48–49**; with **Wholesale Trade (42)** and **Retail Trade (44–45)** sitting in between. So the physical value chain — *make → move/store → sell* — literally spans four different top-level sectors. Manufacturing and supply-chain/logistics are **separate** here.
- **GICS** (the MSCI/S&P system investors use for public stocks): groups **Capital Goods (manufacturing/machinery) + Transportation** together under one **Industrials** sector. So the *investor* lens puts them under **one umbrella** ("Industrials").

**VCs ignore both and use thesis-driven umbrellas** that deliberately cut across the formal sectors:
- **"Supply chain & logistics tech"** (PitchBook, CB Insights, Sapphire): segmented into visibility/asset-tracking, planning & decision intelligence, procurement & sourcing, freight/transportation management, warehouse automation, last-mile, supply-chain finance & payments, plus vertical slices like **food supply chain** and **cold chain**.
- **"Industrial tech" / "Manufacturing 4.0"**: IoT, AI, robotics, MES, predictive maintenance, vision-based quality — the digitization of the factory floor.
- **a16z "American Dynamism"**: explicitly bundles *supply chain + industrials + manufacturing* (alongside defense, energy, aerospace) into **one practice**. The connective thesis is reindustrialization / reshoring and "software eating the physical world" — AI and robotics moving into gritty legacy industries. *(It's framed around US national interest, so treat it as a lens for the US, not a literal fit for India.)*
- **Specialist funds whose theses literally define your space** — good research sources and eventual investor targets: **Schematic Ventures** (supply chain, manufacturing, commerce), **Eclipse Ventures** (industrial/physical economy), **Cambridge Capital** (supply chain), **Prologis Ventures** (logistics).

**Takeaway:** your intersection is best named **"industrial & supply-chain tech"** — the physical-economy / software-eating-atoms wave. It is a *meta-category*, not a single industry, so the job is to keep carving it into lanes small enough to deep-dive in a week.

---

## Where the boundary sits — physical value chain, not just "supply chain"

"Supply chain" has a narrow and a broad meaning, which is why *make → move → sell* can *feel* like simply "supply chain":
- **Narrow (everyday sense):** moving and storing goods — logistics, freight, warehousing, inventory. Just the *move*.
- **Broad (the SCOR model practitioners use):** *Plan → Source → Make → Deliver → Return* — here manufacturing sits *inside* supply chain as the production node. By this reading, make → move → sell is almost exactly "supply chain, broadly defined."

The "almost" is deliberate: your frame is a little *wider* than even the broad definition, at both ends —
- **Make end:** supply chain treats production only as a *flow* node (how much, when — sequenced to demand). It excludes the *engineering* of production: automation, machine maintenance, vision QC, process design. That's **manufacturing tech / Industry 4.0**, a distinct domain. *(Your GE predictive-maintenance and ITC manufacturing-cost work lives here.)*
- **Sell end:** supply chain stops at delivery/fulfilment. The actual *selling* — demand generation, pricing, retail merchandising, the transaction — is **commerce / retail**. *(Your CPG distribution and retail-execution edge straddles this line.)*

So the clean mental model is **three overlapping domains**: supply chain is the end-to-end operational *spine*; manufacturing tech and commerce/retail are the two *end-caps* you keep deliberately in scope. Formally, what you've drawn is closer to Porter's **value chain** (which explicitly includes marketing & sales) than to "supply chain" (its operations-heavy core). That wider boundary matters because two of your five sharpest edges — **manufacturing ops** and **CPG distribution** — sit in exactly the end-zones a pure "supply chain" scope would clip off. Scoping the search as "supply chain" alone would quietly discard a third of your edge.

```
   ◄──────────────── THE PHYSICAL VALUE CHAIN ────────────────►
                make ───────► move ───────► sell

   ┌── MANUFACTURING TECH ──┐                ┌── COMMERCE / RETAIL ──┐
   │ automation · vision QC │                │ demand · pricing ·    │
   │ maintenance · process  │                │ merchandising · POS   │
   └───────────┬────────────┘                └───────────┬───────────┘
               │  overlap                       overlap   │
   ┌───────────┴──────────────────────────────────────────┴───────────┐
   │                          SUPPLY CHAIN                             │
   │             plan · source · make · deliver · return               │
   │                 (the end-to-end operational spine)                │
   └───────────────────────────────────────────────────────────────────┘
```

**Working definition:** the outer boundary of your search is the **physical value chain (make → move → sell)** — with **supply chain as its operational spine**, and **manufacturing tech + CPG/commerce as the two in-scope end-caps.** The lanes below are organized along this spine.

---

## The spine: make → move → sell (+ enabling layers)

Each lane below is roughly one week's deep-dive. ★ = where your edge plausibly clears the "1-in-10" bar.

**MAKE (manufacturing / industrial)**
- **Manufacturing ops & Industry 4.0** ★ — MES, OEE, quality/vision, predictive maintenance. *(Your ITC manufacturing + GE predictive-maintenance work.)*
- **Industrial robotics & automation** — physical automation on the line, cobots, pick-and-place. *(Frontier-robotics angle; edge medium.)*
- **Procurement & sourcing** ★ — supplier discovery, spend analytics, should-cost modeling. *(Your sourcing + cost-optimization muscle.)*

**MOVE (supply chain / logistics)**
- **Cold chain & perishables** ★★ — reefer, storage, last-mile for temperature-sensitive goods. *(Your sharpest, rarest edge.)*
- **Supply-chain planning & decision intelligence** ★ — demand forecasting, inventory optimization, control towers. *(Your forecast-free replenishment work; strongest AI fit.)*
- **Freight & transportation management** — TMS, freight matching, in-transit visibility. *(Your logistics-redesign + co-loading edge.)*
- **Warehousing & fulfillment** — WMS, warehouse robotics, inventory accuracy. *(Your 42-warehouse, 40→80% fulfilment edge.)*

**SELL (distribution / CPG-facing)**
- **CPG/FMCG distribution & retail execution** ★ — distributor management, secondary-sales visibility, general-trade / kirana stack. *(Your ITC distribution core; you know this buyer cold.)*
- **Food supply chain, traceability & safety** ★ — farm-to-shelf provenance, compliance, waste reduction. *(Your QR+blockchain traceability, −30% expiries.)*

**ENABLING (cross-cutting)**
- **Visibility & IoT sensing** — condition monitoring, tracking hardware + data layer.
- **Supply-chain finance & trade compliance** — payments, financing, customs/trade docs. *(Weaker edge; adjacent.)*

---

## The second axis — the end-market vertical

The lanes above are the *horizontal* axis (functions). But the same function is a different business depending on the **vertical** — the industry the goods belong to. Cold chain for ice cream and cold chain for vaccines share a name and almost nothing else: different regulation, value density, buyer, and failure cost. So the real search space is a **grid — function × vertical — and a deep-dive unit is a *cell*, not a whole row.**

**Why the vertical matters as much as the function:** it sets three of your rubric dimensions almost by itself —
- **Willingness to pay / value density** — a spoiled truck of produce costs thousands; a spoiled batch of biologics costs millions. Pharma pays; food scrapes.
- **Why-now (regulation is vertical-specific)** — the forcing functions live in the vertical, not the function: food-traceability mandates (e.g. FSMA 204) vs pharma serialization / cold-chain rules (e.g. DSCSA, GDP-compliant storage). *(Verify current deadlines at deep-dive time.)*
- **Market structure** — food/agri is fragmented and thin-margin; pharma is concentrated and high-margin; heavy industrial is few-large-accounts.

**Verticals, ranked by your edge:**
- **Tier 1 — deepest edge:** *Food & Beverage / CPG / FMCG* (your home turf); *Fresh produce, dairy, meat & agri* (perishables, where your cold-chain/traceability edge is sharpest).
- **Tier 2 — cold-chain skill transfers, high value & regulation:** *Pharma & Life Sciences* (biologics, vaccines, diagnostics, med devices). Strong willingness to pay and hard mandates — but your regulatory/domain depth here is shallower than in food, so the edge is the *logistics* skill, not the pharma knowledge.
- **Tier 3 — physical value chain is central but your edge is thin:** *Electronics / hardware, Automotive & industrial equipment, Chemicals / process, Apparel*. Enter only if a specific problem's why-now is overwhelming.

**Heat matrix — where function × vertical is hottest for you** (★ strong edge · ○ transfers · · thin):

| Function ↓ / Vertical → | Food & Bev / CPG | Fresh & Agri | Pharma / Life-sci | Heavy industrial |
|---|:---:|:---:|:---:|:---:|
| Cold chain & perishables | ★ | ★ | ○ | · |
| Planning & decision intelligence | ★ | ○ | ○ | · |
| Traceability & safety/compliance | ★ | ★ | ○ | · |
| CPG distribution & retail execution | ★ | ○ | · | · |
| Manufacturing ops & Industry 4.0 | ★ | ○ | · | ○ |
| Procurement & sourcing | ○ | ○ | ○ | · |

The concentration of ★s is unmistakable: your search should live in the **top-left block** — the perishable-consumer/agri columns crossed with the cold-chain, planning, traceability, distribution, and manufacturing-ops rows. Pharma is the one worthwhile *reach* column: lower domain edge, but the willingness-to-pay and mandatory why-now can be strong enough to compensate.

---

## Where your edge concentrates

The hottest **cells** (not just lanes) are: cold chain × food/perishables, cold chain × pharma (reach), planning × CPG, traceability × food & pharma, manufacturing ops × F&B. These are where "1-in-10 founder" and "AI/robotics × physical domain" overlap. Bias the running order here; treat thin-edge cells as later-week or park.

---

## How this plugs into the engine (MAP → EVALUATE)

This doc's job is to tell you **which verticals to map, in what order.** The engine (`problem-statement-engine.md`) then runs in two modes:

1. **MAP mode (one-time per vertical, ~2–4 days):** take one vertical (a *column* of the heat matrix) and walk it end-to-end across make → move → sell — cost structure, margin pools, power, players, what changed, pains per step, plus the *seams between* steps. Harvest **30–50 problems**, each tagged with step + cell. A single lane yields a thin list; a full vertical yields a rich one.
2. **EVALUATE mode (weekly):** pull a batch (usually one dense cell) from that problem list → triage → seven-block deep-dive → edge filter → score → weekend interviews → tracker.

**Vertical mapping order** (by edge concentration; revise as maps complete):
1. **Food & Beverage / CPG** — home turf; densest ★ row-coverage.
2. **Fresh produce & Agri** — sharpest cold-chain/traceability overlap.
3. **Pharma / Life Sciences** — reach: thinner domain edge, but high willingness-to-pay and hard regulatory why-nows.
4. Heavy industrial — only if a specific problem's why-now is overwhelming.

**Geography declared per map** (India / US / both) — it changes structure, regulation, and the problem set.
