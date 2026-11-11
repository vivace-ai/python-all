import re

text = "주문 A-1024, 수량 3개, 합계 45,000원 (2026-11-02)"

print(re.findall(r"\d+", text))                 # 숫자가 이어진 덩어리
print(re.findall(r"[A-Z]-\d+", text))           # 대문자, 하이픈, 숫자들
print(re.findall(r"[가-힣]+", text))            # 한글이 이어진 덩어리
print(re.findall(r"\d{4}-\d{2}-\d{2}", text))   # 날짜 모양
print(re.findall(r"[\d,]+원", text))            # 숫자와 쉼표 뒤에 '원'
