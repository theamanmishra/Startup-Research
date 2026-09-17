# Shop-floor data layer — 1-day desk sprint (v2, 2026-09-17)

**Scope:** desk research only. Aman runs all calls himself; this plan produces the desk inputs that
make those calls sharp, and an interview kit. Supersedes v1's 6-sprint schedule.

## The locked board (transcribed 2026-09-17)

> **Scope header:** F&B manufacturers for shop-floor ops.
>
> **Hypothesis:** Data exists\* in shop-floors but is \*not in usable format.
>
> **~~Snowflake~~ for manu. (?)** — *(not just data storage, that's easy — Acquisition —
> Contextualization)*
> ICP: (1) SAAS companies for Manu AI  (2) Manufacturers
> **Q1** — What problem statement in f&b + shop-floor ops can be solved via new tech?
>   ↳ Study process flows of hyper-niches ↳ Study manu AI companies on what they are doing?
> **Q2** — To solve for these problems what data is req'd & in what format?
> **Q3** — Are there commonalities in the data requirements?

## The board is the canonical framework — do not substitute another

**Every source, deliverable and next step maps to a line on the board above.** Do not invent a
parallel set of questions. The mapping:

| Board line | What answers it | Status |
|---|---|---|
| **ICP ② Manufacturers** | Census SUSB 2022 firm counts by product and revenue band (~3,000–3,500 US firms at $10–100M); `../contract-manufacturing/cm-companies.csv` for names to call | Counts done; names weak (lost provenance) |
| **ICP ① SaaS cos for Manu AI** | Population count during the arena pass — tests whether it is a market at all | Not started |
| **Hypothesis, asterisk 1 (*data exists*)** | Regulation that mandates recording (21 CFR 113 retort records; 21 CFR 114 acidified; USDA FSIS) vs. contrary July evidence (60% of sub-$1B food cos on laptops and Excel; the clean-data warning) | Sources identified, conflict open |
| **Hypothesis, asterisk 2 (*not usable*)** | Contextualization gap — what it takes to join a machine signal to batch, product, line, shift | Not started |
| **Q1 — what problem can new tech solve** | (a) process flows of hyper-niches → OEM manuals, SQF/BRC clauses; (b) manu AI companies → arena pass | Not started |
| **Q2 — what data, what format** | Vendor connector docs and job postings (each competitor has already solved this for their problem); then a data column on every harvested problem | Not started |
| **Q3 — commonalities** | The convergence matrix, built from Q2's answers, plus the layer call (acquisition / contextualization / storage) | Not started |

Source grades and dependencies live in `mdl-sources.md`. Communication standard for this
workstream: **MBB-consultant-to-client** — big picture first, then structure, then detail; always
state where a piece of evidence sits in the larger scheme.

## Three things that live here, not on the board

1. **The hypothesis is two claims.** *Data exists* → if false, this is an **acquisition/sensing**
   business. *Not usable* → if true, a **contextualization** business. Test the first half first;
   repo evidence leans against it for mid-market F&B (60% of sub-$1B food companies on laptops and
   Excel; *"it requires a lot of front-end engineered clean data — a lot of people have tried away
   from it"*, former VP Supply Chain, Quality Sterling Group — both in
   `../archive/cm-document-thesis-2026-07/cm-problem-statement.md`).
2. **Q3 needs four tests, not one** — commonality is only the entry ticket. See Block 4.
3. **ICP (1) = informant, not revenue segment** until Block 1 counts how many manu-AI SaaS
   companies actually exist. `Hypothesis:` too few to be a market, and ingestion is their own
   differentiation so they build it in-house.

## Which layer are we claiming?

1. **Acquisition** — getting signal off the machine (PLC taps, retrofit sensors, cameras, protocols)
2. **Contextualization** — making a temperature trace *mean* "batch 4471, product X, line 2,
   pasteurize, shift B"
3. **Storage & access** — keeping and querying it

Snowflake was layer 3, in a world where 1 and 2 were already solved for business data. In
manufacturing 1 and 2 are **not** solved and 3 is nearly free. If the analogy holds at all the prize
is **layer 2**. Block 4 must state which layer the commonality actually sits in.

## The day — six blocks, ~8 hours

| # | Time | Work | Output |
|---|---|---|---|
| **0** | 0:30 | Lock definitions: the "new tech" date test (2026 answer must beat 2019 by ~10x — VLMs on line video, LLMs on batch records, cheap retrofit sensing, edge inference qualify; SCADA, historians, OEE dashboards, rule-based alarms do not) · scope on the co-man loop (**make** + **prove** + the plan/make seam; win-work and settle are out) · data-primitive taxonomy v0 | `mdl-definitions.md` |
| **1** | 2:00 | **Arena, read for data inputs not features.** Two layers charted separately: **DataOps** (HighByte, Litmus, AVEVA PI, Ignition, Tulip — these *are* the competition) and **application** (Augury, Redzone, SafetyChain, Semia, vision players, MaintainX — these *reveal* what data each problem needs). Per player: problem · loop step · **data inputs (signal, granularity, frequency)** · integration surface · segment served · pricing · funding. Best sources for the data column: connector/integration docs and **job postings** (an "integration engineer, Ignition/OPC-UA" listing names the exact data surface). Also: count the manu-AI SaaS population to test ICP (1). | `mdl-arena.md` |
| **2** | 2:00 | **Instrumentation reality per process archetype** — chosen by process physics, not product: **aseptic/high-speed beverage fill** (~149 firms $10–100M; most instrumented, best case for "data exists") · **kettle-cook batch wet-fill** (59 sauces + 231 frozen/prepared; batch, recipe-driven, changeover-heavy) · **dry blend → form/bake** (410 bakery + 242 snacks; weight and allergen control). Per archetype walk receive → batch → process → fill/form → pack → QC hold → ship, and for each step capture what is **metered today on a $20–100M line**, what gets recorded and where, and the failure modes. Cheapest sources: **equipment OEM manuals and spec sheets** (they state which sensors ship standard) and SQF/BRC clauses (they mandate what must be recorded). | `mdl-process-flows.md` |
| **3** | 1:30 | **Harvest 25–35 problems** into `../inventory.csv`, IDs `MDL-US-nn`, in the repo's mandatory format — *sufferer · recurring task that fails · quantified cost* — plus columns `loop_step` · `process_archetype` · `data_required` · `data_exists_today` (yes/partial/no/unknown) · `sensing_gap` · `ai_leverage` · `nearest_funded_competitor` (or `none found — searched: [queries]`). | `../inventory.csv` rows |
| **4** | 1:00 | **Convergence matrix + verdict.** Problems × primitives, then four tests: ① **Common** — do many problems share few primitives? ② **Hard** — if easy it's a feature, not a company (HighByte/Litmus already ship it); the structural reason nobody has assembled it must be *named*. ③ **Paid** — will anyone buy the layer without an outcome? (only segment ACV datapoint: FoodReady ~$18–60k/yr *including consultants*, `[UNVERIFIED]`). ④ **Pooled** — does cross-plant pooling add value? This one is **contractual, not technical**: a co-man's data is entangled with its brands' confidential specs. Verdict: platform / point-solutions / wedge-then-platform, and **which layer**. | `mdl-convergence.md` |
| **5** | 1:00 | Scored problem statements (engine §2 Step D format + rubric) → the IP deliverable. Plus an **interview kit for Aman's calls**: ranked target list by informant type, and a Mom-Test question bank per problem tied to its riskiest assumption. | `mdl-problem-statements.md`, `mdl-interview-kit.md` |

## What a 1-day version cannot deliver (stated up front, not in a footnote)

- **25–35 problems, not 30–50**, and they are **desk hypotheses** — zero operator confirmation.
  Rule 6 applies in full: nothing here is validated.
- **Per-primitive acquisition costs will be ranges or `[UNVERIFIED]`**, not sourced quotes.
- **Tests ③ and ④ can only be partially answered at desk.** Value capture needs a buyer to say what
  they'd pay; pooling rights need a co-man to say what their contracts allow. Both become call
  targets in the interview kit.
- **Process-flow depth is instrumentation-focused**, not full operations depth — enough to answer
  "what signal exists," not enough to design a product.

## Interview targets for Aman's calls (desk output, Block 5)

Ranked by information-per-minute, not by ease:

1. **Systems integrators / controls engineers** — they wire F&B plants for a living and will say
   exactly what is metered on a $40M line and what instrumenting it costs. Fastest route to the
   load-bearing half of the hypothesis. Source: CSIA member directory + "food and beverage system
   integrator" searches.
2. **Plant managers / ops directors / QA leads** at mid-market F&B co-mans — reachable off the
   1,155-firm frame in `../contract-manufacturing/cm-companies.csv`.
3. **Manu-AI founders and forward-deployed/research engineers** — ICP (1) as informants; overlaps
   Adarsh's column, so share transcripts.

## Proposed IP research question

> *What data substrate would be required to make AI usable on the mid-market food & beverage shop
> floor — and does enough of it exist today to build on?*

Falsifiable, needs primary research, useful whichever way it resolves.

## Review flags (rule 7)

- Every figure above is carried from existing repo files with original sourcing; nothing new sourced
  for this plan. Census counts exact from SUSB 2022; "60% on Excel" is report-grade, not primary.
- The three-archetype split is `Hypothesis:` — if Block 2 shows process type barely moves the data
  picture, collapse to one archetype and go deeper.
- "ICP (1) is too small to be a market" is `Hypothesis:`; Block 1 tests it by counting.
- Block 2 will lean partly on Aman's ITC line experience. That is a source of *hypotheses*, not
  evidence, and gets labeled as such — the F&B run's first failure mode was exactly this.
