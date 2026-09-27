---
name: ip-deck
description: Build the weekly PowerPoint update for Aman's HBS Independent Project with Prof. Kris Ferreira ("Market Study for Manufacturing AI") — house style, diagram-led slides, self-explanatory prose, and a render-and-look verification pass. Use this whenever Aman asks for the weekly/IP update, an update deck or slides for Prof. Ferreira, a progress deck for the independent project, or says "make this week's update". Also use it when editing or restyling an existing IP update deck, and as the deck template for any other slides he needs from this repo. Do not hand-roll a deck from scratch — the format below was settled over several painful rounds of revision and the scripts here encode it.
---

# Weekly IP update deck

Aman **sends** this deck; he usually does not present it. That single fact drives
almost every rule below. There is no voice track to carry the meaning, no chance
to answer a question, and the reader — a TOM professor supervising the project,
not a food-manufacturing specialist — has only what is on the slide.

Two files do the mechanical work:

- `deckkit.py` — palette, grid, text measurement, and the shape helpers
  (`titlebar`, `box`, `chev`, `arrow`, `band`, `barchart`, `caption`, `eyebrow`).
  Import it; do not rebuild a layout system.
- `render_check.py` — overflow check plus PNG render of every slide. Run it on
  every draft before showing Aman anything.

## The ten-minute version

1. Read `../../../CLAUDE.md`, plus `manu-data-layer/mdl-decision-log.md`,
   `mdl-sources.md` and whatever research file covers the week's work. **Check
   `origin/main` as well as the current branch** — work often lands there from a
   parallel session, and presenting stale findings is worse than presenting none.
2. Agree the slide-by-slide flow with Aman before writing any code. He thinks in
   flows and will usually hand you one.
3. Write a build script that imports `deckkit`, save the `.pptx` to the scratchpad.
4. Run `render_check.py`, **read the PNGs**, fix, repeat until clean.
5. Send the file with `SendUserFile`. Say what you changed and flag judgment calls.

## Writing for a reader who is not in the room

This is where every revision round has been spent. The deck is not a set of
labels; it is an argument someone reads alone.

**Every term gets unpacked where it appears.** Not in a glossary, not in the
speaker notes — in the sentence. A slide that says `Regulation 30` has told the
reader nothing. The version that works:

> **Regulation 30** — *Does the law force the plant to record process readings?*
> Heaviest weight, and the reason for the whole screen. Where a rule requires a
> temperature or pressure to be recorded, the measurement provably happens.
> Where no rule exists, there may be no data at all.

The pattern is **name → the question it asks → why it matters**. Apply it to
jargon of every kind: `311421` becomes "industry code 311421", `21 CFR 113`
becomes "FDA 21 CFR 113 — canned low-acid food", "retorting" becomes "cooking
food inside sealed cans in a giant industrial pressure cooker". Assume the
reader knows operations and statistics, and knows nothing about food plants,
FDA rules, NAICS codes or the vendor landscape.

**Every figure carries its "why" underneath.** A funnel showing 51 → 25 → 3 is
decoration until a caption says what was counted and what the filters were. A
bar chart of weights is meaningless until each bar says what it measures. If a
figure needs no caption it is probably too obvious to earn its slide.

**Close the loop back to the argument.** The worst slide in the last round put
three niche cards under a scoring criterion without saying what each niche's
rulebook actually forces a plant to record — so the cards never connected to
the criterion that selected them. When a slide introduces a rule, show the rule
being applied.

**Put the conclusion on the slide, not in the notes.** In a meeting Aman would
say "and this cuts against my own hypothesis" out loud. In a sent deck it has
to be written down, usually as a dark `band(...)` so a skimming reader lands on
it. Speaker notes are a backup for the live conversation, never the place where
meaning lives.

**Keep the project's evidence rules visible.** `CLAUDE.md` governs: sourced
claims carry their source, unsourced ones say `[UNVERIFIED]`, inferences are
labelled `Hypothesis:` with what would kill them, and nothing is "validated"
before an operator has said it. On a deck this shows up as a source line under
a figure and an honest status band — e.g. "no plant operator has confirmed any
of this." Aman wants the caveats visible; they are part of the argument, not a
hedge to be smoothed away.

## The look

Plain, high-contrast, no ornament. It should read like a careful analyst's work,
not a consulting pitch.

- **16:9**, Arial throughout, side margin `MX`, content width `CW`.
- **Full-bleed dark navy title bar** at the top of every content slide, white
  bold 22pt, centred. Number the slides (`3.  Narrowing, part 2: …`) so Aman and
  his supervisor can refer to one in an email.
- **Palette** (all in `deckkit`): `NAVY` for the bar and for the one conclusion
  per slide; `STEEL` as the primary accent and for eyebrow labels; `RUST` for
  the critical or surprising item; `TEAL` as the third category colour; `LIGHT`
  card fills on white; `MUTED` for explanatory prose.
- **Colour means something.** When three options are introduced in one colour
  each, keep those colours for the rest of the deck.
- Prose sizes: 13pt for a lead sentence, 11–12pt for explanation, 9.5–10pt for
  sources and captions. Below 9pt is unreadable when emailed.
- Leave the bottom ~0.4in of the slide empty. `BODY_BOTTOM` marks the line.

## Slide patterns that work

| Purpose | Pattern |
|---|---|
| A sequence of stages | `chev()` chevrons across, sub-label inside each |
| Narrowing / filtering | boxes with a big number, `arrow()` between, filter caption beneath each arrow |
| Weighted criteria | `barchart()` — bar, name, the question it asks, why it matters |
| A layered stack | full-width `box()` per layer, `arrow('down')` between, what flows down labelled in italic |
| A process line | stacked `box()`es, the critical step filled `RUST`, stakes called out beside it |
| Comparing options | equal columns, coloured header band, body, and a "Difficulty:" line in the column's own colour |
| The takeaway | full-width dark `band(..., dark=True)` |

A summary box on the title slide ("the update in one minute") is worth its space
in a deck that arrives by email — it lets the reader know the shape of the
argument before slide 2.

`reference-2026-09-21.pptx` in this directory is the deck Aman actually sent —
the worked example of everything above. Open it (or render it) when you want to
see a pattern rather than read about one.

## Verify before you show him

```bash
python3 .claude/skills/ip-deck/render_check.py <deck.pptx>
```

It prints a geometric overflow report and writes `slideNN.png` per slide. Then
**Read every PNG**. The script catches text spilling out of a card and anything
running off the slide; it cannot see two shapes colliding, a column that reads
as crowded, or a diagram that is simply wrong. Those are the failures that make
a deck look shabby, and looking is the only way to find them.

Flags of ~0.1in on a card are usually the deliberate over-measurement in
`deckkit` (it measures against DejaVu, which is wider than the Arial PowerPoint
will use). Confirm against the PNG rather than reflexively resizing.

If `soffice` reports "source file could not be loaded" for every file, Impress
is missing from the image:

```bash
apt-get update -q && apt-get install -y -q libreoffice-impress
pip install python-pptx pypdfium2 pillow
```

## Traps already paid for

- **Do not build a bespoke layout engine.** An early round produced a beautiful
  measured-typography system and Aman's reaction was that it was over-worked.
  `deckkit` is the settled level of machinery.
- **Do not answer "simplify" with default bullet placeholders.** The round after
  that dumped paragraphs into `slide_layouts[1]` and text ran off the slide. The
  fix for over-design is diagrams with less text, not the built-in template.
- **Do not leave bare codes or acronyms anywhere.** This has been the single
  most repeated correction.
- **Do not reuse a deck's speaker notes as the place for the point.**
- **Ask about the flow, don't invent it.** Aman knows what story he wants told.
  Ask for the slide-by-slide outline, then argue with it if something is missing.

## Project facts that recur

Aman Mishra, MBA 2027. Supervisor Prof. Kris Ferreira, Technology & Operations
Management. "Market Study for Manufacturing AI", 3 credits / 90 hours,
11 Sep – 11 Dec 2026, so every deck can carry a "Week N of 13" line. Deliverable
on 11 December is a written market study: operating map with cost structure,
vendor landscape, interview findings on adoption and budget ownership, and three
to five opportunity theses each with its riskiest assumption and kill criterion.
Background worth citing once: five years running manufacturing and supply chain
at ITC, a large food company, then work at an AI startup on data curation.
