# AI가 내놓은 코드: 장바구니 클래스
class Cart:
    items = []

    def add(self, name):
        self.items.append(name)


mine = Cart()
yours = Cart()
mine.add("키보드")
yours.add("마우스")

print("내 장바구니:", mine.items)
print("네 장바구니:", yours.items)
