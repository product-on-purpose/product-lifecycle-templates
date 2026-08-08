#!/usr/bin/env python3
"""Every quoted phrase in a reader-facing file, checked against the research log's Quotable lists.

WHY THIS EXISTS. The dominant defect class in this library is a plausible specific claim no logged source
supports, and its sharpest form is a **quotation that exists in no source**. It has shipped past a green
gate repeatedly, and it has a supply chain: a phrase originates in a research agent's `findings` prose,
passes into the synthesised log's *narrative*, and is then quoted by a drafting agent as source-attributed.
A verification pass over source ENTRIES clears it, because the phrase was never in an entry.

So the rule this checks is structural: **anything a companion quotes must live in an entry's `Quotable:`
clause**, not in the log's prose. An ad-hoc version of this sweep found real fabrications in four
consecutive bundles, including a phrase attributed to a vendor that was the drafting agent's own wording.

TWO BUGS IT INHERITS AND FIXES, both measured 2026-08-06:

  1. A 25-CHARACTER FLOOR exempted the shortest fabrications, which are the hardest to catch by eye. A
     23-character section title reached a shipped companion through exactly that gap. The floor here is 12.
     A threshold chosen to suppress noise is a decision about what you will never see.
  2. `^Quotable:(.*)$` READ ONLY THE FIRST LINE of a wrapped block, so every hand-written log was being
     under-read. Quotables here are joined across continuation lines until the next field or entry.

REPORT ONLY, AND DELIBERATELY SO. Measured across the library, the raw sweep reports well over a hundred
candidates dominated by scare quotes, document titles, the library's own contract vocabulary, and
nested-quote artifacts. Shipping it as a gate half-calibrated would be the "check that cries wolf" mistake
this repository has already learned once. The exclusions below are each earned and each named; what
survives them is a SORT for a reader, never a verdict.

CALIBRATION VERDICT, MEASURED 2026-08-08, AND IT DECIDES HOW THIS SHIPS.

Run over one bundle at the moment it is built, this is useful: `status-report` returns 10 candidates, and
they include the two failure modes that bundle's research had DROPPED as unsourced. That is a builder
triaging a short list at the point of use, which is the job.

Run library-wide it returns 328 candidates, of which 139 sit in a log's narrative. Sampling those shows
they are dominated by **terms being discussed rather than sources being attributed**: "Architectural",
"Confirmation", "works for me". Quoting a term in order to argue about it is not an attribution, and
nothing here can tell the two apart.

**So this is a phase 3.5 tool, run per bundle, and is NOT wired into CI.** Shipping a library-wide check at
that signal-to-noise would train a reader to ignore it, which is the "gate that cries wolf" mistake this
repository already made once and declined to repeat. If it is ever gated, it must be gated per bundle at
build time, on a bundle whose hits have been triaged to zero.

Usage:
    python tools/lint-quotation-provenance.py <type>            # THE INTENDED USE: one bundle
    python tools/lint-quotation-provenance.py                   # every bundle; expect noise
    python tools/lint-quotation-provenance.py <type> --every    # all candidates, not just log-narrative
    python tools/lint-quotation-provenance.py <type> --all      # also drop the earned exclusions
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, "templates")
RED, DIM, OFF = "\033[31m", "\033[2m", "\033[0m"

MIN_LEN = 12  # bug 1: was 25, which exempted section-title-shaped fabrications
READER_FACING = ("_companion.md", "_guide.md")

# A quoted run: straight or curly doubles. Deliberately not single quotes, which collide with apostrophes.
QUOTED = re.compile(r"[\"“]([^\"“”]{%d,400}?)[\"”]" % MIN_LEN)
QUOTABLE_START = re.compile(r"^\s*Quotable:\s*(.*)$")
FIELD_START = re.compile(r"^\s*(Supports|Contested/time-bound|Quotable):|^\*\*\[\d+\]|^###\s|^##\s")


def norm(text):
    """Compare on words only: quoting conventions, case and punctuation differ legitimately."""
    return re.sub(r"[^a-z0-9 ]+", " ", text.lower()).strip()
    # deliberately not collapsing spaces here; callers do it


def squash(text):
    return re.sub(r"\s+", " ", norm(text)).strip()


def quotables(log_text):
    """Every Quotable phrase, joining wrapped continuation lines. This is bug 2."""
    out, buf = [], None
    for line in log_text.splitlines():
        m = QUOTABLE_START.match(line)
        if m:
            if buf:
                out.append(buf)
            buf = m.group(1).strip()
            continue
        if buf is not None:
            # A wrapped Quotable continues until the next field, entry or heading.
            if FIELD_START.match(line) or not line.strip():
                out.append(buf)
                buf = None
            else:
                buf += " " + line.strip()
    if buf:
        out.append(buf)
    return [squash(q.strip().strip('"“”')) for q in out if q.strip()]


def strip_regions(text, path):
    """Remove regions where a quoted phrase is not a source attribution.

    Each exclusion is earned, and removing one only ever adds candidates.
    """
    # The References list: those are citations, and their titles are quoted by convention.
    if "## References" in text:
        text = text.split("## References", 1)[0]
    # Guidance comments: instructions to an author, and their GOOD/WEAK blocks quote example prose
    # deliberately. Companions have none; guides carry rubric cells that quote illustrative wording.
    text = re.sub(r"(?s)<!--.*?-->", " ", text)
    # Fenced code: template skeletons and command output.
    text = re.sub(r"(?s)```.*?```", " ", text)
    return text


def bundle_paths(name):
    d = os.path.join(TEMPLATES, name)
    log = os.path.join(d, name + "_research-log.md")
    files = [os.path.join(d, name + s) for s in READER_FACING]
    return log, [f for f in files if os.path.isfile(f)]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def sweep(name, apply_exclusions=True):
    log_path, files = bundle_paths(name)
    if not os.path.isfile(log_path):
        return None
    allowed = quotables(read(log_path))
    log_squashed = squash(read(log_path))  # a phrase may legitimately be quoting the log's own framing
    hits = []
    for path in files:
        raw = read(path)
        body = strip_regions(raw, path) if apply_exclusions else raw
        for n, line in enumerate(body.splitlines(), 1):
            for phrase in QUOTED.findall(line):
                if phrase != phrase.strip():
                    # Begins or ends on whitespace: this is the regex spanning the GAP between two
                    # real quotations on one line, not a quotation. Measured 2026-08-08: this single
                    # rule removed most of the noise the first calibration run produced.
                    continue
                if "](" in phrase or "[[" in phrase or "-->" in phrase:
                    continue  # markdown link or comment artifact, not an attribution
                s = squash(phrase)
                if len(s) < MIN_LEN:
                    continue
                if any(s in q or q in s for q in allowed):
                    continue
                if apply_exclusions and s in log_squashed:
                    # Present in the log, but NOT in a Quotable clause. This is the exact supply chain the
                    # docstring describes, so it is reported, not excluded. Marked so a reader sees it first.
                    hits.append((os.path.basename(path), n, phrase, "IN LOG NARRATIVE, NOT IN A QUOTABLE"))
                    continue
                hits.append((os.path.basename(path), n, phrase, "not in the log at all"))
    return allowed, hits


def main(argv):
    apply_exclusions = "--all" not in argv
    narrative_only = "--all" not in argv and "--every" not in argv
    names = [a for a in argv if not a.startswith("--")]
    if not names:
        names = sorted(
            d for d in os.listdir(TEMPLATES)
            if os.path.isdir(os.path.join(TEMPLATES, d)) and not d.startswith((".", "_"))
        )

    total_hits, total_quotables, narrative = 0, 0, 0
    for name in names:
        result = sweep(name, apply_exclusions)
        if result is None:
            continue
        allowed, hits = result
        total_quotables += len(allowed)
        narrative += sum(1 for h in hits if "NARRATIVE" in h[3])
        shown = [h for h in hits if "NARRATIVE" in h[3]] if narrative_only else hits
        all_count = len(hits)
        hits = shown
        total_hits += all_count
        if hits:
            print("  %s  (%d shown of %d candidate(s))" % (name, len(hits), all_count))
            for fname, line, phrase, why in hits[:8]:
                flag = RED + "NARRATIVE" + OFF if "NARRATIVE" in why else "unlogged "
                short = phrase if len(phrase) <= 96 else phrase[:93] + "..."
                print("    %s %s:%d  \"%s\"" % (flag, fname, line, short))
            if len(hits) > 8:
                print("    %s... %d more" % (DIM, len(hits) - 8) + OFF)

    print("\nquotation provenance: %d bundle(s), %d logged quotable(s), %d candidate(s)"
          % (len(names), total_quotables, total_hits))
    if narrative:
        print("%s%d sit in the log's NARRATIVE rather than a Quotable clause, and are the ones worth"
              % (RED, narrative) + OFF)
        print("      reading first: that is the exact route every fabricated quotation in this library took.")
    print(DIM + """      REPORT ONLY. A candidate is not a defect. Legitimate hits are expected from scare quotes,
      document and section titles, this library's own contract vocabulary, and nested quotations.
      Judge them; do not delete blindly.

      Exclusions applied (--all to disable): the References list, guidance comments, and fenced code.
      Each was earned, and removing one only ever adds candidates.

      not verified: whether a phrase that IS in a Quotable clause was truly read verbatim at its source.
      Nothing here can check that. Only re-fetching can, and phase 4 of the pipeline is where a reader
      does it.""" + OFF)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
