# Releasing

The executable checklist for cutting a tagged release of this library. Written 2026-07-28, after v0.1.0
shipped without one and the steps lived only in a session log.

**What a release is here:** a git tag, a closed `CHANGELOG.md` section, and a customer-facing note in
[`docs/releases/`](../releases/) written **from this library's own `release-notes` template**. The tag is
the record, the changelog is the detail, the release note is the meaning. That three-way split is the
distinction the `release-notes` bundle itself teaches, and this repository is its first customer.

---

## Versioning

Two version numbers exist here and they are not the same thing.

| Version | Lives in | Means |
|---|---|---|
| **Library version** (`0.1.0`, `0.2.0`) | the git tag, `CHANGELOG.md`, `docs/releases/` | the state of the whole repository: bundles, gates, decisions |
| **`template_version`** (`0.1.0`) | each bundle's `<type>_meta.yaml` and `<type>_history.md` | the state of ONE template, bumped when that template changes |

A consumer pins a template, not the repo, so a bundle's version moves on its own schedule. The library
version never forces a `template_version` bump and a `template_version` bump never forces a release.

**Semantic versioning, applied to a document library** ([semver.org](https://semver.org/)):

- **MAJOR** - a change that breaks a consumer who already filled a template: a section removed, a
  placeholder renamed, a file renamed or moved, a metadata key removed from the schema.
- **MINOR** - new bundles, new sizes or formats, new gate checks, new optional metadata keys. Everything
  that has shipped so far is minor: the library adds, it has not yet taken away.
- **PATCH** - corrections that change no structure: a citation fixed, a typo, a guidance sentence reworded.

The library stays `0.x` while status is `beta`. `1.0.0` waits on real usage, not on coverage: see the
"zero real fills" line in [`STATE.md`](../../STATE.md).

---

## Preconditions

Do not start a release until all of these hold. The first four are machine-checked; the rest are not.

- [ ] `main` is green. Run the full local suite (below) **and** confirm the CI run whose `headSha` equals
      `main`'s tip succeeded. `gh pr checks` can report an older run: match the sha.
- [ ] Every decision record since the last release appears in `CHANGELOG.md` (`check-changelog.py` fails
      otherwise, and it caught a missing ADR 0021 on its first run).
- [ ] `manifest.json` and the atlas are fresh, and the README bundle-count marker agrees.
- [ ] Every research log passes the contract check, or is on its named exemption list.
- [ ] No open finding in `STATE.md` is silently unrecorded in the changelog. A known defect that ships is
      fine; a known defect nobody wrote down is not.
- [ ] Counts in `STATE.md` and `README.md` match the tree. Read them off the tools, never off the last
      release. Assertion counts in particular **scale with the live tree**.

```
python tools/check-bundles.py
python tools/test-check-k.py
python tools/test-check-formats.py
python tools/check-research-logs.py
python tools/test-check-research-logs.py
python tools/check-links.py
python tools/gen-manifest.py --check
python tools/gen-atlas.py --check
python tools/check-adr-index.py
python tools/check-changelog.py
```

---

## The release, in order

Every step is a PR. `main` is protected and requires the gate to pass, so nothing here is pushed directly.

**1. Close the changelog section.** Rename `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD`, add a fresh empty
`[Unreleased]` above it, and update the compare links at the bottom of the file:

```
[Unreleased]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/vX.Y.Z...HEAD
[X.Y.Z]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/vA.B.C...vX.Y.Z
```

Keep a Changelog's rule applies from this moment: **a released section is not rewritten.** Corrections to a
shipped release go in the next section, not back into the closed one.

**2. Write the release note, from the template.** Copy
[`templates/release-notes/release-notes_template-lean.md`](../../templates/release-notes/release-notes_template-lean.md)
to `docs/releases/vX.Y.Z.md` and fill it. Do not write it freehand, and do not copy the previous release
note as a shortcut: **filling the template is the dogfood, and the dogfood is the point.** v0.1.0's release
note produced finding DF-1 (the template assumed a previous version existed) on its first use. A release
note that skips the template tests nothing.

Frontmatter carries `source_template: release-notes` and `source_template_version`, so the note records
which version of the template produced it.

**3. Reconcile the state documents.** `STATE.md` gets the release in its running log and its counts
corrected. `README.md` gets its bundle count checked by `gen-manifest.py --check`, so trust the gate rather
than your memory.

**4. Land it, then tag the merge commit.** The tag points at the commit on `main`, never at a branch tip
that was rebased:

```
git checkout main && git pull --ff-only
git tag -a vX.Y.Z -m "vX.Y.Z: <one line>"
git push origin vX.Y.Z
```

**5. Publish the GitHub release** from the note you already wrote, so the two cannot drift:

```
gh release create vX.Y.Z --title "vX.Y.Z: <one line>" --notes-file docs/releases/vX.Y.Z.md
```

**6. Verify the release exists, from the remote.** Not from local state:

```
git ls-remote --tags origin | grep vX.Y.Z
gh release view vX.Y.Z --json tagName,publishedAt,url
```

---

## The post-release sweep

**Releasing falsifies forward-looking prose.** Sentences written while work was pending ("in an open PR",
"not yet built", "planned", "will ship") become false the moment it lands, and nothing gates them. This
happened on the very first merge after it was written down.

```
git grep -n -i "open PR\|not yet built\|will be built\|in progress\|planned for"
```

Read every hit and fix what the release made untrue. This is a discipline, not a check: a linter that
matched these strings would fire on template guidance text, which legitimately uses all of them.

---

## What a release does NOT prove

State this plainly at each release rather than letting a tag imply more than it means.

- **Not that any template has been used.** Every filled artifact in this repository is an authored example.
  Coverage and usage are separate numbers and both belong in `STATE.md`.
- **Not that citations support their claims.** The gate proves a citation resolves and that a research log
  carries its contract; whether a source supports the sentence citing it is the four-lens review's job.
- **Not that a retrieval status is truthful.** `check-research-logs.py` says so in its own output.
- **Not that the guidance is good.** No check scores a rubric or a guide. That is deliberate: a check that
  counted rows would be the countable-target failure
  [`guide-rubric-spec.md`](guide-rubric-spec.md) warns against.
