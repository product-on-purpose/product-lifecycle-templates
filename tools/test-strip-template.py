#!/usr/bin/env python3
"""
test-strip-template.py - the adversarial test for the fill-provenance strip tool.

WHAT THIS COVERS.
`strip-template.py`'s three jobs: remove guidance comments, refuse on unfilled placeholders, and stamp
fill provenance. It does not test the LP-1 interview flow, which is agent guidance rather than code.

WHY THE REFUSAL IS THE LOAD-BEARING TEST.
The tool's reason to exist is preventing a document that looks finished and is not. If the placeholder
scan silently passes, the tool is worse than nothing: it produces a comment-free document that reads as
shippable with `{{owner}}` still in it. So the assertions that matter are the ones proving it refuses,
and proving it refuses for the right reason.

The subtle case is the one that would break a naive implementation: the guidance comments THEMSELVES
name placeholders. Every variant's preamble says "Replace each {{placeholder}} with your content", and
GOOD examples quote placeholder-shaped text. A tool that scans the raw file before stripping refuses
every document forever, including correctly filled ones. The scan therefore runs on the stripped body,
and that ordering is asserted below rather than left as a comment.

Pure standard library. Runs in CI alongside the gate.
Usage: python tools/test-strip-template.py
"""
import importlib.util
import os
import re
import shutil
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
TOOL = os.path.join(SCRIPT_DIR, "strip-template.py")

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

spec = importlib.util.spec_from_file_location("strip_template", TOOL)
strip = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strip)

results = []


def check(label, passed, detail=""):
    results.append(passed)
    print("  " + (GREEN + "PASS" + OFF if passed else RED + "FAIL" + OFF) + "  " + label)
    if not passed and detail:
        print("        got: " + str(detail)[:300])


# Two fixtures on purpose. FRONT_RAW still carries its {{title}} placeholder, which is what an
# unfilled template looks like and must be refused; FRONT is what a filled one looks like. The
# frontmatter is deliberately in scope for the placeholder scan: a document whose title is still
# {{title}} is not finished, however complete its body looks.
FRONT_RAW = ('---\ntitle: "{{title}}"\ndoc_type: prd\nsize: lean\nstatus: draft\n'
             'source_template: prd\nsource_template_version: 0.1.0\n---\n')
FRONT = ('---\ntitle: "A Real Title"\ndoc_type: prd\nsize: lean\nstatus: draft\n'
         'source_template: prd\nsource_template_version: 0.1.0\n---\n')
PREAMBLE = ("<!--\nHOW TO FILL THIS IN\n"
            "2. Replace each {{placeholder}} with your content.\n-->\n")
GUIDANCE = ("<!-- WHAT  A thing.\n     WHY   Because.\n     ASK   Is it?\n"
            "     GOOD  Something like {{example_token}}.\n"
            "     WEAK  A weak one.\n     TRAP  The trap. -->\n")


def doc(body, front=FRONT):
    return front + PREAMBLE + body


def run(text, argv_extra=None, name="doc.md"):
    """Run the tool over a temp file; return (exit_code, output_text_or_None)."""
    d = tempfile.mkdtemp()
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    out = os.path.join(d, "out.md")
    argv = [p, "--out", out] + (argv_extra or [])
    try:
        code = strip.main(argv)
        got = open(out, encoding="utf-8").read() if os.path.isfile(out) else None
        return code, got
    finally:
        shutil.rmtree(d, ignore_errors=True)


def main():
    print("strip-template: guidance removal, refusal, and fill provenance\n")

    print(DIM + "1. The refusal, which is the reason this tool exists" + OFF)
    code, out = run(doc("## Alpha\n\n" + GUIDANCE + "\n{{unfilled}}\n"))
    check("an unfilled placeholder in the BODY refuses", code == 2, code)
    check("  and writes NO output file", out is None, "wrote a file anyway")

    code, out = run(doc("## Alpha\n\n" + GUIDANCE + "\nreal content\n", front=FRONT_RAW))
    check("an unfilled placeholder in the FRONTMATTER also refuses", code == 2, code)

    code, out = run(doc("## Alpha\n\n" + GUIDANCE + "\nreal content\n"))
    check("a fully filled document is accepted", code == 0, code)

    print("\n" + DIM + "2. Guidance comments name placeholders; that must not refuse a good doc" + OFF)
    # The preamble literally contains {{placeholder}} and GOOD contains {{example_token}}.
    # A scan of the RAW file sees two placeholders in a document that has none.
    raw_hits = sorted(set(strip.PLACEHOLDER_RE.findall(doc("## Alpha\n\n" + GUIDANCE + "\ndone\n"))))
    check("  the raw file does contain placeholder-shaped guidance text",
          "placeholder" in raw_hits and "example_token" in raw_hits, raw_hits)
    code, out = run(doc("## Alpha\n\n" + GUIDANCE + "\ndone\n"))
    check("  yet the tool accepts it, because it scans the STRIPPED body", code == 0, code)
    check("  and neither token survives into the output",
          out is not None and "example_token" not in out and "{{" not in out, out)

    print("\n" + DIM + "3. Comment removal" + OFF)
    code, out = run(doc("## Alpha\n\n" + GUIDANCE + "\nbody\n"))
    check("no HTML comment survives", "<!--" not in out, out)
    check("  the heading survives", "## Alpha" in out, out)
    check("  the content survives", "body" in out, out)
    check("  no run of 3+ blank lines is left behind",
          not re.search(r"\n[ \t]*\n[ \t]*\n", out), repr(out[-200:]))

    print("\n" + DIM + "4. Provenance stamping" + OFF)
    code, out = run(doc("## Alpha\n\n" + GUIDANCE + "\nbody\n"),
                    ["--filled-by", "agent:claude", "--fill-method", "interview"])
    check("stamps all three fill keys", code == 0 and all(
        k in out for k in ["filled_by:", "fill_method:", "fill_date:"]), out)
    check("  filled_by carries the given identity", 'filled_by: "agent:claude"' in out, out)
    check("  fill_method carries the given method", "fill_method: interview" in out, out)
    check("  fill_date is an ISO date", re.search(r"fill_date: \d{4}-\d{2}-\d{2}", out or ""), out)
    order = [out.index("filled_by:"), out.index("fill_method:"), out.index("fill_date:")]
    check("  the three appear in declared order", order == sorted(order), order)
    check("  they sit after the provenance pair the templates already carry",
          out.index("source_template_version:") < out.index("filled_by:"), "wrong position")
    check("  the pre-existing provenance is untouched",
          "source_template: prd" in out and "source_template_version: 0.1.0" in out, out)

    print("\n" + DIM + "5. Re-stamping replaces; it never duplicates" + OFF)
    once = doc("## Alpha\n\n" + GUIDANCE + "\nbody\n")
    code, out = run(once, ["--filled-by", "First"])
    code2, out2 = run(out, ["--filled-by", "Second"])
    check("a second pass succeeds", code2 == 0, code2)
    check("  filled_by appears exactly once", out2.count("filled_by:") == 1, out2.count("filled_by:"))
    check("  and carries the new value", 'filled_by: "Second"' in out2, out2)

    print("\n" + DIM + "6. The partial-save escape hatch" + OFF)
    code, out = run(doc("## Alpha\n\n" + GUIDANCE + "\n{{later}}\n"), ["--allow-placeholders"])
    check("--allow-placeholders lets an unfilled document through", code == 0, code)
    check("  and the placeholder is preserved, not silently dropped", "{{later}}" in out, out)

    print("\n" + DIM + "7. Documents that are not from this library" + OFF)
    code, out = run("# Plain\n\nNo frontmatter here.\n<!-- a note -->\n")
    check("a file with no frontmatter still strips", code == 0 and "<!--" not in out, (code, out))
    code, out = run("# Plain\n\nno frontmatter\n", ["--filled-by", "X"])
    check("  but stamping one without frontmatter is a usage error", code == 1, code)

    print("\n" + DIM + "8. Against a real template from the tree" + OFF)
    real = os.path.join(ROOT, "templates", "prd", "prd_template-lean.md")
    text = open(real, encoding="utf-8").read()
    code, out = run(text, name="prd_template-lean.md")
    check("an UNFILLED real template refuses", code == 2, code)
    filled = text
    body = strip.COMMENT_RE.sub("", text)
    for n in sorted(set(strip.PLACEHOLDER_RE.findall(body))):
        filled = filled.replace("{{" + n + "}}", "X_" + n)
    code, out = run(filled, ["--filled-by", "tester"], name="prd_template-lean.md")
    check("  a FILLED real template strips clean", code == 0, code)
    check("  with no comments and no placeholders left",
          out is not None and "<!--" not in out and "{{" not in out)
    check("  and its frontmatter still parses as YAML", _yaml_ok(out), (out or "")[:200])

    failed = results.count(False)
    print()
    if failed:
        print(RED + "FAIL" + OFF + "  " + str(failed) + " of " + str(len(results)) + " assertion(s) failed.")
        return 1
    print(GREEN + "OK" + OFF + "  " + str(len(results))
          + " assertions, the strip tool refuses when it should and stamps what it claims.")
    return 0


def _yaml_ok(text):
    try:
        import yaml
    except ImportError:
        return True  # same SKIP posture the gate takes when PyYAML is absent
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text or "", re.S)
    if not m:
        return False
    try:
        return isinstance(yaml.safe_load(m.group(1)), dict)
    except Exception:
        return False


if __name__ == "__main__":
    raise SystemExit(main())
