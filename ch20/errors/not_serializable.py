import json
from datetime import date

task = {"title": "보고서 제출", "due": date(2026, 11, 30)}
print(json.dumps(task, ensure_ascii=False))
