# Companion: Release Notes

> The deep explainer for the Release Notes bundle. Read this to understand what release notes are, how
> they differ from a changelog, where the conventions came from, and where teams disagree. The short
> operator card is [`release-notes_guide.md`](release-notes_guide.md); a worked instance is
> [`release-notes_example.md`](release-notes_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references), tagged by source reliability.

---

## 1. Orientation

Release notes **communicate what changed in a release to users and stakeholders**: what is new, what got
better, what was fixed, and what to watch for [[7]](#ref-7). Their job is comprehension, not record-keeping: they
translate a set of changes into something a reader can act on.

The single most important habit is **writing for the reader, not the shipper**. The classic failure is
notes "written for the team that shipped the feature, not the person who needs to make sense of it":
"Implemented enhanced data persistence layer for improved throughput" where the user needed to hear
"Your reports now load twice as fast" [[6]](#ref-6).

**At a glance**
- Group changes into scannable categories (new, improved, fixed) so readers find what matters fast [[6]](#ref-6).
- Lead with user benefit, in plain language, not implementation detail [[5]](#ref-5)[[6]](#ref-6).
- Be transparent about known issues and breaking changes; it builds trust, not doubt [[6]](#ref-6).
- They are related to, but distinct from, a **changelog** (see [§6](#6-debates-and-contested-boundaries)) [[1]](#ref-1).

---

## 2. Origins and evolution

Release notes are an old software-documentation form, but their modern conventions crystallized around
three reference points:

- **Keep a Changelog (2014).** Olivier Lacan's one-page specification, now the de facto standard for
  open-source projects, codified six change types (Added, Changed, Deprecated, Removed, Fixed, Security)
  and a set of human-first principles, captured in the line "Don't let your friends dump git logs into
  changelogs" [[1]](#ref-1). The current version is 1.1.0 [[1]](#ref-1).
- **Semantic Versioning (SemVer 2.0.0).** Gives the version number meaning: MAJOR for breaking changes,
  MINOR for backward-compatible features, PATCH for fixes. This is why "breaking changes" is a
  first-class section: it drives the version bump [[2]](#ref-2).
- **Conventional Commits (1.0.0).** A commit-message convention (`feat:`, `fix:`, `BREAKING CHANGE:`)
  that lets tools derive both the next version and a draft changelog automatically; `fix` maps to PATCH,
  `feat` to MINOR, a breaking change to MAJOR [[3]](#ref-3). Tooling such as conventional-changelog,
  semantic-release, and Google's release-please automates the whole flow [[3]](#ref-3)[[4]](#ref-4)[[8]](#ref-8)[[9]](#ref-9).

The trajectory is from hand-written, ad hoc notes toward a structured, partly-automated pipeline: commits
generate a changelog, and curated release notes are derived from it for the audience that needs them.

---

## 3. Anatomy (section by section)

The lean notes carry the starred sections (the customer-facing announcement); the full variant adds the
developer-facing record.

**Release header (both).** Product and version, with the date and whether the project follows SemVer.
*Why:* readers orient on what shipped and when. *Expert note:* use ISO 8601 dates (YYYY-MM-DD) to avoid
ambiguity, per Keep a Changelog [[1]](#ref-1).

**Summary (lean).** One or two sentences on what the release is about, in user terms. *Beginner trap:*
"various bug fixes and improvements," which says nothing.

**Highlights (full).** The two or three changes worth surfacing above all else. *Why:* most readers scan;
give them the headline. *Expert note:* if everything is a highlight, nothing is.

**New (lean).** New capabilities (Keep a Changelog "Added"), benefit-led. *Why:* readers check this
first [[6]](#ref-6). *Beginner trap:* implementation language instead of user benefit [[5]](#ref-5)[[6]](#ref-6).

**Improved (lean).** Enhancements to existing functionality. *Why:* shows responsiveness to user needs.
*Expert note:* frame as impact ("twice as fast"), not as the internal change that produced it.

**Fixed (lean).** Resolved issues, before-versus-now, framed positively but honestly [[6]](#ref-6). *Beginner trap:*
dumping raw bug IDs with no user-facing meaning.

**Changed (full).** Behavior changes a user or integrator must be aware of (changed defaults, altered
behavior) that are not pure improvements. *Why:* silent behavior changes break integrations and trust.

**Deprecated (full).** Features marked for future removal, with timeline and the recommended alternative
[[1]](#ref-1). *Expert note:* a deprecation without a migration path and a date is just a threat.

**Removed (full).** Features removed this release, usually previously deprecated [[1]](#ref-1). *Beginner trap:*
removing something depended-upon with no prior notice.

**Security (full).** Security fixes and advisories, with severity and required action [[1]](#ref-1). *Expert note:*
do not bury a security-relevant fix in the generic "Fixed" list; it deserves its own visibility.

**Breaking changes and upgrade notes (full).** What requires action to upgrade safely, with the steps.
*Why:* in SemVer this is what makes it a major release [[2]](#ref-2). *Expert note:* every breaking change needs a
concrete upgrade path, or the notes have failed their main job for that change.

**Known issues (full).** Problems shipping in this release, with workarounds and expected fix timing.
*Why:* if something is not fully resolved, saying so costs less than letting users discover it. Users
respect transparency more than they resent imperfection [[6]](#ref-6).

---

## 4. Variants and sizing

The two variants split along the audience line that defines this artifact.

- **Lean.** The customer-facing announcement: Summary, New, Improved, Fixed. The right default for a
  routine release, written for users in plain, benefit-led language.
- **Full.** Adds Highlights and the full developer-facing record: Changed, Deprecated, Removed, Security,
  Breaking changes with upgrade steps, and Known issues. Use it for a major release, a release with
  breaking changes, or notes that double as the permanent changelog entry.

The nesting rule holds: the lean notes' sections are a strict subset of the full notes', so a routine
note can grow into a full release record in place. The full variant's change types align deliberately to
Keep a Changelog so the same notes can serve as a changelog entry [[1]](#ref-1).

---

## 5. Methodology lineage

- **Methodology-agnostic.** Every team that ships writes some form of release notes, regardless of
  process [[7]](#ref-7).
- **Open-source / Keep a Changelog.** The structured, six-type, human-first changelog, maintained by hand
  or semi-automated [[1]](#ref-1).
- **DevOps / continuous delivery.** Automated generation from Conventional Commits via SemVer-aware
  tooling, with human curation for the customer-facing layer [[2]](#ref-2)[[3]](#ref-3)[[4]](#ref-4)[[8]](#ref-8)[[9]](#ref-9).
- **Product / marketing.** Customer-facing release notes and "what's new" announcements, written for
  adoption and delight, often with screenshots and benefit framing [[5]](#ref-5)[[6]](#ref-6).

The same release can produce both a machine-generated changelog and a hand-curated announcement; mature
teams derive the second from the first rather than writing twice [[1]](#ref-1).

---

## 6. Debates and contested boundaries

**Changelog vs release notes.** The defining distinction. A **changelog** is a portable, permanent,
structured record of every notable change, maintained with the project (Keep a Changelog) [[1]](#ref-1). **Release
notes** are a curated, often customer-facing summary for a specific release, which on a hosting platform
may even disappear if the host does [[1]](#ref-1). They overlap but are not the same: the changelog is the complete
record, the release notes are the audience-shaped story. The master catalog folds "changelog" in as an
alias of release notes [[7]](#ref-7), but the canonical sources treat them as related-yet-distinct [[1]](#ref-1).
*Recommendation:* keep a structured changelog as the source of truth and derive release notes from it; do
not maintain two hand-written records that can disagree.

**Hand-written vs automated.** Conventional Commits plus tooling can generate notes from commit messages
[[3]](#ref-3)[[4]](#ref-4)[[8]](#ref-8)[[9]](#ref-9), but raw generated notes are often unreadable to users ("don't dump git logs") [[1]](#ref-1). *Recommendation:*
automate the changelog, hand-curate the customer-facing notes; let the machine do the record-keeping and
the human do the translation.

**Customer-facing vs internal.** One audience wants benefits and plain language [[5]](#ref-5)[[6]](#ref-6);
the other wants exact behavior, breaking changes stated prominently rather than buried, and migration
steps [[10]](#ref-10). *Recommendation:* this bundle's lean variant is
the customer layer and the full variant the complete record; for a release that needs both, ship the full
notes internally and the lean notes externally, derived from the same source.

**How much to include.** Listing every patch is noise for users; omitting breaking changes is dangerous.
*Recommendation:* always surface breaking changes, security, and known issues; summarize the rest by
benefit.

---

## 7. Anti-patterns and failure modes

- **Git-log dump.** Pasting raw commit messages as notes, the exact failure Keep a Changelog names [[1]](#ref-1).
- **Written for the shipper.** Implementation language instead of user benefit [[5]](#ref-5)[[6]](#ref-6).
- **"Various improvements and bug fixes."** A summary that communicates nothing.
- **Hidden breaking changes.** Shipping a breaking change without flagging it or giving an upgrade path [[2]](#ref-2).
- **Security buried in "Fixed."** A security fix with no separate visibility or severity [[1]](#ref-1).
- **No known issues.** Staying silent about what is not fully resolved, when saying so is what earns
  the reader's trust [[6]](#ref-6).
- **Two diverging records.** A hand-written changelog and hand-written notes that drift out of sync;
  derive one from the other instead [[1]](#ref-1).
- **Ambiguous dates.** Non-ISO dates that read differently across regions [[1]](#ref-1).

---

## 8. Relationships to other artifacts

- **Upstream:** the release plan and deployment plan (what ships and when), and the PRD whose feature is
  now shipping [[7]](#ref-7).
- **Sibling:** the changelog (the structured permanent record release notes are derived from) [[1]](#ref-1), and
  the launch checklist and announcement for a coordinated launch.
- **Downstream:** customer communications, in-app "what's new," support and knowledge-base updates, and
  the next release's "previously known issues now fixed" [[7]](#ref-7).

In this library Release Notes pairs with the `deliver-release-notes` skill and completes the
`delivery-docs` family alongside `prd`, `user-stories`, and `acceptance-criteria`.

---

## 9. Adaptations

- **Routine release.** The lean variant: Summary, New, Improved, Fixed, in user language.
- **Major or breaking release.** The full variant; invest in Breaking changes, upgrade notes, and Known
  issues, where the real reader risk sits [[2]](#ref-2).
- **Open-source library.** Maintain a Keep a Changelog-format CHANGELOG.md as the source of truth and tag
  releases to it [[1]](#ref-1).
- **Continuous delivery.** Generate the changelog from Conventional Commits and SemVer tooling, then
  hand-curate the customer-facing notes [[3]](#ref-3)[[4]](#ref-4)[[8]](#ref-8)[[9]](#ref-9).
- **Regulated or enterprise.** Pair release notes with the formal change record and deployment evidence;
  the notes communicate, the change record audits [[7]](#ref-7).

---

## 10. Worked example

See [`release-notes_example.md`](release-notes_example.md) for full release notes announcing the "Saved
Views" feature (from the PRD, story, and acceptance-criteria examples) shipping in a fictional Acme
Analytics 2.4.0, including a benefit-led "New" entry, a behavior "Changed" note, a security item, and an
honest known issue.

---

## References

Tagged by reliability: `[primary]` originating source or de facto standard; `[practitioner]` recognized
authority; `[vendor]` commercially motivated; `[internal]` this project. Researched 2026-06-30.

<a id="ref-1"></a>[1] Olivier Lacan. "[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)," version 1.1.0. keepachangelog.com, 2014 to present (accessed 2026-06-30). [primary]

<a id="ref-2"></a>[2] Tom Preston-Werner. "[Semantic Versioning 2.0.0](https://semver.org/)." semver.org (accessed 2026-06-30). [primary]

<a id="ref-3"></a>[3] "[Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)." conventionalcommits.org (accessed 2026-06-30). [primary]

<a id="ref-4"></a>[4] "[conventional-changelog](https://github.com/conventional-changelog/conventional-changelog)." github.com (accessed 2026-07-16). [vendor]

<a id="ref-5"></a>[5] ProductPlan. "[How to Write Release Notes Your Users Will Actually Read](https://www.productplan.com/learn/release-notes-best-practices)." productplan.com (accessed 2026-06-30). [vendor]

<a id="ref-6"></a>[6] Appcues. "[Release notes examples](https://www.appcues.com/blog/release-notes-examples)." appcues.com (accessed 2026-07-16). [vendor]

<a id="ref-7"></a>[7] "[Master Catalog of Product Management and SDLC Document and Artifact Types](../../docs/internal/catalog.md)," entry 115 (Release Notes). Internal deep-research catalog, 2026. [internal]

<a id="ref-8"></a>[8] "[semantic-release](https://github.com/semantic-release/semantic-release)." github.com (accessed 2026-07-16). [vendor]

<a id="ref-9"></a>[9] "[release-please](https://github.com/googleapis/release-please)." Google, github.com (accessed 2026-07-16). [vendor]

<a id="ref-10"></a>[10] AnnounceKit. "[Release Notes Best Practices](https://announcekit.app/guides/release-notes-best-practices)." announcekit.app (accessed 2026-07-16). [vendor]
