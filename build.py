# -*- coding: utf-8 -*-
"""Genera dist/ : index.html (inglés), es/index.html (español) y los archivos estáticos.

    python3 build.py

Sin dependencias: sólo la biblioteca estándar de Python 3.
"""
import html, json, pathlib, shutil

import figuras
import icons
import marcas
from contenido import (TEXTOS, TEMAS, COLORES_LAPIZ, INSTRUMENTOS, SISTEMAS, HECHOS, FOOT_LINKS,
                       REPO, RELEASES, BASE)

RAIZ = pathlib.Path(__file__).parent
DIST = RAIZ / 'dist'
e = html.escape


def lapiz():
    return '\n      '.join(
        f'<button data-c="{c}" style="--c:{c}" aria-label="Color {i + 1}" '
        f'aria-pressed="{"true" if i == 1 else "false"}"></button>'
        for i, c in enumerate(COLORES_LAPIZ))


def chips(t):
    return '\n        '.join(
        f'<button class="chip" data-t="{slug}" data-name="{e(nombre)}" '
        f'data-alt="{e(t["alt"].format(name=nombre))}" style="--c:{color}"><i></i>{e(nombre)}</button>'
        for slug, nombre, color in TEMAS)


def instrumentos(lang, pre):
    """Las tres piezas: el dibujo a la izquierda, lo que hace a la derecha.

    Los dibujos son SVG hechos para la página (ver figuras.py), no capturas:
    toman el color del tema y se ven nítidos en cualquier pantalla.
    """
    return '\n      '.join(
        f'''<div class="row">
        <div class="tile">{figuras.PANELES[img]()}<span class="vh">{e(alt)}</span></div>
        <div class="say"><h3>{e(titulo)}</h3><p>{e(texto)}</p></div>
      </div>'''
        for img, alt, titulo, texto in INSTRUMENTOS[lang])


def sistemas(lang, t):
    """Una tarjeta por sistema: instalable arriba, portable abajo.

    El orden aquí es el de siempre; al cargar, la página mueve al medio
    la tarjeta del sistema desde el que se mira.
    """
    salida = []
    for marca, os_key, nombre, sub, k1, a1, k2, a2 in SISTEMAS[lang]:
        salida.append(f'''<article class="tj" data-os="{os_key}">
        <header>{marcas.marca(marca, 30)}<h3>{e(nombre)}</h3>
          <span class="tuyo" hidden>{e(t['yours'])}</span></header>
        <p class="sub">{e(sub)}</p>
        <a class="opt primaria" data-a="{k1}" href="{RELEASES}">
          <span class="tipo">{e(t['instalable'])}</span>
          <span class="arch">{e(a1)}<em class="sz"></em></span></a>
        <a class="opt" data-a="{k2}" href="{RELEASES}">
          <span class="tipo">{e(t['portable'])}</span>
          <span class="arch">{e(a2)}<em class="sz"></em></span></a>
      </article>''')
    return '\n      '.join(salida)


def hechos(lang):
    filas = '\n      '.join(
        f'<div><h4>{e(titulo)}</h4><p>{e(texto)}</p></div>'
        for titulo, texto in HECHOS[lang])
    return f'<div class="hechos">\n      {filas}\n    </div>'


def pie_links(lang):
    return '\n      '.join(f'<a href="{h}">{e(n)}</a>' for h, n in FOOT_LINKS[lang])


def pagina(lang):
    t = TEXTOS[lang]
    pre = '' if lang == 'en' else '../'
    url = BASE + ('/' if lang == 'en' else '/es/')
    otro_href, otro_lang, otro_txt = t['lang_other']
    auto = ("if(/^es/i.test(navigator.language||'')) location.replace('es/');"
            ) if lang == 'en' else ''
    inicio = TEMAS[0]

    ld = json.dumps({
        '@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': 'Lienzo',
        'applicationCategory': 'MultimediaApplication',
        'operatingSystem': 'Windows, Linux, macOS',
        'license': 'https://opensource.org/licenses/MIT', 'codeRepository': REPO,
        'downloadUrl': RELEASES, 'inLanguage': lang, 'description': t['desc'],
        'author': {'@type': 'Person', 'name': 'poncho-ajmv'},
        'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'},
    }, ensure_ascii=False)

    nav = '\n      '.join(f'<a class="q" href="{h}">{e(n)}</a>' for h, n in t['nav'])
    sums = f'<a class="sums" href="{RELEASES}">SHA256SUMS.txt</a>'
    fine = e(t['dl_fine']).replace('{sums}', sums)
    intro = e(t['dl_intro'])

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{BASE}/">
<link rel="alternate" hreflang="es" href="{BASE}/es/">
<link rel="alternate" hreflang="x-default" href="{BASE}/">
<link rel="icon" href="{pre}img/icon.png" type="image/png">
<link rel="apple-touch-icon" href="{pre}img/icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="Lienzo">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/win10-l.webp">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'es_ES'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#7fd0f5">
<script type="application/ld+json">{ld}</script>
<link rel="stylesheet" href="{pre}styles.css">
<script>
// Antes del primer cuadro: el modo guardado y, en la página en inglés, el salto
// al español si el navegador está en español y nadie eligió idioma todavía.
(function(){{try{{
  document.documentElement.dataset.mode=localStorage.getItem('lienzo.mode')||
    (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
  {auto}
}}catch(e){{}}}})()
</script>
</head>
<body>
<canvas id="pad" aria-hidden="true"></canvas>

<aside class="console" id="console" aria-label="{e(t['pencil'])}">
  <div class="con-top">
    <span class="con-title">{e(t['pencil'])}</span>
    <button class="con-x" id="toggle" aria-pressed="true"
            data-on="{e(t['on'])}" data-off="{e(t['off'])}">{e(t['on'])}</button>
    <button class="con-min" id="min" aria-expanded="true"
            data-min="{e(t['min'])}" data-max="{e(t['max'])}" title="{e(t['min'])}">–</button>
  </div>
  <div class="swatches" id="swatches">
      {lapiz()}
  </div>
  <button class="mini" id="clear">{e(t['clear'])}</button>
  <p class="con-hint" id="hint">{e(t['hint'])}</p>
</aside>

<header class="nav">
  <div class="wrap nav-in">
    <a class="brand" href="{pre or './'}">
      <img class="pixel-img" src="{pre}img/mark.png" width="24" height="24" alt="">
      <span>Lienzo</span>
    </a>
    <nav class="links">
      {nav}
    </nav>
    <div class="right">
      <button class="ctl" id="mode" aria-label="{e(t['mode_label'])}" aria-pressed="false">
        <span class="i-moon">{icons.svg(icons.MOON)}</span><span class="i-sun">{icons.svg(icons.SUN)}</span>
      </button>
      <a class="q gh" href="{REPO}">{marcas.marca("github", 16)}GitHub</a>
    </div>
  </div>
</header>

<main>
  <section class="hero" id="top">
    <div class="wrap hero-in">
      <p class="ver">{e(t['ver'])}</p>
      <h1>{e(t['h1'])}</h1>
      <p class="lead">{e(t['lead'])}</p>
      <div class="cta">
        <a class="btn" href="{RELEASES}">{e(t['cta'])}</a>
        <a class="btn quiet" href="{REPO}">{e(t['cta_src'])}</a>
      </div>
    </div>
  </section>

  <section class="band" id="themes">
    <div class="wrap band-in">
      <h2>{e(t['themes_h'])}</h2>
      <p class="band-lead">{e(t['themes_p'])}</p>
      <div class="frame stage" id="stage">
        <img id="shot" src="{pre}img/{inicio[0]}-l.webp" data-theme="{inicio[0]}" data-base="{pre}img/"
             width="920" height="536" alt="{e(t['alt'].format(name=inicio[1]))}">
      </div>
      <div class="chips" id="chips">
        {chips(t)}
      </div>
      <div class="metaline">
        <span class="caption" id="caption">{e(inicio[1])} · {e(t['light'])}</span>
        <span class="seg" id="seg"><button data-m="light">{e(t['light'])}</button><button data-m="dark">{e(t['dark'])}</button></span>
      </div>
    </div>
  </section>

  <section class="block wrap" id="features">
    <h2>{e(t['features_h'])}</h2>
    <div class="rows">
      {instrumentos(lang, pre)}
    </div>
    {hechos(lang)}
  </section>

  <section class="block wrap" id="download">
    <h2>{e(t['dl_h'])}</h2>
    <p class="band-lead">{intro}</p>
    <div class="dl">
      {sistemas(lang, t)}
    </div>
    <p class="fine">{fine}</p>
  </section>

  <section class="block wrap" id="status">
    <h2>{e(t['status_h'])}</h2>
    <p class="band-lead" id="ultimo-cambio" data-pre="{e(t['status_pre'])}" hidden></p>
    <div class="estado">
      <div class="col" id="ver-col" hidden>
        <ul class="vers" id="vers"></ul>
        <a class="mas" href="{RELEASES}">{e(t['status_all'])}</a>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap pie">
    <div class="pie-marca">
      <img class="pixel-img" src="{pre}img/icon.png" width="34" height="34" alt="">
      <div>
        <p class="nombre">Lienzo</p>
        <p class="tag">{e(t['h1'])}</p>
      </div>
    </div>
    <nav class="pie-links">
      {pie_links(lang)}
    </nav>
  </div>
  <div class="wrap pie-baja">
    <span>{e(t['foot'])}</span>
  </div>
</footer>

<script src="{pre}app.js"></script>
</body>
</html>
'''


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / 'es').mkdir(parents=True)
    shutil.copytree(RAIZ / 'assets' / 'img', DIST / 'img')
    shutil.copytree(RAIZ / 'assets' / 'fonts', DIST / 'fonts')
    for f in ('styles.css', 'app.js'):
        shutil.copy(RAIZ / 'assets' / f, DIST / f)

    (DIST / 'index.html').write_text(pagina('en'), encoding='utf-8')
    (DIST / 'es' / 'index.html').write_text(pagina('es'), encoding='utf-8')
    (DIST / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
    (DIST / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'  <url><loc>{BASE}/</loc><priority>1.0</priority></url>\n'
        f'  <url><loc>{BASE}/es/</loc><priority>0.8</priority></url>\n'
        '</urlset>\n')

    n = sum(1 for f in DIST.rglob('*') if f.is_file())
    kb = sum(f.stat().st_size for f in DIST.rglob('*') if f.is_file()) // 1024
    print(f'dist/ listo — {n} archivos, {kb} KB')


if __name__ == '__main__':
    main()
