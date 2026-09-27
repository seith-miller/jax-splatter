# Splatter Ops — the internal board

Jax's internal-facing page for the act. **Locally hosted** — it is not part
of the Astro site and never deploys to jaxsplatter.com. `docs/` sits outside
`src/` and `public/`, so `astro build` doesn't see it.

## Run it

```bash
npm run board          # serves docs/board on 127.0.0.1:8787
```

Then open **http://localhost:8787**. Bound to localhost only — nothing on
the network can reach it. Stop it with Ctrl-C.

## Tabs

- **Next** — the show and the days out.
- **Songs** — what we might play on Oct 24, in three pools: **Dildozer**
  originals, **Covers** (neither act's), and **Jax Splatter**. Real lengths
  off the files; tick to build a set and watch the running time. Picks are
  kept in this browser only.

## What's on it

**Stripped to essentials (Jax, 2026-09-26):** the next show, and the songs
in play for it. DILDOZER, Saturday October 24, venue TBD.

**Covers are their own pool (Jax, 2026-09-26)** — Ghost Rider (Suicide),
World Up My Ass (Circle Jerks) and Hella Nervous. They belong to neither
catalog: whoever's night it is can play them. They also carry a
mechanical-licence obligation if a set recording ever reaches a DSP. That
leaves dildozer with 10 originals (17:27) and the covers at 6:56 — 24:23
between them, which is what a DILDOZER night has to draw on.

Track lengths are measured off the masters and bounces, not guessed —
dildozer from `shows/art_farm/audio/mastered/`, Jax Splatter from the
Bitwig project bounces.

An earlier version carried gates, an hour meter, cast fields and money —
too much. That detail lives in [debut-calendar.md](../debut-calendar.md) and
[debut-staging.md](../debut-staging.md) where it belongs.

We build back from October 24, not December 19.

## Editing

`index.html` is the page — plain static HTML, no build step. Save and
refresh.

Keep the `<meta charset="utf-8">`. `python3 -m http.server` sends
`text/html` with no charset, so without that line the browser guesses
windows-1252 and every non-ASCII character breaks — the middle dot in
"Sat · Oct 24" turns into `Â·`.

## Eat My Puss moved

**Jax, 2026-09-26:** Eat My Puss (DLDZR-0014) moves to Jax Splatter. It was
the one dildozer track with no master, and it follows the same path the rest
of the Jax Splatter material took. It has no recording at all yet, so it
counts as a song, not as minutes.

Upstream consequence: DLDZR-0014 should be retired or re-pointed in
`dildozer/catalog/catalog.yaml`, and the song wants a row in
`record-producer-hq/catalog.md` under the Jax Splatter set. Neither is done.

## What Clovers has

Confirmed against Drive 2026-09-26. The handoff was a **Drive share, not an
email** — `Clovers+Dildozer:Lickety-Split/Demos-a-Gogo`, shared as writer
with itscloversb1tch@gmail.com and j.cheyenne.hohman@gmail.com since
2026-08-15. It holds **Piss On Me**, **Put Your Pussy On My Face**,
**Bitch Boy** and **Bruce LaBruce** — flagged on the songs list.

Not shared: Daddy Likes It, Where Is Da Club, Put It In My, Eat My Puss.

**Those four are the in-progress list (Jax, 2026-09-26)** — the work with a
second party waiting on it. Bruce LaBruce joined the Jax Splatter pool with
them: it went out in the same handoff and appears in no dildozer serial.

No terms exist anywhere — no email, no calendar event, nothing written about
what the split is or what's due. Detail in `record-producer-hq/catalog.md`.

## Owed upstream

`smartsquared/dildozer` `catalog/catalog.yaml` records covers on the track
row — DLDZR-0004 Ghost Rider carries `licensing: cover — mechanical needed
for DSP` and names Suicide in its title. **DLDZR-0007 Hella Nervous is also
a cover** (Jax, 2026-09-26) and carries neither; its original artist is not
recorded anywhere and needs confirming. It is the **only** cover missing the
line — DLDZR-0010 World Up My Ass has it (corrected 2026-09-26; an earlier
note here wrongly said it didn't).

The covers also sit under DLDZR serials while belonging to neither act —
worth deciding whether the catalog keeps them or marks them shared.

Not fixed here: that repo was checked out on another thread's branch. The
edit is one `licensing:` line per row, plus the original artist in the
title.
