#!/usr/bin/env python3
"""gen-manifest.py - generate (or verify) the machine catalog, manifest.json.

Walks templates/, reads each bundle's meta, and emits manifest.json at the repo root: the
selectable subset of every bundle's metadata, so an agent can pick the right bundle from
structured data alone rather than parsing prose or guessing from filenames. This is the
consumption surface RFC-0001 proposed and roadmap WP-22 builds. See
docs/internal/decisions/0018-machine-catalog-generated-manifest.md.

The file is GENERATED, never hand-edited. It is committed to version control (RFC-0001 accepted
this as the pragmatic interim until a distribution surface exists), and the gate keeps it honest:
`--check` regenerates in memory and fails if the committed file has drifted, the same
generate-and-check discipline the dashes and links gates already use.

Naming: RFC-0001 called this artifact "index.json"; WP-22 builds it as "manifest.json" per the
roadmap, which also names this script. ADR 0018 records the reconciliation.

Selectable subset per RFC-0001's Detailed Design: id, doc_type, title, summary, family, the taxonomy
axis (phase XOR classification, whichever the meta declares), sizes_available, status, tags, aliases.
Provenance fields (template_version, last_reviewed, catalog_ref, maintainer, license) are deliberately
omitted: they are not selection inputs.

Dependency: PyYAML, to parse the metas. The gate's check J already validates every meta against the
schema, so this generator trusts the metas are well-formed and only reads them. Unlike the gate, a
generator cannot degrade gracefully without a parser, so PyYAML is required here rather than optional.

Usage:
    python tools/gen-manifest.py            # regenerate manifest.json in place
    python tools/gen-manifest.py --check    # exit 1 if manifest.json is stale or a count disagrees

Exit 0 if written / in sync; 1 if --check finds drift.
"""

import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
TEMPLATES_DIR = os.path.join(ROOT, "templates")
MANIFEST_PATH = os.path.join(ROOT, "manifest.json")
README_PATH = os.path.join(ROOT, "README.md")

# The fields an agent selects on. phase and classification are mutually exclusive (ADR 0015); only
# the one the meta declares is emitted. Order here is documentary; the JSON is written sort_keys=True
# so the on-disk field order is stable regardless of this list.
SELECT_FIELDS = [
    "id",
    "doc_type",
    "title",
    "summary",
    "family",
    "phase",
    "classification",
    "sizes_available",
    "status",
    "tags",
    "aliases",
]

# README carries a machine-readable count marker so the human front door cannot silently drift from
# the real bundle count (audit finding C-03; the WP-13 sweep found the README claiming four bundles
# when six existed). The marker is an HTML comment, invisible in the rendered page.
README_COUNT_RE = re.compile(r"<!--\s*bundle-count:\s*(\d+)\s*-->")

GREEN = "\033[32m"
RED = "\033[31m"
OFF = "\033[0m"


def find_bundles(root):
    """Every directory under templates/ that is a real bundle (carries <name>_meta.yaml).

    Skips non-bundle directories like templates/_working/, exactly as the gate's own bundle
    discovery does, so the two agree on what counts as a bundle.
    """
    out = []
    for name in sorted(os.listdir(root)):
        d = os.path.join(root, name)
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, name + "_meta.yaml")):
            out.append(name)
    return out


def build_manifest(yaml):
    """The manifest as a Python dict, built fresh from the metas on disk."""
    bundles = []
    for name in find_bundles(TEMPLATES_DIR):
        meta_path = os.path.join(TEMPLATES_DIR, name, name + "_meta.yaml")
        with open(meta_path, encoding="utf-8") as f:
            meta = yaml.safe_load(f.read())
        entry = {k: meta[k] for k in SELECT_FIELDS if k in meta}
        bundles.append(entry)
    bundles.sort(key=lambda b: b.get("id", ""))
    return {
        "_generated": "by tools/gen-manifest.py from templates/*/*_meta.yaml; do not edit by hand",
        "count": len(bundles),
        "bundles": bundles,
    }


def serialize(manifest):
    """Canonical text form: sorted keys, 2-space indent, trailing newline. Deterministic, so a
    `--check` diff only fires on a real content change, not on formatting noise."""
    return json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def readme_declared_count():
    """The count the README's marker claims, or None if the marker is absent."""
    if not os.path.isfile(README_PATH):
        return None
    m = README_COUNT_RE.search(open(README_PATH, encoding="utf-8").read())
    return int(m.group(1)) if m else None


def check(fresh_text, manifest):
    """Return a list of problems; empty means the committed manifest and the README agree with the
    metas on disk."""
    problems = []
    if not os.path.isfile(MANIFEST_PATH):
        problems.append("manifest.json is missing; run `python tools/gen-manifest.py` to create it")
    else:
        committed = open(MANIFEST_PATH, encoding="utf-8").read()
        if committed != fresh_text:
            problems.append(
                "manifest.json is stale (differs from freshly generated output); run "
                "`python tools/gen-manifest.py` and commit the result"
            )

    declared = readme_declared_count()
    real = manifest["count"]
    if declared is None:
        problems.append(
            "README has no bundle-count marker; add an HTML comment `<!-- bundle-count: "
            + str(real) + " -->` so the front door cannot drift from the manifest"
        )
    elif declared != real:
        problems.append(
            "README bundle-count marker says " + str(declared) + " but there are " + str(real)
            + " bundles; update the marker (and any prose count) to match"
        )
    return problems


def main():
    try:
        import yaml
    except ImportError:
        print("gen-manifest requires PyYAML (pip install pyyaml) to read the metas.")
        return 1

    check_only = "--check" in sys.argv[1:]
    manifest = build_manifest(yaml)
    fresh_text = serialize(manifest)

    if check_only:
        problems = check(fresh_text, manifest)
        if problems:
            for p in problems:
                print(RED + "DRIFT" + OFF + "  " + p)
            return 1
        print(
            GREEN + "OK" + OFF + "  manifest.json is fresh: " + str(manifest["count"])
            + " bundles, README marker agrees."
        )
        return 0

    with open(MANIFEST_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(fresh_text)
    print(
        GREEN + "OK" + OFF + "  wrote manifest.json: " + str(manifest["count"]) + " bundles ("
        + ", ".join(b["id"] for b in manifest["bundles"]) + ")."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
