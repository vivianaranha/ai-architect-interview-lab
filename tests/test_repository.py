import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_question_count():
    q = json.loads((ROOT / "18-tools/questions.json").read_text(encoding="utf-8"))
    assert len(q) >= 120


def test_question_fields():
    q = json.loads((ROOT / "18-tools/questions.json").read_text(encoding="utf-8"))
    assert all(x.get("category") and x.get("question") and x.get("answer") for x in q)


def test_cases():
    assert len(list((ROOT / "13-system-design-case-studies").glob("[0-9][0-9]-*.md"))) >= 20


def test_whiteboards():
    assert len(list((ROOT / "14-whiteboard-challenges").glob("[0-9][0-9]-*.md"))) >= 15


def test_mocks():
    assert len(list((ROOT / "16-mock-interviews").glob("[0-9][0-9]-*.md"))) >= 10
