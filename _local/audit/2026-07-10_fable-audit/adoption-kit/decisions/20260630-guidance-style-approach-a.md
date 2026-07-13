# Carry section guidance as enriched HTML comments (Approach A)

Status: accepted (decided 2026-06-30; transcribed 2026-07-11 from the _working comparison note and methodology B1; ratify on adoption)
Date: 2026-06-30
Deciders: jprisant

## Context and problem statement

Richer per-section author guidance had three candidate homes, prototyped side by side in `_local/templates/_working/`: hidden HTML comments (A), visible blockquote scaffolding the author deletes (B), or a hybrid with one visible prompt line (C). The choice interacts with two locked principles: guidance vanishes on render, and smallest useful default.

## Considered options

* Option A: all guidance in HTML comments (WHAT / WHY / ASK / GOOD / WEAK / TRAP, plus PRIORITY and ROW HINT for tables), invisible on render.
* Option B: visible blockquote scaffolding, clickable companion links, author must delete every block.
* Option C: hybrid; one visible italic prompt line plus a hidden comment.

## Decision outcome

Chosen option: A. It is the only option that keeps both locked principles intact; a template is filled in an editor where comments are fully visible, so help is present exactly at the moment of writing and absent from the finished artifact; and it carries the most guidance per section at zero render cost. Codified in methodology B1; applied across all eight variant files.

### Consequences

* Good: maximum guidance density; clean rendered shape; the comment fields double as a machine-parseable interview script (the LP-1 fill flow consumes ASK lines directly).
* Accepted risk 1: companion deep-links inside comments are prose pointers, not clickable anchors; the pointer names the companion section instead.
* Accepted risk 2: an author reading the file on GitHub's rendered view sees no guidance at all (comments are hidden there too); mitigated by the quickstart instructing authors to open the raw file in an editor.
* Follow-on: the comment field grammar should be gate-enforced once LP-1 depends on it (machine-metadata spec, check K).
