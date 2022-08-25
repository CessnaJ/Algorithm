T= int(input())
stacks = []

for case in range(1, T+1):
    stack = []
    given_parentheses = input()

    for i in given_parentheses:
        if not len(stack):
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)

    if len(stack):
        print(f'#{case} -1')
    else:
        print(f'#{case} 1')

