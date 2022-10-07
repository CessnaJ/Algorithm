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
    max_count = 0
    for z in range(height):
        for y in range(width):
            for x in range(length):
                if max_count < matrix[z][y][x]:
                    max_count = matrix[z][y][x]
                    continue
                if matrix[z][y][x] == 0:
                    return -1
    return max_count -1


def isvalid(newZ, newY, newX):
    if not (0 <= newX < length and 0 <= newY < width and 0 <= newZ < height):
        return False

    if visited[newZ][newY][newX]:
        return False

    if matrix[newZ][newY][newX]:
        return False

    return True

# def isvalid(newZ, newY, newX):
#     if (0 <= newX < length and 0 <= newY < width and 0 <= newZ < height) and matrix[newZ][newY][newX] == 0:
#         return True
#     else:
#         return False

# sys.stdin.readline().strip()
matrix = [[list(map(int, sys.stdin.readline().split())) for y in range(width)] for z in range(height)]
# print(matrix)
visited = [[[False]*length for yy in range(width)] for zz in range(height)]

Q = deque()
for z in range(height):
    for y in range(width):
        for x in range(length):
            if matrix[z][y][x] == 1:
                Q.append((z, y, x)) # 0은 카운트

while Q:
    z, y, x = Q.popleft()
    visited[z][y][x] = True
    # matrix[z][y][x] = matrix[z][y][x] + 1


    for dir in range(6):
        tempz = z + dz[dir]
        tempy = y + dy[dir]
        tempx = x + dx[dir]
        if 0 <= tempx < length and 0 <= tempy < width and 0 <= tempz < height:
            if not matrix[tempz][tempy][tempx]:
                Q.append((tempz, tempy, tempx))
                matrix[tempz][tempy][tempx] = matrix[z][y][x] + 1

print(tomato_check())


------------------------------------------------------개열받음.
나랑 다른점
1. 함수로 묶지 않았음 - 이건 인정 못하겠음.
2. 배열안에 count를 심어서 그걸 마지막에 max value 찾는식으로 비교. - 이건 여러목적을 한번에 달성하는 로직이니까 인정
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
    max_count = 0
    for z in range(height):
        for y in range(width):
            for x in range(length):
                if max_count < matrix[z][y][x]:
                    max_count = matrix[z][y][x]
                    continue
                if matrix[z][y][x] == 0:
                    return -1
    return max_count -1


def isvalid(newZ, newY, newX):
    if not (0 <= newX < length and 0 <= newY < width and 0 <= newZ < height):
        return False

    if visited[newZ][newY][newX]:
        return False

    if matrix[newZ][newY][newX]:
        return False

    return True


matrix = [[list(map(int, sys.stdin.readline().split())) for y in range(width)] for z in range(height)]

Q = deque()
for z in range(height):
    for y in range(width):
        for x in range(length):
            if matrix[z][y][x] == 1:
                Q.append((z, y, x)) # 0은 카운트

while Q:
    z, y, x = Q.popleft()
    visited[z][y][x] = True

    for dir in range(6):
        tempz = z + dz[dir]
        tempy = y + dy[dir]
        tempx = x + dx[dir]
        if 0 <= tempx < length and 0 <= tempy < width and 0 <= tempz < height:
            if not matrix[tempz][tempy][tempx]:
                Q.append((tempz, tempy, tempx))
                matrix[tempz][tempy][tempx] = matrix[z][y][x] + 1

print(tomato_check())