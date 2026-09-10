# Merch round 1 — the plan

Drafted 2026-09-10 for Jax to pick from. The first round of Jax Splatter
merchandise, made almost entirely at the Lexington Public Library
makerspaces ([makerspace.md](makerspace.md)), sized to be on a table at
**DILDOZER, Oct 24** and restocked for **Louisville, Nov 6**. Per D13,
merch is the act's first revenue and it reinvests: this round's net is
earmarked for Phase 1 of the debut build (crew percussion crate first).

Picks are recorded on the pick sheet (link at the bottom); this file is
the reasoning and the numbers.

## Ground rules for anything that goes to print

1. **A JAX-A### behind every print file.** The released marks (A002
   wordmark, A005 key art, A006 avatar) are the only source art. Each
   production file (sticker sheet, button face, HTV cut file, embroidery
   file…) becomes a candidate and gets signed before the machine runs —
   proposed IDs below.
2. **Neon by cut, photo by print.** Slime #39ff14 sits at 99% of sRGB's
   green chroma and Splatter Pink is near the edge — no CMYK, eco-solvent
   or dye-sub process can hit them; they print dull. The neons are
   achievable in **cut vinyl** (fluorescent HTV / adhesive stocks),
   **thread** (neon polyester), **acrylic** (fluorescent cast sheet) and
   **filament**. So: the wordmark on garments is cut, not printed; the
   key-art splat is printed and reads as photo-green, which is fine — it
   is a photo.
3. **Garment colorway is already decided** (swatch notes): blanks in
   Static Gray or Night; shirt-art ink is Bone; the X is always Splatter
   Pink. Light goods (mugs, white stickers) use the sanctioned light-ground
   wordmark — Night letters, pink X.
4. **No faces on merch.** Mark and key art only. The wordmark is never
   stacked, outlined or distressed; splatter lives around it.
5. **Rights gate on the splat.** A005/A006 are built on four keyed
   paintball photos whose source is not recorded in the repo. Confirm the
   licence before anything carrying the splat is *sold*. Fallback if it
   can't be cleared: regenerate the splat with `tools/splat-gen.py` (our
   own code) and sign a v2. Wordmark-only items are clean (Pathway Gothic
   One is SIL OFL).

## The candidates

COGS assume posted makerspace prices plus blanks bought online; sell
prices are whole-dollar, cash-friendly show prices.

| # | Item | Branch / machine | Art | COGS ea | Sell | Round-1 qty | Outlay | Rank |
|---|---|---|---|---|---|---|---|---|
| 1 | **Sticker set** — wordmark kiss-cut 4×1.25", JAX splat die-cut 3", "GET SPLATTERED" QR tile 2.5" | Marksbury Roland, sticker paper $2/ft | A002, A006, A004 QR | $0.06–0.13 | $2 / 3 for $5, free in every bag | ~150 | ~$14 | MUST |
| 2 | **Buttons** — 2.25" JAX avatar pin; 1.25" JAX crop pin | either, button makers | A006, A002 crop | $0.36 / $0.23 | $3 / $2, 2 for $5 | 50 + 50 | ~$30 | MUST |
| 3 | **Tee** — wordmark chest print, 11" wide, two-layer HTV (Bone letters + fluorescent-pink X) on Static Gray / black blank | either, Cricut + auto heat press; BYO blanks + Siser fluorescent HTV | A002 | ~$7 | $25 (tee + beanie $40) | 12 (S1 M3 L4 XL3 2XL1) | ~$95 | MUST |
| 4 | **Beanie** — embroidered wordmark, 3.5" wide, on cuffed charcoal/black beanie | Marksbury embroidery (thread free; BYO neon pink) | A002 | ~$5 | $20 | 12 | ~$60 | STRONG — Oct/Nov shows are cold |
| 5 | **Table banner** — 24×72" wordmark + jaxsplatter.com + QR; doubles as booth front | Eastside HP 24", medium vinyl $4.50/ft | A002, A004 | $27 | display, not for sale | 1 | ~$27 | STRONG |
| 6 | **Acrylic keychain** — 2.5×1" fluorescent pink/green tag, engraved wordmark, edge-lit look | Eastside big laser; BYO 1/8" cast acrylic | A002 | ~$0.50 | $5 | 30 | ~$15 | STRONG — *if acrylic is allowed*; birch-ply fallback |
| 7 | **Key-art print** — 18×18" square A005 on photo paper | Eastside HP 24" photo $2/ft | A005 | $3 | $12 | 10 | ~$30 | BENCH — needs a print-res re-render and the rights gate |
| 8 | **Can cooler** — sublimated light-ground wordmark + "Get Splattered!" on white neoprene | Marksbury sublimation + heat press; BYO blanks | A002 light | ~$1.70 | $5 | 24 | ~$41 | BENCH — easy round-2 add, bar-native |
| 9 | **Mug** — 11 oz white, light-ground wordmark | Marksbury sublimation + mug press; BYO blanks | A002 light | ~$3 | $12 | 12 | ~$36 | BENCH — heavy to haul; Bandcamp item later |
| 10 | **Tote** — black canvas, Bone HTV wordmark | either, Cricut + press | A002 | ~$3 | $12 | 12 | ~$36 | BENCH |
| 11 | **Key-art tee** — full-color A005 as printable HTV, contour-cut | Marksbury Roland heat vinyl $6/ft + press | A005 | ~$8 | $25 | 8 | ~$65 | BENCH — heavier hand than cut HTV; rights gate |
| 12 | **3D-printed JAX tag** — 6 g PLA keychain | either, 3D printer | A002 crop | ~$0.90 | $3 | 20 | ~$18 | BENCH — reads cheaper than acrylic |
| 13 | **Leather-patch beanie** — laser-engraved veg-tan patch, sewn on | Eastside laser + sewing | A002 | ~$6 | $22 | — | LATER — round 2 |
| 14 | **Engraved metal** — anodized dog tags / bottle openers | Marksbury small laser | A002 | ~$1 | $8 | — | LATER |
| 15 | **Kiln / CNC pieces** | Eastside | — | — | — | — | EXPLORE — ask staff what the kiln does |

Same trips, not for sale: **DMX puck enclosures ×2** (~70 g PLA, ~$10.50
each — gate 1 of [dmx-puck.md](dmx-puck.md)), **show flyers** for Oct 24 /
Nov 6 (11×17 on plain paper, ~$0.35 each), the mark engraved into the crew
percussion crate.

## The recommended round

Items 1–6: stickers, buttons, tees, beanies, the banner, keychains.

| | |
|---|---|
| Outlay | ~$240 (materials + blanks; the $8/month credit covers the stickers) |
| Gross at full sell-through | ~$1,025 |
| Break-even sell-through | ~23% |
| Net at full sell-through | ~$785 → funds the crew percussion crate ($200) and starts the stage boxes |

Why this six: two are near-free promo that put the mark on laptops and
jackets (1, 2); two are the garments people actually buy at a show in late
October (3, 4); one makes the table look like the act (5); one is the
cheap impulse item at the register (6). Everything else waits for round 2
or for Bandcamp.

## Proposed sign-off candidates

| Proposed ID | slug | what gets signed |
|---|---|---|
| JAX-A007 | sticker-set | the Roland print+cut sheet: three designs with bleed and CutContour |
| JAX-A008 | button-faces | 2.633" and 1.629" face circles (2.25" and 1.25" makers) |
| JAX-A009 | tee | chest-print spec: 11" wordmark, placement, Bone + fluorescent pink HTV, blank spec |
| JAX-A010 | beanie | embroidery file (PES/DST) + placement, thread colors |
| JAX-A011 | table-banner | 24×72 layout with URL + QR |
| JAX-A012 | keychain | laser cut/engrave file, acrylic color |

Rows land in the registry's Candidates table when the files exist; none
of them exist yet. The wordmark needs a vector export first (Pathway Gothic
One → outlined SVG from `brand/reference/wordmark/jax-wordmark.html`) —
that one file feeds the Cricut, the laser, the Roland and the embroidery
digitizer.

## Schedule against Oct 24

| Week | What | Where |
|---|---|---|
| Sep 14–18 | Sign the agreement; recon visit with the [first-visit checklist](makerspace.md#first-visit-checklist--questions-for-staff); order blanks, HTV, acrylic, beanies (~1 wk delivery). Wordmark SVG + production files → candidates → Jax signs. Optional: Sep 15 button class (Eastside), Sep 17 Cricut class (Marksbury). | both |
| Sep 21–25 | Roland run: stickers + button faces (reserve the printer); press buttons same visit; embroidery test on one beanie. Sep 26–27 weekend (walk-in) for the beanie run. | Marksbury |
| Sep 28–Oct 2 | Laser keychains (reserve); banner on the HP (reserve); tees on the auto press. Oct 3–4 weekend (walk-in) for overflow. | Eastside |
| Oct 5–9 | Fixes and second batch; flyers for Oct 24; puck enclosures. | either |
| Oct 12–16 | Buffer. Oct 17–18 Eastside weekend if needed. | — |
| **Oct 24** | **DILDOZER — the merch table debuts.** | — |
| Oct 26–30 | Restock for Nov 6 Louisville from the sell-through numbers. | both |

Sep 19 (MULTIPASS, stage-managing) stays clear.

## Selling it

- **At the table:** cash box seeded with ones and fives; Square Tap to Pay
  on the phone (no hardware, ~2.6% + a per-tap fee); Venmo / Cash App QR
  on the table sign. Prices on one card in the brand type.
- **Bundles:** tee + beanie $40; any two small items $5; a sticker in every
  bag.
- **Online:** none in round 1. Bandcamp (accounts-inventory row 4, still
  unclaimed) is the round-2 unlock — it is the store and the only platform
  that pays directly.
- **Tax:** Kentucky charges 6% sales tax on tangible goods sold in person;
  registering with the Department of Revenue is a Jax task before Oct 24,
  not something this plan resolves.
- **Books:** `merch/inventory.md` gets created when the run is produced —
  counts in, counts out per show, cash in. Merch income posts to
  `band/instruments/BUDGET.md`'s running total as the reinvestment source.

## Open questions for Jax

- The six-item round, or a different cut of the table? (pick sheet)
- Back print on the tee — "GET SPLATTERED" across the shoulders in
  fluorescent green — yes/no? It's the ratified bio line.
- Blank preference: Bella+Canvas 3001 (softer, ~$7) vs Gildan Softstyle
  (~$4.50) — margin vs hand.
- Who clears the paintball-photo rights (ground rule 5)?
- Is a cast-and-crew making session at the makerspace (10+ needs a call
  ahead) worth doing for the beanie/tee run?

## Pick sheet

**Merch Round 1 Selects** — <https://claude.ai/code/artifact/faad70f9-526b-4f28-b3e4-d7f50a37a18e>
(artifact `faad70f9-526b-4f28-b3e4-d7f50a37a18e`). Tick items, answer the two
tee questions, SAVE; the picks land back here as the round's contents.
