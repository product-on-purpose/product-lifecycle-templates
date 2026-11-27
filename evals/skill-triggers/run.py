#!/usr/bin/env python3
"""run.py - run the skill-trigger suite the way a release that changes a description must.

The release rule, from ADR 0093 (generated skill descriptions, split by family group):
  1. Every case runs at 5 runs on the new wording (the working tree).
  2. The cases tagged `fragile` run at 15 runs on BOTH wordings, in this one session, because
     their rate swings between sessions. The old wording is the latest release tag by default.
  3. score.py applies the rule: a fragile case that drops 3 or more runs in 15 blocks the release
     until the maintainer reads it.

It spends money, so it only prints its plan unless you pass --go. Every run uses Sonnet,
`--ablation none`, `--no-publish`, and a cost cap per eval. Results, logs and traces land in --out,
which must be outside the repository.

Usage:
    python evals/skill-triggers/run.py                    # print the plan and the cost caps
    python evals/skill-triggers/run.py --go               # run the release procedure
    python evals/skill-triggers/run.py --smoke --go       # one case, one run, about USD 0.05
    python evals/skill-triggers/run.py --base v0.28.1 --go

Needs the `claude` CLI on PATH, and a Claude Code login that can run `claude plugin eval`.
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
PY = sys.executable

COMMON = ["--ablation", "none", "--model", "sonnet", "--no-publish", "--trust-plugin", "--threshold", "0", "--keep-temp"]


def latest_tag():
    r = subprocess.run(["git", "-C", ROOT, "tag", "--list", "v*", "--sort=-v:refname"], capture_output=True, text=True)
    tags = [t for t in r.stdout.split() if t[1:2].isdigit()]
    if not tags:
        sys.exit("no release tag found; pass --base")
    return tags[0]


def build(label, ref, out):
    cmd = [PY, os.path.join(HERE, "build-arm.py"), "--label", label, "--out", out] + (["--ref", ref] if ref else [])
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr or r.stdout)
    print(r.stdout.splitlines()[0])
    return r.stdout.strip().splitlines()[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--base", help="the released wording to compare the fragile cases with; default is the latest tag")
    ap.add_argument("--out", default=os.path.join(tempfile.gettempdir(), "plt-skill-triggers"))
    ap.add_argument("--smoke", action="store_true", help="one case, one run: proves the harness starts")
    ap.add_argument("--go", action="store_true", help="actually run; without it, only print the plan")
    args = ap.parse_args()
    sys.stdout.reconfigure(line_buffering=True)  # keep this script's lines in order with its children's

    claude = shutil.which("claude")
    base = args.base or latest_tag()
    out = os.path.abspath(args.out)

    if args.smoke:
        jobs = [("smoke", "new", ["--case", "prd", "--runs", "1", "-j", "1", "--max-cost-usd", "1"])]
    else:
        jobs = [
            ("suite-new", "new", ["--runs", "5", "-j", "2", "--max-cost-usd", "15"]),
            ("fragile-new", "new", ["--tag", "fragile", "--runs", "15", "-j", "2", "--max-cost-usd", "4"]),
            ("fragile-base", "base", ["--tag", "fragile", "--runs", "15", "-j", "2", "--max-cost-usd", "4"]),
        ]
    cap = sum(float(j[2][j[2].index("--max-cost-usd") + 1]) for j in jobs)
    print(f"plan: {len(jobs)} eval(s), cost caps total USD {cap:.0f}; new wording = working tree, base = {base}; out = {out}")
    for name, arm, extra in jobs:
        print(f"  {name}: claude plugin eval <arm-{arm}> {' '.join(extra)} {' '.join(COMMON)}")
    if not args.go:
        print("Nothing run. Pass --go to spend it.")
        return 0
    if not claude:
        sys.exit("the claude CLI is not on PATH")

    arms = {"new": build("new", None, out)}
    if not args.smoke:
        arms["base"] = build("base", base, out)
    procs = []
    for name, arm, extra in jobs:
        res = os.path.join(out, f"{name}.json")
        log = open(os.path.join(out, f"{name}.log"), "w", encoding="utf-8")
        cmd = [claude, "plugin", "eval", arms[arm]] + extra + COMMON + ["--json", res]
        procs.append((name, res, subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT), log))
    for name, res, p, log in procs:
        p.wait()
        log.close()
        print(f"{name}: exit {p.returncode}, results {res}")
    score = [PY, os.path.join(HERE, "score.py")]
    if args.smoke:
        score.append(procs[0][1])
    else:
        r = {n: res for n, res, _, _ in procs}
        score += ["--base", r["fragile-base"], "--new", r["fragile-new"], "--suite", r["suite-new"]]
    return subprocess.run(score).returncode


if __name__ == "__main__":
    sys.exit(main())
