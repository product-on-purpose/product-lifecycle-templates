# Release notes

The curated read of what changed and why it matters. For the full, unabridged record including
unreleased work, read [`CHANGELOG.md`](CHANGELOG.md); for the per-release pages written by filling this
library's own `release-notes` template, read [`docs/releases/`](docs/releases/).

Newest first.

---

## v0.5.0

**A 27th bundle, `epic`, and it is the first one built because the maintainer wanted it rather than
because a plan said so.**

Two decision records made that possible.
[ADR 0041](docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md) made the
maintainer's own preference set the build order, on the ground that a ranking input which has never been
non-zero cannot rank. [ADR 0042](docs/internal/decisions/0042-epic-joins-delivery-docs.md) then admitted
`epic` to the delivery-docs family, after the first attempt to build it stopped on a gate that neither of
the two records removing the *previous* gates had touched.

**The bundle's research is the part worth reading, because it argues against the easy version of the
document it ships.** The 2020 Scrum Guide contains zero occurrences of the word "epic", confirmed by
literal string search rather than by summary. XP substitutes a splitting rule, the Kanban Method has no
product-sized work unit at all, and LeSS Huge partitions one flat backlog instead. Only SAFe formalizes
the artifact. In its native habitat an epic is a tracker record, not a document, and the bundle says so on
its own catalog card rather than overselling itself.

**Nothing here changes an existing template, a meta field, or the bundle contract.** Upgrading is safe.

**The caveat, unchanged since this library existed: nobody outside this repository has filled one of these
templates.** 27 bundles is a bigger library, not a used one.
[The full note](docs/releases/v0.5.0.md).

---

## v0.4.0

**A second skill, for people who are not using the library, and four claims it was making about itself
that were not true.**

[`plt-grade-doc`](skills/plt-grade-doc/) takes a product document you already have and grades it against
that document type's own researched rubric, quoting your own text back as evidence. You do not have to
adopt a template to get something out of it. **Its first run graded this repository's own governance and
found a defect no automated check here looks for.**

The other half is less flattering and more useful. **The eval harness had never run, and not because
nobody tried.** One line missing from `.gitattributes` made it mechanically impossible on Windows: the
harness scripts had been pure CRLF since they were written, and the permission dialog rejected them as
containing control characters. Once fixed it ran, and produced this project's first real cost figure.
**Four separate claims the library published about itself turned out to be false**, each found by running
something rather than by reading it.

**The honest position is unchanged: zero fills by anyone but the author.**
[The full note](docs/releases/v0.4.0.md).

---

## v0.3.1

**A documentation patch, cut because the previous tag denied the evidence it shipped with.**

The doc-honesty sweep landed one commit after `v0.3.0` was tagged. So the tree the marketplace pins told
readers in four places that **"there are no efficacy evaluations"** while carrying two of them in
`evals/results/`. A published tag is not moved, so the correction is a release.

Two more of the same defect were found on the way and fixed here. **This file** said template quality
"has not been measured" in its standing closing section, three headings below its own `v0.3.0` entry
reporting two VOID runs. And [ADR 0036](docs/internal/decisions/0036-library-prefix-and-skill-under-skills.md)
still called the install retest one that "has never been run", after it had been run and its consequences
written into the next record.

**Nothing you use changes.** No template, no bundle, no gate check.
[The full note](docs/releases/v0.3.1.md).

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
[The full note](docs/releases/v0.2.1.md), backfilled 2026-08-09 and dated as such.

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

Every release above describes coverage and governance, both of which are checkable. **None of them claims
the templates are good.**

Quality has been measured **four times**. Two independent runs on 2026-08-08 over three of the bundles
then in the library returned **VOID** on the discrimination gate, as did a single-scenario run on
2026-08-21. What those runs did show is the **circularity signature**: a clear gap on criteria drawn from
the templates' own guide, beside nothing at all on criteria drawn from neither
([the result](evals/results/2026-08-08_matched-rerun.md)).

**The fourth run, on 2026-09-03, is the first that is not void.** All four validity gates pass and the
bootstrap is non-degenerate for the first time, so it produces a countable gap rather than a shrug
([the result](evals/results/2026-09-03_two-scenario.md)). **What it does not produce is a verdict on this
library.** It covers **two scenarios of one bundle**, `prd`, out of twenty-seven. It also returned a probe
gap of exactly **0.00**, which is ambiguous between "the template does not help a reader" and "the
scenarios were too easy", and the protocol currently specifies neither harder scenarios nor a weaker
generation model to tell those apart.

So the position is narrower than "measured" and better than "unmeasured": **the instrument now works well
enough that a null result is informative, and it has been pointed at one bundle.** No template in this
library has been filled in anger by anyone but its author, and the honest scope of the quality claim is
written up in [what the gate proves](docs/explanation/what-the-gate-proves.md).
