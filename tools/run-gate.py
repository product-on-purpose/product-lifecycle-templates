#!/usr/bin/env python3
"""
run-gate.py - run locally what CI runs, and say plainly what it did not run.

WHY THIS EXISTS.
Until 2026-09-05 the way to check this repository before pushing was to loop over `tools/check-*.py`
and `tools/test-*.py`. That is 21 scripts. CI runs **30 steps**. The difference was invisible, and
"all gates pass" meant "the 21 things I happened to iterate passed", which is a different claim.

It cost a red build on the em-dash check, which is an inline heredoc in `ci.yml` rather than a script
under `tools/`, so no glob over that directory could ever have found it. The number was available the
whole time: `check-counts.py` reports the CI step count from `ci.yml` and it said 30.

**So the check list is derived from `ci.yml` and never from a directory listing.** Add a step to CI
and this runs it, whether or not it is a Python file, without anyone remembering to update a glob.

WHAT IT REFUSES TO DO.
Claim completeness it does not have. Every step it skips is printed with a reason, the summary counts
ran and skipped separately, and there is no output line that says everything passed. The failure this
tool exists to prevent is a confident summary over a partial run, so it does not produce one.

WHAT IT CANNOT RUN, AND WHY THAT IS FINE.
Three steps are GitHub actions (`uses:`) that provision the runner: checkout, setup-python, setup-node.
Locally their effect is the working tree and the interpreters you already have. They are reported as
skipped rather than silently dropped, because "27 of 30, and here are the 3" is a true statement and
"all gates pass" is not.

Usage:
    python tools/run-gate.py                # every runnable step, including the network G2 gate
    python tools/run-gate.py --offline      # skip the steps needing network, and say so
    python tools/run-gate.py --install      # also run the pip install step
    python tools/run-gate.py --list         # show the steps and their disposition, run nothing

Exit 0 only if every step that ran passed; 1 otherwise.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
CI_PATH = os.path.join(ROOT, ".github", "workflows", "ci.yml")

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
DIM = "\033[2m"
OFF = "\033[0m"

# Steps that touch the network. Named rather than sniffed, because guessing from the command text
# would silently reclassify a step the day someone rewords it.
NETWORK_STEPS = {"Standard conformance gate (G2, self-hosting)"}
# Steps that modify the ambient environment rather than checking the tree.
INSTALL_STEPS = {"Install gate dependencies"}


def load_steps():
    try:
        import yaml
    except ImportError:
        print("run-gate requires PyYAML (pip install pyyaml) to read ci.yml.")
        raise SystemExit(1)
    with open(CI_PATH, encoding="utf-8") as f:
        wf = yaml.safe_load(f)
    out = []
    for job_name, job in (wf.get("jobs") or {}).items():
        for step in job.get("steps") or []:
            out.append((job_name, step))
    return out


def find_bash():
    for c in ("bash", "/usr/bin/bash", "/bin/bash",
              r"C:\Program Files\Git\bin\bash.exe"):
        p = shutil.which(c) if os.sep not in c else (c if os.path.isfile(c) else None)
        if p:
            return p
    return None


def disposition(step, args):
    """(action, reason) where action is 'run' or 'skip'."""
    name = step.get("name", "")
    if "uses" in step:
        return "skip", ("a GitHub action that provisions the runner (" + step["uses"]
                        + "); locally its effect is the tree and interpreters you already have")
    if name in INSTALL_STEPS and not args.install:
        return "skip", "installs into the ambient Python; pass --install to run it"
    if name in NETWORK_STEPS and args.offline:
        return "skip", "needs network (clone + npm ci); --offline was given"
    if "run" not in step:
        return "skip", "step has neither uses: nor run:"
    return "run", ""


def main():
    ap = argparse.ArgumentParser(prog="run-gate.py",
                                 description="Run locally what CI runs, and report what it did not.")
    ap.add_argument("--offline", action="store_true", help="skip steps needing network")
    ap.add_argument("--install", action="store_true", help="also run the dependency install step")
    ap.add_argument("--list", action="store_true", help="show dispositions and run nothing")
    args = ap.parse_args()

    steps = load_steps()
    bash = find_bash()
    if bash is None and not args.list:
        print(RED + "ERROR" + OFF + "  no bash found; CI steps are shell commands and two are heredocs")
        return 1

    tmp = tempfile.mkdtemp(prefix="run-gate-")
    ran, failed, skipped = [], [], []
    try:
        for i, (job, step) in enumerate(steps, 1):
            name = step.get("name", step.get("uses", "step " + str(i)))
            action, reason = disposition(step, args)

            if args.list:
                mark = (GREEN + "run " + OFF) if action == "run" else (YELLOW + "skip" + OFF)
                print("  %2d  %s  %-46s %s" % (i, mark, name[:46], DIM + reason + OFF if reason else ""))
                continue

            if action == "skip":
                skipped.append((name, reason))
                print("  %2d  %sSKIP%s  %-46s %s" % (i, YELLOW, OFF, name[:46], DIM + reason + OFF))
                continue

            env = dict(os.environ)
            env.update({k: str(v) for k, v in (step.get("env") or {}).items()})
            # The three runner variables the G2 step uses. Supplied rather than stubbed, so the step
            # runs for real instead of running a different command than CI runs.
            env.setdefault("GITHUB_WORKSPACE", ROOT)
            env.setdefault("RUNNER_TEMP", tmp)

            proc = subprocess.run([bash, "-e", "-c", step["run"]], cwd=ROOT, env=env,
                                  capture_output=True, text=True)
            if proc.returncode == 0:
                ran.append(name)
                print("  %2d  %sPASS%s  %s" % (i, GREEN, OFF, name[:46]))
            else:
                failed.append((name, proc))
                print("  %2d  %sFAIL%s  %s" % (i, RED, OFF, name[:46]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if args.list:
        return 0

    print()
    for name, proc in failed:
        print(RED + "FAILED: " + OFF + name)
        tail = (proc.stdout or "").strip().split("\n")[-12:] + \
               (proc.stderr or "").strip().split("\n")[-12:]
        for line in [t for t in tail if t.strip()][-14:]:
            print("      " + line[:160])
        print()

    total = len(steps)
    print("ran %d of %d step(s): %d passed, %d failed. Skipped %d."
          % (len(ran) + len(failed), total, len(ran), len(failed), len(skipped)))
    if skipped:
        print(DIM + "      Skipped, and why, so this is not read as a clean run:" + OFF)
        for name, reason in skipped:
            print(DIM + "        - " + name[:44] + ": " + reason + OFF)
    print(DIM + "      The step list comes from .github/workflows/ci.yml, never from a directory\n"
          "      listing, because the defect this tool exists for was a check that lived\n"
          "      outside tools/ and so could not be found by globbing it." + OFF)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
