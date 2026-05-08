from pathlib import Path

from scripts.render_lessons import render_lesson


def test_hints_are_hidden_and_wired(tmp_path: Path) -> None:
    lesson = tmp_path / "session-99-test.md"
    lesson.write_text(
        """---
title: Test
dark_mode: false
exam_mode: false
---

## TASK

Répondez.

## HINT_1

Premier indice.

## HINT_2

Deuxième indice.

## SOLUTION

La solution.
""",
        encoding="utf-8",
    )

    rendered = render_lesson(lesson, tmp_path).read_text(encoding="utf-8")

    assert 'class="hint-text hidden"' in rendered
    assert "Premier indice" in rendered
    assert "Tous les indices" in rendered
    assert "<h2>HINT_1</h2>" not in rendered
    assert '<details class="solution-block">' in rendered
