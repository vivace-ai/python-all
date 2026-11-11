def average_hours(records: list[dict]) -> float:
    return sum(r["hours"] for r in records) / len(records)


weeks = {"1주": [{"hours": 1.5}, {"hours": 2.0}], "2주": []}
for week, records in weeks.items():
    print(week, average_hours(records))
