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
import json
import os
import re
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

MARKER = re.compile(r"<!--\s*counts:\s*(?P<body>[^>]*?)\s*-->", re.I)

# A fenced code block is a SPECIMEN, not a claim. The inline-code case was fixed on 2026-08-07 and the
# fenced case was never covered, so writing docs/explanation/architecture-detailed.md hit it twice:
# first with real-looking values copied from this file's own docstring, then with a KEY=VALUE
# placeholder that failed as an unknown fact name. Any future document explaining the marker syntax
# hits it again. The sibling folder-readme check calls stripFences for exactly this reason, so until
# now the two checks disagreed about whether a documented example is data.
FENCE = re.compile(r"^(?P<f>```+|~~~+).*?^(?P=f)[ \t]*$", re.M | re.S)

# Documents whose numbers describe a MOMENT, not the tree as it stands. A release note states what was
# true at that release; a v0.2.0 note saying "the gate grew from 15 CI steps to 20" is correct forever
# and becomes false the moment this check forces it to say 22. Gating a dated snapshot against current
# truth does not prevent drift, it manufactures it. Exempted by directory rather than by name because a
# new release note appears on every release and an exemption nobody remembers to extend is not one.
# The exemption is PRINTED on every run, following check-research-logs.py, so it stays visible rather
# than becoming a quiet hole.
FROZEN_PREFIXES = ("docs/releases/",)


def blank_fences(text):
    """Replace fenced-block bodies with spaces, preserving length so offsets stay valid."""
    return FENCE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)


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

    # Tier comes from the catalog, never from an assumption about which bundles are Tier 1.
    #
    # This read `len(bundle_dirs) - (1 if "rfc" in bundle_dirs else 0)` until 2026-09-02, with a comment
    # explaining that rfc was the one Tier-2 bundle and "every other bundle is a Tier-1 type". That was
    # true when it was written and stopped being true the moment Tier-2 building opened: ADR 0039 removed
    # the pull gate, ADR 0041 made the maintainer's preference set the order, and ADR 0042 admitted `epic`
    # as the second Tier-2 bundle ever built. The old expression then counted epic into the Tier-1 floor
    # and reported it as 26 of 27 with 1 remaining, when the floor is 25 with 2 refused under ADR 0030.
    #
    # A hardcoded exception list is a claim about the tree that nothing re-checks. The catalog's `built`
    # flag is derived by gen-atlas.py from the tree itself, and CI gates its freshness, so reading tier
    # from there cannot drift the same way. This does couple this check to a fresh catalog-data.json;
    # that coupling is deliberate and cheaper than the assumption it replaces.
    catalog_path = os.path.join(ROOT, "atlas", "catalog-data.json")
    with open(catalog_path, encoding="utf-8") as fh:
        catalog = json.load(fh)
    catalog_types = catalog["types"] if isinstance(catalog, dict) and "types" in catalog else catalog
    if isinstance(catalog_types, dict):
        catalog_types = list(catalog_types.values())
    tier1_types = [t for t in catalog_types if t.get("tier") == 1]
    tier1_built = sum(1 for t in tier1_types if t.get("built"))
    tier1_total = len(tier1_types)

    # The catalog `state` split, added 2026-09-11 because STATE.md's copy of it had drifted in all three
    # numbers at once (26/177/61 against a real 27/176/58) and one of them, the 61, was never true at any
    # point - the catalog read 59 on the day that sentence was written. That is DF-5 exactly, and DF-5's
    # own remedy is that a fact this repository states about itself should be GENERATED, not retyped.
    #
    # `commoncandidates` is deliberately `candidate` AND `rarity: common`, not "unbuilt and common",
    # which is 60 and includes the two `out-of-scope` types that ADR 0030 refused. The prose says
    # "candidate types" for the same reason: an ambiguous noun makes a gated number un-checkable, since
    # a reader cannot tell which population the check is counting.
    states = [t.get("state") for t in catalog_types]
    state_built = sum(1 for s in states if s == "built")
    state_candidate = sum(1 for s in states if s == "candidate")
    state_oos = sum(1 for s in states if s == "out-of-scope")
    common_candidates = sum(1 for t in catalog_types
                            if t.get("state") == "candidate" and t.get("rarity") == "common")

    return {
        "bundles": _int_from(bundles_out, r"OK\s+(\d+) bundle"),
        "tier1": tier1_built,
        "tier1remaining": tier1_total - tier1_built,
        "statebuilt": state_built,
        "statecandidate": state_candidate,
        "stateoutofscope": state_oos,
        "commoncandidates": common_candidates,
        "adrs": len(adrs),
        "adrmax": max(int(f[:4]) for f in adrs) if adrs else 0,
        "cisteps": len(re.findall(r"^\s+-\s+(?:name|uses):", ci, re.M)),
        "checkk": _int_from(_run("tools/test-check-k.py"), r"OK\s+(\d+) assertions"),
        "checkformats": _int_from(_run("tools/test-check-formats.py"), r"OK\s+(\d+) assertions"),
        "checklogs": _int_from(_run("tools/test-check-research-logs.py"), r"OK\s+(\d+) assertions"),
        "logsgated": _int_from(logs_out, r"contract: (\d+) log"),
        "sourcesgated": _int_from(logs_out, r"(\d+) source"),
    }


# The install-time descriptions. These are JSON, so they cannot carry an HTML comment, which is why they
# sat outside this check for its whole life while being the FIRST prose most users ever read: the plugin
# description is what Claude Code shows at install time, and `library.json`'s is what the registry reads.
#
# Both had gone stale, in different facts, and each had gone stale before - the changelog records
# `plugin.json` claiming 26 bundles and 25 CI steps once already. A defect that recurs after a convention
# gets a check rather than another fix, so these are scanned by PATTERN instead of by marker.
JSON_SURFACES = [".claude-plugin/plugin.json", "library.json"]

# Deliberately narrow. A pattern loose enough to catch every number in a sentence would fire on the
# 205-type catalog figure, which is not a fact this check computes, and a check that cries wolf gets
# suppressed rather than fixed.
JSON_CLAIMS = [
    (re.compile(r"\b(\d+) (?:researched )?(?:document-template )?bundles\b"), "bundles"),
    (re.compile(r"\b(\d+) CI steps\b"), "cisteps"),
]


def json_surface_claims():
    """(path, fact, claimed, snippet) for every number a description states that the tree also knows."""
    out = []
    for rel in JSON_SURFACES:
        path = os.path.join(ROOT, rel)
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as fh:
            desc = json.load(fh).get("description", "") or ""
        for pattern, fact in JSON_CLAIMS:
            for m in pattern.finditer(desc):
                start = max(0, m.start() - 20)
                out.append((rel, fact, int(m.group(1)), desc[start:m.end() + 20].strip()))
    return out


def marked_files():
    """Tracked markdown carrying counts markers, as (label, {fact: claimed}) per MARKER found.

    EVERY marker in a file is read, not just the first. Until 2026-08-07 this used `search`, so a
    document could carry only one gated claim no matter how many numbers it stated, and the check's own
    declared blind spot (it compares markers, never the prose around them) had no remedy available to an
    author who wanted one. The DF-5 defect recurred eight times, and the geometry was the same every
    time: a stale sentence sitting a hundred or more lines from the single marker at the top of its file.
    README.md line 273 was found saying "All nineteen bundles currently pass" against a tree of 25, 142
    lines below a marker that was green and correct.

    With `finditer`, a marker can sit beside the sentence it governs. That does not make the check able to
    read prose, which is still impossible and still stated in its own output. It makes the blind spot
    ADDRESSABLE: an author who knows a sentence quotes a number can now pin it, one line above.
    """
    tracked = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT,
                             capture_output=True, text=True).stdout.split()
    out = []
    frozen = []
    for rel in tracked:
        if rel.replace(os.sep, "/").startswith(FROZEN_PREFIXES):
            frozen.append(rel)
            continue
        path = os.path.join(ROOT, rel)
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        # A marker inside a fenced block documents the syntax; it does not assert anything.
        text = blank_fences(text)
        # A marker wrapped in backticks is an ILLUSTRATION, not a claim. STATE.md's own DF-5 write-up
        # quotes a specimen marker in prose to explain the mechanism, and reading it as live was a
        # regression introduced with finditer on 2026-08-07: the specimen names counts from July and
        # would fail forever. An inline code span is how markdown says "this is an example of a thing",
        # so it is skipped, and the skip is narrow enough that a real marker cannot hide behind it.
        markers = [m for m in MARKER.finditer(text)
                   if not (text[max(0, m.start() - 1):m.start()] == "`"
                           and text[m.end():m.end() + 1] == "`")]
        for n, m in enumerate(markers, 1):
            claimed = {}
            for pair in m.group("body").split(","):
                if "=" not in pair:
                    continue
                k, v = pair.split("=", 1)
                try:
                    claimed[k.strip().lower()] = int(v.strip())
                except ValueError:
                    claimed[k.strip().lower()] = None
            # Label a second or later marker by line, so a failure names WHICH claim went stale.
            label = rel if len(markers) == 1 else "%s (marker %d, line %d)" % (
                rel, n, text.count("\n", 0, m.start()) + 1)
            out.append((label, claimed))
    return out, frozen


def main():
    facts = live_facts()
    files, frozen = marked_files()

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

    json_claims = json_surface_claims()
    for rel, fact, claimed, snippet in json_claims:
        if fact in facts and claimed != facts[fact]:
            bad = True
            print(RED + "FAIL" + OFF + "  %s (description)" % rel)
            print("        %s says %d, the tree says %d" % (fact, claimed, facts[fact]))
            print("        ...%s..." % snippet)

    print("\nself-reported counts: %d document(s) carry a marker; %d number(s) checked across %d "
          "install-time description(s)" % (len(files), len(json_claims), len(JSON_SURFACES)))
    if frozen:
        print(DIM + "      %d dated snapshot(s) exempt, by directory, and named here so the hole stays"
              % len(frozen) + OFF)
        print(DIM + "      visible: %s" % ", ".join(frozen) + OFF)
        print(DIM + "      A release note states what was true AT that release. Gating it against the"
              + OFF)
        print(DIM + "      tree as it stands today would force a correct record to become a false one."
              + OFF)

    if bad:
        print("\n" + RED + "FAIL" + OFF + "  a number this repository states about itself has changed.")
        print("        Do NOT just edit the marker. Re-read the document: the prose around it")
        print("        quotes these numbers, and the prose is what a reader believes.")
        return 1

    print(GREEN + "OK" + OFF + "  every marked document agrees with the tree, and so does every number "
          "the\n      install-time descriptions state.")
    print(DIM + "      not verified: the prose. This check compares markers, and cannot read the"
          "\n      sentences that quote them. A green run means no number has changed since an"
          "\n      author last confirmed the text, not that the text is correct." + OFF)
    return 0


if __name__ == "__main__":
    sys.exit(main())
