#!/usr/bin/env python3
"""test-gen-skill-descriptions.py - the self-test for the skill-description generator.

WHAT IT COVERS.
`gen-skill-descriptions.py --check` in CI proves the committed descriptions match the generator on
today's tree. It cannot prove the generator's rules fire, because today's tree breaks none of them.
A rule that never fires looks exactly like a rule that works. So each case below builds a small
fixture that breaks one rule, and asserts the generator reports it. The rules matter because a
silent pass is the dangerous failure: a type missing from the list never triggers its skill, and
nothing else would say so.

Pure standard library. Usage: python tools/test-gen-skill-descriptions.py
"""
import importlib.util
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("gsd", os.path.join(SCRIPT_DIR, "gen-skill-descriptions.py"))
gsd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gsd)

passed = failed = 0


def check(label, cond):
    global passed, failed
    if cond:
        passed += 1
    else:
        failed += 1
        print(f"FAIL  {label}")


def b(i, name, family="f1"):
    return {"id": i, "trigger_name": name, "family": family}


GROUPS = {"all": {"families": "*"}}
SKILLS = {"s": {"group": "all", "text": "Fills a {count}-bundle library. Use when writing a {list}."}}

# 1. The happy path, including a shared phrase written once.
bs = [b("a", "alpha"), b("b", "beta or gamma"), b("c", "beta or gamma"), b("d", "delta")]
d, e = gsd.build(bs, GROUPS, SKILLS, {"all": ["a", "b", "c", "d"]})
check("happy path has no errors", e == [])
check("shared phrase is written once, Oxford 'or'", d.get("s") == "Fills a 4-bundle library. Use when writing a alpha, beta or gamma, or delta.")

# 2. A bundle missing from ORDER fails, naming the bundle.
d, e = gsd.build(bs, GROUPS, SKILLS, {"all": ["a", "b", "c"]})
check("missing id fails", any("does not place: d" in x for x in e))

# 3. An id in ORDER that is not a bundle fails.
d, e = gsd.build(bs, GROUPS, SKILLS, {"all": ["a", "b", "c", "d", "zz"]})
check("unknown id fails", any("not bundles in this group: zz" in x for x in e))

# 4. An id listed twice fails.
d, e = gsd.build(bs, GROUPS, SKILLS, {"all": ["a", "b", "c", "d", "a"]})
check("duplicate id fails", any("more than once: a" in x for x in e))

# 5. A shared phrase whose bundles are not adjacent fails.
d, e = gsd.build(bs, GROUPS, SKILLS, {"all": ["b", "a", "c", "d"]})
check("non-adjacent shared phrase fails", any("not next to each other" in x for x in e))

# 6. A missing trigger_name fails.
d, e = gsd.build([b("a", ""), b("d", "delta")], GROUPS, SKILLS, {"all": ["a", "d"]})
check("empty trigger_name fails", any("a: no trigger_name" in x for x in e))

# 7. Over the cap fails, and names the split as the remedy.
d, e = gsd.build(bs, GROUPS, SKILLS, {"all": ["a", "b", "c", "d"]}, cap=40)
check("over-cap fails", any("over the 40 cap" in x and "ADR 0093" in x for x in e))

# 8. A description that is not a plain YAML scalar fails.
d, e = gsd.build([b("a", "alpha: one")], GROUPS, SKILLS, {"all": ["a"]})
check("colon-space fails", any("plain YAML scalar" in x for x in e))

# 9. Two groups: each bundle lands in exactly one, by family.
G2 = {"g1": {"families": ["f1"]}, "g2": {"families": ["f2"]}}
S2 = {"s1": {"group": "g1", "text": "One {list}."}, "s2": {"group": "g2", "text": "Two {list}."}}
bs2 = [b("a", "alpha", "f1"), b("x", "xray", "f2")]
d, e = gsd.build(bs2, G2, S2, {"g1": ["a"], "g2": ["x"]})
check("two groups list their own types", e == [] and d == {"s1": "One alpha.", "s2": "Two xray."})
d, e = gsd.build(bs2 + [b("q", "quebec", "f3")], G2, S2, {"g1": ["a"], "g2": ["x"]})
check("a family in no group fails", any("q: family 'f3' is in 0 groups" in x for x in e))

# 10. A shared phrase across two groups fails.
bs3 = [b("a", "shared", "f1"), b("x", "shared", "f2")]
S3 = {"s1": {"group": "g1", "text": "One {list}."}, "s2": {"group": "g2", "text": "Two {list}."}}
d, e = gsd.build(bs3, G2, S3, {"g1": ["a"], "g2": ["x"]})
check("shared phrase across groups fails", any("used in groups" in x for x in e))

# 11. The live tree: every bundle placed once, and the real ORDER covers the manifest exactly.
with open(os.path.join(gsd.ROOT, "manifest.json"), encoding="utf-8") as f:
    live = json.load(f)["bundles"]
d, e = gsd.build(live)
check("live tree builds with no errors", e == [])
check("live ORDER covers every bundle once", sorted(gsd.ORDER["all"]) == sorted(x["id"] for x in live))

print(f"{'OK' if not failed else 'FAIL'}  gen-skill-descriptions self-test: {passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
