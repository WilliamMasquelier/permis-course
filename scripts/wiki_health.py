#!/usr/bin/env python3
"""Validate the Permis course wiki and rendered lesson inputs."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "Wiki" / "wiki"
ASSETS = ROOT / "Wiki" / "assets" / "images"
RAW = ROOT / "raw"

REQUIRED_FRONTMATTER = ("title", "type", "sources", "related", "status", "updated")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    frontmatter = text[3:end]
    body = text[end + 4 :]
    data: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data, body


def wiki_targets() -> tuple[set[str], dict[str, list[str]]]:
    files = {p.relative_to(WIKI).with_suffix("").as_posix() for p in WIKI.rglob("*.md")}
    by_basename: dict[str, list[str]] = {}
    for target in files:
        by_basename.setdefault(target.rsplit("/", 1)[-1], []).append(target)
    return files, by_basename


def resolve_link(raw: str, current: Path, files: set[str], by_basename: dict[str, list[str]]) -> str | None:
    if raw.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg")):
        return "asset" if (ASSETS / raw).exists() else None
    rel = current.relative_to(WIKI).as_posix()
    folder = rel.rsplit("/", 1)[0] if "/" in rel else ""
    if "/" in raw:
        import posixpath

        candidate = posixpath.normpath(posixpath.join(folder, raw)) if raw.startswith(".") else posixpath.normpath(raw)
        return candidate if candidate in files else None
    matches = by_basename.get(raw, [])
    return matches[0] if len(matches) == 1 else None


def validate() -> tuple[int, list[str]]:
    files, by_basename = wiki_targets()
    errors: list[str] = []
    status_counts: Counter[str] = Counter()

    for path in sorted(WIKI.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        meta, body = parse_frontmatter(path)
        if not meta:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        for key in REQUIRED_FRONTMATTER:
            if key not in meta:
                errors.append(f"{rel}: missing frontmatter key '{key}'")
        if status := meta.get("status"):
            status_counts[status] += 1

        for source in re.findall(r"[\w./ -]+\.pdf|[\w./ -]+\.txt", meta.get("sources", "")):
            source = source.strip()
            source_path = (ROOT / source).resolve() if source.startswith("raw/") else (path.parent / source).resolve()
            if "raw/" in source and not source_path.exists():
                errors.append(f"{rel}: source path does not exist: {source}")

        for link in re.findall(r"!?\[\[([^\]|#\n]+)", body):
            if not resolve_link(link.strip(), path, files, by_basename):
                errors.append(f"{rel}: unresolved wikilink or image: [[{link}]]")

    lessons = sorted((WIKI / "lessons").glob("session-*.md"))
    orders = []
    for lesson in lessons:
        meta, _ = parse_frontmatter(lesson)
        if "lesson_order" not in meta:
            errors.append(f"{lesson.relative_to(ROOT).as_posix()}: missing lesson_order")
        else:
            orders.append(meta["lesson_order"])
        if "examen-blanc" not in lesson.name and "## TASK" not in lesson.read_text(encoding="utf-8"):
            errors.append(f"{lesson.relative_to(ROOT).as_posix()}: missing TASK section")

    if len(set(orders)) != len(orders):
        errors.append("lesson_order values must be unique")

    summary = [f"wiki files: {len(files)}", f"status counts: {dict(status_counts)}", f"lessons: {len(lessons)}"]
    return len(errors), summary + errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    count, lines = validate()
    if not args.quiet:
        for line in lines:
            print(line)
    sys.exit(1 if count else 0)


if __name__ == "__main__":
    main()
