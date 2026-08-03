#!/usr/bin/env python3
"""Report specifics in a companion or guide that appear nowhere in that bundle's research log.

WHY THIS EXISTS
---------------
The single most persistent defect in this library is a plausible specific that no source supports. It is not
a misreading and not a stale fact: it is a number, a year, or a named person that reads entirely credible and
that no logged source carries. Every review pass finds some, across six consecutive bundles.

The clearest case shipped in `product-roadmap` on 2026-07-29 and passed all eleven gate checks, the link
gate, both self-tests and CI:

    "Robert Galvin supplied the definition everyone quotes, EIRMA formalised a generic
     method in 1997, and Cambridge's T-Plan packaged it in the late 1990s"

`Galvin`, `1997` and `late 1990` each return ZERO matches in that bundle's research log. Three fabricated
specifics in one sentence, and it took an adversarial review to find them. This check finds that class in
about a second.

WHAT IT CHECKS
--------------
For each bundle, it extracts high-signal specifics from the reader-facing files (companion and guide) and
asks one question of each: does this string appear anywhere in the bundle's own research log?

Two classes, chosen because they carry almost all the signal and almost none of the noise:

  YEARS         a four-digit year in 1000-2999. A date is the most common fabricated specific and the
                easiest to check.
  PROPER NOUNS  a capitalised token that looks like a surname or an organisation, appearing mid-sentence.
                `Galvin`, `EIRMA`, `Lucent`. These are how an invented attribution announces itself.

Percentages and general numbers were deliberately EXCLUDED after calibration: prose is full of "three
formats", "section 3", "two sizes", and flagging them buries the signal. This check is narrow on purpose. A
check that reports everything gets ignored, which is the failure mode its sibling `check-counts.py` names in
its own output.

WHAT IT CANNOT DO, AND THIS IS THE IMPORTANT PART
-------------------------------------------------
A hit means the string appears somewhere in the log. It does NOT mean the log SUPPORTS the claim. `1997`
appearing in some unrelated entry clears a fabricated "EIRMA formalised a method in 1997" just as readily as
a real citation would. This check narrows the search; it does not verify support.

Verifying that a source supports a claim is the four-lens review's job, and per the research it is the one
part that may never be fully mechanizable. This is the cheap half, run on every commit, so the expensive half
has less to find.

It also cannot see fabrication INSIDE the research log. The `okrs` log carried two quotes existing in no
source, and this check would have passed every one of them, because the log is exactly what it compares
against. Only re-fetching catches that, which is what `tools/source-cache.py` makes affordable.
"""
import re
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

YEAR = re.compile(r"\b(1[0-9]{3}|2[0-9]{3})\b")

# A capitalised name-shaped run that FOLLOWS A LOWERCASE WORD. That anchor is what makes this usable.
#
# Calibrated 2026-07-31. The first attempt matched any capitalised token not after a full stop, and it
# flooded: 36 hits on one bundle, every one a heading word, a table label or a bold run ("Edge", "Happy",
# "Full", "Lean"). Markdown is dense with capitals that are formatting rather than names.
#
# Requiring a preceding lowercase word or comma restricts matches to genuine prose position, which is
# exactly where a fabricated attribution lives: "credited to Willyard and McClees", ", Robert Galvin
# supplied". A name at the start of a heading or a table cell is not a claim being made in a sentence.
PROPER = re.compile(r"(?<=[a-z,]\s)((?:[A-Z][a-zA-Z]{2,}\s+)*[A-Z][a-zA-Z]{2,})")

# Vocabulary that is capitalised for reasons other than being a cited proper noun: the library's own terms,
# markdown/HTML furniture, and ordinary sentence-leading words that slip past the lookbehind.
IGNORE = {
    # library vocabulary
    "Tier", "Deep", "Approach", "Objective", "Objectives", "Results", "Result", "Template", "Templates",
    "Companion", "Guide", "Example", "Anatomy", "Orientation", "Origins", "Variants", "Sizing", "Debates",
    "Adaptations", "References", "Relationships", "Methodology", "Confirmation", "Consequences", "Context",
    "Decision", "Drivers", "Status", "Analyst", "Analysts", "Recurring", "Saved", "Views", "View",
    # generic english that survives the lookbehind at line starts, after quotes, in tables
    "This", "That", "These", "Those", "There", "Their", "They", "Then", "Than", "What", "When", "Where",
    "Which", "While", "With", "Without", "Write", "Written", "Would", "Could", "Should", "Every", "Each",
    "Because", "Before", "After", "About", "Above", "Below", "Both", "Some", "Same", "Such", "Still",
    "Never", "Nothing", "Nobody", "Under", "Until", "Unless", "Only", "Once", "Note", "Read", "Reach",
    "Keep", "Make", "Most", "Must", "More", "Less", "Also", "Even", "Here", "Have", "Does", "Doing",
    "Good", "Weak", "Trap", "Priority", "Score", "Scored", "Scoring", "Confidence", "Owner", "Owners",
    "Period", "Initiatives", "Initiative", "Cycle", "Team", "Teams", "Google", "From", "Into", "Their",
}

READER_FACING = ("_companion.md", "_guide.md")


def normalise_for_search(text: str) -> str:
    return text.lower()


def prose_of(path: Path) -> str:
    """Reader-facing prose, minus the reference list, which is bibliography rather than claims."""
    text = path.read_text(encoding="utf-8")
    for marker in ("\n## References", "\n## 11. References"):
        if marker in text:
            text = text.split(marker, 1)[0]
    text = re.sub(r"```.*?```", " ", text, flags=re.S)          # code fences
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)          # comments
    text = re.sub(r"\[\[\d+\]\]\(#ref-\d+\)", " ", text)        # citation markers
    text = re.sub(r"\]\([^)]*\)", "] ", text)                    # link targets, keep labels
    return text


def specifics(text: str) -> tuple[set[str], set[str]]:
    years = set(YEAR.findall(text))
    nouns = {m for m in PROPER.findall(text) if m.rstrip("'s") not in IGNORE and m not in IGNORE}
    return years, nouns


def name_is_present(candidate: str, haystack: str) -> bool:
    """A name counts as present if the log carries it, OR carries its surname.

    Calibrated 2026-07-31 against a real false positive. `adr_companion.md` cites "Kurt Bittner"; the log's
    entry reads "Pureur and Bittner". Matching the full string flagged a correctly cited source, because
    research logs routinely record surnames while prose introduces people by full name. Clearing on the
    LAST token (surname position) fixes that without clearing on a common forename: "Robert Galvin" still
    flags when the log has no "Galvin", which is the case this check exists for.
    """
    c = candidate.rstrip("'s").lower()
    if c in haystack:
        return True
    tokens = [t for t in c.split() if len(t) >= 4]
    return bool(tokens) and tokens[-1] in haystack


def check(bundle: Path) -> tuple[int, list[str]]:
    name = bundle.name
    log = bundle / f"{name}_research-log.md"
    if not log.exists():
        return 0, []
    haystack = normalise_for_search(log.read_text(encoding="utf-8"))

    findings: list[str] = []
    for suffix in READER_FACING:
        f = bundle / f"{name}{suffix}"
        if not f.exists():
            continue
        text = prose_of(f)
        years, nouns = specifics(text)
        missing_years = sorted(y for y in years if y not in haystack)
        missing_nouns = sorted(n for n in nouns if not name_is_present(n, haystack))
        for y in missing_years:
            findings.append(f"    year   {y:<8} in {f.name}, absent from the research log")
        for n in missing_nouns:
            findings.append(f"    name   {n:<20} in {f.name}, absent from the research log")
    return len(findings), findings


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None
    bundles = sorted(
        d for d in TEMPLATES.iterdir()
        if d.is_dir() and not d.name.startswith((".", "_")) and (only is None or d.name == only)
    )

    total, checked = 0, 0
    for b in bundles:
        n, lines = check(b)
        if not (b / f"{b.name}_research-log.md").exists():
            continue
        checked += 1
        if n:
            total += n
            print(f"  {b.name}")
            for line in lines:
                print(line)

    print()
    print(f"number provenance: {checked} bundle(s) checked, {total} unsourced specific(s)")
    print("      Reports years and proper nouns in a companion or guide that appear NOWHERE in that")
    print("      bundle's research log. Narrow on purpose: percentages and plain numbers were excluded")
    print("      after calibration because prose is full of them and the signal drowns.")
    print()
    print("      NOT VERIFIED, and this is the important part: a hit means the string appears in the log,")
    print("      NOT that the log supports the claim. An unrelated mention of a year clears a fabricated")
    print("      sentence about that year just as readily as a real citation would. Verifying support is")
    print("      the four-lens review's job. This is the cheap half so the expensive half has less to find.")
    print()
    print("      It also cannot see fabrication INSIDE the log, which is what it compares against. Only")
    print("      re-fetching catches that; see tools/source-cache.py.")

    # Report-only by design. It is a lint, not a gate: the false-positive floor on proper nouns is real,
    # and a check that blocks merge on a heuristic teaches people to route around it.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
