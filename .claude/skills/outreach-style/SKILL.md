---
name: outreach-style
description: Language gate for co-manufacturer outreach prose — checks an insight clause (or any new outreach sentence) against Aman's writing rules and anti-AI-pattern checks, then returns the minimally corrected version. Called by the outreach skill at the insight step; also usable standalone on follow-up emails or call notes.
---

# Outreach style gate

Adapted from Adarsh Kumar's outreach-style skill (shared 2026-07-28), retargeted from OEM equipment makers to US food/CPG contract manufacturers.

Input: one or more candidate sentences (usually the per-company insight clause that completes "During our research, we read that at [Company], …"). Output: the corrected sentence plus a one-line list of violations fixed. Rewrite minimally — surgical changes only, never restructure a sentence that already passes.

**Never touch the frozen email body.** The template in `outreach_build.py` is Aman's verbatim and is exempt from every rule here. This gate applies only to the variable parts: insight clauses, follow-up emails, any newly written outreach prose.

## Writing rules

1. Short but COMPLETE sentences. No telegraphic fragments.
2. Show causation with plain connectives: because, so, and, while. Not em dashes.
3. State the fact and stop. No editorializing after it, no punchy closer.
4. No rhetorical scaffolding: "X is itself a finding," "the exception proves the rule."
5. No vague openers or filler: "notably," "one caveat," "honest."
6. No undefined jargon. If an industry term appears, it must be one the reader uses daily. For this audience that means: co-pack, co-man, run, changeover, line, SKU, allergen, SQF, BRC, GFSI, chargeback, deduction, yield, tolling. It does NOT mean: control tower, orchestration layer, digital thread, system of record.
7. Plain subject-verb-object for abstractions. Quantify when a number is verified.
8. Use the established term consistently; never cycle synonyms. Pick "co-manufacturing" or "co-packing" per company based on what that company calls itself, and keep it.
9. Company-level nouns only in email prose: plants, certifications, categories, customers, capabilities, acquisitions. Artifact detail (audit report numbers, specific SKU codes, URLs) is banned from emails and belongs in the tracker as proof.

## Anti-AI-pattern checks

- No em dashes or en dashes anywhere in the output. Replace with a period, comma, or restructure.
- No analysis -ing tails: highlighting, underscoring, showcasing, reflecting, ensuring, fostering.
- No rule-of-three rhythm; two items or one, unless three are genuinely enumerated facts.
- No negative parallelism: "not just X, it's Y."
- No copula avoidance: "serves as / stands as / boasts" become "is / has."
- No AI vocabulary: delve, pivotal, crucial, vital, landscape, testament, underscore, vibrant, robust, seamless, tapestry, interplay, journey.
- No promotional adjectives, no false ranges ("from X to Y" where X and Y are not a scale).
- Active voice; straight quotes; at most one specific anchor (a year, a certification, a brand) per sentence.

## Vendor-smell kill-list (instant delete for this audience)

transform, revolutionize, leverage, unlock, empower, disrupt, cutting-edge, game-changer, AI-powered, solutions (as jargon), "we'd love to help," "hop on a quick call," "pick your brain," "reach out," "circle back," "touch base," any unverified ROI number, any LLM/agent/embeddings terminology.

Food-industry-specific additions: "farm to fork," "seed to shelf," "supply chain of the future," "food safety journey," "clean label revolution."

## Procedure

1. Check the input against every rule above; list each hit.
2. Rewrite with the smallest possible change per hit.
3. Read the result aloud once: it must sound like a sentence a person typed after an evening on the company's website, not like copy.
4. Return: final sentence(s) + the violations fixed. If the input already passes, return it unchanged and say so.
