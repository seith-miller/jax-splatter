# jax-splatter — project conventions for Claude Code

## What this project is

Public website for DJ Seith — promo + booking. The site's job: who, what it costs ($150–250/event), how to book, and proof (mixes, sets, visuals). The audio/visuals pipeline is a separate repo ([seith-miller/djseith](https://github.com/seith-miller/djseith)); this repo is the website only.

This repo is a **product of the sakuma process**, not an ecosystem component. The sakuma pipeline built it; its job now is to serve its users. Process and methodology concerns do not live here — see "What this repo does NOT do" below.

## Your first task in this repo

Ratify the open decisions in [docs/brief.md](docs/brief.md) (booking funnel vs portfolio, domain, stack), then build v0. Competitive research on the top-10 DJs' sites lives in [research/](research/).

Per gitflow, do the work on a feature branch off `develop` and open a PR back to `develop` when done.

## Surfacing PRs to the human

**Whenever you ask the human to look at, review, or merge a PR, always give them the link** — the full URL (`https://github.com/<owner>/<repo>/pull/<n>`) or a markdown link. Never reference a PR by number alone when you want them to act on it; the human works across many repos and a bare `#4` makes them hunt. One-click, not a chore.

## Project conventions

- **Static-first** — nothing here needs a server; don't introduce one without a ratified decision.
- **Blade Runner visual identity** — night, city, motion. Black+blue = slow/moody/mournful; black+red = energetic/frenetic. Glitch and VHS artifacts welcome.
- **No recognizable AI artifacts** — and people are present but never important: no faces, waist-down crowds, silhouettes in windows.

## When to log (the logging protocol)

This repo follows the ecosystem logging protocol at `~/Code/ledger/docs/logging-protocol.md`: **open a ledger goal-record at the first mutation toward a stated goal; close it when the goal completes or is abandoned.** Discussions get a record only when they end in a decision (`/log-that`). Never create records on a clock. The SessionStart hook surfaces open records automatically.

## What this repo does NOT do

- **Audio/visual asset production** — the shot catalog, renders, and music pipeline live in [seith-miller/djseith](https://github.com/seith-miller/djseith). This repo consumes finished assets.
- **Methodology and process learnings** — if building this product teaches something about how the pipeline should work, that signal goes to [smartsquared/sakuma](https://github.com/smartsquared/sakuma), not here.
- **Pipeline tooling fixes** — agent-lab, blueprint, compass bugs get filed on those repos, not patched around in this one.

If you find yourself doing any of these here, you've crossed the product/process boundary.

## Andon awareness

While the pipeline is actively building here (agent-lab dispatches), honor andon: poll [STATUS.md](https://github.com/smartsquared/andon) and halt when `pulled`. Interactive sessions with the human present are exempt.

## Useful state to know

- Repo created 2026-06-11 (seed commit from the GTD drain session); retrofitted in place from template smartsquared/seedling-product on 2026-06-11.
- Brief / design doc: [docs/brief.md](docs/brief.md)
- Deployment target: not yet deployed — `*.github.io` acceptable for v0, no domain chosen
- Sibling repo: [seith-miller/djseith](https://github.com/seith-miller/djseith) (audio/visuals pipeline, shot catalog, R2 renders)

## Branch Strategy

This project follows the agent-lab GitFlow conventions. See [gitflow.md](gitflow.md) for the branch model and merge policy.

## Escalation

When in doubt, stop and ask. Trigger conditions: anything user-visible the brief doesn't ratify (page set, domain, stack, pricing display), and anything that would flip the repo public.
