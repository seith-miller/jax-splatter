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
| JAX-A001 | swatch | v1 | released | 2026-08-24 in session (quote not captured; release commit `abfce87`) | `../reference/swatch/` |
| JAX-A002 | wordmark | v1 | released | 2026-08-24 in session (quote not captured; release commit `a6c44f1`) | `../reference/wordmark/jax-wordmark.html` |
| JAX-A003 | type | v1 | released | 2026-08-24 in session (quote not captured; release commit `f8220fa`) | `../reference/type/jax-type.html` |
| JAX-A004 | lower-third | v1 | released | 2026-08-25 in session (quote not captured; release commit `bc11372`) | `../reference/lower-third/` |
| JAX-A005 | key-art | v1 | released | 2026-08-26 in session (quote not captured; release commit `7429c27`) | `../reference/key-art/key-art.html` |
| JAX-A006 | avatar | v1 | released | 2026-08-27 in session — "I sign off on that as a release" | `../reference/key-art/jax-avatar-keyart.html` |

> **Bookkeeping note (2026-08-27):** the A001 row was committed truncated and
> A002–A005 never got rows; the table above was reconstructed from the release
> commits, which all carry the `Signed-off-by` trailer. From A006 onward the
> exact sign-off words are quoted per the procedure.

## Candidates

Proposed but **not signed off**.

| slug | what it is | source of truth |
|---|---|---|
| — | *none* | — |

## Withdrawn

Kept for the record; no longer candidates. Files remain in `../reference/` as archive.

- **logotype / new-song-card / put-it-in-my-shirt** — the Jack Splatter remakes; superseded by the JAX-A002 wordmark. Reference archive only.
- **jax-off** — custom splat TTF experiment; direction dropped 2026-08-24.
- **type v1** — Nosifer/Oswald lineup; superseded by type v2.
