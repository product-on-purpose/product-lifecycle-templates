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
| **Claude Code plugin** | the skill **and** all 26 bundles | you want the library to work. **This is the recommended route** |
| **`npx skills add`** | the skill only, about 12 KB | you use a non-Claude agent, or you want the skill to fetch bundles on demand |
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

Ask your agent to list the available document types. It should read `manifest.json` and name 26 bundles.
If it can read `manifest.json`, everything else in the library is reachable.

---

## Route 2: `npx skills add`

```
npx skills add product-on-purpose/product-lifecycle-templates
```

**This installs the skill and not the library.** Two files land, roughly 12 KB, and none of the 26
bundles come with them. That is not a bug in this repository and it is not a bug in the CLI: a skill is a
directory containing `SKILL.md`, the installer copies that directory, and this library's knowledge lives
outside it in `templates/`.

**What the skill does about it.** Its first instruction is to check whether `manifest.json` is reachable
and to **stop and tell you** if it is not, rather than writing a document from memory. If you have
network access it will fetch the manifest and the single template it needs, pinned to the release tag
matching its own version, which is two requests rather than a repository sync.

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
matching the set [`library.json`](../../library.json) declares. It was written the day the install
reported two.

---

## Route 3: clone it

```
git clone https://github.com/product-on-purpose/product-lifecycle-templates.git
```

Everything is present: 26 bundles, the research logs behind every claim, the gate, the evals. Nothing
manages updates for you.

This is the right route if you want to **read** rather than **use**. The research logs are the part of
this library that is hardest to get any other way.

---

## What to read next

- [Getting started](../tutorials/getting-started.md) - fill your first template in fifteen minutes
- [Choosing a template](../reference/choosing-a-template.md) - from a job to be done to a bundle
- [What the gate proves](../explanation/what-the-gate-proves.md) - the honest scope of the quality claim,
  including what no machine here checks
