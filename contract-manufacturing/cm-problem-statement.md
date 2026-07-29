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
