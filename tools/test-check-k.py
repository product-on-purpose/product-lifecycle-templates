#!/usr/bin/env python3
"""
test-check-k.py - the adversarial test for check K's taxonomy-axis logic.

WHAT THIS COVERS, AND WHAT IT DOES NOT.
This tests check K (family-contract conformance) and nothing else. Checks A through J have no
automated test; they are verified by running the gate against real bundles, which is the same
argument the gate itself makes about the Definition of Done. Do not read a green run here as
"the gate is tested"; read it as "check K's axis logic is tested."

WHY CHECK K EARNED ONE.
Every other check has a live subject: run the gate and nine real bundles exercise it. Check K's
classification-axis branch has no live subject and will not have one until governance-docs lands,
so the only way to prove it works, and more importantly that it FAILS when it should, is a
fixture. A check that has never been observed failing is an assumption, not a check.

The negative cases are the point. Each asserts on the message text, because a check that fails
with an unactionable message costs the next person the same investigation twice.

Pure standard library, no framework, no dependencies. Runs in CI alongside the gate.
Usage: python tools/test-check-k.py
"""
import importlib.util
import os
import shutil
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
GATE = os.path.join(SCRIPT_DIR, "check-bundles.py")

# A contract path that resolves, so the fixtures isolate the axis logic instead of also tripping
# the "contract file missing" problem. Which contract does not matter; that it exists does.
REAL_CONTRACT = "docs/internal/contracts/delivery-docs.md"

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


def fixture(name, family, axis_line):
    """A throwaway bundle dir holding only the meta, which is all check K reads."""
    d = tempfile.mkdtemp()
    body = (
        "id: " + name + "\nfamily: " + family + "\n" + axis_line
        + "\nstatus: beta\nsizes_available: [lean, full]\n"
    )
    with open(os.path.join(d, name + "_meta.yaml"), "w", encoding="utf-8") as f:
        f.write(body)
    return d


def run(name, family, axis_line, registry):
    """Run check K against a fixture under a substituted contract registry."""
    d = fixture(name, family, axis_line)
    saved = gate.FAMILY_CONTRACTS
    gate.FAMILY_CONTRACTS = registry
    try:
        return gate.check_family(name, d)
    finally:
        gate.FAMILY_CONTRACTS = saved
        shutil.rmtree(d, ignore_errors=True)


CLASSIFICATION_FAMILY = {"governance-docs": {
    "contract": REAL_CONTRACT,
    "classification": "utility",
    "status": ["beta", "stable"],
    "size_shapes": [["lean", "full"], ["lean"]],
}}
PHASE_FAMILY = {"delivery-docs": {
    "contract": REAL_CONTRACT,
    "phase": "deliver",
    "status": ["beta", "stable"],
    "size_shapes": [["lean", "full"], ["lean"]],
}}


def main():
    print("check K: taxonomy-axis conformance\n")

    print(DIM + "1. Regression: every real bundle still conforms on the phase axis" + OFF)
    tdir = os.path.join(ROOT, "templates")
    for b in gate.find_bundles(tdir):
        ok, detail = gate.check_family(b, os.path.join(tdir, b))
        check(b, ok, detail)
        if "no ratified contract" not in detail:
            check(b + " reports the phase axis", "(phase," in detail, detail)

    print("\n" + DIM + "2. The new capability: a classification family accepts a member" + OFF)
    ok, detail = run("risk-register", "governance-docs", "classification: utility",
                     CLASSIFICATION_FAMILY)
    check("classification: utility conforms", ok, detail)
    check("reports the classification axis", "(classification," in detail, detail)

    print("\n" + DIM + "3. Adversarial: these MUST fail, and say why" + OFF)

    ok, detail = run("risk-register", "governance-docs", "classification: tool",
                     CLASSIFICATION_FAMILY)
    check("wrong classification value is rejected", not ok, detail)
    check("  message names the required value", "requires utility" in detail, detail)

    ok, detail = run("kpi-dashboard", "governance-docs", "phase: measure", CLASSIFICATION_FAMILY)
    check("phase declared in a classification family is rejected", not ok, detail)
    check("  message names the axis actually found",
          "declares no classification" in detail and "found phase: measure" in detail, detail)

    ok, detail = run("prd", "delivery-docs", "classification: utility", PHASE_FAMILY)
    check("classification declared in a phase family is rejected", not ok, detail)
    check("  message names the axis actually found",
          "declares no phase" in detail and "found classification: utility" in detail, detail)

    both = {"broken-docs": dict(contract=REAL_CONTRACT, phase="deliver",
                                classification="utility", status=["beta"],
                                size_shapes=[["lean", "full"]])}
    ok, detail = run("x", "broken-docs", "phase: deliver", both)
    check("registry entry naming both axes is rejected", not ok, detail)
    check("  message says both", "declares both phase and classification" in detail, detail)

    neither = {"broken-docs": dict(contract=REAL_CONTRACT, status=["beta"],
                                   size_shapes=[["lean", "full"]])}
    ok, detail = run("x", "broken-docs", "phase: deliver", neither)
    check("registry entry naming no axis is rejected", not ok, detail)
    check("  message says neither", "declares neither phase nor classification" in detail, detail)

    print("\n" + DIM + "4. Set-valued axis: a family spanning two classes (ADR 0023)" + OFF)
    # strategy-docs holds foundation artifacts (vision, strategy) and utility ones (roadmap, okrs).
    # Axis coherence is one AXIS, not one value; `status` has always worked this way.
    spanning = {"strategy-docs": {
        "contract": REAL_CONTRACT,
        "classification": ["foundation", "utility"],
        "status": ["beta", "stable"],
        "size_shapes": [["lean", "full"], ["lean"]],
    }}
    ok, detail = run("product-vision", "strategy-docs", "classification: foundation", spanning)
    check("first allowed value conforms", ok, detail)
    ok, detail = run("product-roadmap", "strategy-docs", "classification: utility", spanning)
    check("second allowed value conforms", ok, detail)
    ok, detail = run("runbook", "strategy-docs", "classification: tool", spanning)
    check("a value outside the set is rejected", not ok, detail)
    check("  message lists the allowed set", "allows foundation/utility" in detail, detail)
    ok, detail = run("business-case", "strategy-docs", "phase: discover", spanning)
    check("wrong axis is still rejected against a set", not ok, detail)
    check("  message lists the set, not a bare value",
          "requires classification: foundation/utility" in detail, detail)

    print("\n" + DIM + "5. Unchanged: a family with no ratified contract still passes" + OFF)
    ok, detail = run("wireframe", "design-docs", "phase: develop", CLASSIFICATION_FAMILY)
    check("uncontracted family passes with a note",
          ok and "no ratified contract" in detail, detail)

    failed = results.count(False)
    print()
    if failed:
        print(RED + "FAIL" + OFF + "  " + str(failed) + " of " + str(len(results))
              + " assertion(s) failed.")
        return 1
    print(GREEN + "OK" + OFF + "  " + str(len(results)) + " assertions, check K holds on both axes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
