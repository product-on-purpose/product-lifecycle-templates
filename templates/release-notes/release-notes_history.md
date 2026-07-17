# History: Release Notes bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.1 - 2026-07-17 - DF-1 fixed: a first-release mode

**The dogfood loop closes.** DF-1 was found by using this template to write the library's own v0.1.0
release note (below), recorded rather than patched at the time, and is now fixed as its own change.
This is the first template change in the library driven by evidence from use rather than by review.

- **Both variants gain a "FIRST RELEASE?" rule in the HOW TO FILL block.** On a `0.1.0` there is no
  previous release, so "Improved" and "Fixed" (and, in full, "Changed", "Deprecated", "Removed", and
  "Breaking changes") have nothing to be relative to. **Delete them rather than filling them.**
- **It is stated as an explicit override**, because it contradicts the rule directly above it ("if a
  section does not apply, write 'None in this release' rather than deleting it"). An exception that
  does not announce itself as one just reads as a contradiction, and the author has to guess which
  rule wins.
- **The reasoning is given, not just the instruction:** "None in this release" under Improved and
  Fixed reads as a product that improved nothing and fixed nothing, which is false about the work and
  a poor first impression.
- **The escape hatch is named too**, because it is the case this library itself hit: if real users
  have been living on an untagged `main`, things *did* change for them, so the comparative sections
  may carry that, provided the Summary says what "improved" is measured against. Without this, the
  rule would have forbidden the very note that discovered the gap.
- **`release-notes_guide.md` gains the matching rule**, under "Pick a variant", because the guide is
  what an author reads before they copy a file, and a rule that lives only inside the template arrives
  too late to change the choice.
- Cites Keep a Changelog, which the bundle already referenced and whose guidance it had failed to
  carry across: a first release is entirely "Added".

**Not changed: [`docs/releases/v0.1.0.md`](../../docs/releases/v0.1.0.md) still stamps
`source_template_version: 0.1.0`.** It was genuinely filled from 0.1.0, and provenance is a historical
fact, not a label to keep current. The templates and the worked example move to 0.1.1 because they
represent the current shape; the artifact does not, because it records what actually happened.

## 0.1.0, first dogfood 2026-07-17 - DF-1 recorded, template unchanged

**This bundle became the first template in the library to be used for real.** The repository's own
v0.1.0 release note ([`docs/releases/v0.1.0.md`](../../docs/releases/v0.1.0.md)) was written by
filling `release-notes_template-lean.md`: placeholders replaced, guidance comments deleted, provenance
frontmatter kept, sections in the template's order. It held up. **No template change, so
`template_version` stays 0.1.0.**

**DF-1: the lean template has no first-release mode, and it needs one.** Found by using it, which is
the only way this class of defect is ever found.

- **"Improved" and "Fixed" are defined relative to a previous release.** A `0.1.0` has none. The
  sections are structurally meaningless on a first release, and the template offers no guidance for
  the case.
- **The template's own fill rule makes it worse.** "If a section does not apply, write 'None in this
  release' rather than deleting it" would produce a first release note declaring that nothing was
  improved and nothing was fixed. That is false in spirit: plenty was improved and fixed, it simply
  was never *released* before.
- **What was done instead, and why it is a judgment call the template never flagged.** Both sections
  were filled with pre-tag work (the citation pass, the gate widening, the README corrections),
  defensible because this repo's readers have been watching `main` for weeks, so those changes are
  real changes *to them*. But that reasoning is the author's; the template neither prompts it nor
  warns against it.
- **The cited canon already solves this.** Keep a Changelog treats a first release as entirely
  "Added" [[1]](release-notes_companion.md#references). The bundle cites that source and did not carry
  its guidance across.
- **Candidate fix, deferred to 0.2.0** (not made now: v0.1.0 is being tagged, and changing a template
  during its own release is how you get a template that does not match the artifact it produced):
  add a first-release line to the HOW TO FILL block and a matching line in `release-notes_guide.md`,
  saying that on a `0.x.0` first release, New carries everything and Improved/Fixed are omitted rather
  than filled with "None".

## 0.1.0, reviewed 2026-07-16 - citation integrity pass (WP-10)

**No template change, so `template_version` stays 0.1.0.** Both variants, the example, and the meta
contract are untouched; the corrections are to the companion and the research log. `last_reviewed` is
bumped to 2026-07-16.

Every source was fetched and every claim citing it was checked against the actual text. Six defects
were found in a bundle the gate had always passed green, because check E proves that citation anchors
*resolve*, not that a source *supports the claim*.

- **Two combined references split**, which is what caused the rest. Old `[4]` bundled three tools under
  one URL that reached only the first, and is now `[4]` conventional-changelog, `[8]` semantic-release,
  `[9]` release-please. Old `[6]` bundled Appcues with AnnounceKit, **giving AnnounceKit no URL at
  all**, and is now `[6]` Appcues and `[10]` AnnounceKit. The two support *different* claims, and the
  combined entry made it impossible to tell which, which is precisely how the next three defects hid.
- **The "written for the team that shipped the feature" quote** cited `[5][6]`. It is verbatim in
  Appcues; ProductPlan contains none of it. `[5]` dropped.
- **"Transparency improves credibility; users prefer knowing in advance"** was supported by *neither*
  cited source. Reworded to what Appcues actually says: users respect transparency more than they
  resent imperfection.
- **"Breaking changes and migration detail"** cited `[5][6]`; neither supports migration detail.
  AnnounceKit does, verbatim, so that half of the sentence now cites `[10]`.
- **The "No known issues" anti-pattern** claimed users "hit them unprepared", which no cited source
  frames that way. Reworded.
- **A third source vanished between research and references:** the log recorded old source 6 as
  "Appcues / userpilot / AnnounceKit". No reference ever cited userpilot and no surviving claim needs
  it, so it is dropped rather than added as padding.

**The audit's own instruction for this bundle was wrong and was withdrawn, not executed.** WP-10 said
"Keep a Changelog corrected to 1.1.2 with root URL". The spec site serves **1.1.0** as canonical and
redirects `/en/1.1.1/` and `/en/1.1.2/` back to it; the repo tags the audit likely read are site
releases, not spec versions. The existing citation was already correct, so the roadmap was corrected
instead. See `release-notes_research-log.md`.

## 0.1.0 - 2026-06-30

- Initial Release Notes bundle, fourth and final member of the delivery-docs family.
- Variants: `lean` (4 sections: Summary, New, Improved, Fixed, the customer-facing announcement) and
  `full` (strict superset, 11 sections, adding Highlights, Changed, Deprecated, Removed, Security,
  Breaking changes and upgrade notes, Known issues); full change types align to Keep a Changelog. Nesting
  verified by hand.
- Companion researched 2026-06-30 against a tiered source set (Keep a Changelog 1.1.0 verified directly;
  SemVer, Conventional Commits, and customer-facing best practices via search). See
  `release-notes_research-log.md`.
- Status: `beta`. Pending the CI quality gate once the repo scaffold is stood up.
