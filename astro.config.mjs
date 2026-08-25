// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Repo is seith-miller/jax-splatter (not a *.github.io repo), so GitHub Pages
// serves the site under /jax-splatter/. `base` reflects that.
//
// jaxsplatter.com is registered (Porkbun, 2026-08-22) but DNS is not pointed
// here yet. When it is, this becomes:
//   site: 'https://jaxsplatter.com',
//   base: '/',
// plus a `public/CNAME` holding `jaxsplatter.com` and the domain set in
// Settings -> Pages. Until then the github.io path is what actually serves.
export default defineConfig({
  site: 'https://seith-miller.github.io',
  base: '/jax-splatter',
  trailingSlash: 'ignore',
  integrations: [sitemap()],
});
