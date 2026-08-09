# Release notes

The curated read of what changed and why it matters. For the full, unabridged record including
unreleased work, read [`CHANGELOG.md`](CHANGELOG.md); for the per-release pages written by filling this
library's own `release-notes` template, read [`docs/releases/`](docs/releases/).

Newest first.

---

## v0.3.0

**Gold tier, a withdrawn finding, and two defects found by running the install nobody had run.**

The library reached **Gold (advanced)** on the Advanced Skill Library Standard, measured by the
Standard's own gate running in this repository's CI rather than declared.

**The efficacy pilot's headline was withdrawn.** Its held-out gap of -0.81, which read as evidence these
templates suppress decision-usefulness, was an artifact of the measurement: the control arm had been told
to produce decision-usefulness and the treatment arm had not. With the arms matched it is **-0.03**. What
replaces it is quieter and harder to dismiss, and is now measured across two independent runs: **+0.85 on
criteria drawn from the templates' own guide, beside nothing at all on criteria drawn from neither.** Both
runs remain **VOID**. Nothing here is evidence that the templates improve documents.

**`npx skills add` was executed for the first time**, three weeks after the skill shipped, and produced
two defects. It installed a **maintainer-internal build harness** alongside the real skill, because
removing the root `SKILL.md` in v0.2.0 removed a short-circuit that had been suppressing the installer's
subdirectory search. And it installed **12 KB with none of the 26 bundles**, so the skill was reachable
and inert. Both are fixed: the harness is no longer a skill, a check now asserts that what ships equals
what the manifest declares, and the skill stops rather than writing a document it has no template for.

**If you install this library, read [`docs/how-to/installing.md`](docs/how-to/installing.md).** There are
two routes and they do not give you the same thing.

---

## v0.2.1

**The library became listable.** The Product on Purpose plugin registry refuses to list a repository that
ships no `library.json`, treating it as loose components rather than a library. This release adds that
manifest, binding the [Advanced Skill Library Standard](library.json) and declaring a tier.

**The tier was measured rather than declared.** The Standard ships its own conformance gate. Run against
this repository it exits 0 at tier **universal** and prints a real backlog above that ceiling. Declaring a
tier without running the gate would have been this library's own dominant defect, committed into a
governance registry.

**Why this is a separate release from v0.2.0.** The registry pins a commit SHA and requires it to sit on a
release tag whose tree contains the manifest. `v0.2.0` was tagged before its listing contract was read, so
its tree has no `library.json`, and a published tag is not moved. The cost of reading a downstream contract
late is one extra release, and the lesson is now written down in
[`release-process.md`](docs/internal/release-process.md).

## v0.2.0

**The Tier-1 floor is complete.** Every templatable must-have type in the 205-type catalog now ships as a
governed bundle, across nine complete families, and the build backlog is empty. Coverage was the binding
constraint from the beginning of this library; it no longer is.

**The library got a front door.** Before this release every documentation file was maintainer-internal:
the repository documented how it governs itself far better than how to use it. Four user-facing pages now
exist, reachable from the README:
[getting started](docs/tutorials/getting-started.md),
[choosing a template](docs/reference/choosing-a-template.md),
[filling a template](docs/how-to/filling-a-template.md), and
[what the gate proves](docs/explanation/what-the-gate-proves.md).

**It became installable.** A `SKILL.md` and a plugin manifest close a gap that had been open since
2026-07-17, during which `npx skills add` against this repository cloned it and installed nothing.

**Eight unsourced claims across seven family contracts were corrected.** A back-audit tested every
contract assertion against the research logs of the members actually built. Two of every three failures
were **labelling rather than error**: correct content stated as though the field had discovered it. The
result is a new decision procedure requiring every contract sentence to declare which mood it is in, and
none of the corrections changed an obligation.

## v0.1.0

**The first tagged release.** Four bundles and the governance gate that admits them. The gate is the point:
a bundle is not a folder of files that look right, it is a folder that passes eleven checks, and the
checks were written before the bundles were.

---

## What this library does not claim

Every release above describes coverage and governance, both of which are checkable. None of them claims
the templates are **good**, because that has not been measured. No template in this library has been
filled in anger by anyone but its author, and the honest scope of the quality claim is written up in
[what the gate proves](docs/explanation/what-the-gate-proves.md).
