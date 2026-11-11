"""matplotlib 그래프에서 한글이 깨지지 않도록 글꼴을 고른다."""
from matplotlib import font_manager, rcParams

# 윈도우, macOS, 리눅스에 흔히 설치되어 있는 한글 글꼴
CANDIDATES = [
    "Malgun Gothic", "AppleGothic", "NanumGothic", "Noto Sans CJK KR",
]


def use_korean_font() -> str:
    """설치된 한글 글꼴 가운데 하나를 기본 글꼴로 정하고 그 이름을 돌려준다."""
    installed = {font.name for font in font_manager.fontManager.ttflist}
    for name in CANDIDATES:
        if name in installed:
            rcParams["font.family"] = name
            rcParams["axes.unicode_minus"] = False  # 음수 부호가 깨지지 않게
            return name
    raise RuntimeError("한글 글꼴을 찾지 못했다")
