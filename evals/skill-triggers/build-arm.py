#!/usr/bin/env python3
"""build-arm.py - build a test copy of the plugin for the skill-trigger suite.

A `claude plugin eval` run needs a plugin folder with an `evals/` folder inside it. This script
builds one outside the repository: the plugin manifest, every skill under `skills/`, and one eval
case per entry in `cases.json`. The skills come from the working tree, or from any git ref with
`--ref`, which is how the fragile cases run on the old wording and the new one in one session.

What the copy leaves out, on purpose:
- The MCP server. The manifest's `mcpServers` entry is dropped, because the suite measures whether
  the skill DESCRIPTIONS make an agent load a skill, and the server's tools would compete with them.
- The templates. Only `skills/` is copied, as in every test round on 2026-11-25 and 2026-11-26, so
  results stay comparable with those rounds. A side effect: an agent that loads the fill skill finds
  no bundle to fill. That is fine, because the grader only checks which skill loaded.

Graders match by skill-name prefix, `plt-fill-` or `plt-grade-`, so a split that adds a second fill
skill or grade skill needs no grader change. A split that merges filling and grading into one skill
per group (shape 7c in ADR 0093) does need new graders.

Usage:
    python evals/skill-triggers/build-arm.py --label new
    python evals/skill-triggers/build-arm.py --label base --ref v0.28.1
    python evals/skill-triggers/build-arm.py --label new --out <folder>

Prints the arm's path. Pure standard library plus git.
"""

import argparse
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
CASES_PATH = os.path.join(HERE, "cases.json")

# The prefix each expectation must load. "none" must load no skill of this plugin.
PREFIX = {"fill": "plt-fill-", "grade": "plt-grade-", "none": "plt-"}


def grader(expect):
    pattern = '\'"skill"\\s*:\\s*"(?:[\\w-]+:)?' + PREFIX[expect] + ('[\\w-]+"\'' if expect != "none" else "'")
    limits = "min: 0\nmax: 0\n" if expect == "none" else ""
    return f"---\ntype: tool_used\ntool: Skill\narm: both\n{limits}input_match: {pattern}\n---\n"


def prompt_file(case):
    tags = ", ".join(case["tags"])
    return (f"---\nname: {case['name']}\ntags: [{tags}]\nmax_turns: 3\ntimeout_seconds: 180\n"
            f"allowed_tools: [Skill, Read, Glob, Grep]\n---\n\n{case['prompt']}\n")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))


def copy_plugin(dst, ref):
    """Copy the manifest and skills/ from the working tree, or from a git ref."""
    if ref is None:
        shutil.copytree(os.path.join(ROOT, "skills"), os.path.join(dst, "skills"))
        with open(os.path.join(ROOT, ".claude-plugin", "plugin.json"), encoding="utf-8") as f:
            man = json.load(f)
    else:
        tar = subprocess.run(["git", "-C", ROOT, "archive", "--format=tar", ref, "skills", ".claude-plugin/plugin.json"],
                             capture_output=True)
        if tar.returncode != 0:
            sys.exit(f"git archive {ref} failed: {tar.stderr.decode(errors='replace').strip()}")
        with tarfile.open(fileobj=io.BytesIO(tar.stdout)) as t:
            t.extractall(dst, filter="data")
        with open(os.path.join(dst, ".claude-plugin", "plugin.json"), encoding="utf-8") as f:
            man = json.load(f)
    man.pop("mcpServers", None)
    write(os.path.join(dst, ".claude-plugin", "plugin.json"), json.dumps(man, indent=2) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--label", required=True, help="names the arm folder, such as new or base")
    ap.add_argument("--ref", help="a git ref to take skills/ and the manifest from; default is the working tree")
    ap.add_argument("--out", default=os.path.join(tempfile.gettempdir(), "plt-skill-triggers"),
                    help="parent folder for the arm; must be outside the repository")
    args = ap.parse_args()

    out = os.path.abspath(args.out)
    if os.path.commonpath([out, ROOT]) == ROOT:
        sys.exit("--out must be outside the repository, so run output can never be committed")
    dst = os.path.join(out, f"arm-{args.label}")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    copy_plugin(dst, args.ref)

    with open(CASES_PATH, encoding="utf-8") as f:
        cases = json.load(f)["cases"]
    for c in cases:
        d = os.path.join(dst, "evals", c["name"])
        write(os.path.join(d, "prompt.md"), prompt_file(c))
        write(os.path.join(d, "graders", "skill.md"), grader(c["expect"]))
    skills = sorted(os.listdir(os.path.join(dst, "skills")))
    print(f"built {dst}: {len(cases)} cases, skills {', '.join(skills)}, from {args.ref or 'the working tree'}")
    print(dst)


if __name__ == "__main__":
    main()
