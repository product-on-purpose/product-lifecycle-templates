# Spec: The Machine Metadata Layer (schema, manifest, section schema, gate letters)

- **Status:** proposed | **Roadmap:** WP-21, WP-22, WP-23, WP-53 (M2 core, M5 section schema) | **Effort:** M total | **Closes:** audit findings B-02 (no schema), C-03 (no catalog), C-04 (size non-determinism), C-06 (no token budgets), plus the single-variant gate gap surfaced by 12_catalog-recommendations.md
- **One line:** one schema, one generated manifest, one generated section schema, and a defined gate-check alphabet, so every machine promise the library makes is validated on every push.

Governing rule (from 13_excellence-and-innovation.md, principle 3): **no metadata field without a named first consumer.** Every field below lists its consumer; a field that loses its consumer gets deprecated, not kept.

## 1. meta.yaml: the field contract (v0.2)

Hand-authored fields (author writes these):

| Field | Type / constraint | First consumer |
|---|---|---|
| id | `^[a-z0-9-]+$`, equals folder name | gate A, manifest |
| title, summary (max 300 chars) | string | search_templates, README table |
| doc_type | string | LP-2 type detection |
| phase | enum: discover, define, develop, deliver, measure, iterate, foundation, tool | atlas, manifest |
| family | enum (from family contracts on disk) | gate family check |
| sizes_available | array of enum lean, full, s, m, l; min 1 | gate C/F, get_template |
| default_size | one of sizes_available | search_templates, LP-1 selection (closes C-04) |
| sizing_guidance | one sentence, max 200 chars | LP-1/agent size choice (closes C-04) |
| methodology | string | atlas filter |
| pairs_with | array of skill IDs or null | gate H vs pinned skill-ID list |
| related_templates | array of bundle ids, `future:` prefix allowed | gate L resolver (closes B-05 class) |
| status | enum: beta, stable, deprecated (deprecated requires superseded_by) | manifest, atlas |
| template_version | semver string | provenance chain |
| tags, aliases | string arrays | alias-index generation, search |
| catalog_ref | integer 1-205 | atlas cross-link |
| maintainer | string, must not match `\{\{` | manifest (closes the C-05 placeholder class) |
| last_reviewed | date | freshness reporting |
| license | const Apache-2.0 | manifest |

Generated fields (a tool writes these; hand-editing them is a gate failure):

| Field | Generator | First consumer |
|---|---|---|
| approx_tokens (map: role to int) | gen-manifest from byte counts / 4 | get_template budgets, agents (closes C-06) |
| scorecard (gap, agreement, scenarios, last_run) | EV-1 harness | README badges, atlas, conformance L3 |
| conformance (L1, L2, L3) | gate computes | atlas, manifest, README |

`tools/meta.schema.json` (JSON Schema draft 2020-12) encodes all of the above with `additionalProperties: false`; the AUDIT_REPORT.md B-02 stub is the seed. The schema file itself carries a `schema_version` and changes only with an ADR (it is contract, not code).

## 2. manifest.json: the machine catalog (generated, root-level)

```json
{
  "library": "product-lifecycle-templates",
  "library_version": "0.2.0",
  "generated": "2026-07-XXT00:00:00Z",
  "bundle_count": 4,
  "tier1_built": 4,
  "tier1_total": 27,
  "bundles": [
    {
      "id": "prd",
      "...": "all meta.yaml fields verbatim",
      "files": {
        "template_lean": { "path": "templates/prd/prd_template-lean.md",
                            "bytes": 7193, "approx_tokens": 1798,
                            "sha256": "..." },
        "template_full": { "...": "..." },
        "companion": { "...": "..." }, "guide": { "...": "..." },
        "example": { "...": "..." }, "history": { "...": "..." },
        "research_log": { "...": "..." }
      },
      "conformance": "L2"
    }
  ]
}
```

- Generator: `tools/gen-manifest.py`: walk `templates/*/*_meta.yaml`, validate each against the schema (fail loudly), compute bytes/tokens/hashes, emit deterministically (sorted keys, stable ordering) so regeneration is idempotent and diffs are meaningful.
- Consumers: MCP `template://catalog`, LP-2 type detection, the count-consistency check, the trust-manifest verifier (Play 3), the atlas (may read counts).
- Count-consistency check extends to: README bundle count, manifest `bundle_count`, actual bundle dirs, and the Tier-1 claim ("N of 27"; note the audit-adjacent discovery that prose says 28 while atlas data says 27; reconcile first, then guard).

## 3. Single-variant bundles (unblocks the ADR bundle and six other Tier-1 S-only types)

Decision recommended (record as ADR): single-size types ship ONE variant file named `<type>_template-lean.md` with `sizes_available: [lean]` and `default_size: lean`. Rationale: keeps the 8-file role naming uniform (no new filename pattern), reads correctly ("the minimum genuinely useful version" is the only version), and avoids inventing an s/m/l vocabulary for types the catalog marks S-only.

Gate consequences:
- Check A (files): required set derives from sizes_available (one template file when one size).
- Check C (nesting): applies only when 2+ sizes; single-variant bundles report "single size, nesting n/a (pass)".
- Check F (meta sizes): unchanged logic, now driven by the schema enum.
- Methodology section B1 gains one sentence making this explicit (the "let the type decide" rule, operationalized).

## 4. Instance frontmatter (filled documents) v0.2

Existing: title, doc_type, size, owner, status, doc_version, created, updated, related_links, source_template, source_template_version. Added (audit C-08): `filled_by` (string), `fill_method` (enum: manual, interview, batch, agent), `fill_date` (date; stamped by strip-template.py), optional `extends_template` (bool). Consumers: provenance verifier, LP-1/LP-2, future usage analytics. Ship as placeholder lines in both variants so the fields exist from fill one.

## 5. alias-index.json (generated + curated)

Generated entries from every meta's `aliases` (target: bundle path); curated entries for high-traffic unbuilt types (target: `future:<id>`). Gate check: every non-future target exists; every built bundle contributes all its aliases; no alias maps to two targets (collision fails; the launch-checklist name collision documented in 12_catalog section 4 is the seeded test case). Consumers: LP-2 type detection, MCP search, atlas search.

## 6. Section schema (AG-1): the machine shape of each template

Generated per bundle by `tools/gen-sections.py` from the variant files themselves (derived, never hand-written, so it cannot drift from the templates):

```json
{
  "bundle": "prd", "template_version": "0.1.0",
  "sections": [
    { "id": "summary", "title": "Summary", "level": 2,
      "in_lean": true, "in_full": true,
      "guidance_fields": ["WHAT","WHY","ASK","GOOD","WEAK","TRAP"],
      "has_table": false, "placeholders": ["summary"] },
    { "id": "functional-requirements", "title": "Functional requirements",
      "level": 2, "in_lean": false, "in_full": true,
      "guidance_fields": ["WHAT","WHY","ASK","PRIORITY","ROW HINT","GOOD","WEAK","TRAP"],
      "has_table": true, "placeholders": ["req_1"] }
  ]
}
```

Embedded into manifest.json per bundle (not a ninth bundle file; it is generated data, and the 8-file contract stays stable). Consumers: LP-1 completeness check, LP-2 structure layer, MCP validate_fill, and the comment-grammar gate check (the generator failing to parse a comment IS the grammar check from the LP-1 spec).

## 7. The gate alphabet (target state; letters are the public names)

| Check | What | Since |
|---|---|---|
| A files | Role set derived from sizes_available | exists (adapt in section 3) |
| B dashes | em/en dash sweep, all files | exists |
| C nesting | ordered subset, (level, text) tuples, 2+ sizes only | exists (extend WP-11) |
| D placeholders | example clean AND meta clean | exists (extend WP-11) |
| E citations | inline resolves AND no padded entries (both directions) | exists (extend WP-11) |
| F meta sizes | via schema | exists (subsumed by G) |
| G schema | every meta validates against meta.schema.json | WP-21 |
| H pairs_with | resolves against pinned pm-skills ID list or null | WP-11 |
| I history | entry exists for current template_version | WP-11 |
| J manifest | regeneration is a no-op (manifest fresh, hashes match) | WP-22 |
| K grammar | every guidance comment parses under the LP-1 grammar | WP-53 (with gen-sections) |
| L related | related_templates resolve or carry future: | WP-11 |
| M family | member conforms to its family contract | WP-24 |
| N links | lychee link status (separate CI job, same workflow) | WP-26 |

Gate output ends with the conformance level per bundle (L1 = A-F green; L2 = plus G-M green and citation integrity clean; L3 = plus scorecard above floor).

## 8. Acceptance criteria

- [ ] All four metas validate against the schema with zero warnings; a fixture with an undeclared field and a `{{placeholder}}` fails.
- [ ] `gen-manifest.py` twice in a row produces byte-identical output; CI runs it and fails on diff.
- [ ] The Dimension C selection simulation passes 6 of 6 (bundle AND size) using manifest data alone.
- [ ] A synthetic single-variant fixture bundle passes the gate with "nesting n/a".
- [ ] gen-sections parses all 68 existing guidance comments (the grammar holds against reality); one deliberately malformed comment fixture fails check K.
- [ ] alias collision fixture fails; current aliases produce zero collisions.

## 9. References

Audit findings B-02, B-05, C-03, C-04, C-05, C-06, C-08, D-06; the single-variant need from 12_catalog-recommendations.md section 1; JSON Schema draft 2020-12; the no-consumer rule from 13_excellence-and-innovation.md.
