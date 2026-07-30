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

---

# Outreach method finding (2026-07-28) — food co-mans do not publish personal emails

Research agent covered 6 verified co-mans (Kettle Cuisine, Berner, Tulkoff, Wixon, Palmer Candy,
Anthony-Thomas), crawling 1,700+ pages and 58 company PDFs.

**Result: zero of six publish a double-confirmable personal email pattern.** Five publish only role
inboxes (`info@`, `sales@`, `customerservice@`, `appointments@`, `hiring@`). One (Wixon) yielded a
single personal specimen, `murray_wright@wixon.com`, from an undated association directory.

The agent's conclusion, which matches the evidence: this is a **property of the segment**, not a
search failure. Private, family-held and PE-held co-mans route all contact through a form or a
general inbox. Media contacts in their press releases are outside PR agencies.

**Consequence for the pipeline.** Adarsh's OEM design assumes a confirmable pattern, then derives
addresses for a ranked roster. That step works for equipment makers, who publish parts, dealer and
service contacts. **It does not work here.** Deriving addresses at scale for food co-mans is not
available from public sources.

**What public research DOES yield reliably: names and titles.** The same pass produced current,
company-sourced leadership including exactly the right personas —
- **Rich Ellefson, VP of Food Safety & Quality, Palmer Candy** (live company page)
- **Sara Sarnstrom, Director of Regulatory Affairs, Wixon** (company PDF, Mar 2026)
- **Mike Kagan, CEO, Tulkoff** (company release, Feb 2025)

**Revised approach:** names from web research, addresses from **Mergent Intellect** (D&B data,
unmetered under HBS access, confirmed working by Aman on 2026-07-28). Role inboxes are the
fallback where Mergent has nothing.

**Also recorded:** leadership evidence is stale (pre-2024) at Kettle Cuisine, Berner and
Anthony-Thomas, and both Kettle Cuisine and Berner changed ownership after their last published
leadership news, so titles are likely to have drifted. Kettle Cuisine's own site is Cloudflare-blocked
and was not reconstructed from lead-broker data (CLAUDE.md rule 8).

## Outreach research update (2026-07-29) — the FMCSA route

Batches B and C found what batch A did not: **the FMCSA motor-carrier census
(`data.transportation.gov/resource/az4n-8mr2.json`) publishes registrant emails and company
officers** for any food company that runs its own trucks. This is a verbatim, government-published
source and it broke the deadlock. Also productive: WordPress REST API endpoints
(`/wp-json/wp/v2/pages`), which expose contact blocks hidden on the rendered page.

**Patterns double-confirmed (2+ verbatim addresses):** Lyons Magnus `{f}{last}@lyonsmagnus.com` ·
Stremicks Heritage `{first}{last}@heritage-foods.com` · Cedarlane `{f}{last}@cedarlanefoods.com` ·
Adirondack `{f}{last}@adkbev.com` · Vanee `{first}{last}@vaneefoods.com` · Organic Milling
`{f}{last}@organicmilling.com` (but evidence is 2010–2016 and the company was acquired in 2022).

**Domain traps found — sending to the website domain would bounce:** Vanee's mail is
**vaneefoods.com** not vanee.com · Adirondack's is **adkbev.com** not adirondackbeverages.com ·
Georgia Nut's is **georgianut.com** not georgianutcorp.com · Berner's is **bernerfoods.com**.

**Site bugs worth knowing:** Wolfgang and Lakeside both publish addresses with a stray "www."
inserted (`info@www.wolfgangco.com`), a migration artifact. Wolfgang's legacy domain
wolfgangcandy.com is compromised and serving gambling spam; do not source from it.

**Best personas found, no address yet (Mergent targets):** Rich Ellefson, VP Food Safety & Quality,
Palmer Candy · Dulce Guzman, Director of QA and Arturo Guerrero, Director of Operations, Georgia Nut ·
Lesli Kunkle, Director FSQA and Gary Shortt, VP Operations, Wolfgang · Sara Sarnstrom, Director of
Regulatory Affairs, Wixon.

**Companies that yielded nothing usable:** Union Beverage Packers (no named person anywhere, only
`sales@`), Lief Labs (genuine null result on pattern; two aggregators contradict each other),
Kettle Cuisine (site Cloudflare-blocked, leadership evidence 2017–2020 and ownership has changed).

## Bounce evidence from batch 1 (2026-07-29) — 13 of 15 delivered

Fifteen emails sent 29 Jul. Two bounced. They failed for opposite reasons and the
distinction matters for how the pipeline treats an address.

**`johnkuethe@vaneefoods.com` — DSN 5.7.129, "you don't have permission to send to it."**
This is Exchange Online's *restricted recipient* refusal, not a bad address. The mailbox
exists; it is configured to accept mail only from an approved sender list. Consequence:
the address was correct and the research was correct, and the person is still unreachable
by cold email. There is no retry, no alternate spelling, no pattern fix. Park the person,
try a different persona at the same company. **Do not read a 5.7.129 as a failed
derivation — it says nothing about the pattern.**

**`pbegg@lyonsmagnus.com` — 5.1.1, "pbegg wasn't found at lyonsmagnus.com."**
`jdavis@lyonsmagnus.com`, derived from the same `{f}{last}@` pattern, delivered the same
day. So the pattern is confirmed correct and the *person* is gone. This row had already
been flagged in the tracker: "placement announcement undated, no post-2024 confirmation he
still holds the role." The flag was right and the draft should have been benched rather
than sent. **Rule tightened: a contact whose most recent in-role signal cannot be dated
after the last ownership change, or within ~18 months, is benched, not drafted** — Lyons
Magnus had been acquired by Truelink Capital nine days before we wrote.

Read across both: the email-pattern bar is doing its job (2 of 2 derived-from-confirmed
addresses reached a live mailbox or a live-but-restricted one), and the weak link is
**person recency**, not address construction. Spend the marginal research minute on
"is this person still there" rather than on a third address confirmation.

Bounce codes worth recognising:
- `5.1.1` / "wasn't found at" — address wrong OR person gone. Check whether a sibling
  address at the same domain delivered; if yes, the person is gone.
- `5.7.129` — restricted recipient. Address fine, person unreachable. Park.
- `5.7.1` / `5.7.606` — sender or IP blocked. That is about us, not them; if it recurs
  across domains, the sending reputation is the problem.

## Batch 3 yield evidence (2026-07-30) — what actually predicts a sendable address

Twenty Tier A companies researched by five agents. **Four produced a confirmable email
pattern. Sixteen did not.** That 20% is the real desk-research yield, and the split is not
random.

| Group | Companies | Sendable | What they had going in |
|---|---|---|---|
| 1 | Chelten House, Johanna, Star Snacks, Berner | 2 | verbatim addresses already in the D&B export |
| 2 | Anthony-Thomas, Burke, Coating Place, Coloma | 0 | name only |
| 3 | Best Formulations, ANS, Bakery Barn, CraftMark | 0 | name only |
| 4 | Brooklyn Bottling, Country Pure, Calpack, Consolidated Mills | 0 | name only |
| 5 | Cookies United, Craft Cannery, AZPACK, Bardstown | 2 | name only |

**The finding: an email pattern is not something research discovers, it is something a
company either publishes or does not.** Thirteen of the sixteen failures failed at the same
step — exactly one published address, or only a general inbox. More search time would not
have changed that. Craft Cannery is the instructive exception: a small owner-run co-packer
publishes `Pauly@CraftCannery.com` on its contact page, because at that size the owner *is*
the inbox. Bardstown only worked because a corporate restructuring created a new PR site
with two named-contact addresses on it.

Second-order findings from the same sweep:

- **Mail domain ≠ web domain in 7 of 20 companies.** bernerfoods.com (site is
  bernerfoodandbeverage.com, and bernerfoods.com serves no web at all), cmillsinc.com,
  loftedspirits.com, iberiafood.com and nsbottle.com for Brooklyn Bottling, hppfs.com,
  juice4u.com, and Cookies United's contact page whose visible text says
  `info@cookiesunited.com` while the actual mailto targets `info@silverlakecookie.com`.
  Always read the mailto target, never the link text.
- **The D&B contact columns are dangerously stale.** Anthony-Thomas listed a CEO who died
  in 2013. Berner listed a CEO whose family sold the company in 2015. Best Formulations and
  ANS both listed CEOs who had moved on. Chelten House listed a VP whose bio page 404s.
  Treat every D&B *name* as a lead needing a dated confirmation; the D&B *addresses* have
  held up well, which is the opposite of what one would assume.
- **Tier A is not clean.** Burke Corp is a Hormel subsidiary, AZPACK has been Refresco since
  2019, Best Formulations is a Sirio Pharma subsidiary, Bakery Barn's plant closed in 2025.
  Four of twenty were not independent co-manufacturers at all. The tiering pass checked what
  a company said it did, never who owned it.

**Consequence for the 50-a-day target.** Only 6 untouched Tier A and B rows still carry a
verbatim address. Desk research converts name-only companies at roughly 1 in 8. So 50 a day
is not reachable by adding search effort; it needs an address source — Mergent Intellect
through HBS, or a paid finder API. Until then the honest daily ceiling is closer to ten.
