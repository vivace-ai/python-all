class Stack(list):      # 리스트를 물려받아 만든 스택
    def push(self, item):
        self.append(item)


stack = Stack()
stack.push(1)
stack.push(2)
stack.insert(0, 99)     # 스택에 없어야 할 동작까지 딸려 왔다
print(stack)
