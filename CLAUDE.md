# Startup Problem-Statement Engine — working repo

Structured startup-ideation for Aman (ex-ITC CPG supply chain & ops, HBS MBA, AI-native builder). The methodology, industry running order, and founder-edge filter live in `problem-statement-engine.md`, `industry-priorities.md`, and `founder-profile.md`. **Read all three before any research task.** This file adds the operating discipline learned from prior runs.

## Files

**Method (stable):**
- `problem-statement-engine.md` — the MAP + EVALUATE methodology. Edit only when explicitly asked.
- `industry-priorities.md` — which verticals to map, in what order.
- `founder-profile.md` — the edge filter for scoring. Note the Bespoke IP / invention-assignment constraint on anything in the AI-data space.
- `inventory.csv` — raw problem pool (all harvested problems, unfiltered).
- `tracker.csv` — scored candidates only.

**`manu-data-layer/` — ACTIVE thesis (since 2026-09).** Shop-floor data layer for mid-market US F&B
manufacturers: acquisition and contextualization of machine telemetry, not storage. Aman's
workstream; Adarsh runs the parallel "selling data to frontier/neo labs" column. Plan and locked
whiteboard in `mdl-research-plan.md`. **Aman runs all interviews himself — Claude does desk research
only.** Files prefixed `mdl-`.

**`contract-manufacturing/` — live segment data** (survives the thesis change):
- `cm-companies.csv` — the 1,155-firm D&B-derived frame, now carrying `subsegment_p1` / `p1_basis` / `coman_in_desc`. **Provenance warning:** the original export's filter settings are lost; the frame is inferred to be US food/bev manufacturers with a ~$20M revenue floor, so the $10–20M slice is missing.
- `research-2026-09-10-coman-subsegment-classification.md` · `research-2026-09-11-census-universe-counts.md` — sub-segment taxonomy and exact SUSB 2022 firm counts by receipts band.
- `cm-market-structure.md` · `cm-arena.md` · `cm-operator-voice.md` — market sizing, July arena map, operator quotes.

**`archive/` — superseded, kept for provenance and reusable evidence.** See `archive/README.md`
before citing anything from it. `cm-document-thesis-2026-07/` holds the parked document/paperwork
thesis (and the canonical co-man operating loop: win work → plan → make → prove → settle);
`fnb-run-2026-07/` holds the completed F&B industry map.

Raw sweep notes go inside the active folder as `research-YYYY-MM-DD-topic.md`.

## Hard research rules (non-negotiable)

1. **Source gate.** Every numeric or named claim — market size, margin, regulation, competitor funding or pricing — carries an inline source URL. If no source exists, write `[UNVERIFIED]` next to the claim. Never smooth an unverified claim into confident prose.
2. **Ranges, not points.** When sources conflict, record the range and both sources. False precision is a defect.
3. **No narrative-from-structure.** Never present an inferred mechanism as an observed fact. If reasoning from industry structure to a plausible story, label it `Hypothesis:` and state what evidence would confirm or kill it. (Prior failure: claimed dark-store systems don't track batch-level expiry — inferred, wrong, stated as fact.)
4. **Problem format.** Every harvested problem = *sufferer · recurring task that fails · quantified cost*, at the operator-task level. Test: could a generic consultant write this line without sources? If yes, it is a situation, not a problem — rewrite or discard.
5. **Arena before harvest.** Map funded competitors and incumbent vendors by value-chain step *before* harvesting problems. Every inventory row gets a `nearest_funded_competitor` entry or `none found — searched: [queries used]`.
6. **Desk output is a hypothesis list.** Nothing is "validated" until it has interview evidence. Each surviving problem carries its single riskiest assumption, phrased as a Mom-Test-able question about past behavior.
7. **Self-review pass.** Before finishing any task, re-read the output against rules 1–4 and *surface* violations in a `## Review flags` section rather than silently fixing or ignoring them.
8. **Access failure = full stop, not workaround.** When Aman asks for a specific source (website, database, document) and it is inaccessible, STOP and report the exact block so access can be figured out together. Do NOT substitute a partial reconstruction (search snippets, caches, model memory) and deliver it as the result — caveats do not make a partial deliverable safe; it anchors decisions on incomplete data. (Failure case, 2026-07-26: Baker Library A–Z database list has 162 entries; the site blocked automated access; a search-index sweep surfaced 28 and was delivered as an inventory. 17% coverage, presented politely, is still wrong.) A workaround may run only after Aman has seen the blocker and explicitly approved it, and its coverage limit goes at the top of the output, not in a footnote.

## Tracker conventions

- CSVs are the source of truth. Append rows; never regenerate a file wholesale; never reuse or renumber IDs.
- ID scheme: `S{step}-{GEO}-{nn}` within a vertical. F&B IDs (`S1-IN-01` … `S7-US-xx`) are reserved — those 67 rows are pending import from the original F&B tracker xlsx once it is committed to the repo.
- Score changes require a note (what evidence moved the score).
- Scoring weights live in the rubric table in `problem-statement-engine.md` §2 Step D. The F&B run used an impact-first variant (FMF de-weighted to 5%, freed weight spread across severity, WTP, market size, whitespace); if a run uses variant weights, state them at the top of that vertical's map file.

## Learnings must land in files

Claude Code sessions have no memory of chats or of each other. Any learning that changes method — a new failure mode, a rule refinement, a scoring-weight decision — must be written into this file or the relevant vertical folder *before the session ends*. A learning that lives only in a conversation does not exist.

## Known failure modes (from the F&B run — do not repeat)

- Presenting inferred mechanisms as sourced facts.
- Generic, situation-level problem descriptions instead of operator-task-level ones.
- Whitespace-by-elimination: desk research reproduces publicly quantified pain, which is where funded competitors sit; what survives a competitive screen is "least crowded," not "most demanded." Interviews are the only path to genuinely unclaimed problems — desk work prepares them, never replaces them.
