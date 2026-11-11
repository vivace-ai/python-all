seoyeon = {"등산", "독서", "요리", "영화"}
junho = {"게임", "영화", "요리", "러닝"}

print("공통 관심사:", sorted(seoyeon & junho))
print("서연만:", sorted(seoyeon - junho))
print("모두 합쳐:", len(seoyeon | junho), "가지")
