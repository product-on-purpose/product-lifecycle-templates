#!/usr/bin/env python3
"""
check-bundles.py - the governance gate for the template library.

Runs the structural quality checks that the methodology's Definition of Done requires,
across every bundle under templates/. This turns the hand-verification done during
authoring into one repeatable command.

This IS the gate, not a prototype of one: .github/workflows/ci.yml runs this same script
on every push to main and every pull request. It supersedes the Node script suite that the
implementation plan's P3 (port the CI quality gate from pm-skills) had intended; see
docs/internal/decisions/0008-gate-python-local-interim.md.

Coverage is partial by acknowledgement, not by accident: these six checks automate roughly
half the Definition of Done. The rest is human-verified. Do not read a green run as "the
DoD is met"; read it as "the six structural checks pass." Gate hardening is roadmap WP-11.

THE META IS THE CONTRACT. Every check keys off `sizes_available` in the bundle's meta.yaml
rather than assuming a bundle ships lean and full. Most types earn two weights, but seven
Tier-1 catalog types are single-size, and a few may earn three (s/m/l). The gate's job is
to enforce that the files on disk match what the meta declares, in both directions: a
declared variant that is missing is a failure, and a variant file sitting in the bundle
that the meta never declared is also a failure. See
docs/internal/decisions/0010-meta-declares-size-contract.md.

Usage:
    python tools/check-bundles.py            # check every bundle
    python tools/check-bundles.py prd        # check one bundle

Exit code 0 if every check passes, 1 otherwise.

Checks per bundle:
    A. Files present     the six core files, plus exactly the variants the meta declares,
                         and no undeclared variant files
    B. No dashes         no em-dash (U+2014) or en-dash (U+2013) anywhere in the bundle
    C. Nesting           each variant's sections are an ordered subset of the next larger
                         variant's. Not applicable to a single-size bundle, which is
                         reported as such rather than silently passed
    D. Clean example     no {{placeholder}} remains in the worked example
    E. Citations linked  every inline [[n]](#ref-n) resolves to an <a id="ref-n"> anchor,
                         and no bare [n] citation is left unlinked in the companion body
    F. Meta contract     sizes_available exists, is non-empty, and uses one legal size
                         vocabulary rather than mixing them
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
SIZES_RE = re.compile(r"^sizes_available:\s*(.*)$", re.MULTILINE)

# The files every bundle carries regardless of how many size variants it ships.
CORE_ROLES = [
    "companion.md",
    "guide.md",
    "example.md",
    "meta.yaml",
    "history.md",
    "research-log.md",
]

# The two legal size vocabularies, each ordered smallest to largest. A bundle picks ONE.
# lean/full is the default (the catalog's size_variant column shows most types vary in two
# weights). s/m/l exists only where a type genuinely earns three. A single-size bundle
# declares one value from either list, most commonly [lean].
SIZE_VOCABULARIES = [
    ["lean", "full"],
    ["s", "m", "l"],
]
ALL_SIZES = [s for vocab in SIZE_VOCABULARIES for s in vocab]

GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"
BOLD = "\033[1m"
OFF = "\033[0m"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def variant_file(name, size):
    return name + "_template-" + size + ".md"


def find_bundles(root):
    out = []
    for name in sorted(os.listdir(root)):
        d = os.path.join(root, name)
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, name + "_meta.yaml")):
            out.append(name)
    return out


def parse_sizes(name, d):
    """The size contract, read from the meta. Returns (ordered_sizes, error)."""
    p = os.path.join(d, name + "_meta.yaml")
    if not os.path.isfile(p):
        return None, "meta.yaml missing, so the bundle declares no size contract"
    text = read(p)
    m = SIZES_RE.search(text)
    if not m:
        return None, "meta has no sizes_available field; it is the size contract and is required"

    # Accept an inline list [a, b] or a YAML block list on the following lines.
    region = m.group(1)
    for line in text[m.end():].splitlines():
        if re.match(r"\s*-\s+", line):
            region += " " + line
        elif line.strip():
            break

    declared = set(re.findall(r"\b(" + "|".join(ALL_SIZES) + r")\b", region))
    if not declared:
        return None, "sizes_available is empty or unparseable: " + m.group(1).strip()

    for vocab in SIZE_VOCABULARIES:
        if declared <= set(vocab):
            return [s for s in vocab if s in declared], None

    return None, (
        "sizes_available mixes size vocabularies {"
        + ", ".join(sorted(declared))
        + "}; use lean/full OR s/m/l, never both"
    )


def check_files(name, d):
    sizes, err = parse_sizes(name, d)
    if err:
        return False, err

    expected = [variant_file(name, s) for s in sizes] + [name + "_" + r for r in CORE_ROLES]
    missing = [f for f in expected if not os.path.isfile(os.path.join(d, f))]
    if missing:
        return False, "missing: " + ", ".join(missing)

    # The contract runs both ways: a variant file the meta never declared is drift, not a
    # bonus. Without this, a stale template-full.md could linger in a bundle the meta says
    # is lean-only, and nothing would ever notice.
    stray = [
        variant_file(name, s)
        for s in ALL_SIZES
        if s not in sizes and os.path.isfile(os.path.join(d, variant_file(name, s)))
    ]
    if stray:
        return False, "undeclared variant file(s) present: " + ", ".join(sorted(set(stray)))

    return True, str(len(expected)) + " files present, variants {" + ", ".join(sizes) + "}"


def bundle_files(name, d):
    """Every file the bundle actually owns, for whole-bundle scans."""
    out = []
    for s in ALL_SIZES:
        p = os.path.join(d, variant_file(name, s))
        if os.path.isfile(p):
            out.append(p)
    for r in CORE_ROLES:
        p = os.path.join(d, name + "_" + r)
        if os.path.isfile(p):
            out.append(p)
    return out


def check_dashes(name, d):
    hits = []
    for p in bundle_files(name, d):
        for i, line in enumerate(read(p).splitlines(), 1):
            if DASH_RE.search(line):
                hits.append(os.path.basename(p) + ":" + str(i))
    if hits:
        return False, "dash at " + ", ".join(hits[:5]) + (" ..." if len(hits) > 5 else "")
    return True, "no em/en dashes"


def headings(path):
    return HEADING_RE.findall(read(path))


def is_ordered_subset(small, big):
    it = iter(big)
    return all(h in it for h in small)


def check_nesting(name, d):
    sizes, err = parse_sizes(name, d)
    if err:
        return False, err

    if len(sizes) == 1:
        # Not a pass by omission. A single-size bundle has nothing to nest INTO, so the
        # rule is vacuous rather than skipped. Saying so out loud keeps a green run honest.
        return True, "single-variant bundle {" + sizes[0] + "}; nesting rule not applicable"

    # Every variant must nest in the next one up: lean in full, or s in m in l.
    for small, big in zip(sizes, sizes[1:]):
        sp = os.path.join(d, variant_file(name, small))
        bp = os.path.join(d, variant_file(name, big))
        if not (os.path.isfile(sp) and os.path.isfile(bp)):
            return False, "cannot compare " + small + " to " + big + ": a variant file is missing"
        if not is_ordered_subset(headings(sp), headings(bp)):
            extra = [h for h in headings(sp) if h not in headings(bp)]
            detail = "; ".join(extra) if extra else "same sections, wrong order"
            return False, small + " does not nest in " + big + ": " + detail

    counts = ", ".join(s + "=" + str(len(headings(os.path.join(d, variant_file(name, s))))) for s in sizes)
    return True, "nests " + " < ".join(sizes) + " (" + counts + ")"


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


def check_meta_contract(name, d):
    sizes, err = parse_sizes(name, d)
    if err:
        return False, err
    vocab = next(v for v in SIZE_VOCABULARIES if set(sizes) <= set(v))
    shape = "single-size" if len(sizes) == 1 else str(len(sizes)) + "-variant"
    return True, shape + ", vocabulary {" + "/".join(vocab) + "}, declares {" + ", ".join(sizes) + "}"


CHECKS = [
    ("A files", check_files),
    ("B dashes", check_dashes),
    ("C nesting", check_nesting),
    ("D example", check_example),
    ("E citations", check_citations),
    ("F meta", check_meta_contract),
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
