---
title: "pi-release-retrospective: the admission-test evidence"
description: "Why the PI/release retrospective fails ADR 0030's admission test while the project/milestone retrospective passes it twice over, from one shared research pass"
audience: "both"
level: "intermediate"
tags:
  - admission-evidence
  - process-docs
  - governance
---

# `pi-release-retrospective`: the admission-test evidence

**Supporting evidence for [ADR 0049](decisions/0049-pi-release-retrospective-fails-the-admission-test.md),
which found that `pi-release-retrospective` fails
[ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s admission test and does not ship.**

Following [`prototype-brief-admission-evidence.md`](prototype-brief-admission-evidence.md), this file exists
so the question can be reopened without re-fetching. The bundle was never built, so there is no
`templates/pi-release-retrospective/`.

**The full source record is not duplicated here.** This type was researched in the **same six-dimension pass**
as `project-milestone-retrospective`, because the two share almost their whole source base, and all 80 unique
sources are recorded in
[`project-milestone-retrospective_research-log.md`](../../templates/project-milestone-retrospective/project-milestone-retrospective_research-log.md).
That log carries the retrieval status and quotables for every source cited below.

---

## The decisive finding

**Scaled Agile's own official Inspect & Adapt Facilitator's Guide names the event's outputs, and none of
them is a document.** The guide is freely downloadable, requires no login, and was **read in full**. It
gives three outputs:

1. a predictability/accountability-loop assessment score,
2. tacit understanding of where the ART needs to improve, and
3. *"a set of improvement backlog items (Enablers, Features, or Stories) that go into the ART Backlog for
   consideration in the next PI Planning event."*

**No written retrospective report, record, minutes, or narrative document appears anywhere** in that guide's
purpose, intent, agenda, attendees, or post-event-actions sections. SAFe's main Inspect and Adapt article
page corroborates this in its freely visible summary.

**One limit, stated rather than glossed.** That article page's own embedded schema.org metadata marks the
deeper how-to body `"isAccessibleForFree": false`, behind a SAFe Studio login. So some SAFe content on this
topic could not be read. **Nothing in what is readable - including the vendor's own primary facilitator
material - mentions a document**, and a claim resting on unread gated content would fail this library's
retrieval rules anyway.

---

## The two vendor candidates, checked because a vendor source can suffice here

This library has already admitted a type on **vendor-tier** sources: `sprint-retrospective-notes` was
admitted on Documentero, Smartsheet and Atlassian's Confluence Retrospective Blueprint, and its own research
log says plainly that these are *"template vendors rather than authorities"* and that *"this is a thinner
base than `prd` or `test-plan` rest on"*. So the bar a vendor template must clear is real but low, and both
Type-B candidates were checked against it.

**Neither holds.**

| Candidate | What it actually is | Why it does not admit |
|---|---|---|
| **Aha! - "Create a SAFe PI retrospective"** | A **4-column board**: What went well / What could have been better / What you will do differently / Action items, plus a shoutouts section | **A board is not a document.** ADR 0030 already refused `wireframe` on exactly this ground: the artifact's primary form is a working surface annotated inside a tool, not a written document |
| **EasyRetro - "Release Retrospective Template"** | A **single-team, project-scoped, one-time** retrospective | **Scoped to a different artifact.** This type is defined by ART-scale breadth across multiple teams; a single-team release retro is a neighbouring artifact wearing a similar name |

**That is the `prototype-brief` shape precisely.** ADR 0035 refused that type because *"every candidate
examined turned out to be a neighbouring document type presented under another name"* - a code-based
prototyping kit, a sprint-wide brief, a hypothesis card, vendor blog content. Here it is a board and a
differently-scoped template.

---

## The structural finding underneath it, which is the useful part

**Cadence retrospectives feed a backlog. Terminal retrospectives produce a document.** This is not a quirk
of SAFe.

The **Scrum Guide** (Schwaber and Sutherland, November 2020, read in full) describes the Sprint
Retrospective's output in the identical pattern: the team identifies the most helpful changes, and *"They
may even be added to the Sprint Backlog for the next Sprint."* So "feeds a backlog, produces no document" is
the shape of the **whole cadence line**, team sprint through ART-scale PI, and SAFe did not invent it.

The **after-action review and lessons-learned lineage is different in kind**: it attaches to a **bounded
piece of work that has ended**, where the team may disperse and part of the audience was not present, and
**there a named source does prescribe a written document** - CALL's written after-action report, and PMBOK's
lessons learned register.

**So one research pass produced opposite verdicts for two types, and the difference is principled rather
than accidental.** `project-milestone-retrospective` ships. `pi-release-retrospective` does not.

---

## What this does NOT disturb

**`sprint-retrospective-notes`, which is built and shipped, is not reopened by this.** It sits on the cadence
line and would face the same structural finding - but it was admitted on its own vendor-tier evidence, and
its research log already confronts this directly, stating that *"The Scrum Guide does not ask you to write
this down"* and calling that *"the honest starting point for a bundle whose entire subject is a document."*

**That bundle's admission does not transfer here**, and the reason is specific: three named vendors publish
a fill-in **sprint retrospective document** with fixed headings. No equivalent was found for a PI/release
retrospective. The only Type-B vendor artifact is a board.

A reader who thinks the sprint bundle's base is too thin should argue that against ADR 0030 directly. This
record does not reopen it and does not lean on it.

---

## What would reopen this

1. **A named source publishing a PI or release retrospective as a written document** with fixed headings -
   a vendor template would suffice, on the `sprint-retrospective-notes` precedent, provided it is a document
   and not a board.
2. **Readable SAFe content** using the words document, report or record for an Inspect and Adapt output. The
   relevant material is behind a SAFe Studio login; a maintainer with access could settle this either way in
   minutes, and that is the cheapest available route.
3. **A real pull from a team that writes one**, which would also supply the artifact to examine.
