# Release process

**What this is.** How a release is actually cut here, written from the three that have happened rather than
from an ideal. Where the process went wrong, it says so, because the wrong order is the part worth
remembering.

**Releases stop for the maintainer.** That is the standing rule in
[`decision-procedures.md`](decision-procedures.md). A green bundle PR merges on its own authority; a tag
does not. Merge permission is not release permission, and the two have been granted separately every time.

---

## What a release consists of

Four artifacts, and they are not interchangeable.

| Artifact | Where | What it is for |
|---|---|---|
| `CHANGELOG.md` section | repo root | The record. Every change, for someone who wants all of them |
| Release note | `docs/releases/vX.Y.Z.md` | The announcement. **Written by filling this library's own `release-notes` template** |
| Annotated tag | `vX.Y.Z` | The immutable pointer |
| GitHub release | releases page | The public artifact |

**The release note is a dogfood, and that is the point.** A template library that does not use its own
templates has not tested them. This is how [DF-1](../../STATE.md) was found: filling the lean
`release-notes` template for v0.1.0 exposed that it had no first-release mode, because "Improved" and
"Fixed" are defined against a previous release and a `0.1.0` has none. That defect was found by use, not by
review, and it is the entire argument for doing this.

---

## The sequence

### 1. Confirm the tree is releasable

```
python tools/check-bundles.py          # every bundle, all 11 checks
python tools/check-links.py            # every relative link
python tools/check-counts.py           # every marked document agrees with the tree
python tools/check-changelog.py        # no post-0.1.0 decision record missing
```

`STATE.md` outranks every other document. If it disagrees with the tree, fix `STATE.md` first, and re-read
the prose around each marker rather than only the marker.

### 2. Read the downstream contract BEFORE choosing the version

**This step exists because skipping it cost a release.** See "What went wrong" below.

If the release will be listed anywhere, read that listing contract now. For the Product on Purpose
registry it is [`agent-plugins/CONTRIBUTING.md`](https://github.com/product-on-purpose/agent-plugins),
clauses L1 to L6. It determines what the tagged tree must **contain**, so it is an input to the release and
not a checklist afterwards.

### 3. Promote the changelog

`## [Unreleased]` becomes `## [X.Y.Z] - DATE`, and a fresh empty `[Unreleased]` opens above it. Check that
what shipped is actually recorded: `check-changelog.py` gates decision records only, so bundles and tooling
can be missing while it passes green.

### 4. Write the release note by filling the template

Copy `templates/release-notes/release-notes_template-lean.md`, fill it, and grade it against
`release-notes_guide.md`'s rubric like any other document. Stamp `source_template` and
`source_template_version` in the frontmatter so the provenance is machine-readable.

### 5. Land it, then tag

The changelog and note go through a normal PR and merge. **Then** tag:

```
git tag -a vX.Y.Z -m "..."          # annotated, always
git push origin vX.Y.Z
gh release create vX.Y.Z --notes-file docs/releases/vX.Y.Z.md
```

**The tag object SHA is not the commit SHA.** `git rev-parse vX.Y.Z` gives the annotated tag object;
`git rev-parse vX.Y.Z^{commit}` gives the commit. Anything pinning a release wants the second.

### 6. List it, if it is being listed

Pin the **commit**, bump the registry's own version, add the README row and the registry changelog entry,
and run the registry's validator with a token (`GITHUB_TOKEN=$(gh auth token)`; without one, its sha-on-tag
check fails on every entry with a rate-limit 403 that looks like a real failure and is not).

---

## What went wrong, on 2026-08-08

Recorded because the failure was in the **order**, and the order looks obviously right until it is not.

`v0.2.0` was tagged and released, and only then was the marketplace listing attempted. Reading the listing
contract at that point surfaced **clause L3**: a repository with no root `library.json` binding the family
Standard is "loose components" and **not eligible for a new listing**. This repository had none.

Clause **L4** then made it worse in a useful way: the pinned SHA must sit on a release tag, and the tag,
the registry entry, `library.json` and every native manifest must all carry the same version. `v0.2.0`'s
tree could not contain a file created after it was tagged.

**A published tag is not moved.** So the fix was `v0.2.1`: add the manifest, re-cut, pin that.

**The lesson, generalised.** When work crosses a governance boundary, the receiving system's contract is an
**input to your build**, not a checklist you satisfy at the end. Reading it late cost one extra release,
which is cheap; the alternative was a registry entry failing a clause it claimed to meet.

**One thing that went right and is worth keeping.** The Standard's tier was **measured, not declared**: its
own gate was run against this repository and exits 0 at tier universal. Declaring a tier without running
the gate would have been the same defect this library spends its whole review process catching, committed
into a governance registry rather than a template.

---

## Versioning

[Semantic Versioning](https://semver.org/), applied to the library rather than to any one bundle.

- **Major** would be a breaking change to the bundle contract or the meta schema. None has happened.
- **Minor** is new bundles, new families, new gate checks, new documentation surfaces.
- **Patch** is corrections that change no structure. `v0.2.1` is the worked example: it added a manifest
  and changed no bundle content.

Each bundle carries its own `template_version` in its meta, moving independently of the library version,
with its own `_history.md`. A library release does not bump them.

## What the process does not do

- **It does not prove the release is good.** The gate proves structure. See
  [`review-standards.md`](review-standards.md) for the seven defect classes no machine catches.
- **It does not announce anywhere.** No mailing list, no feed beyond GitHub's own.
- **It does not verify the marketplace entry keeps working.** The registry pins a SHA, so a listing goes
  stale silently as the library moves ahead of it. Re-pinning is a deliberate act.
