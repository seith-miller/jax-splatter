import { defineCollection, z } from 'astro:content';

// Shows-as-data. Each past show is one markdown file in src/content/shows/.
// The body (markdown) is an optional note about the night.
const shows = defineCollection({
  type: 'content',
  schema: z.object({
    date: z.date(), // night of the show
    venue: z.string(),
    city: z.string().optional(),
    event: z.string().optional(), // e.g. INTERZONE — the night's branding, if any
    durationMins: z.number().optional(),
    // Optional recorded set, hosted on Mixcloud (decisions.md D5). When present,
    // a dark-mode embed renders; when absent, the card just logs the show.
    mixUrl: z.string().url().optional(),
    // Optional text tracklist. Licensing exposure of text tracklists is
    // unverified (research open question) — supported but seed none by default.
    tracklist: z.array(z.string()).optional(),
    // Optional flyer/photo in the show card. Path relative to /public or remote.
    image: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { shows };
