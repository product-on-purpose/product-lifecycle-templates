# Bundle pipeline: the reusable per-bundle runbook

> **This runbook is executable.** [`.claude/commands/build-bundle.md`](../../.claude/commands/build-bundle.md)
> drives it, and [`.claude/workflows/build-bundle.js`](../../.claude/workflows/build-bundle.js) runs its three
> stages: `{stage:"research", type, dimensions}`, `{stage:"draft", type, family}`, and
> `{stage:"review", type, family}`, with `sizes: ["lean"]` added to draft and review for a single-size
> bundle. The script enforces in a schema what this document states in prose - the
> retrieval enum, source ownership, grounded findings - so an agent cannot return a quote without having
> claimed it read the body. The prose here remains the authority; the script is one way of executing it.

The executable process for building one Tier-1 bundle to the best-in-class, source-referenced standard,
proven on `sdd` and `product-backlog` (2026-07-20/21). This operationalizes methodology section 8 and the
buildout-plan pipeline, and it is the durable reference a future session (or an autonomous loop) follows.

**The governing principle:** the gate proves a bundle's *structure*, never that its citations *support*
their claims. Three times in one session, every citation defect (combined entries, misattributions, quotes
not in the source) was green in CI and caught only by the adversarial review. So this pipeline's non-
negotiable is the review, not the gate. Never ship a bundle that has not passed the four-lens review with
its findings applied and re-verified.

Per-bundle cost was estimated at 0.6-1M tokens; that estimate was never measured and was low by roughly
10 to 20 times. Measured cost, from the fourteen builds captured end to end, is roughly 6M to 12M weighted
token-equivalents per bundle, or $12 to $41 at API list rates, and the model that drafts is most of the
spread: launch-coordination-checklist, the first build through this runbook's own workflow, cost 7,108,920
and $14.22 with every agent on Sonnet as pinned; issue-log, the second, cost $14.29 for the same 15
research, drafting and review agents ($16.76 with the three agents that swept the counts at landing); and
definition-of-ready, the third and the first single-size build, cost $11.69 for its 15 ($13.89 with its
sweep), its drafting stage the cheapest of the three, which was read at the time as the effect of writing
one template, not two. announcement-internal-comms, the fourth and the second single-size build, cost 8,495,731 weighted and
$16.99 for its 15 agents; change-request, the fifth, cost 7,203,075 weighted and $14.41 for its 15 agents.
**This time the single-size build was the dearer one**: announcement-internal-comms' drafting stage cost
MORE than change-request's two-template drafting, $8.58 against $5.78, mostly cache reads, so the number
of variants is not by itself a predictor of cost. change-log, the sixth, cost 8,472,610 weighted and $16.95
for its 15 agents, and its two-template drafting stage cost $8.14, close to announcement-internal-comms'
single-template $8.58, which points the same way. production-readiness-review, the seventh, cost 7,876,892 weighted
and $15.75 for its 15 agents, its two-template drafting $8.35. project-brief, the eighth, cost 7,120,610 weighted
and $14.24 for its 15 agents, its two-template drafting $5.72. experiment-design-doc, the ninth, cost 6,674,388
weighted and $13.35 for its 15 agents, its two-template drafting $5.90. experiment-readout, the tenth, cost
6,480,996 weighted and $12.96 for its 15 agents, its two-template drafting $5.06; tracking-plan, the eleventh,
cost 7,440,790 weighted and $14.88 for its 15 agents, its two-template drafting $8.57. problem-statement, the
twelfth, cost 10,533,753 weighted and $21.07 for 19 agents, the usual 15 plus a three-agent gap-fill research
pass after drafting and one fact check of that gap-fill, its two-template drafting $9.06 *(corrected
2026-10-21: this read 9,987,114 and $19.97 for 18, before the generator counted agents run through the Agent
tool)*. business-continuity-plan, the thirteenth, cost
10,284,679 weighted and $20.57 for its 15 agents, its two-template drafting $10.10. data-dictionary, the
fourteenth, cost 8,859,179 weighted and $17.72 for 16 agents, the usual 15 plus a seventh research dimension,
its two-template drafting $7.71. use-case-specification, the fifteenth, cost 8,370,585 weighted and $16.74 for
its 15 agents, its two-template drafting $7.77. trade-study, the sixteenth, cost 10,479,257 weighted and
$20.96 for 16 agents, the usual 15 plus a seventh research dimension, its two-template drafting $10.47.
test-strategy, the seventeenth, cost 16,344,533 weighted and $35.11 for 18 agents: the usual 15 plus a seventh
research dimension in workflows, then an Opus head writer ($10.20) and a Sonnet fix agent ($4.71) through the
Agent tool. Its single-template drafting cost $9.17. positioning-statement, the eighteenth, cost 13,476,852
weighted and $30.25 for 18 agents: the usual 15 in workflows, then an Opus research retry ($3.49), an Opus head
writer ($7.67) and a Sonnet fix agent ($2.84) through the Agent tool. Its single-template drafting cost $6.86.
**The step up is the work run outside the workflows**: from their workflow agents alone, the two would read
$20.20 and $16.25, inside the usual range. design-brief, the nineteenth, cost 11,563,997 weighted and $25.38
for 16 agents: the usual 15 in workflows, then an Opus head writer ($8.89) through the Agent tool, so its
workflow agents alone read $16.49. Its two-template drafting cost $6.66. user-research-plan, the twentieth, cost 14,890,444 weighted and $32.47 for 16 agents: the usual 15 in workflows, then an Opus head writer ($8.99) through the Agent tool, so its workflow agents alone read $23.48. Its two-template drafting cost $15.21, the most of any build drafted on Sonnet, and the companion's agent alone cost $9.86, most of it cache reads. Meanwhile test-summary-report (12,123,040, $41.22) and spike-report (9,881,764, $33.21) ran per-bundle scripts that
pinned no model on drafting, which therefore ran on Opus. Each is the whole build, 3 runs; none includes the
orchestrator's own spend.
**A report counts only the agents that built the bundle** (the maintainer's rule, 2026-09-29). Agents
labelled `<bundle>/sweep:N`, which sweep the repository's counts when a bundle lands, go in a separate
`landing_sweep` line of that bundle's report and never into its totals. Whether a landing needs sweep agents
depends on how its counts were swept, not on the bundle, so folding them in made builds incomparable. That is
why issue-log's and definition-of-ready's reports read $14.29 and $11.69, and why the with-sweep figures
above are notes rather than headlines. **Agents a build runs through the Agent tool count too** (since
2026-10-21), but only when the same session also built that bundle in a workflow; a landing sweep run that way
is recognised by its prompt's subject line and kept out of the totals like a labelled one. See the 2026-10-21
correction in [ADR 0056](decisions/0056-build-cost-is-measured-and-ingestion-is-separate-from-verification.md).
Weighted means input x1.0, cache write x1.25, cache read x0.1, output x5.0.
*(Corrected 2026-09-22: this paragraph read "21M to 25M", from a generator that counted each API response
two to three times. See the Correction in
[ADR 0056](decisions/0056-build-cost-is-measured-and-ingestion-is-separate-from-verification.md).)* See
[`bundle-builds/INDEX.md`](../../bundle-builds/INDEX.md) for the per-bundle reports. Realistic pace: 1-2
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

### The terms rule (since 2026-10-25)

**No agent reads a page on a site whose terms of use forbid automated reading.** The ban covers a fetch and
a read from the source cache alike. The maintainer set this rule on 2026-10-25. The sites stay citable:
the maintainer reads a needed page by hand, and the build checks every quote against that copy.

**Check a site's terms before the first read of any page on it, including a read from the cache.** A
site's own terms page, and any licence statement it links to, is the one automated read the rule allows.
Reading it is how a site's status is learned, so the rule cannot forbid it. Two slips on 2026-10-25 read
cached pages from nngroup.com and measuringu.com before their terms were checked. Neither site turned out
to bar reading, but the order was wrong.

**What counts as a bar.** A clause that forbids automated access, crawling, scraping or retrieval is a bar.
A clause that forbids only copying, reproducing or mirroring content is not a bar on reading. An exception
written into the clause itself counts. GitLab's Website Terms of Use bar retrieval "unless otherwise
permitted under applicable content licensing permissions", and the GitLab handbook and docs carry a
Creative Commons BY-SA 4.0 licence on every page, so both stay readable. A site owned by another company is
governed by its own terms: Mind the Product belongs to Pendo, but its own terms carry no such clause.

**No workaround.** No proxy, alternate client or second model is used to get past a block, a challenge or a
terms bar. A second model fetching the page is the same automated read with one more step. A retired
government page may be read through the Internet Archive's Wayback Machine.

**The excluded sites, as of 2026-10-26.** Each clause below was checked against the raw text of the site's
own terms page. A site not on this list is not cleared by its absence; check it before its first read.

| Site | The clause, verbatim | Terms page |
|---|---|---|
| Substack and every newsletter it hosts, including `lennysnewsletter.com`, `productcompass.pm`, `elenaverna.com`, `news.aakashg.com` and `leahtharin.com` | "“Crawls,” “scrapes,” or “spiders” any page, data, or portion of Substack (through use of manual or automated means);" | `<newsletter>/tos` |
| `baymard.com` | "It is explicitly prohibited to use any automated extracting, processing, scraping, or reverse-engineering methods in connection with the Services and on our website." | `https://baymard.com/terms-and-conditions` |
| `anthropic.com` | "To crawl, scrape, or otherwise harvest data or information from our Services other than as permitted under these Terms." | `https://www.anthropic.com/terms` |
| `winningbydesign.com` | "Develop, support, or use software, devices, scripts, robots or another means to scrape the Service;" | `https://winningbydesign.com/terms-and-conditions/` |
| `pendo.io` | "Systematic retrieval of data or other Content to create or compile, directly or indirectly, a collection, database or directory without written permission from Pendo is prohibited." | `https://www.pendo.io/legal/terms-of-use/` |
| `miro.com` | "scrape, data mine, reverse engineer, decompile, disassemble or seek to access the source code or non-public APIs to or unauthorized data from the Service" | `https://miro.com/legal/terms-of-service/` |
| `evidentlyai.com` | "Use any robot, spider, or other automatic device, process, or means to access Service for any purpose, including monitoring or copying any of the material on Service." | `https://www.evidentlyai.com/terms` |
| `productplan.com` | "Use automated tools to scrape, crawl, or extract content without permission" | `https://www.productplan.com/terms` |
| `forgetthefunnel.com` | "You are not permitted to use, or cause others to use, any automated system or software to extract content or data from our Website for commercial purposes." | `https://forgetthefunnel.com/terms-of-use-license` |
| `askable.com` | "Use any automated tool, bot, scraper, crawler, spider, or similar technology to access, extract, or index any content from the Website;" | `https://www.askable.com/legal/terms-of-use` |
| `koji.so` | "Use automated means to access our Services without our permission" | `https://www.koji.so/terms` |
| `entropik.io` | "You agree not to access or attempt to access any content available on the Website by any means other than through the interface that is provided by us." | `https://www.entropik.io/terms-of-use` |
| `getwhy.io` | "...download Insights or other content from the Services through the use of any engine, software, tool, agent, device or mechanism (including spiders, robots, crawlers, data mining tools or the like)..." | `https://www.getwhy.io/terms-of-service` |
| `about.gitlab.com` | "Using any process or device (automated or otherwise) to retrieve, index, “data mine”, “scrape”, or in any way reproduce the presentation of this website or its Content, unless otherwise permitted under applicable content licensing permissions." No content licence was found on this site, unlike the handbook and docs. | `https://handbook.gitlab.com/handbook/legal/policies/website-terms-of-use/` |

**Reading an excluded page by hand.**

1. A research agent that wants a page on an excluded site does not open it. It lists the page under
   `not_read_under_terms`, with what the build needs from it.
2. The orchestrator gives the maintainer one short list: each page's URL and what the build needs from it.
3. The maintainer opens each page in a browser and pastes its text into a gitignored working folder. The
   copy is never committed, and never put in the source cache.
4. The orchestrator checks every quote against that copy before the quote enters the research log.
5. The log entry keeps the `fetched-and-verified` token and says how the page was read, for example
   `**fetched-and-verified, read by hand by the maintainer on 2026-10-26.**` The research-log check
   accepts a qualifier around the token.
6. A page the maintainer does not read goes in the log's `## Pages not read under the terms rule` section,
   described in phase 2. No claim rests on it.

**Earlier builds.** *(Recorded 2026-10-26.)* No build before 2026-10-25 checked terms. The committed
research logs hold 57 `fetched-and-verified` entries on the sites above, across 15 bundles: 34 on
Substack-hosted newsletters, 15 on ProductPlan, 3 on Koji, 2 on Pendo, 2 on about.gitlab.com and 1 on
Miro. The maintainer chose to leave them as recorded. A later revision that needs one of those pages again
reads it by hand.

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

**Pages not read under the terms rule.** A page the build wanted on an excluded site, and that the
maintainer did not read by hand, goes in a `## Pages not read under the terms rule` section after the
sources. Write one bullet per page: its URL, the site's clause in a few words, and what the page would have
supported. No claim rests on it, and it carries no number and no retrieval token. The check parses only
sections whose heading contains the word "source", so this heading must not contain it. The section exists
so a reader can see what the bundle did not read, and why.

**What the check does not do:** it proves the fields are present, never that a retrieval status is truthful,
that a `Supports:` clause is accurate, or that a quoted phrase appears in the source. Those are phase 4's
job, and the check says so in its own output on every run.

## Phase 3: Draft (in this order)

1. **companion** (`<type>_companion.md`): 11-section skeleton (methodology section 5), dual-reader, every
   non-obvious claim cited inline `[[n]](#ref-n)`. **Number each reference with the research log's own
   number, one source per entry**, so `[n]` means the same source in both files; a log entry the companion
   does not cite is simply absent, which leaves a gap in the numbering and is correct. *(Corrected
   2026-09-23: this read "contiguously 1..N", which contradicted the build workflow's instruction to cite by
   the log's numbering; `runbook` and `issue-log` already followed the workflow.)* Only quote a phrase the research log lists as a verbatim quotable for a fetched-and-verified
   source. Reference entries: `<a id="ref-n"></a>[n] Author. "[Title](url)." ... [tier]`, with honest
   retrieval qualifiers on unread/contested sources. Verify with the check-E snippet below before moving
   on.
2. **template-lean** and **template-full**: lean = the smallest useful section set; full = a strict
   superset (every lean H2 appears in full, same order; full only adds). Every section carries the
   Approach-A comment: WHAT, WHY (ending with a `Deep dive: <type>_companion.md section 3 (...)` pointer),
   ASK (2-4 questions), GOOD, WEAK, TRAP; tables add PRIORITY and ROW HINT with GOOD/WEAK example rows. A
   "How to fill this in" preamble sits inside each variant's opening comment block, after the frontmatter.
   Placeholders are quoted `"{{snake_case}}"`.
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
python tools/gen-bundle-build-report.py --ingest       # measured build cost -> bundle-builds/
```

Then: bump the README `<!-- bundle-count: N -->` marker and prose count, add the bundle to the README
family table and the layout tree; update STATE.md (bundle count, family membership) and
`buildout-specs.md`'s progress table. Branch off `origin/main`, PR, let CI pass (no admin merge), stop for
the maintainer read at the family boundary (batch review), then merge and pull. Update the progress table.
The PR body says `Closes #N` for the type's `build-candidate` issue: since 2026-10-10 every proposed bundle
has one (filter on `label:build-candidate`), and the merge closes it as completed on the day it lands.
The build-report ingest must run here, on the machine that ran the build, because it reads per-agent
transcripts under `~/.claude/projects/` that are machine-local and are pruned eventually; the resulting
report is committed with the bundle.

**Your bundle gets published, and one site guard can fail on its prose.** Landing a bundle adds a page
to <https://product-on-purpose.github.io/product-lifecycle-templates/>, generated from the guide, the
companion and the templates by `scripts/gen-site.mjs`. Nothing is hand-listed and there is nothing to
add, but `site.yml` runs an honesty gate over the generated page, and **it fails the site build on a
sentence that calls the bundle proven, verified or validated**. It is not a word filter: a hit must be
un-negated, about the bundle rather than about the document type, and inside a fenced block only when an
explicit meta-phrase ("this bundle", "this template") is present, so a worked example whose fictional
tester "verified" a fix is safe. Writing that *this bundle* has been proven is not. The deliberate
escape is an `<!-- honesty-ok: ... -->` comment, which shows up in the diff and has to be justified.
Note this fails `site.yml`, not the content gate, so a green `run-gate.py` does not clear it. Route
parity allows a new route, so adding a bundle cannot break the site that way. Full explanation:
[`docs/explanation/the-site.md`](../explanation/the-site.md).

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
