class Inventory:
    def __init__(self):
        self._stock = {}    # 상품 이름 -> 수량

    def add(self, name, count):
        self._stock[name] = self._stock.get(name, 0) + count

    def remove(self, name, count):
        if self._stock.get(name, 0) < count:
            raise ValueError(f"재고가 부족하다: {name}")
        self._stock[name] -= count

    def __len__(self):      # len(inventory): 재고가 있는 상품의 가짓수
        return len([n for n, c in self._stock.items() if c > 0])

    def __str__(self):
        return ", ".join(f"{n} {c}개" for n, c in self._stock.items())


inventory = Inventory()
inventory.add("키보드", 5)
inventory.add("마우스", 2)
inventory.remove("키보드", 3)
print(inventory)
print(len(inventory))

try:
    inventory.remove("마우스", 5)
except ValueError as e:
    print("거절:", e)
