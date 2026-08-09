#!/usr/bin/env python3
"""Fail if the library version disagrees with itself across the files that must carry it.

WHY THIS EXISTS.

Listing clause L4 of the Product on Purpose marketplace contract requires that the registry entry, the
release tag, `library.json` and **every native manifest the repo emits** all carry the same version. Its
stated verification method is "Re-pin checklist + review". A human.

Cutting v0.3.1 on 2026-08-08 meant hand-editing the version in SIX places. Five of them are ordinary
metadata. One is not:

    skills/plt-fill-template/SKILL.md says, in its own body, "Fetch from the tag matching this skill's
    own metadata.version", and then fetches templates from
    https://raw.githubusercontent.com/.../v<metadata.version>/...

So `metadata.version` is not a label on the skill. It is half of a URL. A stale value there does not
produce a cosmetic mismatch; it points every installed copy of the skill at a tree that is not the one
it shipped with, and nothing anywhere fails.

WHAT THIS CHECKS.

Every version string that must equal `library.json`'s `version`:

  - library.json            -> .version                       (the canonical value)
  - library.json            -> each declared component's .version
  - .claude-plugin/plugin.json -> .version
  - each declared skill's SKILL.md -> metadata.version

WHAT IT DELIBERATELY DOES NOT CHECK, AND WHY.

**The README badge.** Already covered, and not by this repository: `agent-skills-toolkit` ships
`scripts/check-readme-version.mjs`, which reads library.json and regex-matches the shields.io badge. CI
clones that toolkit already, so the honest fix was to invoke the tool that exists rather than write a
second one here. Duplicating it would create exactly the two-copies-of-one-fact shape this file exists
to prevent.

**INDEX.md.** Covered by the Standard's own G4 (index-drift), which fails on a hand-edited generated
file. Verified by mutation on 2026-08-08: setting the version line to a wrong value makes the Standard's
gate exit non-zero and drop the tier from advanced to convergent.

**That a tag matching the declared version exists.** Tempting and wrong. The version is bumped inside
the release PR, and the tag is created after that PR merges. A check requiring the tag would fail the
one commit whose job is to prepare it, so it would be disabled at exactly the moment it mattered.

WHAT IT CANNOT CHECK.

That the registry entry in `product-on-purpose/agent-plugins` agrees. That value lives in another
repository, no check here can see it, and it goes stale silently every time this library releases
without a re-pin. Re-pinning is a deliberate cross-repository act. This check says so on every run.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def skill_metadata_version(path):
    """Return metadata.version from a SKILL.md, or None with a reason.

    Deliberately not PyYAML. Nine of this gate's checks are pure stdlib and two carry a dependency for
    a reason recorded in an ADR; one scalar under one known key does not earn a third.
    """
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, "no YAML frontmatter block"

    in_metadata = False
    for line in m.group(1).splitlines():
        if re.match(r"^metadata:\s*$", line):
            in_metadata = True
            continue
        if in_metadata:
            # A non-indented, non-blank line ends the metadata mapping.
            if line.strip() and not line[0].isspace():
                in_metadata = False
                continue
            hit = re.match(r"^\s+version:\s*[\"']?([^\"'\s]+)[\"']?\s*$", line)
            if hit:
                return hit.group(1), None
    return None, "no metadata.version key"


def main():
    problems = []
    observed = []

    lib_path = ROOT / "library.json"
    if not lib_path.exists():
        print(f"{RED}FAIL{OFF}  library.json not found at {lib_path}")
        return 1

    lib = json.loads(lib_path.read_text(encoding="utf-8"))
    canonical = lib.get("version")
    if not canonical:
        print(f"{RED}FAIL{OFF}  library.json has no top-level version")
        return 1
    observed.append(("library.json", ".version", canonical))

    # Every declared component, across every component kind the manifest uses.
    for kind, entries in (lib.get("components") or {}).items():
        for entry in entries or []:
            name = entry.get("name", "<unnamed>")
            version = entry.get("version")
            label = f"library.json components.{kind}[{name}]"
            if version is None:
                problems.append(f"{label} declares no version")
                continue
            observed.append((label, ".version", version))
            if version != canonical:
                problems.append(f"{label} is {version}, expected {canonical}")

            # The component's own file, which is the load-bearing one for skills.
            rel = entry.get("path")
            if kind == "skills" and rel:
                skill_path = ROOT / rel
                if not skill_path.exists():
                    problems.append(f"{label} declares path {rel}, which does not exist")
                    continue
                found, reason = skill_metadata_version(skill_path)
                if found is None:
                    problems.append(f"{rel}: {reason}")
                    continue
                observed.append((rel, "metadata.version", found))
                if found != canonical:
                    problems.append(
                        f"{rel} metadata.version is {found}, expected {canonical}. "
                        f"This one is a URL, not a label: the skill fetches its templates from the tag "
                        f"matching it."
                    )

    plugin_path = ROOT / ".claude-plugin" / "plugin.json"
    if not plugin_path.exists():
        problems.append(".claude-plugin/plugin.json not found (listing clause L1 requires it)")
    else:
        plugin_version = json.loads(plugin_path.read_text(encoding="utf-8")).get("version")
        if plugin_version is None:
            problems.append(".claude-plugin/plugin.json has no version")
        else:
            observed.append((".claude-plugin/plugin.json", ".version", plugin_version))
            if plugin_version != canonical:
                problems.append(
                    f".claude-plugin/plugin.json is {plugin_version}, expected {canonical} "
                    f"(listing clause L4)"
                )

    width = max(len(a) for a, _, _ in observed)
    for where, key, value in observed:
        mark = f"{GREEN}ok{OFF}" if value == canonical else f"{RED}NO{OFF}"
        print(f"  {mark}  {where.ljust(width)}  {key} = {value}")

    print()
    if problems:
        for p in problems:
            print(f"{RED}FAIL{OFF}  {p}")
        print(f"\n{RED}FAIL{OFF}  {len(problems)} version disagreement(s). Listing clause L4 requires "
              f"the registry entry, the release tag, library.json and every native manifest to agree.")
        return 1

    print(f"{GREEN}OK{OFF}  every declared version agrees at {canonical}.")
    print(f"{DIM}      not verified: the registry entry in product-on-purpose/agent-plugins, which lives"
          f"\n      in another repository and goes stale silently every time this library releases"
          f"\n      without a re-pin. Re-pinning is a deliberate cross-repository act.{OFF}")
    print(f"{DIM}      not verified here on purpose: the README badge (agent-skills-toolkit's"
          f"\n      check-readme-version.mjs) and INDEX.md (the Standard's own G4).{OFF}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
