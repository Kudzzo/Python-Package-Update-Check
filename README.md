# pypi-health-auditor

A small, no-nonsense Python CLI tool I built to sanity-check packages from a `requirements.txt` file against the PyPI JSON API.

Instead of guessing whether a dependency exists on PyPI, lists a `requires_python` constraint, or quietly breaks a setup, this script pulls the metadata, flags weird/missing info, and drops a readable summary so I can see what's going on at a glance.

## Why I Built It
- I wanted a practical Python project that actually does something useful instead of a toy tutorial script.
- I wanted clean separation between reading files, talking to the network, checking package data, and writing reports—without over-engineering it into 20 files and heavy frameworks.

## How It Works
- `parser.py` — Reads `requirements.txt` and cleans up package lines.
- `fetcher.py` — Queries `https://pypi.org/pypi/<package>/json` with `requests` (including timeouts and error handling) and separates found package metadata from errors/misses.
- `analyzer.py` — Checks the fetched metadata and assigns statuses like `OK` or `WARNING` (for example, when `requires_python` is missing/`None`).
- `reporter.py` — Prints a quick terminal summary and saves `report.md` and `report.json`.
- `cli.py` — Ties the pipeline together with `argparse` so it can be run from the command line.

## Setup & Usage
Install `requests`:

```bash
pip install requests
