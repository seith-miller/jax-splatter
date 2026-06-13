# djseith-site

Public website for **DJ Seith** — promo + booking. This repo is the website only; the audio/visuals pipeline lives in [seith-miller/djseith](https://github.com/seith-miller/djseith).

## What this is

The public face of DJ Seith: who, what it costs, how to book, and proof (mixes, sets, visuals). Blade Runner aesthetic — night, city, motion; black+blue when moody, black+red when frenetic.

This repo is a **product of the sakuma process** — it was built by the sakuma pipeline, but it is not an ecosystem member. It has users, not consumers; a brief, not a substrate role.

## Provenance

| Input | Where |
|---|---|
| Brief / design doc | [docs/brief.md](docs/brief.md) (seeded from the GTD drain session, 2026-06-11) |
| Wave plan | n/a — built interactively so far |
| Driving loop | n/a |

## v0 scope

A static, booking-first one-pager built with **Astro**: hero → recent shows (the proof layer) → recorded sets (Mixcloud) → about → booking (with the $150–250 price and a minimal inquiry form). The brief's "booking funnel vs portfolio" question is resolved as *booking funnel whose proof layer is the show log + mixes* — rationale and evidence in [docs/decisions.md](docs/decisions.md), backed by [research/booking-site-strategy.md](research/booking-site-strategy.md) and [research/dj-site-traits.md](research/dj-site-traits.md).

Content lives in two places: site-wide config (name, price, links, booking email) in [src/data/site.ts](src/data/site.ts), and shows-as-data in [src/content/shows/](src/content/shows/) (one markdown file per show; seeded with Al's Bar, Sep 2025).

## Develop

```bash
npm install
npm run dev      # local dev server
npm run build    # static build → dist/
npm run preview  # serve the build at /djseith-site/
```

## Deployment

Not deployed yet. The site is wired for **GitHub Pages** via [.github/workflows/deploy.yml](.github/workflows/deploy.yml) (the official `withastro/action`). To go live:

1. Make the repo **public** (or use a plan that allows private Pages).
2. **Settings → Pages → Source: GitHub Actions.**
3. Merge to `main` — the workflow builds and deploys to `https://seith-miller.github.io/djseith-site/`.
4. For a custom domain serving from root, set `base: '/'` in [astro.config.mjs](astro.config.mjs) and add the domain in Pages settings.

### Before launch (placeholders to replace)

- **Booking email + Formspree ID** in [src/data/site.ts](src/data/site.ts) (until set, the form composes a `mailto:` instead of posting).
- **Social links** (Mixcloud, Instagram, …) in the same file — empty ones are hidden.
- **Real photos/video** from the [djseith pipeline](https://github.com/seith-miller/djseith) into the image slots (no faces, per the brief).
- **City/region** in `site.locality` for local SEO + schema.

See [docs/decisions.md](docs/decisions.md) for the full list and the reasoning behind each choice.

## Branch Strategy

This project follows the agent-lab GitFlow conventions. See [gitflow.md](gitflow.md) for the branch model and merge policy.

## Built with

This product was built by the **sakuma ecosystem** — see [smartsquared/atlas](https://github.com/smartsquared/atlas) for the system that produced it. Process learnings from building this product flow back to [smartsquared/sakuma](https://github.com/smartsquared/sakuma); they do not live here.
