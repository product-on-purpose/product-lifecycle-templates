export const meta = {
  name: 'build-bundle',
  description: 'Research, draft or review one template bundle: source ownership, files written by agents rather than returned, and scoped lens reads',
  whenToUse: 'Invoked by the build-bundle skill. Pass {stage:"research", type, dimensions}, {stage:"draft", type, family}, or {stage:"review", type, family}.',
  phases: [
    { title: 'Research', detail: 'one sonnet agent per dimension, each owning its sources' },
    { title: 'Draft', detail: 'seven files in dependency order; each agent writes its file and returns a summary' },
    { title: 'Review', detail: 'four sonnet lenses, each reading only its own files' },
  ],
}

// Three stages, one file, sharing the source-ownership and finding schemas. They are separated in time by
// main-loop work the orchestrator must do itself: synthesising the research log after `research`, and
// verifying findings against their sources after `review`. A workflow runs to completion and cannot pause
// for that, so the skill calls this three times. A phases entry with no matching phase() call simply does
// not appear in the progress tree.
//
// args may arrive as a real object or as a JSON STRING, depending on how the caller serialised it. The
// first run of this script died on exactly that: every field read as undefined and the script threw
// "args.type is required" while the caller had supplied it. Parse defensively rather than making every
// future invocation remember which form to use.
let input = args
if (typeof input === 'string') {
  try {
    input = JSON.parse(input)
  } catch (e) {
    throw new Error(`args was a string but not valid JSON: ${e.message}`)
  }
}
input = input || {}

const stage = input.stage
const type = input.type
if (!type) throw new Error('args.type is required (the bundle handle, e.g. "business-case")')

const RUNBOOK = 'docs/internal/bundle-pipeline.md'
const BRIEF = 'docs/internal/review-standards.md'

// Honest retrieval is the library's central quality claim, so the schema ENFORCES the enum rather than
// asking for it in prose. An agent cannot return a quote without having claimed it read the body, and the
// research-log contract check will later fail anything that slipped.
const RESEARCH_SCHEMA = {
  type: 'object',
  required: ['dimension', 'owned_sources', 'referenced_sources', 'findings'],
  properties: {
    dimension: { type: 'string' },
    owned_sources: {
      type: 'array',
      description: 'Sources THIS agent read in full. Only these may carry quotables.',
      items: {
        type: 'object',
        required: ['identity', 'url', 'tier', 'retrieval_status', 'supports'],
        properties: {
          identity: { type: 'string', description: 'Author and title, never one without the other' },
          url: { type: 'string' },
          tier: { type: 'string', enum: ['primary', 'standard', 'practitioner', 'vendor'] },
          retrieval_status: {
            type: 'string',
            enum: ['fetched-and-verified', 'url-confirmed-not-read', 'not-retrieved'],
          },
          from_cache: { type: 'boolean', description: 'True if the body came from source-cache rather than a fetch' },
          supports: { type: 'string', description: 'The specific claim this source supports' },
          quotable: {
            type: 'array',
            description: 'Verbatim phrases. ONLY for fetched-and-verified. Never reconstruct from memory.',
            items: { type: 'string' },
          },
        },
      },
    },
    referenced_sources: {
      type: 'array',
      description: 'Sources this agent needs but does NOT own: URL and the need, no body read, no quotes.',
      items: {
        type: 'object',
        required: ['url', 'what_is_needed'],
        properties: { url: { type: 'string' }, what_is_needed: { type: 'string' } },
      },
    },
    findings: { type: 'string', description: 'The dimension write-up, every claim tied to an owned source' },
    contested: {
      type: 'array',
      description: 'Claims where sources genuinely disagree. Flag rather than resolve.',
      items: { type: 'string' },
    },
    not_found: { type: 'string', description: 'What was searched for and not found. State it; do not fill the gap.' },
  },
}

const FINDINGS_SCHEMA = {
  type: 'object',
  required: ['lens', 'findings'],
  properties: {
    lens: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['severity', 'file', 'location', 'issue', 'fix'],
        properties: {
          severity: { type: 'string', enum: ['blocking', 'major', 'minor'] },
          file: { type: 'string' },
          location: { type: 'string', description: 'Line number or exact quoted phrase. A finding without one is not actionable.' },
          issue: { type: 'string' },
          fix: { type: 'string' },
          grounds: { type: 'string', description: 'The log line or file line that proves it. Required for any claim of fact.' },
        },
      },
    },
    checked_nothing_else: {
      type: 'boolean',
      description: 'True if you confined yourself to your assigned files and did not re-verify what CI proves.',
    },
  },
}

const OWNERSHIP_RULE = `
SOURCE OWNERSHIP. Other agents are researching other dimensions of this same bundle in parallel, and you
will converge on the same canonical sources unless you follow this.

  1. Before ANY fetch, run: python tools/source-cache.py get <url>
     Exit 0 = hit (body returned, no network), 1 = miss, 2 = stale (>14 days, re-fetch).
     On a miss: fetch, then python tools/source-cache.py put <url>.
  2. A source you read in full goes in owned_sources, with retrieval_status fetched-and-verified and any
     verbatim phrases in quotable. Set from_cache honestly.
  3. A source you need but did not read in full goes in referenced_sources: the URL and what you need from
     it. DO NOT read its body. Another dimension likely owns it and will supply the extract. This is the
     rule that stops the same page being read five times.
  4. NEVER fabricate a quote or reconstruct one from memory. A phrase enters quotable only if you read it
     verbatim in the body. If you did not read the body, the status is url-confirmed-not-read at best and
     the source may support the EXISTENCE of a topic but no specific claim about it.
  5. State what you could not find. An honest gap is a finding; a plausible filler is a defect.
`

if (stage === 'research') {
  const dimensions = input.dimensions
  if (!Array.isArray(dimensions) || !dimensions.length) {
    throw new Error('args.dimensions must be a non-empty array for stage "research"')
  }

  phase('Research')
  log(`${type}: ${dimensions.length} dimension(s), source-ownership enforced`)

  const results = await parallel(
    dimensions.map((d, i) => () =>
      agent(
        `Research one dimension for the "${type}" template bundle in product-lifecycle-templates.

DIMENSION ${i + 1}: ${typeof d === 'string' ? d : d.prompt}

Read ${RUNBOOK} phases 1-2 for the research standard. Use real web retrieval.
${OWNERSHIP_RULE}
Return the schema. Your findings text is the raw material for one section of a research log, so tie every
claim to a source in owned_sources by identity. Flag genuine disagreement in contested rather than picking
a winner.`,
        {
          label: `research:${typeof d === 'string' ? d.slice(0, 24) : d.key}`,
          phase: 'Research',
          schema: RESEARCH_SCHEMA,
          model: 'sonnet',
          effort: 'medium',
        },
      ),
    ),
  )

  const ok = results.filter(Boolean)
  const owned = ok.flatMap((r) => r.owned_sources || [])
  const urls = owned.map((s) => s.url)
  const dupes = [...new Set(urls.filter((u, i) => urls.indexOf(u) !== i))]
  const quotable = owned.filter((s) => (s.quotable || []).length)
  const badQuotes = quotable.filter((s) => s.retrieval_status !== 'fetched-and-verified')

  log(`${ok.length}/${dimensions.length} returned, ${owned.length} owned source(s), ${dupes.length} owned twice`)
  if (badQuotes.length) log(`WARNING: ${badQuotes.length} source(s) carry quotables without fetched-and-verified`)

  // Reported, not silently deduped. Two dimensions owning one source is a synthesis decision: one log
  // entry per source, never combined, and the main loop picks which extract survives.
  return {
    stage: 'research',
    type,
    dimensions_returned: ok.length,
    dimensions_lost: dimensions.length - ok.length,
    doubly_owned: dupes,
    quotable_without_fetch: badQuotes.map((s) => s.identity),
    results: ok,
  }
}

if (stage === 'draft') {
  const family = input.family
  if (!family) throw new Error('args.family is required for stage "draft"')
  const b = `templates/${type}/${type}`

  // THE RULE THAT MAKES THIS WORTH DOING: every stage WRITES ITS FILE and returns only a summary. A
  // stage that returned its 600 lines of markdown through the schema would push the whole bundle through
  // the orchestrator's context and move nothing at all. The bulk stays on disk; only the handoff crosses.
  const HOUSE = `
YOU ARE WRITING A FILE, NOT ANSWERING A QUESTION. Use Write to create it at the exact path given, then
return the schema summarising what you wrote. Do not paste the file back in your return value.

READ FOR YOUR STANDARDS, and read nothing else unless these send you there:
  ${BRIEF}
  docs/internal/contracts/${family}.md

NON-NEGOTIABLE, and each has cost this library a defect:
  - NO em-dash or en-dash anywhere. Use " - ", or restructure. Ranges use plain hyphens. CI sweeps for this.
  - EVERY claim must be covered by a Supports: clause in ${b}_research-log.md. If the log does not carry
    it, CUT IT. Do not go looking for a source that would justify a sentence you have already written.
  - ONLY a source marked fetched-and-verified may be quoted. Quote verbatim from the log's Quotable list.
  - The log's not-retrieved entries are QUARANTINED. Nothing may rest on them, and any figure the log
    marks unverified must not appear as fact.
  - Wrap prose at about 100 columns, matching the rest of the library.`

  phase('Draft')
  log(`${type}: drafting 7 files in dependency order, each stage reading the last from disk`)

  // One item, five sequential stages. pipeline() is the honest expression of a dependency chain: the
  // companion is built from the log, the templates from the companion, the guide from both, and so on.
  const [result] = await pipeline(
    [type],
    () =>
      agent(
        `Draft the COMPANION for the "${type}" bundle: ${b}_companion.md
${HOUSE}

Read ${b}_research-log.md in full. It is the only source of fact you have, and its "Honest framing"
section states what this bundle exists to say.

The companion carries all 11 sections of methodology section 5, in order, with ONE Anatomy subsection per
template section. An inapplicable section says so in one line rather than being dropped. It is the deep
background: explanatory, not procedural. Procedure belongs in the guide.

End with a "## References" heading (that exact wording, no section number: the gate splits on it) listing
every source you cited, anchored so [[N]](#ref-N) links resolve. Cite by the log's own numbering.`,
        { label: 'draft:companion', phase: 'Draft', schema: {
          type: 'object', required: ['sections', 'teaching_points', 'refs_cited'],
          properties: {
            sections: { type: 'array', items: { type: 'string' }, description: 'H2 headings written, in order' },
            teaching_points: { type: 'array', items: { type: 'string' }, description: 'The claims the templates and guide must stay consistent with' },
            refs_cited: { type: 'array', items: { type: 'integer' }, description: 'Log entry numbers cited' },
            claims_cut: { type: 'array', items: { type: 'string' }, description: 'Claims you wanted to make and cut because the log did not support them. An empty list here is suspicious.' },
          } }, model: 'sonnet', effort: 'high' },
      ),
    (companion) =>
      agent(
        `Draft BOTH TEMPLATE VARIANTS for "${type}": ${b}_template-lean.md and ${b}_template-full.md
${HOUSE}

Read ${b}_companion.md, which you must stay consistent with. Its teaching points are:
${(companion?.teaching_points || []).map((t) => `  - ${t}`).join('\n')}

The build spec's section list for this type is in docs/internal/buildout-specs.md. Follow it.

ONE AGENT WRITES BOTH because of the nesting rule, which a split would break: the lean variant's H2
sections must be a STRICT ORDERED SUBSET of the full variant's, with shared sections keeping the same
name and the same order. Check C enforces this and it is the easiest thing here to get wrong.

Every section of every variant carries the Approach A guidance comment in an HTML comment: WHAT, WHY
with a companion pointer, ASK, GOOD, WEAK, TRAP, plus PRIORITY and ROW HINT for table sections. Open each
variant with a "How to fill this in" preamble stating the N/A rule and the self-grade step.

Placeholders are {{snake_case}} and consistent across both variants.`,
        { label: 'draft:templates', phase: 'Draft', schema: {
          type: 'object', required: ['lean_sections', 'full_sections'],
          properties: {
            lean_sections: { type: 'array', items: { type: 'string' } },
            full_sections: { type: 'array', items: { type: 'string' } },
            placeholders: { type: 'array', items: { type: 'string' } },
            nesting_verified: { type: 'boolean', description: 'You checked lean is an ordered subset of full, by reading both back' },
          } }, model: 'sonnet', effort: 'high' },
      ),
    (templates) =>
      agent(
        `Draft the GUIDE for "${type}": ${b}_guide.md
${HOUSE}

Read ${b}_companion.md and ${b}_template-full.md.

The guide is PROCEDURAL where the companion is explanatory. It carries: when to use; when NOT to use;
how to pick a variant; a self-gradable rubric; and at least six named anti-patterns.

THE RUBRIC IS THE PART MOST OFTEN GOT WRONG. Brief section 3 states its five house rules. In particular:
cells describe EVIDENCE, NOT COUNTS. The test for a cell is "could someone satisfy this without improving
the document?" If yes, it is written wrong. And the threshold above the table is stated as a CONSEQUENCE,
not a grade: what happens to the reader or the work below the line.

The variants are: lean ${JSON.stringify(templates?.lean_sections || [])} and full
${JSON.stringify(templates?.full_sections || [])}. If any rubric row grades a section a variant does not
ship, you MUST carry a scope table naming, per variant, which rows apply, the maximum, and the threshold.
tools/check-rubric-scope.py enforces the arithmetic and demands that table.`,
        { label: 'draft:guide', phase: 'Draft', schema: {
          type: 'object', required: ['rubric_rows', 'threshold'],
          properties: {
            rubric_rows: { type: 'integer', description: '6 to 12' },
            threshold: { type: 'string' },
            scope_table: { type: 'boolean', description: 'True if any row is variant-scoped and a scope table was written' },
            anti_patterns: { type: 'array', items: { type: 'string' }, description: 'At least six' },
          } }, model: 'sonnet', effort: 'high' },
      ),
    () =>
      agent(
        `Draft the WORKED EXAMPLE for "${type}": ${b}_example.md
${HOUSE}

Read ${b}_template-full.md, and read at least three sibling examples in templates/*/[a-z]*_example.md to
match the library's voice and to chain onto its shared scenario.

FOUR OBLIGATIONS, each of which has been violated before:

  1. A GENUINE worked artifact. No placeholders survive: check D fails on {{any}}.
  2. A DIFFERENT SCENARIO from the template's own guidance comments, and not a reworded one. The reuse
     survives swapping every noun, which is why a convention failed three times and a string check now
     enforces it. tools/check-example-independence.py fails a new bundle on its FIRST copied passage;
     this bundle is not grandfathered.
  3. CHRONOLOGICALLY POSSIBLE. It may only cite documents that existed when it is dated. Read the dates
     in the sibling examples you cite and make yours consistent. The one exception is the opening
     "> **Worked example.**" blockquote, which addresses the library's reader rather than the fictional
     author and may mention later documents.
  4. Its frontmatter carries provenance and a date, and illustrative figures are LABELLED as illustrative.

Read the family contract's shared-scenario rule before choosing your scenario. It may bind you to
specific existing artifacts.`,
        { label: 'draft:example', phase: 'Draft', schema: {
          type: 'object', required: ['scenario', 'dated'],
          properties: {
            scenario: { type: 'string' },
            dated: { type: 'string', description: 'The date in the example frontmatter, YYYY-MM-DD' },
            cites: { type: 'array', items: { type: 'string' }, description: 'Sibling examples cited, with their dates, so chronology is checkable' },
            independent_of_guidance: { type: 'boolean' },
          } }, model: 'sonnet', effort: 'high' },
      ),
    (example) =>
      agent(
        `Write the META and HISTORY for "${type}": ${b}_meta.yaml and ${b}_history.md
${HOUSE}

Read ${b}_companion.md, both templates, and tools/meta.schema.json. Copy the field set and shape from a
recent sibling meta such as templates/okrs/okrs_meta.yaml.

The family contract's section 2 constrains the values: family "${family}", its axis value, status beta,
and a legal size shape. Declare exactly the variants that exist on disk.

pairs_with must resolve against tools/known-skills.txt. VERIFY EACH ONE and claim only what is true of
this type. Do not assume a pairing exists; an empty list is a legitimate answer and a wrong pairing is a
gate failure.

related_templates should point at the siblings this type genuinely relates to. The example cites
${JSON.stringify(example?.cites || [])}, which is a good starting point.

The history records the current template_version with a dated entry. Check H requires one.`,
        { label: 'draft:meta', phase: 'Draft', schema: {
          type: 'object', required: ['variants', 'axis_value'],
          properties: {
            variants: { type: 'array', items: { type: 'string' } },
            axis_value: { type: 'string' },
            pairs_with: { type: 'array', items: { type: 'string' }, description: 'Verified against known-skills.txt, or empty' },
            version: { type: 'string' },
          } }, model: 'sonnet', effort: 'medium' },
      ),
  )

  log(`${type}: drafted. Run the gate and the two phase-3.5 lints next.`)

  return { stage: 'draft', type, family, meta: result }
}

if (stage === 'review') {
  const family = input.family
  if (!family) throw new Error('args.family is required for stage "review"')

  const b = `templates/${type}/${type}`
  // Scoped reads. Each lens gets only the files it needs, so the bundle is not read four times over.
  const LENSES = [
    {
      key: 'citation-support',
      files: [`${b}_research-log.md`, `${b}_companion.md`],
      owns: `Every companion claim against the log's Supports clause. Every quotation against that source's
quotable list. A source that is url-confirmed-not-read or not-retrieved carries NO specific claim and NO
quote. Contested claims must read as contested. Watch the log's NARRATIVE sections as closely as its source
entries: two fabricated quotations once survived a verification pass because they sat in the prose that
cited the entries rather than in the entries themselves.`,
    },
    {
      key: 'dod-family-conformance',
      files: [`${b}_template-lean.md`, `${b}_template-full.md`, `${b}_guide.md`, `docs/internal/contracts/${family}.md`],
      owns: `The Definition of Done items CI cannot see: guidance-comment grammar, the section skeleton, the
guide's rubric shape (brief section 3), and this family's own obligation from its contract. If rubric rows
are variant-scoped, the scope table governs and row markers do not.`,
    },
    {
      key: 'accuracy-teaching-point',
      files: [`${b}_companion.md`, `${b}_guide.md`, `${b}_example.md`],
      owns: `Historical and conceptual claims against the research log, and teaching points consistent across
all three files. The dominant defect class is a plausible specific that no logged source supports: a number,
a year, a named person, a frequency. The fix for a confirmed one is to DELETE it or LABEL it honestly, never
to hunt for a citation that would justify it.`,
    },
    {
      key: 'chaining-consistency',
      files: [`${b}_example.md`, `${b}_template-full.md`],
      owns: `The example internally sound, instantiating every template section, no placeholders, and
consistent with its sibling examples in templates/*/. It must be chronologically possible: it may only cite
documents that existed when it is dated, except inside the opening "> **Worked example.**" blockquote, which
addresses the library's reader rather than the fictional author. It must not be the template's own guidance
text reworded.`,
    },
  ]

  phase('Review')
  log(`${type}: 4 lenses, scoped reads, family ${family}`)

  const reviews = await parallel(
    LENSES.map((l) => () =>
      agent(
        `Adversarially review the "${type}" bundle in product-lifecycle-templates. You are the ${l.key} lens.

READ FIRST, and read nothing else for your standards:
  ${BRIEF}
  docs/internal/contracts/${family}.md

READ THESE BUNDLE FILES, and only these:
${l.files.map((f) => `  ${f}`).join('\n')}

YOU OWN:
${l.owns}

DO NOT re-verify anything the brief's section 1 lists as machine-proved. Eleven gate checks and the CI steps
have already settled file counts, placeholders, section nesting, link resolution, reference padding, YAML
validity, manifest agreement and em-dashes. If one were broken the branch would be red and there would be
nothing to review. Every token you spend re-checking those is a token not spent on the seven defect classes
in section 2, which is the only reason you exist.

Ground every finding: give a line number or an exact quoted phrase, and for any claim of fact give the log
line or file line that proves it. A finding without grounds will be rejected by the main loop, which
verifies each one against the source before applying it.

Return the schema. Set checked_nothing_else honestly.`,
        { label: `lens:${l.key}`, phase: 'Review', schema: FINDINGS_SCHEMA, model: 'sonnet', effort: 'high' },
      ),
    ),
  )

  const ok = reviews.filter(Boolean)
  const all = ok.flatMap((r) => (r.findings || []).map((f) => ({ ...f, lens: r.lens })))
  const ungrounded = all.filter((f) => !f.grounds)
  const order = { blocking: 0, major: 1, minor: 2 }

  log(`${ok.length}/4 lenses returned, ${all.length} finding(s), ${ungrounded.length} ungrounded`)

  return {
    stage: 'review',
    type,
    lenses_returned: ok.length,
    lenses_lost: 4 - ok.length,
    // Sorted, never filtered. Every finding is a CLAIM the main loop verifies against the source before
    // applying: the review reliably finds real defects and occasionally proposes a fix that is wrong.
    findings: all.sort((x, y) => (order[x.severity] ?? 3) - (order[y.severity] ?? 3)),
    ungrounded_count: ungrounded.length,
    strayed: ok.filter((r) => r.checked_nothing_else === false).map((r) => r.lens),
  }
}

throw new Error(`args.stage must be "research", "draft" or "review", got ${JSON.stringify(stage)}`)
