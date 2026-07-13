# Bundle IDs are bare document-type handles; phase lives in metadata, never in path or ID

Status: accepted (practice settled 2026-06-30 in methodology v0.2.0; transcribed 2026-07-11; ratify on adoption)
Date: 2026-06-30
Deciders: jprisant (via methodology.md section 2)

## Context and problem statement

The implementation plan's P1 intended bundle IDs of the form `<phase>-<doctype>` (for example `deliver-prd`, matching pm-skills skill IDs). The library as actually built uses bare doc-type handles: the folder is `prd/`, the meta `id` is `prd`, and `phase: deliver` is a metadata field. This divergence was real, deliberate, and reasoned in the methodology ("Phase is recorded in metadata, never in the path, so the eventual directory scaffold stays a deferred, derivable choice"), but it was never recorded as a decision against the plan's stated intent. This record closes that gap.

## Considered options

* Option A: bare doc-type IDs (`prd`); phase as a metadata axis only.
* Option B: phase-prefixed IDs (`deliver-prd`) mirroring pm-skills skill IDs.

## Decision outcome

Chosen option: A. Document type is the directory spine (the taxonomy decision); encoding phase into the ID would materialize a second lens into the identity, the very move the lens framework forbids, and would force renames if a type's phase assignment is ever refined. The skill-ID mapping that Option B tried to carry in the name is carried explicitly and more flexibly by the `pairs_with` field (`prd` pairs with `deliver-prd`), which also allows a template to serve multiple skills.

### Consequences

* Good: stable IDs independent of phase taxonomy evolution; one spine, lenses as metadata, exactly per the design principles; `pairs_with` does the seam work by data rather than by naming convention.
* Accepted risk: template IDs and skill IDs no longer match visually, so the seam is only discoverable through metadata; mitigated by `pairs_with` being schema-required and (per the audit roadmap) gate-validated.
* Housekeeping: the plan's P1 step 4 text and any doc still teaching `deliver-prd`-style template IDs should gain a superseded note pointing here.
