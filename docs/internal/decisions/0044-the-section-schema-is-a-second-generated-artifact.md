---
status: accepted
date: 2026-09-05
decision-makers: [jprisant]
consulted: [claude]
---

# The section schema is a second generated artifact beside the manifest, and its parser is the guidance grammar's first mechanical reader

## TL;DR

- **Decision:** Generate [`sections.json`](../../../sections.json) at the repository root from the template
  variant files themselves via [`tools/gen-sections.py`](../../../tools/gen-sections.py), commit it, and
  fail CI (`--check`) on drift, exactly as [ADR 0018](0018-machine-catalog-generated-manifest.md) does for
  `manifest.json`. It ships **beside** the manifest rather than inside it, and it groups sections **per
  format** carrying `in_sizes` rather than the `in_lean`/`in_full` booleans the AG-1 sketch proposed.
- **Why:** the manifest answers *which bundle*; nothing answered *what is inside it*. Embedding the answer
  measured **4.6x** on the artifact agents read to select, and the AG-2 spec beside AG-1 caps default
  responses at 1,200 tokens. Two booleans cannot address four bundles shipping three or four variants
  under [ADR 0028](0028-adopt-a-format-axis.md), nor the one shipping a single variant.
- **Also decided, and the part with teeth:** the generator **fails on a guidance comment it cannot parse**.
  Nothing else in this repository reads the Approach A comments mechanically, so this is the grammar's
  first enforcement. A malformed comment now fails a build that would previously have passed.
- **Status:** accepted 2026-09-05. Completes roadmap WP-53 (AG-1). Satisfies the LP-1 spec's own acceptance
  criterion that "the comment-grammar gate check passes on all bundles before LP-1 ships (grammar is
  enforced, not assumed)", and corrects the extraction rule that spec proposed.

## Context and Problem Statement

[ADR 0016](0016-adopt-machine-checkable-metadata-schema.md) made each bundle's meta trustworthy and
[ADR 0018](0018-machine-catalog-generated-manifest.md) made selection deterministic. Both operate on
`meta.yaml`. Neither says anything about what is *inside* a template: its sections, their order, which
sizes carry them, which take a table, where the fill sites are.

That gap has three named consumers. LP-1's use-template flow needs a completeness check; LP-2's grader
needs a structure layer; an AG-2 `validate_fill` needs both. Each would otherwise re-derive the same facts
by parsing HTML comments, and each would get the parsing subtly wrong in its own way.

**The gap was worse than missing.** The LP-1 spec anticipated it and shipped what it called a "normative
contract" for the comment grammar, including an extraction regex. Run against the tree, that regex
extracts **zero of 353 `WHAT` fields** and **357 `WEAK` where there are 353**. Its `^\s*` anchor cannot
reach `WHAT`, which sits on the `<!-- ` opener line; its `\s+` accepts a single space, so `WEAK row:` in
`product-roadmap` and three `WEAK  |` table rows in `okrs` parse as fields. LP-1's flow is "show WHAT plus
the ASK questions verbatim", so the contract as written yields an interview with no questions, while six
of eight field types extract correctly and hide the defect from any spot check.

## Decision Drivers

- **A generated fact stays fresh; a retyped one goes stale.** The standing rationale across this tooling,
  and the reason `--check` exists at all.
- **The selection surface must stay cheap to read.** An agent picking a bundle should not pay for
  fill-time detail it will not use.
- **The tree, not the sketch, is the authority.** The AG-1 sketch is 22 lines written 2026-07-12; it
  predates 20 of the 27 bundles.
- **An unenforced convention drifts.** Procedure 9: a convention tested and failed becomes a check.

## Considered Options

1. **Embed the section schema in `manifest.json`**, as the AG-1 sketch proposed.
2. **Ship a ninth file inside each bundle**, beside the eight the contract names.
3. **A separate generated root-level artifact**, `sections.json`, with a `--check` mode. *(chosen)*
4. **Do not generate it**; let each consumer parse comments itself.

## Decision Outcome

**Option 3.** Option 1 was measured rather than argued: embedding takes the manifest from about 10,850 to
about 49,750 approx-tokens, a **4.6x** increase on the artifact read for selection, while the AG-2 spec
sitting beside AG-1 in the same document requires default responses under 1,200 tokens. The sketch
contradicted its own sibling section. Option 2 breaks the eight-file bundle contract that
[ADR 0010](0010-meta-declares-size-contract.md) and gate check A both depend on, for data that is derived
rather than authored. Option 4 is what the LP-1 regex already demonstrates: three consumers parsing the
same grammar three times, getting it wrong three ways, with nothing to catch any of them.

**Three departures from the AG-1 sketch, each forced by the tree and each measured:**

| Sketch | Shipped | Why |
|---|---|---|
| `in_lean` / `in_full` booleans | per-format grouping with `in_sizes` | Four bundles ship three or four variants under [ADR 0028](0028-adopt-a-format-axis.md); one ships a single variant. Worse, two section titles appear in more than one **format** with genuinely different guidance text (`product-roadmap`'s "What Is Not On Here" across go / now-next-later / themes, `product-strategy`'s "What We Are Not Doing" across kernel / one-pager), so keying by title alone merges documents that share only a heading |
| one `has_table` | `has_table` **and** `has_row_hint` | The two signals **disagree on 10 of 353 sections**. `kpi-dashboard` carries ROW HINT over a bare `{{metric_definitions}}` placeholder the author fills; `prd` ships a real table with its row guidance in WHAT. Both documents are correct; one boolean makes ten sections wrong |
| embedded in `manifest.json` | beside it | the 4.6x measurement above |

**The grammar was measured, not adopted from [methodology B1](../../../templates/methodology.md).** All 58
variant files carry exactly **353** guidance comments and the schema accounts for every one: 4 at H1, 342
at H2, 7 at H3. The load-bearing rule is that **a field label sits at indent exactly 5**, aligning under
the five characters of `<!-- `. "A label followed by two spaces" is not enough and produces 356 WEAK.
Sections are **not only H2**: `release-notes` and `adr` attach guidance to the H1, `adr` and `sdd` to H3s.
The 58 preambles are excluded structurally, since guidance opens `<!-- LABEL` and a preamble opens with a
newline.

### Consequences

- **Good:** the three named consumers read one gate-checked artifact instead of each writing a parser. The
  LP-1 completeness check becomes possible for the first time, and its own acceptance criterion is met.
- **Good:** the Approach A grammar is enforced rather than conventional. It has been a prose convention
  since the first bundle and nothing has ever checked it.
- **Cost, and it is a real one:** landing a malformed guidance comment now fails CI where it previously
  passed silently. That is the point, and it will surprise the next bundle build. Recorded as gotcha 1a in
  [`bundle-pipeline.md`](../bundle-pipeline.md).
- **Cost:** a fourth generated artifact to keep fresh, and a fourth `--check` step. The alternative is
  drift, which this repository has measured six times (finding DF-5).
- **Deliberately not solved:** placeholder **occurrences**. Each section lists a name once, which suits a
  completeness check and not a substituting fill tool: 94 names recur within a single file body, and `prd`
  reuses `{{owner}}` and `{{date}}` at unrelated sites. Keying by occurrence belongs to LP-1, reading the
  file. Stated in the generator's docstring so the next reader does not have to find it.

### Confirmation

- `python tools/gen-sections.py --check` runs in CI and fails on drift or on any comment that will not
  parse.
- [`tools/test-gen-sections.py`](../../../tools/test-gen-sections.py), 40 assertions, runs in CI. Its
  load-bearing cases are **adversarial and drawn from measured shapes**: the `okrs` `WEAK  |` table row,
  the `product-roadmap` `GOOD row:` / `WEAK row:` continuations, guidance on H1 and H3, and every
  malformed shape that must raise. It caught two real defects while being written.
- The reconciliation is the standing check: section instances in the schema must equal the guidance
  comments on disk. It is asserted in the self-test against a fresh scan rather than against a constant.

## More Information

- Roadmap WP-53 (AG-1 section schema); the AG-1 sketch is section 6 of the gitignored
  `spec_machine-metadata.md`, 22 lines.
- [ADR 0018](0018-machine-catalog-generated-manifest.md) is the pattern this follows;
  [ADR 0028](0028-adopt-a-format-axis.md) is what the sketch's booleans could not express.
- [Decision procedure 9](../decision-procedures.md) is the authority for turning the grammar convention
  into a check.
