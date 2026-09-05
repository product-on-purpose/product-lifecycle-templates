# Bundle pipeline: the reusable per-bundle runbook

> **This runbook is executable.** [`.claude/commands/build-bundle.md`](../../.claude/commands/build-bundle.md)
> drives it, and [`.claude/workflows/build-bundle.js`](../../.claude/workflows/build-bundle.js) runs its two
> fan-outs: `{stage:"research", type, dimensions}` and `{stage:"review", type, family}`. The script enforces
> in a schema what this document states in prose - the retrieval enum, source ownership, grounded findings -
> so an agent cannot return a quote without having claimed it read the body. The prose here remains the
> authority; the script is one way of executing it.

The executable process for building one Tier-1 bundle to the best-in-class, source-referenced standard,
proven on `sdd` and `product-backlog` (2026-07-20/21). This operationalizes methodology section 8 and the
buildout-plan pipeline, and it is the durable reference a future session (or an autonomous loop) follows.

**The governing principle:** the gate proves a bundle's *structure*, never that its citations *support*
their claims. Three times in one session, every citation defect (combined entries, misattributions, quotes
not in the source) was green in CI and caught only by the adversarial review. So this pipeline's non-
negotiable is the review, not the gate. Never ship a bundle that has not passed the four-lens review with
its findings applied and re-verified.

Per-bundle cost is roughly 0.6-1M tokens (research fan-out + drafting + review). Realistic pace: 1-2
bundles per focused run.

---

## The pipeline (6 phases)

```
1   Research fan-out (parallel sonnet, real web, honest retrieval)
2   Synthesize the research log (dedupe, tier, contested flags)
3   Draft (research-log -> companion -> templates -> guide -> example -> meta -> history)
3.5 Machine pre-read (two report-only lints; seconds, and it aims phase 4)
4   Adversarial four-lens review (parallel sonnet)
5   Apply findings + re-verify (verify each finding against the source first)
6   Gate + land (stage, gate, manifest, README, STATE, PR)
```

Phases 1 and 4 are Workflow fan-outs (sonnet, per the model-routing rule). Phases 2, 3, 5, 6 are main-loop
work. The main loop synthesizes and **re-verifies** every subagent finding before acting (asymmetric
verification: frontier checks sonnet, never sonnet-checks-sonnet).

---

## Phase 0: Spec

Read the bundle's entry in [`buildout-specs.md`](buildout-specs.md): family, phase/classification, sizes,
default, methodology, catalog_ref, aliases, section-design sketch, key sources. Confirm the family's
**contract exists** (a new family needs its contract adopted first, the [ADR 0020](decisions/0020-adopt-delivery-docs-family-contract.md)
pattern). Read one existing sibling bundle end-to-end to mirror its exact file formats.

## Phase 1: Research fan-out

Run a Workflow of 5-6 parallel sonnet researchers, one per dimension (origins/canon, structure, methodology
lineage, debates/status, relationships/tooling, **the gap question**), each doing **real WebSearch/WebFetch**
under strict honest retrieval. Template:

```js
export const meta = { name: '<type>-research', description: '...', phases: [{ title: 'Research' }] }
const SOURCE_SCHEMA = { type:'object', additionalProperties:false, properties:{
  dimension:{type:'string'},
  sources:{type:'array', items:{ type:'object', additionalProperties:false, properties:{
    title:{type:'string'}, author_or_org:{type:'string'}, url:{type:'string'},
    tier:{enum:['primary','practitioner','vendor','reference']},
    retrieval_status:{enum:['fetched-and-verified','url-confirmed-not-read','not-retrieved']},
    supports:{type:'string'}, quotable:{type:'array',items:{type:'string'}},
    contested_or_timebound:{type:'string'} },
    required:['title','author_or_org','url','tier','retrieval_status','supports'] }},
  key_findings:{type:'string'}, contested_claims:{type:'string'} },
  required:['dimension','sources','key_findings','contested_claims'] }
const DISCIPLINE = `STRICT HONEST RETRIEVAL: use real WebSearch/WebFetch, not memory. Per source record
retrieval_status honestly: fetched-and-verified ONLY if you read the page body (only these may be quoted);
url-confirmed-not-read if the URL resolves but you did not read it (no claim rests on it alone);
not-retrieved otherwise. Put a phrase in quotable ONLY if you read it verbatim. NEVER fabricate a quote,
date, author, or URL. Check the page body, not just a 200 (stale URLs redirect). Tier honestly. Flag
genuine disagreements as contested and name the camps.`
const DIMENSIONS = [ /* {key, prompt: '...' + DISCIPLINE} per dimension */ ]
phase('Research')
const results = await parallel(DIMENSIONS.map(d => () =>
  agent(d.prompt, { label:`research:${d.key}`, phase:'Research', model:'sonnet', schema:SOURCE_SCHEMA })))
return results.filter(Boolean)
```

### Dimension 6: the gap question (standing, since 2026-08-14)

**Added by [ADR 0038](decisions/0038-what-the-circularity-signature-obliges.md).** One researcher is always
assigned this question:

> **What does a good document of this type do that this bundle does not ask for?**

It is a **search for absences**, run deliberately at build time rather than discovered later. The first time
anyone asked it, it was a byproduct of building an evaluation, and it surfaced four candidate properties for
three bundles. Asking it once, accidentally, three bundles into twenty-six, is not a method.

**Three rules make the answer usable rather than a wish list:**

1. **It returns candidates, never obligations.** Anything it finds is routed through
   [decision procedure 12](decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template):
   most terminate as a guide rubric row and never touch a template.
2. **Sources, not intuition.** The dimension is bound by the same honest-retrieval discipline as every
   other. "A good PRD probably should..." is not a finding; a named source publishing documents of that
   type containing the element is.
3. **A null result is a real result and gets recorded.** "Nothing found that this bundle omits" is worth
   writing down, because the next author will otherwise ask again from scratch.

**This dimension must not read the bundle's own rubric before searching**, for the same reason held-out
eval criteria must not be drawn from the template: a search that starts from what the bundle already asks
for will find that the bundle asks for it.

## Phase 2: Synthesize the research log

Consolidate the fan-out into `<type>_research-log.md` (methodology section 6 format): dedupe sources (one
entry per source, **never combine two sources**), tier and status each, list quotable phrases per fetched
source, and collect a "Claims flagged contested or time-bound" section. Add a "Notes for the companion"
block naming the honest framing, the load-bearing sections, and the sharpest teaching points.

### The research-log contract (gated since 2026-07-28, ADR 0029)

`tools/check-research-logs.py` runs in CI and fails the build if any entry in a checked log is missing a
required field, or if a log carries no parseable source entries at all.
**Required per source:** a contiguous unique number, title, author or organisation, `url` (or an explicit
statement of why there is none), tier, retrieval status **as one of the three enum tokens**, and
`Supports:`. **Optional:** `Quotable:` and `Contested/time-bound:` - both are optional in the phase 1 schema
above, and an earlier audit that treated them as mandatory reported 76 defects where there were 2. Verify
the rule before enforcing it.

**Tier vocabulary:** `primary`, `standards`, `academic`, `practitioner`, `vendor`, `reference`, `internal`,
each optionally qualified in parentheses (`primary (book)`, `reference (mirror)`). The list layout writes it
as `[Tier N]`.

**Write `Supports:` even when the answer is nothing.** Four entries in the tree were consulted and support
no claim; they now say `Supports: nothing in this bundle. A general vendor how-to, listed because it was
consulted.` A source that earns no claim is worth recording as such, and it costs one word to say so.

**Three layouts are legal**, and the check accepts any of them. **Use the first one for a new bundle**; the
other two exist because the tree does.

```
**[7] Author - Title.** practitioner. **fetched-and-verified.**      <- numbered prose, the house form
`https://example.com/page`
Supports: what this is relied on for.
Quotable: "an exact phrase"        <- optional
Contested/time-bound: ...           <- optional
```

```
7. **[Tier 2] Author. "Title."** https://example.com/page - **fetched-and-verified** - Supports: ...
```

```
| # | Source | Tier | Retrieval | Claims it supports |
| 7 | Author, "Title" https://example.com/page | practitioner | **fetched-and-verified** | ... |
```

Any shape that carries no per-source record is **not** legal, and a log the check cannot parse **fails**
rather than passing quietly. The table form is legal only if it carries a URL and an enum token in the row;
the six logs that use it today carry neither, and are exempt by name (see the check's `EXEMPT` map and DF-4
in [`STATE.md`](../../STATE.md)). Do not copy those six as a model.

**Print-source exemption.** A physical book that was not retrieved has no URL, and inventing a bookseller
link would manufacture the appearance of retrieval. Such an entry states the absence and why, instead of a
URL. See `risk-register` [33] (Hubbard) for the worked form. `No URL.` on its own does not buy the
exemption; the check requires a stated reason.

**What the check does not do:** it proves the fields are present, never that a retrieval status is truthful,
that a `Supports:` clause is accurate, or that a quoted phrase appears in the source. Those are phase 4's
job, and the check says so in its own output on every run.

## Phase 3: Draft (in this order)

1. **companion** (`<type>_companion.md`): 11-section skeleton (methodology section 5), dual-reader, every
   non-obvious claim cited inline `[[n]](#ref-n)`. **Number references contiguously 1..N, one source per
   entry.** Only quote a phrase the research log lists as a verbatim quotable for a fetched-and-verified
   source. Reference entries: `<a id="ref-n"></a>[n] Author. "[Title](url)." ... [tier]`, with honest
   retrieval qualifiers on unread/contested sources. Verify with the check-E snippet below before moving
   on.
2. **template-lean** and **template-full**: lean = the smallest useful section set; full = a strict
   superset (every lean H2 appears in full, same order; full only adds). Every section carries the
   Approach-A comment: WHAT, WHY (ending with a `Deep dive: <type>_companion.md section 3 (...)` pointer),
   ASK (2-4 questions), GOOD, WEAK, TRAP; tables add PRIORITY and ROW HINT with GOOD/WEAK example rows. A
   "How to fill this in" preamble opens each. Placeholders are quoted `"{{snake_case}}"`.
3. **guide**: when to use / when NOT to use, pick-a-variant, a self-gradable rubric, and named anti-patterns
   (family practice is six). Derived from the companion.
4. **example**: one fully worked instance, no placeholders, illustrative figures labeled, provenance
   frontmatter. For delivery-docs, chain on the shared "Saved Views for Dashboards" scenario and link the
   upstream/downstream siblings with `../<type>/` paths.
5. **meta.yaml**: the 20 fields; `related_templates` as an **inline** list (see gotcha 2); catalog_ref from
   the spec.
6. **history.md**: open at 0.1.0 with the research date.

## Phase 3.5: Machine pre-read

Two report-only lints. Neither is in CI and neither blocks anything, because both have a legitimate-usage
rate too high to gate on. They run in seconds and their output is an input to phase 4.

```
python tools/lint-number-provenance.py <type>              # numbers and proper nouns vs the research log
python tools/lint-unsourced-confidence.py <type> --uncited # frequency and superlative claims, uncited first
```

**Why before the review and not instead of it.** The library's dominant defect class is a plausible
specific claim that no logged source supports, and the four-lens review finds these reliably but
expensively, by reading everything. These lints do the enumeration mechanically so the lenses spend their
attention judging rather than hunting. `lint-unsourced-confidence` was calibrated against all 19 shipped
bundles and, on its first run, found two in the merged `adr` bundle: a failure mode ranked "the single most
common substantive failure" in two files with no frequency measurement anywhere in its log, and a write-only
phenomenon called "universally acknowledged" when that log records both relevant sources as unretrieved.

**Neither output is a defect list.** A flagged line is a candidate. `lint-number-provenance` cannot tell
whether a matched log string actually supports the sentence, and `lint-unsourced-confidence` cannot tell a
sourced frequency claim from an unsourced one, because whether a cited source *measured* the frequency is
the judgement phase 4 exists to make. Fix a confirmed one by **deleting the claim or labelling it honestly,
never by hunting for a citation that would justify it** (the `review-finds-unsourced-confidence` memory).

## Phase 4: Adversarial four-lens review

Run a Workflow of four parallel sonnet lenses over the drafted bundle:

- **citation-support**: every companion claim vs the research log's `Supports:` clause; any quote vs the
  quotable list; contested claims flagged; unread sources carry no claim.
- **dod-family-conformance**: methodology DoD items the gate does not cover (guidance-comment grammar,
  11-section skeleton, guide shape, example quality) + the family contract (including any shared-example
  rule).
- **accuracy-teaching-point**: historical/conceptual claims vs the research log; the teaching points
  accurate and consistent across companion/guide/example.
- **chaining-consistency**: the example internally sound and consistent with its sibling examples;
  instantiates every template section; no placeholders.

Each returns structured findings (`{severity, file, location, issue, fix}`). Use `model:'sonnet'`.

**Give every lens exactly two files to read for its standards: [`review-standards.md`](review-standards.md)
and its family contract.** The brief states what the eleven gate checks and the CI steps have already
proved, so a lens does not re-count files, re-follow links or re-hunt placeholders; it names the seven
defect classes no machine catches; and its lens table assigns each lens only the bundle files it needs, so
the bundle is not read four times over. It also supersedes `design-spec.md` section 13 as the Definition of
Done, because that section names CI scripts and a contract path the build never adopted.

## Phase 5: Apply findings + re-verify

**Every finding is a claim; verify it against the source before applying.** The review reliably catches
real defects and occasionally proposes a fix that is wrong (e.g. a "renumber the References heading" fix
that would break check E's `## References` split). Apply the real ones, reject the wrong ones with a
reason, then re-run check E on the companion.

## Phase 6: Gate + land

```
git add templates/<type>                          # BEFORE the link gate (gotcha 1)
python tools/check-bundles.py <type>              # all 11 checks
python tools/gen-manifest.py                       # regenerate manifest.json
python tools/gen-manifest.py --check               # freshness + README marker
python tools/check-links.py                        # all relative links resolve
```

Then: bump the README `<!-- bundle-count: N -->` marker and prose count, add the bundle to the README
family table and the layout tree; update STATE.md (bundle count, family membership) and
`buildout-specs.md`'s progress table. Branch off `origin/main`, PR, let CI pass (no admin merge), stop for
the maintainer read at the family boundary (batch review), then merge and pull. Update the progress table.

---

## Gotchas (each cost a CI round-trip or a rework pass; see the `bundle-gate-verification-gotchas` memory)

1. **The link gate only scans git-tracked files.** A pre-commit run over an untracked new bundle is a
   FALSE GREEN. `git add templates/<type>` first. Cross-bundle links need `../<other-type>/`.
1a. **Building type X breaks every `future:X` elsewhere in the library.** Since 2026-09-04 check I fails a
   `future:` reference whose target is built, so the PR that lands a bundle must also sweep the sibling
   metas that were waiting on it: `grep -rn "future:<type>" templates/*/*_meta.yaml` and drop the prefix.
   The check exists because three earlier sweeps were done by hand and none of them held.
2. **check I drops the first entry of a *block-style* `related_templates` list** (a regex `\s*` swallows
   the newline). Use an **inline** list `[a, b, c]` so every entry is validated.
3. **Citation numbering: get it right on the first write.** No `12b`-style non-integer ids (the gate's
   `(\d+)` regexes cannot parse them); no combined entries (two sources under one number, methodology 6.1);
   never desync the anchor id `id="ref-N"` from the display number `</a>[N]`. Do not hand-renumber with
   fragile string-replace scripts; if you must, verify `display == anchor` for every entry.
4. **A new family needs its contract adopted before its members** or check K blocks them (well, passes with
   a "no contract" note, but the members are then unenforced). Contract PR first.
5. **Parallel PRs that both edit STATE.md/README/manifest conflict.** Build serially, or rebase the second
   PR (30-second STATE.md "Last updated" reconciliation).
6. **`## References` must stay literally that** - check E splits the companion body on that exact heading;
   numbering it breaks the split and floods the bare-citation check.
7. **Never write a backtick inside a workflow prompt.** The prompts in
   [`build-bundle.js`](../../.claude/workflows/build-bundle.js) live in backtick-delimited template
   literals, so marking up a field name the way you would in markdown closes the literal and the Workflow
   runtime refuses to load the script. Use double quotes. **`node --check` does not catch this**: on
   2026-08-05 a two-word edit of exactly this kind shipped through a green PR, passed `node --check` with
   exit 0, and died at load, because the stray backticks rebalanced into expressions Node tolerates.
   [`check-workflow-prompts.py`](../../tools/check-workflow-prompts.py) now gates the shape in CI, and says
   in its own output that it cannot prove the script loads. **Only invoking the workflow proves that**,
   which is the same lesson CRLF taught: a script can be correct and not loadable, and reading it again
   will never tell you which.

## check E verification snippet (run after drafting the companion)

```python
import re
s=open('templates/<type>/<type>_companion.md',encoding='utf-8').read()
body=s.split('## References',1)[0]
IN=re.compile(r"\(#ref-(\d+)\)"); AN=re.compile(r'id="ref-(\d+)"'); BARE=re.compile(r"(?<!\[)\[(\d+)\](?!\()")
anchors=set(AN.findall(s)); inline=set(IN.findall(body)); cited=set(IN.findall(s))
disp=re.findall(r'<a id="ref-(\d+)"></a>\[(\d+)\]', s)
print("dangling",sorted(inline-anchors,key=int),"padded",sorted(anchors-cited,key=int),
      "bare",sorted(set(BARE.findall(body)),key=int),
      "display!=anchor",[(a,d) for a,d in disp if a!=d])
```

All four lists must be empty.

## Model routing (per `~/.claude/rules/model-routing.md`)

Research and review fan-outs: `sonnet` (rubric-based / research-with-judgment is sonnet's lane; a 4-6 way
fan-out drops one tier from the opus a single adversarial-verify agent would get). The main loop
(drafting, synthesis, re-verifying findings) is the frontier model. Reserve haiku for pure read-only
scouting if delegated. Do not frontier-verify-frontier.
