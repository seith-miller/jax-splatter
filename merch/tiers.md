# The tiers — a philosophy of merch

Drafted 2026-09-28 from Jax's radio notes (two messages via the foreman,
2026-09-27). Jax's frame: four tiers — digital downloads, print-on-demand,
table exclusives (handmade, limited), one-of-one. What follows is how the
tiers reinforce each other, what belongs at each price point, and what
scarcity and story look like at the top. Round 1 ([round-1.md](round-1.md))
is unchanged by this; it is the low end of tier 3.

## The ladder

| Tier | What | Price band | Role | Risk | Margin | Made where | Live today |
|---|---|---|---|---|---|---|---|
| 1 | Paid digital — the music | $1–10, name-your-price | **Reach.** The door. Turns a listener into a fan with an email address. | none | ~100% | Bandcamp | **empty** — needs the first finished original ([distribution-plan.md](../docs/distribution-plan.md)); Bandcamp unclaimed |
| 2 | Print-on-demand — tees, totes, hoodies | $20–45 | **Identity at scale.** Anyone, anywhere, any size, wears the mark. | none | 30–40% | Printful/Printify → Bandcamp merch | not set up |
| 3 | Table exclusives — made by the act, numbered, limited | $2–75 | **The reason to come to the table.** Round 1 is its low end; leather is its high end. | inventory + Jax's hours | 60–85% | the makerspace, Jax's bench | round 1 in production |
| 4 | One-of-one — stage-used instruments, worn stage kit | $300–3,000+ | **Myth.** Provenance objects; the instrument program's retirement fund. | none (it already exists) | n/a | the stage | nothing retired yet |

## How the tiers reinforce each other

1. **One design family, four material truths.** The wordmark is printed
   (tier 2), cut in real neon vinyl or burned into leather (tier 3), and
   scarred into an instrument that played a show (tier 4). Same mark; the
   material tells you which tier you're holding. This is also why POD and
   the table don't cannibalize: CMYK cannot print Slime or Splatter Pink,
   so the neon version of anything *only exists at the show*. Tier 2 is
   the photo key art and one-color designs that survive DTG; the neon tee
   is a table exclusive by physics, not policy.
2. **Down the funnel: story sells the next tier.** A tier-4 guitar that
   played DILDOZER makes the tier-3 strap "cut from the same hide as the
   strap on that guitar" worth $40. Tier-3 exclusives make people come to
   shows. Shows make fans. Fans buy tiers 1–2 from anywhere.
3. **Up the funnel: the list.** Tier-1 downloads are the email list; the
   list is how a tier-4 drop gets announced to the people who'd want it.
   Without tier 1 the top of the ladder has no audience.
4. **Three numbers, not one** (Jax, 2026-09-28). Every object carries a
   **release number** — the signed design, `JAX-A###`, printed small where
   it fits, like a catalogue number on a record. Every production run is a
   **batch** (`b1`, `b2`…) of that release: date, quantity, machine, blank
   and dye lots, tracked in `merch/inventory.md`. Only some objects carry a
   **unit number**: *limited editions* state the edition (No. 7/12) and
   *open series* count without a cap (dog tag No. 047, the crew keeps
   growing). A series and a batch are not the same thing — tags 021–050 are
   batch 1 of the tag series; belts 1–12 are edition 1, which might be made
   in two batches. `merch/register.md` holds only the unit-numbered
   objects: number → who / where / which hide. A unit number is a promise
   that the object is unique and the act knows where it went.
5. **The hide funds five SKUs.** A side of veg-tan is belts first (prime
   strips), then guitar straps (long offcuts), then fobs, pick holders and
   card wallets (scrap). The offcuts drop the effective belt-blank cost
   and populate the $8–40 rungs with objects that share the belt's story.
6. **Reinvestment is literal at the top.** D13 says income funds the next
   phase. Tier 4 is that sentence made physical: an instrument is built,
   communicates for a year of shows, then retires into a collector's hands
   and pays for its successor. "Buy my guitar" is the instrument program's
   funding model, not a joke.

## What belongs at each price point

One item per rung, no gaps, so nobody leaves the table without a size of
purchase that fits them.

| Rung | Item | Tier |
|---|---|---|
| $2 | sticker | 3 |
| $3 | lighter, button | 3 |
| $5 | can cooler | 3 |
| $8 | dog tag (numbered), leather fob | 3 |
| $12 | pick holder | 3 |
| $15 | tote (table run) | 3 |
| $25–35 | tee (screen-printed neon at the table; POD photo/one-color online) | 3 / 2 |
| $30 | card wallet | 3 |
| $40 | guitar strap | 3 |
| $75 | belt (numbered, hand-finished) | 3 |
| $300+ | one-of-one: worn stage kit, retired instrument, by announcement | 4 |
| $1–10 | the music, name-your-price | 1 |

Rules: whole dollars; every rung has one thing, not three; the $8–40 band
is leather because that's where hand-made at 15–25 minutes a piece still
pays; above $75 the object must have a story, not just labor.

## Scarcity and story at the top

**Tier 3 limited (belts and up).**
- Unit-numbered: limited editions state the edition size (No. 7/12);
  open series just count. Edition size is honest — it is the number Jax
  actually made — and the register is the proof.
- Sold at the table first. Leftovers go online after the show, never
  before. The table is the primary market by rule.
- Each one is different because the process is a gesture (hand-dyed,
  hand-splattered), not because we say so.

**Tier 4 one-of-one.**
- **It has to have done something.** A stage object is sellable after it
  has played shows, not before. The provenance is the setlist: which shows,
  which songs, a photo of it on stage. An instrument built and never played
  is inventory, not myth.
- **A provenance card, signed.** The registry's stamp already exists
  (tools/stamp.py). Each tier-4 object gets a card with its number, its
  shows, its build sheet (band/instruments/*.md is the build record — the
  buyer gets the BOM), and Jax's signature. The repo is the provenance.
- **Retire on a rule, not a whim.** An instrument retires when its
  successor is built (the takedown guitar v2 retires v1). That makes tier 4
  a cadence, not a fire sale, and ties every sale to a new build.
- **Announce, don't list.** Tier-4 drops go to the list (tier 1) and the
  socials with the story first; price by ask or auction; one at a time;
  never two in a season.
- **Keep some.** The first of each instrument type is never sold. The act
  needs its own museum.

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

- Round 1: nothing. It is tier 3's low end and ships as planned.
- New file when the first belt is cut: `merch/register.md` — every
  unit-numbered object (tags, belts, straps, instruments, limited prints),
  number → who / where / from which hide. Batches of everything else live
  in `merch/inventory.md`.
- Tier 1 and 2 are set-up tasks that live elsewhere: distribution-plan.md
  (the first release creates tier 1) and accounts-inventory row 4
  (Bandcamp, which also hosts tier-2 POD).

## Open questions for Jax

- Twelve belts as round 1.5, or hold leather until the belt design is
  settled?
- Belt colour: black-dyed and splattered, or a dyed colour (oxblood /
  saddle) with the neon only on the buckle panel?
- Buckle: engraved brass (pending the IR-laser check) or leather panel?
- Round-1 status since Sep 10 — what's been made, what's still to file?
