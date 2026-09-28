# -*- coding: utf-8 -*-
"""Weekly IP update — 28 Sep 2026. Built with the ip-deck house toolkit."""
import sys
sys.path.insert(0, '/home/user/Startup-Research/.claude/skills/ip-deck')
from deckkit import *
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = new_deck()

def lh(pt, f=1.22):
    return int(pt * f * 12700)

# ============================================================ 1 · TITLE
s = slide(prs, bg='222A35')
txt(s, MX, 700000, CW, 300000,
    [{'t': 'HBS INDEPENDENT PROJECT  ·  WEEK 3 OF 13  ·  28 SEPTEMBER 2026',
      'size': 11.5, 'bold': True, 'color': RGBColor(0x8F,0xA8,0xC4)}])
txt(s, MX, 1060000, CW, 900000,
    [{'t': 'Market Study for Manufacturing AI', 'size': 34, 'bold': True, 'color': WHITE}])
txt(s, MX, 1600000, CW, 400000,
    [{'t': 'Aman Mishra   ·   supervisor: Prof. Kris Ferreira, Technology & Operations Management',
      'size': 12, 'color': RGBColor(0x8F,0xA8,0xC4)}])

box(s, MX, 2180000, CW, 3560000, [], fill=RGBColor(0x2C,0x36,0x43), line=None)
txt(s, MX + 300000, 2330000, CW - 600000, 300000,
    [{'t': 'THE UPDATE IN ONE MINUTE', 'size': 11, 'bold': True, 'color': RGBColor(0xC9,0x8A,0x6E)}])
pts = [
 ('Completed a detailed market analysis.', 'Studied 163 companies across industrial automation, industrial data '
  'infrastructure and manufacturing AI, and classified them into clean, non-overlapping buckets based on what each one '
  'actually does to a plant\u2019s data.'),
 ('The map locates the opportunity.', 'Six of the seven buckets have an entrenched owner. The one that does not is joining a '
  'machine reading to the batch it belongs to, at a price a mid-sized plant can pay.'),
 ('Mapped what a plant decides, and how it decides it today.', 'Five recurring decisions on a canned-food line, made on paper '
  'chart recorders, by destroying three cans every few hours, and by reconstructing events over several days.'),
 ('What the published evidence cannot give is the ROI.', 'Read 36 vendor case studies. Every food example is a '
  'multi-billion-dollar manufacturer, none the size of the target, and not one states what the decision cost before the '
  'software went in.'),
 ('So the next phase is primary work.', 'Contact manufacturers to run pilots, and approach the companies already in this market '
  'to learn how they sell, deploy and price.'),
]
py = 2680000
for head, body in pts:
    txt(s, MX + 300000, py, CW - 600000, lh(11.5),
        [{'t': head, 'size': 11.5, 'bold': True, 'color': WHITE}])
    bh = text_h(body, 10.5, CW - 600000, 10.5 * 1.35)
    txt(s, MX + 300000, py + lh(11.5) + 8000, CW - 600000, bh,
        [{'t': body, 'size': 10.5, 'color': RGBColor(0xB4,0xC0,0xCC), 'lh': 1.35}])
    py += lh(11.5) + bh + 130000

# ============================================================ 3 · MARKET MAP
exec(open('/home/user/Startup-Research/manu-data-layer/deck/_map_slide_body.py').read())

# ============================================================ 4 · DECISIONS
s = slide(prs)
titlebar(s, '2.  Which decisions — and how a plant makes them today')

txt(s, MX, 880000, CW, 260000,
    [{'t': 'FIVE DECISIONS FROM ONE PROCESS: CANNED LOW-ACID FOOD, THE NICHE MAPPED IN MOST DEPTH',
      'size': 10.5, 'bold': True, 'color': STEEL}])

DEC = [
 ('Can I release this batch?',
  'QA manager',
  'Reads a circular paper ink chart from the pressure cooker, cross-checked by eye against a mercury thermometer on the vessel.',
  '10,000 cans per cook. If the heat profile is doubted the batch is held, retested or re-cooked.'),
 ('Is the can seamer drifting?',
  'QA technician',
  'Three cans cut open and measured with a micrometer every 2–4 hours. Between checks there is no measurement at all.',
  'A bad seal lets bacteria in after cooking. This is the botulism path, and the recall exposure.'),
 ('Was the filling temperature right?',
  'Line operator',
  'A handheld thermometer dipped every 30–60 minutes, written on a paper log.',
  'If broth cooled during a line stoppage the whole subsequent cook is under-processed.'),
 ('Which batch is in which basket?',
  'Retort operator',
  'A paper tag hung on the cart.',
  'Sets how wide a recall has to be drawn when something is wrong.'),
 ('Why did this batch come out wrong?',
  'Process engineer',
  'Reconstructed afterwards from paper charts, batch sheets and lab results.',
  'Vendors report this dropping from days to hours — the one effect that recurs across every case study I read.'),
]
hdr_y = 1220000
COLW = [2650000, 1250000, 3900000, 3386160]
heads = ['THE DECISION', 'WHO MAKES IT', 'HOW IT IS MADE TODAY', 'WHY IT MATTERS']
box(s, MX, hdr_y, CW, 300000, [], fill=NAVY, line=None, shape=MSO_SHAPE.RECTANGLE)
cx = MX
for h, w in zip(heads, COLW):
    txt(s, cx + 140000, hdr_y + 62000, w - 200000, lh(9.5),
        [{'t': h, 'size': 9.5, 'bold': True, 'color': WHITE}])
    cx += w

ry = hdr_y + 300000
for dec, who, how, why in DEC:
    hh = max(text_h(how, 9.5, COLW[2] - 240000, 12.8),
             text_h(why, 9.5, COLW[3] - 240000, 12.8),
             text_h(dec, 10, COLW[0] - 240000, 13.5)) + 150000
    box(s, MX, ry, CW, hh, [], fill=WHITE, line=BORDER, shape=MSO_SHAPE.RECTANGLE)
    cx = MX
    vals = [(dec, 10, True, NAVY), (who, 9.5, False, MUTED), (how, 9.5, False, INK), (why, 9.5, False, INK)]
    for (v, sz, bd, colr), w in zip(vals, COLW):
        txt(s, cx + 140000, ry + 75000, w - 240000, hh - 120000,
            [{'t': v, 'size': sz, 'bold': bd, 'color': colr, 'lh': 1.35}])
        cx += w
    ry += hh

band(s, ry + 110000, 'THE COLUMN THAT IS MISSING',
     'There is a fifth column this table should have — what each decision costs the plant today, in held inventory, wasted '
     'batches and engineer-days. I could not source a single figure for it at mid-market scale. The next two slides show why.',
     dark=True, size=11.5, line=16.5)

# ============================================================ 5 · THE EVIDENCE
s = slide(prs)
titlebar(s, '3.  What the published evidence actually is — 36 case studies read as a body')

txt(s, MX, 880000, CW, 260000,
    [{'t': 'EVERY QUANTIFIED RESULT I COULD FIND FROM THE VENDORS ON THE MAP, GROUPED BY THE INDUSTRY IT CAME FROM',
      'size': 10.5, 'bold': True, 'color': STEEL}])

BARS = [('Oil, gas & petrochemical', 7, STEEL, '', ''),
        ('Pharma & biotech', 6, STEEL, '', ''),
        ('Automotive & discrete', 6, STEEL, '', ''),
        ('Food & beverage', 5, RUST, '', ''),
        ('Chemicals', 3, STEEL, '', ''),
        ('Pulp, paper & packaging', 2, STEEL, '', ''),
        ('Steel, cable, ethanol', 3, STEEL, '', '')]
by = 1230000
top = max(b[1] for b in BARS)
for name, val, col, _, _ in BARS:
    box(s, MX, by + 40000, int(1850000 * val / float(top)), 150000, [], fill=col, line=None,
        shape=MSO_SHAPE.RECTANGLE)
    txt(s, MX + 1930000, by - 20000, 2600000, lh(10),
        [{'t': '%s   %d' % (name, val), 'size': 10, 'bold': True, 'color': NAVY}])
    by += 310000

box(s, MX + 4700000, 1180000, CW - 4700000, 2200000, [], fill=RUST_L, line=RUST, lw=1.5)
txt(s, MX + 4920000, 1290000, CW - 5140000, lh(12),
    [{'t': 'THE FOOD CASES ARE ALL THE WRONG SIZE', 'size': 12, 'bold': True, 'color': RUST}])
txt(s, MX + 4920000, 1290000 + lh(12) + 40000, CW - 5140000, 1600000,
    [{'t': 'The five food and beverage cases are Kellogg’s, PepsiCo, Barilla, Lindt and one unnamed large CPG. Every one is a '
           'multi-billion-dollar manufacturer, between ten and a hundred times the size of the $10–100M plants this study is about.',
      'size': 10.5, 'color': INK, 'lh': 1.38},
     {'t': 'Not one of the 36 case studies comes from a plant in the target segment.',
      'size': 10.5, 'bold': True, 'color': RUST, 'lh': 1.38, 'sb': 9}])

box(s, MX, 3560000, CW, 1600000, [], fill=TEAL_L, line=TEAL, lw=1.5)
txt(s, MX + 260000, 3650000, CW - 520000, lh(12),
    [{'t': 'ONE MECHANISM RECURS ACROSS UNRELATED VENDORS AND INDUSTRIES — AND IT IS NOT A BETTER ANSWER',
      'size': 12, 'bold': True, 'color': TEAL}])
EX = ['Lake Cable, with Oden — troubleshooting a defect fell from 5 days to 20 minutes',
      'Toyota Industries, with Sight Machine — root-cause analysis from 5 days to under 4 hours',
      'Terumo, with Siemens — releasing material for shipment from days to minutes',
      'BASF, with Siemens — five days of paperwork removed per month']
ey = 3650000 + lh(12) + 40000
for e in EX:
    txt(s, MX + 300000, ey, CW - 600000, lh(10),
        [{'t': '·   ' + e, 'size': 10, 'color': INK}])
    ey += lh(10) + 18000
txt(s, MX + 260000, ey + 30000, CW - 520000, lh(10.5),
    [{'t': 'In each case the plant could already reach the answer. The software collapsed how long it took. The saving is held '
           'inventory and engineer-days, not a better decision.',
      'size': 10.5, 'bold': True, 'color': TEAL, 'lh': 1.3}])

# ============================================================ 6 · THE WALL
s = slide(prs)
titlebar(s, '4.  Why the return on investment cannot be sized from desk research')

box(s, MX, 1020000, CW, 1180000, [], fill=RUST_L, line=RUST, lw=2.0)
txt(s, MX + 300000, 1120000, CW - 600000, lh(14),
    [{'t': 'Not one of the 36 case studies states how the decision was made before the software, or what that cost.',
      'size': 14, 'bold': True, 'color': RUST, 'lh': 1.3}])
txt(s, MX + 300000, 1120000 + lh(14) + 50000, CW - 600000, 500000,
    [{'t': 'Every one gives the improvement — 25% fewer defects, $17.4M saved, five days down to four hours. None gives the '
           'baseline it improved on, which is the comparison a return-on-investment case has to rest on.',
      'size': 11, 'color': INK, 'lh': 1.35}])

WHY = [
 ('Why the baseline is never published', 'A case study is a marketing asset agreed with the customer. The customer will endorse '
  'the improvement. No plant manager signs off a paragraph describing how badly the job was done before.'),
 ('Why the numbers would not transfer anyway', 'The headline figures come from refineries, turbines and biopharma suites. A '
  '$40M food plant has no $7M gas turbine, so the avoided-failure numbers that dominate the corpus do not scale down.'),
 ('Why searching harder will not fix it', 'This is a property of the evidence, not of the search. The only people who know what '
  'a held batch or a lost engineer-day costs are the plants themselves, and they do not publish it.'),
]
wy = 2380000
for head, body in WHY:
    bh = text_h(body, 10.5, CW - 600000, 14)
    box(s, MX, wy, CW, bh + lh(11.5) + 170000, [], fill=LIGHT, line=BORDER)
    txt(s, MX + 300000, wy + 80000, CW - 600000, lh(11.5),
        [{'t': head, 'size': 11.5, 'bold': True, 'color': NAVY}])
    txt(s, MX + 300000, wy + 80000 + lh(11.5) + 10000, CW - 600000, bh,
        [{'t': body, 'size': 10.5, 'color': INK, 'lh': 1.33}])
    wy += bh + lh(11.5) + 170000 + 70000

band(s, wy + 40000, 'THE CONCLUSION I DRAW',
     'The desk phase has done what it can. It located the opportunity precisely and established that the number the whole case '
     'turns on does not exist in public. Getting it requires being inside a plant.',
     dark=True, size=12, line=17)

# ============================================================ 7 · TWO TRACKS
s = slide(prs)
titlebar(s, '5.  The next phase — two kinds of conversation')

T1 = ('TRACK 1', STEEL, STEEL_L, 'A written report on the companies already in this market',
      'I approach the companies on the map as an HBS student writing a report on how this market sells and deploys, for '
      'this independent project. It is a fair trade: they get a copy of the finished analysis, I get the economics.',
      ['HiveMQ, HighByte, Litmus — the data-translation layer',
       'Sight Machine, Oden, Seeq — the ones who traverse the whole stack',
       'Augury — the one that bypasses it',
       'A systems integrator, who sees what a deployment really costs'],
      'What I am trying to learn:  what a mid-market deployment actually costs and how long it takes · what demand walks in '
      'that they turn away, and why · which layer they think is genuinely unsolved.')
T2 = ('TRACK 2', RUST, RUST_L, 'A hands-on project with a plant near Boston',
      'Not an interview. A real piece of work for a real plant, because only being inside one gives the counterfactual — what '
      'the decision costs today, measured rather than estimated.',
      ['45 plants in the $10–150M band across New England',
       'Around 30 within an hour of Boston',
       'Blount Fine Foods and Kettle Cuisine — soups, Fall River and Lynn',
       'Gold Medal Bakery, Demakes, Hans Kissle, Concord Foods, Joseph’s Pasta'],
      'Five of these were already researched or contacted during the July outreach work, so the approach does not start cold.')
cw2 = (CW - 300000) / 2.0
for i, (tag, col, fill, head, why, bullets, foot) in enumerate([T1, T2]):
    x = MX + i * (cw2 + 300000)
    box(s, x, 1000000, cw2, 3260000, [], fill=fill, line=col, lw=1.75)
    txt(s, x + 240000, 1090000, cw2 - 480000, lh(10),
        [{'t': tag, 'size': 10, 'bold': True, 'color': col}])
    txt(s, x + 240000, 1090000 + lh(10) + 20000, cw2 - 480000, lh(13) * 2,
        [{'t': head, 'size': 13, 'bold': True, 'color': NAVY, 'lh': 1.25}])
    yy = 1090000 + lh(10) + lh(13) * 2 + 70000
    bh = text_h(why, 10.5, cw2 - 480000, 14)
    txt(s, x + 240000, yy, cw2 - 480000, bh, [{'t': why, 'size': 10.5, 'color': INK, 'lh': 1.33}])
    yy += bh + 150000
    for b in bullets:
        bb = text_h('·   ' + b, 10, cw2 - 520000, 13.5)
        txt(s, x + 280000, yy, cw2 - 520000, bb,
            [{'t': '·   ' + b, 'size': 10, 'color': INK, 'lh': 1.35}])
        yy += bb + 40000
    yy += 70000
    fh = text_h(foot, 9.5, cw2 - 480000, 13)
    txt(s, x + 240000, yy, cw2 - 480000, fh,
        [{'t': foot, 'size': 9.5, 'bold': True, 'italic': True, 'color': col, 'lh': 1.37}])

band(s, 4390000, 'WHY A PROJECT AND NOT JUST INTERVIEWS',
     'An interview gets an opinion about cost. A project gets the number, because I will be standing next to the paper chart '
     'when the batch is held.', dark=True, size=11.5, line=16)

# ============================================================ 8 · PLAN & ASKS
s = slide(prs)
titlebar(s, '6.  Plan for the remaining ten weeks, and what I need from you')

WK = [('4–5', 'Report research begins', 'First four companies written up; approach letters out to Boston-area plants'),
      ('6', 'Mid-point review with you', 'Interim memo: which hypotheses survived the desk phase'),
      ('7–8', 'Plant project starts', 'One plant agreed; scope a piece of work that produces real cost data'),
      ('9–10', 'Operator interviews alongside', 'Plant leaders, QA managers, controls engineers off the 45-firm New England list'),
      ('11', 'Synthesis', 'Decision inventory completed with real costs; 3–5 opportunity theses'),
      ('12–13', 'Write-up and presentation', 'Final market study, with the assumptions that turned out wrong')]
wy = 1020000
for wk, what, deliv in WK:
    box(s, MX, wy, 6900000, 470000, [], fill=LIGHT, line=BORDER)
    box(s, MX, wy, 780000, 470000, [], fill=STEEL, line=None, shape=MSO_SHAPE.RECTANGLE)
    txt(s, MX, wy + 145000, 780000, lh(11),
        [{'t': 'wk ' + wk, 'size': 11, 'bold': True, 'color': WHITE, 'align': PP_ALIGN.CENTER}])
    txt(s, MX + 900000, wy + 85000, 5900000, lh(10.5),
        [{'t': what, 'size': 10.5, 'bold': True, 'color': NAVY}])
    txt(s, MX + 900000, wy + 85000 + lh(10.5) + 8000, 5900000, lh(9),
        [{'t': deliv, 'size': 9, 'color': MUTED}])
    wy += 470000 + 40000

ax = MX + 7100000
box(s, ax, 1020000, (MX + CW) - ax, 2960000, [], fill=RUST, line=None)
txt(s, ax + 240000, 1120000, (MX + CW) - ax - 480000, lh(15),
    [{'t': 'Three asks', 'size': 15, 'bold': True, 'color': WHITE}])
ASKS = ['An introduction to any food or beverage plant near Boston would be worth more than anything else on this page. '
        'Getting inside one is the whole next phase.',
        'A view on whether a pilot is the right vehicle for sizing the return, or whether a run of structured interviews would '
        'get there faster and cheaper.',
        'If you know anyone at the vendors on slide 1 — Sight Machine, Seeq, Augury, Litmus — a warm introduction turns a '
        'cold email into a conversation.']
ay = 1120000 + lh(15) + 80000
for i, a in enumerate(ASKS, 1):
    hh = text_h(a, 10, (MX + CW) - ax - 620000, 13.5)
    txt(s, ax + 240000, ay, 260000, lh(11),
        [{'t': str(i) + '.', 'size': 11, 'bold': True, 'color': WHITE}])
    txt(s, ax + 480000, ay, (MX + CW) - ax - 720000, hh,
        [{'t': a, 'size': 10, 'color': RGBColor(0xFF,0xE4,0xDB), 'lh': 1.35}])
    ay += hh + 140000

band(s, 4180000, 'WHERE THIS LEAVES THE THESIS',
     'The map says the gap is real and narrow: joining a machine reading to the batch it belongs to, at a price a mid-market '
     'plant can pay. The evidence says nobody has published what that is worth. If the plants say the paperwork is an '
     'irritation rather than a cost, the honest answer is that there is no business here — and I would rather find that out '
     'in week 8 than in week 13.',
     dark=True, size=11.5, line=16.5)

out = '/tmp/claude-0/-home-user-Startup-Research/875053f8-f957-5b4c-a0b6-026315e8daf2/scratchpad/ip-update-2026-09-28.pptx'
prs.save(out)
print('saved:', out, '|', len(prs.slides.__iter__.__self__._sldIdLst), 'slides')
