#!/usr/bin/env python3
"""
test-check-research-logs.py - the adversarial test for the research-log contract check.

WHAT THIS COVERS, AND WHAT IT DOES NOT.
This tests `check-research-logs.py` and nothing else. It proves the check accepts each legal
layout and, far more importantly, that it FAILS on each way an entry can breach the contract.
It does not prove any research log is honest; nothing mechanical can. Read a green run as
"the contract check works", never as "the research is sound".

WHY IT EARNED A TEST (ADR 0025).
Most of the failure branches have no live subject once the tree is clean: no bundle ships a
missing tier, an invalid status token, or a URL-less entry without its exemption, and none
should. A check that has never been observed failing is an assumption, not a check. Each
negative case asserts on the message text, because a failure that does not name the entry and
the missing field costs the next author the same investigation twice.

The fixtures are deliberately minimal: the smallest text that is a legal entry, mutated one
field at a time, so a failure names exactly one cause.

Pure standard library, no framework, no dependencies. Runs in CI alongside the gate.
Usage: python tools/test-check-research-logs.py
"""
import importlib.util
import os
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
CHECK = os.path.join(SCRIPT_DIR, "check-research-logs.py")

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

spec = importlib.util.spec_from_file_location("check_research_logs", CHECK)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

results = []


def check(label, passed, detail=""):
    results.append(passed)
    mark = GREEN + "PASS" + OFF if passed else RED + "FAIL" + OFF
    print("  " + mark + "  " + label)
    if not passed and detail:
        print("        got: " + detail)


def run(body, bundle="fixture"):
    """Write a throwaway log and return the check's problem list."""
    fd, path = tempfile.mkstemp(suffix="_research-log.md")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(body)
    try:
        return checker.check_log(bundle, path)
    finally:
        os.unlink(path)


def says(problems, *fragments):
    """True when some problem mentions every fragment."""
    return any(all(fr.lower() in p.lower() for fr in fragments) for p in problems)


HEADER = "# Research log: fixture\n\n## Sources\n\n"

# The smallest legal entry in each layout. Every negative fixture below is one of these with
# exactly one field damaged.
PROSE = (
    "**[1] Ada Lovelace - On the Analytical Engine.** primary. **fetched-and-verified.**\n"
    "`https://example.org/notes`\n"
    "Supports: the worked example.\n"
)
LIST = (
    '1. **[Tier 1] Lovelace, Ada. "On the Analytical Engine."** https://example.org/notes'
    " - **fetched-and-verified** - Supports: the worked example.\n"
)


def prose(*entries):
    return HEADER + "\n".join(entries)


print("\nLegal layouts are accepted\n")

check("a numbered prose entry with every field passes",
      run(prose(PROSE)) == [], str(run(prose(PROSE))))

check("a numbered list entry with every field passes",
      run(prose(LIST)) == [], str(run(prose(LIST))))

check("both layouts in sequence still pass entry by entry",
      run(prose(PROSE, PROSE.replace("[1]", "[2]"))) == [],
      str(run(prose(PROSE, PROSE.replace("[1]", "[2]")))))

print("\nA missing required field fails, and the message names it\n")

no_tier = PROSE.replace(" primary.", "")
check("missing tier fails",
      says(run(prose(no_tier)), "1", "tier"), str(run(prose(no_tier))))

no_status = PROSE.replace("**fetched-and-verified.**", "")
check("missing retrieval status fails",
      says(run(prose(no_status)), "1", "retrieval status"), str(run(prose(no_status))))

bad_status = PROSE.replace("fetched-and-verified", "fetched and verified")
check("a retrieval status outside the enum fails (prose form is not a token)",
      says(run(prose(bad_status)), "1", "retrieval status"), str(run(prose(bad_status))))

near_miss = PROSE.replace("fetched-and-verified", "not retrieved")
check("`not retrieved` fails where the token is `not-retrieved` (the bug-report [17] defect)",
      says(run(prose(near_miss)), "1", "retrieval status"), str(run(prose(near_miss))))

no_supports = PROSE.replace("Supports: the worked example.", "It is interesting.")
check("missing Supports clause fails",
      says(run(prose(no_supports)), "1", "supports"), str(run(prose(no_supports))))

no_identity = "**[1]** primary. **fetched-and-verified.**\n`https://example.org/x`\nSupports: x.\n"
check("an entry naming no author, organisation or title fails",
      says(run(prose(no_identity)), "1", "identit"), str(run(prose(no_identity))))

print("\nThe URL rule, and the print-source exemption it carves out\n")

no_url = PROSE.replace("`https://example.org/notes`\n", "")
check("an entry with no URL and no stated reason fails",
      says(run(prose(no_url)), "1", "url"), str(run(prose(no_url))))

exempt = (
    "**[1] Douglas W. Hubbard - The Failure of Risk Management (Wiley, 2009).** primary (book)."
    " **not-retrieved.**\n"
    "No URL, deliberately: this is a print book that was not fetched, identified by publisher and\n"
    "year rather than by link. Inventing a bookseller URL would add the appearance of retrieval\n"
    "without the fact of it.\n"
    "Supports: the book-length argument.\n"
)
check("a URL-less entry that states the absence and why passes (risk-register [33])",
      run(prose(exempt)) == [], str(run(prose(exempt))))

hollow = no_url.replace("Supports:", "No URL.\nSupports:")
check("`No URL.` alone does not buy the exemption; a reason is required",
      says(run(prose(hollow)), "1", "url"), str(run(prose(hollow))))

print("\nNumbering is contiguous and unique\n")

gap = prose(PROSE, PROSE.replace("[1]", "[2]"), PROSE.replace("[1]", "[4]"))
check("a gap in the numbering fails and names the missing number",
      says(run(gap), "3"), str(run(gap)))

dup = prose(PROSE, PROSE.replace("[1]", "[2]"), PROSE.replace("[1]", "[2]"))
check("a duplicate number fails and names it",
      says(run(dup), "duplicate", "2"), str(run(dup)))

start = prose(PROSE.replace("[1]", "[0]"), PROSE.replace("[1]", "[1]"))
check("numbering that does not start at 1 fails",
      says(run(start), "1"), str(run(start)))

print("\nA log the check cannot read fails; it never passes by finding nothing\n")

empty = HEADER + "We consulted several sources and they were good.\n"
check("a log with no parseable entries FAILS rather than reporting nothing to check",
      says(run(empty), "no source entries"), str(run(empty)))

subsections = HEADER + "### Origins\n\nSome prose about origins, with no numbered entries.\n"
check("`###` grouping with no numbered entries FAILS",
      says(run(subsections), "no source entries"), str(run(subsections)))

print("\nThe tier vocabulary is the one the tree actually uses\n")

for word in ["primary", "practitioner", "vendor", "reference", "standards", "academic", "internal"]:
    body = PROSE.replace(" primary.", " " + word + ".")
    check("tier `%s` is accepted" % word, run(prose(body)) == [], str(run(prose(body))))

for qualified in ["primary (book)", "reference (mirror)", "primary (custodian committee)"]:
    body = PROSE.replace(" primary.", " " + qualified + ".")
    check("tier `%s` is accepted, the qualifier carries meaning" % qualified,
          run(prose(body)) == [], str(run(prose(body))))

check("tier `[Tier 2]` is accepted in the list layout",
      run(prose(LIST.replace("[Tier 1]", "[Tier 2]"))) == [],
      str(run(prose(LIST.replace("[Tier 1]", "[Tier 2]")))))

invented = PROSE.replace(" primary.", " gold-plated.")
check("an invented tier word fails",
      says(run(prose(invented)), "1", "tier"), str(run(prose(invented))))

print("\nThe numbered-table layout stays legal for anyone who carries the contract in it\n")

TABLE = (
    "| # | Source | Tier | Retrieval | Claims it supports |\n"
    "|---|---|---|---|---|\n"
    '| 1 | Lovelace, Ada. "On the Analytical Engine." https://example.org/notes | primary |'
    " **fetched-and-verified** | the worked example |\n"
)
check("a table log carrying url, tier, enum status and a claims column passes",
      run(HEADER + TABLE) == [], str(run(HEADER + TABLE)))

table_no_url = TABLE.replace(" https://example.org/notes", "")
check("a table row with no URL fails",
      says(run(HEADER + table_no_url), "1", "url"), str(run(HEADER + table_no_url)))

table_prose_status = TABLE.replace("**fetched-and-verified**", "Fetched and verified 2026-07-16")
check("a table row whose retrieval column is prose rather than a token fails",
      says(run(HEADER + table_prose_status), "1", "retrieval status"),
      str(run(HEADER + table_prose_status)))

table_no_claims = TABLE.replace(" | the worked example |", " |  |")
check("a table row with an empty claims column fails",
      says(run(HEADER + table_no_claims), "1", "supports"), str(run(HEADER + table_no_claims)))

table_bad_header = TABLE.replace("| # | Source | Tier | Retrieval | Claims it supports |",
                                 "| # | Source | Tier | Notes |")
check("a numbered table whose header does not declare the contract columns fails",
      says(run(HEADER + table_bad_header), "header"), str(run(HEADER + table_bad_header)))

print("\nThe layout is a property of the file, not of the line\n")

notes_list = prose(PROSE) + "\n## Notes for the companion\n\n1. **Framing.** Lead with the negative.\n"
check("a numbered list in a notes section is not read as a malformed source",
      run(notes_list) == [], str(run(notes_list)))

check("and it is not counted as a source either",
      checker.count_entries(notes_list) == 1, str(checker.count_entries(notes_list)))

print("\nThe exemption list is real, dated, and cannot be silent\n")

check("an exempt bundle is skipped rather than checked",
      checker.is_exempt("adr") and not checker.is_exempt("risk-register"))

check("every exempt bundle carries a recorded reason",
      all(isinstance(r, str) and len(r) > 20 for r in checker.EXEMPT.values()),
      str(checker.EXEMPT))

check("the exemption list is exactly the six table-layout logs measured 2026-07-28",
      set(checker.EXEMPT) == {"acceptance-criteria", "adr", "prd", "release-notes", "rfc",
                              "user-stories"},
      str(sorted(checker.EXEMPT)))

print("\nEvery non-exempt log in the tree passes its own check\n")

for bundle, path in checker.logs_on_disk():
    if checker.is_exempt(bundle):
        continue
    problems = checker.check_log(bundle, path)
    check("%s passes" % bundle, problems == [], "; ".join(problems[:3]))

print()
failed = results.count(False)
if failed:
    print(RED + "FAIL" + OFF + "  %d of %d assertions failed." % (failed, len(results)))
    raise SystemExit(1)
print(GREEN + "OK" + OFF + "  %d assertions, the research-log contract holds." % len(results))
print(DIM + "      not proven here: that any retrieval status is truthful, that a Supports clause is"
      "\n      accurate, or that a quoted phrase appears in its source." + OFF)
