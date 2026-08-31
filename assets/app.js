/* Tres cosas: el lápiz sobre toda la página, el conmutador de temas y las descargas. */

/* ---------- el lápiz: se dibuja sobre cualquier parte de la página ---------- */
(function () {
  const pad = document.getElementById('pad');
  if (!pad) return;
  const ctx = pad.getContext('2d');
  const hint = document.getElementById('hint');
  const toggle = document.getElementById('toggle');
  const swatches = document.getElementById('swatches');
  let color = swatches.querySelector('[aria-pressed="true"]').dataset.c;
  let activo = true, dibujando = false, usado = false, trazos = [];

  function medir() {
    const d = devicePixelRatio || 1;
    const alto = document.documentElement.scrollHeight;
    pad.style.height = alto + 'px';
    pad.width = innerWidth * d;
    pad.height = alto * d;
    ctx.setTransform(d, 0, 0, d, 0, 0);
    ctx.lineCap = ctx.lineJoin = 'round';
    ctx.lineWidth = 3;
    repintar();
  }
  function repintar() {
    ctx.clearRect(0, 0, pad.width, pad.height);
    for (const t of trazos) {
      ctx.strokeStyle = t.c;
      ctx.beginPath();
      t.p.forEach((q, i) => (i ? ctx.lineTo(q[0], q[1]) : ctx.moveTo(q[0], q[1])));
      ctx.stroke();
    }
  }
  // coordenadas del documento: los trazos se quedan donde los dejaste al hacer scroll
  const punto = ev => [ev.clientX + scrollX, ev.clientY + scrollY];
  const esControl = el => el.closest('a, button, input, select, textarea, .console, summary');

  addEventListener('pointerdown', ev => {
    if (!activo || ev.button !== 0 || esControl(ev.target)) return;
    dibujando = true;
    trazos.push({ c: color, p: [punto(ev)] });
    if (!usado) { usado = true; hint.classList.add('gone'); }
    ev.preventDefault();
  });
  addEventListener('pointermove', ev => {
    if (!dibujando) return;
    trazos[trazos.length - 1].p.push(punto(ev));
    repintar();
  });
  addEventListener('pointerup', () => (dibujando = false));

  swatches.addEventListener('click', ev => {
    const b = ev.target.closest('button');
    if (!b) return;
    color = b.dataset.c;
    activo = true;
    aplicar();
    [...swatches.children].forEach(x => x.setAttribute('aria-pressed', x.dataset.c === color));
  });
  document.getElementById('clear').addEventListener('click', () => { trazos = []; repintar(); });

  const consola = document.getElementById('console');
  const btnMin = document.getElementById('min');
  btnMin.addEventListener('click', () => {
    const plegada = consola.classList.toggle('min');
    btnMin.textContent = plegada ? '+' : '–';
    btnMin.title = plegada ? btnMin.dataset.max : btnMin.dataset.min;
    btnMin.setAttribute('aria-expanded', !plegada);
    try { localStorage.setItem('lienzo.consola', plegada ? 'min' : 'open'); } catch (e) {}
  });
  try { if (localStorage.getItem('lienzo.consola') === 'min') btnMin.click(); } catch (e) {}
  toggle.addEventListener('click', () => { activo = !activo; aplicar(); });

  function aplicar() {
    toggle.textContent = activo ? toggle.dataset.on : toggle.dataset.off;
    toggle.setAttribute('aria-pressed', activo);
    document.body.classList.toggle('pintando', activo);
  }
  aplicar();
  addEventListener('resize', medir);
  addEventListener('load', medir);
  medir();
})();

/* ---------- los temas: cambian la captura. El claro/oscuro de la página va aparte ---------- */
(function () {
  const shot = document.getElementById('shot');
  if (!shot) return;
  const chips = document.getElementById('chips');
  const seg = document.getElementById('seg');
  const caption = document.getElementById('caption');
  const stage = document.getElementById('stage');
  const btnModo = document.getElementById('mode');

  const guardar = (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} };
  const leer = k => { try { return localStorage.getItem(k); } catch (e) { return null; } };

  let tema = shot.dataset.theme;
  let modo = leer('lienzo.mode') || document.documentElement.dataset.mode || 'light';  // la página
  let variante = leer('lienzo.shot') || modo;                                          // la captura

  function pintarPagina() {
    document.documentElement.dataset.mode = modo;
    if (btnModo) btnModo.setAttribute('aria-pressed', modo === 'dark');
  }
  function pintarCaptura() {
    const chip = chips.querySelector('[data-t="' + tema + '"]');
    const btn = seg.querySelector('[data-m="' + variante + '"]');
    const nueva = new Image();
    stage.classList.add('swap');
    nueva.onload = () => { shot.src = nueva.src; stage.classList.remove('swap'); };
    nueva.src = shot.dataset.base + tema + (variante === 'dark' ? '-d' : '-l') + '.webp';
    shot.alt = chip.dataset.alt;
    caption.textContent = chip.dataset.name + ' · ' + btn.textContent.trim();
    chips.querySelectorAll('[data-t]').forEach(b => b.setAttribute('aria-pressed', b.dataset.t === tema));
    seg.querySelectorAll('[data-m]').forEach(b => b.setAttribute('aria-pressed', b.dataset.m === variante));
  }

  document.getElementById('themes').addEventListener('click', ev => {
    const b = ev.target.closest('button');
    if (!b) return;
    if (b.dataset.t) tema = b.dataset.t;
    if (b.dataset.m) { variante = b.dataset.m; guardar('lienzo.shot', variante); }
    pintarCaptura();
  });
  if (btnModo) btnModo.addEventListener('click', () => {
    modo = modo === 'dark' ? 'light' : 'dark';
    guardar('lienzo.mode', modo);
    pintarPagina();
  });


  pintarPagina();
  pintarCaptura();
})();

/* ---------- descargas: los archivos del último release ---------- */
(function () {
  const os = document.querySelector('.dl');
  if (!os) return;

  // Los nombres llevan la versión, así que se resuelven contra la API en vez de escribirlos a mano.
  const PATRONES = {
    'win-setup': /windows.*setup\.exe$/i,
    'win-zip':   /windows.*portable\.zip$/i,
    'linux-app': /\.appimage$/i,
    'linux-deb': /\.deb$/i,
    'mac-dmg':   /\.dmg$/i,
    'mac-zip':   /macos.*portable\.zip$/i,
  };
  const mb = n => (n / 1048576).toFixed(1) + ' MB';

  fetch('https://api.github.com/repos/poncho-ajmv/Lienzo/releases/latest')
    .then(r => (r.ok ? r.json() : Promise.reject(r.status)))
    .then(rel => {
      for (const [clave, re] of Object.entries(PATRONES)) {
        const a = (rel.assets || []).find(x => re.test(x.name));
        const el = document.querySelector(`[data-a="${clave}"]`);
        if (!a || !el) continue;
        el.href = a.browser_download_url;
          el.querySelector('.sz').textContent = mb(a.size);
      }
      const sums = (rel.assets || []).find(x => /sha256sums/i.test(x.name));
      if (sums) document.querySelectorAll('.sums').forEach(el => (el.href = sums.browser_download_url));
    })
    .catch(() => {});   // sin red o con la API caída, los enlaces ya apuntan a la página de releases

  // la tarjeta del sistema desde el que se mira va al medio y lleva el botón lleno
  const ua = navigator.userAgent;
  const mio = /Win/i.test(ua) ? 'windows'
            : /Mac/i.test(ua) ? 'macos'
            : /Linux|X11|CrOS/i.test(ua) ? 'linux' : null;
  const tarjeta = mio && os.querySelector(`.tj[data-os="${mio}"]`);
  if (tarjeta) {
    tarjeta.classList.add('yo');
    tarjeta.querySelector('.tuyo').hidden = false;
    os.insertBefore(tarjeta, os.children[1]);   // al medio de las tres
  }
})();

/* ---------- estado del proyecto: versiones desde GitHub ---------- */
(function () {
  const lista = document.getElementById('vers');
  if (!lista) return;
  const REPO = 'poncho-ajmv/Lienzo';
  const lang = document.documentElement.lang;
  const fecha = iso => new Date(iso).toLocaleDateString(lang, { day: 'numeric', month: 'long', year: 'numeric' });

  fetch(`https://api.github.com/repos/${REPO}/releases?per_page=6`)
    .then(r => (r.ok ? r.json() : Promise.reject(r.status)))
    .then(lst => {
      const rel = lst.filter(x => !x.draft && !x.prerelease);
      const col = document.getElementById('ver-col');
      if (!col || rel.length < 2) return;
      for (const x of rel.slice(0, 5)) {
        const li = document.createElement('li');
        const b = document.createElement('b'); b.textContent = (x.tag_name || '').replace(/^v/, '');
        const sp = document.createElement('span'); sp.textContent = fecha(x.published_at);
        li.append(b, sp);
        lista.appendChild(li);
      }
      col.hidden = false;
      dispatchEvent(new Event('resize')); // remedir el lienzo con la altura nueva
    })
    .catch(() => {});

  fetch(`https://api.github.com/repos/${REPO}`)
    .then(r => (r.ok ? r.json() : Promise.reject(r.status)))
    .then(repo => {
      const p = document.getElementById('ultimo-cambio');
      if (!p || !repo.pushed_at) return;
      p.textContent = p.dataset.pre + ': ' + fecha(repo.pushed_at);
      p.hidden = false;
      dispatchEvent(new Event('resize')); // remedir el lienzo con la altura nueva
    })
    .catch(() => {});
})();

