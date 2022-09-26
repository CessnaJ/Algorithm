# def postorder():


T = 10

for case in range(1, T+1):
    nodes = int(input())
    tree = [0]*(nodes+1)
    calc = []
    for _ in range(nodes):
        input_list = input().split()
        if len(input_list) == 4:
            calc.append(input_list)
        else:
            tree[int(input_list[0])] = input_list[1]

    for i in range(len(calc)-1, -1, -1):
        operation = calc[i]
        index = int(operation[0])
        operator = operation[1]
        leftchild = tree[int(operation[2])]
        rightchild = tree[int(operation[3])]

        tree[index] = str(eval(leftchild + operator + rightchild))

    print(f'#{case} {int(float(tree[1]))}')


#
# for t in range(10):
#     N = int(input())
#     # stack = []
#     tree = [0]*(N+1)
#     info = []
#     for _ in range(N):
#         i = input().split()
#         if len(i) == 4:
#             info.append(i)
#         else:
#             tree[int(i[0])] = int(i[1])
#     # print(info)
#     for i in range(len(info)-1, -1, -1):
#         if info[i][1] == '+':
#             tree[int(info[i][0])] = tree[int(info[i][2])] + tree[int(info[i][3])]
#         if info[i][1] == '-':
#             tree[int(info[i][0])] = tree[int(info[i][2])] - tree[int(info[i][3])]
#         if info[i][1] == '*':
#             tree[int(info[i][0])] = tree[int(info[i][2])] * tree[int(info[i][3])]
#         if info[i][1] == '/':
#             tree[int(info[i][0])] = tree[int(info[i][2])] / tree[int(info[i][3])]
#     print(f'#{t+1} {int(tree[1])}')
#
#
# sa