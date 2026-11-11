def handle(command):
    match command:
        case {"action": "add", "subject": subject, "hours": hours}:
            return f"{subject} {hours}시간 기록"
        case {"action": "delete", "day": day}:
            return f"{day}일차 기록 삭제"
        case {"action": "summary"}:
            return "통계 출력"
        case _:
            return "알 수 없는 명령"


print(handle({"action": "add", "subject": "파이썬", "hours": 1.5}))
print(handle({"action": "delete", "day": 3}))
print(handle({"action": "export"}))
