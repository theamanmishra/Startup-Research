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

An HBS student studying how contract food manufacturers run their operations and where AI helps. The reader is an owner, president, COO, plant manager, or quality director at a private, family- or PE-owned co-manufacturer or co-packer. Reply rate is the goal. Public companies route inbound through IR — skip them. Research asks reply at 15–40%; anything that smells like a vendor pitch halves it. The email names one industry issue (the manual work behind customer documentation and what a single error costs) with "Among the issues…" so the reader is not boxed in and can bring their own problem to the call.

The credibility line is short by Aman's choice: recent work at frontier AI startups, written jointly with Adarsh. The frozen body carries no ITC history. If reply rates disappoint, adding one operating line is the first thing to test.

## Data files

- `contract-manufacturing/outreach-tracker.csv` — the live status board. The script replaces a company's non-sent ranked rows and appends the new set; sent history is never touched. Ranks 1–5 = send list; 6–8 = bench, used only when a higher rank bounces.
- `contract-manufacturing/cm-companies.csv` — the ranked company universe (1,155 rows). Columns include `target_tier` (A verified co-man / B likely / C unknown), revenue, plant location, website, up to three contacts with titles/emails/phones, and `source_urls` for Tier A rows. Use it to pick companies and domains. **Treat its contact rows as leads, not facts** — they come from a D&B export and public sweeps, and every person must still pass step 3.
- Drafts: one flat folder per batch — `contract-manufacturing/outreach-drafts/<batch-date>/<slug>-<rank>-<lastname>.eml`. Spec JSONs live at `contract-manufacturing/outreach-drafts/<slug>.spec.json`.
- `send-batch.csv` in each batch folder — the same messages as one table, written by the script. Consumed by `send_drafts.ps1` (Windows + Outlook desktop) so a 50-message batch becomes one command instead of 50 double-clicks. It saves to Drafts by default and only sends with `-Send`; it writes `send-log.csv` next to it, which is what updates the tracker's `Sent?` and `Sent date`.
- **No signature in drafts.** Outlook auto-appends it on send; a signature in the body appears twice. `send_drafts.ps1` reads the signature off a fresh item and re-attaches it below the body, since assigning `HTMLBody` would otherwise wipe it.

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

**3. Double-check every person.** Two independent signals the person holds the role NOW, the fresher the better. Kill signals: an aggregator profile showing a NEW employer, "former"/"ex-", retirement coverage, an obituary. Co-mans change hands often, so also check for an acquisition that replaced leadership — our own sweep found several 2025–26 ownership changes. Run the name search (`"<first> <last>" <company>`) and read the top 5–10 results. Same pass captures: (a) **salutation**, see below; (b) **the current title verbatim**.

**Salutation.** Default is `Dear Mr. <Last>,` / `Dear Ms. <Last>,` — a courtesy title reads as a person who did the work, a bare full name reads as a mailmerge. The title must come from a **published source that states it**: the person's own bio using he/him or she/her, a press release calling them "Mr. X", an interview, an association profile. **Never infer a courtesy title from a first name** — a wrong one is worse than none, and this pipeline does not guess gender. When no source states it, fall back to `Dear <First>,`. Shared family surnames also take `Dear <First>,`. `Dear <First> <Last>,` is rejected by the script. Record the basis in the tracker Notes, e.g. `salutation: Ms. per company bio "she joined in 2019"`. **Recency bar (added 2026-07-29 after a bounce).** A contact whose most recent in-role signal is undated, older than ~18 months, or older than the company's last ownership change is **benched, not drafted**. Batch 1 lost `pbegg@lyonsmagnus.com` exactly this way: the pattern was right (`jdavis@` delivered), the person had left, and the row carried the words "no post-2024 confirmation he still holds the role" while still being drafted. Of the two failure modes — wrong address, absent person — the address bar already works and the person bar is the leak. Spend the marginal search on "is this person still there."

Single-source people get flagged and preferably benched or replaced. Off-thesis roles (HR, marketing) are excluded even when senior — log the exclusion.

**4. Pick eight, rank 1–8.** Top-down by seniority, ties broken by thesis fit: the operations owner ranks high because the frozen body's industry issue is planning and capacity, then quality/FSQA, then the co-pack sales contact, then finance (chargebacks and yield true-ups are their pain), then non-operating family. At a 40-person family co-man there may only be three or four real contacts — send fewer rather than padding with irrelevant names. Ranks below the real roster are left empty, not filled.

**5. The insight — a named pain, not a fact.** The clause sits inside the frozen carrier:

> In **[Company]**'s case, **[insight]**, and we would want to know how much of that is still manual today.

So the clause has a **required two-part shape**, and the script enforces the join word:

> **`<fact we found, in their words> so <the documentation pain it implies>`**

The first half proves we looked at them. The second half is the whole point: it names a specific piece of paperwork we think is painful, and the carrier's closing question turns that into a hypothesis we are asking them to confirm or correct. Both halves are needed. A fact alone ("you run four plants") is a website observation and reads disconnected — **this was the failure of the first 15 emails, 2026-07-29**. A pain alone is a cold generic claim.

The second half must name a **document, spec, questionnaire, audit record or approval** — not capacity, not changeovers. The frozen body's industry issue is documentation, and the two sentences have to be about the same thing.

Gates, in order:
1. **Two-part shape.** Fact `so` consequence. The consequence names a specific document artifact and a repeated action on it (rebuilt, re-entered, chased, reconciled, kept current in N places).
2. **Fact confirmed within the company** — its own capabilities page, brand list, plant list, certification listing or press release is strongest; a verified multi-source third-party record is acceptable; single-source is not. If neither exists, the company is not ready for the batch. The *consequence* half is our inference and does not need a source, because the carrier asks rather than asserts — but it must follow from the fact a reader would recognise, not from a generic industry story.
3. **Painful at senior-management altitude** — hours of skilled time, a launch that slips, an audit finding, an error with a customer's name on it. Not "you have many SKUs".
4–5. **Invoke the `outreach-style` skill** on the clause — it returns the corrected clause.

Worked examples, both halves marked:

| Company | Fact | `so` consequence |
|---|---|---|
| City Brewing | you co-pack seltzer, beer and RTDs across four plants | one customer's specification has to be kept current in four separate sets of paperwork |
| Carolina Foods | you bake your own Duchess line alongside private brands on the same equipment | a single recipe change has to be written up twice, once your way and once the brand owner's |
| Blount | you run other companies' brands in the plants where you make Blount's Family Kitchen | the audit evidence for one line has to be reshaped for whichever owner is asking |

Same clause for all contacts at that company; personalization is per-company, never per-individual.

**6. Assemble by script.** Write the spec JSON (format in the script docstring), then from the project root run:
`python3 .claude/skills/outreach/outreach_build.py contract-manufacturing/outreach-drafts/<slug>.spec.json`
Spot-check one generated `.eml`. The proof pointer never enters an email.

**7. Report.** Pattern status (double-confirmed or flagged), the contacts with ranks and flags (single-source, neutral salutation, weak recency), who was dropped and why, the insight clause with proof URLs, file paths, bounce-test inbox, competitor caveats. Log durable findings (for example "this co-man publishes no quality contact at all") in the vertical's research notes.

## Loop mode and follow-ups

"Run the loop on N companies": one company agent each, ~5 concurrent, stop and report after every batch of ~5 so Aman sends before the next batch starts. Follow-ups: ~3 / 10 / 17 days after the first touch, stop after 3 — new follow-up prose goes through the `outreach-style` skill first. Honor any opt-out immediately and permanently, and record it in the tracker Notes.
