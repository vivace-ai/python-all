amounts = ["12000", "8500", "1,200", "3000원", "4500", "미정"]

total = 0
failed = []
for text in amounts:
    cleaned = text.replace(",", "").removesuffix("원")
    try:
        total += int(cleaned)
    except ValueError:          # 예상한 예외만 잡는다
        failed.append(text)     # 버리지 않고 모아 둔다

print("합계:", total)
if failed:
    print(f"변환하지 못한 값 {len(failed)}건: {failed}")
