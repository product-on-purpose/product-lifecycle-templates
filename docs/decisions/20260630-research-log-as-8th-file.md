# The research log is a committed bundle artifact (the 8th file)

Status: accepted (practice settled 2026-06-30; transcribed 2026-07-11; ratified 2026-07-12)
Date: 2026-06-30
Deciders: jprisant

## Context and problem statement

The design spec and implementation plan defined a six-file bundle; the methodology's research protocol produces a source log as working material. The open call was whether that log is disposable scaffolding, folded into the companion, or a committed artifact. Practice settled it: every shipped bundle carries `<type>_research-log.md`, the gate requires it (ROLES, check A), and the DoD's research clause depends on it, but the methodology's own anatomy table still said "seven files" at audit time.

## Considered options

* Option A: commit the research log as the 8th canonical bundle file.
* Option B: fold sources into the companion's reference list and discard the log.
* Option C: keep logs out of the repo (working-tree only).

## Decision outcome

Chosen option: A. The log is the evidence trail the freshness gate (FR-1, staleness automation) and the audit-grade citation pass (EV-4) both need: it records per-source retrieval state (fetched, 403-blocked, paywalled, search-corroborated) that the reader-facing reference list should summarize but not carry in full. It also keeps the companion readable. The 2026-07-10 audit validated the choice concretely: the research logs' honesty about blocked fetches is what made the citation-integrity findings diagnosable at all.

### Consequences

* Good: claim-to-source tracing is auditable; retrieval honesty has a durable home; freshness automation has structured input.
* Accepted risk: one more file per bundle to maintain; mitigated by the log being append-mostly after authoring.
* Housekeeping this record unblocks: fix methodology section 2 ("seven files" to eight, add the table row and a drafting step); that is audit finding B-04 and roadmap work package WP-06.
