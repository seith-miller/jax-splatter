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
- **Our own bass transcription** — `unmixher transcribe --transcriber bass` on
  our bass stem: **516 notes, grid-lock 1.00 against eighths**, monophonic,
  67 ms glide, margin 0.63 over the silence baseline. 4.5 notes a bar. MIDI and
  a resynth to audition it sit beside the session in
  `~/Music/jax-splatter/tank/`.

  This is why the dossier links tabs rather than copying them. A published tab
  is someone else's transcription and someone else's to license; a transcript
  we make from the record is **ours to edit**, is keyed to our own tempo map
  rather than an idealised grid, and drops straight into the session. Use the
  published tabs to check ourselves, not as source.

  **It stays out of the repo.** The MIDI is our transcription of someone else's
  composition — fine to hold and play from, not ours to publish — so it lives
  with the audio in `~/Music/`, like the stems, and never in git.

## Open questions

- **Writer credits** — not verified. Needed before any recording of a cover.
- **Is the `other` stem a keyboard?** Greenfield's keys are a Stranglers
  signature, and `other` surges exactly where the bass drops out. Unconfirmed
  by ear.
- **Key** — three machine runs gave Em, E:maj and D:maj. Unresolved.
- **Which chairs does it need?** It is a four-piece record; we have nine
  chairs ([band/charts/chairs.md](../../band/charts/chairs.md)).
