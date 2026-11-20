"""Génère le logo Rolliste (lettres vectorisées) et l'icône d20.

Usage :
    python generate-logo.py <CinzelDecorative-Bold.ttf> <logo.svg> <icone.svg>

Prérequis : fonttools (pip install fonttools) et la police Cinzel Decorative
(Google Fonts, licence SIL OFL 1.1), téléchargeable sur
https://github.com/google/fonts/tree/main/ofl/cinzeldecorative

Les lettres sont converties en tracés : le SVG s'affiche à l'identique sans
que la police soit installée. Le « O » est remplacé par un d20 vu de face.
Le premier L et le E utilisent les glyphes minuscules « l » et « e » (capitales
sans ornement dans Cinzel Decorative) ; seuls le R et le second L gardent leur
jambage décoratif.
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
YS=[]

font_path, out_logo, out_icon = sys.argv[1:4]
f = TTFont(font_path)
gs = f.getGlyphSet(); cmap = f.getBestCmap(); hmtx = f["hmtx"]
cap = f["OS/2"].sCapHeight
H = 56.0; sc = H / cap; base = 80.0; track = 3.0   # px

def glyph(ch, x):
    name = cmap[ord(ch)]
    pen = SVGPathPen(gs)
    gs[name].draw(TransformPen(pen, (sc, 0, 0, -sc, x, base)))
    bp = BoundsPen(gs); gs[name].draw(TransformPen(bp, (sc, 0, 0, -sc, x, base)))
    if bp.bounds: YS.extend([bp.bounds[1], bp.bounds[3]])
    return pen.getCommands(), hmtx[name][0] * sc

def d20(cx, cy, r):
    k = 0.866
    hexa = [(0,-r),(r*k,-r/2),(r*k,r/2),(0,r),(-r*k,r/2),(-r*k,-r/2)]
    t = [(0,-0.46*r),(0.45*r,0.32*r),(-0.45*r,0.32*r)]
    P = lambda p: f"{cx+p[0]:.2f},{cy+p[1]:.2f}"
    lines = [(t[0],hexa[0]),(t[0],hexa[1]),(t[0],hexa[5]),
             (t[2],hexa[5]),(t[2],hexa[4]),(t[2],hexa[3]),
             (t[1],hexa[1]),(t[1],hexa[2]),(t[1],hexa[3])]
    sw = r*0.1
    return (f'<polygon class="die-face" points="{" ".join(P(p) for p in hexa)}"/>'
            f'<g class="die" fill="none" stroke-width="{sw:.2f}" stroke-linejoin="round" stroke-linecap="round">'
            f'<polygon points="{" ".join(P(p) for p in hexa)}"/>'
            f'<polygon points="{" ".join(P(p) for p in t)}"/>'
            + "".join(f'<line x1="{cx+a[0]:.2f}" y1="{cy+a[1]:.2f}" x2="{cx+b[0]:.2f}" y2="{cy+b[1]:.2f}"/>' for a,b in lines)
            + '</g>')

STYLE = """<style>
  .ink{fill:#1F1A24}.die{stroke:#B3261E}.die-face{fill:#B3261E;fill-opacity:.10}
  @media (prefers-color-scheme: dark){.ink{fill:#EDE6F2}.die{stroke:#E5534B}.die-face{fill:#E5534B;fill-opacity:.16}}
</style>"""

# --- logo
x = 10.0; paths = []
d, adv = glyph("R", x); paths.append(d); x += adv + track
r = H * 0.60                                   # d20 ≈ 1,2 × hauteur des capitales
cx = x + r * 0.866 + 2; cy = base - H / 2
die = d20(cx, cy, r); x = cx + r * 0.866 + 2 + track
for ch in "lLISTe":  # « l » et « e » = capitales sans ornement
    d, adv = glyph(ch, x); paths.append(d); x += adv + track
W = x + 10 - track
YS.extend([cy - r, cy + r]); y0 = min(YS) - 6; Ht = max(YS) + 6 - y0
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {y0:.1f} {W:.0f} {Ht:.1f}" role="img" aria-labelledby="t">'
       f'<title id="t">Rolliste</title>{STYLE}'
       f'<g class="ink">' + "".join(f'<path d="{p}"/>' for p in paths) + f'</g>{die}</svg>\n')
open(out_logo, "w").write(svg)

# --- icône carrée (d20 seul)
icon = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-labelledby="t">'
        f'<title id="t">Rolliste</title>{STYLE}{d20(50, 50, 44)}</svg>\n')
open(out_icon, "w").write(icon)
print(f"logo viewBox y0={y0:.1f} {W:.0f}x{Ht:.1f}")
