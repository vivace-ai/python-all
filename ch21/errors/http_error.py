import requests

response = requests.get("http://127.0.0.1:8021/wether", timeout=5)
response.raise_for_status()
print(response.json())
