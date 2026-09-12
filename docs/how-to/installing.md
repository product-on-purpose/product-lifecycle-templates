---
title: "Installing the library"
description: "The two install routes, what each one actually gives you, and how to check that it worked"
audience: "both"
level: "beginner"
tags:
  - how-to
  - installation
---

# Installing the library

There are two routes. **They do not give you the same thing**, and the difference is not documented
anywhere else because it was only discovered on 2026-08-08, by running the install for the first time.

| Route | What you get | Use it when |
|---|---|---|
| **Claude Code plugin** | both skills **and** all 27 bundles | you want the library to work. **This is the recommended route** |
| **`npx skills add`** | the two skills only, about 47 KB | you use a non-Claude agent, or you want them to fetch what they need on demand |
| **`git clone`** | everything, unmanaged | you are contributing, or you want to read the research |

**If you only read one line: use the plugin route unless you have a reason not to.**

---

## Route 1: the Claude Code plugin (recommended)

The plugin installs by cloning the repository, so the templates come with it and every path the skill
refers to resolves.

```
/plugin marketplace add product-on-purpose/agent-plugins
/plugin install product-lifecycle-templates
```

### Check that it worked

Ask your agent to list the available document types. It should read `manifest.json` and name 27 bundles.
If it can read `manifest.json`, everything else in the library is reachable.

### The MCP server comes with it

This route also brings an MCP server ([`.mcp.json`](../../.mcp.json), served by
[`tools/mcp_server.py`](../../tools/mcp_server.py)), which gives an agent five tools: search the catalog,
fetch any of the 58 template variants, fetch a grading pack, validate a filled document, and strip and
stamp one. Nothing is embedded or duplicated, because this route already put the templates on disk.

It needs **Python 3 and the `mcp` package, pinned below version 2**, in whichever interpreter `.mcp.json`
names:

```
python3 -m pip install "mcp<2"
python3 tools/mcp_server.py --selftest    # reports what it would serve, starts nothing
```

**The `<2` is required, and a plain `pip install mcp` will not work.** The SDK released version 2 on
2026-07-28 and renamed the class this server imports (`FastMCP` became `MCPServer`), so the unpinned
command succeeds, installs cleanly, exits zero, and leaves the server unable to start. If you already ran
it, `python3 -m pip install "mcp<2"` over the top is the whole fix. The selftest is how you confirm: it
prints `SDK present; the server would start` when the interpreter can actually serve, and says `ABSENT`
otherwise rather than waiting for your agent to fail.

`.mcp.json` says `python3`. If your machine resolves that to an interpreter without the package - and
`python`, `python3` and `py` are routinely three different interpreters on one machine - change the
`command` there. The server names the interpreter it ran under when it cannot find the SDK, so the error
tells you which one to fix.

The rest of the library does not depend on the server. Skip this and every skill, template and check
still works.

---

## Route 2: `npx skills add`

```
npx skills add product-on-purpose/product-lifecycle-templates
```

**This installs the skills and not the library.** Eight files land, about 47 KB, and none of the 26
bundles come with them. That is not a bug in this repository and it is not a bug in the CLI: a skill is a
directory containing `SKILL.md`, the installer copies that directory, and this library's knowledge lives
outside it in `templates/`.

**What the skills do about it.** Each one's first instruction is to check whether `manifest.json` is
reachable and to **stop and tell you** if it is not, rather than working from memory. If you have
network access each fetches the manifest plus the one file it needs, pinned to the release tag
matching its own version: `plt-fill-template` takes a template, `plt-grade-doc` takes that type's
guide. **Two requests either way**, rather than a repository sync.

**What you should expect.** A skill that says "the library is not installed" is behaving correctly. A
skill that cheerfully produces a PRD without ever reading a template is the failure this design exists to
prevent: the library's own measurement scored a template filled with confident generic prose at **1.00
out of 5**, answering **zero of five** retrieval probes. A fluent document is not evidence that anything
worked.

### Check that it worked

```
npx skills add product-on-purpose/product-lifecycle-templates --list
```

**It should report exactly two skills, `plt-fill-template` and `plt-grade-doc`.** If it reports any other
set, that is a defect in this repository, and [`tools/check-export-surface.py`](../../tools/check-export-surface.py)
exists to make it impossible: it fails CI whenever the set of skills the installer would export stops
matching the set [`library.json`](../../library.json) declares. It was written on 2026-08-08, the day
an install reported two skills while `library.json` declared one, the extra being a maintainer-internal
build harness. **Two is now the correct answer**, which is why that sentence needed a date.

---

## Route 3: clone it

```
git clone https://github.com/product-on-purpose/product-lifecycle-templates.git
```

Everything is present: 27 bundles, the research logs behind every claim, the gate, the evals. Nothing
manages updates for you.

This is the right route if you want to **read** rather than **use**. The research logs are the part of
this library that is hardest to get any other way.

---

## What to read next

- [Getting started](../tutorials/getting-started.md) - fill your first template in fifteen minutes
- [Choosing a template](../reference/choosing-a-template.md) - from a job to be done to a bundle
- [What the gate proves](../explanation/what-the-gate-proves.md) - the honest scope of the quality claim,
  including what no machine here checks
