#!/usr/bin/env python3
"""
check-links.py - the link gate.

Fails the build if any tracked Markdown file contains a relative link that does not resolve,
or an in-page anchor that matches no heading in the target file.

WHY THIS EXISTS, SPECIFICALLY.
Twice now, a directory move has silently broken links that no check caught:

  1. Decision 0009 (scaffold graduation) moved the library out of _local/ and broke four
     companion links. The bundle gate passed green. A human found them.
  2. Decision 0013 (the _local/ split) rewrote ten links across the README, the methodology,
     and every companion. Nothing but this script could have proved they all landed.

check-bundles.py does not check links and should not: it enforces bundle STRUCTURE. Links are a
repo-wide property, so they get a repo-wide check. This script is the fitness function named in
decision 0013's Confirmation section, which is the only thing that makes that decision enforceable
rather than merely stated.

THE RULE IT ENFORCES ABOVE ALL: a tracked file may never link into _local/. That path resolves on
exactly one machine on earth and 404s for every other reader. Going public made this a correctness
issue rather than a tidiness one.

Pure standard library, per decision 0008.

Usage:
    python tools/check-links.py

Exit code 0 if every link resolves, 1 otherwise.
"""

import os
import re
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

LINK_RE = re.compile(r"\[[^\]]*\]\(\s*([^)\s]+?)\s*\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.MULTILINE)
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "#!")

GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"
OFF = "\033[0m"


def tracked_markdown():
    out = subprocess.run(
        ["git", "-C", ROOT, "ls-files", "*.md"],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    return [f for f in out if f]


def slug(heading):
    """GitHub's anchor slug: lowercase, drop punctuation, then map EACH space to a hyphen.

    The per-space mapping matters and is easy to get wrong. "Open Questions / Decisions" loses
    the slash and keeps the two spaces around it, so it anchors as `open-questions--decisions`
    with a DOUBLE hyphen. Collapsing runs of whitespace (`\\s+`) produces a single hyphen and
    reports a valid link as broken. This checker shipped with exactly that bug and flagged a
    working anchor on its first run.
    """
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s", "-", s).strip("-")


def anchors(path):
    """Every anchor a file offers: heading slugs, plus explicit <a id="..."> targets."""
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return set()
    out = {slug(h) for h in HEADING_RE.findall(text)}
    out |= set(re.findall(r'id="([^"]+)"', text))
    return out


def main():
    files = tracked_markdown()
    if not files:
        print("no tracked markdown found (is this a git repo?)")
        return 1

    anchor_cache = {}
    problems = []
    checked = 0

    for f in files:
        src = os.path.join(ROOT, f)
        try:
            text = open(src, encoding="utf-8").read()
        except OSError as e:
            problems.append((f, "-", "unreadable: " + str(e)))
            continue

        for raw in LINK_RE.findall(text):
            if raw.startswith(SKIP_PREFIXES):
                continue
            checked += 1

            target, _, frag = raw.partition("#")

            # The rule this whole script exists for.
            if "_local/" in target:
                problems.append((f, raw, "links into _local/, which is untracked; promote the file into docs/internal/ instead (decision 0013)"))
                continue

            if target:
                dest = os.path.normpath(os.path.join(os.path.dirname(src), target))
                if not os.path.exists(dest):
                    problems.append((f, raw, "dead path"))
                    continue
            else:
                dest = src  # a bare "#anchor" points at this same file

            if frag:
                if dest not in anchor_cache:
                    anchor_cache[dest] = anchors(dest)
                if anchor_cache[dest] and frag not in anchor_cache[dest]:
                    problems.append((f, raw, "no such anchor in target"))

    if problems:
        for f, raw, why in problems:
            print(RED + "BROKEN" + OFF + "  " + f)
            print("        " + raw)
            print("        " + DIM + why + OFF)
        print("")
        print(RED + "FAILED" + OFF + "  " + str(len(problems)) + " broken link(s) across " + str(len(files)) + " files.")
        return 1

    print(GREEN + "OK" + OFF + "  " + str(checked) + " relative link(s) across " + str(len(files)) + " files, all resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
