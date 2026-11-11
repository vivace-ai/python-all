rows = ["1,파이썬,1.5", "2,통계학,1.0", "3,파이썬,2.0"]

with open("records.txt", "w", encoding="utf-8") as f:
    for row in rows:
        f.write(row + "\n")     # 줄바꿈은 직접 붙인다

total = 0
with open("records.txt", encoding="utf-8") as f:
    for line in f:              # 파일에서 한 줄씩 꺼낸다
        day, subject, hours = line.strip().split(",")
        print(f"{day}일차 {subject} {hours}시간")
        total += float(hours)
print("합계:", total)
