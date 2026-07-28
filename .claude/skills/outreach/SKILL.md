---
name: outreach
description: Run the contract-manufacturer cold-outreach pipeline — one sub-agent per company double-confirms ranked decision-makers, the email pattern, and one company insight; the insight passes the outreach-style skill; drafts are assembled by outreach_build.py (the body is frozen script text, never LLM-typed) and logged to outreach-tracker.csv. Use when asked to "run outreach on <company>", "prepare emails for <company>", or "run the outreach loop".
---

# Contract-manufacturer outreach pipeline

Adapted from Adarsh Kumar's OEM outreach package (shared 2026-07-28), retargeted from equipment makers to US food/CPG contract manufacturers. Self-contained 3-file package:
- `SKILL.md` (this file) — the pipeline.
- `outreach_build.py` (same directory) — the FROZEN email body and the draft/tracker generator. The body text lives ONLY there; read its `BODY` constant to see it, never retype it.
- `../outreach-style/SKILL.md` — the language gate; invoke the `outreach-style` skill on every insight clause and any new outreach prose.

Per company the output is: up to eight double-confirmed contacts ranked 1–8, one insight clause, the matching `.eml` drafts, rows in `outreach-tracker.csv`. **Never send anything — Aman sends from Outlook.**

**Email is the only channel.** Aman does not cold-call. A company with no confirmable email pattern is parked, not phoned. This makes step 1 the critical path: most addresses are DERIVED from a confirmed pattern, not looked up. `cm-companies.csv` holds a real address for only 139 of 1,155 companies, but 1,080 have a website, so the pattern is confirmable for most of the universe. A company is workable when its domain yields two verbatim published addresses; it is parked when it does not.

## The approach (why these targets, this frame)

An HBS student studying how contract food manufacturers run their operations and where AI helps. The reader is an owner, president, COO, plant manager, or quality director at a private, family- or PE-owned co-manufacturer or co-packer. Reply rate is the goal. Public companies route inbound through IR — skip them. Research asks reply at 15–40%; anything that smells like a vendor pitch halves it. The email names one industry issue (every brand customer audits the same plant against its own paperwork) with "Among the issues…" so the reader is not boxed in and can bring their own problem to the call.

Aman's credibility line is operational, not academic: five years at ITC in manufacturing, planning, and distribution. Keep it that way; it is the reason a plant person answers.

## Data files

- `contract-manufacturing/outreach-tracker.csv` — the live status board. The script replaces a company's non-sent ranked rows and appends the new set; sent history is never touched. Ranks 1–5 = send list; 6–8 = bench, used only when a higher rank bounces.
- `contract-manufacturing/cm-companies.csv` — the ranked company universe (1,155 rows). Columns include `target_tier` (A verified co-man / B likely / C unknown), revenue, plant location, website, up to three contacts with titles/emails/phones, and `source_urls` for Tier A rows. Use it to pick companies and domains. **Treat its contact rows as leads, not facts** — they come from a D&B export and public sweeps, and every person must still pass step 3.
- Drafts: one flat folder per batch — `contract-manufacturing/outreach-drafts/<batch-date>/<slug>-<rank>-<lastname>.eml`. Spec JSONs live at `contract-manufacturing/outreach-drafts/<slug>.spec.json`.
- **No signature in drafts.** Outlook auto-appends it on send; a signature in the body appears twice.

## Orchestration — divide and conquer

The **orchestrator** is whoever is running this skill for a company. **The orchestrator MUST spawn sub-agents for the research — never grind through the searches itself.** Spawn via the Agent tool (subagent_type: general-purpose), run them concurrently, WebSearch/WebFetch only. Typical split: (a) email pattern + general inboxes, (b) roster of 10–12 candidates; then, once (b) returns: (c) double-check contacts 1–6, (d) double-check contacts 7–12, (e) insight artifact hunt. Sub-agents return raw verdicts with claim + URL pairs and never write files.

The orchestrator itself does the judgment and the writes: reviews verdicts, sets ranks, picks the insight and runs it through the `outreach-style` skill, writes the spec JSON, runs `outreach_build.py`, and returns the report.

**Environment note:** WebFetch is currently blocked in the cloud session (403 on every host). Until that is fixed, sub-agents can only use WebSearch, which weakens step 1 and step 5 badly — a company whose pattern cannot be double-confirmed gets flagged, not guessed. If the block persists, run this skill from a local session instead.

**Tracker safety:** each script run rewrites the whole tracker — never let two `outreach_build.py` invocations overlap. When several companies finish together, run their invocations one after another.

## Definition of done (per company)

1. `contract-manufacturing/outreach-drafts/<slug>.spec.json` exists and the script ran once, successfully.
2. The `.eml` files exist and `outreach-tracker.csv` carries the company's ranked rows.
3. The step-7 report is returned. Not done until all three hold.

## Steps per company

**0. Choose.** User-named, else the highest-ranked `cm-companies.csv` rows not yet in the tracker, Tier A first, preferring rows that already carry a real email (the pattern is then free) and otherwise rows with a website. Skip public companies. Skip rows with no website — there is no path to an address. Check the tracker for a direct competitor contacted the same week — if so, never mention one to the other, and avoid insights whose natural reply is "who else are you talking to?"

**1. Email pattern — double-confirmed.** Confirmed = TWO verbatim-published `@domain` addresses agreeing (press releases, PDF spec sheets, association profiles, certification directories, trade-show exhibitor pages, FDA/USDA registration documents), aggregator claims as support only. One verbatim or aggregator-only = flagged in the report. Always collect general inboxes (`info@`, `sales@`, `quality@`) — Aman sends a parallel test to one to catch bounces on inferred addresses.
Note: `cm-companies.csv` already carries real addresses for 139 companies, lifted from the D&B export. A published address there proves the pattern; it does NOT prove the person still holds the role.

**Deriving addresses.** Once the pattern is double-confirmed, construct addresses for the ranked contacts from it and mark each `basis` as `derived from confirmed pattern {f}{last}@`. Never derive from a single published address, and never derive from a pattern guessed off the domain alone. If only one verbatim address exists, send to that person only and bench the rest, or park the company. A derived address always ships alongside the parallel general-inbox test so a bad derivation surfaces as a bounce on a known-good address.

**2. Roster, top-down.** 10–12 candidates so eight survive: Owner/President/CEO, family owners in leadership, COO/CFO, VP Operations, Plant Manager, then Director of Quality / Food Safety / FSQA, Director of Sales or Business Development (the person who fields co-pack inquiries), R&D or Product Development. Each with exact title, source URL, date of most recent in-role signal.

**3. Double-check every person.** Two independent signals the person holds the role NOW, the fresher the better. Kill signals: an aggregator profile showing a NEW employer, "former"/"ex-", retirement coverage, an obituary. Co-mans change hands often, so also check for an acquisition that replaced leadership — our own sweep found several 2025–26 ownership changes. Run the name search (`"<first> <last>" <company>`) and read the top 5–10 results. Same pass captures: (a) **salutation** — a published source using he/she for the person; never infer from a name; no source = `Dear <First> <Last>,`; shared family surnames = `Dear <First>,`; (b) **the current title verbatim**. Single-source people get flagged and preferably benched or replaced. Off-thesis roles (HR, marketing) are excluded even when senior — log the exclusion.

**4. Pick eight, rank 1–8.** Top-down by seniority, ties broken by thesis fit: the quality/FSQA owner ranks high because the frozen body's industry issue is audit duplication, then operations, then the co-pack sales contact, then finance (chargebacks and yield true-ups are their pain), then non-operating family. At a 40-person family co-man there may only be three or four real contacts — send fewer rather than padding with irrelevant names. Ranks below the real roster are left empty, not filled.

**5. The insight — one clause, five gates.** The clause completes the frozen carrier "During my research, I read that at [Company], …". Dig at artifact level (certification directories, capabilities pages, customer/brand lists, plant lists, press releases, acquisition history); write at company level. Gates, in order:
1. **Marries the industry issue** — it is the audit/quality-proof problem showing up at this company, so the reader connects it to the previous sentence without help.
2. **Confirmed within the company** — the company's own artifact (its capabilities page, its certification listing) is strongest; a verified multi-source third-party record is acceptable; single-source is not. If neither exists, the company is not ready for the batch.
3. **Painful at senior-management altitude** — a P&L sentence (margin at risk, capacity lost to non-production work, knowledge living in one person's head), not a website observation.
4–5. **Invoke the `outreach-style` skill** on the clause — it returns the corrected clause.
Worked example: "you run co-packing for retail and foodservice brands across three SQF-certified plants" — company-level, verifiable from the company's own site, and it sets up the audit-duplication issue without stating it. Same clause for all contacts at that company; personalization is per-company, never per-individual.

**6. Assemble by script.** Write the spec JSON (format in the script docstring), then from the project root run:
`python3 .claude/skills/outreach/outreach_build.py contract-manufacturing/outreach-drafts/<slug>.spec.json`
Spot-check one generated `.eml`. The proof pointer never enters an email.

**7. Report.** Pattern status (double-confirmed or flagged), the contacts with ranks and flags (single-source, neutral salutation, weak recency), who was dropped and why, the insight clause with proof URLs, file paths, bounce-test inbox, competitor caveats. Log durable findings (for example "this co-man publishes no quality contact at all") in the vertical's research notes.

## Loop mode and follow-ups

"Run the loop on N companies": one company agent each, ~5 concurrent, stop and report after every batch of ~5 so Aman sends before the next batch starts. Follow-ups: ~3 / 10 / 17 days after the first touch, stop after 3 — new follow-up prose goes through the `outreach-style` skill first. Honor any opt-out immediately and permanently, and record it in the tracker Notes.
