from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


def load_settings(path):
    """'이름=값' 형식의 설정 파일을 딕셔너리로 읽는다. 없으면 기본값."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"{path.name} 파일이 없어 기본 설정을 씁니다.")
        return {"theme": "light", "language": "ko"}
    settings = {}
    for line in text.splitlines():
        name, value = line.split("=")
        settings[name] = value
    return settings


print(load_settings(DATA / "settings.txt"))
print(load_settings(DATA / "missing.txt"))
