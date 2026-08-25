#!/usr/bin/env python3
"""The Jax Splatter wall process — negative-space wordmark.

Models the physical process, in order:
  1. the wall           — Static Gray, faint texture
  2. lay the decals     — letters cut in Unbounded, stuck to the wall
  3. the streak         — one horizontal pass with a spray can (Splatter Pink)
  4. lift the decals    — the name appears as clean negative space
  5. the goo            — neon green fluid thrown across the top

Deterministic per --seed. Writes the final PNG plus a *-process.png strip
showing every stage.

Usage: python3 tools/wall-splat.py --text "JAX SPLATTER" --seed 7 --out wall.png
Needs: numpy, opencv-python, pillow, tools/Unbounded.ttf.
"""
import argparse, math, random, pathlib
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

GRAY = (0x5C, 0x4C, 0x45)       # BGR #454c5c  Static Gray
PINK = (0x86, 0x3E, 0xEA)       # BGR #ea3e86  Splatter Pink
PINK_DEEP = (0x5E, 0x29, 0xB7)  # BGR #b7295e
SLIME = (0x14, 0xFF, 0x39)      # BGR #39ff14
SLIME_RIM = (0x0E, 0xC5, 0x2B)
SLIME_HI = (0x5A, 0xFF, 0xB4)

def letters_mask(text, font_path, weight, W, H):
    fs = 10 + int(W * 0.92 / max(1, len(text)))
    f = ImageFont.truetype(font_path, fs)
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    img = Image.new('L', (W, H), 0)
    ImageDraw.Draw(img).text((W // 2, H // 2), text, font=f, fill=255, anchor='mm')
    return (np.array(img) > 127).astype(np.uint8) * 255

def wall(W, H, rng):
    base = np.zeros((H, W, 3), np.float32); base[:] = GRAY
    noise = rng_noise(W, H, rng, 3.0) * 14 - 7
    return np.clip(base + noise[..., None], 0, 255)

def rng_noise(W, H, rng, sigma):
    n = np.random.default_rng(rng.randrange(1 << 30)).normal(0.5, 0.22, (H, W)).astype(np.float32)
    return np.clip(cv2.GaussianBlur(n, (0, 0), sigma), 0, 1)

def spray_streak(W, H, band_y, band_h, rng):
    """density 0..1 of one horizontal spray-can pass"""
    acc = np.zeros((H, W), np.uint8)
    for p in range(2):
        y = band_y + rng.uniform(-0.08, 0.08) * band_h
        amp = band_h * rng.uniform(0.05, 0.14)
        ph = rng.uniform(0, 6)
        r = int(band_h * rng.uniform(0.42, 0.5))
        for x in range(-r, W + r, max(6, r // 14)):
            yy = y + amp * math.sin(x / (W * 0.11) + ph) + rng.uniform(-8, 8)
            cv2.circle(acc, (x, int(yy)), r, 255, -1)
    d = cv2.GaussianBlur(acc.astype(np.float32) / 255, (0, 0), band_h * 0.09)
    d *= 0.72 + 0.28 * rng_noise(W, H, rng, 2.2)          # spray grain
    edge = (d > 0.04) & (d < 0.30)
    ys, xs = np.nonzero(edge)                              # spatter dots at the fringe
    if len(xs):
        dots = np.zeros((H, W), np.uint8)
        for _ in range(int(len(xs) * 0.004)):
            i = rng.randrange(len(xs))
            cv2.circle(dots, (xs[i], ys[i]), rng.randint(1, 4), 255, -1)
        d = np.maximum(d, dots.astype(np.float32) / 255 * rng.uniform(0.5, 0.8))
    return np.clip(d, 0, 1)

def goo(W, H, band_y, rng):
    ink = np.zeros((H, W), np.uint8)
    for _ in range(rng.randint(3, 4)):
        x = rng.uniform(-W * 0.1, W * 0.6)
        y = band_y + rng.uniform(-0.9, 0.4) * H * 0.22
        vx = rng.uniform(W * 0.010, W * 0.016)
        vy = rng.uniform(-H * 0.004, H * 0.006)
        g = H * rng.uniform(0.0002, 0.0005)
        base = rng.uniform(H * 0.030, H * 0.055)
        pts = []
        for i in range(rng.randint(60, 100)):
            pts.append((x, y)); x += vx; y += vy; vy += g
            if x > W * 1.1 or y > H * 1.2: break
        for i, (px, py) in enumerate(pts):
            t = i / max(1, len(pts) - 1)
            pulse = 0.55 + 0.45 * math.sin(t * rng.uniform(6, 11) + rng.uniform(0, 6))
            r = base * (1.15 - 0.75 * t) * pulse
            cv2.circle(ink, (int(px), int(py)), max(2, int(r)), 255, -1)
            if rng.random() < 0.10:
                cv2.circle(ink, (int(px + rng.uniform(-3, 3) * r), int(py + rng.uniform(0.5, 2.5) * r)),
                           max(1, int(r * rng.uniform(0.2, 0.45))), 255, -1)
        if pts:
            cv2.circle(ink, (int(pts[-1][0]), int(pts[-1][1])), int(base * rng.uniform(1.2, 1.7)), 255, -1)
    return (cv2.GaussianBlur(ink, (0, 0), 6) > 115).astype(np.uint8) * 255

def compose(text, font_path, weight, W, H, seed):
    rng = random.Random(seed)
    stages = []
    img = wall(W, H, rng); stages.append(img.copy())
    letters = letters_mask(text, font_path, weight, W, H)
    band_y, band_h = H * 0.5, H * 0.42
    # stage: decals on the wall (barely visible — matte vinyl)
    decal = img.copy(); decal[letters > 0] = np.clip(decal[letters > 0] + 10, 0, 255)
    stages.append(decal)
    # the streak, over wall AND decals
    d = spray_streak(W, H, int(band_y), int(band_h), rng)
    pink = np.zeros_like(img); pink[:] = PINK
    deep = np.zeros_like(img); deep[:] = PINK_DEEP
    paint = deep + (pink - deep) * np.clip(d * 2.1, 0, 1)[..., None]
    cover = np.clip(d * 1.8, 0, 1)[..., None]
    sprayed = decal * (1 - cover) + paint * cover
    stages.append(sprayed.copy())
    # lift the decals: letter areas return to clean wall (crisp edge, faint seep)
    lifted = sprayed.copy()
    lifted[letters > 0] = img[letters > 0]
    ring = cv2.subtract(letters, cv2.erode(letters, np.ones((7, 7), np.uint8)))
    seep = (ring > 0) & (rng_noise(W, H, rng, 1.2) < 0.30) & (d > 0.15)
    lifted[seep] = sprayed[seep]
    stages.append(lifted.copy())
    # the goo on top of everything
    G = goo(W, H, band_y, rng)
    er = cv2.erode(G, np.ones((7, 7), np.uint8))
    rim = cv2.subtract(G, er)
    e9 = cv2.erode(G, np.ones((11, 11), np.uint8))
    hi = cv2.bitwise_and(e9, cv2.bitwise_not(np.roll(np.roll(e9, 8, 0), 6, 1)))
    final = lifted.copy()
    final[G > 0] = SLIME; final[rim > 0] = SLIME_RIM; final[hi > 0] = SLIME_HI
    stages.append(final)
    return [s.astype(np.uint8) for s in stages]

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--text', default='JAX SPLATTER')
    ap.add_argument('--font', default=str(pathlib.Path(__file__).parent / 'Unbounded.ttf'))
    ap.add_argument('--weight', type=int, default=700)
    ap.add_argument('--width', type=int, default=2600)
    ap.add_argument('--height', type=int, default=900)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--out', default='wall.png')
    a = ap.parse_args()
    stages = compose(a.text, a.font, a.weight, a.width, a.height, a.seed)
    cv2.imwrite(a.out, stages[-1])
    strip = np.vstack([cv2.resize(s, (a.width // 2, a.height // 2)) for s in stages])
    cv2.imwrite(a.out.replace('.png', '-process.png'), strip)
    print(f'seed {a.seed} -> {a.out} (+ process strip)')
