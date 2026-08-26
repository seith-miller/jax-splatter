# jax-splatter

The home of **JAX SPLATTER** — the act. Songs, lights, band, choreo, video,
merch, the brand system, and the website all live here; the name is the artist
name, so the artist project lives under it.

Scope widened 2026-08-25: this repo began as the website only (as
`djseith-site`); the rebrand to Jax Splatter made it the act's repo, with the
site as one section.

## The map

| Section | What lives there |
|---|---|
| [brand/](brand/) | The signed brand system — colors, wordmark, type, release registry ([brand/releases/REGISTRY.md](brand/releases/REGISTRY.md)). Nothing is official until Jax signs off. |
| [songs/](songs/) | The musical body of work — [crates.md](songs/crates.md) is the canonical track library. |
| [lights/](lights/) | The act's lighting identity. |
| [band/](band/) | The performing unit. |
| [choreo/](choreo/) | Movement and staging. |
| [video/](video/) | Video identity and live visuals direction. |
| [merch/](merch/) | Merchandise, built from signed brand releases. |
| `src/`, `public/` | The website — live at [jaxsplatter.com](https://jaxsplatter.com). |
| [docs/](docs/) | Brief and ratified decisions ([docs/decisions.md](docs/decisions.md)). |
| [tools/](tools/) | Repo tooling: release stamp, OG card, splat generators. |

## Neighbours

- [seith-miller/djseith](https://github.com/seith-miller/djseith) — a **tool
  the act uses**: audio ETL (download, analyze, time-stretch, stem-separate).
- [smartsquared/interzone](https://github.com/seith-miller/interzone) — where
  **individual events** live (Death to Summer, MULTIPASS); the act performs at
  them, they are not the act.
- gather — media fetchers; the planned Spotify→TIDAL crate sync lives there.

## The website

A static one-pager (Astro) at **jaxsplatter.com**: hero → link hub → shows →
sets → about. The hub is the one address no platform owns; every account
points here. Site config in [src/data/site.ts](src/data/site.ts), shows as
data in [src/content/shows/](src/content/shows/).

```bash
npm install
npm run dev      # local dev server
npm run build    # static build → dist/
```

Deploys via GitHub Pages on push to `main`
([.github/workflows/deploy.yml](.github/workflows/deploy.yml)); DNS at
Porkbun points the apex at Pages.

### Adding a link

Paste the URL into the matching row in `site.links` and flip `status` to
`'live'`. A row with an empty `url` does not render, so the page is never
broken while the roster fills in.

## Branch Strategy

Agent-lab GitFlow conventions — see [gitflow.md](gitflow.md).

## Built with

This product was built by the **sakuma ecosystem** — see
[smartsquared/atlas](https://github.com/smartsquared/atlas) for the system
that produced it. Process learnings flow back to
[smartsquared/sakuma](https://github.com/smartsquared/sakuma); they do not
live here.
