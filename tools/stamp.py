#!/usr/bin/env python3
"""The Jax Splatter release stamp.

Usage: python3 tools/stamp.py <artifact.png> <RELEASE-ID> <version> <date>
e.g.:  python3 tools/stamp.py brand/releases/JAX-A001_swatch_v1.png JAX-A001 v1 2026-08-24

Renders the official rubber stamp (Splatter Pink, distressed) and presses it
onto the artifact's lower-right corner, slightly rotated, like a real stamp.
Part of the signing procedure in brand/releases/REGISTRY.md — only stamp an
artifact whose registry row records Jax's sign-off.
"""
import sys, pathlib, tempfile

TEMPLATE = """<html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&display=swap" rel="stylesheet">
<style>html,body{{margin:0;padding:0;background:transparent}}</style></head><body>
<svg id="stamp" width="460" height="460" viewBox="0 0 460 460">
  <defs>
    <path id="top" d="M 230,230 m -168,0 a 168,168 0 1,1 336,0"/>
    <path id="bot" d="M 230,230 m -190,0 a 190,190 0 1,0 380,0"/>
    <filter id="rubber" x="-20%" y="-20%" width="140%" height="140%">
      <feTurbulence type="fractalNoise" baseFrequency="0.55" numOctaves="2" seed="7" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="4" result="art"/>
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="holes"/>
      <feColorMatrix in="holes" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  1.6 1.6 1.6 -1.1 0" result="mask"/>
      <feComposite in="art" in2="mask" operator="in"/>
    </filter>
  </defs>
  <g filter="url(#rubber)" fill="#ea3e86" stroke="#ea3e86" opacity="0.92">
    <circle cx="230" cy="230" r="216" fill="none" stroke-width="10"/>
    <circle cx="230" cy="230" r="196" fill="none" stroke-width="3"/>
    <circle cx="230" cy="230" r="132" fill="none" stroke-width="3"/>
    <text font-family="Oswald" font-weight="700" font-size="44" letter-spacing="10" fill="#ea3e86" stroke="none">
      <textPath href="#top" startOffset="50%" text-anchor="middle">JAX SPLATTER</textPath>
    </text>
    <text font-family="Oswald" font-weight="600" font-size="30" letter-spacing="8" fill="#ea3e86" stroke="none">
      <textPath href="#bot" startOffset="50%" text-anchor="middle">OFFICIAL RELEASE</textPath>
    </text>
    <circle cx="66" cy="230" r="7" stroke="none"/>
    <circle cx="394" cy="230" r="7" stroke="none"/>
    <text x="230" y="205" text-anchor="middle" font-family="Oswald" font-weight="700" font-size="52" letter-spacing="3" stroke="none">{rid}</text>
    <text x="230" y="248" text-anchor="middle" font-family="Oswald" font-weight="600" font-size="26" letter-spacing="4" stroke="none">{ver} · {date}</text>
    <line x1="130" y1="270" x2="330" y2="270" stroke-width="3"/>
    <text x="230" y="306" text-anchor="middle" font-family="Oswald" font-weight="700" font-size="34" letter-spacing="8" stroke="none">SIGNED · JAX</text>
  </g>
</svg></body></html>"""


def render_stamp(rid, ver, date, out_png):
    from playwright.sync_api import sync_playwright
    html = TEMPLATE.format(rid=rid, ver=ver, date=date)
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
        f.write(html)
        tmp = f.name
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={'width': 460, 'height': 460})
        pg.goto('file://' + tmp)
        pg.wait_for_timeout(2500)
        pg.locator('#stamp').screenshot(path=out_png, omit_background=True)
        b.close()
    pathlib.Path(tmp).unlink()


def press(artifact, stamp_png, angle=-9, margin=36, size=300):
    from PIL import Image
    art = Image.open(artifact).convert('RGBA')
    st = Image.open(stamp_png).convert('RGBA').resize((size, size), Image.LANCZOS)
    st = st.rotate(angle, expand=True, resample=Image.BICUBIC)
    x = art.width - st.width - margin
    y = art.height - st.height - margin
    art.alpha_composite(st, (x, y))
    art.convert('RGB' if artifact.lower().endswith('.jpg') else 'RGBA').save(artifact)


if __name__ == '__main__':
    artifact, rid, ver, date = sys.argv[1:5]
    out = pathlib.Path(artifact).with_suffix('.stamp.png')
    render_stamp(rid, ver, date, str(out))
    press(artifact, str(out))
    out.unlink()
    print(f'stamped {artifact} as {rid} {ver} ({date})')
