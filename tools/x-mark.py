#!/usr/bin/env python3
"""The X mark — typewriter letters with one big X in a different face, over a
splat mass that fully surrounds the text (Jax, 2026-09-30: "most of the text
the typewriter font, just the X larger and in the first font; the text always
fully surrounded by the splatter").

Letters: Special Elite (Apache 2.0), One-Sheet cream. The X: Rubik Spray Paint
(OFL) by default, Splatter Pink, ~1.55x the cap height. Mass: splat-3 from the
key art, placed along the text until the goo encloses it with margin, on Night.
Deterministic per --seed. Writes into brand/reference/x-mark/.

  python3 tools/x-mark.py [--seed 7] [--xface spray|distressed]
"""
import argparse, math, pathlib, random
from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parent
OUT = ROOT / 'brand/reference/x-mark'
NIGHT, SHEET, PINK = (5, 6, 10, 255), (242, 239, 233, 255), (234, 62, 134, 255)
BASE = HERE / 'SpecialElite-Regular.ttf'
XFACES = {'spray': HERE / 'RubikSprayPaint-Regular.ttf', 'distressed': HERE / 'RubikDistressed-Regular.ttf'}
SPLAT = ROOT / 'brand/reference/key-art/splat-3.png'

def glyph(ch, font_path, size, fill):
    f = ImageFont.truetype(str(font_path), size); bb = f.getbbox(ch)
    im = Image.new('RGBA', (bb[2] - bb[0] + 4, bb[3] - bb[1] + 4), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((2 - bb[0], 2 - bb[1]), ch, font=f, fill=fill)
    return im, bb

def line(text, cap, xface, xscale=1.55, track=0.06):
    """Render `text` with every X in the accent face at xscale. Returns RGBA, baseline-aligned."""
    base = ImageFont.truetype(str(BASE), cap); asc = base.getbbox('H')[3]   # cap height in px (Special Elite H)
    pieces, x = [], 0
    for ch in text:
        if ch == ' ': x += int(cap * 0.45); continue
        if ch == 'X':
            g, bb = glyph('X', xface, int(cap * xscale), PINK); pieces.append((g, x, bb)); x += g.width - 4 + int(cap * track * 1.5)
        else:
            g, bb = glyph(ch, BASE, cap, SHEET); pieces.append((g, x, bb)); x += g.width - 4 + int(cap * track)
    w = x; h = max(g.height for g, _, _ in pieces) + int(cap * 0.3)
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    # align on a common baseline: each glyph's bottom = baseline (bb[3] is bottom in font units at its own size)
    baseline = int(h * 0.78)
    for g, gx, bb in pieces:
        if g.width > cap * 0.9 and bb[3] - bb[1] > cap * 1.2:      # the big X: centre it on the cap height, not the baseline
            im.alpha_composite(g, (gx, baseline - asc // 2 - (g.height - 4) // 2 - 2))
        else:
            im.alpha_composite(g, (gx, baseline - (g.height - 2)))
    return im

def stack(top, bottom):
    w = max(top.width, bottom.width); overlap = int(min(top.height, bottom.height) * 0.10)
    im = Image.new('RGBA', (w, top.height + bottom.height - overlap), (0, 0, 0, 0))
    im.alpha_composite(top, ((w - top.width) // 2, 0)); im.alpha_composite(bottom, ((w - bottom.width) // 2, top.height - overlap)); return im

def mass_around(box_w, box_h, rng, margin=0.28):
    """A splat mass that encloses a box_w x box_h text box with `margin` (fraction of box_h) on every side."""
    s3 = Image.open(SPLAT).convert('RGBA')
    W = int(box_w * (1 + 2 * margin) + box_h * 1.2); H = int(box_h * (1 + 2 * margin) + box_h * 1.4)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    size = int(box_h * 2.6)                                   # each splat ~2.6x the text height
    n = max(2, math.ceil(box_w / (size * 0.42)) + 1)          # overlap along the width
    for i in range(n):
        cx = int(W * 0.5 - box_w * 0.5 + i * (box_w / max(1, n - 1))) if n > 1 else W // 2
        cy = H // 2 + rng.randint(-int(box_h * 0.15), int(box_h * 0.15))
        sp = s3.resize((size, size), Image.LANCZOS).rotate(rng.uniform(0, 360), expand=True, resample=Image.BICUBIC)
        a = sp.getchannel('A').point(lambda v: int(v * rng.uniform(0.92, 1.0))); sp.putalpha(a)
        im.alpha_composite(sp, (cx - sp.width // 2, cy - sp.height // 2))
    return im

def compose(mark, seed, frame=(1920, 1080)):
    rng = random.Random(seed)
    m = mass_around(mark.width, mark.height, rng)
    canvas = Image.new('RGBA', m.size, (0, 0, 0, 0)); canvas.alpha_composite(m, (0, 0))
    canvas.alpha_composite(mark, ((m.width - mark.width) // 2, (m.height - mark.height) // 2))
    # fit into the frame on Night
    k = min(frame[0] * 0.92 / canvas.width, frame[1] * 0.92 / canvas.height)
    c = canvas.resize((int(canvas.width * k), int(canvas.height * k)), Image.LANCZOS)
    bg = Image.new('RGBA', frame, NIGHT); bg.alpha_composite(c, ((frame[0] - c.width) // 2, (frame[1] - c.height) // 2))
    return canvas, bg

def build(seed, xface_key):
    OUT.mkdir(parents=True, exist_ok=True); xf = XFACES[xface_key]
    forms = {'line': line('JAX SPLATTER', 300, xf), 'jax': line('JAX', 420, xf), 'stack': stack(line('JAX', 360, xf), line('SPLATTER', 300, xf))}
    for name, mark in forms.items():
        transparent, framed = compose(mark, seed + hash(name) % 97)
        transparent.save(OUT / f'x-mark-{name}_{xface_key}_s{seed}.png'); framed.convert('RGB').save(OUT / f'x-mark-{name}_{xface_key}_s{seed}_framed.png')
        print('wrote', name, xface_key, transparent.size)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--seed', type=int, default=7); ap.add_argument('--xface', choices=list(XFACES), default='spray')
    a = ap.parse_args(); build(a.seed, a.xface)
