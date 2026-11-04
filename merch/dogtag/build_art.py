#!/usr/bin/env python3
"""Draw the Jax tag's art into art/: filled M/L/Z paths, as scripts/dogtag wants.

    uv run --no-project --with fonttools --with shapely --with pillow --with numpy --with opencv-python-headless merch/dogtag/build_art.py

Wordmark from brand/reference/wordmark (JAX-A002), text in Bebas Neue (JAX-A003).
The long tag is JAX-A006 cut to one colour; the splat images are Jax's own.
"""
import math, os, re, sys
from pathlib import Path

import cv2
import numpy as np
from fontTools.pens.recordingPen import RecordingPen
from fontTools.svgLib.path import parse_path
from fontTools.ttLib import TTFont
from PIL import Image, ImageChops
from shapely import affinity
from shapely.geometry import Point, Polygon
from shapely.ops import unary_union

# the blank's outline and hole come from smart-part's dog tag library
sys.path.insert(0, os.path.expanduser(os.environ.get("DOGTAG_LIB", "~/Code/smart-part/scripts/dogtag")))
import tag as dogtag  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
JAX_W_MM = 15.7  # how wide JAX runs on the tag: the dial for how far the splat bleeds
ANGLE = 45       # degrees, rising left to right as it hangs
DROP_MM = -1.5    # the mark's centre below the middle of the room under the hole
BOLD_PX = 11     # added all round each letter, avatar px
TAG_PX = 40      # art px per tag mm
EDGE_MM = 0.2    # the engraving stops this far inside the outline, off the rack
HOLE_CLEAR_MM = 0.7   # and this far from the chain hole and its peg
MIN_MM = 0.18   # the finest stroke or gap kept
JAX_BOX = (695, 827, 647)   # x, top, width of JAX in A006, measured from the release


def PX_MM_FOR(jax_w_mm):
    return JAX_BOX[2] / jax_w_mm


def flatten(rec, steps=10):
    """A pen recording -> closed polylines."""
    out, cur, pos = [], [], (0, 0)
    for op, a in rec.value:
        if op == "moveTo":
            cur, pos = [a[0]], a[0]
        elif op == "lineTo":
            cur.append(a[0]); pos = a[0]
        elif op == "qCurveTo":
            pts = list(a)
            while pts:
                c = pts.pop(0)
                e = pts[0] if len(pts) == 1 else ((c[0] + pts[0][0]) / 2, (c[1] + pts[0][1]) / 2)
                if len(pts) == 1:
                    pts.pop(0)
                for s in range(1, steps + 1):
                    t = s / steps; u = 1 - t
                    cur.append((u*u*pos[0] + 2*u*t*c[0] + t*t*e[0], u*u*pos[1] + 2*u*t*c[1] + t*t*e[1]))
                pos = e
        elif op == "curveTo":
            p1, p2, p3 = a
            for s in range(1, steps + 1):
                t = s / steps; u = 1 - t
                cur.append(tuple(u**3*pos[i] + 3*u*u*t*p1[i] + 3*u*t*t*p2[i] + t**3*p3[i] for i in (0, 1)))
            pos = p3
        elif op in ("closePath", "endPath"):
            if len(cur) > 2:
                out.append(cur)
            cur = []
    return out


def evenodd(rings):
    g = Polygon()
    for r in rings:
        g = g.symmetric_difference(Polygon(r).buffer(0))
    return g


def wordmark(name="jax-wordmark-cut"):
    """JAX-A002 as signed: the outlined vectors, never reset or restacked."""
    src = (ROOT / f"brand/reference/wordmark/svg/{name}.svg").read_text()
    glyphs = []
    for d in re.findall(r' d="([^"]+)"', src):
        rec = RecordingPen(); parse_path(d, rec)
        glyphs.append(evenodd(flatten(rec)))
    return unary_union(glyphs)


FONT = TTFont(ROOT / "tools/BebasNeue-Regular.ttf")


def text(s, size=1000.0, tracking=0):
    """Bebas Neue, baseline at y=0, y down."""
    gs, cmap, upm = FONT.getGlyphSet(), FONT.getBestCmap(), FONT["head"].unitsPerEm
    x, parts = 0, []
    for ch in s:
        g = gs[cmap[ord(ch)]]
        rec = RecordingPen(); g.draw(rec)
        rings = flatten(rec)
        if rings:
            parts.append(affinity.translate(evenodd(rings), x, 0))
        x += g.width + tracking
    k = size / upm
    return affinity.scale(unary_union(parts), k, -k, origin=(0, 0))


def avatar(px_mm):
    """JAX-A006 as one engraving: its splat composition (jax-avatar-keyart.html,
    same layers and transforms) cut to a silhouette, JAX on it in a dark halo.
    Returns (letters, splat) in the avatar's 2048 px."""
    key = ROOT / "brand/reference/key-art"
    src = Image.open(key / "splat-3.png").getchannel("A")
    mask = Image.new("L", (2048, 2048), 0)
    for (x, y, w, h, deg) in ((220, 345, 1625, 1625, 9), (69, 269, 1950, 1500, -152)):
        pad = 900     # room to turn about the layer's own centre, as CSS does
        layer = Image.new("L", (w + 2 * pad, h + 2 * pad), 0)
        layer.paste(src.resize((w, h), Image.LANCZOS), (pad, pad))
        layer = layer.rotate(-deg, Image.BICUBIC)
        mask = ImageChops.lighter(mask, ImageChops.offset(Image.new("L", mask.size), 0, 0))
        canvas = Image.new("L", (2048, 2048), 0)
        canvas.paste(layer, (x - pad, y - pad))
        mask = ImageChops.lighter(mask, canvas)
    bw = (np.array(mask) > 128).astype(np.uint8)
    # what a laser can hold: nothing finer than MIN_MM, in either direction
    r = max(1, round(MIN_MM * px_mm / 2))
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))
    bw = cv2.morphologyEx(cv2.morphologyEx(bw, cv2.MORPH_OPEN, k), cv2.MORPH_CLOSE, k)
    cs, tree = cv2.findContours(bw, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    least = math.pi * (MIN_MM * px_mm / 2) ** 2
    polys = []
    for i, c in enumerate(cs):
        if tree[0][i][3] != -1 or len(c) < 8 or cv2.contourArea(c) < least:
            continue
        holes, j = [], tree[0][i][2]
        while j != -1:
            if len(cs[j]) >= 8 and cv2.contourArea(cs[j]) >= least:
                holes.append(cs[j][:, 0].tolist())
            j = tree[0][j][0]
        polys.append(Polygon(c[:, 0].tolist(), holes).buffer(0))
    splat = unary_union(polys).simplify(0.8)
    letters = fit_w(wordmark("jax-avatar-cut"), JAX_BOX[2])
    letters = affinity.translate(letters, JAX_BOX[0], JAX_BOX[1])
    # Jax asked for bold, 2026-11-04; the font has one weight, so the outlines are thickened
    letters = letters.buffer(BOLD_PX, join_style=2, mitre_limit=3)
    # A002's light-ground form: the letters stay dark, the bright splat is the ground
    return letters, splat.union(letters.buffer(1.2 * px_mm)).difference(letters)


def fit_w(g, w):
    x0, y0, x1, y1 = g.bounds
    k = w / (x1 - x0)
    return affinity.translate(affinity.scale(g, k, k, origin=(x0, y0)), -x0, -y0)


def rings(g):
    polys = [g] if g.geom_type == "Polygon" else list(g.geoms)
    d = []
    for p in polys:
        for r in [p.exterior, *p.interiors]:
            pts = list(r.coords)[:-1]
            d.append("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z")
    return " ".join(d)


def write(name, parts, anchor=None):
    allg = unary_union(list(parts.values()))
    x0, y0, x1, y1 = allg.bounds
    w, h = x1 - x0, y1 - y0
    pin = f' data-anchor="{anchor[0]-x0:.0f} {anchor[1]-y0:.0f}"' if anchor else ""
    body = "\n".join(
        f'<path fill="#000000" fill-rule="evenodd" data-part="{k}" '
        f'd="{rings(affinity.translate(g, -x0, -y0).simplify(0.35))}"/>' for k, g in parts.items())
    (HERE / "art" / f"{name}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}"{pin}>\n{body}\n</svg>\n')


def bled(jax_w_mm=JAX_W_MM, angle=ANGLE):
    """A006 on the tag, tilted and big enough that the splat runs off the edge:
    clipped to the outline and clear of the hole, in px at TAG_PX per mm, hole left."""
    letters, splat = avatar(PX_MM_FOR(jax_w_mm))
    k = jax_w_mm / JAX_BOX[2] * TAG_PX
    cx, cy = (letters.bounds[0] + letters.bounds[2]) / 2, (letters.bounds[1] + letters.bounds[3]) / 2

    def on_tag(g):
        g = affinity.rotate(g, -angle, origin=(cx, cy))         # y down: minus reads rising
        g = affinity.translate(affinity.scale(g, k, k, origin=(cx, cy)), -cx, -cy)
        # hanging frame, hole up -> tag frame, hole left
        along = (dogtag.HOLE_X + dogtag.HOLE_D / 2 + dogtag.TAG_W) / 2 + DROP_MM
        return affinity.affine_transform(g, [0, 1, -1, 0, along * TAG_PX, dogtag.TAG_H / 2 * TAG_PX])

    blank = Polygon([(x * TAG_PX, y * TAG_PX) for x, y in dogtag.outline_points(EDGE_MM, 24)])
    hole = Point(dogtag.HOLE_X * TAG_PX, dogtag.TAG_H / 2 * TAG_PX).buffer((dogtag.HOLE_D / 2 + HOLE_CLEAR_MM) * TAG_PX)
    room = blank.difference(hole)
    return on_tag(splat).intersection(room)


def main():
    splat = bled()
    w, h = dogtag.TAG_W * TAG_PX, dogtag.TAG_H * TAG_PX
    # what can be cut cleanly: no pinched corners, slivers or specks, and each shape and hole big enough
    least = math.pi * (MIN_MM * TAG_PX / 2) ** 2
    e = 0.06 * TAG_PX
    clean = splat.buffer(-e).buffer(2 * e).buffer(-e).simplify(0.5)
    keep = []
    for g in getattr(clean, "geoms", [clean]):
        if g.area < least:
            continue
        keep.append(Polygon(g.exterior, [r for r in g.interiors if Polygon(r).area >= least]).buffer(0))
    print(f"{len(keep)} shapes, {sum(len(g.interiors) for g in keep)} holes")
    body = "\n".join(f'<path fill="#000000" fill-rule="evenodd" data-part="{n}" d="{rings(g)}"/>'
                     for n, g in (("insignia", unary_union(keep)),))
    (HERE / "art" / "long.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" '
        f'data-tag-px-per-mm="{TAG_PX}">\n{body}\n</svg>\n')

    lines = ["BLOOD TYPE: PINK", "RELIGION: YES", "RANK: NONE", "IF FOUND, HONK"]
    size, lead, out = 200, 228, []
    for i, s in enumerate(lines):
        t = text(s, size=size, tracking=18)
        out.append(affinity.translate(t, -t.bounds[0], i * lead))
    write("short", {"text": unary_union(out)})


if __name__ == "__main__":
    main()
