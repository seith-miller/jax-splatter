#!/usr/bin/env python3
"""Merch round 1 — the five committed production files, from the signed marks.

Writes SVGs (real inches; a `CutContour` group for the Roland where a cut is
needed) plus PNG previews into brand/reference/merch/<slug>/. Text is outlined
from the OFL fonts in tools/ (Pathway Gothic One for the wordmark, Bebas Neue
for everything else), so no file depends on a font being installed.

  python3 tools/merch-files.py            # needs fonttools, uharfbuzz, qrcode

Files (candidates until Jax signs them — see brand/releases/REGISTRY.md):
  A007 sticker-sheet   wordmark kiss-cut 4x1.25 in, 32-up on 18.5x12 (Roland)
  A008 button-face     2.633 in face for the 2.25 in maker, 12-up on 8.5x11
  A011 lighter-wrap    Bic Maxi wrap 2.875x2.375 in, 30-up on 18.5x12.5 (Roland)
  A012 cooler-wrap     12 oz neoprene wrap 8x4 in, mirrored for sublimation, 2-up on 8.5x14
  price-card           8.5x11 table card (not a release; site infrastructure-grade)
"""
import pathlib, uharfbuzz as hb, qrcode
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'brand/reference/merch'
NIGHT, BONE_WHITE, BONE, PINK, SHEET, SLIME_INK, STATIC = '#05060a', '#e8ecf6', '#d2cab6', '#ea3e86', '#f2efe9', '#1f9e06', '#454c5c'
CUT = '#ff00ff'   # the CutContour spot, as VersaWorks expects it

class Face:
    def __init__(self, path):
        self.tt = TTFont(path); self.upem = self.tt['head'].unitsPerEm; self.gs = self.tt.getGlyphSet()
        blob = hb.Blob.from_file_path(str(path)); self.font = hb.Font(hb.Face(blob)); self.font.scale = (self.upem, self.upem)
    def shape(self, text):
        buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(self.font, buf, {'kern': True})
        return [(self.tt.getGlyphName(i.codepoint), p) for i, p in zip(buf.glyph_infos, buf.glyph_positions)]
    def cap(self):
        bp = BoundsPen(self.gs); self.gs['H'].draw(bp); return bp.bounds[3]

PGO = Face(HERE / 'PathwayGothicOne-Regular.ttf'); BEBAS = Face(HERE / 'BebasNeue-Regular.ttf')

def text_paths(face, runs, cap_in, track=0.0, gap=0.0):
    """runs: [(text, fill)] joined with `gap` (em). Returns (list of (d, fill)), width_in, height_in.
    cap_in: cap height in inches. Coordinates in inches, y down, baseline at y=cap_in."""
    scale = cap_in / face.cap()
    items, x = [], 0.0
    for ri, (text, fill) in enumerate(runs):
        for name, pos in face.shape(text):
            items.append((name, x + pos.x_offset * scale, fill)); x += (pos.x_advance + track * face.upem) * scale
        if ri < len(runs) - 1: x += gap * face.upem * scale
    x -= track * face.upem * scale
    paths = []
    for name, gx, fill in items:
        pen = SVGPathPen(face.gs); tp = TransformPen(pen, (scale, 0, 0, -scale, gx, cap_in)); face.gs[name].draw(tp)
        paths.append((pen.getCommands(), fill))
    return paths, x, cap_in

def wordmark(cap_in, dark=True, jax_only=False):
    letters = BONE_WHITE if dark else NIGHT
    runs = [('JA', letters), ('X', PINK)] if jax_only else [('JA', letters), ('X', PINK), ('SPLATTER', letters)]
    # letter-spacing .015em everywhere, .30em gap only between JAX and SPLATTER
    paths, w, h = [], 0.0, cap_in
    scale = cap_in / PGO.cap(); x = 0.0
    words = [[('JA', letters), ('X', PINK)]] + ([] if jax_only else [[('SPLATTER', letters)]])
    for wi, word in enumerate(words):
        for text, fill in word:
            for name, pos in PGO.shape(text):
                pen = SVGPathPen(PGO.gs); tp = TransformPen(pen, (scale, 0, 0, -scale, x + pos.x_offset * scale, cap_in)); PGO.gs[name].draw(tp)
                paths.append((pen.getCommands(), fill)); x += (pos.x_advance + 0.015 * PGO.upem) * scale
        if wi < len(words) - 1: x += 0.30 * PGO.upem * scale
    x -= 0.015 * PGO.upem * scale
    return paths, x, h

def fit(paths, w, h, target_w):
    """Scale (paths, w, h) uniformly so the width equals target_w."""
    k = target_w / w
    return [('<path d="%s" fill="%s" transform="scale(%.6f)"/>' % (d, f, k)) for d, f in paths], w * k, h * k

def g_raw(elems, tx, ty):
    return '<g transform="translate(%.4f %.4f)">%s</g>' % (tx, ty, ''.join(elems))

def g(paths, tx, ty, extra=''):
    return '<g transform="translate(%.4f %.4f)"%s>%s</g>' % (tx, ty, extra, ''.join('<path d="%s" fill="%s"/>' % (d, f) for d, f in paths))

def svg(w, h, body, cut=None):
    cutg = '<g id="CutContour" fill="none" stroke="%s" stroke-width="0.003">%s</g>' % (CUT, cut) if cut else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="%.3fin" height="%.3fin" viewBox="0 0 %.4f %.4f">%s%s</svg>\n' % (w, h, w, h, body, cutg))

def rrect(x, y, w, h, r, fill):
    return '<rect x="%.4f" y="%.4f" width="%.4f" height="%.4f" rx="%.4f" fill="%s"/>' % (x, y, w, h, r, fill)
def rrect_cut(x, y, w, h, r):
    return '<rect x="%.4f" y="%.4f" width="%.4f" height="%.4f" rx="%.4f"/>' % (x, y, w, h, r)

def write(slug, name, content):
    d = OUT / slug; d.mkdir(parents=True, exist_ok=True); (d / name).write_text(content); print('wrote', d / name)

# ---------------------------------------------------------------- A007 sticker
def sticker_unit():
    W, H, B, R = 4.0, 1.25, 0.06, 0.125            # finished size, bleed, corner radius
    wm, ww, wh = wordmark(0.60)
    url, uw, uh = text_paths(BEBAS, [('JAXSPLATTER.COM', BONE)], 0.13, track=0.14)
    body = rrect(-B, -B, W + 2 * B, H + 2 * B, R + B, NIGHT)
    body += g(wm, (W - ww) / 2, 0.22) + g(url, (W - uw) / 2, 0.98)
    return W, H, B, R, body

def sticker_sheet():
    W, H, B, R, unit = sticker_unit()
    SW, SH, GUT = 18.5, 12.0, 0.10
    cols, rows = 4, 8
    pitch_x, pitch_y = W + 2 * B + GUT, H + 2 * B + GUT
    ox = (SW - (cols * pitch_x - GUT)) / 2; oy = (SH - (rows * pitch_y - GUT)) / 2
    body, cut = '', ''
    for r in range(rows):
        for c in range(cols):
            x, y = ox + B + c * pitch_x, oy + B + r * pitch_y
            body += '<g transform="translate(%.4f %.4f)">%s</g>' % (x, y, unit)
            cut += rrect_cut(x, y, W, H, R)
    write('sticker-sheet', 'A007_sticker-sheet_18.5x12.svg', svg(SW, SH, body, cut))
    write('sticker-sheet', 'A007_sticker_unit.svg', svg(W + 2 * B, H + 2 * B, '<g transform="translate(%.4f %.4f)">%s</g>' % (B, B, unit), '<g transform="translate(%.4f %.4f)">%s</g>' % (B, B, rrect_cut(0, 0, W, H, R))))
    return cols * rows

# ---------------------------------------------------------------- A008 button face
def button_face_unit():
    D, FACE = 2.633, 2.25                             # cut diameter for the 2.25 in maker; visible face
    r = D / 2
    wm, ww, wh = wordmark(0.78, jax_only=True)
    body = '<circle cx="%.4f" cy="%.4f" r="%.4f" fill="%s"/>' % (r, r, r, NIGHT)
    body += g(wm, r - ww / 2, r - wh / 2)
    return D, body

def button_sheet():
    D, unit = button_face_unit()
    SW, SH, GUT = 8.5, 11.0, 0.05
    cols, rows = 3, 4
    ox = (SW - (cols * (D + GUT) - GUT)) / 2; oy = (SH - (rows * (D + GUT) - GUT)) / 2
    body, cut = '', ''
    for r in range(rows):
        for c in range(cols):
            x, y = ox + c * (D + GUT), oy + r * (D + GUT)
            body += '<g transform="translate(%.4f %.4f)">%s</g>' % (x, y, unit)
            cut += '<circle cx="%.4f" cy="%.4f" r="%.4f"/>' % (x + D / 2, y + D / 2, D / 2)
    write('button-face', 'A008_button-face_8.5x11.svg', svg(SW, SH, body, cut))
    write('button-face', 'A008_button-face_unit.svg', svg(D, D, unit, '<circle cx="%.4f" cy="%.4f" r="%.4f"/>' % (D / 2, D / 2, D / 2)))
    return cols * rows

# ---------------------------------------------------------------- A011 lighter wrap
def lighter_unit():
    W, H, B, R = 2.875, 2.375, 0.05, 0.06           # around x tall, Bic Maxi — TEST-FIT ONE and adjust
    FRONT = 1.0                                        # the front face band, centred in the circumference
    wm, ww, wh = wordmark(0.34)
    url, uw, uh = text_paths(BEBAS, [('JAXSPLATTER.COM', BONE)], 0.11, track=0.14)
    body = rrect(-B, -B, W + 2 * B, H + 2 * B, R + B, NIGHT)
    # front band: wordmark reads bottom-to-top (rotate -90 about its own centre), centred on the band
    cx, cy = W / 2, H / 2
    body += '<g transform="translate(%.4f %.4f) rotate(-90)">%s</g>' % (cx, cy, g(wm, -ww / 2, -wh / 2))
    # the URL once, on the narrow side face to the right of the front (front spans W/2 ± 0.5; side is the next 0.5)
    sx = W / 2 + FRONT / 2 + 0.25
    body += '<g transform="translate(%.4f %.4f) rotate(-90)">%s</g>' % (sx, cy, g(url, -uw / 2, -uh / 2))
    return W, H, B, R, body

def lighter_sheet():
    W, H, B, R, unit = lighter_unit()
    SW, SH, GUT = 18.5, 12.5, 0.10
    cols, rows = 6, 5
    pitch_x, pitch_y = W + 2 * B + GUT, H + 2 * B + GUT
    ox = (SW - (cols * pitch_x - GUT)) / 2; oy = (SH - (rows * pitch_y - GUT)) / 2
    body, cut = '', ''
    for r in range(rows):
        for c in range(cols):
            x, y = ox + B + c * pitch_x, oy + B + r * pitch_y
            body += '<g transform="translate(%.4f %.4f)">%s</g>' % (x, y, unit)
            cut += rrect_cut(x, y, W, H, R)
    write('lighter-wrap', 'A011_lighter-wrap_18.5x12.5.svg', svg(SW, SH, body, cut))
    write('lighter-wrap', 'A011_lighter-wrap_unit.svg', svg(W + 2 * B, H + 2 * B, '<g transform="translate(%.4f %.4f)">%s</g>' % (B, B, unit), '<g transform="translate(%.4f %.4f)">%s</g>' % (B, B, rrect_cut(0, 0, W, H, R))))
    return cols * rows

# ---------------------------------------------------------------- A012 cooler wrap
def cooler_unit(mirrored):
    W, H = 8.0, 4.0                                    # flat 12 oz neoprene blank — measure the blank, adjust
    PANEL = 3.1                                        # ink width per 4 in panel
    wm, ww, wh = fit(*wordmark(0.62, dark=False), PANEL)
    line, lw, lh = fit(*text_paths(BEBAS, [('GET SPLATTERED!', NIGHT)], 0.55, track=0.06), PANEL)
    body = '<rect x="0" y="0" width="%.4f" height="%.4f" fill="%s"/>' % (W, H, SHEET)   # the blank is white; the cream prints as a tint
    # front panel = left half when flat (seam at the edge); back panel = right half
    body += g_raw(wm, (W / 2 - ww) / 2, (H - wh) / 2)
    body += g_raw(line, W / 2 + (W / 2 - lw) / 2, (H - lh) / 2)
    body += '<line x1="%.4f" y1="0" x2="%.4f" y2="%.4f" stroke="%s" stroke-width="0.004" stroke-dasharray="0.05 0.05"/>' % (W / 2, W / 2, H, STATIC)  # fold guide, faint
    if mirrored:
        body = '<g transform="translate(%.4f 0) scale(-1 1)">%s</g>' % (W, body)
    return W, H, body

def cooler_sheet():
    W, H, unit = cooler_unit(mirrored=True)
    SW, SH = 8.5, 14.0
    ox = (SW - W) / 2; gap = (SH - 2 * H) / 3
    body = ''.join('<g transform="translate(%.4f %.4f)">%s</g>' % (ox, gap + i * (H + gap), unit) for i in range(2))
    write('cooler-wrap', 'A012_cooler-wrap_MIRRORED_8.5x14.svg', svg(SW, SH, body))
    _, _, preview = cooler_unit(mirrored=False)
    write('cooler-wrap', 'A012_cooler-wrap_unit_preview.svg', svg(W, H, preview))
    return 2

# ---------------------------------------------------------------- price card
def qr_paths(url, size_in):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0); q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m); cell = size_in / n
    return ''.join('<rect x="%.4f" y="%.4f" width="%.4f" height="%.4f"/>' % (c * cell, r * cell, cell * 1.02, cell * 1.02) for r in range(n) for c in range(n) if m[r][c])

def price_card():
    W, H, M = 8.5, 11.0, 0.7
    body = '<rect x="0" y="0" width="%.4f" height="%.4f" fill="%s"/>' % (W, H, NIGHT)
    wm, ww, wh = wordmark(1.1); body += g(wm, (W - ww) / 2, 0.9)
    sub, sw, sh = text_paths(BEBAS, [('MERCH', BONE)], 0.28, track=0.3); body += g(sub, (W - sw) / 2, 2.35)
    rows = [('STICKER', '$2'), ('BUTTON', '$3'), ('LIGHTER', '$3'), ('CAN COOLER', '$5')]
    y = 3.4
    for name, price in rows:
        n, nw, nh = text_paths(BEBAS, [(name, BONE_WHITE)], 0.5, track=0.06); p, pw, ph = text_paths(BEBAS, [(price, PINK)], 0.5, track=0.02)
        body += g(n, M + 0.3, y) + g(p, W - M - 0.3 - pw, y); y += 0.9
    y += 0.1
    body += '<line x1="%.3f" y1="%.3f" x2="%.3f" y2="%.3f" stroke="%s" stroke-width="0.01"/>' % (M, y, W - M, y, STATIC); y += 0.4
    b1, bw, bh = text_paths(BEBAS, [('ANY TWO SMALL THINGS  $5', BONE)], 0.3, track=0.06); body += g(b1, M + 0.3, y); y += 0.48
    b2, bw2, _ = text_paths(BEBAS, [('A STICKER IN EVERY BAG', BONE)], 0.3, track=0.06); body += g(b2, M + 0.3, y); y += 0.8
    pay, pw2, _ = text_paths(BEBAS, [('CASH  ·  TAP  ·  VENMO', BONE_WHITE)], 0.34, track=0.1); body += g(pay, M + 0.3, y)
    # QR to the hub, bottom right, on a One-Sheet tile
    qs = 1.25; qx, qy = W - M - qs - 0.12, H - M - qs - 0.12
    body += rrect(qx - 0.12, qy - 0.12, qs + 0.24, qs + 0.24, 0.06, SHEET)
    body += '<g transform="translate(%.4f %.4f)" fill="%s">%s</g>' % (qx, qy, NIGHT, qr_paths('https://jaxsplatter.com', qs))
    u, uw, _ = text_paths(BEBAS, [('JAXSPLATTER.COM', BONE)], 0.22, track=0.14); body += g(u, M, H - M - 0.22)
    write('price-card', 'price-card_8.5x11.svg', svg(W, H, body))

if __name__ == '__main__':
    n1 = sticker_sheet(); n2 = button_sheet(); n3 = lighter_sheet(); n4 = cooler_sheet(); price_card()
    print('per sheet: stickers %d · button faces %d · lighter wraps %d · cooler wraps %d' % (n1, n2, n3, n4))
