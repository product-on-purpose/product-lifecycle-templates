#!/usr/bin/env python3
"""Generate a research log's source entries from a build-bundle research fan-out.

WHY THIS EXISTS, and it is the same argument as gen-manifest.py and gen-atlas.py: in this repository
every GENERATED count stays fresh and every RETYPED one drifts (finding DF-5). Source entries are the
same shape of problem one level down. A research log carries 30 to 45 entries, each with a URL, a tier,
a retrieval-status token and a list of verbatim quotables, and transcribing them by hand puts a typo
between a quotation and its source with nothing downstream able to notice.

THE TWO BUGS THIS FIXES, both measured on 2026-08-06, and both DESTROYED EVIDENCE SILENTLY rather than
failing. That is why they are handled here rather than left to care:

  1. DEDUP ON RAW URLs. A www/non-www pair filed one source under two numbers, so the Scrum Guide
     appeared twice in one log. Fixed by normalising scheme, a leading "www.", trailing slash and
     fragment before using the URL as a key.

  2. MERGE REPLACED THE SOURCE INSTEAD OF UNIONING IT. When two dimensions owned the same source, the
     second overwrote the first and its verified quotables went with it. Entry [1] of one log kept 4 of
     its 10 quotes and nothing reported the loss. Fixed by unioning quotables and Supports clauses, and
     by preferring the stronger retrieval status.

MERGING ACROSS RUNS MATTERS AS MUCH AS ACROSS DIMENSIONS. A dimension that fails and is relaunched
produces a second output file, and the canonical source it owns then appears in both. Measured on
2026-08-07: the Scrum Guide was claimed by three dimensions across two runs, and without cross-file
merging it would have been three entries with their quotables split between them. Pass every run's
output file; the tool treats a cross-file collision exactly like a cross-dimension one.

WHAT THIS DOES NOT DO. It proves nothing about truth. It cannot tell whether a retrieval status is
honest, whether a Supports clause is accurate, or whether a quoted phrase appears in the page it sits
with. Those are the four-lens review's job (review-standards.md section 2). This tool moves fields
without losing them, and that is its whole claim.

The output is the entry block only, in the house form (bundle-pipeline.md phase 2, layout 1). The log's
framing, contested register and notes are written by hand, because they are judgment.

Usage:
    python tools/gen-research-log.py OUT.md RUN.json [RUN2.json ...]
"""
import argparse
import json
import pathlib
import re
import sys
from urllib.parse import urlsplit, urlunsplit

EM_DASH = chr(8212)
EN_DASH = chr(8211)

# Tier vocabulary per bundle-pipeline.md phase 2. The research schema emits a narrower enum than the
# log accepts, and agents in practice also return "standard", so it is mapped rather than rejected.
TIER_MAP = {
    "primary": "primary",
    "standard": "standards",
    "standards": "standards",
    "academic": "academic",
    "practitioner": "practitioner",
    "vendor": "vendor",
    "reference": "reference",
    "internal": "internal",
}

RETRIEVAL_ENUM = {"fetched-and-verified", "url-confirmed-not-read", "not-retrieved"}


def clean(text):
    """Collapse whitespace and remove the two dashes the repository forbids repo-wide.

    Source titles carry em-dashes routinely, and check B rejects them anywhere in a bundle, so this
    has to happen at generation time rather than being caught later by the gate.
    """
    if not text:
        return ""
    out = str(text).replace(EM_DASH, " - ").replace(EN_DASH, "-")
    return re.sub(r"\s+", " ", out).strip()


def normalise_url(url):
    """Key a source by a canonical form of its URL, so www and non-www variants collapse to one entry.

    This is bug 1. Two dimensions fetching http://example.com/x/ and https://www.example.com/x are
    holding the same source, and a raw-string key files them under two numbers.
    """
    if not url:
        return ""
    try:
        parts = urlsplit(url.strip())
    except ValueError:
        return url.strip().lower()
    host = (parts.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = (parts.path or "").rstrip("/")
    return urlunsplit(("https", host, path, parts.query, "")).lower()


def load_runs(paths):
    """Return every dimension result across every run file, in order."""
    results = []
    for path in paths:
        data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
        # A Workflow task-output file wraps the script's return value in "result".
        block = data.get("result", data)
        results.extend(block.get("results", []))
    return results


def merge(results):
    """Collapse owned sources into one entry each, unioning rather than replacing.

    Returns (entries_by_key, key_order, collisions). A collision is reported, never silently resolved:
    two dimensions owning one source is normal and expected, two ENTRIES for it is a defect the
    research-log contract check would fail on.
    """
    entries, order, collisions = {}, [], {}
    for dim in results:
        dimension = clean(dim.get("dimension", "unknown"))
        for src in dim.get("owned_sources", []):
            key = normalise_url(src.get("url", "")) or clean(src.get("identity", ""))
            if key not in entries:
                entries[key] = {
                    "identity": clean(src.get("identity")),
                    "url": (src.get("url") or "").strip(),
                    "tier": TIER_MAP.get((src.get("tier") or "").lower(), "reference"),
                    "status": (src.get("retrieval_status") or "").strip(),
                    "supports": [],
                    "quotable": [],
                    "dimensions": [dimension],
                }
                order.append(key)
            else:
                entry = entries[key]
                if dimension not in entry["dimensions"]:
                    entry["dimensions"].append(dimension)
                collisions.setdefault(key, []).append(dimension)
                # Prefer the stronger status: only fetched-and-verified may carry a quotation, and a
                # dimension that actually read the body outranks one that only confirmed the URL.
                if src.get("retrieval_status") == "fetched-and-verified":
                    entry["status"] = "fetched-and-verified"
            # THE UNION, and this is bug 2. Both lists accumulate across every dimension that owned
            # this source. Replacing the dict here is what discarded verified quotes.
            supports = clean(src.get("supports"))
            if supports and supports not in entries[key]["supports"]:
                entries[key]["supports"].append(supports)
            for phrase in src.get("quotable") or []:
                phrase = clean(phrase)
                if phrase and phrase not in entries[key]["quotable"]:
                    entries[key]["quotable"].append(phrase)
    return entries, order, collisions


def render(entries, order, group=True):
    """Emit the house form. Numbering is contiguous across the whole file, grouping only moves rows."""
    numbering = {key: n for n, key in enumerate(order, 1)}
    if not group:
        return "\n".join(line for key in order for line in render_entry(entries[key], numbering[key]))

    groups, seen = [], set()
    for key in order:
        first = entries[key]["dimensions"][0]
        if first not in seen:
            seen.add(first)
            groups.append(first)
    lines = []
    for name in groups:
        lines.append("### " + name)
        lines.append("")
        for key in order:
            if entries[key]["dimensions"][0] == name:
                lines.extend(render_entry(entries[key], numbering[key]))
    return "\n".join(lines)


def render_entry(entry, number):
    status = entry["status"] if entry["status"] in RETRIEVAL_ENUM else "not-retrieved"
    quotable = entry["quotable"]
    supports = list(entry["supports"])
    if quotable and status != "fetched-and-verified":
        # Honest retrieval: only a body that was read may be quoted. Drop the phrases and SAY SO in
        # the entry, rather than letting a quotation hang off a source nobody opened.
        quotable = []
        supports.append(
            "Quotable phrases were dropped by tools/gen-research-log.py because this entry is not "
            "fetched-and-verified, and only a source that was read may be quoted."
        )
    lines = [
        "**[" + str(number) + "] " + entry["identity"] + ".** " + entry["tier"] + ". **" + status + ".**",
        "`" + entry["url"] + "`" if entry["url"] else "No URL. State the reason in Supports.",
        "Supports: " + " ".join(supports),
    ]
    lines.extend('Quotable: "' + phrase + '"' for phrase in quotable)
    lines.append("")
    return lines


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("out", help="file to write the entry block to")
    parser.add_argument("runs", nargs="+", help="one or more research fan-out output files")
    parser.add_argument("--flat", action="store_true", help="do not group entries under dimension headings")
    args = parser.parse_args(argv)

    entries, order, collisions = merge(load_runs(args.runs))
    pathlib.Path(args.out).write_text(render(entries, order, group=not args.flat), encoding="utf-8")

    fetched = sum(1 for k in order if entries[k]["status"] == "fetched-and-verified")
    quoted = sum(1 for k in order if entries[k]["quotable"])
    phrases = sum(len(entries[k]["quotable"]) for k in order)
    print(str(len(order)) + " unique source(s) from " + str(len(args.runs)) + " run(s) -> " + args.out)
    print("  " + str(fetched) + " fetched-and-verified, " + str(quoted) + " carry " + str(phrases) + " quotable phrase(s)")
    if collisions:
        print("  " + str(len(collisions)) + " source(s) owned by more than one dimension, MERGED not duplicated:")
        for key, dims in collisions.items():
            print("    " + key)
            print("      also claimed by: " + "; ".join(d[:70] for d in dims))
    else:
        print("  no source was owned by more than one dimension")
    print()
    print("      not verified: whether any retrieval status is honest, whether a Supports clause is")
    print("      accurate, or whether a quoted phrase appears in the page it sits with. This tool moves")
    print("      fields without losing them. Judging them is the four-lens review's job.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
