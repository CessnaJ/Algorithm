# T = int(input())
#
# for case in range(1, T+1):
#     cols = int(input())
#     up = 0
#     down = 1
#     matrix = [[0]*2 + list(map(int, input().split())) for _ in range(2)]
#     # stickers = [[0]*2 + list(map(int, input().split())) for _ in range(2)]
#
#     for col in range(2, cols+2):
#         up_case1 = matrix[down][col-1] + matrix[up][col]
#         up_case2 = matrix[down][col-2] + matrix[up][col]
#
#         down_case1 = matrix[up][col-1] + matrix[down][col]
#         down_case2 = matrix[up][col-2] + matrix[down][col]
#
#         matrix[up][col] = max(up_case1, up_case2)
#         matrix[down][col] = max(down_case1, down_case2)
#     print(max(matrix[up][cols+1], matrix[down][cols+1]))
#
#     # matrix[up][col - 2]

# dp문제
# up, down으로 케이스 분류

#up의 경우
# ㅇ  ㅇ
# 	ㅇ
# 이렇게 가거나,
#   X ㅇ
# ㅇ
# 이렇게 갈거고,
#
# #down의 경우
#   ㅇ
# ㅇ  ㅇ
# 이렇게 가거나
# ㅇ
#   X ㅇ 이렇게 갈 것.
# 다만 지그재그로 가는경우, 그 앞 순번 지그재그에서 값을 이미 저장을 해두기 때문에 대각선만 더해주면 그 앞까지 지그재그 누적합을 더하게 된다.



T = int(input())

for case in range(1, T+1):
    cols = int(input())
    up_matrix = [0]*2 + list(map(int, input().split()))
    down_matrix = [0]*2 + list(map(int, input().split()))

    for col in range(2, cols+2):
        up_case1 = down_matrix[col-1] + up_matrix[col]
        up_case2 = down_matrix[col-2] + up_matrix[col]

        down_case1 = up_matrix[col-1] + down_matrix[col]
        down_case2 = up_matrix[col-2] + down_matrix[col]

        up_matrix[col] = max(up_case1, up_case2)
        down_matrix[col] = max(down_case1, down_case2)
    print(max(up_matrix[cols+1], down_matrix[cols+1]))

    # matrix[up][col - 2]