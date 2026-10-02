#!/usr/bin/env python3
"""The ransom-note merch mark — cut-out letters the way the Punk Freud graphic
did them (interzone/events/multipass/promo/punk_freud_starburst.py): each
letter on its own tile in a different face, a different size, a torn corner
or three, a lean, pasted along a rough baseline. Here the tiles are Splatter
Pink and the letters Night (Jax, 2026-09-30: every letter pink), over the
key-art splat on Night.

Deterministic per --seed. Writes, into brand/reference/ransom/:
  ransom-line_sN.png      JAX SPLATTER, one line   (RGBA, mark only)
  ransom-jax_sN.png       JAX                       (RGBA, mark only)
  ransom-stack_sN.png     JAX over SPLATTER         (RGBA, mark only)
  *_on-splat.png          each composited over the splat mass on Night
Needs Pillow. Fonts: the macOS supplemental set plus tools/*.ttf.
"""
import argparse, math, os, pathlib, random
from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parent
OUT = ROOT / 'brand/reference/ransom'
PINK, NIGHT = (234, 62, 134, 255), (5, 6, 10, 255)
FONTS = [f for f in [
    "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "/System/Library/Fonts/Supplemental/Courier New Bold.ttf",
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/System/Library/Fonts/Supplemental/Impact.ttf",
    "/System/Library/Fonts/Supplemental/Futura.ttc",
    "/System/Library/Fonts/Supplemental/Bodoni 72.ttc",
    "/System/Library/Fonts/Supplemental/Copperplate.ttc",
    "/System/Library/Fonts/Supplemental/Didot.ttc",
    "/System/Library/Fonts/Supplemental/Chalkduster.ttf",
    str(HERE / 'BebasNeue-Regular.ttf'), str(HERE / 'PathwayGothicOne-Regular.ttf'), str(HERE / 'Unbounded.ttf'),
] if os.path.exists(f)]

def ransom(text, cap, rng, tile=PINK, ink=NIGHT, gap=None, pad=None):
    """Cut-out letters on tiles. Returns an RGBA strip with the letters pasted along a rough baseline."""
    pad = pad or int(cap * 0.10); gap = gap if gap is not None else int(cap * 0.035)
    tiles, prev = [], None
    for ch in text:
        if ch == ' ':
            tiles.append(None); continue
        fp = rng.choice([f for f in FONTS if f != prev] or FONTS); prev = fp
        size = rng.randint(int(cap * 0.72), cap)
        font = ImageFont.truetype(fp, size)
        bb = font.getbbox(ch)
        tw, th = bb[2] - bb[0] + 2 * pad, bb[3] - bb[1] + 2 * pad
        t = Image.new('RGBA', (tw, th), tile)
        d = ImageDraw.Draw(t)
        d.text((pad - bb[0], pad - bb[1]), ch, font=font, fill=ink)
        n = int(cap * 0.08)
        for _ in range(3):   # torn corners
            x, y = rng.choice([(0, 0), (tw, 0), (0, th), (tw, th)])
            d.polygon([(x, y), (x + rng.randint(-n, n), y + rng.randint(-n, n)), (x + rng.randint(-int(n*1.4), int(n*1.4)), y + rng.randint(-int(n*1.4), int(n*1.4)))], fill=(0, 0, 0, 0))
        t = t.rotate(rng.uniform(-11, 11), expand=True, resample=Image.BICUBIC)
        tiles.append(t)
    wordgap = int(cap * 0.32)
    width = sum((t.width if t else wordgap) for t in tiles) + gap * (len(tiles) - 1)
    height = max(t.height for t in tiles if t) + int(cap * 0.25)
    strip = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    x = 0
    for t in tiles:
        if t is None: x += wordgap + gap; continue
        y = (height - t.height) // 2 + rng.randint(-int(cap * 0.08), int(cap * 0.08))
        strip.paste(t, (x, y), t); x += t.width + gap
    return strip

def splat_mass(w, h):
    """The key-art composition (key-art.html) without the text: splat-3 twice, on Night."""
    s3 = Image.open(ROOT / 'brand/reference/key-art/splat-3.png').convert('RGBA')
    im = Image.new('RGBA', (1920, 1080), NIGHT)
    a = s3.resize((880, 880), Image.LANCZOS).rotate(-12, expand=True, resample=Image.BICUBIC)
    im.alpha_composite(a, (230 - (a.width - 880) // 2, 100 - (a.height - 880) // 2))
    b = s3.resize((1300, 942), Image.LANCZOS).rotate(152, expand=True, resample=Image.BICUBIC)
    bb = b.copy(); bb.putalpha(b.getchannel('A').point(lambda v: int(v * 0.98)))
    im.alpha_composite(bb, (490 - (b.width - 1300) // 2, 78 - (b.height - 942) // 2))
    return im.resize((w, h), Image.LANCZOS)

def on_splat(mark, scale=0.78):
    bg = splat_mass(1920, 1080)
    k = (1920 * scale) / mark.width
    if mark.height * k > 1080 * 0.86: k = (1080 * 0.86) / mark.height
    m = mark.resize((int(mark.width * k), int(mark.height * k)), Image.LANCZOS)
    bg.alpha_composite(m, ((1920 - m.width) // 2, (1080 - m.height) // 2))
    return bg

def build(seed):
    OUT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed)
    line = ransom('JAX SPLATTER', 420, random.Random(seed))
    jax = ransom('JAX', 520, random.Random(seed + 1))
    top = ransom('JAX', 460, random.Random(seed + 2)); bot = ransom('SPLATTER', 400, random.Random(seed + 3))
    top = top.rotate(-2.5, expand=True, resample=Image.BICUBIC); bot = bot.rotate(1.8, expand=True, resample=Image.BICUBIC)
    sw = max(top.width, bot.width); stack = Image.new('RGBA', (sw, top.height + bot.height - int(460 * 0.12)), (0, 0, 0, 0))
    stack.paste(top, ((sw - top.width) // 2, 0), top); stack.paste(bot, ((sw - bot.width) // 2, top.height - int(460 * 0.12)), bot)
    for name, im in (('line', line), ('jax', jax), ('stack', stack)):
        im.save(OUT / f'ransom-{name}_s{seed}.png')
        on_splat(im, {'line': 0.94, 'jax': 0.52, 'stack': 0.66}[name]).convert('RGB').save(OUT / f'ransom-{name}_s{seed}_on-splat.png')
        print('wrote', f'ransom-{name}_s{seed}.png', im.size)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--seed', type=int, default=7); a = ap.parse_args(); build(a.seed)
