# Jam block

**Concept:** A printed slap block shaped like a mouth — the upper jaw is a
tunable tongue the stick hits, the lower jaw carries a tray of ball chain
that rattles behind every hit, a snare-hoop rail along the back takes the
tambourine attachment, and it hangs on the same knurled L-rod and rail hubs
as the printed tom. The one percussion instrument that is plastic
commercially, so PLA+ is the material, not a compromise.
**Role in the set:** the crack in the pattern — a tuned block voice with a
built-in backbeat rattle, mountable anywhere on the stand or the rig; a
family of them at different notes is a melodic block set.
**Stage debut target:** TBD.
**Tier:** <$100.

## Spec (Seith, 2026-09-13)

- Mouth in profile: upper jaw = tongue with a half-round lip on its edge;
  lower jaw = walled tray for chains or beads, with a lip of its own on the
  chin so either surface can be struck.
- **Tunable.** The note is thickness over length squared (`jaw_top`,
  `mouth_depth`); the spec reports the as-printed note, and two M6 weight
  stacks on the tongue's tip tune it down as much as six semitones — nuts
  are half a semitone, washers a quarter. Access holes through the tray's
  floor put the soldering iron and a nut driver straight on the stacks from
  below. Default tongue prints on F♯4, weights down to C4.
- A **hoop rail** along the throat with a triple-flanged snare hoop's edge
  profile (2.3 × 7 flange, edge turned down), flange backward, so the
  tambourine attachment to come clamps here as it will on a snare.
- The tom's captive-eyebolt clamp on a pad behind the throat: the L-rod
  passes straight through, the eyebolt goes in once through the mouth, the
  wing nut sits on the pad's back.
- Prints on its side so every layer is the C profile — no supports.

Designed in smart-part: [`components/jam-block`](https://github.com/smartsquared/smart-part/tree/develop/components/jam-block)
(body v0.10). Pick sheet with the 3D view, tuning table and linked buy list:
https://claude.ai/code/artifact/ae329136-efbd-4fe7-9e45-3d2e4af875e9

## Bill of materials

| Part | Source | Est. | Actual | Have it? |
|---|---|---|---|---|
| Body print, PLA+ 423 cm³ (~24 h, 291 g) | house Ender 3 | $6 | | filament on hand |
| M6 × 8 brass heat-set inserts ×2 (55-pack) | Amazon B0FH8WJNYH | $12 | | |
| M6 × 30 knurled thumb screws ×2 (10-pack) | Amazon B06W2MS1K3 | $8 | | |
| M3–M6 nut/washer kit (tuning weights; shared with the rig) | Amazon B07HVCLTZC | $20 | | |
| M6 nyloc nuts ×2 | hardware store | $2 | | |
| #6 ball chain, 3 ft ×3 | Amazon B00VTY3DPA | $10 | | |
| M6 eyebolt + wing nut + washer (shared with the tom and hubs) | Amazon B0F47TL2T7 / B077Z3W9KH | $0 (shared) | | |
| 10.5 mm knurled L-rod (one per drum) | Drum Factory Direct | $5–42 | | |
| Rail hub print (shared with the stand) | smart-part `rail-hub` | $5 | | |

**BOM subtotal:** ~$63 · **+25% contingency:** ~$16 · **Budget:** ~$80

## Tools required (see BUDGET.md shared-tools table)

- 3D printer (house Ender 3, PLA+)
- Soldering iron with a heat-set insert tip
- Hex keys / 10 mm nut driver

## Build notes

- **Tuning table** (as printed, with the rib; 45 g of weights takes each
  down ~6 semitones): 6 × 70 → G♯3 · 7 × 64 → D4 · **7 × 56 → F♯4**
  (default) · 8 × 52 → B4 · 8 × 46 → D♯5 · 9 × 44 → G5. Print sharp of the
  target, weight down onto the note. Estimates until the first one is hit
  and measured; then the constant gets corrected.
- **Strength:** a 300 N hit puts ~15 MPa at the tongue's root against
  PLA+'s ~60; the root is a 5 mm fillet so a thousand hard hits do not
  start a crack. Lip wear under a nylon tip is the long-run limit; a PETG
  keeper is tougher and ~15 % lower in pitch.
- **Carry-on rule:** 140 × 132 × 65 mm, compliant. Comes off the rod by the
  wing nut alone.
- Puck: the throat is solid; a translucent print and a puck cavity are a
  parameter change when the DMX puck enclosure exists.

## Build log

- 2026-09-13 — designed in smart-part (10 revisions in a day with Seith:
  C-profile block, bead tray, M6 tuning stacks, chin lip, hoop rail, mount
  pad). Not yet printed; first print calibrates the note.
