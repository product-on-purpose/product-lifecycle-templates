#!/usr/bin/env python3
"""Catch a backtick used as markdown inside a workflow prompt string.

WHY THIS EXISTS, AND WHY node --check DOES NOT REPLACE IT.

The workflow scripts in .claude/workflows/ hold their agent prompts in multi-line template
literals, which are delimited by backticks. Writing `location` in that prose, the way you would
in markdown, CLOSES the literal and reopens it. The Workflow runtime then refuses to load the
script with a parse error, and the whole run dies before a single agent starts.

The trap is that `node --check` PASSES on such a file. Measured on 2026-08-05: an edit that put
backticks around two words inside a lens prompt shipped through a green PR, passed `node --check`
with exit 0, and was rejected by the Workflow runtime at load. The backticks happened to rebalance
into expressions Node's parser tolerates. So the one static check available said the file was fine
while the file could not be invoked at all.

This is the second infrastructural failure in this harness that no gate could see. The first was
CRLF line endings making a syntactically perfect script unrunnable, fixed by pinning *.js to LF in
.gitattributes. Both share a shape worth naming: the script was CORRECT and NOT LOADABLE, and
reading it more carefully would never have revealed that.

WHAT THIS CHECKS, AND WHAT IT CANNOT.

It flags a backtick-quoted short token sitting in prose: `word` on a line carrying no template
interpolation, no assignment and no call. Those three exclusions are what keep legitimate one-line
template literals (`templates/${type}/${type}`, log(`...${n}...`)) from being reported.

It does NOT prove the script loads. Only invoking the Workflow tool proves that, and no check in
this repository can stand in for it. This catches the one shape that has actually broken the
harness, which is worth more than a check that aspires to prove loadability and cannot.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKFLOWS = ROOT / ".claude" / "workflows"

# `word` or `word-with-dashes` in prose. Short on purpose: a long backticked span is far more
# likely to be a real template literal than a markdown code span.
PROSE_TICK = re.compile(r"`[\w.\-/]{1,40}`")

# A line doing any of these is code, and its backticks are structural.
CODE_HINTS = ("${", "=", "(", "require", "import ")


def suspect_lines(text):
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        if "`" not in line:
            continue
        stripped = line.strip()
        if stripped.startswith("//") or stripped.startswith("*"):
            continue
        if any(h in line for h in CODE_HINTS):
            continue
        for m in PROSE_TICK.finditer(line):
            out.append((n, m.group(0), stripped[:96]))
    return out


def main():
    if not WORKFLOWS.is_dir():
        print("workflow prompts: no .claude/workflows/ directory, nothing to check")
        return 0

    scripts = sorted(WORKFLOWS.glob("*.js"))
    if not scripts:
        print("workflow prompts: no scripts found, nothing to check")
        return 0

    failures = 0
    for script in scripts:
        hits = suspect_lines(script.read_text(encoding="utf-8"))
        rel = script.relative_to(ROOT).as_posix()
        if not hits:
            print("  OK    %s" % rel)
            continue
        failures += len(hits)
        print("  FAIL  %s" % rel)
        for n, tok, ctx in hits:
            print("        line %d: %s closes the prompt's template literal" % (n, tok))
            print("        %s" % ctx)

    print()
    print("workflow prompts: %d script(s) checked" % len(scripts))
    if failures:
        print("FAIL  %d backtick(s) used as markdown inside a prompt string." % failures)
        print("      Use double quotes instead. A backtick there closes the template literal and")
        print("      the Workflow runtime cannot load the script, even though node --check passes.")
        return 1

    print("OK  no backtick is used as markdown inside a prompt string.")
    print("      not proven here: that the script actually loads. Only invoking the Workflow tool")
    print("      proves that, and nothing in CI can stand in for it. This catches the one shape")
    print("      that has really broken the harness, not every way a script can fail.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
