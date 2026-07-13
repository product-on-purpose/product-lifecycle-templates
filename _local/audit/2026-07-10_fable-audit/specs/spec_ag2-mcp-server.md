# Spec: AG-2 MCP Server (product-lifecycle-templates-mcp)

- **Status:** proposed | **Roadmap:** WP-51 (M5, gated on M3 usage signal) | **Effort:** L+ | **Closes:** the reach half of audit finding C-01; makes "agent-native" literally true
- **One line:** an MCP server that lets any agent discover, select, fetch, validate, and stamp templates deterministically, with token-budgeted responses and provenance on every payload.

## 1. Purpose and posture

The library's agent story today requires filesystem access and prose understanding. The MCP server makes the machine path first-class: a coding or PM agent anywhere (Claude Code, Desktop, any MCP client) gets templates as tools and resources. Design posture, and the reason this spec is smaller than it could be: **the server is deterministic; judgment stays in the client agent.** The server never runs its own LLM. It serves content, structure, rubrics, and validation; the calling agent does selection reasoning, drafting, and grading with materials the server hands it. This keeps the server cheap, testable, and offline-capable, and honors the layered design's bright line (the library is a noun; verbs live in the consumer).

## 2. Stack (mirror the proven sibling)

Mirror `pm-skills-mcp` (inspected 2026-07-10: TypeScript, MCP SDK, `dist/` tsc build, `embed-skills` build step that packages content into the artifact, vitest, npm bin, currently v2.9.3): same layout, same publish flow, name `product-lifecycle-templates-mcp`. The embed step packages `templates/**`, `manifest.json`, `alias-index.json`, and rubric extracts so the server runs with zero repo dependency at runtime. Server version pins to a library release tag and reports both.

## 3. Tools (few, consolidated, high-signal)

Per Anthropic's tool-writing guidance (fetched during the audit): consolidated operations, token-efficient responses, descriptions with examples, errors that teach the next call.

### 3.1 `search_templates`
- **In:** `{ query: string, phase?: string, max?: number = 3 }`
- **Does:** lexical rank over aliases, title, summary, tags (deterministic; no embeddings in v1; the alias index carries most real traffic).
- **Out:** ranked candidates, each: `{ bundle_id, title, one_line_summary, sizes_available, default_size, sizing_guidance, approx_tokens: {template_lean, template_full, guide, companion}, conformance, state }`. Under 400 tokens for 3 candidates: enough for the client agent to decide without a second round trip.
- **Teachable error:** empty result returns the 8 phase names and 3 example queries.

### 3.2 `get_template`
- **In:** `{ bundle_id, size?: "default", parts?: ["template","guide"] }`
- **Does:** returns requested parts with per-part token counts and the bundle's provenance header `{ template_version, sha256, library_version }`.
- **Defaults:** `parts` defaults to template + guide (roughly 1.6-2.5k tokens); **companion is never included by default** and is requested explicitly (budget discipline; the audit measured companions at 3.2-5.3k tokens).
- **Out cap:** refuse combined payloads over 8k tokens with a message naming which parts to drop.

### 3.3 `get_grading_pack`
- **In:** `{ doc_type }`
- **Does:** returns everything the CLIENT needs to run LP-2 grading: the guide rubric (itemized), section lists (lean/full), named anti-patterns + TRAP lines, the report-card format, and the tone rules.
- **Out:** ~800-1,200 tokens. The judgment (scoring a real document) happens in the client agent; the server guarantees the client grades against the same rubric version every time.

### 3.4 `validate_fill`
- **In:** `{ content, bundle_id }`
- **Does (deterministic):** placeholder scan; residual-comment scan; frontmatter provenance check (source_template, source_template_version present and matching); section completeness against the section schema (lean floor; notes full-only sections present); `extends_template` detection.
- **Out:** `{ ok, placeholders_left[], comments_left, missing_sections[], extra_sections[], provenance: pass|fail|mismatch }` plus one actionable line per failure.

### 3.5 `stamp_and_strip`
- **In:** `{ content, bundle_id, filled_by, fill_method }`
- **Does:** the strip-template.py behavior as a service: removes guidance comments, stamps `fill_date` + `filled_by` + `fill_method`, re-runs validate_fill, returns the clean document and the validation summary.

Not in v1 (deliberately): a server-side `fill_template` (drafting is client judgment); embeddings search (alias index first; add only if search misses are logged in telemetry); write-back/post-a-filled-doc (needs a storage decision that does not exist yet).

## 4. Resources

- `template://catalog`: manifest.json verbatim (the machine catalog; includes counts, conformance levels, scorecards).
- `template://{bundle_id}/summary`: guide + meta composed, ~800-1,000 tokens: the default thing a client should read before deciding to fetch more (the bundle-summary pattern from the audit's Dimension C ideas).
- `template://{bundle_id}/companion`: the deep explainer, explicit-request only.

## 5. Cross-cutting rules

- **Provenance everywhere:** every content payload carries `template_version`, `sha256`, `library_version` (Play 3, trust manifest). A client can later verify a filled doc's lineage against `template://catalog`.
- **Token budgets are contract:** default responses under 1,200 tokens; every response includes its own token count; caps are errors that name the cheaper alternative.
- **Determinism:** identical inputs return identical outputs for a given server version (this is what makes the server testable and the client's behavior reproducible).
- **No telemetry in v1** beyond an opt-in counter of tool calls by type (LP-3 is a later, consent-first decision).

## 6. Testing

- vitest unit tests per tool (fixtures from the real bundles).
- **The audit simulation as integration test:** the three Dimension C intents must resolve via `search_templates` to the correct bundle AND size using only tool outputs (the audit showed bundle selection worked 3 of 3 but size failed 3 of 3 pre-metadata; this test locks the fix in).
- A `validate_fill` golden set: one clean fill, one with placeholders, one with comments, one with provenance mismatch.

## 7. Distribution

npm package with bin (mirrors sibling); README config snippets for Claude Code (`claude mcp add`), Claude Desktop, and generic MCP clients; MCP registry listing when published; version policy: server minor tracks library minor.

## 8. Acceptance criteria

- [ ] A fresh agent with only this server configured completes intent-to-validated-document (using LP-1 logic client-side) with zero filesystem access.
- [ ] Default `get_template` payload for every bundle lands under 2.6k tokens; companion never ships unrequested.
- [ ] Integration test: 3 of 3 audit intents resolve to correct bundle and size.
- [ ] Provenance headers verify against manifest hashes for all four bundles.
- [ ] Embedded build runs offline (no repo checkout at runtime).

## 9. Dependencies and references

Hard: manifest.json + alias index (WP-22), sizing metadata (WP-23), section schema (WP-53), strip behavior (WP-25). Gated on: M3 usage signal (per roadmap; the server amplifies a proven loop). References: audit C-01, C-03, C-06; Anthropic writing-tools-for-agents; modelcontextprotocol.io; sibling pm-skills-mcp as the architectural reference.
