#!/usr/bin/env python3
"""
gen-sections.py - generate the AG-1 section schema: the machine shape of every template.

WHAT THIS PRODUCES.
`sections.json` at the repository root: for every bundle, for every format, the ordered list of
sections with their heading level, which sizes carry them, which guidance fields their comment
declares, whether the shipped body contains a table, and which placeholders they hold, plus the
frontmatter fill sites that precede them. It is DERIVED from the variant files themselves and
never hand-written, so it cannot drift from the templates it describes: edit a template and
`--check` reports the schema stale until regenerated.

WHY FRONTMATTER IS IN HERE AND NOT ONLY SECTIONS.
A template's shape is not only its headings. LP-1 collects the frontmatter before it interviews
anything, so a completeness check reading `sections` alone would pass a document whose `author`
and `status` are still `{{placeholder}}`. 181 such sites exist, and they are recorded per size
because they genuinely differ: 13 bundles carry more frontmatter fields in `full` than in `lean`.

WHAT THIS DELIBERATELY DOES NOT RECORD.
Placeholder OCCURRENCES. A section lists each placeholder NAME once, which is what a completeness
check wants ("is anything still unfilled"). It is not what a substituting fill tool wants: 94
names recur within a single file body, and `prd` reuses `{{owner}}` and `{{date}}` across
semantically unrelated sites, so a tool that asked one question per NAME would put the document
owner's name into an open question's owner column. A fill tool must key sites by occurrence, and
must read the file to do it. This schema describes shape, not substitution.

WHY IT IS NOT A NINTH BUNDLE FILE.
The bundle contract is eight files (methodology B1) and every gate check counts on that. This is
generated data about those files, so it lives at the root beside `manifest.json` rather than
inside the bundles. Consumers: LP-1's completeness check, LP-2's structure layer, and an MCP
`validate_fill`.

WHY IT IS NOT INSIDE manifest.json EITHER, WHICH THE AG-1 SKETCH ASKED FOR.
The sketch said "embedded into manifest.json per bundle". Measured, that costs 4.6x: the manifest
goes from about 10,850 approx-tokens to about 49,750. The manifest is the SELECTION surface, read
by an agent choosing a bundle, and the AG-2 MCP spec sitting beside AG-1 in the same document
requires default responses under 1,200 tokens. Loading 39,000 tokens of fill-time section detail
into the artifact used for selection contradicts that budget, so the schema ships beside the
manifest instead of inside it. Both are generated, both are root-level, and a consumer that wants
both reads both.

THE PARSER IS THE GRAMMAR CHECK.
Nothing else in the repository reads the Approach A guidance comments mechanically. Checks A
through K prove files exist, nest, cite and validate; none of them opens a comment and asks
whether it parses. So the generator failing on a malformed comment IS the grammar check, and it
fails loudly rather than skipping the section, because a section silently missing from the schema
is a completeness check that passes for the wrong reason.

THE GRAMMAR, AS MEASURED RATHER THAN AS DOCUMENTED.
Derived 2026-09-05 by measuring all 58 variant files, not by trusting methodology B1, and every
number below is reproducible from the tree:

- 353 guidance comments across 58 files, and every one of them opens `<!-- LABEL` followed by two
  spaces. The 58 "How to fill this in" preambles (one per file) do NOT, because they open with a
  newline. That difference is the whole preamble-exclusion rule; no heuristic about position or
  content is needed.
- A field label sits at INDENT EXACTLY 5, because `<!-- ` is five characters and every later label
  aligns under the first. Requiring only "a label followed by two spaces" is NOT enough: three
  lines in `okrs` (both variants) are table rows inside a ROW HINT value whose first cell is
  literally `WEAK` plus two spaces, and they parse as a second WEAK field under the loose rule.
  With the indent rule the six core fields come out at exactly 353 each; under the loose rule WEAK
  comes out at 356. That is the difference between a schema and a plausible schema.
- Continuation lines are anything else inside the block, at any indent. `product-roadmap`'s
  `go-full` variant has a ROW HINT whose value contains both `GOOD row:` and `WEAK row:` lines;
  they are content, not labels, and only the indent rule keeps them so.
- Sections are not only H2. `release-notes` and `adr` attach guidance to the H1 title, and `adr`
  and `sdd` attach it to H3s. 342 H2 + 7 H3 + 4 H1 = 353, which accounts for every comment with
  none orphaned, so the rule is "any heading immediately followed by a guidance comment" and
  `level` records which. Note the arithmetic is over guidance-carrying headings, not headings:
  nine H3s exist but two of them (`{{option_1}}`, `{{option_2}}` in adr) carry none, being example
  option headings inside another section. Counting headings instead gives 9 and 2 and does not
  reconcile; that error was made and caught by this reconciliation.

WHY has_table AND has_row_hint ARE BOTH RECORDED.
They disagree on 10 of 353 sections, so collapsing them into one boolean makes those ten silently
wrong. `has_table` is the structural fact that the shipped body contains a pipe table; ROW HINT is
a guidance field the author is given. `kpi-dashboard`'s Metric Definitions carries ROW HINT over a
bare `{{metric_definitions}}` placeholder, because the author supplies the table. `prd`'s Open
questions ships a real table but puts its row guidance in WHAT. Both are correct documents; one
boolean cannot describe both.

WHY FORMATS ARE GROUPED AND `in_lean`/`in_full` ARE NOT USED.
The original AG-1 sketch gave each section two booleans. The tree has outgrown that. Four bundles
ship three or four variants under the format axis (ADR 0028) and one ships a single variant, so
two booleans cannot address them. Worse, two section titles appear in more than one FORMAT with
genuinely different guidance text: `product-roadmap`'s "What Is Not On Here" in go, now-next-later
and themes, and `product-strategy`'s "What We Are Not Doing" in kernel and one-pager. Keying
sections by title alone would merge documents that only share a heading. Sections are therefore
grouped per format and carry `in_sizes`, which preserves ADR 0028's model exactly: nesting runs
within a format and never across one.

Usage:
    python tools/gen-sections.py            # write sections.json
    python tools/gen-sections.py --check    # exit 1 if sections.json is stale or a comment is malformed

Exit 0 if written / in sync; 1 if --check finds drift or any variant fails to parse.
"""
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
TEMPLATES_DIR = os.path.join(ROOT, "templates")
SECTIONS_PATH = os.path.join(ROOT, "sections.json")

GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"
OFF = "\033[0m"

# The documented field set (methodology B1). An ALLCAPS token at label position that is NOT on this
# list is a malformed comment and fails the run rather than being dropped, because a dropped field
# is a guidance obligation that quietly stopped being checked.
LABELS = ["WHAT", "WHY", "ASK", "GOOD", "WEAK", "TRAP", "PRIORITY", "ROW HINT"]
_LAB_ALT = "|".join(l.replace(" ", r"\s") for l in LABELS)

# A guidance comment opens `<!-- LABEL` + two spaces. A preamble opens `<!--` + newline, so this
# single expression separates the two with no positional heuristic.
GUIDANCE_OPEN_RE = re.compile(r"^<!--\s(" + _LAB_ALT + r")\s\s")
# A field label sits at indent exactly 5, aligning under the five characters of `<!-- `.
FIELD_RE = re.compile(r"^ {5}(" + _LAB_ALT + r")\s\s")
# Any ALLCAPS-looking token at label position, so an UNKNOWN label is caught rather than ignored.
SUSPECT_LABEL_RE = re.compile(r"^ {5}([A-Z][A-Z ]{1,14}?)\s\s\S")

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.*\S)[ \t]*$", re.M)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
PLACEHOLDER_RE = re.compile(r"\{\{([a-z0-9_]+)\}\}")
# A markdown pipe table needs a delimiter row; a lone pipe in prose is not a table.
TABLE_DELIM_RE = re.compile(r"^[ \t]*\|[\s:|-]+\|[ \t]*$", re.M)


class ParseError(Exception):
    """A template whose guidance does not parse. Carries the file and the offending line."""


def rel(path):
    """Repo-relative path for an error message, falling back to the absolute one.

    `os.path.relpath` raises on Windows when the two paths sit on different drives, which happens
    the moment anything parses a file outside the repository (the self-test's fixtures live under
    the system temp directory, typically on C: while the repo is on E:). An error message is not
    worth crashing over, so a cross-drive path is reported in full.
    """
    try:
        return os.path.relpath(path, ROOT)
    except ValueError:
        return path


def find_bundles(root):
    """Every directory under templates/ carrying <name>_meta.yaml, matching gen-manifest.py."""
    out = []
    for name in sorted(os.listdir(root)):
        d = os.path.join(root, name)
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, name + "_meta.yaml")):
            out.append(name)
    return out


def slug(title):
    """A stable id from a heading. Placeholder headings (`{{option_1}}`, real in adr) keep their
    inner name, so the id stays readable rather than becoming empty."""
    t = PLACEHOLDER_RE.sub(r"\1", title).lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "section"


def split_frontmatter(text):
    """(frontmatter_text, body, lines_consumed). A variant opening without frontmatter yields ''."""
    if not text.startswith("---"):
        return "", text, 0
    m = re.match(r"^---\r?\n.*?\r?\n---[ \t]*\r?\n", text, re.S)
    if not m:
        return "", text, 0
    return m.group(0), text[m.end():], text[:m.end()].count("\n")


def frontmatter_placeholders(path):
    """The fill sites in a variant's instance frontmatter.

    Sections are not the whole shape of a template. LP-1's flow collects the frontmatter before it
    interviews anything, so a completeness check reading only `sections` would pass a document
    whose `author` and `status` are still `{{placeholder}}`. These are recorded per size because
    they genuinely differ: 13 bundles carry more frontmatter fields in `full` than in `lean`.
    """
    with open(path, encoding="utf-8") as f:
        front, _, _ = split_frontmatter(f.read())
    return sorted(set(PLACEHOLDER_RE.findall(front)))


def parse_guidance(block, path, line_no):
    """The ordered field labels declared by one guidance comment.

    Raises ParseError on an unknown label at label position, on a duplicated field, or on a
    comment carrying no WHAT. Each of those is a real defect in the template rather than a
    tolerable variation, and none of them is caught anywhere else in the gate.
    """
    lines = block.split("\n")
    m = GUIDANCE_OPEN_RE.match(lines[0])
    fields = [m.group(1)]
    for offset, line in enumerate(lines[1:], start=1):
        fm = FIELD_RE.match(line)
        if fm:
            fields.append(re.sub(r"\s+", " ", fm.group(1)))
            continue
        # Not a known label. If it still LOOKS like one at label position, the comment is
        # malformed: either a typo'd label or a field the methodology never defined.
        sm = SUSPECT_LABEL_RE.match(line)
        if sm:
            raise ParseError(
                path + ":" + str(line_no + offset) + " unknown guidance label "
                + repr(sm.group(1).strip()) + " at label position; the defined set is "
                + ", ".join(LABELS)
            )
    if "WHAT" not in fields:
        raise ParseError(path + ":" + str(line_no) + " guidance comment declares no WHAT field")
    dupes = sorted({f for f in fields if fields.count(f) > 1})
    if dupes:
        raise ParseError(
            path + ":" + str(line_no) + " guidance comment repeats field(s) "
            + ", ".join(dupes) + "; each field may appear once"
        )
    return fields


def parse_variant(path):
    """Every section in one variant file, in document order.

    A section is a heading immediately followed by a guidance comment. A heading followed by
    anything else is not a section and is skipped silently: that is the H1 in most variants, which
    is the document title rather than a thing to fill in.
    """
    with open(path, encoding="utf-8") as f:
        text = f.read()
    _, body, skipped = split_frontmatter(text)
    heads = list(HEADING_RE.finditer(body))
    sections = []
    for i, h in enumerate(heads):
        start = h.end()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        after = body[start:end]
        cm = re.match(r"[ \t\r\n]*(<!--.*?-->)", after, re.S)
        if not cm or not GUIDANCE_OPEN_RE.match(cm.group(1)):
            continue
        line_no = skipped + body[:start].count("\n") + 1
        fields = parse_guidance(cm.group(1), rel(path), line_no)
        # The body BELOW the guidance comment: what the author actually fills in. Placeholders and
        # tables are read from here only, so guidance prose can mention a placeholder or draw an
        # example row without either being counted as shipped structure.
        rest = COMMENT_RE.sub("", after[cm.end():])
        sections.append({
            "id": slug(h.group(2)),
            "title": h.group(2),
            "level": len(h.group(1)),
            "guidance_fields": fields,
            "has_table": bool(TABLE_DELIM_RE.search(rest)),
            "has_row_hint": "ROW HINT" in fields,
            "placeholders": sorted(set(PLACEHOLDER_RE.findall(rest))),
        })
    if not sections:
        raise ParseError(
            rel(path) + " contains no parseable section; every variant carries "
            "guidance under its headings"
        )
    return sections


def variant_files(bundle, meta):
    """[(format_id, size, filename)] for a bundle, matching gen-manifest.py's naming exactly: the
    default format keeps plain filenames, an additional format prefixes its id (ADR 0028)."""
    out = []
    default_fmt = meta.get("default_format") or "default"
    for size in meta.get("sizes_available", []):
        out.append((default_fmt, size, bundle + "_template-" + size + ".md"))
    for fmt in meta.get("additional_formats") or []:
        for size in fmt.get("sizes", []):
            out.append((fmt["id"], size, bundle + "_template-" + fmt["id"] + "-" + size + ".md"))
    return out


def build_bundle(bundle, meta, bundle_dir):
    """One bundle's schema: formats, each with its sizes and its merged ordered section list.

    Sections are merged ACROSS SIZES within a format and never across formats. Within a format the
    variants nest (gate check C enforces it), so a section present in lean and full is one entry
    carrying both sizes. Across formats they do not nest, and two bundles ship the same heading in
    two formats with different guidance, so merging there would fabricate a section that exists in
    neither document.
    """
    formats = {}
    for fmt, size, fname in variant_files(bundle, meta):
        path = os.path.join(bundle_dir, fname)
        if not os.path.isfile(path):
            # The meta declares the size contract (ADR 0010) and gate check A already fails a
            # declared-but-missing variant. Not this tool's job to report it twice.
            continue
        entry = formats.setdefault(
            fmt, {"sizes": [], "frontmatter": [], "sections": [], "_index": {}, "_front": {}})
        if size not in entry["sizes"]:
            entry["sizes"].append(size)
        for name in frontmatter_placeholders(path):
            entry["_front"].setdefault(name, []).append(size)
        for sec in parse_variant(path):
            key = (sec["id"], sec["level"])
            known = entry["_index"].get(key)
            if known is None:
                sec["in_sizes"] = [size]
                entry["_index"][key] = sec
                entry["sections"].append(sec)
            else:
                if size not in known["in_sizes"]:
                    known["in_sizes"].append(size)
                # A section that ships a table in ANY size ships one: full commonly adds the table
                # that lean leaves as a placeholder, and a consumer asking "can this hold rows"
                # wants yes.
                known["has_table"] = known["has_table"] or sec["has_table"]
                known["has_row_hint"] = known["has_row_hint"] or sec["has_row_hint"]
                known["placeholders"] = sorted(set(known["placeholders"]) | set(sec["placeholders"]))
                for f in sec["guidance_fields"]:
                    if f not in known["guidance_fields"]:
                        known["guidance_fields"].append(f)
    for entry in formats.values():
        entry["frontmatter"] = [{"name": n, "in_sizes": s}
                                for n, s in sorted(entry["_front"].items())]
        del entry["_index"]
        del entry["_front"]
    return {
        "bundle": bundle,
        "template_version": meta.get("template_version"),
        "default_format": meta.get("default_format") or "default",
        "formats": formats,
    }


def build(yaml):
    bundles = []
    for name in find_bundles(TEMPLATES_DIR):
        d = os.path.join(TEMPLATES_DIR, name)
        with open(os.path.join(d, name + "_meta.yaml"), encoding="utf-8") as f:
            meta = yaml.safe_load(f.read())
        bundles.append(build_bundle(name, meta, d))
    total = sum(len(f["sections"]) for b in bundles for f in b["formats"].values())
    front = sum(len(f["frontmatter"]) for b in bundles for f in b["formats"].values())
    return {
        "_generated": "by tools/gen-sections.py from templates/*/*_template-*.md; do not edit by hand",
        "count": len(bundles),
        "section_count": total,
        "frontmatter_count": front,
        "bundles": bundles,
    }


def serialize(schema):
    """Canonical text form, matching gen-manifest.py so a --check diff fires on content only."""
    return json.dumps(schema, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main():
    try:
        import yaml
    except ImportError:
        print("gen-sections requires PyYAML (pip install pyyaml) to read the metas.")
        return 1

    check_only = "--check" in sys.argv[1:]
    try:
        schema = build(yaml)
    except ParseError as e:
        print(RED + "MALFORMED" + OFF + "  " + str(e))
        print(DIM + "      The guidance grammar is methodology.md section B1. This generator is the"
              "\n      only thing that reads it mechanically, so a comment it cannot parse is a"
              "\n      defect no other check would report." + OFF)
        return 1
    fresh = serialize(schema)

    counted = (str(schema["count"]) + " bundles, " + str(schema["section_count"])
               + " sections, " + str(schema["frontmatter_count"]) + " frontmatter fill sites")
    if check_only:
        if not os.path.isfile(SECTIONS_PATH):
            print(RED + "DRIFT" + OFF + "  sections.json is missing; run `python tools/gen-sections.py`")
            return 1
        if open(SECTIONS_PATH, encoding="utf-8").read() != fresh:
            print(RED + "DRIFT" + OFF + "  sections.json is stale (differs from freshly generated "
                  "output); run `python tools/gen-sections.py` and commit the result")
            return 1
        print(GREEN + "OK" + OFF + "  sections.json is fresh: " + counted + ", all guidance parsed.")
        return 0

    with open(SECTIONS_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(fresh)
    print(GREEN + "OK" + OFF + "  wrote sections.json: " + counted + ".")
    return 0


if __name__ == "__main__":
    sys.exit(main())
