# The document flow between a brand and a co-manufacturer

Written 2026-07-28 from the three AlphaSense reports plus the arena map. This is the first
problem *thesis* in this dive, as opposed to a target list. Evidence markers are strict:
**[E]** = operator- or filing-sourced, **[H]** = hypothesis inferred from industry structure
(CLAUDE.md rule 3), **[?]** = unknown, interview question.

## The four moments documents move

### 1. Inquiry → quote
Brand sends a product description, target volume, pack format, sometimes a formula or spec sheet.
Plant must judge feasibility (equipment, allergens, certifications) and produce a price.
**[E]** The tooling for this is "email and spreadsheets" (Former Director of Product Management,
Xometry, expert call 20 Jul 2026).

### 2. Won → tech transfer (the heavy one)
The brand hands over the finished-goods specification, formula, ingredient specs, packaging specs,
label artwork, allergen statements. The plant must:
- convert the formula into a **bill of materials** priced per unit;
- **qualify** every ingredient — **[E]** "going through and looking at all of the various MSDSes,
  all the various product certification sheets, and qualifying it based on the regional value
  content" (Director, Trans America, 29 Dec 2025);
- create item masters, write batch records and manufacturing instructions;
- run trials and document them;
- complete the brand's supplier-qualification questionnaire.

**[E]** Timeline 6–18 months, up to 24 for regulated lines. **[E]** Mi3 Limited: a launch slipped
from 2023 to 2024 "partly by our customers due to documentation burden and resource restraints."
**[E]** Automating just the formula→BOM step cut processing time ~50% at Grape King Bio, and
quote turnaround 2.4 → 1.5 days.

### 3. Ongoing production
**[E]** Hain Celestial 10-K: co-packers must supply "questionnaires, scientific data,
certifications, affidavits, certificates of analysis and analytical testing, where required."
**[E]** Gehl Foods supplier terms define "Provider's Quality Documentation" as a COA "and each
other written or electronic communication/document relating to the quality and/or specifications,"
and require compliance with the customer's supplier-qualification program "as it exists from time
to time" — i.e. the brand can change the requirements unilaterally.

Every lot produces a COA. Every incoming ingredient arrives with a supplier COA that must be
checked against the spec.

### 4. Audits and disputes
Customer audits sit on top of SQF/BRC certification, each with its own document pack.
**[E]** Documents get checked against reality: "look at their COAs actual versus advertised"
(GM, Wherehouse Beverage, 13 Jan 2026). **[E]** When runs go off-spec the exposure is severe —
product destruction, arbitration, litigation (California Custom Beverage v. Reed's; Ascot Valley
ordered to disgorge $2,298,114 to ADF Foods).

## Why this lands on the plant and not the brand — the asymmetry

**[H]** A brand maintains **one** spec format and pushes it out to its co-mans. A co-man with
twenty brand customers **receives twenty different formats**, twenty different questionnaires,
twenty different portals, and must map all of them into one internal system. The translation cost
is therefore structurally concentrated on the plant side, and it scales with the number of
customers — which is exactly the thing a co-man is trying to grow.

This is the strongest available explanation for why brand-side software has not solved it, and it
is the counter-positioning argument: a tool built for the brand's outbound spec push is not the
same product as a tool for the plant's inbound spec intake. **It is a hypothesis, not a finding.**
Confirming or killing it is interview question one.

## Where the money actually leaks

| Leak | Evidence |
|---|---|
| Revenue delayed 6–18 months per new customer | **[E]** multiple sources; Mi3 lost a full year |
| Headcount hired to absorb paperwork | **[E]** FoodReady: previously "required expensive custom solutions **or additional staff**"; **[E]** 1 documentation coordinator/spec specialist typical at $50–250M `[secondary source]` |
| Manual-entry errors | **[E]** Grape King cited "lowering the risk of manual data entry errors" as a benefit |
| Disputes traceable to documents | **[E]** COA actual-vs-advertised checks; off-spec litigation |
| Capacity spent on work that never becomes revenue | **[?]** the 5–10% inquiry conversion figure is secondary-sourced, not operator-confirmed |

## What AI does here that a spreadsheet cannot

1. **Read arbitrary inbound documents** — PDFs, Word specs, Excel formulas, portal exports — and
   map them onto the plant's own schema. The variety is the whole problem, and variety is what
   language models handle that rigid integrations do not.
2. **Qualify a BOM** by cross-checking ingredient specs, MSDSes, and certificates against the
   finished-goods spec, flagging only the mismatches.
3. **Answer customer questionnaires** from the plant's existing document set rather than retyping.
4. **Generate the outbound pack** — COAs, spec confirmations, audit responses — from batch data.

**[E]** An operator names this category unprompted: "anything that deals with being able to
eliminate workflow and simplify the process, you're trying to see ways that AI can come in and
eliminate a lot of that manual effort that goes into the data entry component of it."

## What could kill it

1. **[E] Clean-data dependency.** "It requires a lot of front-end engineered clean data. A lot of
   people have tried away from it." (Former VP Supply Chain, Quality Sterling Group). If a plant's
   specs and costs are not written down anywhere, there is nothing to map onto.
2. **[E] Specright already exists** and sells specification management into CPG (Bob Evans Farms is
   a customer). Its CEO: "traditional PLM systems were never built for the realities of
   fast-moving consumer goods." **[?]** Whether it sells to co-mans or only to brands is unresolved
   and is the next arena question.
3. **[?] Willingness to pay.** The automatable roles are few — one documentation coordinator, one
   to three costing staff. That caps ACV at the low tens of thousands per site.
4. **[H] Switching inertia.** The paperwork is a contractual obligation to the customer. A plant
   may prefer a known-slow manual process over a tool that could produce a wrong COA.

## Interview questions this generates (Mom Test form — past behaviour, not hypotheticals)

1. Walk me through the last new customer you onboarded. What documents did they send, in what
   format, and who turned them into something your plant could use?
2. How long between signing and the first paid run? What was the longest wait caused by paperwork
   rather than production?
3. Who fills in customer quality questionnaires? How long does one take?
4. When did a COA or spec last get disputed, and what did it cost to resolve?
5. What have you bought to make this easier? What did you stop using, and why?

---

# Validation pass — fourth AlphaSense report (2026-07-28)

Ran the task-by-task prompt. The report has a section literally titled "Administrative Burdens:
Verified Task-by-Task Operator Voice." Result: two tasks strengthened, **one task killed**, two
still unevidenced. Detail below, then a revised wedge.

## The asymmetry hypothesis — now stated explicitly

> "When a co-manufacturer scales their business by taking on multiple unique brand customers, **the administrative burden does not scale linearly; it multiplies**. Because there is **no industry standardization**, every brand brings its own unique formulations, custom quality questionnaires, and private label packaging requirements, which **forces the co-packer's administrative team to run highly fragmented processes for each account**."

Caveat: this is AlphaSense's synthesis, supported by a prospectus from an FMCG contract
manufacturer, not by a co-man operator complaining in their own words. Upgrade from `[H]` to
**`[E-weak]`** — stated by an industry source, not yet by a plant.

## Task-by-task verdicts

**Task 1 — spec intake into item master/BOM. `[E-weak]`**
Confirmed as manual and error-sensitive, but the supporting quote is generic (Upfield: "making
processes more user-friendly and less prone to human error, with a particular focus on
strengthening data management"). No hours quantified.

**Task 2 — recipe → costed BOM. `[E-weak, cross-functional]`**
> **Former VP Supply Chain, Strategy & Optimization** (expert call, 23 Jul 2026): "Brand and operations finance are two different groups, and they sit off to the side until we get all this done. **This packet is then handed over to the brand and operations finance and sales and marketing** to take a look at and see if it makes sense."

The report's own note: "direct verbatim quotes detailing the exact administrative hours spent
re-keying recipe weights into internal BOM systems **remain thin in public disclosures**." So the
problem is coordination across silos, not obviously re-keying volume.

**Task 3 — checking incoming ingredient documents. ❌ KILLED as a wedge.**
> **VP of Technical Services, IEH Laboratories** (expert call, 5 Apr 2026): "Normally there's about six [results on a COA]. **If there's 30 COAs, they'll have to spend 10 minutes looking at them.**"

Twenty seconds per COA. This is cheap, not painful. Automating it saves minutes per week. Drop it.
(The requirement itself is real — JBSS: "Certificates of Analysis are required for all received
materials and must be provided to JBSS prior to acceptance" — but meeting it is not expensive.)

**Task 4 — customer questionnaires. `[E]` requirement confirmed, cost not quantified.**
Hain Celestial and Upfield both confirm suppliers must complete detailed questionnaires and
self-assessments. Both quotes are **brands stating requirements**, not co-mans describing the
burden. The multiplication claim above is what makes this expensive; that link is still weak.

**Task 5 — producing lot COAs. `[E]` and the cost is physical, not clerical.**
> **Tridge** (7 Jul 2026): "The cost of compliance shows up as **lab capacity, hold time, and occasional lot segregation — not just as 'paperwork.'**"
> JBSS: "each lot must be sampled… according to a statistical sampling plan (ICMSF, FDA BAM)."

Important reframe: product cannot ship until the COA is validated, so the bottleneck is lab
throughput and hold time. Software does not fix a lab queue. Weakens Task 5 substantially.

**Task 6 — spec change and label updates. `[E]` and digitization has a proven result.**
> **Tasty Bite Eatables** (annual report, 22 Jul 2026): "we sustained **First Time Right (FTR) quality scores of over 99%, driven by the digitisation of change control** and continuous improvement processes."

A minor label error can trigger a recall, so this is high-stakes and someone has already shown
digitizing it moves a measurable number.

**Task 7 — audit document packs. `[E-strong]` — the best-evidenced task.**
> **Director of EHS, Shehadey Family Foods** (expert call, 25 Dec 2025): "We currently have a food certification called SQF. It requires us to have certain inspections, audits, other documentation on a **monthly and weekly basis** completed within the facility. **Right now, it's done just through an Excel.**"
> **Upfield**: implementing SQF at one site took 90 days versus "an achievement that typically takes a year," requiring "cross-functional collaboration across Operations, Maintenance, Supply Chain, HR, and Health and Safety."

A named operator, a named certification, a stated cadence, and the tool named as Excel.

**Task 8 — screening and pricing inquiries. `[E]` and the cycle is long.**
> **Representative Director and President, Natty Swanky Holdings / Grip Factory** (earnings call, 18 Mar 2026): "since each restaurant has its own particular preferences, **it takes many iterations from the initial discussion until contract signing, and currently it takes about a year or so to reach a contract**."

## Systems evidence

- **60% of sub-$1B food companies run on laptops and Excel**; deployed ERPs are described as a "necessary evil" lacking real-time production tracking.
- Failed ERP implementations trace to "poor data quality and misalignment with plant floor realities."

## New competitors surfaced

- **SafetyChain** — and its weaknesses are named: > **Project Specialist & System Administrator, MaryAnn's Baking Co.** (expert call, 9 May 2024): SafetyChain "is valued for its ability to centralize documentation and provide auditor-specific access, but is **criticized for being laggy and lacking an automated scheduling system**."
- **Redzone** — mentioned alongside SafetyChain.
Both belong in `cm-arena.md`, together with Specright and FoodReady.

## Revised wedge after validation

Ranked by evidence strength, not by size of prize:

1. **Audit and compliance documentation (Task 7)** — a named operator says it runs on Excel, weekly and monthly, for a mandatory certification. Errors are cheap (a human reviews before the auditor sees it). Incumbent SafetyChain has named gaps.
2. **Change control (Task 6)** — high stakes, proven ROI at Tasty Bite.
3. **Spec intake and questionnaires (Tasks 1 and 4)** — real, but their expense depends on the multiplication effect, which is still only industry-sourced.

Dropped: **Task 3** (COA checking, measured at 20 seconds per document) and **Task 5** demoted
(the constraint is lab capacity and hold time, not clerical work).
