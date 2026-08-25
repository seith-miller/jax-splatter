#!/usr/bin/env python3
"""The Jax Splatter stencil-spray generator.

Simulates the brand splatter effect: a stencil is cut in Unbounded, viscous
neon-green fluid is sprayed across it in arcing ropes with real momentum —
thick at the throw, tapering mid-flight, blobbing at the landing, droplets
trailing — and then the stencil is lifted, leaving the letterforms filled by
whatever landed through the holes.

Deterministic: the same seed always throws the same ropes.

Usage:
  python3 tools/splat-gen.py --text "JAX SPLATTER" --seed 7 --out splat.png
  python3 tools/splat-gen.py --text "JAX" --font path/to/Unbounded.ttf --weight 700

Needs: numpy, opencv-python, pillow, and an Unbounded TTF (default path below,
or pass --font). Output is a transparent RGBA PNG plus a *-preview.png on the
brand Night ground.
"""
import argparse, math, random, pathlib
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

SLIME = (0x14, 0xFF, 0x39)      # BGR of #39ff14
SLIME_RIM = (0x0E, 0xC5, 0x2B)  # darker rim  #2bc50e
SLIME_HI = (0x5A, 0xFF, 0xB4)   # wet highlight #b4ff5a
NIGHT = (0x0A, 0x06, 0x05)      # BGR of #05060a

def text_stencil(text, font_path, weight, width):
    fs = 10 + int(width * 1.1 / max(1, len(text)))
    f = ImageFont.truetype(font_path, fs)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    pad = fs
    img = Image.new('L', (width + 2 * pad, fs * 3), 0)
    d = ImageDraw.Draw(img)
    d.text((pad, fs * 1.5), text, font=f, fill=255, anchor='lm')
    M = np.array(img)
    ys, xs = np.nonzero(M > 127)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    m = 60
    return (M[y0 - m:y1 + m + 1, x0 - m:x1 + m + 1] > 127).astype(np.uint8) * 255

def rope(ink, rng, W, H):
    # one throw: an arcing trajectory with pulsing thickness
    x = rng.uniform(-W * 0.15, W * 0.75)
    y = rng.uniform(H * 0.05, H * 0.75)
    ang = rng.uniform(-0.30, 0.30)
    vx = math.cos(ang) * rng.uniform(W * 0.010, W * 0.016)
    vy = math.sin(ang) * rng.uniform(W * 0.004, W * 0.009)
    g = H * rng.uniform(0.00008, 0.00025)
    base = rng.uniform(H * 0.07, H * 0.15)
    n = rng.randint(60, 110)
    pts = []
    for i in range(n):
        pts.append((x, y))
        x += vx; y += vy; vy += g
        if x > W * 1.1 or y > H * 1.2:
            break
    for i, (px, py) in enumerate(pts):
        t = i / max(1, len(pts) - 1)
        pulse = 0.55 + 0.45 * math.sin(t * rng.uniform(6, 11) + rng.uniform(0, 6))
        r = base * (1.15 - 0.75 * t) * pulse
        cv2.circle(ink, (int(px), int(py)), max(2, int(r)), 255, -1)
        if rng.random() < 0.10:  # trailing droplet, elongated by momentum
            dx, dy = rng.uniform(-1, 1) * r * 3, rng.uniform(0.2, 1.6) * r * 2
            cv2.ellipse(ink, (int(px + dx), int(py + dy)),
                        (max(2, int(r * 0.5)), max(2, int(r * 0.3))),
                        math.degrees(math.atan2(vy, vx)), 0, 360, 255, -1)
    # terminal blob where it lands
    if pts:
        ex, ey = pts[-1]
        cv2.circle(ink, (int(ex), int(ey)), int(base * rng.uniform(1.2, 1.8)), 255, -1)

def generate(text, font_path, weight, width, seed):
    rng = random.Random(seed)
    stencil = text_stencil(text, font_path, weight, width)
    H, W = stencil.shape
    ink = np.zeros((H, W), np.uint8)
    target = 0.72  # keep throwing until the name is legible
    stpx = max(1, int((stencil > 0).sum()))
    for _ in range(40):
        rope(ink, rng, W, H)
        goo_test = cv2.GaussianBlur(ink, (0, 0), 7) > 115
        if (goo_test & (stencil > 0)).sum() / stpx >= target:
            break
    for _ in range(rng.randint(2, 4)):  # loose splats
        cx, cy = rng.uniform(0, W), rng.uniform(0, H)
        for _ in range(rng.randint(4, 8)):
            cv2.circle(ink, (int(cx + rng.uniform(-40, 40)), int(cy + rng.uniform(-30, 30))),
                       rng.randint(8, 30), 255, -1)
    # viscosity: metaball merge
    ink = (cv2.GaussianBlur(ink, (0, 0), 7) > 115).astype(np.uint8) * 255
    # lift the stencil: keep only what landed through the holes (+2px seep)
    seep = cv2.dilate(stencil, np.ones((5, 5), np.uint8))
    body = cv2.bitwise_and(ink, stencil)
    edge_seep = cv2.bitwise_and(ink, cv2.bitwise_xor(seep, stencil))
    final = cv2.bitwise_or(body, edge_seep)
    # spatter that made it through: fine droplets inside unsprayed letter areas
    dry = cv2.bitwise_and(stencil, cv2.bitwise_not(ink))
    ys, xs = np.nonzero(dry)
    if len(xs):
        for _ in range(int(len(xs) * 0.0012)):
            i = rng.randrange(len(xs))
            cv2.circle(final, (xs[i], ys[i]), rng.randint(1, 4), 255, -1)
    # overspray: fine freckle just outside the cut, where mist crept past the stencil
    ring = cv2.subtract(cv2.dilate(stencil, np.ones((41, 41), np.uint8)), seep)
    ry, rx = np.nonzero(cv2.bitwise_and(ring, ink))
    if len(rx):
        for _ in range(min(140, int(len(rx) * 0.004))):
            i = rng.randrange(len(rx))
            cv2.circle(final, (rx[i], ry[i]), rng.randint(1, 5), 255, -1)
    # color: slime body, dark rim, wet highlight
    er = cv2.erode(final, np.ones((7, 7), np.uint8))
    rim = cv2.subtract(final, er)
    e9 = cv2.erode(final, np.ones((11, 11), np.uint8))
    hi = cv2.bitwise_and(e9, cv2.bitwise_not(np.roll(np.roll(e9, 9, 0), 7, 1)))
    out = np.zeros((H, W, 4), np.uint8)
    out[final > 0] = (*SLIME, 255)
    out[rim > 0] = (*SLIME_RIM, 255)
    out[hi > 0] = (*SLIME_HI, 255)
    out[(final == 0)] = (0, 0, 0, 0)
    return out

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--text', default='JAX SPLATTER')
    ap.add_argument('--font', default=str(pathlib.Path(__file__).parent / 'Unbounded.ttf'))
    ap.add_argument('--weight', type=int, default=700)
    ap.add_argument('--width', type=int, default=2200)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--out', default='splat.png')
    a = ap.parse_args()
    img = generate(a.text, a.font, a.weight, a.width, a.seed)
    cv2.imwrite(a.out, img)
    H, W = img.shape[:2]
    prev = np.zeros((H + 240, W + 240, 3), np.uint8)
    prev[:] = NIGHT
    region = prev[120:120 + H, 120:120 + W]
    alpha = img[:, :, 3:4].astype(np.float32) / 255
    prev[120:120 + H, 120:120 + W] = (region * (1 - alpha) + img[:, :, :3] * alpha).astype(np.uint8)
    cv2.imwrite(a.out.replace('.png', '-preview.png'), prev)
    print(f'seed {a.seed} -> {a.out}')
