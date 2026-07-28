#!/usr/bin/env python3
"""
check-research-logs.py - every source in every research log carries the retrieval contract.

WHY THIS EXISTS (ADR 0029).
The honest-retrieval standard is this library's central quality claim: a source is tagged with how
it was actually retrieved, and only a `fetched-and-verified` source may be quoted verbatim. That
requirement was written into the research workflow's JSON schema, which constrains what the research
agents RETURN. It said nothing about the markdown log a human then writes from those returns, and
nothing downstream re-checked it. Sixteen bundles shipped without it being verified once.

WHAT IS GATED, AND WHAT IS NOT.
Gated, per source: a contiguous unique number, an identity (author or organisation, and a title), a
URL or an explicit statement of why there is none, a tier, a retrieval status from the enum, and a
`Supports:` clause. Three layouts are legal, because the contract is what matters and not its
presentation: numbered prose entries, numbered list entries, and the numbered table.

NOT gated, stated plainly and printed on every run: whether a retrieval status is TRUTHFUL, whether
a `Supports:` clause is ACCURATE, or whether a quoted phrase appears in its source. A source
mislabelled `fetched-and-verified` passes here. This narrows the failure surface from "anything" to
"deliberate or careless mislabelling"; the adversarial review remains the only thing that catches
the rest.

THE EXEMPTION LIST IS THE HONEST PART.
Six bundles use a table layout that carries no URL for any source and no enum retrieval token. That
was measured, not assumed: 0 of 86 sources. They are exempt BY NAME with a reason and a date, rather
than the contract being weakened until they happen to pass, because a URL cannot be invented and a
retrieval status cannot be claimed for a fetch nobody performed. Every run prints what it skipped.

Pure standard library. Runs in CI alongside the gate.
Usage: python tools/check-research-logs.py [bundle ...]
"""
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
TEMPLATES = os.path.join(ROOT, "templates")

GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"

# The retrieval enum, from bundle-pipeline.md phase 1. These are tokens, not prose: the hyphens are
# the point. `bug-report` [17] shipped "not retrieved" where the token is "not-retrieved", which is
# exactly the class of defect a token check catches and a prose check does not.
STATUSES = ("fetched-and-verified", "url-confirmed-not-read", "not-retrieved")

# The tier vocabulary the tree actually uses, enumerated 2026-07-28 across all 430 sources rather
# than assumed from the phase 1 schema, which names only four. The counts were: practitioner 103,
# primary 52, vendor 49, reference 30, standards 10, academic 3. Enforcing the four-word enum would
# have failed 13 correct entries, which is the audit mistake this project has already made once:
# verify the rule before enforcing it. A parenthetical qualifier is free and carries meaning worth
# keeping, so `primary (book)`, `reference (mirror)` and `primary (custodian committee)` all pass.
# The list layout writes the tier as `[Tier N]` instead.
# `internal` is in ADR 0029's contract table and in no entry in the tree. It is accepted anyway: the
# written standard is the rule, and a checker stricter than the standard is the 76-defect mistake.
TIERS = ("primary", "practitioner", "vendor", "reference", "standards", "academic", "internal")
TIER_MARKER = re.compile(r"\[tier\s*\d\]", re.I)

# A URL-less entry passes only if it says so and says why. `No URL.` alone does not buy it; the
# worked form is risk-register [33] (Hubbard), a print book identified by publisher and year.
URL_EXEMPTION = re.compile(r"no url\b\s*[,:]\s*(.{40,})", re.I | re.S)

PROSE_ENTRY = re.compile(r"^\*\*\[(\d+)\]")        # **[7] Author - Title.** tier. **status.**
LIST_ENTRY = re.compile(r"^(\d+)\.\s+\*\*")        # 7. **[Tier 2] Author. "Title."** url - status
TABLE_ROW = re.compile(r"^\|\s*(\d+)\s*\|")        # | 7 | Source | Tier | Retrieval | Claims |
TABLE_HEADER = re.compile(r"^\|\s*#\s*\|", re.M)

# Measured 2026-07-28 against every source in each file. These six carry no URL and no enum
# retrieval token for ANY source; the retrieval column is prose ("Fetched and verified 2026-07-16",
# "BLOCKED. HTTP 403"). Backfilling them means finding and fetching 85 sources again, so they are
# named here and tracked, not silently tolerated and not hidden by a weaker contract.
EXEMPT = {
    "acceptance-criteria": "table layout, 9 of 10 sources carry no URL and none carries an enum token",
    "adr": "table layout, 0 of 22 sources carry a URL and none carries an enum token",
    "prd": "table layout, 0 of 12 sources carry a URL and none carries an enum token",
    "release-notes": "table layout, 0 of 10 sources carry a URL and none carries an enum token",
    "rfc": "table layout, 0 of 20 sources carry a URL and none carries an enum token",
    "user-stories": "table layout, 0 of 12 sources carry a URL and none carries an enum token",
}


def is_exempt(bundle):
    return bundle in EXEMPT


def logs_on_disk():
    """Every <type>_research-log.md under templates/, as (bundle, path)."""
    out = []
    if not os.path.isdir(TEMPLATES):
        return out
    for bundle in sorted(os.listdir(TEMPLATES)):
        d = os.path.join(TEMPLATES, bundle)
        if not os.path.isdir(d) or bundle.startswith((".", "_")):
            continue
        path = os.path.join(d, bundle + "_research-log.md")
        if os.path.isfile(path):
            out.append((bundle, path))
    return out


def _blocks(lines, pattern):
    """Entries as (number, text), each running to the next entry or the next heading."""
    starts = [i for i, line in enumerate(lines) if pattern.match(line)]
    out = []
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        body = [lines[start]]
        for line in lines[start + 1:end]:
            if line.startswith("#"):
                break
            body.append(line)
        out.append((int(pattern.match(lines[start]).group(1)), "\n".join(body)))
    return out


def _identity(body):
    """The bolded lead of an entry, minus any [n] or [Tier n] marker. Empty means no identity.

    Matched across the whole entry, not its first line: a long title wraps, so the closing `**`
    routinely sits on the line below. Reading only the first line reported five correct entries as
    identity-less, which is the same false-positive class the 76-defect audit produced.
    """
    m = re.search(r"\*\*(.+?)\*\*", body, re.S)
    if not m:
        return ""
    return re.sub(r"^\s*\[[^\]]*\]\s*", "", m.group(1)).strip()


def _numbering_problems(numbers):
    problems = []
    seen = set()
    for n in numbers:
        if n in seen:
            problems.append("entry %d: duplicate number" % n)
        seen.add(n)
    ordered = sorted(seen)
    if ordered and ordered[0] != 1:
        problems.append("numbering starts at %d, must start at 1" % ordered[0])
    if ordered:
        missing = [n for n in range(1, ordered[-1] + 1) if n not in seen]
        if missing:
            problems.append("numbering is not contiguous, missing: "
                            + ", ".join(str(n) for n in missing))
    return problems


def _entry_problems(num, body, cells=None):
    """The contract, one entry at a time. `cells` is the split row for the table layout."""
    problems = []
    low = body.lower()

    if cells is None:
        identity = _identity(body)
    else:
        identity = cells[1].strip() if len(cells) > 1 else ""
    if len(identity) < 3:
        problems.append("entry %d: no identity (name an author or organisation, and a title)" % num)

    if "http://" not in low and "https://" not in low:
        if not URL_EXEMPTION.search(body):
            problems.append(
                "entry %d: no url, and no stated reason for its absence "
                "(a print source states the absence and why; see risk-register [33])" % num)

    if not any(t in low for t in TIERS) and not TIER_MARKER.search(body):
        problems.append("entry %d: no tier (%s, or [Tier n])" % (num, ", ".join(TIERS)))

    if not any(s in low for s in STATUSES):
        problems.append("entry %d: no retrieval status token (%s)" % (num, ", ".join(STATUSES)))

    if cells is None:
        if "supports" not in low:
            problems.append("entry %d: no Supports clause" % num)
    elif len(cells) < 5 or not cells[4].strip():
        problems.append("entry %d: empty claims column, so it supports nothing on the record" % num)

    return problems


def _select_layout(text):
    """(prose, listed, rows) with the losing layouts emptied.

    A log is written in ONE layout. Taking whichever pattern matches most decides it, which matters
    because a prose log routinely contains numbered lists in its notes sections and an earlier draft
    of this check read those as malformed sources, and then counted them as sources. The layout is a
    property of the file, not of the line.
    """
    lines = text.splitlines()
    prose = _blocks(lines, PROSE_ENTRY)
    listed = _blocks(lines, LIST_ENTRY)
    rows = [(int(TABLE_ROW.match(l).group(1)), l) for l in lines if TABLE_ROW.match(l)]

    if len(prose) >= len(listed):
        listed = []
    else:
        prose = []
    if rows and len(rows) < max(len(prose), len(listed)):
        rows = []
    return prose, listed, rows


def count_entries(text):
    """How many sources this log declares, after the layout is settled."""
    prose, listed, rows = _select_layout(text)
    return len(prose) + len(listed) + len(rows)


def check_log(bundle, path):
    """Every problem in one research log. An empty list means the contract holds."""
    text = open(path, encoding="utf-8").read()
    prose, listed, rows = _select_layout(text)

    problems = []
    entries = []

    if rows:
        header = TABLE_HEADER.search(text)
        header_line = text[header.start():text.index("\n", header.start())] if header else ""
        needed = ("source", "tier", "retrieval", "supports")
        if not all(word in header_line.lower() for word in needed):
            problems.append("numbered table header does not declare the contract columns "
                            "(# | Source | Tier | Retrieval | Claims it supports), got: "
                            + (header_line.strip() or "no header row"))
        for num, line in rows:
            cells = [c for c in line.split("|")][1:]
            entries.append(num)
            problems += _entry_problems(num, line, cells)
    elif prose or listed:
        for num, body in prose + listed:
            entries.append(num)
            problems += _entry_problems(num, body)
    else:
        problems.append("no source entries found. A research log must number its sources in one of "
                        "the three legal layouts (numbered prose, numbered list, numbered table); "
                        "prose grouped under headings carries no contract a checker can read")

    problems += _numbering_problems(entries)
    return problems


def main(argv):
    wanted = set(argv[1:])
    logs = [(b, p) for b, p in logs_on_disk() if not wanted or b in wanted]

    if not logs:
        print(RED + "FAIL" + OFF + "  no research logs found under templates/")
        return 1

    checked, skipped, failed, sources = 0, [], 0, 0
    for bundle, path in logs:
        if is_exempt(bundle):
            skipped.append(bundle)
            continue
        problems = check_log(bundle, path)
        checked += 1
        sources += count_entries(open(path, encoding="utf-8").read())
        if problems:
            failed += 1
            print(RED + "FAIL" + OFF + "  %s" % bundle)
            for p in problems:
                print("        " + p)

    print("\nresearch-log contract: %d log(s) checked, %d source(s)" % (checked, sources))

    # A check that finds no subject must say so rather than pass. The exemption is louder than the
    # green line it sits next to, on purpose.
    if skipped:
        print(YELLOW + "SKIP" + OFF + "  %d log(s) exempt, NOT checked (ADR 0029, measured 2026-07-28):"
              % len(skipped))
        for bundle in skipped:
            print("        %-20s %s" % (bundle, EXEMPT[bundle]))
        print("        These are tracked debt, not a pass. Backfilling them means re-fetching each")
        print("        source, because a URL cannot be invented and a status cannot be claimed.")

    if failed:
        print("\n" + RED + "FAIL" + OFF + "  %d log(s) breach the contract." % failed)
        return 1

    print(GREEN + "OK" + OFF + "  every source in every checked log carries the retrieval contract.")
    print(DIM + "      not verified: whether a retrieval status is truthful, whether a Supports"
          "\n      clause is accurate, or whether a quoted phrase appears in its source." + OFF)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
