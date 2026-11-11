tags = {"python", "ai", "python", "data"}   # 중괄호로 묶는다

print(len(tags))                            # 중복은 하나로 친다
print("ai" in tags)

tags.add("web")                             # 항목을 넣는다
tags.discard("data")                        # 뺀다. 없어도 오류가 없다
print(sorted(tags))                         # 정렬해서 출력한다
