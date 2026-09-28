# Charts — the written parts

**Jax, 2026-09-27: chart for a professional touring company — nine chairs —
even though that company doesn't exist yet.** The ensemble is defined in
[chairs.md](chairs.md); every song is charted for all nine and any given
night plays a subset. The debut's three (Jax, one guitarist, one
percussionist) is the smallest subset, not a different plan.

A chart here is not notation. The act plays **on track**
([../../docs/stage-vision.md](../../docs/stage-vision.md)): the backing
track is the spine, and a live part is a layer chosen for **legibility and
attack**, not acoustic output. So a chart is a **performance map** — what
you hear, what you play, where you stand, and what the lights do — on one
page, readable on a dark stage.

## The set

| Song | Source | BPM* |
|---|---|---|
| [Piss On Me](piss-on-me.md) | 4:48 | 117.5 |
| [Daddy Likes It](daddy-likes-it.md) | 3:48 | 63.0 (half-time — read ~126) |
| [Where Is Da Club](where-is-da-club.md) | 3:04 | 129.2 |
| [Put It In My](put-it-in-my.md) | 2:11 | 152.0 |
| [Put Your Pussy On My Face](put-your-pussy-on-my-face.md) | 1:33 | 107.7 |
| [Bitch Boy](bitch-boy.md) | 1:37 | 152.0 |

*Machine-estimated off the newest bounce (librosa, 2026-09-26) — **correct
by ear**. New songs get a chart as they're written.

## Covers

| Song | Source | BPM* | Key* |
|---|---|---|---|
| [Tank](tank.md) — The Stranglers | 2:57 | 161.5 | Em |

A cover gets the same chart, built the same way — except the source is
someone else's recording, so the parts are derived by separating it into
stems and analysing them. Published tabs and lyrics are **linked, never
copied in**.

That process has a name: **teach-her** (Jax, 2026-09-27) — un-mix-her's last
stage, the one that ends in paper rather than a DAW session. Spec:
[un-mix-her/docs/teach-her.md](https://github.com/seith-miller/un-mix-her/blob/develop/docs/teach-her.md).
Tank is its first worked example, done by hand.

## How a chart gets filled

1. **Skeleton** — sections, bar numbers and energy are machine-segmented
   off the bounce. It is a starting grid, **not the arrangement**.
2. **Correct it** against the Bitwig project: real section boundaries, real
   bar counts, real names.
3. **Write the parts** — guitar and percussion columns, per section.
4. **Cue it** — for each section, what the player *hears* that tells them
   it changed. On track with in-ears or wedge only, the cue is the part.
5. **Rehearse, then revise.** Charts v2 comes out of rehearsal, not before.
   After **Dec 6 the charts freeze** ([../../docs/debut-calendar.md](../../docs/debut-calendar.md)).

Per-chair writing conventions live in [chairs.md](chairs.md). The two below
predate it and are the fullest worked examples; the rest follow the same
shape.

## Guitar — conventions

- **One voice, not a rhythm section.** The track already has the parts. The
  guitar is the lead string voice and the loud visual gesture.
- **Big and few.** A part the back of the room can *see* being played beats
  a part that's merely correct. Sustains, slides, stabs, whole-arm moves.
- **Never doubles the track's low end.** The subs own it.
- **Plays a normal guitar at the debut.** The lit takedown guitar
  ([../instruments/takedown-guitar.md](../instruments/takedown-guitar.md))
  has no design yet and is not on the debut critical path.
- Wireless, roaming — every part must be playable walking.

## Percussion — conventions

- **Transients, not power.** A roaming drummer cannot out-push the venue's
  subs and shouldn't try. The job is to **punctuate the moment with a hit
  the audience sees land**.
- **Rig:** kick/snare chest rig — piccolo snare left, muffled 13" tom right
  ([../instruments/kick-snare-chest-rig.md](../instruments/kick-snare-chest-rig.md)).
  Until it's built, charts are written for snare-left / tom-right and
  rehearse on stand-ins.
- **Marching-band phrasing.** Figures that read as choreography: unison
  hits, rolls into a drop, a march that moves the player somewhere.
- **The crate moment** is the exception — the percussionist leads the whole
  cast on hand percussion ([../instruments/crew-percussion-crate.md](../instruments/crew-percussion-crate.md)).
- Everything strapped; nothing on a stand.

## Notation on the page

Plain text, no staves. Hits on a bar grid:

```
|x . . x|. . x .|   x = hit   . = rest   X = accent   ~ = roll   > = crash/stop
```

Chords by name (`Dm`, `Dm–F–C`), figures in words ("two bars of eighths,
crescendo into the drop"). Anything a player can read at a glance, in the
dark, while walking.

## Printing

One song per sheet, big type, matte, on the rig case. Laminate after the
Dec 6 freeze.
