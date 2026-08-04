#!/usr/bin/env python3
"""Report frequency, superlative and comparative claims in reader-facing prose, for a human to judge.

WHY THIS EXISTS
---------------
"Most teams", "the most common failure", "almost never", "widely used". Each is an empirical claim about the
world, and each needs a source that actually measured it. This library produces them constantly, and every
review pass finds some that no source supports:

  test-plan       a "most-dropped" section, twice, cited to a source that supported only the section's existence
  test-case       six unsourced frequency or comparative claims in one bundle
  product-roadmap "most often go dishonest", "most slippage", "the most-cited critic"
  okrs            "the most common failure by a distance", "almost never a character problem"

None is a lie. Each is a plausible generalisation written in the authorial voice, and each ships as fact.

WHY IT ONLY REPORTS
-------------------
A four-lens review inventoried every hedged phrase in one bundle and found **39 occurrences, most of them
legitimate**: quotations carrying the source's own hedge, self-referential claims about the document ("the
most important distinction to get right"), and fictional figures inside a worked example. A check that failed
on all 39 would be routed around within a week. So this reports, and a human judges. Its value is
completeness, not verdict: the reviewer sees every candidate rather than the ones they happened to notice.

THE TWO TIERS, AND WHY THE SECOND ONE IS OFF BY DEFAULT
-------------------------------------------------------
Calibration across all 19 shipped bundles tallied every pattern. Four words dominated the output and carried
almost no signal, because this library writes RULES and rules use rule-words:

  never   99 hits   "*Recommendation:* never edit a decided record" - an instruction, not a measurement
  nobody  81 hits   "a document nobody writes and nobody reads" - rhetoric, not a measurement
  no one  15 hits   "and commits no one" - the same rhetorical figure
  always  12 hits   "State it concretely - always, or one time in five" - an instruction again

Together, 207 of 427 hits. Left in, they would bury the 220 that matter, and a report nobody finishes is a
report that catches nothing. They move to a second tier behind `--all` rather than being deleted, and the
default run prints how many it suppressed. Their genuinely empirical forms, "almost never" and "almost
always", stay in tier one as their own patterns and are unaffected.

Two words were rejected outright: `the standard` (26 hits, nearly all referring to a literal named standard
such as ISO/IEC/IEEE 42010) and `every` (146 hits, "applies to every story"). Neither is a frequency claim.

WHAT IT EXCLUDES, AND WHY EACH EXCLUSION IS EARNED
--------------------------------------------------
  QUOTED MATERIAL      a hedge inside quotation marks belongs to the source, not to this library.
  THE EXAMPLE FILE     its figures are explicitly fictional, so its hedges assert nothing about the world.
  THE REFERENCE LIST   bibliography, including retrieval qualifiers that necessarily hedge.
  GUIDANCE COMMENTS    HTML comments in templates are instructions to an author, not assertions.

WHAT IT CANNOT DO
-----------------
It cannot tell a sourced frequency claim from an unsourced one. A sentence carrying a citation looks
identical here to one that does not, because whether the cited source actually MEASURED the frequency is
exactly the judgement the four-lens review exists to make. Nor can it catch a claim phrased without a listed
word: "teams reach for this first" asserts a frequency and appears nowhere in its output.
"""
import re
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

# Grouped so the report says what KIND of claim each is, which tells a reviewer how hard to look.
# Order matters: within a kind the first matching pattern wins, so specific forms precede general ones
# ("most often" before the general "most X"). Across kinds a line can produce one hit per kind,
# deliberately, so a sentence making two different claims is reported twice rather than once.
#
# The general `most X` pattern carries two calibrated qualifiers. It was originally `most \w+s`, requiring
# a plural, and the regression fixture caught it: "Most slippage happens between the Next lane and the
# Later lane" is one of the four historical defects this tool exists for, and it walked straight through,
# because "slippage" is uncountable. Broadening to `most \w+` recovered it and 58 others. The negative
# LOOKAHEAD then drops adverbs, since "most importantly" and "most directly" are discourse markers rather
# than claims; the negative LOOKBEHIND drops "the most", which the superlative group already owns, so a
# phrase like "the most common failure" is reported once rather than twice under two different kinds.
PATTERNS = {
    "frequency": [
        r"\bmost often\b", r"\bmost teams\b", r"\bmany teams\b", r"(?<!the )\bmost (?!\w+ly\b)\w+\b",
        r"\busually\b",
        r"\btypically\b", r"\bcommonly\b", r"\bfrequently\b", r"\boften\b", r"\bgenerally\b",
        r"\brarely\b", r"\bseldom\b", r"\bin practice\b", r"\btend to\b",
        r"\balmost always\b", r"\balmost never\b", r"\bmore often than not\b", r"\bnine times out of ten\b",
    ],
    "superlative": [
        r"\bsingle most\b", r"\bthe most\b", r"\bthe least\b", r"\bmost-cited\b", r"\bmost-\w+\b",
        r"\bbest-known\b", r"\bthe biggest\b", r"\bthe worst\b", r"\bby a distance\b",
    ],
    "comparative": [
        r"\btimes more likely\b", r"\btimes as likely\b", r"\bmore likely\b", r"\bfar more\b",
        r"\bfar fewer\b", r"\bmore than any other\b", r"\bwidely\b", r"\buniversally\b",
        r"\blong predate", r"\bstandard practice\b",
    ],
    "universal": [
        r"\bevery team\b", r"\ball teams\b", r"\beveryone\b", r"\bwithout exception\b",
    ],
}

# Tier two. Measured as 207 of 427 hits and almost pure noise in a library that writes rules. Reported only
# under --all, and the count of what was suppressed is printed on every default run.
RULE_WORDS = {
    "rule-word": [r"\bnever\b", r"\bnobody\b", r"\bno one\b", r"\balways\b"],
}

READER_FACING = ("_companion.md", "_guide.md")


def strip_uncheckable(text: str) -> str:
    """Blank out quoted material, comments, code and the reference list, preserving line numbers."""
    for marker in ("\n## References", "\n## 11. References"):
        if marker in text:
            text = text.split(marker, 1)[0]

    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))

    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)     # guidance comments
    text = re.sub(r"```.*?```", blank, text, flags=re.S)       # code fences
    text = re.sub(r"`[^`\n]*`", blank, text)                   # code spans
    text = re.sub(r'"[^"\n]*"', blank, text)                   # straight-quoted material
    text = re.sub(r"“[^”\n]*”", blank, text)    # curly-quoted material
    return text


def uncited_lines(raw: str) -> set[int]:
    """Line numbers sitting in a blank-line-delimited block that carries no [[N]] citation anywhere.

    Paragraph scope, not line scope, and the difference matters: a citation usually sits at the END of the
    paragraph it supports, so asking "is there a citation on this line" would mark almost every claim
    uncited and the signal would be worthless. This is a SORT, not a verdict. A claim inside a cited
    paragraph can still be unsourced, because whether the cited source measured the frequency is precisely
    what a machine cannot see.
    """
    out, block, start = set(), [], 1
    lines = raw.splitlines()

    def flush(end):
        if block and not any("[[" in ln for ln in block):
            out.update(range(start, end))

    for i, line in enumerate(lines, 1):
        if line.strip():
            if not block:
                start = i
            block.append(line)
        else:
            flush(i)
            block = []
    flush(len(lines) + 1)
    return out


def scan(path: Path, groups: dict) -> list[tuple[int, str, str, str, bool]]:
    raw = path.read_text(encoding="utf-8")
    text = strip_uncheckable(raw)
    uncited = uncited_lines(raw)
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        for kind, pats in groups.items():
            for pat in pats:
                m = re.search(pat, low)
                if m:
                    hits.append((i, kind, m.group(0).strip(), line.strip()[:110], i in uncited))
                    break
    return hits


def main() -> int:
    flags = {"--all", "--uncited"}
    argv = [a for a in sys.argv[1:] if a not in flags]
    show_all = "--all" in sys.argv[1:]
    only_uncited = "--uncited" in sys.argv[1:]
    only = argv[0] if argv else None

    groups = dict(PATTERNS)
    if show_all:
        groups.update(RULE_WORDS)

    bundles = sorted(d for d in TEMPLATES.iterdir()
                     if d.is_dir() and not d.name.startswith((".", "_")) and (only is None or d.name == only))

    total, checked, suppressed, bare = 0, 0, 0, 0
    by_kind: dict[str, int] = {}
    for b in bundles:
        lines = []
        for suffix in READER_FACING:
            f = b / f"{b.name}{suffix}"
            if not f.exists():
                continue
            checked += 1
            if not show_all:
                suppressed += len(scan(f, RULE_WORDS))
            for lineno, kind, phrase, ctx, is_uncited in scan(f, groups):
                by_kind[kind] = by_kind.get(kind, 0) + 1
                if is_uncited:
                    bare += 1
                if only_uncited and not is_uncited:
                    continue
                mark = "UNCITED " if is_uncited else "        "
                lines.append(f"    {mark}{kind:<12} {f.name}:{lineno}  \"{phrase}\"\n                         {ctx}")
        if lines:
            total += len(lines)
            print(f"  {b.name}  ({len(lines)})")
            for line in lines:
                print(line)

    print()
    shown = f", {total} shown" if only_uncited else ""
    print(f"unsourced confidence: {checked} reader-facing file(s) scanned, "
          f"{sum(by_kind.values())} candidate claim(s){shown}")
    if by_kind:
        print("      " + ", ".join(f"{k} {v}" for k, v in sorted(by_kind.items())))
    print(f"      {bare} sit in a paragraph carrying NO citation at all, marked UNCITED and worth reading")
    print("      first (--uncited shows only these). Paragraph scope, not line scope: a citation usually")
    print("      sits at the END of the paragraph it supports, so a line-scoped test would mark nearly")
    print("      everything uncited and mean nothing. This is a SORT, not a verdict.")
    if not show_all:
        print(f"      plus {suppressed} rule-word hit(s) SUPPRESSED: never, nobody, no one, always. Measured")
        print("      across all 19 bundles as almost pure noise, because this library writes rules and rules")
        print("      use rule-words. Not deleted: re-run with --all to see them.")
    print()
    print("      REPORT ONLY, and deliberately so. A review inventoried every hedged phrase in one bundle")
    print("      and found 39, MOST OF THEM LEGITIMATE. A check that failed on all of them would be routed")
    print("      around within a week. The value here is completeness, not verdict: the reviewer sees every")
    print("      candidate rather than the ones they happened to notice.")
    print()
    print("      Excluded, each exclusion earned: quoted material (the hedge belongs to the source), the")
    print("      example file (its figures are labelled fictional), the reference list, and guidance")
    print("      comments (instructions to an author, not assertions).")
    print()
    print("      not verified: whether a claim is SOURCED. A sentence carrying a citation looks identical")
    print("      here to one that does not, because whether the cited source actually MEASURED the")
    print("      frequency is the judgement the four-lens review exists to make. Nor can it catch a claim")
    print("      phrased without a listed word: \"teams reach for this first\" asserts a frequency and")
    print("      appears nowhere above.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
