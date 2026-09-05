#!/usr/bin/env python3
"""
test-gen-sections.py - the adversarial test for the AG-1 section-schema parser.

WHAT THIS COVERS, AND WHAT IT DOES NOT.
This tests `gen-sections.py`'s parsing of the Approach A guidance grammar. It does not test the
`--check` drift machinery, which is the same shape as `gen-manifest.py`'s and is exercised in CI
by running `--check` against the committed file.

WHY THIS ONE MATTERS MORE THAN MOST.
Every other generator in this repository produces data whose wrongness is visible: a bad count, a
missing bundle, a stale marker. This one produces a section list, and a section that goes MISSING
from that list makes a downstream completeness check pass for the wrong reason. LP-1 would report
a filled document complete because the section it failed to check was never in the schema. So the
dangerous failure here is silent and structural, and a test that only asserts the happy path would
not see it.

The negative cases below are therefore the point. Each is drawn from a real shape measured in the
tree on 2026-09-05, not from an imagined one:

  - The `okrs` shape: a ROW HINT value containing a pipe-table row whose first cell is literally
    `WEAK` plus two spaces. Under a "label followed by two spaces" rule this parses as a second
    WEAK field. Three real lines in the tree do this, and they are why the parser anchors labels to
    indent exactly 5.
  - The `product-roadmap` go-full shape: a ROW HINT whose value spans lines beginning `GOOD row:`
    and `WEAK row:`.
  - The preamble: 58 of them, one per variant, and none is a section.
  - `release-notes` and `adr`: guidance attached to an H1. `adr` and `sdd`: guidance attached to
    H3s. Assuming H2 loses 11 real sections.

Pure standard library, no framework. Runs in CI alongside the gate.
Usage: python tools/test-gen-sections.py
"""
import importlib.util
import json
import os
import shutil
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
GEN = os.path.join(SCRIPT_DIR, "gen-sections.py")

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

spec = importlib.util.spec_from_file_location("gen_sections", GEN)
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

results = []


def check(label, passed, detail=""):
    results.append(passed)
    mark = GREEN + "PASS" + OFF if passed else RED + "FAIL" + OFF
    print("  " + mark + "  " + label)
    if not passed and detail:
        print("        got: " + str(detail)[:300])


PREAMBLE = (
    "<!--\n"
    "HOW TO FILL THIS IN\n"
    "1. Read the comment under each heading: WHAT it wants, WHY it matters, questions to ASK,\n"
    "   a GOOD and a WEAK example, and the TRAP to avoid.\n"
    "-->\n"
)


def variant(body, frontmatter=True):
    """A throwaway variant file holding exactly the body under test."""
    d = tempfile.mkdtemp()
    p = os.path.join(d, "fixture_template-lean.md")
    head = "---\nsource_template: fixture\n---\n" if frontmatter else ""
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(head + PREAMBLE + body)
    return d, p


def parse(body, frontmatter=True):
    d, p = variant(body, frontmatter)
    try:
        return gen.parse_variant(p)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def parse_err(body):
    try:
        parse(body)
        return None
    except gen.ParseError as e:
        return str(e)


GUIDANCE = (
    "<!-- WHAT  A thing.\n"
    "     WHY   Because. Deep dive: fixture_companion.md section 3.\n"
    "     ASK   Is it? Why?\n"
    "     GOOD  A good one.\n"
    "     WEAK  A weak one. (why it is weak)\n"
    "     TRAP  The trap. -->\n"
)


def main():
    print("gen-sections: the AG-1 guidance parser\n")

    print(DIM + "1. Regression: the real tree parses, and every guidance block is accounted for" + OFF)
    import yaml
    schema = gen.build(yaml)
    instances = sum(len(s["in_sizes"]) for b in schema["bundles"]
                    for f in b["formats"].values() for s in f["sections"])
    check("all 27 bundles parse", schema["count"] == 27, schema["count"])
    # 353 guidance comments measured directly on disk 2026-09-05: 4 at H1, 342 at H2, 7 at H3.
    # If a template gains or loses a section this number moves, and it SHOULD: the assertion is
    # that the schema accounts for every block the files carry, checked below against a fresh scan.
    on_disk = 0
    for b in gen.find_bundles(gen.TEMPLATES_DIR):
        d = os.path.join(gen.TEMPLATES_DIR, b)
        for fn in sorted(os.listdir(d)):
            if "_template-" not in fn:
                continue
            text = open(os.path.join(d, fn), encoding="utf-8").read()
            import re
            for cm in re.finditer(r"<!--.*?-->", text, re.S):
                if gen.GUIDANCE_OPEN_RE.match(cm.group(0)):
                    on_disk += 1
    check("every guidance block on disk appears in the schema",
          instances == on_disk, "schema=" + str(instances) + " disk=" + str(on_disk))
    check("no id collides within a format", all(
        len({s["id"] for s in f["sections"]}) == len(f["sections"])
        for b in schema["bundles"] for f in b["formats"].values()))

    print("\n" + DIM + "2. The grammar's legal shapes" + OFF)
    secs = parse("## Alpha\n\n" + GUIDANCE + "\n{{alpha}}\n")
    check("a section is found", len(secs) == 1, secs)
    check("  fields come out in order",
          secs[0]["guidance_fields"] == ["WHAT", "WHY", "ASK", "GOOD", "WEAK", "TRAP"], secs[0])
    check("  placeholder is captured", secs[0]["placeholders"] == ["alpha"], secs[0])
    check("  id is slugged from the title", secs[0]["id"] == "alpha", secs[0])

    secs = parse("# {{product}} {{version}}\n\n" + GUIDANCE + "\ntext\n")
    check("guidance on an H1 is a section (release-notes, adr)", len(secs) == 1, secs)
    check("  level records H1", secs and secs[0]["level"] == 1, secs)
    check("  a placeholder title still slugs", secs and secs[0]["id"] == "product-version", secs)

    secs = parse("### Consequences\n\n" + GUIDANCE + "\ntext\n")
    check("guidance on an H3 is a section (adr, sdd)", len(secs) == 1 and secs[0]["level"] == 3, secs)

    print("\n" + DIM + "3. What must NOT become a section" + OFF)
    secs = parse("## Alpha\n\n" + GUIDANCE + "\n### Sub\n\nplain prose, no comment\n")
    check("a heading with no guidance comment is skipped", len(secs) == 1, secs)
    secs = parse("## Alpha\n\n" + GUIDANCE)
    check("the preamble is never a section", len(secs) == 1, [s["title"] for s in secs])
    secs = parse("## Alpha\n\n" + GUIDANCE
                 + "\n## Beta\n\n<!-- a plain note, not guidance -->\n\ntext\n")
    check("a non-guidance comment does not make a section",
          [s["title"] for s in secs] == ["Alpha"], [s["title"] for s in secs])

    print("\n" + DIM + "4. The silent-wrong-answer cases, drawn from the real tree" + OFF)
    # okrs: a ROW HINT value whose continuation is a table row starting `WEAK  |`
    okrs = (
        "<!-- WHAT  A thing.\n"
        "     WHY   Because.\n"
        "     ASK   Is it?\n"
        "     PRIORITY  P1 highest.\n"
        "     ROW HINT  GOOD  | 1 | Ship the model | Done |\n"
        "               WEAK  | 1 | Ship the new matching model | n/a | Done | Eng |\n"
        "     GOOD  A good one.\n"
        "     WEAK  A weak one.\n"
        "     TRAP  The trap. -->\n"
    )
    secs = parse("## Alpha\n\n" + okrs + "\n| a | b |\n|---|---|\n")
    got = secs[0]["guidance_fields"] if secs else []
    check("a `WEAK  |` table row inside ROW HINT is NOT a second field",
          got.count("WEAK") == 1, got)
    check("  and the real field order survives",
          got == ["WHAT", "WHY", "ASK", "PRIORITY", "ROW HINT", "GOOD", "WEAK", "TRAP"], got)

    # product-roadmap go-full: ROW HINT value spanning `GOOD row:` / `WEAK row:` lines
    roadmap = (
        "<!-- WHAT  A thing.\n"
        "     WHY   Because.\n"
        "     ASK   Is it?\n"
        "     ROW HINT  GOOD row: \"Q2 2026 | Signal | outcome |\n"
        "               metric\"\n"
        "               WEAK row: \"Q2 2026 | v2.4 | Improve dispatch |\n"
        "               engagement\" (restates the release name)\n"
        "     GOOD  A good one.\n"
        "     WEAK  A weak one.\n"
        "     TRAP  The trap. -->\n"
    )
    got = parse("## Alpha\n\n" + roadmap + "\ntext\n")[0]["guidance_fields"]
    check("`GOOD row:` / `WEAK row:` continuations are not fields",
          got.count("GOOD") == 1 and got.count("WEAK") == 1, got)

    print("\n" + DIM + "5. Malformed guidance must FAIL, not be skipped" + OFF)
    e = parse_err("## Alpha\n\n<!-- WHAT  A thing.\n     WOMBAT  Not a field.\n     WHY   x.\n"
                  "     ASK  x.\n     GOOD  x.\n     WEAK  x.\n     TRAP  x. -->\n")
    check("an unknown label at label position raises", e is not None, e)
    check("  the message names the bad label", e and "WOMBAT" in e, e)
    check("  the message names the defined set", e and "ROW HINT" in e, e)

    e = parse_err("## Alpha\n\n<!-- WHY   No WHAT here.\n     ASK   x. -->\n")
    check("a guidance comment with no WHAT raises", e is not None, e)
    check("  the message says so", e and "no WHAT" in e, e)

    e = parse_err("## Alpha\n\n<!-- WHAT  One.\n     WHY   x.\n     WHAT  Two.\n     ASK  x. -->\n")
    check("a repeated field raises", e is not None, e)
    check("  the message names the repeat", e and "WHAT" in e and "repeats" in e, e)

    d, p = variant("no headings at all, just prose\n")
    try:
        gen.parse_variant(p)
        check("a variant with no parseable section raises", False, "no exception")
    except gen.ParseError as err:
        check("a variant with no parseable section raises", True)
        check("  the message names the file", "fixture_template-lean.md" in str(err), str(err))
    finally:
        shutil.rmtree(d, ignore_errors=True)

    print("\n" + DIM + "6. has_table and has_row_hint are independent, because they disagree" + OFF)
    s = parse("## Alpha\n\n" + GUIDANCE + "\n| a | b |\n|---|---|\n| 1 | 2 |\n")[0]
    check("a real pipe table sets has_table", s["has_table"] and not s["has_row_hint"], s)
    rh = GUIDANCE.replace("     TRAP", "     ROW HINT  what a row holds.\n     TRAP")
    s = parse("## Alpha\n\n" + rh + "\n{{supplied_by_author}}\n")[0]
    check("ROW HINT over a bare placeholder sets has_row_hint but NOT has_table (kpi-dashboard)",
          s["has_row_hint"] and not s["has_table"], s)
    s = parse("## Alpha\n\n" + GUIDANCE + "\n| a |\n|---|\n")[0]
    check("a table with no ROW HINT sets has_table only (prd Open questions)",
          s["has_table"] and not s["has_row_hint"], s)

    print("\n" + DIM + "7. Guidance prose must not leak into the shipped structure" + OFF)
    leaky = GUIDANCE.replace("GOOD  A good one.",
                             "GOOD  A row like | x | y | with {{not_a_real_placeholder}}")
    s = parse("## Alpha\n\n" + leaky + "\n{{real}}\n")[0]
    check("a placeholder named only in guidance is not counted",
          s["placeholders"] == ["real"], s["placeholders"])
    s = parse("## Alpha\n\n<!-- WHAT  x.\n     WHY   x.\n     ASK   x.\n"
              "     GOOD  | a | b |\n           |---|---|\n"
              "     WEAK  x.\n     TRAP  x. -->\n\nno table here\n")[0]
    check("an example table drawn inside guidance does not set has_table",
          not s["has_table"], s)

    print("\n" + DIM + "8. Formats are grouped, never merged across" + OFF)
    b = [x for x in schema["bundles"] if x["bundle"] == "product-roadmap"][0]
    check("product-roadmap keeps three formats", len(b["formats"]) == 3, sorted(b["formats"]))
    titles = {f: [s["title"] for s in e["sections"]] for f, e in b["formats"].items()}
    shared = [t for t in titles.get("go", []) if t in titles.get("themes", [])]
    check("the same title in two formats stays two sections",
          "What Is Not On Here" in shared, shared)
    b = [x for x in schema["bundles"] if x["bundle"] == "sprint-retrospective-notes"][0]
    check("a single-variant bundle is expressible",
          list(b["formats"].values())[0]["sizes"] == ["lean"], b["formats"])

    failed = results.count(False)
    print()
    if failed:
        print(RED + "FAIL" + OFF + "  " + str(failed) + " of " + str(len(results))
              + " assertion(s) failed.")
        return 1
    print(GREEN + "OK" + OFF + "  " + str(len(results))
          + " assertions, the guidance parser holds on the real tree and on every adversarial shape.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
