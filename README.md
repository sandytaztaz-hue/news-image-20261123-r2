# Sum 23 — Monday 23 November 2026

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![Rank](https://make.fun/badge/news-image-20261123/sandytaztaz-hue/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![Reward](https://make.fun/badge/news-image-20261123/sandytaztaz-hue/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

Entry for [news-image-20261123](https://make.fun/bounty/news-image-20261123) on make.fun: one image that sums up the world's news of Monday 23 November 2026.

The image is a drawn broadsheet front page for Monday 23 November 2026, carrying 36 stories across 7 regions, with 13 illustrated scenes — three hero stories (the COP31 collapse in Antalya, the Russian ship still burning in the Gulf of Finland, and Verstappen's wild Las Vegas Grand Prix win) plus ten illustrated minis, a stat strip, and a timeline of the day.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the bundled `entry.png` into the output directory given by `MAKEFUN_OUTPUT_DIR` (or `/output`) and verifies the SHA-256 of what it wrote before exiting. It also checks the bundled image's own hash first, so a damaged copy in the repository fails fast instead of shipping a wrong file.

Try it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## What's on the page

- 3 heroes: COP31 collapses with no deal · Russian ship still ablaze off Finland · Verstappen wins a wild Las Vegas GP
- 10 illustrated minis, each with a verification tag (CONFIRMED, OFFICIAL, REPORTED, FORECAST)
- Also-on lines numbered 14–36, a six-number stat strip, and a six-moment timeline
- 7 regions: Europe, Middle East, Asia, Americas, Africa, Oceania, Global
