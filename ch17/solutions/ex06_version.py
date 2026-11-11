class Version:
    def __init__(self, text):
        self.parts = tuple(int(n) for n in text.split("."))

    def __str__(self):
        return ".".join(str(n) for n in self.parts)

    def __repr__(self):
        return f"Version('{self}')"

    def __eq__(self, other):
        return self.parts == other.parts

    def __lt__(self, other):
        return self.parts < other.parts     # 튜플은 앞자리부터 차례로 견준다


versions = [Version("1.10.0"), Version("1.2.9"), Version("1.2.10")]
print(sorted(versions))
print(Version("1.2.10") > Version("1.2.9"))

# 문자열로 정렬하면 틀린다
print(sorted(["1.10.0", "1.2.9", "1.2.10"]))
