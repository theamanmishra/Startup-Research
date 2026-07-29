# Operator voice — what co-man executives actually say hurts

Source: AlphaSense generative search report, run by Aman 2026-07-28 ("Operator Perspectives on
Margin Erosion and Operational Burdens in US Food & Beverage Contract Manufacturing"), 12 pages,
expert calls + 10-Ks + earnings transcripts. Quotes below are verbatim from that report.
Note AlphaSense's own disclaimer: the synthesis is AI-generated; the quotes carry their sources.

This is the first **operator-side** evidence in this dive. Everything before it was vendor blogs
and market reports written from the brand's side.

## 1. Unpaid work before a new customer's first real run

- **Former Director, Wildpack Beverage** (expert call, 2 Apr 2026): "Mid-market co-packers must balance flexibility and efficiency, with **onboarding new customers typically taking six to ten months** depending on product readiness."
- **Senior Director of Finance, Mars** (expert call, 29 Jan 2026): "A lot of more entrenched co-manufacturers are not going to jump up and down at the opportunity to do **$75,000 worth of R&D work** for a product that your sales team is projecting is going to run £300,000 next year."
- **Director of Sourcing & Contract Manufacturing, Conagra** (expert call, 11 Mar 2026): "their focus is, '**My line is at 87% utilized. I need that other 13%. Can this product do it for me?**' ... They're going to push back."
- **Mi3 Limited** (filing, 22 Jul 2024): "onboarding of new products is delayed partly by our customers **due to documentation burden** and resource restraints. So, a scheduled production launch for 2023 needed to be postponed to 2024."
- AlphaSense synthesis: plants suffer "severe margin degradation during initial launch phases due to trial costs, unoptimized run speeds, high scrap rates, and significant unbilled line time."

## 2. Unbilled plant time — sanitation, flavour changeovers, maintenance

- **Executive, SunOpta** (conference presentation, 13 Jan 2025): "the more that your equipment consistently runs, the more manufacturing time in a year you have… let's think about how you schedule flavors. **I love chocolate, it is the worst thing to clean out of your equipment. So schedule chocolate near your heavy intensive weekly sanitation process**, not early part of the week when you're just doing it daily. That's an example of creating manufacturing time."
- **Former Director, Wildpack Beverage**: "Contract manufacturer, their goal is to **run at 84% efficiency and be sold out for the whole 12 months**."

## 3. Forecast deviation lands on the plant

- **Max Bowman, CFO, Cal-Maine Foods** (earnings call, 1 Apr 2026): "When you have lower volumes, **the first thing that happens to you is under absorption of fixed cost**, and that was one of the major headwinds for the quarter."
- **FRX Innovations** (filing, 4 Dec 2024): "the Company is generally **challenged to request price changes when volumes differ significantly from production estimates used during the quotation stage**. If estimated production volumes are not achieved, costs incurred by the Company may not be fully recovered."
- **Boston Beer** (10-K, 24 Feb 2026), from the brand side, showing the size of the counter-mechanism: "During 2025 and 2024, the Company recorded **$21.4 million and $13.0 million** in shortfall fees" under its City Brewing and Rauch co-packing agreements.
- Operators defend with shortfall fees, underutilization fees, take-or-pay structures.

## 4. Price lag on conversion fees

- **SunOpta 10-K** (4 Mar 2026): "**In our private label contracts, the timing of pass-through pricing adjustments tends to lag impacts from cost inflation.** As a result, with private label we have greater exposure to price risk, including the impact of changing freight rates."

## 5. Material risk, obsolete packaging, off-spec

- Allocation of obsolete packaging, raw-material shrink, and ingredient expiry is "a constant point of negotiation," turning on whether the deal is **turnkey or tolling**. Under tolling the brand owns the material and absorbs obsolescence; under turnkey the plant does.
- Off-spec runs create "catastrophic financial exposure": product destruction, legal battles, disputes over testing requirements, recall liability, indemnification.
- **Former Senior Director of Operations, TreeHouse Foods** (expert call, 16 Mar 2026): "on private label margins, **virtually no capital will pay back in two years**… they kept deferring maintenance, and so many of their facilities had gotten so far behind."

---

## Which of these can AI actually address (Aman's challenge, answered honestly)

| Pain | AI-addressable? | Why |
|---|---|---|
| Price lag on conversion fees | **No** | A contract-negotiation and indexation problem. Software does not fix it. |
| Capital starvation / deferred maintenance | **No** | Needs money, not software. |
| Take-or-pay and shortfall fee design | **Weak** | Legal/commercial structuring; maybe analytics support. |
| Forecast deviation | **Partial** | Cannot fix the brand's forecast. Can improve the plant's own demand sensing across customers, and price volume risk into quotes. |
| Obsolete packaging / material risk | **Partial** | Early warning and reconciliation, not prevention. |
| Sanitation and changeover sequencing | **Yes** | The SunOpta quote is literally a scheduling heuristic held in one executive's head. Sequencing under allergen and sanitation constraints is a solvable optimization problem. |
| **Onboarding: specs, trials, documentation** | **Yes, strongest** | 6–18 months, explicitly blamed on "documentation burden". Reading brand specs, generating batch records, label and regulatory checks, tech-transfer packets. This is exactly what current models are good at. |
| **Deciding which inquiries to take** | **Yes** | The Conagra quote is a screening problem: which of these inquiries will fill my last 13% profitably? Costing an inquiry from a spec sheet is precisely what Paperless Parts does for machine shops (raised $30M Series B doing it). |

**Conclusion:** several headline pains are genuinely not AI problems, and we should not pretend
otherwise. The intersection of *real pain* and *AI-solvable* is narrow and specific: **the unpaid
work between an inquiry and the first paid run** — quoting it, ingesting the spec, producing the
documentation. That is where the email should point.
