# The chairs — the ideal ensemble

**Jax, 2026-09-27:** build sheets for a **professional touring company**,
even though that company doesn't exist yet. Nine chairs. Every song gets
charted for all nine; any given night plays a subset.

This is not aspiration filed as fact. It is how an **on-track, modular**
act works ([docs/stage-vision.md](../../docs/stage-vision.md)): the backing
track is the spine, live players layer on top, and the lineup changes with
the stage and the gig. Charting all nine means a night can **add** a player
without anyone writing anything — the sheet already exists. Charting only
who's in the room means every new player is a rewrite.

The debut is three chairs ([docs/debut-staging.md](../../docs/debut-staging.md)).
That is the smallest subset, not a different plan.

## The nine

| # | Chair | Instrument | Owes the audience |
|---|---|---|---|
| 1 | **Vocal 1** | wireless handheld/headset — Jax | the song, and the room |
| 2 | **Vocal 2** | wireless — rotating guest | the second voice: answer, harmony, trade |
| 3 | **Guitar 1** | [takedown guitar](../instruments/takedown-guitar.md) | the lead string voice and the lit silhouette |
| 4 | **Guitar 2** | second takedown guitar *(no sheet yet)* | the wall — doubling, counter-riff, the other side of the stage |
| 5 | **Bass** | [takedown bass](../instruments/takedown-bass.md) | attack and silhouette on the low end; the subs carry the weight |
| 6 | **Keytar** | [keytar plate](../instruments/keytar-plate.md) | the keys voice, strapped and roaming instead of parked at a table |
| 7 | **Non-tuned percussion** | [kick/snare chest rig](../instruments/kick-snare-chest-rig.md) · [crew crate](../instruments/crew-percussion-crate.md) | the hit the audience *sees* land |
| 8 | **Tuned percussion** | [rototom chest rack](../instruments/rototom-chest-rack.md) · [jam block](../instruments/jam-block.md) | pitched attack — fills, accents, the crack in the pattern |
| 9 | **DJ** | the [playback rig](../../video/playback-rig.md) · [the Mach](../instruments/the-mach.md) | the track, the bridges, and the gestures nobody can normally see |

## What each chair does when the others aren't there

Every chair has a **fallback**: what happens to its part when nobody fills
it. This is the column that makes a modular lineup actually work, and it
belongs on every chart.

| Chair | Empty ⇒ |
|---|---|
| Vocal 1 | the show doesn't happen. **Load-bearing.** |
| Vocal 2 | track covers the answer lines; trades become solo lines |
| Guitar 1 | track covers it — but the stage loses its loudest visual gesture |
| Guitar 2 | track covers it. The most droppable chair, by design |
| Bass | track covers it; the subs were doing the work anyway |
| Keytar | track covers it |
| Non-tuned percussion | **nothing covers it.** The visible hit is the one thing a track cannot fake |
| Tuned percussion | folds up into non-tuned, or the track takes it |
| DJ | the show doesn't happen — the track *is* the DJ chair. **Load-bearing.** |

Two chairs are load-bearing: **Vocal 1 and DJ**. Everything else is a layer.
That's what makes the three-piece debut legitimate rather than a compromise —
it's both load-bearing chairs plus the two that can't be faked.

**Writing new songs for these chairs** is its own set of rules —
[songs/writing-for-the-ensemble.md](../../songs/writing-for-the-ensemble.md).

## Writing for a chair

The chart format is in [README.md](README.md) — a performance map, not
notation. Per-chair conventions on top of it:

**Vocal 1 / Vocal 2** — mark *entries by bar*, not lyrics. Who leads each
phrase, where the second voice answers, and where both land together. A
vocalist needs the shape and the cues; they already know the words.

**Guitar 1 / Guitar 2** — never write both the same part. If they're doubling,
say *doubling* and give one of them a reason to be on the other side of the
stage. Big and few: a part the back of the room can see beats a part that's
merely correct.

**Bass** — roots and rhythm, and never doubling the track's sub content.

**Keytar** — pads and stabs are the track's job; the keytar takes what reads
as *played* — a riff, a lead, a run someone can watch happen.

**Non-tuned percussion** — hits and figures on a bar grid, phrased as
choreography. Where the player *moves* is not on this sheet: that's the
count sheet's job, and this chair will usually have one.

**Tuned percussion** — same, plus pitch. Rototoms by drum, jam blocks by
note.

**DJ** — the one chart that runs the whole show clock: track starts and
stops, bridge lengths, FX and light cues, where the broadcast plays
([video/interstitials.md](../../video/interstitials.md)). Everyone else's
bar numbers come from this chair's timeline.

## Naming

One file per song: `<song>.md`, with a section per chair. Nine separate
files per song would mean nine files to keep in sync, and a player who
loses their sheet has nothing.

**Per-player extraction comes later** — the point of one source is that
printing one chair's pages is a filter, not a fork. That's a
[teach-her](https://github.com/seith-miller/un-mix-her/blob/develop/docs/teach-her.md)
job when it gets built.

## Open

- **Guitar 2 has no instrument sheet.** A second takedown guitar, or a
  different instrument entirely for contrast?
- **Does Vocal 2 double any other chair?** A guest who sings *and* takes
  crate percussion is one body, two chairs — worth saying which chairs can
  be stacked on one person.
- **Which chairs also need a count sheet?** Settled in principle (Jax,
  2026-09-28): blocking is never chart content, and a musician who roams
  gets a count sheet like anyone else. Open is *which* of the nine actually
  need one per song — all of them, or only the chairs that leave their spot.
