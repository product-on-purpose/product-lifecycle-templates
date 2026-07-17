# History: Release Notes bundle

Per-bundle changelog, by `template_version`. Newest first.

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
