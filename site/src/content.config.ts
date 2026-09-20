import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import { z } from 'astro:content';

// Clause 14.1: the stock docsLoader(), called with no arguments. Content lives
// inside the app at src/content/docs/. Repo-root docs/ is never built.
//
// Site-plan 4.3: docsSchema() is extended only with the fields Starlight needs for
// generated bundle pages. This validates what the generator WRITES, so it is a
// typo-catcher and nothing more - checking the generator against itself is not a
// second gate. The real independent check (the zod mirror of meta.schema.json)
// belongs on the READ side, against manifest.json, and is not in this spike.
export const collections = {
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema({
      extend: z.object({
        bundleId: z.string().optional(),
        family: z.string().optional(),
        phase: z.string().optional(),
        status: z.enum(['beta', 'stable']).optional(),
        approxTokens: z.number().optional(),
      }),
    }),
  }),
};
