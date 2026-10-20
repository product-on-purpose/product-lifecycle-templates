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
python tools/run-gate.py               # every step CI runs, and a named reason for each it skips
```

**Run the whole gate, not a list of scripts.** This document named four of them until 2026-09-06, and CI
runs **32 steps**. Three of those are not files under `tools/` at all - one is an inline heredoc in
`ci.yml` - so no list anyone maintains by hand, and no glob over a directory, can be complete.
`run-gate.py` derives its list from `.github/workflows/ci.yml` and prints every step it skipped with the
reason, which is why it has no output line that says everything passed. Read the skip list before calling
the tree green.

`check-links.py` skips untracked files. Run the gate **after `git add`**, or a new document's broken links
pass.

`STATE.md` outranks every other document. If it disagrees with the tree, fix `STATE.md` first, and re-read
the prose around each marker rather than only the marker.

**Then check the documentation for all three audiences: users, technical readers and agents.** This is the
maintainer's standing rule, set 2026-10-15: every release ships with its release note, its changelog, and
onboarding documentation that is current for each audience. A green gate does not show this. The gate
checks the counts in markers, and it never reads whether a page names the bundles that exist.

| Audience | Surfaces to read |
|---|---|
| User | `README.md` (status line, at-a-glance table, library table by family), `docs/tutorials/getting-started.md`, `docs/how-to/`, `docs/reference/choosing-a-template.md`, `templates/README.md`, the site's `index.mdx` |
| Technical | `STATE.md`, `docs/explanation/`, `CONTRIBUTING.md`, `CHANGELOG.md`, and `docs/internal/backlog.md` (refresh its issue counts from GitHub) |
| Agent | `AGENTS.md`, both skills' `SKILL.md` descriptions and bodies, the `plugin.json` and `library.json` descriptions, `INDEX.md` (regenerate it, never edit it), and the registry listing in `agent-plugins` |

Two checks find most gaps. First, list every one of those files that names an older bundle but not the
newest ones, and read each hit:

```
for f in <the files above>; do grep -q "<an older bundle id>" "$f" && ! grep -q "<the newest bundle id>" "$f" && echo "$f"; done
```

Second, grep those files for counts of bundles, variants, families, ADRs and CI steps outside the markers,
and compare each with the generated artifacts. **A skill description is a trigger list, not prose.** An
agent decides whether to load the skill from that list, so a type missing from it may never reach the skill.
*(Added 2026-10-15: both skill descriptions named the 25 Tier-1 types and `rfc`, and none of the 18
other Tier-2 types. The fill skill also said every bundle has a full variant, while 40 of 44 did. The README
and STATE said the MCP server served 85 variants when it served 89.)*

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

**Then update the compare links at the bottom of the file**, which is the step this document was missing
until 2026-09-05 and which `v0.5.0` consequently skipped: its section closed in the body while the footer
still ran `[Unreleased]` from `v0.4.0` and carried no `[0.5.0]` line at all, so for two days the
"unreleased" diff silently included everything in `v0.5.0`.

```
[Unreleased]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/vX.Y.Z...HEAD
[X.Y.Z]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/vA.B.C...vX.Y.Z
```

Nothing gates this. `check-changelog.py` reads the body and never looks at the footer, which is why it
went unnoticed.

### 4. Write the release note by filling the template

Copy `templates/release-notes/release-notes_template-lean.md`, fill it, and grade it against
`release-notes_guide.md`'s rubric like any other document. Stamp `source_template` and
`source_template_version` in the frontmatter so the provenance is machine-readable.

### 5. Land it, then tag

The changelog and note go through a normal PR and merge. **Then** tag:

```
git tag -a vX.Y.Z -m "..."          # annotated, always, on the merge commit on main
git push origin vX.Y.Z
gh release create vX.Y.Z --title vX.Y.Z --notes-file <the note with its frontmatter removed>
```

**Remove the frontmatter before publishing the release body.** GitHub does not parse YAML frontmatter in a
release body. It renders the opening `---` as a rule and every field as raw text above the title. The
repository copy keeps its frontmatter, because `source_template` is the provenance record. *(Added
2026-10-15: 19 of the 21 releases from `v0.1.0` to `v0.17.0` published the frontmatter this way; only
`v0.2.1` and `v0.6.0` did not. All 19 were corrected that day by editing the release bodies, which removed
only the frontmatter.)*

**Tag the squash commit, not the branch tip.** A squash merge creates a new commit on `main`, so the PR
branch's last commit is not in `main`'s history. Check that `git rev-parse vX.Y.Z^{commit}` equals
`git rev-parse origin/main` before publishing.

**The tag object SHA is not the commit SHA.** `git rev-parse vX.Y.Z` gives the annotated tag object;
`git rev-parse vX.Y.Z^{commit}` gives the commit. Anything pinning a release wants the second.

### 6. List it, if it is being listed

Pin the **commit**, bump the registry's own version, add the README row and the registry changelog entry,
and run the registry's validator with a token (`GITHUB_TOKEN=$(gh auth token)`; without one, its sha-on-tag
check fails on every entry with a rate-limit 403 that looks like a real failure and is not).

### 7. Sweep the forward-looking prose

**Releasing falsifies sentences nobody edited.** Prose written while work was pending - "in an open PR",
"not yet built", "planned", "will ship" - becomes false the moment it lands, and nothing gates it. This
happened on the very first merge after it was first written down.

```
git grep -n -i "open PR\|not yet built\|will be built\|in progress\|planned for\|forthcoming\|to be built"
```

Read every hit and fix what the release made untrue. *(Widened 2026-09-23: "forthcoming" and "to be built"
were added after a documentation audit found seven sentences in sibling bundles still calling `raid-log`,
`kpi-dashboard` and `status-report` forthcoming, the oldest from July. The earlier pattern matched none of
them, which is how they survived every release since.)* This stays a discipline rather than a check, because
a linter matching these strings would fire on template guidance text, which legitimately uses all of them.
The nearest thing to a machine version is check I in `check-bundles.py`, which does catch one instance of
the shape: a `related_templates` entry still labelled `future:` after the bundle was built.

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

## What a release does not prove

State this plainly at each release rather than letting a tag imply more than it means.

- **Not that any template has been used.** Every filled artifact in this repository is an authored example.
  Coverage and usage are separate numbers and both belong in `STATE.md`.
- **Not that citations support their claims.** The gate proves a citation resolves and that a research log
  carries its contract; whether a source supports the sentence citing it is the four-lens review's job.
- **Not that a retrieval status is truthful.** `check-research-logs.py` says so in its own output.
- **Not that the guidance is good.** No check scores a rubric or a guide. That is deliberate: a check that
  counted rows would be the countable-target failure [`guide-rubric-spec.md`](guide-rubric-spec.md) warns
  against.

## What the process does not do

- **It does not prove the release is good.** The gate proves structure. See
  [`review-standards.md`](review-standards.md) for the seven defect classes no machine catches.
- **It does not announce anywhere.** No mailing list, no feed beyond GitHub's own.
- **It does not verify the marketplace entry keeps working.** The registry pins a SHA, so a listing goes
  stale silently as the library moves ahead of it. Re-pinning is a deliberate act.
