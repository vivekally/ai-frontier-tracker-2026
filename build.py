#!/usr/bin/env python3
"""Build step for the Frontier Board tracker.

`data/rounds.json` is the single source of truth for the funding ledger.
This script:

  1. writes `data/rounds.csv`  (flat export, one row per round)
  2. rewrites the inline <script id="rounds-data"> block in index.html
     so the page ships the same data with no external requests

Run it after every edit to data/rounds.json:

    python3 build.py

It is idempotent and prints what changed.
"""

import csv
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
DATA = ROOT / "data" / "rounds.json"
CSV_OUT = ROOT / "data" / "rounds.csv"
HTML = ROOT / "index.html"

FIELDS = [
    "company", "month", "date", "amount", "amount_usd_m", "round",
    "valuation", "valuation_usd_m", "sector", "country", "region",
    "ai", "frontier", "investors", "note",
]

START = '<script id="rounds-data" type="application/json">'
END = "</script>"


def load():
    with DATA.open() as fh:
        return json.load(fh)


def write_csv(doc):
    rows = sorted(doc["rounds"], key=lambda r: (r["month"], -(r["amount_usd_m"] or 0)))
    with CSV_OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            row = dict(r)
            row["investors"] = "; ".join(r["investors"])
            w.writerow(row)
    return len(rows)


def inject(doc):
    """Replace the inline JSON block in index.html with the current dataset."""
    html = HTML.read_text()
    if START not in html:
        sys.exit(f"error: {HTML.name} has no <script id=\"rounds-data\"> block")

    # Minified payload: the page only needs rounds, not the meta prose.
    payload = json.dumps(doc["rounds"], separators=(",", ":"), ensure_ascii=False)
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    new = pattern.sub(START + payload + END, html, count=1)

    if new == html:
        return False
    HTML.write_text(new)
    return True


def main():
    doc = load()
    n = write_csv(doc)
    changed = inject(doc)
    total = sum(r["amount_usd_m"] or 0 for r in doc["rounds"])
    print(f"rounds:      {n}")
    print(f"tracked:     ${total/1000:,.1f}B")
    print(f"csv:         {CSV_OUT.relative_to(ROOT)}")
    print(f"index.html:  {'updated' if changed else 'already current'}")


if __name__ == "__main__":
    main()
