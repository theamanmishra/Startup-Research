# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/user/Startup-Research/.claude/skills/ip-deck')
from deckkit import *
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

prs = new_deck()
s = slide(prs)
titlebar(s, '4.  The manufacturing technology stack — every layer, and who owns it')

STACK_W = 8200000
PAD     = 190000
INNER   = STACK_W - 2 * PAD
RAIL_X  = MX + STACK_W + 180000
RAIL_W  = (MX + CW) - RAIL_X
RINNER  = RAIL_W - 2 * 140000

def lh(pt, f=1.22):
    return int(pt * f * 12700)

eyebrow(s, MX, 862000, STACK_W,
        'ONE ROW PER THING THAT HAPPENS TO THE DATA. A PRODUCT SITS IN THE ROW IT PRIMARILY DOES.')
eyebrow(s, RAIL_X, 862000, RAIL_W, 'ATTACH AT SEVERAL ROWS', color=TEAL)

#            name              tag                        description                                             companies
ROWS = [
 ('1 · SENSE',        '→  a reading exists',
  'Creates the number in the first place — a probe, a camera, or a person writing it down.',
  'Emerson Rosemount · Anderson-Negele · Endress+Hauser · Cognex · Keyence · Augury (fits its own) · Partlow (paper charts)', None),
 ('2 · CONTROL',      '→  action, nothing stored',
  'Acts on the number in milliseconds to move a valve or a motor. It does not keep it.',
  'Rockwell Allen-Bradley · Siemens SIMATIC · Emerson DeltaV · Schneider Modicon · ABB · Beckhoff · Omron · Yokogawa', None),
 ('3 · SUPERVISE',    '→  a live screen',
  'Shows a human what is happening right now: graphics, alarms, start and stop.',
  'Inductive Automation Ignition (the standard in food) · Siemens WinCC · Rockwell FactoryTalk View · AVEVA Wonderware · GE iFIX', None),
 ('4 · MOVE',         '→  a named stream',
  'Translates cryptic machine codes and routes them off the floor. Getting bits out is solved.',
  'HiveMQ · HighByte · Litmus · PTC Kepware · EMQX · Cirrus Link · Siemens Industrial Edge', 'gap'),
 ('5 · STORE',        '→  years of history',
  'Keeps the time-series so it can be looked back through.',
  'AVEVA PI System · AspenTech InfoPlus.21 · GE Proficy Historian · Honeywell PHD · Canary', None),
 ('6 · CONTEXTUALISE','→  a reading that means something',
  'Says which order, recipe, lot and shift the reading belongs to. Joining this to row 4 is the unsolved part.',
  'Siemens Opcenter · Rockwell Plex · SAP Digital Mfg · DELMIA Apriso · TrakSYS · Aptean · Deacom · Nulogy · Sepasoft', 'gap'),
 ('7 · ANALYSE',      '→  an answer to act on',
  'Predicts a failure, explains a defect, lifts a yield, or writes a setpoint back down.',
  'Sight Machine · Seeq · Augury Process Health · Oden · Cognite · Quartic.ai · Senseye · Mtell · Pavilion8 · C3 AI · Falkonry', None),
]

TOP, GAP, RH = 1060000, 30000, 525000
y = TOP
for name, tag, defn, cos, mark in ROWS:
    isgap = mark == 'gap'
    box(s, MX, y, STACK_W, RH, [], fill=RUST_L if isgap else LIGHT,
        line=RUST if isgap else BORDER, lw=1.75 if isgap else 1.0)
    c = RUST if isgap else NAVY
    cy = y + 56000
    txt(s, MX + PAD, cy, INNER - 2450000, lh(10.5),
        [{'t': name, 'size': 10.5, 'bold': True, 'color': c}])
    txt(s, MX + PAD + INNER - 2450000, cy + 14000, 2450000, lh(8),
        [{'t': tag, 'size': 8, 'bold': True, 'italic': True,
          'color': c if isgap else STEEL, 'align': PP_ALIGN.RIGHT}])
    cy += lh(10.5) + 10000
    txt(s, MX + PAD, cy, INNER, lh(8),
        [{'t': defn, 'size': 8, 'italic': True, 'color': MUTED}])
    cy += lh(8) + 8000
    txt(s, MX + PAD, cy, INNER, lh(8),
        [{'t': cos, 'size': 8, 'color': INK}])
    y += RH + GAP
STACK_BOTTOM = y - GAP

# --------------------------------------------------- attached systems (right)
ATT = [
 ('QUALITY & COMPLIANCE', 'SafetyChain · Trustwell · TraceGains · FoodReady · Specright · Safefood 360 · LabWare and SampleManager (lab)'),
 ('MAINTENANCE',          'MaintainX · Fiix · UpKeep · IBM Maximo · Limble'),
 ('PLAN & ORDER',         'SAP · Oracle · NetSuite · Infor · o9 · Blue Yonder · RELEX · PlanetTogether · Semia'),
 ('FRONTLINE CAPTURE',    'Tulip · Redzone · Parsable · Augmentir · Dozuki · Evocon'),
]
ah = (STACK_BOTTOM - TOP - 3 * 30000) / 4.0
ay = TOP
for head, cos in ATT:
    box(s, RAIL_X, ay, RAIL_W, ah, [], fill=TEAL_L, line=TEAL)
    txt(s, RAIL_X + 140000, ay + 52000, RINNER, lh(9),
        [{'t': head, 'size': 9, 'bold': True, 'color': TEAL}])
    txt(s, RAIL_X + 140000, ay + 52000 + lh(9) + 14000, RINNER,
        text_h(cos, 8, RINNER, 8 * 1.28),
        [{'t': cos, 'size': 8, 'color': INK, 'lh': 1.28}])
    ay += ah + 30000

# --------------------------------------------------- footer: gates + bypass
fy = STACK_BOTTOM + 80000
box(s, MX, fy, CW, 400000, [], fill=STEEL_L, line=STEEL)
txt(s, MX + 190000, fy + 58000, CW - 380000, lh(8.5),
    [{'t': 'GATES EVERY ROW:   OT security (Claroty, Dragos)   \u00b7   systems integrators, who are why the bill is $50\u2013150k   '
           '\u00b7   regulation (FDA 21 CFR 113 and 114, Grade A PMO, USDA FSIS)',
      'size': 8.5, 'color': INK}])
txt(s, MX + 190000, fy + 58000 + lh(8.5) + 16000, CW - 380000, lh(8.5),
    [{'t': 'SKIPS MOST ROWS:   Augury fits its own sensors and goes straight to its cloud   \u00b7   Tulip and Redzone ask the operator instead   '
           '\u00b7   these are what actually sold into mid-sized plants',
      'size': 8.5, 'color': INK}])

band(s, fy + 470000, 'WHAT THE MAP SAYS',
     'Rows 4 and 5 are solved and commoditised. Row 6 exists only inside enterprise systems. The unsolved cell is the join '
     'between rows 4 and 6 \u2014 making a reading mean \u201cbatch 4471, line 2, shift B\u201d at a price a $10\u2013100M plant can pay.',
     dark=True, size=11, line=16)

notes(s, 'Stack rows are mutually exclusive on what a product primarily does to the data. The right column holds systems that '
         'own a business obligation and attach at several rows, which is why they are not in the stack. Full roster of 163 '
         'companies and formal definitions: manu-data-layer/mdl-market-map.md.')

out = '/tmp/claude-0/-home-user-Startup-Research/875053f8-f957-5b4c-a0b6-026315e8daf2/scratchpad/market-map-slide.pptx'
prs.save(out)
print('saved:', out)
