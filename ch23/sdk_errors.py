import openai
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8023/v1", api_key="wrong-key")
messages = [{"role": "user", "content": "안녕"}]

try:
    client.chat.completions.create(model="study-model", messages=messages)
except openai.AuthenticationError as e:
    print("인증 실패:", e)
except openai.RateLimitError:
    print("요청이 너무 많습니다. 잠시 뒤에 다시 시도합니다.")
except openai.APIConnectionError:
    print("서버에 닿지 못했습니다.")
