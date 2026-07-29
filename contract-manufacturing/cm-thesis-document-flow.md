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
