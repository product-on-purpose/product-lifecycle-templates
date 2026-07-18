---
status: accepted
date: 2026-07-17
decision-makers: [jprisant]
consulted: [claude]
---

# The gate may use a JSON Schema validator for one more check (meta validation); the stdlib checks stay pure

## Context and Problem Statement

[ADR 0016](0016-adopt-machine-checkable-metadata-schema.md) adopts `tools/meta.schema.json` as the meta
contract. A contract nobody enforces is a suggestion, so the gate needs to validate every meta against
it, and that needs a JSON Schema validator. The Python standard library has none.

[ADR 0008](0008-gate-python-local-interim.md) committed the gate to the **pure standard library**,
explicitly "a decided interim," so anyone could run `python tools/check-bundles.py` with nothing
installed. [ADR 0014](0014-gate-may-use-pyyaml-for-frontmatter-validity.md) already notched that for
PyYAML, confined to check G, on the reasoning that some checks genuinely cannot be done without a real
parser. This is the second notch, for the same class of reason, and like the first it has to be decided
rather than fudged.

## Decision Drivers

- **The schema is worthless unenforced.** ADR 0016's whole value is that CI rejects a bad meta before
  merge; that requires a validator running in the gate.
- **A hand-rolled JSON Schema validator is a trap**, the same trap ADR 0014 named for YAML: a partial
  implementation would pass some invalid metas and reject some valid ones, trading a known gap for
  confident wrong answers. JSON Schema draft 2020-12 has real subtleties (`oneOf` semantics, composition
  of `items` with nested `oneOf`) that an approximation would get wrong.
- **Zero-install local running is still a genuine value** from ADR 0008: the eight pure-stdlib checks must
  keep working with a bare Python.
- **Since M0, CI is the enforcement point.** Branch protection requires the `gate` check, so "enforced in
  CI" means actually enforced.

## Considered Options

* **Option A:** Grant the gate one more dependency, a JSON Schema validator (`jsonschema`), used only by
  the new check J. J SKIPs with a clear message when a dependency is absent; the eight pure-stdlib checks
  always run. CI installs it, so J is enforced there.
* **Option B:** Hand-roll a JSON Schema validator in the standard library, covering the subset the schema
  uses.
* **Option C:** Make `jsonschema` (and PyYAML) hard dependencies of the whole gate: import at the top, let
  the script refuse to run if either is missing.
* **Option D:** Adopt the schema but enforce it only by human review, with no automated check.

## Decision Outcome

Chosen option: **A. One more dependency, one more check, graceful skip.**

Check J tries to `import yaml` and `import jsonschema` (it needs both: PyYAML to parse the meta, the
validator to check it). If either import fails, J returns a distinct **SKIP** state, not a pass, printing
`SKIP  J schema  SKIPPED: <dep> not installed ...`, and the other checks proceed. With both present it
loads `tools/meta.schema.json`, confirms the schema is itself a valid draft 2020-12 schema, parses the
meta, normalizes YAML-native scalars to JSON types via a `json.dumps(..., default=str)` round-trip (so an
unquoted `last_reviewed` date is checked as the ISO string it is on disk rather than rejected as a
`datetime.date`), and validates. CI runs `pip install pyyaml jsonschema`, so J is enforced on every push
and pull request.

This mirrors ADR 0014 exactly: one dependency confined to the one check that cannot be done without it,
SKIP-honestly locally, enforce in CI. Option B was rejected because a partial JSON Schema validator is a
liability dressed as thrift, and the failure it exists to prevent (a meta drifting past the gate) is
exactly the kind of confident-wrong-answer a partial validator produces. Option C was rejected because it
sacrifices the zero-install property of eight checks to enforce one, punishing the checks that never
needed a dependency. Option D was rejected because ADR 0016's value is precisely the automated rejection;
review-only enforcement is the status quo ante the schema exists to replace.

### Consequences

* Good: the meta contract is enforced by a real, spec-conformant validator rather than a regex or a
  stdlib approximation. Reproduced: a meta declaring both `phase` and `classification`, or an illegal
  `status`, or a missing `license`, now fails check J with a located, actionable message.
* Good: ADR 0008's zero-install promise survives for the eight stdlib checks. A contributor with a bare
  Python still runs eight of ten; J announces itself as skipped rather than lying about passing.
* Good: the **SKIP** state, introduced by ADR 0014, does exactly its job again. A check that could not run
  says so instead of being counted as a pass.
* Bad, accepted: **local and CI can disagree.** A contributor without `jsonschema` sees J skip; CI enforces
  it, so a bad meta passes locally and fails in CI. This is the same footgun ADR 0014 accepted, mitigated
  the same two ways: the explicit SKIP message tells you the check did not run and how to run it, and
  branch protection catches it before merge.
* Bad, accepted: the "pure stdlib gate" is now "pure stdlib except two checks." The asterisk grew by one.
  It is documented in the script header, in the gate's own output, and here, so it stays honest, but the
  clean line ADR 0008 drew has a second notch.
* Accepted cost: one more package in the CI install line, and one more thing a thorough local contributor
  installs. `jsonschema` is ubiquitous, pure-Python, and stable, so as dependencies go it is close to the
  cheapest available, and it is the reference validator most agents already have.

### Confirmation

Enforced by CI: `.github/workflows/ci.yml` runs `pip install pyyaml jsonschema` and then
`python tools/check-bundles.py`, and branch protection on `main` requires the resulting `gate` check to
pass. Check J is the fitness function for this decision.

Adversarially tested at authoring time (2026-07-17), the discipline every gate check is held to: inject
the defect, confirm it FAILS with an actionable message, restore. An initial twenty-case battery ran each
obvious defect class against the real `check_meta_schema` end to end (temp metas, never touching a tracked
file): the XOR both/neither modes, illegal enums, malformed patterns, a missing field, an unknown field, a
typo'd field name, a string where `catalog_ref` wants an integer, and mixed or empty size vocabularies each
failed with a located message; the six real metas, a swapped-in `classification` meta (proving the unused
branch works), and empty arrays each passed.

That battery was then checked by an **independent four-lens red-team** (null/XOR encoding, YAML type
coercion, over-strictness, draft-2020-12 correctness), whose job was to find what the authoring battery
missed. It found real gaps, all since fixed and re-tested:

* **A crash, not a failure (high):** a bare invalid calendar date such as `last_reviewed: 2026-13-01` made
  PyYAML raise `ValueError` before validation, so CI would have seen a stack trace rather than a controlled
  FAIL. The parse now catches `ValueError`/`OverflowError`.
* **Silent duplicate keys (medium):** `yaml.safe_load` keeps the last of duplicate keys, so a duplicate
  `phase` could defeat the XOR invisibly. A unique-key loader now rejects it.
* **Whitespace-only strings (medium):** a blank `title` passed `minLength: 1`. Free-text fields now also
  require a non-whitespace character.
* **Permissive values (low):** an integral float (`catalog_ref: 29.0`) passed `type: integer` per the JSON
  Schema spec; an impossible calendar date (`2026-02-30`) passed the structural regex; leading-zero
  versions and trailing/double-hyphen slugs passed. A `catalog_ref` float guard, `format: date` checking,
  a canonical SemVer pattern, and canonical kebab-case patterns close these. `status` also gained `draft`
  for pre-review authoring.

The expanded battery of thirty-seven cases (every original case, every red-team gap proven fixed, and
regression positives including a plausible future Risk Register on the `classification`/`draft` path) all
behave as required. Five edge paths hold: `jsonschema` absent and PyYAML absent each SKIP (not fail, not a
false pass); a missing schema file, a schema that is not valid JSON, and valid JSON that is not a valid
schema each FAIL distinctly. The full gate run is green at 10/10 on all six bundles.

## More Information

Extends [ADR 0014](0014-gate-may-use-pyyaml-for-frontmatter-validity.md)'s precedent to a second check;
it does not supersede 0008 or 0014. The gate is still a local Python script, still runs in CI, and is
still overwhelmingly standard library. What changed is that "pure stdlib" is now the default for eight
checks rather than nine.

A separate ADR, rather than an amendment to 0014, is deliberate: ADRs here are immutable once accepted
(the whole point of a decision record), and one ADR per exceptional dependency keeps each trade-off
localized and independently reviewable, so a future contributor can see exactly why `jsonschema` was
accepted without untangling it from the PyYAML decision. RFC-0001 anticipated this dependency question and
treated 0014 as settled precedent; this ADR is that precedent, applied.
