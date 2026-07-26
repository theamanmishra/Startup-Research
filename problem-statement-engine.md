# Problem-Statement Engine (v4) — industry-agnostic

The operating system for taking **any industry**, understanding it in depth, extracting a large grounded problem list, and narrowing to 1–3 validated candidate problem statements worth building a company on.

**The full flow — three steps:**

| Step | Mode | What it uses | Cadence | Output |
|---|---|---|---|---|
| **0. CHOOSE** the industry | — | Your industry-priority list (a separate doc — currently `industry-priorities.md`) | Once per new industry | Which industry/vertical to map next + geography |
| **1. MAP** — discover problems | Deep Industry Map (§1) | This doc §1 | One-time per industry, heavy (~2–4 days) | Industry structure in depth + 30–50 grounded problems |
| **2. EVALUATE** — judge problems | Evaluation Loop (§2) | This doc §2 + `founder-profile.md` + shortlist tracker | Weekly, repeating | Top 1–3 scored, interview-validated candidates |

This doc is deliberately **agnostic of any specific industry**. Which industries to run it on, and in what order, is decided outside it (Step 0). The only personal input it consumes is the **Founder Profile** (the Step-C edge filter).

**Golden rule:** map with the value-chain lens to *find* problems; select with the edge + problem-quality lens to *choose* them. The lucrative problem where you have no unfair advantage is a trap.

---

## §1 — MAP mode: the Deep Industry Map

**Unit of analysis = one industry vertical** (e.g., a product category, a service sector, a regulated domain), walked **end-to-end along its value chain**. Not a single functional lane (yields a thin ~10-problem list); not a whole meta-sector (unmappable). One vertical, full depth → 30–50 problems.

**Declare geography first** (e.g., India / US / both) — it changes structure, regulation, and the problem set.

**Research discipline:** MAP mode runs on *current, searched sources* (industry reports, funding databases, regulator sites, operator interviews) — never on model memory alone. Capture numbers as **ranges with a source note**; where sources conflict, record the conflict rather than picking one. Named claims (a regulation, a competitor's pricing, a market size) must be verifiable.

### 1a · Frame the industry (the aerial view)

Before decomposing, capture the industry-level picture — this is the "overall understanding" the map must deliver:
- **Size & growth** — rough market size (range, not false precision) and direction; what drives demand?
- **Segments** — the industry's major segments and which are growing / mature / dying.
- **Structure** — fragmented or concentrated? Where in the chain do the powerful players sit?
- **Regulatory & macro context** — the rules and forces that shape conduct in this industry and geography.

### 1b · Decompose the value chain

Break the industry into its **actual chain of steps from raw input to end customer** — whatever those steps are for *this* industry:
- Physical-goods industries typically follow **make → move → sell** (inputs → processing/manufacturing → packaging → logistics/storage → distribution/wholesale → retail → consumer → returns/waste).
- Service or software industries follow their own chain (e.g., origination → underwriting → servicing; or acquisition → onboarding → delivery → renewal). Map the *money flow* (who pays whom) alongside the *goods/service flow* — they often differ, and the gap is informative.
- Add the **enabling layers** that cut across steps: planning/data, compliance/regulation, finance/payments, tooling/infrastructure.

### 1c · Go deep on each step

For **each step**, capture industry-structure depth:
- **Cost structure** — the big cost lines in this step; what % of the end price accrues here?
- **Revenue & margin** — who makes money here, how fat/thin? Where does margin pool?
- **Power** — who holds leverage (suppliers, buyers, platforms, regulators)? Who sets terms?
- **Players** — incumbents, challengers, and the vendors already selling into this step.
- **What changed (~3 yrs)** — cost curves, regulation, entrants, demand/behavior shifts → why-now vectors.
- **Pain points** — where money/time/output leaks *within* this step.

### 1d · Stare at the seams

The richest problems often live **between** steps: handoffs, information loss, misaligned incentives. For every adjacent pair of steps ask: **what breaks in the handoff, who pays for it, and why does neither side fix it?**

### 1e · Harvest the problem list (30–50)

Every pain point → one problem line: **sufferer · the specific task that fails · what the failure costs.** Tag each with its **step** (and segment, if the industry has distinct segments). Reject vague entries ("inefficiency in logistics" ✗; "freight brokers spend ~X hrs/load manually matching capacity; mismatches cost ~$Y" ✓). Breadth first — no filtering at this stage.

**Depth discipline — what does NOT belong in the map:** solution ideas, DMU mapping, LTV:CAC, feasibility. That is evaluation-phase depth (§2), run only on triage survivors. The map answers *how the industry works and where it bleeds*. (Industry-structure depth is not academic: a brutal pain in a step where a powerful player captures all the margin is a bad problem — no room for you to capture value. The map is what reveals this.)

*Output: an Industry Map doc (structure per step + seams + why-now vectors) and the tagged problem list, logged in the tracker's **Inventory** tab (raw pool) — candidates only move to the **Tracker** tab once scored in §2.*

---

## §2 — EVALUATE mode: the weekly loop

Feeds off the problem list from §1. Each week: pull the next batch (usually one dense cluster of related problems), evaluate, validate with humans, score into the tracker.

| When | Phase |
|---|---|
| Day 1 | Pull batch; fast triage (Step A) |
| Days 2–5 | Deep-dive survivors (Step B) → edge filter (Step C) → write & score (Step D) |
| Weekend | Interviews; validate riskiest assumption; update tracker |

### The judging lens (how top incubators evaluate)

A startup = **problem + solution + insight**. Interrogate the problem hardest. Good problems are: **frequent · intense · popular & growing · urgent · expensive · sometimes mandatory.** The two axes that matter most: **frequency × intensity.**

**Start from the problem, never the solution** (avoid SISP — solution in search of a problem).

**Unfair advantage — want at least one (higher = stronger):**
- **Founders** — are you ~1-in-10 *in the world* who can solve this? (Judge against the Founder Profile.)
- **Product** — 10x better, not 2x.
- **Acquisition** — built-in audience/referral loop; paid acquisition is weak.
- **Market** — growing 20%+/yr (weakest — not unique to you).

**Contrarian signal:** the best ideas often look bad to most people. **Evaluator's mindset:** don't poke holes first — work out how it *could* become huge.

### Step A — Fast triage (batch → ~4–6)

Problem-quality screen per problem (fast): frequency? intensity (painkiller/vitamin)? already paying to cope? popular & growing? urgent/mandatory? Keep high-frequency × high-intensity with real spend.

**Kill gates** (any one true → park/kill): no why-now · no founder edge (park) · no one with budget feels it · needs capital/licenses/access you can't get · market too thin for a real business.

### Step B — Deep-dive (seven blocks per survivor)

**1 · Problem severity** — frequency; cost per occurrence; paying / working around / ignoring; painkiller or vitamin; how solved today and *where exactly* it fails.

**2 · Buyer, market & DMU** — user vs buyer; full DMU (champion / economic buyer / influencers & vetoers / procurement — deals die in procurement, not demos); budget line & owner; bottom-up size (# buyers × ACV, show arithmetic; beachhead framing); fragmentation; sales cycle & sign-off chain.

**3 · Why now** — the specific enabling change; why not buildable 3–5 yrs ago; why not trivial in 3–5 more; forcing function pulling demand forward.

**4 · Competition & why the incumbent won't respond** — direct competitors & pricing; who failed and was it *structural* or *executional*; which adjacent player could crush this — and why they won't (**counter-positioning** is the strongest answer: a model they could copy but won't, because it cannibalizes their economics; incumbents also ignore anything < ~10% of enterprise value).

**5 · Wedge & defensibility (benefit + barrier)** — narrowest entry point + path to a larger position; GTM motion & rough CAC vs contract value; **moat = benefit + barrier** — score against the seven powers (scale economies, network economies, switching costs, counter-positioning, branding, cornered resource, process power); "better/faster" is a benefit, not a barrier; does the moat compound?

**6 · Solution & feasibility** — hypothesis-level solution; 10x or 2x; buildable today, by *you/a small team*; hardest technical/operational risk; **the single riskiest assumption** — singular, important, testable → earmark for weekend interviews.

**7 · Business model & unit economics** — how you make money (model ≠ price); recurring or one-off; gross-margin shape; rough LTV:CAC & payback; pricing power (value-based or cost-plus); of the value created, how much do *you* capture vs hand up the chain?

### Step C — Edge filter

Cross survivors against the **Founder Profile**: *why would I be unusually hard to beat here?* Bias toward the meta-thesis stated there. "No particular reason" → discard.

### Step D — Write & score

Problem-statement format:

> For **[segment/persona]** trying to **[job]**, the problem is **[task that fails]** — today they cope by **[status quo]**, costing **[quantified pain per occurrence]**. Newly solvable because **[why-now]**. I have an unfair right to win because **[edge/insight]**. The wedge is **[narrow entry point]**.

**Rubric** (score 1–5 × weight → /100; also in tracker):

| Dimension | Wt | A 5 looks like |
|---|:---:|---|
| Founder-market fit / insight | 20 | Access/insight/skill almost no other founder has |
| Why-now | 15 | Specific recent catalyst; not buildable 3 yrs ago, not trivial in 3 more |
| Problem severity (freq × intensity) | 15 | Frequent AND painful; money already spent coping |
| Willingness & ability to pay | 12 | Clear budget; you can name its owner |
| Market size & headroom | 12 | Room for a business worth full-time commitment — venture-scale *or* durable cash flow |
| Defensibility / moat | 10 | Real, compounding barrier |
| Competitive whitespace | 8 | Structural incumbent blind spot; bonus if it "looks bad" |
| Speed to first customer | 8 | Signed customer in weeks-to-months |

**Graduate ≥ ~70.** Calibration: empirically, *market* is the biggest single determinant of outcome — don't let a strong edge talk you into a weak market; if severity and headroom are both low, be very skeptical.

### Weekend — Talk to humans

Desk research reproduces consensus; the differentiated insight comes from conversations. **3–5 conversations** across top candidates (warm intros, LinkedIn, school/work networks, industry communities).

**Mom Test rules:** ask about actual past behavior and current workarounds, not hypotheticals; never pitch; dig into what they've *paid for* / tried / hacked; talk about their problems, not your solution.

**Goal:** validate or kill each candidate's **riskiest assumption**. Update scores; **promote / park / kill in the tracker.** A week with no tracker update is a week that evaporated.

**Question bank:** Walk me through the last time you dealt with [task] — step by step? Most frustrating part; how often? What have you tried/bought/built? What does it cost when it goes wrong? Who else is involved; who approves spend? If magically solved, what changes? *(Listen for shrug vs relief.)*

---

## Quality signals (read alongside the score)

**Green:** non-consensus but right · you'd be a user / felt the pain · high freq × intensity with money already spent · forcing function pulling demand · genuine 1-in-10 insight · built-in audience/referral loop.

**Red / tarpits:** SISP · "sounds great to everyone" · vitamin dressed as painkiller · behavior change with no forcing function · growth hinges on paid acquisition · margin leaks to a player above you · one platform shift makes it a feature · a schlep you won't do for years.

---

## Output templates

**MAP mode (per industry):**
```
INDUSTRY/VERTICAL: ______  GEOGRAPHY: ______  DATES: ______
VALUE-CHAIN DECOMPOSITION (the steps, this industry's own chain + enabling layers)
- …
STEP-BY-STEP STRUCTURE (per step: cost structure / margin & revenue / power / players / what changed / pains)
- …
SEAMS (per adjacent pair: what breaks in the handoff, who pays, why unfixed)
- …
WHY-NOW VECTORS (3–5)
- …
PROBLEM LIST (30–50: sufferer · task that fails · cost — tagged by step/segment)
- …
```

**EVALUATE mode (per week):**
```
BATCH/CLUSTER: ______  WEEK OF: ______
TRIAGE SURVIVORS (~4–6): …
DEEP-DIVE SUMMARY (per survivor, 7 blocks): …
EDGE FILTER: …
TOP CANDIDATES (statement format, scored /100): …
CONVERSATIONS (who · asked · learned): …
RISKIEST ASSUMPTION per candidate — validated/killed: …
VERDICT → TRACKER — Promote: __  Park: __  Kill: __
```
