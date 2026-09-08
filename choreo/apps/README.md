# choreo apps

Versioned snapshots of the two live choreo tools. The **live, editable**
versions are Claude artifacts — edits made there save to the artifact, not to
this repo:

- **Vouge Counts** (counts sheet + sequenced clip playback):
  https://claude.ai/code/artifact/fac6cdd3-b592-42b6-8e28-93b0a1ca1a55
- **Splatter Steps** (steps library with clips):
  https://claude.ai/code/artifact/52aaa314-2996-456b-a7a5-8a3cb1f914dc

## What's here

- `counts-sheet/index.html` — full self-contained snapshot (embedded 480p
  reel + audio; ~6.5MB). Opens in any browser for viewing/playback; the
  in-page Save only works on claude.ai hosting.
- `counts-sheet/template.html` — the app source with `__STATE__`,
  `__MOVELIB__`, `__REEL__`, `__AUDIO__` placeholders. Media sources live in
  `~/gather/jax-splatter/choreo-vouge/` (masters, clips, overlays).
- `steps-library/index.html` — full snapshot (step clips embedded; ~4.9MB).

## Updating a snapshot

Ask Claude to "snapshot the choreo apps" — it pulls the latest artifact
versions and recommits these files. Snapshots are on-request, not automatic
(each one adds megabytes of history), so take one after meaningful charting
sessions, not every save.

Grid anchor for the vouge piece: count 1.1 = 14.554s in the ref video,
beat = 0.4770s (125.8 BPM). Notation per [../notation.md](../notation.md).
