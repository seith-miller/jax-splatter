# Where everything lives — the storage plan

**Jax, 2026-10-05:** we are going to make a lot of documents. This is where
each kind goes, so the question is never asked twice. The plan was made with
the archivist's contract in hand and filed on it as
[https://github.com/smartsquared/sakuma-archivist/issues/9](https://github.com/smartsquared/sakuma-archivist/issues/9); the five things we need from that component are there.

## The rule in one line

**Self-produced masters go to the archivist; prose goes to git; collected
sources go to gather; third-party transcriptions go nowhere.**

| Artifact | Lives in | Notes |
|---|---|---|
| Charts, count sheets, dossiers, this file | **git** — this repo | git is their archive; never double-stored |
| Backing tracks, sessions, scores, parts, MIDI, grids, video, cues | **[sakuma-archivist](https://github.com/smartsquared/sakuma-archivist)** | project `jax-splatter-<song>`; roles `mixdown session score part midi grid stem video cues` |
| Stems of a cover | **archivist**, `kind=derivative` | the archivist's own position (#7): derived-of-collected is metadata, not exclusion |
| The cover's source recording | **gather** | e.g. Tank is `505780c3` |
| Songsterr and other third-party transcriptions | **nowhere** | received, not ours. Local, outside every archive, used to check our work |

## The working set

`~/Music/jax-splatter/<song>/` is the **workspace tier** — the current working
set, never the archive. Today it is a single copy with no Time Machine; the
archivist's issues #6 (workspace push) and #7 (producer manifest) are what
turn "archive now" into one command. Until they land, ingest is
`uv run archivist add <folder> -p jax-splatter-<song> -r <role>` from
`~/Code/sakuma-archivist`, and it is run by hand at the end of a working
session.

## Versions

Every revision is a new row; rows are never rewritten. "The current score"
is a **bookmark** (archivist #5, per asset). Until it exists, the newest row
for a `(project, role, filename)` is current by convention.

## Numbers

A number isn't finished until a hired band could be handed it
([docs/board/](board/), the Numbers tab). **Proposed ninth thing: archived**
— every master row written. Not yet added to the board; Jax's call.

## Not yet done

No jax-splatter rows exist in the archivist (checked 2026-10-05: 115 rows,
all dildozer). Two calls are Jax's before the first ingest: whether a cover's
stems go in now or wait for an `origin` column, and whether a master score
that still embeds Songsterr's notes is a storable derivative or waits until
our edits make it ours.
