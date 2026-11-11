"""이 장의 예제가 함께 쓰는 LLM 클라이언트.

기본값은 연습용 서버다. 실제 서비스를 쓰려면 환경 변수 세 개를 바꾼다.
"""
import os

from openai import OpenAI

BASE_URL = os.environ.get("LLM_BASE_URL", "http://127.0.0.1:8023/v1")
API_KEY = os.environ.get("LLM_API_KEY", "demo-key")
MODEL = os.environ.get("LLM_MODEL", "study-model")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def ask(messages: list[dict], **options) -> str:
    """메시지 목록을 보내고 모델의 답을 문자열로 돌려준다."""
    response = client.chat.completions.create(
        model=MODEL, messages=messages, **options
    )
    return response.choices[0].message.content or ""
