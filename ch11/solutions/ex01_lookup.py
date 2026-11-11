capitals = {"한국": "서울", "일본": "도쿄", "프랑스": "파리"}

country = input("나라: ").strip()
print(capitals.get(country, "등록되지 않은 나라입니다."))
