# Tank — cover chart (working)

**The Stranglers**, *Black and White* (1978). A cover candidate, so this sits
with the charts rather than in the Jax Splatter pool.

| | |
|---|---|
| **Tempo** | **median 161.5 BPM**, and it moves — see *The grid* below. Bar = 1.49 s at 4/4 |
| **Key** | unresolved — three machine runs gave Em, E:maj and D:maj. Settle by ear |
| **Length** | 2:57 · **114 bars** |
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

## The grid — it moves

**This is not a fixed-tempo recording.** Jax, 2026-10-01: *"a very competent
drummer from before the era that everything was on click — steady, but not
metronomic."*

| | |
|---|---|
| Median | **161.5 BPM** · bar = 1.49 s · **114 bars** |
| Range | **154–172 BPM** — he breathes |
| Bar-to-bar change | median under 1 % |

No single BPM fits: every fixed candidate from 75–175 scored an onset-to-grid
RMS of **28–29 % of a beat**, and uniformly random onsets give 28.9 %. A fixed
grid is right at bar 1 and a beat and a half out by the end. So the session
carries a **tempo map**, one point per bar, and no audio is stretched.

### How the tempo was settled

Four machine attempts gave 161.5, 108, 81, 90 and 174.8, and `grid` twice
reported `tempo_confidence: 0.0`. What settled it was Jax's description of the
part: **kick on 1+ and 3+, snare on 2 and 4.** That is a *full-bar* pattern,
and the machine could only ever see half-bar periodicity — the figure repeats
every two beats, so no analysis can tell bar 1 from bar 2 of it. Checked
against the separated kick and snare, the pattern fits only at 161.5:

| | 1 | 1+ | 2 | 2+ | 3 | 3+ | 4 | 4+ |
|---|---|---|---|---|---|---|---|---|
| kick | 23 % | 23 | 2 | 2 | 23 | 24 | 2 | 2 |
| snare | 4 | 8 | **32** | 5 | 3 | 8 | **37** | 3 |

The kick landing on the **offbeats** also explains the tracking failures: any
algorithm assuming kick-marks-the-downbeat locks half a beat late.

### Two slips, both repaired

Half a beat vanished twice — the tracker caught the offbeat kick and stayed
there, so the click was fine and then wrong from that bar on. Found by ear
first ("something strange happens around measure 16"), then located at
**musical bars 29 and 65**. A bar short by almost exactly half a beat is the
signature; worth automating.

## The click is half-time, and that is correct

**Click on 1 and 3 — 80.75 BPM, 743 ms.** Not a compromise. Measured against
the separated parts:

| | hits coinciding with a click | scatter |
|---|---|---|
| kick | **218** | 24.3 ms |
| snare | **22** | 57.6 ms |

A half-time click sits only on **kick** positions. The snare falls exactly
between clicks and is never tested against the grid. A full-time click moves
onto 2 and 4 — straight onto a snare that wanders ±58 ms — and a click sitting
on a wandering hit is a **flam**, one of the most audible errors there is. The
same 20 ms of grid error is also 2.7 % of a half-time beat but 5.4 % of a
full-time one.

**One click = one dance count.** At 161.5 BPM choreo counts two beats to a
count ([choreo/README.md](../../choreo/README.md)), so a count is 743 ms —
exactly the click interval. The pulse the band plays to and the count the
dancers take are the same thing.

## The intro fill is free

The first bar of drumming (3.41–6.36 s) has a **72 %** spread between hits;
bars 2, 3 and 4 sit at 34–37 %. The opening fill is **rubato** and the band
arrives in time after it. Don't chart it to the grid, and don't expect a
drummer to play it to a click.

## Bar 105 — the drums go into three

From roughly bar 100 the song stops agreeing with itself. Autocorrelating the
drum stem:

| | Strongest periods |
|---|---|
| Body (bars 41–99) | **1.00 beat** (0.79), 2.00 beats (0.64) — locked |
| From bar 105 | **1.53 beats** (0.66), 0.75 beats (0.64) — nothing on the beat |

1.5 beats is three eighth-notes. The drums group **in three against a bar that
stays 4/4** — a hemiola, not a metre change (bar lengths hold at ~3.0 s). Jax:
*"most of the instrumentation becomes timeless — a swirling mass, and the
drums start playing a pattern in three."*

That is also where `other` takes the song over (39 %, 65 %, 57 % across H, I,
J) and the bass stops entirely. **For the chart: this section is felt, not
counted.** Whoever plays it needs the cross-rhythm written as a figure, not as
bar-by-bar hits.

## Section map

Levels are each stem against **its own peak**, so read down a column (when is
the guitar loudest?), not across a row.

| § | Bar | In | Bars | Drums | Bass | Guitar | Vocals | Other |
|---|---|---|---|---|---|---|---|---|
| A | 0 | 0:00.8 | 1 | 9% | 0% | 23% | 0% | 0% |
| B | 1 | 0:03.8 | 2 | 72% | 4% | 12% | 0% | 0% |
| C | 3 | 0:06.7 | 4 | 37% | 54% | 19% | 0% | 0% |
| D | 7 | 0:12.0 | 18 | 26% | 46% | 31% | 17% | 9% |
| E | 25 | 0:38.7 | 22 | 24% | 10% | 38% | 37% | 7% |
| F | 47 | 1:11.3 | 20 | 22% | 11% | 54% | 9% | 0% |
| G | 68 | 1:41.7 | 33 | 25% | 19% | 37% | 22% | 10% |
| H | 100 | 2:30.5 | 7 | 30% | 0% | 40% | 8% | 39% |
| I | 107 | 2:41.2 | 3 | 36% | 0% | 19% | 0% | 65% |
| J | 110 | 2:45.7 | 5 | 42% | 0% | 9% | 0% | 57% |

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
| 1 | 19 | 21 | 2.0 |
| 2 | 21 | 23 | 1.9 |
| 3 | 23 | 33 | 10.0 |
| 4 | 37 | 39 | 2.0 |
| 5 | 39 | 43 | 2.1 |
| 6 | 43 | 47 | 4.4 |
| 7 | 59 | 61 | 1.7 |
| 8 | 61 | 65 | 4.1 |
| 9 | 79 | 79 | 1.9 |
| 10 | 81 | 83 | 2.1 |
| 11 | 83 | 89 | 4.4 |
| 12 | 89 | 95 | 6.6 |
| 13 | 101 | 103 | 1.4 |
| 14 | 113 | 115 | 1.1 |

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
| Drum transcription | [Songsterr, drums](https://www.songsterr.com/a/wsa/stranglers-tank-drum-tab-s251140) — the same Songsterr song page carries two guitars, bass and drums. **Machine origin:** the page began as Songsterr's AI transcription (Jan 2025), with one human edit (Jul 2025, fingering). Missed in the first search; found 2026-10-02. Against our split-and-detect transcription: kick agrees 91%, snare 75%; they disagree on the timekeeping cymbal (Songsterr: hi-hat, mostly foot; ours: ride) and on crashes and toms |
| Lyrics | Widely available; not reproduced here |

So: a bass tab and a Songsterr page with guitars, bass and drums (machine-made, lightly edited). **No MIDI.** Which means our stems plus this analysis are the best
source material available for four of the five parts.

## Counting, for the count sheet

161.5 BPM is **over** the 140 boundary, so **half-time**: one 8-count is
**4 bars**. 114 bars are about **29 8s**, and `8 = ceil(bar / 4)`.

| Section | Bar | 8 |
|---|---|---|
| Body starts (D) | 7 | 2 |
| Instrumental (F) | 47 | 12 |
| Outro begins (H) | 100 | 25 |

Because the tempo moves, an 8-count is **not** a fixed number of seconds — the
Riding column names musical events, never clock times.

Blocking for this song, if it gets any, goes on a count sheet in
[choreo/counts/](../../choreo/counts/) — not on this sheet.

## What's left before these are playable charts

1. **Settle the keyboard question** — listen to `other.wav`.
2. ~~Correct the tempo and the bar-one downbeat by ear.~~ **Done 2026-10-01** —
   tempo map built and auditioned; bar numbers above are keyed to it.
3. **Name the sections.** A–J are machine labels, not musical ones.
4. **Human bass pass** against the stem to fill the dropouts.
5. **Then one sheet per player**, per the format in [README.md](README.md).
