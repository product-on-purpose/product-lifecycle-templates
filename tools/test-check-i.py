#!/usr/bin/env python3
"""
test-check-i.py - the adversarial test for check I's related_templates resolution.

WHAT THIS COVERS, AND WHAT IT DOES NOT.
This tests check I's `related_templates` branch and nothing else. Its `pairs_with` branch is
exercised by every real bundle on every gate run and is not fixtured here. Do not read a green
run as "check I is tested"; read it as "check I's future: logic is tested."

WHY THIS BRANCH EARNED ONE.
The stale-future: direction was unchecked from the convention's adoption until 2026-09-04, and
the defect recurred three times in that window: ADR 0022 corrected `future:rfc` and
`future:design-doc` in the adr and rfc bundles; 2026-07-30 corrected `future:okrs`,
`future:product-roadmap` and `future:product-strategy`; and the sweep that landed this check
found nine more, one of them (`future:prototype-brief`) pointing at a type ADR 0035 refused.
Each fix was correct and none of them held, because nothing re-read the claim. Per decision
procedure 9, a convention tested and failed becomes a check.

The negative cases are the point. A check that has never been observed failing is an assumption.
Each asserts on the message text, because the message is what the next person acts on.

Pure standard library, no framework, no dependencies. Runs in CI alongside the gate.
Usage: python tools/test-check-i.py
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

results = []


def check(label, passed, detail=""):
    results.append(passed)
    mark = GREEN + "PASS" + OFF if passed else RED + "FAIL" + OFF
    print("  " + mark + "  " + label)
    if not passed and detail:
        print("        got: " + detail)


def run(related):
    """Run check I against a throwaway meta carrying only related_templates.

    TEMPLATES_DIR is left pointing at the real tree, so "exists on disk" means what it means
    in production: a real bundle directory. That is deliberate. Substituting a fake bundle set
    would test the fixture rather than the thing the gate actually consults.
    """
    d = tempfile.mkdtemp()
    name = "fixture"
    body = "id: " + name + "\nrelated_templates: [" + ", ".join(related) + "]\n"
    with open(os.path.join(d, name + "_meta.yaml"), "w", encoding="utf-8") as f:
        f.write(body)
    try:
        return gate.check_refs(name, d)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def main():
    print("check I: related_templates resolution\n")

    print(DIM + "1. Regression: every real bundle still resolves its references" + OFF)
    tdir = os.path.join(ROOT, "templates")
    for b in gate.find_bundles(tdir):
        ok, detail = gate.check_refs(b, os.path.join(tdir, b))
        check(b, ok, detail)

    print("\n" + DIM + "2. The two legal shapes" + OFF)

    ok, detail = run(["prd", "user-stories"])
    check("a built bundle resolves", ok, detail)
    check("  detail reports the count", "related_templates 2 resolved" in detail, detail)

    ok, detail = run(["future:solution-brief"])
    check("future: on a genuinely unbuilt type resolves", ok, detail)

    print("\n" + DIM + "3. Adversarial: these MUST fail, and say why" + OFF)

    ok, detail = run(["future:prd"])
    check("future: on a BUILT bundle is rejected", not ok, detail)
    check("  message names the defect",
          "marks a built bundle as future:" in detail, detail)
    check("  message names the offending reference", "future:prd" in detail, detail)
    check("  message says what to do", "drop the future: prefix" in detail, detail)

    ok, detail = run(["no-such-bundle"])
    check("an unresolvable bare name is rejected", not ok, detail)
    check("  message uses the does-not-resolve wording",
          "does not resolve" in detail, detail)

    ok, detail = run(["future:"])
    check("an empty future: reference is rejected", not ok, detail)
    check("  message names it as empty", "empty future: reference" in detail, detail)

    print("\n" + DIM + "4. The two failure kinds do not blur into one message" + OFF)
    ok, detail = run(["future:prd", "no-such-bundle"])
    check("both kinds reported together", not ok, detail)
    check("  the unresolvable one keeps its own wording",
          "does not resolve: no-such-bundle" in detail, detail)
    check("  the stale one keeps its own wording",
          "marks a built bundle as future: future:prd" in detail, detail)
    check("  the stale one is not told to add a future: prefix it already has",
          detail.count("or prefix future: if it does not yet") == 1, detail)

    failed = results.count(False)
    print()
    if failed:
        print(RED + "FAIL" + OFF + "  " + str(failed) + " of " + str(len(results))
              + " assertion(s) failed.")
        return 1
    print(GREEN + "OK" + OFF + "  " + str(len(results))
          + " assertions, check I holds in both directions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
