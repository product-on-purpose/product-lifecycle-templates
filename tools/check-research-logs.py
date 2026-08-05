#!/usr/bin/env python3
"""
check-research-logs.py - every source in every research log carries the retrieval contract.

WHY THIS EXISTS (ADR 0029).
The honest-retrieval standard is this library's central quality claim: a source is tagged with how it
was actually retrieved, and only a `fetched-and-verified` source may be quoted verbatim. That
requirement was written into the research workflow's JSON schema, which constrains what the research
agents RETURN. It said nothing about the markdown log a human then writes from those returns, and
nothing downstream re-checked it. Sixteen bundles shipped without it being verified once.

HOW IT READS A LOG, AND WHY THAT MATTERS.
Fields are read FROM THEIR OWN POSITION IN THE ENTRY GRAMMAR, never found loose in the block. An
earlier draft of this check asked "does the token `fetched-and-verified` appear anywhere in these
lines", which passed a log whose status sat in a quotation, in a legend, in the title, or in the
wrong table column, and passed `not-retrieved-ish` as if it were `not-retrieved`. An adversarial
review reproduced nine such false negatives against a green run. A gate that green-lights a broken
log is worse than no gate, because it converts an unknown into a false assurance.

Source entries are also read only from sections whose heading names sources. Counting markdown shapes
across a whole file let a notes list outvote the real sources and made the check validate the wrong
thing entirely.

WHAT IS GATED, per source: a contiguous unique number in document order, an identity, a URL or an
explicit stated reason for its absence, a tier from the documented vocabulary, a retrieval status
that is EXACTLY one of the three enum tokens, and a non-empty `Supports:` clause. Three layouts are
legal, because the contract is what matters and not its presentation.

WHAT IS NOT GATED, stated plainly and printed on every run:
  - whether a retrieval status is TRUTHFUL. A source mislabelled `fetched-and-verified` passes.
  - whether a `Supports:` clause is ACCURATE, or whether a quoted phrase appears in its source.
  - whether a URL BELONGS to the source it sits with. Nothing mechanical can tell that a link points
    at the cited work rather than at something else; it needs a source registry this library does not
    have. Named here rather than left implied by a green run.
  - whether an identity carries BOTH an author and a title. Real correct entries name a document
    whose author is the organisation itself (`The Scrum Guide (November 2020)`), so requiring both
    would fail correct work, which is the 76-defects-against-2 mistake this repository already made.

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
# the point. `bug-report` [17] shipped "not retrieved" where the token is "not-retrieved". Matched by
# full equality after the field is extracted, so `not-retrieved-ish` fails as it should.
STATUSES = ("fetched-and-verified", "url-confirmed-not-read", "not-retrieved")

# The tier vocabulary, enumerated 2026-07-28 across all 430 sources rather than assumed from the
# phase 1 schema, which names four: practitioner 103, primary 52, vendor 49, reference 30,
# standards 10, academic 3. `internal` is in ADR 0029's contract table and in no entry; accepted
# anyway, because the written standard is the rule. A parenthetical qualifier carries meaning worth
# keeping, so `primary (book)` and `reference (mirror)` pass on their base word.
TIERS = ("primary", "practitioner", "vendor", "reference", "standards", "academic", "internal")

# A URL-less entry passes only if it says so AND says why, in words. The worked form is
# risk-register [33] (Hubbard), a print book identified by publisher and year. `No URL.` alone does
# not buy it, and neither does forty characters of punctuation: the reason must contain real words.
# The reason is read to the end of ITS OWN LINE. Reading further let the rest of the entry supply
# the words: forty characters of punctuation followed by a Supports clause passed, because the
# Supports clause was doing the talking.
URL_EXEMPTION = re.compile(r"no url\b\s*(?:[:,]|because|-)\s*(?P<reason>[^\n]+)", re.I)

# One source, one entry (methodology 6.1). The inverse breach, the same source under two numbers, is
# legal only when the later entry says so and names the entry it repeats.
CROSS_REFERENCE = re.compile(r"(?:same|as)\b[^.\n]{0,40}?\bsource\s+(\d+)", re.I)

SOURCE_HEADING = re.compile(r"^#{2,4}\s+.*\bsources?\b", re.I)
ANY_HEADING = re.compile(r"^#{1,6}\s")
FENCE = re.compile(r"^\s*(```|~~~)")

PROSE_ENTRY = re.compile(r"^\*\*\[(\d+)\]")        # **[7] Author - Title.** tier. **status.**
LIST_ENTRY = re.compile(r"^(\d+)\.\s+\*\*")        # 7. **[Tier 2] Author. "Title."** url - status
TABLE_ROW = re.compile(r"^\|\s*(\d+)\s*\|")        # | 7 | Source | Tier | Retrieval | Claims |
TABLE_HEADER = re.compile(r"^\|\s*(?:#|no\.?|num(?:ber)?)\s*\|", re.I)

# Column synonyms, so a legal table is not failed for saying Identity where this file said Source.
COLUMNS = {
    "identity": ("source", "identity", "citation", "reference", "work"),
    "tier": ("tier", "reliability"),
    "retrieval": ("retrieval", "status", "retrieval status"),
    "supports": ("supports", "claims", "claims it supports", "supported claims"),
}

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
    """Every <type>_research-log.md in a real bundle, as (bundle, path).

    A real bundle is a directory carrying <name>_meta.yaml, the same test check-bundles.py,
    gen-manifest.py and check-counts.py use. Four tools, one definition.

    They did not always agree. On 2026-08-04 a half-built business-case holding only its research log
    was counted by check-counts as a built Tier-1 type, reported by check-bundles as "no matching
    bundle", ignored by gen-manifest, and gated here. Three different answers to "is this a bundle",
    and the counts gate went red for something that was not a defect. During a long build run every
    partially-drafted bundle would do the same.

    NOTHING IS LOST by waiting for the meta. A bundle cannot merge without one: check A requires all
    eight files, so every research log is still gated before it reaches main. The only logs skipped are
    ones in directories that are work in progress, which is what they are.
    """
    out = []
    if not os.path.isdir(TEMPLATES):
        return out
    for bundle in sorted(os.listdir(TEMPLATES)):
        d = os.path.join(TEMPLATES, bundle)
        if not os.path.isdir(d) or bundle.startswith((".", "_")):
            continue
        if not os.path.isfile(os.path.join(d, bundle + "_meta.yaml")):
            continue
        path = os.path.join(d, bundle + "_research-log.md")
        if os.path.isfile(path):
            out.append((bundle, path))
    return out


def _outside_fences(lines):
    """(index, line) for lines outside fenced code blocks.

    A heading inside a fenced excerpt is quoted text, not a section boundary. Reading it as one
    truncated real entries and reported their URL and Supports clause as missing.
    """
    out, fence = [], None
    for i, line in enumerate(lines):
        m = FENCE.match(line)
        if m:
            if fence is None:
                fence = m.group(1)
            elif line.strip().startswith(fence):
                fence = None
            continue
        if fence is None:
            out.append((i, line))
    return out


def source_lines(text):
    """Lines belonging to sections whose heading names sources, fences excluded.

    Scoping to the sources section is what stops a notes list, or an incidental numbered table,
    from being counted as sources and outvoting the real ones.
    """
    lines = text.splitlines()
    live = _outside_fences(lines)
    keep, collecting, depth = [], False, 0
    for i, line in live:
        if ANY_HEADING.match(line):
            level = len(line) - len(line.lstrip("#"))
            if SOURCE_HEADING.match(line):
                collecting, depth = True, level
                continue
            if collecting and level <= depth:
                collecting = False
            continue
        if collecting:
            keep.append((i, line))
    return keep


def _entry_blocks(kept, pattern):
    """(number, body) per entry, each running to the next entry start."""
    starts = [n for n, (_, line) in enumerate(kept) if pattern.match(line)]
    out = []
    for k, s in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else len(kept)
        out.append((int(pattern.match(kept[s][1]).group(1)),
                    "\n".join(line for _, line in kept[s:e])))
    return out


def _split_prose(body):
    """(identity, tier, status) read from their positions in the prose grammar.

    `**[n] IDENTITY** TIER. **STATUS.**` - the identity is the first bold run, the tier is the text
    between it and the next bold run, and the status is that next bold run. Read positionally so a
    token in a quotation or a legend cannot stand in for the entry's own status.
    """
    m = re.match(r"^\*\*\[\d+\]\s*(?P<identity>.*?)\*\*(?P<tail>.*)", body, re.S)
    if not m:
        return "", "", ""
    tail = m.group("tail")
    status_m = re.search(r"\*\*\s*(?P<status>[^*]+?)\s*\*\*", tail, re.S)
    tier = tail[:status_m.start()] if status_m else tail
    status = status_m.group("status") if status_m else ""
    return m.group("identity").strip(), tier.strip(), status.strip()


def _split_list(body):
    """(identity, tier, status) for `7. **[Tier 2] IDENTITY** url - **STATUS** - Supports: ...`."""
    m = re.match(r"^\d+\.\s+\*\*(?P<bold>.*?)\*\*(?P<tail>.*)", body, re.S)
    if not m:
        return "", "", ""
    bold = m.group("bold")
    tier_m = re.match(r"\s*\[(?P<tier>[^\]]+)\]\s*(?P<identity>.*)", bold, re.S)
    tier = tier_m.group("tier") if tier_m else ""
    identity = (tier_m.group("identity") if tier_m else bold).strip()
    status_m = re.search(r"\*\*\s*(?P<status>[^*]+?)\s*\*\*", m.group("tail"), re.S)
    return identity, tier.strip(), (status_m.group("status") if status_m else "").strip()


def _token(field):
    """The leading bare token of a field, so `primary (book)` yields `primary`."""
    m = re.match(r"[^A-Za-z]*([A-Za-z][A-Za-z-]*)", field or "")
    return m.group(1).lower() if m else ""


def _status_token(field):
    """The enum token inside an already-positionally-extracted status field, or "".

    Whole-token matching, so `not-retrieved-ish` is not `not-retrieved`. A qualifier around the token
    is allowed and is often the more honest record: `landing page fetched-and-verified; the model PDF
    itself was not read` says exactly what was and was not read, and five real entries write it that
    way. Because the field is read from its position in the entry grammar rather than found loose in
    the block, a token in a quotation or a legend cannot reach this function at all. Two different
    tokens in one field is ambiguous and fails.
    """
    found = {t for t in STATUSES
             if re.search(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", field or "", re.I)}
    return found.pop() if len(found) == 1 else ""


def _tier_ok(tier):
    """A tier field is one documented word, optionally qualified, or the list layout's [Tier N]."""
    if re.match(r"^\s*tier\s*\d\s*$", tier or "", re.I):
        return True
    return _token(tier) in TIERS


def _supports_value(body):
    """The value of the labelled Supports clause, empty when absent or empty."""
    m = re.search(r"(?:^|\n|\s)\*{0,2}Supports:?\*{0,2}\s*(?P<value>[^\n]*)", body, re.I)
    return (m.group("value").strip(" *") if m else "").strip()


def _url_ok(body):
    """(has_url, has_stated_exemption). A reason must be words, not forty characters of anything."""
    has_url = "http://" in body.lower() or "https://" in body.lower()
    m = URL_EXEMPTION.search(body)
    reason = m.group("reason") if m else ""
    # Two words is the bar: enough to reject forty characters of punctuation, low enough that
    # "No URL because it is print-only." passes. The contract asks for a stated reason, not a word
    # count, and a checker that invents a threshold the standard never set is the failure this
    # repository already has a name for.
    return has_url, len(re.findall(r"[A-Za-z]{2,}", reason)) >= 2


def _entry_problems(num, body, identity, tier, status, supports):
    problems = []

    if len(identity) < 8 or not re.search(r"[A-Za-z]", identity):
        problems.append("entry %d: no identity (name the author or organisation, and the title)" % num)

    has_url, exempt_stated = _url_ok(body)
    if not has_url and not exempt_stated:
        problems.append(
            "entry %d: no url, and no stated reason for its absence. A print source states the "
            "absence and gives the reason in words; see risk-register [33]" % num)

    if not _tier_ok(tier):
        problems.append("entry %d: tier field is %r; expected one of %s, optionally qualified, or "
                        "[Tier n]" % (num, tier[:40], ", ".join(TIERS)))

    if not _status_token(status):
        problems.append("entry %d: retrieval status field is %r; it must contain exactly one of %s"
                        % (num, (status[:60] or "empty"), ", ".join(STATUSES)))

    if not supports:
        problems.append("entry %d: no Supports clause, or it is empty. Write what the source is "
                        "relied on for, or `Supports: nothing in this bundle` and why it is listed"
                        % num)

    return problems


def _numbering_problems(numbers):
    """Contiguous, unique, and in document order."""
    problems = []
    seen = set()
    for n in numbers:
        if n in seen:
            problems.append("entry %d: duplicate number" % n)
        seen.add(n)
    if numbers and numbers != sorted(numbers):
        problems.append("entries are numbered out of document order: %s"
                        % ", ".join(str(n) for n in numbers[:12]))
    ordered = sorted(seen)
    if ordered and ordered[0] != 1:
        problems.append("numbering starts at %d, must start at 1" % ordered[0])
    if ordered:
        missing = [n for n in range(1, ordered[-1] + 1) if n not in seen]
        if missing:
            problems.append("numbering is not contiguous, missing: "
                            + ", ".join(str(n) for n in missing))
    return problems


def _duplicate_problems(entries):
    """The same source under two numbers, unless the later entry declares the repeat."""
    problems, seen = [], {}
    for num, identity, body in entries:
        key = re.sub(r"[^a-z0-9]", "", identity.lower())[:60]
        if not key:
            continue
        if key in seen:
            m = CROSS_REFERENCE.search(body)
            if not (m and int(m.group(1)) == seen[key]):
                problems.append("entry %d: repeats the source already listed as entry %d. One "
                                "source, one entry; a deliberate repeat says which entry it repeats"
                                % (num, seen[key]))
        else:
            seen[key] = num
    return problems


def _table_problems(kept):
    """Validate a numbered table through a header-to-index map, not fixed positions."""
    problems, entries, numbers = [], [], []
    header = next((line for _, line in kept if TABLE_HEADER.match(line)), None)
    if not header:
        return ["a numbered table carries no header row naming its columns"], [], []

    cells = [c.strip().lower() for c in header.strip().strip("|").split("|")]
    index = {}
    for field, names in COLUMNS.items():
        for i, cell in enumerate(cells):
            if cell in names or any(cell.startswith(n) for n in names):
                index[field] = i
                break
    missing = [f for f in COLUMNS if f not in index]
    if missing:
        problems.append("numbered table header does not declare %s; got: %s"
                        % (", ".join(sorted(missing)), header.strip()))
        return problems, [], []

    for _, line in kept:
        m = TABLE_ROW.match(line)
        if not m:
            continue
        num = int(m.group(1))
        numbers.append(num)
        row = [c.strip() for c in line.strip().strip("|").split("|")]

        def cell(field):
            i = index[field]
            return row[i] if i < len(row) else ""

        identity, tier = cell("identity"), cell("tier")
        problems += _entry_problems(num, line, identity, tier, cell("retrieval"), cell("supports"))
        entries.append((num, identity, line))
    return problems, entries, numbers


def check_log(bundle, path):
    """Every problem in one research log. An empty list means the contract holds."""
    text = open(path, encoding="utf-8").read()
    return check_text(text)


def check_text(text):
    kept = source_lines(text)
    if not kept:
        return ["no section heading names the sources. A research log lists its sources under a "
                "heading such as `## Sources`, so a reader and a checker look in the same place"]

    prose = _entry_blocks(kept, PROSE_ENTRY)
    listed = _entry_blocks(kept, LIST_ENTRY)
    has_table = any(TABLE_ROW.match(line) for _, line in kept)

    if not (prose or listed or has_table):
        return ["no source entries found under the sources heading. Number every source in one of "
                "the three legal layouts (numbered prose, numbered list, numbered table)"]

    problems, entries, numbers = [], [], []

    if prose or listed:
        if prose and listed:
            problems.append("mixed source layouts under the sources heading: %d numbered-prose and "
                            "%d numbered-list entries. Pick one so every source is read the same way"
                            % (len(prose), len(listed)))
        for num, body in sorted(prose + listed, key=lambda e: e[0]):
            if PROSE_ENTRY.match(body):
                identity, tier, status = _split_prose(body)
            else:
                identity, tier, status = _split_list(body)
            problems += _entry_problems(num, body, identity, tier, status, _supports_value(body))
            entries.append((num, identity, body))
        numbers = [n for n, _ in (prose + listed)]
        if has_table:
            problems.append("a numbered table appears under the sources heading alongside numbered "
                            "entries; a log uses one layout for its sources")
    else:
        tp, entries, numbers = _table_problems(kept)
        problems += tp

    problems += _numbering_problems(numbers)
    problems += _duplicate_problems(entries)
    return problems


def count_entries(text):
    """How many sources this log declares, after section scoping."""
    kept = source_lines(text)
    prose = _entry_blocks(kept, PROSE_ENTRY)
    listed = _entry_blocks(kept, LIST_ENTRY)
    rows = [1 for _, line in kept if TABLE_ROW.match(line)]
    return len(prose) + len(listed) + len(rows)


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
          "\n      clause is accurate, whether a quoted phrase appears in its source, whether a URL"
          "\n      belongs to the source it sits with, or whether an identity names both an author"
          "\n      and a title." + OFF)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
