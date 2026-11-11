from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: int
    tags: list[str] = field(default_factory=list)

    def discounted(self, rate):
        return round(self.price * (1 - rate))


a = Product("키보드", 89000)
b = Product("키보드", 89000)

print(a)        # __repr__이 만들어져 있다
print(a == b)   # __eq__도 만들어져 있다
a.tags.append("신상품")
print(a.tags, b.tags)
print(a.discounted(0.2))
