"""Export the JAX-A002 wordmark as outlined SVG from Pathway Gothic One.
Layout mirrors brand/reference/wordmark/jax-wordmark.html: letter-spacing .015em
after every glyph, a .30em gap between JAX and SPLATTER, kerning on (HarfBuzz)."""
import sys, pathlib, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONT = str(pathlib.Path(__file__).with_name('PathwayGothicOne-Regular.ttf'))
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[1] / 'brand/reference/wordmark/svg'
BONE_WHITE, PINK, NIGHT = '#e8ecf6', '#ea3e86', '#05060a'

tt = TTFont(FONT); upem = tt['head'].unitsPerEm; gs = tt.getGlyphSet()
blob = hb.Blob.from_file_path(FONT); face = hb.Face(blob); font = hb.Font(face); font.scale = (upem, upem)
TRACK = 0.015 * upem; GAP = 0.30 * upem

def shape(text):
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {'kern': True, 'liga': True})
    names = [tt.getGlyphName(i.codepoint) for i in buf.glyph_infos]
    return list(zip(names, buf.glyph_positions))

def layout(words):
    """words: list of (text, group). Returns [(glyphname, x, group)], total advance."""
    out, x = [], 0.0
    for wi, (text, groups) in enumerate(words):
        for (name, pos), grp in zip(shape(text), groups):
            out.append((name, x + pos.x_offset, grp))
            x += pos.x_advance + TRACK
        if wi < len(words) - 1: x += GAP
    return out, x - TRACK

def glyph_path(name, x):
    pen = SVGPathPen(gs); tp = TransformPen(pen, (1, 0, 0, -1, x, 0)); gs[name].draw(tp)
    return pen.getCommands()

def bounds(items):
    xmin = ymin = 1e9; xmax = ymax = -1e9
    for name, x, _ in items:
        bp = BoundsPen(gs); gs[name].draw(bp)
        if not bp.bounds: continue
        x0, y0, x1, y1 = bp.bounds
        xmin, xmax = min(xmin, x0 + x), max(xmax, x1 + x); ymin, ymax = min(ymin, -y1), max(ymax, -y0)
    return xmin, ymin, xmax, ymax

def svg(items, colors, pad=0.04):
    x0, y0, x1, y1 = bounds(items); p = pad * upem
    x0 -= p; y0 -= p; x1 += p; y1 += p
    w, h = x1 - x0, y1 - y0
    groups = {}
    for name, x, grp in items: groups.setdefault(grp, []).append(glyph_path(name, x))
    body = ''.join('<g id="%s" fill="%s">%s</g>' % (g, colors[g], ''.join('<path d="%s"/>' % d for d in ds)) for g, ds in groups.items())
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.1f %.1f %.1f %.1f" width="%.1f" height="%.1f">%s</svg>\n'
            % (x0, y0, w, h, w, h, body)), w / h

full = [('JAX', ['letters', 'letters', 'x']), ('SPLATTER', ['letters'] * 8)]
jax = [('JAX', ['letters', 'letters', 'x'])]
items_full, adv = layout(full); items_jax, _ = layout(jax)
files = {
    'jax-wordmark.svg':       svg(items_full, {'letters': BONE_WHITE, 'x': PINK}),
    'jax-wordmark-light.svg': svg(items_full, {'letters': NIGHT, 'x': PINK}),
    'jax-wordmark-cut.svg':   svg(items_full, {'letters': '#000000', 'x': '#000000'}),
    'jax-avatar.svg':         svg(items_jax, {'letters': BONE_WHITE, 'x': PINK}),
    'jax-avatar-cut.svg':     svg(items_jax, {'letters': '#000000', 'x': '#000000'}),
}
OUT.mkdir(parents=True, exist_ok=True)
for fn, (txt, ratio) in files.items():
    (OUT / fn).write_text(txt); print('%-24s %6d bytes  aspect %.3f' % (fn, len(txt), ratio))
