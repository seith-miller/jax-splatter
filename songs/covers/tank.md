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
  both. Bass: a human pass from our MIDI (below). Guitar: polyphonic, so the
  pitched backend is **Basic Pitch** via un-mix-her's `[transcription]` extra
  (`basic-pitch[onnx]`, `setuptools<81`); the `htdemucs_6s` guitar stem is the
  input, Songsterr's two guitar exports are the check, and the score is the
  same bar-by-bar chroma used for bass — never the margin alone.

- **Our own bass transcription — partly right, not wrong (reassessed
  2026-10-04).** I first rejected it as "a different line". Scored bar by bar
  against Songsterr's export as an external check, it isn't:

  | candidate | notes/bar | vs Songsterr |
  |---|---|---|
  | **original** `tank-bass.mid` (ft stem) | 4.4 | **0.520** — 0.62–0.63 through the body |
  | retry A — ft stem high-passed 60 Hz | 3.5 | 0.515 |
  | retry B — `htdemucs_6s` bass stem | 1.9 | 0.483 |
  | Songsterr's own | 7.1 | — |

  What's actually wrong with it: **it has 4.4 notes a bar where the part has
  about 7** — the roots are mostly right and the moving notes are missing,
  which is exactly what "sounds like a different melody" means when the
  harmony is intact. It is weak at the entry (0.35 over bars 1–16, under the
  rubato fill), weak in the instrumental (0.42), and **empty after ~152 s**.

  Two corrections to my own earlier reading. The chroma correlation of 0.415
  was against a bass stem that carries kick bleed — a polluted reference, so a
  low number there was never proof of a wrong line. And "78 % below MIDI 40,
  under the lowest string" was a mislabel: MIDI 40 is **E2**, so that is the
  bottom octave of the instrument, where Songsterr's transcription also sits
  (74 %). The register was fine.

  **The outro disagreement is open.** Our stem analysis has the bass at 0 %
  from bar 100 and our MIDI stops there; Songsterr's tab keeps the bass going
  to the end. Either the separator lost the bass under the organ, or an
  AI-origin tab filled in a part that isn't there. Only ears settle it.

  **Fix path:** a human pass against the stem in MuseScore, starting from the
  original MIDI, with Songsterr open as the check. More tracker runs won't get
  there — both retries scored lower.

## Open questions

- **Writer credits** — not verified. Needed before any recording of a cover.
- **Is the `other` stem a keyboard?** Greenfield's keys are a Stranglers
  signature, and `other` surges exactly where the bass drops out. Unconfirmed
  by ear.
- **Key** — three machine runs gave Em, E:maj and D:maj. Unresolved.
- **Which chairs does it need?** It is a four-piece record; we have nine
  chairs ([band/charts/chairs.md](../../band/charts/chairs.md)).
