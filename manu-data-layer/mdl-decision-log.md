# Decision log — shop-floor data layer

**Purpose:** every choice that narrowed the work, with the options considered, the reasoning, and
what would reverse it. Needed later for the IP write-up and for anyone who asks "why these three?"

**Convention:** append only. Never rewrite a past entry — if a decision changes, add a new one that
supersedes it and say so. Each entry carries what would reverse it, so a reversal is a check against
a stated condition rather than a re-argument from scratch.

---

## D1 · Thesis: shop-floor data layer, not document AI
**Date:** 2026-09 · **Board line:** whole board

**Decision.** Move from document/paperwork AI for food co-manufacturers to acquisition and
contextualization of shop-floor machine telemetry.

**Why.** The document thesis's best-evidenced wedge (audit documentation) turned out to be the most
crowded cell — SafetyChain sits there with ~$50M raised and 2,500+ facilities, and its homepage
attacks spreadsheets by name. What remained unclaimed rested on an unverified asymmetry hypothesis.
Separately, the Adarsh co-founder pairing brought physical-AI and robotics capability.

**Superseded work** is in `../archive/cm-document-thesis-2026-07/`, which stays citable.

**Reverse if.** Interviews show the inbound-spec-variety problem is acutely felt and unserved, while
shop-floor data proves absent.

---

## D2 · The layer is acquisition + contextualization, not storage
**Date:** 2026-09-17 · **Board line:** header annotation

**Decision.** Target layers 1 and 2 of the stack: **acquisition** (getting signal off the machine)
and **contextualization** (making a trace mean "batch 4471, product X, line 2, pasteurize, shift B").
Explicitly not layer 3, storage and access.

**Options considered.** All three layers; storage-first (the literal Snowflake analogy).

**Why.** Snowflake was a layer-3 company in a world where layers 1 and 2 were already solved for
business data by decades of ETL vendors and databases. In manufacturing those layers are *not*
solved, and layer 3 is nearly free — object storage, ClickHouse, Postgres, plus the historians
already installed. The analogy imports an assumption that does not hold.

**Reverse if.** The arena pass shows acquisition and contextualization are commoditised by
HighByte/Litmus/Ignition at mid-market price points, leaving the differentiation elsewhere.

---

## D3 · Q3 runs four tests, not one
**Date:** 2026-09-17 · **Board line:** Q3

**Decision.** "Are there commonalities?" is necessary but not sufficient. Q3 tests: ① **common**
(do many problems share few primitives) ② **hard** (if easy it is a feature, not a company — and the
structural reason nobody assembled it must be *named*) ③ **paid** (will anyone buy the layer without
an outcome) ④ **pooled** (does cross-plant pooling add value — a contracts question, not a technical
one).

**Why.** Commonality alone does not make a business. High commonality plus low difficulty is exactly
what an incumbent already ships. Only sourced ACV datapoint for this segment is FoodReady at
~$18–60k/yr *including consultants* `[UNVERIFIED]`, which is thin for infrastructure sold on its own.

**Reverse if.** Nothing — these are additive tests, not a narrowing choice.

---

## D4 · ICP ① (SaaS cos for Manu AI) = informant, not revenue segment
**Date:** 2026-09-17 · **Board line:** ICP ①

**Decision.** Keep ① on the board but treat it as a research channel until the arena pass counts the
population.

**Why.** `Hypothesis:` too few such companies to be a market, and ingestion is their own
differentiation so they build it in-house. But each has already solved "what data does problem X
need," and the answer is legible in their connector docs and job postings — cheap intel.

**Reverse if.** The arena pass finds a large and growing population of manu-AI application companies
that buy rather than build their data layer.

---

## D5 · Scope: all F&B manufacturers, co-man status is a tag not a filter
**Date:** 2026-09-17 · **Aman's call** · **Board line:** scope header

**Decision.** In scope: NAICS 311 and 312, all manufacturers. Co-man status recorded as an attribute,
not used to filter.

**Options considered.** Co-mans only (the prior anchor for the whole repo).

**Why.** The thesis needs plants that *have* machine data. Brand-owned plants are better instrumented
and carry capex budgets; co-mans are thinner on both. Filtering to co-mans would bet the thesis on
the segment least likely to have data. Tag it and let the evidence decide whether it matters.

**Consequence.** Universe is ~3,000–3,500 US firms at $10–100M, not the co-man subset.

**Reverse if.** Evidence shows co-man multi-brand economics create a materially different and more
acute problem, in which case co-man becomes the segmentation variable.

---

## D6 · Unit of analysis: process, not product
**Date:** 2026-09-17 · **Board line:** Q1 sub-branch (a), "hyper-niches"

**Decision.** A hyper-niche is a set of plants sharing a **production process**. NAICS 6-digit is the
working proxy.

**Why.** Process determines what sensors exist and what fails. A bottling line and a kettle line have
different instrument sets, so "does data exist" has a different answer in each. Product grouping
(dairy vs snacks) does not surface that; process grouping does.

**Known imperfection.** Two codes are internally mixed: 311421 blends retort canning, freezing and
pickling; 311999 is an explicit catch-all. Handled by narrowing 311421 in D10 and distrusting 311999.

---

## D7 · Niche screen design: three-stage funnel
**Date:** 2026-09-17 · **Board line:** Q1 step 1

**Decision.** Stage 1 eligibility (binary) → Stage 2 weighted score → Stage 3 deliberate selection.
Full method in `mdl-niche-screen.md`.

**Why.** Replaces judgment with an auditable screen. The first draft of three archetypes (aseptic
beverage / kettle wet-fill / dry blend-bake) was my assertion, not derived — Aman challenged it,
correctly.

---

## D8 · Weights: Reg 30 · Auto 25 · Fail 20 · Arena 15 · Edge 10
**Date:** 2026-09-17 · **Aman approved**

**Decision.** Regulation carries the heaviest weight.

**Why.** Regulation is the only criterion that answers the board's first asterisk (*does data exist*)
from a desk. Where a rule mandates recording a process value, the measurement provably happens.

**Sub-decision: arena deferred.** Scoring arena crowding before the arena pass would be circular, so
the other four were renormalised (Reg 35.3 · Auto 29.4 · Fail 23.5 · Edge 11.8) and **arena will be
applied as a disqualifier on the final three**, not as a score.

**Sub-decision: firm count filters, it does not score.** Counting it in both places would let
big-but-unpromising categories through. This is why 240-firm meat processing ranks below 60-firm
fluid milk.

---

## D9 · Stage 1 filters: ≥50 firms in band · is a plant · NAICS 311–312
**Date:** 2026-09-17

**Decision.** 25 of 51 codes passed.

**Excluded for cause:** retail bakeries (82 firms — storefronts, not shop floors), ice manufacturing
(6), dog & cat food (45) and animal feed (234) — both outside F&B.

**Known casualty.** **311422 specialty canning has the highest regulation score in all of F&B but
only 7 firms in band**, so the size floor drops it. Revisit if the floor is ever lowered or if retort
proves to be the answer.

**Reverse if.** The thesis turns out to need very few, very large customers — then the 50-firm floor
is wrong and should be replaced by a revenue-concentration test.

---

## D10 · The three niches: retort canning, cheese, sauces
**Date:** 2026-09-17 · **Aman's call**

**Decision.**

| Slot | Niche | Firms | Regime | Process |
|---|---|---:|---|---|
| 1 | Retort-canned low-acid vegetables & soups (subset of 311421) | 115 | 21 CFR 113 + 114 | Batch thermal, retort room |
| 2 | Cheese (311513) | 86 | Grade A PMO | Continuous pasteurization + batch vat |
| 3 | Mayo, dressings & prepared sauces (311941) | 59 | 21 CFR 114 acidified | Kettle / wet-fill |

**Options considered.** (a) Literal top 3 by score — fluid milk, cheese, canning. (b) A spanning
sample across the data gradient — canning, sauces, perishable prepared food. (c) The chosen set.

**Why not the literal top 3.** Fluid milk and cheese are nearly the same niche: same PMO regime, same
recording instruments, similar plant. Two of three slots would buy the same learning. And fluid milk
at $10–100M is the weakest commercial pick in the top tier — regional commodity dairies, thin
margins, poorest willingness to pay in food.

**Why this set.** Three *different* regulatory regimes (FDA thermal, PMO dairy, FDA acidified), three
*different* processes, stepping down the data gradient one notch (Reg 5, 5, 4) instead of clustering.
All three commercially plausible at mid-market scale.

**Parked as a group:** meat, poultry, seafood (ranks 4, 6–8). Strongest mandated records in F&B, but
fabrication is manual, founder edge is 2, and they would behave similarly to one another. Revisit if
the thesis survives.

**Dropped:** fluid milk (see above). Confectionery was the runner-up for a low slot — Aman's edge
scores 5 there on his ITC chocolate background — and returns if the low end needs testing.

---

## D11 · Design stance: best-case-first, not spanning
**Date:** 2026-09-17 · **explicit tradeoff, Aman accepted**

**Decision.** Concentrate on the tier where data most likely exists, rather than sampling across the
gradient.

**Why.** Sharper and cheaper for a one-day budget: if data is not digital even in dairy and retort
canning — where the law mandates recording — the thesis is dead everywhere. A strong kill test.

**What is given up.** We will not learn whether the thesis generalises downward to dry processes
(bakery, snacks, confectionery, dry blending). If it passes here, that becomes the next question
rather than an answered one.

**Reverse if.** The three niches all show digital, accessible data — then the open question becomes
generalisability, and the next sample should deliberately include a low-regulation dry process.

---

## D12 · Division of labour: Aman runs all interviews; Claude desk only
**Date:** 2026-09-17 · **Aman's call**

**Decision.** Claude produces desk research and an interview kit. Aman runs every call.

**Consequence.** Q3 tests ③ (paid) and ④ (pooled) cannot be closed at desk — both need a buyer or a
plant to answer — so they carry forward as call targets, not findings.

---

## Standing caveat that could invalidate D8 and D10

**A mandated recording chart can be a paper circle in a drawer.** That satisfies the law and is
worthless as data. Regulation proves the measurement is *taken*; it does not prove it is *digital*.
This is the single largest risk in the niche screen, it cannot be resolved from a desk, and it is
question one for Aman's calls. If the answer is "paper," the business starts at acquisition, not
contextualization — which is D2's first layer, so the thesis survives but the product changes.

---

## D13 · Dual data capture model: machine telemetry + humanoid robotics training data
**Date:** 2026-09-21 · **Aman's input** · **Board line:** scope header & new business model

**Decision.** In mapping every process flow, track two distinct data layers:
1. **Layer A (Machine Telemetry / Process AI):** Slow process readings, fast physics, and batch metadata to solve shop-floor quality, energy, and FDA compliance.
2. **Layer B (Humanoid Robotics Training Data):** Identify specific high-dexterity, spatial, or heavy manual tasks (sorting, tamping, crate divider loading, seam teardown inspection, palletizing) that can be recorded via wearable capture gear (smart glasses / egocentric video, haptic gloves) and sold to frontier humanoid robotics labs (Adarsh's column / Figure, 1X, Tesla Optimus).

**Why.** Food manufacturing has high human dexterity demands in unstructured, wet, and variable environments—the exact data frontier robotics labs lack. Monitored workers wearing capture kits convert a manual factory bottleneck into a high-margin data asset.

**Reverse if.** Plant managers or labor unions forbid wearable recording devices on food safety, privacy, or biosecurity grounds.
