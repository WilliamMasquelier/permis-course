from scripts import wiki_health


def test_wiki_health_passes() -> None:
    count, lines = wiki_health.validate()
    assert count == 0, "\n".join(lines)
