# production-readiness-review: history

Change log for the `production-readiness-review` bundle. Each entry records what changed and why, so a
reader can tell a correction from a preference.

## 0.1.0 - 2026-09-28

**Initial release.** Assigned and specced 2026-09-27 in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md), with an admission sweep run the same day while the
spec was written; built 2026-09-28 with a six-dimension research fan-out covering the Google canon, the
published checklists counted item by item, cadence and the cloud frameworks, the neighbors that share the
ground or the name, running the review, and the standing-gap question.
[`production-readiness-review_research-log.md`](production-readiness-review_research-log.md) records **39
sources, all fetched-and-verified**. Every quotation was checked against the source's raw text rather than
a retrieval tool's summary; of 260 quotations the fan-out returned, 233 passed as returned, 22 more were
verbatim apart from rendering artifacts (Markdown syntax, a PDF line-end hyphen, an HTML entity), one was a
real misquote and is corrected, and one verbatim vendor survey percentage was dropped because nobody read
its underlying method.

**The fifth `standing-standards` member, and the first this family's own forecast never named.**
[ADR 0062](../../docs/internal/decisions/0062-production-readiness-review-joins-standing-standards-as-a-tool.md)
assigns `classification: tool`, argued against the honest `foundation` case: the strongest admission
quotation reads as judged-against language, but every source names a reviewer other than the service's own
team, which is the family contract's `tool` marker.

### Admission rests on three bodies that publish the document itself, not only a description of the practice

[ADR 0048](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md)'s bar is met
by Susan Fowler's Appendix A, GitLab's issue template (three maturity gates, 69 items), and Mercari's
four-file Production Readiness Check. Google's own account of the type, chapter 32 of *Site Reliability
Engineering*, describes a checklist the company maintains without publishing it, and is the type's load-
bearing source for its definition, trigger, team size, and stated limitation regardless.

### One logged source is a name collision the bundle only partly follows

Federal Student Aid's own "Production Readiness Review" reviews each release before implementation, which
is the launch moment, not a standing handoff. It is not counted toward admission on its own. The bundle
takes from it only four elements every readiness review needs: evidence for each item, a written reason
for every not-applicable answer, a sign-off naming the open issues it accepts, and a signatory that rises
with risk. Its release-moment content, rollback activation criteria, the business cost of delay, a
post-implementation configuration check, and a workforce-relations review, is left to
`launch-coordination-checklist` and `runbook` instead. A second, unrelated name collision, the
hardware-manufacturing milestone NASA and the US Department of Defense both publish under the identical
name, shares no lineage at all and is named in the template so a reader who has met the phrase in an
aerospace or defense context is not misled.

### No outcome vocabulary read for this bundle is a published standard, and the template says so

One vendor's own four-state governance model states plainly, "these states are a recommended governance
model, not a Google, AWS, or Kubernetes platform behavior." A second vendor's model is a plain binary
instead. The template borrows three of the four-state model's states, an unconditional "ready" alongside
"ready with conditions" and "not ready," and drops the fourth, "withdrawn," which concerns a launch whose
scope or date moved rather than a service's own readiness, and attributes the borrowed vocabulary rather
than presenting it as settled practice.

### Licenses decided what could be adapted rather than only quoted

Google's two books carry a CC BY-NC-ND 4.0 license, which permits quoting but forbids adapting their
wording; the Readiness Criteria domain list is therefore built across sources rather than copied from
Google's own six-area list. Mercari's production-readiness-checklist repository is MIT-licensed, so its
evidence-and-status mechanics and its not-applicable rule are adapted with attribution rather than only
quoted.

### The review trigger is genuinely sourced, unlike this family's first two members

AWS names three sources for a new question, real incidents, near-misses, and named worries that have not
yet occurred, and ties incident review to the checklist through a named question answered by a standing
"Ops Champion" role. A vendor's own gate model tempers how loosely that trigger should be read: a
question earns a place only when it states the failure it prevents, the evidence that answers it, and the
launch types it applies to.

### The boundary with the launch coordination checklist holds by object, not by trigger

Google's own two chapters separate the two documents by trigger, team, and timing, but adopters blur that
trigger in practice: Mercari gates all services before real production traffic, GitLab gates each maturity
level of a new service, Grafana names a "pre-launch PRR," and Federal Student Aid runs its own PRR on every
release. What holds across every source read is the object rather than the trigger: this review asks
whether a service can be run on a standing basis, the launch checklist asks whether one specific launch is
ready. That reading is this library's own, drawn from the sources' wording rather than stated outright by
any one of them.

### `pairs_with: []`, checked and confirmed empty rather than left empty by default

No pm-skills skill ID in [`tools/known-skills.txt`](../../tools/known-skills.txt) names a production
readiness review, an operational readiness review, or an SRE entrance review. `pairs_with` is declared
empty because that was verified against the pinned list, not assumed.

### No `default_format` key is declared

This bundle found one shape for the document type and carries no format key, consistent with the majority
of members built before the format-axis backfill.
