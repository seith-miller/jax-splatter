# songs

The act's musical body of work: crates (the DJ library), originals, sets in
progress. The canonical crate list is [crates.md](crates.md) — Spotify is the
live source; this file is the copy that survives it. Original tracks are
catalogued in record-producer-hq until they land here on release.

Tooling that feeds this: [seith-miller/djseith](https://github.com/seith-miller/djseith)
(audio ETL — download, analyze, time-stretch, stem-separate) reads playlist
URLs from its own `playlists.md`; keep that file pointed at whatever crates
are in active rotation. A TIDAL sync path (Spotify crates → TIDAL) is planned
to live in gather, not here.
