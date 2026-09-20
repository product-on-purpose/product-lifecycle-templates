// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';

// Clause 14.7: `site` and `base` are set ONCE, here. Nothing else in this repo may
// restate the base as a consumed config value - pages read import.meta.env.BASE_URL,
// and the generator emits base-derived links.
// Clause 14.2: astro-mermaid is registered BEFORE starlight.
// Accent #5C7CFA and the branded mermaid theme are the family values named in
// SITE-STANDARD.md section 2 (Theme and branding).
export default defineConfig({
  site: 'https://product-on-purpose.github.io',
  base: '/product-lifecycle-templates',
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
      editLink: {
        baseUrl:
          'https://github.com/product-on-purpose/product-lifecycle-templates/edit/main/',
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
