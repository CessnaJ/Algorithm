# T = int(input())
# for case in range(1, T+1):
#     N, Q = map(int, input().split())
#
#     line_list = [0] * N
#     for i in range(1, Q+1):
#         L, R = map(int, input().split())
#         line_list[L-1: R] = i
#
#     print(f'#{case}'*line_list)
# 새롭게 알게된 것. list slicing을 위에 input 받은 가변 variable을 통해서는 할 수 없다.


T = int(input())
for case in range(1, T+1):
    N, Q = map(int, input().split())

    line_list = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            line_list[j] = i

    print(f'#{case}', *line_list)