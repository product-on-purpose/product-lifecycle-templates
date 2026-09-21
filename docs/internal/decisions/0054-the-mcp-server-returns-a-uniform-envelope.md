---
status: accepted
date: 2026-09-20
decision-makers: [jprisant]
consulted: [claude]
---

# The MCP server returns a uniform `{ok, data?, error?}` envelope, and `ok` stops meaning three things

## TL;DR

- **Decision.** All five MCP tools return one shape: `{ok: bool, data?: <per-tool>, error?: {code,
  message, ...hints}}`. Outer `ok` means **the call completed and `data` is populated**, nothing else.
  Each tool declares a **per-tool `TypedDict`** return annotation, which is what makes FastMCP emit an
  `outputSchema` and populate `structuredContent`.
- **Why now:** it is a breaking change to a shipping wire format and **nothing external calls the server
  today**. This is the cheapest it will ever be, and every future consumer raises the price.
- **The problem was never the annotation.** Adding one was measured to be the *cause* of a regression,
  not the fix: the SDK validates returns against the schema, and today every tool's error shape is
  structurally different from its success shape, so annotating raises `ToolError` on every refusal path.
  The contract has to be uniform **first**.
- **The find this ADR adds to the spec's framing:** `ok` is **already overloaded three ways** in the
  shipped server. So the naive envelope would produce `{ok: true, data: {ok: false}}` for an invalid
  document, which is correct and a trap. The inner fields are renamed: `data.valid` and `data.refused`.
- **Measured, not recalled.** Three annotation shapes were spiked against the installed SDK. All three
  produce a schema; the pydantic union nests everything under `result`, so it loses. Per-tool
  `TypedDict` wins because it is the only one whose schema asserts something about `data`.
- **Status:** accepted 2026-09-20. Implementation is a separate PR that cites this ADR.

## Context and Problem Statement

[`ag2-mcp-spec.md`](../ag2-mcp-spec.md) section 5 records the gap: tool responses arrive as JSON text in
`content[0].text` rather than as `structuredContent`, the protocol's typed channel. An agent must
re-parse text that the protocol could have handed it as data.

The spec also records a **correction worth more than the original note**. The cause first recorded on
2026-09-06 was that the tools "carry no return annotation for FastMCP to build an output schema from",
which implies annotating would fix it. Measured against `mcp 1.30.0` on 2026-09-11:

- `-> dict` produces **no** `outputSchema` and **no** `structuredContent`. The stated fix does nothing.
- `-> <TypedDict>`, `-> <BaseModel>` and `-> list[<BaseModel>]` all work.
- **And that is why it was still not fixed.** Every tool returns an error shape structurally different
  from its success shape, the SDK validates the return against the schema, so annotating raises
  `ToolError: 1 validation error ... Field required` on every refusal. A refusal would stop being a
  clean, readable result and become a thrown error.

That is a regression in the one behaviour `tools/test-mcp-server.py` calls load-bearing: "a wrapper that
swallowed a refusal and reported success would pass a test that only ever fed it good documents."

So closing the gap requires deciding the error contract first. The spec explicitly left that to the
maintainer and did not decide it here.

### What the shipped server actually returns, enumerated

Read off `tools/mcp_server.py` rather than recalled. Five tools, **three** conventions:

| Tool | Success shape | Failure shape |
|---|---|---|
| `search_templates` | `{query, candidates, ...}` | none; always answers, possibly with zero candidates |
| `get_template` | `{id, format, size, parts, ...}` | `{error, did_you_mean}` / `{error, available, note}` / `{error, available_parts}`, **no `ok` key** |
| `get_grading_pack` | `{id, rubric, ...}` | `{error}` / `{error, id}`, **no `ok` key** |
| `validate_fill` | `{file, ok, findings, not_verified}` | `{ok: false, error}` |
| `stamp_and_strip` | `{ok, exit_code, refused, output, note}` | `{ok: false, exit_code, error}` |

Plus a **nested** failure at line 313: when a bundle ships no requested part, that part's entry inside
`data` is `{"error": "this bundle ships no guide"}`.

### The overload, which the spec's sketch does not address

`ok` currently means three different things:

1. In `validate_fill`, **the document passed validation**. A domain truth.
2. In `stamp_and_strip`, **the wrapped CLI exited 0**. A different domain truth, with `refused` carrying
   the exit-2 case.
3. On file-not-found in both, **your request was bad**. A transport truth.

So `ok: false` is *already* ambiguous: it means either "your file does not exist" or "your document is
invalid", which are unrelated things for a caller to act on. Wrapping this in an envelope without
renaming would yield `{ok: true, data: {ok: false}}` for an invalid document. Correct, and a trap for any
agent that checks one level and stops.

## Decision Drivers

- `structuredContent` is the protocol's typed channel and the reason to have a schema at all.
- A schema must **assert something**. The spec already rejected a `total=False` TypedDict where every key
  is optional as "delivering the label without the value"; that reasoning binds here too.
- A refusal must stay a clean, readable result. This is the behaviour the existing test calls
  load-bearing, and the DF-7 lesson says a check that returns *something* is not one that returns the
  *right* thing.
- Breaking changes get cheaper the earlier they happen, and there is no external consumer yet.
- The mechanism must be **tested before being recorded**, not reasoned about.

## Considered Options

1. **Uniform `{ok, data?, error?}` with per-tool `TypedDict`.** Chosen.
2. **Uniform envelope with one flat `TypedDict`** shared by all five tools, `data: dict[str, Any]`.
3. **Pydantic discriminated `Union[Ok, Err]` on `ok`.**
4. **`total=False` TypedDict**, every key optional. Rejected by the spec already, and rejected here.
5. **Do nothing.** Keep text responses, revisit when a consumer appears.

## Decision Outcome

**Chosen: option 1.** Every tool returns:

```python
class Err(TypedDict):
    code: str        # closed enum, see below
    message: str
    # plus per-code hint fields: did_you_mean, available, available_parts

class EnvValidateFill(TypedDict):
    ok: bool
    data: NotRequired[ValidateFillData]
    error: NotRequired[Err]
```

### Evidence: the spike, run 2026-09-20 against the installed SDK

Three shapes were registered on a scratch `FastMCP` and driven through `list_tools()` and `call_tool()`
on **both** the success and the refusal path. Measured at **`mcp 1.27.2`, `pydantic 2.13.4`**, which is
the version installed here; the spec's earlier measurements were at `1.30.0`.

| Shape | `outputSchema`? | success | refusal | Top-level keys |
|---|---|---|---|---|
| (a) flat `TypedDict`, `data: dict[str, Any]` | yes, `required=['ok']` | populated | **clean, populated** | `ok, data, error` |
| (b) **per-tool `TypedDict`** | yes, `required=['ok']` | populated | **clean, populated** | `ok, data, error` |
| (c) pydantic `Union[Ok, Err]` | yes, `required=['result']` | populated | clean, populated | **`result` only** |

Baseline re-confirmed in the same run: an unannotated tool and a `-> dict` tool both produce
**no** `outputSchema` and **no** `structuredContent`, reproducing the spec's 1.30.0 finding at 1.27.2.

**Why (b) over (a):** both behave identically at the envelope level, but (a) types `data` as
`dict[str, Any]`, so the schema asserts nothing about the payload. That is the same "label without the
value" the spec rejected. (b) types each tool's `data` concretely and is the only option whose schema
carries real information.

**Why not (c):** it works, but FastMCP wraps a union return under a `result` key, so every caller reads
`structuredContent["result"]["ok"]` instead of `structuredContent["ok"]`. An extra level for no gain.

**The absent branch serializes as an explicit `None`** rather than being omitted (`{"ok": true, "data":
{...}, "error": null}`). Accepted, and arguably better: the key is always present to test.

### The contract, stated

1. **Outer `ok` means one thing only:** the call completed and `data` is populated. It is never a domain
   answer.
2. **Inner domain fields are renamed** so no level of the response reuses the word:
   - `validate_fill`: `ok` becomes **`data.valid`**.
   - `stamp_and_strip`: the inner `ok` is **dropped**; `data.exit_code` and `data.refused` already carry
     the information, and `refused` is the meaningful one.
3. **The error-versus-outcome boundary.** `ok: false` is for a request that referenced something which
   does not exist or was malformed. `ok: true` covers everything the server was actually able to do,
   **including answering "your document fails" or "strip refused"**. The server's own note already says
   exit 2 "is the intended outcome for a document that still carries an unfilled placeholder", so a
   refusal is an answer, not an error. An exit code from `strip-template.py` that is neither 0 nor 2 is
   the murky case and is `ok: false` with `error.code: "strip_failed"` and the captured output in the
   error.
4. **`error` is an object, never a string.** Today's refusals carry the genuinely useful parts:
   `did_you_mean`, `available`, `available_parts`, `note`. Those survive as fields on `error`.
   `error.code` is a **closed enum**: `no_such_bundle`, `no_such_variant`, `unknown_part`,
   `no_such_file`, `strip_failed`. A closed enum is what lets the schema assert something.
5. **The nested per-part `error` at line 313 goes.** A bundle shipping no `example` is a fact about the
   bundle, not a caller error, and a key named `error` inside `data` shadows the envelope. It becomes
   `{present: false, reason: "..."}` and the call stays `ok: true`.
6. **`search_templates` gains the envelope** even though it has no failure path today, because a uniform
   contract with one exception is not uniform.

### Consequences

- **This is a breaking change to a shipping wire format.** Under semver on a `0.x` line it is a minor
  bump. It ships in the same release as the site work already queued in `[Unreleased]`.
- `tools/test-mcp-server.py` must assert `structuredContent` is populated **on both the success and the
  refusal path for every tool**, and must **fail rather than skip** when the SDK is absent. That is DF-7
  applied to the new surface: the reason this class of defect shipped before is a self-test that skipped
  its only real assertion and exited 0.
- The two CLI-wrapping tools keep wrapping. `validate_fill` and `stamp_and_strip` still call
  `validate-fill.py` and `strip-template.py`, so server-CLI parity stays true by construction. Only the
  envelope around the result changes.
- `docs/how-to/installing.md` and any documented response shape need updating in the implementation PR.
- **Out of scope, deliberately: the `mcp<2` port.** The SDK renamed `FastMCP` to `MCPServer` in v2 and
  this server is pinned to `<2` (see the module header and ADR 0045). **Whether v2 treats return
  annotations identically is not verified here**, because installing v2 locally would break the running
  server, and bundling the port would turn a wire-format change into a framework migration. If v2 handles
  annotations differently, the envelope shape is still right and only the annotation mechanics move.

## More Information

- The spec this closes: [`ag2-mcp-spec.md`](../ag2-mcp-spec.md) section 5.
- Why the server is Python and lives here:
  [ADR 0045](0045-the-mcp-server-is-python-and-lives-in-this-repository.md).
- The DF-7 precedent, a gate that degraded to a skip and printed OK: recorded in the `mcp_server.py`
  module header, and the reason `tools/test-mcp-server.py --require-sdk` now fails instead of skipping.
- Spike script, not committed: run from the session scratchpad on 2026-09-20; the table above is its
  output and is reproducible by registering the three shapes on a scratch `FastMCP` and driving
  `list_tools()` and `call_tool()` on both paths.
