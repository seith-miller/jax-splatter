# Writing for the ensemble

**Jax, 2026-09-28:** build new tracks with the ensemble and its paperwork in
mind from the start. Most of what follows is cheap before a track exists and
expensive afterwards.

The act is **on track** ([docs/stage-vision.md](../docs/stage-vision.md)): the
backing track is the spine, live players layer on top, and the lineup is
modular night to night ([band/charts/chairs.md](../band/charts/chairs.md)).
That makes a produced track two things at once — the record, and the part of
the show nobody is playing tonight.

## 1. Leave the live layers air

A fully produced track has nothing for a live player to add. Wherever a chair
is supposed to be heard, **the track should be thinner than it wants to be** —
a guitarist doubling a part that's already maxed adds nothing but noise.

The test: mute the chair's live part and the track should sound *complete but
plain*. Unmute it and it should sound *better*, not louder.

## 2. Every chair needs a reason to exist

Not in every song — across the set. A chair that never has a moment is
decoration, and the audience can tell. When a song is done, ask which chairs
it actually needs; if the answer is the same four every time, the other five
are a lineup nobody can justify hiring.

## 3. Build it so it can cover an empty chair

Because the lineup changes, the track has to do two opposite jobs on different
nights: **cover** a part when nobody's there, and **get out of the way** when
someone is.

So produce with per-chair mute groups and render alternates — a "guitar 2
covered" and a "guitar 2 live" bounce of the same song. Deciding this at mix
time is easy. Deciding it the week of a show, with a guest confirmed on
Tuesday, is not.

## 4. Write for legibility, not density

Stage vision's rule: live instruments are judged on **legibility and attack**,
not acoustic output. The subs carry the energy; the performer carries the hit.
So the live parts you write into a song should be **sparse and visible** —
something the back of the room can see land. Busy parts disappear twice: in
the mix and on the stage.

## 5. Write to the count grid

This is the cheapest thing on the list and the most annoying to retrofit.

Choreo counts in 8s, and the conversion is locked
([choreo/README.md](../choreo/README.md)):

| Tempo | One 8-count | So sections want to be |
|---|---|---|
| **under 140 BPM** | 2 bars | multiples of **2 bars** |
| **140 BPM and over** | 4 bars | multiples of **4 bars** |

A 6-bar bridge at 150 BPM costs one and a half 8-counts, and every dancer
downstream of it counts from a different place for the rest of the song.
Odd-length sections are allowed — they just have to be a *choice*.

**Tempo has a choreo consequence.** 138 and 142 BPM are nearly the same
groove, but they are counted completely differently. The current set straddles
the line:

| Song | BPM* | Counting |
|---|---|---|
| Put Your Pussy On My Face | 107.7 | full-time — 8 = 2 bars |
| Piss On Me | 117.5 | full-time |
| Where Is Da Club | 129.2 | full-time |
| Bitch Boy | 152.0 | **half-time** — 8 = 4 bars |
| Put It In My | 152.0 | **half-time** |
| *(Tank, cover)* | 161.5 | **half-time** |

*Machine-estimated — correct by ear before anyone choreographs to them.

If a new song lands near 140, knowing which side it falls on is a decision,
not an accident.

## 6. Put landmarks where the floor can hear them

Section changes are what a dancer feels. Make them **audible from the floor**,
not just visible in the arrangement: something enters, something drops out,
something stops. A transition that only reads as a filter sweep in the
producer's headphones is not a landmark.

This is the Riding column's raw material
([choreo/counts/TEMPLATE.md](../choreo/counts/TEMPLATE.md)).

## 7. The DJ chair owns the clock

The DJ runs track starts, bridge lengths, FX and light cues, and everyone
else's bar numbers come from that timeline. So write **tails and bridges that
can stretch** — a song that only works at exactly one length gives the show no
room to breathe, cover a cast change, or ride a good crowd.

## 8. Our own songs never need teach-her

[teach-her](https://github.com/seith-miller/un-mix-her/blob/develop/docs/teach-her.md)
exists to recover parts from *someone else's* finished record — separate it,
analyse it, guess. For our own material we already know the tempo, the
sections and every part, exactly, from the project.

So the chart and the count sheet should **fall out of production**, not get
reverse-engineered from a bounce later. Export the section map when the
arrangement is locked, while it's free.

## The deliverables a finished track owes

| Artifact | Where |
|---|---|
| The mix | the project |
| Per-chair covered/live alternates | the project |
| Chart — one per song, section per chair | [band/charts/](../band/charts/) |
| Count sheet, if it's danced | [choreo/counts/](../choreo/counts/) |
| A row in the catalog | [crates.md](crates.md) · record-producer-hq |
