# Counts sheet — {TRACK} ({BPM} BPM)

- **Count**: {full-time (1 beat = 1 count) | half-time (2 beats = 1 count)} —
  per the convention in [../README.md](../README.md)
- **One 8-count** = {2 | 4} bars = {3.84s @125 …}
- **Grid anchor**: count 1.1 = {t} in the ref; beat = {s}
- **Dancers**: {who / how many / hired-local vocabulary requirements}
- **Notation**: [../notation.md](../notation.md)
- **Ref video**: {link or path}
- **Chart**: [../../band/charts/{song}.md](../../band/charts/) — where the
  **Riding** column comes from

## What we're riding

One paragraph before any counts: **what the music is doing under the
movement**. The groove, what to lock to, and what to ignore.

A dancer hitting on 5 has to know what they're hitting *with* — a snare, a
stab, a vocal, nothing at all. Without it they're counting in silence and
drifting the moment the monitor is bad, which on our stages is most of the
time.

Name what is **audible from the floor**, not what is on the chart. "Kick and
a rising synth" is useful; "guitar 2 doubles the riff" is not — the dancer
can't hear the difference and doesn't care.

| 8 | Counts | Riding | Material |
|---|---|---|---|
| 1 | 1.1-1.8 | {what you hear} | {what you do} |
| 2 | 2.1-2.4 | {…} | {…} |

Steps in **bold** reference [../steps.md](../steps.md). Fixed material is
marked HIT; everything unmarked is freestyle within the named vocabulary.

## Hits

The fixed accents everyone must land together, by (8, count) — **and what
each one lands on**:

| 8 | Count | Lands on | Hit |
|---|---|---|---|
| {4} | {1} | {the downbeat / crash / vocal "…"} | {all freeze, arms down} |

## Notes

{spacing, formations, entrances, anything the table can't hold}

---

## Filling the Riding column from a chart

The chart ([band/charts/](../../band/charts/)) counts in **bars**; this sheet
counts in **8s**. Convert with the locked convention:

| Tempo | One 8-count | Bar → 8 |
|---|---|---|
| under 140 BPM | 2 bars | `8 = ceil(bar / 2)` |
| 140 BPM and over | 4 bars | `8 = ceil(bar / 4)` |

Then read the chart's section map across: where a stem enters, drops out or
peaks is a thing a dancer can feel. Section boundaries are the strongest
landmarks — they're where the music changes under everyone at once.

If the chart and this sheet disagree about where a section starts, **this
sheet is wrong**: the chart is keyed to the recording.
