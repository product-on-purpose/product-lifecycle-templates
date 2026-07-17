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

Coverage is partial by acknowledgement, not by accident: these nine checks automate roughly
half the Definition of Done. The rest is human-verified. Do not read a green run as "the
DoD is met"; read it as "the structural checks pass." Gate hardening is roadmap WP-11.

Eight checks are pure standard library and always run. The ninth (G, frontmatter YAML)
needs a real parser, which the stdlib does not provide; it uses PyYAML where available and
SKIPS with a clear message otherwise, so a local run without the dependency still gates the
other eight. CI installs PyYAML, so G is enforced there, which since M0 is the enforcement
point. See docs/internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md.

WHAT THE GATE STILL CANNOT DO, STATED PLAINLY.
Check E proves a citation RESOLVES. It cannot prove the cited source SUPPORTS the claim. The
2026-07-16 citation pass (WP-10) found 28 defects across four bundles that had been passing
green for weeks, including two wrong dates, two quotations from sources that could never be
read, and several claims attributed to authors who do not make them. Every one of those was
invisible here and always will be. A green run means the structure holds, not that the
content is true.

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
    E. Citations linked  BOTH directions: every inline [[n]](#ref-n) resolves to an anchor,
                         AND every anchor is cited by something (a reference nothing cites is
                         padding); no bare [n] left unlinked in the companion body
    F. Meta contract     sizes_available exists, is non-empty, uses one legal size vocabulary
                         rather than mixing them, and the meta carries no unfilled placeholder
    G. Frontmatter YAML  the meta.yaml and every template/example frontmatter block parse
                         as valid YAML (so placeholders must be quoted); needs PyYAML, and
                         SKIPS with a message if it is not installed
    H. History           the history has an entry for the template_version the meta claims
    I. Refs resolve      pairs_with names a skill on the pinned list (tools/known-skills.txt);
                         related_templates names a bundle that exists, or uses future:
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "templates"))

# en-dash (U+2013) and em-dash (U+2014), built from codepoints so no glyph sits in this file
DASH_RE = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")
# Captures the level as well as the text. A heading's identity is (level, text), not text
# alone: demoting "## Rollout" to "### Rollout" restructures the document, and a text-only
# comparison cannot see it. See headings().
HEADING_RE = re.compile(r"^(#{2,6})\s+(.*?)\s*$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"\{\{[a-z0-9_]+\}\}")
INLINE_CITE_RE = re.compile(r"\(#ref-(\d+)\)")
ANCHOR_RE = re.compile(r'id="ref-(\d+)"')
BARE_CITE_RE = re.compile(r"(?<!\[)\[(\d+)\](?!\()")
SIZES_RE = re.compile(r"^sizes_available:\s*(.*)$", re.MULTILINE)
VERSION_RE = re.compile(r"^template_version:\s*(.+?)\s*$", re.MULTILINE)
PAIRS_RE = re.compile(r"^pairs_with:\s*(.*)$", re.MULTILINE)
RELATED_RE = re.compile(r"^related_templates:\s*(.*)$", re.MULTILINE)

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
YELLOW = "\033[33m"
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
    """The outline as (level, text) tuples, H2 and deeper.

    Text alone is not a heading's identity. Demoting "## Rollout and Adoption" to
    "### Rollout and Adoption" is a real structural change, and a text-only comparison either
    misses it or (worse) reports the section as simply absent, because the old regex matched
    H2 only. Comparing tuples makes the level part of the contract, which is what the nesting
    rule actually means: the smaller variant's outline must appear in the larger one, at the
    same depths, in the same order.
    """
    return [(len(h), t) for h, t in HEADING_RE.findall(read(path))]


def fmt_heading(h):
    level, text = h
    return "#" * level + " " + text


def yaml_list(region, text, start):
    """The values of a YAML list field, whether inline [a, b] or a block list beneath it.

    Deliberately regex-level rather than a real parse: this runs in the pure-stdlib checks,
    which must work without PyYAML (decision 0014 grants the dependency to check G only).
    Check G is what proves the file is really YAML; this only has to read a list the gate
    already knows is well-formed.
    """
    region = region.strip()
    items = []
    if region.startswith("["):
        inner = region[1:region.rindex("]")] if "]" in region else region[1:]
        items = [i.strip().strip("\"'") for i in inner.split(",")]
    else:
        for line in text[start:].splitlines():
            m = re.match(r"\s*-\s+(.*?)\s*$", line)
            if m:
                items.append(m.group(1).strip().strip("\"'"))
            elif line.strip():
                break
    return [i for i in items if i]


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
            detail = "; ".join(fmt_heading(h) for h in extra) if extra else "same sections, wrong order"
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
    """Citations must resolve in BOTH directions.

    Forward (an inline [n] with no anchor) was always checked. The reverse (an anchor nothing
    cites) was not, and WP-10 proved it matters: on 2026-07-16 the PRD bundle was found
    carrying two references with zero citations each, and the gate had passed it green every
    run since June. A reference nothing cites is padding, and padding is how a bibliography
    borrows authority it never used. The methodology has forbidden it in prose since v0.1
    ("Do not pad the list with sources you did not actually use"); this is the clause finally
    getting automation.

    Anchors are collected from the References section only. Cross-references inside a
    reference entry (an entry pointing at another entry, e.g. a paywalled source noting where
    its claims were corroborated) count as citations, because they are a real use.
    """
    p = os.path.join(d, name + "_companion.md")
    if not os.path.isfile(p):
        return False, "companion missing"
    text = read(p)
    body = text.split("## References", 1)[0]
    anchors = set(ANCHOR_RE.findall(text))
    inline = set(INLINE_CITE_RE.findall(body))
    # A reference may legitimately point at another reference; that is a use, not padding.
    cited = set(INLINE_CITE_RE.findall(text))

    dangling = sorted(inline - anchors, key=int)
    padded = sorted(anchors - cited, key=int)
    bare = sorted(set(BARE_CITE_RE.findall(body)), key=int)

    problems = []
    if dangling:
        problems.append("inline [" + ", ".join(dangling) + "] have no anchor")
    if padded:
        problems.append(
            "padded: reference(s) [" + ", ".join(padded) + "] are never cited; cite them or cut them"
        )
    if bare:
        problems.append("unlinked citation(s) [" + ", ".join(bare) + "] in body")
    if problems:
        return False, "; ".join(problems)
    return True, str(len(anchors)) + " anchors, " + str(len(inline)) + " cited in body, none padded"


def check_meta_contract(name, d):
    sizes, err = parse_sizes(name, d)
    if err:
        return False, err

    # A placeholder in the META is different in kind from one left in a template. The template
    # variants are SUPPOSED to carry {{placeholders}}: that is what makes them templates. The
    # meta is the bundle's own description of itself, so an unfilled placeholder there is an
    # authoring miss that ships as a false claim about the bundle.
    p = os.path.join(d, name + "_meta.yaml")
    left = PLACEHOLDER_RE.findall(read(p))
    if left:
        return False, "meta has unfilled placeholder(s): " + ", ".join(sorted(set(left)))

    vocab = next(v for v in SIZE_VOCABULARIES if set(sizes) <= set(v))
    shape = "single-size" if len(sizes) == 1 else str(len(sizes)) + "-variant"
    return True, shape + ", vocabulary {" + "/".join(vocab) + "}, declares {" + ", ".join(sizes) + "}"


def check_history(name, d):
    """The history must have an entry for the version the meta currently claims.

    Without this, `template_version` can be bumped with no changelog entry, and the per-bundle
    history silently stops being a history. The entry is matched at the start of a heading, so
    both "## 0.1.0 - 2026-06-30" and "## 0.1.0, reviewed 2026-07-16 - citation pass" satisfy
    it: the rule is that the current version is accounted for, not that it is worded a
    particular way.
    """
    mp = os.path.join(d, name + "_meta.yaml")
    hp = os.path.join(d, name + "_history.md")
    if not os.path.isfile(hp):
        return False, "history missing"
    m = VERSION_RE.search(read(mp))
    if not m:
        return False, "meta has no template_version"
    version = m.group(1).strip().strip("\"'")

    heads = [t for lvl, t in headings(hp)]
    if not any(re.match(r"^" + re.escape(version) + r"\b", h) for h in heads):
        return False, (
            "no history entry for template_version " + version
            + "; bumping the version without a changelog entry makes the history a fiction"
        )
    return True, "history documents " + version


def known_skills():
    """The pinned skill-ID list. Absent file = no list to check against, so the check SKIPs."""
    p = os.path.join(SCRIPT_DIR, "known-skills.txt")
    if not os.path.isfile(p):
        return None
    out = []
    for line in read(p).splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def check_refs(name, d):
    """`pairs_with` and `related_templates` must point at things that exist.

    Both fields make claims about the world, and nothing else in the repo checks either:

    - `pairs_with` claims a pm-skills skill reaches for this template. Resolved against a
      pinned list (tools/known-skills.txt), because CI has no sibling clone and no network.
      An empty list is legal and meaningful: the `rfc` bundle has no paired skill because no
      `develop-rfc` skill exists (finding EC-3).
    - `related_templates` claims a sibling type is related. It must name a bundle that exists
      on disk, or use the `future:` prefix for one that does not exist yet. The prefix is the
      whole point: it lets a bundle honestly reference a type the library has not built,
      without that reference rotting into a broken claim.
    """
    p = os.path.join(d, name + "_meta.yaml")
    text = read(p)
    problems = []
    detail = []

    skills = known_skills()
    m = PAIRS_RE.search(text)
    if m:
        pairs = yaml_list(m.group(1), text, m.end())
        if skills is None:
            detail.append("pairs_with unchecked (no pinned skill list)")
        elif not pairs:
            detail.append("pairs_with [] (no paired skill)")
        else:
            unknown = [s for s in pairs if s not in skills]
            if unknown:
                problems.append(
                    "pairs_with names unknown skill(s): " + ", ".join(unknown)
                    + " (add to tools/known-skills.txt only after verifying in pm-skills)"
                )
            else:
                detail.append("pairs_with " + str(len(pairs)) + " resolved")

    local = set(find_bundles(TEMPLATES_DIR))
    m = RELATED_RE.search(text)
    if m:
        related = yaml_list(m.group(1), text, m.end())
        bad = []
        for r in related:
            if r.startswith("future:"):
                if not r[len("future:"):].strip():
                    bad.append(r + " (empty future: reference)")
                continue
            if r not in local:
                bad.append(r)
        if bad:
            problems.append(
                "related_templates does not resolve: " + ", ".join(bad)
                + " (name a bundle that exists, or prefix future: if it does not yet)"
            )
        else:
            detail.append("related_templates " + str(len(related)) + " resolved")

    if problems:
        return False, "; ".join(problems)
    return True, "; ".join(detail) if detail else "no pairs_with or related_templates declared"


def frontmatter(text):
    """The YAML frontmatter block if the file opens with one, else None."""
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    return m.group(1) if m else None


def check_frontmatter_yaml(name, d):
    """Every YAML in the bundle must actually parse as YAML.

    Returns (None, ...) to SKIP when PyYAML is absent; the other five checks are pure
    stdlib and always run, so a local run without the dependency still gates most of the DoD.

    This check exists because of a real escape: on 2026-07-14 the ADR bundle shipped with
    `decision-makers: [{{decision_makers}}]` in both template frontmatters, which is a flow
    mapping with an unhashable key and therefore invalid YAML, and the gate passed it green.
    The gate reads sizes_available with a regex and never parsed YAML as YAML, so "the
    frontmatter is well-formed" was a Definition-of-Done clause with no automation behind it.
    Placeholders must be quoted ("{{title}}") to parse, which is exactly the discipline that
    would have caught the bug. The stdlib has no YAML parser; the one dependency is granted by
    docs/internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md.
    """
    try:
        import yaml
    except ImportError:
        return None, "SKIPPED: PyYAML not installed (pip install pyyaml to run this check locally; CI enforces it)"

    targets = []
    meta = os.path.join(d, name + "_meta.yaml")
    if os.path.isfile(meta):
        targets.append((os.path.basename(meta), read(meta)))
    for p in bundle_files(name, d):
        if p.endswith(".md"):
            block = frontmatter(read(p))
            if block is not None:
                targets.append((os.path.basename(p), block))

    bad = []
    for label, block in targets:
        try:
            yaml.safe_load(block)
        except yaml.YAMLError as e:
            bad.append(label + " (" + str(e).splitlines()[0] + ")")
    if bad:
        return False, "invalid YAML in " + "; ".join(bad[:3]) + (" ..." if len(bad) > 3 else "")
    return True, str(len(targets)) + " YAML block(s) parse"


CHECKS = [
    ("A files", check_files),
    ("B dashes", check_dashes),
    ("C nesting", check_nesting),
    ("D example", check_example),
    ("E citations", check_citations),
    ("F meta", check_meta_contract),
    ("G yaml", check_frontmatter_yaml),
    ("H history", check_history),
    ("I refs", check_refs),
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
            # Three states: True = PASS, False = FAIL (counts against the build),
            # None = SKIP (a check that could not run, e.g. an optional dependency is
            # absent; reported honestly rather than silently counted as a pass).
            if ok is False:
                total_fail += 1
                mark = RED + "FAIL" + OFF
            elif ok is None:
                mark = YELLOW + "SKIP" + OFF
            else:
                mark = GREEN + "PASS" + OFF
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
