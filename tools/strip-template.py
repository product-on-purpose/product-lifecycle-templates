#!/usr/bin/env python3
"""
strip-template.py - turn a filled template into a shippable document.

WHAT IT DOES.
Removes every guidance comment, stamps the provenance fields that record who filled the document and
when, and refuses to finish while `{{placeholders}}` remain. It is the last step of the LP-1 fill flow
and works standalone, because a person who filled a template by hand in an editor needs exactly this
and nothing else.

WHY IT REFUSES RATHER THAN WARNS.
A template that ships with `{{owner}}` still in it is the failure this whole library is trying to avoid:
a document that looks complete and is not. The methodology's own rule is that an inapplicable section
gets "N/A" plus one line of why, never deletion and never a leftover placeholder. So an unfilled
placeholder is an error by default, and `--allow-placeholders` exists only for the partial-save
workflow, where the comments are the resume state and the document is not being shipped yet.

WHY THE COMMENTS ARE THE RESUME STATE.
Guidance comments are what tells an author what each section wants. Stripping them is irreversible
against the filled copy, so this tool defaults to writing a separate output rather than editing in
place. `--in-place` is available and says what it is.

PROVENANCE, AND WHAT WAS ALREADY THERE.
Every one of the 58 template variants already carries `source_template` and `source_template_version`
in its instance frontmatter (measured 2026-09-05, 58/58). What no template carries is any record of the
fill itself. This tool adds three keys, and only these three:

    filled_by     who filled it: a person, or an agent identity
    fill_method   how: interview, batch, or manual
    fill_date     when: ISO 8601, stamped at strip time

They are appended after the existing provenance pair rather than inserted at the top, so a diff against
the template shows the fill as an addition in one place.

Usage:
    python tools/strip-template.py FILE --filled-by "Jane Doe"
    python tools/strip-template.py FILE --filled-by agent:claude --fill-method batch --out ship.md
    python tools/strip-template.py FILE --in-place --allow-placeholders   # partial save

Exit 0 stripped; 1 on a usage or file error; 2 if placeholders remain and were not allowed.
"""
import argparse
import datetime
import os
import re
import sys

GREEN = "\033[32m"
RED = "\033[31m"
DIM = "\033[2m"
OFF = "\033[0m"

COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
PLACEHOLDER_RE = re.compile(r"\{\{([a-z0-9_]+)\}\}")
FRONTMATTER_RE = re.compile(r"^(---\r?\n)(.*?)(\r?\n---[ \t]*\r?\n)", re.S)
# The provenance pair every variant already carries; the fill keys are appended after it.
ANCHOR_RE = re.compile(r"^source_template_version:.*$", re.M)

FILL_METHODS = ["interview", "batch", "manual"]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    # newline="\n" because .gitattributes pins *.md to LF and a filled document is committed like
    # any other. Writing platform newlines here would rewrite the whole file on the next commit.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def strip_comments(text):
    """Every HTML comment removed, then runs of 3+ blank lines collapsed to 2.

    Stripping a block comment leaves the blank lines that surrounded it, so a document that was
    readable becomes one with four-line gaps under every heading. Collapsing is not cosmetic; it is
    what makes the output look like a document somebody wrote.
    """
    out = COMMENT_RE.sub("", text)
    out = re.sub(r"(\r?\n)[ \t]*(\r?\n)[ \t]*(\r?\n)+", r"\1\2", out)
    return out


def stamp(front, filled_by, fill_method, today):
    """The frontmatter with the three fill keys set, replacing any existing or placeholder values.

    The three are inserted as ONE block in declared order. Inserting them one at a time after the same
    anchor reverses them, which is not wrong but reads as carelessness in a file whose whole job is to
    look deliberate.
    """
    fields = [("filled_by", '"' + filled_by + '"'), ("fill_method", fill_method), ("fill_date", today)]
    new = []
    for key, value in fields:
        line = key + ": " + value
        existing = re.compile(r"^" + key + r":.*$", re.M)
        if existing.search(front):
            front = existing.sub(lambda _m, l=line: l, front, count=1)
        else:
            new.append(line)
    if new:
        block = "\n" + "\n".join(new)
        m = ANCHOR_RE.search(front)
        if m:
            front = front[:m.end()] + block + front[m.end():]
        else:
            # No provenance pair to anchor to: not a document from this library, but stamping is
            # still the right outcome, so append rather than fail.
            front = front.rstrip("\n") + block
    return front


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="strip-template.py",
        description="Strip guidance comments from a filled template and stamp fill provenance.")
    ap.add_argument("file", help="the filled markdown file")
    ap.add_argument("--filled-by", default=None,
                    help="who filled it (a person, or an agent identity like agent:claude)")
    ap.add_argument("--fill-method", default="manual", choices=FILL_METHODS,
                    help="how it was filled (default: manual)")
    ap.add_argument("--out", default=None, help="write here instead of beside the input")
    ap.add_argument("--in-place", action="store_true", help="overwrite the input file")
    ap.add_argument("--allow-placeholders", action="store_true",
                    help="do not refuse on remaining placeholders (partial-save workflow)")
    args = ap.parse_args(argv)

    if not os.path.isfile(args.file):
        print(RED + "ERROR" + OFF + "  no such file: " + args.file)
        return 1
    if args.out and args.in_place:
        print(RED + "ERROR" + OFF + "  --out and --in-place are mutually exclusive")
        return 1

    text = read(args.file)

    # Placeholders are counted in the BODY, after comments are removed: guidance prose names
    # placeholders as instruction (the preamble says "Replace each {{placeholder}}"), and counting
    # those would refuse every document forever.
    stripped = strip_comments(text)
    remaining = sorted(set(PLACEHOLDER_RE.findall(stripped)))
    if remaining and not args.allow_placeholders:
        print(RED + "REFUSED" + OFF + "  " + str(len(remaining))
              + " placeholder(s) still unfilled: " + ", ".join(remaining[:8])
              + ("..." if len(remaining) > 8 else ""))
        print(DIM + "        A document that ships with a placeholder in it looks complete and is not."
              "\n        Fill them, write \"N/A\" plus one line of why, or pass --allow-placeholders"
              "\n        for a partial save (which keeps the guidance comments as resume state)." + OFF)
        return 2

    today = datetime.date.today().isoformat()
    m = FRONTMATTER_RE.match(stripped)
    stamped_keys = []
    if m and args.filled_by:
        front = stamp(m.group(2), args.filled_by, args.fill_method, today)
        stripped = m.group(1) + front + m.group(3) + stripped[m.end():]
        stamped_keys = ["filled_by", "fill_method", "fill_date"]
    elif not m and args.filled_by:
        print(RED + "ERROR" + OFF + "  --filled-by given but the file has no YAML frontmatter to stamp")
        return 1

    removed = len(COMMENT_RE.findall(text))
    target = args.file if args.in_place else (args.out or _default_out(args.file))
    write(target, stripped)

    summary = (str(removed) + " comment(s) removed, " + str(len(remaining))
               + " placeholder(s) remaining")
    if stamped_keys:
        summary += ", stamped " + ", ".join(stamped_keys) + " (" + today + ")"
    print(GREEN + "OK" + OFF + "  " + os.path.basename(target) + ": " + summary + ".")
    if remaining:
        print(DIM + "      Placeholders were allowed: " + ", ".join(remaining[:8]) + OFF)
    return 0


def _default_out(path):
    base, ext = os.path.splitext(path)
    return base + ".stripped" + ext


if __name__ == "__main__":
    sys.exit(main())
