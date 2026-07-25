---
title: "{{one_line_summary}}"
report_id: "{{report_id}}"
reported_by: "{{reporter}}"
reported_on: "{{date}}"
affected_build: "{{build_or_version}}"
severity: "{{severity}}"
priority: "{{priority}}"
assigned_to: "{{assignee}}"
status: "{{report_status}}"
doc_type: bug-report
size: full
source_template: bug-report
source_template_version: 0.1.0
---

<!--
FULL BUG REPORT. The tracked record: the reporter's four sections, plus the evidence, the classification, the
triage decision, and what was actually wrong and what now stops it recurring.

NOTICE WHO FILLS IN WHAT. The first four sections are the reporter's, written at intake, and Evidence is
usually theirs too (attach it while you still have it). The remaining three - Impact/Severity/Priority,
Triage and Ownership, and Resolution and Regression Guard - are filled in by other people, later, as the
report moves through triage and resolution. That is the real difference between the two variants: lean is the
intake form, full is what the record becomes. Do not put this version in front of a user or a support agent;
use the lean one and let the record grow.

THIS VARIANT IS A STRICT SUPERSET OF THE LEAN ONE. The four lean sections appear here in the same order, with
the same headings and the same placeholders, and four sections are added.

YOU ARE REPORTING AN ANOMALY, NOT DIAGNOSING A DEFECT. At the moment the report is written nobody knows
whether the cause is a code flaw, a configuration, stale data, or a misunderstanding of intended behavior.
The standards call this document an "anomaly report" or "incident report" for exactly that reason. See
bug-report_companion.md sections 1 and 2.

DESCRIBE THE SYSTEM, NOT THE PERSON. A report that reads as an accusation gets a defensive fix or no fix.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   bug-report_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. For
   tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Sections 5 to 8 stay empty until there is something true
   to put in them; an empty triage section is honest, an invented one is not.
3. If a section does not apply, write "N/A" and one line of why.
4. Before you file or close it: DELETE every HTML comment. They are guidance, not content.
-->

# {{report_id}}: {{one_line_summary}}

## Summary

<!-- WHAT  One or two sentences: the observable failure, where it happens, and who it affects. This is what a
           reader sees in a triage queue before deciding whether to open the report.
     WHY   A triage list is read fast. A summary that names the observable failure and its context can be
           routed without opening it; one that names a suspected cause sends the reader down your hypothesis
           instead of to the evidence. Deep dive: bug-report_companion.md section 3 (Summary).
     ASK   What actually went wrong, in plain words? Where does it happen (feature, screen, endpoint)? Who
           does it affect, and roughly how many? Is anything lost or exposed?
     GOOD  "A user who is not entitled to a region can see that region's totals through a shared saved view.
           Affects any recipient of a shared view whose filter includes data they cannot otherwise access."
     WEAK  "Permissions are broken." (no observable behavior, no location, no affected population - and it is
           a diagnosis, which may be wrong)
     TRAP  Writing your theory as the summary. If you have a theory, it is welcome, but put it at the end of
           Expected and Actual Behavior and label it as a guess. -->

{{summary}}

## Steps to Reproduce

<!-- WHAT  Numbered steps from a known starting state to the failure, short enough that someone will actually
           run them.
     WHY   This is the deliverable. The aim of the whole document is to let the reader see the failure
           themselves, and the research consistently puts steps to reproduce at the top of what developers
           want. It is also what they most often do not get. Deep dive: bug-report_companion.md section 3
           (Steps to Reproduce).
     ASK   What state do you start from - which account, which data, which configuration? What exactly did you
           do, in order? Which step is the one where it goes wrong? What is the shortest path that still
           triggers it? Have you tried it twice?
     GOOD  "1. Sign in as an analyst with access to AMER only (test account R). 2. Open dashboard DB-7.
           3. Select the shared view 'EMEA weekly'. 4. Read the Total Revenue tile. -> The tile shows the
           EMEA total, which this account should not be able to see."
     WEAK  "Open a shared view and look at the total." (which account, which entitlements, which dashboard,
           which view? Two readers will construct two different tests and one of them will not reproduce it)
     TRAP  Starting in the middle. "Open the app" hides the account, the data and the configuration, which are
           usually the parts that matter. If you cannot reproduce it, say so plainly here and put everything
           you do know in Environment and Reproducibility - an honest "seen once, could not repeat" is far
           more useful than invented steps. -->

{{steps_to_reproduce}}

## Expected and Actual Behavior

<!-- WHAT  What you expected to happen, what happened instead, and where your expectation comes from.
     WHY   Two reports in three never say what should have happened, and it is the single most-omitted
           element in real bug reports. It feels obvious to you; the reader often genuinely does not know the
           intended behavior, especially if they did not build that part. Deep dive:
           bug-report_companion.md section 3 (Expected and Actual Behavior).
     ASK   What did you expect, precisely? What happened instead, precisely? Where does the expectation come
           from - an acceptance criterion, documentation, the previous release, or your own assumption? Would
           a reasonable person expect the same?
     GOOD  "Expected: the Total Revenue tile shows only regions this account is entitled to, so AMER only.
           (The design says entitlement is re-checked when a recipient opens a shared view.) Actual: the tile
           shows the combined AMER + EMEA total, and the EMEA rows are correctly hidden from the table below -
           so the row filter works and the total appears not to."
     WEAK  "It shows the wrong number." (wrong compared to what? The reader cannot tell whether this is a bug
           or a misunderstanding, and their fastest move is to close it as working-as-designed)
     TRAP  Skipping the expectation because it feels self-evident, or stating a cause instead of an
           observation. "The aggregate is computed before the filter" is a useful guess - label it as one and
           keep it separate from what you actually saw. -->

{{expected_and_actual}}

## Environment and Reproducibility

<!-- WHAT  Where you saw it (build, environment, account, device, browser, configuration) and how reliably it
           happens.
     WHY   Environment detail is the defense against "works for me", and reproducibility is a field rather
           than an adjective: many bugs are intermittent, and how often it happens changes both the diagnosis
           and the priority. Non-reproducible reports are a large studied category, not a personal failing.
           Deep dive: bug-report_companion.md section 3 (Environment and Reproducibility).
     ASK   Which build or version? Which environment (production, staging, local)? Which account, and with
           what permissions? Which browser, device, OS? How many times out of how many attempts did it
           happen? Did anything else change around the same time? Have you searched for an existing report?
     GOOD  "Staging, build 2.3.1, saved_views flag on. Test account R (AMER entitlement only), Chrome 141 on
           macOS. Reproduced 5 times out of 5, including after a hard refresh and in a private window. No
           existing report found for 'shared view total'."
     WEAK  "Latest version, my machine, happens sometimes." (no build, no account, no configuration, and
           'sometimes' is not a frequency)
     TRAP  Leaving out the account and its permissions on anything access-related. On permission bugs the
           account IS the test case, and a report without it cannot be reproduced at all. -->

{{environment_and_reproducibility}}

## Evidence

<!-- WHAT  Screenshots, recordings, logs, stack traces, request or response captures, and the identifiers that
           let someone find them again.
     WHY   Evidence supports the steps rather than replacing them, and it becomes decisive when the failure is
           intermittent and steps alone will not reproduce it. Stack traces in particular are among the things
           developers most want and most rarely get. Deep dive: bug-report_companion.md section 3 (Evidence).
     ASK   What artifact shows the failure most directly? Is there a trace, a log line, a request ID or a
           correlation ID? What should the reader look at in the attachment, and at what timestamp? Is there
           anything sensitive that needs redacting first?
     GOOD  "Screenshot of the tile showing 1,284,900 with the table below listing only AMER rows
           (attached: shared-view-total.png). API response for GET /dashboards/DB-7/views/SV-31 attached
           (response.json); note `total` at line 3 against the empty EMEA rows array. Request ID
           7f3c-...-a91, staging logs 2026-07-09 14:22 UTC."
     WEAK  "See attached." (which of the four attachments, and what am I looking for in it?)
     TRAP  Attaching a twenty-minute screen recording with no timestamp. Evidence nobody can navigate is
           evidence nobody uses. Say where to look. And redact credentials and personal data before
           attaching. -->

{{evidence}}

## Impact, Severity and Priority

<!-- WHAT  What this costs, how severe it is, how urgent it is, and who set each value.
     WHY   Severity and priority are INDEPENDENT axes and conflating them is the classic classification
           error. Severity is how much damage the defect does; priority is how soon it should be fixed. A
           crash in a rarely used legacy path is high severity and low priority; a cosmetic error on a launch
           homepage is low severity and high priority. Deep dive: bug-report_companion.md section 3 (Impact,
           Severity and Priority).
     ASK   What is the damage: data loss, exposure, wrong numbers, blocked work, annoyance? How many users,
           and can they work around it? On your team's scale, what severity? How soon must it be fixed, and
           why that soon? Who assigned each value?
     PRIORITY  Use your team's defined scale and put the level definitions where reporters can see them.
           There is NO standard severity scale: four, five and six-level scales are all in use, and S1-S4
           numbering means different things in different places. Record who set each value, because the
           certification definitions say what the words mean and specify nobody to assign them.
     ROW HINT  A good row gives the value, the reason in a few words, and the person who set it. A weak row
           gives a bare label.
     GOOD  | Severity | S1 Critical | Data exposure across an entitlement boundary; not user-recoverable | Anjali Rao (QA) |
     WEAK  | Severity | High | | |
     TRAP  Inflating severity to get attention. Severity is the signal the release gate reads; once it is
           used as a negotiating position it stops carrying information, and the gate stops meaning
           anything. -->

| Field | Value | Why | Set by |
|---|---|---|---|
| Severity | {{severity_value}} | {{severity_reason}} | {{severity_owner}} |
| Priority | {{priority_value}} | {{priority_reason}} | {{priority_owner}} |

{{impact_narrative}}

## Triage and Ownership

<!-- WHAT  What triage decided, who owns the defect now, and which release it is assigned to.
     WHY   Triage is where a report stops being a claim and becomes work: the meeting reviews new reports,
           validates or corrects severity and priority, and assigns ownership and a release. Recording the
           outcome is what stops the same argument happening twice, and it is where this document meets the
           test plan's release gate. Deep dive: bug-report_companion.md section 3 (Triage and Ownership).
     ASK   What did triage decide - fix now, fix later, reject, needs investigation, cannot reproduce? If a
           value was changed from what the reporter set, why? Who owns it now, by name? Which release is it
           assigned to? Does it block a gate?
     GOOD  "Triaged 2026-07-09. Severity confirmed S1; priority raised from P2 to P1 because the test plan's
           exit criteria treat any entitlement failure as a suspension event, not a triage item. Owner:
           Marcus Bell. Assigned to the 2.3.1 hotfix. Blocks phase 2 of the Saved Views rollout until fixed
           and re-verified."
     WEAK  "Triaged. Assigned to engineering." (no decision, no named owner, no release, and no record of
           whether the classification changed)
     TRAP  Silently changing the reporter's severity. If triage disagrees, say so and say why - the reporter
           learns the scale, and the next report is better classified. -->

{{triage_and_ownership}}

## Resolution and Regression Guard

<!-- WHAT  What was actually wrong, what changed, and what now stops it coming back.
     WHY   Root cause belongs here rather than in the reporter's sections, because it is the output of the
           investigation rather than an input to it. And the last line is the one that matters most: a closed
           defect with no regression guard is an invitation to fix the same thing twice. Deep dive:
           bug-report_companion.md section 3 (Resolution and Regression Guard).
     ASK   What was the actual cause, as opposed to the first theory? What changed, and where (commit, PR,
           release)? How was the fix verified, by whom, and against which steps? What test now guards this,
           by ID? Was anything else found on the way?
     GOOD  "Cause: the aggregate for the Total tile was computed before the entitlement row filter was
           applied, so filtered rows still contributed to totals. The row-level check was correct throughout,
           which is why the table looked right. Fixed in PR 812, released in 2.3.2. Verified by Anjali Rao
           against the original steps on 2026-07-11. Regression guard: TC-047 step 4, which now asserts the
           aggregate as well as the rows."
     WEAK  "Fixed." (no cause, no change reference, no verification, and nothing stopping a recurrence)
     TRAP  Reopening this report if the defect recurs later. Open a new one and link it: a reopened ticket
           loses the record of what was fixed the first time, and you lose the ability to tell a regression
           from an incomplete fix. -->

{{resolution_and_regression_guard}}
