from pathlib import Path

path = Path("data") / "2026" / "report.txt"     # /로 경로를 잇는다
print(path)
print(path.name)                                # 파일 이름
print(path.stem, path.suffix)                   # 이름과 확장자
print(path.parent)                              # 들어 있는 폴더
print(path.with_suffix(".csv"))                 # 확장자만 바꾼 새 경로
print(path.exists())                            # 실제로 있는가
