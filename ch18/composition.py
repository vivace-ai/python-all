class Stack:
    """맨 위에서만 넣고 꺼내는 자료구조."""

    def __init__(self):
        self._items = []            # 리스트를 물려받지 않고 안에 가진다

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop(), len(stack))
print(hasattr(stack, "insert"))     # 열어 주지 않은 동작은 없다
