import requests

URL = "http://127.0.0.1:8023/v1/chat/completions"

payload = {
    "model": "study-model",
    "messages": [
        {"role": "user", "content": "파이썬을 한 문장으로 소개해 줘."},
    ],
}
headers = {"Authorization": "Bearer demo-key"}

response = requests.post(URL, json=payload, headers=headers, timeout=30)
response.raise_for_status()
data = response.json()

print(data["choices"][0]["message"]["content"])     # 모델의 답
print(data["usage"])                                # 쓴 토큰의 수
