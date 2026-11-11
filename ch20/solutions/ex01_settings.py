import json
from pathlib import Path

path = Path(__file__).parent.parent / "output" / "settings.json"
path.parent.mkdir(exist_ok=True)

settings = {
    "theme": "dark",
    "font_size": 14,
    "recent": ["notes.txt", "todo.md"],
}
with open(path, "w", encoding="utf-8") as f:
    json.dump(settings, f, ensure_ascii=False, indent=2)

with open(path, encoding="utf-8") as f:
    loaded = json.load(f)
loaded["font_size"] += 2
print(loaded["theme"], loaded["font_size"], loaded["recent"][-1])
print(loaded == settings)
