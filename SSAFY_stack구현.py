# stack 구현하기. stack은 list형 자료를 이용. 있어야할 기능-> push. pop. length. top

class Stack:
    def __init__(self):
        self.box = []

    def push(self, item):
        self.box.append(item)

    def pop(self):
        return self.box.pop()

    def size(self):
        return len(self.box)

    def top(self):
        return self.box[-1]



test_stack = Stack()

test_stack.push('a')
test_stack.push('b')
test_stack.push('c')

print(test_stack.pop())
print(test_stack.pop())
print(test_stack.pop())
