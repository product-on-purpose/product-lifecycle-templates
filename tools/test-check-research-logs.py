#!/usr/bin/env python3
"""
test-check-research-logs.py - the adversarial test for the research-log contract check.

WHAT THIS COVERS, AND WHAT IT DOES NOT.
This tests `check-research-logs.py` and nothing else. It proves the check accepts each legal layout
and, far more importantly, that it FAILS on each way an entry can breach the contract. It does not
prove any research log is honest; nothing mechanical can. Read a green run as "the contract check
works", never as "the research is sound".

WHY IT EARNED A TEST (ADR 0025).
Most failure branches have no live subject once the tree is clean. A check that has never been
observed failing is an assumption, not a check.

WHY IT IS SHAPED THIS WAY.
An earlier version of this file reported 49 passing assertions against a checker an adversarial
review then broke nine different ways. The review's diagnosis was that the assertions were
non-exclusive: they asked whether SOME problem mentioned a fragment, never whether the problem list
was right, so a checker that missed a defect entirely still passed. Two rules came out of it and are
enforced here:

  * every negative case asserts the EXACT number of problems, via `fails()`, so a check that reports
    the right complaint for the wrong reason, or reports extra spurious complaints, fails the test;
  * every case in the review's reproduction list appears below as a regression fixture, including
    the ones that were false POSITIVES, because a gate that fails correct work is its own defect.

Fixtures use `check_text()` directly. The previous version wrote temp files, which made the suite
unrunnable in a read-only sandbox and tested the filesystem rather than the contract.

Pure standard library, no framework, no dependencies. Runs in CI alongside the gate.
Usage: python tools/test-check-research-logs.py
"""
import importlib.util
import io
import os
import sys

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


def passes(label, text):
    """The contract holds: NO problems at all, not merely no problem of one kind."""
    problems = checker.check_text(text)
    check(label, problems == [], "; ".join(problems) or "(none)")


def fails(label, text, fragment, count=1):
    """Exactly `count` problems, and one of them names `fragment`.

    The count is the part that matters. Asserting only that some message mentions a word lets a
    checker pass by complaining about the wrong thing.
    """
    problems = checker.check_text(text)
    ok = len(problems) == count and any(fragment.lower() in p.lower() for p in problems)
    check(label, ok, "%d problem(s): %s" % (len(problems), "; ".join(problems) or "(none)"))


HEADER = "# Research log: fixture\n\n## Sources\n\n"

PROSE = (
    "**[1] Ada Lovelace - On the Analytical Engine.** primary. **fetched-and-verified.**\n"
    "`https://example.org/notes`\n"
    "Supports: the worked example.\n"
)
LIST = (
    '1. **[Tier 1] Lovelace, Ada. "On the Analytical Engine."** https://example.org/notes'
    " - **fetched-and-verified** - Supports: the worked example.\n"
)
TABLE = (
    "| # | Source | Tier | Retrieval | Claims it supports |\n"
    "|---|---|---|---|---|\n"
    '| 1 | Lovelace, Ada. "On the Analytical Engine." https://example.org/notes | primary |'
    " **fetched-and-verified** | the worked example |\n"
)


def log(*entries):
    return HEADER + "\n".join(entries)


def renumber(entry, n, same_source=False):
    """Entry `n`, naming a DIFFERENT source unless the caller wants the repeat.

    Distinct identities matter: one source, one entry is part of the contract, so a fixture that
    pastes the same source twice is testing the duplicate rule whether it meant to or not.
    """
    out = entry.replace("[1]", "[%d]" % n).replace("1. **", "%d. **" % n, 1)
    if not same_source:
        out = out.replace("Ada Lovelace - On the Analytical Engine",
                          "Author %d - Work %d" % (n, n))
        out = out.replace('Lovelace, Ada. "On the Analytical Engine."',
                          'Author %d. "Work %d."' % (n, n))
    return out


print("\nEach legal layout is accepted\n")

passes("numbered prose with every field", log(PROSE))
passes("numbered list with every field", log(LIST))
passes("numbered table with every field", HEADER + TABLE)
passes("two prose entries in sequence", log(PROSE, renumber(PROSE, 2)))
passes("two list entries in sequence", log(LIST, renumber(LIST, 2)))
passes("a url-confirmed-not-read status", log(PROSE.replace("fetched-and-verified",
                                                            "url-confirmed-not-read")))
passes("a status qualified around the token, which is the more honest record",
       log(PROSE.replace("**fetched-and-verified.**",
                         "**landing page fetched-and-verified; the PDF itself was not read.**")))

print("\nA field must be in its own place, not merely somewhere in the entry\n")

fails("a status inside a quotation is not the entry's status",
      log("**[1] Ada Lovelace - On the Analytical Engine.** primary.\n"
          "`https://example.org/notes`\n"
          'Quotable: "fetched-and-verified is the archive label."\n'
          "Supports: x.\n"), "retrieval status")

fails("a status in a legend line is not the entry's status",
      log(PROSE.replace("**fetched-and-verified.**", "") +
          "Retrieval legend: fetched-and-verified means read in full.\n"), "retrieval status")

fails("a tier word inside the title does not satisfy an empty tier cell",
      HEADER + TABLE.replace("| primary |", "|  |").replace("Lovelace, Ada.",
                                                            "Lovelace, Ada. Primary Guide."),
      "tier")

fails("a status in the wrong table cell does not satisfy the retrieval column",
      HEADER + TABLE.replace("| **fetched-and-verified** |", "|  |")
                    .replace("On the Analytical Engine.", "The fetched-and-verified Guide."),
      "retrieval status")

fails("`not-retrieved-ish` is not `not-retrieved`",
      log(PROSE.replace("fetched-and-verified", "not-retrieved-ish")), "retrieval status")

fails("`fetched and verified` prose is not the token",
      log(PROSE.replace("fetched-and-verified", "fetched and verified")), "retrieval status")

fails("`not retrieved` fails where the token is `not-retrieved` (the bug-report [17] defect)",
      log(PROSE.replace("fetched-and-verified", "not retrieved")), "retrieval status")

fails("two different status tokens in one field is ambiguous",
      log(PROSE.replace("**fetched-and-verified.**",
                        "**fetched-and-verified and not-retrieved.**")), "retrieval status")

fails("an entry with no identity at all fails",
      log("**[1]** primary. **fetched-and-verified.**\n`https://example.org/n`\nSupports: x.\n"),
      "identity")

fails("a stub identity fails",
      log(PROSE.replace("Ada Lovelace - On the Analytical Engine.", "Ada.")), "identity")

passes("an author-only identity PASSES, and the run says identity completeness is unchecked",
       log(PROSE.replace("Ada Lovelace - On the Analytical Engine.", "Ada Lovelace, 1843.")))

print("\nThe Supports clause must be a labelled clause with a value\n")

fails("a substring of another word is not a Supports clause",
      log(PROSE.replace("Supports: the worked example.", "This presupportscondition is noted.")),
      "supports")

fails("an empty Supports clause fails",
      log(PROSE.replace("Supports: the worked example.", "Supports:")), "supports")

passes("`Supports: nothing in this bundle` is a real answer",
       log(PROSE.replace("Supports: the worked example.",
                         "Supports: nothing in this bundle; listed because it was consulted.")))

fails("an empty claims column in a table fails",
      HEADER + TABLE.replace("| the worked example |", "|  |"), "supports")

print("\nThe URL rule, and the print-source exemption it carves out\n")

no_url = PROSE.replace("`https://example.org/notes`\n", "")

fails("no url and no stated reason fails", log(no_url), "url")

passes("the worked risk-register [33] form passes",
       log(no_url.replace("Supports:",
                          "No URL, deliberately: this is a print book that was not fetched,\n"
                          "identified by publisher and year rather than by link.\nSupports:")))

passes("a concise reason is enough; the contract never asked for a word count",
       log(no_url.replace("Supports:", "No URL: print-only book.\nSupports:")))

passes("`No URL because ...` reads as well as `No URL: ...`",
       log(no_url.replace("Supports:", "No URL because it is a print-only book.\nSupports:")))

passes("a four-word reason passes; the contract set no word count",
       log(no_url.replace("Supports:", "No URL because it is print-only.\nSupports:")))

fails("the reason must be on its own line, not borrowed from the Supports clause below it",
      log(no_url.replace("Supports:", "No URL: " + "-" * 40 + "\nSupports:")), "url")

fails("`No URL.` alone does not buy the exemption",
      log(no_url.replace("Supports:", "No URL.\nSupports:")), "url")

fails("forty characters of punctuation is not a reason",
      log(no_url.replace("Supports:", "No URL: " + "." * 40 + "\nSupports:")), "url")

print("\nNumbering is contiguous, unique, and in document order\n")

fails("a gap in the numbering names the missing number",
      log(PROSE, renumber(PROSE, 2), renumber(PROSE, 4)), "missing: 3")

fails("a duplicate number is named",
      log(PROSE, renumber(PROSE, 2), renumber(PROSE, 3).replace("[3]", "[2]")),
      "duplicate number")

fails("numbering that does not start at 1 says so",
      log(renumber(PROSE, 0), PROSE), "must start at 1")

fails("entries out of document order fail even though the set is contiguous",
      log(renumber(PROSE, 2), PROSE), "out of document order")

print("\nOne source, one entry\n")

fails("the same source under two numbers is a repeat",
      log(PROSE, renumber(PROSE, 2, same_source=True)), "repeats the source")

passes("a repeat that declares which entry it repeats is legal (sdd [10] and [13])",
       log(PROSE, renumber(PROSE, 2, same_source=True).replace(
           "On the Analytical Engine.**",
           "On the Analytical Engine (the same page as source 1).**")))

print("\nSource entries are read from the sources section, not from anywhere in the file\n")

passes("a numbered notes list after the sources section is not a source",
       log(PROSE) + "\n## Notes for the companion\n\n1. **Framing.** Lead with the negative.\n"
       "2. **Risk.** Low.\n")

passes("an incidental numbered table after the sources section is not a source table",
       log(PROSE) + "\n## Notes\n\n| # | Topic |\n|---|---|\n| 1 | Coverage |\n")

check("and neither is counted as a source",
      checker.count_entries(log(PROSE) + "\n## Notes\n\n| # | Topic |\n|---|---|\n| 1 | x |\n") == 1,
      str(checker.count_entries(log(PROSE) + "\n## Notes\n\n| # | Topic |\n|---|---|\n| 1 | x |\n")))

fails("a file with no sources heading fails rather than passing empty",
      "# Research log\n\n## Notes\n\nWe read some things.\n", "no section heading names the sources")

fails("a sources section with no numbered entries fails",
      HEADER + "We consulted several sources and they were good.\n", "no source entries")

fails("`###` grouping with no numbered entries fails",
      HEADER + "### Origins\n\nSome prose about origins.\n", "no source entries")

print("\nMixed layouts are reported, never silently resolved by counting\n")

mixed = log(PROSE) + "\n2. **Broken Source.**\n"
problems = checker.check_text(mixed)
check("a stray list entry beside prose is reported, not discarded",
      any("mixed source layouts" in p for p in problems), "; ".join(problems) or "(none)")
check("and the stray entry is still validated rather than dropped",
      any("entry 2" in p for p in problems), "; ".join(problems) or "(none)")

print("\nA fenced excerpt inside an entry is quoted text, not structure\n")

fenced = log("**[1] Ada Lovelace - On the Analytical Engine.** primary. **fetched-and-verified.**\n"
             "```text\n# a quoted heading\n```\n"
             "`https://example.org/notes`\nSupports: the worked example.\n")
passes("a heading inside a fence does not truncate the entry", fenced)

print("\nThe table is validated through its header, so legal variation is not a defect\n")

passes("column synonyms are accepted",
       HEADER + TABLE.replace("| # | Source | Tier | Retrieval | Claims it supports |",
                              "| # | Identity | Tier | Retrieval | Supports |"))

passes("extra and reordered columns are accepted",
       HEADER
       + "| # | Note | Source | Tier | Retrieval | Claims it supports |\n"
       + "|---|---|---|---|---|---|\n"
       + '| 1 | x | Lovelace, Ada. "Engine." https://example.org/n | primary |'
       + " **fetched-and-verified** | the worked example |\n")

fails("a numbered table whose header declares no contract columns fails",
      HEADER + "| # | Topic | Note |\n|---|---|---|\n| 1 | x | y |\n", "header")

print("\nThe tier vocabulary is the documented one, and only that\n")

for word in ["primary", "practitioner", "vendor", "reference", "standards", "academic", "internal"]:
    passes("tier `%s`" % word, log(PROSE.replace(" primary.", " " + word + ".")))

for qualified in ["primary (book)", "reference (mirror)", "primary (custodian committee)"]:
    passes("tier `%s`, the qualifier carries meaning" % qualified,
           log(PROSE.replace(" primary.", " " + qualified + ".")))

passes("tier `[Tier 2]` in the list layout", log(LIST.replace("[Tier 1]", "[Tier 2]")))
fails("an invented tier word fails", log(PROSE.replace(" primary.", " gold-plated.")), "tier")

print("\nThe exemption list is real, dated, and cannot be silent\n")

check("an exempt bundle is skipped and a checked one is not",
      checker.is_exempt("adr") and not checker.is_exempt("risk-register"))

check("the exemption list is exactly the six table-layout logs measured 2026-07-28",
      set(checker.EXEMPT) == {"acceptance-criteria", "adr", "prd", "release-notes", "rfc",
                              "user-stories"}, str(sorted(checker.EXEMPT)))

captured = io.StringIO()
saved, sys.stdout = sys.stdout, captured
try:
    exit_code = checker.main(["check-research-logs.py"])
finally:
    sys.stdout = saved
output = captured.getvalue()

check("main() exits 0 on the real tree", exit_code == 0, str(exit_code))
check("main() names every exempt bundle in its output",
      all(b in output for b in checker.EXEMPT), output[-200:])
check("main() calls the exemption a skip, not a pass", "SKIP" in output and "NOT checked" in output,
      output[-200:])
check("main() prints what it does not verify, every run",
      "not verified" in output and "truthful" in output, output[-200:])
check("main() names URL ownership as out of scope rather than implying it is checked",
      "belongs to the source" in output, output[-300:])
check("main() reports the source count", "344 source(s)" in output or "source(s)" in output,
      output[:120])

print("\nEvery non-exempt log in the tree passes its own check\n")

for bundle, path in checker.logs_on_disk():
    if checker.is_exempt(bundle):
        continue
    problems = checker.check_log(bundle, path)
    check("%s" % bundle, problems == [], "; ".join(problems[:3]))

print()
failed = results.count(False)
if failed:
    print(RED + "FAIL" + OFF + "  %d of %d assertions failed." % (failed, len(results)))
    raise SystemExit(1)
print(GREEN + "OK" + OFF + "  %d assertions, the research-log contract holds." % len(results))
print(DIM + "      not proven here: that any retrieval status is truthful, that a Supports clause is"
      "\n      accurate, that a quoted phrase appears in its source, or that a URL belongs to the"
      "\n      source it sits with. Those need a reader, not a regex." + OFF)
