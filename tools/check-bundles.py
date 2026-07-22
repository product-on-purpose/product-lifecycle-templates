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

Coverage is partial by acknowledgement, not by accident: these eleven checks automate roughly
half the Definition of Done. The rest is human-verified. Do not read a green run as "the
DoD is met"; read it as "the structural checks pass." Gate hardening is roadmap WP-11.

Nine checks are pure standard library and always run. Two need a real parser the stdlib
does not provide, and both SKIP with a clear message when their dependency is absent, so a
bare-Python local run still gates the other nine: G (frontmatter YAML) uses PyYAML, and J
(meta schema) uses PyYAML plus a JSON Schema validator. CI installs both, so G and J are
enforced there, which since M0 is the enforcement point. See
docs/internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md (G) and
docs/internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md (J).

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
    J. Meta schema       the meta.yaml validates against tools/meta.schema.json: required
                         fields present, enums legal, and exactly one of phase / classification
                         (the ADR 0015 XOR). Needs PyYAML and a JSON Schema validator; SKIPS
                         if either is absent
    K. Family            a bundle declaring a family conforms to that family's contract: the
                         family-specific values (delivery-docs requires phase deliver, a beta/stable
                         status, and a lean/full size shape; methodology is descriptive, not gated)
                         and the contract file resolves. Families with no ratified contract yet pass
                         with a note
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "templates"))
SCHEMA_PATH = os.path.join(SCRIPT_DIR, "meta.schema.json")

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
DEFAULT_SIZE_RE = re.compile(r"^default_size:\s*(.+?)\s*$", re.MULTILINE)
VERSION_RE = re.compile(r"^template_version:\s*(.+?)\s*$", re.MULTILINE)
PAIRS_RE = re.compile(r"^pairs_with:\s*(.*)$", re.MULTILINE)
RELATED_RE = re.compile(r"^related_templates:\s*(.*)$", re.MULTILINE)
FAMILY_RE = re.compile(r"^family:\s*(.+?)\s*$", re.MULTILINE)
PHASE_RE = re.compile(r"^phase:\s*(.+?)\s*$", re.MULTILINE)
CLASSIFICATION_RE = re.compile(r"^classification:\s*(.+?)\s*$", re.MULTILINE)
STATUS_RE = re.compile(r"^status:\s*(.+?)\s*$", re.MULTILINE)

# A meta declares `phase` XOR `classification` (ADR 0015); the schema's oneOf enforces the exclusivity
# in check J. Check K gates whichever of the two its family's contract names, so a classification-axis
# family (governance-docs, standing-standards) is one registry entry, not new check code.
AXIS_KEYS = ("phase", "classification")
AXIS_RE = {"phase": PHASE_RE, "classification": CLASSIFICATION_RE}

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

# Family contracts: for a declared family, the metadata constraints its members must meet (the
# contract's Section 2 allowed-values table) and the contract document that spells them out. A family
# narrows the general schema: any legal phase is fine by check J, but a delivery-docs member's phase
# must be `deliver`. Methodology is descriptive, not a membership criterion, so it is not gated here
# (ADR 0020). Only families with a ratified contract appear here; a bundle in a family with no contract
# yet passes check K with a note, so adding a family does not fail the gate before its contract exists.
# See docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md.
#
# AXIS: each entry declares exactly ONE of `phase` or `classification`, naming the axis that family is
# coherent on (ADR 0015). Both families below are phase-axis; a standing family such as governance-docs
# declares `"classification": "utility"` instead. Declaring both, or neither, is a registry error and
# check K reports it rather than silently gating nothing.
FAMILY_CONTRACTS = {
    "delivery-docs": {
        "contract": "docs/internal/contracts/delivery-docs.md",
        "phase": "deliver",
        "status": ["beta", "stable"],
        "size_shapes": [["lean", "full"], ["lean"]],
    },
    "decision-docs": {
        "contract": "docs/internal/contracts/decision-docs.md",
        "phase": "develop",
        "status": ["beta", "stable"],
        "size_shapes": [["lean", "full"], ["lean"]],
    },
}

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
    text = read(p)
    left = PLACEHOLDER_RE.findall(text)
    if left:
        return False, "meta has unfilled placeholder(s): " + ", ".join(sorted(set(left)))

    # default_size must name one of the declared sizes. The schema (check J) constrains it to a
    # legal size value and requires it, but a JSON Schema cannot express "is a member of THIS
    # meta's sizes_available"; that cross-field rule lives here.
    m = DEFAULT_SIZE_RE.search(text)
    default = m.group(1).strip().strip("\"'") if m else None
    if default is not None and default not in sizes:
        return False, "default_size " + default + " is not one of sizes_available {" + ", ".join(sizes) + "}"

    vocab = next(v for v in SIZE_VOCABULARIES if set(sizes) <= set(v))
    shape = "single-size" if len(sizes) == 1 else str(len(sizes)) + "-variant"
    detail = shape + ", vocabulary {" + "/".join(vocab) + "}, declares {" + ", ".join(sizes) + "}"
    if default is not None:
        detail += ", default " + default
    return True, detail


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


def load_yaml_unique(yaml, text):
    """Parse YAML like safe_load, but raise on a duplicate mapping key.

    yaml.safe_load silently keeps the last of duplicate keys, so a meta with
    `phase: something-bogus` on one line and `phase: deliver` on the next parses to
    phase=deliver, and the bogus first value is invisible to every check. A duplicate key is an
    authoring error, and a duplicate `phase` would quietly defeat the very XOR check J exists to
    enforce. This loader rejects the duplication. (Check G's safe_load shares the blind spot;
    tightening it there is tracked as a follow-up.)
    """
    class UniqueKeyLoader(yaml.SafeLoader):
        pass

    def construct_mapping(loader, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in mapping:
                raise yaml.YAMLError("duplicate key " + repr(key) + " in mapping")
            mapping[key] = loader.construct_object(value_node, deep=deep)
        return mapping

    UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)
    return yaml.load(text, Loader=UniqueKeyLoader)


def check_meta_schema(name, d):
    """Every meta.yaml must validate against tools/meta.schema.json, the metadata contract.

    Check G proves the meta is well-formed YAML; this proves it is a well-formed META. Where G
    accepts `status: banana`, or a meta missing `license` entirely, or one carrying both a
    `phase` and a `classification`, J rejects them, because the schema names what a meta must
    contain and which values are legal, not merely that it parses. The XOR is the point: ADR
    0015 settled that a bundle declares exactly one of `phase` (a lifecycle artifact) or
    `classification` (a standing, cross-phase artifact), never both and never neither, and the
    schema is where that rule finally has automation. See
    docs/internal/decisions/0016-adopt-machine-checkable-metadata-schema.md.

    Two dependencies, both SKIPped honestly when absent (the ADR 0014 pattern, extended to a
    second check by docs/internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md):
    PyYAML to parse the meta, and a JSON Schema validator to check it. The stdlib has neither.
    CI installs both, so J is enforced there; a bare-Python local run SKIPs it and still gets
    the eight pure-stdlib checks.

    YAML dates need care. `last_reviewed: 2026-07-16` parses to a datetime.date, which a JSON
    Schema validator (a JSON tool) rejects against `type: string`. The parsed meta is passed
    through a JSON round-trip (json.dumps(..., default=str)) first, so the validator sees the
    six JSON types the schema is written against, and the date is checked as the ISO string it
    is on disk.
    """
    try:
        import yaml
    except ImportError:
        return None, "SKIPPED: PyYAML not installed (pip install pyyaml jsonschema to run this check locally; CI enforces it)"
    try:
        import jsonschema
    except ImportError:
        return None, "SKIPPED: jsonschema not installed (pip install jsonschema to run this check locally; CI enforces it)"
    import json

    if not os.path.isfile(SCHEMA_PATH):
        return False, "tools/meta.schema.json is missing; the metadata contract has no schema to validate against"
    try:
        schema = json.loads(read(SCHEMA_PATH))
    except json.JSONDecodeError as e:
        return False, "tools/meta.schema.json is not valid JSON: " + str(e).splitlines()[0]
    try:
        jsonschema.Draft202012Validator.check_schema(schema)
    except jsonschema.exceptions.SchemaError as e:
        return False, "tools/meta.schema.json is not a valid Draft 2020-12 schema: " + str(e).splitlines()[0]

    mp = os.path.join(d, name + "_meta.yaml")
    if not os.path.isfile(mp):
        return False, "meta.yaml missing"
    try:
        raw = load_yaml_unique(yaml, read(mp))
    except (yaml.YAMLError, ValueError, OverflowError) as e:
        # ValueError/OverflowError cover a bare invalid calendar date such as
        # `last_reviewed: 2026-13-01`, which PyYAML tries to build with datetime.date() and
        # which raises before validation. Catch it so the gate reports a failure, not a crash.
        return False, "meta.yaml is not valid YAML: " + str(e).splitlines()[0]
    # Normalize YAML-native scalars (dates especially) to JSON types before validating, so the
    # JSON Schema validator sees the JSON the schema is written against. allow_nan=False turns a
    # non-finite float (YAML .inf / .nan) into a controlled failure instead of non-standard JSON.
    try:
        data = json.loads(json.dumps(raw, default=str, allow_nan=False))
    except ValueError:
        return False, "meta.yaml contains a non-finite number (Infinity or NaN), which is not a legal value"
    if not isinstance(data, dict):
        return False, "meta.yaml is not a mapping at the top level"

    # format_checker enforces `format: date`, so an impossible calendar date like 2026-02-30
    # (which the structural pattern alone accepts) is rejected.
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if not errors:
        # JSON Schema `type: integer` admits an integral float (29.0), because the spec defines
        # integer mathematically, not by representation. A catalog_ref should be a real int.
        cref = data.get("catalog_ref")
        if isinstance(cref, float):
            return False, "does not match meta.schema.json - catalog_ref must be a whole integer, not the float " + repr(cref)
        axis = "phase" if "phase" in data else "classification"
        return True, "validates against meta.schema.json (" + axis + " axis)"

    has_p, has_c = "phase" in data, "classification" in data
    msgs = []
    for err in errors[:4]:
        path = list(err.path)
        if err.validator == "oneOf" and not path:
            # The top-level XOR. jsonschema's default message dumps the whole meta; say what is
            # actually wrong instead. The final else is a safety net for a future tightening of
            # the branches; it is unreachable while exactly-one-present satisfies exactly one branch.
            if has_p and has_c:
                msgs.append("declares both phase and classification; exactly one is allowed (ADR 0015)")
            elif not has_p and not has_c:
                msgs.append("declares neither phase nor classification; exactly one is required (ADR 0015)")
            else:
                msgs.append("phase/classification: " + err.message)
        elif err.validator == "oneOf" and path == ["sizes_available"]:
            sizes = data.get("sizes_available")
            if isinstance(sizes, list) and not sizes:
                msgs.append("sizes_available is empty; declare at least one size from lean/full or s/m/l")
            else:
                msgs.append("sizes_available mixes size vocabularies; use lean/full OR s/m/l, never both")
        else:
            loc = "/".join(str(p) for p in path) or "(meta root)"
            msgs.append(loc + ": " + err.message)
    more = " ..." if len(errors) > 4 else ""
    return False, "does not match meta.schema.json - " + "; ".join(msgs) + more


def check_family(name, d):
    """A bundle that declares a family must conform to that family's contract.

    Where check J validates a meta against the general schema (any legal phase, any legal status), a
    family narrows those to its own values: a delivery-docs member's phase must be `deliver`, not
    merely a legal phase, and its status and size shape must match the family's. Methodology is
    descriptive (what the template leans on), not a membership criterion, so it is not gated here: a
    user-stories bundle honestly declaring `agile-scrum-xp` is still a delivery-docs member (ADR 0020).

    A family is coherent on ONE taxonomy axis (ADR 0015): lifecycle families on `phase`, standing
    families on `classification`. The registry entry names which, and this check gates that one. The
    two are mutually exclusive on a meta, and check J's schema `oneOf` is what proves a bundle declares
    exactly one; check K's job is narrower, proving it declared the one its family requires. A member
    that brings the wrong axis entirely (a `phase: measure` bundle in a classification family) is
    reported as such rather than as a bare "phase is None", because the fix differs: one is a typo,
    the other means the bundle or the family is misfiled.
    This enforces the mechanical half of the contract, its Section 2 allowed-values table. The
    structural obligations (Section 3) are checks A through E; the shared-example and shareable-boundary
    rules (Sections 4 and 5) are review obligations, not mechanically checkable. See
    docs/internal/contracts/delivery-docs.md and
    docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md.

    Only families with a ratified contract are enforced. A bundle in a family that has none yet (a
    future family such as strategy-docs, before its contract is written) passes with a note, so adding a
    family does not silently fail the gate before its contract exists.
    """
    p = os.path.join(d, name + "_meta.yaml")
    text = read(p)
    fm = FAMILY_RE.search(text)
    family = fm.group(1).strip().strip("\"'") if fm else None
    if family is None:
        return True, "no family declared"
    contract = FAMILY_CONTRACTS.get(family)
    if contract is None:
        return True, "family " + family + " has no ratified contract yet; not enforced"

    def field(rx):
        m = rx.search(text)
        return m.group(1).strip().strip("\"'") if m else None

    problems = []
    cpath = os.path.normpath(os.path.join(SCRIPT_DIR, "..", contract["contract"]))
    if not os.path.isfile(cpath):
        problems.append("contract file missing at " + contract["contract"])

    # Gate the axis this family is coherent on: phase for a lifecycle family, classification for a
    # standing one. A member declares one or the other (ADR 0015); check J proves it declares exactly
    # one, check K proves it is the one this family requires, with the value the contract names.
    declared_axes = [a for a in AXIS_KEYS if a in contract]
    axis = declared_axes[0] if len(declared_axes) == 1 else None
    if axis is None:
        problems.append(
            "registry entry for " + family + " declares "
            + ("both phase and classification" if declared_axes else "neither phase nor classification")
            + "; a family contract gates exactly one axis (ADR 0015)"
        )
    else:
        other = "classification" if axis == "phase" else "phase"
        value = field(AXIS_RE[axis])
        if value is None:
            found = field(AXIS_RE[other])
            problems.append(
                "declares no " + axis
                + (" (found " + other + ": " + found + ")" if found else "")
                + "; " + family + " is a " + axis + "-axis family and requires "
                + axis + ": " + contract[axis]
            )
        elif value != contract[axis]:
            problems.append(
                axis + " is " + repr(value) + ", " + family + " requires " + contract[axis]
            )
    status = field(STATUS_RE)
    if status not in contract["status"]:
        problems.append("status is " + repr(status) + ", " + family + " allows " + "/".join(contract["status"]))

    sizes, err = parse_sizes(name, d)
    if err:
        problems.append(err)
    elif sizes not in contract["size_shapes"]:
        allowed = " or ".join("[" + ", ".join(s) + "]" for s in contract["size_shapes"])
        problems.append("sizes_available is [" + ", ".join(sizes) + "], " + family + " allows " + allowed)

    if problems:
        return False, "out of " + family + " contract: " + "; ".join(problems)
    return True, "conforms to " + family + " contract (" + axis + ", status, sizes)"


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
    ("J schema", check_meta_schema),
    ("K family", check_family),
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
