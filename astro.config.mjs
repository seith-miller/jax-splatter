// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Serving at the apex domain: DNS A records at Porkbun point jaxsplatter.com
// at GitHub Pages, `public/CNAME` claims it, and the custom domain is set in
// Settings -> Pages. The old seith-miller.github.io/jax-splatter URL redirects.
export default defineConfig({
  site: 'https://jaxsplatter.com',
  base: '/',
  trailingSlash: 'ignore',
  integrations: [sitemap()],
});
