---
title: "{{product_name}} Requirements Traceability Matrix"
product: "{{product_name}}"
owner: "{{owner}}"
last_reconciled: "{{last_reconciled}}"
status: "{{status}}"
doc_type: requirements-traceability-matrix
size: lean
source_template: requirements-traceability-matrix
source_template_version: 0.1.0
---

<!--
LEAN REQUIREMENTS TRACEABILITY MATRIX. The smallest matrix that is still a real one: what it covers
and which place is the record, the rules that say what a link and a status mean, the table of
requirements with what verifies each, the gaps in both directions, and the owner with a stated trigger
for updating it. This is what TestDevLab describes, requirement to test, read in both directions. Use it
by default. To grow it into the full form (see requirements-traceability-matrix_template-full.md), ADD
sections: Implementation Trace, Risk Control Trace and Baselines, after Coverage Gaps and before Upkeep
and Review Trigger. Never rename or reorder the sections below, because the full variant is a strict
superset of this one. The signal to scale up is a question the team owes an answer to that this table
cannot give: which design element implements a requirement, which control covers a risk, or what an
auditor saw at a given release. That signal is this library's POSITION, and confidence in the lean and
full split is medium-low.

WHAT A REQUIREMENTS TRACEABILITY MATRIX IS. TestDevLab, a vendor, gives the narrowest definition: "A
Traceability Matrix is a document that links and maps project requirements to their corresponding test
cases." In this library's reading, it is a standing register, edited as requirements and tests change, not a record filed once.
Traceability is a property, and the matrix is one way to hold it: InfoQ reports Brad Appleton writing
"Traceability matrix on the other hand is one of the possible implementations of traceability." The
first use of the phrase is not established by anything read, and this template offers no origin story.

A LINKED TEST IS NOT A VERIFIED REQUIREMENT. NASA ties completion of verification to "documented
objective evidence of compliance with requirements or waiver" and to "closure of all discrepancy and
nonconformance reports". A test case ID in a Verified by cell shows that a test exists, not that the
requirement was verified. Trace Conventions is where the matrix says which of the two its status words
mean.

THIS TYPE IS CONTESTED, AND NOTHING READ SHOWS THAT KEEPING ONE IMPROVES OUTCOMES. InfoQ's 2008 roundup
reports Alistair Cockburn writing "I have, in 30 years in the business, in industry, research and a
little bit in government, NEVER seen a traceability matrix pay off." That is a second-hand report of a
mailing-list post. This research found no named software team outside regulated or safety-critical work
that describes keeping one (high confidence that the search found none, medium that none exists). A
mapping study of 63 papers says "strong empirical evidence from industry is needed to validate the
impact of traceability on maintenance and evolution". Keep a matrix only where the team has decided it
owes a whole-set answer to the question of which requirement has no verification, and say so in Purpose
and Boundary. Where a tracker already holds the links, that tracker is the record and this file should
say so. That recommendation is this library's POSITION. This matrix is also not NASA's requirements
verification matrix, which is a related artifact. No standard was read for this bundle, so nothing here
says what IEEE 829, IEEE 830, ISO/IEC/IEEE 29148, 21 CFR 820 or DO-178C requires.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP;
   the three table sections also carry PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. Write the Purpose and Boundary and Trace Conventions sections before
   you fill a single row, because the rows mean nothing until the status words are defined. Give each
   requirement a short label and a link to its source document; never copy the requirement's text
   into the matrix.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it. A reader
   cannot tell a deleted section from one nobody considered.
4. A matrix is never finished, but before you share it: self-grade against
   requirements-traceability-matrix_guide.md, then DELETE every HTML comment. They are guidance, not
   content.
-->

# {{product_name}} Requirements Traceability Matrix

## Purpose and Boundary

<!-- WHAT  A short statement of the product and requirement set this matrix covers, what the team
           chose not to trace, who keeps it, and whether this file or a named tool is the record.
     WHY   The sources disagree on what the matrix is: a table of requirements and test cases for
           TestDevLab, a wider chain for Visure, and for Jama, a vendor that sells the live
           replacement, the wrong form altogether. A reader needs to know which of these the file
           claims to be, so the section names the one place that is the record. NASA says a matrix
           "can be manually created and maintained, or may be a by-product of a requirements
           management tool". This is also where an unregulated team justifies the matrix to itself:
           what it chose to trace, what it chose not to, and when it will stop. The boundary
           statement is this library's POSITION, and no source read asks for one. Deep dive:
           requirements-traceability-matrix_companion.md section 3 (Purpose and Boundary) and
           section 6.
     ASK   Which product, and which set of requirements, does this matrix cover, and what did the
           team choose not to trace? Who keeps it? Is this file the record, or does a tracker hold
           the links, and if so what does this file add? Why is the team keeping a matrix at all,
           and what will make it stop?
     GOOD  "This matrix covers the offline-sync requirements of Harbor Notes, REQ-20 to REQ-27, and
           nothing else in the product. It is kept by the sync team's QA lead. This file is the
           record: the team's tracker holds tickets but no requirement-to-test links. Not traced:
           attachment sync, which is out of scope this quarter. The team keeps a matrix because a
           sync defect can lose a user's notes, and will stop when the sync rewrite ships and the
           tracker holds the links."
     WEAK  "Requirements traceability matrix for the product." (names no requirement set, no record,
           no reason to keep one and no stop condition, so a reader cannot tell what the table
           claims to cover or whether it is still wanted)
     TRAP  Keeping the table because tables are kept. A team that cannot say what it chose to trace,
           what it chose not to trace and when it will stop has no reason to keep a matrix, and the
           file will drift into a second copy of whatever the tracker already says. -->

**Product and requirement set covered:** {{covered_set}}

**Not traced:** {{not_traced}}

**Kept by:** {{owner}}

**The record:** {{record_of_truth}}

**Why this team keeps a matrix:** {{reason_for_matrix}}

**When it will stop:** {{stop_condition}}

## Trace Conventions

<!-- WHAT  The identifier schemes for requirements and tests, the rule for what counts as a
           requirement, a statement of what counts as verified, how other means of verification are
           marked, how links that are not one-to-one are written, and the status vocabulary.
     WHY   A table of links is only as meaningful as the rules that decide what a link means. No
           source read gives a template for this section, so its form is this library's POSITION,
           and the companion lists the supports. NASA's verification guidance ties completion to
           "documented objective evidence of compliance with requirements or waiver", together with
           "closure of all discrepancy and nonconformance reports". In this library's reading, a
           linked test case is therefore a claim that a test exists, and not a claim that the
           requirement was verified. The jamb documentation, a practitioner's tool guide, flags
           requirements "indicating they are verified by other means (inspection, analysis,
           demonstration)". Without such a status, in this library's reading, a requirement
           verified by inspection reads as a gap. NASA also says "the relationships identified in
           the matrix are not required to be one-to-one". Who may mark a row verified is not
           established by any source read, so a team that wants a rule states it as its own. Deep
           dive: requirements-traceability-matrix_companion.md section 3 (Trace Conventions).
     ASK   How are requirements and tests numbered, and which statements count as requirements? In
           one sentence, what must be true before a row is marked verified: a test exists, a test
           passed, or evidence is attached and no defect against the requirement is open? How does
           the matrix mark a requirement checked by inspection, analysis or demonstration, and how
           are many-to-many links written? What does each status word mean, in one sentence each?
     PRIORITY  The definition of verified is written before any status word is used, and it says
           what evidence a verified row rests on, not only that a test is linked. If the team says covered, define that word here: it can mean a linked test or a verified requirement.
     ROW HINT  A good status row names the status and the condition that earns it, so two people
           reading the same row would mark it the same way. A weak row names a status with no
           condition, or defines it as the existence of a test.
     GOOD  Requirement IDs: "REQ-n, assigned in the sync spec and not reused." Test IDs: "T-n, from
           the test management tool." Scope: "Every numbered sentence in sections 4 and 5 of the sync
           spec; the introduction and the glossary are not requirements." Verified: "A named test
           passed on a named build, the evidence is attached to the test record and no defect against
           the requirement is open." Other means: "A requirement checked by inspection carries the
           status Other means and names the review record." Links: "One requirement may list several
           tests and one test may list several requirements; both directions are written out."
           Status table rows:
           | No verification | Nothing is linked: no test and no other-means record |
           | Test linked | A test exists but has not yet run or has not passed |
           | Verified | The verified condition above is met |
           | Other means | Checked by inspection, analysis or demonstration, with the record named |
     WEAK  Status table row: | Covered | Done | (does not say what evidence earns it, so a linked test
           and a verified requirement read the same)
     TRAP  Letting covered mean that a test case ID sits in the Verified by cell. A table full of
           green rows can then hide requirements that were never verified, and nothing in the file
           shows it. -->

**Requirement identifiers:** {{requirement_id_scheme}}

**Test identifiers:** {{test_id_scheme}}

**What counts as a requirement:** {{scope_rule}}

**What counts as verified:** {{verified_definition}}

**Verified by other means:** {{other_means_rule}}

**Links that are not one-to-one:** {{cardinality_rule}}

| Status | What it means in this matrix |
|---|---|
| {{status_name}} | {{status_meaning}} |

## The Matrix

<!-- WHAT  One row per requirement, with its identifier, a short label, its source, what verifies it,
           its status and any notes.
     WHY   This table is the artifact. The other sections explain it, bound it or extend it. The
           columns draw on Visure's component list, "Requirements ID and Description", "Source of
           Requirements" and "Associated Test Cases", and on TestDevLab's requirement-to-test pair.
           Neither the Visure page nor the TestDevLab page shows a full table, so the column set is this library's assembly from
           partial lists and not any one source's shipped layout. The row holds a short label and not
           the requirement's full text, because NASA's handbook says "do not duplicate requirements
           in the traceability matrix". In this library's reasoning, a copy of the text drifts from the original. The source
           document owns the text, and the matrix owns the links. One matrix or several is a stated
           choice: NASA says "Traceability matrices can be included in the documents to which they
           apply", or "they can be combined into a single matrix covering higher level requirements,
           software requirements, design, code, and verification", and its systems handbook adds
           "This matrix could be divided into multiple matrices (e.g., one for each requirements
           document)". This template ships one table for the covered set. The table is read in both
           directions and is not kept as two: TestDevLab describes both checks on the same table,
           that "every requirement is covered by at least one test case, and conversely, that every
           test case is linked to a valid requirement". A table with one row per requirement cannot
           show a test that has no requirement, because that test has no row, so Coverage Gaps is
           where that half of the check lives; that reading is this library's inference. Deep
           dive: requirements-traceability-matrix_companion.md section 3 (The Matrix).
     ASK   Which requirements are in scope, and does every one of them have a row, including those
           with nothing yet in the Verified by cell? Where does each requirement's source document
           say it, and does the row link there rather than copy it? Is this one table, or does the
           team split it by requirements document, and where are the other tables?
     PRIORITY  Every requirement in scope has a row, including the ones with no verification. An
           empty Verified by cell is the reason the table exists, and a row for a requirement with no
           verification is a finding and not an error.
     ROW HINT  A good row has a stable identifier, a label short enough to scan, a source a reader can
           open, every test or other means that verifies it, and a status that follows the
           definitions in Trace Conventions. A weak row copies the requirement's full text, leaves the
           source blank, or marks a status the Verified by cell does not support.
     GOOD  | REQ-22 | Edits made offline are synced on reconnect | Sync spec 4.2 | T-31, T-32 |
           Verified | T-32 passed on build 118 with the log attached; no defect open |
     WEAK  | 22 | sync | | T-31 | Covered | |
     TRAP  Filling in rows only for the requirements that already have a test. The table then shows
           the team's tests, not its requirements, and the requirement nobody verified is the one that
           is missing from it. -->

| Requirement ID | Requirement (short label) | Source | Verified by | Status | Notes |
|---|---|---|---|---|---|
| {{requirement_id}} | {{requirement_label}} | {{requirement_source}} | {{verified_by}} | {{requirement_status}} | {{requirement_notes}} |

## Coverage Gaps

<!-- WHAT  The requirements with no verification, the tests with no requirement, and what each gap's
           owner decided.
     WHY   Both vendor sources name finding gaps as a purpose. TestDevLab lists "Identify Gaps:
           Highlight any requirements that do not have a corresponding test case." Visure's product
           description includes the ability to "detect missing links". The backward half matters too:
           Orcanos, a vendor selling a medical-device quality platform, says "An RTM that only maps
           forward is incomplete." Its frame is an audit of a medical device, and the claim is one
           vendor's. A gap that is only flagged has not been dealt with. NASA says orphans "need to
           be discussed by the project team and assurance personnel", and that "If they are
           determined to be necessary, any missing source requirements are added to the project." So
           the section asks what each gap's owner decided: add a test, add a requirement, mark the
           requirement as verified by other means, or remove the orphan. How a gap is displayed is
           not shown by any source read, so this section's layout is this library's POSITION. Do not
           read an empty list as a clean bill of health: it is only as good as the rows and the
           definition of verified behind it. That caution is this library's inference. Deep dive:
           requirements-traceability-matrix_companion.md section 3 (Coverage Gaps).
     ASK   Which requirements have no test or other means of verification? Which tests point to no
           requirement? Who owns each gap, and what did they decide to do about it?
     PRIORITY  Every gap has an owner and a decision. A gap with no owner and no decision is a list of
           worries. If the list is empty, say so in one line and say when the rows were last checked.
     ROW HINT  A good row names the kind of gap, the identifier, an owner, and a decision that is one
           of the four above or a reasoned alternative. A weak row says that something is missing
           and names neither the identifier nor the owner.
     GOOD  | Requirement with no verification | REQ-25 | Sync lead | Add a test: T-40 to be written
           before the beta | Beta is the next review point |
     WEAK  | gap | sync stuff | team | look into it | |
     TRAP  Flagging a gap and leaving it. A gap list that grows without decisions teaches readers to
           ignore it, and it makes the matrix look more complete than the verification behind it. -->

| Gap | ID | Owner | Decision | Notes |
|---|---|---|---|---|
| {{gap_kind}} | {{gap_id}} | {{gap_owner}} | {{gap_decision}} | {{gap_notes}} |

## Upkeep and Review Trigger

<!-- WHAT  The events that require an update, the owner who makes it, the points at which the matrix
           is reviewed, and the date it was last reconciled.
     WHY   A matrix that nobody maintains turns from a record into false assurance. NASA's guidance
           is "Assign responsibility for creating and maintaining the matrix to a project team
           member" and "Ensure a review of the matrix at major phases/key reviews of the project.",
           and it warns that manual methods "do not include automatic updates". The update rule
           comes from Jama, a vendor: a matrix "should be updated whenever requirements, test
           cases, or linked lifecycle artifacts change, not just on a calendar schedule." No source
           read gives a calendar interval, and this template does not invent one. Tools handle
           staleness with a mechanism, such as the content hash the jamb documentation describes. A
           hand-kept table has none, so this template's stand-in is an owner, a list of trigger
           events and a date last reconciled. No source read puts a last-confirmed field on a
           hand-kept row, so that form is this library's POSITION. Deep dive:
           requirements-traceability-matrix_companion.md section 3 (Upkeep and Review Trigger).
     ASK   Who owns the upkeep? Which events force an update: a changed requirement, a
           new or retired test, a change to a linked ticket? At which reviews or releases is the
           whole table checked? When was it last checked against its sources?
     GOOD  "Owner: the sync team's QA lead. Triggers: a requirement is added, changed or deferred; a
           test is added, retired or fails after passing; a change request touching sync is approved.
           Review points: before each beta and release review. Last reconciled: 2026-09-10, against
           sync spec v6 and the test management tool."
     WEAK  "Updated as needed." (no owner, no trigger and no date, so a reader cannot tell whether the
           table is current or was current once)
     TRAP  Setting a calendar interval and calling it a rule. Jama ties updates to change and NASA ties
           reviews to major phases and key reviews, and no source read gives an interval. A date older
           than the last trigger event is a warning that the table may be stale, however recently the
           calendar says it was reviewed. -->

**Owner:** {{owner}}

**Events that require an update:** {{update_triggers}}

**Review points:** {{review_points}}

**Date last reconciled:** {{last_reconciled}}
