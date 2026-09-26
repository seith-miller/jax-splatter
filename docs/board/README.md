# Splatter Ops — the internal board

**Live board (private artifact):** https://claude.ai/artifact/R3NfwCrkh6wBBiJBZMbVr6

Jax's internal-facing page for the act — **not** jaxsplatter.com, and not
public. One screen showing where the debut actually stands: the countdown,
the nine gates, the hour meter, cast and venue, the money, and the calls
only Jax can settle.

Same pattern as the [setlist builder](../../songs/setlist-builder/) and the
choreo apps: **the artifact is the board of record.** `board.html` here is
a code snapshot, not the live state — ticking a gate or advancing a song on
the live page republishes it, and this file doesn't follow.

## What it does

- **Countdown** to Saturday 2026-12-19.
- **Gates** — the nine from [debut-calendar.md](../debut-calendar.md), the
  next open one marked, each showing days left or LATE. Tick when true.
- **The hour meter** — ready minutes against the 60-minute target. A song
  advances through Arranged → Tracked → Charted → Rehearsed → Ready; only
  Ready counts. The three non-song blocks (DJ passages 12:00, the drum
  features 9:00, broadcast bridges 5:00) count when built and timed.
  Songs budget 34:00, blocks 26:00.
- **Cast and venue** fields — G1 and G4 live here.
- **Money and kit**, and the six open calls.

Press **Save** after changing anything; it republishes the page to the same
URL, so every open view gets the new state.

## Regenerating the snapshot

The live page is authoritative. To refresh this file from it, read the
published artifact and overwrite `board.html`. To push a *structural*
change (new section, new gate, restyle), edit `board.html` and republish it
to the same URL — that overwrites whatever state the live page holds, so
copy the live state into the file's `#state` block first.
