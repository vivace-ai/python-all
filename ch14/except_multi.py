def per_day(total_text, days_text):
    """총 학습 시간을 일수로 나눈 하루 평균을 돌려준다."""
    try:
        return float(total_text) / int(days_text)
    except ValueError:
        print("숫자가 아닌 값이 있습니다.")
    except ZeroDivisionError:
        print("일수는 0일 수 없습니다.")
    return None


print(per_day("10.5", "7"))
print(per_day("10.5", "0"))
print(per_day("열 시간", "7"))
