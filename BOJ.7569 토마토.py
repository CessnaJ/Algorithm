# 델타탐색
# 확장성, 재사용성에 대한 고민
# 3차원이상의 배열이면 접근할때 고차원 -> 저차원으로 간다는것.

import sys
from collections import deque
length, width, height = map(int, input().split()) # 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100
# 1 - 익은 토마토
# 0 - 안익은 토마토
# -1 - 빈칸 (진출불가)

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]

def tomato_check():
    global count
    for z in range(height):
        for y in range(width):
            for x in range(length):
                if matrix[z][y][x] == 0:
                    count = -1
                    return


def isvalid(newZ, newY, newX):
    if not (0 <= newX < length and 0 <= newY < width and 0 <= newZ < height):
        return False

    if visited[newZ][newY][newX]:
        return False

    if matrix[newZ][newY][newX] in [-1, 1]:
        return False
    return True

# sys.stdin.readline().strip()
matrix = [[list(map(int, sys.stdin.readline().split())) for y in range(width)] for z in range(height)]
# print(matrix)
visited = [[[False]*length for yy in range(width)] for zz in range(height)]

Q = deque()
for z in range(height):
    for y in range(width):
        for x in range(length):
            if matrix[z][y][x] == 1:
                Q.append((z, y, x, 0)) # 0은 카운트

while Q:
    # current = Q.popleft()
    # # print(current)
    # z = current[0]
    # y = current[1]
    # x = current[2]
    # count = current[3]
    z, y, x, count = Q.popleft()
    matrix[z][y][x] = 1
    visited[z][y][x] = True

    for dir in range(6):
        tempz = z + dz[dir]
        tempy = y + dy[dir]
        tempx = x + dx[dir]
        if isvalid(tempz, tempy, tempx):
            Q.append((tempz, tempy, tempx, count+1))

tomato_check()
print(count)



