export const meta = {
  name: 'build-bundle',
  description: 'Research fan-out or four-lens review for one template bundle, with source ownership and scoped lens reads',
  whenToUse: 'Invoked by the build-bundle skill. Pass {stage:"research", type, dimensions} or {stage:"review", type, family}.',
  phases: [
    { title: 'Research', detail: 'one sonnet agent per dimension, each owning its sources' },
    { title: 'Review', detail: 'four sonnet lenses, each reading only its own files' },
  ],
}

// Two stages, one file, because they share the source-ownership and finding schemas but are separated in
// time by main-loop drafting. A workflow runs to completion and cannot pause for that, so the skill calls
// this twice. A phases entry with no matching phase() call simply does not appear in the progress tree.
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

throw new Error(`args.stage must be "research" or "review", got ${JSON.stringify(stage)}`)
