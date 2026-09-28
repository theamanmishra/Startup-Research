# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/user/Startup-Research/.claude/skills/ip-deck')
from deckkit import *
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = new_deck()
s = slide(prs)
titlebar(s, '4.  The manufacturing technology stack — who owns each layer')

STACK_W = 8600000
PAD     = 200000
INNER   = STACK_W - 2 * PAD
RAIL_X  = MX + STACK_W + 200000
RAIL_W  = (MX + CW) - RAIL_X
RINNER  = RAIL_W - 2 * 160000

eyebrow(s, MX, 870000, STACK_W,
        'NOTHING IS ACTUALLY KEPT UNTIL LAYER 4 — READ THE TAGS DOWN THE RIGHT EDGE')

def line_h(pt, lh=1.25):
    return int(pt * lh * 12700)

LAYERS = [
    ('1 \u00b7 SENSORS & INSTRUMENTS', '\u2192  a signal, or nothing',
     'Does a number exist at all? A probe in the tank, a camera over the line \u2014 or nothing. '
     'Whoever built the line decided this years ago.',
     'Emerson Rosemount \u00b7 Anderson-Negele \u00b7 Endress+Hauser \u00b7 Cognex \u00b7 Keyence  |  '
     'Groen \u00b7 Lee \u00b7 Admix (equipment)  |  Partlow (paper charts)'),
    ('2 \u00b7 CONTROL', '\u2192  live values, not kept',
     'The machine\u2019s own computer. Reads the probe and moves the valve thousands of times a second \u2014 '
     'but it acts on the number, it does not keep it.',
     'Rockwell Allen-Bradley \u00b7 Siemens SIMATIC \u00b7 Emerson DeltaV \u00b7 Schneider Modicon \u00b7 ABB \u00b7 '
     'Beckhoff \u00b7 Mitsubishi \u00b7 Omron \u00b7 Yokogawa'),
    ('3 \u00b7 OPERATOR SCREENS', '\u2192  a screen, not a record',
     'What the operator sees: live graphics, alarms, start and stop. Built for a human watching now, '
     'not for a record read later.',
     'Inductive Automation Ignition (the standard in food) \u00b7 Siemens WinCC \u00b7 Rockwell FactoryTalk View \u00b7 '
     'AVEVA Wonderware \u00b7 GE iFIX'),
    None,
    ('5 \u00b7 THE PLANT RECORD', '\u2192  history you can search',
     'Keeps the readings, and knows what was being made at the time \u2014 which order, which recipe, which lot.',
     'AVEVA PI System \u00b7 Siemens Opcenter \u00b7 Rockwell Plex \u00b7 SAP Digital Manufacturing \u00b7 Aptean \u00b7 '
     'Deacom \u00b7 Nulogy \u00b7 GE Proficy'),
    ('6 \u00b7 ANALYTICS & AI', '\u2192  an answer to act on',
     'Turns that history into a prediction, an explanation, or a yield gain. The layer everyone is trying to sell.',
     'Sight Machine \u00b7 Seeq \u00b7 Augury \u00b7 Oden \u00b7 Cognite \u00b7 Quartic.ai \u00b7 Siemens Senseye \u00b7 '
     'AspenTech Mtell \u00b7 C3 AI \u00b7 Falkonry'),
]

TOP, GAP = 1080000, 46000
NORM_H, GAP_H = 622000, 968000

y = TOP
for L in LAYERS:
    if L is None:
        box(s, MX, y, STACK_W, GAP_H, [], fill=RUST_L, line=RUST, lw=2.0)
        cy = y + 72000
        txt(s, MX + PAD, cy, 1700000, line_h(11.5),
            [{'t': '4 · DATA TRANSLATION', 'size': 11.5, 'bold': True, 'color': RUST}])
        txt(s, MX + PAD + 1740000, cy + 12000, INNER - 1740000 - 2300000, line_h(9.5),
            [{'t': '←  where this project is aimed', 'size': 9.5, 'bold': True, 'italic': True, 'color': RUST}])
        txt(s, MX + PAD + INNER - 2300000, cy + 22000, 2300000, line_h(8.5),
            [{'t': '→  a named, storable stream', 'size': 8.5, 'bold': True, 'italic': True,
              'color': RUST, 'align': PP_ALIGN.RIGHT}])
        cy += line_h(11.5) + 16000
        txt(s, MX + PAD, cy, INNER, line_h(8.5),
            [{'t': 'Turns a code like “N7:0” into “Mixer 3 temperature”, and sends it somewhere it can be kept.',
              'size': 8.5, 'italic': True, 'color': MUTED}])
        cy += line_h(8.5) + 10000
        txt(s, MX + PAD, cy, INNER, line_h(8.5),
            [{'t': 'HiveMQ · HighByte · Litmus · PTC Kepware · EMQX · Cirrus Link · Siemens Industrial Edge',
              'size': 8.5, 'color': INK}])
        cy += line_h(8.5) + 24000
        txt(s, MX + PAD, cy, INNER, line_h(8.5),
            [{'t': 'SOLVED — getting the bits off the machine. Litmus ships 250+ drivers; Kepware translates almost any protocol.',
              'size': 8.5, 'bold': True, 'color': TEAL}])
        cy += line_h(8.5) + 10000
        txt(s, MX + PAD, cy, INNER, line_h(8.5),
            [{'t': 'NOT SOLVED — making that reading mean “batch 4471, line 2, shift B”. Every tag is mapped by hand.',
              'size': 8.5, 'bold': True, 'color': RUST}])
        y += GAP_H + GAP
    else:
        name, handson, defn, cos = L
        box(s, MX, y, STACK_W, NORM_H, [], fill=LIGHT, line=BORDER)
        cy = y + 76000
        txt(s, MX + PAD, cy, INNER - 2300000, line_h(11),
            [{'t': name, 'size': 11, 'bold': True, 'color': NAVY}])
        txt(s, MX + PAD + INNER - 2300000, cy + 22000, 2300000, line_h(8.5),
            [{'t': handson, 'size': 8.5, 'bold': True, 'italic': True, 'color': STEEL,
              'align': PP_ALIGN.RIGHT}])
        cy += line_h(11) + 14000
        txt(s, MX + PAD, cy, INNER, line_h(8.5),
            [{'t': defn, 'size': 8.5, 'italic': True, 'color': MUTED}])
        cy += line_h(8.5) + 12000
        txt(s, MX + PAD, cy, INNER, line_h(8.5),
            [{'t': cos, 'size': 8.5, 'color': INK}])
        y += NORM_H + GAP

STACK_BOTTOM = y - GAP

# ------------------------------------------------------------------ rails
def rail(x, ytop, h, fill, edge, head, hcol, items):
    box(s, x, ytop, RAIL_W, h, [], fill=fill, line=edge)
    txt(s, x + 160000, ytop + 100000, RINNER, line_h(9.5),
        [{'t': head, 'size': 9.5, 'bold': True, 'color': hcol}])
    cy = ytop + 100000 + line_h(9.5) + 60000
    for body, bold, col in items:
        hh = text_h(body, 8.5, RINNER, 8.5 * 1.3)
        txt(s, x + 160000, cy, RINNER, hh,
            [{'t': body, 'size': 8.5, 'bold': bold, 'color': col, 'lh': 1.3}])
        cy += hh + 95000

rh = (STACK_BOTTOM - TOP - 150000) / 2.0
rail(RAIL_X, TOP, rh, STEEL_L, STEEL, 'GATES EVERY LAYER', STEEL, [
    ('OT network security — Claroty, Dragos, Nozomi. Nothing leaves the plant network without a security review.', False, INK),
    ('Systems integrators — they build these deployments, and they are why the bill is $50–150k.', False, INK),
    ('Regulation — FDA 21 CFR 113 and 114, Grade A PMO, USDA FSIS. The only force that makes a measurement compulsory.', False, INK),
])
rail(RAIL_X, TOP + rh + 150000, rh, TEAL_L, TEAL, 'SKIPS EVERY LAYER', TEAL, [
    ('Augury fits its own wireless sensors and goes straight to its own cloud.', False, INK),
    ('Tulip and Redzone ask the operator on a tablet, never touching the control system.', False, INK),
    ('These are the products that actually sold into mid-sized plants — by avoiding layers 2 to 5.', True, TEAL),
])

# ------------------------------------------------------------------ conclusion
band(s, STACK_BOTTOM + 110000, 'WHAT THE MAP SAYS',
     'Every layer has an entrenched owner except one — joining a machine reading to the batch it belongs to, '
     'at a price a $10–100M plant can pay. Whether that gap is a business depends on what the decision costs '
     'today without it, which no vendor publishes.',
     dark=True, size=12, line=17.5)

notes(s, 'One-slide market map. Layers 1-6 are the stack; the right column carries the two things a linear '
         'chart hides - what gates every layer, and who skips it entirely. Full roster of 163 companies, formal '
         'layer definitions and the interaction web are in manu-data-layer/mdl-market-map.md.')

out = '/tmp/claude-0/-home-user-Startup-Research/875053f8-f957-5b4c-a0b6-026315e8daf2/scratchpad/market-map-slide.pptx'
prs.save(out)
print('saved:', out)
