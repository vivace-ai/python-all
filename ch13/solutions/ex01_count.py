from pathlib import Path

path = Path(__file__).parent.parent / "data" / "notes.txt"
text = path.read_text(encoding="utf-8")

print("줄 수:", len(text.splitlines()))
print("낱말 수:", len(text.split()))
print("글자 수:", len(text))
