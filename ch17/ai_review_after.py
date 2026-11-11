class Cart:
    def __init__(self):
        self.items = []     # 객체가 만들어질 때마다 새 리스트

    def add(self, name):
        self.items.append(name)


mine = Cart()
yours = Cart()
mine.add("키보드")
yours.add("마우스")

print("내 장바구니:", mine.items)
print("네 장바구니:", yours.items)
