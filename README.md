# 파이썬 완전 정복 (개정판) 예제 코드

『파이썬 완전 정복』 개정판(김영희 지음, 부크크)에 실린 코드입니다.
책의 실행 결과는 모두 이 저장소의 코드를 실제로 실행해 얻은 것입니다.

## 준비

파이썬과 라이브러리는 [uv](https://docs.astral.sh/uv/)로 관리합니다. 설치 방법은 책 1장에 있습니다.

```
git clone https://github.com/vivace-ai/python-all.git
cd python-all
uv sync
uv run ch01/hello.py
```

uv를 쓸 수 없는 환경에서는 가상환경을 만든 뒤 `pip install -r requirements.txt`로 설치하고,
`uv run` 대신 `python`으로 실행합니다(부록 C).

## 폴더

| 폴더 | 내용 |
|---|---|
| `ch01` ~ `ch26` | 장별 예제. 책의 코드 상자 오른쪽 위에 적힌 경로와 같습니다 |
| `chNN/solutions` | 연습문제 풀이 |
| `chNN/errors` | 일부러 오류를 낸 코드('오류 메시지 읽기' 절) |
| `chNN/study_log` | 5장부터 키워 가는 학습 기록 프로그램의 그 장 단계 |
| `appendix` | 부록 예제 |

## 서버가 필요한 장

- 21장: `uv run ch21/server.py`를 다른 터미널에서 켜 둡니다.
- 23장: `uv run ch23/llm_server.py`를 켜 둡니다. 실제 언어 모델이 아니라 요청과 응답의 형식만 같은 연습용 서버입니다.
- 25장: `uv run uvicorn app:app --app-dir ch25 --port 8025`와 `uv run ch25/llm_server.py`를 켜 둡니다.

실제 언어 모델 서비스에 연결하려면 환경 변수 `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL`을 정합니다(23장).

## 실행 환경

파이썬 3.14, 라이브러리 버전은 `uv.lock`에 고정되어 있습니다.
