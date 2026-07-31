#!/usr/bin/env python3
"""A local cache of fetched source pages, so the same URL is downloaded once per bundle instead of five times.

WHY THIS EXISTS
---------------
Building one bundle costs roughly 1.5 to 2M tokens, and measurement on 2026-07-30 showed that close to half
of that is re-reading. Two specific wastes:

  1. DUPLICATE FETCHING ACROSS RESEARCH DIMENSIONS. Google's re:Work guide was fetched by four of the five
     `okrs` research agents and then again by the verifier. Five downloads of one page. Every heavily cited
     source has the same shape, and each fetch is 3-5K tokens of converted markdown.

  2. VERIFICATION RE-DOWNLOADING WHAT RESEARCH ALREADY READ. The pre-draft verification pass on `okrs` cost
     863K tokens, most of it re-fetching pages an agent had read an hour earlier and discarded.

With a cache, the second cost nearly vanishes: confirming a quote becomes a local string search rather than a
network round trip. That matters twice over, because quote fabrication inside a research log is the one defect
class that is NOT otherwise mechanizable. A provenance linter cannot catch it, since the log itself is what is
wrong. Only re-reading the source catches it, and this makes re-reading cheap.

WHERE IT LIVES
--------------
`_local/source-cache/`, which is gitignored. Deliberately NOT the session scratchpad: a scratchpad is keyed to
one session's UUID, so a cache there would be thrown away between sessions and could never serve the second
bundle. `_local/` survives, and is already the agreed home for local working data.

THE HONESTY CONSTRAINT, WHICH IS THE POINT
------------------------------------------
This library's central quality claim is honest retrieval: a source is tagged with how it was actually
retrieved, and only `fetched-and-verified` may be quoted. A cache could quietly corrupt that, by letting an
author write "fetched-and-verified" today on the strength of a download from months ago.

So every entry records the timestamp of the ACTUAL network fetch, `get` prints that date on every hit, and
entries past the staleness horizon are reported as STALE rather than served silently. A stale hit is a prompt
to re-fetch, not a licence to quote. The research log records when a source was read, and this tool is what
makes that date true rather than assumed.

WHAT IT DOES NOT DO
-------------------
It does not fetch. It has no network access and no opinion about how content arrives; it stores what it is
given and hands it back. It cannot tell whether the page changed since it was stored, and it cannot tell
whether the stored text was ever accurate. Freshness past the horizon is a human or agent decision.
"""
import argparse
import hashlib
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CACHE = Path(__file__).resolve().parent.parent / "_local" / "source-cache"

# A hit older than this is reported STALE. Chosen to comfortably outlive one bundle build (hours) while
# expiring well inside the interval over which a live page can meaningfully change.
STALE_DAYS = 14

HEADER = "<!-- source-cache\nurl: {url}\nfetched: {fetched}\nbytes: {n}\n-->\n"


def key(url: str) -> str:
    return hashlib.sha1(url.strip().encode("utf-8")).hexdigest()


def path_for(url: str) -> Path:
    return CACHE / f"{key(url)}.md"


def parse(text: str) -> tuple[dict, str]:
    """Split a cache file into its header fields and its body."""
    if not text.startswith("<!-- source-cache"):
        return {}, text
    end = text.find("-->\n")
    if end == -1:
        return {}, text
    meta = {}
    for line in text[: end].splitlines()[1:]:
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
    return meta, text[end + 4:]


def age_days(meta: dict) -> float | None:
    stamp = meta.get("fetched")
    if not stamp:
        return None
    try:
        when = datetime.fromisoformat(stamp)
    except ValueError:
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - when).total_seconds() / 86400


def cmd_get(args) -> int:
    p = path_for(args.url)
    if not p.exists():
        print(f"MISS  {args.url}", file=sys.stderr)
        print("      Not cached. Fetch it, then store it with:", file=sys.stderr)
        print(f"      python tools/source-cache.py put \"{args.url}\" --file <path>", file=sys.stderr)
        return 1
    meta, body = parse(p.read_text(encoding="utf-8"))
    age = age_days(meta)
    if age is not None and age > STALE_DAYS and not args.allow_stale:
        print(f"STALE  {args.url}", file=sys.stderr)
        print(f"       Cached {age:.1f} days ago (horizon {STALE_DAYS}). Re-fetch before quoting from it.",
              file=sys.stderr)
        print("       Pass --allow-stale to read it anyway, for orientation only.", file=sys.stderr)
        return 2
    note = f"fetched {meta.get('fetched', 'unknown')}"
    if age is not None:
        note += f" ({age:.1f} days ago)"
    print(f"HIT  {args.url}  {note}", file=sys.stderr)
    sys.stdout.write(body)
    return 0


def cmd_put(args) -> int:
    body = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    if not body.strip():
        print("REFUSED  empty body; a cache entry with no content is worse than a miss", file=sys.stderr)
        return 1
    CACHE.mkdir(parents=True, exist_ok=True)
    stamp = args.fetched or datetime.now(timezone.utc).isoformat(timespec="seconds")
    p = path_for(args.url)
    p.write_text(HEADER.format(url=args.url, fetched=stamp, n=len(body)) + body,
                 encoding="utf-8", newline="\n")
    print(f"STORED  {args.url}  -> {p.name}  ({len(body)} bytes)", file=sys.stderr)
    return 0


def cmd_stat(args) -> int:
    p = path_for(args.url)
    if not p.exists():
        print(f"MISS   {args.url}")
        return 1
    meta, body = parse(p.read_text(encoding="utf-8"))
    age = age_days(meta)
    state = "STALE" if (age is not None and age > STALE_DAYS) else "HIT"
    print(f"{state}   {args.url}")
    print(f"       file    {p.name}")
    print(f"       fetched {meta.get('fetched', 'unknown')}" + (f"  ({age:.1f} days ago)" if age else ""))
    print(f"       bytes   {len(body)}")
    return 0


def cmd_list(args) -> int:
    if not CACHE.exists():
        print("source cache: empty (no _local/source-cache directory yet)")
        return 0
    rows = []
    for p in sorted(CACHE.glob("*.md")):
        meta, body = parse(p.read_text(encoding="utf-8"))
        rows.append((meta.get("url", "?"), age_days(meta), len(body)))
    if not rows:
        print("source cache: empty")
        return 0
    fresh = sum(1 for _, a, _ in rows if a is None or a <= STALE_DAYS)
    total_bytes = sum(n for _, _, n in rows)
    print(f"source cache: {len(rows)} entr(y/ies), {fresh} fresh, {len(rows) - fresh} stale, "
          f"{total_bytes // 1024} KB")
    print(f"      staleness horizon {STALE_DAYS} days; a stale hit is a prompt to re-fetch, not a licence")
    print(f"      location {CACHE}  (gitignored)")
    if args.verbose:
        for url, age, n in sorted(rows, key=lambda r: (r[1] is None, -(r[1] or 0))):
            mark = "stale" if (age is not None and age > STALE_DAYS) else "fresh"
            print(f"        {mark}  {(f'{age:.1f}d' if age is not None else '  ?  '):>7}  "
                  f"{n // 1024:>4}KB  {url[:96]}")
    return 0


def cmd_prune(args) -> int:
    if not CACHE.exists():
        print("nothing to prune")
        return 0
    dropped = 0
    for p in sorted(CACHE.glob("*.md")):
        meta, _ = parse(p.read_text(encoding="utf-8"))
        age = age_days(meta)
        if age is not None and age > args.days:
            p.unlink()
            dropped += 1
    print(f"pruned {dropped} entr(y/ies) older than {args.days} days")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("get", help="print a cached page body; exit 1 on miss, 2 on stale")
    g.add_argument("url")
    g.add_argument("--allow-stale", action="store_true", help="serve a stale entry for orientation only")
    g.set_defaults(fn=cmd_get)

    p = sub.add_parser("put", help="store a fetched page body from a file or stdin")
    p.add_argument("url")
    p.add_argument("--file", help="read the body from this path instead of stdin")
    p.add_argument("--fetched", help="ISO timestamp of the ACTUAL network fetch; defaults to now")
    p.set_defaults(fn=cmd_put)

    s = sub.add_parser("stat", help="report whether a URL is cached, and how old it is")
    s.add_argument("url")
    s.set_defaults(fn=cmd_stat)

    l = sub.add_parser("list", help="inventory the cache")
    l.add_argument("-v", "--verbose", action="store_true")
    l.set_defaults(fn=cmd_list)

    pr = sub.add_parser("prune", help="delete entries older than N days")
    pr.add_argument("--days", type=int, default=STALE_DAYS)
    pr.set_defaults(fn=cmd_prune)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
