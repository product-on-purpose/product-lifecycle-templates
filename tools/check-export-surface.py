#!/usr/bin/env python3
"""Fail if this repository would publish a skill it does not declare.

WHY THIS EXISTS, AND WHY IT IS NOT ABOUT build-bundle.

On 2026-08-08, the first execution of `npx skills add product-on-purpose/product-lifecycle-templates`
reported **two** skills and installed both. The second was the maintainer-internal build harness at
.claude/skills/build-bundle/, whose own description says it is not shipped to library users.

Nothing was done wrong to cause it. The vercel-labs skills CLI short-circuits its subdirectory search
when a SKILL.md exists at the repository root, and this repository had one until ADR 0036 correctly
moved the public skill under skills/ to satisfy the Agent Skills specification and the Advanced Skill
Library Standard. Removing the root file removed a protection nobody knew was there.

MOVING ONE FILE FIXED ONE LEAK. THIS CHECK IS THE PART THAT LASTS.

The CLI scans a hardcoded list of THIRTY-TWO prefixes, twenty-seven of them agent-config directories:
.claude/skills, .codex/skills, .cursor-adjacent tools, .github/skills, and twenty-three more. It reads
no ignore file; its skip list is hardcoded to node_modules, .git, dist, build and __pycache__. So the
next leak will not be build-bundle. It will be the first time anyone adds .codex/skills/<anything> to a
repository whose maintainer also uses Codex, and it will ship silently, past every other check here.

WHAT THIS CHECKS.

The set of skills the CLI would export must equal exactly the set library.json declares. Not a subset,
not a superset. A skill that ships without being declared is the leak above; a declared skill that does
not ship is a broken install, which is the same defect pointed the other way.

WHAT IT CANNOT CHECK.

That the upstream CLI keeps these rules. PRIORITY_PREFIXES below is a copy of a hardcoded list in a
package that ships often, read from skills@1.5.22 on 2026-08-08. If upstream adds a directory or walks
the whole tree, this check goes stale in the dangerous direction: it keeps passing. That limitation is
printed on every run, and the honest mitigation is to re-read the list when the CLI majors.
"""

import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

# Copied verbatim from PRIORITY_PREFIXES in skills@1.5.22 (package/dist/cli.mjs). The empty string is
# the repository root, and it behaves differently: a root SKILL.md short-circuits the whole search.
PRIORITY_PREFIXES = [
    "",
    "skills/", "skills/.curated/", "skills/.experimental/", "skills/.system/",
    ".agents/skills/", ".claude/skills/", ".cline/skills/", ".codebuddy/skills/",
    ".codex/skills/", ".commandcode/skills/", ".continue/skills/", ".github/skills/",
    ".goose/skills/", ".grok/skills/", ".iflow/skills/", ".junie/skills/",
    ".kilocode/skills/", ".kimchi/skills/", ".kiro/skills/", ".minimax/skills/",
    ".mux/skills/", ".neovate/skills/", ".opencode/skills/", ".openhands/skills/",
    ".pi/skills/", ".qoder/skills/", ".roo/skills/", ".trae/skills/",
    ".windsurf/skills/", ".zcode/skills/", ".zencoder/skills/",
]

CLI_VERSION_READ = "skills@1.5.22, read 2026-08-08"


def tracked_skill_files():
    """Every tracked SKILL.md, repo-relative, posix-separated.

    Tracked only, deliberately: the CLI clones the repository, so an untracked file cannot ship no
    matter which directory it sits in.
    """
    out = subprocess.run(["git", "ls-files", "*SKILL.md", "SKILL.md"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    return sorted({p.replace(os.sep, "/") for p in out if p})


def would_export(skill_files):
    """The set the CLI would install, applying its own two rules."""
    # Rule 1: a root SKILL.md short-circuits. The CLI returns it and never searches subdirectories.
    if "SKILL.md" in skill_files:
        return ["SKILL.md"], True
    # Rule 2: otherwise, anything under a priority prefix.
    exported = []
    for path in skill_files:
        for prefix in PRIORITY_PREFIXES:
            if prefix and path.startswith(prefix):
                exported.append(path)
                break
    return sorted(set(exported)), False


def declared():
    data = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    return sorted({s["path"].replace(os.sep, "/")
                   for s in data.get("components", {}).get("skills", [])})


def main():
    skill_files = tracked_skill_files()
    exported, short_circuited = would_export(skill_files)
    want = declared()

    extra = [p for p in exported if p not in want]
    missing = [p for p in want if p not in exported]

    if not extra and not missing:
        print(GREEN + "OK" + OFF + "  the published skill surface is exactly what library.json declares "
              "(%d skill(s))." % len(want))
        for p in want:
            print("      ships: %s" % p)
        if short_circuited:
            print(DIM + "      note: a root SKILL.md is present, so the CLI short-circuits and never "
                  "searches subdirectories." + OFF)
        print(DIM + "      not verified: that the CLI still uses these rules. PRIORITY_PREFIXES is a "
              "copy of a" + OFF)
        print(DIM + "      hardcoded upstream list (%s). If upstream adds a directory," % CLI_VERSION_READ + OFF)
        print(DIM + "      this check goes stale by continuing to pass. Re-read it when the CLI majors."
              + OFF)
        return 0

    print(RED + "FAIL" + OFF + "  the published skill surface does not match library.json.")
    print()
    if extra:
        print("  WOULD SHIP BUT IS NOT DECLARED (%d):" % len(extra))
        for p in extra:
            print("    %s" % p)
        print()
        print("    `npx skills add` installs every SKILL.md under one of %d scanned prefixes,"
              % (len(PRIORITY_PREFIXES) - 1))
        print("    including .claude/skills/, .codex/skills/ and .github/skills/. The CLI reads no")
        print("    ignore file, so a skill cannot be excluded in place. Move it somewhere unscanned")
        print("    (a slash command under .claude/commands/ works, and so does tools/), or declare it")
        print("    in library.json if it is genuinely meant to ship. See ADR 0037.")
    if missing:
        print("  DECLARED BUT WOULD NOT SHIP (%d):" % len(missing))
        for p in missing:
            print("    %s" % p)
        print()
        print("    This is the same defect pointed the other way: an install that silently omits a")
        print("    component the library promises. Check the path, and that the file is tracked.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
