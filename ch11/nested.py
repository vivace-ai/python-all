response = {
    "status": "ok",
    "items": [
        {"title": "파이썬 입문", "price": 18000, "tags": ["python"]},
        {"title": "데이터 분석", "price": 24000, "tags": ["pandas", "data"]},
    ],
}

print(response["status"])
print(response["items"][0]["title"])    # 리스트의 0번 항목에서 title
print(response["items"][1]["tags"][0])

for item in response["items"]:          # 항목 하나하나가 딕셔너리다
    print(f"{item['title']}: {item['price']:,}원")
