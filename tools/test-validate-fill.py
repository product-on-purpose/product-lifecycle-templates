#!/usr/bin/env python3
"""
test-validate-fill.py - the adversarial test for the fill validator.

WHAT THIS COVERS.
`validate-fill.py`'s four checks: section completeness against `sections.json`, unfilled placeholders,
leftover guidance, and fill provenance. It does not test grading, which the tool explicitly does not do.

WHY THE REGRESSION OVER ALL 58 VARIANTS IS THE LOAD-BEARING CASE.
The validator looks a section up by slugging its heading and matching the id `gen-sections.py` wrote.
Two functions in two files must agree exactly, forever. If they drift, the validator reports sections
missing that are present, or worse, reports a document complete because it matched nothing and found
nothing missing. Neither failure is visible from one hand-written fixture. Running the real tree
through it proves the two agree on every heading the library actually contains, including the
multi-format bundles and the H1 and H3 sections that the AG-1 sketch did not anticipate.

THE FAILURE THAT WOULD BE INVISIBLE.
A validator that silently resolves nothing passes everything. So the assertions below check not only
that a good document passes, but that a BROKEN one fails, and that a document naming a bundle which
does not exist is an error rather than a pass.

Pure standard library. Runs in CI alongside the gate.
Usage: python tools/test-validate-fill.py
"""
import importlib.util
import json
import os
import re
import shutil
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"


def _load(name):
    spec = importlib.util.spec_from_file_location(
        name.replace("-", "_"), os.path.join(SCRIPT_DIR, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


val = _load("validate-fill")
gen = _load("gen-sections")

results = []


def check(label, passed, detail=""):
    results.append(passed)
    print("  " + (GREEN + "PASS" + OFF if passed else RED + "FAIL" + OFF) + "  " + label)
    if not passed and detail:
        print("        got: " + str(detail)[:300])


def tmpdoc(text):
    d = tempfile.mkdtemp()
    p = os.path.join(d, "doc.md")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return d, p


def run(text):
    d, p = tmpdoc(text)
    try:
        return val.validate(p)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def levels(findings):
    return {m.split(",")[0][:24]: l for l, m in findings}


def fails(findings):
    return [m for l, m in findings if l == "fail"]


def build_good():
    """A complete filled prd/lean document, with its section list taken FROM THE SCHEMA.

    Hand-writing the headings here would make the fixture drift the moment a template gains a
    section, and it would fail in the most confusing way possible: the validator reporting sections
    missing while being entirely correct. Deriving the fixture means this test asserts the
    validator's behaviour rather than a snapshot of prd.
    """
    schema = val.load_schema()
    declared, err = val.find_variant(schema, "prd", None, "lean")
    assert not err, err
    head = ('---\ntitle: "A Real PRD"\ndoc_type: prd\nsize: lean\nstatus: draft\n'
            'source_template: prd\nsource_template_version: 0.1.0\n'
            'filled_by: "tester"\nfill_method: manual\nfill_date: 2026-09-05\n---\n\n'
            '# A Real PRD\n')
    body = "".join("\n" + "#" * s["level"] + " " + s["title"] + "\n\nSomething.\n"
                   for s in declared)
    return head + body


GOOD = build_good()


def main():
    print("validate-fill: completeness, placeholders, guidance, provenance\n")

    print(DIM + "1. The slug contract: two files must agree on every heading in the tree" + OFF)
    mismatched = []
    for b in gen.find_bundles(gen.TEMPLATES_DIR):
        d = os.path.join(gen.TEMPLATES_DIR, b)
        for fn in sorted(os.listdir(d)):
            if "_template-" not in fn:
                continue
            for sec in gen.parse_variant(os.path.join(d, fn)):
                if val.slug(sec["title"]) != sec["id"]:
                    mismatched.append((fn, sec["title"], sec["id"], val.slug(sec["title"])))
    check("validate-fill.slug agrees with gen-sections on every real section",
          not mismatched, mismatched[:4])

    print("\n" + DIM + "2. Every real variant resolves its schema entry" + OFF)
    schema = val.load_schema()
    check("sections.json loads", schema is not None)
    unresolved = []
    import yaml
    for b in gen.find_bundles(gen.TEMPLATES_DIR):
        d = os.path.join(gen.TEMPLATES_DIR, b)
        meta = yaml.safe_load(open(os.path.join(d, b + "_meta.yaml"), encoding="utf-8").read())
        for fmt, size, fname in gen.variant_files(b, meta):
            if not os.path.isfile(os.path.join(d, fname)):
                continue
            declared, err = val.find_variant(schema, b, None if fmt == "default" else fmt, size)
            if err or not declared:
                unresolved.append((fname, err))
    check("all 58 variants resolve to a non-empty declared section list",
          not unresolved, unresolved[:4])

    print("\n" + DIM + "3. A good document passes; the tool is not vacuously green" + OFF)
    ok, f = run(GOOD)
    check("a complete document validates", ok, fails(f))
    check("  and reports the section count it checked",
          any("declared section(s) present" in m for _, m in f), f)

    print("\n" + DIM + "4. Each check must FAIL independently" + OFF)
    ok, f = run(GOOD.replace("## Problem\n\nSomething.\n", ""))
    check("a missing section fails", not ok and any("missing" in m for m in fails(f)), fails(f))

    ok, f = run(GOOD.replace("Something.", "{{unfilled}}", 1))
    check("an unfilled placeholder fails",
          not ok and any("placeholder" in m for m in fails(f)), fails(f))

    ok, f = run(GOOD.replace("# A Real PRD", "# A Real PRD\n\n<!-- WHAT  leftover guidance. -->"))
    check("a leftover guidance comment fails",
          not ok and any("guidance comment" in m for m in fails(f)), fails(f))

    ok, f = run(GOOD.replace('filled_by: "tester"\n', ""))
    check("missing provenance fails", not ok and any("provenance" in m for m in fails(f)), fails(f))
    check("  and names the missing key", any("filled_by" in m for m in fails(f)), fails(f))

    print("\n" + DIM + "5. Documents it must refuse to guess about" + OFF)
    ok, f = run(GOOD.replace("source_template: prd", "source_template: no-such-bundle"))
    check("an unknown source_template is an error, not a pass",
          not ok and any("no bundle named" in m for m in fails(f)), fails(f))

    ok, f = run(GOOD.replace("size: lean", "size: enormous"))
    check("an unknown size is an error", not ok and any("no size" in m for m in fails(f)), fails(f))

    ok, f = run("# No frontmatter\n\ntext\n")
    check("a document with no frontmatter is an error", not ok, f)

    ok, f = run(GOOD.replace("source_template: prd\n", ""))
    check("a document with no source_template is an error",
          not ok and any("source_template" in m for m in fails(f)), fails(f))

    print("\n" + DIM + "6. The document title is not an 'extra section'" + OFF)
    ok, f = run(GOOD)
    notes = [m for l, m in f if l == "note"]
    check("a plain H1 title produces no extra-section note", not notes, notes)
    ok, f = run(GOOD.replace("## Summary", "## Summary\n\ntext\n\n## Invented Section"))
    notes = [m for l, m in f if l == "note"]
    check("  but a genuinely extra H2 IS noted", any("extra section" in m for m in notes), notes)
    check("  and an extra section does not fail the document", ok, fails(f))

    print("\n" + DIM + "7. A multi-format bundle resolves per format" + OFF)
    declared_canvas, err1 = val.find_variant(schema, "product-vision", None, "lean")
    declared_prfaq, err2 = val.find_variant(schema, "product-vision", "prfaq", "full")
    check("the default format resolves", err1 is None and declared_canvas, err1)
    check("a named additional format resolves", err2 is None and declared_prfaq, err2)
    check("  and they are different section sets",
          {s["id"] for s in declared_canvas} != {s["id"] for s in declared_prfaq})
    _, err3 = val.find_variant(schema, "product-vision", "nonesuch", "full")
    check("an unknown format is an error", err3 is not None and "no format" in err3, err3)

    failed = results.count(False)
    print()
    if failed:
        print(RED + "FAIL" + OFF + "  " + str(failed) + " of " + str(len(results)) + " assertion(s) failed.")
        return 1
    print(GREEN + "OK" + OFF + "  " + str(len(results))
          + " assertions, the validator agrees with the schema and fails when it should.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
