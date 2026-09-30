# Tank — cover chart (working)

**The Stranglers**, *Black and White* (1978). A cover candidate, so this sits
with the charts rather than in the Jax Splatter pool.

| | |
|---|---|
| **Tempo** | **161.5 BPM** (machine — correct by ear). Bar = 1.49 s at 4/4 |
| **Key** | **Em** (machine, confidence 0.83; strongest pitch classes E, B, D, G) |
| **Length** | 2:57 · **≈119 bars** |
| **Source** | `~/gather/jax-splatter-refs/Tank.mp4` — YouTube, AAC 128 kbps. Approved by Jax 2026-09-27 |
| **Production folder** | `~/Music/jax-splatter/tank/` — source recording, six stems (`htdemucs_6s/`), mix, REAPER session `tank.rpp`; everything the session uses lives in this one folder |

This is the first song through **teach-her** — un-mix-her's stage that ends
in paper rather than a DAW session
([spec](https://github.com/seith-miller/un-mix-her/blob/develop/docs/teach-her.md)).
Done by hand; the stage isn't built yet.

Everything below is **derived from the recording by us** (demucs separation,
then librosa analysis). Published tabs and lyrics are linked at the foot, not
copied in — they belong to their authors, and our own timings are more use to
this band anyway.

## First: is it really a five-piece?

Jax's read was one guitar, one bass, one drummer, one vocalist, one
keyboardist. The separation only half agrees.

| Stem | Level | Share of mix |
|---|---|---|
| guitar | −17.3 dB | **45.1%** |
| drums | −19.5 dB | 26.7% |
| vocals | −23.2 dB | 11.5% |
| bass | −23.7 dB | 10.2% |
| other | −25.6 dB | 6.6% |
| **piano** | **−76.7 dB** | **0.0%** |

The piano stem is **silence**. The keyboard-shaped content is in `other`, and
it is **not spread across the song** — it sits at 0–10% for the whole body and
then jumps to **39%, 65%, 57%** across the last three sections (bar 102 to the
end), exactly as the bass drops to zero.

Two readings, and only ears can settle it:

1. **The keys are an outro part**, and a keyboardist has almost nothing to do
   for the first 100 bars.
2. **The keys are buried in the guitar stem** for the body — plausible, since
   guitar is 45% of the mix and separators smear organ into guitar routinely.

**Listen to `other.wav` before charting a keyboard part.** htdemucs's piano
model is trained on acoustic piano, so a Hammond or a synth would never land
in that stem — its silence is not evidence of no keyboard.

## Section map

Levels are each stem against **its own peak**, so read down a column (when is
the guitar loudest?), not across a row.

| § | Bar | In | Bars | Drums | Bass | Guitar | Vocals | Other |
|---|---|---|---|---|---|---|---|---|
| A | 1 | 0:00.8 | 2 | 9% | 0% | 23% | 0% | 0% |
| B | 3 | 0:03.8 | 2 | 72% | 4% | 12% | 0% | 0% |
| C | 5 | 0:06.7 | 4 | 37% | 54% | 19% | 0% | 0% |
| D | 9 | 0:12.0 | 18 | 26% | 46% | 31% | 17% | 9% |
| E | 27 | 0:38.7 | 22 | 24% | 10% | 38% | 37% | 7% |
| F | 49 | 1:11.3 | 20 | 22% | 11% | 54% | 9% | 0% |
| G | 70 | 1:41.7 | 33 | 25% | 19% | 37% | 22% | 10% |
| H | 102 | 2:30.5 | 7 | 30% | 0% | 40% | 8% | 39% |
| I | 109 | 2:41.2 | 3 | 36% | 0% | 19% | 0% | 65% |
| J | 112 | 2:45.7 | 3 | 42% | 0% | 9% | 0% | 57% |

Shape: a two-bar guitar figure alone (A), drums in (B), bass in (C), then the
body from bar 9. **F (bars 49–69) is the guitar's loudest stretch with the
vocal nearly out** — the instrumental. The last three sections hand the song
to whatever `other` is.

## Vocals — when the singer sings

Phrase boundaries off the vocal stem. **Words are not reproduced here**; see
the lyric link below, or work from the stem, which is cleaner than any
transcript.

| Phrase | In (bar) | Out (bar) | Length (s) |
|---|---|---|---|
| 1 | 20 | 22 | 2.0 |
| 2 | 22 | 24 | 1.9 |
| 3 | 25 | 35 | 10.0 |
| 4 | 38 | 40 | 2.0 |
| 5 | 41 | 44 | 2.1 |
| 6 | 44 | 49 | 4.4 |
| 7 | 61 | 62 | 1.7 |
| 8 | 63 | 67 | 4.1 |
| 9 | 80 | 81 | 1.9 |
| 10 | 82 | 84 | 2.1 |
| 11 | 85 | 90 | 4.4 |
| 12 | 90 | 97 | 6.6 |
| 13 | 104 | 105 | 1.4 |
| 14 | 116 | 117 | 1.1 |

Note the gaps: **nothing from bar 49 to 60**, and **nothing from bar 97 to
103**. Fourteen phrases, most of them 2–3 s, with four longer runs.

## Drums

**757 onsets over 119 bars — 6.3 hits/bar**, and remarkably flat: almost every
bar sits between 6 and 8. This is a machine-steady part with no fills to speak
of; the interest is in the two-bar intro and the last four bars, where it
drops to 1, 0, 0.

Bars 1–2 are empty, bar 3 starts at 5, and from bar 5 it holds 6–8 the whole
way. Density creeps up slightly over the last quarter (bars 97+ run 7–8).

## Bass — sounding root by bar

Machine pitch-tracking of the bass stem (yin). **Treat as a sketch.** `—` means
the tracker found nothing confident, not that the bass is silent; it drops out
badly wherever the stem is distorted or masked, which is most of the middle.

| From bar | Roots |
|---|---|
| 1 | `—` `—` `—` `—` `D` `D` `E` `D` |
| 9 | `B` `D` `B` `D` `B` `D` `B` `A` |
| 17 | `A` `G` `G` `A` `G` `G` `A` `G` |
| 25 | `G` `E` `—` `—` `—` `—` `—` `—` |
| 33 | `—` `—` `—` `A` `—` `G` `A` `E` |
| 41 | `A` `A` `E` `G` `—` `—` `—` `—` |
| 49 | `—` `—` `—` `—` `—` `—` `—` `—` |
| 57 | `—` `—` `—` `D#` `D#` `E` `G` `D#` |
| 65 | `C` `—` `—` `—` `—` `—` `—` `E` |
| 73 | `B` `E` `B` `A` `A` `G` `E` `A` |
| 81 | `E` `G` `E` `—` `—` `—` `—` `D` |
| 89 | `A` `B` `A` `—` `—` `—` `—` `E` |
| 97 | `E` `E` `A` `—` `—` `—` `—` `—` |
| 105 | `—` `—` `—` `—` `—` `—` `—` `—` |
| 113 | `—` `—` `—` `—` `—` `—` `—` |

What survives is consistent with **E minor**: the opening moves on D and E,
then a long B/D alternation, then an A/G stretch. Bars 49–56 are a total
tracking dropout — the instrumental. **This wants a human pass against the
stem before anyone plays from it.**

## References

Linked, not copied.

| What | Where |
|---|---|
| Bass tab | [Songsterr](https://www.songsterr.com/a/wsa/stranglers-tank-bass-tab-s251140) · [Ultimate Guitar](https://tabs.ultimate-guitar.com/tab/the-stranglers/tank-bass-6582443) |
| All Stranglers tabs | [Songsterr, guitar](https://www.songsterr.com/a/wsa/the-stranglers-tabs-a5147?inst=guitar) · [bass](https://www.songsterr.com/a/wsa/the-stranglers-tabs-a5147?inst=bass) · [bigbasstabs](https://www.bigbasstabs.com/s/stranglers_bass_tabs.html) |
| Album context | [Black and White (Wikipedia)](https://en.wikipedia.org/wiki/Black_and_White_(The_Stranglers_album)) — Tank was the B-side to "Walk On By", later pressed as a double-A for radio |
| MIDI | **None found for Tank.** [MIDI DB](https://www.mididb.com/the-stranglers/) carries Stranglers files but not this one; requests for it go back years on [alt.music.stranglers](https://groups.google.com/g/alt.music.stranglers/c/K4E8av19Vzw) |
| Drum transcription | **None found.** Nothing published that I could locate |
| Lyrics | Widely available; not reproduced here |

So: a bass tab exists, and that's it. **No MIDI, no drum chart, no guitar tab
specific to this song.** Which means our stems plus this analysis are the best
source material available for four of the five parts.

## Counting, for the count sheet

161.5 BPM is over the 140 boundary, so **half-time**: one 8-count is **4
bars** ([choreo/README.md](../../choreo/README.md)). The ~119 bars are about
**30 8s**, and `8 = ceil(bar / 4)`.

| Section | Bar | 8 |
|---|---|---|
| Body starts (D) | 9 | 3 |
| Instrumental (F) | 49 | 13 |
| Outro begins (H) | 102 | 26 |

Blocking for this song, if it gets any, goes on a count sheet in
[choreo/counts/](../../choreo/counts/) — not on this sheet.

## What's left before these are playable charts

1. **Settle the keyboard question** — listen to `other.wav`.
2. **Correct the tempo and the bar-one downbeat by ear.** Every bar number here
   hangs off 161.5 BPM; if that's off, everything shifts.
3. **Name the sections.** A–J are machine labels, not musical ones.
4. **Human bass pass** against the stem to fill the dropouts.
5. **Then one sheet per player**, per the format in [README.md](README.md).
