# Spec: LP-1 Use-Template Flow (blank template to validated document)

- **Status:** proposed | **Roadmap:** WP-50 (M5, gated on M3 usage signal) | **Effort:** L | **Closes:** audit finding C-01 (no machine fill path)
- **One line:** an interview-driven (or batch) fill flow that turns a blank template plus author answers into a validated, provenance-stamped, guidance-stripped document, using the guidance comments that already exist as its interview script.

## 1. Purpose

The enriched comments were designed as author guidance; their WHAT and ASK fields are, unmodified, a per-section interview script. LP-1 is therefore an orchestration layer over existing content, not a content build: select, interview, fill, stamp, strip, validate. The audit confirmed every ingredient exists except the connective code (finding C-01, CONFIRMED).

## 2. Packaging

- **v1:** `skills/use-template/SKILL.md` in this repo (interactive; agent-executed).
- **v2:** `tools/fill-template.py` CLI for scripted/batch use (same core steps, no interview).
- The strip step is a standalone tool from day one (`tools/strip-template.py`, WP-25) because it is useful without LP-1.

## 3. The comment grammar (normative contract)

LP-1 depends on the guidance-comment format being machine-stable. This grammar is the contract; add it to the family contract and gate:

- A guidance block is a single HTML comment (`<!-- ... -->`) immediately following a section heading (or the frontmatter, for the preamble).
- Fields are uppercase labels at line start within the comment, in this order where present: `WHAT`, `WHY`, `ASK`, `GOOD`, `WEAK`, `TRAP`, and for table sections `PRIORITY`, `ROW HINT`.
- A field's value runs until the next label or comment end. Extraction regex (Python flavor):

```python
FIELD_RE = re.compile(
    r"^\s*(WHAT|WHY|ASK|GOOD|WEAK|TRAP|PRIORITY|ROW HINT)\s+(.*?)(?=^\s*(?:WHAT|WHY|ASK|GOOD|WEAK|TRAP|PRIORITY|ROW HINT)\s|\Z)",
    re.M | re.S)
```

- Gate extension (machine-metadata spec, check letter per that doc): every section comment parses under this grammar; parse failure fails the bundle. This converts the comment standard from prose convention to enforced interface.

## 4. Flow (interactive mode)

1. **Select.** Resolve intent to bundle via manifest.json (aliases, summary, tags); pick size via `default_size` unless the user's stated scope triggers `sizing_guidance` escalation; confirm both in one line ("Filling: PRD, lean. Right?").
2. **Frontmatter.** Collect title/owner; stamp `source_template`, `source_template_version` from meta; set `status: draft`, dates.
3. **Interview, section by section.** For each section (order from the template): show WHAT plus the ASK questions verbatim; capture the answer; draft the section content from the answer (respecting GOOD as the register to imitate and TRAP as the check to run on the draft before showing it); confirm or revise. The author may answer "N/A": write "N/A" plus their one-line reason (the methodology's rule), never delete the section.
4. **Table sections.** Use ROW HINT as the row template and PRIORITY as the legend; gather rows conversationally.
5. **Self-check.** Run the drafted document against the bundle guide's rubric (this is LP-2's scoring layer reused); if below B, present the weak items and offer one revision pass.
6. **Stamp and strip.** Fill `filled_by` (author name or agent identity), `fill_method: interview`, then run strip-template.py, which removes every guidance comment and stamps `fill_date`.
7. **Validate.** Placeholder scan (no `{{...}}` remaining), comment scan (none remaining), section-schema completeness when available (machine-metadata spec section 6). Report the validation summary as the final message.

**Batch mode** (v2 and agent-to-agent use): the caller provides a context pack (facts, constraints, links) instead of interactive answers; the flow drafts all sections, marks any section whose confidence is low with a visible `TODO(review):` line, and never fabricates specifics (illustrative numbers get the "(illustrative)" label per methodology B4).

## 5. strip-template.py (behavioral spec, ~25 lines)

- Input: a filled markdown file path. Output: in-place or `--out` copy.
- Removes every `<!-- ... -->` block (multi-line aware); collapses runs of 3+ blank lines to 2.
- Stamps `fill_date: YYYY-MM-DD` into frontmatter if a `fill_date` key is absent or placeholder.
- Refuses (exit 2, message) if `{{placeholders}}` remain, unless `--allow-placeholders` (partial-save workflow).
- Exit 0 plus a one-line summary: comments removed, placeholders remaining, fill_date stamped.

## 6. Edge cases

| Case | Behavior |
|---|---|
| Author wants sections beyond the template | Allowed; appended after template sections; frontmatter gains `extends_template: true` so validation does not flag them as drift |
| Lean-to-full upgrade mid-fill | Supported by the nesting rule: fetch full variant, carry existing sections over unchanged, interview only the added sections |
| Partial fill, resume later | Save with comments intact (they are the resume state); strip only at ship |
| Author rejects a drafted section twice | Stop drafting, capture their raw text verbatim, move on (the tool assists, never argues) |
| Fabrication pressure (batch mode asked for metrics it does not have) | Insert `{{metric}}` placeholder or "(illustrative)" label; never invent unlabeled specifics |

## 7. Acceptance criteria

- [ ] End-to-end interactive fill of the lean PRD by someone other than the maintainer, producing a validated document in under 25 minutes.
- [ ] Output carries all provenance fields; strip leaves zero comments and zero placeholders; validation summary printed.
- [ ] Batch mode fills user-stories from a context pack with every low-confidence section visibly marked.
- [ ] The comment-grammar gate check passes on all bundles before LP-1 ships (grammar is enforced, not assumed).
- [ ] Upgrade path demo: a filled lean PRD grows to full with original sections byte-identical.

## 8. Dependencies and references

Depends on: WP-25 (strip tool + `filled_by`/`fill_method` fields, C-08/C-09), WP-22 manifest (selection), WP-23 sizing metadata (C-04), grammar gate check. Enhanced by: AG-1 section schema. References: audit C-01; methodology B1/B4; Anthropic tool-writing guidance (one consolidated operation per user intent).
