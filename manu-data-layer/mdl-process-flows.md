# Process Flows & Instrumentation Reality (2026-09-21)

**Board lines served:** Q1 (*Study process flows of hyper-niches*), Q2 (*What data is required & in what format*), and the frontier humanoid training data workstream.

---

## Overview

This document walks the physical shop-floor line for our 3 selected mid-market ($10M–$100M) F&B manufacturing niches:
1. **Niche 1: Retort-Canned Low-Acid Foods** (Soups, vegetables, beans — 21 CFR 113)
2. **Niche 2: Cheese & Cultured Dairy** (Grade A PMO) — *[Upcoming]*
3. **Niche 3: Mayonnaise, Dressings & Sauces** (Acidified foods — 21 CFR 114) — *[Upcoming]*

For each process step, we map two parallel layers:
* **Layer A (Machine Telemetry & Process AI):** What instruments physically exist, what is metered vs. unmetered, how data is recorded today (paper vs. digital), and where product is ruined.
* **Layer B (Humanoid Robotics Training Data):** Which tasks remain stubbornly manual, dexterous, or spatial, and represent high-value egocentric video and motion-capture data targets for humanoid robotics developers (e.g., Figure, 1X, Tesla Optimus).

---

## Niche 1: Retort Canning (NAICS 311421)

**Regulatory Regime:** FDA 21 CFR 113 (Thermally processed low-acid foods in hermetically sealed containers).  
**The Core Physics:** Industrial autoclaves heating product to 250°F (121°C) under 15–22 PSI steam pressure to achieve legal commercial sterility ($F_0 \ge 3.0–6.0$ min for *Clostridium botulinum* spore destruction).

```
[1. Raw Prep] ──► [2. Can Fill] ──► [3. Seamer] ──► [4. Basket Load] ──► [5. Retort Cook] ──► [6. Unload & Pack]
    (Sort)           (Solid+Liquid)   (Double Seam)    (Stack Carts)      (250°F Steam)       (Case Pack)
```

---

### Step 1: Raw Material Prep & Batching

* **Physical Equipment:** Rotary steam blanchers, vegetable dicers/slicers, broth batching tanks with impellers.
* **Instrumentation Reality (Layer A):**
  * *Standard on machines:* Blancher water temperature RTD, jacket steam pressure gauge, batch tank load cells.
  * *Unmetered / Data gaps:* Ingredient moisture variability, raw produce firmness, starch slurry viscosity during initial hydration.
  * *Current recording:* Handwritten batch sheet on clipboard ("Added 2 bags salt, 1 drum oil, operator initials").
* **Manual Tasks & Humanoid Data Opportunity (Layer B):**
  * **Visual Sorting & Culling:** Workers stand at high-speed conveyor belts, performing rapid bimanual picking of defective produce (rotten potatoes, stones, stems, discolored beans).
    * *Robotics Data Value:* High-speed hand-eye coordination, deformable non-rigid object manipulation, natural visual variability.
  * **Bulk Bag Dumping:** Slicing open and manually inverting 50 lb bags of dry starch, seasonings, and salt into mix hoppers.
    * *Robotics Data Value:* Heavy lifting, dual-arm compliant handling, bag tearing/pouring dynamics.

---

### Step 2: Can Filling (Solid Pocket + Liquid Top-Off)

* **Physical Equipment:** Rotary pocket filler (volumetric cups for diced vegetables/meat), rotary liquid gravity or piston filler (hot broth/brine).
* **Instrumentation Reality (Layer A):**
  * *Standard on machines:* Liquid filler supply bowl temperature sensor, can-presence proximity switch, in-line checkweigher load cell (gross weight).
  * *Critical Parameter:* **Liquid Fill Temperature ($I_T$).** Federal retort filing specifies an "Initial Temperature" (e.g., minimum 160°F or 180°F). If broth cools to 140°F due to a 10-minute line stoppage, the subsequent retort cook will **under-process** the can.
  * *Current recording:* Manual thermometer check of fill temperature once every 30–60 minutes on a paper log.
* **Failure Modes & Financial Stakes:**
  * **Headspace Variation:** Overfilling leaves no expansion volume, causing can buckling/bursting during retort cooling. Underfilling causes net-weight non-compliance. Cost: line jams, scrapped cans ($500–$2,000/shift).
* **Manual Tasks & Humanoid Data Opportunity (Layer B):**
  * **Headspace Tamping:** In mid-market lines, if solids bridge or stick above the can rim, line operators manually tamp down protruding chunks using spatulas or gloved hands before the seamer turret.

---

### Step 3: Can Seaming (The Double Seamer)

* **Physical Equipment:** High-speed rotary double seamer (e.g., Angelus, Ferrum) operating at 200–600 cans/minute. Mechanically forms the interlocking hermetic seal in two operations (First Operation: curling flange and end curl; Second Operation: compressing and flattening the hook).
* **Instrumentation Reality (Layer A):**
  * *Standard on machines:* Main motor speed/current, can-infeed starwheel jam sensors.
  * *The Blind Spot:* The seamer does **not** continuously meter seal quality. Seam tightness, overlap, and compound distribution are completely invisible to the machine during running.
  * *Current recording:* Highly regulated manual tear-down inspections.
* **Failure Modes & Financial Stakes:**
  * **Defective Seams (False seams, cut-overs, droop):** If seam overlap falls below 0.040 inches, cooling water and bacteria get sucked into the can during post-retort cooling. Cost: Catastrophic class-1 recall, botulism liability ($1M+).
* **Manual Tasks & Humanoid Data Opportunity (Layer B):**
  * **Lid Sleeve Loading:** Loading 200-count paper tubes of metal can ends into vertical gravity chutes every 10 minutes without dropping or bending lids.
  * **Seam Tear-Down Inspection:** Every 2–4 hours, an operator removes 3 cans, uses a specialized seam saw to cut cross-sections, peels the seam open with nippers, and measures overlap, body hook, and seam thickness with an optical projector or digital micrometer.
    * *Robotics Data Value:* Fine-motor tool use (wire nippers, micrometers, precision alignment).

---

### Step 4: Retort Basket Loading & Staging

* **Physical Equipment:** Sweep crate loader or manual staging conveyor; perforated retort crates/baskets (iron or stainless steel); wheeled transfer dollies on embedded floor tracks.
* **Instrumentation Reality (Layer A):**
  * *Standard:* Can layer counter.
  * *Data Gap:* Which specific batch ID and pallet number is placed into which specific Retort Basket is rarely digitized in mid-market plants. It exists as a paper traveler tag hung from the cart.
* **Manual Tasks & Humanoid Data Opportunity (Layer B - Prime Humanoid Target):**
  * **Layer Pad Insertion:** Manually picking up flexible perforated plastic/aluminum divider sheets (3 ft × 3 ft) and laying them flat on top of each tier of 250 cans.
  * **Heavy Basket Transport & Track Alignment:** Unhooking 1,500 lb loaded metal baskets, pushing them along floor dollies, aligning them with the retort chamber rails, and shoving them into the vessel.
    * *Robotics Data Value:* Whole-body locomotion, high-payload pushing, track alignment, spatial divider placement.

---

### Step 5: The Retort Sterilization Cycle (Autoclave)

* **Physical Equipment:** Batch horizontal steam or water-spray retort vessel (30 ft cylindrical steel pressure vessel, 4-basket capacity).
* **Instrumentation Reality (Layer A - The High-Stakes Telemetry Core):**
  * *Sensors present:*
    1. 3–5 Class-A RTD temperature sensors (inlet, chamber center, bleeders, drain).
    2. Chamber pressure transducer (0–30 PSI).
    3. Vent line thermometer & valve limit switch (to confirm complete air purge at 212°F for 7 minutes).
    4. Compressed air overpressure control valve & cooling water flowmeter.
  * *Federal Mandate (21 CFR 113.100):* Continuous recording of time, temperature, and pressure per retort cycle.
  * *Incumbent Technology:* **Circular paper chart recorders** with physical ink pens (e.g., Partlow, Anderson-Negele) mounted on the control panel.
* **Failure Modes & Financial Stakes:**
  * **Pressure or Temperature Dip:** If steam temperature drops below 250°F for even 30–60 seconds, or if an air pocket prevents heat transfer, the thermal lethality ($F_0$) target is missed.
  * *Result:* The entire batch (10,000 cans = $20,000–$50,000) must be quarantined, biologically tested, or re-cooked (which turns food into inedible mush).
* **Manual Tasks & Humanoid Data Opportunity (Layer B):**
  * **Vessel Door Locking ("Dogging"):** Rotating heavy mechanical hand-wheels or locking ring levers to seal the 5-ton door against 20 PSI internal pressure.
  * **Visual Reference Thermometer Verification (21 CFR 113 requirement):** Operator must physically read the analog **Mercury-in-Glass (MIG) thermometer** mounted on the vessel shell and cross-check it against the chart recorder pen at the start and end of process timing, recording the verification on the paper chart.
  * **Chart Handling:** Inserting, winding, dating, and signing paper circular chart discs.

---

### Step 6: Basket Unloading, Drying, Labeling & Palletizing

* **Physical Equipment:** Retort unloader, air knife blowers, roll-through can labeler, case packer, stretch wrapper.
* **Instrumentation Reality (Layer A):**
  * *Sensors:* Air knife pressure, label presence sensor, case packer jam photo-eyes, checkweigher.
* **Manual Tasks & Humanoid Data Opportunity (Layer B - Highest Volume Humanoid Deployment):**
  * **Can Culling / Leaker Inspection:** Inspecting hot cans exiting the retort for buckled ends, dented rims, or thermal burst leaks.
  * **Manual Case Packing:** Grasping 4–6 cans per hand and packing into corrugated paper trays/cases at 30–50 cases/minute.
  * **Palletizing & Corner Board Stacking:** Lifting 25–40 lb finished cases, building interlocking pallet patterns, placing cardboard edge-corner protectors, and staging for forklift pickup.
    * *Robotics Data Value:* Heavy repetitive lifting, spatial pallet stacking, box manipulation—the exact primary market targeted by humanoid manufacturers.

---

## Retort Canning Summary Matrix

| Process Step | Primary Machine Telemetry (Layer A) | Current Data Storage | Financial Risk / Failure Mode | Humanoid Training Data Target (Layer B) |
|---|---|---|---|---|
| **1. Prep & Batch** | Water temp, tank load cells | Handwritten batch sheet | Ingredient ratio errors ($1k–$5k) | Bimanual produce sorting; 50 lb bag lifting/dumping |
| **2. Can Fill** | Broth fill temp, checkweigher | Paper log every 30 min | Headspace overflow / low initial temp ($2k) | Hand-tamping overflow chunks below rim |
| **3. Can Seam** | Motor RPM, torque | Paper seam inspection log | Micro-leaks $\rightarrow$ botulism risk ($1M+ recall) | Can lid sleeve feeding; micrometer seam tear-down tool use |
| **4. Basket Load** | Can layer count | Paper traveler tag on cart | Basket mix-up / untracked cook schedule | Perforated layer sheet placement; 1,500 lb cart pushing/alignment |
| **5. Retort Cook** | RTD temperatures (3–5), steam PSI, vent time | **Circular paper ink charts** | $F_0$ lethality drop $\rightarrow$ 10,000 cans ruined ($30k+) | 5-ton door locking; analog MIG thermometer visual cross-check |
| **6. Pack & Pallet** | Line speed, case count | End-of-shift whiteboard | Packing bottlenecks, crushed cases | Case packing (4–6 cans/hand); 35 lb box palletizing & corner board placement |
