# The tiers — a philosophy of merch

Drafted 2026-09-28 from Jax's radio notes; **reframed to three tiers by
Jax, 2026-09-29.** Round 1 ([round-1.md](round-1.md)) spans tiers 1 and 2.

## The three tiers

| Tier | What | Job | Examples | Margin rule |
|---|---|---|---|---|
| 1 | **Free or nearly free per unit** | Attract attention, engage the audience, establish the brand. | stickers, downloads / name-your-price music, the sticker in every bag, temporary tattoos | none — the unit cost is the marketing budget; judge by reach |
| 2 | **High-volume, mass-produced** | Move as many units as possible. | T-shirts, buttons, totes, lighters, can coolers, LED wands, print-on-demand online | **percentage margin** — a floor on (price − cost) ÷ price; ≥60% garments, ≥75% small goods |
| 3 | **Handmade artifacts** | Give fans something to hold onto; make them part of the experience. | belts and the leather line, engraved Zippos, guitar pedals, instruments Jax builds, the stage-used relic | **cash minimum per unit** — a floor in dollars each sale must clear; for handmade, also **cash per hour** |

Not for sale at this time (Jax, 2026-09-29): DMX pucks, rigs, clamps. They
are the act's kit, not merch.

## Two rules for margin (Jax, 2026-09-29)

Projected profit is the same sum everywhere — units × (price − cost) — but
which term you police depends on how many you expect to sell. Tier 2 is
policed by **percentage** (per-unit cash is small; only the ratio
guarantees the pile adds up and survives bundles). Tier 3 is policed by a
**cash floor per unit** (units are few; the ratio is noise; each sale has to
clear a number), and where the object is Jax's hours, by **cash per hour**.
Tier 1 has no margin rule; its cost is what attention costs.

Market sanity checks, not rules: small-run hardware sits at 2.5–4× BOM;
a stage relic at 1.5–3× the made-to-sell version, never below it.

## How the tiers reinforce each other

1. **One design family, three material truths.** The wordmark is printed
   (tier 2), cut in real neon vinyl or burned into leather and metal
   (tier 3), and scarred into a relic that played a show (tier 3, top).
   CMYK cannot print Slime or Splatter Pink, so the neon version of
   anything *only exists at the show*; print-on-demand gets the photo key
   art and one-color designs. Tiers 2 and 3 don't cannibalize by physics.
2. **Tier 1 pays for itself in tier 2.** The sticker in every bag and the
   free download are how a listener becomes a fan with an address; the
   list is how a tier-3 drop finds the people who'd want it.
3. **Story flows down.** A relic that played DILDOZER makes the strap
   "cut from the same hide" worth $40; the artifacts make people come to
   the table; the table makes the show a place to be.
4. **Three numbers, not one** (Jax, 2026-09-28). Every object carries a
   **release number** — the signed design, `JAX-A###`, printed small like
   a catalogue number. Every production run is a **batch** (`b1`, `b2`…)
   tracked in `merch/inventory.md`. Only some objects carry a **unit
   number**: limited editions state the edition (No. 7/12); open series
   count without a cap (dog tag No. 047). A series and a batch are not the
   same thing. `merch/register.md` holds the unit-numbered objects: number
   → who / where / which hide.
5. **The hide funds five SKUs.** Belts first, then straps, then fobs, pick
   holders and wallets from the scrap — one tier-3 story across the $8–75
   rungs, and a lower effective blank cost.
6. **Two kinds of everything Jax builds.** The units *made to sell*
   (pedals, guitars) and the unit *used on stage*. Same line, same
   serials — the relic is serial 001 of the model anyone can buy 004–010
   of. The relic proves the object is real; the line gives the relic a
   market underneath the story. A made-to-sell unit owes what a relic
   doesn't: a spec sheet (the build sheet in band/instruments/), a setup,
   a fix-it promise. **Pedals lead** — a stompbox is the most merch-shaped
   thing the act builds, and the mark on its top plate lands on other
   people's boards.
7. **Reinvestment is literal at the top.** D13 says income funds the next
   phase. A relic retires when its successor is built and pays for it;
   its cash floor is the successor's BOM.

## What belongs at each price point

One item per rung, no gaps, so nobody leaves the table without a size of
purchase that fits them.

| Rung | Item | Tier |
|---|---|---|
| free | sticker in every bag; name-your-price download | 1 |
| $2 | sticker | 1 |
| $3 | wrapped lighter, button | 2 |
| $5 | can cooler, LED wand | 2 |
| $8 | dog tag (open series), leather fob | 2 / 3 |
| $12 | pick holder | 3 |
| $15 | tote | 2 |
| $25–35 | tee (neon at the table; photo or one-color online) | 2 |
| $30 | card wallet | 3 |
| $40 | guitar strap | 3 |
| $50 | engraved Zippo | 3 |
| $75 | belt, numbered | 3 |
| $120–180 | a pedal from the line | 3 |
| $1,200–3,000 | a guitar from the line | 3 |
| by announcement | the stage-used relic | 3 |

## Scarcity and story in tier 3

- Unit-numbered: limited editions state the edition (No. 7/12); open
  series just count. Edition size is honest — the number Jax actually
  made — and the register is the proof.
- Sold at the table first; leftovers online after the show, never before.
- Each one is different because the process is a gesture (hand-dyed,
  hand-splattered), not because we say so.
- **Relics have to have done something.** Sellable after shows, not
  before; provenance is the setlist, a photo of it on stage, and the build
  sheet. A signed provenance card (the registry stamp exists in
  tools/stamp.py). Retire on a rule — when the successor exists — not a
  whim. Announce, don't list; one at a time. The first of each type is
  never sold.

## Leather goods — the belt, costed

Jax's numbers: Tandy veg-tan belt blanks hand-dyed a distinct colour,
laser-engraved panel buckles (Buckleguy / Ohio Travel Bag), materials
$25–35, price $75, 15–25 min labour, run of ~100.

| Component | Source | Each |
|---|---|---|
| Belt strip 1.5" × 50–55", 8–9 oz veg-tan | Tandy blanks $15–22; or cut from a side ($150–220, 12–16 strips + offcuts) → ~$12–15 | $12–22 |
| Buckle, solid brass 1.5" plate/panel | Buckleguy / Ohio Travel Bag | $8–18 |
| Chicago screws (swappable buckle) | — | $0.50 |
| Dye, oil, finish, edge paint | Fiebing's / Angelus | $1.50–2 |
| **Materials** | | **$25–35** ✓ — $22–28 if cut from a side |
| Labour | cut, bevel, punch, dye, oil, finish, buckle | 15–25 min touch time, **over two days of drying** |

At $75: ~55% gross margin before labour; ~$40 net per belt at 20 minutes
each — roughly $120/hour for the hands, which is the best-paid thing on
the table.

**Where it sits against the thread.** Round 1 is $255 of materials and
sells for $2–15. A run of 100 belts is $2,500–3,500 of materials and 30–40
hours before Oct 24, and a bar table moves one to three belts a night. It
is the right *product* and the wrong *run size* for the first round.

**Recommendation: twelve numbered belts as round 1.5** (Nov 6 Louisville
and the winter shows): ~$360 materials, 4–5 hours, $900 at sell-through.
Prove the $75 at two shows, then cut a side and scale in the winter with
the offcut line alongside.

**Two realities to design around.**
- *Colour.* No leather dye reaches Slime or Splatter Pink. Dyes reach
  black (Night), oxblood (≈ Blood Red) and saddle tan (≈ Leeloo). Neon on
  leather is acrylic (Angelus Neon), which sits on top and cracks at the
  flex points if it's a solid field. So: **dye the belt black, then
  splatter it** — Slime and pink flicked across by hand, the brand's own
  gesture, each belt unique, and a splatter survives flexing where a field
  wouldn't. The wall-splat variant (mask the wordmark, splatter, lift)
  works on leather too. Wordmark and number laser-burned at the tip.
- *The buckle.* A CO2 laser does not mark bare brass; it needs a marking
  spray (Cermark/LaserBond, ~$60 a can) the library may not permit, or an
  IR/fiber source. **Verify whether Marksbury's small laser has the IR
  module** (it sells metal blanks, which suggests yes) before committing to
  engraved brass. Fallbacks: a laser-engraved veg-tan panel set into a
  frame buckle (leather engraves beautifully), or black-anodized plate
  buckles, which any laser marks.

**The offcut line** (same hide, same story, fills the $8–40 rungs): guitar
straps 2.5" × 50" ($40), key fobs ($8), pick holders ($12), card wallets
($30). Straps and wallets unit-numbered; fobs and pick holders batch-only.
Each register line says which belt's hide it came from.

## What this changes

- Round 1: nothing. Stickers are tier 1; buttons, totes, wrapped lighters,
  coolers are tier 2; the dog tags and the proof Zippo are the first
  tier-3 objects.
- New file when the first belt is cut: `merch/register.md` — every
  unit-numbered object, number → who / where / from which hide. Batches of
  everything else live in `merch/inventory.md`.
- Downloads and print-on-demand are set-up tasks that live elsewhere:
  distribution-plan.md (the first release creates the download) and
  accounts-inventory row 4 (Bandcamp, which also hosts POD).

## Open questions for Jax

- Twelve belts as round 1.5, or hold leather until the belt design is
  settled?
- Belt colour: black-dyed and splattered, or a dyed colour (oxblood /
  saddle) with the neon only on the buckle panel?
- Buckle: engraved brass (pending the IR-laser check) or leather panel?
- LED wands — a tier-2 item for the debut? (blank glow wands with a
  wrap; the crowd lights the room in brand colours)
