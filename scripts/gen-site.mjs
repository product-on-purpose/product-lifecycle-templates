#!/usr/bin/env node
// what-it-is:   the site content generator, and the honesty gate over its own output
// what-it-does: reads manifest.json, sections.json, the catalog and templates/, and writes one
//               Starlight page per bundle plus an index into site/src/content/docs/bundles/
// why:          site-s0-spec.md AC-1, AC-2 and AC-16 require every bundle to reach the site from
//               the tree with nothing hand-listed, and require the build to FAIL on a page that
//               calls a bundle proven
// used-by:      npm run gen and npm run prebuild in site/package.json; node scripts/gen-site.mjs --check
//
// gen-site.mjs - generate the Astro Starlight bundle pages from the repository's own tree.
//
// WHAT IT READS (clause 14.3, AC-2). Four inputs, all of them already generated from the
// templates by the Python tooling, which is why this script needs no YAML parser:
//   manifest.json            per-bundle catalog metadata, by tools/gen-manifest.py
//   sections.json            per-bundle section inventory, by tools/gen-sections.py
//   atlas/catalog-data.json  the research catalog (methodology / owner / stage)
//   templates/<id>/*.md      the bundle's own role files, read verbatim
//
// WHAT IT WRITES. Only into site/src/content/docs/bundles/, which is the single gitignored
// generated subpath (AC-3). Hand-authored narrative pages live in site/src/content/docs/ and
// are NEVER touched: this script does not know they exist and must not learn.
//
// WHY .mdx AND NOT .md. Measured 2026-09-20, not assumed. The same template excerpt was built
// both ways and the rendered <details> bodies were byte-identical but for whitespace, so a
// fenced template survives verbatim in either. .mdx wins because it carries components, which
// is what the role tabs need, and because every hand-authored page in this tree is already
// .mdx. The brace hazard that argued for .md is real only for UNFENCED content: across all 30
// bundles (re-checked at 31 on 2026-09-22) the guide files contain zero braces and zero tags, templates are always fenced, and
// the 1,907 tag-like strings in companions are <a id="ref-N"> citation anchors, which MDX
// treats as intrinsic elements. Nothing inlined here can open a JSX expression.
//
// WHY NO ROUTE MANIFEST. The donor emits none. scripts/check-route-parity.mjs reads a
// COMMITTED baseline snapshotted from a finished build, so a generator that wrote one would be
// grading its own homework. See docs/internal/site-s0-spec.md section 7.
//
// WHY NO REMARK PLUGIN. The donor needs one because it emits relative .md links inherited from
// three retired Python generators. This script authors every link it emits and emits
// base-absolute slugs directly, so there is nothing to repair at build time.
//
// Zero dependencies. Node ESM. UTF-8 and LF in, UTF-8 and LF out.
//
// Usage:
//   node scripts/gen-site.mjs            generate the pages
//   node scripts/gen-site.mjs --check    scan the GENERATED output for honesty violations (AC-16)

import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync, readdirSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join, resolve } from 'node:path';

import { BASE } from './site-base.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const TEMPLATES = join(ROOT, 'templates');
const OUT = join(ROOT, 'site', 'src', 'content', 'docs', 'bundles');

// The base is IMPORTED, never restated (clause 14.7, AC-5). An earlier draft kept a copy here
// and asserted it matched astro.config.mjs at startup; importing the single literal is strictly
// better, because one literal cannot disagree with itself and there is no assertion to forget.
const REPO = 'https://github.com/product-on-purpose/product-lifecycle-templates';
const GH_BLOB = `${REPO}/blob/main`;
const GH_EDIT = `${REPO}/edit/main`;

// Roles the site does NOT publish as pages. A link to one of these resolves to GitHub, because
// resolving it in-site would be a promise the build does not keep.
const UNPUBLISHED_ROLES = new Set(['companion', 'history', 'research-log']);

// ---------------------------------------------------------------- io helpers

const readText = (p) => readFileSync(p, 'utf8').replace(/\r\n/g, '\n');
const readJson = (p) => JSON.parse(readText(p));

function writeOut(path, content) {
  mkdirSync(dirname(path), { recursive: true });
  // Explicit \n throughout; Node does not translate line endings, and this repository has been
  // bitten more than once by a whole-file CRLF rewrite that no diff-based check can see.
  writeFileSync(path, content.replace(/\r\n/g, '\n'), 'utf8');
}

// ---------------------------------------------------------------- manifest model

/**
 * Every (format, size) a bundle actually ships, default format first.
 *
 * Ported from tools/mcp_server.py's variants(). A non-default format does NOT necessarily carry
 * every size - product-roadmap ships `go` and `themes` in `full` only - so enumerating the cross
 * product would invent two files that do not exist.
 */
function variants(bundle) {
  const out = (bundle.sizes_available || []).map((s) => [bundle.default_format || null, s]);
  for (const extra of bundle.additional_formats || []) {
    for (const s of extra.sizes || []) out.push([extra.id, s]);
  }
  return out;
}

/** The filename, per ADR 0028. The format segment is omitted for the default format. */
function variantFile(id, fmt, size, defaultFormat) {
  const stem = fmt === (defaultFormat ?? null) || fmt === null ? size : `${fmt}-${size}`;
  return `${id}_template-${stem}.md`;
}

const roleFile = (id, role) => join(TEMPLATES, id, `${id}_${role}.md`);

// ---------------------------------------------------------------- link rewriting

/**
 * Rewrite the link forms that appear in authored bundle prose so they resolve in a browser.
 *
 * Measured across all 30 guides, and re-checked at 31 on 2026-09-22, there are exactly four forms:
 *   ../<other>/                       another bundle's directory  -> that bundle's page
 *   ../<other>/<other>_guide.md       another bundle's guide      -> that bundle's page
 *   ../<other>/<other>_<role>.md      an unpublished role file    -> GitHub blob
 *   <id>_<role>.md                    a sibling role file         -> GitHub blob, or this page
 *   http(s)://...                     left alone
 *
 * This is the analog of the donor's rewriteInternalPaths, and it is the reason this repository
 * does not need the donor's 178-line remark plugin: the repair happens once, here, at authoring
 * time, rather than on every build against already-emitted bad links.
 */
function rewriteLinks(text, id, bundleIds) {
  return text.replace(/\]\(([^)\s]+)(\s+"[^"]*")?\)/g, (whole, url, title) => {
    const keep = title || '';
    if (/^(https?:|mailto:|#)/.test(url)) return whole;

    // ../<other>/ or ../<other>/<other>_<role>.md
    let m = url.match(/^\.\.\/([a-z0-9-]+)\/(?:([a-z0-9-]+)_([a-z-]+)\.md)?$/);
    if (m) {
      const [, other, , role] = m;
      if (!bundleIds.has(other)) return `](${GH_BLOB}/templates/${other}/${keep})`;
      if (!role || role === 'guide') return `](${BASE}/bundles/${other}/${keep})`;
      return `](${GH_BLOB}/templates/${other}/${other}_${role}.md${keep})`;
    }

    // <id>_<role>.md, a sibling of the file being read
    m = url.match(/^([a-z0-9-]+)_([a-z-]+)\.md$/);
    if (m) {
      const [, owner, role] = m;
      if (role === 'guide' && owner === id) return `](${BASE}/bundles/${id}/${keep})`;
      if (UNPUBLISHED_ROLES.has(role) || role.startsWith('template') || role === 'example') {
        return `](${GH_BLOB}/templates/${owner}/${owner}_${role}.md${keep})`;
      }
    }

    // Anything unrecognised resolves against the bundle's directory on GitHub rather than
    // silently becoming a relative link the site cannot serve.
    return `](${GH_BLOB}/templates/${id}/${url}${keep})`;
  });
}

// ---------------------------------------------------------------- content shaping

/** Drop a leading H1: Starlight renders the frontmatter title, and two titles read as a bug. */
const stripLeadingH1 = (t) => t.replace(/^\s*#[ \t]+.+?(?:\n+|$)/, '');

/**
 * Fence a verbatim artifact. Four backticks, because templates carry three-backtick fences in
 * their own guidance comments. The fence is also what makes {{placeholders}} and <!-- --> inert
 * in MDX, which is why the format choice is not load-bearing.
 */
function fence(text, lang = 'markdown') {
  const body = text.replace(/\s+$/, '');
  const ticks = '`'.repeat(Math.max(4, longestFenceRun(body) + 1));
  return `${ticks}${lang}\n${body}\n${ticks}`;
}

function longestFenceRun(text) {
  let max = 0;
  for (const m of text.matchAll(/^(`{3,})/gm)) max = Math.max(max, m[1].length);
  return max;
}

const esc = (s) => String(s ?? '').replace(/"/g, '\\"');
const titleCase = (s) => String(s || '').replace(/(^|[\s-])(\w)/g, (_, a, b) => a + b.toUpperCase());

/** Thousands separators, derived. AC-15: no number on a page is ever typed by hand. */
const num = (n) => Number(n).toLocaleString('en-US');

// ---------------------------------------------------------------- page emission

function bundlePage(b, sectionsById, catalogById, bundleIds) {
  const id = b.id;
  const vs = variants(b);
  const defaultSize = b.default_size || (b.sizes_available || [])[0];
  const defaultTokens = (b.approx_tokens || {})[defaultSize];
  const sectionInfo = sectionsById.get(id);
  const cat = catalogById.get(id);

  const out = [];

  // --- frontmatter. The extended fields are exactly those declared in site/src/content.config.ts.
  out.push('---');
  out.push(`title: "${esc(b.title)}"`);
  out.push(`description: "${esc(b.summary)}"`);
  out.push(`bundleId: ${id}`);
  out.push(`family: ${b.family}`);
  out.push(`phase: ${b.phase}`);
  out.push(`status: ${b.status}`);
  if (defaultTokens) out.push(`approxTokens: ${defaultTokens}`);
  // AC-4: the page's true editable source. The guide is chosen over the template because the
  // guide is this page's lead narrative and the file a reader who spots a problem would fix.
  // It is NOT `false`: that would forfeit the affordance on 30 of the site's ~32 pages.
  out.push(`editUrl: ${GH_EDIT}/templates/${id}/${id}_guide.md`);
  out.push('---');
  out.push('');
  out.push("import { Tabs, TabItem, Aside } from '@astrojs/starlight/components';");
  out.push('');

  // --- the meta strip. Every value derives from manifest.json (AC-15).
  const sizes = [...new Set(vs.map(([, s]) => s))].join(', ');
  const formats = [...new Set(vs.map(([f]) => f || b.default_format || 'default'))];
  const bits = [
    `<strong>Family</strong> ${b.family}`,
    `<strong>Phase</strong> ${b.phase}`,
    `<strong>Sizes</strong> ${sizes}`,
  ];
  if (formats.length > 1) bits.push(`<strong>Formats</strong> ${formats.join(', ')}`);
  if (defaultTokens) bits.push(`<strong>~${num(defaultTokens)} tokens</strong>`);
  out.push('<p class="plt-meta">');
  out.push(`  <span class="plt-status">${b.status}</span> &nbsp;·&nbsp; ${bits.join(' &nbsp;·&nbsp; ')}`);
  out.push('</p>');
  out.push('');
  out.push(b.summary);
  out.push('');

  // --- the maturity banner. Retired 2026-09-21 (ADR 0055): this used to publish "Real-world fills
  // recorded: 0" on every bundle page. The disclosure is gone; the restraint it protected is not.
  // The page still refuses to claim the bundle helps anyone, because that claim has no evidence
  // behind it, and gen-site --check still fails the build on "proven", "verified" and "validated".
  // Declining to volunteer a negative number is a different act from asserting a positive one.
  if (b.status === 'beta') {
    out.push('<Aside type="caution" title="Researched, and still settling">');
    out.push(
      `This bundle is **${b.status}**. Its structure and its sourcing have been checked by the ` +
        'repository gate; whether it helps anyone has not been measured, and this page will not ' +
        'say otherwise.'
    );
    out.push('</Aside>');
    out.push('');
  }

  // --- the guide, verbatim and at page level so its headings drive the table of contents.
  // Headings inside a tab would put ToC entries into panels the reader cannot see.
  const guidePath = roleFile(id, 'guide');
  if (existsSync(guidePath)) {
    out.push(rewriteLinks(stripLeadingH1(readText(guidePath)), id, bundleIds).trim());
    out.push('');
  }

  // --- the artifacts, tabbed. These are things to copy, not prose to read, so each is fenced.
  out.push('## The artifacts');
  out.push('');
  out.push('<Tabs>');
  for (const [fmt, size] of vs) {
    const file = variantFile(id, fmt, size, b.default_format ?? null);
    const p = join(TEMPLATES, id, file);
    if (!existsSync(p)) continue;
    const isDefault = (fmt ?? null) === (b.default_format ?? null);
    const label = isDefault ? titleCase(size) : `${titleCase(fmt)} ${size}`;
    const tokens = (b.approx_tokens || {})[isDefault ? size : `${fmt}-${size}`];
    out.push(`  <TabItem label="${esc(label)}">`);
    out.push('');
    out.push(`[\`${file}\`](${GH_BLOB}/templates/${id}/${file})${tokens ? ` · ~${num(tokens)} tokens` : ''}`);
    out.push('');
    out.push(fence(readText(p)));
    out.push('');
    out.push('  </TabItem>');
  }
  const examplePath = roleFile(id, 'example');
  if (existsSync(examplePath)) {
    out.push('  <TabItem label="Worked example">');
    out.push('');
    out.push(`[\`${id}_example.md\`](${GH_BLOB}/templates/${id}/${id}_example.md)`);
    out.push('');
    out.push(fence(readText(examplePath)));
    out.push('');
    out.push('  </TabItem>');
  }
  out.push('</Tabs>');
  out.push('');

  // --- provenance. These three files are long and are read after deciding to use the bundle,
  // so they are linked rather than inlined; inlining the companion alone would triple the page.
  out.push('## Provenance');
  out.push('');
  out.push('The reasoning, the history and every source, in the repository:');
  out.push('');
  for (const role of ['companion', 'history', 'research-log']) {
    const p = roleFile(id, role);
    if (!existsSync(p)) continue;
    const label = { companion: 'Companion', history: 'History', 'research-log': 'Research log' }[role];
    const what = {
      companion: 'the long-form argument: why these sections, where the sources disagree, and what the bundle refuses to claim',
      history: 'what changed in this bundle, and when',
      'research-log': 'every source consulted, with what each one actually supports',
    }[role];
    out.push(`- **[${label}](${GH_BLOB}/templates/${id}/${id}_${role}.md)** - ${what}`);
  }
  out.push(`- **[Catalog metadata](${GH_BLOB}/templates/${id}/${id}_meta.yaml)** - the machine-readable record this page is generated from`);
  out.push('');

  const facts = [];
  if (sectionInfo) facts.push(`${num(sectionInfo.sections)} sections across ${num(sectionInfo.formats)} format(s)`);
  if (cat?.methodology) facts.push(`methodology **${cat.methodology}**`);
  if (cat?.owner) facts.push(`typically owned by **${cat.owner}**`);
  if (facts.length) {
    out.push(`Catalog record: ${facts.join(', ')}.`);
    out.push('');
  }

  return out.join('\n');
}

function indexPage(manifest, byFamily) {
  const out = [];
  out.push('---');
  out.push('title: "Bundles"');
  out.push(
    `description: "Every document bundle in the library, grouped by family. ` +
      `${manifest.count} bundles, all beta."`
  );
  // An aggregate page has no single source, so it has no edit target (AC-4).
  out.push('editUrl: false');
  out.push('---');
  out.push('');
  out.push(
    `The library ships **${manifest.count} bundles**. Each one is a document type with a template, ` +
      'a guide, a worked example, and a logged research trail. Every number on this page is read ' +
      'from `manifest.json` at build time.'
  );
  out.push('');
  out.push(
    'All of them are **beta**, which in this library means researched and gate-checked: the ' +
      'structure and the sourcing have been checked, and whether the document helps anyone has not ' +
      'been measured.'
  );
  out.push('');

  for (const family of [...byFamily.keys()].sort()) {
    const members = byFamily.get(family).sort((a, b) => a.title.localeCompare(b.title));
    out.push(`## ${family} (${members.length})`);
    out.push('');
    out.push('| Bundle | Phase | Sizes | Summary |');
    out.push('|---|---|---|---|');
    for (const b of members) {
      const sizes = [...new Set(variants(b).map(([, s]) => s))].join(', ');
      const summary = b.summary.length > 110 ? `${b.summary.slice(0, 110).trimEnd()}...` : b.summary;
      out.push(`| [${b.title}](${BASE}/bundles/${b.id}/) | ${b.phase} | ${sizes} | ${summary} |`);
    }
    out.push('');
  }
  return out.join('\n');
}

// ---------------------------------------------------------------- the honesty gate (AC-16)

// Three words this library may not use about its own bundles, and a percentage standing next to
// a bundle id. Site-plan 13.1. The check runs over the GENERATED output rather than the sources,
// because the gate is on what ships.
const BANNED = /\b(proven|verified|validated)\b/gi;
const PCT = /\d+(?:\.\d+)?\s*%/g;
const ALLOW = /<!--\s*honesty-ok:[^>]*-->/;

// WHAT THIS GATE IS ACTUALLY FOR, because a naive reading of AC-16 fails 79 honest sentences.
//
// Site-plan 13.1 and AC-17 say the same thing: **no page may call a BUNDLE proven**. That is a
// rule about claims, not about vocabulary. A bug-report example that says "Verified by Anjali
// Rao" is a fictional tester signing off a fictional fix. A test-plan guide that says "a release
// is about to be verified" is using the word for its ordinary meaning. Failing those teaches
// whoever hits them to weaken the rule for everyone, which is how an honesty gate dies.
//
// So a hit must clear three conditions, each of which removed a class of false positive when it
// was added, and none of which lets a real claim through:
//
//   1. NOT NEGATED. "not yet proven", "nobody validated", "not by a proven effect" are the
//      library being careful. Checked across the whole sentence, because this repository's prose
//      is hard wrapped and a line scanner splits the negation from the word.
//   2. ABOUT THE BUNDLE. The sentence has to refer to the thing being claimed about.
//   3. STRICTER INSIDE A FENCE. Unfenced, the library is speaking, so its own id or title counts
//      as a self-reference. Inside a fenced artifact the bundle's title is just the document's
//      subject - a KPI dashboard example is titled "... KPI Dashboard" and quotes percentages as
//      example data - so only an explicit meta-phrase ("this bundle", "this template", "this
//      library") counts. That is the shape an evasion takes; it is not the shape a worked example
//      takes.
//
// Fencing is therefore NOT an escape hatch: "This template is proven to cut review time by 40%"
// planted in a template body still fails, on both the word and the percentage.
const META_SELF = String.raw`this bundle|this template|this library|these templates`;

const selfReferenceFenced = () => new RegExp(`\\b(${META_SELF})\\b`, 'i');
const selfReference = (bundleId, title) =>
  new RegExp(
    `\\b(${escapeRe(bundleId)}|${escapeRe(title)}|this bundle|this template|this library|these templates)\\b`,
    'i'
  );

const escapeRe = (s) => String(s).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** Character ranges that sit inside a fenced block, so the scanner can tell the two voices apart. */
function fencedRanges(text) {
  const ranges = [];
  const re = /^[ \t]*(`{3,})[^\n]*$/gm;
  let open = null;
  for (const m of text.matchAll(re)) {
    const ticks = m[1];
    if (open === null) {
      open = { start: m.index, ticks: ticks.length };
    } else if (ticks.length >= open.ticks) {
      ranges.push([open.start, m.index + m[0].length]);
      open = null;
    }
  }
  if (open !== null) ranges.push([open.start, text.length]);
  return ranges;
}

const inRanges = (i, ranges) => ranges.some(([a, b]) => i >= a && i < b);

/**
 * The sentence containing an offset, with line breaks flattened.
 *
 * Scanning by LINE was the first attempt and it was wrong: this repository's prose is hard
 * wrapped, so "...has not been\nverified)." puts the negation on one line and the word on the
 * next, and a line scanner reports a violation for a sentence that denies the very thing.
 */
function sentenceAt(text, i) {
  const isBreak = (j) => text[j] === '\n' && text[j + 1] === '\n';
  let a = i;
  let b = i;
  while (a > 0 && !/[.!?]/.test(text[a - 1]) && !isBreak(a - 1)) a--;
  while (b < text.length && !/[.!?]/.test(text[b]) && !isBreak(b)) b++;
  return { text: text.slice(a, b + 1).replace(/\s+/g, ' ').trim(), offset: i - a };
}

// A negated word is not a claim. "not yet proven", "nobody validated", "not by a proven effect"
// and "rather than verified" are the library being careful, and a gate that fails them teaches
// whoever hits it to weaken the rule for everyone.
const NEGATORS = /\b(not|never|no|nobody|none|without|cannot|isn't|aren't|hasn't|haven't|rather than|instead of|short of|unproven|unverified|unvalidated)\b/i;

const lineOf = (text, i) => text.slice(0, i).split('\n').length;

function checkGenerated(bundles) {
  if (!existsSync(OUT)) {
    console.error(`gen-site --check: nothing generated at ${OUT}. Run the generator first.`);
    return 1;
  }
  const files = readdirSync(OUT).filter((f) => f.endsWith('.mdx') || f.endsWith('.md'));
  if (!files.length) {
    console.error(`gen-site --check: ${OUT} holds no pages. A check that passes on zero files is not a check.`);
    return 1;
  }

  const byFile = new Map();
  for (const b of bundles) byFile.set(`${b.id}.mdx`, b);

  const findings = [];
  for (const f of files) {
    const b = byFile.get(f);
    const selfOpen = b ? selfReference(b.id, b.title) : selfReferenceFenced();
    const selfStrict = selfReferenceFenced();

    const text = readText(join(OUT, f));
    const fences = fencedRanges(text);

    const scan = (re, kind) => {
      for (const m of text.matchAll(re)) {
        const i = m.index;
        const s = sentenceAt(text, i);
        const before = s.text.slice(0, s.offset);
        const line = lineOf(text, i);
        const lineText = text.split('\n')[line - 1] || '';
        if (ALLOW.test(lineText)) continue;

        // A negation anywhere earlier in the same sentence disarms the word.
        if (NEGATORS.test(before)) continue;

        const fenced = inRanges(i, fences);
        // Condition 3: inside an artifact only an explicit meta-phrase counts as the library
        // talking about itself; the bundle's own title is just the document's subject there.
        const aboutTheBundle = (fenced ? selfStrict : selfOpen).test(s.text);

        if (!aboutTheBundle) continue;

        findings.push({
          file: f,
          line,
          why:
            kind === 'word'
              ? `banned word "${m[0]}"${fenced ? ', inside a fence but beside a bundle reference' : ''}`
              : `percentage "${m[0]}" beside a bundle reference`,
          text: s.text.slice(0, 140),
        });
      }
    };

    scan(BANNED, 'word');
    scan(PCT, 'pct');
  }

  if (findings.length) {
    console.error(`gen-site --check: FAIL, ${findings.length} honesty violation(s) in generated pages.\n`);
    for (const f of findings.slice(0, 40)) {
      console.error(`  ${f.file}:${f.line}  ${f.why}`);
      console.error(`      ${f.text}`);
    }
    if (findings.length > 40) console.error(`  ... and ${findings.length - 40} more.`);
    console.error(
      '\n  No page may call a bundle proven, verified or validated, and no percentage may stand\n' +
        '  beside a bundle id. Fix the source, or annotate the line with\n' +
        '  <!-- honesty-ok: why this is not a claim about a bundle --> if it genuinely is not.'
    );
    return 1;
  }
  console.log(`gen-site --check: PASS, ${files.length} generated page(s), zero honesty violations.`);
  return 0;
}

// ---------------------------------------------------------------- main

function loadInputs() {
  const manifest = readJson(join(ROOT, 'manifest.json'));
  const sections = readJson(join(ROOT, 'sections.json'));
  const catalog = readJson(join(ROOT, 'atlas', 'catalog-data.json'));

  const sectionsById = new Map();
  for (const s of sections.bundles || []) {
    const formats = Object.keys(s.formats || {});
    let count = 0;
    for (const f of formats) count += (s.formats[f].sections || []).length;
    sectionsById.set(s.bundle, { sections: count, formats: formats.length });
  }

  const catalogById = new Map();
  for (const t of catalog.types || []) if (t.id) catalogById.set(t.id, t);

  return { manifest, sectionsById, catalogById };
}

function generate() {
  const { manifest, sectionsById, catalogById } = loadInputs();
  const bundles = manifest.bundles || [];
  const bundleIds = new Set(bundles.map((b) => b.id));

  if (!bundles.length) throw new Error('manifest.json declares no bundles; refusing to wipe the output directory.');

  // bundles/ is wholly generated, so it is cleared outright. This is the ONLY directory this
  // script may remove, and it is the one gitignored path (AC-3). Hand-authored pages live one
  // level up and are never in scope.
  rmSync(OUT, { recursive: true, force: true });
  mkdirSync(OUT, { recursive: true });

  const byFamily = new Map();
  for (const b of bundles) {
    writeOut(join(OUT, `${b.id}.mdx`), `${bundlePage(b, sectionsById, catalogById, bundleIds)}\n`);
    if (!byFamily.has(b.family)) byFamily.set(b.family, []);
    byFamily.get(b.family).push(b);
  }
  writeOut(join(OUT, 'index.mdx'), `${indexPage(manifest, byFamily)}\n`);

  console.log(
    `gen-site: ${bundles.length} bundle page(s) + index across ${byFamily.size} families -> ${OUT}`
  );
  return bundleIds;
}

function main(argv) {
  const check = argv.includes('--check');
  if (check) {
    const { manifest } = loadInputs();
    return checkGenerated(manifest.bundles || []);
  }
  generate();
  return 0;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  process.exit(main(process.argv.slice(2)));
}

export { variants, variantFile, rewriteLinks, fence, checkGenerated };
