import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from llm import ask     # noqa: E402

print(ask([{"role": "user", "content": "변수가 뭐야?"}]))
