# stack을 이용하면 쉽다. 문제 자체가 stack을 써보라고 요구하고 있음.
# 연습용으로 숙련도를 위해서 stack을 class로 만들어서 진행하겠음.

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

T = int(input())

for case in range(1, T+1):
    given_str = input()
    test_stack = Stack()
    for i in given_str:
        if not test_stack.size():
            test_stack.push(i)
        else:
            if test_stack.top() == i:
                test_stack.pop()
            else:
                test_stack.push(i)
    print(f'#{case} {test_stack.size()}')