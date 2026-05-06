#!/usr/bin/env python3
"""Standalone lesson renderer — no report-renderer dependency.

Reads Wiki/wiki/lessons/session-*.md, converts to HTML using the
local permis-lesson Jinja2 template, writes to rendered/.

Usage:
    python scripts/render_lessons.py                  # render all sessions
    python scripts/render_lessons.py session-01       # render one session
    python scripts/render_lessons.py --check          # dry-run, list what would render
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from markdown_it import MarkdownIt

REPO = Path(__file__).parent.parent
LESSONS_DIR = REPO / "Wiki" / "wiki" / "lessons"
ASSETS_SRC = REPO / "Wiki" / "assets" / "images"
RENDERED_DIR = REPO / "rendered"
TEMPLATES_DIR = REPO / "templates"
TEMPLATE_NAME = "permis-lesson.html.j2"


# ── Frontmatter ──────────────────────────────────────────────────────────────

def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines(keepends=True)
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip("\r\n") == "---"), -1)
    if end == -1:
        return {}, text
    meta: dict[str, str] = {}
    for line in lines[1:end]:
        m = re.match(r"^([\w-]+)\s*:\s*(.*)$", line.rstrip("\r\n"))
        if m:
            val = m.group(2).strip().strip('"').strip("'")
            meta[m.group(1)] = val
    return meta, "".join(lines[end + 1:])


def _truthy(val: str | None) -> bool:
    return (val or "").strip().lower() in ("true", "1", "yes")


# ── Obsidian syntax pre-processing ───────────────────────────────────────────

def _preprocess(md: str) -> str:
    # ![[image.png]] → block div with img (on its own line so markdown-it doesn't wrap in <p>)
    md = re.sub(
        r"!\[\[([^\]]+)\]\]",
        lambda m: f'\n\n<div class="wiki-image-wrap"><img class="wiki-image" src="assets/{m.group(1)}" alt="{m.group(1)}"></div>\n\n',
        md,
    )
    # [[slug]] → <span class="wikilink">slug</span>
    md = re.sub(r"\[\[([^\]]+)\]\]", r'<span class="wikilink">\1</span>', md)
    return md


# ── Render one lesson ─────────────────────────────────────────────────────────

_md_parser = MarkdownIt("commonmark", {"html": True}).enable("table")

_jinja_env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    autoescape=False,
)


def render_lesson(lesson_path: Path, output_dir: Path) -> Path:
    raw = lesson_path.read_text(encoding="utf-8")
    meta, body_md = _parse_frontmatter(raw)

    title = meta.get("title", lesson_path.stem.replace("-", " ").title())
    dark_mode = _truthy(meta.get("dark_mode"))
    exam_mode = _truthy(meta.get("exam_mode"))

    body_md = _preprocess(body_md)
    html_body = _md_parser.render(body_md)

    template = _jinja_env.get_template(TEMPLATE_NAME)
    full_html = template.render(title=title, body=html_body, dark_mode=dark_mode, exam_mode=exam_mode)

    out_path = output_dir / f"{lesson_path.stem}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(full_html, encoding="utf-8")
    return out_path


# ── Assets copy ───────────────────────────────────────────────────────────────

def sync_assets(output_dir: Path) -> int:
    assets_dst = output_dir / "assets"
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

    lessons = sorted(LESSONS_DIR.glob("session-*.md")) if LESSONS_DIR.exists() else []
    if filter_slug:
        lessons = [l for l in lessons if filter_slug in l.stem]

    if not lessons:
        print(f"No lesson files found in {LESSONS_DIR}")
        sys.exit(1)

    if dry_run:
        print("Would render:")
        for l in lessons:
            print(f"  {l.name} → rendered/{l.stem}.html")
        return

    copied = sync_assets(RENDERED_DIR)
    print(f"Assets: {copied} file(s) copied to rendered/assets/")

    for lesson in lessons:
        out = render_lesson(lesson, RENDERED_DIR)
        size = out.stat().st_size
        print(f"✓ {lesson.name} → {out.name} ({size:,} bytes)")

    print(f"\nDone. Open: python -m http.server 8080 --directory {RENDERED_DIR}")


if __name__ == "__main__":
    main()
