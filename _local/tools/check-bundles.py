#!/usr/bin/env python3
"""
check-bundles.py - the governance gate for the template library.

Runs the structural quality checks that the methodology's Definition of Done requires,
across every bundle under _local/templates/. This turns the hand-verification done during
authoring into one repeatable command. It is a local prototype of the CI gate planned in
the implementation plan (P3).

Usage:
    python _local/tools/check-bundles.py            # check every bundle
    python _local/tools/check-bundles.py prd        # check one bundle

Exit code 0 if every check passes, 1 otherwise.

Checks per bundle:
    A. Files present     the eight canonical bundle files exist
    B. No dashes         no em-dash (U+2014) or en-dash (U+2013) anywhere in the bundle
    C. Nesting           lean sections are an ordered subset of full sections
    D. Clean example     no {{placeholder}} remains in the worked example
    E. Citations linked  every inline [[n]](#ref-n) resolves to an <a id="ref-n"> anchor,
                         and no bare [n] citation is left unlinked in the companion body
    F. Meta sizes        sizes_available in the meta matches the variant files present
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "templates"))

# en-dash (U+2013) and em-dash (U+2014), built from codepoints so no glyph sits in this file
DASH_RE = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")
HEADING_RE = re.compile(r"^##\s+(.*?)\s*$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"\{\{[a-z0-9_]+\}\}")
INLINE_CITE_RE = re.compile(r"\(#ref-(\d+)\)")
ANCHOR_RE = re.compile(r'id="ref-(\d+)"')
BARE_CITE_RE = re.compile(r"(?<!\[)\[(\d+)\](?!\()")

ROLES = [
    "template-lean.md",
    "template-full.md",
    "companion.md",
    "guide.md",
    "example.md",
    "meta.yaml",
    "history.md",
    "research-log.md",
]

GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"
BOLD = "\033[1m"
OFF = "\033[0m"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def find_bundles(root):
    out = []
    for name in sorted(os.listdir(root)):
        d = os.path.join(root, name)
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, name + "_meta.yaml")):
            out.append(name)
    return out


def check_files(name, d):
    missing = [r for r in ROLES if not os.path.isfile(os.path.join(d, name + "_" + r))]
    if missing:
        return False, "missing: " + ", ".join(missing)
    return True, "all 8 files present"


def check_dashes(name, d):
    hits = []
    for r in ROLES:
        p = os.path.join(d, name + "_" + r)
        if not os.path.isfile(p):
            continue
        for i, line in enumerate(read(p).splitlines(), 1):
            if DASH_RE.search(line):
                hits.append(name + "_" + r + ":" + str(i))
    if hits:
        return False, "dash at " + ", ".join(hits[:5]) + (" ..." if len(hits) > 5 else "")
    return True, "no em/en dashes"


def headings(path):
    return HEADING_RE.findall(read(path))


def is_ordered_subset(small, big):
    it = iter(big)
    return all(h in it for h in small)


def check_nesting(name, d):
    lean = os.path.join(d, name + "_template-lean.md")
    full = os.path.join(d, name + "_template-full.md")
    if not (os.path.isfile(lean) and os.path.isfile(full)):
        return False, "lean or full variant missing"
    ls, fs = headings(lean), headings(full)
    if not is_ordered_subset(ls, fs):
        extra = [h for h in ls if h not in fs]
        return False, "lean headings not an ordered subset of full: " + ("; ".join(extra) if extra else "order differs")
    return True, str(len(ls)) + " lean sections nest in " + str(len(fs)) + " full"


def check_example(name, d):
    p = os.path.join(d, name + "_example.md")
    if not os.path.isfile(p):
        return False, "example missing"
    left = PLACEHOLDER_RE.findall(read(p))
    if left:
        uniq = sorted(set(left))
        return False, str(len(left)) + " placeholders left: " + ", ".join(uniq[:5])
    return True, "no placeholders"


def check_citations(name, d):
    p = os.path.join(d, name + "_companion.md")
    if not os.path.isfile(p):
        return False, "companion missing"
    text = read(p)
    body = text.split("## References", 1)[0]
    anchors = set(ANCHOR_RE.findall(text))
    inline = set(INLINE_CITE_RE.findall(body))
    dangling = sorted(inline - anchors, key=int)
    bare = sorted(set(BARE_CITE_RE.findall(body)), key=int)
    problems = []
    if dangling:
        problems.append("inline [" + ", ".join(dangling) + "] have no anchor")
    if bare:
        problems.append("unlinked citation(s) [" + ", ".join(bare) + "] in body")
    if problems:
        return False, "; ".join(problems)
    return True, str(len(anchors)) + " anchors, " + str(len(inline)) + " cited, all resolve"


def check_meta_sizes(name, d):
    p = os.path.join(d, name + "_meta.yaml")
    if not os.path.isfile(p):
        return False, "meta missing"
    text = read(p)
    m = re.search(r"sizes_available:\s*(.*)", text)
    if not m:
        return True, "no sizes_available field (skipped)"
    # collect size tokens from an inline [a, b] list or a following block list
    region = m.group(1)
    tail = text[m.end():]
    for line in tail.splitlines():
        if re.match(r"\s*-\s+", line):
            region += " " + line
        elif line.strip() and not line.startswith(" "):
            break
    declared = set(re.findall(r"\b(lean|full|s|m|l)\b", region))
    present = set()
    if os.path.isfile(os.path.join(d, name + "_template-lean.md")):
        present.add("lean")
    if os.path.isfile(os.path.join(d, name + "_template-full.md")):
        present.add("full")
    for w in ("s", "m", "l"):
        if os.path.isfile(os.path.join(d, name + "_template-" + w + ".md")):
            present.add(w)
    if declared and declared != present:
        return False, "meta says {" + ", ".join(sorted(declared)) + "} but files are {" + ", ".join(sorted(present)) + "}"
    return True, "sizes match files: {" + ", ".join(sorted(present)) + "}"


CHECKS = [
    ("A files", check_files),
    ("B dashes", check_dashes),
    ("C nesting", check_nesting),
    ("D example", check_example),
    ("E citations", check_citations),
    ("F meta", check_meta_sizes),
]


def main():
    if not os.path.isdir(TEMPLATES_DIR):
        print("templates dir not found: " + TEMPLATES_DIR)
        return 1
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    bundles = find_bundles(TEMPLATES_DIR)
    if only:
        bundles = [b for b in bundles if b in only]
        if not bundles:
            print("no matching bundle for: " + ", ".join(only))
            return 1
    total_fail = 0
    for name in bundles:
        d = os.path.join(TEMPLATES_DIR, name)
        print(BOLD + name + OFF)
        for label, fn in CHECKS:
            ok, detail = fn(name, d)
            if not ok:
                total_fail += 1
            mark = (GREEN + "PASS" + OFF) if ok else (RED + "FAIL" + OFF)
            print("  " + mark + "  " + label.ljust(12) + DIM + detail + OFF)
        print("")
    n = len(bundles)
    if total_fail == 0:
        print(GREEN + "OK" + OFF + "  " + str(n) + " bundle(s), all checks passed.")
        return 0
    print(RED + "FAILED" + OFF + "  " + str(total_fail) + " check(s) across " + str(n) + " bundle(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
