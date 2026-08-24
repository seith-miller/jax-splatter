# v0 design decisions

Decisions made for the v0 build, with the evidence behind each. Research base: [research/booking-site-strategy.md](../research/booking-site-strategy.md) and [research/dj-site-traits.md](../research/dj-site-traits.md). The brief left several of these open ([docs/brief.md](brief.md#open-decisions-not-yet-ratified)); these are **proposals for ratification**, built so any of them is cheap to reverse.

> Built autonomously overnight on 2026-06-12 under the operator's standing license to "do a bunch of work overnight." Nothing is merged to `main` and the repo stays private — this whole site is one feature branch / PR for morning review. Reverse any decision by editing one config file or closing the PR.

## D1 — Primary job: the brand home *and* the link hub  — REVISED 2026-08-21
~~Booking funnel, with the portfolio as its proof layer.~~ Superseded in session with the operator.

The site's job is to be **the one address for DJ Seith that no platform owns**. Every social account points here; this page points back out to all of them. That is the anti-vendor-lock position: platforms come and go, accounts get suspended, algorithms change — the hub survives all of it, and the audience only ever has to remember one URL.

So the spine is: **identity → every place to follow → proof (shows/mixes/about)**. Booking is one row in the hub, not a funnel.

The link roster lives in `site.links` in [src/data/site.ts](../src/data/site.ts). A row renders only when its `url` is non-empty, so the page is never broken while the roster fills in; unclaimed platforms are listed with `status: 'planned'` so the outstanding work has one home. Adding a platform is one line.

## D2 — Do NOT show the price  — REVERSED 2026-08-21
~~Show the $150–250 range.~~ Reversed in session with the operator: **"I'm not a wedding DJ."**

The "show the price" evidence in [research/booking-site-strategy.md](../research/booking-site-strategy.md) comes from wedding-vendor marketplaces, where buyers comparison-shop a list and ghost the ones without numbers. The research itself flagged the caveat — transfer beyond weddings is "plausible but unproven" — and this page's audience is now fans and promoters, not couples shopping vendors.

Against publishing it here:
- A public number anchors every negotiation to the floor of the range.
- It sorts the brand into *DJ for hire* rather than *artist*, which fights the Interzone/club side of the work.
- Fans, the hub's primary audience, don't care; it's noise on the page's main job.

The research's strongest pricing finding was actually about **first replies**, not websites — vendors started quoting in their reply because prospects went quiet without a number. That benefit survives intact with nothing on the page. The rate lives in the operator's canned reply.

## D3 — Stack: Astro, static, GitHub Pages
Both Astro and Eleventy are verified for clean GH Pages deploys. Chose **Astro** for content collections (shows-as-data with a typed schema), build-time image optimization (image/video-heavy site), and component reuse. Zero client JS by default fits a fast, dark, visual one-pager. Deploys via the official `withastro/action`.
- Repo is `seith-miller/jax-splatter` (not `*.github.io`), so Pages serves under `/jax-splatter/`. `astro.config.mjs` sets `site` + `base` accordingly. **If a custom domain is later chosen, set `base: '/'`** and update `site` (one-line change, noted in the config).

## D4 — Shows as data, seeded with one real show
Shows live as markdown files in `src/content/shows/` with a typed frontmatter schema (date, venue, city, event, duration, optional tracklist, optional mixUrl, optional flyer). Seeded with the one confirmed real show: **Al's Bar, Sat Sep 20 2025, 90-min set**. The homepage shows the most recent few; the spine scales to an archive page when there are enough.

## D5 — Mixes on Mixcloud (dark embed)
HIGH-confidence: Mixcloud's blanket licensing + no-strike model is materially safer for posting recorded sets than SoundCloud's per-track-permission + content-ID-takedown regime. Dark-mode embed matches the aesthetic. v0 ships embed slots driven by `mixUrl`; they render only when a URL is present, so there are no broken players before real mixes exist.

## D6 — Contact: one booking row, no form  — REVISED 2026-08-21
~~Minimal Formspree form + direct email.~~ The inquiry form and its Formspree wiring are removed along with the funnel (D1/D2).

Booking is now a single row at the foot of the hub — visually set apart (red mood, its own border) but mechanically the same as every other row: a link. It resolves to `mailto:` the booking address.
- **Action needed before launch:** set a real booking inbox in `src/data/site.ts`. Until then `hasRealBookingEmail()` is false and the row reads "Get in touch" rather than printing the placeholder address on a public page.

## D7 — Aesthetic: Blade Runner dark, blue=moody / red=energetic, no faces
Per the Aug 2025 identity notes: near-black base, cold electric **blue** as the default/moody primary, neon **red** as the energetic accent, subtle glitch/scanline texture (CSS only, no recognizable AI artifacts). People-never-important: imagery slots are sized for rooms/booth/lights/crowd-from-behind, never faces. Real photos beat stock (NN/g) — image slots are placeholders until real shots from the [djseith pipeline](https://github.com/seith-miller/djseith) drop in.

## D8 — SEO: modest and honest
Basic meta + OpenGraph + a sitemap + conventional `Person`/`LocalBusiness` JSON-LD. The research did NOT verify that schema markup helps for a site like this, so this is low-cost convention, not a bet. Per-event-type content is anchored sections (wedding/corporate/private) rather than thin separate pages, to avoid doorway-page treatment.


## D9 — The hub sits high, above shows/mixes/about  — 2026-08-21
Ratified in session. Most arrivals are one tap from a link in a platform bio: they already know who DJ Seith is and want the follow link, not an introduction. So the order is hero → **links** → shows → mixes → about. The hero is deliberately short (`min(46vh, 24rem)`) so four link rows clear the fold on a phone.

Shows, mixes, and about are kept — the operator wants the page to work as a standalone home, not only as a redirect board.

## D10 — The share card ships as PNG  — 2026-08-21
The previous `og.svg` would have rendered as **nothing** in every context that matters: Facebook/Instagram, X, iMessage, Slack and Discord do not support SVG OpenGraph images. For a page whose whole purpose is being linked from bios and DMs, the share card is the most-viewed asset on the site.

Now `public/og.png` (1200×630), rendered from [tools/og-card.html](../tools/og-card.html) so it uses the real Oswald face and the site's own gradient. `og:image:width/height/alt`, `og:site_name`, and `twitter:image` added. Regeneration command is in [tools/README.md](../tools/README.md).

## D11 — Repo goes public  — 2026-08-21
Approved by the operator (CLAUDE.md escalation trigger). Required: GitHub Pages needs a public repo on the free plan. Pre-flight scan found no emails, phone numbers, addresses, or credentials in tracked files or git history; commit authorship uses the GitHub noreply address.

Flagged as publicly readable once flipped, since going public exposes the repo and not just the built site: `research/screenshots/` (20 captures of competitors' commercial sites) and this file's pricing rationale.

## Still needs the operator (not decided here)
- **The link roster itself** — no DJ Seith accounts exist yet (2026-08-21); handles are being claimed in a separate thread. Until URLs land in `site.links`, the hub renders only the booking row.
- Domain (still none; `*.github.io` fine for v0).
- Real booking email (D6).
- Real photos/video from the pipeline (D7).
- Whether to publish text tracklists (licensing exposure unverified; v0 supports them but seeds none).
- City/region for the LocalBusiness schema + local SEO (left blank).
