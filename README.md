# djseith-site

The one address for **DJ Seith** that no platform owns — a link hub and brand home. This repo is the website only; the audio/visuals pipeline lives in [seith-miller/djseith](https://github.com/seith-miller/djseith).

## What this is

A single page that does two jobs: it is the **hub** every DJ Seith platform account points at — Instagram, Mixcloud, YouTube, Twitch and the rest — and it is the standalone **home** that stands on its own if any of those platforms disappears. Fans have one URL to remember; the brand is not hostage to anyone's algorithm.

Blade Runner aesthetic — night, city, motion; black+blue when moody, black+red when frenetic.

This repo is a **product of the sakuma process** — it was built by the sakuma pipeline, but it is not an ecosystem member. It has users, not consumers; a brief, not a substrate role.

## Provenance

| Input | Where |
|---|---|
| Brief / design doc | [docs/brief.md](docs/brief.md) (seeded from the GTD drain session, 2026-06-11) |
| Wave plan | n/a — built interactively so far |
| Driving loop | n/a |

## v0 scope

A static one-pager built with **Astro**: hero → **link hub** → recent shows → recorded sets (Mixcloud) → about. The hub sits high because most arrivals come one tap from a platform bio and want the follow link, not an introduction. Booking is one row at the foot of the hub; no rates are published (see [docs/decisions.md](docs/decisions.md) D1, D2, D9).

Content lives in two places: site-wide config in [src/data/site.ts](src/data/site.ts), and shows-as-data in [src/content/shows/](src/content/shows/) (one markdown file per show; seeded with Al's Bar, Sep 2025).

### Adding a link

Paste the URL into the matching row in `site.links` and flip `status` to `'live'`. The row appears; nothing else to touch. A row with an empty `url` does not render, so the page is never broken while the roster fills in — `npm run build` prints which platforms are still unclaimed.

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

- **The links themselves** — no DJ Seith accounts existed as of 2026-08-21. Until URLs land in `site.links`, the hub renders only the booking row.
- **Booking email** in [src/data/site.ts](src/data/site.ts) — until it is real, the booking row reads "Get in touch" rather than printing the placeholder address publicly.
- **Real photos/video** from the [djseith pipeline](https://github.com/seith-miller/djseith) into the image slots (no faces, per the brief).
- **City/region** in `site.locality` for local SEO + schema.

See [docs/decisions.md](docs/decisions.md) for the full list and the reasoning behind each choice.

## Branch Strategy

This project follows the agent-lab GitFlow conventions. See [gitflow.md](gitflow.md) for the branch model and merge policy.

## Built with

This product was built by the **sakuma ecosystem** — see [smartsquared/atlas](https://github.com/smartsquared/atlas) for the system that produced it. Process learnings from building this product flow back to [smartsquared/sakuma](https://github.com/smartsquared/sakuma); they do not live here.
