#!/usr/bin/env python3
"""
check-changelog.py - every decision record must be mentioned in the changelog.

WHY THIS EXISTS.
This repository already gates three generated artifacts for freshness (manifest.json, the atlas, the ADR
index), and each of those checks was written after the corresponding drift was found in the tree. The
changelog had no such check, and it drifted exactly as far as the absence of enforcement predicts: at the
time this script was written, `[Unreleased]` was empty while 28 commits, nine bundles, five family contracts
and fourteen decision records had landed since 0.1.0. Recorded as finding EC-6 in STATE.md.

The rule: if a decision is important enough to get a record, it is important enough to appear in the
changelog, either in a released section or in [Unreleased].

WHAT THIS CHECK DOES *NOT* VERIFY, STATED PLAINLY.
It asserts that the string "ADR NNNN" or a link to the record appears somewhere in CHANGELOG.md. It does
NOT verify that the entry describes the decision, sits in the right release section, or is accurate. A
changelog line reading "ADR 0028 (see the ADR)" would satisfy it. This is a drift alarm, not a review, and
it is deliberately shallow so that it is deterministic and cheap. Do not read a green run as "the changelog
is good"; read it as "no decision record is missing from it."

Pure standard library. Runs in CI alongside the gate.
Usage: python tools/check-changelog.py
"""
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
DECISIONS = os.path.join(ROOT, "docs", "internal", "decisions")
CHANGELOG = os.path.join(ROOT, "CHANGELOG.md")

GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"

# Records predating the changelog convention. 0.1.0 was the first tagged release (2026-07-17) and its
# changelog entry describes the shipped library rather than enumerating the decisions behind it. Requiring
# those retroactively would mean rewriting a released section, which is exactly what Keep a Changelog says
# not to do. New records get no such exemption.
GRANDFATHERED = set(range(1, 15))


def adr_numbers():
    out = {}
    for name in sorted(os.listdir(DECISIONS)):
        m = re.match(r"^(\d{4})-(.+)\.md$", name)
        if m:
            out[int(m.group(1))] = name
    return out


def main():
    if not os.path.isfile(CHANGELOG):
        print(RED + "FAIL" + OFF + "  CHANGELOG.md not found")
        return 1

    text = open(CHANGELOG, encoding="utf-8").read()
    records = adr_numbers()
    if not records:
        print(RED + "FAIL" + OFF + "  no decision records found under docs/internal/decisions/")
        return 1

    missing, grandfathered_missing = [], []
    for num, filename in sorted(records.items()):
        # Either a prose reference ("ADR 0028") or a link to the file counts.
        cited = re.search(r"ADR[\s-]*0*%d\b" % num, text) or (filename in text)
        if cited:
            continue
        (grandfathered_missing if num in GRANDFATHERED else missing).append(num)

    print("changelog freshness: %d decision record(s) on disk\n" % len(records))

    if grandfathered_missing:
        print(DIM + "  %d pre-0.1.0 record(s) not cited, exempt by design: %s"
              % (len(grandfathered_missing),
                 ", ".join("%04d" % n for n in grandfathered_missing)) + OFF)

    if missing:
        print(RED + "FAIL" + OFF + "  %d decision record(s) missing from CHANGELOG.md:" % len(missing))
        for num in missing:
            print("        %04d  %s" % (num, records[num]))
        print("\n  Add a line under [Unreleased], or under the release that shipped it.")
        return 1

    # Say what was not checked, every run. A check whose limits are only in its source file
    # gets read as stronger than it is.
    print(GREEN + "OK" + OFF + "  every decision record after 0.1.0 is cited in CHANGELOG.md")
    print(DIM + "      not verified: whether each entry is accurate, well-placed, or meaningful." + OFF)
    return 0


if __name__ == "__main__":
    sys.exit(main())
