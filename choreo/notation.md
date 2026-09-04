# Choreo notation

The typed grammar for counts sheets, step cards, and cut clips. There is no
industry-standard text notation for choreography (Labanotation and Benesh are
graphical scores; step sheets are genre vocabularies without a grammar), so
this is ours — borrowing the living conventions where they exist.

## Time

- Counts per the counting convention in [README.md](README.md).
- **`8.beat`** addresses a moment: `3.1` = first count of the third 8.
- Ranges are inclusive of the start, exclusive of the next: `3.1-3.4` is four
  counts, ending where `3.5` begins. Clips cut on these boundaries loop in
  musical time.
- **`&`** is the half-beat subdivision (standard dance counting): `3.1&`.

## Sequence and simultaneity

- **`-`** means *then*: `L - R` = left, then right.
- **`+`** means *at the same time*: `arms + travel` = both at once.

## Sides and limbs

- **`L` / `R`** for sides: `Frisbees (L - R)` = the left-arm frisbee then the
  right-arm frisbee.
- **`LF` / `RF`** when a specific foot matters (line-dance convention):
  `step RF, cross LF behind`.

## Travel and facing (stage directions)

Directions use the theater standard, always from the **performer's**
perspective facing the audience: `US` (upstage, away), `DS` (downstage,
toward), `SL` / `SR` (performer's left / right), corners `USL USR DSL DSR`,
`C` center.

- **`>DIR`** — travel toward: `Catwalk >US`, `Chassé >SL`, `>DSR`.
- **`@DIR`** — facing (no travel implied): `Hands block @US`.
- Combine with the operators: `Duckwalk >SL - cat turn @DS`.

On drawn sheets and in the counts app, travel renders as an arrow in
**audience view** (a dancer traveling `>SL` moves rightward on screen);
the letters stay performer-perspective. Both describe the same motion.

## Structure words

- **step** — atomic named movement (one card in the steps library).
- **phrase** — a composed arc with a landing, usually 2-4 counts.
- **block** — a full 8 (or more) with one job, e.g. a hands-performance block.
- A step name with a modifier is a variant of the base step: *Halftime
  Catwalk* = catwalk at one step per two counts.

First used on the vouge routine (125.8 BPM, count 1 anchored at 14.554s in
the ref video). The steps library lives in the Splatter Steps app; cards
carry `vouge 8.b-8.b` refs using this grammar.
