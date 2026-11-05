---
status: accepted
date: 2026-11-05
decision-makers: [jprisant]
consulted: [claude]
---

# `manager-user-guide` clears the admission test and does not ship: the maintainer chose not to open a family for it

## TL;DR

- **Decision.** `manager-user-guide` (issue #329, no catalog row) **does not ship**. No family holds it without
  either opening a new one or redefining an existing one, and the maintainer chose neither.
- **This is not a zero-source refusal.** The type clears admission on one readable source, and no shipped bundle does
  its job. Build order and selection are the maintainer's
  ([ADR 0041](0041-maintainer-preference-sets-the-build-order.md)).
- **This is not a general scope ruling.** It does not say the library can never hold a document about one person.
- **Who loses.** A manager who wants a template for a "working with me" page.
- **Status:** accepted 2026-11-05. An earlier draft of this record proposed a new `personal-docs` family and never
  landed. Given the plain-English choice, the maintainer answered "Build matrix, skip guide".

## Context and Problem Statement

The maintainer queued the type for an admission sweep on 2026-10-25. Admission sweep 7 recommended admitting it on
2026-10-29, and it found that no family fits without a contract change. A read on 2026-11-05 tested the placement options
and recommended a new one-member family at medium-low confidence, with declining as the realistic alternative.

## Decision Drivers

- **Admission and the build decision are separate questions**
  ([ADR 0064 (deployment plan declined)](0064-deployment-plan-is-declined.md)).
- **A new family has a standing cost:** a contract, a check K entry and a test fixture, for a family with no forecast of
  further members.
- **The evidence thinned on inspection**, as the next section records.

## Considered Options

1. **Decline.** Chosen.
2. **A new one-member family, `personal-docs`, at `classification: utility`.** The candidate's own draft recommendation. It
   would have widened the library past products and their delivery, for one bundle.
3. **Amend `standing-standards`, at `foundation`.** It fits on cadence. Its adopting record,
   [ADR 0032](0032-adopt-standing-standards-family-contract.md), says "The axis question is the substance", and filing the
   guide as `foundation` would call one person's preferences a standard that reports are judged against.
4. **Amend `communication-docs`.** Its audience is outside the team, and its members own none of their facts. The guide
   fails both.

## Decision Outcome

**Chosen: option 1.**

### Admission clears, on one readable source

[Amy Shiel's README](https://handbook.gitlab.com/handbook/engineering/readmes/amy-shiel) in the GitLab handbook is a sectioned
page by an engineering manager at a software company: "This page is intended to help others understand what it might be like to
work with me, especially people who haven't worked with me before." That clears checks 1 and 5 under
[ADR 0048 (one named source clears admission)](0048-one-named-source-clears-the-admission-test.md). No shipped bundle is written
by one person about themselves, so check 4 passes.

**First Round Review no longer carries admission.** The issue named its reproduction of Jay Desai's guide. firstround.com's terms
say: "You may not “crawl,” “scrape,” or “spider” any portion of the Site (through use of manual or automated means)." This
library reads that as covering The Review. Agents read the page in earlier runs and on 2026-11-05 before anyone checked the terms,
and this record takes no evidence from it.

### What weighed against building

- **All three named critics question the genre.** Camille Fournier: "there is no way to write these and not be self-serving", and
  "your documentation is out of date the minute you write it down". Ed Batista: "A Manager README is no substitute for a
  feedback-rich culture". Diwaker Gupta disputes the name: "There's nothing "manager"-specific about them."
- **A new family would have one member and no forecast.** On the catalog's descriptions, a team charter (entry 80) and a working
  agreement (entry 100) are agreed by a team, so they would fit `standing-standards` as written.
- **The subject is new.** Every shipped bundle concerns a product or its delivery.

### Consequences

- **The issue closes** as not planned, relabelled `status:declined`, and no catalog row is added.
- **The boundary work is lost for now.** Whether a team charter or a working agreement differs from this guide stays unargued
  until one of them is swept.
- **`firstround.com` stays on the excluded-sites list**, on this library's reading of its terms. The maintainer may reverse that.

### What would reopen this, stated so it is falsifiable

1. **The maintainer chooses to build it**, as ADR 0041 allows. The placement analysis above and the local read are ready to use.
2. **Another candidate written by one person about themselves is admitted**, which would give a family more than one member.
3. **A real reader asks for the template.**

## More Information

- The read and the sweep are held locally, at `_local/research/2026-11-05_manager-guide-read/read.md` and
  `_local/research/2026-10-29_admission-sweep-7/digest.md`.
