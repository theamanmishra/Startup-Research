# Problem statement — US food co-manufacturing (v1, 2026-07-28)

Written in the format required by `problem-statement-engine.md` §2 Step D. Built from four
AlphaSense reports (operator voice), the arena map, and market structure work. Evidence markers:
**[E]** operator- or filing-sourced · **[E-weak]** industry-source, not a plant operator ·
**[H]** hypothesis from structure · **[?]** unknown, interview target.

---

## The statement

> For **QA and operations leaders at US food co-manufacturers of $10–250M revenue** trying to
> **keep every brand customer's compliance paperwork current**, the problem is that **the same
> facts have to be re-entered in a different shape for every customer, every audit, and every spec
> change** — today they cope with **Excel and email**, costing **`[?]` hours per week (not yet
> quantified) and months of delay on new launches**. Newly solvable because **language models can
> now read arbitrary document formats reliably, and format variety is exactly what defeated rigid
> integrations**. I have an unfair right to win because **I ran the brand side of co-manufacturer
> relationships at ITC and can build the software myself**. The wedge is **audit and certification
> documentation** — weekly work, done in a spreadsheet today, where a wrong answer is caught by a
> human before an auditor ever sees it.

---

## The proof

### The work is real and contractual

**[E]** Hain Celestial 10-K (15 Sep 2025) — what co-packers must supply, continuously:
> "…technical assessments, including **questionnaires, scientific data, certifications, affidavits, certificates of analysis and analytical testing**, where required."

**[E]** Gehl Foods supplier terms (Feb 2026) — and the brand can change the rules at will:
> "Provider shall comply with Customer's supplier qualification/compliance program **as it exists from time to time**…"

### The tool today is a spreadsheet

**[E]** Director of EHS, Shehadey Family Foods (expert call, 25 Dec 2025):
> "We currently have a food certification called SQF. It requires us to have certain inspections, audits, other documentation on a **monthly and weekly basis** completed within the facility. **Right now, it's done just through an Excel.**"

**[E]** Former Director of Product Management, Xometry (expert call, 20 Jul 2026), on quoting and costing workflows:
> "If the trope is paper and pencil, it's not. **It's email and spreadsheets.**"

**[E]** Report finding: **60% of sub-$1B food companies run on laptops and Excel**; deployed ERPs are described as a "necessary evil" lacking real-time production tracking.

### Serving more customers multiplies the work

**[E-weak]** (AlphaSense synthesis + FMCG contract manufacturer prospectus, 30 Jun 2026):
> "When a co-manufacturer scales their business by taking on multiple unique brand customers, **the administrative burden does not scale linearly; it multiplies**. Because there is **no industry standardization**, every brand brings its own unique formulations, custom quality questionnaires, and private label packaging requirements, which **forces the co-packer's administrative team to run highly fragmented processes for each account**."

This is the spine of the thesis and it is the weakest link in the evidence chain: stated by an
industry source, not yet by a plant operator. **Interview question one.**

### The delay is expensive

**[E]** Mi3 Limited (filing, 22 Jul 2024): a launch slipped from 2023 to 2024 "partly by our
customers **due to documentation burden** and resource restraints."
**[E]** Onboarding runs 6–18 months; GFSI scheme onboarding "typically takes a year" (Upfield did
one site in 90 days with cross-functional effort).
**[E]** FoodReady (14 Apr 2026): bridging food-safety regulation into production workflows
"previously required expensive custom solutions **or additional staff**."

### An operator asks for exactly this

**[E]** Director, Trans America (expert call, 29 Dec 2025):
> "Really, anything that deals with being able to eliminate workflow and simplify the process, **you're trying to see ways that AI can come in and eliminate a lot of that manual effort that goes into the data entry component of it**."

### Digitizing it has a measured result

**[E]** Tasty Bite Eatables (annual report, 22 Jul 2026):
> "we sustained **First Time Right (FTR) quality scores of over 99%**, driven by the **digitisation of change control** and continuous improvement processes."

**[E]** Grape King Bio (2025 ESG report): quote processing **2.4 → 1.5 days (37.5%)**; formula-to-BOM
conversion automated to one click, **~50% time reduction**.

**[E]** Bega Cheese (Investor Day, 28 Apr 2026): 11 RPA bots in back office, headcount **120 → 70**.

---

## How AI solves it

Four jobs. Each is document-in or document-out, which is what current models do well.

**1. Read any inbound format and map it onto the plant's own structure.**
Brand specs, formulas, ingredient sheets, and portal exports arrive as PDFs, Word files, and
spreadsheets, all differently shaped. The variety is the problem, and variety is precisely what
defeats rigid integrations and suits language models.

**2. Answer customer questionnaires from documents the plant already holds.**
The answers exist — in the food-safety plan, the certification records, prior questionnaires. The
work is finding and reshaping them, not knowing them. Retrieval plus generation.

**3. Keep the audit record continuously instead of assembling it under pressure.**
SQF and BRC need weekly and monthly evidence. A system that files each record as it is created,
and can answer "show me the evidence for clause X," replaces the pre-audit scramble.

**4. Diff a spec change and list what it touches.**
When a brand changes an ingredient or a label, compare old to new and enumerate the affected BOM
lines, batch records, labels, and packaging stock.

**Order of attack is set by the cost of being wrong, not by the size of the prize:**
- Wrong questionnaire answer → a human corrects it. Harmless.
- Wrong item master → a bad production run. Expensive.
- Wrong COA → a legal document with a customer's name on it. Serious.

So start at audit documentation and questionnaires, earn trust, and only then touch specs.

---

## What is still unknown

| Question | Status |
|---|---|
| Hours per week spent on this | **[?]** never quantified in any report |
| What a plant would pay | **[?]** no software pricing found for this segment |
| Does the multiplication effect hold at plant level | **[E-weak]** industry-sourced only |
| Do SafetyChain, Specright, FoodReady already cover it | **[?]** next arena task |
| Does the plant's data exist to work with | **[E]** flagged as the main failure mode: "it requires a lot of front-end engineered clean data. A lot of people have tried away from it" |

---

## What has been ruled out

- **Checking incoming COAs.** **[E]** VP Technical Services, IEH Laboratories: "If there's 30 COAs, they'll have to spend **10 minutes** looking at them." Twenty seconds each. Not a business.
- **Producing lot COAs.** **[E]** Tridge: "The cost of compliance shows up as **lab capacity, hold time, and occasional lot segregation** — not just as 'paperwork'." Software does not shorten a lab queue.
- Price lag on conversion fees, deferred maintenance, take-or-pay design — real pains, not software problems.

---

## Known competition

| Player | What | Gap |
|---|---|---|
| **SafetyChain** | Food safety and quality management | **[E]** user at MaryAnn's Baking: "valued for its ability to centralize documentation… but **criticized for being laggy and lacking an automated scheduling system**" |
| **Specright** | Specification management for CPG | Appears brand-side; Bob Evans Farms is a customer. Co-man coverage **[?]** |
| **FoodReady** | Food safety plans, HACCP, audit prep | Positioning vs mid-market co-mans **[?]** |
| **Redzone** | Plant productivity | Adjacent |
| ERPs (SAP, NetSuite, Infor, Plex, Doss) | System of record | **[E]** "consistently fail to address the highly specific requirements of process manufacturing and recipe-driven production" |

Resolving this table is the last desk task before interviews.

---

# Competitor scan (2026-07-28) — who already sells into this

Method: fetched each vendor's own site, plus funding/pricing search. Company self-descriptions are
marketing claims, not audited facts.

## SafetyChain — the incumbent to beat

- **Self-description:** "#1 Digital Plant Management Platform for Food & Beverage… trusted in **2,500+ manufacturing facilities** to digitize quality, streamline compliance, and power plant-wide processes." (safetychain.com)
- **Its marketing names our exact problem:** "Whether you're relying on **paper and pens, homegrown tools, or a clunky ERP system**…"; "**Always Audit Ready. Stop scrambling**"; "Replace **outdated spreadsheets** with real-time data"; "speed up pre-shipment reviews."
- **Funding:** ~$50M growth equity, Oct 2021 (CB Insights via search).
- **Pricing:** facility-based subscription, unlimited users; no public price at higher tiers.
- **Known weakness, from a user:** **[E]** Project Specialist, MaryAnn's Baking Co. (expert call, 9 May 2024): "valued for its ability to centralize documentation and provide auditor-specific access, but **criticized for being laggy and lacking an automated scheduling system**."

**Read:** the audit-documentation wedge is occupied, at scale, by a funded incumbent whose
homepage attacks spreadsheets by name. This materially weakens wedge #1 from the earlier ranking.

## Specright — occupies the specification layer

- **Self-description:** "#1 Platform for Specification Management"; modules for Packaging Management, **Product Data Management** ("raw materials, ingredients, formulas, recipes, and finished goods"), **Supplier Collaboration**, Project Management ("quickly build BOMs, forecast costs"), and an **R&D Workbench** with "AI-driven formulation tools."
- Sells into Food & Beverage among other industries; markets a "Spec-First AI Platform," an "AI Assistant," and "AI-Native Formulation."
- **[E]** Bob Evans Farms CIO is a public customer reference.

**Read:** spec intake, BOM building, and supplier collaboration are all explicitly in their
product. They are further ahead on this thesis than the earlier arena map assumed.

## Trustwell (FoodLogiQ + Genesis) — the compliance and labeling stack

- Covers "formulation and labeling to traceability and recall management." Named use cases include **"Manage Food Specifications," "Make Compliant Labels," "Comply with Regulations," "Manage Quality."**
- Markets "Trustwell AI" and **AskReg**, "your AI Expert for navigating the complexities of regulations in nutritional labeling."
- Industry pages include **Food Manufacturers + CPG** and **Supplement Manufacturers**.

## FoodReady — software plus consultants, priced for the small end

- Food safety, quality and traceability software **bundled with GFSI/HACCP/SQF/BRC consulting**.
- **Funding:** $4M seed, Sep 2023, ~$16M pre-money (search).
- **Pricing (secondary source):** **$1,500–$5,000/month** including consultant time (qtraca.com pricing guide) `[UNVERIFIED — vendor comparison site, not FoodReady's own page; their pricing page lists no figures]`.

**Read:** this is the first real ACV datapoint for the segment: roughly **$18k–60k per year**,
consistent with the earlier estimate that this is a low-tens-of-thousands product, not enterprise.

## Revised competitive picture

| Layer | Occupied by | Strength |
|---|---|---|
| Audit / compliance documentation | **SafetyChain** (2,500+ facilities, $50M), FoodReady (SMB + consulting) | **Strong.** Directly attacks spreadsheets. |
| Specification and BOM management | **Specright** (AI assistant, formulation, supplier collaboration) | **Strong**, though apparently brand-first. |
| Labeling and regulatory | **Trustwell** (AskReg AI) | Strong |
| Plant productivity | Redzone | Adjacent |
| ERP / system of record | SAP, NetSuite, Infor, Plex, Doss | **[E]** "consistently fail… recipe-driven production" |

## Honest consequence for the thesis

The earlier wedge ranking put **audit documentation first because it was best evidenced**. That
ranking did not account for competition. Corrected: audit documentation is the **most crowded**
cell, defended by a $50M-funded incumbent in 2,500+ facilities.

What remains genuinely unclaimed is narrower and rests on the asymmetry hypothesis: **not
managing the plant's own documents, but absorbing the inbound variety of many brand customers'
differing formats, questionnaires, and portals.** Every incumbent above organises the plant's own
data. None was found selling "we take whatever your twenty customers send and turn it into your
one internal standard."

That distinction is now the whole thesis. It is **[H]**, not **[E]**, and it is exactly what the
first interviews must confirm or kill. If a plant's answer is "SafetyChain already handles it,"
the dive should stop and re-aim.
