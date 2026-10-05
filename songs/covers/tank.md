# Tank — The Stranglers

**Status:** in work — stems cut, grid settled, chart started
**Why we want it:** Jax called it in on the hook, *"I can drive my very own
tank."* Fast, mean, short, and built on a figure a three-piece can carry.

## The record

| | |
|---|---|
| Written by | **to confirm** — Stranglers credits of this era are usually the whole band (Burnel / Cornwell / Greenfield / Black); not verified |
| From | *Black and White* (1978) |
| Released | album 12 May 1978. Tank was the **B-side to "Walk On By"**, later pressed as a double-A for radio |
| Label | United Artists; A&M in America |
| Producer | **Martin Rushent** — their first three albums |
| Engineer | **Alan Winstanley** — all tracks |
| Studio | **T.W. Studios, Fulham, London** |
| Recorded | February–March 1978 |
| Personnel | to confirm per track |

Sources: [Black and White (Wikipedia)](https://en.wikipedia.org/wiki/Black_and_White_(The_Stranglers_album))
· [Discogs release](https://www.discogs.com/release/1490350-The-Stranglers-Black-And-White)

## The context

Third album in about eighteen months, made fast by a band already past the
first punk wave and deliberately getting stranger. The album is noted for
**experimental song structures and time signatures** — "Curfew" is in 7/4 —
which matters directly to us: the metric trick we found in Tank is in
character for the record, not an accident of our analysis.

Rushent and Winstanley are the same production team as the first two albums,
so the sound is a known quantity: dry, close, keyboard-forward, very little
air. Worth knowing when we decide how much of the original tone to chase —
per [teach-her](https://github.com/seith-miller/un-mix-her/blob/develop/docs/teach-her.md),
a band re-voices a cover anyway.

## What exists to learn from

| What | Where | Quality |
|---|---|---|
| Bass tab | [Songsterr](https://www.songsterr.com/a/wsa/stranglers-tank-bass-tab-s251140) · [Ultimate Guitar](https://tabs.ultimate-guitar.com/tab/the-stranglers/tank-bass-6582443) | unassessed — Songsterr's plays along with the original |
| All Stranglers tabs | [Songsterr guitar](https://www.songsterr.com/a/wsa/the-stranglers-tabs-a5147?inst=guitar) · [bass](https://www.songsterr.com/a/wsa/the-stranglers-tabs-a5147?inst=bass) · [bigbasstabs](https://www.bigbasstabs.com/s/stranglers_bass_tabs.html) | — |
| Reference recording | `~/gather/jax-splatter-refs/Tank.mp4` — gather `505780c3`, YouTube, AAC 128 kbps | fine for reference, too lossy to build from |
| Clean capture (unfetched) | gather `ab33dcc5` — [TIDAL track 1563164](https://tidal.com/browse/track/1563164) | queued; the fetcher records the desktop app in real time |

| **Songsterr MIDI export** — gtr ×2, bass, drums | `~/Music/jax-splatter/tank/refs/songsterr/` (local, outside git) | **Their transcription, not ours.** `songsterr.json` records it: machine-origin (initial revision "via AI", 2025-01-17), human-edited 2025-07-15, written at a fixed 160 BPM. Use to *check* our work; never as source |

**Does not exist** (checked 2026-09-27): **no MIDI** — [MIDI DB](https://www.mididb.com/the-stranglers/)
carries Stranglers files but not this one, and requests for it go back years on
[alt.music.stranglers](https://groups.google.com/g/alt.music.stranglers/c/K4E8av19Vzw).
**No drum transcription. No song-specific guitar tab.** So our own stems and
analysis are the best source that exists for four of the five parts.

## What we derived

Full detail in [band/charts/tank.md](../../band/charts/tank.md). Headlines:

- **Six stems** (htdemucs_6s) plus a **drum cascade** — kick, snare, toms, hh,
  ride, crash.
- **161.5 BPM median, moving 154–172, 114 bars.** Not fixed tempo; the session
  carries a tempo map, one point per bar.
- **Kick on 1+ and 3+, snare on 2 and 4** — Jax by ear, then confirmed against
  the separated parts. The offbeat kick is why every tracker slipped half a
  beat.
- **The click is half-time** and that is correct: it sits only on kick
  positions, while the snare wanders ±58 ms and never has to agree with it.
- **The opening drum fill is rubato** — don't chart it, don't click it.
- **From bar 105 the drums go into three** against a bar that stays 4/4, while
  the keys take over and the bass stops. In character for this album.
- **Drums: transcribed and notated (2026-10-02).** Per-part MIDI from the
  cascade (kick, snare, hh, ride, toms, crash), cleaned and quantised at 161.5
  over **117 bars**; `drums_patterns.json` holds the groove per section with a
  **3.1 ms median timing residual** (p90 17.7 ms) — a real lock. Its kick
  `x.x.....x.x.....` and snare `....x.......x...` are Jax's "1+ and 3+ / 2 and
  4" exactly. Notated in MuseScore: `notation/tank-drums-clean.pdf` is a
  **handable drum part**, with `.mscz` source and MusicXML beside it. One of
  five parts done.

- **Guitar and bass parts: next.** Jax, 2026-10-04 — tabs and charts for
  both. Same route as drums: transcribe from *our* stems, score the result by
  chroma correlation against the stem, notate in MuseScore, export tab +
  MIDI. Bass needs a cleaner source first (below). Guitar is polyphonic and
  harder; the `htdemucs_6s` guitar stem is the input and Songsterr's export
  is the check.

- **Our own bass transcription — attempted and REJECTED (2026-10-02).**
  `unmixher transcribe --transcriber bass` produced 516 notes that Jax heard
  immediately as a different line from the record. The numbers agree:

  | | |
  |---|---|
  | chroma correlation, resynth vs bass stem | **0.415** (under 0.5 = a different line) |
  | margin over silence | 0.63 — **below** un-mix-her's own 0.76–0.81 "transparent" band |
  | median note | **A#1**, with **78 % below E1** — under a bass's lowest string |
  | pitch classes | E **31 %** against 13 % in the stem |

  Diagnosis: the `htdemucs_ft` bass stem carries **kick bleed**, and the
  tracker followed it into the sub region, reporting a near-drone instead of
  the line. `--transcriber spectral` is worse (margin 0.349); `mono` and
  `basic-pitch` have no backend installed here.

  **The lesson for reading these reports:** `grid_lock_8ths: 1.00` means every
  note landed on an eighth. It says nothing about whether the pitches are
  right, and it was read as quality here when it is only rhythm.

  Next thing to try, one at a time: high-pass the bass stem above the kick
  fundamental before transcribing, or transcribe the `htdemucs_6s` bass stem
  instead, and score each by chroma correlation against the stem rather than by
  the margin alone.

## Open questions

- **Writer credits** — not verified. Needed before any recording of a cover.
- **Is the `other` stem a keyboard?** Greenfield's keys are a Stranglers
  signature, and `other` surges exactly where the bass drops out. Unconfirmed
  by ear.
- **Key** — three machine runs gave Em, E:maj and D:maj. Unresolved.
- **Which chairs does it need?** It is a four-piece record; we have nine
  chairs ([band/charts/chairs.md](../../band/charts/chairs.md)).
