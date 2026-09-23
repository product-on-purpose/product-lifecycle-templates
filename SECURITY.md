# Security policy

## What this repository is, and what that means for risk

This repository ships **markdown documents, Python scripts, and a local MCP server**
([`tools/mcp_server.py`](tools/mcp_server.py)). The server runs only when an agent starts it, as a child
process that talks over stdio: it opens no network port. Neither the server nor any script in `tools/`
makes a network request of its own, with one exception: `run-gate.py` runs CI's steps locally, and one of
them clones the pinned standard toolkit from GitHub and installs its Node packages (`--offline` skips it).
The Python dependencies are three packages, all installed by CI: `pyyaml` and `jsonschema` for the gate,
and `mcp` (pinned below 2) for the server. The website under `site/` is built from Node packages (Astro and
Starlight) in CI and serves static pages; none of that code runs on a reader's machine. Nothing here
executes on a user's machine unless they choose to run a script in `tools/` or let an agent start the
server.
*(Corrected 2026-09-23: this paragraph said the repository had no server and two dependencies. The MCP
server has shipped since `v0.6.0`, and `mcp` is the third package CI installs.)*

The realistic risks are therefore narrow, and worth naming precisely rather than covering with a generic
policy:

- **A malicious link in a template or research log.** Every relative link is gated by CI, but external URLs
  in research logs point wherever the source lived. Treat them as you would any link in a document.
- **A script in `tools/` doing more than it says.** Most are stdlib-only; the ones that import `pyyaml`,
  `jsonschema` or `mcp` do so at the point of use. They are read-only apart from the generators (the
  `gen-*.py` scripts and `scripts/gen-site.mjs`), `strip-template.py`, which writes a stripped copy of the
  document it is given, and `source-cache.py`, which writes to a local cache under `_local/`. Read before
  running.
- **The MCP server acting on a path an agent chose.** Four of its five tools only read. The fifth,
  `stamp_and_strip`, writes one file: beside the document it is given, or at the `out` path the agent passes.
  An agent you would not trust with a file write should not be given this server.
- **A supply-chain issue in a dependency.** The three Python packages and the site's Node packages affect CI
  and the published site. A user who runs the MCP server installs `mcp` and inherits its supply chain.

## Reporting

Open a **private security advisory** through GitHub on this repository, or a normal issue if the finding is
not sensitive. There is no separate security contact and no bug bounty.

**Expected response:** this is a single-maintainer project. A realistic acknowledgement window is days, not
hours. If that is not fast enough for your situation, say so in the report and treat the finding as public.

## What is not a security issue here

- A factual error in a template, companion, or research log. Those are correctness issues and belong in a
  normal issue. They are taken seriously; `CONTRIBUTING.md` explains how.
- A template producing a document that discloses something it should not. The templates prompt for content;
  what a filled document contains is the author's call. Several bundles warn about this explicitly.
