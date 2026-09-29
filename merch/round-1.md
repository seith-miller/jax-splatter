# Merch round 1 — the plan

Drafted 2026-09-10; **the round was decided by Jax the same day** (see "The
round"). The first round of Jax Splatter merchandise, made mostly at the
Lexington Public Library makerspaces ([makerspace.md](makerspace.md)), sized
to be on a table at **DILDOZER, Oct 24** and restocked for **Louisville,
Nov 6**. Per D13, merch is the act's first revenue and it reinvests: this
round's net is earmarked for Phase 1 of the debut build (crew percussion
crate first).

## Ground rules for anything that goes to print

1. **A JAX-A### behind every print file.** The released marks (A002
   wordmark, A005 key art, A006 avatar) are the only source art. Each
   production file (sticker sheet, button face, HTV cut file, marking
   file…) becomes a candidate and gets signed before the machine runs —
   proposed IDs below. That ID is the item's **release number**, printed
   small on the back or edge where it fits; each production run is a
   **batch** of it, logged in `merch/inventory.md`. Unit numbers on the dog
   tags (open series) and the Zippos (edition of 12) in this round.
2. **Neon by cut, photo by print.** Slime #39ff14 sits at 99% of sRGB's
   green chroma and Splatter Pink is near the edge — no CMYK, eco-solvent
   or dye-sub process can hit them; they print dull. The neons are
   achievable in **cut vinyl** (fluorescent HTV / adhesive stocks),
   **thread** (neon polyester), **acrylic** (fluorescent cast sheet),
   **anodized metal**, **filament** and **fluorescent plastisol** (screen
   print). So: the wordmark on garments is cut or screened, not CMYK; the
   key-art splat is printed and reads as photo-green, which is fine — it
   is a photo.
3. **Garment colorway per the swatch notes** as the starting point: blanks
   in Static Gray or Night; shirt-art ink Bone; the X always Splatter Pink.
   Light goods (can coolers, white stickers) use the sanctioned
   light-ground wordmark — Night letters, pink X. The tee design pass may
   revise the garment rule; it revises it in the registry, not on the press.
4. **No faces on merch.** Mark and key art only. The wordmark is never
   stacked, outlined or distressed; splatter lives around it.
5. **Rights gate on the splat.** A005/A006 are built on four keyed
   paintball photos whose source is not recorded in the repo. Confirm the
   licence before anything carrying the splat is *sold*. Fallback if it
   can't be cleared: regenerate the splat with `tools/splat-gen.py` (our
   own code) and sign a v2. Wordmark-only items are clean (Pathway Gothic
   One is SIL OFL).

## The round (Jax, 2026-09-10)

Stickers · buttons · dog tags · tote bags · lighters (two kinds) · can coolers.

**Two lighters (Jax, 2026-09-28):** vinyl-wrapped Bic-style plastic at $3, and
laser-engraved Zippos as a numbered edition at $40. The Zippo is the round's
first limited edition.

**Magnets shelved (Jax, 2026-09-28)** — same press and face as the buttons,
so they're a one-visit add whenever wanted.

**Tees swapped for totes (Jax, 2026-09-10):** one SKU, no sizes, the library
makes the whole run, flat canvas takes the neon and the stencil process
better than a knit. The tee moves to round 2 with the design pass it
deserves.

**Button standard (Jax, 2026-09-10): one size, 2.25".** It is the only size
both branches stock, it fits the A006 avatar and the full wordmark legibly,
and one face template (2.633" circle) serves buttons — and magnets, if they come back.

| Item | Make | COGS ea | Sell | Qty | Outlay | Gross at sell-through | Status |
|---|---|---|---|---|---|---|---|
| **Stickers** — two designs (Jax, 2026-09-10): wordmark kiss-cut 4×1.25" with jaxsplatter.com small beneath; JAX splat die-cut 3". QR tile dropped. | Marksbury Roland, sticker paper $2/ft | $0.06–0.13 | $2 · 3/$5 · free in every bag | ~150 (90 + 60) | ~$12 | ~$85 (50 sold) | ready to file |
| **Buttons** — 2.25" only (the one size both branches have); avatar face | either branch, 2.25" button maker | ~$0.36 | $3 · 2/$5 | 50 | ~$18 | ~$125 | ready to file |
| **Dog tags** — colored anodized aluminum blanks (50×29×2 mm, ~100/pack with chains), laser-marked, numbered | either laser; test one tag first (painted vs anodized) | ~$0.30 | $8 | 30 | ~$25 (one pack) | ~$240 | blank candidate found (Jax, 2026-09-10); pink or black, not green |
| **Tote bag** — heavyweight black canvas (10–12 oz, ~15×16"), wordmark in Bone HTV + pink X, or the wall-splat stencil | Cricut HTV / stencil mask + fabric spray, either branch; BYO blanks | ~$3.50 | $15 | 24 | ~$85 | ~$360 | design pick (HTV vs stencil) then file |
| **Lighters, wrapped** — Bic-style plastic, full vinyl wrap (~2.9×2.1" around the body) | Marksbury Roland: printed on sticker stock, contour-cut, laminated if the branch has it; fallback Cricut permanent vinyl (cut, true neon) | ~$1.00 | $3 | 50 | ~$50 | ~$150 | ready to file |
| **Lighters, Zippo** — genuine matte-black Zippo (218), wordmark laser-engraved on the lid, unit-numbered on the base | either laser; insert out, unfueled, in a jig | ~$20 | $40 | 12 (edition 1) | ~$240 | ~$480 | blank to order; test one |
| **Can coolers** — light-ground wordmark + "Get Splattered!" on white neoprene | Marksbury sublimation + heat press; BYO blanks | ~$1.70 | $5 | 24 | ~$41 | ~$120 | ready to file |

| | Round 1 |
|---|---|
| Outlay | ~$480 (half of it the twelve Zippos) |
| Gross at full sell-through | ~$1,450 |
| Break-even sell-through | ~33% |

**Table kit, not merch (confirm):** 24×72" wordmark banner with URL + QR on
the Eastside HP (~$27) and a price card in the brand type. The table has to
look like the act.

**On hold:** beanies, hats and patches — wait for the embroidery machine
landing later in September (Jax, 2026-09-10). Marksbury already lists one;
the hold stands regardless.

**Out of round 1:** the T-shirt (round 2, after the design pass — see
below), acrylic keychains (dog tags own that slot), key-art print (needs
print-res re-render + the rights gate), mugs, key-art printable-HTV tee,
3D-printed tags, kiln/CNC pieces. Bench for round 2.

Same trips, not for sale: **DMX puck enclosures ×2** (~70 g PLA, ~$10.50
each — gate 1 of [dmx-puck.md](dmx-puck.md)), **show flyers** for Oct 24 /
Nov 6 (11×17 on plain paper, ~$0.35 each), the mark engraved into the crew
percussion crate.

## The two open design threads

**The tee (round 2).** The flagship, not a line item: the surface people wear for
years and the one that carries the brand into rooms Jax isn't in. Great band
tees are an artwork with a name attached, not a logo alone. The library can
cut one or two flat neon colors (HTV) or cut the letters as a **stencil
mask** for fluorescent fabric spray — which is the wall-splat process
(`tools/wall-splat.py`) applied to a shirt: the blank is the wall, a pink
streak, the name as negative space, slime thrown over. Neither branch screen
prints; a production run of two-color fluorescent plastisol is the standard
route at ~$10/shirt. Plan: library = prototype shop (3–4 samples across
directions, worn and photographed), then decide production — after round 1.
Open: wordmark vs artwork front; blank (Static Gray vs black); cut (unisex vs
crop/tank — the scene buys both); back copy ("GET SPLATTERED!" / "NEON GLITCH
SLUT POP", both ratified lines). Next step once Jax answers "wordmark or
artwork": a tee pick sheet, 4–6 directions rendered on the blank. The
tote is the first test of that same question at lower stakes: HTV wordmark
versus the wall-splat stencil on canvas.

**The dog tag.** In. The effect decides the process:

| Effect wanted | Process | Where |
|---|---|---|
| Military authenticity — stamped steel, the rattle | embossing machine (neither branch) or hand letter-punches at home (rough, punk) | home / supplier |
| Neon brand object — pink or slime tag, silver letters | laser-engraved anodized aluminum (dye removal) | either laser |
| Crew token — numbered stainless, cast wears theirs first | IR/fiber marking on bare steel; verify Marksbury's small laser has it (it sells metal keychain blanks) | Marksbury |

Blank found (Jax, 2026-09-10): colored anodized aluminum, 50×29×2 mm, ~100
per pack with ball chains — route 2. Pink or black, not green (anodized green
is emerald, not Slime). Test one tag before the run: painted blanks flake.

### Numbering — how it works

Dog tags are an **open series** — unit-numbered, no cap (Jax, 2026-09-28:
most items carry only a release number and a batch; unit numbers are for
limited editions and open series like this one — see
[tiers.md](tiers.md)). One continuous tag series for the life of the act,
every tag unique, never reissued. Three digits with leading zeros
(001–999); the day it passes 999 is a good day. Round 1 = batch 1 of the
series (021–050).

| Block | Who | Rule |
|---|---|---|
| 001 | Jax | — |
| 002–020 | the cast — band, dancers, guest vocalists, crew | assigned as people join; a tag is how you know you're in the crew (stage-vision's rotating cast, made physical) |
| 021 → | fans, in order sold | round 1 = 021–050 |

- **Register:** `merch/dog-tags.md` — number → cast name, or show + date
  sold (buyer anonymous unless they want in). Updated after every show; it
  is the crew roster and the sales log in one table.
- **Layout:** front — wordmark, number small at the bottom edge (visible
  when worn; the number is the point). Back — the GI five-line block:
  SPLATTER, JAX / No. ### / GET SPLATTERED / NEON GLITCH SLUT POP /
  JAXSPLATTER.COM.
- **The file:** one signed marking file (JAX-A010) with a `{NUMBER}` field.
  If the library runs LightBurn, its Variable Text does serials natively
  (CSV or auto-increment) — one job, thirty numbers. If it runs xTool
  Creative Space or similar, `tools/dog-tag-gen.py` (to write) emits one
  SVG per number laid onto the jig positions.
- **The jig:** laser-cut 3 mm MDF or chipboard with 50×29 mm pockets, cut
  on the Eastside laser in the same reservation. Tags drop in, batch
  engraves front; flip each in place, batch engraves back. ~30–60 s per
  face; a run of 30 is one reservation.
- **Gates, in order:** buy one pack → mark one tag (anodized vs painted)
  → sign A010 with the numbering scheme → cut the jig → run 021–050 →
  cast tags 001–020 as the roster fills.

## Proposed sign-off candidates

| Proposed ID | slug | what gets signed |
|---|---|---|
| JAX-A007 | sticker-set | the Roland print+cut sheet: two designs with bleed and CutContour |
| JAX-A008 | button-face | one 2.633" face circle for the 2.25" maker |
| JAX-A009 | tote | the tote art: HTV cut file or stencil mask, placement, blank spec |
| JAX-A010 | dog-tag | marking file, both faces, numbering scheme |
| JAX-A011 | lighter-wrap | full-wrap print+cut file for the Bic body |
| JAX-A013 | zippo | lid engraving file + base numbering |
| JAX-A012 | can-cooler | light-ground sublimation wrap |
| JAX-A014 | table-banner | 24×72 layout with URL + QR (if confirmed) |

Rows land in the registry's Candidates table when the files exist; none
of them exist yet. The wordmark needs a vector export first (Pathway Gothic
One → outlined SVG from `brand/reference/wordmark/jax-wordmark.html`) —
that one file feeds the Cricut, the lasers, the Roland and the sublimation
wrap.

## Schedule

Superseded 2026-09-28 by [implementation.md](implementation.md) — the
run sheet across Oct 24, Nov 6 and Dec 19, with orders, visits, gates.

## Selling it

- **At the table:** cash box seeded with ones and fives; Square Tap to Pay
  on the phone (no hardware, ~2.6% + a per-tap fee); Venmo / Cash App QR
  on the table sign. Prices on one card in the brand type.
- **Bundles:** any two small items $5; a sticker in every bag; tote + tag
  $20.
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

- Tote art: HTV wordmark or the wall-splat stencil? (two samples first)
- Tee, round 2: wordmark front, or an artwork the name rides on?
- Dog tag: which of the three effects?
- Table banner — confirm as table kit?
- Who clears the paintball-photo rights (ground rule 5)?

## Pick sheet

**Merch Round 1 Selects** — <https://claude.ai/code/artifact/faad70f9-526b-4f28-b3e4-d7f50a37a18e>
(artifact `faad70f9-526b-4f28-b3e4-d7f50a37a18e`). The round was picked in
chat 2026-09-10; the sheet is republished with those picks baked in and
stands as the record of the options considered.
