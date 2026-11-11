"""21장 예제가 요청을 보내는 연습용 웹 API 서버.

터미널 하나에서 이 파일을 실행해 둔 채로, 다른 터미널에서 예제를 실행한다.
    uv run ch21/server.py
끝낼 때는 Ctrl+C를 누른다. 표준 라이브러리만으로 만들었다.
"""
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

PORT = 8021
API_KEY = "demo-key"

WEATHER = {
    "서울": {"temp": 12.5, "sky": "맑음"},
    "부산": {"temp": 15.0, "sky": "흐림"},
    "대구": {"temp": 13.5, "sky": "맑음"},
    "제주": {"temp": 17.0, "sky": "비"},
}
# 서버가 켜져 있는 동안만 기억한다
MEMOS: list[dict] = []
RECORDS: list[dict] = []


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status: int, data: object) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self) -> object:
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length) or b"null")

    def do_GET(self) -> None:
        url = urlparse(self.path)
        query = {key: values[0] for key, values in parse_qs(url.query).items()}

        if url.path == "/hello":
            self.send_json(200, {"message": "안녕하세요. 연습용 서버입니다."})
        elif url.path == "/weather":
            time.sleep(float(query.get("delay", 0)))    # 느린 서버를 흉내 낸다
            city = query.get("city", "")
            if city not in WEATHER:
                self.send_json(404, {"error": f"모르는 도시입니다: {city}"})
            else:
                self.send_json(200, {"city": city, **WEATHER[city]})
        elif url.path == "/private":
            if self.headers.get("Authorization") != f"Bearer {API_KEY}":
                self.send_json(401, {"error": "API 키가 없거나 틀렸습니다."})
            else:
                self.send_json(200, {"message": "인증된 요청입니다."})
        elif url.path == "/memos":
            self.send_json(200, MEMOS)
        elif url.path == "/records":
            self.send_json(200, RECORDS)
        elif url.path == "/page":
            page = "<html><body><h1>점검 중입니다</h1></body></html>"
            body = page.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_json(404, {"error": f"없는 주소입니다: {url.path}"})

    def do_POST(self) -> None:
        try:
            data = self.read_json()
        except json.JSONDecodeError:
            self.send_json(400, {"error": "본문이 JSON이 아닙니다."})
            return
        if not isinstance(data, dict):
            self.send_json(400, {"error": "본문은 JSON 객체여야 합니다."})
        elif self.path == "/memos":
            memo = {"id": len(MEMOS) + 1, "text": str(data.get("text", ""))}
            MEMOS.append(memo)
            self.send_json(201, memo)
        elif self.path == "/records":
            if not {"day", "subject", "hours"} <= data.keys():
                message = "day, subject, hours가 있어야 합니다."
                self.send_json(400, {"error": message})
            else:
                RECORDS.append(data)
                self.send_json(201, data)
        else:
            self.send_json(404, {"error": f"없는 주소입니다: {self.path}"})

    def log_message(self, format: str, *args: object) -> None:
        pass                                            # 요청 기록을 끈다


if __name__ == "__main__":
    print(f"http://127.0.0.1:{PORT} 에서 기다리는 중입니다. 끝내려면 Ctrl+C")
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\n서버를 끝냅니다.")
