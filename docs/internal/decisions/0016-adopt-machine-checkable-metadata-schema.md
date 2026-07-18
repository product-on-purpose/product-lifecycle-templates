---
status: accepted
date: 2026-07-17
decision-makers: [jprisant]
consulted: [claude]
---

# A machine-checkable metadata schema is the meta contract, validated in CI

## Context and Problem Statement

Every bundle ships a `<type>_meta.yaml`, but nothing defines what a valid one is. No field is required
by anything, no value is constrained, and the only field the gate understands is `sizes_available`, which
it reads with a regular expression. The library's front door calls itself "agent-native," and that claim
is on credit: an agent that wants the right template for "document an architecture decision" has no
structured way to learn the answer is `adr`. It reads prose, or guesses.

The cost grows with every bundle. Six bundles are hand-tractable; the catalog's 27 Tier-1 types are not.
Without a contract, each new meta drifts a little from the last, and the day an agent (or an installer, or
a marketplace) wants to consume the library, we retrofit a schema onto 27 inconsistent files instead of
validating one.

This was proposed as [RFC-0001](../../../templates/rfc/rfc_example.md) (the library's worked RFC example,
which is a genuine in-flight proposal, not a toy), circulated for comment, and is now accepted. Its one
hard blocker, whether `phase` can be a required enum, was settled first by
[ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md): a meta declares `phase` XOR
`classification`. With that resolved, this ADR records the decision the accepted RFC produces: adopt the
schema as the meta contract.

## Decision Drivers

- **Drift is cheap to prevent now and expensive to fix later.** Building the contract at six bundles is
  the whole point; retrofitting it at twenty-seven is the failure mode.
- **"Agent-native" needs a mechanism, not a slogan.** A structured, validated meta is the smallest thing
  that makes the claim true rather than aspirational.
- **The taxonomy blocker is gone.** ADR 0015 turned "is `phase` required?" into "`phase` unless
  `classification`," which a schema can express honestly.
- **The gate already has the shape for this.** Check G validates YAML validity in CI; a schema check is
  the same move one level up, from "is it YAML" to "is it a valid meta."

## Considered Options

* **Option A: a per-meta JSON Schema (draft 2020-12), validated by the gate in CI.** Every
  `<type>_meta.yaml` must validate against one published schema. Chosen.
* **Option B: a generated `index.json` only, no per-meta schema.** Emit a machine-readable catalog from
  the metas and stop there.
* **Option C: adopt an existing standard** (Backstage `catalog-info`, a plugin manifest, JSON-Resume
  style).
* **Option D: do nothing; keep meta as convention.**
* **Option E: a richer schema language than JSON Schema** (e.g. CUE).

## Decision Outcome

Chosen option: **A. One JSON Schema, validated in CI.**

`tools/meta.schema.json` (draft 2020-12) is the contract. Every `<type>_meta.yaml` must validate against
it, enforced by the gate's new check J and by branch protection. The schema codifies the eighteen fields
the six current metas actually carry (read from disk, not guessed): the seventeen always-required fields
plus the `phase`/`classification` axis, with enums where values are closed (`phase`, `classification`,
`status`, the two size vocabularies), patterns where they are shaped (`id`, `template_version`,
`last_reviewed`, `related_templates`), and `additionalProperties: false` so a typo'd field name is a
failure rather than silent drift. The XOR from ADR 0015 is encoded as `oneOf`: a meta validates iff
exactly one of `phase` / `classification` is present, each against its enum. The `status` vocabulary is
`draft` / `beta` / `stable` / `deprecated` (RFC-0001's three, plus `draft` for a bundle under authoring
that is not yet offered for use).

The schema and its check were adversarially hardened before landing. An independent red-team, run after a
first authoring pass, drove value-level tightening the first pass had missed: canonical kebab-case ids,
real SemVer versions, calendar-valid dates (via `format: date`, which rejects an impossible `2026-02-30`),
non-whitespace free-text, a `catalog_ref` whole-integer guard, and duplicate-key rejection at parse time.
The full battery and the dependency decision behind the check are recorded in
[ADR 0017](0017-gate-may-use-jsonschema-for-meta-validation.md).

Three refinements were decided during implementation, where the accepted RFC left latitude:

- **Location: `tools/`, not a new `schema/` directory.** The RFC floated either. The schema is a gate
  artifact and lives beside the gate that reads it, next to `known-skills.txt`. One fewer top-level
  directory, one convention set.
- **No per-meta `meta_schema_version` field for v1.** The RFC proposed versioned schema filenames and a
  per-meta version pointer to allow a flag-day-free v2 migration. That is machinery for a migration that
  does not exist yet. v1 is a single unversioned `meta.schema.json`; changing it is a deliberate,
  reviewed edit to one file. If a v2 ever needs staged migration, the version field is added then, when
  its shape is known, rather than guessed now.
- **`index.json` is out of scope, deferred to WP-22.** The RFC bundled a generated catalog index with the
  schema. The schema is the half that keeps the inputs honest; the index is a consumer of it. WP-21 lands
  the schema; WP-22 (machine catalog) builds the index against it.

Option B was rejected because an index generated from unconstrained metas faithfully reports inconsistent
data: it makes drift consumable without stopping it. Option C was rejected because none of the surveyed
standards fits a document-template library without importing a vocabulary that fights the catalog's own;
worth revisiting only if a distribution target demands a specific format. Option D was rejected because
the retrofit cost is the whole argument for acting now. Option E was rejected because JSON Schema is
boring, ubiquitous, and has validators everywhere an agent might run, which matters more than expressive
power for a contract this simple.

### Consequences

* Good: meta drift is now caught in CI, the same way YAML validity is, before it can compound across
  bundles.
* Good: the "agent-native" claim gets its first real mechanism. An agent can validate and read a meta as
  structured data, and (once WP-22 lands the index) select across bundles without parsing prose.
* Good: every new bundle validates against the schema as part of its Definition of Done, so the twenty-
  seventh meta will be as consistent as the first.
* Bad, accepted: the schema constrains every future bundle. A genuinely novel type that does not fit is
  now a deliberate schema change, not just a new folder. That is the contract working as intended; a
  reviewed edit to one file is the cost, and it is small.
* Bad, accepted: requiring all seventeen universal fields is calibrated to the six current bundles, all
  of which are lifecycle artifacts. The first `classification` (standing-artifact) bundle may reveal a
  field that is nonsensical to require of it. The `classification` branch is proven to validate, but no
  bundle exercises it yet; when one does, revisit whether any required field should become optional. Empty
  arrays are already allowed for `pairs_with`, `tags`, `related_templates`, and `aliases`, which absorbs
  the most likely case.
* Neutral: codifying the current fields freezes a couple of accidents (a field or two exists because the
  first bundle happened to include it). Writing the schema forced the reckoning, which is healthy; the
  outcome was that the field set is almost entirely deliberate.

### Confirmation

Enforced by check J in `tools/check-bundles.py`, run by `.github/workflows/ci.yml` on every push and pull
request, with branch protection on `main` requiring the `gate` check to pass. Check J is the fitness
function for this decision.

Verified at authoring time (2026-07-17): the schema is a well-formed draft 2020-12 schema
(`Draft202012Validator.check_schema` passes), and all six current metas validate against it, every one on
the `phase` branch. The `classification` branch, which no bundle uses yet, was proven working by a
positive control (a `prd` meta with `phase` swapped for `classification: foundation` validates). The
dependency and enforcement decisions are recorded separately in
[ADR 0017](0017-gate-may-use-jsonschema-for-meta-validation.md), whose Confirmation records the full
adversarial test battery.

## More Information

This ADR is written from the acceptance of [RFC-0001](../../../templates/rfc/rfc_example.md), following
the rfc bundle's own teaching that an accepted RFC's decision is what an ADR is written from. RFC-0001's
Outcome is updated to accepted, pointing here.

The three decisions the RFC produced are deliberately split across records: the taxonomy content is
[ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md), this ADR is the schema-as-contract, and
the validator dependency is [ADR 0017](0017-gate-may-use-jsonschema-for-meta-validation.md). The generated
`index.json` the RFC also proposed is roadmap WP-22, built against this schema.
