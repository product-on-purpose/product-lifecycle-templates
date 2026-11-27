#!/usr/bin/env python3
"""gen-skill-descriptions.py - write (or verify) both skill descriptions from manifest.json.

WHY THIS EXISTS.
An agent decides whether to load a skill by reading its description, and each description here
lists every document type by name. That list is the trigger: a type it leaves out may never reach
the skill (measured on 2026-11-25 and 2026-11-26; see ADR 0093). Until this script, the two lists
were hand-written copies of each other, kept in step by a release-process reminder. Now each
bundle's `trigger_name` meta field holds the phrase it is listed under, and this script writes
both descriptions from manifest.json, so a new bundle reaches the trigger list the way it already
reaches the manifest.

WHAT IT DOES NOT DECIDE.
The ORDER table below is the list's order, and it is hand-chosen. It is neither manifest order nor
family order, and the tests showed that a name's position changes how often it triggers, so this
script never sorts. A new bundle needs its id placed in ORDER, and the check fails until it is.
Bundles that share a phrase ("product or sprint backlog") carry the same `trigger_name` and sit next
to each other in ORDER; the phrase is written once, where the first of them sits.

THE CAP.
The Agent Skills specification caps `description` at 1,024 characters. This script fails when a
description would pass it. That failure is the signal to split the skills by family group, which
ADR 0093 describes and leaves to a confirming test. GROUPS is where that split would go: today
there is one group, holding every family, and both skills list it.

Usage:
    python tools/gen-skill-descriptions.py            # rewrite the description line in both SKILL.md files
    python tools/gen-skill-descriptions.py --check    # exit 1 if either description differs, or a rule fails
    python tools/gen-skill-descriptions.py --print    # print each description and its length

Pure standard library. Exit 0 if written or in sync; 1 on drift or a rule failure.
"""

import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
MANIFEST_PATH = os.path.join(ROOT, "manifest.json")

CAP = 1024

# One group today. A split would add groups, each naming the families it holds and its own ORDER.
GROUPS = {
    "all": {"families": "*"},
}

# Each skill: the group whose types it lists, and the sentence around the list. {count} is the
# number of bundles in the manifest, and {list} is the group's phrases.
SKILLS = {
    "plt-fill-template": {
        "group": "all",
        "text": "Selects and fills a product-document template from a {count}-bundle library, then grades it "
                "on that type's rubric. Use when writing a {list}.",
    },
    "plt-grade-doc": {
        "group": "all",
        "text": "Grades a product document on its type's rubric, with three fixes worth an hour. Use for a "
                "review, critique, second opinion or score of a {list}.",
    },
}

# The order the list names types in, as shipped in v0.28.1. Hand-chosen: do not sort it.
ORDER = {
    "all": [
        "prd", "epic", "user-stories", "use-case-specification", "acceptance-criteria",
        "product-backlog", "sprint-backlog", "change-request", "release-notes",
        "announcement-internal-comms", "risk-register", "raid-log", "issue-log", "change-log",
        "kpi-dashboard", "tracking-plan", "data-dictionary", "test-plan", "test-case",
        "requirements-traceability-matrix", "platform-device-support-matrix", "bug-report",
        "test-summary-report", "adr", "rfc", "sdd", "spike-report", "trade-study", "product-vision",
        "product-strategy", "product-roadmap", "lean-canvas", "lean-ux-canvas",
        "positioning-statement", "competitive-analysis", "okrs", "north-star-metrics",
        "problem-statement", "design-brief", "user-research-plan", "user-research-report",
        "project-brief", "business-case", "user-persona", "experiment-design-doc",
        "experiment-readout", "definition-of-done", "definition-of-ready", "design-principles",
        "product-principles", "test-strategy", "runbook", "launch-coordination-checklist",
        "production-readiness-review", "business-continuity-plan", "incident-postmortem",
        "sprint-retrospective-notes", "project-milestone-retrospective", "status-report",
    ],
}

DESC_RE = re.compile(r"^description: (.*)$", re.M)

GREEN = "\033[32m"
RED = "\033[31m"
OFF = "\033[0m"


def join_list(phrases):
    """'a, b, or c', the shape the shipped descriptions use."""
    if len(phrases) == 1:
        return phrases[0]
    return ", ".join(phrases[:-1]) + ", or " + phrases[-1]


def build(bundles, groups=GROUPS, skills=SKILLS, order=ORDER, cap=CAP):
    """Return ({skill: description}, [errors]). Pure, so the self-test can call it on fixtures."""
    errors = []
    by_id = {b["id"]: b for b in bundles}

    # Which group each bundle belongs to, by family.
    members = {g: [] for g in groups}
    for b in bundles:
        homes = [g for g, spec in groups.items()
                 if spec["families"] == "*" or b["family"] in spec["families"]]
        if len(homes) != 1:
            errors.append(f"{b['id']}: family {b['family']!r} is in {len(homes)} groups, not exactly one")
            continue
        members[homes[0]].append(b["id"])
        if not b.get("trigger_name"):
            errors.append(f"{b['id']}: no trigger_name in manifest.json")

    phrases = {}
    phrase_group = {}
    for g in groups:
        seq = order.get(g, [])
        dupes = sorted({i for i in seq if seq.count(i) > 1})
        if dupes:
            errors.append(f"ORDER[{g!r}] lists these more than once: {', '.join(dupes)}")
        missing = sorted(set(members[g]) - set(seq))
        if missing:
            errors.append(f"ORDER[{g!r}] does not place: {', '.join(missing)}. Add each id where its "
                          f"name should sit in the list")
        extra = sorted(set(seq) - set(members[g]))
        if extra:
            errors.append(f"ORDER[{g!r}] names ids that are not bundles in this group: {', '.join(extra)}")
        out = []
        last = None
        for i in seq:
            if i not in by_id:
                continue
            p = by_id[i].get("trigger_name") or ""
            if p == last:
                continue
            if p in out:
                errors.append(f"trigger_name {p!r} is shared by bundles that are not next to each other "
                              f"in ORDER[{g!r}]; place them together")
                continue
            if p in phrase_group and phrase_group[p] != g:
                errors.append(f"trigger_name {p!r} is used in groups {phrase_group[p]!r} and {g!r}; a shared "
                              f"phrase must stay in one group")
            phrase_group[p] = g
            out.append(p)
            last = p
        phrases[g] = out

    descs = {}
    for name, spec in skills.items():
        g = spec["group"]
        if g not in groups:
            errors.append(f"{name}: group {g!r} does not exist")
            continue
        if not phrases.get(g):
            errors.append(f"{name}: group {g!r} has no types to list")
            continue
        d = spec["text"].format(count=len(bundles), list=join_list(phrases[g]))
        if len(d) > cap:
            errors.append(f"{name}: description is {len(d)} characters, over the {cap} cap. That is the "
                          f"signal to split the skills by family group (ADR 0093)")
        # The description is written as a plain YAML scalar, so it must stay one.
        if ": " in d or " #" in d or d[:1] in "&*!|>'\"%@`[]{},?:-#":
            errors.append(f"{name}: description would not parse as a plain YAML scalar")
        descs[name] = d
    return descs, errors


def skill_path(name):
    return os.path.join(ROOT, "skills", name, "SKILL.md")


def main():
    args = sys.argv[1:]
    check = "--check" in args
    show = "--print" in args
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        bundles = json.load(f)["bundles"]
    descs, errors = build(bundles)
    for e in errors:
        print(f"{RED}FAIL{OFF}  {e}")
    if errors:
        return 1
    if show:
        for name, d in descs.items():
            print(f"{name} ({len(d)} characters):\n  {d}\n")
        return 0
    drift = []
    for name, d in descs.items():
        path = skill_path(name)
        with open(path, "rb") as f:
            raw = f.read().decode("utf-8")
        m = DESC_RE.search(raw)
        if not m:
            print(f"{RED}FAIL{OFF}  {path}: no single-line description field")
            return 1
        current = m.group(1).rstrip("\r")
        if current == d:
            continue
        if check:
            drift.append(name)
            continue
        end = m.start(1) + len(current)
        raw = raw[: m.start(1)] + d + raw[end:]
        with open(path, "wb") as f:
            f.write(raw.encode("utf-8"))
        print(f"{GREEN}OK{OFF}  wrote the {name} description ({len(d)} characters)")
    if drift:
        for name in drift:
            print(f"{RED}FAIL{OFF}  skills/{name}/SKILL.md: description differs from what the manifest "
                  f"generates. Run python tools/gen-skill-descriptions.py, and treat the change as a trigger "
                  f"change: see release-process.md section 1")
        return 1
    lengths = ", ".join(f"{n} {len(d)}" for n, d in descs.items())
    print(f"{GREEN}OK{OFF}  skill descriptions are fresh: {len(bundles)} bundles named ({lengths} of {CAP} characters).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
