# # 미완성. 다시.
#
# # 문제에서 주어진 방식은 정점의 max 개수가 100개. 각 정점에서 길이 max 2개
# # input은 출발node, 목적지 node 순의 경로를
# case, routes = map(int, input().split())
# input_start_destination_list = list(map(int, input().split()))
# start_destination_list = [[]*100]
# print(start_destination_list)
# stack = []
# visited = []
# for i in range(len(input_start_destination_list)):
#     if not i%2:
#         start_destination_list[input_start_destination_list[i]].append(input_start_destination_list[i+1])
#
#
# print(start_destination_list)



# 혼자 하다가 포기. 운창님꺼 보면서 베껴보자.
# case, routes = map(int, input().split())
start_end_corr_list = [[] for _ in range(100)]
#
given_input = list(map(int, input().split()))
# stack = []
# visited = []
# for i in range(len(given_input)):
#     if not i%2:
#         start_end_corr_list[given_input[i]].append(given_input[i+1])
#
# print(start_end_corr_list)
#
# node_count = 0
# for j in start_end_corr_list:
#     if j:
#         node_count += 1
#
# print(node_count)
#
# def dfs(n):
#     if n not in visited:
#         visited.append(n)
#
#     for k in start_end_corr_list:
#         for destination in k:
#             if destination not in visited:
#                 dfs(destination)
#
# dfs(1)


def dfs(n): # n으로 가는 길이 있는지 없는지.
    if n == 99:
        board[101] = 1
    board[100].append(n)
    if len(board[n]):
        for i in board[n]:
            if i not in board[100]:
                dfs(i)

for case in range(10):
    case, N = map(int, input().split())
    routes = list(map(int, input().split()))
    board = [[] for _ in range(102)]
    for i in range(len(routes)//2):
        board[routes[2*i]].append(routes[i*2 + 1])
    board[101] = 0
    dfs(0)
    print(f'#{case} {board[101]}')