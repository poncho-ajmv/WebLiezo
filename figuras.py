# -*- coding: utf-8 -*-
"""Los tres paneles de la sección de funciones, dibujados en SVG.

No son capturas: son vectores, así que toman el color del tema y se ven nítidos
en cualquier pantalla. Las formas y la paleta son las mismas que trae la app.
"""
from math import cos, sin, pi

TRAZO = 'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'


def _poly(cx, cy, r, n, giro=-pi / 2, achatar=1.0):
    pts = [(cx + r * cos(giro + 2 * pi * i / n),
            cy + r * sin(giro + 2 * pi * i / n) * achatar) for i in range(n)]
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + 'Z'


def _estrella(cx, cy, r, puntas, interior=.45, giro=-pi / 2):
    pts = []
    for i in range(puntas * 2):
        rr = r if i % 2 == 0 else r * interior
        a = giro + pi * i / puntas
        pts.append((cx + rr * cos(a), cy + rr * sin(a)))
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + 'Z'


def _flecha(cx, cy, r, ang):
    base = [(-r, -.34*r), (.15*r, -.34*r), (.15*r, -.72*r), (r, 0),
            (.15*r, .72*r), (.15*r, .34*r), (-r, .34*r)]
    c, s = cos(ang), sin(ang)
    pts = [(cx + x*c - y*s, cy + x*s + y*c) for x, y in base]
    return 'M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + 'Z'


def _formas(cx, cy, r):
    """Las veinticuatro formas, en el mismo orden que la galería de la app."""
    d = []
    d.append(f'M{cx-r:.1f} {cy-r:.1f}L{cx+r:.1f} {cy+r:.1f}')
    d.append(f'M{cx-r:.1f} {cy+r:.1f}L{cx+r:.1f} {cy-r:.1f}')
    d.append(f'M{cx-r:.1f} {cy}A{r} {r} 0 1 0 {cx+r:.1f} {cy}A{r} {r} 0 1 0 {cx-r:.1f} {cy}')
    d.append(f'M{cx-r:.1f} {cy-r:.1f}h{2*r}v{2*r}h{-2*r}Z')
    d.append(f'M{cx-r+4:.1f} {cy-r:.1f}h{2*r-8}a4 4 0 0 1 4 4v{2*r-8}a4 4 0 0 1 -4 4h{-(2*r-8)}'
             f'a4 4 0 0 1 -4 -4v{-(2*r-8)}a4 4 0 0 1 4 -4Z')
    d.append(f'M{cx-r:.1f} {cy-r+2:.1f}h{2*r}v{2*r-4}h{-2*r}Z')
    d.append(f'M{cx} {cy-r:.1f}L{cx+r:.1f} {cy+r:.1f}L{cx-r:.1f} {cy+r:.1f}Z')
    d.append(f'M{cx-r:.1f} {cy-r:.1f}L{cx+r:.1f} {cy+r:.1f}L{cx-r:.1f} {cy+r:.1f}Z')
    d.append(_poly(cx, cy, r, 4))
    d.append(_poly(cx, cy, r, 5))
    d.append(_poly(cx, cy, r, 6, giro=0))
    d.append(_flecha(cx, cy, r, 0))
    d.append(_flecha(cx, cy, r, pi))
    d.append(_flecha(cx, cy, r, -pi / 2))
    d.append(_flecha(cx, cy, r, pi / 2))
    d.append(_estrella(cx, cy, r, 4, .38))
    d.append(_estrella(cx, cy, r, 5, .46))
    d.append(_estrella(cx, cy, r, 6, .55))
    d.append(f'M{cx-r:.1f} {cy-r+1:.1f}h{2*r}v{1.4*r:.1f}h{-r*0.55:.1f}l{-r*0.35:.1f} {r*0.7:.1f}'
             f'l0 {-r*0.7:.1f}h{-r*1.1:.1f}Z')
    d.append(f'M{cx} {cy-r+1:.1f}a{r} {r*0.72:.1f} 0 1 0 {-r*0.5:.1f} {r*1.35:.1f}'
             f'l{-r*0.28:.1f} {r*0.5:.1f}l{r*0.75:.1f} {-r*0.4:.1f}'
             f'a{r} {r*0.72:.1f} 0 1 0 {-r*-0.0:.1f} {-r*1.45:.1f}Z')
    d.append(f'M{cx-r*0.45:.1f} {cy+r*0.5:.1f}a{r*0.4:.1f} {r*0.4:.1f} 0 0 1 -{r*0.05:.1f} -{r*0.8:.1f}'
             f'a{r*0.42:.1f} {r*0.42:.1f} 0 0 1 {r*0.7:.1f} -{r*0.35:.1f}'
             f'a{r*0.45:.1f} {r*0.45:.1f} 0 0 1 {r*0.85:.1f} {r*0.3:.1f}'
             f'a{r*0.38:.1f} {r*0.38:.1f} 0 0 1 {r*0.05:.1f} {r*0.85:.1f}Z')
    d.append(f'M{cx} {cy+r:.1f}C{cx-r*1.75:.1f} {cy-r*0.15:.1f} {cx-r*1.05:.1f} {cy-r*1.5:.1f} {cx} {cy-r*0.5:.1f}'
             f'C{cx+r*1.05:.1f} {cy-r*1.5:.1f} {cx+r*1.75:.1f} {cy-r*0.15:.1f} {cx} {cy+r:.1f}Z')
    d.append(f'M{cx+r*0.35:.1f} {cy-r:.1f}L{cx-r*0.6:.1f} {cy+r*0.12:.1f}h{r*0.55:.1f}'
             f'L{cx-r*0.3:.1f} {cy+r:.1f}L{cx+r*0.65:.1f} {cy-r*0.15:.1f}h{-r*0.55:.1f}Z')
    d.append(_poly(cx, cy, r, 8, giro=-pi / 8))
    return d


def panel_formas():
    r, celda = 12, 42
    x0, y0 = 32, 30
    partes = []
    for i, d in enumerate(_formas(0, 0, r)):
        col, fila = i % 8, i // 8
        cx, cy = x0 + col * celda + celda / 2, y0 + fila * 46
        partes.append(f'<g transform="translate({cx:.0f} {cy:.0f})"><path d="{d}" {TRAZO}/></g>')
    return '<svg class="fig" viewBox="0 0 400 168" role="img">' + ''.join(partes) + '</svg>'


HERRAMIENTAS = {
 'lapiz':  'M-8 8L-6 2L4 -8L8 -4L-2 6Z M2 -6L6 -2',
 'balde':  'M-8 -1L0 -9L8 -1L0 7Z M8 -1L11 4a2.6 2.6 0 1 1 -5 0Z',
 'texto':  'M-7 -8H7 M0 -8V8 M-3 8H3',
 'goma':   'M-9 4L-1 -6a2.5 2.5 0 0 1 3.5 -.5L7.5 -2a2.5 2.5 0 0 1 .5 3.5L2 8H-5Z M-9 8H9',
 'linea':  'M-8 8L8 -8 M6 -8h2v2',
 'lupa':   'M-2 -2m-6 0a6 6 0 1 0 12 0a6 6 0 1 0 -12 0 M3 3L9 9',
 'pincel': 'M-9 9C-9 3 -6 1 -3 0L4 -9a3 3 0 0 1 5 4L1 3C0 6 -3 9 -9 9Z',
}


def panel_herramientas():
    partes = []
    for i, k in enumerate(['lapiz', 'balde', 'texto', 'goma', 'linea', 'lupa']):
        col, fila = i % 3, i // 3
        cx, cy = 62 + col * 56, 62 + fila * 52
        partes.append(f'<g transform="translate({cx} {cy}) scale(1.15)">'
                      f'<path d="{HERRAMIENTAS[k]}" {TRAZO}/></g>')
    partes.append('<path d="M242 34V134" stroke="currentColor" stroke-width="1" opacity=".3"/>')
    partes.append(f'<g transform="translate(318 84) scale(1.9)">'
                  f'<path d="{HERRAMIENTAS["pincel"]}" {TRAZO}/></g>')
    return '<svg class="fig" viewBox="0 0 400 168" role="img">' + ''.join(partes) + '</svg>'


PALETA = [
 ['#000000','#7f7f7f','#880015','#ed1c24','#ff7f27','#fff200','#22b14c','#00a2e8','#3f48cc','#a349a4'],
 ['#ffffff','#c3c3c3','#b97a57','#ffaec9','#ffc90e','#efe4b0','#b5e61d','#99d9ea','#7092be','#c8bfe7'],
]


def panel_colores():
    lado, hueco = 26, 6
    ancho = 10 * lado + 9 * hueco
    x0 = (400 - ancho) / 2
    partes = []
    for f, fila in enumerate(PALETA):
        for c, color in enumerate(fila):
            x, y = x0 + c * (lado + hueco), 30 + f * (lado + hueco)
            partes.append(f'<rect x="{x:.0f}" y="{y}" width="{lado}" height="{lado}" fill="{color}" '
                          f'stroke="currentColor" stroke-opacity=".28"/>')
    y = 30 + 2 * (lado + hueco) + 12
    for c in range(10):
        x = x0 + c * (lado + hueco)
        partes.append(f'<rect x="{x:.0f}" y="{y}" width="{lado}" height="{lado}" fill="none" '
                      f'stroke="currentColor" stroke-opacity=".55" stroke-dasharray="3 3"/>')
    return '<svg class="fig" viewBox="0 0 400 168" role="img">' + ''.join(partes) + '</svg>'


PANELES = {'tools': panel_herramientas, 'formas': panel_formas, 'colores': panel_colores}
