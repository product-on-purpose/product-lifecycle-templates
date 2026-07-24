#!/usr/bin/env python3
"""check-adr-index.py - the ADR index in docs/internal/decisions/README.md lists every ADR, and only real ones.

The decision-record index is a hand-maintained table in docs/internal/decisions/README.md, one row per
ADR. Hand-maintained indexes drift: 0022 and 0023 were both landed without an index row and sat missing
for a session (fixed in PR #33). This is the same failure class as the manifest (ADR 0018), the atlas
built flags (gen-atlas), and the counts PR #30 corrected: a derived list kept honest only by memory.

This gate closes it without generating the index (the per-ADR one-line summaries are curated prose worth
writing by hand). It checks two directions:
  - every NNNN-*.md decision file has a row in the index table;
  - every row in the index points to a decision file that exists.

The index table row shape it keys on is `| [NNNN](NNNN-slug.md) | summary | date |`.

Usage:
    python tools/check-adr-index.py     # exit 1 if the index and the files on disk disagree

Exit 0 if in sync; 1 on any mismatch.
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
DECISIONS_DIR = os.path.join(ROOT, "docs", "internal", "decisions")
INDEX = os.path.join(DECISIONS_DIR, "README.md")

FILE_RE = re.compile(r"^(\d{4})-.+\.md$")
# An index table row's first cell: | [NNNN](NNNN-slug.md) | ...
ROW_RE = re.compile(r"^\|\s*\[(\d{4})\]\((\d{4})-[^)]+\.md\)", re.MULTILINE)

GREEN = "\033[32m"
RED = "\033[31m"
OFF = "\033[0m"


def main():
    if not os.path.isfile(INDEX):
        print(RED + "FAIL" + OFF + "  no ADR index at docs/internal/decisions/README.md")
        return 1

    files = {m.group(1) for m in map(FILE_RE.match, os.listdir(DECISIONS_DIR)) if m}

    text = open(INDEX, encoding="utf-8").read()
    indexed = set()
    mismatched = []  # rows where the display number and the link target disagree
    for disp, target in ROW_RE.findall(text):
        indexed.add(disp)
        if disp != target:
            mismatched.append((disp, target))

    problems = []
    missing = sorted(files - indexed)
    if missing:
        problems.append("ADR file(s) with no index row: " + ", ".join(missing))
    dangling = sorted(indexed - files)
    if dangling:
        problems.append("index row(s) with no ADR file: " + ", ".join(dangling))
    if mismatched:
        problems.append("index row(s) whose number does not match the linked file: "
                        + ", ".join("%s->%s" % (d, t) for d, t in mismatched))

    if problems:
        print(RED + "FAILED" + OFF + "  ADR index out of sync:")
        for p in problems:
            print("        " + p)
        print("        fix docs/internal/decisions/README.md so its table lists every NNNN-*.md file.")
        return 1

    print(GREEN + "OK" + OFF + "  ADR index lists all %d decision records, and only real ones." % len(files))
    return 0


if __name__ == "__main__":
    sys.exit(main())
