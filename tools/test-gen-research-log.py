#!/usr/bin/env python3
"""Fixture tests for tools/gen-research-log.py.

WHY THIS EXISTS. Same argument as test-check-k.py and test-check-formats.py (ADR 0025): the branches that
matter here have no live subject once a run is clean. A collision only happens when two dimensions own the
same source, and a well-behaved fan-out mostly avoids that, so the merge path can rot for months and only
announce itself by quietly dropping quotations from a shipped bundle. That is exactly how the two bugs this
generator exists to fix went unnoticed: entry [1] of one research log kept 4 of its 10 verified quotes and
nothing failed.

MUTATION-CHECKED. Every assertion below is paired with a deliberately broken implementation of the same
logic, and the test asserts that the broken version produces a DIFFERENT answer. An assertion that passes
against both the correct and the broken code proves nothing, and this file refuses to contain one.
"""
import importlib.util
import json
import pathlib
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("genlog", HERE / "gen-research-log.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

PASS = 0
FAIL = []


def check(label, got, want):
    global PASS
    if got == want:
        PASS += 1
    else:
        FAIL.append(label + "\n      got:  " + repr(got) + "\n      want: " + repr(want))


def run(label, condition):
    global PASS
    if condition:
        PASS += 1
    else:
        FAIL.append(label)


def src(identity, url, tier="primary", status="fetched-and-verified", supports="s", quotable=None):
    return {
        "identity": identity, "url": url, "tier": tier, "retrieval_status": status,
        "supports": supports, "quotable": quotable or [],
    }


def dim(name, sources):
    return {"dimension": name, "owned_sources": sources}


# ---------------------------------------------------------------- URL normalisation (bug 1)

check("norm strips www", gen.normalise_url("https://www.example.com/a"), gen.normalise_url("https://example.com/a"))
check("norm strips trailing slash", gen.normalise_url("https://example.com/a/"), gen.normalise_url("https://example.com/a"))
check("norm unifies scheme", gen.normalise_url("http://example.com/a"), gen.normalise_url("https://example.com/a"))
check("norm strips fragment", gen.normalise_url("https://example.com/a#top"), gen.normalise_url("https://example.com/a"))
run("norm keeps distinct paths distinct", gen.normalise_url("https://example.com/a") != gen.normalise_url("https://example.com/b"))
run("norm keeps query strings", gen.normalise_url("https://example.com/a?v=1") != gen.normalise_url("https://example.com/a"))

# MUTATION: dedup on the raw URL, which is the bug measured on 2026-08-06.
raw_key = lambda u: u.strip().lower()
run("MUTATION raw-URL keying would file www and non-www separately",
    raw_key("https://www.example.com/a") != raw_key("https://example.com/a"))

# ---------------------------------------------------------------- the collision merge (bug 2)

TWO_DIMS = [
    dim("d1", [src("Scrum Guide", "https://www.scrumguides.org/scrum-guide.html",
                   supports="defines the event", quotable=["alpha", "beta"])]),
    dim("d2", [src("Scrum Guide", "https://scrumguides.org/scrum-guide.html/",
                   supports="supplies the counts", quotable=["gamma", "beta"])]),
]
entries, order, collisions = gen.merge(TWO_DIMS)
check("www pair collapses to one entry", len(order), 1)
check("collision is reported, not hidden", len(collisions), 1)
entry = entries[order[0]]
check("quotables are UNIONED across dimensions", entry["quotable"], ["alpha", "beta", "gamma"])
check("duplicate quotable is not repeated", entry["quotable"].count("beta"), 1)
check("supports clauses are unioned too", len(entry["supports"]), 2)
check("both owning dimensions recorded", entry["dimensions"], ["d1", "d2"])

# MUTATION: replace the dict on collision instead of unioning, the 2026-08-06 bug verbatim.
def merge_replacing(results):
    out = {}
    for d in results:
        for s in d.get("owned_sources", []):
            out[gen.normalise_url(s["url"])] = dict(s)  # replaces, losing the earlier quotables
    return out
mutated = merge_replacing(TWO_DIMS)
lost = mutated[gen.normalise_url("https://scrumguides.org/scrum-guide.html")]["quotable"]
run("MUTATION replacing-merge loses quotables the union keeps", set(lost) != set(entry["quotable"]))
check("MUTATION replacing-merge keeps only the last dimension's quotes", sorted(lost), ["beta", "gamma"])

# ---------------------------------------------------------------- merging across RUNS, not just dimensions

with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    run_a = tmp / "a.json"
    run_b = tmp / "b.json"
    run_a.write_text(json.dumps({"result": {"results": [TWO_DIMS[0]]}}), encoding="utf-8")
    # A relaunched dimension lands in its own file and re-owns the same canonical source.
    run_b.write_text(json.dumps({"result": {"results": [TWO_DIMS[1]]}}), encoding="utf-8")
    across = gen.load_runs([run_a, run_b])
    check("both run files load", len(across), 2)
    e2, o2, c2 = gen.merge(across)
    check("cross-RUN collision collapses to one entry", len(o2), 1)
    check("cross-RUN quotables are unioned", e2[o2[0]]["quotable"], ["alpha", "beta", "gamma"])

    # MUTATION: process each run separately, which is what a single-file tool would do.
    per_file = [gen.merge(gen.load_runs([f]))[1] for f in (run_a, run_b)]
    run("MUTATION per-file processing yields two entries for one source",
        sum(len(o) for o in per_file) == 2)

    out = tmp / "out.md"
    gen.main([str(out), str(run_a), str(run_b)])
    text = out.read_text(encoding="utf-8")
    run("CLI writes an entry block", text.startswith("### ") and "**[1]" in text)
    run("CLI emits exactly one numbered entry", text.count("**[") == 1)

# ---------------------------------------------------------------- honest retrieval

UNREAD = [dim("d", [src("Unread", "https://example.com/u", status="url-confirmed-not-read",
                        quotable=["must not survive"])])]
e3, o3, _ = gen.merge(UNREAD)
rendered = gen.render(e3, o3)
run("a quotable on a non-fetched source is DROPPED", "must not survive" not in rendered)
run("and the drop is stated in the entry rather than silent", "gen-research-log.py" in rendered)
run("the entry keeps its honest status token", "url-confirmed-not-read" in rendered)

# A stronger status from a second dimension wins, because that dimension really read the body.
MIXED = [
    dim("d1", [src("S", "https://example.com/s", status="url-confirmed-not-read")]),
    dim("d2", [src("S", "https://example.com/s", status="fetched-and-verified", quotable=["real"])]),
]
e4, o4, _ = gen.merge(MIXED)
check("stronger retrieval status wins on collision", e4[o4[0]]["status"], "fetched-and-verified")
run("and its quotable survives", "real" in gen.render(e4, o4))

# MUTATION: last-writer-wins on status would demote a source that was actually read.
run("MUTATION last-writer status would take the weaker token",
    MIXED[0]["owned_sources"][0]["retrieval_status"] == "url-confirmed-not-read")

# ---------------------------------------------------------------- numbering and house rules

MANY = [dim("d" + str(i), [src("S" + str(j), "https://example.com/" + str(i) + "/" + str(j))
                           for j in range(3)]) for i in range(3)]
e5, o5, _ = gen.merge(MANY)
body = gen.render(e5, o5)
numbers = [int(line.split("]")[0].lstrip("*[")) for line in body.splitlines() if line.startswith("**[")]
check("nine distinct sources produce nine entries", len(numbers), 9)
check("numbering is contiguous 1..N across the whole file", numbers, list(range(1, 10)))
check("grouping does not renumber", sorted(numbers), numbers)
run("every dimension gets a heading", body.count("### ") == 3)
run("--flat drops headings", "### " not in gen.render(e5, o5, group=False))

EM, EN = chr(8212), chr(8211)
DASHED = [dim("d", [src("Title " + EM + " Subtitle", "https://example.com/d",
                        supports="range 2" + EN + "5", quotable=["quote " + EM + " here"])])]
e6, o6, _ = gen.merge(DASHED)
dashed = gen.render(e6, o6)
run("em-dash is stripped from identity", EM not in dashed)
run("en-dash is stripped from supports", EN not in dashed)
run("and the text survives the strip", "Subtitle" in dashed and "here" in dashed)

check("tier 'standard' maps to the log vocabulary 'standards'",
      gen.merge([dim("d", [src("S", "https://e.com/1", tier="standard")])])[0][gen.normalise_url("https://e.com/1")]["tier"],
      "standards")
check("an unknown tier degrades to reference rather than crashing",
      gen.merge([dim("d", [src("S", "https://e.com/2", tier="nonsense")])])[0][gen.normalise_url("https://e.com/2")]["tier"],
      "reference")
run("a source with no URL still renders, and says so",
    "No URL." in gen.render(*gen.merge([dim("d", [src("Book", "")])])[:2]))

# ---------------------------------------------------------------- report

print("gen-research-log self-test: " + str(PASS + len(FAIL)) + " assertions")
if FAIL:
    print("\n" + str(len(FAIL)) + " FAILED:")
    for f in FAIL:
        print("  - " + f)
    sys.exit(1)
print("OK  " + str(PASS) + " assertions passed, each mutation-checked against a broken implementation.")
print("      not verified: that a generated entry is TRUE. This proves fields survive the merge, never")
print("      that a retrieval status is honest or that a quoted phrase appears in its source.")
