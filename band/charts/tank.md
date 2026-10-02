# Tank — cover chart (working)

**The Stranglers**, *Black and White* (1978). A cover candidate, so this sits
with the charts rather than in the Jax Splatter pool.

| | |
|---|---|
| **Tempo** | **median 80.75 BPM**, and it moves — see *The grid* below. Bar = 2.97 s at 4/4 |
| **Key** | unresolved — three machine runs gave Em, E:maj and D:maj. Settle by ear |
| **Length** | 2:57 · **58 bars** |
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
metronomic."* The measurements agree exactly:

| | |
|---|---|
| Median | **80.75 BPM** · bar = 2.97 s · **58 bars** |
| Beat range (5th–95th pct) | **78.3 – 86.1 BPM** — he breathes about 8 BPM |
| Bar-to-bar change | median **0.8 %**, 90th pct 2.3 % |

Small, smooth, continuous — a player holding tempo, not drift and not noise.
No single BPM fits: every candidate from 75–175 scored an onset-to-grid RMS of
**28–29 % of a beat**, and uniformly random onsets against an arbitrary grid
give 28.9 %. A fixed grid is right at bar 1 and a beat and a half out by the
end.

So the session carries a **tempo map**, one point per bar:
`~/Music/jax-splatter/tank/tank-tempomap.rpp`. Bar 1 is a free lead-in that
absorbs the offset; every bar line after it sits on a detected downbeat, and
no audio is stretched.

**Earlier numbers here were wrong.** 161.5 BPM was a doubling error of mine
and 162 was forced with `--tempo-octave double`, which manufactured a
confidence the machine never had. un-mix-her's `grid` reported
`tempo_confidence: 0.0` twice and was right to.

### Two slips, both repaired

Half a beat vanished twice — the tracker jumped to the offbeat and stayed
there, so the click was fine then wrong from that bar on. Found by ear first
("something strange happens around measure 16"), then located:

| Bar | Short by | |
|---|---|---|
| 15 | 348 ms | 0.47 beats |
| 33 | 372 ms | 0.50 beats |

A bar short by almost exactly half a beat is the signature. Worth automating.

## The intro fill is free

The first bar of drumming (3.41–6.36 s) has a **72 %** spread between hits;
bars 2, 3 and 4 sit at 34–37 %. The opening fill is **rubato** and the band
arrives in time after it. Don't chart it to the grid, and don't expect a
drummer to play it to a click.

## Bar 53 — the drums go into three

From roughly bar 51 the song stops agreeing with itself. Autocorrelating the
drum stem:

| | Strongest periods |
|---|---|
| Body (bars 21–50) | **1.00 beat** (0.79), 2.00 beats (0.64) — locked |
| From bar 53 | **1.53 beats** (0.66), 0.75 beats (0.64) — nothing on the beat |

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
| B | 1 | 0:03.8 | 1 | 72% | 4% | 12% | 0% | 0% |
| C | 2 | 0:06.7 | 2 | 37% | 54% | 19% | 0% | 0% |
| D | 4 | 0:12.0 | 9 | 26% | 46% | 31% | 17% | 9% |
| E | 13 | 0:38.7 | 11 | 24% | 10% | 38% | 37% | 7% |
| F | 24 | 1:11.3 | 10 | 22% | 11% | 54% | 9% | 0% |
| G | 34 | 1:41.7 | 16 | 25% | 19% | 37% | 22% | 10% |
| H | 51 | 2:30.5 | 4 | 30% | 0% | 40% | 8% | 39% |
| I | 54 | 2:41.2 | 1 | 36% | 0% | 19% | 0% | 65% |
| J | 56 | 2:45.7 | 3 | 42% | 0% | 9% | 0% | 57% |

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
| 1 | 10 | 11 | 2.0 |
| 2 | 11 | 12 | 1.9 |
| 3 | 12 | 17 | 10.0 |
| 4 | 19 | 20 | 2.0 |
| 5 | 20 | 22 | 2.1 |
| 6 | 22 | 24 | 4.4 |
| 7 | 30 | 31 | 1.7 |
| 8 | 31 | 33 | 4.1 |
| 9 | 40 | 40 | 1.9 |
| 10 | 41 | 42 | 2.1 |
| 11 | 42 | 45 | 4.4 |
| 12 | 45 | 48 | 6.6 |
| 13 | 51 | 52 | 1.4 |
| 14 | 57 | 58 | 1.1 |

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

80.75 BPM is **under** the 140 boundary, so **full-time**: one 8-count is
**2 bars** ([choreo/README.md](../../choreo/README.md)). 58 bars are about
**29 8s**, and `8 = ceil(bar / 2)`.

| Section | Bar | 8 |
|---|---|---|
| Body starts (D) | 4 | 2 |
| Instrumental (F) | 24 | 12 |
| Outro begins (H) | 51 | 26 |

This reverses what this sheet said at 161.5 BPM, where the song counted
half-time at 4 bars to an 8. The tempo map also means an 8-count is not a
fixed number of seconds — the Riding column should name musical events, not
clock times.

Blocking for this song, if it gets any, goes on a count sheet in
[choreo/counts/](../../choreo/counts/) — not on this sheet.

## What's left before these are playable charts

1. **Settle the keyboard question** — listen to `other.wav`.
2. ~~Correct the tempo and the bar-one downbeat by ear.~~ **Done 2026-10-01** —
   tempo map built and auditioned; bar numbers above are keyed to it.
3. **Name the sections.** A–J are machine labels, not musical ones.
4. **Human bass pass** against the stem to fill the dropouts.
5. **Then one sheet per player**, per the format in [README.md](README.md).
