"""23장과 25장 예제가 요청을 보내는 연습용 LLM 서버.

실제 서비스와 같은 형식(Chat Completions)으로 요청을 받고 응답한다.
진짜 모델이 아니라, 이 장의 예제에 나오는 질문에 정해진 규칙으로 답을 흉내 낸다.
    uv run ch25/llm_server.py
끝낼 때는 Ctrl+C를 누른다.
"""
import json
import re
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8023
SUBJECTS = ["파이썬", "통계학", "글쓰기", "영어"]
HOURS = {"한 시간 반": 1.5, "두 시간": 2.0, "한 시간": 1.0, "30분": 0.5}
busy_calls = 0                          # busy-model이 불린 횟수


def find_name(messages: list[dict]) -> str | None:
    """앞선 대화에서 사용자가 밝힌 이름을 찾는다."""
    for message in messages:
        m = re.search(r"내 이름은 (\S+?)(?:이야|야|입니다)", message["content"])
        if message["role"] == "user" and m:
            return m.group(1)
    return None


def extract(text: str) -> dict:
    """문장에서 과목과 시간을 뽑는다. 시간을 알 수 없으면 원문 표현을 그대로 둔다."""
    subject = next((s for s in SUBJECTS if s in text), "모름")
    hours: float | str = "조금" if "조금" in text else 0
    for phrase, value in HOURS.items():
        if phrase in text:
            hours = value
            break
    return {"subject": subject, "hours": hours}


def coach(text: str) -> str:
    """요약에 적힌 과목별 시간을 읽어 조언을 만든다."""
    pairs = [(s, float(h)) for s, h in re.findall(r"(\S+) ([\d.]+)시간", text)]
    if not pairs:
        return "기록이 없어 드릴 조언이 없습니다. 오늘 30분부터 시작해 보세요."
    most = max(pairs, key=lambda pair: pair[1])
    least = min(pairs, key=lambda pair: pair[1])
    total = sum(hours for _, hours in pairs)
    return (
        f"모두 {total:.1f}시간을 공부하셨습니다. "
        f"{most[0]}에 가장 많은 시간을 쓰셨고 {least[0]}가 가장 적습니다. "
        f"다음 주에는 {least[0]}에 30분씩 두 번만 더 배정해 보세요."
    )


def reply(messages: list[dict], json_mode: bool) -> str:
    """마지막 사용자 메시지에 대한 답을 만든다."""
    system = " ".join(m["content"] for m in messages if m["role"] == "system")
    question = messages[-1]["content"]

    if "JSON" in system + question:
        answer = json.dumps(extract(question), ensure_ascii=False)
        if json_mode:
            return answer
        return f"요청하신 결과입니다.\n```json\n{answer}\n```"
    if "학습 코치" in system:
        return coach(question)
    if "내 이름이" in question:
        name = find_name(messages[:-1])
        if name:
            return f"{name} 님이라고 하셨습니다."
        return "이름을 들은 적이 없습니다. 저는 앞선 대화를 기억하지 못합니다."
    if "내 이름은" in question:
        return f"반갑습니다, {find_name(messages)} 님. 무엇을 도와드릴까요?"
    if "변수" in question:
        if "초등학생" in system:
            return (
                "변수는 이름표를 붙인 상자예요. "
                "상자에 값을 넣어 두고 이름을 불러 꺼내 써요."
            )
        return "변수는 값을 저장해 두고 이름으로 다시 참조하기 위한 식별자입니다."
    if "파이썬" in question:
        return (
            "파이썬은 읽기 쉬운 문법으로 누구나 빠르게 배워 "
            "폭넓게 쓰는 프로그래밍 언어입니다."
        )
    return "연습용 서버는 이 장의 예제에 나오는 질문에만 답합니다."


def count_tokens(text: str) -> int:
    """토큰 수를 어림한다. 실제 모델은 전용 도구로 정확히 센다."""
    return max(1, len(text) * 2 // 3)


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status: int, data: object) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_error_json(self, status: int, kind: str, message: str) -> None:
        self.send_json(status, {"error": {"type": kind, "message": message}})

    def do_POST(self) -> None:
        global busy_calls
        if self.path != "/v1/chat/completions":
            message = f"없는 주소입니다: {self.path}"
            self.send_error_json(404, "not_found", message)
            return
        key = self.headers.get("Authorization", "")
        if not key.startswith("Bearer demo-"):
            message = "API 키가 없거나 틀렸습니다."
            self.send_error_json(401, "authentication_error", message)
            return
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        messages = body.get("messages", [])
        model = body.get("model", "")
        if not model or not messages:
            message = "model과 messages가 있어야 합니다."
            self.send_error_json(400, "invalid_request_error", message)
            return
        if model == "busy-model":
            busy_calls += 1
            if busy_calls % 3 != 0:     # 세 번에 두 번은 거절한다
                message = "요청이 너무 많습니다. 잠시 뒤에 다시 시도하세요."
                self.send_error_json(429, "rate_limit_error", message)
                return

        json_mode = body.get("response_format", {}).get("type") == "json_object"
        answer = reply(messages, json_mode)
        prompt_tokens = sum(count_tokens(m["content"]) + 4 for m in messages)
        usage = {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": count_tokens(answer),
            "total_tokens": prompt_tokens + count_tokens(answer),
        }
        base = {"id": "chatcmpl-demo", "created": int(time.time()), "model": model}

        if body.get("stream"):
            self.stream(base, answer)
            return
        choice = {
            "index": 0,
            "message": {"role": "assistant", "content": answer},
            "finish_reason": "stop",
        }
        data = {**base, "object": "chat.completion", "choices": [choice]}
        self.send_json(200, {**data, "usage": usage})

    def stream(self, base: dict, answer: str) -> None:
        """답을 낱말 단위로 잘라 조금씩 보낸다."""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.end_headers()
        pieces = re.findall(r"\S+\s*", answer)
        for index, piece in enumerate(pieces):
            last = index == len(pieces) - 1
            choice = {
                "index": 0,
                "delta": {"content": piece},
                "finish_reason": "stop" if last else None,
            }
            chunk = {**base, "object": "chat.completion.chunk", "choices": [choice]}
            line = f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n"
            self.wfile.write(line.encode("utf-8"))
            self.wfile.flush()
            time.sleep(0.05)
        self.wfile.write(b"data: [DONE]\n\n")

    def log_message(self, format: str, *args: object) -> None:
        pass                            # 요청 기록을 끈다


if __name__ == "__main__":
    print(f"http://127.0.0.1:{PORT}/v1 에서 기다리는 중입니다. 끝내려면 Ctrl+C")
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\n서버를 끝냅니다.")
