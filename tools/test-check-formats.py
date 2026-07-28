#!/usr/bin/env python3
"""
test-check-formats.py - the adversarial test for the format axis (ADR 0028).

WHAT THIS COVERS, AND WHAT IT DOES NOT.
This tests the format-axis logic in check A (file derivation and stray detection), check C
(per-format nesting), and the parser they share. It does not test checks B, D through J, or K;
check K has its own test. Do not read a green run here as "the gate is tested"; read it as
"the format axis is tested."

WHY IT EARNED ONE.
Same argument as test-check-k.py. Most of this logic has no live subject: at the time of writing
exactly one bundle ships a second format, and none ships two, none ships a format whose sizes
differ in vocabulary, and by construction none ships a stray file. A check that has never been
observed failing is an assumption, not a check. The negative cases are the point.

THE THREE THAT MATTER MOST, because each is a bug that would otherwise ship silently:
  * Section 4: two formats with unrelated outlines must PASS. If nesting were still asserted
    across formats, the axis would be decorative.
  * Section 5: a `_template-*.md` file with an unrecognised token must FAIL. Before ADR 0028 it
    was invisible to the stray check AND to bundle_files(), so no scan ever read it.
  * Section 7: a size word inside a guidance sentence must not invent a variant. The parser
    scopes its search to the sizes region precisely to avoid this.

Pure standard library, no framework, no dependencies. Runs in CI alongside the gate.
Usage: python tools/test-check-formats.py
"""
import importlib.util
import os
import shutil
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
GATE = os.path.join(SCRIPT_DIR, "check-bundles.py")

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

spec = importlib.util.spec_from_file_location("check_bundles", GATE)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

NAME = "widget"
results = []
tempdirs = []


def check(label, passed, detail=""):
    results.append(passed)
    mark = GREEN + "PASS" + OFF if passed else RED + "FAIL" + OFF
    print("  " + mark + "  " + label)
    if not passed and detail:
        print("        got: " + detail)


def fixture(meta_extra="", sizes="[lean, full]", templates=None):
    """A throwaway bundle dir: a meta, the six core role files, and named template files.

    Unlike check K's fixtures this must touch disk, because check A and check C read the files
    themselves rather than only the meta.
    """
    d = tempfile.mkdtemp()
    tempdirs.append(d)
    meta = (
        "id: " + NAME + "\n"
        "doc_type: " + NAME + "\n"
        "title: Widget\n"
        "family: test-docs\n"
        "phase: develop\n"
        "status: beta\n"
        "sizes_available: " + sizes + "\n"
        "default_size: lean\n" + meta_extra
    )
    with open(os.path.join(d, NAME + "_meta.yaml"), "w", encoding="utf-8") as f:
        f.write(meta)
    for role in gate.CORE_ROLES:
        if role == "meta.yaml":
            continue
        with open(os.path.join(d, NAME + "_" + role), "w", encoding="utf-8") as f:
            f.write("# " + role + "\n")
    for suffix, heads in (templates or {}).items():
        with open(os.path.join(d, NAME + "_" + suffix), "w", encoding="utf-8") as f:
            f.write("\n\n".join("## " + h for h in heads) + "\n")
    return d


# The two files a plain lean/full bundle ships, with a legal nesting relationship.
PLAIN = {
    "template-lean.md": ["Alpha", "Beta"],
    "template-full.md": ["Alpha", "Beta", "Gamma"],
}


def main():
    print("format axis (ADR 0028): file derivation, stray detection, per-format nesting\n")

    print(DIM + "1. Regression: every real bundle is unaffected" + OFF)
    tdir = os.path.join(ROOT, "templates")
    for b in gate.find_bundles(tdir):
        d = os.path.join(tdir, b)
        ok, detail = gate.check_files(b, d)
        check(b + " files", ok, detail)
        ok, detail = gate.check_nesting(b, d)
        check(b + " nesting", ok, detail)

    print("\n" + DIM + "2. Backward compatibility: a bundle declaring no format keys" + OFF)
    d = fixture(templates=PLAIN)
    default_fmt, additional, err = gate.parse_formats(NAME, d)
    check("parses as (None, [], None)", (default_fmt, additional, err) == (None, [], None),
          str((default_fmt, additional, err)))
    ok, detail = gate.check_files(NAME, d)
    check("check A passes", ok, detail)
    ok, detail = gate.check_nesting(NAME, d)
    check("check C message carries no format label", ok and detail.startswith("nests lean < full"),
          detail)

    print("\n" + DIM + "3. default_format alone: recording a choice made silently" + OFF)
    d = fixture(meta_extra="default_format: madr\n", templates=PLAIN)
    ok, detail = gate.check_files(NAME, d)
    check("check A passes and names the format", ok and "format madr" in detail, detail)
    ok, detail = gate.check_nesting(NAME, d)
    check("check C labels the format", ok and detail.startswith("madr nests"), detail)

    print("\n" + DIM + "4. THE CAPABILITY: formats are siblings, not parent and child" + OFF)
    # The canvas and the press release share no section spine. If nesting were still asserted
    # across formats this would fail, and the whole axis would be decorative.
    d = fixture(
        meta_extra=(
            "default_format: canvas\n"
            "additional_formats:\n"
            "  - id: prfaq\n"
            "    sizes: [full]\n"
            "    guidance: Use when the audience needs a launch narrative.\n"
        ),
        templates=dict(PLAIN, **{"template-prfaq-full.md": ["Press Release", "Customer FAQ"]}),
    )
    ok, detail = gate.check_nesting(NAME, d)
    check("unrelated outlines across formats PASS", ok, detail)
    check("  and the report says so explicitly",
          "no nesting asserted across formats" in detail, detail)
    ok, detail = gate.check_files(NAME, d)
    check("check A derives the compound filename", ok and "prfaq {full}" in detail, detail)

    print("\n" + DIM + "   ...but nesting is still enforced WITHIN a format" + OFF)
    d = fixture(
        meta_extra=(
            "default_format: canvas\n"
            "additional_formats:\n"
            "  - id: narrative\n"
            "    sizes: [lean, full]\n"
            "    guidance: Prose rather than cells.\n"
        ),
        templates=dict(PLAIN, **{
            "template-narrative-lean.md": ["Opening", "Rogue Section"],
            "template-narrative-full.md": ["Opening", "Closing"],
        }),
    )
    ok, detail = gate.check_nesting(NAME, d)
    check("a format that breaks its own nesting is rejected", not ok, detail)
    check("  message names the offending format", "narrative " in detail and "Rogue Section" in detail,
          detail)

    print("\n" + DIM + "5. THE CLOSED GAP: undeclared template files are now caught" + OFF)
    d = fixture(templates=dict(PLAIN, **{"template-narrative-full.md": ["Opening"]}))
    ok, detail = gate.check_files(NAME, d)
    check("compound-token file with no declaration is rejected", not ok, detail)
    check("  message names the file",
          "widget_template-narrative-full.md" in detail, detail)

    d = fixture(templates=dict(PLAIN, **{"template-wat.md": ["Opening"]}))
    ok, detail = gate.check_files(NAME, d)
    check("a wholly unrecognised token is rejected too", not ok, detail)

    # The other half of the same bug: such a file must also be SCANNED, or it ships unread.
    d = fixture(
        meta_extra=(
            "default_format: canvas\n"
            "additional_formats:\n"
            "  - id: prfaq\n"
            "    sizes: [full]\n"
            "    guidance: Launch narrative.\n"
        ),
        templates=dict(PLAIN, **{"template-prfaq-full.md": ["Press Release"]}),
    )
    scanned = [os.path.basename(p) for p in gate.bundle_files(NAME, d)]
    check("bundle_files() returns the additional-format file",
          NAME + "_template-prfaq-full.md" in scanned, str(scanned))
    check("  so whole-bundle scans (dashes, citations, links) read it",
          len([s for s in scanned if s.startswith(NAME + "_template-")]) == 3, str(scanned))

    print("\n" + DIM + "6. Adversarial: malformed declarations MUST fail, and say why" + OFF)

    d = fixture(
        meta_extra=(
            "additional_formats:\n"
            "  - id: prfaq\n"
            "    sizes: [full]\n"
            "    guidance: Launch narrative.\n"
        ),
        templates=dict(PLAIN, **{"template-prfaq-full.md": ["Press Release"]}),
    )
    ok, detail = gate.check_files(NAME, d)
    check("additional_formats without default_format is rejected", not ok, detail)
    check("  message explains the reader's problem",
          "cannot tell which format the plain template files are" in detail, detail)

    d = fixture(
        meta_extra=(
            "default_format: canvas\n"
            "additional_formats:\n"
            "  - id: canvas\n"
            "    sizes: [full]\n"
            "    guidance: Same name as the default.\n"
        ),
        templates=dict(PLAIN, **{"template-canvas-full.md": ["Opening"]}),
    )
    ok, detail = gate.check_files(NAME, d)
    check("a format that is both default and additional is rejected", not ok, detail)
    check("  message says it is one or the other", "it is one or the other" in detail, detail)

    d = fixture(
        meta_extra=(
            "default_format: canvas\n"
            "additional_formats:\n"
            "  - id: prfaq\n"
            "    sizes: [full]\n"
            "    guidance: One.\n"
            "  - id: prfaq\n"
            "    sizes: [lean]\n"
            "    guidance: Two.\n"
        ),
        templates=dict(PLAIN, **{
            "template-prfaq-full.md": ["A"], "template-prfaq-lean.md": ["A"],
        }),
    )
    ok, detail = gate.check_files(NAME, d)
    check("duplicate additional format ids are rejected", not ok, detail)
    check("  message names the duplicate", "prfaq" in detail, detail)

    d = fixture(
        meta_extra=(
            "default_format: canvas\n"
            "additional_formats:\n"
            "  - id: narrative\n"
            "    sizes: [lean, m]\n"
            "    guidance: Mixed vocabularies.\n"
        ),
        templates=PLAIN,
    )
    _, _, err = gate.parse_formats(NAME, d)
    check("a format mixing size vocabularies is rejected", bool(err), str(err))
    check("  message names the format and the rule",
          bool(err) and "narrative" in err and "never both" in err, str(err))

    d = fixture(meta_extra="default_format: canvas\nadditional_formats:\n", templates=PLAIN)
    _, _, err = gate.parse_formats(NAME, d)
    check("an empty additional_formats block is rejected", bool(err), str(err))

    print("\n" + DIM + "7. THE PARSER TRAP: a size word inside prose must not invent a variant" + OFF)
    # `guidance` is free prose and will contain words like "lean". Searching the whole entry for
    # size tokens would silently add a variant, then check A would demand a file for it.
    d = fixture(
        meta_extra=(
            "default_format: canvas\n"
            "additional_formats:\n"
            "  - id: narrative\n"
            "    sizes: [full]\n"
            "    guidance: Reach for this when the lean canvas is too thin to carry the argument.\n"
        ),
        templates=dict(PLAIN, **{"template-narrative-full.md": ["Opening"]}),
    )
    _, additional, err = gate.parse_formats(NAME, d)
    check("the word 'lean' in guidance is not read as a size",
          err is None and additional == [("narrative", ["full"])], str((additional, err)))
    ok, detail = gate.check_files(NAME, d)
    check("  so check A demands exactly the declared file", ok, detail)

    print("\n" + DIM + "8. Block-list syntax parses the same as inline" + OFF)
    d = fixture(
        meta_extra=(
            "default_format: canvas\n"
            "additional_formats:\n"
            "  - id: narrative\n"
            "    sizes:\n"
            "      - lean\n"
            "      - full\n"
            "    guidance: Block list rather than inline.\n"
        ),
        templates=dict(PLAIN, **{
            "template-narrative-lean.md": ["Opening"],
            "template-narrative-full.md": ["Opening", "Closing"],
        }),
    )
    _, additional, err = gate.parse_formats(NAME, d)
    check("a nested '- lean' is not mistaken for a new entry",
          err is None and additional == [("narrative", ["lean", "full"])], str((additional, err)))
    ok, detail = gate.check_files(NAME, d)
    check("  and check A derives both files", ok, detail)

    for d in tempdirs:
        shutil.rmtree(d, ignore_errors=True)

    failed = results.count(False)
    print()
    if failed:
        print(RED + "FAIL" + OFF + "  " + str(failed) + " of " + str(len(results))
              + " assertion(s) failed.")
        return 1
    print(GREEN + "OK" + OFF + "  " + str(len(results))
          + " assertions, the format axis holds and formats do not nest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
