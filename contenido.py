# -*- coding: utf-8 -*-
"""Todo el texto del sitio. Es el único archivo que hay que tocar para cambiar copy."""

REPO = 'https://github.com/poncho-ajmv/Lienzo'
RELEASES = REPO + '/releases'
# La versión no se muestra en ninguna parte: los enlaces y los pesos salen
# del último release de GitHub, así que publicar una nueva no obliga a tocar el sitio.
BASE = 'https://lienzo.surge.sh'       # dominio final: cambiar antes de publicar

# Los seis colores del lápiz, tomados de la paleta del logo.
COLORES_LAPIZ = ['#0d1826', '#2f6fbf', '#e05038', '#f2a72c', '#3f8f63', '#7fd0f5']

# (archivo, nombre, color de la familia)
TEMAS = [
    ('win10',  'Win 10',  '#0078d7'),
    ('win11',  'Win 11',  '#005fb8'),
    ('win7',   'Win 7',   '#2e8fdc'),
    ('winxp',  'XP',      '#0a246a'),
    ('macos',  'macOS',   '#007aff'),
    ('gnome',  'GNOME',   '#3584e4'),
    ('kde',    'KDE',     '#3daee9'),
    ('lienzo', 'Lienzo',  '#0d1826'),
    ('2077',   '2077',    '#00e5ff'),
    ('sw',     'SW',      '#c93b18'),
]

# Los tres recortes del producto de la sección de funciones.
# (imagen, alt, título, texto)
INSTRUMENTOS = {
 'en': [
  ('tools', 'The tool group: pencil, fill, text, eraser, line, zoom, and the brush picker', 'Tools',
   'Pencil, brush and eraser with a width slider. Marquee or lasso selection with eight-grip resize. Text in real fonts.'),
  ('formas', 'Part of the shape gallery: lines, rectangles, arrows, stars, speech bubbles', 'Seventy-three shapes',
   'Every one draws its own icon from the same list of points it draws with. Nine brushes, outline and fill.'),
  ('colores', 'The color palette, with a row of custom slots', 'Colors and files',
   'The full palette plus ten slots of your own. Opens and saves PNG, JPEG, BMP, GIF, TIFF and ICO.'),
 ],
 'es': [
  ('tools', 'El grupo de herramientas: lápiz, relleno, texto, borrador, línea, lupa y el selector de pinceles', 'Herramientas',
   'Lápiz, pincel y borrador con grosor ajustable. Selección rectangular o libre con estirado por ocho manijas. Texto con fuentes de verdad.'),
  ('formas', 'Parte de la galería de formas: líneas, rectángulos, flechas, estrellas, globos de diálogo', 'Setenta y tres formas',
   'Cada una dibuja su icono con la misma lista de puntos con la que dibuja. Nueve pinceles, contorno y relleno.'),
  ('colores', 'La paleta de colores, con la fila de espacios propios', 'Colores y archivos',
   'La paleta completa más diez espacios propios. Abre y guarda PNG, JPEG, BMP, GIF, TIFF e ICO.'),
 ],
}

# (marca, clave del sistema, nombre, subtítulo, clave instalable, archivo, clave portable, archivo)
SISTEMAS = {
 'en': [
  ('windows', 'windows', 'Windows', '10 / 11 · x86_64',      'win-setup', 'Setup.exe', 'win-zip',   'ZIP'),
  ('linux',   'linux',   'Linux',   'x86_64 · glibc 2.35+',  'linux-deb', 'DEB',       'linux-app', 'AppImage'),
  ('apple',   'macos',   'macOS',   '11+ · Apple Silicon',   'mac-dmg',   'DMG',       'mac-zip',   'ZIP'),
 ],
 'es': [
  ('windows', 'windows', 'Windows', '10 / 11 · x86_64',      'win-setup', 'Setup.exe', 'win-zip',   'ZIP'),
  ('linux',   'linux',   'Linux',   'x86_64 · glibc 2.35+',  'linux-deb', 'DEB',       'linux-app', 'AppImage'),
  ('apple',   'macos',   'macOS',   '11+ · Apple Silicon',   'mac-dmg',   'DMG',       'mac-zip',   'ZIP'),
 ],
}

TEXTOS = {
'en': {
  'lang_other': ('es/', 'es', 'Español'),
  'title': 'Lienzo — a free Paint for Windows, Linux and macOS',
  'desc': 'Lienzo is a small raster editor written in Rust, with twenty themes so it looks like the '
          'system you are on. Free and MIT-licensed, for Windows, Linux and macOS.',
  'nav': [('#download', 'Download')],
  'lang_code': 'EN', 'mode_label': 'Switch between light and dark',

  'ver': 'Free · MIT · Rust',
  'h1': 'A free Paint for Windows, Linux and macOS.',
  'lead': 'A small raster editor with twenty themes, so it looks like the system you are on.',
  'cta': 'Download', 'cta_src': 'View on GitHub',

  'pencil': 'Pencil', 'on': 'On', 'off': 'Off', 'clear': 'Clear',
  'min': 'Minimize', 'max': 'Expand',
  'hint': 'Draw anywhere on this page',

  'themes_h': 'Twenty themes, ten families.',
  'themes_p': 'Not just colors — the toolbar moves too: a ribbon on top, a rail on the side, a floating console.',
  'alt': 'Lienzo with the {name} theme',
  'light': 'Light', 'dark': 'Dark',

  'features_h': 'Features',
  'built': 'Written in Rust with egui. One native binary — no runtime, nothing to configure.',

  'dl_h': 'Get Lienzo',
  'dl_intro': 'Free and MIT-licensed. Every file comes straight from the latest GitHub release.',
  'yours': 'Your system',
  'instalable': 'Installable', 'portable': 'Portable',
  'dl_fine': 'Checksums in {sums}. Not signed yet, so Windows SmartScreen and macOS Gatekeeper may warn on first launch.',

  'foot': 'MIT · poncho-ajmv', 'foot_src': 'GitHub', 'foot_rel': 'Releases',
},
'es': {
  'lang_other': ('../', 'en', 'English'),
  'title': 'Lienzo — un Paint libre para Windows, Linux y macOS',
  'desc': 'Lienzo es un editor de imágenes pequeño escrito en Rust, con veinte temas para que se vea '
          'como el sistema en el que estás. Libre y con licencia MIT, para Windows, Linux y macOS.',
  'nav': [('#download', 'Descargas')],
  'lang_code': 'ES', 'mode_label': 'Cambiar entre claro y oscuro',

  'ver': 'Libre · MIT · Rust',
  'h1': 'Un Paint libre para Windows, Linux y macOS.',
  'lead': 'Un editor de imágenes pequeño con veinte temas, para que se vea como el sistema en el que estás.',
  'cta': 'Descargar', 'cta_src': 'Ver en GitHub',

  'pencil': 'Lápiz', 'on': 'On', 'off': 'Off', 'clear': 'Borrar',
  'min': 'Minimizar', 'max': 'Ampliar',
  'hint': 'Dibujá en cualquier parte de esta página',

  'themes_h': 'Veinte temas, diez familias.',
  'themes_p': 'No sólo los colores — la barra también se mueve: una cinta arriba, un riel al costado, una consola flotante.',
  'alt': 'Lienzo con el tema {name}',
  'light': 'Claro', 'dark': 'Oscuro',

  'features_h': 'Funciones',
  'built': 'Escrito en Rust con egui. Un ejecutable nativo — sin runtime, nada que configurar.',

  'dl_h': 'Descargar Lienzo',
  'dl_intro': 'Libre y con licencia MIT. Cada archivo sale del último release de GitHub.',
  'yours': 'Tu sistema',
  'instalable': 'Instalable', 'portable': 'Portable',
  'dl_fine': 'Sumas de verificación en {sums}. Todavía sin firma comercial, así que Windows SmartScreen y macOS Gatekeeper pueden avisar la primera vez.',

  'foot': 'MIT · poncho-ajmv', 'foot_src': 'GitHub', 'foot_rel': 'Releases',
},
}

TEXTOS['en'].update({'status_h': 'Project status', 'status_pre': 'Last change', 'status_all': 'All releases →'})
TEXTOS['es'].update({'status_h': 'El estado del proyecto', 'status_pre': 'Último cambio', 'status_all': 'Todos los releases →'})

HECHOS = {
 'en': [
  ('Native', 'Written in Rust with egui. One executable — no runtime, nothing to configure.'),
  ('No network', 'No account, no internet, no telemetry. It opens and saves on your disk.'),
  ('Ten languages', 'Spanish, English, Portuguese, French, German, Italian, Russian, Polish, Turkish and Dutch.'),
 ],
 'es': [
  ('Nativo', 'Escrito en Rust con egui. Un ejecutable, sin runtime ni nada que configurar.'),
  ('Sin red', 'No pide cuenta, no se conecta a internet y no manda telemetría. Abre y guarda en tu disco.'),
  ('Diez idiomas', 'Español, inglés, portugués, francés, alemán, italiano, ruso, polaco, turco y neerlandés.'),
 ],
}

FOOT_LINKS = {
 'en': [
  (REPO, 'Code'),
  (RELEASES, 'Releases'),
  (REPO + '/issues', 'Report an issue'),
  (REPO + '/blob/main/.github/SECURITY.md', 'Security'),
  (REPO + '/blob/main/LICENSE', 'License'),
 ],
 'es': [
  (REPO, 'Código'),
  (RELEASES, 'Releases'),
  (REPO + '/issues', 'Reportar un problema'),
  (REPO + '/blob/main/.github/SECURITY.md', 'Seguridad'),
  (REPO + '/blob/main/LICENSE', 'Licencia'),
 ],
}
