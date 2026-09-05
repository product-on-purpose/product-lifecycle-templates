#!/usr/bin/env python3
"""
validate-fill.py - check a filled document against the template it came from.

WHAT IT ANSWERS.
Four questions, in the order they matter: is every section the template declares still present, is
anything still unfilled, is the guidance gone, and does the document say where it came from. It is
LP-1's step 7, and it is the first check in this repository that can be run against a document that
does not live in this repository.

WHY IT NEEDED sections.json FIRST.
The completeness question is "does this document still have the sections its template declared", and
until [ADR 0044](../docs/internal/decisions/0044-the-section-schema-is-a-second-generated-artifact.md)
nothing knew what a template declared without re-parsing its guidance comments. That is why the LP-1
spec wrote "section-schema completeness WHEN AVAILABLE": it was not. It is now, so the check is not
optional here.

WHAT IT DELIBERATELY DOES NOT DO.
It does not grade. Whether a section says anything worth reading is LP-2's job and a human's; this
tool only reports whether the section is there. A document can pass every check here and be empty
prose under every heading, and the output says so rather than implying otherwise.

HOW IT FINDS THE TEMPLATE.
From the document's own frontmatter: `source_template` names the bundle, `size` names the variant, and
`format` names the format when the bundle ships more than one (ADR 0028). All three are stamped into
every variant by the templates themselves, so a document filled from this library carries them without
anyone adding anything. A document that carries none of them is not from this library and is reported
as such rather than guessed at.

Usage:
    python tools/validate-fill.py FILE
    python tools/validate-fill.py FILE --json

Exit 0 if the document validates; 1 on a usage or lookup error; 2 if any check fails.
"""
import argparse
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
SECTIONS_PATH = os.path.join(ROOT, "sections.json")

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
DIM = "\033[2m"
OFF = "\033[0m"

FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---[ \t]*\r?\n", re.S)
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.*\S)[ \t]*$", re.M)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
PLACEHOLDER_RE = re.compile(r"\{\{([a-z0-9_]+)\}\}")


def slug(title):
    """Must match tools/gen-sections.py exactly, or every lookup misses."""
    t = PLACEHOLDER_RE.sub(r"\1", title).lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "section"


def frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    body = text[m.end():]
    fields = {}
    for line in m.group(1).split("\n"):
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km:
            fields[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return fields, body


def load_schema():
    if not os.path.isfile(SECTIONS_PATH):
        return None
    with open(SECTIONS_PATH, encoding="utf-8") as f:
        return json.load(f)


def find_variant(schema, bundle, fmt, size):
    """The declared section list for one (bundle, format, size), or an error string."""
    entry = next((b for b in schema["bundles"] if b["bundle"] == bundle), None)
    if entry is None:
        return None, ("no bundle named " + repr(bundle) + " in sections.json; known bundles are "
                      + ", ".join(sorted(b["bundle"] for b in schema["bundles"])[:6]) + ", ...")
    fmt = fmt or entry.get("default_format") or "default"
    formats = entry["formats"]
    if fmt not in formats:
        return None, ("bundle " + bundle + " has no format " + repr(fmt) + "; it ships "
                      + ", ".join(sorted(formats)))
    block = formats[fmt]
    if size and size not in block["sizes"]:
        return None, ("bundle " + bundle + " format " + fmt + " has no size " + repr(size)
                      + "; it ships " + ", ".join(block["sizes"]))
    declared = [s for s in block["sections"] if not size or size in s["in_sizes"]]
    return declared, None


def validate(path):
    """(ok, list of (level, message)) where level is 'pass', 'fail' or 'note'."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    out = []
    fields, body = frontmatter(text)

    if fields is None:
        return False, [("fail", "no YAML frontmatter, so there is nothing to say where this came from")]

    bundle = fields.get("source_template")
    if not bundle:
        return False, [("fail", "frontmatter carries no source_template, so this is not a document "
                                "filled from this library (or the field was removed)")]

    schema = load_schema()
    if schema is None:
        return False, [("fail", "sections.json is missing; run python tools/gen-sections.py")]

    declared, err = find_variant(schema, bundle, fields.get("format"), fields.get("size"))
    if err:
        return False, [("fail", err)]

    # 1. Completeness. Headings present in the document, by the same slug the schema uses.
    #
    # Only headings at a level the schema actually declares are candidates for "extra". Most
    # variants' H1 is the document title and carries no guidance, so it is not a section; counting
    # it would put a spurious "extra section" note on every document ever validated. Where a bundle
    # DOES attach guidance to its H1 (adr and release-notes do), level 1 is in the declared set and
    # an unexpected H1 is flagged normally.
    declared_levels = {s["level"] for s in declared}
    seen = [(len(m.group(1)), slug(m.group(2))) for m in HEADING_RE.finditer(COMMENT_RE.sub("", body))]
    present = {sid for level, sid in seen}
    missing = [s for s in declared if s["id"] not in present]
    extra = {sid for level, sid in seen if level in declared_levels} - {s["id"] for s in declared}
    if missing:
        out.append(("fail", "missing " + str(len(missing)) + " of " + str(len(declared))
                    + " declared section(s): " + ", ".join(s["title"] for s in missing[:6])
                    + ("..." if len(missing) > 6 else "")))
    else:
        out.append(("pass", "all " + str(len(declared)) + " declared section(s) present"))
    if extra:
        # Extra sections are legal (the LP-1 spec allows a filled document to grow), so this is a
        # note rather than a failure. It is reported because a heading the template never declared
        # is also what a typo looks like.
        note = "extra section(s) not in the template: " + ", ".join(sorted(extra)[:6])
        if fields.get("extends_template") in ("true", "True", "yes"):
            note += " (declared via extends_template)"
        out.append(("note", note))

    # 2. Placeholders, counted after comments are stripped, for the reason strip-template states.
    left = sorted(set(PLACEHOLDER_RE.findall(COMMENT_RE.sub("", text))))
    if left:
        out.append(("fail", str(len(left)) + " unfilled placeholder(s): " + ", ".join(left[:8])
                    + ("..." if len(left) > 8 else "")))
    else:
        out.append(("pass", "no unfilled placeholders"))

    # 3. Guidance comments.
    comments = len(COMMENT_RE.findall(text))
    if comments:
        out.append(("fail", str(comments) + " guidance comment(s) remain; run "
                    "python tools/strip-template.py before shipping"))
    else:
        out.append(("pass", "no guidance comments remain"))

    # 4. Provenance. source_template got us here, so it exists; the fill record is what may not.
    have = [k for k in ("source_template", "source_template_version", "filled_by", "fill_method",
                        "fill_date") if fields.get(k)]
    lack = [k for k in ("filled_by", "fill_method", "fill_date") if not fields.get(k)]
    if lack:
        out.append(("fail", "provenance incomplete, missing " + ", ".join(lack)
                    + "; strip-template.py --filled-by stamps all three"))
    else:
        out.append(("pass", "provenance complete (" + ", ".join(have) + ")"))

    ok = not any(level == "fail" for level, _ in out)
    return ok, out


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="validate-fill.py",
        description="Check a filled document against the template it declares it came from.")
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)

    if not os.path.isfile(args.file):
        print(RED + "ERROR" + OFF + "  no such file: " + args.file)
        return 1

    ok, findings = validate(args.file)

    if args.json:
        print(json.dumps({"file": os.path.basename(args.file), "ok": ok,
                          "findings": [{"level": l, "message": m} for l, m in findings]},
                         indent=2))
        return 0 if ok else 2

    print(os.path.basename(args.file))
    for level, message in findings:
        mark = {"pass": GREEN + "PASS" + OFF, "fail": RED + "FAIL" + OFF,
                "note": YELLOW + "NOTE" + OFF}[level]
        print("  " + mark + "  " + message)
    print()
    if ok:
        print(GREEN + "OK" + OFF + "  the document is structurally complete.")
        print(DIM + "      not verified: whether any section says anything worth reading. This checks"
              "\n      that the shape survived the fill, never that the content is good. That is the"
              "\n      guide's rubric and a reader, not a script." + OFF)
    else:
        print(RED + "FAILED" + OFF + "  the document is not ready to ship.")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
