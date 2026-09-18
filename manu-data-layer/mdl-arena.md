# Arena Pass — Industrial DataOps & Manu-AI Applications (2026-09-18)

**Board lines served:** ICP ① (*SaaS cos for Manu AI*), Q1 (*What problem statements can be solved via new tech*), and Q2 (*What data is required & in what format*).

---

## Executive Summary: The Three Architectural Archetypes

Reading the arena by **how systems ingest and contextualize data** reveals three distinct operating patterns across manufacturing tech:

1. **The Infrastructure / Tooling Trap (DataOps & SCADA):**
   * *Players:* HighByte, Litmus Edge, Inductive Automation (Ignition), Tulip.
   * *Mechanism:* Provide robust plumbing (250+ PLC drivers, OPC-UA, MQTT, ISA-95 model builders).
   * *Reality:* **They provide the empty filing cabinet; they do not file the papers.** Contextualization (mapping raw register `N7:0` to "Mixer 3 Speed" and joining it to Batch ID) must be manually hand-configured by a systems integrator. At $50k–$150k in implementation services, mid-market ($10M–$100M) food plants cannot afford the overhead.
2. **The Sensor Bypass Pattern (Physical-AI / PdM):**
   * *Players:* Augury, generic vibration/bearing monitoring.
   * *Mechanism:* **Completely bypass the plant PLC and SCADA network.** They install their own drop-in wireless magnetic/epoxy sensors (vibration, ultrasound, surface temperature) and their own cellular gateways.
   * *Reason:* Extracting high-frequency physics signals (kHz waveforms) from legacy PLCs is too invasive, brittle, and non-standardized.
3. **The Heavy Enterprise Digital Twin (Process Analytics):**
   * *Players:* Sight Machine.
   * *Mechanism:* Ingests multi-source data (PLCs, historians, MES, ERP, quality documents) into a standardized digital twin.
   * *Reality:* Delivers genuine contextualization (joining process telemetry to batches and SKUs), but the platform is architected and priced for Fortune 500 multinationals (Heineken, Hershey, Nissan) at $150k–$500k+ ACV, leaving the 3,000 mid-market food plants stranded on Excel and paper.

---

## Tier 1: Industrial DataOps & Infrastructure Platforms

These platforms represent the potential *underlying plumbing* or direct competition in the data layer.

### 1. HighByte (HighByte Intelligence Hub)
* **Category:** Industrial DataOps / Unified Namespace (UNS) Modeling.
* **Architecture:** Software hub deployed at the edge or on-prem. Normalizes and transforms raw industrial telemetry into contextualized payloads before sending to cloud/MQTT.
* **Protocols & Ingestion:** OPC UA, MQTT (Sparkplug B), Modbus TCP, SQL, REST, CSV, Parquet.
* **Data Contextualization Approach:** Native ISA-95 hierarchical modeling (Site → Area → Line → Workcell → Asset). Normalizes units of measure and data types.
* **The Mid-Market Barrier:** HighByte is middleware. It does not provide the application, dashboards, or predictive insights. A mid-market plant must already have an internal OT/IT engineer capable of defining the schema, or pay an external integrator.
* **Source:** https://highbyte.com/

### 2. Litmus Automation (Litmus Edge)
* **Category:** Industrial Edge Data Platform / Connectivity.
* **Architecture:** Edge appliance / software running on industrial IPCs. Collects machine data, normalizes it locally into JSON, and routes via MQTT/broker.
* **Protocols & Ingestion:** 250+ native PLC drivers (Rockwell/Allen-Bradley, Siemens, Mitsubishi, Omron, Modbus, Beckhoff), OPC UA client/server.
* **Pricing & Economics:** Subscription tiers (Foundation/Growth/Scale), entry ~$1,500/month, but production rollouts typically require $50,000–$150,000 in professional services integration.
* **The Mid-Market Barrier:** While acquisition (getting bits off PLCs) is largely commoditized by Litmus's 250 drivers, contextualization is still a manual tag-mapping exercise.
* **Source:** https://litmus.io/

### 3. Inductive Automation (Ignition)
* **Category:** Shop-floor SCADA / IIoT Gateway / MES runtime.
* **Architecture:** Modular server gateway. The de facto standard in food & beverage for HMI/SCADA.
* **Protocols & Ingestion:** Native Allen-Bradley/Siemens drivers, native OPC-UA server and client, MQTT modules (via Cirrus Link / Sparkplug B), SQL database bridge.
* **Pricing & Economics:** Perpetual per-server license (Ignition Edge <$2,000; full gateway $10,000–$30,000 depending on modules) + annual support (16–24%).
* **Role in Thesis:** When an F&B plant *does* have a digital data layer, it is almost always Ignition. Any successful data layer for mid-market food must either sit on top of Ignition (via OPC-UA/MQTT) or replace the need for an expensive Ignition integrator.
* **Source:** https://inductiveautomation.com/

### 4. Tulip Interfaces
* **Category:** Frontline Operations / No-Code Connected Worker.
* **Architecture:** Device-based edge platform connecting operator tablets, workstations, and edge I/O.
* **Protocols & Ingestion:** USB peripherals (scales, calipers, barcode scanners), OPC-UA, MQTT, REST APIs.
* **Pricing:** $100–$250/month per active interface.
* **The Mid-Market Barrier:** Exceptional for digitizing human workflows (line-clearance checklists, manual weigh-and-dispense, SOPs), but weak on deep high-frequency machine telemetry (e.g. continuous motor load or thermal profiling).
* **Source:** https://tulip.co/

---

## Tier 2: Application & Manu-AI Players (Reverse-Engineering Data Requirements)

Examining what these application players ingest reveals exactly what data primitives are required to solve high-value factory problems.

### 1. Augury
* **Problem Solved:** Predictive maintenance / catastrophic failure prevention on rotating equipment (pumps, chillers, agitators, compressors).
* **Data Ingested:** High-frequency vibration waveforms, FFT frequency spectra, surface temperature, magnetic flux.
* **Ingestion Surface:** Completely decoupled from the PLC. Dedicated wireless battery-powered sensors attached magnetically or with epoxy; cellular edge gateways.
* **Data Format:** Raw time-series arrays / spectral frequency distributions.
* **Lesson for Data Layer:** Physics-level mechanical failure detection *does not rely on PLC telemetry* because legacy PLCs do not sample at the kilohertz frequencies required for vibration FFT analysis.
* **Source:** https://www.augury.com/

### 2. Sight Machine
* **Problem Solved:** Continuous process optimization, batch cycle-time variation, yield loss, and automated root-cause analysis.
* **Data Ingested:** 
  1. *Time-series machine data:* temperatures, pressures, line speeds, motor amperage.
  2. *Batch execution data:* Batch ID, SKU recipe parameters, phase start/stop times.
  3. *Quality / Lab data:* off-line lab test results (viscosity, moisture, Brix, pH).
* **Ingestion Surface:** Connectors to PLC/SCADA (Ignition, Kepware), historians (PI System), MES, and ERP.
* **Data Format:** Relational join between continuous time-series (1 Hz – 0.1 Hz) and discrete batch/lot metadata.
* **Lesson for Data Layer:** The core value in process manufacturing is **joining the time-series trace to the batch record**. Raw sensor data without batch context is useless for yield or quality optimization.
* **Source:** https://sightmachine.com/

### 3. LandingAI (LandingLens / LandingEdge)
* **Problem Solved:** High-variability visual quality inspection (baked good browning/rise, package seal integrity, foreign object detection, fill levels).
* **Data Ingested:** 2D industrial camera frames (color/monochrome, GenICam / GigE Vision standard).
* **Ingestion Surface:** Industrial cameras connected to an edge industrial PC (IPC) running inference.
* **PLC Integration:** Minimal 1-bit or 2-bit digital handshake:
  - *Input to Vision:* Line photo-eye trigger ("bottle in position, take image").
  - *Output to PLC:* Rejection actuator signal ("defective product, fire air-reject blast").
* **Data Format:** Uncompressed image frames (`.png` / `.bmp` / raw tensor) + bounding box / segmentation mask coordinates.
* **Lesson for Data Layer:** Modern computer vision solves inspection at the edge; it needs zero historical PLC telemetry to make decisions, but generates rich visual metadata that is currently lost (not logged to quality records).
* **Source:** https://landing.ai/

### 4. SafetyChain
* **Problem Solved:** Food Safety and Quality Assurance (FSQA), HACCP compliance, digital batch sign-offs, and SPC (Statistical Process Control).
* **Data Ingested:** Critical Control Point (CCP) verification records, weights, temperature logs, sanitation checklists.
* **Ingestion Surface:** Operator tablet entry, direct digital scale/gage Bluetooth/serial inputs, and recent OPC-UA connectors into Ignition.
* **Data Format:** Tabular records with timestamps, operator IDs, batch IDs, and pass/fail thresholds.
* **Lesson for Data Layer:** Compliance data in F&B is fundamentally event-driven and threshold-based (e.g. "Did retort temperature exceed 250°F for 35 minutes? Yes/No").
* **Source:** https://safetychain.com/

### 5. Redzone
* **Problem Solved:** Frontline worker engagement, visual factory management, and rapid OEE improvements.
* **Data Ingested:** Line run/stop status, scrap counts, operator downtime reason codes.
* **Ingestion Surface:** Low-friction approach: often a single external photo-eye sensor on the infeed/discharge starwheel or simple operator taps on iPads at huddles. Avoids deep PLC integration.
* **Lesson for Data Layer:** High adoption in mid-market plants was achieved specifically by *avoiding* complex PLC data engineering.
* **Source:** https://rzsoftware.com/

---

## Synthesis: Reverse-Engineered Data Primitives (Preview of Q2)

From the arena, modern manufacturing tech requires four distinct data primitives:

| Primitive | Typical Sampling Rate | Source / Hardware | Examples in F&B | Primary Consumer |
|---|---|---|---|---|
| **1. Slow Process Telemetry** | 0.1 Hz – 1 Hz (every 1–10s) | In-line process instruments (RTDs, pressure transmitters, flowmeters, load cells) | Retort cook temperature, pasteurizer holding tube flow, mix tank agitator load | Sight Machine, Ignition, SPC tools |
| **2. Fast Physics / Condition Telemetry** | 1 kHz – 20 kHz (high burst) | Retrofit wireless accelerometers, current CTs | Homogenizer pump vibration, motor bearing temperature | Augury, PdM tools |
| **3. Edge Vision & Spatial Streams** | 10 fps – 60 fps (triggered frames) | GigE / USB3 industrial cameras | Jar seal inspection, cookie color/bake uniformity, fill-level check | LandingAI, custom edge models |
| **4. Discrete Batch & Contextual Metadata** | Event-driven (state changes) | Operator input, MES, barcode scans, ERP order | Batch ID, Recipe name, Step start/stop, Lot number, Operator ID | SafetyChain, Tulip, Traceability ERP |

---

## Strategic Implications for the Data Layer Thesis

1. **Acquisition (Layer 1) has two polar realities:**
   * *For Slow Process Telemetry:* The sensors already exist on the machines (OEM-fitted RTDs, flowmeters), but they are locked inside isolated PLC memory registers or paper circular chart recorders.
   * *For Fast Physics Telemetry:* The sensors do not exist on the machine; application vendors supply their own wireless hardware.
2. **Contextualization (Layer 2) is the true missing link:**
   * No tool provides *automatic* contextualization for mid-market F&B. HighByte and Litmus give you the modeling tools, but require human engineers to map every single tag manually. Sight Machine does it, but at enterprise pricing ($200k+).
   * **The Seam:** The highest-value problem is uniting **Primitive 1 (Slow Process Telemetry)** with **Primitive 4 (Batch/Lot Metadata)** without requiring a $100k systems integration contract.
