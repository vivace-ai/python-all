from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8023/v1", api_key="wrong-key")
messages = [{"role": "user", "content": "안녕"}]
client.chat.completions.create(model="study-model", messages=messages)
