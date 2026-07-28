#!/usr/bin/env python3
"""Assemble outreach .eml drafts + tracker rows from a company spec JSON.

Part of the 3-file outreach package (adapted from Adarsh Kumar's OEM pipeline,
shared 2026-07-28, retargeted to US food/CPG contract manufacturers):
  .claude/skills/outreach/SKILL.md          - the pipeline (main skill)
  .claude/skills/outreach/outreach_build.py - this script (single source of truth for the body)
  .claude/skills/outreach-style/SKILL.md    - language gate for the insight clause

The email body is FROZEN here. The only variables: recipient address, salutation,
company short name, per-company insight clause. Never retype the body into a draft;
read the BODY constant if you need to see it.

DEVIATION FROM AK'S VERSION: the tracker is CSV, not xlsx. Reasons: CLAUDE.md makes
CSVs the source of truth for this repo, CSV diffs readably in git, and this removes the
openpyxl dependency so the script runs anywhere. Columns match AK's tracker exactly.

Usage (from the project root):
  python3 .claude/skills/outreach/outreach_build.py contract-manufacturing/outreach-drafts/<slug>.spec.json

Spec format:
{
  "company": "Blount Fine Foods Corp.",   // tracker display name
  "short":   "Blount",                    // name used inside the sentence
  "slug":    "blount",                    // filename prefix
  "date":    "2026-07-28",                // drafted date for tracker
  "batch":   "2026-07-28",                // drafts subfolder; defaults to date
  "insight": "you make soups for retail and foodservice brands under SQF certification",
  "proof":   "[proof: blountfinefoods.com/capabilities, SQF cert page]",  // tracker only
  "contacts": [
    {"rank":1, "name":"Todd Blount", "title":"President",
     "salutation":"Dear Mr. Blount,", "email":"tblount@blountfinefoods.com",
     "file":"1-blount.eml", "basis":"confirmed pattern {f}{last}@",
     "check":"CURRENT - company leadership page 2026 + trade press 2025", "notes":""}
  ]
}
"""
import csv, json, os, sys

FROM = '"Mishra, Aman" <amishra@mba2027.hbs.edu>'
CC = None  # optional second sender/classmate address; header omitted while unset
SUBJECT = "Harvard Business School research - contract manufacturing operations"
TRACKER = os.path.join("contract-manufacturing", "outreach-tracker.csv")
DRAFTS_ROOT = os.path.join("contract-manufacturing", "outreach-drafts")

TRACKER_COLUMNS = ["Company", "Rank", "Contact", "Title", "Email", "Email basis",
                   "Person check", "Insight", "Drafted date", "Sent date", "Sent?",
                   "Reply?", "Notes"]

# NO signature block: Outlook auto-appends the sender signature; including one here duplicates it.
# FROZEN BODY - Aman's verbatim, mirroring Adarsh Kumar's proven OEM email (sent 27 Jul 2026).
# Edit only with Aman's explicit approval, never as a side effect.
BODY = """<html><body style="font-family: Calibri, Arial, sans-serif; font-size: 11pt;">
<p>{salutation}</p>
<p>I am Aman, a Harvard Business School student. Adarsh (my classmate at HBS) and I have a combined decade of experience in operations, management, manufacturing, and supply chain. I spent five years running supply chain and new product development at ITC, one of India's largest packaged foods companies, and we've spent the last few years working at frontier AI startups in SF, Boston, and India.</p>
<p>As part of a project, we're studying the current challenges in contract food manufacturing and how AI can help solve them. Among the issues that come up repeatedly in our research is the challenge of proving the same quality system to every brand customer separately, because each one audits the plant against its own standard. During our research, we read that at {short}, {insight}.</p>
<p>We would love to get 30 minutes of your time to deeply understand the problems you're facing today and whether we can help solve them using modern technology.</p>
</body></html>"""


def build_eml(to, salutation, short, insight):
    headers = ["X-Unsent: 1", f"From: {FROM}", f"To: {to}"]
    if CC:
        headers.append(f"Cc: {CC}")
    headers += [f"Subject: {SUBJECT}", "MIME-Version: 1.0",
                "Content-Type: text/html; charset=utf-8", ""]
    assert insight and not insight.endswith("."), "insight clause must not end with a period"
    body = BODY.format(salutation=salutation, short=short, insight=insight)
    assert "{" not in body, "unfilled placeholder"
    return "\n".join(headers) + "\n" + body


def load_tracker():
    if not os.path.exists(TRACKER):
        return []
    with open(TRACKER, newline="") as f:
        return list(csv.DictReader(f))


def main(spec_path):
    spec = json.load(open(spec_path))
    outdir = os.path.join(DRAFTS_ROOT, spec.get("batch", spec["date"]))
    os.makedirs(outdir, exist_ok=True)
    for c in spec["contacts"]:
        path = os.path.join(outdir, f"{spec['slug']}-{c['file']}")
        with open(path, "w") as f:
            f.write(build_eml(c["email"], c["salutation"], spec["short"], spec["insight"]))

    rows = load_tracker()
    # replace this company's non-sent RANKED rows only; sent history and unranked
    # audit rows (bench/excluded, empty Rank) are never touched
    kept = [r for r in rows if not (r["Company"] == spec["company"]
                                    and r["Sent?"] != "Y"
                                    and str(r["Rank"]).strip().isdigit())]
    insight_cell = spec["insight"] + ". " + spec.get("proof", "")
    for c in spec["contacts"]:
        kept.append({"Company": spec["company"], "Rank": c["rank"], "Contact": c["name"],
                     "Title": c["title"], "Email": c["email"], "Email basis": c.get("basis", ""),
                     "Person check": c.get("check", ""), "Insight": insight_cell,
                     "Drafted date": spec["date"], "Sent date": "", "Sent?": "N",
                     "Reply?": "N", "Notes": c.get("notes", "")})
    os.makedirs(os.path.dirname(TRACKER), exist_ok=True)
    with open(TRACKER, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TRACKER_COLUMNS)
        w.writeheader()
        w.writerows(kept)
    print(f"{spec['company']}: {len(spec['contacts'])} emls -> {outdir}/, tracker updated")


if __name__ == "__main__":
    main(sys.argv[1])
