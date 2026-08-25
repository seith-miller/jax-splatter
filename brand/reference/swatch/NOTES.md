# Swatch working notes

Rationale removed from the presentation sheet in v8 (the sheet now reads as a
neutral spec). This file keeps the provenance and the usage logic.

## Provenance

- **Splatter Pink #ea3e86** — sampled from the Jack Splatter AI originals; the
  color that is the name. Kin to Blade Runner's neon title lettering.
- **Blood Red #c70f38 / Deep Blue #1668d6 / Electric Blue #46b3ff / Smog Indigo
  #11141f / Night #05060a** — the site theme (D7): black + blue reads slow and
  mournful, black + red/orange reads frenetic. Neon Red #ff2d55 was retired from
  the brand deck in v5 (site theme still carries it pending a D7 amendment).
- **Leeloo Orange #ff6a1f** — the Fifth Element one-sheets: hair, flame column,
  MULTIPASS warmth.
- **Slime #39ff14** — from Slaves' "The Hunter" video (sampled #a9ff00 at the
  drip, pushed greener by operator call). Sits at 99% of sRGB's maximum green
  chroma. **Slime Ink #1f9e06** is the same hue cut dark for light grounds
  (3.1:1 on One-Sheet), where full Slime disappears (1.2:1).
- **One-Sheet #f2efe9** — Guetta's gallery white; the Fifth Element one-sheet
  ground. **Bone #d2cab6** — the shirt-art ink, warmed in v7 to mirror Static
  Gray across the wheel (C 0.029 at 89° vs 267°).
- **Static Gray #454c5c** — blue-leaning gunmetal: 2.35:1 on Night (blends),
  7.5:1 on One-Sheet (pops). Utility neutral: garment blanks, secondary type on
  light grounds, hardware.
- **Night #05060a** — the only black (Void #070607 retired in v6: visually
  identical, chromatically dead). Blue-violet at 271°, same bloodline as Smog
  Indigo (272°) and Static Gray (267°).

## Usage logic

- One accent per surface — ground plus a single voice.
- Black + blue = slow/moody; black + red/orange = frenetic (D7).
- On One-Sheet the inks are the deep variants (Deep Blue, Blood Red, Slime Ink,
  Static Gray); the bright neons live on dark grounds. Splatter Pink on light
  grounds is display-size only (3.3:1).
- Splatter Pink belongs to the mark and merch, not UI chrome.
- Slime is the loudest voice — drips, hits, one-off shocks; never a second
  ground. Slime × Blood Red is the strongest duo (4.4:1, legible as text-on-
  color). Pink × Slime is the maximum-tension clash pair — big blocks only.
- Bone is ink on dark grounds; Night is ink on light ones. Bone × Smog Indigo
  is a near-perfect quiet complement (183° apart, matched chroma, mirrored
  lightness, 11.25:1) — warm paper against cool night.
- Between the named neutrals, UI ramps (dim text, hairlines) are derived tokens,
  interpolated as needed — they are not brand colors and don't get signed off.

## Companion views

- `jax-wheel.html` — the color solid in four lightness slices, all 11 colors
  plotted.
- `jax-neutrals.html` — the neutral family: hub zoom + lightness ladder.
