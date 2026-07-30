#!/usr/bin/env python3
"""Fail when a bundle's worked example reuses its own template's GOOD/WEAK illustration text.

WHY THIS EXISTS
---------------
A template's guidance comments carry GOOD: and WEAK: snippets that illustrate a section. The worked
example is supposed to demonstrate the template INDEPENDENTLY. When the example is the guidance text
reworded, it demonstrates nothing, and a reader who has read the comments learns nothing new from the
example.

This defect has now recurred three times:

  product-strategy (2026-07-28)  seven of eight sections were the template's GOOD text reworded.
  product-roadmap  (2026-07-29)  three of eight, one sentence verbatim, after the convention
                                 "use a different scenario in the comments than in the example"
                                 had been adopted specifically to prevent it.
  okrs             (2026-07-30)  two sections, WITH a deliberately different scenario in place
                                 (hiring platform in the comments, Acme Analytics in the example).

That third occurrence is why this check exists rather than another convention. Scenario separation is
NECESSARY AND NOT SUFFICIENT: the reuse survives a total change of nouns, because it lives in the
sentence skeleton, not the subject. The okrs example swapped every proper noun and still carried
"the number moves in the meeting or it does not get recorded" and "gets a written note on what we
learned, not a remediation plan" straight out of the hints.

WHAT IT DOES
------------
Extracts every GOOD: and WEAK: snippet from the bundle's template guidance comments, extracts the
example's prose, normalises both (lowercase, punctuation stripped, numbers and capitalised words
folded), and reports shared word n-grams.

WHAT IT CANNOT DO
-----------------
It cannot tell a reworded illustration from an independent sentence that happens to share a common
phrase. It measures verbatim overlap only. An example that paraphrases a hint completely, keeping the
idea and none of the words, passes this check and may still be the defect. That judgement stays with
the review lenses. This check exists to stop the cheap half of the problem cheaply.
"""
import re
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

FAIL_N = 8   # a shared run of this many words fails the build
WARN_N = 6   # a shared run of this many words is reported, not fatal

# Words too structural to be evidence of copying on their own.
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "than", "that", "this", "these", "those",
    "is", "are", "was", "were", "be", "been", "being", "it", "its", "to", "of", "in", "on", "at",
    "for", "with", "as", "by", "from", "not", "no", "we", "you", "they", "their", "our", "your",
}


def guidance_snippets(text: str) -> list[str]:
    """Every GOOD: and WEAK: illustration inside a guidance comment block."""
    out = []
    for block in re.findall(r"<!--(.*?)-->", text, re.S):
        # A snippet runs from GOOD/WEAK until the next all-caps grammar key or the block end.
        for m in re.finditer(
            r"^\s*(GOOD|WEAK)\s+(.*?)(?=^\s*(?:WHAT|WHY|ASK|GOOD|WEAK|TRAP|PRIORITY|ROW HINT)\s|\Z)",
            block, re.S | re.M,
        ):
            out.append(m.group(2))
    return out


def example_prose(text: str) -> str:
    """The example body, minus frontmatter and the editorial blockquote."""
    text = re.sub(r"\A---.*?^---\s*$", "", text, flags=re.S | re.M)   # frontmatter
    text = re.sub(r"^>.*$", "", text, flags=re.M)                     # editorial blockquote
    return text


def normalise(text: str) -> list[str]:
    text = re.sub(r"`[^`]*`", " ", text)                 # code spans
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links keep their label
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return [w for w in text.split() if w]


def ngrams(words: list[str], n: int) -> set[tuple]:
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def informative(gram: tuple) -> bool:
    """Ignore runs that are entirely structural filler."""
    return sum(1 for w in gram if w not in STOPWORDS) >= 3


CAP = 60


def longest_shared(snippets: list[str], example: list[str]) -> list[tuple]:
    """Maximal shared runs, longest first, one report per copied passage.

    Two reporting defects were measured on 2026-07-30 and are fixed here.

    (A) CROSS-SNIPPET GHOST RUNS. Joining every snippet into one string let an n-gram run off the end of
        one hint into the start of the next and match text no hint ever contained: 67 such ghosts at n>=8
        across the library, one of which was an entire reported failure. Hint n-grams are now built PER
        SNIPPET and unioned, so a run must live inside a single illustration.

    (B) SLIDING-WINDOW FRAGMENTATION. Suppressing a hit only when its text was a substring of an accepted
        hit did nothing for windows offset by one word, so a single copied passage was reported as many
        near-identical lines: 31 of one bundle's 37 lines came from 3 passages. Suppression is now by
        POSITION in the example, so each copied passage reports once.

    Together these dropped reported lines from 159 to a readable number WITHOUT changing which bundles
    fail. They buy honesty in the count, not leniency.
    """
    hits: list[tuple] = []
    claimed: list[tuple[int, int]] = []
    for n in range(CAP, WARN_N - 1, -1):
        if n > len(example):
            continue
        hint_grams: set[tuple] = set()
        for s in snippets:
            w = normalise(s)
            if len(w) >= n:
                hint_grams |= ngrams(w, n)
        if not hint_grams:
            continue
        for i in range(len(example) - n + 1):
            g = tuple(example[i:i + n])
            if g not in hint_grams or not informative(g):
                continue
            span = (i, i + n)
            if any(min(span[1], c[1]) > max(span[0], c[0]) for c in claimed):
                continue
            claimed.append(span)
            hits.append(g)
    return hits


def check(bundle: Path) -> tuple[int, int, list[str]]:
    name = bundle.name
    example = bundle / f"{name}_example.md"
    templates = sorted(bundle.glob(f"{name}_template-*.md"))
    if not example.exists() or not templates:
        return 0, 0, []

    snippets = []
    for t in templates:
        snippets.extend(guidance_snippets(t.read_text(encoding="utf-8")))
    if not snippets:
        return 0, 0, []

    ex_words = normalise(example_prose(example.read_text(encoding="utf-8")))

    fails, warns, lines = 0, 0, []
    for gram in longest_shared(snippets, ex_words):
        n = len(gram)
        if n >= FAIL_N:
            fails += 1
            lines.append(f"    FAIL  {n} words: \"{' '.join(gram)}\"")
        else:
            warns += 1
            lines.append(f"    warn  {n} words: \"{' '.join(gram)}\"")
    return fails, warns, lines


# Bundles that shipped before this check existed, with the passage count measured on the day it was
# written. THE NUMBERS ARE CEILINGS AND MAY ONLY SHRINK. A grandfathered bundle whose count rises fails
# the build; a bundle absent from this map fails on its first overlap. Delete an entry as its example is
# rewritten, and delete this whole mechanism when the map is empty.
#
# Triaged 2026-07-30 by reading all 16 against their raw comment blocks: ZERO false positives, and the
# check was found to UNDER-report rather than over-report (at least two further verbatim copies escape
# because an inserted article breaks the run below threshold). No document-type exemption was warranted:
# every surviving run carries invented proper nouns, figures or IDs rather than required format grammar.
GRANDFATHERED = {
    "acceptance-criteria": (10, "5 of 6 guidance sections copied verbatim, including a whole Given/When/Then scenario"),
    "adr": (10, "title is character-identical to the GOOD hint; 8 sections near-verbatim"),
    "bug-report": (4, "hints pre-state the example's answers: same PR, build, verifier and guard test"),
    "kpi-dashboard": (10, "metric formula, limitation, owner and data steward carried over intact"),
    "prd": (15, "10+ sections copied, several whole table rows and the user story word for word"),
    "product-backlog": (3, "Product Goal is the GOOD line with one capitalisation changed"),
    "product-strategy": (1, "partially repaired 2026-07-28; the falsifier sentence still survives"),
    "product-vision": (13, "worst in the library: one example patched from the hints of all four formats"),
    "raid-log": (11, "four register rows and the Review paragraph lifted, blending lean and full hints"),
    "release-notes": (13, "every substantive section has a verbatim run; header reuses the hint's own date"),
    "risk-register": (8, "a whole risk row, the appetite paragraph and the likelihood bands lifted"),
    "sdd": (1, "Non-Goals hint reused for 18 running words"),
    "sprint-backlog": (6, "Sprint Goal is the GOOD sentence with a parenthetical inserted"),
    "test-case": (8, "an entire approval-table row copied, plus a fictional automation path"),
    "test-plan": (9, "scope, entry/exit, environment, suspension and schedule dates reused"),
    "user-stories": (10, "nearly every section of both variants is hint prose relocated"),
}


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    bundles = sorted(
        d for d in TEMPLATES.iterdir()
        if d.is_dir() and not d.name.startswith((".", "_")) and (only is None or d.name == only)
    )

    total_f = total_w = checked = 0
    breaches: list[str] = []
    debt: list[tuple[str, int, int, str]] = []

    for b in bundles:
        f, w, lines = check(b)
        if not (b / f"{b.name}_example.md").exists():
            continue
        checked += 1
        total_f += f
        total_w += w

        if f and b.name in GRANDFATHERED:
            ceiling, reason = GRANDFATHERED[b.name]
            debt.append((b.name, f, ceiling, reason))
            if f > ceiling:
                breaches.append(
                    f"  FAIL  {b.name}: {f} copied passage(s), above its grandfathered ceiling of {ceiling}. "
                    f"These may only shrink."
                )
                for line in lines:
                    print(line)
            continue

        if f:
            breaches.append(f"  FAIL  {b.name}: {f} copied passage(s), and it is not grandfathered.")
            print(f"  FAIL  {b.name}")
            for line in lines:
                print(line)
        elif w:
            print(f"  warn  {b.name}")
            for line in lines:
                print(line)

    print()
    print(f"example independence: {checked} bundle(s) checked, "
          f"{total_f} copied passage(s), {total_w} warning overlap(s)")
    print(f"      a run of {FAIL_N}+ shared words is a copied passage; {WARN_N}-{FAIL_N - 1} is reported only.")

    if debt:
        owed = sum(d[1] for d in debt)
        print()
        print(f"  DEBT  {len(debt)} bundle(s) grandfathered, {owed} copied passage(s) outstanding.")
        print("        These shipped before the check existed. They are NOT a pass. Each ceiling may only")
        print("        shrink; rewrite the example, lower the number, and delete the entry when it hits 0.")
        for name, count, ceiling, reason in sorted(debt, key=lambda d: -d[1]):
            print(f"        {name:<22} {count}/{ceiling}  {reason}")

    print()
    print("      not verified: a paraphrase that keeps the idea and none of the words. This check")
    print("      measures verbatim overlap only, so a fully reworded illustration passes it, and")
    print("      triage on 2026-07-30 found it UNDER-reports: at least two known verbatim copies")
    print("      escape because an inserted article breaks the run below threshold.")

    if breaches:
        print()
        for line in breaches:
            print(line)
        print("FAIL  a worked example reuses its own template's illustration text.")
        return 1

    print()
    print("OK  no bundle exceeds its example-independence ceiling.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
