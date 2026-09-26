---
title: "Dashboard Sharing Opens for the Reporting Squad"
doc_type: announcement-internal-comms
size: lean
audience: "All Acme Analytics staff"
channel: "#platform-launches Slack channel and the Friday company email digest"
send_date: "2026-07-18"
sender: "Priya Nair (PM, Reporting)"
status: sent
doc_version: "1.0"
created: "2026-07-18"
updated: "2026-07-18"
related_links:
  - "../prd/prd_example.md (Saved Views for Dashboards PRD, the feature this announcement covers)"
  - "../launch-coordination-checklist/launch-coordination-checklist_example.md (the Go/No-Go record this step shipped against)"
source_template: announcement-internal-comms
source_template_version: 0.1.0
---

> **Worked example.** A filled `announcement-internal-comms`, the bundle's only size, sent the day after the
> Saved Views Sharing launch's exit review on 2026-07-17, the same review the
> [`launch-coordination-checklist`](../launch-coordination-checklist/launch-coordination-checklist_example.md)
> example records as a same-day snapshot. Its sender, Priya Nair, is that checklist's own named communications
> owner for this launch. Its Known Issues section names two open items that must not be confused: the checklist's
> accepted Yellow (no switch yet that turns sharing off everywhere at once) and R-05, the program's shared-view
> exposure risk, escalated to the steering group on 14 July. It does not link the family's `release-notes`
> example, because that document predates this launch and already lists sharing as shipped; the research log
> records that contradiction. Two later events in the same Acme Analytics thread postdate
> this announcement and are not cited in the body below: the Reporting Squad Definition of Done's 2026-07-24
> amendment, and `status-report_example.md`'s account of 14 to 28 July, which still carries R-05 as escalated
> and unresolved on the day it was written. Read this alongside
> [`announcement-internal-comms_guide.md`](announcement-internal-comms_guide.md), the rubric it was graded
> against. Names already established elsewhere in the library's Acme Analytics thread are reused as
> established; the Slack channel name, the email digest, and any date or figure not otherwise cited are
> illustrative.

# Dashboard Sharing Opens for the Reporting Squad

## Headline

As of today, a teammate on the Reporting squad can share a saved dashboard view with you. Nobody
outside that squad has the button yet.

## What Is Changing, and When

Sharing is the second half of the Saved Views work, the half that lets one person's saved filter,
date range, and column setup reach someone else's screen instead of staying locked to the account
that built it. It rolls out behind the same `saved_views` flag that has already carried private
views since late June, in two separate steps rather than one. The first step goes live today and only
reaches dashboards the Reporting squad itself owns; nobody on another team can open a shared view
yet, whatever their own dashboards look like. The platform team is holding this first step open for
48 hours under close watch before anyone decides whether to widen it. A second step, turning sharing
on everywhere at Acme Analytics, follows only once Dana Osei signs off a second time. That sign-off
has not happened, and no date for it exists yet.

**Who this applies to:** Reporting squad members who own a dashboard, and any teammate they choose
to share a saved view with. Everyone else keeps using Saved Views exactly as before.

**Effective date:** 2026-07-18 for the Reporting-squad step above. A date for the wider step is not
set.

## Why It Matters

The friction study behind this feature found one pattern more often than any other: an analyst
reopening a report and rebuilding a filter and date range they had already built the day before,
because nobody else could reach their saved setup. Sharing removes the rebuilding, not the
permissions underneath it. Hand a teammate a view, and they open your filters already applied; they
do not open your access.

## What It Means for You

If you are on the Reporting squad, you can already share a saved view with a teammate today, the
same way you save one now. If you sit outside Reporting, this step does not reach your dashboards
yet, and you will hear from this same channel before it does. If a colleague asks why they cannot
share a view on a dashboard the two of you both use outside Reporting, the honest answer is timing,
not a fault: that capability simply is not turned on for them yet.

**What is not changing:** Opening a view someone shared with you never hands you a row, a column, or
a total your own account could not already reach on its own. The view moves; your entitlement does
not move with it.

**What you need to do:** Nothing, if you sit outside the Reporting squad. If you manage a Reporting
dashboard that people outside the squad also use, tell Marcus Bell before turning sharing on for it:
today's step assumes every dashboard it reaches is one the Reporting squad itself owns.

**By when:** Before you enable sharing on any dashboard used outside the Reporting squad. There is no
deadline for anyone else.

## Known Issues

Two things are still open, and they are different. First, the program's risk register carries R-05: a
shared view could disclose data its recipient's own entitlement should not reach. The fix that let this launch
pass its security review on 2026-07-15 closed the case that was actually found, but the wider risk has been
with the steering group since 14 July, neither funded down nor formally accepted. If anyone reports a total
on a shared view that looks more complete than their own access should allow, treat it as urgent and send it
straight to Jordan Ames. Second, sharing can only be switched off one dashboard at a time. On-call can do that
immediately, with no approval needed, and every other dashboard keeps working; a switch that turns sharing off
everywhere at once does not exist yet. Dana Osei accepted that gap for launch on 2026-07-17, through
2026-08-15.

## Where to Learn More

The feature itself is specified in the
[Saved Views for Dashboards PRD](../prd/prd_example.md). The
[platform team's launch coordination checklist](../launch-coordination-checklist/launch-coordination-checklist_example.md)
carries the actual Go/No-Go record this step shipped against, including the accepted gap named above.
A short guide covering how to save a view, turn sharing on for it, and choose a default already lives
in the help center, linked from the Views control itself. The customer-facing release note for this step is
being drafted separately and is not linked here yet; treat this announcement as today's internal record.

**Questions:** Priya Nair (PM, Reporting) for anything above. Route an access or entitlement question
straight to Jordan Ames (Support Lead), who already has the briefing this note summarizes.

**Next update:** No later than 2026-08-15, when Dana Osei is due to revisit the accepted kill-switch
gap either way. Sooner, the day the wider step actually opens.
