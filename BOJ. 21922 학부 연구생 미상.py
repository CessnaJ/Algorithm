# 이거 그냥 BFS로 쭉 돌면서 visited 칠하는문제 아님? + 핀볼게임
from collections import deque
import sys
length, width = map(int, input().split())
#
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(length)]
visited = [[False]*width for _ in range(length)]

dr = [-1, 1, 0, 0] # 상 하 좌 우
dc = [0, 0, -1, 0] # 상 하 좌 우

# 물건 1 -> 상하0,1만 그대로 보내줌. 좌우2,3는 막힌다.
# 물건 2 -> 좌우2,3만 그대로 보내줌. 상하0,1은 막힌다.

# 물건 3 -> // 0<->3 , 1<->2
# 물건 4 -> // 0<->2 , 1<->3

def bfs(Q, visit):

    while Q:
        row, col, direction = Q.popleft()
        visit[row][col] = True
        if matrix[row][col] == 1:



    pass


queue = deque()
for i in range(length):
    for j in range(width):
        if matrix[i][j] == 9:
            visited[i][j] = True
            queue.append([i,j,0])
            queue.append([i, j, 1])
            queue.append([i, j, 2])
            queue.append([i, j, 3])