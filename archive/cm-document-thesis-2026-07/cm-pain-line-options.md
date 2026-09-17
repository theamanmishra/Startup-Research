# Industry pain line — options for the frozen email body

The line completes: *"Among the issues that come up repeatedly in our research is ___."*
It is the same in every email, so it must be true of almost every US food/CPG co-man.

Evidence gathered 2026-07-28. Search quota hit mid-sweep, so options F–H rest on thinner
sourcing than A–C; that is marked per option, not smoothed over.

---

## A. Forecast volatility eats capacity `[currently in the script]`

> the challenge of planning a shared plant around customer forecasts that keep moving, because the co-manufacturer absorbs the cost of the idle line and the extra changeover, not the brand

**Who nods:** owner, COO, plant manager.
**Evidence:** "Co-packers often juggle multiple customers with shifting forecasts, promotions, and seasonal spikes… aligning production orders with material availability and ship dates a daily challenge" (https://erpsoftwareblog.com/2026/07/co-packing-and-co-manufacturing-in-food-beverage-where-the-model-breaks-and-how-dynamics-365-business-central-can-help/); "Demand volatility and short production runs are common" (https://snackteva.com/co-packer-problems/).
**Why it works:** it is the co-man's own P&L, caused by someone else's data.

## B. A new customer takes more than a year to pay back

> how long it takes a new customer to pay for itself, because the trials, the line time, and the paperwork all come before the first full run

**Who nods:** owner, CFO.
**Evidence:** "In most cases, the onboarding costs associated with bringing you in aren't paid back in the first year" (https://www.catapultserv.com/blog-list/the-secret-to-succes-with-contract-manufacurers).
**Why it works:** it names a number the owner already knows and no vendor ever mentions. Strongest "how did you know that" candidate.

## C. Customer-owned material sitting in the plant

> keeping track of customer-owned ingredients that sit at the plant for weeks, because the material belongs to the brand while the cost of holding and reconciling it sits with the manufacturer

**Who nods:** COO, materials/purchasing, CFO.
**Evidence:** "brand-owned ingredients may sit at a co-packer's facility for weeks while co-packers need to keep customer-specific materials separated" (erpsoftwareblog, as above).

## D. Runs keep getting smaller

> how much line time goes to changeovers as customers order smaller and more frequent runs

**Who nods:** plant manager, COO.
**Evidence:** same two sources as A. Narrower than A — a subset of it, sharper for a plant person, weaker for an owner.

## E. Off-spec runs and who pays

> what happens when a run comes off spec, because the rework and the argument about who pays for it both land on the manufacturer

**Who nods:** quality director, owner.
**Evidence:** "The biggest issue in a co-packing relationship often happens when the co-packer delivers a product that deviates from specifications" (https://snackteva.com/co-packer-problems/). Note the source writes from the *brand's* side; the "who pays" half is our reading, not a quoted claim.

## F. Concentration `[thinner]`

> how much of a plant's output depends on a few customers, because capacity is committed long and the contracts are usually short

**Who nods:** owner, CFO. Also the most likely to feel intrusive from a stranger.
**Evidence:** generic corporate-finance thresholds (single customer >15% of sales, top five >25% = significant risk), not co-man-specific reporting. `[UNVERIFIED for this industry]`

## G. Knowledge walking out the door `[half-sourced]`

> how much of a plant's setup and troubleshooting knowledge sits with a few long-serving operators, because hiring has become harder and none of it was written down

**Who nods:** owner, plant manager.
**Evidence:** CPA 2025 State of the Industry names labor shortages and a widening skills gap (https://www.contractpackaging.org/state-of-the-industry-report). The "never written down" half is our inference. `[Hypothesis — confirm with an operator before relying on it]`

## H. Quoting work that never runs `[thinnest]`

> how much work goes into quoting a job that may never run, because every inquiry needs a costed line rate before anyone knows whether the brand will launch

**Who nods:** owner, sales lead.
**Evidence:** quoting friction referenced in passing (folio3, catapultserv) but no direct source on unpaid quoting volume at food co-mans. `[UNVERIFIED]`

---

## Recommendation

**A** is the safest default: best-sourced, universal, and squarely the reader's own money.
**B** is the highest-upside test: most specific, most likely to earn a reply from an owner, and
it opens the same conversation (capacity, planning, cost of new work) from a different door.

Worth running as an A/B: same targets, two batches, compare reply rates in the tracker.
Changing this line means editing `BODY` in `.claude/skills/outreach/outreach_build.py`.
