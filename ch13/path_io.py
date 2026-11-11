from pathlib import Path

BASE = Path(__file__).parent
out_dir = BASE / "output"
out_dir.mkdir(exist_ok=True)    # 폴더를 만든다. 이미 있어도 괜찮다

note = out_dir / "hello.txt"
note.write_text("안녕하세요\n", encoding="utf-8")
print(note.read_text(encoding="utf-8"), end="")
print(note.stat().st_size, "바이트")
