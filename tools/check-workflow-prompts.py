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

It does NOT prove the script runs. Only invoking the Workflow tool proves that. This catches the one
shape that has actually broken the harness, which is worth more than a check that aspires to prove
loadability and cannot.

CORRECTED 2026-08-10. The paragraph above used to end "and no check in this repository can stand in
for it", about proving the script LOADS. That was too strong, and it discouraged the obvious next
step for two days. A static parse IS available, and this check now does it: see wrapped_parse.
Parsing is necessary and not sufficient - imports, globals and the runtime contract remain unproven
by anything static - so the claim narrows rather than disappears.

THE TWO CHECKS ARE COMPLEMENTARY AND NEITHER IS REDUNDANT. Do not delete the backtick heuristic on
the grounds that a parser now runs. The 2026-08-05 defect is the reason: its stray backticks
REBALANCED into expressions Node's parser accepts, which is exactly why node --check returned 0 on
a file the runtime refused. A parse check cannot see that shape by construction. Conversely the
heuristic cannot see an unbalanced brace, a missing comma, or any of the ordinary syntax errors the
parser catches immediately. Each covers the other's blind spot.

WHY THE SEARCH PATH WIDENED, 2026-08-08.

This check originally globbed `.claude/workflows/*.js` and found exactly one script. The EV-1 eval
harness at evals/harness/output-eval.workflow.mjs is a workflow script by every definition that
matters here - it holds agent prompts, it is loaded by the same runtime, and it dies the same way -
and it sat outside both the directory and the extension this check looked for. So a tool written
because a broken harness is invisible until someone runs it was not looking at the harness that had
most recently been written.

The lesson is not "remember to add new files". It is that a check scoped by a hardcoded directory
silently narrows every time the tree grows. Discovery is now by shape (a workflows directory, or a
*.workflow.* name) across the tracked tree, and the script count is printed on every run so a
scope that collapses to one file is visible rather than reassuring.
"""
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Discovery is by shape, not by one hardcoded path. Both patterns are load-bearing: the first is
# the conventional home, the second catches a harness that lives beside the thing it tests.
SCRIPT_GLOBS = (
    ".claude/workflows/*.js",
    ".claude/workflows/*.mjs",
    "**/*.workflow.js",
    "**/*.workflow.mjs",
)

SKIP_PARTS = {"node_modules", "_local", ".git"}

# `word` or `word-with-dashes` in prose. Short on purpose: a long backticked span is far more
# likely to be a real template literal than a markdown code span.
PROSE_TICK = re.compile(r"`[\w.\-/]{1,40}`")

# A line doing any of these is code, and its backticks are structural.
CODE_HINTS = ("${", "=", "(", "require", "import ")


def wrapped_parse(script):
    """Parse a workflow script the way the runtime actually treats it.

    Returns (status, detail) where status is one of "ok", "fail", "skip".

    WHY THE OBVIOUS COMMAND DOES NOT WORK. A workflow script's body runs inside an async function,
    so a top-level `return` is legal there. In an ESM file it is not, and `node --check` reads a
    .mjs file as ESM. So running `node --check` directly on evals/harness/output-eval.workflow.mjs
    reports SyntaxError: Illegal return statement on a file that is completely correct, and has
    done so since the harness was written. Measured 2026-08-10, by walking into it.

    That asymmetry is why the harness went unparsed while .claude/workflows/build-bundle.js did
    not: the .js file is CommonJS, where top-level return is allowed, so the naive command happened
    to work there and silently did not generalise.

    Wrapping the body in an async function reproduces the runtime's own framing, and `export` is
    stripped because an export statement inside a function is illegal.
    """
    text = script.read_text(encoding="utf-8")
    wrapped = "async function __wrap(){\n" + text.replace("export const meta", "const meta", 1) + "\n}\n"
    with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False, encoding="utf-8") as fh:
        fh.write(wrapped)
        tmp = fh.name
    try:
        proc = subprocess.run(
            ["node", "--check", tmp], capture_output=True, text=True
        )
    except (OSError, FileNotFoundError):
        return "skip", "node not on PATH"
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass
    if proc.returncode == 0:
        return "ok", ""
    # Line numbers refer to the wrapped copy, which is offset by the one line the wrapper adds.
    first = next((ln for ln in proc.stderr.splitlines() if "Error" in ln), proc.stderr.strip()[:200])
    return "fail", first


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


def discover():
    found = set()
    for pattern in SCRIPT_GLOBS:
        for path in ROOT.glob(pattern):
            if not path.is_file():
                continue
            if SKIP_PARTS & set(path.relative_to(ROOT).parts):
                continue
            found.add(path)
    return sorted(found)


def main():
    scripts = discover()
    if not scripts:
        print("workflow prompts: no workflow scripts found, nothing to check")
        print("      searched: %s" % ", ".join(SCRIPT_GLOBS))
        return 0

    failures = 0
    parse_failures = 0
    skipped_parse = 0
    for script in scripts:
        hits = suspect_lines(script.read_text(encoding="utf-8"))
        rel = script.relative_to(ROOT).as_posix()

        status, detail = wrapped_parse(script)
        if status == "skip":
            skipped_parse += 1
            parse_note = "  (parse SKIPPED: %s)" % detail
        elif status == "fail":
            parse_failures += 1
            parse_note = "  (PARSE FAILED)"
        else:
            parse_note = "  (parses)"

        if not hits and status != "fail":
            print("  OK    %s%s" % (rel, parse_note))
            continue
        print("  FAIL  %s%s" % (rel, parse_note))
        if status == "fail":
            print("        does not parse when wrapped as the runtime wraps it:")
            print("        %s" % detail)
        failures += len(hits)
        for n, tok, ctx in hits:
            print("        line %d: %s closes the prompt's template literal" % (n, tok))
            print("        %s" % ctx)

    print()
    print("workflow prompts: %d script(s) checked" % len(scripts))
    if parse_failures:
        print("FAIL  %d script(s) do not parse when wrapped as the runtime wraps them." % parse_failures)
        print("      Do NOT reach for `node --check` on a .mjs workflow script to confirm this. It")
        print("      reads the file as ESM, where the top-level return every workflow body ends with")
        print("      is illegal, so it reports a SyntaxError on a perfectly correct file.")
        return 1
    if failures:
        print("FAIL  %d backtick(s) used as markdown inside a prompt string." % failures)
        print("      Use double quotes instead. A backtick there closes the template literal and")
        print("      the Workflow runtime cannot load the script, even though node --check passes.")
        return 1

    print("OK  no backtick is used as markdown inside a prompt string, and every script parses.")
    if skipped_parse:
        print("      %d parse check(s) SKIPPED because node is not on PATH." % skipped_parse)
    print("      not proven here: that a script actually RUNS. Parsing is necessary and not")
    print("      sufficient; imports, globals and the runtime contract are still only proven by")
    print("      invoking the Workflow tool. This proves the file is syntactically loadable, which")
    print("      is strictly more than this check claimed before 2026-08-10.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
