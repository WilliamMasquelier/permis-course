#!/usr/bin/env python3
"""
Module-based course renderer for the Permis Côtier lesson redesign.

Reads Wiki/wiki/lessons/module-*.md files, builds a full course manifest,
and outputs per-session HTML files plus an index page.

File naming convention: module-{N}-{M}-{slug}.md
  N = module number (0 = prologue, 7 = epilogue)
  M = session within module (0-indexed for single-session modules)
  slug = short title slug

Output structure:
  output/lessons/index.html              ← course map
  output/lessons/module-N/session-N-M-slug.html

Usage:
    python scripts/render_course.py              # render everything
    python scripts/render_course.py --check      # dry-run
    python scripts/render_course.py 3-2          # render session matching "3-2"
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from markdown_it import MarkdownIt

REPO = Path(__file__).parent.parent
LESSONS_DIR = REPO / "Wiki" / "wiki" / "lessons"
ASSETS_SRC = REPO / "Wiki" / "assets" / "images"
OUTPUT_DIR = REPO / "output" / "lessons"
TEMPLATES_DIR = REPO / "templates"


# ── Data model ────────────────────────────────────────────────────────────────

@dataclass
class SessionMeta:
    path: Path
    module_num: int
    session_num: int
    slug: str
    title: str
    module_title: str
    duration_min: int = 30
    status: str = "draft"
    # Populated after full manifest is built
    prev: "SessionMeta | None" = field(default=None, repr=False)
    next: "SessionMeta | None" = field(default=None, repr=False)

    @property
    def code(self) -> str:
        return f"{self.module_num}.{self.session_num}"

    @property
    def output_path(self) -> Path:
        return OUTPUT_DIR / f"module-{self.module_num}" / f"session-{self.module_num}-{self.session_num}-{self.slug}.html"

    @property
    def rel_path(self) -> str:
        """Relative URL from output/lessons/"""
        return f"module-{self.module_num}/session-{self.module_num}-{self.session_num}-{self.slug}.html"

    def rel_from(self, other_path: Path) -> str:
        """Relative URL from a sibling session page to this one."""
        import os
        return os.path.relpath(self.output_path, other_path.parent)


@dataclass
class ModuleMeta:
    num: int
    title: str
    sessions: list[SessionMeta] = field(default_factory=list)


# ── Frontmatter ───────────────────────────────────────────────────────────────

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines(keepends=True)
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip("\r\n") == "---"), -1)
    if end == -1:
        return {}, text
    meta: dict = {}
    for line in lines[1:end]:
        m = re.match(r"^([\w-]+)\s*:\s*(.*)$", line.rstrip("\r\n"))
        if m:
            val = m.group(2).strip().strip('"').strip("'")
            meta[m.group(1)] = val
    return meta, "".join(lines[end + 1:])


# ── Manifest builder ──────────────────────────────────────────────────────────

_FILE_PAT = re.compile(r"^module-(\d+)-(\d+)-(.+)\.md$")

MODULE_TITLES = {
    0: "Prologue — Le Départ",
    1: "Le Bateau et ses Règles",
    2: "Lire la Mer",
    3: "Naviguer",
    4: "Manœuvrer",
    5: "Sécurité",
    6: "Radio et Réglementation",
    7: "Épilogue et Examen Blanc",
}


def build_manifest(filter_slug: str | None = None) -> tuple[list[ModuleMeta], list[SessionMeta]]:
    if not LESSONS_DIR.exists():
        return [], []

    sessions: list[SessionMeta] = []
    for f in sorted(LESSONS_DIR.glob("module-*.md")):
        m = _FILE_PAT.match(f.name)
        if not m:
            continue
        mod_n, sess_n, slug = int(m.group(1)), int(m.group(2)), m.group(3)
        raw = f.read_text(encoding="utf-8")
        meta, _ = _parse_frontmatter(raw)
        title = meta.get("title", slug.replace("-", " ").title())
        mod_title = meta.get("module_title", MODULE_TITLES.get(mod_n, f"Module {mod_n}"))
        duration = int(meta.get("duration_min", 30))
        status = meta.get("status", "draft")
        sessions.append(SessionMeta(
            path=f,
            module_num=mod_n,
            session_num=sess_n,
            slug=slug,
            title=title,
            module_title=mod_title,
            duration_min=duration,
            status=status,
        ))

    # Wire prev/next
    for i, s in enumerate(sessions):
        s.prev = sessions[i - 1] if i > 0 else None
        s.next = sessions[i + 1] if i < len(sessions) - 1 else None

    # Group into modules
    modules: dict[int, ModuleMeta] = {}
    for s in sessions:
        if s.module_num not in modules:
            modules[s.module_num] = ModuleMeta(num=s.module_num, title=s.module_title)
        modules[s.module_num].sessions.append(s)

    ordered_modules = [modules[k] for k in sorted(modules)]
    return ordered_modules, sessions


# ── Markdown pre/post processing ──────────────────────────────────────────────

_md_parser = MarkdownIt("commonmark", {"html": True}).enable("table")


def _slug_to_label(slug: str) -> str:
    name = slug.split("/")[-1].split("|")[0]
    return name.replace("-", " ").title()


CALLOUT_TYPES = {
    "SCENE": ("callout-scene", "⚓ Scène"),
    "EXEMPLE GOLFE": ("callout-golfe", "🗺️ Exemple — Golfe de Fethiye"),
    "ATTENTION": ("callout-attention", "⚠️ Attention"),
    "MINI-QUIZ": ("callout-quiz", "📝 Mini-Quiz"),
    "TRANSITION": ("callout-transition", "→ Cap sur la suite"),
    "SAVOIR FAIRE": ("callout-savoir", "✅ À retenir"),
}


def _preprocess_callouts(md: str) -> str:
    """Convert > [TYPE]\n> content blocks into HTML callout divs."""
    lines = md.splitlines()
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect callout start: "> [TYPE]" possibly with trailing text
        callout_match = re.match(r"^>\s*\[([A-ZÀÂÇÈÉÊËÎÏÙÛÜ/ ]+)\]\s*(.*)$", line)
        if callout_match:
            ctype = callout_match.group(1).strip()
            rest_first = callout_match.group(2).strip()
            css_class, label = CALLOUT_TYPES.get(ctype, (f"callout-{ctype.lower().replace(' ', '-')}", ctype))
            # Collect continuation lines (lines starting with ">")
            content_lines = []
            if rest_first:
                content_lines.append(rest_first)
            i += 1
            while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
                if lines[i].startswith(">"):
                    stripped = lines[i][1:].lstrip(" ")
                    content_lines.append(stripped)
                elif lines[i].strip() == "" and i + 1 < len(lines) and lines[i + 1].startswith(">"):
                    content_lines.append("")
                else:
                    break
                i += 1
            inner_md = "\n".join(content_lines)
            # Escape the inner content so we can inject it as raw HTML after rendering
            result.append(f'<div class="callout {css_class}"><div class="callout-label">{label}</div><div class="callout-body">')
            result.append(f'%%CALLOUT_INNER%%{inner_md}%%CALLOUT_END%%')
            result.append('</div></div>')
        else:
            result.append(line)
            i += 1
    return "\n".join(result)


def _render_callout_inners(html: str) -> str:
    """Render markdown inside callout blocks."""
    def render_inner(m: re.Match) -> str:
        inner_md = m.group(1)
        rendered = _md_parser.render(inner_md).strip()
        return rendered

    return re.sub(r"%%CALLOUT_INNER%%(.*?)%%CALLOUT_END%%", render_inner, html, flags=re.DOTALL)


def _preprocess_wikilinks(md: str) -> str:
    # Image embeds
    md = re.sub(
        r"!\[\[([^\]|#\n]+?)(?:\|([^\]\n]*))?\]\]",
        lambda m: (
            f'\n\n<div class="wiki-image-wrap">'
            f'<img class="wiki-image" src="../assets/{m.group(1).strip()}" '
            f'alt="{(m.group(2) or m.group(1)).strip()}">'
            f'</div>\n\n'
        ),
        md,
    )
    # Internal wikilinks
    md = re.sub(
        r"\[\[([^\]|#\n]+?)(?:\|([^\]\n]*))?\]\]",
        lambda m: (
            f'<span class="wikilink" '
            f'data-label="{_slug_to_label((m.group(2) or m.group(1)).strip())}">'
            f'{(m.group(2) or m.group(1)).strip()}</span>'
        ),
        md,
    )
    return md


def _wrap_quiz_answers(html: str) -> str:
    """Make quiz answer lines collapsible."""
    return re.sub(
        r'<strong>Réponse\s*:</strong>(.*?)(?=<br|<p>|<li>|</ul>|</div>|$)',
        lambda m: (
            f'<details class="quiz-answer"><summary>Voir la réponse</summary>'
            f'<strong>Réponse :</strong>{m.group(1)}</details>'
        ),
        html,
        flags=re.DOTALL,
    )


# ── Render one session ────────────────────────────────────────────────────────

_jinja_env: Environment | None = None


def _get_jinja_env() -> Environment:
    global _jinja_env
    if _jinja_env is None:
        _jinja_env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            autoescape=False,
        )
    return _jinja_env


def render_session(session: SessionMeta, all_modules: list[ModuleMeta]) -> Path:
    raw = session.path.read_text(encoding="utf-8")
    meta, body_md = _parse_frontmatter(raw)

    # Pre-process
    body_md = _preprocess_callouts(body_md)
    body_md = _preprocess_wikilinks(body_md)

    # Render markdown (callout inners still tagged)
    html_body = _md_parser.render(body_md)

    # Post-process
    html_body = _render_callout_inners(html_body)
    html_body = _wrap_quiz_answers(html_body)

    # Build course nav for sidebar (relative paths from this session's location)
    course_nav = []
    for mod in all_modules:
        mod_sessions = []
        for s in mod.sessions:
            mod_sessions.append({
                "code": s.code,
                "title": s.title,
                "slug": s.slug,
                "rel_url": s.rel_from(session.output_path),
                "is_current": s is session,
                "duration_min": s.duration_min,
            })
        course_nav.append({
            "num": mod.num,
            "title": mod.title,
            "sessions": mod_sessions,
            "has_current": any(s["is_current"] for s in mod_sessions),
        })

    prev_url = session.prev.rel_from(session.output_path) if session.prev else None
    next_url = session.next.rel_from(session.output_path) if session.next else None
    index_url = "../index.html"

    template = _get_jinja_env().get_template("permis-course.html.j2")
    full_html = template.render(
        title=session.title,
        session_code=session.code,
        module_title=session.module_title,
        module_num=session.module_num,
        duration_min=session.duration_min,
        body=html_body,
        course_nav=course_nav,
        prev_url=prev_url,
        prev_title=session.prev.title if session.prev else None,
        next_url=next_url,
        next_title=session.next.title if session.next else None,
        index_url=index_url,
        total_sessions=sum(len(m.sessions) for m in all_modules),
        course_nav_json=json.dumps(course_nav),
    )

    session.output_path.parent.mkdir(parents=True, exist_ok=True)
    session.output_path.write_text(full_html, encoding="utf-8")
    return session.output_path


# ── Render index page ─────────────────────────────────────────────────────────

def render_index(all_modules: list[ModuleMeta]) -> Path:
    template = _get_jinja_env().get_template("permis-course-index.html.j2")

    # Build index data
    modules_data = []
    for mod in all_modules:
        sessions_data = []
        for s in mod.sessions:
            sessions_data.append({
                "code": s.code,
                "title": s.title,
                "slug": s.slug,
                "url": s.rel_path,
                "duration_min": s.duration_min,
                "status": s.status,
            })
        modules_data.append({
            "num": mod.num,
            "title": mod.title,
            "sessions": sessions_data,
            "total_duration": sum(s.duration_min for s in mod.sessions),
        })

    total_sessions = sum(len(m.sessions) for m in all_modules)
    total_duration = sum(s.duration_min for s in (s for m in all_modules for s in m.sessions))

    full_html = template.render(
        modules=modules_data,
        total_sessions=total_sessions,
        total_duration=total_duration,
    )

    index_path = OUTPUT_DIR / "index.html"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(full_html, encoding="utf-8")
    return index_path


# ── Assets copy ───────────────────────────────────────────────────────────────

def sync_assets() -> int:
    assets_dst = OUTPUT_DIR / "assets"
    assets_dst.mkdir(parents=True, exist_ok=True)
    count = 0
    if ASSETS_SRC.exists():
        for f in ASSETS_SRC.iterdir():
            if f.is_file():
                shutil.copy2(f, assets_dst / f.name)
                count += 1
    return count


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    args = sys.argv[1:]
    dry_run = "--check" in args
    filter_slug = next((a for a in args if not a.startswith("--")), None)

    all_modules, all_sessions = build_manifest()
    if not all_sessions:
        print(f"No module-*.md files found in {LESSONS_DIR}")
        sys.exit(1)

    if filter_slug:
        all_sessions = [s for s in all_sessions if filter_slug in f"{s.module_num}-{s.session_num}" or filter_slug in s.slug]

    if dry_run:
        print(f"Course manifest: {len(all_modules)} modules, {sum(len(m.sessions) for m in all_modules)} sessions total")
        print()
        for mod in all_modules:
            print(f"  Module {mod.num}: {mod.title}")
            for s in mod.sessions:
                flag = " [FILTER]" if filter_slug and s in all_sessions else ""
                print(f"    {s.code} — {s.title} ({s.duration_min}min) → {s.rel_path}{flag}")
        return

    copied = sync_assets()
    print(f"Assets: {copied} file(s) copied to output/lessons/assets/")

    all_modules_full, _ = build_manifest()  # always pass full manifest for nav

    rendered_count = 0
    for session in all_sessions:
        out = render_session(session, all_modules_full)
        size = out.stat().st_size
        print(f"  ✓ {session.code} {session.title} → {out.relative_to(REPO)} ({size:,} bytes)")
        rendered_count += 1

    if not filter_slug:
        idx = render_index(all_modules_full)
        print(f"\n  ✓ Index → {idx.relative_to(REPO)}")

    print(f"\nDone. {rendered_count} sessions rendered.")
    print(f"Open: python -m http.server 8080 --directory {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
