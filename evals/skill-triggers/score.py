#!/usr/bin/env python3
"""score.py - read `claude plugin eval` results for the skill-trigger suite, and apply the release rule.

Two jobs.

1. Per case, it prints how many runs loaded the expected skill, and which skills each run actually
   loaded, read from the run's trace. The pass count alone cannot tell a confused agent from one
   that loaded nothing: on 2026-11-26 the trace tally is what showed a split caused no confusion.
   Traces exist only when the run used `--keep-temp`.

2. With `--base` and `--new`, it applies the release rule from ADR 0093 (generated skill
   descriptions, split by family group):
   - A case tagged `fragile` that ran 15 times on both wordings BLOCKS when the new wording loads
     the right skill on 3 or more fewer runs. Five runs cannot separate a regression from noise on
     these cases, which is why they run at 15, on both wordings, in one session.
   - Any other case is compared with `baseline.json`. A drop of 2 or more runs in 5 is printed as
     READ: it does not block, because a 5-run result is noisy, but the maintainer reads it.

Usage:
    python evals/skill-triggers/score.py <result.json> [...]
    python evals/skill-triggers/score.py --base <base-fragile.json> --new <new-fragile.json> [--suite <new-suite.json>]

Exit 0 when nothing blocks; 1 when a fragile case blocks or an input is partial. Pure standard library.
"""

import argparse
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_RE = re.compile(r'"name"\s*:\s*"Skill"\s*,\s*"input"\s*:\s*\{[^}]*?"skill"\s*:\s*"(?:[\w-]+:)?([\w-]+)"')
BLOCK_DROP = 3
READ_DROP = 2


def skills_loaded(trace_path):
    if not trace_path or not os.path.exists(trace_path):
        return None
    with open(trace_path, encoding="utf-8", errors="replace") as f:
        return sorted({m.group(1) for line in f for m in SKILL_RE.finditer(line)})


def load(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    out = {}
    for c in d["cases"]:
        runs = c["arms"]["with"]
        tally = Counter()
        for r in runs:
            s = skills_loaded(r.get("tracePath"))
            tally["no trace" if s is None else ("+".join(s) or "none")] += 1
        out[c["name"]] = {"passed": sum(1 for r in runs if r.get("passed")), "runs": len(runs), "tally": dict(tally)}
    return d, out


def report(path):
    d, cases = load(path)
    print(f"== {path}: partial={d.get('partial')} cost=${d.get('costUsd', 0):.2f}")
    for name, c in cases.items():
        print(f"  {name:28} {c['passed']}/{c['runs']}  {c['tally']}")
    print(f"  TOTAL {sum(c['passed'] for c in cases.values())}/{sum(c['runs'] for c in cases.values())}")
    return d, cases


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("results", nargs="*")
    ap.add_argument("--base", help="fragile cases, 15 runs, on the released wording")
    ap.add_argument("--new", help="fragile cases, 15 runs, on the new wording, from the same session")
    ap.add_argument("--suite", help="every case, 5 runs, on the new wording")
    args = ap.parse_args()

    status = 0
    for p in args.results:
        d, _ = report(p)
        if d.get("partial"):
            status = 1
    if not (args.base or args.new or args.suite):
        return status
    if bool(args.base) != bool(args.new):
        print("FAIL  --base and --new go together: the fragile cases run on both wordings in one session")
        return 1

    if args.base:
        db, base = report(args.base)
        dn, new = report(args.new)
        if db.get("partial") or dn.get("partial"):
            print("FAIL  a fragile run is partial, so the rule cannot be applied")
            status = 1
        for name in sorted(set(base) & set(new)):
            b, n = base[name], new[name]
            if b["runs"] != 15 or n["runs"] != 15:
                print(f"FAIL  {name}: the rule needs 15 runs on each wording, got {b['runs']} and {n['runs']}")
                status = 1
                continue
            drop = b["passed"] - n["passed"]
            verdict = "BLOCK" if drop >= BLOCK_DROP else "ok"
            print(f"{verdict:5} {name}: base {b['passed']}/15, new {n['passed']}/15")
            if verdict == "BLOCK":
                status = 1

    if args.suite:
        ds, suite = report(args.suite)
        if ds.get("partial"):
            print("FAIL  the suite run is partial")
            status = 1
        with open(os.path.join(HERE, "baseline.json"), encoding="utf-8") as f:
            baseline = json.load(f)["cases"]
        for name, c in suite.items():
            b = baseline.get(name)
            if not b or b["runs"] == 0 or c["runs"] == 0:
                print(f"READ  {name}: no baseline to compare with")
                continue
            expected = b["passed"] * c["runs"] / b["runs"]
            if expected - c["passed"] >= READ_DROP:
                print(f"READ  {name}: {c['passed']}/{c['runs']}, baseline {b['passed']}/{b['runs']} ({b['source']})")
    print("BLOCKED: the maintainer reads the result before release" if status else "No block.")
    return status


if __name__ == "__main__":
    sys.exit(main())
