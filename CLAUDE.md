# jax-splatter — project conventions for Claude Code

## What this project is

The home of **JAX SPLATTER**, the act — Jax's artist project. Songs, lights,
band, choreo, video, merch, the signed brand system, and the public website
all live here (see the README's map). The website's job within that: who,
what it costs ($150–250/event), how to book, and proof — live at
[jaxsplatter.com](https://jaxsplatter.com).

This repo is a **product of the sakuma process**, not an ecosystem component.
Process and methodology concerns do not live here — see "What this repo does
NOT do" below.

Scope history: began as `djseith-site` (website only); widened to the act's
repo with the Jax Splatter rebrand, 2026-08-25.

## The brand is governed

Visual identity is a system of **signed releases** in
[brand/releases/REGISTRY.md](brand/releases/REGISTRY.md) — colors (JAX-A001),
wordmark (JAX-A002), type (JAX-A003), and onward. **Nothing is an official
release until Jax signs off**; the registry records the words, the stamp
(tools/stamp.py), and the release commit carries
`Signed-off-by: Jax <booking@jaxsplatter.com>`. Working material lives in
brand/reference/. When making anything user-visible, use the signed system —
don't invent colors or faces.

In the context of this repo, address the user as **Jax**.

## Project conventions

- **Static-first** (the site) — nothing here needs a server; don't introduce
  one without a ratified decision.
- **Site aesthetic**: Blade Runner dark per [docs/decisions.md](docs/decisions.md)
  D7 — black+blue moody, black+red frenetic — with the signed brand system
  layered on top (wordmark, type, One-Sheet letter white).
- **No recognizable AI artifacts** on the site — people present but never
  important: no faces.
- **Truth over polish**: the site never claims accounts, mixes, or shows that
  don't exist. Empty states are honest.

## Surfacing PRs to the human

**Whenever you ask Jax to look at, review, or merge a PR, give the full URL**
(`https://github.com/<owner>/<repo>/pull/<n>`). Never a bare number.

## When to log (the logging protocol)

This repo follows the ecosystem logging protocol at
`~/Code/ledger/docs/logging-protocol.md`: open a ledger goal-record at the
first mutation toward a stated goal; close it when the goal completes or is
abandoned. Never create records on a clock.

## What this repo does NOT do

- **Audio ETL tooling** — [seith-miller/djseith](https://github.com/seith-miller/djseith)
  is a tool the act uses (download, analyze, time-stretch, stem-separate).
  Its bugs get fixed there.
- **Individual events** — event production (rigs, runbooks, event promo)
  lives in interzone (Death to Summer, MULTIPASS). The act performs at
  events; events are not the act. Act-branded assets an event consumes (e.g.
  the lower-third) are released here, installed there.
- **Methodology and process learnings** — signals about how the pipeline
  should work go to [smartsquared/sakuma](https://github.com/smartsquared/sakuma).
- **Pipeline tooling fixes** — agent-lab, blueprint, compass bugs get filed
  on those repos.

## Andon awareness

While the pipeline is actively building here (agent-lab dispatches), honor
andon: poll [STATUS.md](https://github.com/smartsquared/andon) and halt when
`pulled`. Interactive sessions with Jax present are exempt.

## Useful state to know

- **Live**: jaxsplatter.com (GitHub Pages, deploys on push to `main`; DNS at
  Porkbun). Booking email booking@jaxsplatter.com and Instagram @jaxsplatter
  are real and claimed; other platform rows render only when claimed.
- Brief / design doc: [docs/brief.md](docs/brief.md); ratified decisions in
  [docs/decisions.md](docs/decisions.md).
- Canonical track library: [songs/crates.md](songs/crates.md).
- Repo created 2026-06-11 from template smartsquared/seedling-product.

## Branch Strategy

Agent-lab GitFlow conventions — see [gitflow.md](gitflow.md). Feature branches
off `develop`; releases merge `develop` → `main` (which deploys the site).

## Escalation

When in doubt, stop and ask. Trigger conditions: anything user-visible the
brief or a signed release doesn't ratify (page set, pricing display, brand
changes), and anything that would flip the repo private/public.
