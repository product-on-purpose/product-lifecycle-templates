---
title: "Reporting Squad Definition of Done"
doc_type: definition-of-done
size: full
team: "Reporting Squad, Acme Analytics"
owner: "Priya Nair (PM, Reporting)"
status: active
doc_version: "1.1.0"
created: "2026-02-02"
updated: "2026-07-24"
related_links:
  - "../sprint-backlog/sprint-backlog_example.md (Sprint 24 Sprint Backlog; items are judged against this document)"
  - "../acceptance-criteria/acceptance-criteria_example.md (acceptance criteria for the default-view story; this document is the standing floor beneath it)"
  - "../bug-report/bug-report_example.md (DEF-2291; the incident that triggered the 2026-07-24 amendment below)"
  - "../test-plan/test-plan_example.md (Saved Views test plan; its permission matrix is now a Sprint-level criterion here)"
source_template: definition-of-done
source_template_version: 0.1.0
---

<!--
This is a worked example for the definition-of-done bundle: a realistic, fully filled full-variant
Definition of Done for the Reporting Squad at the fictional Acme Analytics, the same squad and product
whose Saved Views feature the delivery-docs and qa-docs family examples deliver. Per this family's own
contract, the chaining is deliberately lighter than a phase-output document's: this is written as the
kind of Definition of Done the sprint-backlog and acceptance-criteria examples could plausibly be judged
against, not as an artifact either of those documents produces.

It is shown mid-life, at doc_version 1.1.0, not at first adoption, so the Review Trigger section can be
demonstrated firing rather than only described: DEF-2291 (see bug-report_example.md) shipped because no
criterion here required the permission matrix to be re-executed when entitlement-relevant code changed,
and the squad amended this document once that gap was named. Figures marked "illustrative" are made up
for the example; the rest is drawn from names, dates and facts already established elsewhere in this
library's Acme Analytics thread. A Definition of Done is a living document; this is a snapshot as of the
updated date above, with every guidance comment already deleted, as the template itself instructs before
a real team shares it.
-->

# Reporting Squad Definition of Done

## Scope and Ownership

Binds every Developer on the Reporting Squad, for every Product Backlog Item the squad presents at Sprint
Review, regardless of which of the squad's services the item touches (the dashboard-service today,
whatever the squad owns next). Acme Analytics carries no organization-wide Definition of Done as of this
writing, so under the branch of the rule that applies when no such standard exists, the Reporting Squad
has written its own rather than inheriting one. This is the only Definition of Done the squad uses: there
is no separate release-level or program-level version sitting underneath or on top of it, and the squad
does not maintain one document for features and another for hotfixes.

If Acme Analytics adopts an organization-wide standard later, this document must be raised to at least
that floor and never left below it; any criterion here that already exceeds the future organizational
standard stays exactly as written, unchanged by the adoption. Until that happens, this squad's own
agreement is the whole of the bar.

## Done Criteria

- [ ] Merged through a pull request carrying an approving review from a Developer other than the author,
      with every review comment resolved, not merely acknowledged.
- [ ] Every changed line is exercised by the CI pipeline's unit and integration suite, and the suite is
      green on the merge commit, not on an earlier commit in the same branch.
- [ ] The story's agreed acceptance criteria are all checked off, confirmed by a Developer other than the
      one who implemented the story.
- [ ] The feature ships behind a flag, and the flag's intended default state at merge (on or off) is
      written into the pull request description before it is merged, not decided afterward.
- [ ] Confirmed working on staging by a squad member who did not write the change, using the same steps a
      user would take, not just a passing automated check.
- [ ] Any new or changed REST endpoint has its request and response shapes recorded in the squad's API
      contract notes before merge.
- [ ] No new S1 Critical or S2 Major defect is open against the surface the change touches at the moment the item
      is presented at Sprint Review.

## Criteria by Level

Sorted by asking, for each item above and each item below: can the squad realistically clear this for
every single feature? If not, every sprint? If not, only at release. An item that reads stricter than
that at a glance still gets placed at the level it actually clears, not the level that looks best.

| Criterion | Level |
|---|---|
| Pull request reviewed and approved by a Developer other than the author, all comments resolved | Feature |
| Confirmed working on staging by a squad member other than the author | Feature |
| Story's acceptance criteria checked off by someone other than the implementer | Feature |
| New or changed REST endpoint's contract recorded before merge | Feature |
| Full end-to-end regression suite green against the release branch | Sprint |
| Entitlement or permission matrix re-executed in full whenever entitlement-relevant code changes (added 2026-07-24; see Review Trigger) | Sprint |
| Keyboard and screen-reader check (WCAG 2.2 AA) on any new or changed UI control | Sprint |
| Migration dry run and rollback rehearsal completed against a production-sized dataset | Release |
| Security review sign-off for any change that touches a permission boundary | Release |

## What This Excludes

**Not a Definition of Ready.** The squad does not currently keep one. Entry into a sprint is judged at
backlog refinement against the item's own clarity, not against a written document; if the squad adopts a
Definition of Ready later, it will gate entry into the sprint, not exit from it, and will not replace
anything above.

**Not the CI quality gate.** The pipeline's own gate (line coverage at or above 80 percent (illustrative
threshold), no new critical or blocker static-analysis findings) runs on every pull request automatically.
"Every changed line is exercised" and "the suite is green," the first Done Criterion above, take that gate
as one input among several; this document does not restate the gate's own configuration, which lives in
the pipeline, not here.

**Not the squad's coding style guide.** Naming, formatting and file-layout conventions live in the
Reporting Squad's own wiki page and are enforced by lint on commit. A pull request can fail lint and still
be reviewable; it cannot merge, but that is the lint job's rule, not a line in this document.

**Not "done done."** A few engineers on the squad still use that older phrase informally for the same idea
this document now formalizes. Where the phrase and this document would disagree about a specific item,
this document wins, because it is the one Sprint Review is actually judged against.

## When Work Does Not Meet It

An item that still fails a criterion above when the sprint ends does not go to Sprint Review and does not
ship, regardless of how close it is or how much work remains on it. It goes back onto the Product Backlog
for Priya Nair to re-rank against everything else the squad could work on instead; it is never carried
into the next sprint's plan by default just because it was already in progress. It does not count toward
the sprint's velocity either, so pulling in more than the squad can finish does not make the burndown look
better, it only moves the shortfall from one number to another.

Confirming that an item does not meet this bar is not Priya Nair's call alone. Any Developer on the squad
can flag that a criterion above is not met, and once flagged, the item does not go to Sprint Review even
if the rest of the squad would rather present it anyway. Priya Nair checks in on trending risk at the
Daily Scrum, but she is not the gate; the criteria above are.

## Review Trigger

**Trigger:** a shipped S1 Critical or S2 Major defect is confirmed to have escaped because none of the criteria
above covered the failure mode it exposed. A defect that slipped past a criterion that already existed is
a testing gap, not a gap in this document, and does not fire this trigger on its own. Separately: the
squad adding a deployment environment beyond staging and production also fires it.

**Noticed by:** the Developer who owns the fix names the specific gap in the incident's regression-guard
note. That named gap is brought to the squad's next sprint planning, not the retrospective, because
planning is the moment the squad next commits to what "done" means for the work ahead of it, and a gap
named at planning gets tested against real upcoming work before it is adopted.

**Fired once, on 2026-07-24.** DEF-2291 shipped in build 2.3.2 because nothing in the original Done
Criteria required the entitlement or permission matrix to be re-executed when entitlement-relevant code
changed; every row-level check in the original list passed cleanly while the aggregate total leaked data
across the entitlement boundary. Marcus Bell, who owned the fix, raised the gap at the planning session
that opened the next sprint, where the squad adopted the Sprint-level "entitlement or permission matrix
re-executed" row above, taking this document from version 1.0.0 to 1.1.0.
Nothing else in this document changed at that revision.
