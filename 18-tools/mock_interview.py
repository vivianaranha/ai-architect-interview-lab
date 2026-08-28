from __future__ import annotations

import json
import random
from pathlib import Path

DATA = Path(__file__).with_name("questions.json")


def load_questions():
    return json.loads(DATA.read_text(encoding="utf-8"))


def main(count=10):
    questions = load_questions()
    items = random.sample(questions, min(count, len(questions)))
    print("AI Architect Mock Interview")
    print("=" * 28)
    for i, item in enumerate(items, 1):
        print(f"\nQuestion {i} — {item['category']}")
        print(item["question"])
        input("\nPress Enter to reveal the model answer...")
        print("\nModel answer:")
        print(item["answer"])
        input("\nPress Enter for the next question...")
    print("\nSession complete.")


if __name__ == "__main__":
    main()
