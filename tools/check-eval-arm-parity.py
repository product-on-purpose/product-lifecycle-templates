#!/usr/bin/env python3
"""Fail if the eval's two arm prompts stop sharing an identical discipline block.

WHY THIS EXISTS

The EV-1 pilot could not interpret its own headline number because the control arm was told to produce
decision-usefulness and the treatment arm was not, while held-out criteria scored exactly that. The fix was
to give the treatment arm the identical seven discipline points. "Identical" is doing all the work: a
paraphrase would leave open the argument that one arm received better-worded advice, which is the confound
the fix removes.

That identity now lives in two hand-maintained files. Every time this repository has held one fact in two
places without a check, the copies drifted: the atlas built flags, the ADR index, the changelog, five prose
counts, and the templates README inventory. Drift here would silently un-match the arms and quietly
invalidate every number produced afterwards, with nothing failing and nothing looking wrong.

WHAT IT CHECKS

The bullet run inside each file's blockquoted prompt must be byte-identical. It deliberately does NOT
compare the surrounding framing: the control is told to structure its document freely and the treatment is
told to follow a template, and that difference IS the experiment's independent variable. Making the framing
identical would delete the thing being measured.

WHAT IT CANNOT CHECK

That the workflow actually delivers both blocks to their arms. It compares two documents, not a run.
"""

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

CONTROL = REPO / "evals" / "harness" / "control-prompt.md"
TREATMENT = REPO / "evals" / "harness" / "treatment-prompt.md"

# A bullet line, or a wrapped continuation of one, inside a markdown blockquote.
BULLET = re.compile(r"^> - ")
CONTINUATION = re.compile(r"^>   ")


def discipline_block(path):
    """Return the maximal run of blockquoted bullets, starting at the first one.

    The run ends at the first line that is neither a bullet nor a wrapped continuation, which in both
    files is the bare '>' separating the bullets from the closing framing paragraph.
    """
    if not path.exists():
        return None, f"{path.relative_to(REPO)}: file does not exist"

    lines = path.read_text(encoding="utf-8").splitlines()

    start = None
    for i, line in enumerate(lines):
        if BULLET.match(line):
            start = i
            break
    if start is None:
        return None, f"{path.relative_to(REPO)}: found no blockquoted bullet list"

    run = []
    for line in lines[start:]:
        if BULLET.match(line) or CONTINUATION.match(line):
            run.append(line)
        else:
            break

    return run, None


def main():
    control, err_c = discipline_block(CONTROL)
    treatment, err_t = discipline_block(TREATMENT)

    for err in (err_c, err_t):
        if err:
            print(f"FAIL: {err}")
            return 1

    n_control = sum(1 for line in control if BULLET.match(line))
    n_treatment = sum(1 for line in treatment if BULLET.match(line))

    if control == treatment:
        print(
            f"OK: the control and treatment arms share an identical discipline block "
            f"({n_control} points, {len(control)} lines)."
        )
        print(
            "     Framing is deliberately NOT compared: structural freedom is the independent variable."
        )
        return 0

    print("FAIL: the eval's two arm prompts no longer share an identical discipline block.")
    print(f"  control-prompt.md:   {n_control} bullet(s), {len(control)} line(s)")
    print(f"  treatment-prompt.md: {n_treatment} bullet(s), {len(treatment)} line(s)")
    print()

    width = max(len(control), len(treatment))
    shown = 0
    for i in range(width):
        c = control[i] if i < len(control) else "(absent)"
        t = treatment[i] if i < len(treatment) else "(absent)"
        if c != t:
            print(f"  line {i + 1} differs:")
            print(f"    control:   {c}")
            print(f"    treatment: {t}")
            shown += 1
            if shown == 5:
                print("  ... further differences not shown.")
                break

    print()
    print("The arms must be told the same things about what a good document does, so that the only")
    print("difference between them is whether one got a template. If this block was edited on purpose,")
    print("edit BOTH files, and version both prompts in their change logs: a change here changes every")
    print("number either arm has ever produced.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
