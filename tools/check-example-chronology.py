#!/usr/bin/env python3
"""Fail when a worked example cites a sibling example dated later than itself.

WHY THIS EXISTS
---------------
This library's differentiator is one continuous worked thread: a single Acme Analytics scenario running from
a product vision down to a bug report, with each example chaining onto the artifacts around it. That thread
is the demonstration no single bundle can make, and it only works if the artifacts could actually have
existed in the order the documents claim.

On 2026-07-29 the `product-roadmap` example, dated `2026-02-11`, described work as:

    "Specified in the Saved Views PRD; in build."

The Saved Views PRD is dated `created: 2026-06-12`, status `in-review`. A February document cited a June
document as an existing specification, and also cited a July test plan. Four months of time travel, in the
file whose whole job is to demonstrate that the thread holds together. It passed every gate check.

WHAT IT CHECKS
--------------
For every `*_example.md`, it reads the frontmatter date, finds links to sibling examples, and fails when a
link points at an example dated LATER than the linking document.

THE EDITORIAL ESCAPE HATCH, AND WHY IT IS A BLOCKQUOTE
-------------------------------------------------------
Not every forward reference is a defect. An example legitimately carries a note to the READER of the library
saying where this artifact sits in the thread, and that note is allowed to mention documents written later,
because its speaker is the library rather than the fictional author.

Those notes already live in blockquotes by convention: every example opens with a `> **Worked example.**`
block. So links inside blockquote lines are exempt, and links in body prose are not. That is not an arbitrary
rule; it is the exact distinction the `product-roadmap` fix used, moving the PRD and test-plan links out of
the in-world text and into the editorial block, where they read as navigation rather than as a claim about
what existed in February.

WHAT IT CANNOT DO
-----------------
It compares dates and nothing else. It cannot tell whether an example refers to a sibling WITHOUT linking to
it, which is the same defect wearing plainer clothes: "specified in the PRD" with no link is invisible here.
It cannot judge whether a same-day or earlier reference is plausible. And it cannot tell a legitimate
editorial note from an in-world claim that happens to sit inside a blockquote.
"""
import re
import sys
from datetime import date
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

# THE COMPARISON IS ASYMMETRIC, and getting that wrong produced two false positives on the first run.
#
# A reference is impossible only when the TARGET DID NOT EXIST YET. So the two sides need different dates:
#
#   SPEAKS  the latest moment the citing document could be talking from. A document revised on the 9th can
#           legitimately cite anything that existed by the 9th.
#   EXISTS  the earliest moment the cited document came into being. `sdd_example.md` is created 2026-07-02
#           and updated 2026-07-09; a test plan dated the 6th citing it is FINE, because the SDD existed.
#           Comparing against the update date flagged it, wrongly.
#
# A standing instrument that records only `last_reviewed` has no recorded birth date at all, so its
# existence is UNKNOWN and it is skipped rather than guessed at. A risk register reviewed on the 20th may
# well have existed since March.
#
# The field lists are long by measurement, not by taste: on the first run six of nineteen examples were
# skipped as undated, and every one carried a date under a name particular to its document type. A check
# that silently skips a third of its subjects is worse than none, because it reports a clean run over work
# it never looked at.
SPEAKS_FIELDS = (
    "last_updated", "updated", "reported_on", "last_reviewed", "last_refined", "dates", "created", "date",
)
EXISTS_FIELDS = ("created", "reported_on", "dates", "date")
DATE_FIELDS = tuple(dict.fromkeys(SPEAKS_FIELDS + EXISTS_FIELDS))
# Captures a range's END date where one is present. A document covering 13 to 24 July speaks until the 24th,
# so a reference is only impossible if it points past the later bound.
DATE_RE = re.compile(
    r"^(" + "|".join(DATE_FIELDS) + r")\s*:\s*[\"']?(\d{4}-\d{2}-\d{2})"
    r"(?:\s*(?:to|-|through)\s*(\d{4}-\d{2}-\d{2}))?",
    re.M,
)
LINK_RE = re.compile(r"\]\(\.\./([a-z0-9-]+)/\1_example\.md\)")


def frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[:end] if end != -1 else ""


def _mk(s: str) -> date:
    y, m, d = (int(x) for x in s.split("-"))
    return date(y, m, d)


def example_dates(path: Path) -> tuple[tuple[date, str] | None, tuple[date, str] | None]:
    """Return (speaks_as_of, existed_from). Either may be None when the frontmatter cannot say."""
    fm = frontmatter(path.read_text(encoding="utf-8"))
    # For a range, `speaks` takes the end and `exists` takes the start.
    end = {m.group(1): (m.group(3) or m.group(2)) for m in DATE_RE.finditer(fm)}
    start = {m.group(1): m.group(2) for m in DATE_RE.finditer(fm)}

    speaks = next(((_mk(end[f]), f) for f in SPEAKS_FIELDS if f in end), None)
    exists = next(((_mk(start[f]), f) for f in EXISTS_FIELDS if f in start), None)
    return speaks, exists


def body_links(text: str) -> list[tuple[int, str]]:
    """Sibling-example links in body prose, excluding blockquote lines (editorial notes)."""
    out = []
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or line.lstrip().startswith(">"):
            continue
        for m in LINK_RE.finditer(line):
            out.append((i, m.group(1)))
    return out


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    examples = {}
    for d in sorted(TEMPLATES.iterdir()):
        if not d.is_dir() or d.name.startswith((".", "_")):
            continue
        p = d / f"{d.name}_example.md"
        if p.exists():
            examples[d.name] = p

    speaks, exists, undated = {}, {}, []
    for name, p in examples.items():
        s, e = example_dates(p)
        if s is None:
            undated.append(name)
        else:
            speaks[name] = s
        if e is not None:
            exists[name] = e

    failures, checked, links_seen, unknown = [], 0, 0, 0
    for name, p in examples.items():
        if only and name != only:
            continue
        if name not in speaks:
            continue
        checked += 1
        mine, myfield = speaks[name]
        text = p.read_text(encoding="utf-8")
        for lineno, target in body_links(text):
            if target == name:
                continue
            links_seen += 1
            if target not in exists:
                unknown += 1
                continue
            theirs, theirfield = exists[target]
            if theirs > mine:
                delta = (theirs - mine).days
                failures.append(
                    f"  FAIL  {name}_example.md:{lineno}\n"
                    f"        speaks as of {mine} ({myfield}), cites {target}_example.md which did not\n"
                    f"        exist until {theirs} ({theirfield}), {delta} days later.\n"
                    f"        An in-world reference cannot point forward. Either correct a date, or move\n"
                    f"        the link into the editorial blockquote where it reads as navigation."
                )

    print(f"example chronology: {checked} example(s) checked, {links_seen} in-world sibling link(s)")
    if undated:
        print(f"      {len(undated)} example(s) carry no parseable date and were skipped: "
              f"{', '.join(sorted(undated))}")
    if unknown:
        print(f"      {unknown} link(s) point at an example whose CREATION date is not recorded (it carries")
        print("      only a last-reviewed style field), so its existence could not be judged and it was")
        print("      skipped rather than guessed at. A register reviewed in July may have existed since March.")
    print("      Links inside blockquotes are exempt: those are editorial notes addressed to the reader")
    print("      of the library, not claims by the document's fictional author.")
    print("      not verified: a reference made WITHOUT a link, which is the same defect in plainer")
    print("      clothes and is invisible here; and whether an earlier-dated reference is plausible.")

    if failures:
        print()
        for f in failures:
            print(f)
        print("FAIL  an example cites a sibling that did not exist yet.")
        return 1
    print()
    print("OK  no example cites a sibling dated later than itself.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
