# The wordmark as vectors

Outlined-path SVG exports of the signed JAX-A002 wordmark, for every machine
that cuts, engraves, prints or stitches: Cricut, the lasers, the Roland, the
sublimation wrap, the embroidery digitizer. Same letterforms, spacing and
colours as the signed sheet — Pathway Gothic One, letter-spacing .015em,
.30em gap between JAX and SPLATTER, kerning on. Regenerate with
`python3 tools/wordmark-svg.py` (needs fontTools + uharfbuzz; the OFL font
is in tools/).

| File | What |
|---|---|
| `jax-wordmark.svg` | dark-ground: letters #e8ecf6, X #ea3e86 |
| `jax-wordmark-light.svg` | light-ground: letters #05060a, X #ea3e86 |
| `jax-wordmark-cut.svg` | one colour, two groups (`letters`, `x`) — cut/engrave files start here |
| `jax-avatar.svg` | JAX alone, dark-ground (the sanctioned crop) |
| `jax-avatar-cut.svg` | JAX alone, one colour |

Aspect: wordmark 5.36 : 1; JAX 1.45 : 1. These are a *format* of A002, not
a revision — production files derived from them (sticker sheet, wraps,
marking files) are what get signed, as JAX-A007 onward.
