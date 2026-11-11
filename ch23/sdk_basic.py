from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8023/v1", api_key="demo-key")
question = [{"role": "user", "content": "파이썬을 한 문장으로 소개해 줘."}]

response = client.chat.completions.create(
    model="study-model", messages=question
)
print(response.choices[0].message.content)
print(response.usage.prompt_tokens, response.usage.completion_tokens)
