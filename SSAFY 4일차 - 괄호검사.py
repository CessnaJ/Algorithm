T = int(input())
parentheses_list = ['[', '{', '(',  ']', '}', ')']
parentheses_matching_dict = {']': '[',
                             '}': '{',
                             ')': '('}
for case in range(1, T+1):
    stack = []
    given_str = input()

    for i in given_str:
        if i in parentheses_list[:3]: # 왼쪽 괄호끼리 모아줌
            stack.append(i)
        elif i in parentheses_list[3:]: # 오른쪽 괄호끼리 모아줌. 닫을때만 검사.
            if len(stack) and stack[-1] == parentheses_matching_dict[i]: # 처음에 idx error 안나게 하기 위함.
                stack.pop()
            else:
                stack.append(i)
        else:
            pass
    if not len(stack):
        ans = 1
    else:
        ans = 0

    print(f'#{case} {ans}')
