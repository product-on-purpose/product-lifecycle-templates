#!/usr/bin/env python3
"""
check-counts.py - the numbers this repository states about itself must match the tree.

WHY THIS EXISTS (finding DF-5, "prose counts drift", in STATE.md).
Five times now, a count retyped into prose has gone stale within hours of the thing it counts changing:
the bundle inventory, two self-test assertion counts, the gated-log count, a README badge that sat at
11 of 27 while the real figure reached 17, and the freshness banners in `roadmap.md` and `plan.md` that
were added to manage staleness and then went stale themselves.

The pattern is exact and it is not about diligence. **Every count this repository GENERATES stays fresh.
Every count it RETYPES goes stale.** The control case is the README's `<!-- bundle-count: N -->` marker,
which `gen-manifest.py --check` has compared against reality on every run since it was added, and which
has never drifted once.

WHAT THIS CHECK DOES.
Each participating document carries one marker line listing the repository facts it quotes in prose:

    <!-- counts: bundles=18, tier1=17, adrs=29 -->

The check recomputes each fact from the tree and fails when a marker disagrees. That is all it can do.

WHAT IT DOES NOT DO, STATED PLAINLY AND PRINTED ON EVERY RUN.
It cannot read prose. A marker that agrees with the tree does NOT mean the sentences around it are
correct; it means nobody has changed the underlying number since the last time an author confirmed them.
The check's real job is to make a changed number IMPOSSIBLE TO MISS, so an author re-reads the file
rather than discovering the drift in a review six weeks later. Treat a failure as "go re-read this
document", not as "change this one number".

Pure standard library. Runs in CI alongside the gate.
Usage: python tools/check-counts.py
"""
import os
import re
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

MARKER = re.compile(r"<!--\s*counts:\s*(?P<body>[^>]*?)\s*-->", re.I)


ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _run(*args):
    """Run one of the repo's own tools and return its stdout, colour codes stripped.

    The tools colour their OK and FAIL markers, so a pattern like `OK\\s+(\\d+)` silently matches
    nothing against raw output. That failure mode is invisible: the fact comes back as -1 and every
    marker disagrees with it, which looks like the documents are wrong rather than the check.
    """
    out = subprocess.run([sys.executable] + list(args), cwd=ROOT,
                         capture_output=True, text=True).stdout
    return ANSI.sub("", out)


def _int_from(text, pattern):
    m = re.search(pattern, text)
    return int(m.group(1)) if m else -1


def live_facts():
    """Every fact a document may claim, computed from the tree rather than remembered."""
    bundles_out = _run("tools/check-bundles.py")
    logs_out = _run("tools/check-research-logs.py")

    # A bundle is a directory carrying <name>_meta.yaml, which is the SAME test check-bundles.py and
    # gen-manifest.py use. This once read "any directory not starting with . or _", and the three tools
    # then disagreed about what a bundle is: on 2026-08-04 a half-built business-case holding only its
    # research log was counted here as a built Tier-1 type while check-bundles reported "no matching
    # bundle" and gen-manifest ignored it, so the counts gate went red for something that was not a
    # defect. During a long build run every partially-drafted bundle would do the same. The meta is the
    # right marker because it is the file that declares a bundle's identity; a directory without one is
    # work in progress, not a bundle.
    templates = os.path.join(ROOT, "templates")
    bundle_dirs = [d for d in sorted(os.listdir(templates))
                   if os.path.isdir(os.path.join(templates, d))
                   and not d.startswith((".", "_"))
                   and os.path.isfile(os.path.join(templates, d, d + "_meta.yaml"))]

    decisions = os.path.join(ROOT, "docs", "internal", "decisions")
    adrs = [f for f in os.listdir(decisions) if re.match(r"^\d{4}-.+\.md$", f)]

    ci = open(os.path.join(ROOT, ".github", "workflows", "ci.yml"), encoding="utf-8").read()

    # rfc is catalog Tier 2, built early; every other bundle is a Tier-1 type. See D-D in buildout-specs.
    tier1_built = len(bundle_dirs) - (1 if "rfc" in bundle_dirs else 0)

    return {
        "bundles": _int_from(bundles_out, r"OK\s+(\d+) bundle"),
        "tier1": tier1_built,
        "tier1remaining": 27 - tier1_built,
        "adrs": len(adrs),
        "adrmax": max(int(f[:4]) for f in adrs) if adrs else 0,
        "cisteps": len(re.findall(r"^\s+-\s+(?:name|uses):", ci, re.M)),
        "checkk": _int_from(_run("tools/test-check-k.py"), r"OK\s+(\d+) assertions"),
        "checkformats": _int_from(_run("tools/test-check-formats.py"), r"OK\s+(\d+) assertions"),
        "checklogs": _int_from(_run("tools/test-check-research-logs.py"), r"OK\s+(\d+) assertions"),
        "logsgated": _int_from(logs_out, r"contract: (\d+) log"),
        "sourcesgated": _int_from(logs_out, r"(\d+) source"),
    }


def marked_files():
    """Tracked markdown carrying a counts marker, as (path, {fact: claimed})."""
    tracked = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT,
                             capture_output=True, text=True).stdout.split()
    out = []
    for rel in tracked:
        path = os.path.join(ROOT, rel)
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        m = MARKER.search(text)
        if not m:
            continue
        claimed = {}
        for pair in m.group("body").split(","):
            if "=" not in pair:
                continue
            k, v = pair.split("=", 1)
            try:
                claimed[k.strip().lower()] = int(v.strip())
            except ValueError:
                claimed[k.strip().lower()] = None
        out.append((rel, claimed))
    return out


def main():
    facts = live_facts()
    files = marked_files()

    if not files:
        print(RED + "FAIL" + OFF + "  no document carries a counts marker. At least STATE.md should.")
        return 1

    bad = False
    for rel, claimed in files:
        problems = []
        for key, value in claimed.items():
            if key not in facts:
                problems.append("unknown fact %r (known: %s)" % (key, ", ".join(sorted(facts))))
            elif value is None:
                problems.append("%s has no integer value" % key)
            elif value != facts[key]:
                problems.append("%s says %d, the tree says %d" % (key, value, facts[key]))
        if problems:
            bad = True
            print(RED + "FAIL" + OFF + "  %s" % rel)
            for p in problems:
                print("        " + p)

    print("\nself-reported counts: %d document(s) carry a marker" % len(files))

    if bad:
        print("\n" + RED + "FAIL" + OFF + "  a number this repository states about itself has changed.")
        print("        Do NOT just edit the marker. Re-read the document: the prose around it")
        print("        quotes these numbers, and the prose is what a reader believes.")
        return 1

    print(GREEN + "OK" + OFF + "  every marked document agrees with the tree.")
    print(DIM + "      not verified: the prose. This check compares markers, and cannot read the"
          "\n      sentences that quote them. A green run means no number has changed since an"
          "\n      author last confirmed the text, not that the text is correct." + OFF)
    return 0


if __name__ == "__main__":
    sys.exit(main())
