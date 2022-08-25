T = 10
parentheses_list = ["[", "{", "(", "<", "]", "}", ")", ">"]
parentheses_matching_dict = {"]": "[",
                             "}": "{",
                             ")": "(",
                             ">": "<",
                             "[": None,
                             "{": None,
                             "(": None,
                             "<": None}
for case in range(1, T+1):
    stack = []
    str_length = int(input())
    given_str = input()

    for i in given_str:
        if i in parentheses_list[:4]: # 왼쪽 괄호끼리 모아줌
            stack.append(i)
        elif i in parentheses_list[4:]: # 오른쪽 괄호끼리 모아줌. 닫을때만 검사.
            if len(stack) and stack[-1] == parentheses_matching_dict[i]: # 처음에 idx error 안나게 하기 위함.
                stack.pop()
            else:
                stack.append(i)
        else:
            pass
    if len(stack):
        ans = 0
    else:
        ans = 1

    print(f"#{case} {ans}")