class Report:
    """합계를 내고, 문장으로 만들고, 파일에 저장까지 한다."""

    def __init__(self, hours):
        self.hours = hours

    def run(self, path):
        total = sum(self.hours)                                 # 계산
        average = total / len(self.hours)
        text = f"총 {total}시간, 하루 평균 {average:.1f}시간"   # 표현
        with open(path, "w", encoding="utf-8") as f:            # 저장
            f.write(text + "\n")
        return text
