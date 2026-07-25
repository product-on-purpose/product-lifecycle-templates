---
title: "{{one_line_summary}}"
report_id: "{{report_id}}"
reported_by: "{{reporter}}"
reported_on: "{{date}}"
affected_build: "{{build_or_version}}"
status: "{{report_status}}"
doc_type: bug-report
size: lean
source_template: bug-report
source_template_version: 0.1.0
---

<!--
LEAN BUG REPORT. The intake form: what you saw, how to see it again, what you expected instead, and where.
Four sections, because this is the one document in this family written by people who are not testers -
support agents, salespeople, users, developers in a hurry - and every extra field is a reason to give up and
say nothing. To carry the record through triage and resolution (see bug-report_template-full.md), ADD
sections; never rename or reorder the ones below, because the full variant is a strict superset of this one.

YOU ARE REPORTING AN ANOMALY, NOT DIAGNOSING A DEFECT. At the moment you write this you do not know whether
the cause is a code flaw, a configuration, stale data, or a misunderstanding of the intended behavior. The
standards call this document an "anomaly report" or "incident report" for exactly that reason. Report what
you observed and what you expected; let the investigation decide what it was. Writing as though you already
know is what produces the defensive reply. See bug-report_companion.md sections 1 and 2.

THE ONE THING MOST REPORTS GET WRONG: they leave out what SHOULD have happened. Across roughly 3,000 real
reports, the observed behavior appeared in 93.5 percent and the expected behavior in only 35.2 percent. It
feels obvious to you and it is frequently not obvious to the reader. See bug-report_companion.md section 3.

DESCRIBE THE SYSTEM, NOT THE PERSON. A report that reads as an accusation gets a defensive fix or no fix.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   bug-report_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content. If you can only fill in two sections, fill in Steps to
   Reproduce and Expected and Actual Behavior; those two carry most of the value.
3. If a section does not apply, write "N/A" and one line of why. "Could not reproduce" is a real answer and a
   useful one - do not invent steps to fill the space.
4. Before you file it: DELETE every HTML comment. They are guidance, not content.
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
