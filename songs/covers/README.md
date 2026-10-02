# Cover dossiers — know the song before you touch it

**Jax, 2026-10-02:** before we try to cover or adapt a track, build our own
internalised reference library for it — tabs, drum transcriptions, how it was
made, when it was written, who wrote it.

One file per candidate. The point is that **the band arrives already knowing
the song**: not just the notes, but why it sounds like that, what the original
players were doing, and which bits are the song versus which bits are 1978.

## The hard rule: link, don't copy

Tabs, transcriptions and lyrics belong to whoever made them. A dossier
**records that they exist and where**; it never contains them.

| Goes in the dossier | Stays as a link |
|---|---|
| Facts — writers, dates, label, producer, studio, personnel | tab and transcription pages |
| Background **in our own words**, with the source cited | lyric sites |
| Our own analysis of the recording — tempo, form, parts | published MIDI |

This is not only the legal position, it is the better artifact: our timings
are keyed to the recording the band actually plays along to, which no
published tab is. The chart in [band/charts/](../../band/charts/) holds the
derived work; the dossier holds the provenance and the context.

## What a dossier holds

1. **The record** — writers, producer, engineer, studio, recording and release
   dates, label, the personnel who played it. Facts, cited.
2. **The context** — what was going on when it was made, why it sounds like
   this, what the band was reacting to. Our words, sources listed.
3. **What exists to learn from** — every tab, transcription, isolated track,
   interview and teardown we could find, linked, with a note on quality. And
   honestly: **what does not exist**, so nobody searches twice.
4. **What we derived** — the stems, grid, form and part analysis, pointing at
   the chart.
5. **Open questions** — what we still cannot answer about the song.

Start from [TEMPLATE.md](TEMPLATE.md).

## Why this is a gather process

The collecting half is mechanical and fans out across many sources, which is
exactly what `gather`'s ticket/forage system is for: a **ticket declares the
intent** ("a reference dossier for *Tank* by The Stranglers"), approved
tickets are claimed by **foragers** that go find the sources, and the assets
land linked to the ticket.

`gather`'s forager registry is deliberately a set — several foragers can take
one ticket, so different strategies compete on identical intent. Today it has
one member (`DirectForager`) with a documented slot for LLM-backed foragers.
A `reference-dossier` forager belongs there. Filed against gather; until it
exists, dossiers are built by hand and the template is the spec.

## The library

| Track | Dossier | Chart |
|---|---|---|
| Tank — The Stranglers | [tank.md](tank.md) | [band/charts/tank.md](../../band/charts/tank.md) |

Candidates waiting for one are in [../references.md](../references.md) — 29 in
the covers list, and the covers hiding in the inspo list.
