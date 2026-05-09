#!/usr/bin/env python3
"""
Monolithic single-page course renderer for the Permis Côtier.

Generates output/permis-cours-complet.html — a self-contained HTML file with
sidebar navigation, all 21 lessons inline, lightbox, progress tracking, and
responsive design. Intended for use in the Cloth (Cowork) app.

Reuses the markdown pipeline from render_course.py (callouts, wikilinks, quiz
answer wrapping).

Usage:
    python scripts/render_complete.py
"""

from __future__ import annotations

import html
import json
import shutil
from pathlib import Path

from render_course import (
    ASSETS_SRC,
    build_manifest,
    _parse_frontmatter,
    _preprocess_wikilinks,
    _preprocess_callouts,
    _md_parser,
    _wrap_quiz_answers,
)

REPO = Path(__file__).parent.parent
OUTPUT_FILE = REPO / "output" / "permis-cours-complet.html"
ASSETS_DST = REPO / "output" / "assets"


def _render_body(md_path: Path) -> str:
    raw = md_path.read_text(encoding="utf-8")
    _, body_md = _parse_frontmatter(raw)
    body_md = _preprocess_wikilinks(body_md)
    body_md = _preprocess_callouts(body_md)
    body_html = _md_parser.render(body_md)
    body_html = _wrap_quiz_answers(body_html)
    # Rewrite image paths: ../assets/ → assets/ (monolithic file sits next to assets/)
    body_html = body_html.replace('src="../assets/', 'src="assets/')
    return body_html


def _build_sidebar_html(modules_data: list[dict]) -> str:
    parts: list[str] = []
    parts.append('<div class="sb-hdr">')
    parts.append('  <span class="anc">⚓</span>')
    parts.append('  <div><div class="bt">Permis Côtier</div><div class="bs">Golfe de Fethiye</div></div>')
    parts.append('</div>')
    parts.append('<div class="sb-idx" onclick="goTo(\'__idx__\')">← Plan du cours</div>')
    parts.append('<div class="sb-nav">')

    for mod in modules_data:
        parts.append(f'<div class="mgroup"><div class="mhdr" data-mod="{mod["num"]}" onclick="toggleMod(this)">'
                     f'<span class="mnum">{mod["num"]}</span>'
                     f'<span class="mtitle">{html.escape(mod["title"])}</span>'
                     f'<span class="mchev">▶</span></div>'
                     f'<ul class="mitems collapsed">')
        for s in mod["sessions"]:
            parts.append(f'<li class="sitem" data-slug="{s["slug"]}" data-mod="{mod["num"]}" onclick="goTo(\'{s["slug"]}\')">'
                         f'<span class="sc">{s["code"]}</span>'
                         f'<span><span class="sn">{html.escape(s["title"])}</span>'
                         f'<span class="sd">{s["duration"]} min</span></span></li>')
        parts.append('</ul></div>')

    parts.append('</div>')
    parts.append('<div class="sb-prog">')
    parts.append('  <div class="pl"><span>Progression</span><span id="pc">0 / 21</span></div>')
    parts.append('  <div class="pb"><div class="pf" id="pf" style="width:0%"></div></div>')
    parts.append('</div>')
    return "\n".join(parts)


def _build_index_html(modules_data: list[dict]) -> str:
    parts: list[str] = []
    parts.append('<div class="spage" id="sp-__idx__" style="display:none">')
    parts.append('  <div class="card">')
    parts.append('    <div class="session-meta"><span class="meta-badge meta-module">Permis Côtier</span></div>')
    parts.append('    <h1>⚓ Plan du Cours</h1>')

    total = sum(len(m["sessions"]) for m in modules_data)
    total_dur = sum(s["duration"] for m in modules_data for s in m["sessions"])
    total_hrs = total_dur // 60
    parts.append(f'    <p class="idx-intro">{total} sessions · environ {total_hrs} heures d\'étude. Cliquez sur une session pour commencer.</p>')
    parts.append('    <div class="igrid" id="igrid">')

    for mod in modules_data:
        parts.append(f'<div class="icard"><p class="ictitle"><span class="ibadge">{mod["num"]}</span>{html.escape(mod["title"])}</p><ul>')
        for s in mod["sessions"]:
            parts.append(f'<li onclick="goTo(\'{s["slug"]}\')" data-index-slug="{s["slug"]}">'
                         f'<span class="li-code">{s["code"]}</span>{html.escape(s["title"])}</li>')
        parts.append('</ul></div>')

    parts.append('</div></div></div>')
    return "\n".join(parts)


def _build_sessions_html(modules_data: list[dict]) -> str:
    all_sessions = [s for m in modules_data for s in m["sessions"]]
    parts: list[str] = []

    for i, sess in enumerate(all_sessions):
        slug = sess["slug"]
        parts.append(f'<div class="spage" id="sp-{slug}" style="display:none">')
        parts.append('<div class="card">')
        parts.append('<div class="session-meta">')
        parts.append(f'        <span class="meta-badge meta-module">{html.escape(sess["module_title"])}</span>')
        parts.append(f'        <span class="meta-badge meta-code">Session {sess["code"]}</span>')
        parts.append(f'        <span class="meta-duration">~{sess["duration"]} min</span>')
        parts.append('      </div>')
        parts.append(f'      <h1>{html.escape(sess["title"])}</h1>')
        parts.append('')
        parts.append(f'      {sess["body_html"]}')
        parts.append('')

        # Prev/next nav
        nav_parts: list[str] = []
        if i > 0:
            prev = all_sessions[i - 1]
            nav_parts.append(f'<button class="nav-btn nav-prev" onclick="goTo(\'{prev["slug"]}\')">'
                             f'<span class="nav-dir">← Session précédente</span>'
                             f'<span class="nav-title">{html.escape(prev["title"])}</span></button>')
        if i < len(all_sessions) - 1:
            nxt = all_sessions[i + 1]
            nav_parts.append(f'<button class="nav-btn nav-next" onclick="goTo(\'{nxt["slug"]}\')">'
                             f'<span class="nav-dir">Session suivante →</span>'
                             f'<span class="nav-title">{html.escape(nxt["title"])}</span></button>')
        if nav_parts:
            parts.append(f'      <!-- Prev/Next navigation --><nav class="snav">{"".join(nav_parts)}</nav>')

        parts.append('</div></div>')

    return "\n".join(parts)


def _build_js(modules_data: list[dict]) -> str:
    all_sessions = [s for m in modules_data for s in m["sessions"]]
    slugs = [s["slug"] for s in all_sessions]
    titles = {s["slug"]: s["title"] for s in all_sessions}
    mods = {s["slug"]: str(s["mod_num"]) for s in all_sessions}
    total = len(all_sessions)

    return f"""<script>
(function(){{
  var SLUGS={json.dumps(slugs)},TITLES={json.dumps(titles, ensure_ascii=False)},MODS={json.dumps(mods)},TOTAL={total},PK='permis_v3';
  var done=[];
  try{{var _d=localStorage.getItem(PK);if(_d)done=JSON.parse(_d)||[];}}catch(e){{}}
  function save(){{try{{localStorage.setItem(PK,JSON.stringify(done));}}catch(e){{}}}}
  function ui(){{
    var pct=Math.min(100,done.length/TOTAL*100);
    var pc=document.getElementById('pc');if(pc)pc.textContent=done.length+' / '+TOTAL;
    var pf=document.getElementById('pf');if(pf)pf.style.width=pct+'%';
    document.querySelectorAll('.sitem').forEach(function(el){{
      var s=el.getAttribute('data-slug'),isDone=done.includes(s);
      el.classList.toggle('done',isDone);
      var sc=el.querySelector('.sc');
      if(sc&&isDone&&sc.textContent.indexOf('✓')<0)sc.textContent+=' ✓';
    }});
    document.querySelectorAll('[data-index-slug]').forEach(function(li){{
      li.classList.toggle('idone',done.includes(li.getAttribute('data-index-slug')));
    }});
  }}
  var cur=null,doneT=null;
  window.goTo=function(slug){{
    document.querySelectorAll('.spage').forEach(function(el){{el.style.display='none';}});
    document.querySelectorAll('.sitem.current').forEach(function(el){{el.classList.remove('current');}});
    document.querySelectorAll('.mhdr.active').forEach(function(el){{el.classList.remove('active');}});
    var page=document.getElementById('sp-'+slug);
    if(!page){{console.error('Not found: sp-'+slug);return;}}
    page.style.display='';
    var item=document.querySelector('.sitem[data-slug="'+slug+'"]');
    if(item){{
      item.classList.add('current');
      var ul=item.closest('.mitems');
      if(ul){{ul.classList.remove('collapsed');var hdr=ul.previousElementSibling;
        if(hdr){{hdr.classList.add('open');hdr.classList.add('active');}}}}
    }}
    var mt=document.getElementById('mtitle');
    if(mt)mt.textContent=slug==='__idx__'?'Plan du cours':(TITLES[slug]||slug);
    cur=slug;closeSb();window.scrollTo(0,0);
    if(slug!=='__idx__'){{
      if(doneT)clearTimeout(doneT);
      doneT=setTimeout(function(){{if(!done.includes(slug)){{done.push(slug);save();ui();}}}},30000);
    }}
  }};
  window.toggleMod=function(hdr){{
    hdr.classList.toggle('open');
    var ul=hdr.nextElementSibling;if(ul)ul.classList.toggle('collapsed');
  }};
  window.toggleSb=function(){{
    document.getElementById('sb').classList.toggle('open');
    document.getElementById('ov').classList.toggle('open');
  }};
  window.closeSb=function(){{
    document.getElementById('sb').classList.remove('open');
    document.getElementById('ov').classList.remove('open');
  }};
  document.addEventListener('keydown',function(e){{
    if(!cur||cur==='__idx__')return;
    if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')return;
    var i=SLUGS.indexOf(cur);
    if(e.key==='ArrowRight'&&i<SLUGS.length-1)goTo(SLUGS[i+1]);
    if(e.key==='ArrowLeft'&&i>0)goTo(SLUGS[i-1]);
  }});
  document.querySelectorAll('.callout-quiz ol,.callout-quiz ul').forEach(function(list){{
    list.querySelectorAll('li').forEach(function(li){{
      li.addEventListener('click',function(){{
        list.querySelectorAll('li').forEach(function(o){{o.classList.remove('sel');}});
        li.classList.add('sel');
      }});
    }});
  }});
  document.querySelectorAll('table').forEach(function(t){{
    if(t.closest('.table-wrap'))return;
    var w=document.createElement('div');w.className='table-wrap';
    t.parentNode.insertBefore(w,t);w.appendChild(t);
  }});
  ui();
  goTo('0-0-prologue');
}})();

// Lightbox
(function(){{
  var lb=document.getElementById('lb');
  var lbImg=document.getElementById('lb-img');
  var lbCap=document.getElementById('lb-cap');
  var lbPrev=document.getElementById('lb-prev');
  var lbNext=document.getElementById('lb-next');
  var imgs=[],lbIdx=0;
  function collectImgs(){{
    var visPage=document.querySelector('.spage[style=""], .spage:not([style])');
    if(!visPage) visPage=document.body;
    imgs=Array.from(visPage.querySelectorAll('.wiki-image'));
  }}
  function open(idx){{
    collectImgs();
    if(!imgs.length) return;
    lbIdx=((idx%imgs.length)+imgs.length)%imgs.length;
    var img=imgs[lbIdx];
    lbImg.src=img.src; lbImg.alt=img.alt||'';
    var fig=img.closest('figure');
    var cap=img.getAttribute('data-caption')||img.alt||
            (fig&&fig.querySelector('figcaption')?fig.querySelector('figcaption').textContent:'')||'';
    lbCap.textContent=cap;
    lb.classList.add('open');
    document.body.style.overflow='hidden';
    lbPrev.style.display=imgs.length>1?'flex':'none';
    lbNext.style.display=imgs.length>1?'flex':'none';
  }}
  function close(){{lb.classList.remove('open');document.body.style.overflow='';}}
  document.addEventListener('click',function(e){{
    var img=e.target.closest('.wiki-image');
    if(img){{collectImgs();var idx=imgs.indexOf(img);open(idx>=0?idx:0);e.stopPropagation();}}
  }});
  lb.addEventListener('click',function(e){{if(e.target===lb)close();}});
  document.getElementById('lb-close').addEventListener('click',close);
  lbPrev.addEventListener('click',function(e){{e.stopPropagation();open(lbIdx-1);}});
  lbNext.addEventListener('click',function(e){{e.stopPropagation();open(lbIdx+1);}});
  document.addEventListener('keydown',function(e){{
    if(!lb.classList.contains('open'))return;
    if(e.key==='Escape')close();
    if(e.key==='ArrowLeft')open(lbIdx-1);
    if(e.key==='ArrowRight')open(lbIdx+1);
  }});
}})();
</script>"""


# The CSS is extracted verbatim from the existing permis-cours-complet.html
CSS = """\
:root{
  color-scheme:light;
  --navy:#1a2e4a;--navy-d:#0e1e30;--teal:#0d7377;--tl:#14a0a5;
  --tp:rgba(13,115,119,.08);--amber:#f5a623;--as:rgba(245,166,35,.12);
  --red:#dc2626;--green:#059669;--gs:rgba(5,150,105,.08);
  --bg:#f0f4f9;--sur:#fff;--text:#18202e;--muted:#64748b;--bdr:#e2e8f0;
  --sm:0 1px 3px rgba(15,23,42,.06);--md:0 4px 16px rgba(15,23,42,.10);--lg:0 12px 40px rgba(15,23,42,.16);
  --fb:'Georgia','Times New Roman',serif;
  --fu:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  --fm:'SF Mono','Courier New',monospace;
  --r1:6px;--r2:10px;--r3:16px;--r4:24px;
  --sw:290px;
}
*,*::before,*::after{box-sizing:border-box}
html,body{margin:0;padding:0;min-height:100%;background:var(--bg);color:var(--text)}
body{font-family:var(--fb);font-size:18px;line-height:1.82;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:var(--teal);text-decoration:none}a:hover{text-decoration:underline}
img{max-width:100%;height:auto;display:block}hr{border:none;border-top:1px solid var(--bdr);margin:3em 0}

/* Layout */
#app{display:flex;min-height:100vh}

/* Sidebar */
#sb{width:var(--sw);flex-shrink:0;background:var(--navy-d);color:#c8d6e8;
  display:flex;flex-direction:column;position:sticky;top:0;height:100vh;
  overflow-y:auto;font-family:var(--fu);scrollbar-width:thin;
  scrollbar-color:rgba(255,255,255,.1) transparent;z-index:100}
#sb::-webkit-scrollbar{width:4px}#sb::-webkit-scrollbar-thumb{background:rgba(255,255,255,.12);border-radius:2px}

.sb-hdr{padding:22px 20px 16px;border-bottom:1px solid rgba(255,255,255,.06);
  display:flex;align-items:center;gap:10px;flex-shrink:0}
.sb-hdr .anc{font-size:22px}
.bt{color:var(--tl);font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase}
.bs{color:rgba(255,255,255,.35);font-size:10px;letter-spacing:.10em;text-transform:uppercase;margin-top:1px}

.sb-idx{display:flex;align-items:center;gap:8px;margin:10px 14px 2px;padding:8px 10px;
  border-radius:var(--r1);font-size:12px;color:rgba(255,255,255,.5);cursor:pointer;
  border:1px solid rgba(255,255,255,.06);transition:all .15s}
.sb-idx:hover{color:var(--tl);border-color:rgba(20,160,165,.3);background:rgba(20,160,165,.06)}

.sb-nav{padding:8px 0 16px;flex:1}

.mgroup{margin-bottom:2px}
.mhdr{display:flex;align-items:center;gap:8px;padding:8px 14px 6px;cursor:pointer;
  user-select:none;font-size:10px;font-weight:700;letter-spacing:.14em;
  text-transform:uppercase;color:rgba(255,255,255,.38);transition:color .15s}
.mhdr:hover{color:rgba(255,255,255,.65)}
.mhdr.active{color:var(--tl)}
.mnum{width:18px;height:18px;border-radius:4px;background:rgba(255,255,255,.06);
  display:inline-flex;align-items:center;justify-content:center;font-size:9px;flex-shrink:0}
.mhdr.active .mnum{background:rgba(20,160,165,.25);color:var(--tl)}
.mchev{margin-left:auto;font-size:8px;transition:transform .2s}
.mhdr.open .mchev{transform:rotate(90deg)}

.mitems{padding-left:0;list-style:none;margin:0}
.mitems.collapsed{display:none}

.sitem{display:flex;align-items:flex-start;gap:10px;padding:7px 14px 7px 30px;
  font-size:12.5px;color:rgba(255,255,255,.60);cursor:pointer;
  transition:all .14s;border-left:2px solid transparent;line-height:1.35}
.sitem:hover{color:rgba(255,255,255,.88);background:rgba(255,255,255,.03)}
.sitem.current{color:#fff;background:rgba(20,160,165,.12);border-left-color:var(--tl)}
.sitem.done{opacity:.65}
.sc{flex-shrink:0;font-size:10px;color:rgba(255,255,255,.28);margin-top:2px;font-family:var(--fm)}
.sitem.current .sc{color:var(--tl)}
.sn{display:block}.sd{display:block;font-size:10px;color:rgba(255,255,255,.25);margin-top:1px}

.sb-prog{padding:14px 16px 18px;border-top:1px solid rgba(255,255,255,.06);flex-shrink:0}
.pl{display:flex;justify-content:space-between;font-size:10px;color:rgba(255,255,255,.38);
  letter-spacing:.1em;text-transform:uppercase;margin-bottom:7px}
.pb{height:3px;background:rgba(255,255,255,.06);border-radius:2px;overflow:hidden}
.pf{height:100%;background:linear-gradient(90deg,var(--teal),var(--tl));transition:width .4s}

/* Main */
#main{flex:1;min-width:0;padding:40px clamp(16px,3vw,56px) 80px;
  display:flex;flex-direction:column;align-items:stretch}

/* Card */
.card{background:var(--sur);border-radius:var(--r4);box-shadow:var(--md);
  padding:52px clamp(24px,4vw,72px) 60px;width:100%;max-width:980px;
  margin:0 auto;overflow:hidden}

.session-meta{display:flex;align-items:center;gap:10px;margin-bottom:22px;font-family:var(--fu);flex-wrap:wrap}
.meta-badge{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:3px 10px;border-radius:999px}
.meta-module{background:var(--tp);color:var(--teal)}
.meta-code{background:rgba(26,46,74,.08);color:var(--navy)}
.meta-duration{color:var(--muted);font-size:12px;margin-left:auto}

/* Typography */
h1{font-family:var(--fu);font-weight:800;font-size:clamp(28px,3.5vw,40px);
  line-height:1.12;letter-spacing:-.025em;color:var(--navy);margin:0 0 40px}
h2{font-family:var(--fu);font-weight:700;font-size:22px;color:var(--navy);
  border-left:4px solid var(--teal);padding-left:14px;margin:56px 0 18px;line-height:1.3}
h3{font-family:var(--fu);font-weight:600;font-size:18px;color:var(--teal);margin:34px 0 12px}
h4{font-family:var(--fu);font-weight:600;font-size:15px;color:var(--navy);margin:24px 0 8px}
p{margin:0 0 1.15em}
strong{color:var(--navy);font-weight:700}em{color:var(--teal);font-style:italic}
blockquote{margin:1.5em 0;padding:14px 20px;border-left:4px solid var(--amber);
  background:var(--as);border-radius:0 var(--r1) var(--r1) 0;font-style:italic}
blockquote p:last-child{margin-bottom:0}
ul,ol{padding-left:1.7em;margin:0 0 1.2em}li{margin-bottom:.38em}li::marker{color:var(--teal)}
code{font-family:var(--fm);font-size:.87em;padding:2px 6px;background:var(--tp);color:var(--teal);border-radius:4px}
pre{background:var(--navy-d);color:#e0e8f0;padding:18px 22px;border-radius:var(--r2);
  overflow-x:auto;font-family:var(--fm);font-size:14px;line-height:1.55}
pre code{background:transparent;color:inherit;padding:0}

/* Tables */
.table-wrap{overflow-x:auto;margin:24px 0;border-radius:var(--r2);box-shadow:var(--sm)}
table{width:100%;border-collapse:collapse;font-family:var(--fu);font-size:14.5px;min-width:400px}
thead{background:var(--navy);color:#fff}
th{text-align:left;padding:12px 16px;font-weight:600;font-size:12px;letter-spacing:.05em;text-transform:uppercase}
td{padding:11px 16px;border-bottom:1px solid var(--bdr);vertical-align:top}
tbody tr:nth-child(even){background:rgba(13,115,119,.025)}
tbody tr:hover{background:rgba(13,115,119,.06)}
tbody tr:last-child td{border-bottom:none}

/* Callouts */
.callout{margin:28px 0;border-radius:var(--r2);overflow:hidden;box-shadow:var(--sm)}
.callout-label{font-family:var(--fu);font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;padding:9px 18px}
.callout-body{padding:4px 18px 16px}.callout-body p:last-child{margin-bottom:0}
.callout-scene{background:linear-gradient(135deg,#0e1e30,#1a2e4a);color:#d4e6f4;border-left:4px solid var(--tl)}
.callout-scene .callout-label{color:var(--tl)}
.callout-scene .callout-body{color:#c8d8e8;font-style:italic;line-height:1.78}
.callout-scene strong{color:#e8f4ff}.callout-scene em{color:var(--tl);font-style:normal}
.callout-golfe{background:var(--tp);border-left:4px solid var(--teal)}
.callout-golfe .callout-label{color:var(--teal)}
.callout-attention{background:var(--as);border-left:4px solid var(--amber)}
.callout-attention .callout-label{color:#9a6310}
.callout-quiz{background:rgba(26,46,74,.04);border:1px solid rgba(26,46,74,.12);border-left:4px solid var(--navy)}
.callout-quiz .callout-label{color:var(--navy)}
.callout-quiz ol,.callout-quiz ul{padding-left:0;list-style:none;margin:8px 0 12px}
.callout-quiz li{padding:8px 14px;border-radius:var(--r1);border:1px solid rgba(26,46,74,.12);
  margin-bottom:6px;cursor:pointer;transition:all .15s;font-size:16px;
  font-family:var(--fu);background:var(--sur);color:var(--text);user-select:none}
.callout-quiz li::marker{content:none}
.callout-quiz li:hover{border-color:var(--teal);background:var(--tp)}
.callout-quiz li.sel{border-color:var(--teal);background:var(--tp);color:var(--teal);font-weight:600}
.callout-quiz li.sel::before{content:"✓ "}
.callout-transition{background:transparent;border:1px dashed var(--bdr);border-left:3px solid var(--muted)}
.callout-transition .callout-label{color:var(--muted)}
.callout-transition .callout-body{font-style:italic;color:var(--muted)}
.callout-savoir{background:var(--gs);border-left:4px solid var(--green)}
.callout-savoir .callout-label{color:var(--green)}

/* Quiz answers */
.quiz-answer{margin:6px 0;border-left:3px solid var(--teal);background:var(--tp);border-radius:var(--r1);overflow:hidden}
.quiz-answer summary{list-style:none;cursor:pointer;padding:8px 14px;font-family:var(--fu);font-size:13px;font-weight:600;color:var(--teal);user-select:none}
.quiz-answer summary::-webkit-details-marker{display:none}
.quiz-answer summary::before{content:"▶  ";font-size:9px}
.quiz-answer[open] summary::before{content:"▼  "}
.quiz-answer>*:not(summary){padding:0 14px 10px}

/* Wikilinks */
.wikilink{display:inline-block;font-family:var(--fm);font-size:11px;padding:1px 7px;
  background:var(--tp);color:var(--teal);border:1px solid rgba(13,115,119,.25);
  border-radius:999px;vertical-align:baseline;line-height:1.6;margin:0 2px}

/* Images */
.wiki-image-wrap{margin:36px 0;text-align:center}
.wiki-image-wrap figcaption{font-family:var(--fu);font-size:13px;color:var(--muted);margin-top:10px;font-style:italic}
.wiki-image{display:inline-block;max-width:100%;border-radius:var(--r2);box-shadow:var(--md)}

/* Static prev/next nav */
.snav{display:flex;gap:16px;margin-top:60px;padding-top:32px;border-top:1px solid var(--bdr);font-family:var(--fu)}
.nav-btn{flex:1;display:flex;flex-direction:column;gap:4px;padding:18px 22px;
  border:1px solid var(--bdr);border-radius:var(--r2);transition:all .15s;
  color:var(--text);cursor:pointer;background:var(--sur)}
.nav-btn:hover{border-color:var(--teal);box-shadow:var(--sm);background:var(--tp)}
.nav-prev{align-items:flex-start;text-align:left}
.nav-next{align-items:flex-end;text-align:right}
.nav-dir{font-size:11px;color:var(--muted);letter-spacing:.1em;text-transform:uppercase;font-weight:600;display:block}
.nav-title{font-size:15px;font-weight:600;color:var(--navy);line-height:1.3;display:block}
.nav-btn:hover .nav-dir{color:var(--teal)}

/* Details */
details{margin:18px 0;border-left:3px solid var(--teal);background:var(--tp);border-radius:var(--r2);overflow:hidden}
details summary{list-style:none;cursor:pointer;padding:13px 16px;font-family:var(--fu);font-weight:600;color:var(--teal);display:flex;align-items:center;gap:8px;user-select:none}
details summary::-webkit-details-marker{display:none}
details summary::before{content:"▶";font-size:9px;display:inline-block;transition:transform .2s}
details[open] summary::before{transform:rotate(90deg)}
details>*:not(summary){padding:0 16px 14px}

/* Index */
.idx-intro{font-family:var(--fu);font-size:15px;color:var(--muted);margin-bottom:32px}
.igrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px}
.icard{background:var(--sur);border:1px solid var(--bdr);border-radius:var(--r3);padding:22px;transition:box-shadow .15s}
.icard:hover{box-shadow:var(--md)}
.ictitle{font-family:var(--fu);font-size:14px;font-weight:700;color:var(--navy);margin:0 0 12px;display:flex;align-items:center;gap:8px}
.ibadge{width:22px;height:22px;background:var(--tp);color:var(--teal);border-radius:5px;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;flex-shrink:0}
.icard ul{padding:0;list-style:none;margin:0}
.icard ul li{padding:7px 0;border-bottom:1px solid var(--bdr);font-family:var(--fu);font-size:13px;cursor:pointer;color:var(--teal);display:flex;align-items:center;gap:8px;transition:color .12s}
.icard ul li:last-child{border-bottom:none}
.icard ul li:hover{color:var(--navy)}
.li-code{font-size:10px;color:var(--muted);font-family:var(--fm);flex-shrink:0;width:26px}
.icard ul li.idone{color:var(--muted)}.icard ul li.idone .li-code::after{content:" ✓";color:var(--green)}

/* Scrollbar */
::-webkit-scrollbar{width:6px;height:6px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:rgba(26,46,74,.15);border-radius:3px}

/* Mobile */
#mbar{display:none;position:fixed;top:0;left:0;right:0;height:52px;background:var(--navy-d);
  z-index:200;align-items:center;padding:0 16px;gap:12px;border-bottom:1px solid rgba(255,255,255,.07)}
#mbar button{background:none;border:none;color:rgba(255,255,255,.8);font-size:22px;cursor:pointer;padding:4px;line-height:1}
#mbar span{font-family:var(--fu);font-size:13px;font-weight:600;color:rgba(255,255,255,.85);
  flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#ov{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:150}
#ov.open{display:block}

@media(max-width:768px){
  #mbar{display:flex}
  #app{flex-direction:column}
  #sb{position:fixed;top:0;left:0;height:100vh;width:290px;
    transform:translateX(-100%);z-index:200;transition:transform .3s}
  #sb.open{transform:translateX(0)}
  #main{padding:68px 12px 80px}
  .card{padding:24px 18px 32px;border-radius:var(--r3)}
  h1{font-size:clamp(22px,6vw,28px);margin-bottom:24px}
  h2{font-size:19px;margin:40px 0 14px}
  .snav{flex-direction:column}
}

/* Lightbox */
#lb{position:fixed;inset:0;background:rgba(0,0,0,0);z-index:1000;
  display:flex;align-items:center;justify-content:center;
  cursor:zoom-out;pointer-events:none;transition:background .25s}
#lb.open{background:rgba(0,0,0,.92);pointer-events:auto}
#lb-inner{position:relative;max-width:94vw;max-height:94vh;
  display:flex;flex-direction:column;align-items:center;gap:12px;
  opacity:0;transform:scale(.94);transition:opacity .22s,transform .22s}
#lb.open #lb-inner{opacity:1;transform:scale(1)}
#lb-img{max-width:92vw;max-height:82vh;border-radius:10px;
  object-fit:contain;box-shadow:0 8px 60px rgba(0,0,0,.7);cursor:default}
#lb-cap{color:rgba(255,255,255,.7);font-family:var(--fu);font-size:14px;
  font-style:italic;text-align:center;max-width:600px}
#lb-close{position:fixed;top:18px;right:22px;width:40px;height:40px;
  background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);
  border-radius:50%;color:#fff;font-size:18px;display:flex;
  align-items:center;justify-content:center;cursor:pointer;z-index:1001;
  transition:background .2s;line-height:1}
#lb-close:hover{background:rgba(255,255,255,.25)}
#lb-prev,#lb-next{position:fixed;top:50%;transform:translateY(-50%);
  width:44px;height:44px;background:rgba(255,255,255,.1);
  border:1px solid rgba(255,255,255,.18);border-radius:50%;color:#fff;
  font-size:20px;display:flex;align-items:center;justify-content:center;
  cursor:pointer;z-index:1001;transition:background .2s;line-height:1}
#lb-prev{left:16px}#lb-next{right:16px}
#lb-prev:hover,#lb-next:hover{background:rgba(255,255,255,.22)}
.wiki-image{cursor:zoom-in;transition:box-shadow .2s,transform .2s}
.wiki-image:hover{box-shadow:0 8px 32px rgba(15,23,42,.18);transform:scale(1.005)}
"""


def main() -> None:
    all_modules, all_sessions = build_manifest()
    if not all_sessions:
        print("No module-*.md files found.")
        return

    # Build data structure with rendered HTML
    modules_data: list[dict] = []
    for mod in all_modules:
        sessions_data = []
        for s in mod.sessions:
            body_html = _render_body(s.path)
            sessions_data.append({
                "slug": f"{s.module_num}-{s.session_num}-{s.slug}",
                "code": s.code,
                "title": s.title,
                "module_title": s.module_title,
                "mod_num": s.module_num,
                "duration": s.duration_min,
                "body_html": body_html,
            })
        modules_data.append({
            "num": mod.num,
            "title": mod.title,
            "sessions": sessions_data,
        })

    # Copy assets
    ASSETS_DST.mkdir(parents=True, exist_ok=True)
    asset_count = 0
    if ASSETS_SRC.exists():
        for f in ASSETS_SRC.iterdir():
            if f.is_file():
                shutil.copy2(f, ASSETS_DST / f.name)
                asset_count += 1

    # Assemble the HTML
    sidebar_html = _build_sidebar_html(modules_data)
    index_html = _build_index_html(modules_data)
    sessions_html = _build_sessions_html(modules_data)
    js_html = _build_js(modules_data)

    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Permis Côtier — Cours Complet</title>
<style>
{CSS}</style>
</head>
<body>
<div id="mbar">
  <button onclick="toggleSb()">☰</button>
  <span id="mtitle">Permis Côtier</span>
</div>
<div id="ov" onclick="closeSb()"></div>
<div id="app">
  <nav id="sb">
{sidebar_html}
  </nav>
  <div id="main">
{index_html}

{sessions_html}
  </div>
</div>
{js_html}

<!-- Lightbox -->
<div id="lb" role="dialog" aria-modal="true" aria-label="Image agrandie">
  <button id="lb-close" aria-label="Fermer">✕</button>
  <button id="lb-prev"  aria-label="Précédente">‹</button>
  <button id="lb-next"  aria-label="Suivante">›</button>
  <div id="lb-inner">
    <img id="lb-img" src="" alt="">
    <div id="lb-cap"></div>
  </div>
</div>
</body>
</html>"""

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(full_html, encoding="utf-8")

    size_kb = OUTPUT_FILE.stat().st_size / 1024
    total_sessions = sum(len(m["sessions"]) for m in modules_data)
    print(f"Assets: {asset_count} file(s) copied to {ASSETS_DST.relative_to(REPO)}")
    print(f"Generated: {OUTPUT_FILE.relative_to(REPO)} ({size_kb:.0f} KB, {total_sessions} sessions)")


if __name__ == "__main__":
    main()
