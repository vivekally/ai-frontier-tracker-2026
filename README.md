# The Frontier Board — AI Startup Tracker, August 2026

A standing tracker on three questions:

1. **Who is working on problems nobody has solved?** 38 companies sorted by the
   *problem* rather than the company — self-improving systems, world models,
   continual learning, post-transformer architectures, and AI that runs the
   experiment. Skyfall AI, Mirendil, Oak Lab, Ineffable Intelligence, AMI Labs,
   Discovery Loop, Ndea and the rest.
2. **Where did 2026's money actually go?** A sortable, filterable ledger of 192
   rounds and $394B, 1 January – 7 August 2026, plus regional and lead-investor
   cuts, dilution maths, and the finding underneath all of it: strip the single
   largest round out of each month and the underlying US venture market has been
   flat at roughly $17B since February.
3. **What came out of Y Combinator?** W26, Spring 26 and S26 — batch composition,
   the categories that grew, and the companies worth watching.
4. **How do you track this yourself?** The source stack, the signals that a lab is
   about to launch, a weekly routine, saved queries, and the four errors that make
   most AI funding data wrong.

## Viewing

Open [`index.html`](index.html) in any browser. It is fully self-contained — no
external fonts, scripts or assets, no tracking. Five tabs, deep-linkable via URL
hash (`index.html#money`), with a light/dark/auto toggle in the header.

Live: <https://vivekally.github.io/ai-frontier-tracker-2026/>

## Contents

- **§1 The frontier board** — five unsolved problems, a five-test rubric for
  telling a frontier bet from a wrapper, and the companies attacking each one.
  Filterable by problem cluster.
- **§2 The money** — the ledger of 192 rounds (sort, filter, search, export),
  the US monthly chart with and without each month's largest round, regional and
  investor breakdowns, and implied-dilution maths.
- **§3 Y Combinator** — W26 by category, the ARC-AGI cluster, and the P26/S26 lists.
- **§4 How to track this** — the source stack in four tiers, pre-launch signals, a
  weekly routine, saved queries, and the four common data errors.
- **§5 Watchlist & sources** — eight dated events that would change the page, a
  14-entry conflicts log, method notes, and 36 principal sources.

## The data

[`data/rounds.json`](data/rounds.json) is the single source of truth for the
ledger. [`build.py`](build.py) regenerates [`data/rounds.csv`](data/rounds.csv)
and rewrites the inline data block in `index.html`, so the page and the exports
cannot drift apart.

```bash
$EDITOR data/rounds.json     # add or edit rows
python3 build.py             # regenerate csv + inline block
git commit -am "ledger: ..." && git push
```

Each row carries `company`, `amount_usd_m`, `amount` (as reported), `round`,
`date`, `valuation`, `sector`, `country`, `region`, `ai`, `frontier`, `investors`
and a free-text `note` where a disagreement between sources is written down
rather than silently resolved.

## Caveats

Compiled 7 August 2026 from public reporting. Round sizes, valuations, headcounts
and benchmark scores are press-reported and not independently verified.

The ledger is **not exhaustive** — it is assembled from published monthly and
weekly roundups, so a round no roundup covered is not here, and coverage is
thinner for January and for non-US rounds below $200M. Treat totals as a floor.
The one exception runs the other way: Project Prometheus appears twice because
sources disagree on whether that is one raise or two, so totals may overstate by
up to $12B.

Fourteen figures are reported inconsistently across sources. Every one is in the
conflicts log in §5 with the number this page chose and why. Cluster assignments,
the five tests and the watchlist are editorial judgement.

Not affiliated with, endorsed by, or published by any company named.

## Companion reports

- [The AI Technology Stack](https://vivekally.github.io/ai-stack-report/) — where the value sits, 12 layers, 97 companies.
- [The State of the Labs](https://vivekally.github.io/ai-labs-briefing-2026/) — what 22 frontier labs believe.
- [Index](https://vivekally.github.io/)
