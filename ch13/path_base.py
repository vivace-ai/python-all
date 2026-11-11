from pathlib import Path

print(Path.cwd().name)                      # 명령을 실행한 폴더
BASE = Path(__file__).parent                # 이 코드 파일이 들어 있는 폴더
print(BASE.name)

print(Path("data/notes.txt").exists())      # 실행한 폴더 기준
print((BASE / "data/notes.txt").exists())   # 코드 파일 기준
