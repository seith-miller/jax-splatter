# Jax Splatter — art release registry

The system of record for brand/art releases. **Nothing is an official release
until the operator signs off** — sign-off is recorded here (date + where it was
given) and only then does the file get a release ID and land in this directory.
Everything else, however finished it looks, lives in [../reference/](../reference/)
as reference material.

## The signing procedure

A release becomes official in four moves, in order:

1. **The words** — Jax signs off explicitly, in session or in writing. The exact
   words are quoted in the registry row. No quote, no release.
2. **The row** — the registry table gets the ID (next `JAX-A###`), version,
   date, and the quote.
3. **The stamp** — the artifact is pressed with the official release stamp
   (`python3 tools/stamp.py <artifact> <ID> <version> <date>`): Splatter Pink,
   distressed, lower-right, carrying ID · version · date · SIGNED · JAX. Only
   sign-off-recorded artifacts get stamped; the unstamped working copy stays in
   `reference/`.
4. **The commit** — the release lands in its own commit whose message carries
   the trailer `Signed-off-by: Jax <booking@jaxsplatter.com>`.

## The scheme

- **ID**: `JAX-A###` — A for art, sequential, never reused, assigned only at
  sign-off. (Music releases, if ever tracked here, would be `JAX-M###`; the music
  catalog currently lives in record-producer-hq.)
- **Canonical filename**: `JAX-A001_logotype_v1.png` — ID, short slug, version.
- **Revisions** to a released asset bump `v#` under the same ID and get a fresh
  sign-off; the old version stays in the directory (the registry says which is
  current).
- **Status flow**: `reference` → `candidate` (proposed for release, listed below)
  → `released` (signed off, file present here). Retired releases become
  `retired`, never deleted.

## Releases

| ID | slug | version | status | signed off | source |
|---|---|---|---|---|---|
| JAX-A001 
## Candidates

Proposed but **not signed off**.

| slug | what it is | source of truth |
|---|---|---|
| key-art | the act's key art: A002 wordmark over the keyed paintball splats on Night; wide (1920×1080) and square (2048×2048) crops | `../reference/key-art/key-art.html` |

## Withdrawn

Kept for the record; no longer candidates. Files remain in `../reference/` as archive.

- **logotype / new-song-card / put-it-in-my-shirt** — the Jack Splatter remakes; superseded by the JAX-A002 wordmark. Reference archive only.
- **jax-off** — custom splat TTF experiment; direction dropped 2026-08-24.
- **type v1** — Nosifer/Oswald lineup; superseded by type v2.
