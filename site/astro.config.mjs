// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';

import { BASE, SITE } from '../scripts/site-base.mjs';

// Clause 14.7 and AC-5: `site` and `base` are CONSUMED as config exactly once, here, and the
// literals themselves live exactly once, in scripts/site-base.mjs, which this file and every
// validator import. Nothing restates them. Pages read import.meta.env.BASE_URL; the generator
// and the link checker import BASE. A base that disagrees between the build and a validator
// passes every local check and 404s live, which is the failure this arrangement removes.
// Clause 14.2: astro-mermaid is registered BEFORE starlight.
// Accent #5C7CFA and the branded mermaid theme are the family values named in
// SITE-STANDARD.md section 2 (Theme and branding).
export default defineConfig({
  site: SITE,
  base: BASE,
  integrations: [
    mermaid({
      theme: 'base',
      themeVariables: {
        lineColor: '#5C7CFA',
        fontFamily: 'system-ui, sans-serif',
        fontSize: '14px',
      },
    }),
    starlight({
      title: 'Product Lifecycle Templates',
      description:
        'Researched, governed document templates for the product lifecycle. Every claim traced to a logged source.',
      favicon: '/favicon.png',
      customCss: ['./src/styles/custom.css'],
      // The `/site/` segment is load-bearing and its absence was a live 404. Starlight builds an
      // edit link as baseUrl + the entry's filePath, and under Pattern S that filePath is relative
      // to the app: `src/content/docs/index.mdx`. Without `site/` here the link resolved to
      // `edit/main/src/content/docs/index.mdx`, a path that does not exist in this repository, so
      // "Edit this page" 404'd on both hand-authored pages from the day they shipped.
      //
      // Nothing noticed, because a build cannot tell a wrong URL from a right one. It was caught
      // by scripts/verify-edit-links.mjs on its first run against a real build, which is the
      // entire argument for porting guards before trusting a green build.
      //
      // Generated bundle pages were unaffected: they set an explicit `editUrl` in frontmatter
      // pointing at `templates/<id>/<id>_guide.md`, so they never used this fallback.
      editLink: {
        baseUrl:
          'https://github.com/product-on-purpose/product-lifecycle-templates/edit/main/site/',
      },
      lastUpdated: true,
      // Hand-authored groups are listed; the Bundles group autogenerates from the
      // generated directory so no bundle is ever named here by hand (clause 14.3, and
      // clause 14.4's coverage rule). That directory is gitignored and empty until
      // scripts/gen-site.mjs lands in S0 PR 2. Verified 2026-09-20 by building with it
      // empty: Starlight tolerates an empty autogenerate target and emits 3 pages, so
      // this config is correct now and stays correct after the generator lands.
      sidebar: [
        { label: 'Start here', link: '/' },
        // A labelled group wraps `autogenerate` inside `items`. `{ label, autogenerate }`
        // side by side is not a legal SidebarItem and fails config validation, which is
        // worth a comment because Starlight's error prints the CORRECT shape and reads
        // like an echo of what you wrote.
        { label: 'Families', items: [{ autogenerate: { directory: 'families' } }] },
        { label: 'Bundles', items: [{ autogenerate: { directory: 'bundles' } }] },
      ],
    }),
  ],
});
