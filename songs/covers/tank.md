# Tank — The Stranglers

**Status:** in work — stems cut, grid settled, chart started
**Why we want it:** Jax called it in on the hook, *"I can drive my very own
tank."* Fast, mean, short, and built on a figure a three-piece can carry.

## The record

| | |
|---|---|
| Written by | **The Stranglers** — Hugh Cornwell, Jean-Jacques Burnel, Dave Greenfield, Jet Black (album credit: all tracks, except as noted; Tank carries no separate credit) |
| From | *Black and White* (1978) |
| Released | album 12 May 1978 — **White side, track 1, 2:54**. Then the **B-side to "Walk On By"** (July 1978, with "Old Codger"); an edited version with Tank was pressed as a double-A radio single |
| Label | United Artists; A&M in America |
| Producer | **Martin Rushent** — their first three albums |
| Engineer | **Alan Winstanley** — all tracks; co-produced "Old Codger" |
| Studio | **T.W. Studios, Fulham, London** |
| Recorded | February–March 1978 |
| Personnel | Hugh Cornwell — guitar, lead/backing vocals · Jean-Jacques Burnel — bass, lead/backing vocals · **Dave Greenfield — keyboards: Hammond L100 organ, Hohner Cembalet, Minimoog** · Jet Black — drums, percussion |

Sources: [Black and White (Wikipedia)](https://en.wikipedia.org/wiki/Black_and_White_(The_Stranglers_album)) — credits and personnel read 2026-10-05
· [Discogs release](https://www.discogs.com/release/1490350-The-Stranglers-Black-And-White) — refuses non-browser requests (403); unverified against it

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

| Bass tab — Ultimate Guitar | [page](https://tabs.ultimate-guitar.com/tab/the-stranglers/tank-bass-6582443) | script-rendered; unreadable without a browser (2026-10-05). Author, date and whether it covers the outro all unknown |

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
- **Master score (2026-10-05) — Songsterr's four parts only.** First built
  with our three machine transcriptions alongside for A/B; Jax judged the
  comparison in one listen ("see how much more usable than anything that is
  ours") and had them removed. The working score is now Songsterr's lead,
  rhythm, bass and drums on one bar grid, each pitched part with a TAB staff.
  Our raw MIDIs stay as separate files, out of the score.

  How it was built —
  Ours (drums quantised at 161, bass, guitar) sit on the measured grid
  (161.499 BPM, first downbeat 0.406 s); Songsterr's four sit on their fixed
  160. Each is mapped to **bar.beat on its own grid** and rebuilt on one
  timeline at 161.5, so alignment holds by construction and the 160-vs-161.5
  drift never enters. Check: both basses enter at bar 5, both lead lines at
  bar 1, drum entries differ only by the rubato fill (2.73 vs 3.00). Songsterr's
  "gtr0" is set to a synth-lead program so the Minimoog question can be heard,
  not just argued. Built by `midimaster.py`.

  **With tablature (same day):** `notation/tank-master.musicxml` is the same
  seven parts as MusicXML, with a **TAB staff under every pitched part** —
  guitars on standard six-string tuning, basses on four — strings and frets
  assigned per note, chords grouped, ties across barlines, every measure
  checked to sum to one bar. Written so the tab exists on open rather than
  being added by hand in the GUI. Built by `xmlmaster.py`. Jax's native save
  is `tank-master.mscz` — the copy that keeps mixer state and edits; the tab
  is fully editable there (strings, frets, slides, bars that don't match the
  ear), and that editing is the point: Songsterr's reading is the start of
  our arrangement, not something we file as ours.

- **Drums: transcribed and notated (2026-10-02).** Per-part MIDI from the
  cascade (kick, snare, hh, ride, toms, crash), cleaned and quantised at 161.5
  over **117 bars**; `drums_patterns.json` holds the groove per section with a
  **3.1 ms median timing residual** (p90 17.7 ms) — a real lock. Its kick
  `x.x.....x.x.....` and snare `....x.......x...` are Jax's "1+ and 3+ / 2 and
  4" exactly. Notated in MuseScore: `notation/tank-drums-clean.pdf` is a
  **handable drum part**, with `.mscz` source and MusicXML beside it. One of
  five parts done. **Timekeeping cymbal resolved (2026-10-09), Seith's call:
  the verses have a ride. Matches our transcription; Songsterr's hi-hat
  reading was wrong** (see
  [band/charts/tank.md](../../band/charts/tank.md)'s Drum transcription row).

- **Guitar and bass parts: next.** Jax, 2026-10-04 — tabs and charts for
  both. Bass: a human pass from our MIDI (below). Guitar: polyphonic, so the
  pitched backend is **Basic Pitch** via un-mix-her's `[transcription]` extra
  (`basic-pitch[onnx]`, `setuptools<81`); the `htdemucs_6s` guitar stem is the
  input, Songsterr's two guitar exports are the check, and the score is the
  same bar-by-bar chroma used for bass — never the margin alone.

- **Guitar: transcribed (2026-10-04) — the best transcription we have.**
  Basic Pitch on the `htdemucs_6s` guitar stem: **1553 notes, 13.3 a bar,
  margin 0.700** — the closest any run has come to un-mix-her's 0.76
  "transparent" band. Scored against Songsterr's two guitar exports:

  | vs | bar-by-bar chroma |
  |---|---|
  | gtr 1 — strummed rhythm | **0.678** |
  | both merged | 0.629 |
  | gtr 0 — lead / intro figure | 0.558 |

  Rhythm alone beats the merge, so **the stem is mostly the rhythm guitar** —
  our **Guitar 2** chair — with the lead/intro figure only partly captured.
  That is what a separator does with two guitars: the louder strummed part
  wins. MIDI and a resynth sit beside the session in
  `~/Music/jax-splatter/tank/` (outside git, like the stems). Next: a human
  pass in MuseScore to split what's there into the rhythm part and recover
  the lead figure from the intro, where it plays alone.

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

  **The outro disagreement, sharpened (2026-10-05).** Songsterr's bass runs
  at a steady **8 notes a bar — straight eighths — from bar 9 through bar
  112**, and only stops for the last five bars. Our stems have it gone from
  bar ~100. So it is not a vague difference: either the separator lost eight
  bars of bass under the organ, or an AI tab invented them. **Ears, at
  2:30–2:50 of the mix.** The same table diagnoses our transcription exactly:
  4.4 notes a bar against a steady 8 means it caught **every other eighth**.

  **Fix path:** a human pass against the stem in MuseScore, starting from the
  original MIDI, with Songsterr open as the check. More tracker runs won't get
  there — both retries scored lower.

## Open questions

- ~~Writer credits~~ — **resolved 2026-10-05**: The Stranglers, all four, per the album credit.
- **Is the `other` stem a keyboard?** Greenfield's keys are a Stranglers
  signature, and `other` surges exactly where the bass drops out. Unconfirmed
  by ear.
- **Key** — three machine runs gave Em, E:maj and D:maj. Unresolved.
- **Which chairs does it need?** It is a four-piece record; we have nine
  chairs ([band/charts/chairs.md](../../band/charts/chairs.md)). First
  evidence on the guitar question, 2026-10-04: **Songsterr's export carries
  two distinct guitar parts** — guitar 0 is a lead/intro figure (972 notes,
  8.3 a bar, from 0:00, range up to F#5) and guitar 1 is a strummed rhythm
  part (2065 notes, 17.6 a bar, 60 % chordal, enters at 0:06). They correlate
  at 0.67 bar by bar — related, not doubled. That is an AI-origin tab's
  arrangement choice, not ground truth.

  **Jax, 2026-10-04: "yes, Tank has two 'guitars' — I think one is actually a
  keyboard."** The lead/intro figure, then, would be Greenfield's keys — which
  fits a keyboard-forward record and a single-line part that climbs to F#5.
  Tested against our stems by bar-by-bar chroma:

  | Songsterr track | vs guitar stem | vs `other` (keys) | vs piano |
  |---|---|---|---|
  | gtr 0 — lead / intro figure | **0.517** | 0.271 | 0.368 |
  | gtr 1 — strummed rhythm | **0.631** | 0.308 | 0.440 |

  **The personnel settle most of it (2026-10-05).** This is a four-piece with
  **one guitarist**. Two "distortion guitar" tracks can only both be guitars
  if Cornwell overdubbed; the far likelier reading is that Songsterr's
  "guitar 0" is **Greenfield on the Minimoog** — a monophonic lead line that
  climbs to F#5 is exactly what an AI transcriber would file as a guitar.
  Songsterr's own density profile agrees: that track is sparse through the
  verses (2 notes a bar), fills in for the instrumental, and is busiest at
  bars 97–104 (19.5 a bar) — precisely where our keys-ish `other` stem surges.

  Both land in the guitar stem — but that only says where the **separator**
  put the energy. `htdemucs_6s` is known to file organ under guitar, and
  `other` correlating weakly with everything says that stem holds almost no
  pitched material through the body (it only surges in the outro). So the
  numbers cannot distinguish "a lead guitar" from "a keyboard mis-filed as
  guitar". **Inconclusive by machine; Jax's ear decides.** If he's right, the
  chairs are **Guitar (rhythm) + Keytar (the lead figure)**, not Guitar 1 and
  2 — and the Basic Pitch transcription of the guitar stem (below) contains
  the keyboard part too, to be split out by hand.
