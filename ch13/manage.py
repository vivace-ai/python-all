from pathlib import Path

out_dir = Path(__file__).parent / "output"
out_dir.mkdir(exist_ok=True)

draft = out_dir / "draft.txt"
draft.write_text("초안\n", encoding="utf-8")

final = draft.rename(out_dir / "final.txt")     # 이름을 바꾼다
print(final.name, final.exists(), draft.exists())

final.unlink()                                  # 파일을 지운다
print(final.exists())
