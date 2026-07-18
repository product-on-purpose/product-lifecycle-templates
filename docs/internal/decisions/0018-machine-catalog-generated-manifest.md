---
status: accepted
date: 2026-07-17
decision-makers: [jprisant]
consulted: [claude]
---

# The machine catalog is a generated manifest.json, committed to VC and kept fresh by the gate

## Context and Problem Statement

[ADR 0016](0016-adopt-machine-checkable-metadata-schema.md) made every bundle's meta trustworthy: it
validates against a schema in CI. But a valid meta is still one file among six, and an agent that wants
to pick the right bundle for a task has no single place to look. It must open each `<type>_meta.yaml`, or
fall back to parsing prose, which is the exact gap that kept the README's "agent-native" claim on credit.

[RFC-0001](../../../templates/rfc/rfc_example.md), now accepted, proposed two artifacts: the schema
(landed as WP-21) and a generated catalog listing every bundle with the fields an agent selects on. This
ADR is the second half: the machine catalog, roadmap WP-22.

The human front door has a related failure mode. The README states the bundle count in prose, and it has
drifted before: the WP-13 claim reconciliation (2026-07-14) found the README advertising four bundles
when six existed, a stale list that had omitted the entire `decision-docs` family. A count that lives
only in prose will drift again.

## Decision Drivers

- **Agents need one structured surface**, not an N-file scavenger hunt, to select a bundle deterministically.
- **The selection data must not drift from the metas.** A catalog that can silently disagree with its
  sources is worse than no catalog, because it looks authoritative while lying.
- **The README count must not drift from reality** (audit finding C-03; demonstrated by WP-13).
- **The roadmap already names the artifact and its generator** (`manifest.json`, `tools/gen-manifest.py`).

## Considered Options

* **Option A: a generated `manifest.json` at the repo root, committed to version control, and a
  `--check` mode the gate runs in CI to fail on any drift.** Chosen (this is RFC-0001's proposal).
* **Option B: generate the manifest in CI and publish it elsewhere**, keeping it out of the repo.
* **Option C: no manifest; agents read the six metas directly.**
* **Option D: a hand-maintained catalog file.**

## Decision Outcome

Chosen option: **A. A generated manifest, committed, freshness-checked by the gate.**

`tools/gen-manifest.py` walks `templates/`, reads each bundle's meta, and writes `manifest.json` at the
repo root: for every bundle, the selection subset from RFC-0001's Detailed Design (`id`, `doc_type`,
`title`, `summary`, `family`, the taxonomy axis `phase` XOR `classification`, `sizes_available`,
`status`, `tags`, `aliases`). Provenance fields (`template_version`, `last_reviewed`, `catalog_ref`,
`maintainer`, `license`) are omitted; they are not selection inputs. The output is canonical (sorted keys,
stable indent), so a diff only fires on a real change. `python tools/gen-manifest.py --check` regenerates
in memory and fails if the committed `manifest.json` has drifted, and if the README's machine-readable
`<!-- bundle-count: N -->` marker disagrees with the real bundle count. CI runs `--check`, and branch
protection covers the gate job, so a stale manifest or a lying README count cannot merge.

**Naming.** RFC-0001 called the artifact `index.json`; this ADR adopts the roadmap's `manifest.json` (and
`gen-manifest.py`) so there is one name everywhere. RFC-0001's Outcome reference is reconciled to match.
The two names denoted the same artifact; the ambiguity is resolved rather than left to rot.

Option B was rejected because publishing elsewhere needs a distribution surface the repo does not have
yet; committing the generated file is the pragmatic interim RFC-0001 explicitly accepted. Option C was
rejected because "read six files" is exactly the friction the catalog removes, and it gets worse at
twenty-seven bundles. Option D was rejected because a hand-maintained catalog is the drift the `--check`
exists to prevent.

### Consequences

* Good: an agent has one structured surface to select from, and (per the gate) it cannot silently
  disagree with the metas it summarizes. The README's "agent-native" claim moves from credit to earned,
  save for installability (the missing `SKILL.md`, D2/D3).
* Good: the README bundle count is now enforced against reality, closing the drift class WP-13 found.
* Bad, accepted: `manifest.json` is a generated file under version control, which some consider an
  anti-pattern. RFC-0001 weighed this and accepted it as the interim until a distribution surface exists;
  the `--check` keeps it honest so it is a cached read model, not a second source of truth.
* Bad, accepted: the manifest duplicates data already in the metas. That is deliberate: it is a
  denormalized, selection-shaped view, and the freshness check is what makes the duplication safe.
* Neutral: `gen-manifest.py` requires PyYAML to read the metas, already a gate dependency
  ([ADR 0014](0014-gate-may-use-pyyaml-for-frontmatter-validity.md)). Unlike the gate it cannot degrade
  gracefully without a parser, so it requires the dependency rather than skipping.

### Confirmation

Enforced by CI: `.github/workflows/ci.yml` runs `python tools/gen-manifest.py --check` on every push and
pull request, and branch protection on `main` requires the `gate` job to pass. The `--check` is the
fitness function for this decision.

Adversarially tested at authoring time (2026-07-17), the discipline every gate check is held to. A battery
ran each drift class against the real `--check` logic over a temp repo: a stale manifest (a meta changed),
a new bundle absent from the committed manifest, a README marker that disagrees with the count, a missing
marker, and a missing `manifest.json` were each caught with an actionable message; a non-bundle directory
(`templates/_working/`) was correctly ignored, matching the gate's own bundle discovery; and a freshly
generated, marker-agreeing state passed clean. Eight cases, all as required.

## More Information

Builds directly on [ADR 0016](0016-adopt-machine-checkable-metadata-schema.md): the schema is what makes
the metas trustworthy inputs, and this manifest is the trustworthy output. It delivers the second of the
two artifacts [RFC-0001](../../../templates/rfc/rfc_example.md) proposed; the first was the schema.

Roadmap WP-23 (selection metadata) will extend each manifest entry with sizing guidance and an approximate
token count, regenerating through the same generator; the field set here is the v1 selection surface, not
the last word.
