// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Repo is seith-miller/djseith-site (not a *.github.io repo), so GitHub Pages
// serves the site under /djseith-site/. `base` reflects that.
//
// If a custom domain is added later (serving from root), set:
//   site: 'https://your-domain',
//   base: '/',
// and update the CNAME / Pages settings. That's the only change needed here.
export default defineConfig({
  site: 'https://seith-miller.github.io',
  base: '/djseith-site',
  trailingSlash: 'ignore',
  integrations: [sitemap()],
});
