raw = "  Hello, Python!  "

print(f"[{raw}]")
print(f"[{raw.strip()}]")   # 양 끝의 공백을 없앤다
print(raw.strip().upper())  # 모두 대문자로
print(raw.strip().lower())  # 모두 소문자로
