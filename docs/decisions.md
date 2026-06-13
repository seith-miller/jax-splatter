# v0 design decisions

Decisions made for the v0 build, with the evidence behind each. Research base: [research/booking-site-strategy.md](../research/booking-site-strategy.md) and [research/dj-site-traits.md](../research/dj-site-traits.md). The brief left several of these open ([docs/brief.md](brief.md#open-decisions-not-yet-ratified)); these are **proposals for ratification**, built so any of them is cheap to reverse.

> Built autonomously overnight on 2026-06-12 under the operator's standing license to "do a bunch of work overnight." Nothing is merged to `main` and the repo stays private — this whole site is one feature branch / PR for morning review. Reverse any decision by editing one config file or closing the PR.

## D1 — Primary job: booking funnel, with the portfolio as its proof layer
The brief posed "booking funnel vs portfolio" as either/or. Research dissolves it: the strongest small-DJ pattern is booking-first, where the show log + set lists + mixes ARE the trust/proof layer that converts the inquiry. So the site is a one-pager whose spine is: **identity → proof (shows/mixes) → offer+price → book**.

## D2 — Show the price ($150–250)
HIGH-confidence research finding: visible pricing pre-qualifies leads and is the #1 factor clients use to decide who to contact; hiding it is a top reason inquiries die. Displayed as a range with a one-line "what drives the variance" note, integrated into the booking section — not a standalone price list. Single source of truth: `src/data/site.ts`.

## D3 — Stack: Astro, static, GitHub Pages
Both Astro and Eleventy are verified for clean GH Pages deploys. Chose **Astro** for content collections (shows-as-data with a typed schema), build-time image optimization (image/video-heavy site), and component reuse. Zero client JS by default fits a fast, dark, visual one-pager. Deploys via the official `withastro/action`.
- Repo is `seith-miller/djseith-site` (not `*.github.io`), so Pages serves under `/djseith-site/`. `astro.config.mjs` sets `site` + `base` accordingly. **If a custom domain is later chosen, set `base: '/'`** and update `site` (one-line change, noted in the config).

## D4 — Shows as data, seeded with one real show
Shows live as markdown files in `src/content/shows/` with a typed frontmatter schema (date, venue, city, event, duration, optional tracklist, optional mixUrl, optional flyer). Seeded with the one confirmed real show: **Al's Bar, Sat Sep 20 2025, 90-min set**. The homepage shows the most recent few; the spine scales to an archive page when there are enough.

## D5 — Mixes on Mixcloud (dark embed)
HIGH-confidence: Mixcloud's blanket licensing + no-strike model is materially safer for posting recorded sets than SoundCloud's per-track-permission + content-ID-takedown regime. Dark-mode embed matches the aesthetic. v0 ships embed slots driven by `mixUrl`; they render only when a URL is present, so there are no broken players before real mixes exist.

## D6 — Contact: minimal form + direct email, no server
Static-first means no server to process a form. v0 ships a minimal inquiry form (name, email, event date, location, optional event type) wired to **Formspree** (a placeholder endpoint in `src/data/site.ts` — set `FORMSPREE_FORM_ID` to go live) with a `mailto:` booking link as the always-works fallback.
- **Action needed before launch:** set a real booking email and Formspree ID in `src/data/site.ts`. v0 uses clearly-marked placeholders rather than publishing a personal address without ratification.

## D7 — Aesthetic: Blade Runner dark, blue=moody / red=energetic, no faces
Per the Aug 2025 identity notes: near-black base, cold electric **blue** as the default/moody primary, neon **red** as the energetic accent, subtle glitch/scanline texture (CSS only, no recognizable AI artifacts). People-never-important: imagery slots are sized for rooms/booth/lights/crowd-from-behind, never faces. Real photos beat stock (NN/g) — image slots are placeholders until real shots from the [djseith pipeline](https://github.com/seith-miller/djseith) drop in.

## D8 — SEO: modest and honest
Basic meta + OpenGraph + a sitemap + conventional `Person`/`LocalBusiness` JSON-LD. The research did NOT verify that schema markup helps for a site like this, so this is low-cost convention, not a bet. Per-event-type content is anchored sections (wedding/corporate/private) rather than thin separate pages, to avoid doorway-page treatment.

## Still needs the operator (not decided here)
- Domain (still none; `*.github.io` fine for v0).
- Real booking email + Formspree ID (D6).
- Real photos/video from the pipeline (D7).
- Whether to publish text tracklists (licensing exposure unverified; v0 supports them but seeds none).
- City/region for the LocalBusiness schema + local SEO (left blank).
