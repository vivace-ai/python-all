def describe(name, **details):      # 키워드 인자를 딕셔너리로 받는다
    print(name, details)


describe("이서연", age=34, city="서울")

options = {"sep": " / ", "end": " <끝>\n"}
print("A", "B", "C", **options)     # 딕셔너리를 키워드 인자로 풀어 넘긴다
