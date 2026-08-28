import json
from collections import Counter
from pathlib import Path

questions = json.loads(Path(__file__).with_name("questions.json").read_text(encoding="utf-8"))
for topic, count in sorted(Counter(x["category"] for x in questions).items()):
    print(f"{topic}: {count}")
print(f"\nTotal questions: {len(questions)}")
