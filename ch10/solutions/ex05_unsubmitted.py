students = {"서연", "준호", "민지", "도윤", "하은"}
submitted = ["민지", "서연", "민지", "하은"]    # 두 번 낸 사람이 있다

missing = students - set(submitted)
print(f"제출 {len(set(submitted))}명, 미제출 {len(missing)}명")
print("미제출:", sorted(missing))
